# Review queue — CO (2026-27)

Pages fetched: 360; failures: 16. Candidates: 20 (4 without issues, 16 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 1 | 2 | 0 | 1 | 1 | 0 | 30 |
| cost_of_attendance | 0 | 2 | 0 | 1 | 2 | 0 | 30 |
| admissions_tests | 1 | 0 | 0 | 2 | 2 | 0 | 30 |
| common_data_set | 1 | 0 | 0 | 2 | 0 | 2 | 30 |
| merit_scholarships | 1 | 2 | 0 | 0 | 4 | 0 | 28 |
| ap_credit | 0 | 2 | 0 | 1 | 2 | 1 | 29 |
| clep_credit | 0 | 2 | 0 | 1 | 2 | 1 | 29 |
| ib_credit | 0 | 1 | 0 | 1 | 2 | 1 | 30 |
| dual_enrollment | 0 | 0 | 0 | 0 | 3 | 1 | 31 |
| transfer_credit | 2 | 8 | 0 | 0 | 4 | 0 | 21 |
| statewide_articulation | 0 | 0 | 0 | 0 | 1 | 3 | 31 |
| residency | 0 | 0 | 0 | 0 | 4 | 0 | 31 |
| degree_requirements | 6 | 0 | 0 | 0 | 1 | 1 | 27 |
| aid_appeals | 0 | 0 | 0 | 2 | 1 | 1 | 31 |

## Ready for review (4)

### `138d23999e80c23e` Arapahoe Community College — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://www.arapahoe.edu/admissions/paying-college/tuition-fees (sha256 8432abf9728a)
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 4410.0 ⟵ “Tuition | $4410.00 | Budgeted estimate based on on-campus tuition at 12 credits per semester. For specific tuition charges per credit hour, view the tables above.”
  - column:Fees: 455.66 ⟵ “Fees | $455.66 | Estimate based on on-campus required fees. For specific fees, view the information in the Fees section below.”
### `5035f126d968b566` Arapahoe Community College — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.arapahoe.edu/admissions/paying-college/tuition-fees (sha256 8432abf9728a)
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 18102 ⟵ “Tuition | $18,102 | Budgeted estimate based on on-campus tuition at 12 credits per semester. For specific tuition charges per credit hour, view the table above.”
  - column:Fees: 455.66 ⟵ “Fees | $455.66 | Estimate based on on-campus required fees. For specific fees, view the Fees section below.”
### `6c4b45ea19246395` Front Range Community College — costs 2026-27 · residency=out_of_state [same] (source_unlabeled)
- source: https://www.frontrange.edu/admissions-aid/paying-for-college/tuition-fees/cost-of-attendance.html (sha256 023490fa48e7)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition/Fees: 18528 ⟵ “Tuition/Fees | $4,836 | $4,836 | $18,528 | $18,528”
  - off_campus_not_with_family:Food & Housing: 17442 ⟵ “Food & Housing | $17,442 | $11,781 | $17,442 | $11,781”
  - off_campus_not_with_family:Books/Supplies: 1460 ⟵ “Books/Supplies | $1,460 | $1,460 | $1,460 | $1,460”
  - off_campus_not_with_family:Personal/Medical: 9918 ⟵ “Personal/Medical | $9,918 | $9,819 | $9,918 | $9,819”
  - off_campus_not_with_family:Transportation: 1512 ⟵ “Transportation | $1,512 | $1,512 | $1,512 | $1,512”
  - off_campus_not_with_family:Loan Fees: 38 ⟵ “Loan Fees | $38 | $38 | $38 | $38”
  - off_campus_not_with_family:Total:: 48898 ⟵ “Total: | $35,206 | $29,446 | $48,898 | $43,138”
  - with_parents_or_family:Tuition/Fees: 18528 ⟵ “Tuition/Fees | $4,836 | $4,836 | $18,528 | $18,528”
  - with_parents_or_family:Food & Housing: 11781 ⟵ “Food & Housing | $17,442 | $11,781 | $17,442 | $11,781”
  - with_parents_or_family:Books/Supplies: 1460 ⟵ “Books/Supplies | $1,460 | $1,460 | $1,460 | $1,460”
  - with_parents_or_family:Personal/Medical: 9819 ⟵ “Personal/Medical | $9,918 | $9,819 | $9,918 | $9,819”
  - with_parents_or_family:Transportation: 1512 ⟵ “Transportation | $1,512 | $1,512 | $1,512 | $1,512”
  - with_parents_or_family:Loan Fees: 38 ⟵ “Loan Fees | $38 | $38 | $38 | $38”
  - with_parents_or_family:Total:: 43138 ⟵ “Total: | $35,206 | $29,446 | $48,898 | $43,138”
### `a6f5a8ed85313789` Front Range Community College — costs 2026-27 · residency=in_state [same] (source_unlabeled)
- source: https://www.frontrange.edu/admissions-aid/paying-for-college/tuition-fees/cost-of-attendance.html (sha256 023490fa48e7)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition/Fees: 4836 ⟵ “Tuition/Fees | $4,836 | $4,836 | $18,528 | $18,528”
  - off_campus_not_with_family:Food & Housing: 17442 ⟵ “Food & Housing | $17,442 | $11,781 | $17,442 | $11,781”
  - off_campus_not_with_family:Books/Supplies: 1460 ⟵ “Books/Supplies | $1,460 | $1,460 | $1,460 | $1,460”
  - off_campus_not_with_family:Personal/Medical: 9918 ⟵ “Personal/Medical | $9,918 | $9,819 | $9,918 | $9,819”
  - off_campus_not_with_family:Transportation: 1512 ⟵ “Transportation | $1,512 | $1,512 | $1,512 | $1,512”
  - off_campus_not_with_family:Loan Fees: 38 ⟵ “Loan Fees | $38 | $38 | $38 | $38”
  - off_campus_not_with_family:Total:: 35206 ⟵ “Total: | $35,206 | $29,446 | $48,898 | $43,138”
  - with_parents_or_family:Tuition/Fees: 4836 ⟵ “Tuition/Fees | $4,836 | $4,836 | $18,528 | $18,528”
  - with_parents_or_family:Food & Housing: 11781 ⟵ “Food & Housing | $17,442 | $11,781 | $17,442 | $11,781”
  - with_parents_or_family:Books/Supplies: 1460 ⟵ “Books/Supplies | $1,460 | $1,460 | $1,460 | $1,460”
  - with_parents_or_family:Personal/Medical: 9819 ⟵ “Personal/Medical | $9,918 | $9,819 | $9,918 | $9,819”
  - with_parents_or_family:Transportation: 1512 ⟵ “Transportation | $1,512 | $1,512 | $1,512 | $1,512”
  - with_parents_or_family:Loan Fees: 38 ⟵ “Loan Fees | $38 | $38 | $38 | $38”
  - with_parents_or_family:Total:: 29446 ⟵ “Total: | $35,206 | $29,446 | $48,898 | $43,138”

## Exceptions (16)

### `760d4c63adb1aa61` Arapahoe Community College — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.arapahoe.edu/sites/default/files/about-acc/ir/common-data-set-2024-2025-acc.pdf (sha256 bdaab3b5ec72)
- issues: stale_year_label:2024-25
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 2770 ⟵ “Total first-time, first-year (degree-seeking) who applied          2613         156              0          1      2770”
  - admits: 2770 ⟵ “Total first-time, first-year (degree-seeking) who were admitted    2613         156              0          1      2770”
  - enrolled: 1074 ⟵ “Total first-time, first-year (degree-seeking) enrolled             1059         14               0          1      1074”
### `230878f03de4866e` Arapahoe Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.arapahoe.edu/sites/default/files/finaid/2025-2026-professional-judgment-with-income-projection-form.pdf (sha256 da218d9c6e34)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.arapahoe.edu/admissions/paying-college/financial-aid
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment Request 2025-2026 A.”
  - sentence: professional_judgment ⟵ “REASON FOR REQUEST • You can request a Professional Judgment review if something about your financial situation has changed since the tax year used on your FAFSA.”
### `40824ccc0fd84e58` Arapahoe Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.arapahoe.edu/admissions/paying-college/financial-aid (sha256 d89b3c2dc043)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.arapahoe.edu/sites/default/files/finaid/2025-2026-professional-judgment-with-income-projection-form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgement: Financial aid may be reassessed if the FAFSA on file doesn’t reflect your current financial situation (for example: divorce, loss of job, marriage, or other qualifying event).”
### `b4a34e5151d0be65` Arapahoe Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.arapahoe.edu/sites/default/files/finaid/how-to-request-professional-judgment-review.pdf (sha256 4a393ec015d0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “How to Request a Professional Judgment Review 1.”
  - sentence: professional_judgment ⟵ “Note: Professional Judgment is available under specific circumstances.”
### `f765e88689b2d330` Arapahoe Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.arapahoe.edu/sites/default/files/finaid/how-to-request-professional-judgment-review.pdf (sha256 4a393ec015d0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Appeal: If you are not in contact with your parents and want to be considered independent or if you are orphaned, an emancipated minor, etc. 2.”
### `b97bb1cbdf1d8a41` Front Range Community College — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.frontrange.edu/_resources/docs/about-frcc/ir-student-data/FRCC%202024-2025%20CDS-remediated.pdf (sha256 8fd7f53b8432)
- issues: stale_year_label:2024-25
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 6506 ⟵ “Total first-time, first-year (degree-seeking) who applied             6168      338       Not Available         6506”
  - admits: 6506 ⟵ “Total first-time, first-year (degree-seeking) who were admitted       6168      338       Not Available         6506”
  - enrolled: 2172 ⟵ “Total first-time, first-year (degree-seeking) enrolled                2133      39        Not Available         2172”
### `6b2bd2d8074b2589` Front Range Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.frontrange.edu/admissions-aid/paying-for-college/tuition-fees/cost-of-attendance.html (sha256 023490fa48e7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Child Care Professional Judgment to Increase Cost of Attendance (COA) Students who feel that their assigned cost of attendance does not appropriately reflect their personal childcare expenses can file a Professional Judgment appeal to have their cost of attendance reevaluated.”
### `8f8f6afbeb0231c0` Front Range Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.frontrange.edu/admissions-aid/paying-for-college/financial-aid/financial-aid-basics/satisfactory-academic-progress.html (sha256 7eff1beaebc9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appeal Forms To complete a financial aid appeal, you will need to submit your request via the Financial Aid Satisfactory Academic Progress (SAP) Appeal form.”
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress (SAP) Appeal Form If you are appealing for a medical and/or mental health reason, you are required to have your doctor or mental health practitioner complete the FRCC Medical/Mental Health Documentation Form to include with your appeal.”
  - sentence: sap_appeal ⟵ “Processing Timeline Satisfactory Academic Progress appeals are reviewed consistently throughout the year and students who have appealed through financial aid should receive a decision within two to three weeks after submitting the online SAP Appeal form.”
### `efbc2f1b63b2e94c` Front Range Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.frontrange.edu/admissions-aid/paying-for-college/ (sha256 930e5af230ba)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Our Financial Aid Office will help you access funds from the state and FRCC programs. east Financial Aid Options Special & Unusual Circumstances Does the FAFSA (Free Application for Federal Student Aid) not portray an accurate picture of your situation?”
  - sentence: need_based_special_circumstances ⟵ “Learn more about special or unusual circumstances. east Special Circumstances More Information Financial Aid FAQs Financial Aid Tutorials Refunds Loan Repayment Satisfactory Academic Progress CARES ACT Report & Disclosure Front Range Community College home page chat_bubbleContact Usvolunteer_activismGive to FRCC Locations Boulder County 2190 Miller Drive Longmont, CO 80501 303-678-3722 Westminster”
### `22c2865bff417ec9` University of Colorado Boulder — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.colorado.edu/undergraduate/admissions/credit-examination/ (sha256 a3cb7cb87fa0)
- issues: conflicting_sources:https://catalog.colorado.edu/undergraduate/admissions/credit-examination/credit-examination.pdf
- checks: {"distinct_exams": 34, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4,5]:  ⟵ “African American Studies | African American Studies | 4,5 | 3 lower-division Ethnic Studies (ETHN) credits that count toward Social Science category of the A&S Gen. Ed. Distribution Requirement | 3”
  - equivalencies[AP-BIOLOGY|5, 4]:  ⟵ “Biology | Biology | 5, 4 | EBIO 1210, EBIO 1220, EBIO 1230 and EBIO 1240 | 8”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | Chemistry | 5 | CHEM 1113 and CHEM 1114 | 5”
  - equivalencies[AP-COMPUTER-SCIENCE-A|5]:  ⟵ “Computer Science 1 | Computer Science A | 5 | CSCI 1300 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|5]:  ⟵ “ | Computer Science Principles | 5 | CSCI 1300 | 4”
  - equivalencies[AP-MICROECONOMICS|5, 4]:  ⟵ “Economics | Economics: Micro | 5, 4 | ECON 2010 | 4”
  - equivalencies[AP-MACROECONOMICS|5, 4]:  ⟵ “ | Economics: Macro | 5, 4 | ECON 2020 | 4”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|5,4]:  ⟵ “English | English Literature and Composition | 5,4 | ENGL 1500 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5,4]:  ⟵ “ | English Language and Composition | 5,4 | WRTG 1150 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|5, 4, 3]:  ⟵ “Environmental Science | Environmental Science | 5, 4, 3 | 4 lower-division Arts & Science credits that fulfill the lab portion of and count toward the A&S Gen. Ed. Natural Science requirement and the CMDI Core Natural World requirement | 4”
  - equivalencies[AP-DRAWING|5, 4]:  ⟵ “Fine Arts | Studio-Drawing Portfolio or Studio-General Portfolio | 5, 4 | 3 lower-division ARTS elective credits that count toward the A&S Gen. Ed. Arts and Humanities requirement and the CMDI Core Humanities and the Arts requirement | 3”
  - equivalencies[AP-ART-HISTORY|5, 4]:  ⟵ “ | Art History | 5, 4 | 3 lower-division ARTH credits that count toward ARTH and ARTS majors and the A&S Gen. Ed. Arts and Humanities requirement and the CMDI Core Humanities and the Arts requirement | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|5, 4]:  ⟵ “Geography | Human Geography | 5, 4 | GEOG 1992 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|5, 4]:  ⟵ “History | US History | 5, 4 | HIST 1025 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|5, 4]:  ⟵ “ | European History | 5, 4 | HIST 1012 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|5, 4]:  ⟵ “ | World History | 5, 4 | 3 lower-division History credits that count toward the A&S Gen. Ed. Arts & Humanities requirement and the CMDI Core Humanities & the Arts and Historical Perspectives requirements | 3”
  - equivalencies[AP-CALCULUS-AB|5, 4]:  ⟵ “Mathematics | Math-Calculus AB | 5, 4 | MATH 1300 | 5”
  - equivalencies[AP-CALCULUS-BC|5, 4]:  ⟵ “ | Math-Calculus BC | 5, 4 | MATH 1300 and MATH 2300 | 10”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “ | Math-Calculus BC | 3 |  | ”
  - equivalencies[AP-PRECALCULUS|4,5]:  ⟵ “ | Precalculus | 4,5 | MATH1150 | 4”
  - equivalencies[AP-STATISTICS|5, 4]:  ⟵ “ | Statistics | 5, 4 | MATH 2510 | 3”
  - equivalencies[AP-MUSIC-THEORY|5]:  ⟵ “Music | Music Theory | 5 | MUSC 1101, MUSC 1111, MUSC 1121 and MUSC 1131 | 6”
  - equivalencies[AP-PHYSICS-1|5, 4]:  ⟵ “Physics | Physics 1 | 5, 4 | PHYS 2010 | 5”
  - equivalencies[AP-PHYSICS-2|5, 4]:  ⟵ “ | Physics 2 | 5, 4 | PHYS 2020 | 5”
  - equivalencies[AP-PHYSICS-C-MECHANICS|5]:  ⟵ “ | Physics C-Mechanics | 5 | PHYS 1110 | 4”
  - … 10 more rows
### `b71c7211e26b10c0` University of Colorado Boulder — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.colorado.edu/undergraduate/admissions/credit-examination/credit-examination.pdf (sha256 31e6f7334e6b)
- issues: score_scale_mismatch, conflicting_sources:https://catalog.colorado.edu/undergraduate/admissions/credit-examination/
- checks: {"distinct_exams": 16, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry      Chemistry             5   CHEM 1113 and CHEM 1114 5                                                     Core Humanities and the”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History   5, HIST 1012                   3              Statistics          5, MATH 2510                     3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History      5, 3 lower-division History   3     Music     Music Theory        5   MUSC 1101, MUSC 1111,   6”
  - equivalencies[AP-CALCULUS-AB|5]:  ⟵ “Mathematics Math-Calculus AB    5, MATH 1300                   5                                  4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C-Mechanics 5   PHYS 1110                    4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4]:  ⟵ “Physics C-Electricity 5   PHYS 1120                  4        department strongly recommends enrolling at the lower of the two”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology   Psychology           5, PSYC 1001                    3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language      5    FREN 2110, FREN 2120 and 9      granted 24 hours of college credit. This credit will be applied toward”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language      5    GRMN 2020 and              7    exam—shall be granted 24 hours of college credit. If a student scores”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin                5    LATN 1024, LATN 2114 and 12”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|5]:  ⟵ “Spanish Language     5    SPAN 2110, SPAN 2120 and 11     Anthropology Higher                     4   ANTH 2100 and 3 lower-         6”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|5]:  ⟵ “Spanish Literature   5    SPAN 1000 and SPAN 3002 6                                                   Core People and Society”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology        Higher           4   EBIO 1210, EBIO 1220,       8                                  requirement and the CMDI”
  - equivalencies[AP-CHEMISTRY|7]:  ⟵ “Chemistry      Higher           7   CHEM 1113, CHEM 1114,   10        Environmental Standard   4   3 lower-division Arts &     3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese A:   Higher             4   CHIN 3110, CHIN 3120        10                             5”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History Standard   4   3 lower-division Arts &      3    and                     6,”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|6]:  ⟵ “Italian B     Higher     7, ITAL 2110 and ITAL 2120       6                                Thinking requirement”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|7]:  ⟵ “Italian B     Standard   7   ITAL 2110 and ITAL 2120      6                                Reasoning & Mathematical”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|7]:  ⟵ “Italian AB    Initio     7   ITAL 1020                    5”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4]:  ⟵ “Japanese A: Higher       4   JPNS 3110, JPNS 3120         10                               Skills requirement and the”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|5]:  ⟵ “Japanese AB Initio       5   JPNS 1010, JPNS 1020         10”
  - equivalencies[AP-PSYCHOLOGY|4]:  ⟵ “Psychology     Higher           4   PSYC 1001 and 3 lower-       6”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|4]:  ⟵ “Spanish A:   Higher             4   SPAN 3000 and SPAN 3100 8”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|60]:  ⟵ “German 9             60         ARSC       AH4        3 credits”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|63]:  ⟵ “Spanish 9            63         ARSC       AH4        3 credits              Western 3        50      ARSC     HI1       Arts and”
  - … 2 more rows
### `cb9527ddb538f242` University of Colorado Boulder — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.colorado.edu/undergraduate/admissions/credit-examination/ (sha256 a3cb7cb87fa0)
- issues: score_column_not_scores
- checks: {"distinct_exams": 23, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|Higher]:  ⟵ “Anthropology | Higher | 4 | ANTH 2100 and 3 lower-division credit hours that count toward the A&S Gen. Ed. Social Science requirement and the CMDI Core People and Society requirement | 6”
  - equivalencies[IB-BIOLOGY|Higher]:  ⟵ “Biology | Higher | 4 | EBIO 1210, EBIO 1220, EBIO 1230 and EBIO 1240 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Higher]:  ⟵ “Business and Management | Higher | 4 | 6 lower-division BADM credit hours | 6”
  - equivalencies[IB-CHEMISTRY|Higher]:  ⟵ “Chemistry | Higher | 7 | CHEM 1113, CHEM 1114, CHEM 1133 and CHEM 1134 | 10”
  - equivalencies[IB-COMPUTER-SCIENCE|Higher]:  ⟵ “Computer Science | Higher | 4 | CSCI 1300 | 4”
  - equivalencies[IB-ECONOMICS|Higher]:  ⟵ “Economics | Higher | 4 | 4 lower-division ECON credits that count toward the A&S Gen. Ed. Social Science requirement and the CMDI Core People and Society requirement | 4”
  - equivalencies[IB-ENGLISH-A-LITERATURE|Higher]:  ⟵ “English A: Literature | Higher | 4 | ENGL 1500 | 3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|Higher]:  ⟵ “English A: Language and Literature | Higher | 4 | WRTG 1150 | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|Standard]:  ⟵ “Environmental Systems & Societies | Standard | 4 | 3 lower-division Arts & Science credits that count toward the A&S Gen. Ed. Natural Science requirement and the CMDI Core Natural World requirement | 3”
  - equivalencies[IB-FRENCH|Higher]:  ⟵ “French B | Higher | 7 | FREN 2120 and FREN 2500 | 6”
  - equivalencies[IB-FRENCH|Standard]:  ⟵ “French B | Standard | 7 | FREN 2110 and FREN 2120 | 6”
  - equivalencies[IB-FRENCH|Initio]:  ⟵ “French AB | Initio | 7 | FREN 1050 | 5”
  - equivalencies[IB-GEOGRAPHY|Higher]:  ⟵ “Geography | Higher | 4 | GEOG 1992 and 3 lower-division GEOG credits that count toward the A&S Gen. Ed. Social Science requirement and the CMDI Core People and Society requirement | 6”
  - equivalencies[IB-GERMAN|Standard]:  ⟵ “German B | Standard | 6, 7 | GRMN 1010 and GRMN 1020 | 8”
  - equivalencies[IB-GLOBAL-POLITICS|Higher]:  ⟵ “Global Politics | Higher | 4 | 3 lower division PSCI credits that count toward the A&S Gen. Ed. Social Science requirement and the CMDI Core People and Society requirement | 3”
  - equivalencies[IB-HISTORY|Higher]:  ⟵ “History of Africa and the Middle East | Higher | 4 | Two 3-credit lower-division HIST courses that count toward the A&S Gen. Ed. Arts and Humanities requirement and the CMDI Core Humanities and the Arts and Historical Perspectives requirements. One of the courses will also fulfill the Global Perspec”
  - equivalencies[IB-HISTORY|Higher]:  ⟵ “History of the Americas | Higher | 4 | HIST 1025 and 3 lower-division HIST credits that count toward the A&S Gen. Ed. Arts and Humanities requirement and the CMDI Core Humanities and the Arts and Historical Perspectives requirements | 6”
  - equivalencies[IB-HISTORY|Higher]:  ⟵ “History of Asia and Oceania | Higher | 4 | Two 3-credit lower division HIST that count toward the A&S Gen. Ed. Arts and Humanities requirement and the CMDI Core Humanities and the Arts and Historical Perspectives requirements | 6”
  - equivalencies[IB-HISTORY|Higher]:  ⟵ “History of Europe | Higher | 4 | HIST 1012 and 3 lower-division HIST credits that count toward the A&S Gen. Ed. Arts and Humanities requirement and the CMDI Core Humanities and the Arts and Historical Perspectives requirements | 6”
  - equivalencies[IB-HISTORY|Standard]:  ⟵ “World History | Standard | 4 | 3 lower-division Arts & Science credits that count toward the A&S Gen. Ed. Arts and Humanities requirement and the CMDI Core Humanities and the Arts and Historical Perspectives requirements | 3”
  - equivalencies[IB-LATIN|Higher]:  ⟵ “Latin | Higher | 6, 7 | LATN 1024, LATN 2114, LATN 2124 | 12”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|Higher]:  ⟵ “Mathematics: Analysis and Approaches | Higher | 7 | MATH1300 | 5”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|Higher]:  ⟵ “Mathematics: Applications and Interpretation | Higher | 4 , 5, 6, 7 | MATH 2510 | 3”
  - equivalencies[IB-MUSIC|Higher]:  ⟵ “Music | Higher | 4 | Elective credit hours | 6”
  - equivalencies[IB-PHILOSOPHY|Higher]:  ⟵ “Philosophy | Higher | 4 | PHIL 1000 and 3 lower-division PHIL credits that count toward the A&S Gen. Ed. Arts and Humanities requirement and the CMDI Core Humanities and the Arts requirement | 6”
  - … 6 more rows
### `d92890285d4fcf0f` University of Colorado Boulder — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.colorado.edu/undergraduate/admissions/credit-examination/ (sha256 a3cb7cb87fa0)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 27, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “Composition and Literature | American Literature | 3 | 50 | ARSC 1999TC | AH2 | Arts and Humanities”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “ | Analyzing and Interpreting Literature | 3 | 50 | ARSC 1999TC | AH2 | Arts and Humanities”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “ | College Composition | 6 | 50 | ARSC 1999TC | CO1 & CO2 | Written Communication”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “ | College Composition Modular | 3 | 50 | ARSC 1999TC | CO1 | Written Communication”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “ | English Literature | 3 | 50 | ARSC 1999TC | AH2 | Arts and Humanities”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | Humanities | 3 | 50 | ARSC 1999TC | AH1 | Arts and Humanities”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “Languages | French Language: Level 2 | 9 | 59 | ARSC 1999TC | AH4 | 3 credits of Arts and Humanities and 6 credits of Electives”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “ | German Language: Level 2 | 9 | 60 | ARSC 1999TC | AH4 | 3 credits of Arts and Humanities and 6 credits of Electives”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “ | Spanish Language: Level 2 | 9 | 63 | ARSC 1999TC | AH4 | 3 credits of Arts and Humanities and 6 credits of Electives”
  - equivalencies[CLEP-SPANISH-LANGUAGE|65]:  ⟵ “ | Spanish Language w/Writing: Level 2 | 12 | 65 | ARSC 1999TC | AH4 | 3 credits of Arts and Humanities and 9 credits of Electives”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “History and Social Sciences | American Government | 3 | 50 | ARSC 1999TC | SS1 | Social Sciences”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “ | History of the United States I | 3 | 50 | ARSC 1999TC | HI1 | Arts and Humanities”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “ | History of the United States II | 3 | 50 | ARSC 1999TC | HI1 | Arts and Humanities”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “ | Human Growth and Development | 3 | 50 | ARSC 1999TC | SS3 | Social Sciences”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “ | Introduction to Educational Psychology | 3 | 50 | ARSC 1999TC | SS3 | Social Sciences”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|54]:  ⟵ “ | Introductory Psychology | 3 | 54 | PSYC 1001 |  | Social Sciences”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|54]:  ⟵ “ | Introductory Sociology | 3 | 54 | SOCY 1001 | SS3 | Social Sciences”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|54]:  ⟵ “ | Principles of Macroeconomics | 4 | 54 | ECON 2020 |  | Social Sciences”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|54]:  ⟵ “ | Principles of Microeconomics | 4 | 54 | ECON 2010 |  | Social Sciences”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “ | Social Sciences and History | 3 | 50 | ARSC 1999TC | HI1 or SS1 | Social Sciences”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “ | Western Civilization I: Ancient Near East to 1648 | 3 | 50 | ARSC 1999TC | HI1 | Arts and Humanities”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “ | Western Civilization II: 1648 to the Present | 3 | 50 | ARSC 1999TC | HI1 | Arts and Humanities”
  - equivalencies[CLEP-BIOLOGY|54]:  ⟵ “Biological and Physical Sciences | Biology | 6 | 54 | EBIO 1210, EBIO 1220 | SC2 | Natural Science”
  - equivalencies[CLEP-CHEMISTRY|54]:  ⟵ “ | Chemistry | 6 | 54 | CHEM 1113, ARSC1999TC | SC2 | 4 credits of Natural Sciences and 2 credits of Electives”
  - equivalencies[CLEP-CALCULUS|54]:  ⟵ “Mathematics | Calculus | 5 | 54 | MATH 1300 | MA1 | Quantitative Reasoning”
  - … 5 more rows
### `mf758ef9217dc1ec` University of Colorado Boulder — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/policies-requirements/ (sha256 e5b015e8de04)
- issues: conflicting_sources:min_grade
- checks: {"fields": ["min_grade", "residency_requirement_credits"], "merged_pages": 4}
  - min_grade: C ⟵ “The minimum admission criteria to transfer to the BA in Computer Science Degree Program are as follows: Cumulative GPA of 2.5 or higher Calculus 1 (grade of C or better) Calculus 2 (grade of C or better) Introduction to Computer Programming Must be a computer programming language course (Java, Python, C, C++) C++ is preferred B grade or higher in all computing courses Note: AP/IB credit does not c”
  - min_grade: C ⟵ “The minimum admission criteria to transfer to the BA in Computer Science Degree Program are as follows: Cumulative GPA of 2.5 or higher Calculus 1 (grade of C or better) Calculus 2 (grade of C or better) Introduction to Computer Programming Must be a computer programming language course (Java, Python, C, C++) C++ is preferred B grade or higher in all computing courses Note: AP/IB credit does not c”
  - min_grade: C- ⟵ “Criteria for Acceptance of Credit Only courses taken at a college or university of recognized standing with grades of C- (1.70) or better are accepted for transfer.”
  - min_grade: C- ⟵ “Only courses taken at a college or university of recognized standing with grades of C- or better are accepted for transfer.”
  - min_grade: C- ⟵ “Transfer of College-Level Credit 1 TRANSFER OF COLLEGE- Criteria for Acceptance of Credit Only courses taken at a college or university of recognized standing with LEVEL CREDIT grades of C- (1.70) or better are accepted for transfer.”
  - min_grade: C- ⟵ “Transfer Credit Policies Transfer of credit from other institutions of higher education Work from another accredited institution of higher education that has been completed with a grade of C- (1.70) or better may be transferred to the University of Colorado.”
  - min_grade: C- ⟵ “Only courses taken at a college or university of recognized standing with grades of C- or better are accepted for transfer.”
  - residency_requirement_credits: 30 ⟵ “Graduation with Distinction Students will graduate "With Distinction" if they have completed at least 30 credit hours with a letter grade at the University of Colorado Boulder and have a grade point average of 3.750 or higher for all coursework completed at the University of Colorado.”
### `2237beaf20273255` University of Colorado Denver/Anschutz Medical Campus — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://clas.ucdenver.edu/esl/future-students/tuition-fees (sha256 eef7b2c909cd)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition*: 3600 ⟵ “Tuition* | $3,600”
  - column:Student Fees**: 744 ⟵ “Student Fees** | $744”
  - column:Health Insurance (Estimated): 400 ⟵ “Health Insurance (Estimated) | $400”
  - column:Books (Estimated): 250 ⟵ “Books (Estimated) | $250”
  - column:Other Living Expenses (Estimated): 4920 ⟵ “Other Living Expenses (Estimated) | $4,920”
  - column:Total Cost of Attendance for I-20:: 9914 ⟵ “Total Cost of Attendance for I-20: | $9,914”
  - column:Cost per dependent (Estimated annually): 9000 ⟵ “Cost per dependent (Estimated annually) | $9,000”
  - column:Total Tuition and Fee Charge: 4344 ⟵ “Total Tuition and Fee Charge | $4,344”
### `71dbbd3a03a256d6` University of Colorado Denver/Anschutz Medical Campus — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://clas.ucdenver.edu/esl/lynxdirect-pathway-program (sha256 acbcc77e6cbc)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition & Fees*: 12807 ⟵ “Tuition & Fees* | $12,807”
  - column:Living Expenses: 9841 ⟵ “Living Expenses | $9,841”
  - column:Books & Insurance: 1300 ⟵ “Books & Insurance | $1,300”
  - column:Total (I-20 Amount): 23948 ⟵ “Total (I-20 Amount) | $23,948”

## Re-verification of existing records (92)

- source_not_fetched: data/institutions/aims/credit_policies/2026-27.json ["credit_policies", "ipeds-126207", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/aims/credit_policies/2026-27.json ["credit_policies", "ipeds-126207", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/coloradocollege/transfer_policies/2026-27.json ["transfer_policies", "ipeds-126678", null, "2026-27", {}]
- source_not_fetched: data/institutions/coloradomesa/transfer_policies/2026-27.json ["transfer_policies", "ipeds-127556", null, "2026-27", {}]
- source_not_fetched: data/institutions/mines/transfer_policies/2026-27.json ["transfer_policies", "ipeds-126775", null, "2026-27", {}]
- source_not_fetched: data/institutions/colostate/transfer_policies/2026-27.json ["transfer_policies", "ipeds-126818", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/frontrange/costs/2026-27.json ["costs", "ipeds-127200", null, "2026-27", {"residency": "in_state"}]
- all_values_found_year_not_labeled: data/institutions/frontrange/costs/2026-27.json ["costs", "ipeds-127200", null, "2026-27", {"residency": "out_of_state"}]
- source_not_fetched: data/institutions/morgancc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-127617", null, "2026-27", {}]
- source_not_fetched: data/institutions/njc/awards/2026-27.json ["awards", "ipeds-127732", null, "2026-27", {"award_name": "Faculty Senate Impact Scholarship"}]
- source_not_fetched: data/institutions/njc/awards/2026-27.json ["awards", "ipeds-127732", null, "2026-27", {"award_name": "NJC Foundation International Studies Scholarship (Freshman)"}]
- source_not_fetched: data/institutions/njc/awards/2026-27.json ["awards", "ipeds-127732", null, "2026-27", {"award_name": "NJC Foundation International Studies Scholarship (Sophomores)"}]
- source_not_fetched: data/institutions/njc/awards/2026-27.json ["awards", "ipeds-127732", null, "2026-27", {"award_name": "NJC Foundation Transfer Scholarship Application (For NJC Graduates)"}]
- source_not_fetched: data/institutions/njc/awards/2026-27.json ["awards", "ipeds-127732", null, "2026-27", {"award_name": "Spring Beginnings Scholarship"}]
- source_not_fetched: data/institutions/njc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-127732", null, "2026-27", {}]
- source_not_fetched: data/institutions/otero/transfer_policies/2026-27.json ["transfer_policies", "ipeds-127778", null, "2026-27", {}]
- source_not_fetched: data/institutions/pueblocc/costs/2026-27.json ["costs", "ipeds-127884", null, "2026-27", {"residency": "in_state"}]
- source_not_fetched: data/institutions/pueblocc/costs/2026-27.json ["costs", "ipeds-127884", null, "2026-27", {"residency": "out_of_state"}]
- source_not_fetched: data/institutions/regis/transfer_policies/2026-27.json ["transfer_policies", "ipeds-127918", null, "2026-27", {}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "cinema-studies-bachelor-of-arts-ba", "requirement_key": "critical-studies-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "cinema-studies-bachelor-of-arts-ba", "requirement_key": "production-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "earth-science-bachelor-of-science-bs", "requirement_key": "geosciences-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "earth-science-bachelor-of-science-bs", "requirement_key": "geophysics-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "english-bachelor-of-arts-ba", "requirement_key": "literature-track"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "english-bachelor-of-arts-ba", "requirement_key": "creative-writing-track"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "geography-bachelor-of-science-bs", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "russian-east-european-and-eurasian-studies-bachelor-of-arts-ba", "requirement_key": "track-a-russian-language"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "russian-east-european-and-eurasian-studies-bachelor-of-arts-ba", "requirement_key": "track-b-russian-east-european-and-eurasian-culture-and-literature"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "russian-east-european-and-eurasian-studies-bachelor-of-arts-ba", "requirement_key": "track-c-russian-east-european-and-eurasian-studies-major-for-heritage-speakers"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "jewish-studies-bachelor-of-arts-ba", "requirement_key": "culture-intensive-concentration"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "jewish-studies-bachelor-of-arts-ba", "requirement_key": "foreign-language-intensive-concentration"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "theatre-bachelor-of-fine-arts-bfa", "requirement_key": "acting-concentration"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "theatre-bachelor-of-fine-arts-bfa", "requirement_key": "design-technology-management-concentration"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "theatre-bachelor-of-fine-arts-bfa", "requirement_key": "musical-theatre-concentration"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "women-and-gender-studies-bachelor-of-arts-ba", "requirement_key": "queer-and-trans-studies-concentration"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "media-production-bachelor-of-arts-ba", "requirement_key": "documentary-concentration"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "media-production-bachelor-of-arts-ba", "requirement_key": "immersive-media-concentration"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "media-production-bachelor-of-arts-ba", "requirement_key": "sound-practices-concentration"}]
- nothing_to_check: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "middle-and-high-school-teaching-bachelor-of-arts-ba", "requirement_key": "english-language-arts-track"}] year=2026-27
- nothing_to_check: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "middle-and-high-school-teaching-bachelor-of-arts-ba", "requirement_key": "mathematics-track"}] year=2026-27
- nothing_to_check: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "middle-and-high-school-teaching-bachelor-of-arts-ba", "requirement_key": "science-track"}] year=2026-27
- nothing_to_check: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "middle-and-high-school-teaching-bachelor-of-arts-ba", "requirement_key": "social-studies-track"}] year=2026-27
- nothing_to_check: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "middle-and-high-school-teaching-bachelor-of-arts-ba", "requirement_key": "spanish-track"}] year=2026-27
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "biomedical-engineering-bachelor-of-science-bsbm", "requirement_key": "premedical-track"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "integrated-design-engineering-bachelor-of-science-bside", "requirement_key": "aerospace-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "integrated-design-engineering-bachelor-of-science-bside", "requirement_key": "architectural-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "integrated-design-engineering-bachelor-of-science-bside", "requirement_key": "civil-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "integrated-design-engineering-bachelor-of-science-bside", "requirement_key": "electrical-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "integrated-design-engineering-bachelor-of-science-bside", "requirement_key": "environmental-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "integrated-design-engineering-bachelor-of-science-bside", "requirement_key": "mechanical-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-education-bachelor-of-music-education-bmue", "requirement_key": "choral-music-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-education-bachelor-of-music-education-bmue", "requirement_key": "choral-general-music-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-education-bachelor-of-music-education-bmue", "requirement_key": "instrumental-music-emphasis-band"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-education-bachelor-of-music-education-bmue", "requirement_key": "instrumental-emphasis-strings"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-education-bachelor-of-music-education-bmue", "requirement_key": "instrumental-general-music-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-education-bachelor-of-music-education-bmue", "requirement_key": "instrumental-jazz-emphasis-saxophone-trumpet-trombone-percussion"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-arts-in-music-bamus", "requirement_key": "general-program-no-emphasis"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-arts-in-music-bamus", "requirement_key": "emphasis-in-jazz"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-arts-in-music-bamus", "requirement_key": "emphasis-in-music-production"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-arts-in-music-bamus", "requirement_key": "emphasis-in-music-technology-and-media-studies"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-arts-in-music-bamus", "requirement_key": "emphasis-in-musicology-and-world-musics"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-arts-in-music-bamus", "requirement_key": "emphasis-in-songwriting"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "brass-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "brass-performance-with-secondary-emphasis-in-jazz-available-for-trumpet-trombone"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "classical-guitar-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "composition-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "harp-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "harpsichord-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "jazz-piano-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "jazz-studies-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "musical-theatre-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "musicology-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "organ-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "percussion-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "percussion-performance-with-secondary-emphasis-in-jazz-available-for-vibes-marim"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "piano-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "string-performance-concentration-area-double-bass-viola-violin-and-violoncello"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "voice-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "woodwind-performance-concentration-area"}]
- source_not_fetched: data/institutions/colorado/degree_requirements/2026-27.json ["degree_requirements", "ipeds-126614", null, "2026-27", {"program_key": "music-bachelor-of-music-bmus", "requirement_key": "woodwind-performance-with-secondary-emphasis-in-jazz-available-for-saxophone"}]
- source_not_fetched: data/institutions/uccs/credit_policies/2026-27.json ["credit_policies", "ipeds-126580", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/uccs/credit_policies/2026-27.json ["credit_policies", "ipeds-126580", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/uccs/credit_policies/2026-27.json ["credit_policies", "ipeds-126580", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/western/awards/2026-27.json ["awards", "ipeds-128391", null, "2026-27", {"award_name": "East Merit"}]
- source_not_fetched: data/institutions/western/awards/2026-27.json ["awards", "ipeds-128391", null, "2026-27", {"award_name": "Slate Merit"}]
- source_not_fetched: data/institutions/western/awards/2026-27.json ["awards", "ipeds-128391", null, "2026-27", {"award_name": "Taylor Merit"}]
- source_not_fetched: data/institutions/western/awards/2026-27.json ["awards", "ipeds-128391", null, "2026-27", {"award_name": "Basin Merit"}]
- source_not_fetched: data/institutions/western/awards/2026-27.json ["awards", "ipeds-128391", null, "2026-27", {"award_name": "Ridgeline Merit"}]
- source_not_fetched: data/institutions/western/awards/2026-27.json ["awards", "ipeds-128391", null, "2026-27", {"award_name": "Peak Merit"}]
- source_not_fetched: data/institutions/western/degree_requirements/2026-27.json ["degree_requirements", "ipeds-128391", null, "2026-27", {"program_key": "graphic-design-bachelor-of-arts", "requirement_key": "graphic-design-bachelor-of-arts-one-of-the-following-career-pathways"}]
- source_not_fetched: data/institutions/western/degree_requirements/2026-27.json ["degree_requirements", "ipeds-128391", null, "2026-27", {"program_key": "graphic-design-bachelor-of-arts", "requirement_key": "graphic-design-bachelor-of-arts-and-12-credits-of-the-following"}]
- source_not_fetched: data/institutions/western/degree_requirements/2026-27.json ["degree_requirements", "ipeds-128391", null, "2026-27", {"program_key": "graphic-design-bachelor-of-fine-arts", "requirement_key": "graphic-design-bachelor-of-fine-arts-and-the-following-required-courses"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Arapahoe Community College: cost_of_attendance, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Front Range Community College: merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency
- University of Colorado Boulder: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, aid_appeals
- University of Colorado Denver/Anschutz Medical Campus: admissions_tests, merit_scholarships, ib_credit, transfer_credit, residency
