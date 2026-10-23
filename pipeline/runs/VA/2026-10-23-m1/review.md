# Review queue — VA (2026-27)

Pages fetched: 487; failures: 28. Candidates: 309 (4 without issues, 305 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 8 | 1 | 0 | 0 | 5 | 0 | 59 |
| cost_of_attendance | 4 | 1 | 0 | 0 | 6 | 0 | 62 |
| admissions_tests | 0 | 0 | 0 | 0 | 6 | 0 | 67 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 6 | 67 |
| merit_scholarships | 2 | 4 | 0 | 0 | 6 | 0 | 61 |
| ap_credit | 1 | 4 | 0 | 1 | 2 | 2 | 63 |
| clep_credit | 0 | 4 | 0 | 1 | 2 | 3 | 63 |
| ib_credit | 1 | 1 | 1 | 1 | 0 | 4 | 65 |
| dual_enrollment | 1 | 1 | 0 | 0 | 4 | 2 | 65 |
| transfer_credit | 1 | 8 | 1 | 0 | 4 | 0 | 59 |
| statewide_articulation | 0 | 0 | 0 | 0 | 4 | 2 | 67 |
| residency | 0 | 0 | 0 | 0 | 5 | 1 | 67 |
| degree_requirements | 6 | 0 | 0 | 0 | 2 | 1 | 64 |
| aid_appeals | 0 | 0 | 0 | 5 | 0 | 1 | 67 |

## Ready for review (4)

### `m95eb789785cdb4a` George Mason University — transfer_policies 2026-27 [same] (labeled_in_source)
- source: https://catalog.gmu.edu/admissions/undergraduate-policies/ (sha256 231fba4f4234)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Transfer credit is accepted from colleges holding accreditation from George Mason-recognized U.S. institutional accrediting agencies or from an international university recognized by that country’s Ministry of Education or equivalent, provided that a grade of C or better has been earned in the course, and the course content aligns with George Mason University's academic standards.”
  - min_grade: C ⟵ “Transfer credit is accepted from colleges holding accreditation from George Mason-recognized U.S. institutional accrediting agencies or from an international university recognized by that country’s Ministry of Education, or equivalent, provided that a grade of C or better has been earned in the course, and the course content aligns with George Mason University's academic standards.”
  - max_transfer_credits: 75 ⟵ “A maximum of 90 transfer credit hours, with no more than 75 credit hours from a community college, may apply to a bachelor’s degree at Mason.”
### `8beeda4aa09a6a4a` Old Dominion University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.odu.edu/academics/academic-records/score-analysis/ap-ib (sha256 d7e60dda37dc)
- checks: {"distinct_exams": 37, "equivalencies": 79, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 105N, or BIOL 106N, or BIOL 110N & 111N, or BIOL 112N & 113N, or BIOL 117N & 118N | 4”
  - equivalencies[IB-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 121N & 122N | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|3, 4, 5]:  ⟵ “Computer Science A | 3, 4, 5 | CS 151 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CS 1ELE | 3”
  - equivalencies[IB-ECONOMICS|3, 4, 5]:  ⟵ “Economics: Macro | 3, 4, 5 | ECON 201S | 3”
  - equivalencies[IB-ECONOMICS|3, 4, 5]:  ⟵ “Economics: Micro | 3, 4, 5 | ECON 202S | 3”
  - equivalencies[IB-HISTORY|3,4]:  ⟵ “European History | 3,4 | HIST 102H | 3”
  - equivalencies[IB-HISTORY|5]:  ⟵ “European History | 5 | HIST 102H & INTP 1REQ | 6”
  - equivalencies[IB-HISTORY|4]:  ⟵ “European History | 4 | 212F | 6”
  - equivalencies[IB-HISTORY|5]:  ⟵ “European History | 5 | 212F & 3ELE | 9”
  - equivalencies[IB-FRENCH|3]:  ⟵ “French Language & Culture | 3 | FR 201 | 3”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French Language & Culture | 4 | FR 201 & 202 | 6”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French Language & Culture | 5 | FR 202 & 3ELE | 6”
  - equivalencies[IB-GERMAN|3]:  ⟵ “German Language & Culture | 3 | GER 201 | 3”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German Language & Culture | 4 | GER 201 & 202 | 6”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German Language & Culture | 5 | GER 202 & 3ELE | 6”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German Language & Culture | 4 | 201 & 202 | 6”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German Language & Culture | 5 | 202 & 3ELE | 6”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German Language & Culture | 4 | 212F | 6”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German Language & Culture | 5 | 212F & 3ELE | 9”
  - equivalencies[IB-LATIN|3]:  ⟵ “Latin | 3 | LATN 201 | 3”
  - equivalencies[IB-LATIN|4]:  ⟵ “Latin | 4 | LATN 201 & 202 | 6”
  - equivalencies[IB-LATIN|5]:  ⟵ “Latin | 5 | LATN 202 & 3ELE | 6”
  - equivalencies[IB-SPANISH|3]:  ⟵ “Spanish Language & Culture | 3 | SPAN 201 | 3”
  - equivalencies[IB-SPANISH|4]:  ⟵ “Spanish Language & Culture | 4 | SPAN 201 & 202 | 6”
  - … 54 more rows
### `8cf3c507e8c6ab66` Old Dominion University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.odu.edu/sites/default/files/documents/gaa-odu-and-vccs.pdf (sha256 889bce4eb3ba)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Course requirements: In order for credits to transfer to ODU, students are required to earn a grade of “C” or better in each community college course applicable to the transfer degree from a VCCS 1 institution.”
### `ebdcf120baeed02a` Virginia Polytechnic Institute and State University — credit_policies 2026-27 · policy_kind=AP [same] (labeled_in_title)
- source: https://transferguide.registrar.vt.edu/Advanced-Placement/Advanced-Placement-2026.html (sha256 34764bc17a05)
- checks: {"distinct_exams": 36, "equivalencies": 70, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, or 5]:  ⟵ “AFST: African American Studies |  | 3, 4, or 5 | AFST 2XXX | Africana Studies Elective | 3”
  - equivalencies[AP-DRAWING|3, 4, or 5]:  ⟵ “ART: Drawing |  | 3, 4, or 5 | ART 1404 | Drawing I | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, or 5]:  ⟵ “ART: 2-D Design |  | 3, 4, or 5 | ART 2XXX | Art Elective | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, or 5]:  ⟵ “ART: 3-D Design |  | 3, 4, or 5 | ART 1XXX | Art Elective | 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “ART: Art History |  | 3 | ART 2385 | Survey of the History of Western Art | 3”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “ART: Art History |  | 4 or 5 | ART 2385 + ART 2386 | Survey of the Hist of West Art + Survey of the Hist of West Art | 3+3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “BIOL: Biology |  | 3 | BIOL 1014 | Introduction to Biology | 3”
  - equivalencies[AP-BIOLOGY|4 or 5]:  ⟵ “BIOL: Biology |  | 4 or 5 | BIOL 1105 + BIOL 1115 + BIOL 1106 + BIOL 1116 | Principles of Biology + Principles of Biology Lab + Principles of Biology + Principles of Biology Lab | 3+1+3+1”
  - equivalencies[AP-CYBERSECURITY|3, 4, or 5]:  ⟵ “BIT: Cybersecurity |  | 3, 4, or 5 | BIT 2XXX | Business Information Technology Elective | ”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “CHEM: Chemistry |  | 3 | CHEM 1015 + CHEM 1025 +CHEM 1016 + CHEM 1026 | Introduction to Chemistry + Introduction to Chemistry Lab + Introduction to Chemistry + Introduction to Chemistry Lab | 3+1+3+1”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “CHEM: Chemistry |  | 4 or 5 | CHEM 1035 + CHEM 1045 + CHEM 1036 + CHEM 1046 | General Chemistry + General Chemistry Lab + General Chemistry + General Chemistry Lab | 3+1+3+1”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “CHIN: Chinese Language & Culture |  | 3 | CHN 2XXX | Chinese Elective | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “CHIN: Chinese Language & Culture |  | 4 | CHN 3XXX | Chinese Elective | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “CHIN: Chinese Language & Culture |  | 5 | CHN 3XXX + CHN 3XXX | Chinese Elective + Chinese Elective | 3+3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, or 5]:  ⟵ “CS: Computer Science A |  | 3, 4, or 5 | CS 1114 | Introduction to Software Design | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, or 5]:  ⟵ “CS: Computer Science Principles |  | 3, 4, or 5 | CS 1014 | Intro to Computational Thinking | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “ECON: Macroeconomics |  | 3 | ECON 1XXX | Economics Elective | 3”
  - equivalencies[AP-MACROECONOMICS|4 or 5]:  ⟵ “ECON: Macroeconomics |  | 4 or 5 | ECON 2006 | Principles of Economics | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “ECON: Microeconomics |  | 3 | ECON 1XXX | Economics Elective | 3”
  - equivalencies[AP-MICROECONOMICS|4 or 5]:  ⟵ “ECON: Microeconomics |  | 4 or 5 | ECON 2005 | Principles of Economics | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “ENSC: Environmental Science |  | 3 | ENSC 1015 | Found. Environmental Science | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4 or 5]:  ⟵ “ENSC: Environmental Science |  | 4 or 5 | ENSC 1015 + ENSC 1016 | Found. Environmental Science + Found. Environmental Science | 3+3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “FR: French Language & Culture |  | 3 | FR 2XXX | French Elective | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “FR: French Language & Culture |  | 4 | FR 3XXX | French Elective | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “FR: French Language & Culture |  | 5 | FR 3XXX + FR 3XXX | French Elective + French Elective | 3+3”
  - … 45 more rows

## Exceptions (305)

### `1fba68e3534fb9d5` George Mason University — academic_programs 2026-27 · program_key=business-bs [same] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
- checks: {"courses": 307, "groups": 44, "groups_skipped": 1}
  - program_name: Business, BS ⟵ “Business, BS | George Mason University Catalog”
  - total_credits: 120 ⟵ “Total credits: 120”
### `67e00f1727c5f48c` George Mason University — academic_programs 2026-27 · program_key=communication-ba [same] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
- checks: {"courses": 261, "groups": 17, "groups_skipped": 3}
  - program_name: Communication, BA ⟵ “Communication, BA | George Mason University Catalog”
### `1d4be37217515b7a` George Mason University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gmu.edu/financial-aid-parent/eligibility/satisfactory-academic-progress-sap-policy (sha256 26d3ff8c06ca)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Students who do not meet the SAP requirements at the end of the appeal-approved semester will be placed on financial aid suspension (described above). *To appeal the loss of a Mason scholarship, please see the Scholarships Page for information.”
### `5e9bc578e9821668` George Mason University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gmu.edu/financial-aid-parent/eligibility/satisfactory-academic-progress-sap-policy (sha256 26d3ff8c06ca)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Suspension Students who do not meet the SAP requirement are automatically placed on financial aid suspension (unless the student is approved for a SAP appeal, see below).”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal All students have the right to appeal the suspension of their financial aid if there were mitigating circumstances that caused failure to meet SAP standards.”
  - sentence: sap_appeal ⟵ “How to Submit an Appeal Complete and submit the Satisfactory Academic Progress (SAP) Appeal Form and Student Educational Plan (SEP) Form that is attached to it, located on the Forms Page.”
### `00d5ec1f7d18be1a` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-financial-planning-and-wealth-management-fpwm-required-courses-2 [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: FNAN 390 ⟵ “FNAN 390 - Introduction to Financial Planning and Wealth Management”
  - courses: FNAN 311 ⟵ “FNAN 311 - Principles of Investment”
  - courses: ACCT 351 ⟵ “ACCT 351 - Taxation and Managerial Decision Making”
  - courses: ACCT 408 ⟵ “ACCT 408 - Taxes Insurance and Risk Management”
  - courses: ACCT 441 ⟵ “ACCT 441 - Estate Planning”
  - courses: ACCT 493 ⟵ “ACCT 493 - Financial Planning and Wealth Management Capstone (Mason Core)”
### `0667f6183c1af341` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=bam-ms-in-finance-pathway-requirements-2 [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MSF 603 ⟵ “MSF 603 - Managerial Economics and Decisions of the Firm”
  - courses: MSF 632 ⟵ “MSF 632 - Statistical and Quantitative Methods for Finance”
  - courses: MSF 643 ⟵ “MSF 643 - Financial Economics and Statement Analysis”
  - courses: MSF 672 ⟵ “MSF 672 - Corporate Finance and Governance”
  - courses: MSF 683 ⟵ “MSF 683 - Ethical and Professional Standards in Finance”
### `094c9c6db8233b0b` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=bam-ms-accounting-pathway-requirements [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: ACCT 630 ⟵ “ACCT 630 - Advanced Financial Accounting”
  - courses: ACCT 633 ⟵ “ACCT 633 - Advanced Issues in Financial Reporting”
  - courses: ACCT 651 ⟵ “ACCT 651 - Advanced Issues in Taxation”
  - courses: ACCT 670 ⟵ “ACCT 670 - International Accounting”
### `0e7d8566f9e0046a` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-public-relations-strategic-communication-prsc-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 203 ⟵ “COMM 203 - Introduction to Journalism”
  - courses: COMM 208 ⟵ “COMM 208 - Introduction to Media Production”
  - courses: COMM 302 ⟵ “COMM 302 - Media Theory”
  - courses: COMM 304 ⟵ “COMM 304 - Foundations of Health Communication”
  - courses: COMM 318 ⟵ “COMM 318 - Persuasion”
  - courses: COMM 335 ⟵ “COMM 335 - Organizational Communication”
  - courses: COMM 359 ⟵ “COMM 359 - Digital Media Management”
  - courses: COMM 375 ⟵ “COMM 375 - Digital Advertising Strategies”
  - courses: COMM 384 ⟵ “COMM 384 - Social Media and Strategic Communication”
  - courses: COMM 388 ⟵ “COMM 388 - Special Topics in Public Relations and Strategic Communication”
  - courses: COMM 389 ⟵ “COMM 389 - Strategic Communication for Nonprofits”
  - courses: COMM 411 ⟵ “COMM 411 - Public Relations in Practice”
  - courses: COMM 433 ⟵ “COMM 433 - Environmental Communication, Campaigns, and Social Movements”
  - courses: COMM 435 ⟵ “COMM 435 - Digital Communication”
  - courses: COMM 454 ⟵ “COMM 454 - Free Speech and Ethics (Mason Core)”
### `1af4a515678fc67f` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-financial-planning-and-wealth-management-fpwm-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: FNAN 390 ⟵ “FNAN 390 - Introduction to Financial Planning and Wealth Management”
  - courses: FNAN 311 ⟵ “FNAN 311 - Principles of Investment”
  - courses: ACCT 351 ⟵ “ACCT 351 - Taxation and Managerial Decision Making”
  - courses: ACCT 408 ⟵ “ACCT 408 - Taxes Insurance and Risk Management”
  - courses: ACCT 441 ⟵ “ACCT 441 - Estate Planning”
  - courses: ACCT 493 ⟵ “ACCT 493 - Financial Planning and Wealth Management Capstone (Mason Core)”
### `1d3821779e4cb505` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-accounting-acct-required-courses-2 [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: ACCT 311 ⟵ “ACCT 311 - Managerial and Cost Accounting”
  - courses: ACCT 331 ⟵ “ACCT 331 - Intermediate Accounting I”
  - courses: ACCT 332 ⟵ “ACCT 332 - Intermediate Accounting II”
  - courses: ACCT 351 ⟵ “ACCT 351 - Taxation and Managerial Decision Making”
  - courses: ACCT 361 ⟵ “ACCT 361 - Accounting Analytics”
  - courses: ACCT 461 ⟵ “ACCT 461 - Assurance and Audit Services (Mason Core)”
### `24895d33fe10b10d` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-journalism-jnl-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 145 ⟵ “COMM 145 - Newspaper Workshop I”
  - courses: COMM 148 ⟵ “COMM 148 - Podcasting and Radio Workshop I”
  - courses: COMM 208 ⟵ “COMM 208 - Introduction to Media Production”
  - courses: COMM 227 ⟵ “COMM 227 - Introduction to Political Communication”
  - courses: COMM 302 ⟵ “COMM 302 - Media Theory”
  - courses: COMM 309 ⟵ “COMM 309 - Writing across the Media”
  - courses: COMM 345 ⟵ “COMM 345 - Newspaper Workshop II”
  - courses: COMM 353 ⟵ “COMM 353 - Broadcast Journalism”
  - courses: COMM 356 ⟵ “COMM 356 - Performance for Digital Production”
  - courses: COMM 369 ⟵ “COMM 369 - Multimedia Storytelling (Mason Core)”
  - courses: COMM 370 ⟵ “COMM 370 - Feature Writing”
  - courses: COMM 371 ⟵ “COMM 371 - Sports Writing and Reporting”
  - courses: COMM 374 ⟵ “COMM 374 - Political Journalism”
  - courses: COMM 387 ⟵ “COMM 387 - Special Topics in Journalism”
  - courses: COMM 454 ⟵ “COMM 454 - Free Speech and Ethics (Mason Core)”
### `256885a945648fd4` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=co-curricular-requirements-acct [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: ACCT 462 ⟵ “ACCT 462 - Honors Seminar in Accounting”
### `2c909f3ead425695` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=co-curricular-requirements-busa [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MIS 462 ⟵ “MIS 462 - Honors Seminar in Management Information Systems (Topic Varies)”
### `338089612fa0d1a9` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=co-curricular-requirements-oscm [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: OSCM 462 ⟵ “OSCM 462 - Honors Seminar in Operations Management (Topic Varies)”
### `343da0bd707a8b61` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=co-curricular-requirements-mktg [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MKTG 462 ⟵ “MKTG 462 - Honors Seminar in Marketing (Topic Varies)”
### `355404519a451538` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=business-foundations [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: ACCT 203 ⟵ “ACCT 203 - Survey of Accounting”
  - courses: BUS 100 ⟵ “BUS 100 - Business and Society (Mason Core)”
  - courses: BUS 103 ⟵ “BUS 103 - Develop Professional Skills I: Foundational Elements”
  - courses: BUS 200 ⟵ “BUS 200 - Global Environment of Business (Mason Core)”
  - courses: BUS 210 ⟵ “BUS 210 - Business Analytics I (Mason Core)”
  - courses: BUS 310 ⟵ “BUS 310 - Business Analytics II”
  - courses: ECON 103 ⟵ “ECON 103 - Contemporary Microeconomic Principles (Mason Core)”
  - courses: ECON 104 ⟵ “ECON 104 - Contemporary Macroeconomic Principles (Mason Core)”
  - courses: MATH 108 ⟵ “MATH 108 - Introductory Calculus with Business Applications (Mason Core)”
  - courses: MATH 113 ⟵ “MATH 113 - Analytic Geometry and Calculus I (Mason Core)”
  - courses: MATH 114 ⟵ “MATH 114 - Analytic Geometry and Calculus II”
### `3a444f22f1b572b5` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=social-and-behavioral-sciences-soci [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, choice_rule_unparsed
  - courses: GGS 101 ⟵ “GGS 101 - Major World Regions (Mason Core)”
  - courses: GGS 103 ⟵ “GGS 103 - Human Geography (Mason Core)”
  - courses: GGS 110 ⟵ “GGS 110 - Introduction to Geoinformation Technologies”
  - courses: GGS 301 ⟵ “GGS 301 - Political Geography (Mason Core)”
  - courses: GGS 303 ⟵ “GGS 303 - Geography of Resource Conservation (Mason Core)”
  - courses: GGS 304 ⟵ “GGS 304 - Population Geography (Mason Core)”
  - courses: GGS 305 ⟵ “GGS 305 - Economic Geography”
  - courses: GGS 306 ⟵ “GGS 306 - Urban Geography”
  - courses: GGS 315 ⟵ “GGS 315 - Geography of the United States”
  - courses: GGS 316 ⟵ “GGS 316 - Geography of Latin America”
  - courses: GGS 320 ⟵ “GGS 320 - Geography of Europe”
  - courses: GGS 325 ⟵ “GGS 325 - Geography of North Africa and the Middle East”
  - courses: GGS 326 ⟵ “GGS 326 - Geography of Eastern Europe and Russia”
  - courses: GGS 357 ⟵ “GGS 357 - Urban Planning”
  - courses: GGS 380 ⟵ “GGS 380 - Geography of Virginia”
### `4a8d7e82f3c7f3de` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-finance-fnan-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: FNAN 311 ⟵ “FNAN 311 - Principles of Investment”
  - courses: FNAN 321 ⟵ “FNAN 321 - Financial Institutions”
  - courses: FNAN 341 ⟵ “FNAN 341 - Introduction to Firm Valuation”
  - courses: FNAN 401 ⟵ “FNAN 401 - Advanced Financial Management”
  - courses: FNAN 477 ⟵ “FNAN 477 - Student Managed Investment Fund (Mason Core)”
  - courses: FNAN 498 ⟵ “FNAN 498 - RS: Contemporary Topics in Finance (Mason Core)”
### `4c1ca8ccafe66ba4` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=co-curricular-requirements [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: BUS 498 ⟵ “BUS 498 - Capstone Course: Advanced Business Models (Mason Core) (Honors Section)”
### `4f766af6da54ce3d` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-management-information-systems-mis-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MIS 341 ⟵ “MIS 341 - Cloud Computing Essentials”
  - courses: MIS 350 ⟵ “MIS 350 - AI - Assisted Programming for Business Applications”
  - courses: MIS 410 ⟵ “MIS 410 - Advanced Database Systems”
  - courses: MIS 412 ⟵ “MIS 412 - E-Business Systems Development”
  - courses: MIS 415 ⟵ “MIS 415 - Information Systems Audit and Control”
  - courses: MIS 420 ⟵ “MIS 420 - Information Security and Assurance”
  - courses: MIS 430 ⟵ “MIS 430 - Data Warehousing”
  - courses: MIS 431 ⟵ “MIS 431 - Data Mining for Business Applications (Mason Core)”
  - courses: MIS 432 ⟵ “MIS 432 - Advanced Data Mining”
  - courses: MIS 433 ⟵ “MIS 433 - Programming for Analytics”
  - courses: MIS 436 ⟵ “MIS 436 - AI for Information Systems Applications”
  - courses: MIS 441 ⟵ “MIS 441 - Cloud System Management”
  - courses: MIS 462 ⟵ “MIS 462 - Honors Seminar in Management Information Systems (Topic Varies)”
  - courses: MIS 490 ⟵ “MIS 490 - Professional Readiness through Client Projects & Solutioning”
  - courses: MIS 491 ⟵ “MIS 491 - Seminar in Management Information Systems”
  - courses: MIS 492 ⟵ “MIS 492 - Internship in Management Information Systems”
  - courses: MIS 499 ⟵ “MIS 499 - Independent Study in Management Information Systems”
  - courses: GBUS 662 ⟵ “GBUS 662 - Management of Information Technology and The Digital Enterprise”
  - courses: MSBA 610 ⟵ “MSBA 610 - Essentials of Business Analytics and AI: From Data Ethics to Data Driven Decision-making”
  - courses: MSBA 615 ⟵ “MSBA 615 - Database Management for Business Analytics”
  - courses: MSBA 618 ⟵ “MSBA 618 - Programming for Business Analytics”
  - courses: MSBA 625 ⟵ “MSBA 625 - Exploratory Data Analysis and Visualization”
  - courses: OSCM 352 ⟵ “OSCM 352 - Management Science”
  - courses: OSCM 435 ⟵ “OSCM 435 - Business Process Analysis and Simulation”
  - courses: OSCM 456 ⟵ “OSCM 456 - Quality Management (Mason Core)”
  - … 2 more rows
### `50560863e5b67252` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-financial-planning-and-wealth-management-fpwm-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: FNAN 341 ⟵ “FNAN 341 - Introduction to Firm Valuation”
  - courses: FNAN 411 ⟵ “FNAN 411 - Investment Analysis and Portfolio Management”
  - courses: FNAN 444 ⟵ “FNAN 444 - Socially Responsible Finance”
  - courses: FNAN 483 ⟵ “FNAN 483 - Ethical and Professional Standards in Finance”
  - courses: FNAN 492 ⟵ “FNAN 492 - Internship in Finance”
  - courses: ACCT 315 ⟵ “ACCT 315 - Personal Financial Planning”
  - courses: ACCT 372 ⟵ “ACCT 372 - Financial Statement Analysis”
  - courses: ACCT 451 ⟵ “ACCT 451 - Advanced Federal Taxation”
  - courses: MSF 603 ⟵ “MSF 603 - Managerial Economics and Decisions of the Firm”
  - courses: MSF 632 ⟵ “MSF 632 - Statistical and Quantitative Methods for Finance”
  - courses: MSF 643 ⟵ “MSF 643 - Financial Economics and Statement Analysis”
  - courses: MSF 672 ⟵ “MSF 672 - Corporate Finance and Governance”
  - courses: MSF 683 ⟵ “MSF 683 - Ethical and Professional Standards in Finance”
### `534a39ee98c15116` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=bam-msm-pathway-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: GBUS 613 ⟵ “GBUS 613 - Financial Reporting and Decision Making”
  - courses: GBUS 623 ⟵ “GBUS 623 - Marketing Management”
  - courses: GBUS 638 ⟵ “GBUS 638 - Operations Management”
  - courses: GBUS 643 ⟵ “GBUS 643 - Managerial Finance”
  - courses: GBUS 653 ⟵ “GBUS 653 - Organizational Behavior”
  - courses: GBUS 662 ⟵ “GBUS 662 - Management of Information Technology and The Digital Enterprise”
### `5ab0edf92157b691` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-communication-studies-coms-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 201 ⟵ “COMM 201 - Small Group Communication”
  - courses: COMM 202 ⟵ “COMM 202 - Media and Society”
  - courses: COMM 210 ⟵ “COMM 210 - Voice and Articulation”
  - courses: COMM 230 ⟵ “COMM 230 - Case Studies in Persuasion”
  - courses: COMM 260 ⟵ “COMM 260 - Basic Debate Theory and Practice”
  - courses: COMM 261 ⟵ “COMM 261 - Theories of Argumentation”
  - courses: COMM 302 ⟵ “COMM 302 - Media Theory”
  - courses: COMM 304 ⟵ “COMM 304 - Foundations of Health Communication”
  - courses: COMM 306 ⟵ “COMM 306 - Issues in Intercultural Communication”
  - courses: COMM 307 ⟵ “COMM 307 - Field Study in Communication”
  - courses: COMM 310 ⟵ “COMM 310 - Performance for Communication Arts”
  - courses: COMM 332 ⟵ “COMM 332 - Nonverbal Communication”
  - courses: COMM 334 ⟵ “COMM 334 - Family and Health Communication”
  - courses: COMM 359 ⟵ “COMM 359 - Digital Media Management”
  - courses: COMM 365 ⟵ “COMM 365 - Gender, Race, and Class in the Media”
  - courses: COMM 367 ⟵ “COMM 367 - Children and Media”
  - courses: COMM 380 ⟵ “COMM 380 - Media Criticism (Mason Core)”
  - courses: COMM 384 ⟵ “COMM 384 - Social Media and Strategic Communication”
  - courses: COMM 385 ⟵ “COMM 385 - Special Topics in Communication Studies”
  - courses: COMM 389 ⟵ “COMM 389 - Strategic Communication for Nonprofits”
  - courses: COMM 395 ⟵ “COMM 395 - Special Topics in Health Communication”
  - courses: COMM 401 ⟵ “COMM 401 - Interpersonal Skills for Career Development”
  - courses: COMM 433 ⟵ “COMM 433 - Environmental Communication, Campaigns, and Social Movements”
  - courses: COMM 434 ⟵ “COMM 434 - Interviewing”
  - courses: COMM 435 ⟵ “COMM 435 - Digital Communication”
  - … 4 more rows
### `66bd990e8dd5ceca` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=co-curricular-requirements-mgmt [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MGMT 462 ⟵ “MGMT 462 - Honors Seminar in Management (Topic Varies)”
### `6c9d84f10c6dc1f9` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-management-mgmt-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: BULE 402 ⟵ “BULE 402 - Commercial Law”
  - courses: MGMT 325 ⟵ “MGMT 325 - Creating Value for Business Stakeholders”
  - courses: MGMT 412 ⟵ “MGMT 412 - Diversity in Organizations”
  - courses: MGMT 413 ⟵ “MGMT 413 - Organizational Development and Management Consulting”
  - courses: MGMT 421 ⟵ “MGMT 421 - Advanced Human Resource Management”
  - courses: MGMT 431 ⟵ “MGMT 431 - The Legal Environment for Employee and Labor Relations”
  - courses: MGMT 441 ⟵ “MGMT 441 - International Strategy”
  - courses: MGMT 451 ⟵ “MGMT 451 - Introduction to Entrepreneurship”
  - courses: MGMT 452 ⟵ “MGMT 452 - Experiential Entrepreneurship”
  - courses: MGMT 453 ⟵ “MGMT 453 - Starting a Business”
  - courses: MGMT 454 ⟵ “MGMT 454 - Social Impact and Entrepreneurship”
  - courses: MGMT 461 ⟵ “MGMT 461 - Cross Cultural and Global Management”
  - courses: MGMT 462 ⟵ “MGMT 462 - Honors Seminar in Management (Topic Varies)”
  - courses: MGMT 463 ⟵ “MGMT 463 - Negotiations in Organizations”
  - courses: MGMT 464 ⟵ “MGMT 464 - Teamwork and Interpersonal Skills”
  - courses: MGMT 471 ⟵ “MGMT 471 - Competitive Strategy”
  - courses: MGMT 491 ⟵ “MGMT 491 - Current Topics in Management”
  - courses: MGMT 492 ⟵ “MGMT 492 - Internship in Management”
  - courses: MGMT 499 ⟵ “MGMT 499 - Independent Study”
  - courses: GBUS 653 ⟵ “GBUS 653 - Organizational Behavior”
### `6f2eaf2ef598e401` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-business-analytics-busa-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: FNAN 430 ⟵ “FNAN 430 - Empirical Methods in Finance”
  - courses: FNAN 436 ⟵ “FNAN 436 - Probability Methods for Finance”
  - courses: MIS 432 ⟵ “MIS 432 - Advanced Data Mining”
  - courses: MIS 436 ⟵ “MIS 436 - AI for Information Systems Applications”
  - courses: MIS 490 ⟵ “MIS 490 - Professional Readiness through Client Projects & Solutioning”
  - courses: MIS 492 ⟵ “MIS 492 - Internship in Management Information Systems”
  - courses: MKTG 351 ⟵ “MKTG 351 - Marketing Research”
  - courses: MKTG 352 ⟵ “MKTG 352 - Marketing Analytics: AI, Data, and Models”
  - courses: OSCM 352 ⟵ “OSCM 352 - Management Science”
  - courses: OSCM 435 ⟵ “OSCM 435 - Business Process Analysis and Simulation”
  - courses: OSCM 452 ⟵ “OSCM 452 - Business Forecasting”
  - courses: STAT 463 ⟵ “STAT 463 - Introduction to Exploratory Data Analysis”
  - courses: SYST 473 ⟵ “SYST 473 - Decision and Risk Analysis”
  - courses: MSBA 610 ⟵ “MSBA 610 - Essentials of Business Analytics and AI: From Data Ethics to Data Driven Decision-making”
  - courses: MSBA 615 ⟵ “MSBA 615 - Database Management for Business Analytics”
  - courses: MSBA 618 ⟵ “MSBA 618 - Programming for Business Analytics”
  - courses: MSBA 625 ⟵ “MSBA 625 - Exploratory Data Analysis and Visualization”
### `7f626a218d3af272` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-advocacy-advo-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 140 ⟵ “COMM 140 - Forensics Seminar I”
  - courses: COMM 141 ⟵ “COMM 141 - Forensics Seminar II”
  - courses: COMM 142 ⟵ “COMM 142 - Debate Seminar I”
  - courses: COMM 143 ⟵ “COMM 143 - Debate Seminar II”
  - courses: COMM 230 ⟵ “COMM 230 - Case Studies in Persuasion”
  - courses: COMM 260 ⟵ “COMM 260 - Basic Debate Theory and Practice”
  - courses: COMM 261 ⟵ “COMM 261 - Theories of Argumentation”
  - courses: COMM 318 ⟵ “COMM 318 - Persuasion”
  - courses: COMM 340 ⟵ “COMM 340 - Forensics Seminar III”
  - courses: COMM 341 ⟵ “COMM 341 - Forensics Seminar IV”
  - courses: COMM 342 ⟵ “COMM 342 - Debate Seminar III”
  - courses: COMM 343 ⟵ “COMM 343 - Debate Seminar IV”
  - courses: COMM 350 ⟵ “COMM 350 - Mass Communication and Public Policy”
  - courses: COMM 374 ⟵ “COMM 374 - Political Journalism”
  - courses: COMM 380 ⟵ “COMM 380 - Media Criticism (Mason Core)”
  - courses: COMM 386 ⟵ “COMM 386 - Special Topics in Advocacy”
  - courses: COMM 412 ⟵ “COMM 412 - Media and Political Controversy”
  - courses: COMM 431 ⟵ “COMM 431 - Social Media and Democratic Engagement”
  - courses: COMM 433 ⟵ “COMM 433 - Environmental Communication, Campaigns, and Social Movements”
  - courses: COMM 440 ⟵ “COMM 440 - Ceremonial Speech Writing and Performance”
  - courses: COMM 457 ⟵ “COMM 457 - Communicating Dissent: Revolutions and Social Movements (Mason Core)”
### `8935148f731c3358` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=co-curricular-requirements-fnan [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: FNAN 462 ⟵ “FNAN 462 - Honors Seminar in Finance”
### `8fe6e728bfee7dcc` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=bam-ms-in-business-analytics-pathway-requirements [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MSBA 610 ⟵ “MSBA 610 - Essentials of Business Analytics and AI: From Data Ethics to Data Driven Decision-making”
  - courses: MSBA 615 ⟵ “MSBA 615 - Database Management for Business Analytics”
  - courses: MSBA 618 ⟵ “MSBA 618 - Programming for Business Analytics”
  - courses: MSBA 625 ⟵ “MSBA 625 - Exploratory Data Analysis and Visualization”
### `90bd00ffe7376655` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=general-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - section: general-electives ⟵ “General Electives”
### `924efb297ffd746c` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=bam-ms-in-finance-pathway-requirements [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MSF 603 ⟵ “MSF 603 - Managerial Economics and Decisions of the Firm”
  - courses: MSF 632 ⟵ “MSF 632 - Statistical and Quantitative Methods for Finance”
  - courses: MSF 643 ⟵ “MSF 643 - Financial Economics and Statement Analysis”
  - courses: MSF 672 ⟵ “MSF 672 - Corporate Finance and Governance”
  - courses: MSF 683 ⟵ “MSF 683 - Ethical and Professional Standards in Finance”
### `976e74d57ac203ba` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-accounting-acct-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: ACCT 311 ⟵ “ACCT 311 - Managerial and Cost Accounting”
  - courses: ACCT 331 ⟵ “ACCT 331 - Intermediate Accounting I”
  - courses: ACCT 332 ⟵ “ACCT 332 - Intermediate Accounting II”
  - courses: ACCT 351 ⟵ “ACCT 351 - Taxation and Managerial Decision Making”
  - courses: ACCT 361 ⟵ “ACCT 361 - Accounting Analytics”
  - courses: ACCT 461 ⟵ “ACCT 461 - Assurance and Audit Services (Mason Core)”
### `9c18546401dfed3a` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-journalism-jnl-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 203 ⟵ “COMM 203 - Introduction to Journalism”
  - courses: COMM 351 ⟵ “COMM 351 - News Writing and Reporting”
  - courses: COMM 352 ⟵ “COMM 352 - News Editing”
  - courses: COMM 369 ⟵ “COMM 369 - Multimedia Storytelling (Mason Core)”
  - courses: COMM 475 ⟵ “COMM 475 - Journalism Law”
### `9d03ccc94e0dcd93` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-accounting-acct-600-level-courses-for-student-s-in-the-accelera [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: ACCT 611 ⟵ “ACCT 611 - Advanced Issues in Managerial Accounting”
  - courses: ACCT 621 ⟵ “ACCT 621 - GovCon Acquisition Regulations and Reporting”
  - courses: ACCT 630 ⟵ “ACCT 630 - Advanced Financial Accounting”
  - courses: ACCT 633 ⟵ “ACCT 633 - Advanced Issues in Financial Reporting”
  - courses: ACCT 636 ⟵ “ACCT 636 - Fraud Examination”
  - courses: ACCT 651 ⟵ “ACCT 651 - Advanced Issues in Taxation”
  - courses: ACCT 661 ⟵ “ACCT 661 - Advanced Accounting Analytics I”
  - courses: ACCT 665 ⟵ “ACCT 665 - Advanced Accounting Analytics II”
  - courses: ACCT 670 ⟵ “ACCT 670 - International Accounting”
  - courses: ACCT 672 ⟵ “ACCT 672 - Governmental and Nonprofit Accounting”
  - courses: ACCT 673 ⟵ “ACCT 673 - Advanced Accounting Information Systems”
  - courses: ACCT 696 ⟵ “ACCT 696 - Directed Studies in Accounting”
  - courses: ACCT 697 ⟵ “ACCT 697 - Special Topics in Accounting”
### `a127c9fa00afe8aa` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=capstone [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: BUS 498 ⟵ “BUS 498 - Capstone Course: Advanced Business Models (Mason Core)”
### `a5d9fb33493e87ea` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=reserve-credit [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: REAL 601 ⟵ “REAL 601 - Fundamentals of Affordable Housing”
  - courses: REAL 602 ⟵ “REAL 602 - Sustainable Real Estate Development”
  - courses: REAL 605 ⟵ “REAL 605 - Policy and Planning of the Built Environment”
  - courses: REAL 615 ⟵ “REAL 615 - Brokerage and Market Analysis”
  - courses: REAL 625 ⟵ “REAL 625 - Financial Analysis and Valuation”
  - courses: REAL 635 ⟵ “REAL 635 - The Development Process”
### `a6ed90a28700a661` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-management-mgmt-human-resources-management [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MGMT 421 ⟵ “MGMT 421 - Advanced Human Resource Management”
  - courses: MGMT 431 ⟵ “MGMT 431 - The Legal Environment for Employee and Labor Relations”
### `a739f9001feb569b` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=non-western-culture [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: ANTH 114 ⟵ “ANTH 114 - Introduction to Cultural Anthropology (Mason Core)”
  - courses: ANTH 300 ⟵ “ANTH 300 - Civilizations”
  - courses: ANTH 302 ⟵ “ANTH 302 - Peoples and Cultures of Latin America (Mason Core)”
  - courses: ANTH 307 ⟵ “ANTH 307 - Ancient Mesoamerica (Mason Core)”
  - courses: ANTH 308 ⟵ “ANTH 308 - Peoples and Cultures of the Middle East (Mason Core)”
  - courses: ANTH 309 ⟵ “ANTH 309 - Peoples and Cultures of India (Mason Core)”
  - courses: ANTH 313 ⟵ “ANTH 313 - Myth, Magic, and Mind (Mason Core)”
  - courses: ANTH 314 ⟵ “ANTH 314 - Zombies”
  - courses: ANTH 317 ⟵ “ANTH 317 - East Asian Cultures (Mason Core)”
  - courses: ANTH 330 ⟵ “ANTH 330 - Peoples and Cultures of Selected Regions: Non-Western”
  - courses: ANTH 332 ⟵ “ANTH 332 - Cross-Cultural Perspectives on Globalization (Mason Core)”
  - courses: ANTH 381 ⟵ “ANTH 381 - Medical Anthropology”
  - courses: ANTH 396 ⟵ “ANTH 396 - Issues in Anthropology: Social Sciences (Mason Core)”
  - courses: ARAB 360 ⟵ “ARAB 360 - Topics in Arabic Cultural Production”
  - courses: ARAB 365 ⟵ “ARAB 365 - Black and Minority Cultures in Arabic Literature (Mason Core)”
  - courses: ARAB 420 ⟵ “ARAB 420 - Survey of Arabic Literature”
  - courses: ARAB 440 ⟵ “ARAB 440 - Topics in Arabic Religious Thought and Texts (Mason Core)”
  - courses: ARTH 203 ⟵ “ARTH 203 - Survey of Asian Art (Mason Core)”
  - courses: ARTH 204 ⟵ “ARTH 204 - Survey of Latin American Art (Mason Core)”
  - courses: ARTH 206 ⟵ “ARTH 206 - Survey of African Art (Mason Core)”
  - courses: ARTH 317 ⟵ “ARTH 317 - The Black Pharaohs: Art and Archaeology of Ancient Nubia (Mason Core)”
  - courses: ARTH 318 ⟵ “ARTH 318 - Art and Archaeology of Ancient Egypt”
  - courses: ARTH 319 ⟵ “ARTH 319 - Art and Archaeology of the Ancient Near East (Mason Core)”
  - courses: ARTH 320 ⟵ “ARTH 320 - Overview of Art of the Islamic World (Mason Core)”
  - courses: ARTH 382 ⟵ “ARTH 382 - Arts of India (Mason Core)”
  - … 15 more rows
### `a9af5b0a9869e105` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-operations-and-supply-chain-management-oscm-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: OSCM 330 ⟵ “OSCM 330 - Service Operations”
  - courses: OSCM 352 ⟵ “OSCM 352 - Management Science”
  - courses: OSCM 430 ⟵ “OSCM 430 - Design Thinking for Innovative Operations”
  - courses: OSCM 435 ⟵ “OSCM 435 - Business Process Analysis and Simulation”
  - courses: OSCM 440 ⟵ “OSCM 440 - Public Sector Operations”
  - courses: OSCM 452 ⟵ “OSCM 452 - Business Forecasting”
  - courses: OSCM 460 ⟵ “OSCM 460 - Management of Product and Process Technologies”
  - courses: OSCM 462 ⟵ “OSCM 462 - Honors Seminar in Operations Management (Topic Varies)”
  - courses: OSCM 465 ⟵ “OSCM 465 - Government Contracting and Procurement”
  - courses: OSCM 490 ⟵ “OSCM 490 - Professional Readiness through Client Projects & Solutioning”
  - courses: OSCM 491 ⟵ “OSCM 491 - Seminar in Operations Management”
  - courses: OSCM 492 ⟵ “OSCM 492 - Internship in Operations and Supply Chain Management”
  - courses: OSCM 499 ⟵ “OSCM 499 - Independent Study in Operations Management”
  - courses: MIS 310 ⟵ “MIS 310 - Database Management Systems”
  - courses: MIS 350 ⟵ “MIS 350 - AI - Assisted Programming for Business Applications”
  - courses: MIS 412 ⟵ “MIS 412 - E-Business Systems Development”
  - courses: MIS 430 ⟵ “MIS 430 - Data Warehousing”
  - courses: MIS 431 ⟵ “MIS 431 - Data Mining for Business Applications (Mason Core)”
  - courses: MIS 432 ⟵ “MIS 432 - Advanced Data Mining”
  - courses: MIS 433 ⟵ “MIS 433 - Programming for Analytics”
  - courses: MIS 436 ⟵ “MIS 436 - AI for Information Systems Applications”
  - courses: GBUS 638 ⟵ “GBUS 638 - Operations Management”
  - courses: MSBA 610 ⟵ “MSBA 610 - Essentials of Business Analytics and AI: From Data Ethics to Data Driven Decision-making”
  - courses: MSBA 615 ⟵ “MSBA 615 - Database Management for Business Analytics”
  - courses: MSBA 618 ⟵ “MSBA 618 - Programming for Business Analytics”
  - … 1 more rows
### `b49398eb5f17cc30` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `ba9f4f352d93e70c` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=social-and-behavioral-sciences [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - section: social-and-behavioral-sciences ⟵ “Social and Behavioral Sciences”
### `c0614f435cad9f8e` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=advanced-standing [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: REAL 602 ⟵ “REAL 602 - Sustainable Real Estate Development”
  - courses: REAL 605 ⟵ “REAL 605 - Policy and Planning of the Built Environment”
  - courses: REAL 615 ⟵ “REAL 615 - Brokerage and Market Analysis”
  - courses: REAL 625 ⟵ “REAL 625 - Financial Analysis and Valuation”
  - courses: REAL 635 ⟵ “REAL 635 - The Development Process”
### `c2009098f4c542bd` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-advocacy-advo-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 227 ⟵ “COMM 227 - Introduction to Political Communication”
  - courses: COMM 300 ⟵ “COMM 300 - Writing and Rhetorical Criticism (Mason Core)”
  - courses: COMM 454 ⟵ “COMM 454 - Free Speech and Ethics (Mason Core)”
  - courses: COMM 459 ⟵ “COMM 459 - Argument and Public Policy”
### `c6a232a487fae837` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-digital-production-and-media-studies-dpms-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 208 ⟵ “COMM 208 - Introduction to Media Production”
  - courses: COMM 302 ⟵ “COMM 302 - Media Theory”
  - courses: COMM 360 ⟵ “COMM 360 - Digital Postproduction”
  - courses: COMM 380 ⟵ “COMM 380 - Media Criticism (Mason Core)”
### `c830a67c0a27b4ea` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-digital-production-and-media-studies-dpms-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: COMM 148 ⟵ “COMM 148 - Podcasting and Radio Workshop I (Digital Production Track)”
  - courses: COMM 310 ⟵ “COMM 310 - Performance for Communication Arts”
  - courses: COMM 347 ⟵ “COMM 347 - Cable TV Programming and Marketing”
  - courses: COMM 348 ⟵ “COMM 348 - Podcasting and Radio Workshop II”
  - courses: COMM 354 ⟵ “COMM 354 - Podcasting Production”
  - courses: COMM 356 ⟵ “COMM 356 - Performance for Digital Production”
  - courses: COMM 358 ⟵ “COMM 358 - Multi-Camera Studio Production”
  - courses: COMM 363 ⟵ “COMM 363 - Media Career Seminar”
  - courses: COMM 364 ⟵ “COMM 364 - Videography”
  - courses: COMM 369 ⟵ “COMM 369 - Multimedia Storytelling (Mason Core)”
  - courses: COMM 397 ⟵ “COMM 397 - Special Topics in Production”
  - courses: COMM 452 ⟵ “COMM 452 - Advanced Portfolio in Media Production”
  - courses: COMM 202 ⟵ “COMM 202 - Media and Society”
  - courses: COMM 350 ⟵ “COMM 350 - Mass Communication and Public Policy”
  - courses: COMM 359 ⟵ “COMM 359 - Digital Media Management”
  - courses: COMM 365 ⟵ “COMM 365 - Gender, Race, and Class in the Media”
  - courses: COMM 367 ⟵ “COMM 367 - Children and Media”
  - courses: COMM 372 ⟵ “COMM 372 - Sports and the Media”
  - courses: COMM 375 ⟵ “COMM 375 - Digital Advertising Strategies”
  - courses: COMM 396 ⟵ “COMM 396 - Special Topics in Media Studies”
  - courses: COMM 435 ⟵ “COMM 435 - Digital Communication”
  - courses: COMM 454 ⟵ “COMM 454 - Free Speech and Ethics (Mason Core)”
### `c8359962c9b423ed` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-management-mgmt-entrepreneurship [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MGMT 451 ⟵ “MGMT 451 - Introduction to Entrepreneurship”
  - courses: MGMT 452 ⟵ “MGMT 452 - Experiential Entrepreneurship”
  - courses: MGMT 454 ⟵ “MGMT 454 - Social Impact and Entrepreneurship”
  - courses: BULE 402 ⟵ “BULE 402 - Commercial Law”
### `c87b55e3bc303fa5` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=co-curricular-requirements-fpwm [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: FNAN 462 ⟵ “FNAN 462 - Honors Seminar in Finance”
### `c9b208662c04f321` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-management-mgmt-management-consulting [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MGMT 412 ⟵ “MGMT 412 - Diversity in Organizations”
  - courses: MGMT 463 ⟵ “MGMT 463 - Negotiations in Organizations”
  - courses: MGMT 464 ⟵ “MGMT 464 - Teamwork and Interpersonal Skills”
### `cd6b820b577a0acf` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-finance-fnan-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: FNAN 311 ⟵ “FNAN 311 - Principles of Investment”
  - courses: FNAN 321 ⟵ “FNAN 321 - Financial Institutions”
  - courses: FNAN 341 ⟵ “FNAN 341 - Introduction to Firm Valuation”
  - courses: FNAN 351 ⟵ “FNAN 351 - Principles of Real Estate”
  - courses: FNAN 401 ⟵ “FNAN 401 - Advanced Financial Management”
  - courses: FNAN 411 ⟵ “FNAN 411 - Investment Analysis and Portfolio Management”
  - courses: FNAN 412 ⟵ “FNAN 412 - Futures and Options Markets”
  - courses: FNAN 421 ⟵ “FNAN 421 - Money and Capital Markets”
  - courses: FNAN 430 ⟵ “FNAN 430 - Empirical Methods in Finance”
  - courses: FNAN 431 ⟵ “FNAN 431 - Venture Capital and Private Financing of Startups”
  - courses: FNAN 432 ⟵ “FNAN 432 - Fixed-Income Securities”
  - courses: FNAN 436 ⟵ “FNAN 436 - Probability Methods for Finance”
  - courses: FNAN 440 ⟵ “FNAN 440 - International Financial Management”
  - courses: FNAN 441 ⟵ “FNAN 441 - Advanced Topics in Firm Valuation”
  - courses: FNAN 444 ⟵ “FNAN 444 - Socially Responsible Finance”
  - courses: FNAN 451 ⟵ “FNAN 451 - Real Estate Finance”
  - courses: FNAN 454 ⟵ “FNAN 454 - Real Estate Development and Investment Fund”
  - courses: FNAN 462 ⟵ “FNAN 462 - Honors Seminar in Finance”
  - courses: FNAN 472 ⟵ “FNAN 472 - Fintech and Blockchain in Finance”
  - courses: FNAN 477 ⟵ “FNAN 477 - Student Managed Investment Fund (Mason Core)”
  - courses: FNAN 483 ⟵ “FNAN 483 - Ethical and Professional Standards in Finance”
  - courses: FNAN 491 ⟵ “FNAN 491 - Special Topics in Finance”
  - courses: FNAN 492 ⟵ “FNAN 492 - Internship in Finance”
  - courses: FNAN 498 ⟵ “FNAN 498 - RS: Contemporary Topics in Finance (Mason Core)”
  - courses: FNAN 499 ⟵ “FNAN 499 - Independent Study”
  - … 5 more rows
### `d0179edc2db6a6ae` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-management-mgmt-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MGMT 313 ⟵ “MGMT 313 - Organizational Behavior (Mason Core)”
  - courses: MGMT 321 ⟵ “MGMT 321 - Introduction to Human Resource Management”
### `d129eaf32b83c126` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-accounting-acct-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: ACCT 370 ⟵ “ACCT 370 - International Accounting”
  - courses: ACCT 372 ⟵ “ACCT 372 - Financial Statement Analysis”
  - courses: ACCT 390 ⟵ “ACCT 390 - Introduction to Financial Planning and Wealth Management”
  - courses: ACCT 408 ⟵ “ACCT 408 - Taxes Insurance and Risk Management”
  - courses: ACCT 411 ⟵ “ACCT 411 - Advanced Managerial Accounting”
  - courses: ACCT 433 ⟵ “ACCT 433 - Advanced Financial Accounting”
  - courses: ACCT 441 ⟵ “ACCT 441 - Estate Planning”
  - courses: ACCT 451 ⟵ “ACCT 451 - Advanced Federal Taxation”
  - courses: ACCT 462 ⟵ “ACCT 462 - Honors Seminar in Accounting”
  - courses: ACCT 472 ⟵ “ACCT 472 - Government and Not-for-Profit Accounting”
  - courses: ACCT 491 ⟵ “ACCT 491 - Seminar in Accounting”
  - courses: ACCT 492 ⟵ “ACCT 492 - Internship in Accounting”
  - courses: ACCT 499 ⟵ “ACCT 499 - Independent Study”
  - courses: BULE 402 ⟵ “BULE 402 - Commercial Law”
### `d177f3068c054ecc` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=co-curricular-requirements-mis [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MIS 462 ⟵ “MIS 462 - Honors Seminar in Management Information Systems (Topic Varies)”
### `d27c162ee7b2bd23` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-marketing-mktg-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MKTG 312 ⟵ “MKTG 312 - Consumer Behavior”
  - courses: MKTG 351 ⟵ “MKTG 351 - Marketing Research”
  - courses: MKTG 471 ⟵ “MKTG 471 - Marketing Management (Mason Core)”
### `d5e00782d9e7f3d7` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-business-analytics-busa-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MIS 310 ⟵ “MIS 310 - Database Management Systems”
  - courses: MIS 430 ⟵ “MIS 430 - Data Warehousing”
  - courses: MIS 431 ⟵ “MIS 431 - Data Mining for Business Applications (Mason Core)”
  - courses: MIS 433 ⟵ “MIS 433 - Programming for Analytics”
### `d7df2ed7c3bb2c41` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=core-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 200 ⟵ “COMM 200 - Communication Theory”
  - courses: COMM 305 ⟵ “COMM 305 - Foundations of Intercultural Communication (Mason Core)”
  - courses: COMM 320 ⟵ “COMM 320 - Digital Innovations in Professional Communication (Mason Core)”
  - courses: COMM 400 ⟵ “COMM 400 - Research Methods in Communication”
### `d9e487616fdd0e36` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-public-relations-strategic-communication-prsc-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 204 ⟵ “COMM 204 - Introduction to Public Relations and Strategic Communication”
  - courses: COMM 308 ⟵ “COMM 308 - Writing for Public Relations and Strategic Communication (Mason Core)”
  - courses: COMM 325 ⟵ “COMM 325 - AI-enhanced Research Analytics for Strategic Communication”
  - courses: COMM 410 ⟵ “COMM 410 - Strategic Communication Campaigns”
### `dd2133fe6deb1cd5` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=bam-ms-accounting-pathway-requirements-reserve-credit-courses-up-to-6-credits [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: ACCT 611 ⟵ “ACCT 611 - Advanced Issues in Managerial Accounting”
  - courses: ACCT 621 ⟵ “ACCT 621 - GovCon Acquisition Regulations and Reporting”
  - courses: ACCT 636 ⟵ “ACCT 636 - Fraud Examination”
  - courses: ACCT 661 ⟵ “ACCT 661 - Advanced Accounting Analytics I”
  - courses: ACCT 665 ⟵ “ACCT 665 - Advanced Accounting Analytics II”
  - courses: ACCT 672 ⟵ “ACCT 672 - Governmental and Nonprofit Accounting”
  - courses: ACCT 673 ⟵ “ACCT 673 - Advanced Accounting Information Systems”
### `e13785e960e4fe98` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-operations-and-supply-chain-management-oscm-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: OSCM 320 ⟵ “OSCM 320 - Supply Chain Management in a Global Economy”
  - courses: OSCM 456 ⟵ “OSCM 456 - Quality Management (Mason Core)”
  - courses: OSCM 493 ⟵ “OSCM 493 - Management of Technology Projects”
### `e650302ea41d3155` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=courses-limited-to-10-credits [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 140 ⟵ “COMM 140 - Forensics Seminar I”
  - courses: COMM 141 ⟵ “COMM 141 - Forensics Seminar II”
  - courses: COMM 142 ⟵ “COMM 142 - Debate Seminar I”
  - courses: COMM 143 ⟵ “COMM 143 - Debate Seminar II”
  - courses: COMM 145 ⟵ “COMM 145 - Newspaper Workshop I”
  - courses: COMM 148 ⟵ “COMM 148 - Podcasting and Radio Workshop I”
  - courses: COMM 340 ⟵ “COMM 340 - Forensics Seminar III”
  - courses: COMM 341 ⟵ “COMM 341 - Forensics Seminar IV”
  - courses: COMM 342 ⟵ “COMM 342 - Debate Seminar III”
  - courses: COMM 343 ⟵ “COMM 343 - Debate Seminar IV”
  - courses: COMM 345 ⟵ “COMM 345 - Newspaper Workshop II”
  - courses: COMM 348 ⟵ “COMM 348 - Podcasting and Radio Workshop II”
  - courses: COMM 398 ⟵ “COMM 398 - Research Practicum in Communication”
  - courses: COMM 450 ⟵ “COMM 450 - Internship in Communication”
  - courses: COMM 451 ⟵ “COMM 451 - Facilitating Communication Education”
  - courses: COMM 452 ⟵ “COMM 452 - Advanced Portfolio in Media Production”
  - courses: COMM 491 ⟵ “COMM 491 - RS: Honors Research Project in Communication”
  - courses: COMM 498 ⟵ “COMM 498 - RS: Research Projects in Communication”
  - courses: COMM 499 ⟵ “COMM 499 - Independent Study in Communication”
### `e9f272c60227d071` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - section: electives ⟵ “Electives”
### `f3cb21ab0b47fb83` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=philosophy-or-religious-studies [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - section: philosophy-or-religious-studies ⟵ “Philosophy or Religious Studies”
### `f6d77d728e36605a` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-management-information-systems-mis-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MIS 310 ⟵ “MIS 310 - Database Management Systems”
  - courses: MIS 320 ⟵ “MIS 320 - Networks and Security”
  - courses: MIS 330 ⟵ “MIS 330 - Systems Analysis and Design (Mason Core)”
### `fc81acf711ebf8c9` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=business-core [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: ACCT 303 ⟵ “ACCT 303 - Accounting for Decision Making”
  - courses: BULE 303 ⟵ “BULE 303 - Legal Environment of Business”
  - courses: BUS 303 ⟵ “BUS 303 - Develop Professional Skills II: Advanced Elements”
  - courses: FNAN 303 ⟵ “FNAN 303 - Financial Management”
  - courses: MGMT 303 ⟵ “MGMT 303 - Principles of Management”
  - courses: MIS 303 ⟵ “MIS 303 - Introduction to Business Information Systems (Mason Core)”
  - courses: MKTG 303 ⟵ “MKTG 303 - Principles of Marketing”
  - courses: OSCM 303 ⟵ “OSCM 303 - Operations Management”
### `fd69e492daffb8f3` George Mason University — degree_requirements 2026-27 · program_key=business-bs · requirement_key=concentration-in-marketing-mktg-electives [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/business/business-bs/ (sha256 909229944926)
- issues: requirement_groups_skipped
  - courses: MKTG 307 ⟵ “MKTG 307 - Federal Government Marketing”
  - courses: MKTG 310 ⟵ “MKTG 310 - Consultative Selling”
  - courses: MKTG 311 ⟵ “MKTG 311 - Sales Management”
  - courses: MKTG 313 ⟵ “MKTG 313 - Advertising and Marketing Communications”
  - courses: MKTG 315 ⟵ “MKTG 315 - Digital Marketing in the Age of AI”
  - courses: MKTG 316 ⟵ “MKTG 316 - Social Media Marketing Strategy”
  - courses: MKTG 332 ⟵ “MKTG 332 - Retailing and E-Commerce Management”
  - courses: MKTG 333 ⟵ “MKTG 333 - Business to Business Marketing”
  - courses: MKTG 335 ⟵ “MKTG 335 - Strategic Brand Management”
  - courses: MKTG 352 ⟵ “MKTG 352 - Marketing Analytics: AI, Data, and Models”
  - courses: MKTG 353 ⟵ “MKTG 353 - New Product Development”
  - courses: MKTG 355 ⟵ “MKTG 355 - Direct Marketing”
  - courses: MKTG 407 ⟵ “MKTG 407 - Global Marketing”
  - courses: MKTG 415 ⟵ “MKTG 415 - GenAI Applications in Marketing”
  - courses: MKTG 437 ⟵ “MKTG 437 - Fashion Marketing”
  - courses: MKTG 450 ⟵ “MKTG 450 - Marketing Consulting”
  - courses: MKTG 455 ⟵ “MKTG 455 - Ethnic and Multicultural Marketing”
  - courses: MKTG 462 ⟵ “MKTG 462 - Honors Seminar in Marketing (Topic Varies)”
  - courses: MKTG 481 ⟵ “MKTG 481 - RS: Marketing in the Nonprofit Sector”
  - courses: MKTG 491 ⟵ “MKTG 491 - Seminar in Marketing”
  - courses: MKTG 492 ⟵ “MKTG 492 - Internship in Marketing”
  - courses: MKTG 499 ⟵ “MKTG 499 - Independent Study”
### `fe3db6246c781606` George Mason University — degree_requirements 2026-27 · program_key=communication-ba · requirement_key=concentration-in-communication-studies-coms-required-courses [new] (labeled_in_source)
- source: https://catalog.gmu.edu/colleges-schools/humanities-social-sciences/communication/communication-ba/ (sha256 17d5fe47bf84)
- issues: requirement_groups_skipped
  - courses: COMM 300 ⟵ “COMM 300 - Writing and Rhetorical Criticism (Mason Core)”
  - courses: COMM 301 ⟵ “COMM 301 - Interpersonal Communication: Theory to Practice (core course)”
  - courses: COMM 318 ⟵ “COMM 318 - Persuasion”
  - courses: COMM 335 ⟵ “COMM 335 - Organizational Communication (core course)”
### `b4915eda976d4cb3` James Madison University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.jmu.edu/financialaid/learn/finaid-appeals.shtml (sha256 8255f4ddc997)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “In order to submit a Professional Judgment Request a student would need a FAFSA and be meeting the eligibility requirements for financial aid.”
  - sentence: professional_judgment ⟵ “A letter may also be mailed to: Office of Financial Aid & Scholarships Professional Judgement Committee MSC 3519 738 South Mason St.”
### `f74c917dc7216eea` James Madison University — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.jmu.edu/admissions/fastfacts.shtml (sha256 5586e1938dbe)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees*: 32576 ⟵ “Tuition and Fees* | $14,768 | $32,576”
  - column:Housing and Food: 15220 ⟵ “Housing and Food | $15,220 | $15,220”
  - column:TOTAL: 47796 ⟵ “TOTAL | $29,988 | $47,796”
### `f7de31c09f6c8988` James Madison University — costs 2026-27 · residency=in_state [same] (source_unlabeled)
- source: https://www.jmu.edu/about/fact-and-figures.shtml (sha256 92c3343fdd5e)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees*: 14768 ⟵ “Tuition and Fees* | $14,768 | $32,576”
  - column:Housing and Food: 15220 ⟵ “Housing and Food | $15,220 | $15,220”
  - column:TOTAL: 29988 ⟵ “TOTAL | $29,988 | $47,796”
### `a671af8c0b639738` Liberty University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.liberty.edu/student-financial-services/eligibility-and-enrollment/ (sha256 c1eac2ead3ab)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If any appeal supporting documents are requested when you complete the online Financial Aid SAP appeal form, you will be prompted to upload the documents while completing and submitting the form in SSB – Financial Aid (All documents needing signatures must be signed).”
  - sentence: sap_appeal ⟵ “Decision: A decision to approve or deny your appeal will be made by the Financial Aid Committee within one week of the receipt of your Financial Aid SAP appeal form and any required additional documents.”
### `085eaa705f04e080` Old Dominion University — academic_programs 2026-27 · program_key=special-education-with-a-major-in-special-education-adapted-curriculum-k-12-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/special-education-adapted-curriculum-k12-bs/ (sha256 3739387c8fb1)
- issues: requirement_groups_skipped
- checks: {"courses": 18, "groups": 2, "groups_skipped": 3}
  - program_name: Special Education with a Major in Special Education Adapted Curriculum K-12 (BS) ⟵ “Special Education with a Major in Special Education Adapted Curriculum K-12 (BS) < Old Dominion University”
### `0a7d7b11e29c953f` Old Dominion University — academic_programs 2026-27 · program_key=african-american-and-african-studies-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-ba/ (sha256 33b79ef74f7b)
- issues: requirement_groups_skipped
- checks: {"courses": 45, "groups": 4, "groups_skipped": 2}
  - program_name: African American and African Studies (BA) ⟵ “African American and African Studies (BA) < Old Dominion University”
### `0da4b15ed5788ab7` Old Dominion University — academic_programs 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-industrial-technology-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-industrial-technology-bs/ (sha256 201fc53177e7)
- issues: requirement_groups_skipped
- checks: {"courses": 22, "groups": 4, "groups_skipped": 2}
  - program_name: Occupational and Technical Studies with a Major in Industrial Technology (BS) ⟵ “Occupational and Technical Studies with a Major in Industrial Technology (BS) < Old Dominion University”
### `10386fc40f494182` Old Dominion University — academic_programs 2026-27 · program_key=special-education-with-a-major-in-early-intervention-early-childhood-special-edu [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/special-education-early-intervention-early-childhood-special-education-birth-5-bs/ (sha256 0dce08dad768)
- issues: requirement_groups_skipped
- checks: {"courses": 21, "groups": 2, "groups_skipped": 3}
  - program_name: Special Education with a Major in Early Intervention/Early Childhood Special Education (Birth-5) (BS) ⟵ “Special Education with a Major in Early Intervention/Early Childhood Special Education (Birth-5) (BS) < Old Dominion University”
### `1232129d8844ab64` Old Dominion University — academic_programs 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
- checks: {"courses": 90, "groups": 16, "groups_skipped": 3}
  - program_name: Communication with a Major in Strategic Communication and Journalism (BA) ⟵ “Communication with a Major in Strategic Communication and Journalism (BA) < Old Dominion University”
### `128c2741734c1358` Old Dominion University — academic_programs 2026-27 · program_key=physical-education-with-a-major-in-coaching-and-physical-activity-leadership-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/physical-education-coaching-and-physical-activity-leadership-bs/ (sha256 62cb31f9a532)
- issues: requirement_groups_skipped
- checks: {"courses": 23, "groups": 1, "groups_skipped": 2}
  - program_name: Physical Education with a Major in Coaching and Physical Activity Leadership (BS) ⟵ “Physical Education with a Major in Coaching and Physical Activity Leadership (BS) < Old Dominion University”
### `159f1080903ff47b` Old Dominion University — academic_programs 2026-27 · program_key=physical-education-with-a-major-in-prek-12-health-and-physical-education-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/physical-education-prek-12-health-bs/ (sha256 6f1dba08ef11)
- issues: requirement_groups_skipped
- checks: {"courses": 24, "groups": 2, "groups_skipped": 2}
  - program_name: Physical Education with a Major in PreK-12 Health and Physical Education (BS) ⟵ “Physical Education with a Major in PreK-12 Health and Physical Education (BS) < Old Dominion University”
### `2c01b534d9a0133c` Old Dominion University — academic_programs 2026-27 · program_key=music-with-a-major-in-jazz-studies-bm [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/music/jazz-studies-bm/ (sha256 93a26dd823ef)
- issues: requirement_groups_skipped
- checks: {"courses": 34, "groups": 2, "groups_skipped": 3}
  - program_name: Music with a Major in Jazz Studies (BM) ⟵ “Music with a Major in Jazz Studies (BM) < Old Dominion University”
### `2c547d4f9d60d099` Old Dominion University — academic_programs 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-ba/ (sha256 359f7abf5fe7)
- issues: requirement_groups_skipped
- checks: {"courses": 31, "groups": 5, "groups_skipped": 2}
  - program_name: Interdisciplinary Studies with a Major in Women's and Gender Studies (BA) ⟵ “Interdisciplinary Studies with a Major in Women's and Gender Studies (BA) < Old Dominion University”
### `2e940b11400df319` Old Dominion University — academic_programs 2026-27 · program_key=sport-management-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/sport-management-bs/ (sha256 3de3b3afb84d)
- issues: requirement_groups_skipped
- checks: {"courses": 16, "groups": 2, "groups_skipped": 2}
  - program_name: Sport Management (BS) ⟵ “Sport Management (BS) < Old Dominion University”
### `397ab89c12f84459` Old Dominion University — academic_programs 2026-27 · program_key=women-s-studies-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/womens-studies/womens-studies-bs/ (sha256 0c3f4590054d)
- issues: requirement_groups_skipped
- checks: {"courses": 29, "groups": 2, "groups_skipped": 3}
  - program_name: Women's Studies (BS) ⟵ “Women's Studies (BS) < Old Dominion University”
### `4f77f35a013fad02` Old Dominion University — academic_programs 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
- checks: {"courses": 72, "groups": 13, "groups_skipped": 3}
  - program_name: Communication with a Major in Cinema Screenwriting and Studies (BA) ⟵ “Communication with a Major in Cinema Screenwriting and Studies (BA) < Old Dominion University”
### `57311863cc8bcbe8` Old Dominion University — academic_programs 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
- checks: {"courses": 72, "groups": 12, "groups_skipped": 3}
  - program_name: Communication with a Major in Cinema Screenwriting and Studies (BS) ⟵ “Communication with a Major in Cinema Screenwriting and Studies (BS) < Old Dominion University”
### `5ace93b00379614d` Old Dominion University — academic_programs 2026-27 · program_key=career-and-technical-education-with-a-major-in-marketing-education-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-marketing-bs/ (sha256 c38ad1d36dc9)
- issues: requirement_groups_skipped
- checks: {"courses": 26, "groups": 4, "groups_skipped": 4}
  - program_name: Career and Technical Education with a Major in Marketing Education (BS) ⟵ “Career and Technical Education with a Major in Marketing Education (BS) < Old Dominion University”
### `61bbdd68c36d54e1` Old Dominion University — academic_programs 2026-27 · program_key=park-recreation-and-tourism-studies-with-a-major-in-tourism-and-hospitality-mana [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/park-recreation-tourism-studies-hospitality-management-bs/ (sha256 ac6ca2491f1c)
- issues: requirement_groups_skipped
- checks: {"courses": 15, "groups": 2, "groups_skipped": 3}
  - program_name: Park, Recreation and Tourism Studies with a Major in Tourism and Hospitality Management (BS) ⟵ “Park, Recreation and Tourism Studies with a Major in Tourism and Hospitality Management (BS) < Old Dominion University”
### `711522189bd82e5a` Old Dominion University — academic_programs 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-fashion-merchandising-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-fashion-merchandising-bs/ (sha256 8cf2795df528)
- issues: requirement_groups_skipped
- checks: {"courses": 30, "groups": 1, "groups_skipped": 2}
  - program_name: Occupational and Technical Studies with a Major in Fashion Merchandising (BS) ⟵ “Occupational and Technical Studies with a Major in Fashion Merchandising (BS) < Old Dominion University”
### `75242265d1c03d89` Old Dominion University — academic_programs 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
- checks: {"courses": 78, "groups": 18, "groups_skipped": 2}
  - program_name: Interdisciplinary Studies with a Major in Asian Studies (BA) ⟵ “Interdisciplinary Studies with a Major in Asian Studies (BA) < Old Dominion University”
### `7e28d6857f1b7112` Old Dominion University — academic_programs 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-training-specialist-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-training-specialist-bs/ (sha256 e9e73afa7e78)
- issues: requirement_groups_skipped
- checks: {"courses": 17, "groups": 2, "groups_skipped": 2}
  - program_name: Occupational and Technical Studies with a Major in Training Specialist (BS) ⟵ “Occupational and Technical Studies with a Major in Training Specialist (BS) < Old Dominion University”
### `81cf1f617b162436` Old Dominion University — academic_programs 2026-27 · program_key=world-languages-and-cultures-with-a-major-in-japanese-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/world-languages-cultures/world-languages-cultures-japanese-ba/ (sha256 fa2e03649f15)
- issues: requirement_groups_skipped
- checks: {"courses": 5, "groups": 2, "groups_skipped": 4}
  - program_name: World Languages and Cultures with a Major in Japanese (BA) ⟵ “World Languages and Cultures with a Major in Japanese (BA) < Old Dominion University”
### `88a9e80886a03724` Old Dominion University — academic_programs 2026-27 · program_key=environmental-health-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/joint-school-public-health/epidemiology-biostatistics-and-environmental-health/environmental-health-bs/ (sha256 daea2f065cee)
- issues: requirement_groups_skipped
- checks: {"courses": 27, "groups": 2, "groups_skipped": 2}
  - program_name: Environmental Health (BS) ⟵ “Environmental Health (BS) < Old Dominion University”
### `8910edd3e79e0ab6` Old Dominion University — academic_programs 2026-27 · program_key=english-with-a-major-in-technical-and-professional-writing-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-technical-and-professional-writing-ba/ (sha256 24304c241949)
- issues: requirement_groups_skipped
- checks: {"courses": 50, "groups": 5, "groups_skipped": 3}
  - program_name: English with a Major in Technical and Professional Writing (BA) ⟵ “English with a Major in Technical and Professional Writing (BA) < Old Dominion University”
### `955af4b31fec91ab` Old Dominion University — academic_programs 2026-27 · program_key=park-recreation-and-tourism-studies-with-a-major-in-park-and-recreation-manageme [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/park-recreation-tourism-studies-bs/ (sha256 5679c450cf75)
- issues: requirement_groups_skipped
- checks: {"courses": 14, "groups": 2, "groups_skipped": 3}
  - program_name: Park, Recreation and Tourism Studies with a Major in Park and Recreation Management (BS) ⟵ “Park, Recreation and Tourism Studies with a Major in Park and Recreation Management (BS) < Old Dominion University”
### `962b934b7bc8cdbd` Old Dominion University — academic_programs 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
- checks: {"courses": 90, "groups": 15, "groups_skipped": 3}
  - program_name: Communication with a Major in Strategic Communication and Journalism (BS) ⟵ “Communication with a Major in Strategic Communication and Journalism (BS) < Old Dominion University”
### `99cb1a05432a047f` Old Dominion University — academic_programs 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-general-studies-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-general-studies-bs/ (sha256 616940b1bd39)
- issues: requirement_groups_skipped
- checks: {"courses": 3, "groups": 1, "groups_skipped": 4}
  - program_name: Interdisciplinary Studies with a Major in General Studies (BS) ⟵ “Interdisciplinary Studies with a Major in General Studies (BS) < Old Dominion University”
### `a44b41e4907a08a3` Old Dominion University — academic_programs 2026-27 · program_key=women-s-studies-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/womens-studies/womens-studies-ba/ (sha256 abf03dc3b73c)
- issues: requirement_groups_skipped
- checks: {"courses": 30, "groups": 2, "groups_skipped": 3}
  - program_name: Women's Studies (BA) ⟵ “Women's Studies (BA) < Old Dominion University”
### `af1a92e3b02c3842` Old Dominion University — academic_programs 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-bs/ (sha256 a576d3c1b66a)
- issues: requirement_groups_skipped
- checks: {"courses": 29, "groups": 5, "groups_skipped": 2}
  - program_name: Interdisciplinary Studies with a Major in Women's and Gender Studies (BS) ⟵ “Interdisciplinary Studies with a Major in Women's and Gender Studies (BS) < Old Dominion University”
### `b3793baefaf9c755` Old Dominion University — academic_programs 2026-27 · program_key=career-and-technical-education-with-a-major-in-technology-education-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-technology-bs/ (sha256 96e93c2cb7e2)
- issues: requirement_groups_skipped
- checks: {"courses": 25, "groups": 4, "groups_skipped": 4}
  - program_name: Career and Technical Education with a Major in Technology Education (BS) ⟵ “Career and Technical Education with a Major in Technology Education (BS) < Old Dominion University”
### `c0532a57faaa8c37` Old Dominion University — academic_programs 2026-27 · program_key=asian-studies-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
- checks: {"courses": 57, "groups": 17, "groups_skipped": 2}
  - program_name: Asian Studies (BA) ⟵ “Asian Studies (BA) < Old Dominion University”
### `c52b2de208e10e76` Old Dominion University — academic_programs 2026-27 · program_key=exercise-science-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/health-sciences/exercise-science/exercise-science-bs/ (sha256 39f7d122aeba)
- issues: requirement_groups_skipped
- checks: {"courses": 19, "groups": 3, "groups_skipped": 4}
  - program_name: Exercise Science (BS) ⟵ “Exercise Science (BS) < Old Dominion University”
### `c709b2bae21903ec` Old Dominion University — academic_programs 2026-27 · program_key=speech-language-pathology-and-audiology-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/health-sciences/speech-language-pathology/speech-language-pathology-audiology-bs/ (sha256 abcf5727ca35)
- issues: requirement_groups_skipped
- checks: {"courses": 17, "groups": 1, "groups_skipped": 2}
  - program_name: Speech-Language Pathology and Audiology (BS) ⟵ “Speech-Language Pathology and Audiology (BS) < Old Dominion University”
### `cc0a84268b9c7052` Old Dominion University — academic_programs 2026-27 · program_key=special-education-with-a-major-in-special-education-general-curriculum-k-12-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/special-education-general-curriculum-k12-bs/ (sha256 f33ea5dcbf71)
- issues: requirement_groups_skipped
- checks: {"courses": 16, "groups": 2, "groups_skipped": 3}
  - program_name: Special Education with a Major in Special Education General Curriculum K-12 (BS) ⟵ “Special Education with a Major in Special Education General Curriculum K-12 (BS) < Old Dominion University”
### `d1eaeade888a4b5b` Old Dominion University — academic_programs 2026-27 · program_key=data-science-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-bs/ (sha256 bea76769d765)
- issues: requirement_groups_skipped
- checks: {"courses": 78, "groups": 5, "groups_skipped": 2}
  - program_name: Data Science (BS) ⟵ “Data Science (BS) < Old Dominion University”
### `e28d77fba8b4bd99` Old Dominion University — academic_programs 2026-27 · program_key=english-with-a-major-in-applied-linguistics-ba [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-applied-linguistics-ba/ (sha256 387330ef24ca)
- issues: requirement_groups_skipped
- checks: {"courses": 51, "groups": 5, "groups_skipped": 3}
  - program_name: English with a Major in Applied Linguistics (BA) ⟵ “English with a Major in Applied Linguistics (BA) < Old Dominion University”
### `e56d182a050f3a31` Old Dominion University — academic_programs 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-supply-chain-and-maritime-logistics-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-supply-chain-and-maritime-logistics-bs/ (sha256 0c18deed219f)
- issues: requirement_groups_skipped
- checks: {"courses": 40, "groups": 6, "groups_skipped": 3}
  - program_name: Interdisciplinary Studies with a Major in Supply Chain and Maritime Logistics (BS) ⟵ “Interdisciplinary Studies with a Major in Supply Chain and Maritime Logistics (BS) < Old Dominion University”
### `e60ee9df3ab42995` Old Dominion University — academic_programs 2026-27 · program_key=african-american-and-african-studies-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-bs/ (sha256 af978b675a37)
- issues: requirement_groups_skipped
- checks: {"courses": 45, "groups": 4, "groups_skipped": 2}
  - program_name: African American and African Studies (BS) ⟵ “African American and African Studies (BS) < Old Dominion University”
### `eb390a17e05b445c` Old Dominion University — academic_programs 2026-27 · program_key=early-childhood-education-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/teaching-learning/early-childhood-education-bs/ (sha256 6ccb7afd4afa)
- issues: requirement_groups_skipped
- checks: {"courses": 22, "groups": 2, "groups_skipped": 2}
  - program_name: Early Childhood Education (BS) ⟵ “Early Childhood Education (BS) < Old Dominion University”
### `f1cf27aa418c4d93` Old Dominion University — academic_programs 2026-27 · program_key=chemistry-with-a-major-in-chemical-forensic-science-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/sciences/chemistry-biochemistry/chemistry-chemical-forensic-science-bs/ (sha256 2f424b98ebb5)
- issues: requirement_groups_skipped
- checks: {"courses": 20, "groups": 3, "groups_skipped": 3}
  - program_name: Chemistry with a Major in Chemical Forensic Science (BS) ⟵ “Chemistry with a Major in Chemical Forensic Science (BS) < Old Dominion University”
### `f33b8266b23f0cbf` Old Dominion University — academic_programs 2026-27 · program_key=data-science-with-a-major-in-data-for-a-human-world-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-data-for-a-human-world-bs/ (sha256 e583b8d1f70b)
- issues: requirement_groups_skipped
- checks: {"courses": 29, "groups": 3, "groups_skipped": 2}
  - program_name: Data Science with a Major in Data for a Human World (BS) ⟵ “Data Science with a Major in Data for a Human World (BS) < Old Dominion University”
### `fea54a98985119e2` Old Dominion University — academic_programs 2026-27 · program_key=criminal-justice-with-a-major-in-cybercriminology-bs [same] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/sociology-criminal-justice/cybercriminology-bs/ (sha256 efc94ead6d8d)
- issues: requirement_groups_skipped
- checks: {"courses": 29, "groups": 1, "groups_skipped": 2}
  - program_name: Criminal Justice with a Major in Cybercriminology (BS) ⟵ “Criminal Justice with a Major in Cybercriminology (BS) < Old Dominion University”
### `c60448fe6d55ef76` Old Dominion University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.odu.edu/financial-aid/manage/sap (sha256 a5a3bce4ec0f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “The deadlines are listed on the SAP appeal form.”
  - sentence: sap_appeal ⟵ “Use the SATISFACTORY ACADEMIC PROGRESS APPEAL FORM to submit your appeal.”
  - sentence: sap_appeal ⟵ “Students awaiting a response from the SAP Appeal Review Committee are responsible for paying their tuition and other fees by the payment deadline to avoid late and collection fees.”
  - sentence: sap_appeal ⟵ “SAP Appeal Form Re-establishing eligibility Students may re-establish their eligibility for financial assistance by achieving the satisfactory progress standards.”
### `f0fd8603166d6422` Old Dominion University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.odu.edu/financial-aid/manage/sap (sha256 a5a3bce4ec0f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “The University will consider appeals for uncontrollable events, students having trouble adjusting to college, special circumstances that happen in a student's life such as death of a family member, student illness, transition to college issues, being called to the military, etc.”
  - sentence: need_based_special_circumstances ⟵ “Other special circumstance beyond your control (transition that may lead to depression, anxiety, and other problems that can be documented, divorce/separation, natural disaster, extreme change in financial or legal circumstances, etc.) Documentation or evidence that supports the reason(s) must be included with your appeal.”
### `5fcc512dd5d5e7b4` Old Dominion University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.odu.edu/academics/academic-records/score-analysis/ap-ib (sha256 d7e60dda37dc)
- issues: rows_without_score
- checks: {"distinct_exams": 36, "equivalencies": 56, "rows_without_score": 1}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARTH 121A | 3”
  - equivalencies[AP-ART-HISTORY|4, 5]:  ⟵ “Art History | 4, 5 | ARTH 211 & 212 or ARTH 121A & 1ELE | 6”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “2-D Art & Design | 3, 4, 5 | ARTS 202 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, 5]:  ⟵ “3-D Art & Design | 3, 4, 5 | ARTS 203 | 3”
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “Drawing | 3, 4, 5 | ARTS 231 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 105N, or BIOL 106N, or BIOL 110N & 111N, or BIOL 112N & 113N, or BIOL 117N & 118N | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 121N & 122N | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, 5]:  ⟵ “Computer Science A | 3, 4, 5 | CS 151 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CS 1ELE | 3”
  - equivalencies[AP-MACROECONOMICS|3, 4, 5]:  ⟵ “Economics: Macro | 3, 4, 5 | ECON 201S | 3”
  - equivalencies[AP-MICROECONOMICS|3, 4, 5]:  ⟵ “Economics: Micro | 3, 4, 5 | ECON 202S | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3, 4, 5]:  ⟵ “English Language & Composition | 3, 4, 5 | ENGL 110C | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, 5]:  ⟵ “English Literature & Composition | 3, 4, 5 | ENGL 112L | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3, 4, 5]:  ⟵ “Environmental Science | 3, 4, 5 | BIOL 110N & 111N | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|3,4]:  ⟵ “European History | 3,4 | HIST 102H | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|5]:  ⟵ “European History | 5 | HIST 102H & INTP 1REQ | 6”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | 111F | 6”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture | 4 | 212F | 6”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language & Culture | 5 | 212F & 3ELE | 9”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | FR 201 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language & Culture | 4 | FR 201 & 202 | 6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture | 5 | FR 202 & 3ELE | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture | 3 | GER 201 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language & Culture | 4 | GER 201 & 202 | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language & Culture | 5 | GER 202 & 3ELE | 6”
  - … 31 more rows
### `0061c6828ec11745` Old Dominion University — degree_requirements 2026-27 · program_key=early-childhood-education-bs · requirement_key=early-childhood-education-major-major-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/teaching-learning/early-childhood-education-bs/ (sha256 6ccb7afd4afa)
- issues: requirement_groups_skipped
  - courses: GEOG 100S ⟵ “GEOG 100S - Human Geography”
  - courses: LIBS 110G ⟵ “LIBS 110G - Information Literacy for the Digital Age”
  - courses: STAT 130M ⟵ “STAT 130M - Elementary Statistics”
  - courses: HPE 327 ⟵ “HPE 327 - Teaching of Health and Physical Education, Pre-K-8”
  - courses: MATH 302 ⟵ “MATH 302 - Geometry”
  - courses: TLED 320 ⟵ “TLED 320 - Perspectives on the Young Child and the Family”
  - courses: TLED 328 ⟵ “TLED 328 - Observation and Assessment in Early Childhood”
  - courses: TLED 330 ⟵ “TLED 330 - The Arts in Early Childhood and Elementary Education”
  - courses: TLED 337 ⟵ “TLED 337 - Literature for Young Children”
  - courses: TLED 338 ⟵ “TLED 338 - Integrated Methods & Curriculum in Early Childhood Ed: Birth-Pre-K”
  - courses: TLED 483 ⟵ “TLED 483 - Seminar in Teacher Education **”
  - courses: TLED 487 ⟵ “TLED 487 - Teacher Candidate Internship for Early Childhood Education **”
  - courses: TLED 492 ⟵ “TLED 492 - Integrating Instruction: Mathematics and Science Across the Early Childhood Curriculum”
  - courses: TLED 493 ⟵ “TLED 493 - Integrating Literacy and Social Studies Across the PreK - 3 Curriculum”
### `00891e756b4c84a7` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-bs · requirement_key=women-s-and-gender-studies-major-women-s-and-gender-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-bs/ (sha256 a576d3c1b66a)
- issues: requirement_groups_skipped
  - courses: WGS 301 ⟵ “WGS 301 - Feminist Foundations”
  - courses: WGS/QUST 302W ⟵ “WGS/QUST 302W - Dimensions of Diversity: Intersectionality Among Women”
  - courses: WGS/QUST 303 ⟵ “WGS/QUST 303 - Queer Studies”
  - courses: WGS 304 ⟵ “WGS 304 - Gender and Sexuality in Film”
  - courses: WGS/QUST 305 ⟵ “WGS/QUST 305 - Queer Literature”
  - courses: WGS 306 ⟵ “WGS 306 - Women, the Environment, and Climate Change”
  - courses: WGS 368 ⟵ “WGS 368 - Internship”
  - courses: WGS 390T ⟵ “WGS 390T - Women, Gender, and Technology Worldwide”
  - courses: WGS 395 ⟵ “WGS 395 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 396 ⟵ “WGS 396 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 401W ⟵ “WGS 401W - Women: A Global Perspective”
  - courses: WGS/QUST 402 ⟵ “WGS/QUST 402 - Feminisms and Sexualities”
  - courses: WGS 406 ⟵ “WGS 406 - Gender, Fashion & the Body”
  - courses: WGS 410 ⟵ “WGS 410 - Sexing the Body”
  - courses: WGS 495 ⟵ “WGS 495 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 496 ⟵ “WGS 496 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 497 ⟵ “WGS 497 - Independent Study”
  - courses: WGS 498 ⟵ “WGS 498 - Independent Study”
### `00dd142e44aa8f15` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=additional-communication-major-courses-study-abroad [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 300 ⟵ “COMM 300 - International Sojourning”
  - courses: COMM 440 ⟵ “COMM 440 - Documentary Filmmaking Study Abroad”
### `02d819e0a8382a18` Old Dominion University — degree_requirements 2026-27 · program_key=career-and-technical-education-with-a-major-in-technology-education-bs · requirement_key=career-and-technical-education-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-technology-bs/ (sha256 96e93c2cb7e2)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: FOUN 301 ⟵ “FOUN 301 - Learning and Development”
  - courses: FOUN 302 ⟵ “FOUN 302 - Assessment of Learning”
  - courses: STEM 370T ⟵ “STEM 370T - Technology and Society (Writing Intensive) *”
  - courses: TLED 326 ⟵ “TLED 326 - Socio-Cultural Perspectives in Education”
  - courses: TLED 426 ⟵ “TLED 426 - Introduction to Literacy, Linguistics and Practice in the Classroom”
### `094694fb0a5a10f4` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=strategic-communication-and-journalism-major-journalism-public-information [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, mixed_required_and_choice
  - courses: COMM 363 ⟵ “COMM 363 - Introduction to Journalism”
  - courses: ENGL 486 ⟵ “ENGL 486 - Media Law and Ethics”
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
  - courses: COMM 309 ⟵ “COMM 309 - Media Relations”
  - courses: COMM 310 ⟵ “COMM 310 - Strategic Communications Campaigns (Strategic Communication)”
  - courses: COMM 437 ⟵ “COMM 437 - Podcasting”
  - courses: COMM 438 ⟵ “COMM 438 - The Advertising Industry”
  - courses: COMM 457 ⟵ “COMM 457 - Market Research”
  - courses: COMM 460 ⟵ “COMM 460 - Social Marketing”
  - courses: COMM 462 ⟵ “COMM 462 - Sport Communication”
  - courses: COMM 484 ⟵ “COMM 484 - Strategic Media Design and Production”
  - courses: MKTG 402 ⟵ “MKTG 402 - Consumer Behavior”
  - courses: COMM 309 ⟵ “COMM 309 - Media Relations”
  - courses: COMM 387 ⟵ “COMM 387 - TV News Production”
  - courses: COMM 403 ⟵ “COMM 403 - Public Information and Crisis Communications”
  - courses: COMM 404 ⟵ “COMM 404 - Emergency Management Communication”
  - courses: COMM 435 ⟵ “COMM 435 - Arts Journalism”
  - courses: COMM 436 ⟵ “COMM 436 - Multimedia Journalism”
  - courses: COMM 437 ⟵ “COMM 437 - Podcasting”
  - courses: COMM 462 ⟵ “COMM 462 - Sport Communication”
  - courses: COMM 466 ⟵ “COMM 466 - Feature Story Writing”
  - courses: ENGL 385 ⟵ “ENGL 385 - The Press and Making of American Democracy”
### `0c7aa422ff2a4e1d` Old Dominion University — degree_requirements 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-industrial-technology-bs · requirement_key=industrial-technology-major-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-industrial-technology-bs/ (sha256 201fc53177e7)
- issues: requirement_groups_skipped
  - section: industrial-technology-major-electives ⟵ “Industrial Technology Major — Electives”
### `0d8fd640fab2633d` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=communication-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 103R ⟵ “COMM 103R - Voice and Diction”
  - courses: COMM 112R ⟵ “COMM 112R - Introduction to Interpersonal Communication”
  - courses: COMM 195 ⟵ “COMM 195 - Topics in Communication”
  - courses: COMM 225 ⟵ “COMM 225 - Introduction to Production Technology”
  - courses: COMM 269 ⟵ “COMM 269 - Visual Storytelling”
  - courses: COMM 270A ⟵ “COMM 270A - Film Appreciation”
  - courses: COMM 271 ⟵ “COMM 271 - Introduction to Filmmaking”
  - courses: COMM 272G ⟵ “COMM 272G - Digital Literacy”
  - courses: COMM 280T ⟵ “COMM 280T - Entertainment Technologies”
  - courses: COMM 295 ⟵ “COMM 295 - Topics in Communication”
  - courses: COMM 304 ⟵ “COMM 304 - Advanced Public Speaking”
  - courses: COMM 307 ⟵ “COMM 307 - Understanding European Film”
  - courses: COMM 321 ⟵ “COMM 321 - Production Management for Television and Stage”
  - courses: COMM 325 ⟵ “COMM 325 - Sound Design for Stage and Camera”
  - courses: COMM 341 ⟵ “COMM 341 - Lighting Design for Stage and Film”
  - courses: COMM 349 ⟵ “COMM 349 - Costume Design for Stage and Camera”
  - courses: COMM 354 ⟵ “COMM 354 - Drafting and Rendering for Stage and Screen”
  - courses: COMM 356 ⟵ “COMM 356 - 3D Animation”
  - courses: COMM 357 ⟵ “COMM 357 - 3D Animation”
  - courses: COMM 359 ⟵ “COMM 359 - Costume Crafts”
  - courses: COMM 367 ⟵ “COMM 367 - Cooperative Education”
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
  - courses: COMM 382 ⟵ “COMM 382 - Reporting News for Television and Digital Media”
  - courses: COMM 453 ⟵ “COMM 453 - Voice Over”
### `10c0a3a923df516a` Old Dominion University — degree_requirements 2026-27 · program_key=world-languages-and-cultures-with-a-major-in-japanese-ba · requirement_key=japanese-major-japanese-major-prerequisites [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/world-languages-cultures/world-languages-cultures-japanese-ba/ (sha256 fa2e03649f15)
- issues: requirement_groups_skipped
  - courses: JAPN 301 ⟵ “JAPN 301 - Intermediate to Advanced Japanese I”
  - courses: JAPN 302 ⟵ “JAPN 302 - Intermediate to Advanced Japanese II **”
### `11aa3fe0880e9177` Old Dominion University — degree_requirements 2026-27 · program_key=african-american-and-african-studies-bs · requirement_key=african-american-and-african-studies-requirements-african-american-and-african-s [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-bs/ (sha256 af978b675a37)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: AAST 100S ⟵ “AAST 100S - Introduction to African American Studies”
  - courses: AAST/HIST 105H ⟵ “AAST/HIST 105H - Interpreting the African Past”
  - courses: AAST 410 ⟵ “AAST 410 - Africana Intellectual Thought and Economic Development”
  - courses: AAST 420W ⟵ “AAST 420W - African American Political and Social Thought *”
  - courses: AAST/POLS 308 ⟵ “AAST/POLS 308 - Research Design”
  - courses: AAST 320 ⟵ “AAST 320 - Introduction to Research Methods”
  - courses: SOC 337 ⟵ “SOC 337 - Social Research Methods”
  - courses: AAST 490 ⟵ “AAST 490 - Senior Seminar”
  - courses: SOC 320 ⟵ “SOC 320 - Social Inequality”
### `11bf75629cc330c7` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-ba · requirement_key=women-s-and-gender-studies-major-history [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-ba/ (sha256 359f7abf5fe7)
- issues: requirement_groups_skipped
  - courses: HIST 363 ⟵ “HIST 363 - Women in U.S. History”
### `136a55606c145b37` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-supply-chain-and-maritime-logistics-bs · requirement_key=foundations-coursework-leadership [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-supply-chain-and-maritime-logistics-bs/ (sha256 0c18deed219f)
- issues: requirement_groups_skipped
  - courses: COMM 355 ⟵ “COMM 355 - Organizational Communication”
  - courses: CPD 400 ⟵ “CPD 400 - Foundations of Leadership”
  - courses: ENGL 334W ⟵ “ENGL 334W - Technical Writing”
  - courses: PHIL 303E ⟵ “PHIL 303E - Business Ethics”
### `13946e7f85a5ac0c` Old Dominion University — degree_requirements 2026-27 · program_key=women-s-studies-bs · requirement_key=women-s-studies-major-women-s-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/womens-studies/womens-studies-bs/ (sha256 0c3f4590054d)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, mixed_required_and_choice
  - courses: WGS 201S ⟵ “WGS 201S - Introduction to Women's, Gender, and Sexuality Studies”
  - courses: WGS 301 ⟵ “WGS 301 - Feminist Foundations”
  - courses: WGS 302W ⟵ “WGS 302W - Dimensions of Diversity: Intersectionality Among Women”
  - courses: WGS 390T ⟵ “WGS 390T - Women, Gender, and Technology Worldwide”
  - courses: WGS 400 ⟵ “WGS 400 - History of U.S. Women's Activism”
  - courses: WGS 401W ⟵ “WGS 401W - Women: A Global Perspective”
  - courses: WGS 460W ⟵ “WGS 460W - Feminist and Queer Theory”
  - courses: WGS 470 ⟵ “WGS 470 - Feminist Research Methods”
  - courses: WGS 303 ⟵ “WGS 303 - Queer Studies”
  - courses: WGS 304 ⟵ “WGS 304 - Gender and Sexuality in Film”
  - courses: WGS 305 ⟵ “WGS 305 - Queer Literature”
  - courses: WGS 306 ⟵ “WGS 306 - Women, the Environment, and Climate Change”
  - courses: WGS 368 ⟵ “WGS 368 - Internship”
  - courses: WGS 395 ⟵ “WGS 395 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 396 ⟵ “WGS 396 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 402 ⟵ “WGS 402 - Feminisms and Sexualities”
  - courses: WGS 405 ⟵ “WGS 405 - Gender and Media”
  - courses: WGS 406 ⟵ “WGS 406 - Gender, Fashion & the Body”
  - courses: WGS 410 ⟵ “WGS 410 - Sexing the Body”
  - courses: WGS 415 ⟵ “WGS 415 - Migration and Refugee Studies”
  - courses: WGS 495 ⟵ “WGS 495 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 497 ⟵ “WGS 497 - Independent Study”
  - courses: WGS 498 ⟵ “WGS 498 - Independent Study”
### `151edb494f3c50d4` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-economics [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: ECON 450 ⟵ “ECON 450 - International Economics”
  - courses: ECON 454W ⟵ “ECON 454W - Economic Development”
  - courses: ECON 455 ⟵ “ECON 455 - Comparative Economic Systems”
  - courses: ECON 495 ⟵ “ECON 495 - Selected Topics in Economics ++”
### `156ec37ac2d25069` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=additional-communication-major-courses-roar [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped, mixed_required_and_choice, choice_rule_unparsed
  - courses: COMM 490 ⟵ “COMM 490 - ROAR Communications Agency (available only for Strategic Communication and Journalism majors)”
  - courses: COMM 439 ⟵ “COMM 439 - WHRO Production”
  - courses: COMM 482 ⟵ “COMM 482 - Screenwriting II”
  - courses: COMM 483 ⟵ “COMM 483 - Advanced Cinema Projects”
  - courses: COMM 486 ⟵ “COMM 486 - Advanced Filmmaking”
  - courses: COMM 493 ⟵ “COMM 493 - Feature Film Production”
### `16a992d8129267b8` Old Dominion University — degree_requirements 2026-27 · program_key=special-education-with-a-major-in-special-education-adapted-curriculum-k-12-bs · requirement_key=special-education-adapted-curriculum-k-12-major-special-education-adapted-curric [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/special-education-adapted-curriculum-k12-bs/ (sha256 3739387c8fb1)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: LIBS 110G ⟵ “LIBS 110G - Information Literacy for the Digital Age **”
  - courses: SPED 402 ⟵ “SPED 402 - Instructional Design I: Learner Characteristics and Assessment”
  - courses: SPED 404 ⟵ “SPED 404 - Characteristics and Medical Aspects of Disabling Conditions”
  - courses: SPED 415 ⟵ “SPED 415 - Instructional Design II: Curricular Procedures and Individualized Education Planning ***”
  - courses: SPED 418 ⟵ “SPED 418 - Instructional Strategies to Meet Diverse Learning Needs in Math”
  - courses: SPED 428 ⟵ “SPED 428 - Instructional Strategies for Students Accessing the Adapted Curriculum ***”
  - courses: SPED 440 ⟵ “SPED 440 - Assistive Technology for Diverse Students ***”
  - courses: SPED 441 ⟵ “SPED 441 - Teaching Students with Severe Physical and Sensorimotor Disabilities ***”
  - courses: SPED 469 ⟵ “SPED 469 - Communication/Language Development/Intervention for Students with Significant Disabilities”
  - courses: SPED 486 ⟵ “SPED 486 - Teacher Candidate Internship for Special Endorsement ***++”
### `16ec8458e72e3290` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=additional-communication-major-courses-study-abroad [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 300 ⟵ “COMM 300 - International Sojourning”
  - courses: COMM 440 ⟵ “COMM 440 - Documentary Filmmaking Study Abroad”
### `17562b649502254c` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=additional-communication-major-courses-capstone [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 433 ⟵ “COMM 433 - Capstone”
### `19d828c7e756befc` Old Dominion University — degree_requirements 2026-27 · program_key=african-american-and-african-studies-ba · requirement_key=african-american-and-african-studies-requirements-african-american-and-african-s [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-ba/ (sha256 33b79ef74f7b)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: AAST 100S ⟵ “AAST 100S - Introduction to African American Studies”
  - courses: AAST/HIST 105H ⟵ “AAST/HIST 105H - Interpreting the African Past”
  - courses: AAST 410 ⟵ “AAST 410 - Africana Intellectual Thought and Economic Development”
  - courses: AAST 420W ⟵ “AAST 420W - African American Political and Social Thought *”
  - courses: AAST/POLS 308 ⟵ “AAST/POLS 308 - Research Design”
  - courses: AAST 320 ⟵ “AAST 320 - Introduction to Research Methods”
  - courses: SOC 337 ⟵ “SOC 337 - Social Research Methods”
  - courses: AAST 490 ⟵ “AAST 490 - Senior Seminar”
  - courses: SOC 320 ⟵ “SOC 320 - Social Inequality”
### `1d5acee7264a63d1` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-applied-linguistics-ba · requirement_key=applied-linguistics-major-applied-linguistics [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-applied-linguistics-ba/ (sha256 387330ef24ca)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: ENGL 350 ⟵ “ENGL 350 - Aspects of the English Language”
  - courses: ENGL 371W ⟵ “ENGL 371W - Language and Culture”
  - courses: ENGL 390 ⟵ “ENGL 390 - TESL Methods, Materials, & Assessment”
  - courses: ENGL 440 ⟵ “ENGL 440 - General Linguistics”
  - courses: ENGL 442 ⟵ “ENGL 442 - English Grammar”
  - courses: ENGL 443 ⟵ “ENGL 443 - Southern and African American English”
  - courses: ENGL 444 ⟵ “ENGL 444 - History of the English Language”
  - courses: ENGL 445 ⟵ “ENGL 445 - Forensic Linguistics”
  - courses: ENGL 450 ⟵ “ENGL 450 - American English”
  - courses: ENGL 477 ⟵ “ENGL 477 - Language, Gender and Power”
  - courses: ENGL 495 ⟵ “ENGL 495 - Topics in English (linguistics-related)”
### `1dda2eec705b2a45` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=asian-studies-major-capstone-seminar-in-asian-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: ASIA 461W ⟵ “ASIA 461W - Asian Studies Capstone Seminar *”
### `2220ced43e502255` Old Dominion University — degree_requirements 2026-27 · program_key=data-science-bs · requirement_key=data-science-major-core-requirements [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-bs/ (sha256 bea76769d765)
- issues: requirement_groups_skipped
  - courses: BDA 200T ⟵ “BDA 200T - Elements of Data Science”
  - courses: DASC/SOC 205S ⟵ “DASC/SOC 205S - Data, Technology, Society”
  - courses: DASC 300 ⟵ “DASC 300 - Foundations of Data Science”
  - courses: DASC/PHIL 357E ⟵ “DASC/PHIL 357E - Ethics and Data”
  - courses: DASC 434 ⟵ “DASC 434 - Principles of Data Science with Generative AI”
  - courses: IT 360T ⟵ “IT 360T - Principles of Information Technology”
  - courses: IT 450 ⟵ “IT 450 - Database Concepts”
  - courses: STAT 310 ⟵ “STAT 310 - Introductory Data Analysis”
  - courses: DASC 436W ⟵ “DASC 436W - Data Science Capstone Project *”
### `22a250247cf340df` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-supply-chain-and-maritime-logistics-bs · requirement_key=supply-chain-and-maritime-logistics-major-major-prerequisite [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-supply-chain-and-maritime-logistics-bs/ (sha256 0c18deed219f)
- issues: requirement_groups_skipped
  - courses: SCLM 204 ⟵ “SCLM 204 - Fundamentals of Global Supply Chain Management”
### `2325905bceec939e` Old Dominion University — degree_requirements 2026-27 · program_key=data-science-with-a-major-in-data-for-a-human-world-bs · requirement_key=data-for-a-human-world-major-foundation-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-data-for-a-human-world-bs/ (sha256 e583b8d1f70b)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, mixed_required_and_choice
  - courses: MATH 163 ⟵ “MATH 163 - Precalculus II **”
  - courses: STAT 130M ⟵ “STAT 130M - Elementary Statistics”
### `2355d7d2d5388c70` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=special-topics-in-communication-courses-and-communication-tutorials [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 395 ⟵ “COMM 395 - Topics in Communication”
  - courses: COMM 396 ⟵ “COMM 396 - Topics in Communication”
  - courses: COMM 495 ⟵ “COMM 495 - Topics in Communication”
  - courses: COMM 496 ⟵ “COMM 496 - Topics in Communication”
  - courses: COMM 497 ⟵ “COMM 497 - Tutorial Work in Special Topics in Communication”
### `23a27b45f6312745` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-applied-linguistics-ba · requirement_key=english-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-applied-linguistics-ba/ (sha256 387330ef24ca)
- issues: requirement_groups_skipped
  - courses: ENGL 307T ⟵ “ENGL 307T - Digital Writing”
  - courses: ENGL 490 ⟵ “ENGL 490 - Professionalization in English”
### `28fbc0e980754743` Old Dominion University — degree_requirements 2026-27 · program_key=park-recreation-and-tourism-studies-with-a-major-in-tourism-and-hospitality-mana · requirement_key=tourism-and-hospitality-management-major-tourism-and-hospitality-management [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/park-recreation-tourism-studies-hospitality-management-bs/ (sha256 ac6ca2491f1c)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ACCT 202 ⟵ “ACCT 202 - Principles of Managerial Accounting”
  - courses: PRTS 271 ⟵ “PRTS 271 - Introduction to Tourism & Hospitality Management *”
  - courses: PRTS 350 ⟵ “PRTS 350 - Lodging Operations”
  - courses: PRTS 441 ⟵ “PRTS 441 - Marketing of Hospitality Services”
  - courses: PRTS 461 ⟵ “PRTS 461 - Hospitality Leadership and Management”
  - courses: PRTS 465 ⟵ “PRTS 465 - Hospitality Revenue Management”
  - courses: PRTS 491 ⟵ “PRTS 491 - Festival, Meeting, and Event Management”
### `29eef93825bf9e0a` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-women-s-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: WGS 390T ⟵ “WGS 390T - Women, Gender, and Technology Worldwide”
  - courses: WGS 401W ⟵ “WGS 401W - Women: A Global Perspective”
  - courses: WGS 415 ⟵ “WGS 415 - Migration and Refugee Studies”
  - courses: WGS 495 ⟵ “WGS 495 - Topics in Women's, Gender, and Sexuality Studies ++”
### `2b041f8f6910c8bd` Old Dominion University — degree_requirements 2026-27 · program_key=special-education-with-a-major-in-special-education-general-curriculum-k-12-bs · requirement_key=special-education-general-curriculum-k-12-major-special-education-general-curric [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/special-education-general-curriculum-k12-bs/ (sha256 f33ea5dcbf71)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: LIBS 110G ⟵ “LIBS 110G - Information Literacy for the Digital Age **”
  - courses: SPED 402 ⟵ “SPED 402 - Instructional Design I: Learner Characteristics and Assessment”
  - courses: SPED 403 ⟵ “SPED 403 - Directed Field Experience in Special Education ***”
  - courses: SPED 415 ⟵ “SPED 415 - Instructional Design II: Curricular Procedures and Individualized Education Planning ***”
  - courses: SPED 418 ⟵ “SPED 418 - Instructional Strategies to Meet Diverse Learning Needs in Math”
  - courses: SPED 440 ⟵ “SPED 440 - Assistive Technology for Diverse Students”
  - courses: SPED 486 ⟵ “SPED 486 - Teacher Candidate Internship for Special Endorsement ***++”
  - courses: TLED 408 ⟵ “TLED 408 - Reading and Writing in Content Areas”
### `2b16dabc4120c71c` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=special-topics-in-communication-courses-and-communication-tutorials [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 395 ⟵ “COMM 395 - Topics in Communication”
  - courses: COMM 396 ⟵ “COMM 396 - Topics in Communication”
  - courses: COMM 495 ⟵ “COMM 495 - Topics in Communication”
  - courses: COMM 496 ⟵ “COMM 496 - Topics in Communication”
  - courses: COMM 497 ⟵ “COMM 497 - Tutorial Work in Special Topics in Communication”
### `2d9bfc2839ebdac9` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-supply-chain-and-maritime-logistics-bs · requirement_key=supply-chain-and-maritime-logistics-major-interdisciplinary-studies-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-supply-chain-and-maritime-logistics-bs/ (sha256 0c18deed219f)
- issues: requirement_groups_skipped
  - courses: IDS 300W ⟵ “IDS 300W - Interdisciplinary Theory and Concepts *”
  - courses: IDS 301 ⟵ “IDS 301 - Data and Humanities Research **”
  - courses: IDS 493 ⟵ “IDS 493 - IDS Electronic Portfolio Project **”
### `2daa30c1d6885a53` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=strategic-communication-and-journalism-major-strategic-communication [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 303 ⟵ “COMM 303 - Introduction to Strategic Communications”
  - courses: COMM 478 ⟵ “COMM 478 - Media Marketing and Promotion”
### `2e59a347f7d80c77` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=strategic-communication-and-journalism-major-comm-elective [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - section: strategic-communication-and-journalism-major-comm-elective ⟵ “Strategic Communication and Journalism Major — COMM Elective”
### `3069ef68d8995f71` Old Dominion University — degree_requirements 2026-27 · program_key=career-and-technical-education-with-a-major-in-technology-education-bs · requirement_key=technology-education-major-technology-education [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-technology-bs/ (sha256 96e93c2cb7e2)
- issues: requirement_groups_skipped
  - courses: SEPS 195 ⟵ “SEPS 195 - Topics (Design & Visualization)”
  - courses: SEPS 297 ⟵ “SEPS 297 - Observation and Participation”
  - courses: SEPS 400 ⟵ “SEPS 400 - Instructional Systems Development”
  - courses: SEPS 401 ⟵ “SEPS 401 - Foundations of Career and Technical Education”
  - courses: SEPS 402 ⟵ “SEPS 402 - Instructional Methods in Occupational Studies”
  - courses: SEPS 408 ⟵ “SEPS 408 - Advanced Classroom Issues and Practices in Career and Technical Education”
  - courses: SEPS 485 ⟵ “SEPS 485 - Student Teaching”
  - courses: SPED 400 ⟵ “SPED 400 - Foundations of Special Education: Legal Aspects and Characteristics”
  - courses: STEM 110T ⟵ “STEM 110T - Technology and Your World”
  - courses: STEM 221 ⟵ “STEM 221 - Industrial Materials”
  - courses: STEM 231 ⟵ “STEM 231 - Materials and Processes Technology”
  - courses: STEM 241 ⟵ “STEM 241 - Energy Systems: Basic Electricity”
  - courses: STEM 242 ⟵ “STEM 242 - Technological Systems Control”
  - courses: STEM 251G ⟵ “STEM 251G - Computer Literacy: Communication and Information”
  - courses: STEM 351 ⟵ “STEM 351 - Communication Technology”
  - courses: STEM 382 ⟵ “STEM 382 - Industrial Design”
### `316f02fdcacdbb28` Old Dominion University — degree_requirements 2026-27 · program_key=women-s-studies-bs · requirement_key=double-majoring-in-philosophy-and-women-s-gender-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/womens-studies/womens-studies-bs/ (sha256 0c3f4590054d)
- issues: requirement_groups_skipped
  - courses: PHIL 365 ⟵ “PHIL 365 - Race & Power”
  - courses: PHIL 402 ⟵ “PHIL 402 - Gender and Philosophy”
  - courses: REL 403 ⟵ “REL 403 - Gender and Sexuality in Islam”
  - courses: WGS 302W ⟵ “WGS 302W - Dimensions of Diversity: Intersectionality Among Women”
  - courses: WGS 303 ⟵ “WGS 303 - Queer Studies”
  - courses: WGS 460W ⟵ “WGS 460W - Feminist and Queer Theory”
### `322e4b9ff325b952` Old Dominion University — degree_requirements 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-industrial-technology-bs · requirement_key=industrial-technology-major-technical-content-general [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-industrial-technology-bs/ (sha256 201fc53177e7)
- issues: requirement_groups_skipped
  - courses: SEPS 195 ⟵ “SEPS 195 - Topics (Design & Visualization)”
  - courses: STEM 221 ⟵ “STEM 221 - Industrial Materials”
  - courses: STEM 231 ⟵ “STEM 231 - Materials and Processes Technology”
  - courses: STEM 241 ⟵ “STEM 241 - Energy Systems: Basic Electricity”
  - courses: STEM 242 ⟵ “STEM 242 - Technological Systems Control”
  - courses: STEM 320 ⟵ “STEM 320 - Manufacturing and Construction Technology”
  - courses: STEM 351 ⟵ “STEM 351 - Communication Technology”
  - courses: STEM 382 ⟵ “STEM 382 - Industrial Design”
  - courses: SEPS 395 ⟵ “SEPS 395 - Topics in Occupational Education (Design for Production)”
  - courses: STEM 495 ⟵ “STEM 495 - Topics (Building, Design, and Development)”
### `324e153b0b181e81` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=additional-communication-major-courses-study-abroad [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 300 ⟵ “COMM 300 - International Sojourning”
  - courses: COMM 440 ⟵ “COMM 440 - Documentary Filmmaking Study Abroad”
### `32eaea978dce0551` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-international-business [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: INBU 463 ⟵ “INBU 463 - International Business Seminar Abroad”
### `32feb7da111593de` Old Dominion University — degree_requirements 2026-27 · program_key=african-american-and-african-studies-bs · requirement_key=african-studies-ba-and-bs-6-credit-hours-300-and-400-level-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-bs/ (sha256 af978b675a37)
- issues: requirement_groups_skipped
  - courses: AAST 310 ⟵ “AAST 310 - Human Rights and Social Change in Africa”
  - courses: AAST/POLS 316 ⟵ “AAST/POLS 316 - Politics of Africa”
  - courses: AAST/HIST 381 ⟵ “AAST/HIST 381 - Africa in the 20th Century”
  - courses: GEOG 452 ⟵ “GEOG 452 - Africa”
  - courses: HIST 370 ⟵ “HIST 370 - Africa and the Atlantic Slave Trade”
  - courses: HIST 382 ⟵ “HIST 382 - African Civilizations”
  - courses: HIST 475 ⟵ “HIST 475 - Global Africa”
  - courses: POLS 439 ⟵ “POLS 439 - International Relations of African States”
### `34f4c33c03c88179` Old Dominion University — degree_requirements 2026-27 · program_key=special-education-with-a-major-in-early-intervention-early-childhood-special-edu · requirement_key=early-intervention-early-childhood-special-education-birth-5-major-early-interve [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/special-education-early-intervention-early-childhood-special-education-birth-5-bs/ (sha256 0dce08dad768)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: LIBS 110G ⟵ “LIBS 110G - Information Literacy for the Digital Age **”
  - courses: SPED 313 ⟵ “SPED 313 - Fundamentals of Human Growth and Development: Birth through Adolescence”
  - courses: SPED 404 ⟵ “SPED 404 - Characteristics and Medical Aspects of Disabling Conditions”
  - courses: TLED 320 ⟵ “TLED 320 - Perspectives on the Young Child and the Family”
  - courses: TLED 338 ⟵ “TLED 338 - Integrated Methods & Curriculum in Early Childhood Ed: Birth-Pre-K”
  - courses: SPED 415 ⟵ “SPED 415 - Instructional Design II: Curricular Procedures and Individualized Education Planning ***”
  - courses: SPED 440 ⟵ “SPED 440 - Assistive Technology for Diverse Students”
  - courses: SPED 441 ⟵ “SPED 441 - Teaching Students with Severe Physical and Sensorimotor Disabilities ***”
  - courses: SPED 469 ⟵ “SPED 469 - Communication/Language Development/Intervention for Students with Significant Disabilities”
  - courses: SPED 460 ⟵ “SPED 460 - Teaching Preschoolers With Diverse Abilities ***”
  - courses: SPED 461 ⟵ “SPED 461 - Developmental Assessment of Young Children with Diverse Abilities”
  - courses: SPED 467 ⟵ “SPED 467 - Family-Centered Practices in Early Childhood Intervention ***”
  - courses: SPED 486 ⟵ “SPED 486 - Teacher Candidate Internship for Special Endorsement ***++”
### `35afc09adbdead24` Old Dominion University — degree_requirements 2026-27 · program_key=career-and-technical-education-with-a-major-in-technology-education-bs · requirement_key=licensure-endorsement-programs [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-technology-bs/ (sha256 96e93c2cb7e2)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: SEPS 297 ⟵ “SEPS 297 - Observation and Participation”
  - courses: SPED 313 ⟵ “SPED 313 - Fundamentals of Human Growth and Development: Birth through Adolescence”
  - courses: TLED 408 ⟵ “TLED 408 - Reading and Writing in Content Areas”
  - courses: SEPS 485 ⟵ “SEPS 485 - Student Teaching”
### `386b92b96393972a` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=special-topics-in-communication-courses-and-communication-tutorials [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 395 ⟵ “COMM 395 - Topics in Communication”
  - courses: COMM 396 ⟵ “COMM 396 - Topics in Communication”
  - courses: COMM 495 ⟵ “COMM 495 - Topics in Communication”
  - courses: COMM 496 ⟵ “COMM 496 - Topics in Communication”
  - courses: COMM 497 ⟵ “COMM 497 - Tutorial Work in Special Topics in Communication”
### `3961d0fe097feea5` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=additional-communication-major-courses-research-practicum [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
### `39c00394301dab42` Old Dominion University — degree_requirements 2026-27 · program_key=women-s-studies-ba · requirement_key=double-majoring-in-philosophy-and-women-s-gender-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/womens-studies/womens-studies-ba/ (sha256 abf03dc3b73c)
- issues: requirement_groups_skipped
  - courses: PHIL 365 ⟵ “PHIL 365 - Race & Power”
  - courses: PHIL 402 ⟵ “PHIL 402 - Gender and Philosophy”
  - courses: REL 403 ⟵ “REL 403 - Gender and Sexuality in Islam”
  - courses: WGS 302W ⟵ “WGS 302W - Dimensions of Diversity: Intersectionality Among Women”
  - courses: WGS 303 ⟵ “WGS 303 - Queer Studies”
  - courses: WGS 460W ⟵ “WGS 460W - Feminist and Queer Theory”
### `39ea655a1495e256` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-technical-and-professional-writing-ba · requirement_key=english-core-writing [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-technical-and-professional-writing-ba/ (sha256 24304c241949)
- issues: requirement_groups_skipped
  - courses: ENGL 300W ⟵ “ENGL 300W - Introduction to Creative Writing”
  - courses: ENGL 327W ⟵ “ENGL 327W - Advanced Composition”
  - courses: ENGL 334W ⟵ “ENGL 334W - Technical Writing”
  - courses: ENGL 427W ⟵ “ENGL 427W - Writing in the Disciplines”
### `3a05d30ddb660227` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=internships-and-practicum-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
### `3a51065c193f1fa6` Old Dominion University — degree_requirements 2026-27 · program_key=data-science-with-a-major-in-data-for-a-human-world-bs · requirement_key=data-for-a-human-world-major-core-requirements [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-data-for-a-human-world-bs/ (sha256 e583b8d1f70b)
- issues: requirement_groups_skipped
  - courses: BDA 200T ⟵ “BDA 200T - Elements of Data Science”
  - courses: DASC/SOC 205S ⟵ “DASC/SOC 205S - Data, Technology, Society”
  - courses: DASC 300 ⟵ “DASC 300 - Foundations of Data Science”
  - courses: DASC/PHIL 357E ⟵ “DASC/PHIL 357E - Ethics and Data”
  - courses: DASC 434 ⟵ “DASC 434 - Principles of Data Science with Generative AI”
  - courses: IT 360T ⟵ “IT 360T - Principles of Information Technology”
  - courses: IT 450 ⟵ “IT 450 - Database Concepts”
  - courses: STAT 310 ⟵ “STAT 310 - Introductory Data Analysis”
  - courses: DASC 436W ⟵ “DASC 436W - Data Science Capstone Project *”
### `3a52dcc1bde06706` Old Dominion University — degree_requirements 2026-27 · program_key=environmental-health-bs · requirement_key=environmental-health-major-environmental-health-major [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/joint-school-public-health/epidemiology-biostatistics-and-environmental-health/environmental-health-bs/ (sha256 daea2f065cee)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: PUBH 200 ⟵ “PUBH 200 - Principles of Public Health”
  - courses: ENVH 301 ⟵ “ENVH 301 - Principles of Environmental Health Science”
  - courses: ENVH 402W ⟵ “ENVH 402W - Environmental and Occupational Health Administration and Law **”
  - courses: ENVH 403 ⟵ “ENVH 403 - Environmental and Occupational Health Internship I”
  - courses: ENVH 406 ⟵ “ENVH 406 - Principles of Occupational Safety and Health”
  - courses: ENVH 420 ⟵ “ENVH 420 - Communicable Diseases”
  - courses: ENVH 422 ⟵ “ENVH 422 - Water and Wastewater Technology”
  - courses: ENVH 441 ⟵ “ENVH 441 - Industrial Hygiene”
  - courses: ENVH 443 ⟵ “ENVH 443 - Principles of Toxicology”
  - courses: ENVH 448 ⟵ “ENVH 448 - Epidemiology and Biostatistics”
  - courses: ENVH 466 ⟵ “ENVH 466 - Environmental and Occupational Risk Assessment and Decision Analysis”
  - courses: ENVH 499 ⟵ “ENVH 499 - Environmental and Occupational Health Senior Seminar”
  - courses: ENVH 401 ⟵ “ENVH 401 - Occupational Health”
  - courses: ENVH 407 ⟵ “ENVH 407 - Occupational Safety Standards, Laws and Regulations”
  - courses: ENVH 421 ⟵ “ENVH 421 - Food Safety”
  - courses: ENVH 423 ⟵ “ENVH 423 - Vector-Borne Diseases and Their Control”
  - courses: ENVH 425 ⟵ “ENVH 425 - Occupational Safety and Health Program Management”
  - courses: ENVH 426 ⟵ “ENVH 426 - Physical Hazards and Their Control”
  - courses: ENVH 440 ⟵ “ENVH 440 - Principles of Ergonomics”
  - courses: ENVH 442 ⟵ “ENVH 442 - Industrial Hygiene Sampling Methods”
  - courses: ENVH 445 ⟵ “ENVH 445 - Air Pollution and Its Control”
  - courses: ENVH 470 ⟵ “ENVH 470 - Industrial Environmental Management”
### `3b51a529840597c5` Old Dominion University — degree_requirements 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-training-specialist-bs · requirement_key=training-specialist-major-technical-content-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-training-specialist-bs/ (sha256 e9e73afa7e78)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ACCT 201 ⟵ “ACCT 201 - Principles of Financial Accounting”
  - courses: HMSV 339 ⟵ “HMSV 339 - Interpersonal Relations”
  - courses: MGMT 325 ⟵ “MGMT 325 - Contemporary Organizations and Management”
  - courses: MGMT 330 ⟵ “MGMT 330 - Organizational Behavior”
  - courses: MKTG 311 ⟵ “MKTG 311 - Marketing Principles and Problems”
  - courses: PSYC 201S ⟵ “PSYC 201S - Introduction to Psychology”
  - courses: PSYC 303 ⟵ “PSYC 303 - Industrial/Organizational Psychology”
  - courses: SEPS 302 ⟵ “SEPS 302 - Workforce Supervision Management”
  - courses: SEPS 389 ⟵ “SEPS 389 - Education and Training of Adults”
  - courses: SEPS 400 ⟵ “SEPS 400 - Instructional Systems Development”
  - courses: SEPS 402 ⟵ “SEPS 402 - Instructional Methods in Occupational Studies”
  - courses: SEPS 405 ⟵ “SEPS 405 - Directed Work Experience”
  - courses: SEPS 450 ⟵ “SEPS 450 - Assessment, Evaluation and Improvement”
  - courses: SEPS 481 ⟵ “SEPS 481 - Career and Professional Development”
  - courses: STEM 350 ⟵ “STEM 350 - Communication Technology Processes”
  - courses: STEM 365 ⟵ “STEM 365 - Safety and OSHA Certification”
  - courses: STEM 370T ⟵ “STEM 370T - Technology and Society (Writing Intensive) *”
### `3e0710e73f4b5a91` Old Dominion University — degree_requirements 2026-27 · program_key=speech-language-pathology-and-audiology-bs · requirement_key=speech-language-pathology-and-audiology-major-speech-language-pathology-and-audi [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/health-sciences/speech-language-pathology/speech-language-pathology-audiology-bs/ (sha256 abcf5727ca35)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CSD 350 ⟵ “CSD 350 - Survey in Communication Disorders (Fall, Spring)”
  - courses: CSD 351 ⟵ “CSD 351 - Anatomy of Speech, Language, and Swallowing (Fall only)”
  - courses: CSD 352 ⟵ “CSD 352 - Phonetics”
  - courses: CSD 445 ⟵ “CSD 445 - Foundations of Augmentative and Alternative Communication”
  - courses: CSD 446 ⟵ “CSD 446 - Neural Bases of Communication and Swallowing Disorders (Fall, Spring)”
  - courses: CSD 447 ⟵ “CSD 447 - Introduction to Language Disorders in Children (Fall, Spring)”
  - courses: CSD 449W ⟵ “CSD 449W - Clinical Observation and Writing in Communication Sciences and Disorders (Fall, Spring)”
  - courses: CSD 451 ⟵ “CSD 451 - Introduction to Speech Sound Disorders (Fall, Summer)”
  - courses: CSD 453 ⟵ “CSD 453 - Speech and Language Development (Fall, Spring)”
  - courses: CSD 458 ⟵ “CSD 458 - Speech and Hearing Science (Spring, Summer)”
  - courses: CSD 460 ⟵ “CSD 460 - Hearing Disorders and Basic Audiometry (Fall, Spring)”
  - courses: CSD 461 ⟵ “CSD 461 - Aural Rehabilitation I (Fall, Spring)”
  - courses: CSD 465 ⟵ “CSD 465 - Sign Language and Deaf Culture I (Fall, Spring)”
  - courses: CGE 450 ⟵ “CGE 450 - Social Justice & Literacy for Immigrant and Refugee Learners”
  - courses: ENGL 370 ⟵ “ENGL 370 - English Linguistics”
  - courses: SPED 313 ⟵ “SPED 313 - Fundamentals of Human Growth and Development: Birth through Adolescence”
  - courses: SPED 400 ⟵ “SPED 400 - Foundations of Special Education: Legal Aspects and Characteristics”
### `453e906b898e466a` Old Dominion University — degree_requirements 2026-27 · program_key=exercise-science-bs · requirement_key=clinical-and-research-preparation [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/health-sciences/exercise-science/exercise-science-bs/ (sha256 39f7d122aeba)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PHYS 112N ⟵ “PHYS 112N - Introductory General Physics”
  - courses: STAT 130M ⟵ “STAT 130M - Elementary Statistics”
  - courses: EXSC 420 ⟵ “EXSC 420 - Research Methods in Exercise Science (STAT 130M required as prerequisite)”
### `454a81e18b209a78` Old Dominion University — degree_requirements 2026-27 · program_key=african-american-and-african-studies-bs · requirement_key=upper-division-humanities-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-bs/ (sha256 af978b675a37)
- issues: requirement_groups_skipped
  - courses: AAST/HIST 361 ⟵ “AAST/HIST 361 - African-American History to 1865”
  - courses: AAST 368 ⟵ “AAST 368 - Internship”
  - courses: AAST 395 ⟵ “AAST 395 - Topics in African American Studies”
  - courses: AAST 396 ⟵ “AAST 396 - Topics in African American Studies”
  - courses: ENGL 465W ⟵ “ENGL 465W - African American Literature”
  - courses: HIST 362 ⟵ “HIST 362 - African-American History Since 1865”
  - courses: HIST 370 ⟵ “HIST 370 - Africa and the Atlantic Slave Trade”
  - courses: HIST 455 ⟵ “HIST 455 - African-American Historiography”
  - courses: HIST 475 ⟵ “HIST 475 - Global Africa”
  - courses: MUSC 460 ⟵ “MUSC 460 - History of Jazz”
  - courses: WGS 302W ⟵ “WGS 302W - Dimensions of Diversity: Intersectionality Among Women”
### `456c441fd11d2a7b` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-psycholo [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: PSYC 420 ⟵ “PSYC 420 - Cross-Cultural Psychology”
### `45d33d9a4d9645ba` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-bs · requirement_key=interdisciplinary-studies-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-bs/ (sha256 a576d3c1b66a)
- issues: requirement_groups_skipped
  - courses: IDS 300W ⟵ “IDS 300W - Interdisciplinary Theory and Concepts *”
  - courses: IDS 301 ⟵ “IDS 301 - Data and Humanities Research **”
  - courses: IDS 493 ⟵ “IDS 493 - IDS Electronic Portfolio Project **”
### `47b7adf4bf01384b` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-interdisciplinary-studies-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ASIA 332 ⟵ “ASIA 332 - South Asia Since Independence”
  - courses: ASIA/HIST 336 ⟵ “ASIA/HIST 336 - The Emergence of New China”
  - courses: ASIA 337 ⟵ “ASIA 337 - Japan's Era of Transformation”
  - courses: ASIA/POLS 338W ⟵ “ASIA/POLS 338W - Politics of East Asia”
  - courses: ASIA/PHIL 353 ⟵ “ASIA/PHIL 353 - Asian Religions”
  - courses: ASIA/ARTH 360 ⟵ “ASIA/ARTH 360 - Asian Art”
  - courses: ASIA 395 ⟵ “ASIA 395 - Topics in Asian Studies”
  - courses: ASIA/POLS 435 ⟵ “ASIA/POLS 435 - Chinese Politics”
  - courses: ASIA 461W ⟵ “ASIA 461W - Asian Studies Capstone Seminar”
  - courses: ASIA 495 ⟵ “ASIA 495 - Topics in Asian Studies”
  - courses: GEOG 453 ⟵ “GEOG 453 - Asia”
  - courses: HIST 330 ⟵ “HIST 330 - Modern South Asia, c. 1700 to Present”
  - courses: REL 483 ⟵ “REL 483 - Tibet, Happiness, and this Precious Life”
### `483a24f0bd9e08a0` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-english [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: ENGL 396 ⟵ “ENGL 396 - Topics in English ++”
  - courses: ENGL 466W ⟵ “ENGL 466W - Asian American Literature”
  - courses: ENGL 495 ⟵ “ENGL 495 - Topics in English ++”
### `4a096dcfe446f214` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=communication-core-ba-core-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 200S ⟵ “COMM 200S - Introduction to Human Communication”
  - courses: COMM 260 ⟵ “COMM 260 - Understanding Media”
  - courses: COMM 301 ⟵ “COMM 301 - Critical Methodologies”
### `4a92776d838c9297` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-women-s- [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: WGS 401W ⟵ “WGS 401W - Women: A Global Perspective”
  - courses: WGS 495 ⟵ “WGS 495 - Topics in Women's, Gender, and Sexuality Studies”
### `4b051a66980d638d` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=additional-communication-major-courses-roar [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped, mixed_required_and_choice, choice_rule_unparsed
  - courses: COMM 490 ⟵ “COMM 490 - ROAR Communications Agency (available only for Strategic Communication and Journalism majors)”
  - courses: COMM 439 ⟵ “COMM 439 - WHRO Production”
  - courses: COMM 482 ⟵ “COMM 482 - Screenwriting II”
  - courses: COMM 483 ⟵ “COMM 483 - Advanced Cinema Projects”
  - courses: COMM 486 ⟵ “COMM 486 - Advanced Filmmaking”
  - courses: COMM 493 ⟵ “COMM 493 - Feature Film Production”
### `4bf890967341253d` Old Dominion University — degree_requirements 2026-27 · program_key=data-science-bs · requirement_key=data-science-areas-of-specialization-required-courses-3 [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-bs/ (sha256 bea76769d765)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: GEOG 102T ⟵ “GEOG 102T - Digital Earth: Geospatial Technology and Society”
  - courses: GEOG 402 ⟵ “GEOG 402 - Geographic Information Systems”
  - courses: GEOG 404 ⟵ “GEOG 404 - Digital Techniques for Remote Sensing”
  - courses: GEOG 425 ⟵ “GEOG 425 - Internet Geographic Information Systems”
  - courses: GEOG 432 ⟵ “GEOG 432 - Advanced GIS”
  - courses: GEOG 462 ⟵ “GEOG 462 - Advanced Spatial Analysis”
  - courses: CRJS 344 ⟵ “CRJS 344 - Social Science and Crime Mapping”
  - courses: CS 361 ⟵ “CS 361 - Data Structures and Algorithms”
  - courses: CS 422 ⟵ “CS 422 - Introduction to Machine Learning”
  - courses: CS 432 ⟵ “CS 432 - Web Science”
  - courses: CS 480 ⟵ “CS 480 - Introduction to Artificial Intelligence”
  - courses: DASC 324 ⟵ “DASC 324 - Introduction to Data Visualization”
  - courses: DASC 424 ⟵ “DASC 424 - Data Storytelling”
  - courses: DASC 446 ⟵ “DASC 446 - Fundamentals of Data Collection and Sourcing”
  - courses: DASC 447 ⟵ “DASC 447 - Practical and Principled Prompt Engineering”
  - courses: GEOG 300 ⟵ “GEOG 300 - Maps and Geographic Information”
  - courses: GEOG 463 ⟵ “GEOG 463 - GIS Programming”
  - courses: IT 452 ⟵ “IT 452 - Cloud Database”
  - courses: IT 453 ⟵ “IT 453 - Advanced Database Concepts”
### `4cf288f7e110fb5b` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-politica [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: POLS/ASIA 338W ⟵ “POLS/ASIA 338W - Politics of East Asia”
  - courses: POLS/ASIA 435 ⟵ “POLS/ASIA 435 - Chinese Politics”
  - courses: POLS 437 ⟵ “POLS 437 - International Relations in East Asia”
### `4f0189ba3f29e8fe` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=strategic-communication-and-journalism-major-journalism-public-information [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, mixed_required_and_choice
  - courses: COMM 363 ⟵ “COMM 363 - Introduction to Journalism”
  - courses: ENGL 486 ⟵ “ENGL 486 - Media Law and Ethics”
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
  - courses: COMM 309 ⟵ “COMM 309 - Media Relations”
  - courses: COMM 310 ⟵ “COMM 310 - Strategic Communications Campaigns”
  - courses: COMM 437 ⟵ “COMM 437 - Podcasting”
  - courses: COMM 438 ⟵ “COMM 438 - The Advertising Industry”
  - courses: COMM 457 ⟵ “COMM 457 - Market Research”
  - courses: COMM 460 ⟵ “COMM 460 - Social Marketing”
  - courses: COMM 462 ⟵ “COMM 462 - Sport Communication”
  - courses: COMM 484 ⟵ “COMM 484 - Strategic Media Design and Production”
  - courses: MKTG 402 ⟵ “MKTG 402 - Consumer Behavior”
  - courses: COMM 309 ⟵ “COMM 309 - Media Relations”
  - courses: COMM 387 ⟵ “COMM 387 - TV News Production”
  - courses: COMM 403 ⟵ “COMM 403 - Public Information and Crisis Communications”
  - courses: COMM 404 ⟵ “COMM 404 - Emergency Management Communication”
  - courses: COMM 435 ⟵ “COMM 435 - Arts Journalism”
  - courses: COMM 436 ⟵ “COMM 436 - Multimedia Journalism”
  - courses: COMM 437 ⟵ “COMM 437 - Podcasting”
  - courses: COMM 462 ⟵ “COMM 462 - Sport Communication”
  - courses: COMM 466 ⟵ “COMM 466 - Feature Story Writing”
  - courses: ENGL 385 ⟵ “ENGL 385 - The Press and Making of American Democracy”
### `5186240949d557a0` Old Dominion University — degree_requirements 2026-27 · program_key=career-and-technical-education-with-a-major-in-marketing-education-bs · requirement_key=career-and-technical-education-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-marketing-bs/ (sha256 c38ad1d36dc9)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: FOUN 301 ⟵ “FOUN 301 - Learning and Development”
  - courses: FOUN 302 ⟵ “FOUN 302 - Assessment of Learning”
  - courses: SEPS 408 ⟵ “SEPS 408 - Advanced Classroom Issues and Practices in Career and Technical Education”
  - courses: SPED 400 ⟵ “SPED 400 - Foundations of Special Education: Legal Aspects and Characteristics”
  - courses: STEM 370T ⟵ “STEM 370T - Technology and Society (Writing Intensive) *”
  - courses: TLED 326 ⟵ “TLED 326 - Socio-Cultural Perspectives in Education”
  - courses: TLED 426 ⟵ “TLED 426 - Introduction to Literacy, Linguistics and Practice in the Classroom”
### `5202ea1ff6d69739` Old Dominion University — degree_requirements 2026-27 · program_key=world-languages-and-cultures-with-a-major-in-japanese-ba · requirement_key=japanese-major-japanese-major-requirements [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/world-languages-cultures/world-languages-cultures-japanese-ba/ (sha256 fa2e03649f15)
- issues: requirement_groups_skipped
  - courses: JAPN 311 ⟵ “JAPN 311 - Global Conversations *”
  - courses: JAPN 312W ⟵ “JAPN 312W - Writing Around the World **”
  - courses: JAPN 323 ⟵ “JAPN 323 - World Cultures and Contexts”
### `525457ed1faf0ba6` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-ba · requirement_key=women-s-and-gender-studies-major-interdisciplinary-studies-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-ba/ (sha256 359f7abf5fe7)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: WGS 201S ⟵ “WGS 201S - Introduction to Women's, Gender, and Sexuality Studies”
  - courses: WGS/QUST 302W ⟵ “WGS/QUST 302W - Dimensions of Diversity: Intersectionality Among Women”
  - courses: WGS/QUST 305 ⟵ “WGS/QUST 305 - Queer Literature”
  - courses: WGS 400 ⟵ “WGS 400 - History of U.S. Women's Activism”
  - courses: WGS/QUST 460W ⟵ “WGS/QUST 460W - Feminist and Queer Theory”
### `52d7d664c0445d90` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=additional-communication-major-courses-roar [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped, mixed_required_and_choice, choice_rule_unparsed
  - courses: COMM 490 ⟵ “COMM 490 - ROAR Communications Agency (available only for Strategic Communication and Journalism majors)”
  - courses: COMM 439 ⟵ “COMM 439 - WHRO Production”
  - courses: COMM 482 ⟵ “COMM 482 - Screenwriting II”
  - courses: COMM 483 ⟵ “COMM 483 - Advanced Cinema Projects”
  - courses: COMM 486 ⟵ “COMM 486 - Advanced Filmmaking”
  - courses: COMM 493 ⟵ “COMM 493 - Feature Film Production”
### `53426b24d20d652b` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=communication-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 103R ⟵ “COMM 103R - Voice and Diction”
  - courses: COMM 112R ⟵ “COMM 112R - Introduction to Interpersonal Communication”
  - courses: COMM 195 ⟵ “COMM 195 - Topics in Communication”
  - courses: COMM 225 ⟵ “COMM 225 - Introduction to Production Technology”
  - courses: COMM 269 ⟵ “COMM 269 - Visual Storytelling”
  - courses: COMM 270A ⟵ “COMM 270A - Film Appreciation”
  - courses: COMM 271 ⟵ “COMM 271 - Introduction to Filmmaking”
  - courses: COMM 272G ⟵ “COMM 272G - Digital Literacy”
  - courses: COMM 280T ⟵ “COMM 280T - Entertainment Technologies”
  - courses: COMM 295 ⟵ “COMM 295 - Topics in Communication”
  - courses: COMM 304 ⟵ “COMM 304 - Advanced Public Speaking”
  - courses: COMM 307 ⟵ “COMM 307 - Understanding European Film”
  - courses: COMM 321 ⟵ “COMM 321 - Production Management for Television and Stage”
  - courses: COMM 325 ⟵ “COMM 325 - Sound Design for Stage and Camera”
  - courses: COMM 341 ⟵ “COMM 341 - Lighting Design for Stage and Film”
  - courses: COMM 349 ⟵ “COMM 349 - Costume Design for Stage and Camera”
  - courses: COMM 354 ⟵ “COMM 354 - Drafting and Rendering for Stage and Screen”
  - courses: COMM 356 ⟵ “COMM 356 - 3D Animation”
  - courses: COMM 357 ⟵ “COMM 357 - 3D Animation 2”
  - courses: COMM 359 ⟵ “COMM 359 - Costume Crafts”
  - courses: COMM 367 ⟵ “COMM 367 - Cooperative Education”
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
  - courses: COMM 382 ⟵ “COMM 382 - Reporting News for Television and Digital Media”
  - courses: COMM 453 ⟵ “COMM 453 - Voice Over”
### `5547fc5f5f5d4cf0` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-supply-chain-and-maritime-logistics-bs · requirement_key=foundations-coursework-major-preparation [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-supply-chain-and-maritime-logistics-bs/ (sha256 0c18deed219f)
- issues: requirement_groups_skipped
  - courses: ACCT 201 ⟵ “ACCT 201 - Principles of Financial Accounting”
  - courses: DASC 300 ⟵ “DASC 300 - Foundations of Data Science”
  - courses: ECON 202S ⟵ “ECON 202S - Principles of Microeconomics”
  - courses: SCLM 201 ⟵ “SCLM 201 - Introduction to Spreadsheet Applications”
  - courses: SCLM 202 ⟵ “SCLM 202 - Data-Driven Decision Making in Supply Chain and Maritime Operations”
### `572cc4f269352867` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=cinema-screenwriting-and-studies-major-applied-theories [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, mixed_required_and_choice
  - courses: COMM 471W ⟵ “COMM 471W - International Film History”
  - courses: COMM 485 ⟵ “COMM 485 - Film and Television Genres”
  - courses: COMM 307 ⟵ “COMM 307 - Understanding European Film”
  - courses: COMM 334 ⟵ “COMM 334 - Narrative Adaptation”
  - courses: COMM 344 ⟵ “COMM 344 - Introduction to Media Industries”
  - courses: COMM 345 ⟵ “COMM 345 - Media Audiences”
  - courses: COMM 361 ⟵ “COMM 361 - Editing Aesthetics”
  - courses: COMM 388 ⟵ “COMM 388 - Motion Picture Aesthetics”
  - courses: COMM 430 ⟵ “COMM 430 - TV Screenwriting”
  - courses: COMM 433 ⟵ “COMM 433 - Capstone”
  - courses: COMM 443 ⟵ “COMM 443 - Hispanic Film”
  - courses: COMM 444 ⟵ “COMM 444 - German Cinema I”
  - courses: COMM 473 ⟵ “COMM 473 - Television and Society”
  - courses: COMM 474 ⟵ “COMM 474 - Reality Television”
  - courses: COMM 482 ⟵ “COMM 482 - Screenwriting II”
### `5830006e2645591e` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-maritime-operations [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: SCLM 495 ⟵ “SCLM 495 - Selected Topics in Supply Chain, Logistics and Maritime Operations ++”
### `5832a3a24f13b5fd` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=strategic-communication-and-journalism-major-strategic-communication [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 303 ⟵ “COMM 303 - Introduction to Strategic Communications”
  - courses: COMM 478 ⟵ “COMM 478 - Media Marketing and Promotion”
### `587542040c9f09fe` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=interdisciplinary-studies-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: IDS 300W ⟵ “IDS 300W - Interdisciplinary Theory and Concepts *”
  - courses: IDS 301 ⟵ “IDS 301 - Data and Humanities Research **”
  - courses: IDS 493 ⟵ “IDS 493 - IDS Electronic Portfolio Project **”
### `5a53981e71827eef` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-internat [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: INBU 463 ⟵ “INBU 463 - International Business Seminar Abroad”
### `602e46a4764d655d` Old Dominion University — degree_requirements 2026-27 · program_key=physical-education-with-a-major-in-prek-12-health-and-physical-education-bs · requirement_key=driver-education-endorsement [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/physical-education-prek-12-health-bs/ (sha256 6f1dba08ef11)
- issues: requirement_groups_skipped
  - courses: HPE 308 ⟵ “HPE 308 - Driver Education Foundations of Traffic Safety”
  - courses: HPE 309 ⟵ “HPE 309 - Principles and Methodologies of Classroom and In-Car Instruction”
### `65155631b32778ef` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=writing-intensive-requirement [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 308W ⟵ “COMM 308W - Effective Media Writing”
  - courses: COMM 315W ⟵ “COMM 315W - Sex, Gender, and Communication”
  - courses: COMM 335W ⟵ “COMM 335W - Rhetorical Criticism”
  - courses: COMM 400W ⟵ “COMM 400W - Intercultural Communication”
  - courses: COMM 412W ⟵ “COMM 412W - Interpersonal Communication Theory and Research”
  - courses: COMM 447W ⟵ “COMM 447W - Electronic Media Law and Policy”
  - courses: COMM 471W ⟵ “COMM 471W - International Film History”
  - courses: COMM 479W ⟵ “COMM 479W - American Film History”
### `656aa90a4dafd1b1` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=internships-and-practicum-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
### `68a79e570705b96a` Old Dominion University — degree_requirements 2026-27 · program_key=women-s-studies-ba · requirement_key=women-s-studies-major-women-s-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/womens-studies/womens-studies-ba/ (sha256 abf03dc3b73c)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, mixed_required_and_choice
  - courses: WGS 201S ⟵ “WGS 201S - Introduction to Women's, Gender, and Sexuality Studies”
  - courses: WGS 301 ⟵ “WGS 301 - Feminist Foundations”
  - courses: WGS 302W ⟵ “WGS 302W - Dimensions of Diversity: Intersectionality Among Women”
  - courses: WGS 390T ⟵ “WGS 390T - Women, Gender, and Technology Worldwide”
  - courses: WGS 400 ⟵ “WGS 400 - History of U.S. Women's Activism”
  - courses: WGS 401W ⟵ “WGS 401W - Women: A Global Perspective”
  - courses: WGS 460W ⟵ “WGS 460W - Feminist and Queer Theory”
  - courses: ENGL 463W ⟵ “ENGL 463W - Women Writers”
  - courses: WGS 303 ⟵ “WGS 303 - Queer Studies”
  - courses: WGS 304 ⟵ “WGS 304 - Gender and Sexuality in Film”
  - courses: WGS 305 ⟵ “WGS 305 - Queer Literature”
  - courses: WGS 306 ⟵ “WGS 306 - Women, the Environment, and Climate Change”
  - courses: WGS 368 ⟵ “WGS 368 - Internship”
  - courses: WGS 395 ⟵ “WGS 395 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 396 ⟵ “WGS 396 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 402 ⟵ “WGS 402 - Feminisms and Sexualities”
  - courses: WGS 405 ⟵ “WGS 405 - Gender and Media”
  - courses: WGS 406 ⟵ “WGS 406 - Gender, Fashion & the Body”
  - courses: WGS 410 ⟵ “WGS 410 - Sexing the Body”
  - courses: WGS 415 ⟵ “WGS 415 - Migration and Refugee Studies”
  - courses: WGS 470 ⟵ “WGS 470 - Feminist Research Methods”
  - courses: WGS 495 ⟵ “WGS 495 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 497 ⟵ “WGS 497 - Independent Study”
  - courses: WGS 498 ⟵ “WGS 498 - Independent Study”
### `69b9cd1501a47f31` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=communication-core-ba-core-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 200S ⟵ “COMM 200S - Introduction to Human Communication”
  - courses: COMM 260 ⟵ “COMM 260 - Understanding Media”
  - courses: COMM 301 ⟵ “COMM 301 - Critical Methodologies”
### `6b589126c2f8a365` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=additional-communication-major-courses-internship [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
### `6b91fa9fd1beac92` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-psychology [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: PSYC 420 ⟵ “PSYC 420 - Cross-Cultural Psychology”
### `6c07ffdb4d2da217` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=additional-communication-major-courses-internship [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
### `7081302f886c6913` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-communications [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: COMM 300 ⟵ “COMM 300 - International Sojourning”
  - courses: COMM 400W ⟵ “COMM 400W - Intercultural Communication”
  - courses: COMM 495 ⟵ “COMM 495 - Topics in Communication ++”
### `71b7a975b4d6edad` Old Dominion University — degree_requirements 2026-27 · program_key=data-science-bs · requirement_key=data-science-areas-of-specialization-required-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-bs/ (sha256 bea76769d765)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: MATH 211 ⟵ “MATH 211 - Calculus I”
  - courses: MATH 212 ⟵ “MATH 212 - Calculus II”
  - courses: MATH 316 ⟵ “MATH 316 - Introductory Linear Algebra”
  - courses: CS 252 ⟵ “CS 252 - Introduction to Unix for Programmers”
  - courses: CS 422 ⟵ “CS 422 - Introduction to Machine Learning”
  - courses: BDA 431 ⟵ “BDA 431 - Modern Statistical Methods for Big Data Analytics”
  - courses: BDA 432 ⟵ “BDA 432 - Introduction to Optimization in Data Science”
  - courses: CS 361 ⟵ “CS 361 - Data Structures and Algorithms”
  - courses: CS 432 ⟵ “CS 432 - Web Science”
  - courses: CS 469 ⟵ “CS 469 - Data Analytics for Cybersecurity”
  - courses: CS 480 ⟵ “CS 480 - Introduction to Artificial Intelligence”
  - courses: CYSE 420 ⟵ “CYSE 420 - Applied Machine Learning in Cybersecurity”
  - courses: DASC 324 ⟵ “DASC 324 - Introduction to Data Visualization”
  - courses: DASC 424 ⟵ “DASC 424 - Data Storytelling”
  - courses: DASC 428 ⟵ “DASC 428 - Introduction to Deep Learning and Modern AI”
  - courses: DASC 446 ⟵ “DASC 446 - Fundamentals of Data Collection and Sourcing”
  - courses: DASC 447 ⟵ “DASC 447 - Practical and Principled Prompt Engineering”
  - courses: DASC 448 ⟵ “DASC 448 - Foundations of Computer Vision”
  - courses: ECE 407 ⟵ “ECE 407 - Introduction to Game Development”
  - courses: GEOG 402 ⟵ “GEOG 402 - Geographic Information Systems”
  - courses: IT 452 ⟵ “IT 452 - Cloud Database”
  - courses: IT 453 ⟵ “IT 453 - Advanced Database Concepts”
  - courses: STAT 331 ⟵ “STAT 331 - Theory of Probability”
  - courses: STAT 405 ⟵ “STAT 405 - Introduction to Data Handling”
  - courses: STAT 437 ⟵ “STAT 437 - Applied Regression and Time Series Analysis”
### `72337bb55145855f` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=strategic-communication-and-journalism-major-foundations [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped, mixed_required_and_choice, choice_rule_unparsed
  - courses: COMM 308W ⟵ “COMM 308W - Effective Media Writing”
### `72f80079aec4987c` Old Dominion University — degree_requirements 2026-27 · program_key=park-recreation-and-tourism-studies-with-a-major-in-park-and-recreation-manageme · requirement_key=core-courses-for-park-recreation-and-tourism-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/park-recreation-tourism-studies-bs/ (sha256 5679c450cf75)
- issues: requirement_groups_skipped
  - courses: PRTS 210S ⟵ “PRTS 210S - Leisure and Human Behavior”
  - courses: PRTS 475 ⟵ “PRTS 475 - Sustainable Management in Parks, Recreation, and Tourism”
  - courses: PRTS 482W ⟵ “PRTS 482W - Evaluation in Parks, Recreation, and Tourism”
  - courses: ACCT 201 ⟵ “ACCT 201 - Principles of Financial Accounting”
  - courses: MGMT 325 ⟵ “MGMT 325 - Contemporary Organizations and Management”
  - courses: MKTG 311 ⟵ “MKTG 311 - Marketing Principles and Problems”
  - courses: PRTS 366 ⟵ “PRTS 366 - Internship Seminar”
  - courses: PRTS 368 ⟵ “PRTS 368 - Internship”
### `73d4b1fae879ae57` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=internships-and-practicum-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
### `756ff84f70986f59` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=strategic-communication-and-journalism-major-applied-theories [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 311 ⟵ “COMM 311 - Strategic Communications Tactics”
  - courses: COMM 323 ⟵ “COMM 323 - Leadership and Events Management”
  - courses: COMM 333 ⟵ “COMM 333 - Persuasion”
  - courses: COMM 454 ⟵ “COMM 454 - Strategic Communications Case Studies”
  - courses: COMM 455 ⟵ “COMM 455 - Critical Analysis of Journalism”
  - courses: COMM 456 ⟵ “COMM 456 - Organizations and Social Influence”
  - courses: COMM 472 ⟵ “COMM 472 - New Media Topics: Theories and Practices”
  - courses: COMM 491 ⟵ “COMM 491 - Communication and Activism”
  - courses: COMM 494 ⟵ “COMM 494 - Entrepreneurship and Public Relations”
  - courses: COMM 495 ⟵ “COMM 495 - Topics in Communication”
  - courses: ENGL 383 ⟵ “ENGL 383 - Digital Journalism”
### `7721a776f924455b` Old Dominion University — degree_requirements 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-industrial-technology-bs · requirement_key=industrial-technology-major-business-cognate [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-industrial-technology-bs/ (sha256 201fc53177e7)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ACCT 201 ⟵ “ACCT 201 - Principles of Financial Accounting”
  - courses: MGMT 325 ⟵ “MGMT 325 - Contemporary Organizations and Management”
  - courses: MGMT 330 ⟵ “MGMT 330 - Organizational Behavior”
  - courses: MKTG 311 ⟵ “MKTG 311 - Marketing Principles and Problems”
### `78982e39ce046d2d` Old Dominion University — degree_requirements 2026-27 · program_key=sport-management-bs · requirement_key=sport-management-major-additional-required-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/sport-management-bs/ (sha256 3de3b3afb84d)
- issues: requirement_groups_skipped
  - courses: ACCT 201 ⟵ “ACCT 201 - Principles of Financial Accounting”
  - courses: ECON 202S ⟵ “ECON 202S - Principles of Microeconomics”
  - courses: MKTG 311 ⟵ “MKTG 311 - Marketing Principles and Problems”
  - courses: MGMT 325 ⟵ “MGMT 325 - Contemporary Organizations and Management”
### `7b9f10e25af041e3` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-technical-and-professional-writing-ba · requirement_key=english-core-required-literature-and-cultural-studies-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-technical-and-professional-writing-ba/ (sha256 24304c241949)
- issues: requirement_groups_skipped
  - courses: ENGL 301 ⟵ “ENGL 301 - Introduction to British Literature I”
  - courses: ENGL 302 ⟵ “ENGL 302 - Introduction to British Literature II”
  - courses: ENGL 303 ⟵ “ENGL 303 - Shakespeare and Comedy”
  - courses: ENGL 304 ⟵ “ENGL 304 - Shakespeare and Tragedy”
  - courses: ENGL 340 ⟵ “ENGL 340 - American Drama”
  - courses: ENGL 342 ⟵ “ENGL 342 - Southern Literature”
  - courses: ENGL 345 ⟵ “ENGL 345 - American Literature to 1860”
  - courses: ENGL 346 ⟵ “ENGL 346 - American Literature Since 1860”
  - courses: ENGL 360 ⟵ “ENGL 360 - World Literature I”
  - courses: ENGL 363 ⟵ “ENGL 363 - World Literature II”
  - courses: ENGL 407 ⟵ “ENGL 407 - Chaucer's Canterbury Tales”
  - courses: ENGL 416 ⟵ “ENGL 416 - English Renaissance Drama”
  - courses: ENGL 418W ⟵ “ENGL 418W - Jewish Writers”
  - courses: ENGL 419 ⟵ “ENGL 419 - The Harlem Renaissance”
  - courses: ENGL 421 ⟵ “ENGL 421 - British Literature 1660-1800”
  - courses: ENGL 423 ⟵ “ENGL 423 - The Romantic Movement in Britain”
  - courses: ENGL 432 ⟵ “ENGL 432 - Origins and Early Development of the British Novel to 1800”
  - courses: ENGL 433 ⟵ “ENGL 433 - Victorian Literature”
  - courses: ENGL 438 ⟵ “ENGL 438 - The Twentieth-Century British Novel”
  - courses: ENGL 441 ⟵ “ENGL 441 - American Travel Literature”
  - courses: ENGL 447 ⟵ “ENGL 447 - The American Novel to 1920”
  - courses: ENGL 448 ⟵ “ENGL 448 - The American Novel 1920 to Present”
  - courses: ENGL 453 ⟵ “ENGL 453 - The Short Story”
  - courses: ENGL 459W ⟵ “ENGL 459W - New Literatures in English”
  - courses: ENGL 461 ⟵ “ENGL 461 - American Poetry of the Early Twentieth Century”
  - … 6 more rows
### `7c4aa9280059df18` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-foreign- [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: CHIN 395 ⟵ “CHIN 395 - Topics in Chinese”
  - courses: CHIN 311 ⟵ “CHIN 311 - Advanced Chinese Language and Culture I”
  - courses: CHIN 312 ⟵ “CHIN 312 - Advanced Chinese Language and Culture II”
  - courses: JAPN 301 ⟵ “JAPN 301 - Intermediate to Advanced Japanese I”
  - courses: JAPN 302 ⟵ “JAPN 302 - Intermediate to Advanced Japanese II”
  - courses: JAPN 309 ⟵ “JAPN 309 - Kanji Skills for Reading Japanese”
  - courses: JAPN 310 ⟵ “JAPN 310 - Japan: A Cultural Odyssey”
  - courses: JAPN 311 ⟵ “JAPN 311 - Global Conversations”
  - courses: JAPN 312W ⟵ “JAPN 312W - Writing Around the World”
  - courses: JAPN 323 ⟵ “JAPN 323 - World Cultures and Contexts”
  - courses: JAPN 335 ⟵ “JAPN 335 - Japanese Society and Language”
  - courses: JAPN 396 ⟵ “JAPN 396 - Topics in Japanese”
  - courses: WCS 310 ⟵ “WCS 310 - Japan: A Cultural Odyssey (Culture class in English)”
### `7d772854fd7f559b` Old Dominion University — degree_requirements 2026-27 · program_key=chemistry-with-a-major-in-chemical-forensic-science-bs · requirement_key=chemistry-core-required-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/sciences/chemistry-biochemistry/chemistry-chemical-forensic-science-bs/ (sha256 2f424b98ebb5)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CHEM 121N ⟵ “CHEM 121N - Foundations of Chemistry I Lecture”
  - courses: CHEM 122N ⟵ “CHEM 122N - Foundations of Chemistry I Laboratory”
  - courses: CHEM 123N ⟵ “CHEM 123N - Foundations of Chemistry II Lecture”
  - courses: CHEM 124N ⟵ “CHEM 124N - Foundations of Chemistry II Laboratory”
  - courses: CHEM 160G ⟵ “CHEM 160G - Introduction to Chemistry and Biochemistry Research and Careers”
  - courses: CHEM 211 ⟵ “CHEM 211 - Organic Chemistry I Lecture”
  - courses: CHEM 212 ⟵ “CHEM 212 - Organic Chemistry I Laboratory”
  - courses: CHEM 213 ⟵ “CHEM 213 - Organic Chemistry II Lecture”
  - courses: CHEM 214 ⟵ “CHEM 214 - Organic Chemistry II Laboratory”
  - courses: CHEM 441 ⟵ “CHEM 441 - Biochemistry Lecture”
### `7e211449360efe7f` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-leadership [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: CPD 400 ⟵ “CPD 400 - Foundations of Leadership”
### `7e3adf60944039b8` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-filipino [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: FAST 395 ⟵ “FAST 395 - Topics in Filipino American Studies”
### `7fbf237b313ca924` Old Dominion University — degree_requirements 2026-27 · program_key=african-american-and-african-studies-ba · requirement_key=upper-division-humanities-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-ba/ (sha256 33b79ef74f7b)
- issues: requirement_groups_skipped
  - courses: AAST/HIST 361 ⟵ “AAST/HIST 361 - African-American History to 1865”
  - courses: AAST 368 ⟵ “AAST 368 - Internship”
  - courses: AAST 395 ⟵ “AAST 395 - Topics in African American Studies”
  - courses: AAST 396 ⟵ “AAST 396 - Topics in African American Studies”
  - courses: ENGL 465W ⟵ “ENGL 465W - African American Literature”
  - courses: HIST 362 ⟵ “HIST 362 - African-American History Since 1865”
  - courses: HIST 370 ⟵ “HIST 370 - Africa and the Atlantic Slave Trade”
  - courses: HIST 455 ⟵ “HIST 455 - African-American Historiography”
  - courses: HIST 475 ⟵ “HIST 475 - Global Africa”
  - courses: MUSC 460 ⟵ “MUSC 460 - History of Jazz”
  - courses: WGS 302W ⟵ “WGS 302W - Dimensions of Diversity: Intersectionality Among Women”
### `80e5d1fac176d83f` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-bs · requirement_key=women-s-and-gender-studies-major-history [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-bs/ (sha256 a576d3c1b66a)
- issues: requirement_groups_skipped
  - courses: HIST 363 ⟵ “HIST 363 - Women in U.S. History”
### `812db0d25822f80c` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=strategic-communication-and-journalism-major-applied-theories [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 311 ⟵ “COMM 311 - Strategic Communications Tactics”
  - courses: COMM 323 ⟵ “COMM 323 - Leadership and Events Management”
  - courses: COMM 333 ⟵ “COMM 333 - Persuasion”
  - courses: COMM 454 ⟵ “COMM 454 - Strategic Communications Case Studies”
  - courses: COMM 455 ⟵ “COMM 455 - Critical Analysis of Journalism”
  - courses: COMM 456 ⟵ “COMM 456 - Organizations and Social Influence”
  - courses: COMM 472 ⟵ “COMM 472 - New Media Topics: Theories and Practices”
  - courses: COMM 491 ⟵ “COMM 491 - Communication and Activism”
  - courses: COMM 494 ⟵ “COMM 494 - Entrepreneurship and Public Relations”
  - courses: COMM 495 ⟵ “COMM 495 - Topics in Communication”
  - courses: ENGL 383 ⟵ “ENGL 383 - Digital Journalism”
### `81c15a9884c82358` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-business [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: MGMT 463 ⟵ “MGMT 463 - Management Seminar Abroad (Korea, Philippines, China and/or other Asian countries)”
  - courses: MKTG 496 ⟵ “MKTG 496 - Selected Topics in Marketing (Asian content)”
### `821568af744a2f8e` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-philosophy-and-religious-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: PHIL 303E ⟵ “PHIL 303E - Business Ethics”
  - courses: PHIL/REL 380 ⟵ “PHIL/REL 380 - Hinduism”
  - courses: PHIL/REL 381 ⟵ “PHIL/REL 381 - Buddhist Traditions”
  - courses: PHIL 482 ⟵ “PHIL 482 - Chinese Religion and Philosophy”
  - courses: PHIL 485 ⟵ “PHIL 485 - Japanese Religion and Philosophy”
  - courses: PHIL/REL 495 ⟵ “PHIL/REL 495 - Topics in Philosophy ++”
  - courses: PHIL/REL 496 ⟵ “PHIL/REL 496 - Topics in Philosophy ++”
  - courses: REL 352 ⟵ “REL 352 - Islam”
### `823abb7c4f98a738` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=asian-studies-major-research-methods [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: HIST 201 ⟵ “HIST 201 - Introduction to Historical Methods”
  - courses: POLS 308 ⟵ “POLS 308 - Research Design”
  - courses: SOC 337 ⟵ “SOC 337 - Social Research Methods”
  - courses: PSYC 317 ⟵ “PSYC 317 - Quantitative Methods”
  - courses: ECON 400 ⟵ “ECON 400 - From Correlation to Causation: Applied Causal Inference”
### `8570962e73f8811a` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=additional-communication-major-courses-capstone [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 433 ⟵ “COMM 433 - Capstone”
### `86ce0a9d000706cb` Old Dominion University — degree_requirements 2026-27 · program_key=data-science-bs · requirement_key=data-science-major-foundation-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-bs/ (sha256 bea76769d765)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, mixed_required_and_choice
  - courses: MATH 163 ⟵ “MATH 163 - Precalculus II **”
  - courses: STAT 130M ⟵ “STAT 130M - Elementary Statistics”
### `875cb2fcd17c1e5d` Old Dominion University — degree_requirements 2026-27 · program_key=data-science-bs · requirement_key=data-science-areas-of-specialization-required-courses-2 [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-bs/ (sha256 bea76769d765)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, mixed_required_and_choice
  - courses: COMM 260 ⟵ “COMM 260 - Understanding Media”
  - courses: COMM 303 ⟵ “COMM 303 - Introduction to Strategic Communications”
  - courses: DASC 324 ⟵ “DASC 324 - Introduction to Data Visualization”
  - courses: DASC 424 ⟵ “DASC 424 - Data Storytelling”
  - courses: IT 150G ⟵ “IT 150G - Basic Information Literacy and Research”
  - courses: IT 325 ⟵ “IT 325 - Web Site and Web Page Design”
  - courses: BNAL 206 ⟵ “BNAL 206 - Business Analytics I”
  - courses: BNAL 306 ⟵ “BNAL 306 - Business Analytics II”
  - courses: BNAL 403 ⟵ “BNAL 403 - Data Visualization and Exploration”
  - courses: COMM 402 ⟵ “COMM 402 - Communicating Data”
  - courses: CRJS 344 ⟵ “CRJS 344 - Social Science and Crime Mapping”
  - courses: CS 361 ⟵ “CS 361 - Data Structures and Algorithms”
  - courses: CS 432 ⟵ “CS 432 - Web Science”
  - courses: DASC 312 ⟵ “DASC 312 - The Art of Data Visualization”
  - courses: ECE 406 ⟵ “ECE 406 - Computer Graphics and Visualization”
  - courses: ECE 407 ⟵ “ECE 407 - Introduction to Game Development”
  - courses: ENGL 307T ⟵ “ENGL 307T - Digital Writing”
  - courses: GAME 201T ⟵ “GAME 201T - Introduction to Game Studies”
  - courses: GAME 340 ⟵ “GAME 340 - Visual Design and Digital Graphics for Games”
  - courses: GAME 440 ⟵ “GAME 440 - Advanced Visual Design and Digital Graphics for Games”
  - courses: GEOG 300 ⟵ “GEOG 300 - Maps and Geographic Information”
  - courses: IT 452 ⟵ “IT 452 - Cloud Database”
  - courses: IT 453 ⟵ “IT 453 - Advanced Database Concepts”
### `87efbb7a427fa35b` Old Dominion University — degree_requirements 2026-27 · program_key=career-and-technical-education-with-a-major-in-marketing-education-bs · requirement_key=licensure-endorsement-programs [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-marketing-bs/ (sha256 c38ad1d36dc9)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: SEPS 297 ⟵ “SEPS 297 - Observation and Participation”
  - courses: SPED 313 ⟵ “SPED 313 - Fundamentals of Human Growth and Development: Birth through Adolescence”
  - courses: TLED 408 ⟵ “TLED 408 - Reading and Writing in Content Areas”
  - courses: SEPS 485 ⟵ “SEPS 485 - Student Teaching”
### `87f97560003f65b7` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=writing-intensive-requirement [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 308W ⟵ “COMM 308W - Effective Media Writing”
  - courses: COMM 315W ⟵ “COMM 315W - Sex, Gender, and Communication”
  - courses: COMM 335W ⟵ “COMM 335W - Rhetorical Criticism”
  - courses: COMM 400W ⟵ “COMM 400W - Intercultural Communication”
  - courses: COMM 412W ⟵ “COMM 412W - Interpersonal Communication Theory and Research”
  - courses: COMM 447W ⟵ “COMM 447W - Electronic Media Law and Policy”
  - courses: COMM 471W ⟵ “COMM 471W - International Film History”
  - courses: COMM 479W ⟵ “COMM 479W - American Film History”
### `89546c44c3b463d5` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-supply-chain-and-maritime-logistics-bs · requirement_key=supply-chain-and-maritime-logistics-major-major-coursework [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-supply-chain-and-maritime-logistics-bs/ (sha256 0c18deed219f)
- issues: requirement_groups_skipped
  - courses: SCLM 301 ⟵ “SCLM 301 - Supply Chain Analytics”
  - courses: SCLM/CPD 303T ⟵ “SCLM/CPD 303T - Maritime Leadership, Technology, and Society”
  - courses: SCLM 370 ⟵ “SCLM 370 - Global Logistics”
  - courses: SCLM 414 ⟵ “SCLM 414 - Maritime Operations”
  - courses: SCLM 430 ⟵ “SCLM 430 - Global Sourcing and Supply Market Analysis”
  - courses: SCLM 450 ⟵ “SCLM 450 - Supply Chain 4.0 Technologies and Innovations”
  - courses: SCLM 461 ⟵ “SCLM 461 - Warehousing, Distribution and Material Management”
  - courses: SCLM 368 ⟵ “SCLM 368 - Internship in Supply Chain, Logistics, and Maritime Operations”
### `8ab3250a9e314e4b` Old Dominion University — degree_requirements 2026-27 · program_key=sport-management-bs · requirement_key=sport-management-major-sport-management [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/sport-management-bs/ (sha256 3de3b3afb84d)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: SMGT 214 ⟵ “SMGT 214 - Introduction to Sport Management *”
  - courses: SMGT 305 ⟵ “SMGT 305 - Sport Administrative Theory *”
  - courses: SMGT 312 ⟵ “SMGT 312 - Sport Sales *”
  - courses: SMGT 315 ⟵ “SMGT 315 - Sport Media and Public Relations *”
  - courses: SMGT 331 ⟵ “SMGT 331 - Fiscal Planning and Management in Sport and Recreation *”
  - courses: SMGT 369 ⟵ “SMGT 369 - Sport Management Pre-Internship *”
  - courses: SMGT 414 ⟵ “SMGT 414 - Sport Marketing *”
  - courses: SMGT 421 ⟵ “SMGT 421 - Legal Aspects in Recreation and Sport Management *”
  - courses: SMGT 432 ⟵ “SMGT 432 - Sport Facility and Event Management *”
  - courses: SMGT 450W ⟵ “SMGT 450W - Ethics and Morality in Sport **”
  - courses: SMGT 455 ⟵ “SMGT 455 - Sport in Contemporary Society *”
  - courses: SMGT 468 ⟵ “SMGT 468 - Sport Management Internship *”
### `8b573c49e5285000` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-economic [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: ECON 450 ⟵ “ECON 450 - International Economics”
  - courses: ECON 454W ⟵ “ECON 454W - Economic Development”
  - courses: ECON 495 ⟵ “ECON 495 - Selected Topics in Economics (Asian content)”
### `8b8cae3a975c2719` Old Dominion University — degree_requirements 2026-27 · program_key=park-recreation-and-tourism-studies-with-a-major-in-park-and-recreation-manageme · requirement_key=park-and-recreation-management-major-park-and-recreation-management [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/park-recreation-tourism-studies-bs/ (sha256 5679c450cf75)
- issues: requirement_groups_skipped
  - courses: PAS 300 ⟵ “PAS 300 - Foundations of Public Service”
  - courses: PRTS 251 ⟵ “PRTS 251 - Introduction to Park and Recreation Management *”
  - courses: PRTS 302 ⟵ “PRTS 302 - Facilitating the Recreation Experience”
  - courses: PRTS 404 ⟵ “PRTS 404 - Recreation Resource Management”
  - courses: PRTS 405 ⟵ “PRTS 405 - Outdoor Recreation”
  - courses: PRTS 433 ⟵ “PRTS 433 - Camp Administration”
### `8df37499cc156684` Old Dominion University — degree_requirements 2026-27 · program_key=early-childhood-education-bs · requirement_key=early-childhood-education-major-core-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/teaching-learning/early-childhood-education-bs/ (sha256 6ccb7afd4afa)
- issues: requirement_groups_skipped
  - courses: TLED 301 ⟵ “TLED 301 - Foundations and Introduction to Assessment of Education *”
  - courses: SPED 400 ⟵ “SPED 400 - Foundations of Special Education: Legal Aspects and Characteristics”
  - courses: SPED 411 ⟵ “SPED 411 - Classroom and Behavioral Management Techniques for Students with Diverse Needs”
  - courses: FOUN 301 ⟵ “FOUN 301 - Learning and Development”
  - courses: FOUN 302 ⟵ “FOUN 302 - Assessment of Learning”
  - courses: TLED 326 ⟵ “TLED 326 - Socio-Cultural Perspectives in Education”
  - courses: TLED 426 ⟵ “TLED 426 - Introduction to Literacy, Linguistics and Practice in the Classroom”
  - courses: TLED 430W ⟵ “TLED 430W - PK-12 Instructional Technology (C or better required; satisfies Impact of Technology requirement)”
### `8ea494af6ee46df7` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-world-languages-and-cultures [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: CHIN 311 ⟵ “CHIN 311 - Advanced Chinese Language and Culture I”
  - courses: CHIN 312 ⟵ “CHIN 312 - Advanced Chinese Language and Culture II”
  - courses: CHIN 395 ⟵ “CHIN 395 - Topics in Chinese”
  - courses: CHIN 396 ⟵ “CHIN 396 - Topics in Chinese”
  - courses: CHIN 495 ⟵ “CHIN 495 - Topics in Chinese”
  - courses: JAPN 301 ⟵ “JAPN 301 - Intermediate to Advanced Japanese I”
  - courses: JAPN 302 ⟵ “JAPN 302 - Intermediate to Advanced Japanese II”
  - courses: JAPN 309 ⟵ “JAPN 309 - Kanji Skills for Reading Japanese”
  - courses: JAPN 310 ⟵ “JAPN 310 - Japan: A Cultural Odyssey”
  - courses: JAPN 311 ⟵ “JAPN 311 - Global Conversations”
  - courses: JAPN 312W ⟵ “JAPN 312W - Writing Around the World”
  - courses: JAPN 323 ⟵ “JAPN 323 - World Cultures and Contexts”
  - courses: JAPN 335 ⟵ “JAPN 335 - Japanese Society and Language”
  - courses: JAPN 395 ⟵ “JAPN 395 - Topics in Japanese”
  - courses: JAPN 396 ⟵ “JAPN 396 - Topics in Japanese”
  - courses: JAPN 422 ⟵ “JAPN 422 - Analyzing Japanese Conversation”
  - courses: JAPN 445 ⟵ “JAPN 445 - Japanese Language Acquisition and Teaching”
  - courses: JAPN 495 ⟵ “JAPN 495 - Topics in Japanese”
### `8f09d6b0e6c097df` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-communic [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: COMM 300 ⟵ “COMM 300 - International Sojourning”
  - courses: COMM 400W ⟵ “COMM 400W - Intercultural Communication”
### `8f8cb7fa58d3bbb2` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-technical-and-professional-writing-ba · requirement_key=technical-and-professional-writing-major-technical-and-professional-writing [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-technical-and-professional-writing-ba/ (sha256 24304c241949)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: ENGL 334W ⟵ “ENGL 334W - Technical Writing”
  - courses: ENGL 335 ⟵ “ENGL 335 - Editing and Document Design”
  - courses: ENGL 368 ⟵ “ENGL 368 - English Internship”
  - courses: ENGL 435W ⟵ “ENGL 435W - Management Writing”
  - courses: ENGL 327W ⟵ “ENGL 327W - Advanced Composition”
  - courses: ENGL 427W ⟵ “ENGL 427W - Writing in the Disciplines”
  - courses: ENGL 436 ⟵ “ENGL 436 - Writing for the Government”
  - courses: ENGL 439 ⟵ “ENGL 439 - Usability and User Experience”
  - courses: ENGL 468 ⟵ “ENGL 468 - Advanced English Internship”
  - courses: ENGL 495 ⟵ “ENGL 495 - Topics in English *”
### `92cbb7a95d55a8b0` Old Dominion University — degree_requirements 2026-27 · program_key=career-and-technical-education-with-a-major-in-technology-education-bs · requirement_key=technology-education-major-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-technology-bs/ (sha256 96e93c2cb7e2)
- issues: requirement_groups_skipped
  - section: technology-education-major-electives ⟵ “Technology Education Major — Electives”
### `92f6cdfc9d1fdc65` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=special-topics-in-communication-courses-and-communication-tutorials [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 395 ⟵ “COMM 395 - Topics in Communication”
  - courses: COMM 396 ⟵ “COMM 396 - Topics in Communication”
  - courses: COMM 495 ⟵ “COMM 495 - Topics in Communication”
  - courses: COMM 496 ⟵ “COMM 496 - Topics in Communication”
  - courses: COMM 497 ⟵ “COMM 497 - Tutorial Work in Special Topics in Communication”
### `949d918a7b7b410b` Old Dominion University — degree_requirements 2026-27 · program_key=physical-education-with-a-major-in-coaching-and-physical-activity-leadership-bs · requirement_key=coaching-in-physical-activity-and-leadership-major-coaching-and-physical-educati [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/physical-education-coaching-and-physical-activity-leadership-bs/ (sha256 62cb31f9a532)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIOL 240 ⟵ “BIOL 240 - Fundamentals of Anatomy and Physiology I”
  - courses: TLED 430W ⟵ “TLED 430W - PK-12 Instructional Technology”
  - courses: HPE 200 ⟵ “HPE 200 - Foundations of Education, Physical Education and Health”
  - courses: HPE 218 ⟵ “HPE 218 - Aquatics and Outdoor Education”
  - courses: HPE 220 ⟵ “HPE 220 - Teaching of Team Sports”
  - courses: HPE 222 ⟵ “HPE 222 - Teaching Individual Sports and Dance”
  - courses: HPE 300 ⟵ “HPE 300 - Teaching Elementary Physical Education”
  - courses: HPE 301W ⟵ “HPE 301W - Methods and Materials in Teaching Physical Education”
  - courses: HPE 317 ⟵ “HPE 317 - Human Growth & Motor Development”
  - courses: HPE 318 ⟵ “HPE 318 - Motor Learning”
  - courses: HPE 324 ⟵ “HPE 324 - Teaching Injury Care for Sports”
  - courses: HPE 400 ⟵ “HPE 400 - Management Skills for Teaching Health and Physical Education”
  - courses: HPE 404 ⟵ “HPE 404 - Adapted Physical Education”
  - courses: HPE 406 ⟵ “HPE 406 - Tests and Measurement in Physical Education and Health”
  - courses: HPE 409 ⟵ “HPE 409 - Physiology of Exercise”
  - courses: HPE 415 ⟵ “HPE 415 - Principles of Coaching Management”
  - courses: HPE 430 ⟵ “HPE 430 - Nutrition and Fitness Education”
  - courses: HPE 456 ⟵ “HPE 456 - Sports Psychology”
  - courses: HPE 368 ⟵ “HPE 368 - Coaching Internship”
  - courses: SMGT 315 ⟵ “SMGT 315 - Sport Media and Public Relations”
  - courses: SMGT 331 ⟵ “SMGT 331 - Fiscal Planning and Management in Sport and Recreation”
  - courses: SMGT 414 ⟵ “SMGT 414 - Sport Marketing”
  - courses: SMGT 432 ⟵ “SMGT 432 - Sport Facility and Event Management”
### `96d4a9f0d8e121fb` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=communication-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 103R ⟵ “COMM 103R - Voice and Diction”
  - courses: COMM 112R ⟵ “COMM 112R - Introduction to Interpersonal Communication”
  - courses: COMM 195 ⟵ “COMM 195 - Topics in Communication”
  - courses: COMM 225 ⟵ “COMM 225 - Introduction to Production Technology”
  - courses: COMM 269 ⟵ “COMM 269 - Visual Storytelling”
  - courses: COMM 270A ⟵ “COMM 270A - Film Appreciation”
  - courses: COMM 271 ⟵ “COMM 271 - Introduction to Filmmaking”
  - courses: COMM 272G ⟵ “COMM 272G - Digital Literacy”
  - courses: COMM 280T ⟵ “COMM 280T - Entertainment Technologies”
  - courses: COMM 295 ⟵ “COMM 295 - Topics in Communication”
  - courses: COMM 304 ⟵ “COMM 304 - Advanced Public Speaking”
  - courses: COMM 307 ⟵ “COMM 307 - Understanding European Film”
  - courses: COMM 321 ⟵ “COMM 321 - Production Management for Television and Stage”
  - courses: COMM 325 ⟵ “COMM 325 - Sound Design for Stage and Camera”
  - courses: COMM 341 ⟵ “COMM 341 - Lighting Design for Stage and Film”
  - courses: COMM 349 ⟵ “COMM 349 - Costume Design for Stage and Camera”
  - courses: COMM 354 ⟵ “COMM 354 - Drafting and Rendering for Stage and Screen”
  - courses: COMM 356 ⟵ “COMM 356 - 3D Animation”
  - courses: COMM 357 ⟵ “COMM 357 - 3D Animation 2”
  - courses: COMM 359 ⟵ “COMM 359 - Costume Crafts”
  - courses: COMM 367 ⟵ “COMM 367 - Cooperative Education”
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
  - courses: COMM 382 ⟵ “COMM 382 - Reporting News for Television and Digital Media”
  - courses: COMM 453 ⟵ “COMM 453 - Voice Over”
### `9a28bc3d4585bef4` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-ba · requirement_key=women-s-and-gender-studies-major-english [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-ba/ (sha256 359f7abf5fe7)
- issues: requirement_groups_skipped
  - courses: ENGL 463W ⟵ “ENGL 463W - Women Writers”
  - courses: ENGL 477 ⟵ “ENGL 477 - Language, Gender and Power”
### `9b37f10b7cdc5ec4` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-bs · requirement_key=women-s-and-gender-studies-major-english [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-bs/ (sha256 a576d3c1b66a)
- issues: requirement_groups_skipped
  - courses: ENGL 463W ⟵ “ENGL 463W - Women Writers”
  - courses: ENGL 477 ⟵ “ENGL 477 - Language, Gender and Power”
### `9d059c43023bff82` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=additional-communication-major-courses-internship [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
### `9dc8b48b825f1216` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=communication-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 103R ⟵ “COMM 103R - Voice and Diction”
  - courses: COMM 112R ⟵ “COMM 112R - Introduction to Interpersonal Communication”
  - courses: COMM 195 ⟵ “COMM 195 - Topics in Communication”
  - courses: COMM 225 ⟵ “COMM 225 - Introduction to Production Technology”
  - courses: COMM 269 ⟵ “COMM 269 - Visual Storytelling”
  - courses: COMM 270A ⟵ “COMM 270A - Film Appreciation”
  - courses: COMM 271 ⟵ “COMM 271 - Introduction to Filmmaking”
  - courses: COMM 272G ⟵ “COMM 272G - Digital Literacy”
  - courses: COMM 280T ⟵ “COMM 280T - Entertainment Technologies”
  - courses: COMM 295 ⟵ “COMM 295 - Topics in Communication”
  - courses: COMM 304 ⟵ “COMM 304 - Advanced Public Speaking”
  - courses: COMM 307 ⟵ “COMM 307 - Understanding European Film”
  - courses: COMM 321 ⟵ “COMM 321 - Production Management for Television and Stage”
  - courses: COMM 325 ⟵ “COMM 325 - Sound Design for Stage and Camera”
  - courses: COMM 341 ⟵ “COMM 341 - Lighting Design for Stage and Film”
  - courses: COMM 349 ⟵ “COMM 349 - Costume Design for Stage and Camera”
  - courses: COMM 354 ⟵ “COMM 354 - Drafting and Rendering for Stage and Screen”
  - courses: COMM 356 ⟵ “COMM 356 - 3D Animation 1”
  - courses: COMM 357 ⟵ “COMM 357 - 3D Animation 2”
  - courses: COMM 359 ⟵ “COMM 359 - Costume Crafts”
  - courses: COMM 367 ⟵ “COMM 367 - Cooperative Education”
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
  - courses: COMM 382 ⟵ “COMM 382 - Reporting News for Television and Digital Media”
  - courses: COMM 453 ⟵ “COMM 453 - Voice Over”
### `9f77c252f6a572cb` Old Dominion University — degree_requirements 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-industrial-technology-bs · requirement_key=industrial-technology-major-supervision [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-industrial-technology-bs/ (sha256 201fc53177e7)
- issues: requirement_groups_skipped
  - courses: HMSV 339 ⟵ “HMSV 339 - Interpersonal Relations”
  - courses: SEPS 302 ⟵ “SEPS 302 - Workforce Supervision Management”
  - courses: SEPS 400 ⟵ “SEPS 400 - Instructional Systems Development”
  - courses: SEPS 402 ⟵ “SEPS 402 - Instructional Methods in Occupational Studies”
  - courses: SEPS 405 ⟵ “SEPS 405 - Directed Work Experience (Internship)”
  - courses: SEPS 481 ⟵ “SEPS 481 - Career and Professional Development”
  - courses: STEM 365 ⟵ “STEM 365 - Safety and OSHA Certification”
  - courses: STEM 370T ⟵ “STEM 370T - Technology and Society (Writing Intensive) *”
### `a180429726248717` Old Dominion University — degree_requirements 2026-27 · program_key=music-with-a-major-in-jazz-studies-bm · requirement_key=jazz-studies-major-additional-requirements [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/music/jazz-studies-bm/ (sha256 93a26dd823ef)
- issues: requirement_groups_skipped
  - courses: MUSC 101 ⟵ “MUSC 101 - Class Piano I”
  - courses: MUSC 102 ⟵ “MUSC 102 - Class Piano II”
  - courses: MUSA 139 ⟵ “MUSA 139 - Half-Hour Applied Lesson”
  - courses: MUSA 140 ⟵ “MUSA 140 - Half-Hour Applied Lesson”
  - courses: MUSC 230 ⟵ “MUSC 230 - Jazz Keyboard Techniques”
  - courses: MUSC 326 ⟵ “MUSC 326 - Jazz Theory and Aural Skills”
  - courses: MUSC 333 ⟵ “MUSC 333 - Music Business and Entrepreneurship”
  - courses: MUSC 337 ⟵ “MUSC 337 - Jazz Improvisation I”
  - courses: MUSC 338 ⟵ “MUSC 338 - Jazz Improvisation II”
  - courses: MUSC 417 ⟵ “MUSC 417 - Jazz Pedagogy and Conducting”
  - courses: MUSC 418 ⟵ “MUSC 418 - Jazz Arranging”
  - courses: MUSC 419 ⟵ “MUSC 419 - Jazz Performance Practice Workshop”
  - courses: MUSC 460 ⟵ “MUSC 460 - History of Jazz”
### `a18aaea5ad118f86` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=additional-communication-major-courses-capstone [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 433 ⟵ “COMM 433 - Capstone”
### `a18bb055df333486` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-history [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ASIA/HIST 336 ⟵ “ASIA/HIST 336 - The Emergence of New China”
  - courses: ASIA 337 ⟵ “ASIA 337 - Japan's Era of Transformation”
  - courses: HIST 316 ⟵ “HIST 316 - Cold War in History”
  - courses: HIST 330 ⟵ “HIST 330 - Modern South Asia, c. 1700 to Present”
  - courses: HIST 396 ⟵ “HIST 396 - Topics in History ++”
  - courses: HIST 495 ⟵ “HIST 495 - Topics in History ++”
### `a4324a8a7e5f597c` Old Dominion University — degree_requirements 2026-27 · program_key=chemistry-with-a-major-in-chemical-forensic-science-bs · requirement_key=chemistry-core-other-required-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/sciences/chemistry-biochemistry/chemistry-chemical-forensic-science-bs/ (sha256 2f424b98ebb5)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 211 ⟵ “MATH 211 - Calculus I”
  - courses: MATH 212 ⟵ “MATH 212 - Calculus II”
### `a5411d2ae9a5739d` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=additional-communication-major-courses-study-abroad [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 300 ⟵ “COMM 300 - International Sojourning”
  - courses: COMM 440 ⟵ “COMM 440 - Documentary Filmmaking Study Abroad”
### `a59957a4e8dcb5b0` Old Dominion University — degree_requirements 2026-27 · program_key=career-and-technical-education-with-a-major-in-marketing-education-bs · requirement_key=marketing-education-major-marketing-education [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-marketing-bs/ (sha256 c38ad1d36dc9)
- issues: requirement_groups_skipped
  - courses: ECON 200S ⟵ “ECON 200S - Basic Economics”
  - courses: MGMT 325 ⟵ “MGMT 325 - Contemporary Organizations and Management”
  - courses: MKTG 311 ⟵ “MKTG 311 - Marketing Principles and Problems”
  - courses: MKTG 402 ⟵ “MKTG 402 - Consumer Behavior”
  - courses: SEPS 100 ⟵ “SEPS 100 - Sales Techniques”
  - courses: SEPS 102 ⟵ “SEPS 102 - Advertising and Promotion”
  - courses: SEPS 297 ⟵ “SEPS 297 - Observation and Participation”
  - courses: SEPS 400 ⟵ “SEPS 400 - Instructional Systems Development”
  - courses: SEPS 401 ⟵ “SEPS 401 - Foundations of Career and Technical Education”
  - courses: SEPS 402 ⟵ “SEPS 402 - Instructional Methods in Occupational Studies”
  - courses: SEPS 405 ⟵ “SEPS 405 - Directed Work Experience”
  - courses: SEPS 415 ⟵ “SEPS 415 - Advanced Merchandising”
  - courses: SEPS 485 ⟵ “SEPS 485 - Student Teaching”
  - courses: STEM 251G ⟵ “STEM 251G - Computer Literacy: Communication and Information”
  - courses: STEM 351 ⟵ “STEM 351 - Communication Technology”
### `a7df25d95a0654d0` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-business-management-and-marketing [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: MGMT 361 ⟵ “MGMT 361 - International Business Operations”
  - courses: MGMT 463 ⟵ “MGMT 463 - Management Seminar Abroad”
### `a932edcaa791eab2` Old Dominion University — degree_requirements 2026-27 · program_key=music-with-a-major-in-jazz-studies-bm · requirement_key=jazz-studies-major-departmental-requirements [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/music/jazz-studies-bm/ (sha256 93a26dd823ef)
- issues: requirement_groups_skipped
  - courses: MUSC 150 ⟵ “MUSC 150 - Freshman Seminar for Music Students”
  - courses: MUSC 160 ⟵ “MUSC 160 - Music and Ideas”
  - courses: MUSC 221 ⟵ “MUSC 221 - Music Theory 1 *”
  - courses: MUSC 222 ⟵ “MUSC 222 - Music Theory 2 *”
  - courses: MUSC 223 ⟵ “MUSC 223 - Aural Skills 1 *”
  - courses: MUSC 224 ⟵ “MUSC 224 - Aural Skills 2 *”
  - courses: MUSC 266 ⟵ “MUSC 266 - Music in World Cultures”
  - courses: MUSC 309 ⟵ “MUSC 309 - Principles of Conducting”
  - courses: MUSC 321 ⟵ “MUSC 321 - Music Theory 3 *”
  - courses: MUSC 323 ⟵ “MUSC 323 - Aural Skills 3 *”
  - courses: MUSC 335T ⟵ “MUSC 335T - Music Technology Survey (Satisfies Impact of Technology)”
  - courses: MUSC 361 ⟵ “MUSC 361 - History of Western Art Music from Ancient through Baroque **”
  - courses: MUSC 362W ⟵ “MUSC 362W - History of Western Art Music from Classical through Modern *”
  - courses: MUSA 141 ⟵ “MUSA 141 - Hour Lesson”
  - courses: MUSA 142 ⟵ “MUSA 142 - Hour Lesson”
  - courses: MUSA 241 ⟵ “MUSA 241 - Hour Lesson”
  - courses: MUSA 242 ⟵ “MUSA 242 - Hour Lesson”
  - courses: MUSA 341 ⟵ “MUSA 341 - Hour Lesson”
  - courses: MUSA 342 ⟵ “MUSA 342 - Hour Lesson”
  - courses: MUSA 441 ⟵ “MUSA 441 - Hour Lesson”
  - courses: MUSA 442 ⟵ “MUSA 442 - Hour Lesson”
### `acdca7d96f554f26` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-geography [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: GEOG 453 ⟵ “GEOG 453 - Asia”
  - courses: GEOG 495 ⟵ “GEOG 495 - Topics in Geography ++”
### `acf26ea4a9500353` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=cinema-screenwriting-and-studies-major-applied-theories [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text, mixed_required_and_choice
  - courses: COMM 471W ⟵ “COMM 471W - International Film History”
  - courses: COMM 485 ⟵ “COMM 485 - Film and Television Genres”
  - courses: COMM 307 ⟵ “COMM 307 - Understanding European Film”
  - courses: COMM 334 ⟵ “COMM 334 - Narrative Adaptation”
  - courses: COMM 344 ⟵ “COMM 344 - Introduction to Media Industries”
  - courses: COMM 345 ⟵ “COMM 345 - Media Audiences”
  - courses: COMM 361 ⟵ “COMM 361 - Editing Aesthetics”
  - courses: COMM 388 ⟵ “COMM 388 - Motion Picture Aesthetics”
  - courses: COMM 430 ⟵ “COMM 430 - TV Screenwriting”
  - courses: COMM 433 ⟵ “COMM 433 - Capstone”
  - courses: COMM 443 ⟵ “COMM 443 - Hispanic Film”
  - courses: COMM 444 ⟵ “COMM 444 - German Cinema I”
  - courses: COMM 473 ⟵ “COMM 473 - Television and Society”
  - courses: COMM 474 ⟵ “COMM 474 - Reality Television”
  - courses: COMM 482 ⟵ “COMM 482 - Screenwriting II”
### `adcddd8d91d8ab5e` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=strategic-communication-and-journalism-major-foundations [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped, mixed_required_and_choice, choice_rule_unparsed
  - courses: COMM 308W ⟵ “COMM 308W - Effective Media Writing”
### `af0859fe3762382e` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-general-studies-bs · requirement_key=interdisciplinary-studies-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-general-studies-bs/ (sha256 616940b1bd39)
- issues: requirement_groups_skipped
  - courses: IDS 300W ⟵ “IDS 300W - Interdisciplinary Theory and Concepts *”
  - courses: IDS 301 ⟵ “IDS 301 - Data and Humanities Research **”
  - courses: IDS 493 ⟵ “IDS 493 - IDS Electronic Portfolio Project **”
### `b03ff98139be3328` Old Dominion University — degree_requirements 2026-27 · program_key=career-and-technical-education-with-a-major-in-marketing-education-bs · requirement_key=marketing-education-major-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/career-technical-education-marketing-bs/ (sha256 c38ad1d36dc9)
- issues: requirement_groups_skipped
  - section: marketing-education-major-electives ⟵ “Marketing Education Major — Electives”
### `b9cc918e74e13a44` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=additional-communication-major-courses-roar [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped, mixed_required_and_choice, choice_rule_unparsed
  - courses: COMM 490 ⟵ “COMM 490 - ROAR Communications Agency (available only for Strategic Communication and Journalism majors)”
  - courses: COMM 439 ⟵ “COMM 439 - WHRO Production”
  - courses: COMM 482 ⟵ “COMM 482 - Screenwriting II”
  - courses: COMM 483 ⟵ “COMM 483 - Advanced Cinema Projects”
  - courses: COMM 486 ⟵ “COMM 486 - Advanced Filmmaking”
  - courses: COMM 493 ⟵ “COMM 493 - Feature Film Production”
### `ba60f557111fcca9` Old Dominion University — degree_requirements 2026-27 · program_key=exercise-science-bs · requirement_key=exercise-science-major-exercise-science [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/health-sciences/exercise-science/exercise-science-bs/ (sha256 39f7d122aeba)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIOL 240 ⟵ “BIOL 240 - Fundamentals of Anatomy and Physiology I”
  - courses: BIOL 241 ⟵ “BIOL 241 - Fundamentals of Anatomy and Physiology II”
  - courses: EXSC 225 ⟵ “EXSC 225 - Introduction to Exercise Science”
  - courses: EXSC 250 ⟵ “EXSC 250 - Strength and Conditioning Leadership”
  - courses: EXSC 310 ⟵ “EXSC 310 - Gross Anatomy for Exercise Science”
  - courses: EXSC 322 ⟵ “EXSC 322 - Anatomical Kinesiology and Musculoskeletal Injuries”
  - courses: EXSC 326 ⟵ “EXSC 326 - Exercise Physiology I”
  - courses: EXSC 327 ⟵ “EXSC 327 - Exercise Physiology II”
  - courses: EXSC 366 ⟵ “EXSC 366 - Exercise Science Seminar”
  - courses: EXSC 408 ⟵ “EXSC 408 - Nutrition for Fitness and Sport”
  - courses: EXSC 415 ⟵ “EXSC 415 - Exercise Testing for Normal and Special Populations”
  - courses: EXSC 417 ⟵ “EXSC 417 - Biomechanics”
  - courses: EXSC 428 ⟵ “EXSC 428 - Exercise Prescription for Chronic Disease”
  - courses: EXSC 431W ⟵ “EXSC 431W - Wellness Programming and Administration *”
  - courses: PHYS 111N ⟵ “PHYS 111N - Introductory General Physics”
### `bb838291c6a90602` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-geograph [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: GEOG 453 ⟵ “GEOG 453 - Asia”
### `bbfbce43c791738d` Old Dominion University — degree_requirements 2026-27 · program_key=african-american-and-african-studies-ba · requirement_key=upper-division-social-science-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-ba/ (sha256 33b79ef74f7b)
- issues: requirement_groups_skipped
  - courses: AAST 310 ⟵ “AAST 310 - Human Rights and Social Change in Africa”
  - courses: AAST/POLS 316 ⟵ “AAST/POLS 316 - Politics of Africa”
  - courses: AAST/SOC 323 ⟵ “AAST/SOC 323 - Sociology of Minority Families”
  - courses: AAST 368 ⟵ “AAST 368 - Internship”
  - courses: AAST 395 ⟵ “AAST 395 - Topics in African American Studies”
  - courses: AAST 396 ⟵ “AAST 396 - Topics in African American Studies”
  - courses: AAST/POLS 412 ⟵ “AAST/POLS 412 - Politics of the Civil Rights Movement”
  - courses: AAST/SOC 426 ⟵ “AAST/SOC 426 - Minority Group Relations”
  - courses: AAST/CRJS/SOC 452 ⟵ “AAST/CRJS/SOC 452 - Diversity in Criminal Justice Organizations”
  - courses: AAST/PSYC 460 ⟵ “AAST/PSYC 460 - Psychology of African Americans”
  - courses: CRJS 450 ⟵ “CRJS 450 - Blacks, Crime and Justice”
  - courses: GEOG 452 ⟵ “GEOG 452 - Africa”
  - courses: POLS 309 ⟵ “POLS 309 - Race, Culture and Public Policy”
  - courses: POLS 410 ⟵ “POLS 410 - African American Politics”
  - courses: POLS 439 ⟵ “POLS 439 - International Relations of African States”
  - courses: POLS 470 ⟵ “POLS 470 - African Americans and Foreign Affairs”
  - courses: SOC/CRJS 444 ⟵ “SOC/CRJS 444 - Community Justice”
### `bc74f209eee54989` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=strategic-communication-and-journalism-major-comm-elective [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - section: strategic-communication-and-journalism-major-comm-elective ⟵ “Strategic Communication and Journalism Major — COMM Elective”
### `bf10fbff7adf76ec` Old Dominion University — degree_requirements 2026-27 · program_key=exercise-science-bs · requirement_key=exercise-and-sport-specialist [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/health-sciences/exercise-science/exercise-science-bs/ (sha256 39f7d122aeba)
- issues: requirement_groups_skipped
  - courses: EXSC 368 ⟵ “EXSC 368 - Internship (*)”
### `bf5033dbe3f549af` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=communication-core-bs-core-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 200S ⟵ “COMM 200S - Introduction to Human Communication”
  - courses: COMM 260 ⟵ “COMM 260 - Understanding Media”
  - courses: COMM 301 ⟵ “COMM 301 - Critical Methodologies”
  - courses: COMM 302 ⟵ “COMM 302 - Communication Research Methods I”
### `c15145362a349599` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=communication-core-ba-additional-core-course [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: COMM 335W ⟵ “COMM 335W - Rhetorical Criticism”
### `c19a7fb38807e754` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-technical-and-professional-writing-ba · requirement_key=english-core-theory-analytics [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-technical-and-professional-writing-ba/ (sha256 24304c241949)
- issues: requirement_groups_skipped
  - courses: ENGL 325 ⟵ “ENGL 325 - Introduction to Rhetorical Studies”
  - courses: ENGL 333 ⟵ “ENGL 333 - Introduction to Critical Theory”
  - courses: ENGL 370 ⟵ “ENGL 370 - English Linguistics”
### `c4b7227607fd7ad1` Old Dominion University — degree_requirements 2026-27 · program_key=special-education-with-a-major-in-special-education-general-curriculum-k-12-bs · requirement_key=special-education-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/special-education-general-curriculum-k12-bs/ (sha256 f33ea5dcbf71)
- issues: requirement_groups_skipped
  - courses: FOUN 301 ⟵ “FOUN 301 - Learning and Development”
  - courses: FOUN 302 ⟵ “FOUN 302 - Assessment of Learning”
  - courses: SPED 400 ⟵ “SPED 400 - Foundations of Special Education: Legal Aspects and Characteristics +”
  - courses: SPED 411 ⟵ “SPED 411 - Classroom and Behavioral Management Techniques for Students with Diverse Needs”
  - courses: SPED 417 ⟵ “SPED 417 - Collaboration and Transitions”
  - courses: STEM 370T ⟵ “STEM 370T - Technology and Society (writing intensive; C or better required) **”
  - courses: TLED 326 ⟵ “TLED 326 - Socio-Cultural Perspectives in Education”
  - courses: TLED 426 ⟵ “TLED 426 - Introduction to Literacy, Linguistics and Practice in the Classroom”
### `c5542caca3a579e1` Old Dominion University — degree_requirements 2026-27 · program_key=criminal-justice-with-a-major-in-cybercriminology-bs · requirement_key=cybercriminology-major-foundation-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/sociology-criminal-justice/cybercriminology-bs/ (sha256 efc94ead6d8d)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: CRJS 215S ⟵ “CRJS 215S - Introduction to Criminology”
  - courses: CRJS 222 ⟵ “CRJS 222 - The Criminal Justice System”
  - courses: CRJS 262 ⟵ “CRJS 262 - Law and the Criminal Justice System”
  - courses: CRJS 305 ⟵ “CRJS 305 - Introduction to Intelligence Analysis”
  - courses: CRJS 310 ⟵ “CRJS 310 - Cybercriminology: Foundations”
  - courses: CRJS/CPD/CYSE 406 ⟵ “CRJS/CPD/CYSE 406 - Cyber Law”
  - courses: CRJS/CYSE 409 ⟵ “CRJS/CYSE 409 - Crime and Computer Applications”
  - courses: CRJS 426W ⟵ “CRJS 426W - Criminological Theory (C or better required)”
  - courses: CRJS 499 ⟵ “CRJS 499 - Entrepreneurship in Cybercriminology”
  - courses: SOC 337 ⟵ “SOC 337 - Social Research Methods”
  - courses: CRJS 306 ⟵ “CRJS 306 - Law Enforcement Intelligence **”
  - courses: CRJS 319 ⟵ “CRJS 319 - Public and Private Security **”
  - courses: CRJS 320 ⟵ “CRJS 320 - Law and Social Control *”
  - courses: CRJS 344 ⟵ “CRJS 344 - Social Science and Crime Mapping **”
  - courses: CRJS 368 ⟵ “CRJS 368 - Internship”
  - courses: CRJS 404 ⟵ “CRJS 404 - Law and Digital Forensics *”
  - courses: CRJS 411 ⟵ “CRJS 411 - Cyberlaw II *”
  - courses: CRJS 415 ⟵ “CRJS 415 - Courtroom As a Social System *”
  - courses: CRJS 416 ⟵ “CRJS 416 - The American Jury *”
  - courses: CRJS 423 ⟵ “CRJS 423 - Public Policy in Criminal Justice *”
  - courses: CRJS 445 ⟵ “CRJS 445 - Workplace Law and Society *”
  - courses: CRJS 448 ⟵ “CRJS 448 - Women, Sex Discrimination and the Law *”
  - courses: CRJS 462 ⟵ “CRJS 462 - Substantive Criminal Law *”
  - courses: CYSE 270 ⟵ “CYSE 270 - Linux System for Cybersecurity **”
  - courses: CYSE 300 ⟵ “CYSE 300 - Introduction to Cybersecurity **”
  - … 4 more rows
### `c6d8ce0716881923` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-political-science [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: ASIA/POLS 435 ⟵ “ASIA/POLS 435 - Chinese Politics”
  - courses: POLS 325W ⟵ “POLS 325W - World Politics”
  - courses: POLS 437 ⟵ “POLS 437 - International Relations in East Asia”
  - courses: POLS 495 ⟵ “POLS 495 - Topics in Political Science ++”
  - courses: POLS 496 ⟵ “POLS 496 - Topics in Political Science ++”
### `cb6c923adf683fd2` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-asian-st [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ASIA 332 ⟵ “ASIA 332 - South Asia Since Independence”
  - courses: ASIA/HIST 336 ⟵ “ASIA/HIST 336 - The Emergence of New China”
  - courses: ASIA/POLS 338W ⟵ “ASIA/POLS 338W - Politics of East Asia”
  - courses: ASIA/PHIL 353 ⟵ “ASIA/PHIL 353 - Asian Religions”
  - courses: ASIA 360 ⟵ “ASIA 360 - Asian Art”
  - courses: ASIA 395 ⟵ “ASIA 395 - Topics in Asian Studies”
  - courses: ASIA/POLS 435 ⟵ “ASIA/POLS 435 - Chinese Politics”
  - courses: ASIA 461W ⟵ “ASIA 461W - Asian Studies Capstone Seminar”
  - courses: ASIA 495 ⟵ “ASIA 495 - Topics in Asian Studies”
### `ccd465fe209c7eb0` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=cinema-screenwriting-and-studies-major-foundations [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 346 ⟵ “COMM 346 - Screenwriting I”
  - courses: COMM 330 ⟵ “COMM 330 - The Short Script”
  - courses: COMM 391 ⟵ “COMM 391 - Film Theory and Criticism”
### `cf194abb26431307` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-bs · requirement_key=women-s-and-gender-studies-major-interdisciplinary-studies-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-bs/ (sha256 a576d3c1b66a)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: WGS 201S ⟵ “WGS 201S - Introduction to Women's, Gender, and Sexuality Studies”
  - courses: WGS/QUST 302W ⟵ “WGS/QUST 302W - Dimensions of Diversity: Intersectionality Among Women”
  - courses: WGS 400 ⟵ “WGS 400 - History of U.S. Women's Activism”
  - courses: WGS/QUST 460W ⟵ “WGS/QUST 460W - Feminist and Queer Theory”
  - courses: WGS 470 ⟵ “WGS 470 - Feminist Research Methods”
### `cffd479ef485ca82` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-finance [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: FIN 497 ⟵ “FIN 497 - Selected Topics in Finance ++”
### `d0a776b818aa945c` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-sociolog [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: SOC 306 ⟵ “SOC 306 - Religion and Society”
  - courses: SOC 395 ⟵ “SOC 395 - Topics in Sociology (Asian content)”
### `d16abdac6aa9f202` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=writing-intensive-requirement [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 308W ⟵ “COMM 308W - Effective Media Writing”
  - courses: COMM 315W ⟵ “COMM 315W - Sex, Gender, and Communication”
  - courses: COMM 335W ⟵ “COMM 335W - Rhetorical Criticism”
  - courses: COMM 400W ⟵ “COMM 400W - Intercultural Communication”
  - courses: COMM 412W ⟵ “COMM 412W - Interpersonal Communication Theory and Research”
  - courses: COMM 447W ⟵ “COMM 447W - Electronic Media Law and Policy”
  - courses: COMM 471W ⟵ “COMM 471W - International Film History”
  - courses: COMM 479W ⟵ “COMM 479W - American Film History”
### `d25ba4d945c1f74b` Old Dominion University — degree_requirements 2026-27 · program_key=african-american-and-african-studies-ba · requirement_key=african-studies-ba-and-bs-6-credit-hours-300-and-400-level-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-ba/ (sha256 33b79ef74f7b)
- issues: requirement_groups_skipped
  - courses: AAST 310 ⟵ “AAST 310 - Human Rights and Social Change in Africa”
  - courses: AAST/POLS 316 ⟵ “AAST/POLS 316 - Politics of Africa”
  - courses: AAST/HIST 381 ⟵ “AAST/HIST 381 - Africa in the 20th Century”
  - courses: GEOG 452 ⟵ “GEOG 452 - Africa”
  - courses: HIST 370 ⟵ “HIST 370 - Africa and the Atlantic Slave Trade”
  - courses: HIST 382 ⟵ “HIST 382 - African Civilizations”
  - courses: HIST 475 ⟵ “HIST 475 - Global Africa”
  - courses: POLS 439 ⟵ “POLS 439 - International Relations of African States”
### `d331a13bafe9c724` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=communication-core-bs-core-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 200S ⟵ “COMM 200S - Introduction to Human Communication”
  - courses: COMM 260 ⟵ “COMM 260 - Understanding Media”
  - courses: COMM 301 ⟵ “COMM 301 - Critical Methodologies”
  - courses: COMM 302 ⟵ “COMM 302 - Communication Research Methods I”
### `d65f3f8d18816a42` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=additional-communication-major-courses-internship [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
### `d919a34f7d6ce34a` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-technical-and-professional-writing-ba · requirement_key=english-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-technical-and-professional-writing-ba/ (sha256 24304c241949)
- issues: requirement_groups_skipped
  - courses: ENGL 307T ⟵ “ENGL 307T - Digital Writing”
  - courses: ENGL 490 ⟵ “ENGL 490 - Professionalization in English”
### `d969311276b8444d` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=additional-communication-major-courses-research-practicum [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
### `daa8e109a3e0aae4` Old Dominion University — degree_requirements 2026-27 · program_key=physical-education-with-a-major-in-prek-12-health-and-physical-education-bs · requirement_key=health-and-physical-education-major-health-and-physical-education [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/physical-education-prek-12-health-bs/ (sha256 6f1dba08ef11)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIOL 240 ⟵ “BIOL 240 - Fundamentals of Anatomy and Physiology I”
  - courses: EXSC 322 ⟵ “EXSC 322 - Anatomical Kinesiology and Musculoskeletal Injuries”
  - courses: TLED 408 ⟵ “TLED 408 - Reading and Writing in Content Areas”
  - courses: TLED 430W ⟵ “TLED 430W - PK-12 Instructional Technology”
  - courses: HPE 200 ⟵ “HPE 200 - Foundations of Education, Physical Education and Health”
  - courses: HPE 218 ⟵ “HPE 218 - Aquatics and Outdoor Education”
  - courses: HPE 220 ⟵ “HPE 220 - Teaching of Team Sports”
  - courses: HPE 222 ⟵ “HPE 222 - Teaching Individual Sports and Dance”
  - courses: HPE 300 ⟵ “HPE 300 - Teaching Elementary Physical Education”
  - courses: HPE 301W ⟵ “HPE 301W - Methods and Materials in Teaching Physical Education”
  - courses: HPE 317 ⟵ “HPE 317 - Human Growth & Motor Development”
  - courses: HPE 318 ⟵ “HPE 318 - Motor Learning”
  - courses: HPE 324 ⟵ “HPE 324 - Teaching Injury Care for Sports”
  - courses: HPE 400 ⟵ “HPE 400 - Management Skills for Teaching Health and Physical Education”
  - courses: HPE 402 ⟵ “HPE 402 - Methods and Materials in Health Education”
  - courses: HPE 404 ⟵ “HPE 404 - Adapted Physical Education”
  - courses: HPE 406 ⟵ “HPE 406 - Tests and Measurement in Physical Education and Health”
  - courses: HPE 409 ⟵ “HPE 409 - Physiology of Exercise”
  - courses: HPE 430 ⟵ “HPE 430 - Nutrition and Fitness Education”
  - courses: HPE 469 ⟵ “HPE 469 - Practicum Experience and Instructional Planning in Health and Physical Education”
  - courses: HPE 480 ⟵ “HPE 480 - Teacher Candidate Seminar”
  - courses: HPE 485 ⟵ “HPE 485 - Teacher Candidate Internship”
### `de45fd82f0e20fa4` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-applied-linguistics-ba · requirement_key=english-core-required-literature-and-cultural-studies-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-applied-linguistics-ba/ (sha256 387330ef24ca)
- issues: requirement_groups_skipped
  - courses: ENGL 301 ⟵ “ENGL 301 - Introduction to British Literature I”
  - courses: ENGL 302 ⟵ “ENGL 302 - Introduction to British Literature II”
  - courses: ENGL 303 ⟵ “ENGL 303 - Shakespeare and Comedy”
  - courses: ENGL 304 ⟵ “ENGL 304 - Shakespeare and Tragedy”
  - courses: ENGL 340 ⟵ “ENGL 340 - American Drama”
  - courses: ENGL 342 ⟵ “ENGL 342 - Southern Literature”
  - courses: ENGL 345 ⟵ “ENGL 345 - American Literature to 1860”
  - courses: ENGL 346 ⟵ “ENGL 346 - American Literature Since 1860”
  - courses: ENGL 360 ⟵ “ENGL 360 - World Literature I”
  - courses: ENGL 363 ⟵ “ENGL 363 - World Literature II”
  - courses: ENGL 407 ⟵ “ENGL 407 - Chaucer's Canterbury Tales”
  - courses: ENGL 416 ⟵ “ENGL 416 - English Renaissance Drama”
  - courses: ENGL 418W ⟵ “ENGL 418W - Jewish Writers”
  - courses: ENGL 419 ⟵ “ENGL 419 - The Harlem Renaissance”
  - courses: ENGL 421 ⟵ “ENGL 421 - British Literature 1660-1800”
  - courses: ENGL 423 ⟵ “ENGL 423 - The Romantic Movement in Britain”
  - courses: ENGL 432 ⟵ “ENGL 432 - Origins and Early Development of the British Novel to 1800”
  - courses: ENGL 433 ⟵ “ENGL 433 - Victorian Literature”
  - courses: ENGL 438 ⟵ “ENGL 438 - The Twentieth-Century British Novel”
  - courses: ENGL 441 ⟵ “ENGL 441 - American Travel Literature”
  - courses: ENGL 447 ⟵ “ENGL 447 - The American Novel to 1920”
  - courses: ENGL 448 ⟵ “ENGL 448 - The American Novel 1920 to Present”
  - courses: ENGL 453 ⟵ “ENGL 453 - The Short Story”
  - courses: ENGL 459W ⟵ “ENGL 459W - New Literatures in English”
  - courses: ENGL 461 ⟵ “ENGL 461 - American Poetry of the Early Twentieth Century”
  - … 6 more rows
### `df0e9eaf980d1f94` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=additional-communication-major-courses-research-practicum [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
### `e0d3010df0834a9e` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=writing-intensive-requirement [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 308W ⟵ “COMM 308W - Effective Media Writing”
  - courses: COMM 315W ⟵ “COMM 315W - Sex, Gender, and Communication”
  - courses: COMM 335W ⟵ “COMM 335W - Rhetorical Criticism”
  - courses: COMM 400W ⟵ “COMM 400W - Intercultural Communication”
  - courses: COMM 412W ⟵ “COMM 412W - Interpersonal Communication Theory and Research”
  - courses: COMM 447W ⟵ “COMM 447W - Electronic Media Law and Policy”
  - courses: COMM 471W ⟵ “COMM 471W - International Film History”
  - courses: COMM 479W ⟵ “COMM 479W - American Film History”
### `e1a4935197f3eb2a` Old Dominion University — degree_requirements 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-training-specialist-bs · requirement_key=training-specialist-major-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-training-specialist-bs/ (sha256 e9e73afa7e78)
- issues: requirement_groups_skipped
  - section: training-specialist-major-electives ⟵ “Training Specialist Major — Electives”
### `e2da309d7a34325e` Old Dominion University — degree_requirements 2026-27 · program_key=environmental-health-bs · requirement_key=environmental-health-major-departmental-requirements [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/joint-school-public-health/epidemiology-biostatistics-and-environmental-health/environmental-health-bs/ (sha256 daea2f065cee)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: STAT 130M ⟵ “STAT 130M - Elementary Statistics *”
  - courses: BIOL 150 ⟵ “BIOL 150 - Introductory Microbiology *”
  - courses: BIOL 151 ⟵ “BIOL 151 - Introductory Microbiology Laboratory *”
  - courses: BIOL 240 ⟵ “BIOL 240 - Fundamentals of Anatomy and Physiology I *”
  - courses: PHYS 111N ⟵ “PHYS 111N - Introductory General Physics”
### `e326762d897fcee3` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=additional-communication-major-courses-capstone [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 433 ⟵ “COMM 433 - Capstone”
### `e442e9301e640411` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-ba · requirement_key=internships-and-practicum-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-ba/ (sha256 66bce2c2b25d)
- issues: requirement_groups_skipped
  - courses: COMM 368 ⟵ “COMM 368 - Internship”
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
### `e554fec0e7c9b7a6` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-ba · requirement_key=interdisciplinary-studies-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-ba/ (sha256 359f7abf5fe7)
- issues: requirement_groups_skipped
  - courses: IDS 300W ⟵ “IDS 300W - Interdisciplinary Theory and Concepts *”
  - courses: IDS 301 ⟵ “IDS 301 - Data and Humanities Research **”
  - courses: IDS 493 ⟵ “IDS 493 - IDS Electronic Portfolio Project **”
### `e5bd03584281940d` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-english [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped
  - courses: ENGL 396 ⟵ “ENGL 396 - Topics in English (Contemporary Filipino/Filipino-American Literature)”
  - courses: ENGL 495 ⟵ “ENGL 495 - Topics in English (Techno-Orientalism in Science Fiction Film & Literature)”
### `e6428d97c95f0f70` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-women-s-and-gender-studies-ba · requirement_key=women-s-and-gender-studies-major-women-s-and-gender-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-womens-and-gender-studies-ba/ (sha256 359f7abf5fe7)
- issues: requirement_groups_skipped
  - courses: WGS 301 ⟵ “WGS 301 - Feminist Foundations”
  - courses: WGS/QUST 302W ⟵ “WGS/QUST 302W - Dimensions of Diversity: Intersectionality Among Women”
  - courses: WGS/QUST 303 ⟵ “WGS/QUST 303 - Queer Studies”
  - courses: WGS 304 ⟵ “WGS 304 - Gender and Sexuality in Film”
  - courses: WGS/QUST 305 ⟵ “WGS/QUST 305 - Queer Literature”
  - courses: WGS 306 ⟵ “WGS 306 - Women, the Environment, and Climate Change”
  - courses: WGS 368 ⟵ “WGS 368 - Internship”
  - courses: WGS 390T ⟵ “WGS 390T - Women, Gender, and Technology Worldwide”
  - courses: WGS 395 ⟵ “WGS 395 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 396 ⟵ “WGS 396 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 401W ⟵ “WGS 401W - Women: A Global Perspective”
  - courses: WGS/QUST 402 ⟵ “WGS/QUST 402 - Feminisms and Sexualities”
  - courses: WGS 405 ⟵ “WGS 405 - Gender and Media”
  - courses: WGS 406 ⟵ “WGS 406 - Gender, Fashion & the Body”
  - courses: WGS 410 ⟵ “WGS 410 - Sexing the Body”
  - courses: WGS 470 ⟵ “WGS 470 - Feminist Research Methods”
  - courses: WGS 495 ⟵ “WGS 495 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 496 ⟵ “WGS 496 - Topics in Women's, Gender, and Sexuality Studies”
  - courses: WGS 497 ⟵ “WGS 497 - Independent Study”
  - courses: WGS 498 ⟵ “WGS 498 - Independent Study”
### `e6bbe063d2561b40` Old Dominion University — degree_requirements 2026-27 · program_key=special-education-with-a-major-in-special-education-adapted-curriculum-k-12-bs · requirement_key=special-education-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/special-education-adapted-curriculum-k12-bs/ (sha256 3739387c8fb1)
- issues: requirement_groups_skipped
  - courses: FOUN 301 ⟵ “FOUN 301 - Learning and Development”
  - courses: FOUN 302 ⟵ “FOUN 302 - Assessment of Learning”
  - courses: SPED 400 ⟵ “SPED 400 - Foundations of Special Education: Legal Aspects and Characteristics +”
  - courses: SPED 411 ⟵ “SPED 411 - Classroom and Behavioral Management Techniques for Students with Diverse Needs”
  - courses: SPED 417 ⟵ “SPED 417 - Collaboration and Transitions”
  - courses: STEM 370T ⟵ “STEM 370T - Technology and Society (writing intensive; C or better required) **”
  - courses: TLED 326 ⟵ “TLED 326 - Socio-Cultural Perspectives in Education”
  - courses: TLED 426 ⟵ “TLED 426 - Introduction to Literacy, Linguistics and Practice in the Classroom”
### `eab3946ba78d5e82` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-asian-studies-ba · requirement_key=asian-studies-major-sociology [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-asian-studies-ba/ (sha256 9e2238b81d66)
- issues: requirement_groups_skipped
  - courses: SOC 306 ⟵ “SOC 306 - Religion and Society”
  - courses: SOC 395 ⟵ “SOC 395 - Topics in Sociology ++”
### `ecfe442c728cfd4e` Old Dominion University — degree_requirements 2026-27 · program_key=chemistry-with-a-major-in-chemical-forensic-science-bs · requirement_key=chemical-forensic-science-major-chemical-forensic-science-major [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/sciences/chemistry-biochemistry/chemistry-chemical-forensic-science-bs/ (sha256 2f424b98ebb5)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CHEM 320T ⟵ “CHEM 320T - Survey of Forensic Science”
  - courses: CHEM 325 ⟵ “CHEM 325 - Forensic Biochemistry and Microscopy with Laboratory”
  - courses: CHEM 359 ⟵ “CHEM 359 - Forensic Chemistry with Laboratory”
  - courses: CHEM 459 ⟵ “CHEM 459 - Advanced Forensic Chemistry and Crime Scene Investigation”
  - courses: CHEM 461 ⟵ “CHEM 461 - Forensic Professional Practice”
  - courses: CHEM 498 ⟵ “CHEM 498 - Independent Study”
  - courses: CHEM 442W ⟵ “CHEM 442W - Biochemistry Laboratory *”
  - courses: CRJS 222 ⟵ “CRJS 222 - The Criminal Justice System”
### `edeeb3c5312fef42` Old Dominion University — degree_requirements 2026-27 · program_key=african-american-and-african-studies-bs · requirement_key=upper-division-social-science-courses [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/african-american-studies/african-american-studies-bs/ (sha256 af978b675a37)
- issues: requirement_groups_skipped
  - courses: AAST 310 ⟵ “AAST 310 - Human Rights and Social Change in Africa”
  - courses: AAST/POLS 316 ⟵ “AAST/POLS 316 - Politics of Africa”
  - courses: AAST/SOC 323 ⟵ “AAST/SOC 323 - Sociology of Minority Families”
  - courses: AAST 368 ⟵ “AAST 368 - Internship”
  - courses: AAST 395 ⟵ “AAST 395 - Topics in African American Studies”
  - courses: AAST 396 ⟵ “AAST 396 - Topics in African American Studies”
  - courses: AAST/POLS 412 ⟵ “AAST/POLS 412 - Politics of the Civil Rights Movement”
  - courses: AAST/SOC 426 ⟵ “AAST/SOC 426 - Minority Group Relations”
  - courses: AAST/CRJS/SOC 452 ⟵ “AAST/CRJS/SOC 452 - Diversity in Criminal Justice Organizations”
  - courses: AAST/PSYC 460 ⟵ “AAST/PSYC 460 - Psychology of African Americans”
  - courses: CRJS 450 ⟵ “CRJS 450 - Blacks, Crime and Justice”
  - courses: GEOG 452 ⟵ “GEOG 452 - Africa”
  - courses: POLS 309 ⟵ “POLS 309 - Race, Culture and Public Policy”
  - courses: POLS 410 ⟵ “POLS 410 - African American Politics”
  - courses: POLS 439 ⟵ “POLS 439 - International Relations of African States”
  - courses: POLS 470 ⟵ “POLS 470 - African Americans and Foreign Affairs”
  - courses: SOC/CRJS 444 ⟵ “SOC/CRJS 444 - Community Justice”
### `ef325354b8e4b32f` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-ba · requirement_key=communication-core-ba-additional-core-course [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-ba/ (sha256 11ecab4e77c7)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: COMM 335W ⟵ “COMM 335W - Rhetorical Criticism”
### `f15d4287dafe7464` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-philosop [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: REL 352 ⟵ “REL 352 - Islam”
  - courses: PHIL/ASIA 353 ⟵ “PHIL/ASIA 353 - Asian Religions”
  - courses: PHIL 380 ⟵ “PHIL 380 - Hinduism”
  - courses: PHIL 381 ⟵ “PHIL 381 - Buddhist Traditions”
  - courses: PHIL 482 ⟵ “PHIL 482 - Chinese Religion and Philosophy”
  - courses: PHIL 485 ⟵ “PHIL 485 - Japanese Religion and Philosophy”
### `f5b562ef12289bbb` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-applied-linguistics-ba · requirement_key=english-core-writing [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-applied-linguistics-ba/ (sha256 387330ef24ca)
- issues: requirement_groups_skipped
  - courses: ENGL 300W ⟵ “ENGL 300W - Introduction to Creative Writing”
  - courses: ENGL 327W ⟵ “ENGL 327W - Advanced Composition”
  - courses: ENGL 334W ⟵ “ENGL 334W - Technical Writing”
  - courses: ENGL 427W ⟵ “ENGL 427W - Writing in the Disciplines”
### `f7d7d5c589988c0d` Old Dominion University — degree_requirements 2026-27 · program_key=asian-studies-ba · requirement_key=upper-level-elective-courses-24-26-credit-hours-at-the-300-or-400-level-history [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/asian-studies/asian-studies-ba/ (sha256 527278b00908)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST/ASIA 336 ⟵ “HIST/ASIA 336 - The Emergence of New China”
  - courses: HIST 396 ⟵ “HIST 396 - Topics in History”
  - courses: HIST 495 ⟵ “HIST 495 - Topics in History”
### `f99bdf24e9cf2814` Old Dominion University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-with-a-major-in-supply-chain-and-maritime-logistics-bs · requirement_key=supply-chain-and-maritime-logistics-major-approved-program-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/interdisciplinary-studies/interdisciplinary-studies-supply-chain-and-maritime-logistics-bs/ (sha256 0c18deed219f)
- issues: requirement_groups_skipped
  - courses: BDA 411 ⟵ “BDA 411 - Introduction to Machine Learning”
  - courses: CS 480 ⟵ “CS 480 - Introduction to Artificial Intelligence”
  - courses: CYSE 301 ⟵ “CYSE 301 - Cybersecurity Techniques and Operations”
  - courses: HIST 359 ⟵ “HIST 359 - American Maritime History”
  - courses: SCLM 311 ⟵ “SCLM 311 - Project Management in Supply Chain & Logistics Operations”
  - courses: SCLM 380 ⟵ “SCLM 380 - Multimodal Freight Transportation”
  - courses: SCLM 410 ⟵ “SCLM 410 - International Maritime and Transportation Law and Policy”
  - courses: SCLM 415 ⟵ “SCLM 415 - Maritime and Supply Chain Safety and Security”
  - courses: SCLM 419 ⟵ “SCLM 419 - Maritime and Supply Chain Risk and Insurance”
  - courses: SCLM 442 ⟵ “SCLM 442 - Supply Chain and Maritime Intelligence”
  - courses: SCLM 443 ⟵ “SCLM 443 - Building Sustainable Supply Chains”
  - courses: SCLM 471 ⟵ “SCLM 471 - Port and Terminal Operations”
  - courses: SCLM 472 ⟵ “SCLM 472 - Vessel Fleet Operations”
  - courses: SCLM 473 ⟵ “SCLM 473 - Inland Waterways and Dredging Operations”
  - courses: SCLM 474 ⟵ “SCLM 474 - Shipbuilding & Ship Repair Logistics”
  - courses: SCLM 481 ⟵ “SCLM 481 - Freight Brokerage and 3PL Services”
  - courses: SCLM 486 ⟵ “SCLM 486 - Cruise Ship Operations”
  - courses: SCLM 495 ⟵ “SCLM 495 - Selected Topics in Supply Chain, Logistics and Maritime Operations”
  - courses: SCLM 497 ⟵ “SCLM 497 - Independent Study”
### `fbf9cb4c4991389c` Old Dominion University — degree_requirements 2026-27 · program_key=special-education-with-a-major-in-early-intervention-early-childhood-special-edu · requirement_key=special-education-core [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/special-education-early-intervention-early-childhood-special-education-birth-5-bs/ (sha256 0dce08dad768)
- issues: requirement_groups_skipped
  - courses: FOUN 301 ⟵ “FOUN 301 - Learning and Development”
  - courses: FOUN 302 ⟵ “FOUN 302 - Assessment of Learning”
  - courses: SPED 400 ⟵ “SPED 400 - Foundations of Special Education: Legal Aspects and Characteristics +”
  - courses: SPED 411 ⟵ “SPED 411 - Classroom and Behavioral Management Techniques for Students with Diverse Needs”
  - courses: SPED 417 ⟵ “SPED 417 - Collaboration and Transitions”
  - courses: STEM 370T ⟵ “STEM 370T - Technology and Society (writing intensive; C or better required) **”
  - courses: TLED 326 ⟵ “TLED 326 - Socio-Cultural Perspectives in Education”
  - courses: TLED 426 ⟵ “TLED 426 - Introduction to Literacy, Linguistics and Practice in the Classroom”
### `fd327acdc0f5c3a4` Old Dominion University — degree_requirements 2026-27 · program_key=data-science-with-a-major-in-data-for-a-human-world-bs · requirement_key=data-for-a-human-world-major-major-electives [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/data-science/data-science-data-for-a-human-world-bs/ (sha256 e583b8d1f70b)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: COMM 402 ⟵ “COMM 402 - Communicating Data”
  - courses: CRJS 395 ⟵ “CRJS 395 - Topics in Criminal Justice ***”
  - courses: ENGL 370 ⟵ “ENGL 370 - English Linguistics”
  - courses: IDS 301 ⟵ “IDS 301 - Data and Humanities Research”
  - courses: PHIL 447 ⟵ “PHIL 447 - Philosophy of Information”
  - courses: SOC 309 ⟵ “SOC 309 - Population and Society”
  - courses: COMM 303 ⟵ “COMM 303 - Introduction to Strategic Communications”
  - courses: COMM 408 ⟵ “COMM 408 - Health Communication”
  - courses: CRJS 344 ⟵ “CRJS 344 - Social Science and Crime Mapping”
  - courses: ENGL 334W ⟵ “ENGL 334W - Technical Writing”
  - courses: GEOG 300 ⟵ “GEOG 300 - Maps and Geographic Information”
  - courses: GEOG 402 ⟵ “GEOG 402 - Geographic Information Systems”
  - courses: IDS 300W ⟵ “IDS 300W - Interdisciplinary Theory and Concepts”
  - courses: QUST/WGS 302W ⟵ “QUST/WGS 302W - Dimensions of Diversity: Intersectionality Among Women”
  - courses: PHIL/AI 446 ⟵ “PHIL/AI 446 - Artificial Intelligence (AI) Ethics and Policy”
  - courses: SOC 337 ⟵ “SOC 337 - Social Research Methods”
  - courses: WGS 470 ⟵ “WGS 470 - Feminist Research Methods”
  - courses: REL 395 ⟵ “REL 395 - Topics in Religious Studies ***”
### `fdc5e8bc220b227b` Old Dominion University — degree_requirements 2026-27 · program_key=english-with-a-major-in-applied-linguistics-ba · requirement_key=english-core-theory-analytics [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/english/english-applied-linguistics-ba/ (sha256 387330ef24ca)
- issues: requirement_groups_skipped
  - courses: ENGL 325 ⟵ “ENGL 325 - Introduction to Rhetorical Studies”
  - courses: ENGL 333 ⟵ “ENGL 333 - Introduction to Critical Theory”
  - courses: ENGL 370 ⟵ “ENGL 370 - English Linguistics”
### `fecde2f07719fbf7` Old Dominion University — degree_requirements 2026-27 · program_key=occupational-and-technical-studies-with-a-major-in-fashion-merchandising-bs · requirement_key=fashion-merchandising-major-fashion-merchandising [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/educational-leadership-workforce-development/occupational-technical-studies-fashion-merchandising-bs/ (sha256 8cf2795df528)
- issues: requirement_groups_skipped, mixed_required_and_choice
  - courses: ACCT 201 ⟵ “ACCT 201 - Principles of Financial Accounting”
  - courses: SEPS 100 ⟵ “SEPS 100 - Sales Techniques”
  - courses: SEPS 102 ⟵ “SEPS 102 - Advertising and Promotion”
  - courses: SEPS 203S ⟵ “SEPS 203S - Dress, Culture and Society”
  - courses: SEPS 208 ⟵ “SEPS 208 - Retail Merchandising and Buying”
  - courses: SEPS 220 ⟵ “SEPS 220 - The Fashion Industry”
  - courses: SEPS 234 ⟵ “SEPS 234 - Survey of Dress and Costume”
  - courses: SEPS 302 ⟵ “SEPS 302 - Workforce Supervision Management”
  - courses: SEPS 355 ⟵ “SEPS 355 - Fashion Consumer Behavior”
  - courses: STEM 365 ⟵ “STEM 365 - Safety and OSHA Certification”
  - courses: SEPS 405 ⟵ “SEPS 405 - Directed Work Experience (summer only)”
  - courses: SEPS 415 ⟵ “SEPS 415 - Advanced Merchandising”
  - courses: SEPS 422 ⟵ “SEPS 422 - Fashion Product Development”
  - courses: SEPS 427 ⟵ “SEPS 427 - Fashion Marketing (fall)”
  - courses: SEPS 435 ⟵ “SEPS 435 - International Retailing”
  - courses: SEPS 456 ⟵ “SEPS 456 - E-Commerce and Social Media in Fashion”
  - courses: SEPS 480 ⟵ “SEPS 480 - Senior Project: Merchandise Retailing (Prerequisite SEPS 415)”
  - courses: SEPS 481 ⟵ “SEPS 481 - Career and Professional Development”
  - courses: STEM 370T ⟵ “STEM 370T - Technology and Society (Writing Intensive) *”
  - courses: SEPS 223A ⟵ “SEPS 223A - Visual Merchandising and Display”
  - courses: STEM 321 ⟵ “STEM 321 - Manufacturing Technology”
  - courses: SEPS 367 ⟵ “SEPS 367 - Cooperative Education (requires employment)”
  - courses: STEM 382 ⟵ “STEM 382 - Industrial Design”
  - courses: SEPS 400 ⟵ “SEPS 400 - Instructional Systems Development”
  - courses: SEPS 409 ⟵ “SEPS 409 - Fashion Forecasting Market Trip”
  - … 5 more rows
### `ff4433f0c6185203` Old Dominion University — degree_requirements 2026-27 · program_key=park-recreation-and-tourism-studies-with-a-major-in-tourism-and-hospitality-mana · requirement_key=core-courses-for-park-recreation-and-tourism-studies [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/education/human-movement-studies-special-education/park-recreation-tourism-studies-hospitality-management-bs/ (sha256 ac6ca2491f1c)
- issues: requirement_groups_skipped
  - courses: PRTS 210S ⟵ “PRTS 210S - Leisure and Human Behavior”
  - courses: PRTS 475 ⟵ “PRTS 475 - Sustainable Management in Parks, Recreation, and Tourism”
  - courses: PRTS 482W ⟵ “PRTS 482W - Evaluation in Parks, Recreation, and Tourism”
  - courses: ACCT 201 ⟵ “ACCT 201 - Principles of Financial Accounting”
  - courses: MGMT 325 ⟵ “MGMT 325 - Contemporary Organizations and Management”
  - courses: MKTG 311 ⟵ “MKTG 311 - Marketing Principles and Problems”
  - courses: PRTS 366 ⟵ “PRTS 366 - Internship Seminar”
  - courses: PRTS 368 ⟵ “PRTS 368 - Internship”
### `ff8bdb5211c52078` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-strategic-communication-and-journalism-bs · requirement_key=additional-communication-major-courses-research-practicum [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/communication-strategic-communication-and-journalism-bs/ (sha256 10310859b91e)
- issues: requirement_groups_skipped
  - courses: COMM 369 ⟵ “COMM 369 - Research Practicum”
### `ffd79356ebc7e4b8` Old Dominion University — degree_requirements 2026-27 · program_key=communication-with-a-major-in-cinema-screenwriting-and-studies-bs · requirement_key=cinema-screenwriting-and-studies-major-foundations [new] (labeled_in_source)
- source: https://catalog.odu.edu/undergraduate/arts-letters/communication-theatre-arts/cinema-screenwriting-and-studies-bs/ (sha256 ac05ea1d2741)
- issues: requirement_groups_skipped
  - courses: COMM 346 ⟵ “COMM 346 - Screenwriting I”
  - courses: COMM 330 ⟵ “COMM 330 - The Short Script”
  - courses: COMM 391 ⟵ “COMM 391 - Film Theory and Criticism”
### `0d9825df40fc0e9e` Virginia Polytechnic Institute and State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://finaid.vt.edu/undergraduate/policies-regulations/satisfactory-academic-progress-sap.html (sha256 22a2006842a7)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The following will be considered: injury or illness of student or family member, death of a close relative, or other special circumstances.”
### `169088d8f61201be` Virginia Polytechnic Institute and State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-q-a.html (sha256 e11df34b808b)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://finaid.vt.edu/appeals/satisfactory-academic-progress.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal/sap-guideline.html,https://finaid.vt.edu/undergraduate/policies-regulations/satisfactory-academic-progress-sap.html
- checks: {"negative_sentences": 0, "sentences": 13}
  - sentence: sap_appeal ⟵ “Submitting a SAP Appeal Q: How do I submit my SAP appeal to your office?”
  - sentence: sap_appeal ⟵ “A: You can submit it one of two ways: Upload through the Financial Aid Document Uploader Drop it off in person at the Office of University Scholarships and Financial Aid (USFA) Q: What do I need to include in a SAP appeal?”
  - sentence: sap_appeal ⟵ “A: You’ll need to submit: A completed SAP Appeal Form Supporting documentation An Academic Advisor Form (required for maximum timeframe) More information about SAP Appeals are on our SAP Appeal webpage.”
  - sentence: sap_appeal ⟵ “We also encourage you to use our How to Write a SAP Appeal webpage to assist you in this process.”
  - sentence: sap_appeal ⟵ “A: This is third-party proof that supports the reason why you did not meet SAP in your appeal.”
  - sentence: sap_appeal ⟵ “Examples include: Doctor’s notes or medical records Police or legal documents Letters from counselors, clergy, or campus support services Proof of unexpected life events (family emergency, illness, etc.) More information on supporting documentation can be found on our How to Write a SAP Appeal webpage.”
### `335ce41d25cc6a4c` Virginia Polytechnic Institute and State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal/sap-guideline.html (sha256 f51d45f30ea5)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://finaid.vt.edu/appeals/satisfactory-academic-progress.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-q-a.html,https://finaid.vt.edu/undergraduate/policies-regulations/satisfactory-academic-progress-sap.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “What Not to Use as Appeal Reasons The following are not valid reasons for a SAP appeal: Difficulty adjusting to college life Balancing school with work or extracurriculars Supporting Documentation If you're submitting a Satisfactory Academic Progress (SAP) appeal, you'll need to include supporting documentation.”
  - sentence: sap_appeal ⟵ “SAP Resources Helpful Webpages: SAP Policy SAP Appeal Process How to Write a SAP Appeal SAP Q & A Ready to Complete a SAP Appeal?”
### `3e7128218de3ffbb` Virginia Polytechnic Institute and State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://finaid.vt.edu/appeals/satisfactory-academic-progress.html (sha256 b377eb7f393b)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal/sap-guideline.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-q-a.html,https://finaid.vt.edu/undergraduate/policies-regulations/satisfactory-academic-progress-sap.html
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Important: Receiving approval for a SAP appeal does not reverse an academic suspension decision.”
  - sentence: sap_appeal ⟵ “Appeal Process If you’ve lost aid eligibility due to SAP, you may submit an appeal if you experienced extenuating circumstances, such as: Serious illness or injury Death of a close family member Other documented hardships Appeals must include supporting documentation and a clear explanation of how the issue has been resolved or managed moving forward.”
  - sentence: sap_appeal ⟵ “Visit the How to Write a SAP Appeal webpage for deadlines and how to submit.”
  - sentence: sap_appeal ⟵ “SAP Resources Helpful Webpages: SAP Policy SAP Appeal Process How to Write a SAP Appeal SAP Q & A Ready to Complete a SAP Appeal?”
### `716f159a8ca0afc1` Virginia Polytechnic Institute and State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal.html (sha256 e6985e9f2b1c)
- issues: semantic_review_required, conflicting_sources:https://finaid.vt.edu/appeals/satisfactory-academic-progress.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal/sap-guideline.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-q-a.html,https://finaid.vt.edu/undergraduate/policies-regulations/satisfactory-academic-progress-sap.html
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “A SAP appeal is your opportunity to explain why you didn’t meet the required standards and show what steps you're taking to get back on track.”
  - sentence: sap_appeal ⟵ “On your SAP Appeal Form, you must: Explain what happened that affected your academic performance.”
  - sentence: sap_appeal ⟵ “For guidance on submitting your SAP Appeal, check out our How to Write a SAP Appeal webpage.”
  - sentence: sap_appeal ⟵ “Priority Dates & Appeal Deadlines You should submit your appeal as early as possible to avoid delays in aid processing. | 2026-2027 SAP Appeal Priority Dates and Deadlines by Term | | | | | Term Fall 2026 | Priority Date 1 June 16, 2026 | Final Deadline August 10, 2026 | | Spring 2027 | N/A | January 11, 2027 | | Summer 2026 | N/A | May 28, 2027 | *Students who meet priority date will receive deci”
  - sentence: sap_appeal ⟵ “When Will I Hear Back About My SAP Appeal?”
  - sentence: sap_appeal ⟵ “Once you’ve submitted all required documents, your SAP appeal will be reviewed.”
### `da4e4a1e902d8895` Virginia Polytechnic Institute and State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://finaid.vt.edu/undergraduate/policies-regulations/satisfactory-academic-progress-sap.html (sha256 22a2006842a7)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://finaid.vt.edu/appeals/satisfactory-academic-progress.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-appeal/sap-guideline.html,https://finaid.vt.edu/appeals/satisfactory-academic-progress/sap-q-a.html
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “When a student exceeds 150% they will be required to submit a SAP appeal for the following semester to determine if they will continue to receive financial aid. (This does include the certification of Plus loans and Private/Alternative student loans) Table 3 (above) shows how different grades and courses are counted towards the Maximum-Time Frame allowance.”
  - sentence: sap_appeal ⟵ “If a student fails any of the above SAP standards, the student’s financial aid eligibility is suspended. | Grade | Units Completed | Units Attempted | Counted Toward Maximum Time-Frame | A, B, C, D (+,-) | YES | YES | YES | P, X, EQ | YES | YES | YES | F, NG, NR | NO | YES | YES | I, WG, W, WP | NO | YES | YES | RG, RP | YES | YES | YES | Dual Enroll, AP | YES | YES | YES Appeal Procedures Notific”
  - sentence: sap_appeal ⟵ “The deadlines are listed on the SAP appeal form.”
  - sentence: sap_appeal ⟵ “Regaining Financial Aid Eligibility with Maximum Timeframe Undergraduate and Graduate students who need additional time to complete their first degree must complete the SAP Appeal form explaining why they have not completed the degree, a SAP Academic Advisor form signed by their Academic Advisor listing what classes remain, what terms they will be taken in, and the student’s expected graduation da”
  - sentence: sap_appeal ⟵ “Notification of Appeal Decision SAP appeals will be reviewed once ALL required documentation is received.”
  - sentence: sap_appeal ⟵ “Students Who Do Not Appeal Students who choose not to appeal will be required to meet the Satisfactory Academic Progress standards before regaining eligibility for financial aid.”
### `3af7cb3c52abffaa` Virginia Polytechnic Institute and State University — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_title)
- source: https://transferguide.registrar.vt.edu/CLEP/CLEP-DANTES-2026.html (sha256 d13cb6bd0918)
- issues: score_scale_mismatch, conflicting_sources:https://www.registrar.vt.edu/content/dam/registrar_vt_edu/documents/Updates/ap_ib_clep/Cambridge-2024.pdf,https://www.registrar.vt.edu/content/dam/registrar_vt_edu/documents/Updates/ap_ib_clep/CambridgeCredits2025.pdf
- checks: {"distinct_exams": 34, "equivalencies": 42, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “ACCT | Financial Accounting |  | 50 | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “ACIS | Information Systems |  | 50 | ACIS 1504 | Introduction to Business Analytics & Business Intelligence | 3”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “BIOL | Natural Sciences |  | 50 | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “BIOL | Biology |  | 50 | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “CHEM | Chemistry |  | 50 | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “ECON | Principles of Microeconomics |  | 50 | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “ECON | Principles of Macroeconomics |  | 50 | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “ENGL | College Composition |  | 50 | ENGL 1105 | First-Year Writing | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “ENGL | College Composition Modular |  | 50 | ENGL 1XXX | English Elective | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “ENGL | Analyzing & Interp. Literature |  | 50 | ENGL 1XXX | English Elective | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “ENGL | American Literature |  | 50 | ENGL 1XXX | English Elective | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “ENGL | English Literature |  | 50 | ENGL 1XXX | English Elective | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “FIN | Introductory Business Law |  | 50 | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “FREN | French Language Level 1 |  | 50 | FR 1XXX + FR 1XXX | French Elective + French Elective | 3+3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “FREN | French Language Level 2 |  | 59 | FR 2XXX + FR 2XXX | French Elective + French Elective | 3+3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “GER | German Language Level 1 |  | 50 | GER 1XXX + GER 1XXX | German Elective + German Elective | 3+3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “GER | German Language Level 2 |  | 60 | GER 2XXX + GER 2XXX | German Elective + German Elective | 3+3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “HD | Human Growth & Development |  | 50 | HD 1004 | Childhood and Adolescence | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “HIST | History of the United States I |  | 50 | HIST 1115 | History of the United States | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “HIST | History of the United States II |  | 50 | HIST 1116 | History of the United States | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “HIST | Western Civilization I |  | 50 | HIST 1025 | Intro. to European History | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “HIST | Western Civilization II |  | 50 | HIST 1026 | Intro. to European History | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “HIST | Social Sciences & History |  | 50 | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “HUM | Humanities |  | 50 | HUM 1604 | Intro. to Humanities and the Arts | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “MATH | College Algebra |  | 50 | VT 1XXX | Virginia Tech Elective | 3”
  - … 17 more rows
### `4f8b5120b3c965be` Virginia Polytechnic Institute and State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.registrar.vt.edu/content/dam/registrar_vt_edu/documents/Updates/ap_ib_clep/Cambridge-2024.pdf (sha256 85d43fe3e72a)
- issues: score_scale_mismatch, conflicting_sources:https://transferguide.registrar.vt.edu/CLEP/CLEP-DANTES-2026.html,https://www.registrar.vt.edu/content/dam/registrar_vt_edu/documents/Updates/ap_ib_clep/CambridgeCredits2025.pdf
- checks: {"distinct_exams": 9, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|4]:  ⟵ “Biology A                        A   E     A-C              BIOL 1105, 1115          Principles of Biology + lab                                 4”
  - equivalencies[CLEP-BIOLOGY|3]:  ⟵ “Biology AS                       A E       A-C              VT 1XXX                  Virginia Tech Elective                                      3”
  - equivalencies[CLEP-CHEMISTRY|4]:  ⟵ “Chemistry A                      A E       A-C              CHEM 1035, 1045,         General Chemistry + lab                                     4”
  - equivalencies[CLEP-CHEMISTRY|3]:  ⟵ “Chemistry AS                     A E       A-C              VT 1XXX                  Virginia Tech Elective                                      3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature A             A   E     A-C              ENGL 2XXX                English Elective                                            3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “Environmental Management         A E       A-C              ENSC 1015                Foundation Environmental Science                            3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|3]:  ⟵ “French A                         A E       A-C              FR 2XXX                  French Elective                                             3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|3]:  ⟵ “German A                         A E       A-C              GER 2XXX                 German Elective                                             3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Psychology A                     A E       A-C              PSYC 1004                Introductory Psychology                                     3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Psychology AS                    A   E     A-C              PSYC 2XXX                PSYC Elective                                               3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|3]:  ⟵ “Sociology A                      A   E     A-C              SOC 1004                 Introductory Sociology                                      3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|3]:  ⟵ “Spanish A                        A   E     A-C              SPAN 2XXX                Spanish Elective                                            3”
### `5710ac51f967f7f9` Virginia Polytechnic Institute and State University — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_title)
- source: https://transferguide.registrar.vt.edu/International-Baccalaureate/International-Baccalaureate-2026.html (sha256 57b473caba51)
- issues: score_column_not_scores
- checks: {"distinct_exams": 24, "equivalencies": 70, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|BIOL - Biology]:  ⟵ “BIOL - Biology | 4 |  | BIOL 1014 | Introduction to Biology | 3”
  - equivalencies[IB-BIOLOGY|BIOL - Biology]:  ⟵ “BIOL - Biology | 5 - 7 |  | BIOL 1105 + BIOL 1115 + BIOL 1106 + BIOL 1116 | Principles of Biology + Principles of Biology Lab + Principles of Biology + Principles of Biology Lab | 3+1+3+1”
  - equivalencies[IB-BUSINESS-MANAGEMENT|BMGT - Business Management]:  ⟵ “BMGT - Business Management | 4 - 7 |  | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[IB-CHEMISTRY|CHEM - Chemistry]:  ⟵ “CHEM - Chemistry | 4 |  | CHEM 1015 + CHEM 1025 +CHEM 1016 + CHEM 1026 | Introduction to Chemistry + Introduction to Chemistry Lab + Introduction to Chemistry + Introduction to Chemistry Lab | 3+1+3+1”
  - equivalencies[IB-CHEMISTRY|CHEM - Chemistry]:  ⟵ “CHEM - Chemistry | 5 - 7 |  | CHEM 1035 + CHEM 1045 + CHEM 1036 + CHEM 1046 | General Chemistry + General Chemistry Lab + General Chemistry + General Chemistry Lab | 3+1+3+1”
  - equivalencies[IB-COMPUTER-SCIENCE|CS - Computer Science]:  ⟵ “CS - Computer Science | 4 - 7 | IB Computer Science is available in multiple programming languages. If a student takes this course in a programming language other than Java it will need a faculty review. | CS 1114 | Intro to Software Design | 3”
  - equivalencies[IB-ECONOMICS|ECON - Economics]:  ⟵ “ECON - Economics | 4 |  | VT 1XXX | Virginia Tech Elective | 3”
  - equivalencies[IB-ECONOMICS|ECON - Economics]:  ⟵ “ECON - Economics | 5 - 7 |  | ECON 2005 + ECON 2006 | Principles of Economics (Micro) + Principles of Economics (Macro) | 3+3”
  - equivalencies[IB-FILM|FILM - Film]:  ⟵ “FILM - Film | 4 - 7 |  | CINE 2054 | Introduction to Cinema | 3”
  - equivalencies[IB-FRENCH|FR - French B]:  ⟵ “FR - French B | 4 - 7 |  | FR 2106 | Intermediate French | 3”
  - equivalencies[IB-GEOGRAPHY|GEOG - Geography]:  ⟵ “GEOG - Geography | 4 |  | GEOG 1004 | Intro to Human Geography | 3”
  - equivalencies[IB-GEOGRAPHY|GEOG - Geography]:  ⟵ “GEOG - Geography | 5 - 7 |  | GEOG 1004 + GEOG 1104 | Introduction to Human Geography + Introduction to Environmental Geography | 3+3”
  - equivalencies[IB-GERMAN|GER - German B]:  ⟵ “GER - German B | 4 - 7 |  | GER 2106 | Intermediate German | 3”
  - equivalencies[IB-HISTORY|HIST - History, Americas]:  ⟵ “HIST - History, Americas | 4 |  | HIST 1215 | Intro to World History | 3”
  - equivalencies[IB-HISTORY|HIST - History, Americas]:  ⟵ “HIST - History, Americas | 5 |  | HIST 1215 + 1216 | Intro to World History + Intro to World History | 3+3”
  - equivalencies[IB-HISTORY|HIST - History, Americas]:  ⟵ “HIST - History, Americas | 6 |  | HIST 1215 + HIST 1216 + HIST 1234 | Intro to World History + Intro to World History + Colonial Latin America | 3+3+3”
  - equivalencies[IB-HISTORY|HIST - History of Africa and the Middle East]:  ⟵ “HIST - History of Africa and the Middle East | 4 |  | HIST 1215 | Intro to World History | 3”
  - equivalencies[IB-HISTORY|HIST - History of Africa and the Middle East]:  ⟵ “HIST - History of Africa and the Middle East | 5 |  | HIST 1215 + 1216 | Intro to World History + Intro to World History | 3+3”
  - equivalencies[IB-HISTORY|HIST - History of Africa and the Middle East]:  ⟵ “HIST - History of Africa and the Middle East | 6 |  | HIST 1215 + HIST 1216 + HIST 1516 | Intro to World History + Intro to World History + History of Africa | 3+3+3”
  - equivalencies[IB-HISTORY|HIST - History of Asia and Oceania]:  ⟵ “HIST - History of Asia and Oceania | 4 |  | HIST 1215 | Intro to World History | 3”
  - equivalencies[IB-HISTORY|HIST - History of Asia and Oceania]:  ⟵ “HIST - History of Asia and Oceania | 5 |  | HIST 1215 + 1216 | Intro to World History + Intro to World History | 3+3”
  - equivalencies[IB-HISTORY|HIST - History of Asia and Oceania]:  ⟵ “HIST - History of Asia and Oceania | 6 |  | HIST 1215 + HIST 1216 + HIST 1354 | Intro to World History + Intro to World History + Conflict and Security in East Asia | 3+3+3”
  - equivalencies[IB-HISTORY|HIST - History of Europe]:  ⟵ “HIST - History of Europe | 4 |  | HIST 1025 | Introduction to European History | 3”
  - equivalencies[IB-HISTORY|HIST - History of Europe]:  ⟵ “HIST - History of Europe | 5 |  | HIST 1025 + HIST 1026 | Introduction to European History + Introduction to European History | 3+3”
  - equivalencies[IB-HISTORY|HIST - History of Europe]:  ⟵ “HIST - History of Europe | 6 |  | HIST 1025 + HIST 1026 + HIST 1XXX | Introduction to European History + Introduction to European History + History Elective | 3+3+3”
  - … 45 more rows
### `95d771086509204d` Virginia Polytechnic Institute and State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.registrar.vt.edu/content/dam/registrar_vt_edu/documents/Updates/ap_ib_clep/CambridgeCredits2025.pdf (sha256 0202673a82d2)
- issues: score_scale_mismatch, conflicting_sources:https://transferguide.registrar.vt.edu/CLEP/CLEP-DANTES-2026.html,https://www.registrar.vt.edu/content/dam/registrar_vt_edu/documents/Updates/ap_ib_clep/Cambridge-2024.pdf
- checks: {"distinct_exams": 9, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|4]:  ⟵ “Biology A                        A–E       A-C              BIOL 1105, 1115          Principles of Biology + lab                                 4”
  - equivalencies[CLEP-BIOLOGY|3]:  ⟵ “Biology AS                       A–E       A-C              VT 1XXX                  Virginia Tech Elective                                      3”
  - equivalencies[CLEP-CHEMISTRY|4]:  ⟵ “Chemistry A                      A–E       A-C              CHEM 1035, 1045,         General Chemistry + lab                                     4”
  - equivalencies[CLEP-CHEMISTRY|3]:  ⟵ “Chemistry AS                     A–E       A-C              VT 1XXX                  Virginia Tech Elective                                      3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature A             A–E       A-C              ENGL 2XXX                English Elective                                            3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “Environmental Management         A–E       A-C              ENSC 1015                Foundation Environmental Science                            3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|3]:  ⟵ “French A                         A–E       A-C              FR 2XXX                  French Elective                                             3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|3]:  ⟵ “German A                         A–E       A-C              GER 2XXX                 German Elective                                             3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Psychology A                     A–E       A-C              PSYC 1004                Introductory Psychology                                     3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Psychology AS                    A–E       A-C              PSYC 2XXX                PSYC Elective                                               3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|3]:  ⟵ “Sociology A                      A–E       A-C              SOC 1004                 Introductory Sociology                                      3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|3]:  ⟵ “Spanish A                        A–E       A-C              SPAN 2XXX                Spanish Elective                                            3”

## Re-verification of existing records (52)

- source_not_fetched: data/institutions/brcc/costs/2026-27.json ["costs", "ipeds-231536", null, "2026-27", {"residency": "in_state"}]
- source_not_fetched: data/institutions/brcc/costs/2026-27.json ["costs", "ipeds-231536", null, "2026-27", {"residency": "out_of_state"}]
- source_not_fetched: data/institutions/brcc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-231536", null, "2026-27", {}]
- source_not_fetched: data/institutions/bluefield/credit_policies/2026-27.json ["credit_policies", "ipeds-231554", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/bridgewater/transfer_policies/2026-27.json ["transfer_policies", "ipeds-231581", null, "2026-27", {}]
- source_not_fetched: data/institutions/bryantstratton/transfer_policies/2026-27.json ["transfer_policies", "ipeds-231785", null, "2026-27", {}]
- source_not_fetched: data/institutions/emu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-232043", null, "2026-27", {}]
- source_not_fetched: data/institutions/es/transfer_policies/2026-27.json ["transfer_policies", "ipeds-232052", null, "2026-27", {}]
- source_not_fetched: data/institutions/hamptonu/credit_policies/2026-27.json ["credit_policies", "ipeds-232265", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/hollins/awards/2026-27.json ["awards", "ipeds-232308", null, "2026-27", {"award_name": "The Sunflower Initiative"}]
- source_not_fetched: data/institutions/hollins/awards/2026-27.json ["awards", "ipeds-232308", null, "2026-27", {"award_name": "Visit Grant"}]
- source_not_fetched: data/institutions/hollins/awards/2026-27.json ["awards", "ipeds-232308", null, "2026-27", {"award_name": "Alumnae Referral Scholarship All Students"}]
- source_not_fetched: data/institutions/longwood/credit_policies/2026-27.json ["credit_policies", "ipeds-232566", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/longwood/credit_policies/2026-27.json ["credit_policies", "ipeds-232566", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/nr/credit_policies/2026-27.json ["credit_policies", "ipeds-232867", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/odu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-232982", null, "2026-27", {"program_key": "english-with-a-major-in-secondary-english-education-6-12-ba", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/odu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-232982", null, "2026-27", {"program_key": "physics-with-a-major-in-physics-professional-bs", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/odu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-232982", null, "2026-27", {"program_key": "engineering-technology-with-a-major-in-civil-engineering-technology-bset", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/odu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-232982", null, "2026-27", {"program_key": "engineering-technology-with-a-major-in-mechanical-engineering-technology-bset", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/rmc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-233295", null, "2026-27", {}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Chancellors"}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Trustees"}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Presidents"}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Achievement"}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Royals"}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Chancellors Booster"}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Trustees Booster"}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Presidents Booster"}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Achievement Booster"}]
- source_not_fetched: data/institutions/regent/awards/2026-27.json ["awards", "ipeds-231651", null, "2026-27", {"award_name": "Royals Booster"}]
- source_not_fetched: data/institutions/svu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-233611", null, "2026-27", {}]
- source_not_fetched: data/institutions/southside/credit_policies/2026-27.json ["credit_policies", "ipeds-233639", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/southside/credit_policies/2026-27.json ["credit_policies", "ipeds-233639", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/sw/credit_policies/2026-27.json ["credit_policies", "ipeds-233648", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/sw/credit_policies/2026-27.json ["credit_policies", "ipeds-233648", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/sbc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-233718", null, "2026-27", {}]
- source_not_fetched: data/institutions/lynchburg/transfer_policies/2026-27.json ["transfer_policies", "ipeds-232609", null, "2026-27", {}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Presidential Award (Out-of-State Merit Scholarship)"}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Provost Award (Out-of-State Merit Scholarship)"}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Eagle Award (Out-of-State Merit Scholarship)"}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Blue & Gray Award (Out-of-State Merit Scholarship)"}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Aerie Award"}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Collegiate Award"}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Presidential Award (In-State Merit Scholarship)"}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Provost Award (In-State Merit Scholarship)"}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Eagle Award (In-State Merit Scholarship)"}]
- source_not_fetched: data/institutions/umw/awards/2027-28.json ["awards", "ipeds-232681", null, "2027-28", {"award_name": "Blue & Gray Award (In-State Merit Scholarship)"}]
- source_not_fetched: data/institutions/richmond/awards/2026-27.json ["awards", "ipeds-233374", null, "2026-27", {"award_name": "Davis United World College Scholars"}]
- source_not_fetched: data/institutions/richmond/awards/2026-27.json ["awards", "ipeds-233374", null, "2026-27", {"award_name": "Bonner Scholars Program"}]
- source_not_fetched: data/institutions/vcu/credit_policies/2026-27.json ["credit_policies", "ipeds-234030", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/vsu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-234155", null, "2026-27", {"program_key": "visual-arts-bachelor-of-fine-arts-with-a-concentration-in-studio-arts-b-f-a", "requirement_key": "restricted-and-unrestricted-electives"}]
- source_not_fetched: data/institutions/vsu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-234155", null, "2026-27", {"program_key": "computer-science-major-bachelor-of-science-b-s", "requirement_key": "sample-plan"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- George Mason University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, statewide_articulation, residency
- James Madison University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Liberty University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency
- Old Dominion University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency
- University of Virginia-Main Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency
- Virginia Polytechnic Institute and State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
