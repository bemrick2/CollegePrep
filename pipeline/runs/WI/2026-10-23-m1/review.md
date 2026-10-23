# Review queue — WI (2026-27)

Pages fetched: 208; failures: 16. Candidates: 29 (8 without issues, 21 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 5 | 0 | 1 | 1 | 1 | 0 | 50 |
| cost_of_attendance | 1 | 0 | 0 | 1 | 2 | 0 | 54 |
| admissions_tests | 0 | 0 | 0 | 0 | 3 | 0 | 55 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 3 | 55 |
| merit_scholarships | 0 | 2 | 0 | 0 | 3 | 0 | 53 |
| ap_credit | 1 | 3 | 0 | 0 | 2 | 1 | 51 |
| clep_credit | 1 | 1 | 0 | 0 | 1 | 2 | 53 |
| ib_credit | 0 | 1 | 0 | 0 | 1 | 2 | 54 |
| dual_enrollment | 0 | 5 | 0 | 0 | 1 | 2 | 50 |
| transfer_credit | 1 | 6 | 0 | 0 | 3 | 0 | 48 |
| statewide_articulation | 0 | 0 | 0 | 0 | 1 | 2 | 55 |
| residency | 0 | 0 | 0 | 0 | 3 | 0 | 55 |
| degree_requirements | 3 | 0 | 0 | 0 | 0 | 1 | 54 |
| aid_appeals | 0 | 0 | 0 | 1 | 2 | 0 | 55 |

## Ready for review (8)

### `0716144e78bc6a1d` University of Wisconsin-Madison — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://bursar.wisc.edu/tuition-and-fees/fall-2026-increase (sha256 60de270f1634)
- checks: {"columns": 1, "rows": 5}
  - on_campus:Current Tuition Rate: 10506.48 ⟵ “Current Tuition Rate | $10,506.48 | $42,530.88”
  - on_campus:Amount of Tuition Rate Increase: 210.13 ⟵ “Amount of Tuition Rate Increase | $210.13 | $1,701.24”
  - on_campus:Current Segregated Fee Rate: 1659.97 ⟵ “Current Segregated Fee Rate | $1,659.97 | $1,659.97”
  - on_campus:Amount of Segregated Fee Rate Increase: 39.51 ⟵ “Amount of Segregated Fee Rate Increase | $39.51 | $39.51”
  - on_campus:New Total Tuition & Segregated Fee Rate for the 26-27 Academic Year: 12416.09 ⟵ “New Total Tuition & Segregated Fee Rate for the 26-27 Academic Year | $12,416.09 | $45,931.60”
### `5e53d2efc29a146b` University of Wisconsin-Madison — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://bursar.wisc.edu/tuition-and-fees/fall-2026-increase (sha256 60de270f1634)
- checks: {"columns": 1, "rows": 5}
  - on_campus:Current Tuition Rate: 42530.88 ⟵ “Current Tuition Rate | $10,506.48 | $42,530.88”
  - on_campus:Amount of Tuition Rate Increase: 1701.24 ⟵ “Amount of Tuition Rate Increase | $210.13 | $1,701.24”
  - on_campus:Current Segregated Fee Rate: 1659.97 ⟵ “Current Segregated Fee Rate | $1,659.97 | $1,659.97”
  - on_campus:Amount of Segregated Fee Rate Increase: 39.51 ⟵ “Amount of Segregated Fee Rate Increase | $39.51 | $39.51”
  - on_campus:New Total Tuition & Segregated Fee Rate for the 26-27 Academic Year: 45931.6 ⟵ “New Total Tuition & Segregated Fee Rate for the 26-27 Academic Year | $12,416.09 | $45,931.60”
### `bc8289a75cd4e830` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=engineering-bs [same] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 e9764d3fa741)
- checks: {"courses": 6, "groups": 5, "groups_skipped": 0}
  - program_name: Engineering, BS ⟵ “Engineering, BS | UW-Milwaukee Academic Catalog”
### `390c480340fe3ea0` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=engineering-bs · requirement_key=engineering-major-requirements-engineering-requirement-46-credits [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 e9764d3fa741)
  - courses: EAS 200 ⟵ “EAS 200 - Professional Seminar”
### `5aaee7af08806c41` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=engineering-bs · requirement_key=engineering-major-requirements-natural-science-6-credits [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 e9764d3fa741)
  - section: engineering-major-requirements-natural-science-6-credits ⟵ “Engineering Major Requirements — Natural Science - 6 credits”
### `62cc31236af07267` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=engineering-bs · requirement_key=engineering-major-requirements-mathematics-14-credits [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 e9764d3fa741)
  - courses: MATH 231 ⟵ “MATH 231 - Calculus and Analytic Geometry I”
  - courses: MATH 232 ⟵ “MATH 232 - Calculus and Analytic Geometry II”
### `c74bc57228c4bdcc` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=engineering-bs · requirement_key=engineering-major-requirements-bio-sci-203 [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 e9764d3fa741)
  - courses: CHEM 102 ⟵ “CHEM 102 - General Chemistry”
  - courses: CHEM 104 ⟵ “CHEM 104 - General Chemistry and Qualitative Analysis”
  - courses: CHEM 105 ⟵ “CHEM 105 - General Chemistry for Engineering”
### `f544ca7eccf366b9` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=engineering-bs · requirement_key=engineering-major-requirements-engineering-technical-electives-30-credits [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 e9764d3fa741)
  - section: engineering-major-requirements-engineering-technical-electives-30-credits ⟵ “Engineering Major Requirements — Engineering Technical Electives - 30 credits”

## Exceptions (21)

### `af5762d7dee88709` Madison Area Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://madisoncollege.edu/paying-for-college/tuition (sha256 e10dd0fdcefc)
- issues: residency_unknown
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition: 6584 ⟵ “Tuition | $6,584 | $4,938 | $3,292 | $1,646”
  - off_campus_not_with_family:Books: 1000 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3072 ⟵ “Personal | $3,072 | $3,072 | $3,072 | $0”
  - off_campus_not_with_family:Food and Housing: 13760 ⟵ “Food and Housing | $13,760 | $13,760 | $13,760 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 3040 ⟵ “Transportation | $3,040 | $3,040 | $3,040 | $3,040”
  - off_campus_not_with_family:Total: 27540 ⟵ “Total | $27,540 | $25,644 | $23,748 | $4,936”
  - off_campus_not_with_family:Tuition: 4938 ⟵ “Tuition | $6,584 | $4,938 | $3,292 | $1,646”
  - off_campus_not_with_family:Books: 750 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3072 ⟵ “Personal | $3,072 | $3,072 | $3,072 | $0”
  - off_campus_not_with_family:Food and Housing: 13760 ⟵ “Food and Housing | $13,760 | $13,760 | $13,760 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 3040 ⟵ “Transportation | $3,040 | $3,040 | $3,040 | $3,040”
  - off_campus_not_with_family:Total: 25644 ⟵ “Total | $27,540 | $25,644 | $23,748 | $4,936”
  - off_campus_not_with_family:Tuition: 3292 ⟵ “Tuition | $6,584 | $4,938 | $3,292 | $1,646”
  - off_campus_not_with_family:Books: 500 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3072 ⟵ “Personal | $3,072 | $3,072 | $3,072 | $0”
  - off_campus_not_with_family:Food and Housing: 13760 ⟵ “Food and Housing | $13,760 | $13,760 | $13,760 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 3040 ⟵ “Transportation | $3,040 | $3,040 | $3,040 | $3,040”
  - off_campus_not_with_family:Total: 23748 ⟵ “Total | $27,540 | $25,644 | $23,748 | $4,936”
  - off_campus_not_with_family:Tuition: 1646 ⟵ “Tuition | $6,584 | $4,938 | $3,292 | $1,646”
  - off_campus_not_with_family:Books: 250 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 0 ⟵ “Personal | $3,072 | $3,072 | $3,072 | $0”
  - off_campus_not_with_family:Food and Housing: 0 ⟵ “Food and Housing | $13,760 | $13,760 | $13,760 | $0”
  - … 3 more rows
### `c3f6a8b49be6dc7c` Madison Area Technical College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://madisoncollege.edu/paying-for-college/tuition (sha256 e10dd0fdcefc)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition: 6224 ⟵ “Tuition | $6,224 | $4,668 | $3,112 | $1,556”
  - off_campus_not_with_family:Books: 1000 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3040 ⟵ “Personal | $3,040 | $3,040 | $3,040 | $0”
  - off_campus_not_with_family:Food and Housing: 13824 ⟵ “Food and Housing | $13,824 | $13,824 | $13,824 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | $2,400”
  - off_campus_not_with_family:Total: 26572 ⟵ “Total | $26,572 | $24,766 | $22,960 | $4,206”
  - off_campus_not_with_family:Tuition: 4668 ⟵ “Tuition | $6,224 | $4,668 | $3,112 | $1,556”
  - off_campus_not_with_family:Books: 750 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3040 ⟵ “Personal | $3,040 | $3,040 | $3,040 | $0”
  - off_campus_not_with_family:Food and Housing: 13824 ⟵ “Food and Housing | $13,824 | $13,824 | $13,824 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | $2,400”
  - off_campus_not_with_family:Total: 24766 ⟵ “Total | $26,572 | $24,766 | $22,960 | $4,206”
  - off_campus_not_with_family:Tuition: 3112 ⟵ “Tuition | $6,224 | $4,668 | $3,112 | $1,556”
  - off_campus_not_with_family:Books: 500 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3040 ⟵ “Personal | $3,040 | $3,040 | $3,040 | $0”
  - off_campus_not_with_family:Food and Housing: 13824 ⟵ “Food and Housing | $13,824 | $13,824 | $13,824 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | $2,400”
  - off_campus_not_with_family:Total: 22960 ⟵ “Total | $26,572 | $24,766 | $22,960 | $4,206”
  - off_campus_not_with_family:Tuition: 1556 ⟵ “Tuition | $6,224 | $4,668 | $3,112 | $1,556”
  - off_campus_not_with_family:Books: 250 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 0 ⟵ “Personal | $3,040 | $3,040 | $3,040 | $0”
  - off_campus_not_with_family:Food and Housing: 0 ⟵ “Food and Housing | $13,824 | $13,824 | $13,824 | $0”
  - … 3 more rows
### `42b885a547393663` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=actuarial-science-ba [same] (labeled_in_source)
- source: https://catalog.uwm.edu/letters-science/mathematical-sciences/actuarial-science-ba/ (sha256 e63d6f0a1435)
- issues: requirement_groups_skipped
- checks: {"courses": 5, "groups": 2, "groups_skipped": 4}
  - program_name: Actuarial Science, BA ⟵ “Actuarial Science, BA | UW-Milwaukee Academic Catalog”
### `55a68aea8a15bde4` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=theatre-practices-ba-theatre-education [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-education-ba/ (sha256 025d5a7f7355)
- issues: requirement_groups_skipped
- checks: {"courses": 0, "groups": 2, "groups_skipped": 1}
  - program_name: Theatre Practices, BA: Theatre Education ⟵ “Theatre Practices, BA: Theatre Education | UW-Milwaukee Academic Catalog”
### `5702e6646814c033` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=music-bfa-versatile-voice [same] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 70bd524e0872)
- issues: requirement_groups_skipped
- checks: {"courses": 41, "groups": 7, "groups_skipped": 4}
  - program_name: Music, BFA: Versatile Voice ⟵ “Music, BFA: Versatile Voice | UW-Milwaukee Academic Catalog”
### `e39596c2fc123ace` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=theatre-practices-ba [same] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-ba/ (sha256 bba7df228cf1)
- issues: requirement_groups_skipped
- checks: {"courses": 0, "groups": 1, "groups_skipped": 3}
  - program_name: Theatre Practices, BA ⟵ “Theatre Practices, BA | UW-Milwaukee Academic Catalog”
### `31c4d009d64d4836` University of Wisconsin-Milwaukee — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://uwm.edu/finances/finances/receiving-financial-aid/satisfactory-academic-progress-sap/ (sha256 0eeb7acdeb9e)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Review: If you believe your FAFSA does not adequately reflect your current financial situation.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances If you or your family have faced financial challenges that weren’t captured on your FAFSA form, you can schedule an appointment to talk with a Student Financial Service Center advisor.”
### `5f9b232aaabd805e` University of Wisconsin-Milwaukee — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://uwm.edu/finances/finances/receiving-financial-aid/satisfactory-academic-progress-sap/ (sha256 0eeb7acdeb9e)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal: If you’ve been notified you no longer meet financial aid’s Satisfactory Academic Progress requirements.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Form is provided to the student after meeting with an Advisor in the Student Financial Service Center.”
  - sentence: sap_appeal ⟵ “While Advisors may request assistance from the Financial Aid SAP Appeals Committee for any appeal, students who submit more than two appeals must have their appeal reviewed by a committee.”
  - sentence: sap_appeal ⟵ “Whether or not an academic plan is needed will be determined when the student meets with an Advisor in the Student Financial Service Center to discuss whether they are eligible to complete a SAP appeal.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Form is provided to the student after meeting with an Advisor in the Student Financial Service Center.”
  - sentence: sap_appeal ⟵ “While Advisors may request assistance from the Financial Aid SAP Appeals Committee for any appeal, students who submit more than two appeals must have their appeal reviewed by the committee.”
### `fe6dc136f3b50900` University of Wisconsin-Milwaukee — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://uwm.edu/finances/finances/receiving-financial-aid/satisfactory-academic-progress-sap/ (sha256 0eeb7acdeb9e)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: budget_increase ⟵ “Budget Adjustment Request: If you believe your Cost of Attendance does not adequately reflect your educational expenses.”
  - sentence: budget_increase ⟵ “Budget Adjustment You may qualify for an adjustment to your Cost of Attendance (COA).”
  - sentence: budget_increase ⟵ “This is called a Budget Adjustment and is available for the documented rental or purchase of a personal computer, the costs expected to be incurred for dependent care, and when documented expenses are significantly different than those used in our estimates.”
  - sentence: budget_increase ⟵ “A Budget Adjustment may or may not increase the amount of financial aid offered.”
  - sentence: budget_increase ⟵ “If Joe needs extra financial aid, Joe could borrow a maximum of $13,588 in a private loan without having to complete a request for a budget increase.”
  - sentence: budget_increase ⟵ “If you need to borrow additional loan funds and you aren’t sure whether this form is needed, please make an appointment to discuss your circumstances for a budget adjustment.”
### `033ab4b55e5a4e74` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements-music-theory-electives [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 70bd524e0872)
- issues: requirement_groups_skipped
  - courses: MUSIC 220 ⟵ “MUSIC 220 - Introduction to Computers and Music”
  - courses: MUSIC 321 ⟵ “MUSIC 321 - Counterpoint”
  - courses: MUSIC 323 ⟵ “MUSIC 323 - Instrumental and Choral Orchestration”
  - courses: MUSIC 327 ⟵ “MUSIC 327 - Studio Techniques”
  - courses: MUSIC 328 ⟵ “MUSIC 328 - Interactive Electronic Music”
  - courses: MUSIC 420 ⟵ “MUSIC 420 - Advanced Electronic Music and Sound Art:”
  - courses: MUSIC 680 ⟵ “MUSIC 680 - Special Studies in Music:”
### `219165d3b1911ca5` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements-music-history-electives [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 70bd524e0872)
- issues: requirement_groups_skipped
  - courses: MUSIC 310 ⟵ “MUSIC 310 - Introduction to World Musics”
  - courses: MUSIC 311 ⟵ “MUSIC 311 - Music of the Baroque Era”
  - courses: MUSIC 312 ⟵ “MUSIC 312 - Music of the Classic Era”
  - courses: MUSIC 313 ⟵ “MUSIC 313 - Music of the Romantic Era”
  - courses: MUSIC 314 ⟵ “MUSIC 314 - Music since 1900”
  - courses: MUSIC 317 ⟵ “MUSIC 317 - Introduction to American Music”
### `3cbe471f1cb3e775` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=theatre-practices-ba-theatre-education · requirement_key=major-requirements-electives [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-education-ba/ (sha256 025d5a7f7355)
- issues: requirement_groups_skipped
  - section: major-requirements-electives ⟵ “Major Requirements — Electives”
### `586324ce8f5a5ca8` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=theatre-practices-ba · requirement_key=major-requirements-electives [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-ba/ (sha256 bba7df228cf1)
- issues: requirement_groups_skipped
  - section: major-requirements-electives ⟵ “Major Requirements — Electives”
### `8c53412aebd7a8bb` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=actuarial-science-ba · requirement_key=professional-development [new] (labeled_in_source)
- source: https://catalog.uwm.edu/letters-science/mathematical-sciences/actuarial-science-ba/ (sha256 e63d6f0a1435)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ECON 103 ⟵ “ECON 103 - Principles of Microeconomics (VEE-Economics)”
  - courses: ECON 104 ⟵ “ECON 104 - Principles of Macroeconomics (VEE-Economics)”
### `93308053a90c8202` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=music-bfa-requirements-music-history [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 70bd524e0872)
- issues: requirement_groups_skipped
  - courses: MUSIC 106 ⟵ “MUSIC 106 - Foundations of Music”
  - courses: MUSIC 211 ⟵ “MUSIC 211 - General History of Western Music I”
  - courses: MUSIC 212 ⟵ “MUSIC 212 - General History of Western Music II”
### `b7c83827bf06d512` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements-recital [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 70bd524e0872)
- issues: requirement_groups_skipped
  - courses: MUSIC 659 ⟵ “MUSIC 659 - Junior Recital”
  - courses: MUSIC 660 ⟵ “MUSIC 660 - Senior Recital:”
### `bf8dff5f187ef518` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=actuarial-science-ba · requirement_key=requirements-additional-preparatory-coursework [new] (labeled_in_source)
- source: https://catalog.uwm.edu/letters-science/mathematical-sciences/actuarial-science-ba/ (sha256 e63d6f0a1435)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 234 ⟵ “MATH 234 - Linear Algebra and Differential Equations”
  - courses: ECON 103 ⟵ “ECON 103 - Principles of Microeconomics”
  - courses: ECON 104 ⟵ “ECON 104 - Principles of Macroeconomics”
### `cb8e5c6d5996cee4` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=theatre-practices-ba-theatre-education · requirement_key=major-requirements-school-of-education [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-education-ba/ (sha256 025d5a7f7355)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - section: major-requirements-school-of-education ⟵ “Major Requirements — School of Education”
### `d12f8b79c78cbd5c` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 70bd524e0872)
- issues: requirement_groups_skipped
  - courses: DANCE 111 ⟵ “DANCE 111 - Ballet I”
  - courses: DANCE 113 ⟵ “DANCE 113 - Modern Dance Technique I”
  - courses: DANCE 115 ⟵ “DANCE 115 - Jazz Dance I”
  - courses: DANCE 117 ⟵ “DANCE 117 - Tap I”
  - courses: DANCE 170 ⟵ “DANCE 170 - Hip-Hop Foundations I”
  - courses: DANCE 270 ⟵ “DANCE 270 - Hip-Hop II”
  - courses: DANCE 272 ⟵ “DANCE 272 - Salsa, Merengue, and Bachata I”
  - courses: DANCE 327 ⟵ “DANCE 327 - Dance for the Musical Theatre I”
  - courses: DANCE 321 ⟵ “DANCE 321 - Alexander Technique for the Performer”
  - courses: MUSIC 604 ⟵ “MUSIC 604 - Business for Performing Artists”
  - courses: MUSIC 245 ⟵ “MUSIC 245 - Basic and Italian Lyric Diction”
  - courses: MUSIC 246 ⟵ “MUSIC 246 - German and French Lyric Diction”
  - courses: MUSIC 444 ⟵ “MUSIC 444 - Vocal Pedagogy I”
  - courses: MUSIC 457 ⟵ “MUSIC 457 - Opera Theatre”
  - courses: MUSIC 520 ⟵ “MUSIC 520 - Voice Performance in Popular Music Styles”
### `e88cd3ddb96c2d2a` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=music-bfa-requirements-music-theory [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 70bd524e0872)
- issues: requirement_groups_skipped
  - courses: MUSIC 123 ⟵ “MUSIC 123 - Aural Theory I”
  - courses: MUSIC 124 ⟵ “MUSIC 124 - Aural Theory II”
  - courses: MUSIC 127 ⟵ “MUSIC 127 - Materials of Theory I”
  - courses: MUSIC 128 ⟵ “MUSIC 128 - Materials of Theory II”
  - courses: MUSIC 225 ⟵ “MUSIC 225 - Materials of Theory III”
  - courses: MUSIC 226 ⟵ “MUSIC 226 - Aural Theory III”
  - courses: MUSIC 421 ⟵ “MUSIC 421 - Materials of Theory IV”
### `f94519812e13d08a` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements-music-56 [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 70bd524e0872)
- issues: requirement_groups_skipped, choice_rule_unparsed
  - courses: MUSIC 457 ⟵ “MUSIC 457 - Opera Theatre”

## Re-verification of existing records (166)

- source_not_fetched: data/institutions/beloit/awards/2026-27.json ["awards", "ipeds-238333", null, "2026-27", {"award_name": "Presidential Scholarship"}]
- source_not_fetched: data/institutions/beloit/awards/2026-27.json ["awards", "ipeds-238333", null, "2026-27", {"award_name": "Eaton Scholarship"}]
- source_not_fetched: data/institutions/beloit/awards/2026-27.json ["awards", "ipeds-238333", null, "2026-27", {"award_name": "Deans\u2019 Award"}]
- source_not_fetched: data/institutions/beloit/transfer_policies/2026-27.json ["transfer_policies", "ipeds-238333", null, "2026-27", {}]
- source_not_fetched: data/institutions/bryantstratton-451750/transfer_policies/2026-27.json ["transfer_policies", "ipeds-451750", null, "2026-27", {}]
- source_not_fetched: data/institutions/carrollu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-238458", null, "2026-27", {}]
- source_not_fetched: data/institutions/cuw/transfer_policies/2026-27.json ["transfer_policies", "ipeds-238616", null, "2026-27", {}]
- source_not_fetched: data/institutions/lawrence/credit_policies/2026-27.json ["credit_policies", "ipeds-239017", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/mbu/awards/2026-27.json ["awards", "ipeds-239071", null, "2026-27", {"award_name": "Academic Merit Scholarship: ACT Composite Score 30+, SAT Composite Score 1360+"}]
- source_not_fetched: data/institutions/mbu/awards/2026-27.json ["awards", "ipeds-239071", null, "2026-27", {"award_name": "Academic Merit Scholarship: ACT Composite Score 27-29, SAT Composite Score 1260-1350"}]
- source_not_fetched: data/institutions/mbu/awards/2026-27.json ["awards", "ipeds-239071", null, "2026-27", {"award_name": "Academic Merit Scholarship: ACT Composite Score 25-26, SAT Composite Score 1200-1250"}]
- source_not_fetched: data/institutions/mbu/credit_policies/2026-27.json ["credit_policies", "ipeds-239071", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/marianuniversity/credit_policies/2026-27.json ["credit_policies", "ipeds-239080", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/matc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-239248", null, "2026-27", {}]
- source_not_fetched: data/institutions/miad/credit_policies/2026-27.json ["credit_policies", "ipeds-239309", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ntc/credit_policies/2026-27.json ["credit_policies", "ipeds-239460", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/nwtc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-239488", null, "2026-27", {}]
- source_not_fetched: data/institutions/uwlax/credit_policies/2026-27.json ["credit_policies", "ipeds-240329", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "animation-arts-ba", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "animation-arts-bfa", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "studio-art-bfa-dual-discipline-focus", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "public-health-bs", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "dance-bfa", "requirement_key": "major-3-technique"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "animation-arts-ba", "requirement_key": "major-7-advanced-animation-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "music-bfa-strings", "requirement_key": "major-4-chamber-music"}]
- policy_text_not_verbatim: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "music-bfa-versatile-voice", "requirement_key": "major-3-major-requirements"}] year=2026-27
- nothing_to_check: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "music-bfa-versatile-voice", "requirement_key": "major-4-major-requirements"}] year=2026-27
- nothing_to_check: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "music-bfa-versatile-voice", "requirement_key": "major-6-major-requirements"}] year=2026-27
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "education-bs-social-studies-education", "requirement_key": "major-2-program-core"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "exceptional-education-bs-early-childhood", "requirement_key": "major-2-program-core"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "exceptional-education-bs-early-childhood", "requirement_key": "major-4-program-core"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "exceptional-education-bs-early-childhood", "requirement_key": "major-5-program-core"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "exceptional-education-bs-k4-12-special-education", "requirement_key": "major-1-program-core"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "criminal-justice-and-criminology-bs", "requirement_key": "major-2-required-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "applied-math-and-computer-science-bs-college-of-engineering-and-applied-science-", "requirement_key": "major-2-core-requirements"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "applied-math-and-computer-science-bs-college-of-engineering-and-applied-science-", "requirement_key": "major-4-core-requirements"}]
- policy_text_not_verbatim: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "industrial-engineering-bse", "requirement_key": "major-3-mathematics-and-natural-science-requirement-30-credits"}] year=2026-27
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "geography-ba", "requirement_key": "major-1-core-curriculum"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "geography-ba", "requirement_key": "major-2-core-curriculum"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "geography-ba", "requirement_key": "major-4-core-curriculum"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "geography-bs", "requirement_key": "major-1-core-curriculum"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "geography-bs", "requirement_key": "major-2-core-curriculum"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "geography-bs", "requirement_key": "major-4-core-curriculum"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "journalism-advertising-and-media-studies-ba", "requirement_key": "major-2-required"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "journalism-advertising-and-media-studies-ba", "requirement_key": "major-3-required"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "philosophy-ba", "requirement_key": "major-2-required-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "philosophy-ba", "requirement_key": "major-3-required-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "philosophy-ba", "requirement_key": "major-4-required-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "psychology-ba", "requirement_key": "major-1-core-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "psychology-ba", "requirement_key": "major-3-core-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "psychology-ba", "requirement_key": "major-4-core-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "major-1-core-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "major-3-core-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "major-4-core-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "nutritional-sciences-bs", "requirement_key": "major-1-foundation-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "nutritional-sciences-bs", "requirement_key": "major-7-foundation-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "nutritional-sciences-bs", "requirement_key": "major-8-foundation-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "nutritional-sciences-bs", "requirement_key": "major-9-foundation-courses"}]
- source_not_fetched: data/institutions/uwm/degree_requirements/2026-27.json ["degree_requirements", "ipeds-240453", null, "2026-27", {"program_key": "nutritional-sciences-bs", "requirement_key": "major-10-foundation-courses"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "acct-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "apc-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "art-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "art-bfa"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "ai-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "artm-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "becon-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "biochem-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "biol-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "botany-plt"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "bus-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "ccp-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "chem-c-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "chm-eng-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "cle-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "clinic"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "cnr-41"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "com-ntr"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "com-ntr-41"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "com-sus-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "csd-32-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "csd-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "cyber-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "cyf-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "data-an-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "desgn-tech"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "dietet-41"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "dietetics"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "dnce-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "ece-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "ecosys-mgt"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "eei-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "electr-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "elem-ed-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "en-eth-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "en-eth-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "engl-t-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "engl-lit"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "engl-wep"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "fcs-t-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "fin-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "fish-aqua"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "for-mang"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "gd-bfa"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "general-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "general-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "geosp-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "germ-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "germ-t-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "his-sse-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "his-sse-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "hist-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "hist-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "histotech"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "hsw-32-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "hsw-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "hum-animal"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "hum-serv"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "hydrology"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "ia-bfa"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "instrument"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "intl-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "jazz"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "law-jus-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "law-jus-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "math"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "math-t-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "mechnc-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "medtech"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "mgt-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "mktg-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "mlt-mls"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "mstu-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "mstu-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "mued-bm"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "mus-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "mus-thea"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "network-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "ntsc-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "nurs-bsn"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "orgl-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "pcom-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "pe-32-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "phil-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "phil-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "phy-ed-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "phys-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "physcl-sci"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "pno"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "poli-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "poli-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "psen-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "psyc-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "recreation"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "rel-st-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "rel-st-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "sb-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "sec-std-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "soc-ba"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "soc-bs"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "soc-hbs-mn"}]
- source_not_fetched: data/institutions/uwsp/academic_programs/2026-27.json ["academic_programs", "ipeds-240480", null, "2026-27", {"program_key": "social-sci"}]
- source_not_fetched: data/institutions/uwsuper/transfer_policies/2026-27.json ["transfer_policies", "ipeds-240426", null, "2026-27", {}]
- source_not_fetched: data/institutions/wctc/credit_policies/2026-27.json ["credit_policies", "ipeds-240125", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/wctc/credit_policies/2026-27.json ["credit_policies", "ipeds-240125", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/wctc/credit_policies/2026-27.json ["credit_policies", "ipeds-240125", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/wlc/credit_policies/2026-27.json ["credit_policies", "ipeds-240338", null, "2026-27", {"policy_kind": "dual_enrollment"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Madison Area Technical College: admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency, aid_appeals
- University of Wisconsin-Madison: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency, aid_appeals
- University of Wisconsin-Milwaukee: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
