# Review queue — NJ (2026-27)

Pages fetched: 3707; failures: 255. Candidates: 435 (133 without issues, 302 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 8 | 17 | 22 | 6 | 19 |
| cost_of_attendance | 0 | 0 | 3 | 14 | 26 | 10 | 19 |
| admissions_tests | 0 | 0 | 0 | 1 | 47 | 5 | 19 |
| common_data_set | 0 | 0 | 0 | 1 | 8 | 44 | 19 |
| merit_scholarships | 0 | 0 | 2 | 4 | 38 | 9 | 19 |
| ap_credit | 0 | 0 | 4 | 8 | 19 | 22 | 19 |
| clep_credit | 0 | 0 | 1 | 4 | 11 | 37 | 19 |
| ib_credit | 0 | 0 | 1 | 5 | 4 | 43 | 19 |
| dual_enrollment | 0 | 0 | 6 | 1 | 27 | 19 | 19 |
| transfer_credit | 0 | 0 | 14 | 4 | 26 | 9 | 19 |
| statewide_articulation | 0 | 0 | 0 | 0 | 23 | 30 | 19 |
| residency | 0 | 0 | 0 | 0 | 25 | 28 | 19 |
| degree_requirements | 0 | 0 | 2 | 0 | 34 | 17 | 19 |
| aid_appeals | 0 | 0 | 0 | 36 | 7 | 10 | 19 |

## Ready for review (133)

### `486e0659dce35b1b` Atlantic Cape Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://atlanticcape.edu/one-stop/student-types/high-school/dual-enrollment.php (sha256 f77034813d6c)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 73 ⟵ “Through Atlantic Cape’s Dual Enrollment program students only pay $73 per credit—a savings of nearly 60%! To earn college credit, students must earn a grade of C or better in their high school dual credit course.”
### `50f4bf79a0af09dc` Atlantic Cape Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://atlanticcape.edu/student-resources/transfer-planning/transfer-agreements.php (sha256 c75492aad427)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Typically, any college-level course that is completed with a grade of "C" or better is eligible to transfer.”
### `m927cbc331f62022` Bergen Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://bergen.edu/new-students/transfertobcc/ (sha256 6a63da7d1b28)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Only those courses that have received a grade of “C” or better are accepted for transfer.”
  - min_grade: C ⟵ “Only those courses that have received a grade of “C” or better are accepted for transfer.”
### `25436eb2c7c086b6` Brookdale Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.brookdalecc.edu/financial-aid/about-your-award/ (sha256 01b07c153736)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - off_campus_not_with_family:Tuition: 8112.0 ⟵ “Tuition | $5,408.00 | $7,462.00 | $8,112.00”
  - off_campus_not_with_family:Books and Supplies: 2000.0 ⟵ “Books and Supplies | $2,000.00 | $2,000.00 | $2,000.00”
  - off_campus_not_with_family:Fees: 1190.0 ⟵ “Fees | $1,190.00 | $1,190.00 | $1,190.00”
  - off_campus_not_with_family:Personal Expenses: 8708.0 ⟵ “Personal Expenses | $8,708.00 | $8,708.00 | $8,708.00”
  - off_campus_not_with_family:Food and Housing: 15678.0 ⟵ “Food and Housing | $15,678.00 | $15,678.00 | $15,678.00”
  - off_campus_not_with_family:Transportation: 3204.0 ⟵ “Transportation | $3,204.00 | $3,204.00 | $3,204.00”
  - off_campus_not_with_family:Loan Fees: 60.0 ⟵ “Loan Fees | $60.00 | $60.00 | $60.00”
  - off_campus_not_with_family:Total Budget: 38952.0 ⟵ “Total Budget | $36,248.00 | $38,302.00 | $38,952.00”
### `fff4321429468cb6` Caldwell University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.caldwell.edu/tuition-and-fees/ (sha256 cc73bc6c59f7)
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition: 20600 ⟵ “Tuition | $20,600 | $20,600”
  - on_campus:Comprehensive Fee*: 1220 ⟵ “Comprehensive Fee* | $1,220 | $1,220”
  - on_campus:Technology Fee*: 188 ⟵ “Technology Fee* | $188 | $188”
  - on_campus:Room Charge (MJRH)**: 4125 ⟵ “Room Charge (MJRH)** | $4,125 | –”
  - on_campus:Resident Meal Plan: 3621 ⟵ “Resident Meal Plan | $3,621 | –”
  - on_campus:Total: 29754 ⟵ “Total | $29,754 | $22,176”
  - with_parents_or_family:Tuition: 20600 ⟵ “Tuition | $20,600 | $20,600”
  - with_parents_or_family:Comprehensive Fee*: 1220 ⟵ “Comprehensive Fee* | $1,220 | $1,220”
  - with_parents_or_family:Technology Fee*: 188 ⟵ “Technology Fee* | $188 | $188”
  - with_parents_or_family:Commuter Meal Plan ($168 Cougar Cash): 168 ⟵ “Commuter Meal Plan ($168 Cougar Cash) | – | $168”
  - with_parents_or_family:Total: 22176 ⟵ “Total | $29,754 | $22,176”
### `ffce796eeb06c8f1` Caldwell University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.caldwell.edu/admissions/transfer-students/standardized-exams/ (sha256 f890c87f4b60)
- checks: {"distinct_exams": 13, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[IB-THEATRE|4 or better on HL]:  ⟵ “Theatre Arts | International Baccalaureate (IB)-HL ONLY | 3 | 4 or better on HL | DR102 | English & Drama”
  - equivalencies[IB-FRENCH|4 or better on HL]:  ⟵ “French B | International Baccalaureate (IB)-HL ONLY | 6 | 4 or better on HL | FR201 & FR202 | Language & Enriched Core”
  - equivalencies[IB-SPANISH|4 or better on HL]:  ⟵ “Spanish 2 | International Baccalaureate (IB)-HL ONLY | 6 | 4 or better on HL | SP201 & SP202 | Language & Enriched Core”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4 or better on HL]:  ⟵ “Business and Management | International Baccalaureate (IB)-HL ONLY | 3 | 4 or better on HL | BU105 | Business”
  - equivalencies[IB-ECONOMICS|4 or better on HL]:  ⟵ “Economics | International Baccalaureate (IB)-HL ONLY | 3 | 4 or better on HL | BU205 | Business”
  - equivalencies[IB-HISTORY|4 or better on SL or HL]:  ⟵ “History | International Baccalaureate (IB)-SL or HL | 3 | 4 or better on SL or HL | Elective Credit | History, Political Science, & Social Studies”
  - equivalencies[IB-HISTORY|4 or better on HL or SL]:  ⟵ “Islamic History | International Baccalaureate (IB)-SL or HL | 3 | 4 or better on HL or SL | HI 338 | History, Political Science, & Social Studies”
  - equivalencies[IB-GEOGRAPHY|4 or better on HL or SL]:  ⟵ “Geography | International Baccalaureate (IB)-SL or HL | 3 | 4 or better on HL or SL | GY 335 | History, Political Science, & Social Studies”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4 or better on HL]:  ⟵ “Social and Cultural Anthropology | International Baccalaureate (IB)-HL ONLY | 3 | 4 or better on HL | AN 225 | Sociology & Anthropology”
  - equivalencies[IB-PSYCHOLOGY|4 or better on HL]:  ⟵ “Psychology | International Baccalaureate (IB)-HL ONLY | 3 | 4 or better on HL | PS150 | Psychology”
  - equivalencies[IB-BIOLOGY|4 or better on HL]:  ⟵ “Biology | International Baccalaureate (IB)-HL ONLY | 3 | 4 or better on HL | BI101 | Sciences”
  - equivalencies[IB-PHYSICS|4 or better on HL]:  ⟵ “Physics | International Baccalaureate (IB)-HL ONLY | 3 | 4 or better on HL | PY201 | Sciences”
  - equivalencies[IB-CHEMISTRY|4 or better on HL]:  ⟵ “Chemistry | International Baccalaureate (IB)-HL ONLY | 3 | 4 or better on HL | CH111 | Sciences”
  - equivalencies[IB-MUSIC|5 or better on HL]:  ⟵ “Music | International Baccalaureate (IB)-HL ONLY | 4 | 5 or better on HL | Music Elective (3 cr.) and MU101 ( 1cr.) | Music”
  - equivalencies[IB-MUSIC|4 or better on SL]:  ⟵ “Music | International Baccalaureate (IB)-SL ONLY | 4 | 4 or better on SL | MU122 (3 cr) and MU 100 (1 cr.) | Music”
### `m9fb5e4eaf1363a6` Caldwell University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.caldwell.edu/admissions/transfer-students/ (sha256 e46f2bb9631b)
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “Only courses in which grades of C or better are earned are eligible for transfer.”
  - min_grade: C ⟵ “Only courses in which grades of C or better are earned are eligible for transfer.”
  - min_grade: C ⟵ “Only courses in which grades of C or better are earned are eligible for transfer.”
### `9a3a60018c2b74e0` County College of Morris — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ccm.edu/wp-content/uploads/2024/08/AP_ExamScores.pdf (sha256 25943dc9a937)
- checks: {"distinct_exams": 22, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                       3          BIO 132”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                       4          BIO 121”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology                       5          BIO 121 & 122”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                     3          CHM 117/118”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                     4          CHM 125/126”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry                     5          CHM 125/126 & CHM 127/128”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese                       3          CHI 111”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Chinese                       4 or 5     CHI 111 & 112”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4 or 5]:  ⟵ “Computer Science A            4 or 5     CMP 128 & 129”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4 or 5]:  ⟵ “English Language              4 or 5     ENG 111”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature            4          ENG 111”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|5]:  ⟵ “English Literature            5          ENG 111 & 112”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3 or 4]:  ⟵ “Environmental Science         3 or 4     BIO 127”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|5]:  ⟵ “Environmental Science         5          BIO 202”
  - equivalencies[AP-EUROPEAN-HISTORY|4 or 5]:  ⟵ “European History              4 or 5     HIS 113”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language               3          FRE 111”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4 or 5]:  ⟵ “French Language               4 or 5     FRE111 & 112”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Literature             3          FRE 221”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German                        3          GER 111”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4 or 5]:  ⟵ “German                        4 or 5     GER 111 & 112”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4 or 5]:  ⟵ “Human Geography               4 or 5     SOC 108”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian                       3          ITL 111”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Italian                       4 or 5     ITL 111 & 112”
  - equivalencies[AP-MICROECONOMICS|4 or 5]:  ⟵ “Microeconomics                4 or 5     ECO 212”
  - equivalencies[AP-MACROECONOMICS|4 or 5]:  ⟵ “Macroeconomics                4 or 5     ECO 211”
  - … 9 more rows
### `c212ea1fdc505539` County College of Morris — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ccm.edu/wp-content/uploads/2024/03/Testing-Center-CLEP-Policy.pdf (sha256 09323d305f1a)
- checks: {"distinct_exams": 8, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology         BIO-121               General Biology I                               Biology                       50            4”
  - equivalencies[CLEP-BIOLOGY|54]:  ⟵ “Biology         BIO-122               General Biology II                              Biology                       54            4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry        CHM-125              General Chemistry I                             Chemistry                      50            3”
  - equivalencies[CLEP-CHEMISTRY|53]:  ⟵ “Chemistry        CHM-127              General Chemistry II                            Chemistry                      53            3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French         FRE-111              Elementary French I                    French Language, Level 1                50            3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “French         FRE-112             Elementary French II                    French Language, Level 2                62            3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German          GER-111             Elementary German I                    German Language, Level 1                 50            3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “German          GER-112             Elementary German II                   German Language, Level 2                 63            3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing        MKT-113            Principles of Marketing                    Principles of Marketing               50            3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology        PSY-113              General Psychology                      Introductory Psychology                50            3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology        SOC-120            Principles of Sociology                  Introductory Sociology **               50            3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish         SPN-111             Elementary Spanish I                   Spanish Language, Level 1                50            3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish         SPN-112             Elementary Spanish II                  Spanish Language, Level 2                63            3”
### `8652988617c83ba0` Drew University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://drew.edu/academic/office-of-the-registrar/transfer-credit/ (sha256 e67e4679ec2e)
- checks: {"distinct_exams": 23, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4 or 5]:  ⟵ “African American Studies | 4 or 5 | 4 | AFRC 101 | [BINT] [PPD]”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History | 4 or 5 | 4 | ARTH 101 or ARTH 102 | [BART] [BHUM]”
  - equivalencies[AP-BIOLOGY|4 or 5]:  ⟵ “Biology | 4 or 5 | 4 | BIOL 189 | [BNS]”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “Calculus AB | 4 or 5 | 4 | MATH 150* | [QUAN]*Students who take both calculus exams (AB and BC) will only receive credit for MATH 150 once.”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 4 | MATH 150* | [QUAN]”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “Calculus BC | 4 or 5 | 8 | MATH 150**andMATH 151 | [2 QUAN] **Students who receive credit for Calculus AB will only receive MATH 151 for Calculus BC. Students may consult with the department for the appropriate course placement.”
  - equivalencies[AP-PRECALCULUS|3, 4, or 5]:  ⟵ “Precalculus | 3, 4, or 5 | 4 | MATH 100 | ”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 4 | CHEM 189 | [BNS]”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | 8 | CHEM 150/160 | [BNS] [QUAN]*Effective Fall 2022”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Chinese Language & Culture | 4 or 5 | 4 | CHIN 201 | Language requirement [FLAN]”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4 or 5]:  ⟵ “Computer Science Principles | 4 or 5 | 4 | CSCI 189 | ”
  - equivalencies[AP-MICROECONOMICS|4 or 5]:  ⟵ “Economics, Microeconomics | 4 or 5 | 4 | ECON 101 | [BSS] [QUAN]”
  - equivalencies[AP-MACROECONOMICS|4 or 5]:  ⟵ “Economics, Macroeconomics | 4 or 5 | 4 | ECON 102 | [BSS] [QUAN]”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4 or 5]:  ⟵ “Environmental Science | 4 or 5 | 4 | ENV 150 | [BNS] [BINT]”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4 or 5]:  ⟵ “French | 4 or 5 | 4 | FREN 201 | Language requirement [FLAN]”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4 or 5]:  ⟵ “German | 4 or 5 | 4 | GERM 201 | Language requirement [FLAN]”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4 or 5]:  ⟵ “Human Geography | 4 or 5 | 4 | ANTH 189 | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Italian Language & Culture | 4 or 5 | 4 | ITAL 201 | Language requirement [FLAN]”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Japanese Language & Culture | 4 or 5 | 4 | TR 189 | Language requirement [FLAN]”
  - equivalencies[AP-LATIN|4 or 5]:  ⟵ “Latin (Vergil or Literature) | 4 or 5 | 4 | LAT 201 | Language requirement [FLAN]”
  - equivalencies[AP-PSYCHOLOGY|4 or 5]:  ⟵ “Psychology | 4 or 5 | 4 | PSYC 101 | [BSS]”
  - equivalencies[AP-RESEARCH|4 or 5]:  ⟵ “Research | 4 or 5 | 4 | TR 189 | ”
  - equivalencies[AP-SEMINAR|4 or 5]:  ⟵ “Seminar | 4 or 5 | 4 | TR 189 | ”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Spanish (Language or Literature) | 4 or 5 | 4 | SPAN 201 | Language requirement [FLAN]”
  - equivalencies[AP-STATISTICS|4 or 5]:  ⟵ “Statistics | 4 or 5 | 4 | STAT 117 | [QUAN]Formerly (MATH 117 and STAT 207)”
### `f17152ccae3de91d` Essex County College — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.essex.edu/policies-academics/academic-standing/transfer-credit/ (sha256 b6afcb8b1ae1)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Courses transferred from other institution of higher learning must carry the grade of “C” or higher.”
### `241783db48a84d9b` Georgian Court University — academic_programs 2026-27 · program_key=clinical-laboratory-sciences-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/clinical-laboratory-sciences-bs/ (sha256 1a10533ff090)
- checks: {"courses": 21, "groups": 5, "groups_skipped": 0}
  - program_name: Clinical Laboratory Sciences, B.S. ⟵ “Clinical Laboratory Sciences, B.S. < Georgian Court University”
### `257061fba35feb79` Georgian Court University — academic_programs 2026-27 · program_key=marketing-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/marketing-bs/ (sha256 be885a50b64a)
- checks: {"courses": 31, "groups": 4, "groups_skipped": 0}
  - program_name: Marketing, B.S. ⟵ “Marketing, B.S. < Georgian Court University”
### `41f0608e31011b29` Georgian Court University — academic_programs 2026-27 · program_key=history-b-a [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/history-politics/history-ba/ (sha256 846bcbd3c13d)
- checks: {"courses": 4, "groups": 1, "groups_skipped": 0}
  - program_name: History, B.A. ⟵ “History, B.A. < Georgian Court University”
### `43cb2749bfe91eba` Georgian Court University — academic_programs 2026-27 · program_key=business-administration-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/business-administration-bs/ (sha256 fb47c1b738cf)
- checks: {"courses": 19, "groups": 2, "groups_skipped": 0}
  - program_name: Business Administration, B.S. ⟵ “Business Administration, B.S. < Georgian Court University”
### `4c12df0cf0949785` Georgian Court University — academic_programs 2026-27 · program_key=mathematics-b-a [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/mathematics-ba/ (sha256 b680b3919e26)
- checks: {"courses": 25, "groups": 4, "groups_skipped": 0}
  - program_name: Mathematics, B.A. ⟵ “Mathematics, B.A. < Georgian Court University”
### `4d8ff215f98ca82d` Georgian Court University — academic_programs 2026-27 · program_key=visual-art-b-a [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/art-visual-studies/visual-arts-bachelor-art/ (sha256 49dfcec1bfaf)
- checks: {"courses": 7, "groups": 4, "groups_skipped": 0}
  - program_name: Visual Art, B.A. ⟵ “Visual Art, B.A. < Georgian Court University”
### `5b5f8c422b8a81fd` Georgian Court University — academic_programs 2026-27 · program_key=chemistry-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/chem-bs/ (sha256 90f036344f5d)
- checks: {"courses": 17, "groups": 3, "groups_skipped": 0}
  - program_name: Chemistry, B.S. ⟵ “Chemistry, B.S. < Georgian Court University”
### `5c678c0910774951` Georgian Court University — academic_programs 2026-27 · program_key=psychiatric-rehabilitation-psychology-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/psychiatric-rehabilitation-psychology-bs/ (sha256 d86f4e80de74)
- checks: {"courses": 11, "groups": 1, "groups_skipped": 0}
  - program_name: Psychiatric Rehabilitation & Psychology, B.S. ⟵ “Psychiatric Rehabilitation & Psychology, B.S. < Georgian Court University”
### `5cfec509581cd8d0` Georgian Court University — academic_programs 2026-27 · program_key=finance-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/finance-bs/ (sha256 4decb6d8d5d8)
- checks: {"courses": 22, "groups": 2, "groups_skipped": 0}
  - program_name: Finance, B.S. ⟵ “Finance, B.S. < Georgian Court University”
### `7915cb625477622b` Georgian Court University — academic_programs 2026-27 · program_key=sport-management-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/sports-management-bs/ (sha256 0d380d137ae3)
- checks: {"courses": 30, "groups": 3, "groups_skipped": 0}
  - program_name: Sport Management, B.S. ⟵ “Sport Management, B.S. < Georgian Court University”
### `82e50d6d5e9d3f64` Georgian Court University — academic_programs 2026-27 · program_key=biology-b-a-including-medical-imaging-medical-lab-science [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-ba/ (sha256 9f71d74f98f9)
- checks: {"courses": 61, "groups": 7, "groups_skipped": 0}
  - program_name: Biology, B.A. (including Medical Imaging & Medical Lab Science) ⟵ “Biology, B.A. (including Medical Imaging & Medical Lab Science) < Georgian Court University”
### `8802551e92e8e33b` Georgian Court University — academic_programs 2026-27 · program_key=computer-science-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/computer-sci-bs/ (sha256 4f1c0ef1048e)
- checks: {"courses": 23, "groups": 4, "groups_skipped": 0}
  - program_name: Computer Science, B.S. ⟵ “Computer Science, B.S. < Georgian Court University”
### `8c2a50e1ad9017d8` Georgian Court University — academic_programs 2026-27 · program_key=interdisciplinary-studies-b-a [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/interdisciplinary-studies/ (sha256 d513dfc5f90d)
- checks: {"courses": 28, "groups": 1, "groups_skipped": 0}
  - program_name: Interdisciplinary Studies, B.A. ⟵ “Interdisciplinary Studies, B.A. < Georgian Court University”
### `a2a579001d43d4af` Georgian Court University — academic_programs 2026-27 · program_key=accounting-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/accounting-bs/ (sha256 0e516917634a)
- checks: {"courses": 26, "groups": 2, "groups_skipped": 0}
  - program_name: Accounting, B.S. ⟵ “Accounting, B.S. < Georgian Court University”
### `af5c6d08dcf6522a` Georgian Court University — academic_programs 2026-27 · program_key=english-b-a [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
- checks: {"courses": 51, "groups": 13, "groups_skipped": 0}
  - program_name: English, B.A. ⟵ “English, B.A. < Georgian Court University”
### `c012c2072b2a7c66` Georgian Court University — academic_programs 2026-27 · program_key=biochemistry-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biochem-bs/ (sha256 92769992962a)
- checks: {"courses": 23, "groups": 3, "groups_skipped": 0}
  - program_name: Biochemistry, B.S. ⟵ “Biochemistry, B.S. < Georgian Court University”
### `c27e80cf05f27e88` Georgian Court University — academic_programs 2026-27 · program_key=graphic-design-b-a [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/graphic-design-ba/ (sha256 82b2dc58eee0)
- checks: {"courses": 19, "groups": 2, "groups_skipped": 0}
  - program_name: Graphic Design, B.A. ⟵ “Graphic Design, B.A. < Georgian Court University”
### `cf409407a1ca238b` Georgian Court University — academic_programs 2026-27 · program_key=psychology-b-a [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/psychology-ba/ (sha256 990ae5b4921e)
- checks: {"courses": 40, "groups": 5, "groups_skipped": 0}
  - program_name: Psychology, B.A. ⟵ “Psychology, B.A. < Georgian Court University”
### `dc77734214b8e7e8` Georgian Court University — academic_programs 2026-27 · program_key=health-information-management-b-s [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/health-info-mgt-bs/ (sha256 00cc80d8eac4)
- checks: {"courses": 4, "groups": 1, "groups_skipped": 0}
  - program_name: Health Information Management, B.S. ⟵ “Health Information Management, B.S. < Georgian Court University”
### `dcdc0e96253836c7` Georgian Court University — academic_programs 2026-27 · program_key=biology-b-s-including-medical-lab-sci [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-bs/ (sha256 fc37529f9743)
- checks: {"courses": 34, "groups": 5, "groups_skipped": 0}
  - program_name: Biology, B.S. (including Medical Lab Sci) ⟵ “Biology, B.S. (including Medical Lab Sci) < Georgian Court University”
### `de9cea3b6eecc961` Georgian Court University — academic_programs 2026-27 · program_key=computer-information-systems-b-a [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/computer-information-systems-ba/ (sha256 a0e46c134bc5)
- checks: {"courses": 14, "groups": 1, "groups_skipped": 0}
  - program_name: Computer Information Systems, B.A. ⟵ “Computer Information Systems, B.A. < Georgian Court University”
### `51ccf872d30cd3a6` Georgian Court University — awards 2026-27 [new] (source_unlabeled)
- source: https://georgian.edu/financial-aid/scholarships/ (sha256 975e01fc441d)
- checks: {"thresholds": {"gpa_min": 2.0}}
  - award_amount_text: $10,000 ⟵ “GCU Award | $10,000 | 2.0 or above”
  - gpa_requirement: 2.0 or above ⟵ “GCU Award | $10,000 | 2.0 or above”
  - renewal_requirements: 2.0 or above ⟵ “GCU Award | $10,000 | 2.0 or above”
### `5771e655987d14b8` Georgian Court University — awards 2026-27 [new] (source_unlabeled)
- source: https://georgian.edu/financial-aid/scholarships/ (sha256 975e01fc441d)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $18,000 ⟵ “Presidential Scholarship | $18,000 | 2.5 or above”
  - gpa_requirement: 2.5 or above ⟵ “Presidential Scholarship | $18,000 | 2.5 or above”
  - renewal_requirements: 2.5 or above ⟵ “Presidential Scholarship | $18,000 | 2.5 or above”
### `73ecbfdd0d276f2c` Georgian Court University — awards 2026-27 [new] (source_unlabeled)
- source: https://georgian.edu/financial-aid/scholarships/ (sha256 975e01fc441d)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Honors Scholarship | $2,500 | -”
### `7bfddf4a4829d075` Georgian Court University — awards 2026-27 [new] (source_unlabeled)
- source: https://georgian.edu/financial-aid/scholarships/ (sha256 975e01fc441d)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $19,000 ⟵ “Trustee Scholarship | $19,000 | 2.5 or above”
  - gpa_requirement: 2.5 or above ⟵ “Trustee Scholarship | $19,000 | 2.5 or above”
  - renewal_requirements: 2.5 or above ⟵ “Trustee Scholarship | $19,000 | 2.5 or above”
### `c04346717ff33dba` Georgian Court University — awards 2026-27 [new] (source_unlabeled)
- source: https://georgian.edu/financial-aid/scholarships/ (sha256 975e01fc441d)
- checks: {"thresholds": {"gpa_min": 2.0}}
  - award_amount_text: $14,000 ⟵ “McAuley Scholarship | $14,000 | 2.0 or above”
  - gpa_requirement: 2.0 or above ⟵ “McAuley Scholarship | $14,000 | 2.0 or above”
  - renewal_requirements: 2.0 or above ⟵ “McAuley Scholarship | $14,000 | 2.0 or above”
### `ca790c0b920a5edc` Georgian Court University — awards 2026-27 [new] (source_unlabeled)
- source: https://georgian.edu/financial-aid/scholarships/ (sha256 975e01fc441d)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $17,000 ⟵ “Dean's Scholarship | $17,000 | 2.5 or above”
  - gpa_requirement: 2.5 or above ⟵ “Dean's Scholarship | $17,000 | 2.5 or above”
  - renewal_requirements: 2.5 or above ⟵ “Dean's Scholarship | $17,000 | 2.5 or above”
### `01ff92094c3c1f0a` Georgian Court University — degree_requirements 2026-27 · program_key=clinical-laboratory-sciences-b-s · requirement_key=requirements-mathematics [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/clinical-laboratory-sciences-bs/ (sha256 1a10533ff090)
  - courses: MA 110 ⟵ “MA 110 - Precalculus”
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
### `053d38b0a58b9bb3` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=major-sequence-english-electives [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - section: major-sequence-english-electives ⟵ “Major Sequence — English Electives”
### `063c5aa291becb76` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=major-sequence-american-literature [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: EN 310 ⟵ “EN 310 - American Drama”
  - courses: EN 321 ⟵ “EN 321 - American Renaissance”
  - courses: EN 322 ⟵ “EN 322 - American Realism”
  - courses: EN 323 ⟵ “EN 323 - Modern American Literature”
  - courses: EN 324 ⟵ “EN 324 - Contemporary American Literature”
  - courses: EN 327 ⟵ “EN 327 - Make It New: Modern American Poetry”
### `0a3857b59332903f` Georgian Court University — degree_requirements 2026-27 · program_key=biochemistry-b-s · requirement_key=major-sequence-strongly-recommended-additional-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biochem-bs/ (sha256 92769992962a)
  - courses: CH 334 ⟵ “CH 334 - Inorganic Chemistry”
  - courses: CH 402 ⟵ “CH 402 - Instrumental Analysis”
### `0bf45f8fd788f465` Georgian Court University — degree_requirements 2026-27 · program_key=finance-b-s · requirement_key=major-sequence-required-finance-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/finance-bs/ (sha256 4decb6d8d5d8)
  - courses: EC 481 ⟵ “EC 481 - Comparative Economic Systems”
  - courses: FIN 335 ⟵ “FIN 335 - Financial Management I”
  - courses: FIN 339 ⟵ “FIN 339 - Introduction to Financial Technology”
  - courses: FIN 382 ⟵ “FIN 382 - International Finance & Economics”
  - courses: FIN 434 ⟵ “FIN 434 - Investment Analysis”
  - courses: FIN 482 ⟵ “FIN 482 - Financial Market & Institutions”
### `0f02a78b50835528` Georgian Court University — degree_requirements 2026-27 · program_key=graphic-design-b-a · requirement_key=graphic-design-b-a-graphic-design-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/graphic-design-ba/ (sha256 82b2dc58eee0)
  - courses: GD 111 ⟵ “GD 111 - Introduction to Design”
  - courses: GD 112 ⟵ “GD 112 - Drawing for Designers”
  - courses: GD 113 ⟵ “GD 113 - Computer Graphics”
  - courses: GD 114 ⟵ “GD 114 - Graphic Design I”
  - courses: GD 212 ⟵ “GD 212 - Intro to Design Thinking”
  - courses: GD 213 ⟵ “GD 213 - Typography I”
  - courses: GD 214 ⟵ “GD 214 - Graphic Design II”
  - courses: GD 220 ⟵ “GD 220 - Visual Principles & Strategy”
  - courses: GD 226 ⟵ “GD 226 - Video & Sound Editing”
  - courses: GD 230 ⟵ “GD 230 - Brand Identity Systems”
  - courses: GD 322 ⟵ “GD 322 - Web Design”
  - courses: GD 324 ⟵ “GD 324 - Typography II”
  - courses: GD 327 ⟵ “GD 327 - Motion Graphics”
  - courses: GD 328 ⟵ “GD 328 - Design Thinking & Innovation”
  - courses: GD 422 ⟵ “GD 422 - Creative Web & Interaction Design”
  - courses: GD 429 ⟵ “GD 429 - Internship”
  - courses: GD 430 ⟵ “GD 430 - Professional Practices”
  - courses: GD 440 ⟵ “GD 440 - Special Topics”
### `10ad72b8bcf245f1` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=major-sequence-required-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: EN 300 ⟵ “EN 300 - Gateways to Literary Study”
### `144316007e5fad0f` Georgian Court University — degree_requirements 2026-27 · program_key=mathematics-b-a · requirement_key=b-a-in-mathematics-with-data-science-concentration-mathematics-core-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/mathematics-ba/ (sha256 b680b3919e26)
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
  - courses: MA 209 ⟵ “MA 209 - Linear Algebra”
  - courses: MA 210 ⟵ “MA 210 - Discrete Mathematics”
  - courses: MA 215 ⟵ “MA 215 - Calculus III”
  - courses: MA 331 ⟵ “MA 331 - Probability & Statistics I”
### `1968c5346645ae16` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=major-sequence-multi-ethnic-literature [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: EN 370 ⟵ “EN 370 - AsianAmericanLit”
  - courses: EN 375 ⟵ “EN 375 - USMultiEthnicLit”
  - courses: EN 376 ⟵ “EN 376 - NativeAmLit&Crit”
  - courses: EN 380 ⟵ “EN 380 - African Diaspora”
### `1e5affed1e3c54d7` Georgian Court University — degree_requirements 2026-27 · program_key=chemistry-b-s · requirement_key=major-sequence-strongly-recommended [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/chem-bs/ (sha256 90f036344f5d)
  - courses: MA 215 ⟵ “MA 215 - Calculus III”
### `2bef5abd43b501fe` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-s-including-medical-lab-sci · requirement_key=requirements-for-medical-laboratory-science-track [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-bs/ (sha256 fc37529f9743)
  - courses: BI 121 ⟵ “BI 121 - Cellular Organiz., Energetics & Function”
  - courses: BI 201 ⟵ “BI 201 - Biological Literature”
  - courses: BI 204 ⟵ “BI 204 - Genetics & Evolution”
  - courses: BI 213 ⟵ “BI 213 - Human Anatomy & Physiology I”
  - courses: BI 214 ⟵ “BI 214 - Human Anatomy & Physiology II”
  - courses: BI 219 ⟵ “BI 219 - Microbiology”
  - courses: BI 401 ⟵ “BI 401 - Medical Technology Internship I”
  - courses: BI 402 ⟵ “BI 402 - Medical Technology Internship II”
  - courses: BI 427 ⟵ “BI 427 - Immunology (4 credits)”
  - courses: BI 428 ⟵ “BI 428 - Fundamentals of Immunology (3 credits)”
  - courses: BI 437 ⟵ “BI 437 - Biochemistry I”
  - courses: BI 444 ⟵ “BI 444 - Capstone in Biology: BS”
### `386b486476c03cba` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=major-sequence-british-literature-from-the-nineteenth-century-to-the-present [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: EN 318 ⟵ “EN 318 - Romantic Literature”
  - courses: EN 319 ⟵ “EN 319 - Victorian Literature”
  - courses: EN 325 ⟵ “EN 325 - Modern Irish/British Literature”
  - courses: EN 326 ⟵ “EN 326 - Contemporary Irish/British Literature”
### `39b3f5b06dab7343` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=digital-humanities-concentration-additional-english-elective [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - section: digital-humanities-concentration-additional-english-elective ⟵ “Digital Humanities Concentration — Additional English Elective”
### `410d0c2de77254c6` Georgian Court University — degree_requirements 2026-27 · program_key=marketing-b-s · requirement_key=major-sequence-elective-marketing-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/marketing-bs/ (sha256 be885a50b64a)
  - courses: BU 321 ⟵ “BU 321 - Electronic Commerce”
  - courses: CM 309 ⟵ “CM 309 - Public Relations Writing”
  - courses: MK 266 ⟵ “MK 266 - Going Viral & Growth Hacking”
  - courses: MK 342 ⟵ “MK 342 - Principles of Advertising & PR”
  - courses: MK 343 ⟵ “MK 343 - Sales & Sales Management”
  - courses: MK 356 ⟵ “MK 356 - Lifecycle & Email Marketing”
  - courses: MK 446 ⟵ “MK 446 - Digital Mktg Analytics & Experimentation”
  - courses: SM 241 ⟵ “SM 241 - Sport Marketing”
### `411e24f1172f51d4` Georgian Court University — degree_requirements 2026-27 · program_key=psychology-b-a · requirement_key=concentration-in-forensic-psychology-required-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/psychology-ba/ (sha256 990ae5b4921e)
  - courses: PS 320 ⟵ “PS 320 - Forensic Psychology”
  - courses: PS 321 ⟵ “PS 321 - Criminal Profiling”
  - courses: CJ 167 ⟵ “CJ 167 - Race, Ethnicity & Criminal Justice”
  - courses: CJ 231 ⟵ “CJ 231 - Juvenile Justice”
  - courses: CJ 320 ⟵ “CJ 320 - Mental Health, Neurodiver. & Crim. Just.”
  - courses: CJ 325 ⟵ “CJ 325 - Gender & Crime”
  - courses: CJ 401 ⟵ “CJ 401 - Sex Crimes”
### `423ed3a4f6b82881` Georgian Court University — degree_requirements 2026-27 · program_key=computer-science-b-s · requirement_key=major-sequence-cs-ma232 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/computer-sci-bs/ (sha256 4f1c0ef1048e)
  - courses: CS 306 ⟵ “CS 306 - Topics in CS or CIS”
### `4cb2e26883ecdd56` Georgian Court University — degree_requirements 2026-27 · program_key=clinical-laboratory-sciences-b-s · requirement_key=requirements [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/clinical-laboratory-sciences-bs/ (sha256 1a10533ff090)
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
  - courses: PH 121 ⟵ “PH 121 - University Physics I”
  - courses: PH 122 ⟵ “PH 122 - University Physics II”
### `563a753d0152a8fa` Georgian Court University — degree_requirements 2026-27 · program_key=interdisciplinary-studies-b-a · requirement_key=major-sequence [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/interdisciplinary-studies/ (sha256 d513dfc5f90d)
  - courses: AN 244 ⟵ “AN 244 - City, Suburb, & Society”
  - courses: AN 312 ⟵ “AN 312 - Native Cultures of North America”
  - courses: CJ 200 ⟵ “CJ 200 - Theories of Crime”
  - courses: CJ 210 ⟵ “CJ 210 - Introduction to Law Enforcement”
  - courses: EN 310 ⟵ “EN 310 - American Drama”
  - courses: EN 321 ⟵ “EN 321 - American Renaissance”
  - courses: EN 322 ⟵ “EN 322 - American Realism”
  - courses: EN 323 ⟵ “EN 323 - Modern American Literature”
  - courses: EN 324 ⟵ “EN 324 - Contemporary American Literature”
  - courses: EN 327 ⟵ “EN 327 - Make It New: Modern American Poetry”
  - courses: EN 370 ⟵ “EN 370 - AsianAmericanLit”
  - courses: EN 375 ⟵ “EN 375 - USMultiEthnicLit”
  - courses: EN 376 ⟵ “EN 376 - NativeAmLit&Crit”
  - courses: EN 380 ⟵ “EN 380 - African Diaspora”
  - courses: HST 304 ⟵ “HST 304 - American Revolution & Aftermath”
  - courses: HST 308 ⟵ “HST 308 - Civil War & Reconstruction”
  - courses: HST 312 ⟵ “HST 312 - U.S. Politics & Society, 1890-1945”
  - courses: HST 316 ⟵ “HST 316 - America Since 1945”
  - courses: HST 320 ⟵ “HST 320 - Rebels & Radicals in U.S. History”
  - courses: HST 330 ⟵ “HST 330 - America & the World Since 1898”
  - courses: HST 331 ⟵ “HST 331 - Vietnam & America”
  - courses: IDS 250 ⟵ “IDS 250 - Introduction to African American Studies”
  - courses: IH 345 ⟵ “IH 345 - Native American Medicine”
  - courses: MU 214 ⟵ “MU 214 - Music of the Americas”
  - courses: PO 211 ⟵ “PO 211 - American National Government”
  - … 3 more rows
### `577abe7038bb8255` Georgian Court University — degree_requirements 2026-27 · program_key=health-information-management-b-s · requirement_key=major-sequence [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/health-info-mgt-bs/ (sha256 00cc80d8eac4)
  - courses: BI 213 ⟵ “BI 213 - Human Anatomy & Physiology I”
  - courses: BI 214 ⟵ “BI 214 - Human Anatomy & Physiology II”
  - courses: MA 103 ⟵ “MA 103 - Introduction to Statistical Thinking”
  - courses: MA 109 ⟵ “MA 109 - College Algebra”
### `606e92f28f784948` Georgian Court University — degree_requirements 2026-27 · program_key=psychology-b-a · requirement_key=psychology-scholars-program [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/psychology-ba/ (sha256 990ae5b4921e)
  - courses: PS 113 ⟵ “PS 113 - Foundations of Psychology”
  - courses: PS 223 ⟵ “PS 223 - Psychopathology”
  - courses: PS 332 ⟵ “PS 332 - Psychology of Learning”
  - courses: PS 360 ⟵ “PS 360 - Cognitive Psychology”
  - courses: PS 334 ⟵ “PS 334 - Social Psychology”
  - courses: PS 341 ⟵ “PS 341 - Biological Psychology”
  - courses: PS 430 ⟵ “PS 430 - Rsrch Mthds & Stats for the Beh Sciences”
  - courses: PS 431 ⟵ “PS 431 - Experimental Psychology”
### `6109a886db4ab655` Georgian Court University — degree_requirements 2026-27 · program_key=sport-management-b-s · requirement_key=major-sequence-elective-sport-management-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/sports-management-bs/ (sha256 0d380d137ae3)
  - courses: ES 211 ⟵ “ES 211 - Theory of Coaching”
  - courses: ES 310 ⟵ “ES 310 - Sport & Exercise Psychology”
  - courses: ES 315 ⟵ “ES 315 - Sports in Society”
  - courses: ES 325 ⟵ “ES 325 - Wellness Program Management”
  - courses: ES 326 ⟵ “ES 326 - Wellness Program Practices”
  - courses: ES 360 ⟵ “ES 360 - Administrative Aspects of Sport”
  - courses: MK 246 ⟵ “MK 246 - Social Media Marketing”
  - courses: SM 215 ⟵ “SM 215 - Introduction to Esports”
  - courses: SM 416 ⟵ “SM 416 - Research in Sport”
  - courses: SM 417 ⟵ “SM 417 - Special Events Management”
  - courses: SM 451 ⟵ “SM 451 - Sport Management Internship”
### `66319efdcac3af2e` Georgian Court University — degree_requirements 2026-27 · program_key=history-b-a · requirement_key=major-sequence [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/history-politics/history-ba/ (sha256 846bcbd3c13d)
  - courses: HST 110 ⟵ “HST 110 - US History Survey to 1877”
  - courses: HST 111 ⟵ “HST 111 - US History Survey since 1877”
  - courses: HST 120 ⟵ “HST 120 - World History Survey to 1500”
  - courses: HST 121 ⟵ “HST 121 - World History Survey since 1500”
### `73d419d13e0552e5` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=writing-concentration-required-other-courses-substitute-for-english-electives [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: EN 207 ⟵ “EN 207 - News Writing & Reporting”
  - courses: EN 208 ⟵ “EN 208 - News Editing”
  - courses: EN 210 ⟵ “EN 210 - Writing for the Mass Media”
  - courses: EN 215 ⟵ “EN 215 - Creative Writing”
  - courses: EN 221 ⟵ “EN 221 - HNRS: Rhetoric, Research & Digital Lit”
  - courses: EN 225 ⟵ “EN 225 - Topics in Writing”
  - courses: EN 230 ⟵ “EN 230 - Writing on the Web”
  - courses: EN 245 ⟵ “EN 245 - Writing About Television”
  - courses: EN 250 ⟵ “EN 250 - The Power of Grammar”
  - courses: EN 309 ⟵ “EN 309 - Public Relations Writing”
  - courses: EN 416 ⟵ “EN 416 - HistoryStructureofEnglish”
### `76e4edca18efb998` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=writing-concentration-additional-english-elective [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - section: writing-concentration-additional-english-elective ⟵ “Writing Concentration — Additional English Elective”
### `7c41fd6214dcf0d2` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=major-sequence-senior-seminar [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: EN 429 ⟵ “EN 429 - Bookends: A Global Literature Seminar”
  - courses: EN 430 ⟵ “EN 430 - Senior Seminar II”
### `7e9c86e8f13ab950` Georgian Court University — degree_requirements 2026-27 · program_key=psychology-b-a · requirement_key=addictions-counseling-recommended-course-sequence [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/psychology-ba/ (sha256 990ae5b4921e)
  - courses: PS 270 ⟵ “PS 270 - Theories of Personality”
  - courses: PS 281 ⟵ “PS 281 - Introduction to Addictions & Recovery”
  - courses: PS 282 ⟵ “PS 282 - Foundations of Addictions Treatment”
  - courses: PS 331 ⟵ “PS 331 - Basic Counseling”
  - courses: PS 380 ⟵ “PS 380 - Prof Issues of Addiction Counseling”
  - courses: PS 456 ⟵ “PS 456 - Internship in Psych:Addictions Treatment”
### `8281bcbc7fea70df` Georgian Court University — degree_requirements 2026-27 · program_key=computer-information-systems-b-a · requirement_key=major-sequence [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/computer-information-systems-ba/ (sha256 a0e46c134bc5)
  - courses: CS 123 ⟵ “CS 123 - Computer Programming I”
  - courses: CS 126 ⟵ “CS 126 - Computer Programming II”
  - courses: CS 220 ⟵ “CS 220 - Python Programming”
  - courses: CS 227 ⟵ “CS 227 - Data Structures”
  - courses: CS 231 ⟵ “CS 231 - Introduction to Database Systems”
  - courses: CS 450 ⟵ “CS 450 - Applications Project”
  - courses: IS 224 ⟵ “IS 224 - Introduction to Business Analytics”
  - courses: IS 320 ⟵ “IS 320 - Management Information Systems”
  - courses: CS 212 ⟵ “CS 212 - Data Analytics for Business”
  - courses: CS 225 ⟵ “CS 225 - Computer Architecture”
  - courses: CS 306 ⟵ “CS 306 - Topics in CS or CIS”
  - courses: CS 326 ⟵ “CS 326 - Survey of Networks & Telecommunications”
  - courses: CS 327 ⟵ “CS 327 - Computer Network Administration”
  - courses: IS 122 ⟵ “IS 122 - Introduction to Cybersecurity”
### `85b5015e7459b3b8` Georgian Court University — degree_requirements 2026-27 · program_key=visual-art-b-a · requirement_key=major-sequences-studio-art-electives [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/art-visual-studies/visual-arts-bachelor-art/ (sha256 49dfcec1bfaf)
  - section: major-sequences-studio-art-electives ⟵ “Major Sequences — Studio Art Electives”
### `89bff385e333dff2` Georgian Court University — degree_requirements 2026-27 · program_key=clinical-laboratory-sciences-b-s · requirement_key=requirements-chemistry [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/clinical-laboratory-sciences-bs/ (sha256 1a10533ff090)
  - courses: CH 113 ⟵ “CH 113 - General Chemistry I”
  - courses: CH 114 ⟵ “CH 114 - General Chemistry II”
  - courses: CH 223 ⟵ “CH 223 - Organic Chemistry I”
  - courses: CH 224 ⟵ “CH 224 - Organic Chemistry II”
### `8ae33122cff0242d` Georgian Court University — degree_requirements 2026-27 · program_key=visual-art-b-a · requirement_key=major-sequences-visual-art [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/art-visual-studies/visual-arts-bachelor-art/ (sha256 49dfcec1bfaf)
  - courses: AR 111 ⟵ “AR 111 - Drawing I”
  - courses: AR 113 ⟵ “AR 113 - Visual Thinking & Design”
  - courses: AR 201 ⟵ “AR 201 - Drawing II”
  - courses: AR 220 ⟵ “AR 220 - Modern Art”
  - courses: AR 228 ⟵ “AR 228 - European & U.S. Art”
  - courses: AR 229 ⟵ “AR 229 - World Art History”
### `8cd90d2a09f43c48` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-a-including-medical-imaging-medical-lab-science · requirement_key=requirements-for-mci-medical-imaging-track-for-students-who-will-take-sonography [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-ba/ (sha256 9f71d74f98f9)
  - courses: BI 121 ⟵ “BI 121 - Cellular Organiz., Energetics & Function”
  - courses: BI 204 ⟵ “BI 204 - Genetics & Evolution”
  - courses: BI 213 ⟵ “BI 213 - Human Anatomy & Physiology I”
  - courses: BI 214 ⟵ “BI 214 - Human Anatomy & Physiology II”
  - courses: BI 431 ⟵ “BI 431 - Clinical Sonography Internship I”
  - courses: BI 432 ⟵ “BI 432 - Clinical Sonography Internship II”
  - courses: BI 433 ⟵ “BI 433 - Clinical Sonography Internship III”
### `9e21a3fdd778c165` Georgian Court University — degree_requirements 2026-27 · program_key=biochemistry-b-s · requirement_key=major-sequence-related-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biochem-bs/ (sha256 92769992962a)
  - courses: BI 121 ⟵ “BI 121 - Cellular Organiz., Energetics & Function”
  - courses: BI 204 ⟵ “BI 204 - Genetics & Evolution”
  - courses: BI 219 ⟵ “BI 219 - Microbiology”
  - courses: BI 320 ⟵ “BI 320 - Cell Biology”
  - courses: BI 422 ⟵ “BI 422 - Advanced Molecular Genetics”
  - courses: PH 121 ⟵ “PH 121 - University Physics I”
  - courses: PH 122 ⟵ “PH 122 - University Physics II”
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
### `a5684e23287f2ea1` Georgian Court University — degree_requirements 2026-27 · program_key=chemistry-b-s · requirement_key=major-sequence-related-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/chem-bs/ (sha256 90f036344f5d)
  - courses: PH 121 ⟵ “PH 121 - University Physics I”
  - courses: PH 122 ⟵ “PH 122 - University Physics II”
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
### `b08f8635eff69bb6` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=digital-humanities-concentration-required-courses-10-credits-see-note-for-en430- [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: CM 205 ⟵ “CM 205 - Transmedia Storytelling”
  - courses: EN 210 ⟵ “EN 210 - Writing for the Mass Media”
  - courses: EN 225 ⟵ “EN 225 - Topics in Writing”
  - courses: EN 405 ⟵ “EN 405 - Internship”
  - courses: EN 420 ⟵ “EN 420 - Special Studies”
  - courses: EN 430 ⟵ “EN 430 - Senior Seminar II (credit counted above in English major requirements section)”
  - courses: EN 421 ⟵ “EN 421 - Independent Project”
### `b38fa289437772ea` Georgian Court University — degree_requirements 2026-27 · program_key=accounting-b-s · requirement_key=major-sequence-business-core-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/accounting-bs/ (sha256 0e516917634a)
  - courses: AC 171 ⟵ “AC 171 - Principles of Financial Accounting”
  - courses: AC 172 ⟵ “AC 172 - Principles of Managerial Accounting”
  - courses: EC 181 ⟵ “EC 181 - Principles of Macroeconomics”
  - courses: EC 182 ⟵ “EC 182 - Principles of Microeconomics”
  - courses: BU 121 ⟵ “BU 121 - Quantitative Business Concepts”
  - courses: CAR 200 ⟵ “CAR 200 - Internship Prep & Career Development”
  - courses: BU 211 ⟵ “BU 211 - Business Law”
  - courses: BU 213 ⟵ “BU 213 - Mgmt Theory & Org. Behavior”
  - courses: BU 221 ⟵ “BU 221 - Business Statistics & Probability”
  - courses: IS 224 ⟵ “IS 224 - Introduction to Business Analytics”
  - courses: FIN 235 ⟵ “FIN 235 - Introduction to Finance”
  - courses: MK 241 ⟵ “MK 241 - Principles of Marketing”
  - courses: BU 351 ⟵ “BU 351 - Internship”
  - courses: BU 491 ⟵ “BU 491 - Business Strategies & Policy”
### `ba431e1bfb913f88` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=writing-concentration [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: CAR 465 ⟵ “CAR 465 - NonCredit Internship”
  - courses: EN 299 ⟵ “EN 299 - Practicum”
  - courses: EN 405 ⟵ “EN 405 - Internship”
  - courses: EN 421 ⟵ “EN 421 - Independent Project”
### `c342e95cf17eefc7` Georgian Court University — degree_requirements 2026-27 · program_key=clinical-laboratory-sciences-b-s · requirement_key=requirements-biology [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/clinical-laboratory-sciences-bs/ (sha256 1a10533ff090)
  - courses: BI 121 ⟵ “BI 121 - Cellular Organiz., Energetics & Function”
  - courses: BI 204 ⟵ “BI 204 - Genetics & Evolution”
  - courses: BI 213 ⟵ “BI 213 - Human Anatomy & Physiology I”
  - courses: BI 214 ⟵ “BI 214 - Human Anatomy & Physiology II”
  - courses: BI 219 ⟵ “BI 219 - Microbiology”
  - courses: BI 427 ⟵ “BI 427 - Immunology (4 credits)”
  - courses: BI 428 ⟵ “BI 428 - Fundamentals of Immunology (3 credits)”
  - courses: BI 437 ⟵ “BI 437 - Biochemistry I”
### `c516dbac73ccabec` Georgian Court University — degree_requirements 2026-27 · program_key=mathematics-b-a · requirement_key=b-a-in-mathematics-mathematics-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/mathematics-ba/ (sha256 b680b3919e26)
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
  - courses: MA 209 ⟵ “MA 209 - Linear Algebra”
  - courses: MA 210 ⟵ “MA 210 - Discrete Mathematics”
  - courses: MA 215 ⟵ “MA 215 - Calculus III”
  - courses: MA 311 ⟵ “MA 311 - Introduction to Abstract Algebra I”
  - courses: MA 312 ⟵ “MA 312 - Introduction to Abstract Algebra II”
  - courses: MA 401 ⟵ “MA 401 - Introduction to Analysis”
  - courses: MA 216 ⟵ “MA 216 - Vector Calculus”
  - courses: MA 331 ⟵ “MA 331 - Probability & Statistics I”
### `cb44ec3c95799934` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-s-including-medical-lab-sci · requirement_key=course-requirements-except-for-medical-laboratory-science-track-biology-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-bs/ (sha256 fc37529f9743)
  - courses: BI 120 ⟵ “BI 120 - Biological Diversity & Phylogeny”
  - courses: BI 121 ⟵ “BI 121 - Cellular Organiz., Energetics & Function”
  - courses: BI 201 ⟵ “BI 201 - Biological Literature”
  - courses: BI 204 ⟵ “BI 204 - Genetics & Evolution”
  - courses: BI 305 ⟵ “BI 305 - Biological Interactions: Ecology (4 credits)”
  - courses: BI 310 ⟵ “BI 310 - Ecology & Health (3 credits)”
  - courses: BI 444 ⟵ “BI 444 - Capstone in Biology: BS”
### `cf3579b33be3faa4` Georgian Court University — degree_requirements 2026-27 · program_key=computer-science-b-s · requirement_key=major-sequence-cs-ma325 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/computer-sci-bs/ (sha256 4f1c0ef1048e)
  - courses: CS 326 ⟵ “CS 326 - Survey of Networks & Telecommunications”
  - courses: CS 327 ⟵ “CS 327 - Computer Network Administration”
  - courses: CS 328 ⟵ “CS 328 - Big Data”
  - courses: CS 329 ⟵ “CS 329 - Artificial Intelligence”
### `d2056db6632f70e4` Georgian Court University — degree_requirements 2026-27 · program_key=marketing-b-s · requirement_key=major-sequence-marketing-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/marketing-bs/ (sha256 be885a50b64a)
  - courses: MK 246 ⟵ “MK 246 - Social Media Marketing”
  - courses: MK 341 ⟵ “MK 341 - Consumer Behavior”
  - courses: MK 442 ⟵ “MK 442 - Marketing Research”
### `d31bbf75c548bbcf` Georgian Court University — degree_requirements 2026-27 · program_key=biochemistry-b-s · requirement_key=major-sequence-biochemistry-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biochem-bs/ (sha256 92769992962a)
  - courses: CH 113 ⟵ “CH 113 - General Chemistry I”
  - courses: CH 114 ⟵ “CH 114 - General Chemistry II”
  - courses: CH 223 ⟵ “CH 223 - Organic Chemistry I”
  - courses: CH 224 ⟵ “CH 224 - Organic Chemistry II”
  - courses: CH 241 ⟵ “CH 241 - Quant. Analysis”
  - courses: CH 304 ⟵ “CH 304 - Chemical Literature”
  - courses: CH 311 ⟵ “CH 311 - Biochemistry I”
  - courses: CH 312 ⟵ “CH 312 - Biochemistry II”
  - courses: CH 331 ⟵ “CH 331 - Quantum Chemistry”
  - courses: CH 332 ⟵ “CH 332 - Reaction Dynamics”
  - courses: CH 416 ⟵ “CH 416 - Topics in Chemistry/Biochemistry”
  - courses: CH 420 ⟵ “CH 420 - Chemistry/Biochemistry Seminar”
### `d3a08a7ccb109cd6` Georgian Court University — degree_requirements 2026-27 · program_key=marketing-b-s · requirement_key=optional-concentration-in-digital-marketing [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/marketing-bs/ (sha256 be885a50b64a)
  - courses: MK 100 ⟵ “MK 100 - Career Exploration in Digital Marketing”
  - courses: MK 266 ⟵ “MK 266 - Going Viral & Growth Hacking”
  - courses: MK 356 ⟵ “MK 356 - Lifecycle & Email Marketing”
  - courses: MK 446 ⟵ “MK 446 - Digital Mktg Analytics & Experimentation”
### `d74f8c29c9d1865f` Georgian Court University — degree_requirements 2026-27 · program_key=clinical-laboratory-sciences-b-s · requirement_key=requirements-statistics [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/clinical-laboratory-sciences-bs/ (sha256 1a10533ff090)
  - courses: MA 103 ⟵ “MA 103 - Introduction to Statistical Thinking”
  - courses: SO 201 ⟵ “SO 201 - Social and Crime Statistics”
### `d900e8545ce67aaa` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=major-sequence [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: EN 250 ⟵ “EN 250 - The Power of Grammar”
  - courses: EN 260 ⟵ “EN 260 - Exploring Children's Literature”
  - courses: EN 264 ⟵ “EN 264 - Journeys in Young Adult Literature”
  - courses: EN 416 ⟵ “EN 416 - HistoryStructureofEnglish (when offered)”
### `e21e05617de6fe22` Georgian Court University — degree_requirements 2026-27 · program_key=english-b-a · requirement_key=major-sequence-british-literature-before-the-nineteenth-century [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/english-ba/ (sha256 96fade3f977a)
  - courses: EN 301 ⟵ “EN 301 - Shakespeare I: Of Kings & Lovers”
  - courses: EN 302 ⟵ “EN 302 - Shakespeare II: Deception & Betrayal”
  - courses: EN 312 ⟵ “EN 312 - Heroes, Myths, & Monsters”
  - courses: EN 313 ⟵ “EN 313 - Medieval Literature”
  - courses: EN 314 ⟵ “EN 314 - Chaucer: Bawds & Churls”
  - courses: EN 315 ⟵ “EN 315 - Shakespeare Theater Violence & Obsession”
  - courses: EN 316 ⟵ “EN 316 - Seventeenth Century Literature”
  - courses: EN 317 ⟵ “EN 317 - Eighteenth Century Literature”
### `e76ee1aab96a07bf` Georgian Court University — degree_requirements 2026-27 · program_key=mathematics-b-a · requirement_key=b-a-in-mathematics-related-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/mathematics-ba/ (sha256 b680b3919e26)
  - courses: CS 123 ⟵ “CS 123 - Computer Programming I”
### `f08d80c7a9b2d481` Georgian Court University — degree_requirements 2026-27 · program_key=chemistry-b-s · requirement_key=major-sequence-chemistry-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/chem-bs/ (sha256 90f036344f5d)
  - courses: CH 113 ⟵ “CH 113 - General Chemistry I”
  - courses: CH 114 ⟵ “CH 114 - General Chemistry II”
  - courses: CH 223 ⟵ “CH 223 - Organic Chemistry I”
  - courses: CH 224 ⟵ “CH 224 - Organic Chemistry II”
  - courses: CH 241 ⟵ “CH 241 - Quant. Analysis”
  - courses: CH 304 ⟵ “CH 304 - Chemical Literature”
  - courses: CH 331 ⟵ “CH 331 - Quantum Chemistry”
  - courses: CH 332 ⟵ “CH 332 - Reaction Dynamics”
  - courses: CH 334 ⟵ “CH 334 - Inorganic Chemistry”
  - courses: CH 402 ⟵ “CH 402 - Instrumental Analysis”
  - courses: CH 416 ⟵ “CH 416 - Topics in Chemistry/Biochemistry”
  - courses: CH 420 ⟵ “CH 420 - Chemistry/Biochemistry Seminar”
### `f13f86643ca1aea4` Georgian Court University — degree_requirements 2026-27 · program_key=visual-art-b-a · requirement_key=major-sequences-major-electives [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/art-visual-studies/visual-arts-bachelor-art/ (sha256 49dfcec1bfaf)
  - section: major-sequences-major-electives ⟵ “Major Sequences — Major Electives”
### `f15faf57edd990b9` Georgian Court University — degree_requirements 2026-27 · program_key=sport-management-b-s · requirement_key=major-sequence-sport-management-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/sports-management-bs/ (sha256 0d380d137ae3)
  - courses: SM 213 ⟵ “SM 213 - Principles of Sport Management”
  - courses: SM 241 ⟵ “SM 241 - Sport Marketing”
  - courses: SM 311 ⟵ “SM 311 - LegalAspectsinSport”
  - courses: SM 375 ⟵ “SM 375 - Sport in Society”
### `fd38e1b02f68b908` Georgian Court University — degree_requirements 2026-27 · program_key=computer-science-b-s · requirement_key=major-sequence-cs-ma350 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/computer-sci-bs/ (sha256 4f1c0ef1048e)
  - courses: CS 433 ⟵ “CS 433 - Numerical Analysis”
  - courses: MA 331 ⟵ “MA 331 - Probability & Statistics I”
### `fd7223a5110acc08` Georgian Court University — degree_requirements 2026-27 · program_key=visual-art-b-a · requirement_key=major-sequences-other-art-history [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/art-visual-studies/visual-arts-bachelor-art/ (sha256 49dfcec1bfaf)
  - courses: AR 499 ⟵ “AR 499 - Senior Exhibition Seminar”
### `fea288a3045fb660` Georgian Court University — degree_requirements 2026-27 · program_key=business-administration-b-s · requirement_key=major-sequence-required-business-administration-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/business-administration-bs/ (sha256 fb47c1b738cf)
  - courses: BU 217 ⟵ “BU 217 - Introduction to Leadership”
  - courses: BU 319 ⟵ “BU 319 - Business & Professional Ethics”
### `ac04315d8ec33929` Hudson County Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.hccc.edu/student-success/career-transfer-pathways/transfer/partnerships/stevens-institute-of-technology/index.html (sha256 5cc114224391)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Stevens will consider grades of C or higher for transfer credit.”
### `5edab4c0fc34996b` Mercer County Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mccc.edu/admissions_transfer (sha256 e086fdd43d9d)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Only courses in which a grade of C or better was earned are eligible for transfer credits.”
### `58f0a960ca7cebe7` Middlesex College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://middlesexcollege.edu/funding-your-education/tuition-and-fees/estimated-financial-aid-cost-of-attendance/ (sha256 6dfb2ece64c7)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition: 5712.0 ⟵ “Tuition | $3,072.00 | $3,312.00 | $5,712.00”
  - column:Fees: 2172.0 ⟵ “Fees | $2,172.00 | $2,172.00 | $2,172.00”
  - column:Books: 1570.0 ⟵ “Books | $1,570.00 | $1,570.00 | $1,570.00”
  - column:Transportation: 2070.0 ⟵ “Transportation | $2,070.00 | $2,070.00 | $2,070.00”
  - column:Housing and Meals: 19022.0 ⟵ “Housing and Meals | $19,022.00 | $19,022.00 | $19,022.00”
  - column:Personal Expenses: 3362.0 ⟵ “Personal Expenses | $3,362.00 | $3,362.00 | $3,362.00”
  - column:Loan Fees: 50.0 ⟵ “Loan Fees | $50.00 | $50.00 | $50.00”
  - column:Total Budget*: 33958.0 ⟵ “Total Budget* | $31,318.00 | $31,558.00 | $33,958.00”
### `39584f3974655589` Middlesex College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://middlesexcollege.edu/admissions/high-school-dual-enrollment/ (sha256 a723ada68d61)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 0}
  - max_credit_hours_per_term: 8 ⟵ “3-4 credits per course (up to 8 credits can be taken per semester).”
### `0d540126f4db90a8` Monmouth University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.monmouth.edu/admission/undergraduate/transfer-admission/credit-evaluation/ (sha256 369da8caf99e)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Monmouth University currently accepts transfer credit from undergraduate courses that a have a grade of “C” or higher assuming the credits come from an accredited institution.”
### `07c54ead9473d932` Montclair State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.montclair.edu/admissions-aid/transfer-students (sha256 cf6bb6dab1ca)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “What Credits Transfer Courses at the 100 level or higher with a grade of C- or higher, and “P,” “CR,” or “S” grades, are accepted for full credit.”
  - min_grade: C- ⟵ “In general, no: only grades of C- or better are accepted in transfer; however there are two exceptions: When a D grade is earned through an associate degree (AA, AS, or AFA) from a community college.”
### `4a8d5c8cad7707e9` New Jersey Institute of Technology — academic_programs 2026-27 · program_key=b-s-in-human-computer-interaction [new] (labeled_in_source)
- source: https://catalog.njit.edu/undergraduate/computing-sciences/informatics/human-computer-interaction-bs/index.html (sha256 861896b09585)
- checks: {"courses": 21, "groups": 1, "groups_skipped": 0}
  - program_name: B.S. in Human-Computer Interaction ⟵ “B.S. in Human-Computer Interaction | NJIT Catalog”
### `d9d555635e93e2fe` New Jersey Institute of Technology — academic_programs 2026-27 · program_key=b-s-in-industrial-engineering-technology [new] (labeled_in_source)
- source: https://catalog.njit.edu/undergraduate/newark-college-engineering/saet-semd/manufacturing-engineering-technology/index.html (sha256 8272f594812d)
- checks: {"courses": 55, "groups": 2, "groups_skipped": 0}
  - program_name: B.S. in Industrial Engineering Technology ⟵ “B.S. in Industrial Engineering Technology | NJIT Catalog”
### `e680eafc2b172b6d` New Jersey Institute of Technology — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.njit.edu/rest/admissions/tuition-costs (sha256 b3917ba1793b)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition: 18352 ⟵ “Tuition | $18,352 | $38,226”
  - column:Fees: 4074 ⟵ “Fees | $4,074 | $4,074”
  - column:Total Tuition and Fees: 22426 ⟵ “Total Tuition and Fees | $22,426 | $42,300”
### `fc0e0f07635068d0` New Jersey Institute of Technology — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.njit.edu/cybersecurity/admissions/tuition-costs (sha256 a2931360e540)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition: 38226 ⟵ “Tuition | $18,352 | $38,226”
  - column:Fees: 4074 ⟵ “Fees | $4,074 | $4,074”
  - column:Total Tuition and Fees: 42300 ⟵ “Total Tuition and Fees | $22,426 | $42,300”
### `2a3b176430a4a9d1` New Jersey Institute of Technology — degree_requirements 2026-27 · program_key=b-s-in-industrial-engineering-technology · requirement_key=approved-technical-electives [new] (labeled_in_source)
- source: https://catalog.njit.edu/undergraduate/newark-college-engineering/saet-semd/manufacturing-engineering-technology/index.html (sha256 8272f594812d)
  - courses: BME 111 ⟵ “BME 111 - Introduction to Physiology”
  - courses: BMET 320 ⟵ “BMET 320 - Applied Biomedical Data Acquisition”
  - courses: BMET 415 ⟵ “BMET 415 - Biomedical Mechatronics”
  - courses: BMET 440 ⟵ “BMET 440 - Biomedical Experiential Learning”
  - courses: CET 314 ⟵ “CET 314 - Principles of Building Construction”
  - courses: CET 322 ⟵ “CET 322 - Construction Codes and Regulations”
  - courses: CMT 452 ⟵ “CMT 452 - Mechanical and Electrical Systems for Construction”
  - courses: ECET 210 ⟵ “ECET 210 - Intro. to Microprocessors and Computer Architecture”
  - courses: ECET 211 ⟵ “ECET 211 - Computer Architecture and Embedded Systems”
  - courses: ECET 311 ⟵ “ECET 311 - Embedded Systems I”
  - courses: ECET 319 ⟵ “ECET 319 - Electrical Systems and Power”
  - courses: ECET 411 ⟵ “ECET 411 - Embedded Systems II”
  - courses: ENGR 301 ⟵ “ENGR 301 - Engineering Applications of Data Science”
  - courses: ENGR 320 ⟵ “ENGR 320 - Prototyping Essentials”
  - courses: ENGR 330 ⟵ “ENGR 330 - Applications of Microcontrollers and IoT devices”
  - courses: ENGR 350 ⟵ “ENGR 350 - Intellectual Property for Engineers”
  - courses: ENGR 360 ⟵ “ENGR 360 - Applications of Geometric Dimensioning and Tolerancing”
  - courses: ENGR 423 ⟵ “ENGR 423 - Drone Science Fundamentals”
  - courses: ENGR 424 ⟵ “ENGR 424 - Robotics Science Fundamentals”
  - courses: ENGR 430 ⟵ “ENGR 430 - Engineering for Quality and Reliability”
  - courses: IE 449 ⟵ “IE 449 - Industrial Robotics”
  - courses: IE 456 ⟵ “IE 456 - Introduction to Industrial Hygiene”
  - courses: IE 473 ⟵ “IE 473 - Safety Engineering”
  - courses: IET 395 ⟵ “IET 395 - Coop Experience I”
  - courses: MET 235 ⟵ “MET 235 - Statics for Technology”
  - … 15 more rows
### `83e14b8bf8741624` New Jersey Institute of Technology — degree_requirements 2026-27 · program_key=b-s-in-industrial-engineering-technology · requirement_key=suggested-free-electives [new] (labeled_in_source)
- source: https://catalog.njit.edu/undergraduate/newark-college-engineering/saet-semd/manufacturing-engineering-technology/index.html (sha256 8272f594812d)
  - courses: ENGR 220 ⟵ “ENGR 220 - Introduction to Manual Machining”
  - courses: ENGR 221 ⟵ “ENGR 221 - Intro to CNC Machining”
  - courses: ENGR 222 ⟵ “ENGR 222 - Introduction to Wood Working”
  - courses: ENGR 223 ⟵ “ENGR 223 - Introduction to CNC Routing”
  - courses: ENGR 224 ⟵ “ENGR 224 - Introduction to Welding”
  - courses: ENGR 225 ⟵ “ENGR 225 - Introduction to Physical Metrology”
  - courses: ENTR 320 ⟵ “ENTR 320 - Financing New Venture”
  - courses: ENTR 440 ⟵ “ENTR 440 - Lean Startup Accelerator”
  - courses: IE 447 ⟵ “IE 447 - Legal Aspects of Engineering”
  - courses: IE 492 ⟵ “IE 492 - Engineering Management”
  - courses: MGMT 390 ⟵ “MGMT 390 - Principles of Business”
### `ae7494afa2df5d2c` New Jersey Institute of Technology — degree_requirements 2026-27 · program_key=b-s-in-human-computer-interaction · requirement_key=hci-electives [new] (labeled_in_source)
- source: https://catalog.njit.edu/undergraduate/computing-sciences/informatics/human-computer-interaction-bs/index.html (sha256 861896b09585)
  - courses: IT 265 ⟵ “IT 265 - Game Architecture and Design”
  - courses: IT 270 ⟵ “IT 270 - 3D Modeling and Animation”
  - courses: IT 286 ⟵ “IT 286 - Foundations of Game Production”
  - courses: IT 380 ⟵ “IT 380 - Educational Software Design”
  - courses: IT 383 ⟵ “IT 383 - Advanced Topics in Game Design for XR”
  - courses: IT 487 ⟵ “IT 487 - Advanced Game Production”
  - courses: IT 488 ⟵ “IT 488 - Independent Study in Information Technology”
  - courses: DD 275 ⟵ “DD 275 - Foundations of Game Design”
  - courses: AD 112 ⟵ “AD 112 - Communication in Art and Design - Digital Media”
  - courses: ID 203 ⟵ “ID 203 - Past, Present and Future of Design”
  - courses: IS 219 ⟵ “IS 219 - Adv Website Development”
  - courses: IS 322 ⟵ “IS 322 - Mobile Applications: Design, Interface, Implementation”
  - courses: IS 373 ⟵ “IS 373 - Content Management Systems”
  - courses: IS 488 ⟵ “IS 488 - Independent Study in Information Systems”
  - courses: CS 488 ⟵ “CS 488 - Independent Study in Computer Science”
  - courses: DS 488 ⟵ “DS 488 - Independent Study in Data Science”
  - courses: PSY 361 ⟵ “PSY 361 - Advanced Topics in Cyberpsychology”
  - courses: PSY 321 ⟵ “PSY 321 - Social Psychology”
  - courses: PSY 339 ⟵ “PSY 339 - Psychology of Diversity”
  - courses: YWCC 310 ⟵ “YWCC 310 - Co-op Work Experience I”
  - courses: YWCC 410 ⟵ “YWCC 410 - Co-op Work Experience II”
### `m32b8ddb70492da8` Ocean County College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ocean.edu/wp-content/uploads/2026/08/OCC-Early-College-Information-Steps-2026.pdf (sha256 5f3caf708ec5)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 47, "tiers": 0}
  - per_credit_hour_charge: 133 ⟵ “Cost                              Ocean County Early College Tuition Rate: $133.00/credit”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 153 ⟵ “$153 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 153 ⟵ “$153 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 146 ⟵ “$146 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 126 ⟵ “$126 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - per_credit_hour_charge: 133 ⟵ “$133 per credit (*plus any applicable course fees)”
  - … 22 more rows
### `3191530b6f19cffb` Ramapo College of New Jersey — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://apply.ramapo.edu/register/deinquiryform (sha256 3c8afbe0249a)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Students must have a 3.0 GPA or higher and the minimum age to participate is 16”
### `d392e1445d9f95b5` Ramapo College of New Jersey — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ramapo.edu/undergraduate/transfer/faqs/ (sha256 ba8dd0867f2c)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “If you are taking coursework where we offer a comparable course and/or discipline, and you receive a grade of C or better, your credit will transfer.”
### `1b7849e0df6895d2` Raritan Valley Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.raritanval.edu/education-for-everyone/who-you-are/high-school-students/early-college-credit/ (sha256 2f9b2605342f)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “Students must be a high school sophomore, junior, or senior with a minimum GPA of 3.0.”
  - eligibility_tier: 3.0 ⟵ “Request your high school transcript showing a 3.0+ GPA.”
### `cbffc7c2f679df26` Rider University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.rider.edu/tuition-aid/tuition-fees/undergraduate (sha256 dcd3bf593232)
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition (Annual): 43580 ⟵ “Tuition (Annual) | $43,580 | $43,580”
  - on_campus:Fees: 1870 ⟵ “Fees | $1,870 | $1,870”
  - on_campus:Room and Board*: 19470 ⟵ “Room and Board* | $19,470 | $0”
  - on_campus:Total (Annual): 64920 ⟵ “Total (Annual) | $64,920 | $45,450”
  - with_parents_or_family:Tuition (Annual): 43580 ⟵ “Tuition (Annual) | $43,580 | $43,580”
  - with_parents_or_family:Fees: 1870 ⟵ “Fees | $1,870 | $1,870”
  - with_parents_or_family:Room and Board*: 0 ⟵ “Room and Board* | $19,470 | $0”
  - with_parents_or_family:Total (Annual): 45450 ⟵ “Total (Annual) | $64,920 | $45,450”
### `d9f5ef1e4748c381` Rowan College at Burlington County — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://rcbc.edu/transfer-students (sha256 9745b744cad3)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “RCBC accepts transfer credits, not grades, from accredited colleges submitted as official transcripts with a grade of C or better.”
### `7f9dcc961bcbbcd8` Rutgers University-Camden — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.camden.rutgers.edu/costs-and-aid/tuition-fees (sha256 f5f583b71c79)
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - with_parents_or_family:Tuition: 36831 ⟵ “Tuition | $36,831 | $36,831”
  - with_parents_or_family:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - with_parents_or_family:Food and Housing: 6060 ⟵ “Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total: 46720 ⟵ “Total | $46,720 | $62,603”
  - on_campus:Tuition: 36831 ⟵ “Tuition | $36,831 | $36,831”
  - on_campus:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - on_campus:Food and Housing: 21943 ⟵ “Food and Housing | $6,060 | $21,943”
  - on_campus:Total: 62603 ⟵ “Total | $46,720 | $62,603”
### `06eb89a195f6210e` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: $2000 ⟵ “Hudson County Community College Alumni Grant | $2000”
### `1b765b9ca22bb2ce` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: $18,000 ⟵ “Petrean | 2.5-2.99 | $18,000”
  - gpa_requirement: 2.5-2.99 ⟵ “Petrean | 2.5-2.99 | $18,000”
### `39ebb4e2cc99ac8e` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - award_amount_text: $20,000 to $25,000 ⟵ “Loyola | 3.0 or above | $20,000 to $25,000”
  - gpa_requirement: 3.0 or above ⟵ “Loyola | 3.0 or above | $20,000 to $25,000”
### `45caf9f9173a6083` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: full tuition ⟵ “Presidential | Admissions committee | full tuition”
  - gpa_requirement: Admissions committee ⟵ “Presidential | Admissions committee | full tuition”
### `48782a7d62a486b4` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: $21,000 ⟵ “Pavonia | 3.0-3.24 | $21,000”
  - gpa_requirement: 3.0-3.24 ⟵ “Pavonia | 3.0-3.24 | $21,000”
### `4bb1bdaeced76e32` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: $2000 ⟵ “Legacy (Parent or grandparent is an alum of Saint Peter’s University | $2000”
### `4beb32e8d31a9ce5` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: $1500 ⟵ “Phi Theta Kappa Member | $1500”
### `58846fea7df6a35c` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $30,000 ⟵ “Academic Excellence | 4.0 | $30,000”
  - gpa_requirement: 4.0 ⟵ “Academic Excellence | 4.0 | $30,000”
### `59bd527f73895e66` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: $27,000 ⟵ “Dean’s | 3.5-3.99 | $27,000”
  - gpa_requirement: 3.5-3.99 ⟵ “Dean’s | 3.5-3.99 | $27,000”
### `6d7f23f1c26406bb` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: $20,000 ⟵ “Arrupe | 2.99 or under | $20,000”
  - gpa_requirement: 2.99 or under ⟵ “Arrupe | 2.99 or under | $20,000”
### `6fb58aaac66a023f` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: $23,000 ⟵ “Ignatian | 3.25-3.49 | $23,000”
  - gpa_requirement: 3.25-3.49 ⟵ “Ignatian | 3.25-3.49 | $23,000”
### `8cb2165d4f8d7c40` Saint Peter's University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/enrollment-services/student-financial-aid/scholarships/ (sha256 472af94e7757)
- checks: {"thresholds": null}
  - award_amount_text: $15,000 ⟵ “Pavo | 2.0-2.49 | $15,000”
  - gpa_requirement: 2.0-2.49 ⟵ “Pavo | 2.0-2.49 | $15,000”
### `492d833d5705ba67` Saint Peter's University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.saintpeters.edu/undergraduate-admission/applying-to-saint-peters/transfer-students/transfer-faqs/ (sha256 ee1f02874215)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Courses with a grade of C or better will be transferred when they correspond to the Saint Peter’s University curriculum.”
### `31b8d789ef834b5b` Stevens Institute of Technology — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stevens.edu/admission-aid/tuition-financial-aid/undergraduate-costs-and-aid (sha256 b297343467cd)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and Fees: 68230 ⟵ “Tuition and Fees | $68,230”
  - on_campus:Loan Fees (for students offered federal student loans): 70 ⟵ “Loan Fees (for students offered federal student loans) | $70”
  - on_campus:Housing and Meals: 20744 ⟵ “Housing and Meals | $20,744”
  - on_campus:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200”
  - on_campus:Miscellaneous: 1050 ⟵ “Miscellaneous | $1,050”
  - on_campus:Total Cost of Attendance: 91294 ⟵ “Total Cost of Attendance | $91,294”
### `9ba3fee98dc03e53` Stevens Institute of Technology — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.stevens.edu/admission-aid/undergraduate-admissions/accepted-students/ap-ib-and-college-transfer-credit (sha256 13dc57611081)
- checks: {"distinct_exams": 30, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|African American Studies (4,5)]:  ⟵ “African American Studies (4,5) | HHS-LEQ | 3”
  - equivalencies[AP-ART-HISTORY|Art History (4,5)]:  ⟵ “Art History (4,5) | HAR-LEQ | 3”
  - equivalencies[AP-BIOLOGY|Biology (4,5)]:  ⟵ “Biology (4,5) | BIO 181 and BIO 182 | 4”
  - equivalencies[AP-CHEMISTRY|Chemistry (4,5)]:  ⟵ “Chemistry (4,5) | CH 115, 116, 117, and 118 | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|Chinese Language and Culture (4,5)]:  ⟵ “Chinese Language and Culture (4,5) | General Elective | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|Computer Science A (4,5)]:  ⟵ “Computer Science A (4,5) | Computer Science (CS) and Artificial Intelligence (AI) majors will receive credit for one technical elective. Cybersecurity (CyS) majors will receive credit for one computer science elective. School of Business and Quantitative Finance majors will receive credit for MIS 11”
  - equivalencies[AP-MACROECONOMICS|Economics - Macroeconomics (4,5)]:  ⟵ “Economics - Macroeconomics (4,5) | ECON 243* | 3”
  - equivalencies[AP-MICROECONOMICS|Economics - Microeconomics (4,5)]:  ⟵ “Economics - Microeconomics (4,5) | ECON 244* | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|Environmental Science (4,5)]:  ⟵ “Environmental Science (4,5) | General Elective | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|French Language (4,5)]:  ⟵ “French Language (4,5) | General Elective | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|German Language (4,5)]:  ⟵ “German Language (4,5) | General Elective | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|Human Geography (4,5)]:  ⟵ “Human Geography (4,5) | HSSC-LEQ | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|Italian Language and Culture (4,5)]:  ⟵ “Italian Language and Culture (4,5) | General Elective | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|Japanese Language and Culture (4,5)]:  ⟵ “Japanese Language and Culture (4,5) | General Elective | 3”
  - equivalencies[AP-LATIN|Latin (4,5)]:  ⟵ “Latin (4,5) | General Elective | 3”
  - equivalencies[AP-CALCULUS-AB|Mathematics - Calculus AB (4,5)* * Please note, Stevens does not accept the Calculus AB subscore.]:  ⟵ “Mathematics - Calculus AB (4,5)* * Please note, Stevens does not accept the Calculus AB subscore. | School of Engineering and Science, Quantitative Finance, and Quantitative Social Science majors receive credit for MA 121 and MA 122 | 4”
  - equivalencies[AP-CALCULUS-AB|Mathematics - Calculus AB (4,5)** Please note, Stevens does not accept the Calculus AB subscore.]:  ⟵ “Mathematics - Calculus AB (4,5)** Please note, Stevens does not accept the Calculus AB subscore. | School of Business (except QF) and School of Humanities, Arts and Social Science (except QSS) majors receive credit for MA 111 | 2”
  - equivalencies[AP-CALCULUS-BC|Mathematics - Calculus BC (4,5)]:  ⟵ “Mathematics - Calculus BC (4,5) | School of Engineering and Science, and Quantitative Social Science majors receive credit for MA 121 and MA 122 | 4”
  - equivalencies[AP-CALCULUS-BC|Mathematics - Calculus BC (4,5)]:  ⟵ “Mathematics - Calculus BC (4,5) | Quantitative Finance majors receive credit for MA 121, MA 122, & MA 123 | 6”
  - equivalencies[AP-CALCULUS-BC|Mathematics - Calculus BC (4,5)]:  ⟵ “Mathematics - Calculus BC (4,5) | School of Business (except QF) and School of Humanities, Arts and Social Science (except QSS) majors receive credit for MA 111 | 2”
  - equivalencies[AP-MUSIC-THEORY|Music Theory (4,5)]:  ⟵ “Music Theory (4,5) | HMU 201 | 3”
  - equivalencies[AP-PHYSICS-1|Physics 1 (4,5)]:  ⟵ “Physics 1 (4,5) | PEP 123 (for Business and Humanities majors) | 3”
  - equivalencies[AP-PHYSICS-2|Physics 2 (4,5)]:  ⟵ “Physics 2 (4,5) | PEP 124 (for Business and Humanities Majors) | 3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|Physics C - Mechanics (4,5)]:  ⟵ “Physics C - Mechanics (4,5) | PEP 111 | 3”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|Physics C - E & M (4,5)]:  ⟵ “Physics C - E & M (4,5) | PEP 112 | 3”
  - … 8 more rows
### `m6bc3ae5a0c29df6` Stevens Institute of Technology — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.stevens.edu/admission-aid/undergraduate-admissions/transfer-students/after-applying (sha256 b43611afbf71)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Credit Evaluation Policies A grade of C or higher is required for credits to be eligible for transfer.”
  - min_grade: C ⟵ “Credit Evaluation Policies A grade of C or higher is required for credits to be eligible for transfer.”
### `me96ec3c5ae71ec0` The College of New Jersey — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.tcnj.edu/applications/international-applicants/guidelines-for-international-transfer-applicants/ (sha256 c76bb4562d26)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Generally, 100- and 200- level courses where a grade of C or better was earned will usually transfer to TCNJ.”
  - min_grade: C ⟵ “Generally, 100- and 200- level courses where a grade of C or better was earned will usually transfer to TCNJ.”
### `84306aeeedb57476` UCNJ Union College of Union County, NJ — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ucc.edu/admissions/admissions-process/high-school-dual-enrollment/ (sha256 17a024c54c43)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a cumulative ‘B’ average or 3.0 grade point average in your high school studies”
### `099d8aa6d16a6892` UCNJ Union College of Union County, NJ — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ucc.edu/administration/institutional-research/common-data-set/transfer-admission/ (sha256 5138da4dc193)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “TRANSFER CREDIT POLICIES Non-remedial courses with a grade of “C” (2.0) or better will be considered for transfer credit.”
### `44a76c41264ef03f` William Paterson University of New Jersey — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.wpunj.edu/studentaccounts/tuition-and-fees/index.html (sha256 2e8e275a81b8)
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:TUITION - per semester*: 8379 ⟵ “TUITION - per semester* | $ 8,379 | $13,692”
  - column:Technology Fee: 178 ⟵ “Technology Fee | $178 | $178”
  - column:Student Govt Assn Fee: 105 ⟵ “Student Govt Assn Fee | $ 105 | $105”
  - column:TOTAL per semester: 8662 ⟵ “TOTAL per semester | $ 8,662 | $ 13,975”
### `ad7351abde09e837` William Paterson University of New Jersey — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.wpunj.edu/studentaccounts/tuition-and-fees/index.html (sha256 2e8e275a81b8)
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:TUITION - per semester*: 13692 ⟵ “TUITION - per semester* | $ 8,379 | $13,692”
  - column:Technology Fee: 178 ⟵ “Technology Fee | $178 | $178”
  - column:Student Govt Assn Fee: 105 ⟵ “Student Govt Assn Fee | $ 105 | $105”
  - column:TOTAL per semester: 13975 ⟵ “TOTAL per semester | $ 8,662 | $ 13,975”
### `9164c0715953283e` William Paterson University of New Jersey — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.wpunj.edu/admissions/undergraduate/accepted-students/advanced-placement-information (sha256 02721936767c)
- checks: {"distinct_exams": 39, "equivalencies": 60, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3, 4, or 5]:  ⟵ “Arts | Art History | 3, 4, or 5 | ARTH 1010 | Understanding Art | 3”
  - equivalencies[AP-MUSIC-THEORY|3, 4, or 5]:  ⟵ “Arts | Music Theory | 3, 4, or 5 | MUSI 1600 | Music Theory I | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, or 5]:  ⟵ “Arts | Studio Art 2D Design | 3, 4, or 5 | ARTS 1200 | 2-D Design | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, or 5]:  ⟵ “Arts | Studio Art 3D Design | 3, 4, or 5 | ARTS 1100 | 3-D Design | 3”
  - equivalencies[AP-DRAWING|3, 4, or 5]:  ⟵ “Arts | Studio Art Drawing | 3, 4, or 5 | ARTS 1050 | Drawing Studio | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3, 4, or 5]:  ⟵ “English | English Language and Composition | 3, 4, or 5 | ENG 1100 | College Writing | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, or 5]:  ⟵ “English | English Literature and Composition | 3, 4, or 5 | ENG 1500 | Experiencing Literature | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3, 4, or 5]:  ⟵ “History and Social Sciences | Comparative Government and Politics | 3, 4, or 5 | POLS 2990 | Elective Credit | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3, 4, or 5]:  ⟵ “History and Social Sciences | European History | 3, 4, or 5 | HIST 1120 | The West and the World: Ancient and Medieval | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3, 4, or 5]:  ⟵ “History and Social Sciences | Human Geography | 3, 4, or 5 | GEOG 2020 | Introduction to Human Geography | 3”
  - equivalencies[AP-MACROECONOMICS|3, 4, or 5]:  ⟵ “History and Social Sciences | Macroeconomics | 3, 4, or 5 | ECON 2020 | Principles of Macroeconomics | 3”
  - equivalencies[AP-MICROECONOMICS|3, 4, or 5]:  ⟵ “History and Social Sciences | Microeconomics | 3, 4, or 5 | ECON 2010 | Principles of Microeconomics | 3”
  - equivalencies[AP-PSYCHOLOGY|3, 4, or 5]:  ⟵ “History and Social Sciences | Psychology | 3, 4, or 5 | PSY 1100 | General Psychology | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3, 4, or 5]:  ⟵ “History and Social Sciences | United States Government and Politics | 3, 4, or 5 | POLS 1100 | American Government | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3, 4, or 5]:  ⟵ “History and Social Sciences | United States History | 3, 4, or 5 | HIST 2050 and HIST 2060 | U.S. History to 1865 and U.S. History Since 1865 | 6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3, 4, or 5]:  ⟵ “History and Social Sciences | World History: Modern | 3, 4, or 5 | HIST 1060 | Foundations of Civilization | 3”
  - equivalencies[AP-CALCULUS-AB|3, 4, or 5]:  ⟵ “Mathematics & Computer Science | Calculus AB | 3, 4, or 5 | MATH 1600 | Calculus I | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Mathematics & Computer Science | Calculus BC | 3 | MATH 1600 | Calculus I | 4”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Mathematics & Computer Science | Calculus BC | 4, 5 | MATH 1600 & MATH 1610 | Calculus I & II | 8”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Mathematics & Computer Science | Statistics | 3 | MATH 1300 | Elementary Statistics | 3”
  - equivalencies[AP-STATISTICS|4, 5]:  ⟵ “Mathematics & Computer Science | Statistics | 4, 5 | MATH 2300 | Statistics I | 4”
  - equivalencies[AP-PRECALCULUS|3, 4, or 5]:  ⟵ “Mathematics & Computer Science | Precalculus | 3, 4, or 5 | MATH 1160 | Precalculus | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, or 5]:  ⟵ “Mathematics & Computer Science | Computer Science Principles | 3, 4, or 5 | CS 2010 | Computer and Information Technology | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4, 5]:  ⟵ “Mathematics & Computer Science | Computer Science A | 4, 5 | CS 2300 | Computer Science I | 4”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Sciences | Biology | 3 | BIO 1200 or BIO 1300 | Human Biology or Field Biology | 4”
  - … 35 more rows

## Exceptions (302)

### `f383cc157ae51700` Atlantic Cape Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://atlanticcape.edu/one-stop/financial-aid/index.php (sha256 daf18f70434f)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Learn More Financial Aid Appeals & Special Circumstances Life happens.”
### `3f4b03e3c67250f4` Atlantic Cape Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://atlanticcape.edu/one-stop/testing/advanced-placement.php (sha256 b4d45d25a733)
- issues: course_column_missing
- checks: {"distinct_exams": 9, "equivalencies": 11, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|3-4]:  ⟵ “Biology | BIOL109 General Biology I | 3-4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “ | BIOL109 General Biology I & BIOL110 General Biology II | 5”
  - equivalencies[AP-CHEMISTRY|3-4]:  ⟵ “Chemistry | CHEM110 General Chemistry I | 3-4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “ | CHEM110 General Chemistry I & CHEM111 General Chemistry II | 5”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3-5]:  ⟵ “French | FREN111 Elementary French I | 3-5”
  - equivalencies[AP-UNITED-STATES-HISTORY|3-5]:  ⟵ “History, United States | HIST103 US History I and HIST104 US History II | 3-5”
  - equivalencies[AP-PHYSICS-1|3-5]:  ⟵ “Physics-B | PHYS125 College Physics I & PHYS126 College Physics II | 3-5”
  - equivalencies[AP-PSYCHOLOGY|3-5]:  ⟵ “Psychology | PSYC101 General Psychology | 3-5”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3-5]:  ⟵ “Spanish | SPAN111 Elementary Spanish I | 3-5”
  - equivalencies[AP-2-D-ART-DESIGN|3-5]:  ⟵ “Studio Art | ARTS100 Color & 2-D Design | 3-5”
  - equivalencies[AP-DRAWING|3-5]:  ⟵ “ | ARTS110 Fundamental Drawing | 3-5”
### `5678343b91b201de` Bergen Community College — appeals 2026-27 [new] (labeled_in_heading)
- source: https://bergen.edu/financial-aid/ (sha256 0f1cec3741ae)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Bergen Community College Federal School Code: 004736 FAFSA® Filing Deadlines and Workshop information Special Circumstances If you or your family’s financial situation has changed due to loss of job or benefits, separation or divorce, death, or other special circumstances, we encourage you to submit the Special Circumstance Form to our office with the required documentation to have your financial ”
  - sentence: need_based_special_circumstances ⟵ “Items families will need to provide will vary but, in general, for a student’s file to be re-evaluated for Special Circumstances the following must be provided to the Financial Aid Office: Letter explaining the Extenuating Circumstances Supporting Documentation (examples are listed on the Special Circumstances form).”
  - sentence: need_based_special_circumstances ⟵ “Submit the Request for Special Circumstance form applicable to your FAFSA award application: For the 2025-2026 academic year/FAFSA special circumstances, use the 2025-2026 Request For Special Circumstance (Online Form).”
  - sentence: need_based_special_circumstances ⟵ “For the 2026-2027 academic year/FAFSA special circumstances, complete the 2026-2027 Request For Special Circumstance (Online Form).”
### `83f4720ad942ff8e` Bergen Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://bergen.edu/financial-aid/standards-of-satisfactory-academic-progress/ (sha256 3420d3f2ec0c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “PLAN AHEAD: The Satisfactory Academic Progress (SAP) appeal deadlines can be found at the Financial Aid Workshops and Deadlines Web page.”
  - sentence: sap_appeal ⟵ “Late submitted SAP appeals will not be reviewed.”
  - sentence: sap_appeal ⟵ “Check your Bergen CC email to complete the SAP Appeal.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Form is to be initiated with the assistance of an Academic Counselor/Advisor.”
  - sentence: sap_appeal ⟵ “A notification with instructions to complete the rest of SAP appeal form content sections will be then be sent to your BCC student Email account.”
  - sentence: sap_appeal ⟵ “Information about SAP Appeal Submissions deadlines can be found on the Financial Aid Dates & Deadlines Web page.”
### `25a7d237316bd9fa` Bergen Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://bergen.edu/financial-aid/cost-of-attendance/ (sha256 9bab649172ef)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 4, "rows": 26}
  - with_parents_or_family:Registration Fee per semester: 17.55 ⟵ “Registration Fee per semester | $17.55 | $17.55 | $17.55 | $17.55 | $17.55 | $17.55”
  - with_parents_or_family:Tuition and Fees (based on 24 credits): 5286.0 ⟵ “Tuition and Fees (based on 24 credits) | $5,286.00 | $5,286.00 | $9,572.00 | $9,572.00 | $10,006.00 | $10,006.00”
  - with_parents_or_family:Food and Housing: 5844.0 ⟵ “Food and Housing | $5,844.00 | $15,086.00 | $5,844.00 | $15,086.00 | $5,844.00 | $15,086.00”
  - with_parents_or_family:Books and Supplies: 1500.0 ⟵ “Books and Supplies | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00”
  - with_parents_or_family:Transportation: 2940.0 ⟵ “Transportation | $2,940.00 | $2,940.00 | $2,940.00 | $2,940.00 | $2,940.00 | $2,940.00”
  - with_parents_or_family:Personal: 3000.0 ⟵ “Personal | $3,000.00 | $3,000.00 | $3,000.00 | $3,00.00 | $3,000.00 | $3,00.00”
  - with_parents_or_family:Loans & Fees: 36.0 ⟵ “Loans & Fees | $36.00 | $36.00 | $36.00 | $36.00 | $36.00 | $36.00”
  - with_parents_or_family:TOTAL: 18606.0 ⟵ “TOTAL | $18,606.00 | $27,848.00 | $22,892.00 | $32,134.00 | $23,326.00 | $32,568.00”
  - with_parents_or_family:Tuition and Fees (based on 24 credits) (2): 3974.0 ⟵ “Tuition and Fees (based on 24 credits) | $3,974.00 | $3,974.00 | $7,188.00 | $7,188.00 | $7,514.00 | $7,514.00”
  - with_parents_or_family:Food and Housing (2): 5584.0 ⟵ “Food and Housing | $5,584.00 | $15,086.00 | $5,584.00 | $15,086.00 | $5,584.00 | $15,086.00”
  - with_parents_or_family:Books and Supplies (2): 1125.0 ⟵ “Books and Supplies | $1,125.00 | $1,125.00 | $1,125.00 | $1,125.00 | $1,125.00 | $1,125.00”
  - with_parents_or_family:Transportation (2): 2205.0 ⟵ “Transportation | $2,205.00 | $2,205.00 | $2,205.00 | $2,205.00 | $2,205.00 | $2,205.00”
  - with_parents_or_family:Personal (2): 2250.0 ⟵ “Personal | $2,250.00 | $2,250.00 | $2,250.00 | $2,250.00 | $2,250.00 | $2,250.00”
  - with_parents_or_family:Loans & Fees (2): 36.0 ⟵ “Loans & Fees | $36.00 | $36.00 | $36.00 | $36.00 | $36.00 | $36.00”
  - with_parents_or_family:TOTAL (2): 15174.0 ⟵ “TOTAL | $15,174.00 | $24,676.00 | $18,388.00 | $27,890.00 | $18,714.00 | $28,216.00”
  - with_parents_or_family:Tuition and Fees (based on 24 credits) (3): 2660.0 ⟵ “Tuition and Fees (based on 24 credits) | $2,660.00 | $2,660.00 | $4,804.00 | $4,804.00 | $5,020.00 | $5,020.00”
  - with_parents_or_family:Food and Housing (3): 5584.0 ⟵ “Food and Housing | $5,584.00 | $15,086.00 | $5,584.00 | $15,086.00 | $5,584.00 | $15,086.00”
  - with_parents_or_family:Books and Supplies (3): 750.0 ⟵ “Books and Supplies | $750.00 | $750.00 | $750.00 | $750.00 | $750.00 | $750.00”
  - with_parents_or_family:Transportation (3): 1470.0 ⟵ “Transportation | $1,470.00 | $1,470.00 | $1,470.00 | $1,470.00 | $1,470.00 | $1,470.00”
  - with_parents_or_family:Personal (3): 1500.0 ⟵ “Personal | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00”
  - with_parents_or_family:Loans & Fees (3): 36.0 ⟵ “Loans & Fees | $36.00 | $36.00 | $36.00 | $36.00 | $36.00 | $36.00”
  - with_parents_or_family:TOTAL (3): 12000.0 ⟵ “TOTAL | $12,000.00 | $21,502.00 | $14,144.00 | $23,646.00 | $14,360.00 | $23,862.00”
  - with_parents_or_family:Tuition and Fees (based on 24 credits) (4): 1348.0 ⟵ “Tuition and Fees (based on 24 credits) | $1,348.00 | $1,348.00 | $2,420.00 | $2,420.00 | $2,528.00 | $2,528.00”
  - with_parents_or_family:Books and Supplies (4): 375.0 ⟵ “Books and Supplies | $375.00 | $375.00 | $375.00 | $375.00 | $375.00 | $375.00”
  - with_parents_or_family:Transportation (4): 735.0 ⟵ “Transportation | $735.00 | $735.00 | $735.00 | $735.00 | $735.00 | $735.00”
  - … 79 more rows
### `c0ea78e221bfcc80` Bergen Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://bergen.edu/financial-aid/cost-of-attendance/ (sha256 9bab649172ef)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 9933.6 ⟵ “Tuition and Fees | $9,933.60 | $9,933.60”
  - with_parents_or_family:Food and Housing: 5844.0 ⟵ “Food and Housing | $5,844.00 | $15,086.00”
  - with_parents_or_family:Books and Supplies: 1500.0 ⟵ “Books and Supplies | $1,500.00 | $1,500.00”
  - with_parents_or_family:Transportation: 2940.0 ⟵ “Transportation | $2,940.00 | $2,940.00”
  - with_parents_or_family:Personal/Miscellaneous: 3000.0 ⟵ “Personal/Miscellaneous | $3,000.00 | $3,000.00”
  - with_parents_or_family:Loan Fees: 36.0 ⟵ “Loan Fees | $36.00 | $36.00”
  - with_parents_or_family:TOTAL: 23253.6 ⟵ “TOTAL | $23,253.60 | $32,495.60”
  - off_campus_not_with_family:Tuition and Fees: 9933.6 ⟵ “Tuition and Fees | $9,933.60 | $9,933.60”
  - off_campus_not_with_family:Food and Housing: 15086.0 ⟵ “Food and Housing | $5,844.00 | $15,086.00”
  - off_campus_not_with_family:Books and Supplies: 1500.0 ⟵ “Books and Supplies | $1,500.00 | $1,500.00”
  - off_campus_not_with_family:Transportation: 2940.0 ⟵ “Transportation | $2,940.00 | $2,940.00”
  - off_campus_not_with_family:Personal/Miscellaneous: 3000.0 ⟵ “Personal/Miscellaneous | $3,000.00 | $3,000.00”
  - off_campus_not_with_family:Loan Fees: 36.0 ⟵ “Loan Fees | $36.00 | $36.00”
  - off_campus_not_with_family:TOTAL: 32495.6 ⟵ “TOTAL | $23,253.60 | $32,495.60”
### `d27997bc81b986d9` Bergen Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://bergen.edu/financial-aid/cost-of-attendance/ (sha256 9bab649172ef)
- issues: arrangement_unlabeled, multiple_total_rows
- checks: {"columns": 2, "rows": 26}
  - with_parents_or_family:Registration Fee per semester: 17.55 ⟵ “Registration Fee per semester | $17.55 | $17.55 | $17.55 | $17.55 | $17.55 | $17.55”
  - with_parents_or_family:Tuition and Fees (based on 24 credits): 10006.0 ⟵ “Tuition and Fees (based on 24 credits) | $5,286.00 | $5,286.00 | $9,572.00 | $9,572.00 | $10,006.00 | $10,006.00”
  - with_parents_or_family:Food and Housing: 5844.0 ⟵ “Food and Housing | $5,844.00 | $15,086.00 | $5,844.00 | $15,086.00 | $5,844.00 | $15,086.00”
  - with_parents_or_family:Books and Supplies: 1500.0 ⟵ “Books and Supplies | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00”
  - with_parents_or_family:Transportation: 2940.0 ⟵ “Transportation | $2,940.00 | $2,940.00 | $2,940.00 | $2,940.00 | $2,940.00 | $2,940.00”
  - with_parents_or_family:Personal: 3000.0 ⟵ “Personal | $3,000.00 | $3,000.00 | $3,000.00 | $3,00.00 | $3,000.00 | $3,00.00”
  - with_parents_or_family:Loans & Fees: 36.0 ⟵ “Loans & Fees | $36.00 | $36.00 | $36.00 | $36.00 | $36.00 | $36.00”
  - with_parents_or_family:TOTAL: 23326.0 ⟵ “TOTAL | $18,606.00 | $27,848.00 | $22,892.00 | $32,134.00 | $23,326.00 | $32,568.00”
  - with_parents_or_family:Tuition and Fees (based on 24 credits) (2): 7514.0 ⟵ “Tuition and Fees (based on 24 credits) | $3,974.00 | $3,974.00 | $7,188.00 | $7,188.00 | $7,514.00 | $7,514.00”
  - with_parents_or_family:Food and Housing (2): 5584.0 ⟵ “Food and Housing | $5,584.00 | $15,086.00 | $5,584.00 | $15,086.00 | $5,584.00 | $15,086.00”
  - with_parents_or_family:Books and Supplies (2): 1125.0 ⟵ “Books and Supplies | $1,125.00 | $1,125.00 | $1,125.00 | $1,125.00 | $1,125.00 | $1,125.00”
  - with_parents_or_family:Transportation (2): 2205.0 ⟵ “Transportation | $2,205.00 | $2,205.00 | $2,205.00 | $2,205.00 | $2,205.00 | $2,205.00”
  - with_parents_or_family:Personal (2): 2250.0 ⟵ “Personal | $2,250.00 | $2,250.00 | $2,250.00 | $2,250.00 | $2,250.00 | $2,250.00”
  - with_parents_or_family:Loans & Fees (2): 36.0 ⟵ “Loans & Fees | $36.00 | $36.00 | $36.00 | $36.00 | $36.00 | $36.00”
  - with_parents_or_family:TOTAL (2): 18714.0 ⟵ “TOTAL | $15,174.00 | $24,676.00 | $18,388.00 | $27,890.00 | $18,714.00 | $28,216.00”
  - with_parents_or_family:Tuition and Fees (based on 24 credits) (3): 5020.0 ⟵ “Tuition and Fees (based on 24 credits) | $2,660.00 | $2,660.00 | $4,804.00 | $4,804.00 | $5,020.00 | $5,020.00”
  - with_parents_or_family:Food and Housing (3): 5584.0 ⟵ “Food and Housing | $5,584.00 | $15,086.00 | $5,584.00 | $15,086.00 | $5,584.00 | $15,086.00”
  - with_parents_or_family:Books and Supplies (3): 750.0 ⟵ “Books and Supplies | $750.00 | $750.00 | $750.00 | $750.00 | $750.00 | $750.00”
  - with_parents_or_family:Transportation (3): 1470.0 ⟵ “Transportation | $1,470.00 | $1,470.00 | $1,470.00 | $1,470.00 | $1,470.00 | $1,470.00”
  - with_parents_or_family:Personal (3): 1500.0 ⟵ “Personal | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00”
  - with_parents_or_family:Loans & Fees (3): 36.0 ⟵ “Loans & Fees | $36.00 | $36.00 | $36.00 | $36.00 | $36.00 | $36.00”
  - with_parents_or_family:TOTAL (3): 14360.0 ⟵ “TOTAL | $12,000.00 | $21,502.00 | $14,144.00 | $23,646.00 | $14,360.00 | $23,862.00”
  - with_parents_or_family:Tuition and Fees (based on 24 credits) (4): 2528.0 ⟵ “Tuition and Fees (based on 24 credits) | $1,348.00 | $1,348.00 | $2,420.00 | $2,420.00 | $2,528.00 | $2,528.00”
  - with_parents_or_family:Books and Supplies (4): 375.0 ⟵ “Books and Supplies | $375.00 | $375.00 | $375.00 | $375.00 | $375.00 | $375.00”
  - with_parents_or_family:Transportation (4): 735.0 ⟵ “Transportation | $735.00 | $735.00 | $735.00 | $735.00 | $735.00 | $735.00”
  - … 27 more rows
### `dcfa6fd9603db713` Bergen Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://bergen.edu/financial-aid/cost-of-attendance/ (sha256 9bab649172ef)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 5416.8 ⟵ “Tuition and Fees | $5,416.80 | $5,416.80”
  - with_parents_or_family:Food and Housing: 5844.0 ⟵ “Food and Housing | $5,844.00 | $15,086.00”
  - with_parents_or_family:Books and Supplies: 1500.0 ⟵ “Books and Supplies | $1,500.00 | $1,500.00”
  - with_parents_or_family:Transportation: 2940.0 ⟵ “Transportation | $2,940.00 | $2,940.00”
  - with_parents_or_family:Personal/Miscellaneous: 3000.0 ⟵ “Personal/Miscellaneous | $3,000.00 | $3,000.00”
  - with_parents_or_family:Loan Fees: 36.0 ⟵ “Loan Fees | $36.00 | $36.00”
  - with_parents_or_family:TOTAL: 18736.8 ⟵ “TOTAL | $18,736.80 | $27,978.80”
  - off_campus_not_with_family:Tuition and Fees: 5416.8 ⟵ “Tuition and Fees | $5,416.80 | $5,416.80”
  - off_campus_not_with_family:Food and Housing: 15086.0 ⟵ “Food and Housing | $5,844.00 | $15,086.00”
  - off_campus_not_with_family:Books and Supplies: 1500.0 ⟵ “Books and Supplies | $1,500.00 | $1,500.00”
  - off_campus_not_with_family:Transportation: 2940.0 ⟵ “Transportation | $2,940.00 | $2,940.00”
  - off_campus_not_with_family:Personal/Miscellaneous: 3000.0 ⟵ “Personal/Miscellaneous | $3,000.00 | $3,000.00”
  - off_campus_not_with_family:Loan Fees: 36.0 ⟵ “Loan Fees | $36.00 | $36.00”
  - off_campus_not_with_family:TOTAL: 27978.8 ⟵ “TOTAL | $18,736.80 | $27,978.80”
### `b2874ef75765cb7a` Bergen Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://bergen.edu/wp-content/uploads/BCC-Dual-Enrollment-2026_2027.pdf (sha256 28c474fa66a9)
- issues: multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.75 ⟵ “Minimum 2.75 GPA and                   Courses are taught at your high school     A letter grade on your official Bergen”
### `56a93eb98cf4389c` Brookdale Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.brookdalecc.edu/financial-aid/ (sha256 c55d9e192706)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.brookdalecc.edu/financial-aid/about-your-award/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Find out if your parent(s) or spouse will need to be contributors (contribute their info on your FAFSA form) Special Circumstance Review: Changes at home financially since filing the FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “Students may request a Special Circumstance Review*.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances/Dependency Override: If you have extraordinary reasons for not being able to provide parent information on your FAFSA, you may request a Dependency Override*.”
### `bcf7f6e33e4f30a5` Brookdale Community College — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.brookdalecc.edu/financial-aid/about-your-award/ (sha256 01b07c153736)
- issues: semantic_review_required, conflicting_sources:https://www.brookdalecc.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If a student’s or family financial situation has changed since filing the FAFSA, a student may request a Request for Special Circumstance Review.”
### `e90ce95f57f68e43` Brookdale Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.brookdalecc.edu/financial-aid/about-your-award/ (sha256 01b07c153736)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition: 5408.0 ⟵ “Tuition | $5,408.00 | $7,462.00 | $8,112.00”
  - with_parents_or_family:Books and Supplies: 2000.0 ⟵ “Books and Supplies | $2,000.00 | $2,000.00 | $2,000.00”
  - with_parents_or_family:Fees: 1190.0 ⟵ “Fees | $1,190.00 | $1,190.00 | $1,190.00”
  - with_parents_or_family:Personal Expenses: 8708.0 ⟵ “Personal Expenses | $8,708.00 | $8,708.00 | $8,708.00”
  - with_parents_or_family:Food and Housing: 10503.0 ⟵ “Food and Housing | $10,503.00 | $10,503.00 | $10,503.00”
  - with_parents_or_family:Transportation: 3204.0 ⟵ “Transportation | $3,204.00 | $3,204.00 | $3,204.00”
  - with_parents_or_family:Loan Fees: 60.0 ⟵ “Loan Fees | $60.00 | $60.00 | $60.00”
  - with_parents_or_family:Total Budget: 31073.0 ⟵ “Total Budget | $31,073.00 | $31,127.00 | $33,777.00”
  - with_parents_or_family:Tuition: 7462.0 ⟵ “Tuition | $5,408.00 | $7,462.00 | $8,112.00”
  - with_parents_or_family:Books and Supplies: 2000.0 ⟵ “Books and Supplies | $2,000.00 | $2,000.00 | $2,000.00”
  - with_parents_or_family:Fees: 1190.0 ⟵ “Fees | $1,190.00 | $1,190.00 | $1,190.00”
  - with_parents_or_family:Personal Expenses: 8708.0 ⟵ “Personal Expenses | $8,708.00 | $8,708.00 | $8,708.00”
  - with_parents_or_family:Food and Housing: 10503.0 ⟵ “Food and Housing | $10,503.00 | $10,503.00 | $10,503.00”
  - with_parents_or_family:Transportation: 3204.0 ⟵ “Transportation | $3,204.00 | $3,204.00 | $3,204.00”
  - with_parents_or_family:Loan Fees: 60.0 ⟵ “Loan Fees | $60.00 | $60.00 | $60.00”
  - with_parents_or_family:Total Budget: 31127.0 ⟵ “Total Budget | $31,073.00 | $31,127.00 | $33,777.00”
### `m0bf025553d050d5` Brookdale Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.brookdalecc.edu/documents/transfer-services/out-of-state/penn_college_tech_culinary_agreement.pdf (sha256 1b3577416c8e)
- issues: ambiguous_year_labels
- checks: {"fields": ["min_grade"], "merged_pages": 7}
  - min_grade: C ⟵ “Brookdale Community College applicants must have completed the courses to be transferred (see Part IV) with grades of C or higher.”
  - min_grade: C ⟵ “Only courses with earned grades of C or higher are eligible for transfer.”
  - min_grade: C ⟵ “Students must complete the courses in the specified associate degree program herein with a grade of C or better to receive the credits for transfer.”
  - min_grade: C ⟵ “To receive the transfer credit identified above, Brookdale Community College students must successfully complete the designated courses identified on the attached Program Checklists with individual course grades of “C” or better and a minimum cumulative Grade Point Average at the time of transfer of 2.0. 5.”
  - min_grade: C ⟵ “Monmouth University Agrees to: Monmouth University will award transfer credits for courses listed in the attached sequence chart in which Brookdale Community College students receive a grade of C (2.0) or better.”
  - min_grade: C ⟵ “Monmouth University Agrees to: Monmouth University will award transfer credits for courses listed in the attached sequence chart in which Brookdale Community College students receive a grade of C (2.0) or better.”
  - min_grade: C ⟵ “All courses for which a grade of C or higher was earned will be reviewed for transfer consideration.”
### `05668dc9e5b130e7` Caldwell University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.caldwell.edu/cost-aid/financial-aid/ (sha256 ed6fa578d8b7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency Override Worksheet A Financial Aid Administrator may authorize Dependency Status Override only if you thoroughly document extreme family circumstances.”
### `49a40fdbfe363290` Caldwell University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.caldwell.edu/cost-aid/financial-aid/ (sha256 ed6fa578d8b7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “These forms include Tax Return Transcripts, Verification of Non-Filing Status and W-2 requests. 2023-24 Tax Request forms 2021 Form 4506-T – Tax Return Transcript 2021 Form 4506-T – Verification of Non-Filing 2021 Form 4506-T – W-2 Request Verification of 2021 IRS Tax Return Information with Unusual Circumstances Special Circumstance Forms Request for Special Circumstance Review If you feel there ”
### `2e54707de2cab681` Centenary University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.centenaryuniversity.edu/consumer-information/satisfactory-academic-progress/ (sha256 b70cae08afa3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP appeals: If you are placed on financial aid suspension, you may request reinstatement of financial aid eligibility by sending an appeal to the Office of Financial Aid.”
### `4f563be898c259a6` Centenary University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.centenaryuniversity.edu/costs-and-aid/cost-of-attendance/ (sha256 5f4b40e4b463)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "rows": 7}
  - on_campus:UG Tuition: 19042 ⟵ “UG Tuition | $19,042 | $38,804”
  - on_campus:UG Fees: 774 ⟵ “UG Fees | $774 | $1,548”
  - on_campus:UG Books, Course Materials, Supplies, and Equipment: 500 ⟵ “UG Books, Course Materials, Supplies, and Equipment | $500 | $1,000”
  - on_campus:UG On Campus: 5020 ⟵ “UG On Campus | $5,020 | $10,040”
  - on_campus:UG On Campus Food: 2628 ⟵ “UG On Campus Food | $2,628 | $5,256”
  - on_campus:Personal and Living Expenses: 1653 ⟵ “Personal and Living Expenses | $1,653 | $3,306”
  - on_campus:Transportation on Campus: 327 ⟵ “Transportation on Campus | $327 | $654”
  - on_campus:UG Tuition: 38804 ⟵ “UG Tuition | $19,042 | $38,804”
  - on_campus:UG Fees: 1548 ⟵ “UG Fees | $774 | $1,548”
  - on_campus:UG Books, Course Materials, Supplies, and Equipment: 1000 ⟵ “UG Books, Course Materials, Supplies, and Equipment | $500 | $1,000”
  - on_campus:UG On Campus: 10040 ⟵ “UG On Campus | $5,020 | $10,040”
  - on_campus:UG On Campus Food: 5256 ⟵ “UG On Campus Food | $2,628 | $5,256”
  - on_campus:Personal and Living Expenses: 3306 ⟵ “Personal and Living Expenses | $1,653 | $3,306”
  - on_campus:Transportation on Campus: 654 ⟵ “Transportation on Campus | $327 | $654”
### `0419afc224ebfbbf` County College of Morris — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.ccm.edu/wp-content/uploads/2025/03/Financial-Aid-Cost-Card-2025.pdf (sha256 917ae33695fe)
- issues: arrangement_unlabeled, implausible_amount, residency_unknown, conflicting_sources:https://www.ccm.edu/wp-content/uploads/2026/02/Financial-Aid-Cost-Card-2026.pdf
- checks: {"columns": 3, "rows": 4}
  - column:Tuition: 173 ⟵ “Tuition | $173 | $317 | $443”
  - column:College Fee: 29 ⟵ “College Fee | $29 | $29 | $29”
  - column:Technology Fee: 35 ⟵ “Technology Fee | $35”
  - column:Registration Fee: 7 ⟵ “Registration Fee | $7”
  - column:Tuition: 317 ⟵ “Tuition | $173 | $317 | $443”
  - column:College Fee: 29 ⟵ “College Fee | $29 | $29 | $29”
  - column:Tuition: 443 ⟵ “Tuition | $173 | $317 | $443”
  - column:College Fee: 29 ⟵ “College Fee | $29 | $29 | $29”
### `229453cddf238630` County College of Morris — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.ccm.edu/wp-content/uploads/2026/02/Financial-Aid-Cost-Card-2026.pdf (sha256 8490d3e92cb6)
- issues: arrangement_unlabeled, implausible_amount, residency_unknown, conflicting_sources:https://www.ccm.edu/wp-content/uploads/2025/03/Financial-Aid-Cost-Card-2025.pdf
- checks: {"columns": 3, "rows": 4}
  - column:Tuition: 211 ⟵ “Tuition | $211 | $355 | $481”
  - column:College Fee: 30 ⟵ “College Fee | $30 | $30 | $30”
  - column:Technology Fee: 35 ⟵ “Technology Fee | $35”
  - column:Registration Fee: 7 ⟵ “Registration Fee | $7”
  - column:Tuition: 355 ⟵ “Tuition | $211 | $355 | $481”
  - column:College Fee: 30 ⟵ “College Fee | $30 | $30 | $30”
  - column:Tuition: 481 ⟵ “Tuition | $211 | $355 | $481”
  - column:College Fee: 30 ⟵ “College Fee | $30 | $30 | $30”
### `06909035e5b55335` Drew University — appeals 2027-28 [new] (labeled_in_source)
- source: https://drew.edu/admissions-and-aid/student-financial-services/financial-aid-scholarships/ (sha256 158489c05757)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Learn More Special/Unusual Circumstances (Undergraduate Financial Aid) Drew’s Financial Aid Office understands that students and families may at times experience unique situations.”
  - sentence: need_based_special_circumstances ⟵ “LEARN MORE Special Circumstances Special circumstances are financial situations that support a change to the cost of attendance or expected family contribution (SAI) calculation.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances include, but are not limited to: Human trafficking.”
  - sentence: need_based_special_circumstances ⟵ “Please note that unusual circumstances do not include: Parents’ refusal to contribute to student’s education.”
  - sentence: need_based_special_circumstances ⟵ “A Student may access the Unusual Circumstances Request Form by logging on to their TreeHouse.”
  - sentence: need_based_special_circumstances ⟵ “Adjustments A student may have both a special circumstances and an unusual circumstance.”
### `492bde81500ee68b` Drew University — appeals 2026-27 [new] (source_unlabeled)
- source: https://drew.edu/admissions-and-aid/student-financial-services/financial-aid-scholarships/how-to-apply-for-aid/verification-and-outstanding-requirements/ (sha256 aa69848c26c7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Securely upload your required documents Verification Documents Dependent Verification Worksheet Independent Verification Worksheet Unusual Enrollment Verification Form Special Circumstances Form Unusual Circumstances (Dependency Override) Form Alternative Application Affidavit Consortium Agreement Unusual Enrollment Directory Contact Us Maps & Directions Privacy Policy Notice of Nondiscrimination ”
### `87f48595d4bb489c` Drew University — appeals 2026-27 [new] (source_unlabeled)
- source: https://drew.edu/admissions-and-aid/student-financial-services/financial-aid-scholarships/faq/ (sha256 fdc0f1e770f0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “If you have extenuating circumstances, or the relationship between you and your parents has dissolved, you may be eligible for a Dependency Override.”
  - sentence: dependency_override ⟵ “Please call our office and request to speak with a financial aid counselor to see if you qualify for a Dependency Override.”
### `a0ba678d149a27ff` Drew University — appeals 2027-28 [new] (labeled_in_source)
- source: https://drew.edu/admissions-and-aid/student-financial-services/financial-aid-scholarships/ (sha256 158489c05757)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “A Professional Judgement may apply in such cases.”
### `6b511c36f94475a3` Drew University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://drew.edu/admissions-and-aid/student-financial-services/financial-aid-scholarships/cost-of-attendance/ (sha256 f3a5eb80fab8)
- issues: ambiguous_year_labels, components_do_not_reconcile, conflicting_sources:https://drew.edu/admissions-and-aid/student-financial-services/student-accounts/tuition-and-fees-schedules/
- checks: {"columns": 3, "components_reconcile": false, "rows": 13}
  - on_campus:Tuition: 45950.0 ⟵ “Tuition | $45,950.00 | $45,950.00 | $45,950.00”
  - on_campus:Fees: 1150.0 ⟵ “Fees | $1,150.00 | $1,150.00 | $1,150.00”
  - on_campus:Housing*: 11254.0 ⟵ “Housing* | $11,254.00 | $0.00 | $0.00”
  - on_campus:Food: 6386.0 ⟵ “Food | $6,386.00 | $0.00 | $0.00”
  - on_campus:sub total of direct charges*: 64740.0 ⟵ “sub total of direct charges* | $64,740.00 | $47,100.00 | $47,100.00”
  - on_campus:Housing: 0.0 ⟵ “Housing | $0.00 | $0 | $12,230.00”
  - on_campus:Food (2): 0.0 ⟵ “Food | $0.00 | $5,113 | $5,113.00”
  - on_campus:Books / Supplies: 1226.0 ⟵ “Books / Supplies | $1,226.00 | $1,226.00 | $1,226.00”
  - on_campus:Misc (incl. computer): 809.0 ⟵ “Misc (incl. computer) | $809.00 | $809.00 | $2,823.00”
  - on_campus:Transportation: 948.0 ⟵ “Transportation | $948.00 | $2,560.00 | $2,560.00”
  - on_campus:Pesonal Expenses: 2512.0 ⟵ “Pesonal Expenses | $2,512.00 | $2,512.00 | $2,512.00”
  - on_campus:Loan Fees: 55.0 ⟵ “Loan Fees | $55.00 | $55.00 | $55.00”
  - on_campus:Total: 69140.0 ⟵ “Total | $69,140.00 | $58,225.33 | $73,619.00”
  - with_parents_or_family:Tuition: 45950.0 ⟵ “Tuition | $45,950.00 | $45,950.00 | $45,950.00”
  - with_parents_or_family:Fees: 1150.0 ⟵ “Fees | $1,150.00 | $1,150.00 | $1,150.00”
  - with_parents_or_family:Housing*: 0.0 ⟵ “Housing* | $11,254.00 | $0.00 | $0.00”
  - with_parents_or_family:Food: 0.0 ⟵ “Food | $6,386.00 | $0.00 | $0.00”
  - with_parents_or_family:sub total of direct charges*: 47100.0 ⟵ “sub total of direct charges* | $64,740.00 | $47,100.00 | $47,100.00”
  - with_parents_or_family:Housing: 0 ⟵ “Housing | $0.00 | $0 | $12,230.00”
  - with_parents_or_family:Food (2): 5113 ⟵ “Food | $0.00 | $5,113 | $5,113.00”
  - with_parents_or_family:Books / Supplies: 1226.0 ⟵ “Books / Supplies | $1,226.00 | $1,226.00 | $1,226.00”
  - with_parents_or_family:Misc (incl. computer): 809.0 ⟵ “Misc (incl. computer) | $809.00 | $809.00 | $2,823.00”
  - with_parents_or_family:Transportation: 2560.0 ⟵ “Transportation | $948.00 | $2,560.00 | $2,560.00”
  - with_parents_or_family:Pesonal Expenses: 2512.0 ⟵ “Pesonal Expenses | $2,512.00 | $2,512.00 | $2,512.00”
  - with_parents_or_family:Loan Fees: 55.0 ⟵ “Loan Fees | $55.00 | $55.00 | $55.00”
  - … 14 more rows
### `9cb75e1ffeebbed1` Drew University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://drew.edu/admissions-and-aid/student-financial-services/student-accounts/tuition-and-fees-schedules/ (sha256 7f25dd8083cd)
- issues: conflicting_sources:https://drew.edu/admissions-and-aid/student-financial-services/financial-aid-scholarships/cost-of-attendance/
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (12-21 credits): 49550 ⟵ “Tuition (12-21 credits) | $ 24,775 | $ 49,550”
  - column:General Fee: 800 ⟵ “General Fee | $ 400 | $ 800”
  - column:Technology Fee: 350 ⟵ “Technology Fee | $ 175 | $ 350”
### `99aab96fd5fe4172` Drew University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://drew.edu/academic/office-of-the-registrar/transfer-credit/ (sha256 d498bdabafb0)
- issues: rows_without_score, conflicting_sources:https://drew.edu/academic/office-of-the-registrar/transfer-credit/
- checks: {"distinct_exams": 24, "equivalencies": 48, "rows_without_score": 48}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | SL | For a score of 5 or higher a student will receive four 100-level elective credits toward the major or minor with the gen ed attribute BNS. Students may take the tests for exemption from BIOL 150 and/or 160. | Student must take the placement test to determine course exemptions.”
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | HL | For a score of 5 or higher a student will receive credit for BIOL 150 and 160. | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business and Management | SL | For a score of 5 or higher a student will receive four 100-level elective credits toward the major or minor. | Student must contact the department chair to have the credits applied to the major or minor.”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business and Management | HL | For a score of 5 or higher a student will receive four 100-level elective credits toward the major or minor plus four Drew elective credits. | Student must contact the department chair to have the credits applied to the major or minor.”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | SL | For a score of 5 or higher, students will receive four elective credits. Students who scored 6 or higher and who wish to receive credit for CHEM 150 and/or CHEM 160 should consult with the department chair. | Students who wish to receive credit for CHEM 150 and/or CHEM 160 should co”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | HL | For a score of 5 or higher, students will receive eight elective credits. Students who scored 6 or higher and who wish to receive credit for CHEM 150 and/or CHEM 160 should consult with the department. | Students who wish to receive credit for CHEM 150 and/or CHEM 160 should consult”
  - equivalencies[IB-LATIN|None]:  ⟵ “Classic Languages (Greek, Latin) | SL | Score of 5 or better completes Drew’s language requirement and grants the student 4 credits in the language. | ”
  - equivalencies[IB-LATIN|None]:  ⟵ “Classic Languages (Greek, Latin) | HL | Score of 5 or better completes Drew’s language requirement and grants the student 8 credits in the language. | ”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | SL | For a score of 5 or higher, students will receive four elective credits. | Student must contact the department chair to determine if the course equivalency can be applied to the major or minor.”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | HL | For a score of 5 or higher, students will receive eight elective credits. | Student must contact the department chair to determine if the course equivalencies can be applied to the major or minor.”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | SL | For a score of 5 or higher a student will receive credit for ECON 101 or 102. | Student must contact their adviser if they prefer to have credit for ECON 102, otherwise credit for ECON 101 will be granted.”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | HL | For a score of 5 or higher a student will receive credit for ECON 101 and ECON 102. | ”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|None]:  ⟵ “Environmental Systems and Societies | SL | For a score of 5 or higher a student will receive credit for ESS 215. | ”
  - equivalencies[IB-FILM|None]:  ⟵ “Film | SL | For a score of 5 or higher a student will receive credit for ENGH 120. | ”
  - equivalencies[IB-FILM|None]:  ⟵ “Film | HL | For a score of 5 or higher a student will receive credit for ENGH 120 plus four elective credit. | ”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French Language & Literature A or French Language B | SL | Score of 5 or better in either Language & Literature A or Language B is the equivalent of FREN 201 and completes Drew’s language requirement. | ”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French Language & Literature A or French Language B | HL | Score of 5 or better in either Language & Literature A or Language B grants the student eight credits towards the completion of a minor or major in French. The student should still take the Drew Placement Test to determine appropriate course”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French Language ab initio (foreign language for beginners) | SL | The student should still take the Drew Placement Test to determine appropriate courses for completion of the minor or major. | ”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | HL | Score of 5 or better is the equivalent of ESS 189. | ”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German A Language and Literature | SL | Score of 5 or better is the equivalent of GERM 201 and completes Drew’s language requirement. | ”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German Language ab initio (foreign language for beginners) | SL | The student should still take the Drew Placement Test to determine appropriate courses for completion of the minor or major. | ”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German Language B | SL | Score of 5 or better is the equivalent of German 201 and completes Drew’s language requirement. | ”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German Language B (foreign language for experienced students) | HL | Score of 5 or better is the equivalent of German 201 and completes Drew’s language requirement. It also grants the student eight credits towards the completion of a minor or major in the language. The student should still take the ”
  - equivalencies[IB-GLOBAL-POLITICS|None]:  ⟵ “Global Politics | SL | For a score of 5 or higher a student will receive credit for PSCI 104. | ”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History | SL | For a score of 5 or higher a student will receive four credit for HIST 101, which fulfills the American History Survey requirement for the major, or HIST 189 which can be applied to the Global History requirement for the major. | Student must contact the department chair to have the c”
  - … 23 more rows
### `a65eb0514af69439` Drew University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://drew.edu/academic/office-of-the-registrar/transfer-credit/ (sha256 e67e4679ec2e)
- issues: rows_without_score, conflicting_sources:https://drew.edu/academic/office-of-the-registrar/transfer-credit/
- checks: {"distinct_exams": 24, "equivalencies": 62, "rows_without_score": 48}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | SL | For a score of 5 or higher a student will receive four 100-level elective credits toward the major or minor with the gen ed attribute BNS. Students may take the tests for exemption from BIOL 150 and/or 160. | Student must take the placement test to determine course exemptions.”
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | HL | For a score of 5 or higher a student will receive credit for BIOL 150 and 160. | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business and Management | SL | For a score of 5 or higher a student will receive four 100-level elective credits toward the major or minor. | Student must contact the department chair to have the credits applied to the major or minor.”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business and Management | HL | For a score of 5 or higher a student will receive four 100-level elective credits toward the major or minor plus four Drew elective credits. | Student must contact the department chair to have the credits applied to the major or minor.”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | SL | For a score of 5 or higher, students will receive four elective credits. Students who scored 6 or higher and who wish to receive credit for CHEM 150 and/or CHEM 160 should consult with the department chair. | Students who wish to receive credit for CHEM 150 and/or CHEM 160 should co”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | HL | For a score of 5 or higher, students will receive eight elective credits. Students who scored 6 or higher and who wish to receive credit for CHEM 150 and/or CHEM 160 should consult with the department. | Students who wish to receive credit for CHEM 150 and/or CHEM 160 should consult”
  - equivalencies[IB-LATIN|None]:  ⟵ “Classic Languages (Greek, Latin) | SL | Score of 5 or better completes Drew’s language requirement and grants the student 4 credits in the language. | ”
  - equivalencies[IB-LATIN|None]:  ⟵ “Classic Languages (Greek, Latin) | HL | Score of 5 or better completes Drew’s language requirement and grants the student 8 credits in the language. | ”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | SL | For a score of 5 or higher, students will receive four elective credits. | Student must contact the department chair to determine if the course equivalency can be applied to the major or minor.”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | HL | For a score of 5 or higher, students will receive eight elective credits. | Student must contact the department chair to determine if the course equivalencies can be applied to the major or minor.”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | SL | For a score of 5 or higher a student will receive credit for ECON 101 or 102. | Student must contact their adviser if they prefer to have credit for ECON 102, otherwise credit for ECON 101 will be granted.”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | HL | For a score of 5 or higher a student will receive credit for ECON 101 and ECON 102. | ”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|None]:  ⟵ “Environmental Systems and Societies | SL | For a score of 5 or higher a student will receive credit for ESS 215. | ”
  - equivalencies[IB-FILM|None]:  ⟵ “Film | SL | For a score of 5 or higher a student will receive credit for ENGH 120. | ”
  - equivalencies[IB-FILM|None]:  ⟵ “Film | HL | For a score of 5 or higher a student will receive credit for ENGH 120 plus four elective credit. | ”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French Language & Literature A or French Language B | SL | Score of 5 or better in either Language & Literature A or Language B is the equivalent of FREN 201 and completes Drew’s language requirement. | ”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French Language & Literature A or French Language B | HL | Score of 5 or better in either Language & Literature A or Language B grants the student eight credits towards the completion of a minor or major in French. The student should still take the Drew Placement Test to determine appropriate course”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French Language ab initio (foreign language for beginners) | SL | The student should still take the Drew Placement Test to determine appropriate courses for completion of the minor or major. | ”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | HL | Score of 5 or better is the equivalent of ESS 189. | ”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German A Language and Literature | SL | Score of 5 or better is the equivalent of GERM 201 and completes Drew’s language requirement. | ”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German Language ab initio (foreign language for beginners) | SL | The student should still take the Drew Placement Test to determine appropriate courses for completion of the minor or major. | ”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German Language B | SL | Score of 5 or better is the equivalent of German 201 and completes Drew’s language requirement. | ”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German Language B (foreign language for experienced students) | HL | Score of 5 or better is the equivalent of German 201 and completes Drew’s language requirement. It also grants the student eight credits towards the completion of a minor or major in the language. The student should still take the ”
  - equivalencies[IB-GLOBAL-POLITICS|None]:  ⟵ “Global Politics | SL | For a score of 5 or higher a student will receive credit for PSCI 104. | ”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History | SL | For a score of 5 or higher a student will receive four credit for HIST 101, which fulfills the American History Survey requirement for the major, or HIST 189 which can be applied to the Global History requirement for the major. | Student must contact the department chair to have the c”
  - … 37 more rows
### `271e8a3e0d2ac401` Essex County College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.essex.edu/wp-content/uploads/2026/01/4-Complete-SAP-2526.pdf (sha256 5918b7467726)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Section 3 - Financial Aid Application Procedures (Procedimientos de solicitud de ayuda financiera) Page (Página) - 3 SATISFACTORY ACADEMIC PROGRESS SUPPORTING DOCUMENTATION FOR APPEAL CIRCUMSTANCE(S) REQUIRED DOCUMENTATION EMPLOYMENT-RELATED RELACIONADOS CON EL EMPLEO Employer letter with effective dates(s) and whether the Required overtime and/or change in work schedule increase in hours was nece”
  - sentence: sap_appeal ⟵ “SUMMARY • Have a 2.0 GPA or better • Passing at least 67% of all courses attempted • Have not reached 150% time-frame of published academic program length • Failure • Fail at least one of the satisfactory academic progress standards • Submit appeal letter, if eligible.”
### `3252361e236326e8` Fairleigh Dickinson University-Florham Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fdu.edu/admissions/financial-aid/rights-responsibilities/undergraduate-academic-progress/ (sha256 2158d96f4c21)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “However, a student who fails to achieve SAP may submit an appeal.”
  - sentence: sap_appeal ⟵ “A SAP appeal must be submitted before the end of the add/drop period for the payment period for which the student is requesting financial aid.”
  - sentence: sap_appeal ⟵ “If at any point, the student fails to meet the terms of the academic plan, the student is again not making SAP but may appeal to be considered again for probation with a new academic plan.”
  - sentence: sap_appeal ⟵ “Regaining Aid Eligibility A student who has lost aid eligibility because he is not making satisfactory academic progress may regain eligibility by successfully appealing as described above or by completing a sufficient number of credits with a sufficient GPA to regain satisfactory academic progress without financial aid.”
  - sentence: sap_appeal ⟵ “If the student regains satisfactory academic progress without an appeal by completing additional credits without financial aid, the student should notify the financial aid office so that eligibility can be reinstated.”
### `cf0296010f7aa246` Fairleigh Dickinson University-Florham Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fdu.edu/admissions/financial-aid/rights-responsibilities/undergraduate-academic-progress/ (sha256 2158d96f4c21)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/financial-aid/undergraduate/professional-judgement/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Extenuating circumstances may include, but are not limited to serious illness or injury to the student, death or serious illness of an immediate family member, significant trauma in student’s life that impaired the student’s emotional and/or physical health, or other special circumstances.”
### `f79add0467b4a88e` Fairleigh Dickinson University-Florham Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fdu.edu/admissions/financial-aid/undergraduate/professional-judgement/ (sha256 f09c6605a354)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/financial-aid/rights-responsibilities/undergraduate-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Special circumstances are financial situations that support a change to the cost of attendance or expected family contribution (EFC) calculation.”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances include, but are not limited to: Changes in employment status, income, or assets.”
  - sentence: need_based_special_circumstances ⟵ “DOWNLOAD SPECIAL CIRCUMSTANCES REQUEST Unusual Circumstances Unusual Circumstances are conditions that support a change to a student’s dependency status based on a unique situation.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances include, but are not limited to: Human trafficking.”
  - sentence: need_based_special_circumstances ⟵ “Please note that unusual circumstances do not include: Parents’ refusal to contribute to students’ education.”
  - sentence: need_based_special_circumstances ⟵ “DOWNLOAD UNUSUAL CIRCUMSTANCES REQUEST Adjustments A student may have both a special circumstance and an unusual circumstance.”
### `2f5b0a0bc0d95d53` Fairleigh Dickinson University-Florham Campus — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.fdu.edu/admissions/tuition-fees/undergraduate-part-time/ (sha256 1837ae22b64b)
- issues: shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/tuition-fees/florham-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/metropolitan-campus-tuition-fees/,https://www.fdu.edu/wp-content/uploads/2026/05/PA-Website-Tuition-Chart-5.28.26.pdf
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - on_campus:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - on_campus:Housing: 10976 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - on_campus:Meals: 6118 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - on_campus:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 732 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - on_campus:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - on_campus:Total cost of attendance: 62888 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - with_parents_or_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - with_parents_or_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - with_parents_or_family:Housing: 1252 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - with_parents_or_family:Meals: 4070 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - with_parents_or_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - with_parents_or_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - with_parents_or_family:Total cost of attendance: 54042 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - off_campus_not_with_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - off_campus_not_with_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - off_campus_not_with_family:Housing: 16182 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - off_campus_not_with_family:Meals: 6256 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - off_campus_not_with_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - off_campus_not_with_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - off_campus_not_with_family:Total cost of attendance: 71158 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
### `36ab673bce01ed50` Fairleigh Dickinson University-Florham Campus — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fdu.edu/admissions/financial-aid/undergraduate/award-letter/ (sha256 ca5ccf82b09b)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition (Based on enrollment from 12-18 credits): 37364 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $37,364 | $37,364 | $37,364”
  - on_campus:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2192 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,192 | $2,192 | $2,192”
  - on_campus:Housing: 10868 ⟵ “Housing | $10,868 | $1,214 | $16,012”
  - on_campus:Meals: 5940 ⟵ “Meals | $5,940 | $3,936 | $6,040”
  - on_campus:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 708 ⟵ “Transportation | $708 | $3,538 | $3,538”
  - on_campus:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - on_campus:Total cost of attendance: 61414 ⟵ “Total cost of attendance | $61,414 | $52,586 | $69,488”
  - with_parents_or_family:Tuition (Based on enrollment from 12-18 credits): 37364 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $37,364 | $37,364 | $37,364”
  - with_parents_or_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2192 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,192 | $2,192 | $2,192”
  - with_parents_or_family:Housing: 1214 ⟵ “Housing | $10,868 | $1,214 | $16,012”
  - with_parents_or_family:Meals: 3936 ⟵ “Meals | $5,940 | $3,936 | $6,040”
  - with_parents_or_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3538 ⟵ “Transportation | $708 | $3,538 | $3,538”
  - with_parents_or_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - with_parents_or_family:Total cost of attendance: 52586 ⟵ “Total cost of attendance | $61,414 | $52,586 | $69,488”
  - off_campus_not_with_family:Tuition (Based on enrollment from 12-18 credits): 37364 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $37,364 | $37,364 | $37,364”
  - off_campus_not_with_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2192 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,192 | $2,192 | $2,192”
  - off_campus_not_with_family:Housing: 16012 ⟵ “Housing | $10,868 | $1,214 | $16,012”
  - off_campus_not_with_family:Meals: 6040 ⟵ “Meals | $5,940 | $3,936 | $6,040”
  - off_campus_not_with_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3538 ⟵ “Transportation | $708 | $3,538 | $3,538”
  - off_campus_not_with_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - off_campus_not_with_family:Total cost of attendance: 69488 ⟵ “Total cost of attendance | $61,414 | $52,586 | $69,488”
### `470d8e2e644fc2f7` Fairleigh Dickinson University-Florham Campus — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.fdu.edu/wp-content/uploads/2026/05/PA-Website-Tuition-Chart-5.28.26.pdf (sha256 c7446956a2f5)
- issues: arrangement_unlabeled, cost_period_semester, multiple_total_rows, shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/tuition-fees/florham-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/metropolitan-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/undergraduate-part-time/
- checks: {"columns": 8, "rows": 8}
  - column:Tuition: 21830 ⟵ “Tuition | $21,830**** | No Tuition | $21,830**** | $21,830**** | No Tuition | $21,830**** | $21,830**** | $109,150”
  - column:Fees: 1666 ⟵ “Fees | $1,666** | $1,666** | $1,666** | $1,666** | $1,666** | $8,330”
  - column:Total Estimated: 23496 ⟵ “Total Estimated | $23,496 | $23,496 | $23,496 | $23,496 | $23,496 | $117,480”
  - column:Room: 5980 ⟵ “Room | $5,980 | $4,500 | $5,980 | $5,980 | $4,500 | $5,980 | $5,980 | $38,900”
  - column:Board: 2511 ⟵ “Board | $2,511 | $1,125 | $2,511 | $2,511 | $1,125 | $2,511 | $2,511 | $14,805”
  - column:Transportation $1,860: 1300 ⟵ “Transportation $1,860 | $1,300 | $1,860 | $1,860 | $1,300 | $1,860 | $1,860 | $11,900”
  - column:Miscellaneous $3,153: 1637 ⟵ “Miscellaneous $3,153 | $1,637 | $3,153 | $3,153 | $1,637 | $3,153 | $3,153 | $19,039”
  - column:Total: 37000 ⟵ “Total | $37,000 | $8,562 | $37,000 | $37,000 | $8,562 | $37,000 | $37,000 | $202,124”
  - column:Fees: 1666 ⟵ “Fees | $1,666** | $1,666** | $1,666** | $1,666** | $1,666** | $8,330”
  - column:Total Estimated: 23496 ⟵ “Total Estimated | $23,496 | $23,496 | $23,496 | $23,496 | $23,496 | $117,480”
  - column:Room: 4500 ⟵ “Room | $5,980 | $4,500 | $5,980 | $5,980 | $4,500 | $5,980 | $5,980 | $38,900”
  - column:Board: 1125 ⟵ “Board | $2,511 | $1,125 | $2,511 | $2,511 | $1,125 | $2,511 | $2,511 | $14,805”
  - column:Transportation $1,860: 1860 ⟵ “Transportation $1,860 | $1,300 | $1,860 | $1,860 | $1,300 | $1,860 | $1,860 | $11,900”
  - column:Miscellaneous $3,153: 3153 ⟵ “Miscellaneous $3,153 | $1,637 | $3,153 | $3,153 | $1,637 | $3,153 | $3,153 | $19,039”
  - column:Total: 8562 ⟵ “Total | $37,000 | $8,562 | $37,000 | $37,000 | $8,562 | $37,000 | $37,000 | $202,124”
  - column:Tuition: 21830 ⟵ “Tuition | $21,830**** | No Tuition | $21,830**** | $21,830**** | No Tuition | $21,830**** | $21,830**** | $109,150”
  - column:Fees: 1666 ⟵ “Fees | $1,666** | $1,666** | $1,666** | $1,666** | $1,666** | $8,330”
  - column:Total Estimated: 23496 ⟵ “Total Estimated | $23,496 | $23,496 | $23,496 | $23,496 | $23,496 | $117,480”
  - column:Room: 5980 ⟵ “Room | $5,980 | $4,500 | $5,980 | $5,980 | $4,500 | $5,980 | $5,980 | $38,900”
  - column:Board: 2511 ⟵ “Board | $2,511 | $1,125 | $2,511 | $2,511 | $1,125 | $2,511 | $2,511 | $14,805”
  - column:Transportation $1,860: 1860 ⟵ “Transportation $1,860 | $1,300 | $1,860 | $1,860 | $1,300 | $1,860 | $1,860 | $11,900”
  - column:Miscellaneous $3,153: 3153 ⟵ “Miscellaneous $3,153 | $1,637 | $3,153 | $3,153 | $1,637 | $3,153 | $3,153 | $19,039”
  - column:Total: 8562 ⟵ “Total | $13, 504*** $8,562*** | $13, 504*** $13, 504 | $8,562*** | $13, 504*** | $13, 504*** | $84,644”
  - column:Total (2): 37000 ⟵ “Total | $37,000 | $8,562 | $37,000 | $37,000 | $8,562 | $37,000 | $37,000 | $202,124”
  - column:Tuition: 21830 ⟵ “Tuition | $21,830**** | No Tuition | $21,830**** | $21,830**** | No Tuition | $21,830**** | $21,830**** | $109,150”
  - … 33 more rows
### `52ea7b8939f436ad` Fairleigh Dickinson University-Florham Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fdu.edu/admissions/tuition-fees/metropolitan-campus-tuition-fees/ (sha256 33879586581d)
- issues: shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/tuition-fees/florham-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/undergraduate-part-time/,https://www.fdu.edu/wp-content/uploads/2026/05/PA-Website-Tuition-Chart-5.28.26.pdf
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - on_campus:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - on_campus:Housing: 10976 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - on_campus:Meals: 6118 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - on_campus:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 732 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - on_campus:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - on_campus:Total cost of attendance: 62888 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - with_parents_or_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - with_parents_or_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - with_parents_or_family:Housing: 1252 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - with_parents_or_family:Meals: 4070 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - with_parents_or_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - with_parents_or_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - with_parents_or_family:Total cost of attendance: 54042 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - off_campus_not_with_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - off_campus_not_with_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - off_campus_not_with_family:Housing: 16182 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - off_campus_not_with_family:Meals: 6256 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - off_campus_not_with_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - off_campus_not_with_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - off_campus_not_with_family:Total cost of attendance: 71158 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
### `91f5382d0b7dca4f` Fairleigh Dickinson University-Florham Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fdu.edu/admissions/tuition-fees/florham-campus-tuition-fees/ (sha256 a962783cf29a)
- issues: shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/tuition-fees/metropolitan-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/undergraduate-part-time/,https://www.fdu.edu/wp-content/uploads/2026/05/PA-Website-Tuition-Chart-5.28.26.pdf
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - on_campus:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - on_campus:Housing: 10976 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - on_campus:Meals: 6118 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - on_campus:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 732 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - on_campus:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - on_campus:Total cost of attendance: 62888 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - with_parents_or_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - with_parents_or_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - with_parents_or_family:Housing: 1252 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - with_parents_or_family:Meals: 4070 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - with_parents_or_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - with_parents_or_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - with_parents_or_family:Total cost of attendance: 54042 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - off_campus_not_with_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - off_campus_not_with_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - off_campus_not_with_family:Housing: 16182 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - off_campus_not_with_family:Meals: 6256 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - off_campus_not_with_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - off_campus_not_with_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - off_campus_not_with_family:Total cost of attendance: 71158 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
### `2c2f013f2c74ebe1` Fairleigh Dickinson University-Florham Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.fdu.edu/academics/academic-policies/international-baccalaureate-courses/ (sha256 0f4662db9a58)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 22, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[IB-THEATRE|5 or higher]:  ⟵ “Language and Performance | 5 or higher | THEAH 1103 | Intro to Theater | 3”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French | 5 | FREN 1101, 1102 | Elementary French I and II | 6”
  - equivalencies[IB-FRENCH|6]:  ⟵ “French | 6 | FREN 1101, 1102, 2103 | Elementary French I and II, and Intermediate French I | 9”
  - equivalencies[IB-FRENCH|7]:  ⟵ “French | 7 | FREN 1101, 1102, 2103, 2104 | Elementary French I and II, and Intermediate French I and II | 12”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German | 5 | GERM 1101, 1102 | Elementary German I and II | 6”
  - equivalencies[IB-GERMAN|6]:  ⟵ “German | 6 | GERM 1101, 1102, 2103 | Elementary German I and II, and Intermediate German I | 9”
  - equivalencies[IB-GERMAN|7]:  ⟵ “German | 7 | GERM 1101, 1102, 2103, 2104 | Elementary German I and II, and Intermediate German I and II | 12”
  - equivalencies[IB-LATIN|5]:  ⟵ “Latin | 5 | LATN 1101, 1102 | Elementary Latin I and II | 6”
  - equivalencies[IB-SPANISH|5]:  ⟵ “Spanish | 5 | SPAN 1101, 1102 | Elementary Spanish I and II | 6”
  - equivalencies[IB-SPANISH|6]:  ⟵ “Spanish | 6 | SPAN 1101, 1102, 2103 | Elementary Spanish I and II, and Intermediate Spanish I | 9”
  - equivalencies[IB-SPANISH|7]:  ⟵ “Spanish | 7 | SPAN 1101, 1102, 2103, 2104 | Elementary Spanish I and II, and Intermediate Spanish I and II | 12”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5 or higher]:  ⟵ “Business Management | 5 or higher | BUSI 1111 | Principles of Management | 3”
  - equivalencies[IB-ECONOMICS|5 or higher]:  ⟵ “Economics | 5 or higher | ECON 2001 | Intro to Microeconomics | 3”
  - equivalencies[IB-HISTORY|5 or higher]:  ⟵ “History | 5 or higher | HIST 1151 | World History Since 1500 | 3”
  - equivalencies[IB-PHILOSOPHY|5 or higher]:  ⟵ “Philosophy | 5 or higher | PHIL 1102 | Introduction to Philosophy | 3”
  - equivalencies[IB-PSYCHOLOGY|5 or higher]:  ⟵ “Psychology | 5 or higher | PSYC 1201 | General Psychology | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5 or higher]:  ⟵ “Social and Cultural Anthropology | 5 or higher | ANTH 1202 | Cultural Anthropology | 3”
  - equivalencies[IB-GEOGRAPHY|5 or higher]:  ⟵ “Geography | 5 or higher | GEOG 1102 | Geography and World Issues | 3”
  - equivalencies[IB-GLOBAL-POLITICS|5 or higher]:  ⟵ “Global Politics | 5 or higher | GOVT 1000 | Global Politics | 3”
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “Biology | 5 | BIOL 1201/1203 | Biological Diversity | 4”
  - equivalencies[IB-BIOLOGY|6 or higher]:  ⟵ “Biology | 6 or higher | BIOL 1202/1204 | Introduction to Molecules, Cells and Genes | 4”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM 1201/03 | General Chemistry I and Lab | 4”
  - equivalencies[IB-CHEMISTRY|6 or higher]:  ⟵ “Chemistry | 6 or higher | CHEM 1202/04 | General Chemistry II and Lab | 4”
  - equivalencies[IB-PHYSICS|5]:  ⟵ “Physics | 5 | PHYS 1001/1011 | General Physics I and Lab | 4”
  - equivalencies[IB-PHYSICS|6 or higher]:  ⟵ “Physics | 6 or higher | PHYS 1002/1012 | General Physics II and Lab | 4”
  - … 7 more rows
### `657ce1a5c623240a` Fairleigh Dickinson University-Florham Campus — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.fdu.edu/academics/academic-policies/clep-scores/ (sha256 9ed74c457105)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 34, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|55]:  ⟵ “Financial Accounting | ACCT 2021 Intro to Financial Accounting | 55 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | MIS 2101 Management Information Systems | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | LAW 2276 Business and the Law | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | MGMT 1111 Principkes of Management | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | MKTG 2030 Intro to Marketing Management | 50 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|60]:  ⟵ “American Literature | LITS 2301 American Literature I | 60 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | LITS 1100 Intro to Literary Analysis | 50 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | WRIT 1002 Composition I | 50 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|NA]:  ⟵ “College Composition Modular | No credits granted for this exam | NA | 0”
  - equivalencies[CLEP-ENGLISH-LITERATURE|60]:  ⟵ “English Literature | LITS 2101 British & European | 60 | 3”
  - equivalencies[CLEP-HUMANITIES|60]:  ⟵ “Humanities | HUMN 2201 Humanities Seminar | 60 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level 1 Proficiency | FREN 1001 Beginning French I | 50 | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level 1 Proficiency | GERM 1001 Beginning German I | 50 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1 Proficiency | SPAN 1001 Beginning Spanish I | 50 | 3”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing, Level 1 Proficiency | SPAN 1001 and SPAN 1007 Beginning Spanish I and Practicum | 50 | 4”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | GOVT 1000 American Government & Politics | 50 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | HIST 1130 The United States to 1877 | 50 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present | HIST 1131 The United States since 1877 | 50 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|NA]:  ⟵ “Human Growth and Development | No credits granted for this exam | NA | 0”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|60]:  ⟵ “Introduction to Educational Psychology | PSYC 3308 Educational Psychology | 60 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PSYC 1201 General Psychology | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | SOCI 1201 Introduction to Sociology | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | ECON 2002 Intro to Macroeconomics | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | ECON 2001 Intro to Microeconomics | 50 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | HIST 1000 Social Studies | 50 | 3”
  - … 9 more rows
### `a5f72563c9689950` Fairleigh Dickinson University-Florham Campus — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.fdu.edu/academics/academic-policies/ap-exam-scores/ (sha256 c2fad6ab332e)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 39, "equivalencies": 53, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | AFAM 1100: African American Studies | 3 | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4 or 5]:  ⟵ “African American Studies | AFAM 1100: African American Studies and AFAM 2010: The Black Diaspora | 4 or 5 | 6”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Art - Drawing | ART 1151: General Drawing I | 3 | 3”
  - equivalencies[AP-DRAWING|4 or 5]:  ⟵ “Studio Art - Drawing | ART 1151: General Drawing I, ART 1153: General Life Drawing I | 4 or 5 | 6”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | ARTH 1205: Art History Prehisto+B98ry to Medieval | 3 | 3”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History | ARTH 1205: Art History Prehistory to Medieval and ARTH 1206: Art History Renaissance through Today | 4 or 5 | 6”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2D Design | ART 1231: 2 Dimensional Design | 3 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|4 or 5]:  ⟵ “2D Design | ART 1231: 2 Dimensional Design and Art free elective | 4 or 5 | 6”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3D Design | ART 2233: 3-Dimensional Design | 3 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|4 or 5]:  ⟵ “3D Design | ART 2233: 3-Dimensional Design and ART 1315 Ceramics I | 4 or 5 | 6”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “AP Biology | BIOL 1233/1234/1235: Intro to Molecules, Cells, and Genes (Lecture, Recitation, Lab) | 4 | 4 credits”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “AP Biology | BIOL 1233/1234/1235: Intro to Molecules, Cells, and Genes (Lecture, Recitation, Lab) and BIOL 1000: AP Biology | 5 | 4 credits”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “Math/Calculus AB | Math 1203: Calculus I | 4 or 5 | 4 credits”
  - equivalencies[AP-CALCULUS-BC|3, 4, or 5]:  ⟵ “Math/Calculus BC (Test 2) | Math 1203: Calculus I; Math 2202: Calculus II | 3, 4, or 5 | 4 credits”
  - equivalencies[AP-RESEARCH|4 or 5]:  ⟵ “AP Research | WRIT 1003: Comp II Research and Argument | 4 or 5 | 3 credits”
  - equivalencies[AP-SEMINAR|3, 4, or 5]:  ⟵ “AP Seminar | WRIT 1800: AP Seminar | 3, 4, or 5 | 3 credits”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “AP Chemistry | CHEM 1201/1203/1211: General Chemistry I (Lecture, Lab, Recitation) | 4 or 5 | 4 credits”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | CHIN 1101: Elementary Chinese I | 3 | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Chinese Language and Culture | CHIN 1101: Elementary Chinese I; CHIN 1102: Elementary Chinese II | 4 or 5 | 6”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, or 5]:  ⟵ “Computer Science A | CSCI 1201: Computer Programming I | 3, 4, or 5 | 3 credits”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, or 5]:  ⟵ “Computer Science Principles | CSCI 1145: Computer Science Fundamentals | 3, 4, or 5 | 3 credits”
  - equivalencies[AP-MICROECONOMICS|4 or 5]:  ⟵ “Micro | ECON 2001: Introduction to Microeconomics | 4 or 5 | 3 credits”
  - equivalencies[AP-MACROECONOMICS|4 or 5]:  ⟵ “Macro | ECON 2102: Introduction to Macroeconomics | 4 or 5 | 3 credits”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4 or 5]:  ⟵ “Environmental Science | ENVR 1000: Environmental Science | 4 or 5 | 4 credits”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4 or 5]:  ⟵ “English Language and Composition | WRIT 1002: Composition I: Rhetoric & Inquiry | 4 or 5 | 3 credits”
  - … 28 more rows
### `0b86702f5c6a1beb` Fairleigh Dickinson University-Metropolitan Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fdu.edu/admissions/financial-aid/undergraduate/professional-judgement/ (sha256 67afec925aae)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/financial-aid/rights-responsibilities/undergraduate-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Special circumstances are financial situations that support a change to the cost of attendance or expected family contribution (EFC) calculation.”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances include, but are not limited to: Changes in employment status, income, or assets.”
  - sentence: need_based_special_circumstances ⟵ “DOWNLOAD SPECIAL CIRCUMSTANCES REQUEST Unusual Circumstances Unusual Circumstances are conditions that support a change to a student’s dependency status based on a unique situation.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances include, but are not limited to: Human trafficking.”
  - sentence: need_based_special_circumstances ⟵ “Please note that unusual circumstances do not include: Parents’ refusal to contribute to students’ education.”
  - sentence: need_based_special_circumstances ⟵ “DOWNLOAD UNUSUAL CIRCUMSTANCES REQUEST Adjustments A student may have both a special circumstance and an unusual circumstance.”
### `8e004c4dca7afa07` Fairleigh Dickinson University-Metropolitan Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fdu.edu/admissions/financial-aid/rights-responsibilities/undergraduate-academic-progress/ (sha256 2158d96f4c21)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “However, a student who fails to achieve SAP may submit an appeal.”
  - sentence: sap_appeal ⟵ “A SAP appeal must be submitted before the end of the add/drop period for the payment period for which the student is requesting financial aid.”
  - sentence: sap_appeal ⟵ “If at any point, the student fails to meet the terms of the academic plan, the student is again not making SAP but may appeal to be considered again for probation with a new academic plan.”
  - sentence: sap_appeal ⟵ “Regaining Aid Eligibility A student who has lost aid eligibility because he is not making satisfactory academic progress may regain eligibility by successfully appealing as described above or by completing a sufficient number of credits with a sufficient GPA to regain satisfactory academic progress without financial aid.”
  - sentence: sap_appeal ⟵ “If the student regains satisfactory academic progress without an appeal by completing additional credits without financial aid, the student should notify the financial aid office so that eligibility can be reinstated.”
### `f2526d870e544d92` Fairleigh Dickinson University-Metropolitan Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fdu.edu/admissions/financial-aid/rights-responsibilities/undergraduate-academic-progress/ (sha256 2158d96f4c21)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/financial-aid/undergraduate/professional-judgement/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Extenuating circumstances may include, but are not limited to serious illness or injury to the student, death or serious illness of an immediate family member, significant trauma in student’s life that impaired the student’s emotional and/or physical health, or other special circumstances.”
### `01e33bb9dd82e89b` Fairleigh Dickinson University-Metropolitan Campus — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fdu.edu/admissions/financial-aid/undergraduate/award-letter/ (sha256 ca5ccf82b09b)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition (Based on enrollment from 12-18 credits): 37364 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $37,364 | $37,364 | $37,364”
  - on_campus:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2192 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,192 | $2,192 | $2,192”
  - on_campus:Housing: 10868 ⟵ “Housing | $10,868 | $1,214 | $16,012”
  - on_campus:Meals: 5940 ⟵ “Meals | $5,940 | $3,936 | $6,040”
  - on_campus:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 708 ⟵ “Transportation | $708 | $3,538 | $3,538”
  - on_campus:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - on_campus:Total cost of attendance: 61414 ⟵ “Total cost of attendance | $61,414 | $52,586 | $69,488”
  - with_parents_or_family:Tuition (Based on enrollment from 12-18 credits): 37364 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $37,364 | $37,364 | $37,364”
  - with_parents_or_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2192 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,192 | $2,192 | $2,192”
  - with_parents_or_family:Housing: 1214 ⟵ “Housing | $10,868 | $1,214 | $16,012”
  - with_parents_or_family:Meals: 3936 ⟵ “Meals | $5,940 | $3,936 | $6,040”
  - with_parents_or_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3538 ⟵ “Transportation | $708 | $3,538 | $3,538”
  - with_parents_or_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - with_parents_or_family:Total cost of attendance: 52586 ⟵ “Total cost of attendance | $61,414 | $52,586 | $69,488”
  - off_campus_not_with_family:Tuition (Based on enrollment from 12-18 credits): 37364 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $37,364 | $37,364 | $37,364”
  - off_campus_not_with_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2192 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,192 | $2,192 | $2,192”
  - off_campus_not_with_family:Housing: 16012 ⟵ “Housing | $10,868 | $1,214 | $16,012”
  - off_campus_not_with_family:Meals: 6040 ⟵ “Meals | $5,940 | $3,936 | $6,040”
  - off_campus_not_with_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3538 ⟵ “Transportation | $708 | $3,538 | $3,538”
  - off_campus_not_with_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - off_campus_not_with_family:Total cost of attendance: 69488 ⟵ “Total cost of attendance | $61,414 | $52,586 | $69,488”
### `413787882b150a74` Fairleigh Dickinson University-Metropolitan Campus — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.fdu.edu/wp-content/uploads/2026/05/PA-Website-Tuition-Chart-5.28.26.pdf (sha256 c7446956a2f5)
- issues: arrangement_unlabeled, cost_period_semester, multiple_total_rows, shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/tuition-fees/florham-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/metropolitan-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/undergraduate-part-time/
- checks: {"columns": 8, "rows": 8}
  - column:Tuition: 21830 ⟵ “Tuition | $21,830**** | No Tuition | $21,830**** | $21,830**** | No Tuition | $21,830**** | $21,830**** | $109,150”
  - column:Fees: 1666 ⟵ “Fees | $1,666** | $1,666** | $1,666** | $1,666** | $1,666** | $8,330”
  - column:Total Estimated: 23496 ⟵ “Total Estimated | $23,496 | $23,496 | $23,496 | $23,496 | $23,496 | $117,480”
  - column:Room: 5980 ⟵ “Room | $5,980 | $4,500 | $5,980 | $5,980 | $4,500 | $5,980 | $5,980 | $38,900”
  - column:Board: 2511 ⟵ “Board | $2,511 | $1,125 | $2,511 | $2,511 | $1,125 | $2,511 | $2,511 | $14,805”
  - column:Transportation $1,860: 1300 ⟵ “Transportation $1,860 | $1,300 | $1,860 | $1,860 | $1,300 | $1,860 | $1,860 | $11,900”
  - column:Miscellaneous $3,153: 1637 ⟵ “Miscellaneous $3,153 | $1,637 | $3,153 | $3,153 | $1,637 | $3,153 | $3,153 | $19,039”
  - column:Total: 37000 ⟵ “Total | $37,000 | $8,562 | $37,000 | $37,000 | $8,562 | $37,000 | $37,000 | $202,124”
  - column:Fees: 1666 ⟵ “Fees | $1,666** | $1,666** | $1,666** | $1,666** | $1,666** | $8,330”
  - column:Total Estimated: 23496 ⟵ “Total Estimated | $23,496 | $23,496 | $23,496 | $23,496 | $23,496 | $117,480”
  - column:Room: 4500 ⟵ “Room | $5,980 | $4,500 | $5,980 | $5,980 | $4,500 | $5,980 | $5,980 | $38,900”
  - column:Board: 1125 ⟵ “Board | $2,511 | $1,125 | $2,511 | $2,511 | $1,125 | $2,511 | $2,511 | $14,805”
  - column:Transportation $1,860: 1860 ⟵ “Transportation $1,860 | $1,300 | $1,860 | $1,860 | $1,300 | $1,860 | $1,860 | $11,900”
  - column:Miscellaneous $3,153: 3153 ⟵ “Miscellaneous $3,153 | $1,637 | $3,153 | $3,153 | $1,637 | $3,153 | $3,153 | $19,039”
  - column:Total: 8562 ⟵ “Total | $37,000 | $8,562 | $37,000 | $37,000 | $8,562 | $37,000 | $37,000 | $202,124”
  - column:Tuition: 21830 ⟵ “Tuition | $21,830**** | No Tuition | $21,830**** | $21,830**** | No Tuition | $21,830**** | $21,830**** | $109,150”
  - column:Fees: 1666 ⟵ “Fees | $1,666** | $1,666** | $1,666** | $1,666** | $1,666** | $8,330”
  - column:Total Estimated: 23496 ⟵ “Total Estimated | $23,496 | $23,496 | $23,496 | $23,496 | $23,496 | $117,480”
  - column:Room: 5980 ⟵ “Room | $5,980 | $4,500 | $5,980 | $5,980 | $4,500 | $5,980 | $5,980 | $38,900”
  - column:Board: 2511 ⟵ “Board | $2,511 | $1,125 | $2,511 | $2,511 | $1,125 | $2,511 | $2,511 | $14,805”
  - column:Transportation $1,860: 1860 ⟵ “Transportation $1,860 | $1,300 | $1,860 | $1,860 | $1,300 | $1,860 | $1,860 | $11,900”
  - column:Miscellaneous $3,153: 3153 ⟵ “Miscellaneous $3,153 | $1,637 | $3,153 | $3,153 | $1,637 | $3,153 | $3,153 | $19,039”
  - column:Total: 8562 ⟵ “Total | $13, 504*** $8,562*** | $13, 504*** $13, 504 | $8,562*** | $13, 504*** | $13, 504*** | $84,644”
  - column:Total (2): 37000 ⟵ “Total | $37,000 | $8,562 | $37,000 | $37,000 | $8,562 | $37,000 | $37,000 | $202,124”
  - column:Tuition: 21830 ⟵ “Tuition | $21,830**** | No Tuition | $21,830**** | $21,830**** | No Tuition | $21,830**** | $21,830**** | $109,150”
  - … 33 more rows
### `e1b829031f678105` Fairleigh Dickinson University-Metropolitan Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fdu.edu/admissions/tuition-fees/metropolitan-campus-tuition-fees/ (sha256 33879586581d)
- issues: shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/tuition-fees/florham-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/undergraduate-part-time/,https://www.fdu.edu/wp-content/uploads/2026/05/PA-Website-Tuition-Chart-5.28.26.pdf
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - on_campus:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - on_campus:Housing: 10976 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - on_campus:Meals: 6118 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - on_campus:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 732 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - on_campus:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - on_campus:Total cost of attendance: 62888 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - with_parents_or_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - with_parents_or_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - with_parents_or_family:Housing: 1252 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - with_parents_or_family:Meals: 4070 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - with_parents_or_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - with_parents_or_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - with_parents_or_family:Total cost of attendance: 54042 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - off_campus_not_with_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - off_campus_not_with_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - off_campus_not_with_family:Housing: 16182 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - off_campus_not_with_family:Meals: 6256 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - off_campus_not_with_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - off_campus_not_with_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - off_campus_not_with_family:Total cost of attendance: 71158 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
### `e97c8906986e90c8` Fairleigh Dickinson University-Metropolitan Campus — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.fdu.edu/admissions/tuition-fees/undergraduate-part-time/ (sha256 1837ae22b64b)
- issues: shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/tuition-fees/florham-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/metropolitan-campus-tuition-fees/,https://www.fdu.edu/wp-content/uploads/2026/05/PA-Website-Tuition-Chart-5.28.26.pdf
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - on_campus:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - on_campus:Housing: 10976 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - on_campus:Meals: 6118 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - on_campus:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 732 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - on_campus:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - on_campus:Total cost of attendance: 62888 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - with_parents_or_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - with_parents_or_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - with_parents_or_family:Housing: 1252 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - with_parents_or_family:Meals: 4070 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - with_parents_or_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - with_parents_or_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - with_parents_or_family:Total cost of attendance: 54042 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - off_campus_not_with_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - off_campus_not_with_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - off_campus_not_with_family:Housing: 16182 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - off_campus_not_with_family:Meals: 6256 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - off_campus_not_with_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - off_campus_not_with_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - off_campus_not_with_family:Total cost of attendance: 71158 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
### `f3ce0e1161f557c7` Fairleigh Dickinson University-Metropolitan Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fdu.edu/admissions/tuition-fees/florham-campus-tuition-fees/ (sha256 a962783cf29a)
- issues: shared_site_attribution_review, conflicting_sources:https://www.fdu.edu/admissions/tuition-fees/metropolitan-campus-tuition-fees/,https://www.fdu.edu/admissions/tuition-fees/undergraduate-part-time/,https://www.fdu.edu/wp-content/uploads/2026/05/PA-Website-Tuition-Chart-5.28.26.pdf
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - on_campus:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - on_campus:Housing: 10976 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - on_campus:Meals: 6118 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - on_campus:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 732 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - on_campus:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - on_campus:Total cost of attendance: 62888 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - with_parents_or_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - with_parents_or_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - with_parents_or_family:Housing: 1252 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - with_parents_or_family:Meals: 4070 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - with_parents_or_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - with_parents_or_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - with_parents_or_family:Total cost of attendance: 54042 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
  - off_campus_not_with_family:Tuition (Based on enrollment from 12-18 credits): 38600 ⟵ “Tuition (Based on enrollment from 12-18 credits) | $38,600 | $38,600 | $38,600”
  - off_campus_not_with_family:Standard Fees (Technology fee, wellness fee, and one-time new student fee): 2120 ⟵ “Standard Fees (Technology fee, wellness fee, and one-time new student fee) | $2,120 | $2,120 | $2,120”
  - off_campus_not_with_family:Housing: 16182 ⟵ “Housing | $10,976 | $1,252 | $16,182”
  - off_campus_not_with_family:Meals: 6256 ⟵ “Meals | $6,118 | $4,070 | $6,256”
  - off_campus_not_with_family:Books and supplies: 1290 ⟵ “Books and supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3658 ⟵ “Transportation | $732 | $3,658 | $3,658”
  - off_campus_not_with_family:Miscellaneous: 3052 ⟵ “Miscellaneous | $3,052 | $3,052 | $3,052”
  - off_campus_not_with_family:Total cost of attendance: 71158 ⟵ “Total cost of attendance | $62,888 | $54,042 | $71,158”
### `0a9ba3bdcce1f12e` Fairleigh Dickinson University-Metropolitan Campus — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.fdu.edu/academics/academic-policies/clep-scores/ (sha256 9ed74c457105)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 34, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|55]:  ⟵ “Financial Accounting | ACCT 2021 Intro to Financial Accounting | 55 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | MIS 2101 Management Information Systems | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | LAW 2276 Business and the Law | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | MGMT 1111 Principkes of Management | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | MKTG 2030 Intro to Marketing Management | 50 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|60]:  ⟵ “American Literature | LITS 2301 American Literature I | 60 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | LITS 1100 Intro to Literary Analysis | 50 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | WRIT 1002 Composition I | 50 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|NA]:  ⟵ “College Composition Modular | No credits granted for this exam | NA | 0”
  - equivalencies[CLEP-ENGLISH-LITERATURE|60]:  ⟵ “English Literature | LITS 2101 British & European | 60 | 3”
  - equivalencies[CLEP-HUMANITIES|60]:  ⟵ “Humanities | HUMN 2201 Humanities Seminar | 60 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level 1 Proficiency | FREN 1001 Beginning French I | 50 | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level 1 Proficiency | GERM 1001 Beginning German I | 50 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1 Proficiency | SPAN 1001 Beginning Spanish I | 50 | 3”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing, Level 1 Proficiency | SPAN 1001 and SPAN 1007 Beginning Spanish I and Practicum | 50 | 4”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | GOVT 1000 American Government & Politics | 50 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | HIST 1130 The United States to 1877 | 50 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present | HIST 1131 The United States since 1877 | 50 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|NA]:  ⟵ “Human Growth and Development | No credits granted for this exam | NA | 0”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|60]:  ⟵ “Introduction to Educational Psychology | PSYC 3308 Educational Psychology | 60 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PSYC 1201 General Psychology | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | SOCI 1201 Introduction to Sociology | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | ECON 2002 Intro to Macroeconomics | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | ECON 2001 Intro to Microeconomics | 50 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | HIST 1000 Social Studies | 50 | 3”
  - … 9 more rows
### `ae5d5467d1851983` Fairleigh Dickinson University-Metropolitan Campus — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.fdu.edu/academics/academic-policies/ap-exam-scores/ (sha256 c2fad6ab332e)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 39, "equivalencies": 53, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | AFAM 1100: African American Studies | 3 | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4 or 5]:  ⟵ “African American Studies | AFAM 1100: African American Studies and AFAM 2010: The Black Diaspora | 4 or 5 | 6”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Art - Drawing | ART 1151: General Drawing I | 3 | 3”
  - equivalencies[AP-DRAWING|4 or 5]:  ⟵ “Studio Art - Drawing | ART 1151: General Drawing I, ART 1153: General Life Drawing I | 4 or 5 | 6”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | ARTH 1205: Art History Prehisto+B98ry to Medieval | 3 | 3”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History | ARTH 1205: Art History Prehistory to Medieval and ARTH 1206: Art History Renaissance through Today | 4 or 5 | 6”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2D Design | ART 1231: 2 Dimensional Design | 3 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|4 or 5]:  ⟵ “2D Design | ART 1231: 2 Dimensional Design and Art free elective | 4 or 5 | 6”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3D Design | ART 2233: 3-Dimensional Design | 3 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|4 or 5]:  ⟵ “3D Design | ART 2233: 3-Dimensional Design and ART 1315 Ceramics I | 4 or 5 | 6”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “AP Biology | BIOL 1233/1234/1235: Intro to Molecules, Cells, and Genes (Lecture, Recitation, Lab) | 4 | 4 credits”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “AP Biology | BIOL 1233/1234/1235: Intro to Molecules, Cells, and Genes (Lecture, Recitation, Lab) and BIOL 1000: AP Biology | 5 | 4 credits”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “Math/Calculus AB | Math 1203: Calculus I | 4 or 5 | 4 credits”
  - equivalencies[AP-CALCULUS-BC|3, 4, or 5]:  ⟵ “Math/Calculus BC (Test 2) | Math 1203: Calculus I; Math 2202: Calculus II | 3, 4, or 5 | 4 credits”
  - equivalencies[AP-RESEARCH|4 or 5]:  ⟵ “AP Research | WRIT 1003: Comp II Research and Argument | 4 or 5 | 3 credits”
  - equivalencies[AP-SEMINAR|3, 4, or 5]:  ⟵ “AP Seminar | WRIT 1800: AP Seminar | 3, 4, or 5 | 3 credits”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “AP Chemistry | CHEM 1201/1203/1211: General Chemistry I (Lecture, Lab, Recitation) | 4 or 5 | 4 credits”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | CHIN 1101: Elementary Chinese I | 3 | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Chinese Language and Culture | CHIN 1101: Elementary Chinese I; CHIN 1102: Elementary Chinese II | 4 or 5 | 6”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, or 5]:  ⟵ “Computer Science A | CSCI 1201: Computer Programming I | 3, 4, or 5 | 3 credits”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, or 5]:  ⟵ “Computer Science Principles | CSCI 1145: Computer Science Fundamentals | 3, 4, or 5 | 3 credits”
  - equivalencies[AP-MICROECONOMICS|4 or 5]:  ⟵ “Micro | ECON 2001: Introduction to Microeconomics | 4 or 5 | 3 credits”
  - equivalencies[AP-MACROECONOMICS|4 or 5]:  ⟵ “Macro | ECON 2102: Introduction to Macroeconomics | 4 or 5 | 3 credits”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4 or 5]:  ⟵ “Environmental Science | ENVR 1000: Environmental Science | 4 or 5 | 4 credits”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4 or 5]:  ⟵ “English Language and Composition | WRIT 1002: Composition I: Rhetoric & Inquiry | 4 or 5 | 3 credits”
  - … 28 more rows
### `e5b3c80543f7d25d` Fairleigh Dickinson University-Metropolitan Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.fdu.edu/academics/academic-policies/international-baccalaureate-courses/ (sha256 0f4662db9a58)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 22, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[IB-THEATRE|5 or higher]:  ⟵ “Language and Performance | 5 or higher | THEAH 1103 | Intro to Theater | 3”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French | 5 | FREN 1101, 1102 | Elementary French I and II | 6”
  - equivalencies[IB-FRENCH|6]:  ⟵ “French | 6 | FREN 1101, 1102, 2103 | Elementary French I and II, and Intermediate French I | 9”
  - equivalencies[IB-FRENCH|7]:  ⟵ “French | 7 | FREN 1101, 1102, 2103, 2104 | Elementary French I and II, and Intermediate French I and II | 12”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German | 5 | GERM 1101, 1102 | Elementary German I and II | 6”
  - equivalencies[IB-GERMAN|6]:  ⟵ “German | 6 | GERM 1101, 1102, 2103 | Elementary German I and II, and Intermediate German I | 9”
  - equivalencies[IB-GERMAN|7]:  ⟵ “German | 7 | GERM 1101, 1102, 2103, 2104 | Elementary German I and II, and Intermediate German I and II | 12”
  - equivalencies[IB-LATIN|5]:  ⟵ “Latin | 5 | LATN 1101, 1102 | Elementary Latin I and II | 6”
  - equivalencies[IB-SPANISH|5]:  ⟵ “Spanish | 5 | SPAN 1101, 1102 | Elementary Spanish I and II | 6”
  - equivalencies[IB-SPANISH|6]:  ⟵ “Spanish | 6 | SPAN 1101, 1102, 2103 | Elementary Spanish I and II, and Intermediate Spanish I | 9”
  - equivalencies[IB-SPANISH|7]:  ⟵ “Spanish | 7 | SPAN 1101, 1102, 2103, 2104 | Elementary Spanish I and II, and Intermediate Spanish I and II | 12”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5 or higher]:  ⟵ “Business Management | 5 or higher | BUSI 1111 | Principles of Management | 3”
  - equivalencies[IB-ECONOMICS|5 or higher]:  ⟵ “Economics | 5 or higher | ECON 2001 | Intro to Microeconomics | 3”
  - equivalencies[IB-HISTORY|5 or higher]:  ⟵ “History | 5 or higher | HIST 1151 | World History Since 1500 | 3”
  - equivalencies[IB-PHILOSOPHY|5 or higher]:  ⟵ “Philosophy | 5 or higher | PHIL 1102 | Introduction to Philosophy | 3”
  - equivalencies[IB-PSYCHOLOGY|5 or higher]:  ⟵ “Psychology | 5 or higher | PSYC 1201 | General Psychology | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5 or higher]:  ⟵ “Social and Cultural Anthropology | 5 or higher | ANTH 1202 | Cultural Anthropology | 3”
  - equivalencies[IB-GEOGRAPHY|5 or higher]:  ⟵ “Geography | 5 or higher | GEOG 1102 | Geography and World Issues | 3”
  - equivalencies[IB-GLOBAL-POLITICS|5 or higher]:  ⟵ “Global Politics | 5 or higher | GOVT 1000 | Global Politics | 3”
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “Biology | 5 | BIOL 1201/1203 | Biological Diversity | 4”
  - equivalencies[IB-BIOLOGY|6 or higher]:  ⟵ “Biology | 6 or higher | BIOL 1202/1204 | Introduction to Molecules, Cells and Genes | 4”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM 1201/03 | General Chemistry I and Lab | 4”
  - equivalencies[IB-CHEMISTRY|6 or higher]:  ⟵ “Chemistry | 6 or higher | CHEM 1202/04 | General Chemistry II and Lab | 4”
  - equivalencies[IB-PHYSICS|5]:  ⟵ “Physics | 5 | PHYS 1001/1011 | General Physics I and Lab | 4”
  - equivalencies[IB-PHYSICS|6 or higher]:  ⟵ “Physics | 6 or higher | PHYS 1002/1012 | General Physics II and Lab | 4”
  - … 7 more rows
### `49205bd19b5d99c8` Felician University — appeals 2026-27 [new] (source_unlabeled)
- source: https://felician.edu/admissions/student-financial-services/satisfactory-academic-progress-sap/ (sha256 f5f8810272ba)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Evaluation of one or more of the following conditions may result in reinstatement of financial aid: Exceptional medical or personal circumstances Personal injury or illness of the student Family difficulties, such as divorce or family illness Death of a relative Other unusual circumstances Appeal process Students must submit an ‘Appeal Form to Reinstate Financial Assistance’ available in the Finan”
### `9a94f9e6a491ff77` Felician University — appeals 2026-27 [new] (source_unlabeled)
- source: https://felician.edu/admissions/student-financial-services/satisfactory-academic-progress-sap/ (sha256 f5f8810272ba)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “An appeal will be reviewed by the SAP Appeals Committee which is comprised of multidisciplinary members of the staff and faculty.”
  - sentence: sap_appeal ⟵ “Appeal requests submitted after the deadline will not be accepted if the SAP Appeals Committee has met for the final time prior to the start of classes.”
  - sentence: sap_appeal ⟵ “Reinstatement of aid for the following semester will be considered by the SAP Appeals Committee after a review of the student’s academic progress and/or successful completion of the ‘academic plan’.”
  - sentence: sap_appeal ⟵ “All decisions made by the SAP Appeals Committee are final.”
  - sentence: sap_appeal ⟵ “Financial aid probation A student who is failing to make satisfactory academic progress whose appeal is approved by the appeals committee will be placed on ‘financial aid probation’.”
### `39e9d54f9aa24aa5` Felician University — awards 2025-26 [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/scholarships-and-grants/ (sha256 3b8fe20e7666)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $20,000 ⟵ “Felician Scholarship | 3.50 – 3.99 GPA | $20,000”
  - eligibility_summary: 3.50 – 3.99 GPA ⟵ “Felician Scholarship | 3.50 – 3.99 GPA | $20,000”
### `40927f2907924755` Felician University — awards 2025-26 [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/scholarships-and-grants/ (sha256 3b8fe20e7666)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $8,000 ⟵ “Falcon Grant | Below 2.29 GPA | $8,000”
  - eligibility_summary: Below 2.29 GPA ⟵ “Falcon Grant | Below 2.29 GPA | $8,000”
### `85dfec4f569a9b7e` Felician University — awards 2025-26 [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/scholarships-and-grants/ (sha256 3b8fe20e7666)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “St. Francis Scholarship | Must be graduate from Clifton High School | $2,500”
  - eligibility_summary: Must be graduate from Clifton High School ⟵ “St. Francis Scholarship | Must be graduate from Clifton High School | $2,500”
### `b54b804c48688004` Felician University — awards 2025-26 [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/scholarships-and-grants/ (sha256 3b8fe20e7666)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $22,000 ⟵ “Presidential Scholarship | 4.0 + GPA | $22,000”
  - eligibility_summary: 4.0 + GPA ⟵ “Presidential Scholarship | 4.0 + GPA | $22,000”
### `bff45ac12bf250e6` Felician University — awards 2025-26 [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/scholarships-and-grants/ (sha256 3b8fe20e7666)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “Franciscan Scholarship | 2.30 – 2.89 GPA | $14,000”
  - eligibility_summary: 2.30 – 2.89 GPA ⟵ “Franciscan Scholarship | 2.30 – 2.89 GPA | $14,000”
### `ce73ddb26e25ab1e` Felician University — awards 2025-26 [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/scholarships-and-grants/ (sha256 3b8fe20e7666)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Honors Scholarship & Honors Program Participation | 4.0 GPA – competitive and limited spaces | $2,500”
  - eligibility_summary: 4.0 GPA – competitive and limited spaces ⟵ “Honors Scholarship & Honors Program Participation | 4.0 GPA – competitive and limited spaces | $2,500”
### `d2bb7da05dddd8d9` Felician University — awards 2025-26 [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/scholarships-and-grants/ (sha256 3b8fe20e7666)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $17,000 ⟵ “Founder Scholarship | 2.90 – 3.49 GPA | $17,000”
  - eligibility_summary: 2.90 – 3.49 GPA ⟵ “Founder Scholarship | 2.90 – 3.49 GPA | $17,000”
### `4f6fef4d6501e051` Felician University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/tuition-and-fees/ (sha256 f1a710651881)
- issues: implausible_amount, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 47}
  - column:Undergraduate Full Time (12 to 18 credits): 18275.0 ⟵ “Undergraduate Full Time (12 to 18 credits) | $18,275.00”
  - column:Undergraduate Part time (less than 12 credits): 1215.0 ⟵ “Undergraduate Part time (less than 12 credits) | $1,215.00”
  - column:Associate and Select Bachelors Completion Program for Adult Learners: 550.0 ⟵ “Associate and Select Bachelors Completion Program for Adult Learners | $550.00”
  - column:Masters of Science in Nursing: 1187 ⟵ “Masters of Science in Nursing | $1,187”
  - column:Master of Business Administration: 1190 ⟵ “Master of Business Administration | $1,190”
  - column:Online Master of Business Administration- Executive Leadership: 520 ⟵ “Online Master of Business Administration- Executive Leadership | $520”
  - column:Master of Science in Health Care Admin.: 1190 ⟵ “Master of Science in Health Care Admin. | $1,190”
  - column:Master of Arts in Religious Education: 350 ⟵ “Master of Arts in Religious Education | $350”
  - column:Master of Science in Computer Science: 1190 ⟵ “Master of Science in Computer Science | $1,190”
  - column:Online Master of Business Administration: 520 ⟵ “Online Master of Business Administration | $520”
  - column:Doctor of Business Administration: 1066 ⟵ “Doctor of Business Administration | $1,066”
  - column:Master of Counseling Psychology: 925 ⟵ “Master of Counseling Psychology | $925”
  - column:Doctorate in Counseling Psychology: 1160 ⟵ “Doctorate in Counseling Psychology | $1,160”
  - column:Education Programs: 725 ⟵ “Education Programs | $725”
  - column:Graduate Certification Programs: 299 ⟵ “Graduate Certification Programs | $299”
  - column:Master in Data Science: 795 ⟵ “Master in Data Science | $795”
  - column:Online Masters in Computer Science: 725 ⟵ “Online Masters in Computer Science | $725”
  - column:Certificate Tuition: 299 ⟵ “Certificate Tuition | $299”
  - column:Project Forward (Lodi, Paterson, Queen Of Peace): 75 ⟵ “Project Forward (Lodi, Paterson, Queen Of Peace) | $75”
  - column:DUAL Enrollment: 60 ⟵ “DUAL Enrollment | $60”
  - column:Jumpstart (Incoming Freshman, transfer students): 75 ⟵ “Jumpstart (Incoming Freshman, transfer students) | $75”
  - column:Non-Matriculated TUG: 1175 ⟵ “Non-Matriculated TUG | $1,175”
  - column:Non-Matriculated AUG: 550 ⟵ “Non-Matriculated AUG | $550”
  - column:Comprehensive Fees Full Time: 1050 ⟵ “Comprehensive Fees Full Time | $1,050”
  - column:Comprehensive Fees Part Time/Graduate: 340 ⟵ “Comprehensive Fees Part Time/Graduate | $340”
  - … 22 more rows
### `8bf8224bdee76fe4` Felician University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/tuition-and-fees/ (sha256 f1a710651881)
- issues: implausible_amount, stacked_header_unparsed, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 10}
  - column:Winter Break: 1082 ⟵ “Winter Break | $1,082”
  - column:Food Plan* Included in housing charge*: 2120 ⟵ “Food Plan* Included in housing charge* | $2,120”
  - column:Orientation Fee: 125 ⟵ “Orientation Fee | $125”
  - column:Accident Insurance Fee: 11 ⟵ “Accident Insurance Fee | $11”
  - column:PLA Assessment Fee: 300 ⟵ “PLA Assessment Fee | $300”
  - column:Dual Enrollment Fees (Weehawkin), Off campus, Felician Instructor: 55 ⟵ “Dual Enrollment Fees (Weehawkin), Off campus, Felician Instructor | $55”
  - column:ATI Fee: Year 1: 3450 ⟵ “ATI Fee: Year 1 | $3,450”
  - column:ATI Fee: Year 2: 3600 ⟵ “ATI Fee: Year 2 | $3,600”
  - column:ATI Fee: Year 3: 3750 ⟵ “ATI Fee: Year 3 | $3,750”
  - column:ABSN ATI Fee: 1150 ⟵ “ABSN ATI Fee | $1,150”
### `f86af64a8d300d71` Felician University — costs 2019-20 · residency=not_applicable [new] (labeled_in_source)
- source: https://felician.edu/admissions/student-financial-services/heerf-reporting/ (sha256 a910c0dfa27a)
- issues: arrangement_unlabeled, implausible_amount, stale_year_label:2019-20
- checks: {"columns": 3, "rows": 8}
  - column:Providing additional emergency financial aid grants to students.1: 0 ⟵ “Providing additional emergency financial aid grants to students.1 | $ 0 | $ 0 | $ 0 | ”
  - column:Providing reimbursements for tuition, housing, room and board, or other fee refunds.: 529087 ⟵ “Providing reimbursements for tuition, housing, room and board, or other fee refunds. | $ 529,087 | $ 0 | $ 0 | ”
  - column:Covering the cost of providing additional technology hardware to students, such as laptops or tablets, or covering the added cost of technology fees.: 99993 ⟵ “Covering the cost of providing additional technology hardware to students, such as laptops or tablets, or covering the added cost of technology fees. | $ 99,993 | $ 0 | $ 0 | ”
  - column:Providing or subsidizing the costs of high‐speed internet to students or faculty to transition to an online environment.: 0 ⟵ “Providing or subsidizing the costs of high‐speed internet to students or faculty to transition to an online environment. | $ 0 | $ 0 | $ 0 | ”
  - column:Subsidizing off‐campus housing costs due to dormitory closures or decisions to limit housing to one student per room; subsidizing housing costs to reduce housing density; paying for hotels or other off‐campus housing for students who need to be isolated; paying travel expenses for students who need to leave campus early due to coronavirus infections or campus interruptions.: 0 ⟵ “Subsidizing off‐campus housing costs due to dormitory closures or decisions to limit housing to one student per room; subsidizing housing costs to reduce housing density; paying for hotels or other off‐campus housing for students who need t”
  - column:Subsidizing food service to reduce density in eating facilities, to provide pre‐packaged meals, or to add hours to food service operations to accommodate social distancing.: 0 ⟵ “Subsidizing food service to reduce density in eating facilities, to provide pre‐packaged meals, or to add hours to food service operations to accommodate social distancing. | $ 0 | $ 0 | $ 0 | ”
  - column:Costs related to operating additional class sections to enable social distancing, such as those for hiring more instructors and increasing campus hours of operations.: 0 ⟵ “Costs related to operating additional class sections to enable social distancing, such as those for hiring more instructors and increasing campus hours of operations. | $ 0 | $ 0 | $ 0 | ”
  - column:Campus safety and operations.2: 244100 ⟵ “Campus safety and operations.2 | $ 244,100 | $ 0 | $ 0 | ”
  - column:Providing additional emergency financial aid grants to students.1: 0 ⟵ “Providing additional emergency financial aid grants to students.1 | $ 0 | $ 0 | $ 0 | ”
  - column:Providing reimbursements for tuition, housing, room and board, or other fee refunds.: 0 ⟵ “Providing reimbursements for tuition, housing, room and board, or other fee refunds. | $ 529,087 | $ 0 | $ 0 | ”
  - column:Providing tuition discounts.: 0 ⟵ “Providing tuition discounts. |  | $ 0 | $ 0 | ”
  - column:Covering the cost of providing additional technology hardware to students, such as laptops or tablets, or covering the added cost of technology fees.: 0 ⟵ “Covering the cost of providing additional technology hardware to students, such as laptops or tablets, or covering the added cost of technology fees. | $ 99,993 | $ 0 | $ 0 | ”
  - column:Providing or subsidizing the costs of high‐speed internet to students or faculty to transition to an online environment.: 0 ⟵ “Providing or subsidizing the costs of high‐speed internet to students or faculty to transition to an online environment. | $ 0 | $ 0 | $ 0 | ”
  - column:Subsidizing off‐campus housing costs due to dormitory closures or decisions to limit housing to one student per room; subsidizing housing costs to reduce housing density; paying for hotels or other off‐campus housing for students who need to be isolated; paying travel expenses for students who need to leave campus early due to coronavirus infections or campus interruptions.: 0 ⟵ “Subsidizing off‐campus housing costs due to dormitory closures or decisions to limit housing to one student per room; subsidizing housing costs to reduce housing density; paying for hotels or other off‐campus housing for students who need t”
  - column:Subsidizing food service to reduce density in eating facilities, to provide pre‐packaged meals, or to add hours to food service operations to accommodate social distancing.: 0 ⟵ “Subsidizing food service to reduce density in eating facilities, to provide pre‐packaged meals, or to add hours to food service operations to accommodate social distancing. | $ 0 | $ 0 | $ 0 | ”
  - column:Costs related to operating additional class sections to enable social distancing, such as those for hiring more instructors and increasing campus hours of operations.: 0 ⟵ “Costs related to operating additional class sections to enable social distancing, such as those for hiring more instructors and increasing campus hours of operations. | $ 0 | $ 0 | $ 0 | ”
  - column:Campus safety and operations.2: 0 ⟵ “Campus safety and operations.2 | $ 244,100 | $ 0 | $ 0 | ”
  - column:Providing additional emergency financial aid grants to students.1: 0 ⟵ “Providing additional emergency financial aid grants to students.1 | $ 0 | $ 0 | $ 0 | ”
  - column:Providing reimbursements for tuition, housing, room and board, or other fee refunds.: 0 ⟵ “Providing reimbursements for tuition, housing, room and board, or other fee refunds. | $ 529,087 | $ 0 | $ 0 | ”
  - column:Providing tuition discounts.: 0 ⟵ “Providing tuition discounts. |  | $ 0 | $ 0 | ”
  - column:Covering the cost of providing additional technology hardware to students, such as laptops or tablets, or covering the added cost of technology fees.: 0 ⟵ “Covering the cost of providing additional technology hardware to students, such as laptops or tablets, or covering the added cost of technology fees. | $ 99,993 | $ 0 | $ 0 | ”
  - column:Providing or subsidizing the costs of high‐speed internet to students or faculty to transition to an online environment.: 0 ⟵ “Providing or subsidizing the costs of high‐speed internet to students or faculty to transition to an online environment. | $ 0 | $ 0 | $ 0 | ”
  - column:Subsidizing off‐campus housing costs due to dormitory closures or decisions to limit housing to one student per room; subsidizing housing costs to reduce housing density; paying for hotels or other off‐campus housing for students who need to be isolated; paying travel expenses for students who need to leave campus early due to coronavirus infections or campus interruptions.: 0 ⟵ “Subsidizing off‐campus housing costs due to dormitory closures or decisions to limit housing to one student per room; subsidizing housing costs to reduce housing density; paying for hotels or other off‐campus housing for students who need t”
  - column:Subsidizing food service to reduce density in eating facilities, to provide pre‐packaged meals, or to add hours to food service operations to accommodate social distancing.: 0 ⟵ “Subsidizing food service to reduce density in eating facilities, to provide pre‐packaged meals, or to add hours to food service operations to accommodate social distancing. | $ 0 | $ 0 | $ 0 | ”
  - column:Costs related to operating additional class sections to enable social distancing, such as those for hiring more instructors and increasing campus hours of operations.: 0 ⟵ “Costs related to operating additional class sections to enable social distancing, such as those for hiring more instructors and increasing campus hours of operations. | $ 0 | $ 0 | $ 0 | ”
  - … 1 more rows
### `b68be1152945b4ac` Georgian Court University — academic_programs 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
- checks: {"courses": 49, "groups": 11, "groups_skipped": 2}
  - program_name: Communication, B.A. (Including Dual Major in Communication and Business Administration) ⟵ “Communication, B.A. (Including Dual Major in Communication and Business Administration) < Georgian Court University”
### `ddf59360d1d425e6` Georgian Court University — academic_programs 2026-27 · program_key=criminal-justice-b-a [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/crim-justice-ba/ (sha256 5017f1747e5e)
- issues: requirement_groups_skipped
- checks: {"courses": 48, "groups": 6, "groups_skipped": 2}
  - program_name: Criminal Justice, B.A. ⟵ “Criminal Justice, B.A. < Georgian Court University”
### `4db2cc14c92ecbc6` Georgian Court University — appeals 2026-27 [new] (source_unlabeled)
- source: https://georgian.edu/wp-content/uploads/Satisfactory-Academic-Progress-Appeal-Form.pdf (sha256 19b3a29e71cc)
- issues: semantic_review_required, conflicting_sources:http://georgian.edu/financial-aid/,https://georgian.edu/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL FORM Read carefully and follow these steps to file your appeal: 1.”
### `f1760adc247dd185` Georgian Court University — appeals 2026-27 [new] (source_unlabeled)
- source: http://georgian.edu/financial-aid/ (sha256 ccf037883fdc)
- issues: semantic_review_required, conflicting_sources:https://georgian.edu/financial-aid/satisfactory-academic-progress/,https://georgian.edu/wp-content/uploads/Satisfactory-Academic-Progress-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Tuition & Fees Take the Next Step Quick Links Financial Aid Applying for Financial Aid (FAFSA Guide) Benefits for Veterans Financial Aid FAQ First-Year & Graduate Aid Forms & Resources Grants Returning Students & Renewal Satisfactory Academic Progress & Appeals Scholarships Student Loans Summer Financial Aid Types of Financial Aid Work-Study Contact Information Financial Aid Scully Registration an”
### `f493e2ecca77267b` Georgian Court University — appeals 2026-27 [new] (source_unlabeled)
- source: https://georgian.edu/financial-aid/satisfactory-academic-progress/ (sha256 e8f7a25de9e6)
- issues: semantic_review_required, conflicting_sources:http://georgian.edu/financial-aid/,https://georgian.edu/wp-content/uploads/Satisfactory-Academic-Progress-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress & Appeals | Georgian Court University | Lakewood, New Jersey Skip to content Apply Visit Request Info Apply Visit Request Info Home Financial Aid Satisfactory Academic Progress & Appeals Admissions Who are you?”
  - sentence: sap_appeal ⟵ “How to appeal: Submit your appeal within 14 days of the date on your Satisfactory Academic Progress Letter.”
  - sentence: sap_appeal ⟵ “Download the Satisfactory Academic Progress Appeal Form [pdf] Other Reinstatement Situations Eligibility Reinstatement Following Disability Discharge — if your federal student loans were previously discharged due to total and permanent disability and you're now returning to school, a separate reinstatement request process applies.”
### `02244a4cc566dbc0` Georgian Court University — degree_requirements 2026-27 · program_key=sport-management-b-s · requirement_key=major-sequence-business-core-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/sports-management-bs/ (sha256 0d380d137ae3)
- issues: course_alternatives_in_rule_text
  - courses: AC 171 ⟵ “AC 171 - Principles of Financial Accounting”
  - courses: AC 172 ⟵ “AC 172 - Principles of Managerial Accounting”
  - courses: EC 181 ⟵ “EC 181 - Principles of Macroeconomics”
  - courses: EC 182 ⟵ “EC 182 - Principles of Microeconomics”
  - courses: BU 121 ⟵ “BU 121 - Quantitative Business Concepts”
  - courses: CAR 200 ⟵ “CAR 200 - Internship Prep & Career Development”
  - courses: BU 213 ⟵ “BU 213 - Mgmt Theory & Org. Behavior”
  - courses: BU 221 ⟵ “BU 221 - Business Statistics & Probability”
  - courses: IS 224 ⟵ “IS 224 - Introduction to Business Analytics”
  - courses: FIN 235 ⟵ “FIN 235 - Introduction to Finance”
  - courses: MK 241 ⟵ “MK 241 - Principles of Marketing”
  - courses: BU 242 ⟵ “BU 242 - Managerial Communications”
  - courses: IS 320 ⟵ “IS 320 - Management Information Systems”
  - courses: BU 351 ⟵ “BU 351 - Internship”
  - courses: BU 491 ⟵ “BU 491 - Business Strategies & Policy”
### `111e32657a856764` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-a-including-medical-imaging-medical-lab-science · requirement_key=course-requirements-except-for-medical-laboratory-science-track-and-medical-imag-2 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-ba/ (sha256 9f71d74f98f9)
- issues: course_alternatives_in_rule_text
  - courses: MA 109 ⟵ “MA 109 - College Algebra”
  - courses: MA 110 ⟵ “MA 110 - Precalculus”
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
  - courses: CH 113 ⟵ “CH 113 - General Chemistry I”
  - courses: CH 114 ⟵ “CH 114 - General Chemistry II”
  - courses: CH 223 ⟵ “CH 223 - Organic Chemistry I”
### `1f55d1223f10c4dc` Georgian Court University — degree_requirements 2026-27 · program_key=criminal-justice-b-a · requirement_key=global-justice-society-cj-po313 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/crim-justice-ba/ (sha256 5017f1747e5e)
- issues: requirement_groups_skipped
  - courses: CJ 353 ⟵ “CJ 353 - Victimology”
### `29595d30796e0473` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=additional-requirements [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BU 121 ⟵ “BU 121 - Quantitative Business Concepts (to fulfill Mathematical Reasoning)”
  - courses: CM 244 ⟵ “CM 244 - Women in Film (to fulfill Power & Society)”
  - courses: BU 319 ⟵ “BU 319 - Business & Professional Ethics (to fulfill Ethics)”
  - courses: BU 351 ⟵ “BU 351 - Internship (to fulfill Experiential Learning)”
### `3506f340ea7b0f66` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=journalism-public-relations-cm-en208 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
  - courses: CM 209 ⟵ “CM 209 - Introduction to Public Relations”
### `39bb869a7ca1489f` Georgian Court University — degree_requirements 2026-27 · program_key=marketing-b-s · requirement_key=major-sequence-business-core-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/marketing-bs/ (sha256 be885a50b64a)
- issues: course_alternatives_in_rule_text
  - courses: AC 171 ⟵ “AC 171 - Principles of Financial Accounting”
  - courses: AC 172 ⟵ “AC 172 - Principles of Managerial Accounting”
  - courses: EC 181 ⟵ “EC 181 - Principles of Macroeconomics”
  - courses: EC 182 ⟵ “EC 182 - Principles of Microeconomics”
  - courses: BU 121 ⟵ “BU 121 - Quantitative Business Concepts”
  - courses: CAR 200 ⟵ “CAR 200 - Internship Prep & Career Development”
  - courses: BU 211 ⟵ “BU 211 - Business Law”
  - courses: BU 213 ⟵ “BU 213 - Mgmt Theory & Org. Behavior”
  - courses: BU 221 ⟵ “BU 221 - Business Statistics & Probability”
  - courses: IS 224 ⟵ “IS 224 - Introduction to Business Analytics”
  - courses: FIN 235 ⟵ “FIN 235 - Introduction to Finance”
  - courses: MK 241 ⟵ “MK 241 - Principles of Marketing”
  - courses: BU 242 ⟵ “BU 242 - Managerial Communications”
  - courses: IS 320 ⟵ “IS 320 - Management Information Systems”
  - courses: BU 351 ⟵ “BU 351 - Internship”
  - courses: BU 491 ⟵ “BU 491 - Business Strategies & Policy”
### `408d9d9d65c65b37` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-a-including-medical-imaging-medical-lab-science · requirement_key=requirements-for-mci-medical-imaging-track-for-students-who-will-take-sonography-2 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-ba/ (sha256 9f71d74f98f9)
- issues: course_alternatives_in_rule_text
  - courses: MA 103 ⟵ “MA 103 - Introduction to Statistical Thinking”
  - courses: MA 109 ⟵ “MA 109 - College Algebra”
  - courses: MA 110 ⟵ “MA 110 - Precalculus”
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
  - courses: CH 113 ⟵ “CH 113 - General Chemistry I”
### `4e91b41e53d45b70` Georgian Court University — degree_requirements 2026-27 · program_key=accounting-b-s · requirement_key=major-sequence-accounting-major-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/accounting-bs/ (sha256 0e516917634a)
- issues: course_alternatives_in_rule_text
  - courses: CS 120 ⟵ “CS 120 - Introduction to Python”
  - courses: AC 272 ⟵ “AC 272 - Intermediate Accounting I”
  - courses: AC 273 ⟵ “AC 273 - Intermediate Accounting II”
  - courses: IS 122 ⟵ “IS 122 - Introduction to Cybersecurity”
  - courses: IS 312 ⟵ “IS 312 - Data Analytics for Business”
  - courses: BU 319 ⟵ “BU 319 - Business & Professional Ethics”
  - courses: AC 371 ⟵ “AC 371 - Accounting Information Systems”
  - courses: AC 372 ⟵ “AC 372 - Cost Accounting & Budgetary Control”
  - courses: AC 471 ⟵ “AC 471 - Individual Federal Taxation”
  - courses: AC 472 ⟵ “AC 472 - Entity Federal Taxation”
  - courses: AC 473 ⟵ “AC 473 - Fund & Advanced Accounting”
  - courses: AC 478 ⟵ “AC 478 - Auditing with Data Analytics”
### `4ff8725d72b9f854` Georgian Court University — degree_requirements 2026-27 · program_key=finance-b-s · requirement_key=major-sequence-business-core-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/finance-bs/ (sha256 4decb6d8d5d8)
- issues: course_alternatives_in_rule_text
  - courses: AC 171 ⟵ “AC 171 - Principles of Financial Accounting”
  - courses: AC 172 ⟵ “AC 172 - Principles of Managerial Accounting”
  - courses: EC 181 ⟵ “EC 181 - Principles of Macroeconomics”
  - courses: EC 182 ⟵ “EC 182 - Principles of Microeconomics”
  - courses: BU 121 ⟵ “BU 121 - Quantitative Business Concepts”
  - courses: CAR 200 ⟵ “CAR 200 - Internship Prep & Career Development”
  - courses: BU 211 ⟵ “BU 211 - Business Law”
  - courses: BU 213 ⟵ “BU 213 - Mgmt Theory & Org. Behavior”
  - courses: BU 221 ⟵ “BU 221 - Business Statistics & Probability”
  - courses: IS 224 ⟵ “IS 224 - Introduction to Business Analytics”
  - courses: FIN 235 ⟵ “FIN 235 - Introduction to Finance”
  - courses: MK 241 ⟵ “MK 241 - Principles of Marketing”
  - courses: BU 242 ⟵ “BU 242 - Managerial Communications”
  - courses: IS 320 ⟵ “IS 320 - Management Information Systems”
  - courses: BU 351 ⟵ “BU 351 - Internship”
  - courses: BU 491 ⟵ “BU 491 - Business Strategies & Policy”
### `52c2a105bc1f3cfc` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=communication-core-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
  - courses: CM 100 ⟵ “CM 100 - Fundamentals of Communication”
  - courses: CM 101 ⟵ “CM 101 - Introduction to Mass Communication”
  - courses: CM 105 ⟵ “CM 105 - Public Speaking”
  - courses: CM 217 ⟵ “CM 217 - Media Production”
  - courses: CM 302 ⟵ “CM 302 - Mass Media & Social Issues”
  - courses: CM 305 ⟵ “CM 305 - Media Law & Ethics”
  - courses: CM 310 ⟵ “CM 310 - Interpersonal Communication”
  - courses: CM 401 ⟵ “CM 401 - Communication Theory”
  - courses: CM 404 ⟵ “CM 404 - Communication Research”
### `54deafde6fe0e8e7` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-a-including-medical-imaging-medical-lab-science · requirement_key=requirements-for-medical-laboratory-science-track [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-ba/ (sha256 9f71d74f98f9)
- issues: course_alternatives_in_rule_text
  - courses: BI 121 ⟵ “BI 121 - Cellular Organiz., Energetics & Function”
  - courses: BI 201 ⟵ “BI 201 - Biological Literature”
  - courses: BI 204 ⟵ “BI 204 - Genetics & Evolution”
  - courses: BI 213 ⟵ “BI 213 - Human Anatomy & Physiology I”
  - courses: BI 214 ⟵ “BI 214 - Human Anatomy & Physiology II”
  - courses: BI 219 ⟵ “BI 219 - Microbiology”
  - courses: BI 401 ⟵ “BI 401 - Medical Technology Internship I”
  - courses: BI 402 ⟵ “BI 402 - Medical Technology Internship II”
  - courses: BI 427 ⟵ “BI 427 - Immunology (4 credits)”
  - courses: BI 428 ⟵ “BI 428 - Fundamentals of Immunology (3 credits)”
  - courses: BI 437 ⟵ “BI 437 - Biochemistry I”
  - courses: BI 443 ⟵ “BI 443 - Capstone in Biology: BA”
### `563bfc74d4ac9f9d` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=journalism-public-relations-cm-en230 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
  - courses: CM 252 ⟵ “CM 252 - Organizational Communication”
### `58e991adaec8dd5d` Georgian Court University — degree_requirements 2026-27 · program_key=criminal-justice-b-a · requirement_key=law-enforcement-corrections [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/crim-justice-ba/ (sha256 5017f1747e5e)
- issues: requirement_groups_skipped
  - courses: CJ 167 ⟵ “CJ 167 - Race, Ethnicity & Criminal Justice (if also taking AN112 as a core CJ requirement)”
  - courses: CJ 210 ⟵ “CJ 210 - Introduction to Law Enforcement (if also taking CJ212 as a core CJ requirement)”
  - courses: CJ 231 ⟵ “CJ 231 - Juvenile Justice”
  - courses: CJ 301 ⟵ “CJ 301 - Cyber Security & GIS”
  - courses: CJ 302 ⟵ “CJ 302 - Cyber Crime”
  - courses: CJ 343 ⟵ “CJ 343 - Criminal Investigation”
  - courses: CJ 353 ⟵ “CJ 353 - Victimology”
  - courses: CJ 398 ⟵ “CJ 398 - Selected Topics in Criminal Justice (dependent on semester, and when designated as concentration course by dept. chair)”
  - courses: CJ 401 ⟵ “CJ 401 - Sex Crimes”
  - courses: CJ 410 ⟵ “CJ 410 - Independent Research in Criminal Justice (dependent on research topic; dept. chair approval required)”
  - courses: IH 335 ⟵ “IH 335 - Integrative Stress Management & Health”
  - courses: PO 211 ⟵ “PO 211 - American National Government”
  - courses: PO 221 ⟵ “PO 221 - State & Local Government in America”
  - courses: PS 320 ⟵ “PS 320 - Forensic Psychology”
  - courses: PS 321 ⟵ “PS 321 - Criminal Profiling”
### `5bfd6b76c6c4c3d6` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-s-including-medical-lab-sci · requirement_key=course-requirements-except-for-medical-laboratory-science-track-related-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-bs/ (sha256 fc37529f9743)
- issues: course_alternatives_in_rule_text
  - courses: MA 110 ⟵ “MA 110 - Precalculus”
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
  - courses: CH 113 ⟵ “CH 113 - General Chemistry I”
  - courses: CH 114 ⟵ “CH 114 - General Chemistry II”
  - courses: CH 223 ⟵ “CH 223 - Organic Chemistry I”
  - courses: CH 224 ⟵ “CH 224 - Organic Chemistry II”
### `6124f1fed70c574d` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=media-visual-studies-requirements [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
  - courses: CM 200 ⟵ “CM 200 - Visual Communication”
  - courses: CM 205 ⟵ “CM 205 - Transmedia Storytelling”
  - courses: CM 235 ⟵ “CM 235 - The Art of Film”
  - courses: CM 244 ⟵ “CM 244 - Women in Film”
### `61a5b4bde0c0efdb` Georgian Court University — degree_requirements 2026-27 · program_key=criminal-justice-b-a · requirement_key=major-sequence-core-requirements [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/crim-justice-ba/ (sha256 5017f1747e5e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CJ 111 ⟵ “CJ 111 - The Criminal Justice System”
  - courses: CJ 167 ⟵ “CJ 167 - Race, Ethnicity & Criminal Justice”
  - courses: CJ 210 ⟵ “CJ 210 - Introduction to Law Enforcement”
  - courses: CJ 213 ⟵ “CJ 213 - Criminal Law & Practice”
  - courses: CJ 320 ⟵ “CJ 320 - Mental Health, Neurodiver. & Crim. Just.”
  - courses: CJ 325 ⟵ “CJ 325 - Gender & Crime”
  - courses: CJ 331 ⟵ “CJ 331 - Research Methods in Criminal Justice”
  - courses: CJ 351 ⟵ “CJ 351 - Comparative Criminal Justice Systems”
  - courses: CJ 435 ⟵ “CJ 435 - Ethical Issues in Criminal Justice”
  - courses: SO 101 ⟵ “SO 101 - Principles of Sociology”
### `62296ca87426f844` Georgian Court University — degree_requirements 2026-27 · program_key=psychology-b-a · requirement_key=major-sequence [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/psychology-ba/ (sha256 990ae5b4921e)
- issues: course_alternatives_in_rule_text
  - courses: PS 111 ⟵ “PS 111 - Introduction to Psychology”
  - courses: PS 214 ⟵ “PS 214 - Information Literacy for Psychology”
  - courses: PS 223 ⟵ “PS 223 - Psychopathology”
  - courses: PS 232 ⟵ “PS 232 - Intro to Stats for the Beh Sciences”
  - courses: PS 332 ⟵ “PS 332 - Psychology of Learning”
  - courses: PS 334 ⟵ “PS 334 - Social Psychology”
  - courses: PS 341 ⟵ “PS 341 - Biological Psychology”
  - courses: PS 430 ⟵ “PS 430 - Rsrch Mthds & Stats for the Beh Sciences”
  - courses: PS 431 ⟵ “PS 431 - Experimental Psychology”
  - courses: PS 450 ⟵ “PS 450 - Internship in Psychology”
  - courses: PS 456 ⟵ “PS 456 - Internship in Psych:Addictions Treatment”
  - courses: PS 455 ⟵ “PS 455 - Senior Seminar”
### `66a3fe7194e62757` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=journalism-public-relations-requirements [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
  - section: journalism-public-relations-requirements ⟵ “Journalism & Public Relations — Requirements”
### `6ca6e247de44b1ef` Georgian Court University — degree_requirements 2026-27 · program_key=graphic-design-b-a · requirement_key=graphic-design-b-a-related-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/graphic-design-ba/ (sha256 82b2dc58eee0)
- issues: course_alternatives_in_rule_text
  - courses: AR 220 ⟵ “AR 220 - Modern Art”
### `77732bea8ea87694` Georgian Court University — degree_requirements 2026-27 · program_key=mathematics-b-a · requirement_key=b-a-in-mathematics-with-data-science-concentration-data-science-concentration-co [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/mathematics-ba/ (sha256 b680b3919e26)
- issues: course_alternatives_in_rule_text
  - courses: CS 220 ⟵ “CS 220 - Python Programming”
  - courses: CS 231 ⟵ “CS 231 - Introduction to Database Systems”
  - courses: CS 414 ⟵ “CS 414 - Research Problem in CS or CIS”
  - courses: CS 415 ⟵ “CS 415 - Internship”
  - courses: MA 414 ⟵ “MA 414 - Research Problem in Mathematics”
  - courses: MA 415 ⟵ “MA 415 - Internship/Externship Program”
  - courses: PH 470 ⟵ “PH 470 - Research Project”
  - courses: PH 471 ⟵ “PH 471 - Research in Physics”
### `807dd23a5715929d` Georgian Court University — degree_requirements 2026-27 · program_key=criminal-justice-b-a · requirement_key=global-justice-society-cj-po355 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/crim-justice-ba/ (sha256 5017f1747e5e)
- issues: requirement_groups_skipped
  - courses: CJ 365 ⟵ “CJ 365 - International Human Rights Law”
  - courses: CJ 375 ⟵ “CJ 375 - Global Justice & Law”
  - courses: CJ 398 ⟵ “CJ 398 - Selected Topics in Criminal Justice (dependent on semester, and when designated as concentration course by dept. chair)”
  - courses: CJ 410 ⟵ “CJ 410 - Independent Research in Criminal Justice (dependent on research topic; dept. chair approval required)”
  - courses: SO 304 ⟵ “SO 304 - Globalization & Sustainability”
  - courses: PO 211 ⟵ “PO 211 - American National Government”
  - courses: PO 233 ⟵ “PO 233 - Modern Political Thought”
  - courses: SW 253 ⟵ “SW 253 - Human Rights & Social Justice”
### `917494a6c96df088` Georgian Court University — degree_requirements 2026-27 · program_key=business-administration-b-s · requirement_key=major-sequence-business-core-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-business-digital-media/business-administration/business-administration-bs/ (sha256 fb47c1b738cf)
- issues: course_alternatives_in_rule_text
  - courses: AC 171 ⟵ “AC 171 - Principles of Financial Accounting”
  - courses: AC 172 ⟵ “AC 172 - Principles of Managerial Accounting”
  - courses: EC 181 ⟵ “EC 181 - Principles of Macroeconomics”
  - courses: EC 182 ⟵ “EC 182 - Principles of Microeconomics”
  - courses: BU 121 ⟵ “BU 121 - Quantitative Business Concepts”
  - courses: CAR 200 ⟵ “CAR 200 - Internship Prep & Career Development”
  - courses: BU 211 ⟵ “BU 211 - Business Law”
  - courses: BU 213 ⟵ “BU 213 - Mgmt Theory & Org. Behavior”
  - courses: BU 221 ⟵ “BU 221 - Business Statistics & Probability”
  - courses: IS 224 ⟵ “IS 224 - Introduction to Business Analytics”
  - courses: FIN 235 ⟵ “FIN 235 - Introduction to Finance”
  - courses: MK 241 ⟵ “MK 241 - Principles of Marketing”
  - courses: BU 242 ⟵ “BU 242 - Managerial Communications”
  - courses: IS 320 ⟵ “IS 320 - Management Information Systems”
  - courses: BU 351 ⟵ “BU 351 - Internship”
  - courses: BU 411 ⟵ “BU 411 - Human Resource Management”
  - courses: BU 491 ⟵ “BU 491 - Business Strategies & Policy”
### `95e8f127df581498` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-a-including-medical-imaging-medical-lab-science · requirement_key=course-requirements-except-for-medical-laboratory-science-track-and-medical-imag [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-ba/ (sha256 9f71d74f98f9)
- issues: course_alternatives_in_rule_text
  - courses: BI 120 ⟵ “BI 120 - Biological Diversity & Phylogeny”
  - courses: BI 121 ⟵ “BI 121 - Cellular Organiz., Energetics & Function”
  - courses: BI 201 ⟵ “BI 201 - Biological Literature”
  - courses: BI 204 ⟵ “BI 204 - Genetics & Evolution”
  - courses: BI 305 ⟵ “BI 305 - Biological Interactions: Ecology (4 credits)”
  - courses: BI 310 ⟵ “BI 310 - Ecology & Health (3 credits)”
  - courses: BI 443 ⟵ “BI 443 - Capstone in Biology: BA”
### `962b4e2577fab317` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-s-including-medical-lab-sci · requirement_key=requirements-for-the-pre-med-track-within-the-b-s-in-biology-degree [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-bs/ (sha256 fc37529f9743)
- issues: course_alternatives_in_rule_text
  - courses: BI 310 ⟵ “BI 310 - Ecology & Health”
### `a7615dfa77cbf43a` Georgian Court University — degree_requirements 2026-27 · program_key=computer-science-b-s · requirement_key=major-sequence-required-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/mathematics-computer-science-physics/computer-sci-bs/ (sha256 4f1c0ef1048e)
- issues: course_alternatives_in_rule_text
  - courses: CS 123 ⟵ “CS 123 - Computer Programming I”
  - courses: CS 126 ⟵ “CS 126 - Computer Programming II”
  - courses: CS 220 ⟵ “CS 220 - Python Programming”
  - courses: CS 225 ⟵ “CS 225 - Computer Architecture”
  - courses: CS 227 ⟵ “CS 227 - Data Structures”
  - courses: CS 231 ⟵ “CS 231 - Introduction to Database Systems”
  - courses: CS 322 ⟵ “CS 322 - Software Engineering”
  - courses: CS 324 ⟵ “CS 324 - Algorithmic Analysis”
  - courses: CS 410 ⟵ “CS 410 - Operating Systems”
  - courses: CS 414 ⟵ “CS 414 - Research Problem in CS or CIS”
  - courses: CS 450 ⟵ “CS 450 - Applications Project”
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
  - courses: MA 209 ⟵ “MA 209 - Linear Algebra”
  - courses: MA 210 ⟵ “MA 210 - Discrete Mathematics”
  - courses: CS 211 ⟵ “CS 211 - Introduction to Cybersecurity”
### `b15da89b38d7713c` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=journalism-public-relations-cm-en309 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
  - courses: CM 317 ⟵ “CM 317 - Advanced Media Production”
  - courses: CM 350 ⟵ “CM 350 - Special Topics”
### `b6b9300b8c366fbc` Georgian Court University — degree_requirements 2026-27 · program_key=criminal-justice-b-a · requirement_key=articulation-agreement-with-ocean-county-police-academy-courses-for-which-ocpa-g [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/crim-justice-ba/ (sha256 5017f1747e5e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CJ 111 ⟵ “CJ 111 - The Criminal Justice System”
  - courses: CJ 210 ⟵ “CJ 210 - Introduction to Law Enforcement”
  - courses: CJ 213 ⟵ “CJ 213 - Criminal Law & Practice”
  - courses: CM 251 ⟵ “CM 251 - Intercultural Communication”
### `c10b3aca25b1dcfe` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=business-administration-business-core-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: AC 171 ⟵ “AC 171 - Principles of Financial Accounting”
  - courses: AC 172 ⟵ “AC 172 - Principles of Managerial Accounting”
  - courses: EC 181 ⟵ “EC 181 - Principles of Macroeconomics”
  - courses: EC 182 ⟵ “EC 182 - Principles of Microeconomics”
  - courses: BU 121 ⟵ “BU 121 - Quantitative Business Concepts”
  - courses: CAR 200 ⟵ “CAR 200 - Internship Prep & Career Development”
  - courses: BU 211 ⟵ “BU 211 - Business Law”
  - courses: BU 213 ⟵ “BU 213 - Mgmt Theory & Org. Behavior”
  - courses: CM 251 ⟵ “CM 251 - Intercultural Communication”
  - courses: FIN 235 ⟵ “FIN 235 - Introduction to Finance”
  - courses: IS 224 ⟵ “IS 224 - Introduction to Business Analytics”
  - courses: MK 241 ⟵ “MK 241 - Principles of Marketing”
  - courses: IS 320 ⟵ “IS 320 - Management Information Systems”
  - courses: BU 411 ⟵ “BU 411 - Human Resource Management”
  - courses: BU 491 ⟵ “BU 491 - Business Strategies & Policy”
### `c1421b962099b131` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=media-visual-studies-cm-en245 [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
  - courses: CM 317 ⟵ “CM 317 - Advanced Media Production”
  - courses: CM 350 ⟵ “CM 350 - Special Topics”
### `d06202aa1464ed82` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=major-sequence-core-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
  - courses: CM 100 ⟵ “CM 100 - Fundamentals of Communication”
  - courses: CM 101 ⟵ “CM 101 - Introduction to Mass Communication”
  - courses: CM 105 ⟵ “CM 105 - Public Speaking”
  - courses: CM 217 ⟵ “CM 217 - Media Production”
  - courses: CM 305 ⟵ “CM 305 - Media Law & Ethics”
  - courses: CM 310 ⟵ “CM 310 - Interpersonal Communication”
  - courses: CM 401 ⟵ “CM 401 - Communication Theory”
  - courses: CM 404 ⟵ “CM 404 - Communication Research”
  - courses: CM 405 ⟵ “CM 405 - Communication Internship”
### `d67d2ba825f65eac` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-a-including-medical-imaging-medical-lab-science · requirement_key=requirements-for-medical-laboratory-science-track-related-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-ba/ (sha256 9f71d74f98f9)
- issues: course_alternatives_in_rule_text
  - courses: MA 109 ⟵ “MA 109 - College Algebra”
  - courses: MA 110 ⟵ “MA 110 - Precalculus”
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
  - courses: CH 113 ⟵ “CH 113 - General Chemistry I”
  - courses: CH 114 ⟵ “CH 114 - General Chemistry II”
  - courses: CH 223 ⟵ “CH 223 - Organic Chemistry I”
  - courses: CH 224 ⟵ “CH 224 - Organic Chemistry II”
### `d7dbbf1b6d941eac` Georgian Court University — degree_requirements 2026-27 · program_key=psychology-b-a · requirement_key=concentration-in-sport-exercise-psychology-required-course [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/psychology-ba/ (sha256 990ae5b4921e)
- issues: course_alternatives_in_rule_text
  - courses: PS 331 ⟵ “PS 331 - Basic Counseling”
  - courses: PS 333 ⟵ “PS 333 - Intro to Applied Behavior Analysis”
  - courses: ES 320 ⟵ “ES 320 - Gender in Sports”
  - courses: PS 227 ⟵ “PS 227 - Lifespan Development”
  - courses: PS 331 ⟵ “PS 331 - Basic Counseling”
  - courses: PS 332 ⟵ “PS 332 - Psychology of Learning”
  - courses: PS 333 ⟵ “PS 333 - Intro to Applied Behavior Analysis”
### `e0563eefd554858d` Georgian Court University — degree_requirements 2026-27 · program_key=criminal-justice-b-a · requirement_key=cyber-crime [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/crim-justice-ba/ (sha256 5017f1747e5e)
- issues: requirement_groups_skipped
  - courses: CS 105 ⟵ “CS 105 - Computer Literacy”
  - courses: CS 111 ⟵ “CS 111 - Foundations Of Computer Science”
  - courses: CS 123 ⟵ “CS 123 - Computer Programming I”
  - courses: CJ 301 ⟵ “CJ 301 - Cyber Security & GIS”
  - courses: CJ 302 ⟵ “CJ 302 - Cyber Crime”
  - courses: CJ 355 ⟵ “CJ 355 - Political Crimes & Terrorism”
  - courses: CJ 398 ⟵ “CJ 398 - Selected Topics in Criminal Justice (when approved for cyber crime)”
  - courses: AC 171 ⟵ “AC 171 - Principles of Financial Accounting”
  - courses: IS 122 ⟵ “IS 122 - Introduction to Cybersecurity”
  - courses: IS 320 ⟵ “IS 320 - Management Information Systems”
### `e442e689ed7e3eec` Georgian Court University — degree_requirements 2026-27 · program_key=psychiatric-rehabilitation-psychology-b-s · requirement_key=major-sequence-for-psychiatric-rehabilitation-psychology [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/psychology-counseling/psychiatric-rehabilitation-psychology-bs/ (sha256 d86f4e80de74)
- issues: course_alternatives_in_rule_text
  - courses: PS 111 ⟵ “PS 111 - Introduction to Psychology”
  - courses: PS 214 ⟵ “PS 214 - Information Literacy for Psychology”
  - courses: PS 223 ⟵ “PS 223 - Psychopathology”
  - courses: PS 232 ⟵ “PS 232 - Intro to Stats for the Beh Sciences”
  - courses: PS 270 ⟵ “PS 270 - Theories of Personality”
  - courses: PS 332 ⟵ “PS 332 - Psychology of Learning”
  - courses: PS 333 ⟵ “PS 333 - Intro to Applied Behavior Analysis”
  - courses: PS 334 ⟵ “PS 334 - Social Psychology”
  - courses: PS 341 ⟵ “PS 341 - Biological Psychology”
  - courses: PS 430 ⟵ “PS 430 - Rsrch Mthds & Stats for the Beh Sciences”
  - courses: PS 431 ⟵ “PS 431 - Experimental Psychology”
### `ea1f4c199704a5e5` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-a-including-medical-imaging-medical-lab-science · requirement_key=requirements-for-pre-medical-imaging-sciences-track-for-students-who-transfer-to [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-ba/ (sha256 9f71d74f98f9)
- issues: course_alternatives_in_rule_text
  - courses: BI 213 ⟵ “BI 213 - Human Anatomy & Physiology I (Rutgers GenEd NatSci)”
  - courses: BI 214 ⟵ “BI 214 - Human Anatomy & Physiology II (Rutgers GenEd NatSci)”
  - courses: BI 219 ⟵ “BI 219 - Microbiology (Rutgers GenEd NatSci)”
  - courses: CH 151 ⟵ “CH 151 - Chemistry for the Health Sciences (Rutgers GenEd NatSci)”
  - courses: PH 111 ⟵ “PH 111 - Physics in Everyday Life I (Rutgers GenEd NatSci)”
  - courses: MA 109 ⟵ “MA 109 - College Algebra (Rutgers GenEd Quantitative)”
  - courses: EN 111 ⟵ “EN 111 - Writing, Research, and Digital Literacy (Rutgers GenEd Writing&Comm)”
  - courses: EN 112 ⟵ “EN 112 - Academic Writing and Research II (Rutgers GenEd Writing&Comm)”
  - courses: PS 111 ⟵ “PS 111 - Introduction to Psychology (Rutgers GenEd SocialSci)”
  - courses: HRP 200 ⟵ “HRP 200 - Medical Terminology (Rutgers GenEd Writing&Comm)”
  - courses: MA 103 ⟵ “MA 103 - Introduction to Statistical Thinking (Rutgers GenEd Quantitative)”
  - courses: GPS 311 ⟵ “GPS 311 - Gender, Power, &Society:Voices of Change (Rutgers GenEd History,Lit&Contemp)”
  - courses: GEN 101 ⟵ “GEN 101 - Pathway to the Bridge”
  - courses: GEN 199 ⟵ “GEN 199 - WI:Discovering Self in the Universe”
### `f4b178d4dd9e725a` Georgian Court University — degree_requirements 2026-27 · program_key=biology-b-s-including-medical-lab-sci · requirement_key=requirements-for-medical-laboratory-science-track-related-courses [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/biology/biology-bs/ (sha256 fc37529f9743)
- issues: course_alternatives_in_rule_text
  - courses: MA 110 ⟵ “MA 110 - Precalculus”
  - courses: MA 115 ⟵ “MA 115 - Calculus I”
  - courses: MA 116 ⟵ “MA 116 - Calculus II”
  - courses: CH 113 ⟵ “CH 113 - General Chemistry I”
  - courses: CH 114 ⟵ “CH 114 - General Chemistry II”
  - courses: CH 223 ⟵ “CH 223 - Organic Chemistry I”
  - courses: CH 224 ⟵ “CH 224 - Organic Chemistry II”
### `fa4123ea5cfe7887` Georgian Court University — degree_requirements 2026-27 · program_key=communication-b-a-including-dual-major-in-communication-and-business-administrat · requirement_key=major-sequence [new] (labeled_in_source)
- source: https://catalog.georgian.edu/undergraduate/school-arts-sciences/english/communication-ba/ (sha256 5db52c692275)
- issues: requirement_groups_skipped
  - courses: CM 251 ⟵ “CM 251 - Intercultural Communication”
  - courses: CM 302 ⟵ “CM 302 - Mass Media & Social Issues”
### `602f002b8f9f318a` Hudson County Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.hccc.edu/admissions/placement-testing/testing-service/index.html (sha256 ccc6f9f5d7e4)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 2, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[CLEP-INFORMATION-SYSTEMS|CSC 100]:  ⟵ “Information Systems | 3 | 50 | CSC 100”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | Principles of Accounting | 3 | 50 | ACC 121”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | Introductory Business Law | 3 | 50 | BUS 230”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | Principles of Marketing | 3 | 50 | MAN 221”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | Analyzing and Interpreting Literature w/essay | 6 | 50 | 2 Literature Electives”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | College Composition | 3 | 50 | ENG 101”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | Humanities (1) | 6 | 50 | 2 Electives: ART,MUS,LIT or THA”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | College Spanish I and II (2 semesters) | 6 | 50 | MLS 101 + MLS 102”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | College German I and II (2 semesters) | 6 | 50 | 2 HUM or Modern Languages electives”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|6 points]:  ⟵ “Information Systems | NYU Language Proficiency Exams | 6 | 6 points | 2 HUM or Modern Languages electives*”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | American Government | 3 | 50 | PSC 102”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | History of the US I | 3 | 50 | HIS 105”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | History of the US II | 3 | 50 | HIS 106”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Human Growth and Development | 3 | 50 | PSY 260”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Principles of Macroeconomics | 3 | 50 | ECO 201”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Principles of Microeconomics | 3 | 50 | ECO 202”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Social Sciences and History (3) | 6 | 50 | 1 Soc. Science + 1 History elective”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Introduction to Educational Psychology | 3 | 50 | PSY 270”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Introductory Psychology | 3 | 50 | PSY 101”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Introductory Sociology | 3 | 50 | SOC 101”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Western Civilization I | 3 | 50 | HIS 210”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Western Civilization II | 3 | 50 | HIS 211”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Natural Science (4) | 6 | 50 | 2 non-lab Science electives”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | College Algebra | 3 | 50 | MAT 100”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Pre-Calculus | 4 | 50 | MAT 110”
  - … 1 more rows
### `23a94b14d7d98cdc` Kean University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.kean.edu/offices/financial-aid/satisfactory-academic-progress-policy (sha256 9ad6234bb29f)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Students deemed not to be making Satisfactory Academic Progress will be notified by Kean email and may file an appeal with the Office of Financial Aid.”
  - sentence: sap_appeal ⟵ “Students will be notified by Kean email as to the outcome of their SAP appeal.”
  - sentence: sap_appeal ⟵ “SAP Appeal Applications are filed at https://kean.studentforms.com/school/dashboard.”
  - sentence: sap_appeal ⟵ “In addition to the SAP Appeal Application, all documents related to that appeal must be uploaded through the url.”
  - sentence: sap_appeal ⟵ “PLEASE NOTE - Final Notice: The SAP appeal deadline date was extended from Friday, August 7, 2026, to Friday, August 21, 2026, for consideration of 2026-2027 financial aid eligibility.”
  - sentence: sap_appeal ⟵ “The SAP Appeal portal is now closed.”
### `35797d6f25ba72dc` Kean University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kean.edu/offices/office-scholarship-services/climb-success-scholarship (sha256 52e0579bd117)
- issues: semantic_review_required, conflicting_sources:https://www.kean.edu/offices/financial-aid/special-circumstances,https://www.kean.edu/offices/office-scholarship-services/climb-completion
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Please note: FAFSA filing is not required for undocumented students, international students, or special circumstances.”
### `69fc49af4c18a867` Kean University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kean.edu/offices/office-scholarship-services/climb-completion (sha256 63f5ec413ea8)
- issues: semantic_review_required, conflicting_sources:https://www.kean.edu/offices/financial-aid/special-circumstances,https://www.kean.edu/offices/office-scholarship-services/climb-success-scholarship
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “FAFSA filing required, except in special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Please note: FAFSA filing is not required for undocumented students, international students, or special circumstances.”
### `ab0e903e61a77b0b` Kean University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.kean.edu/offices/financial-aid/special-circumstances (sha256 8c08dce297e1)
- issues: semantic_review_required, conflicting_sources:https://www.kean.edu/offices/office-scholarship-services/climb-completion,https://www.kean.edu/offices/office-scholarship-services/climb-success-scholarship
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “In some cases, the Office of Financial Aid and Scholarship Services may be able to adjust income information based on these special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “If students and/or their families have been affected by national emergencies, like natural disasters, they may consider requesting a Special Circumstances review as well.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Special Circumstances may include, but not limited to: Job termination or loss of income (due to loss of job and/or reduction in hours worked) Divorce or separation after the FAFSA was completed Death of a parent or spouse after the FAFSA was completed Reduced earnings due to disability or natural disaster Loss or reduction of untaxed income or benefits Loss or reduction of child suppo”
  - sentence: need_based_special_circumstances ⟵ “Contact the Office of Financial Aid to review your situation and if applicable, complete the appropriate Special Circumstances Form (listed below) which is pertinent to your Special Circumstances request, and submit it with all required documentation to the Office of Financial Aid by uploading in Keanwise Financial Aid Self Service portal, in-person, or by mail (email cannot be accepted). 3.”
  - sentence: need_based_special_circumstances ⟵ “The Special Circumstances review cannot be processed until all documentation is received.”
  - sentence: need_based_special_circumstances ⟵ “A Special Circumstance review does not guarantee additional aid.”
### `ea10f136c653971b` Kean University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.kean.edu/offices/financial-aid/cost-attendance (sha256 6c736391f643)
- issues: residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition and Fees: 16370 ⟵ “Tuition and Fees | $16,370 | $16,370 | $16,370”
  - with_parents_or_family:Housing and Food: 7486 ⟵ “Housing and Food | $ 7,486 | $19,808 | ”
  - with_parents_or_family:Books, Course Materials, Supplies, and Equipment: 1280 ⟵ “Books, Course Materials, Supplies, and Equipment | $ 1,280 | $ 1,280 | $ 1,280”
  - with_parents_or_family:Transportation: 3240 ⟵ “Transportation | $ 3,240 | $ 3,240 | $ 1,620”
  - with_parents_or_family:Miscellaneous Personal Expenses: 1916 ⟵ “Miscellaneous Personal Expenses | $ 1,916 | $ 1,916 | $ 1,916”
  - with_parents_or_family:Loan Fees (Direct Stafford Loans): 68 ⟵ “Loan Fees (Direct Stafford Loans) | $ 68 | $ 68 | $ 68”
  - with_parents_or_family:Total Cost of Attendance: 30360 ⟵ “Total Cost of Attendance | $30,360 | $42,682 | $41,422”
  - with_parents_or_family:Total Direct Costs: 16370 ⟵ “Total Direct Costs | $16,370 | $16,370 | $36,538”
  - off_campus_not_with_family:Tuition and Fees: 16370 ⟵ “Tuition and Fees | $16,370 | $16,370 | $16,370”
  - off_campus_not_with_family:Housing and Food: 19808 ⟵ “Housing and Food | $ 7,486 | $19,808 | ”
  - off_campus_not_with_family:Books, Course Materials, Supplies, and Equipment: 1280 ⟵ “Books, Course Materials, Supplies, and Equipment | $ 1,280 | $ 1,280 | $ 1,280”
  - off_campus_not_with_family:Transportation: 3240 ⟵ “Transportation | $ 3,240 | $ 3,240 | $ 1,620”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1916 ⟵ “Miscellaneous Personal Expenses | $ 1,916 | $ 1,916 | $ 1,916”
  - off_campus_not_with_family:Loan Fees (Direct Stafford Loans): 68 ⟵ “Loan Fees (Direct Stafford Loans) | $ 68 | $ 68 | $ 68”
  - off_campus_not_with_family:Total Cost of Attendance: 42682 ⟵ “Total Cost of Attendance | $30,360 | $42,682 | $41,422”
  - off_campus_not_with_family:Total Direct Costs: 16370 ⟵ “Total Direct Costs | $16,370 | $16,370 | $36,538”
  - on_campus:Tuition and Fees: 16370 ⟵ “Tuition and Fees | $16,370 | $16,370 | $16,370”
  - on_campus:Housing and Food (double occupancy): 20168 ⟵ “Housing and Food (double occupancy) |  |  | $20,168”
  - on_campus:Books, Course Materials, Supplies, and Equipment: 1280 ⟵ “Books, Course Materials, Supplies, and Equipment | $ 1,280 | $ 1,280 | $ 1,280”
  - on_campus:Transportation: 1620 ⟵ “Transportation | $ 3,240 | $ 3,240 | $ 1,620”
  - on_campus:Miscellaneous Personal Expenses: 1916 ⟵ “Miscellaneous Personal Expenses | $ 1,916 | $ 1,916 | $ 1,916”
  - on_campus:Loan Fees (Direct Stafford Loans): 68 ⟵ “Loan Fees (Direct Stafford Loans) | $ 68 | $ 68 | $ 68”
  - on_campus:Total Cost of Attendance: 41422 ⟵ “Total Cost of Attendance | $30,360 | $42,682 | $41,422”
  - on_campus:Total Direct Costs: 36538 ⟵ “Total Direct Costs | $16,370 | $16,370 | $36,538”
### `086d60bb8445fd6d` Mercer County Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.mccc.edu/pdf/financial-aid/2026-27/2026-2027-sap-appeal-form.pdf (sha256 da7c599419b7)
- issues: semantic_review_required, conflicting_sources:https://www.mccc.edu/admissions_financial.shtml
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: sap_appeal ⟵ “2026-2027 Satisfactory Academic Progress Appeal Form While you have not met the minimum terms of Satisfactory Academic Progress (SAP) and are therefore ineligible for financial aid, the Financial Aid Office allows you to submit an appeal explaining your circumstances and requesting reinstatement of your eligibility.”
  - sentence: sap_appeal ⟵ “Please review the following important information about the Satisfactory Academic Progress appeal process: 1.”
  - sentence: sap_appeal ⟵ “Instructions for completing and submitting a SAP appeal: 1.”
  - sentence: sap_appeal ⟵ “Meet with an Academic Advisor to discuss the SAP appeal process and your appeal. 2.”
  - sentence: sap_appeal ⟵ “Complete the SAP Appeal Form in its entirety, including all signatures and certifications.”
  - sentence: sap_appeal ⟵ “Submit your completed SAP Appeal Form, the document containing your responses to the questions in Section B, and any desired supporting documents to the Financial Aid Office in person or via email at sap@mccc.edu.”
### `1e9367f456dffa15` Mercer County Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.mccc.edu/pdf/financial-aid/2025-26/2025-26%20Special%20Circumstances%20Review%20Request.pdf (sha256 647383766717)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.mccc.edu/pdf/financial-aid/2025-26/2025-26%20Special%20Circumstances%20Review%20Guidelines.pdf
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: need_based_special_circumstances ⟵ “2025-2026 Special Circumstance Review Request The Free Application for Federal Student Aid (FAFSA) requires students and parents of dependent students to provide financial information from a prior year.”
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office recognizes that special circumstances may arise that result in the reduction of a household’s income or the addition of or increase in extraordinary expenses and that the financial information provided may no longer accurately reflect a household’s current ability to finance a student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Students have the right to request a Special Circumstance Review if they believe one of these situations applies.”
  - sentence: need_based_special_circumstances ⟵ “A student may only submit a Special Circumstance Review Request if they have satisfied all verification requirements for the award year.”
  - sentence: need_based_special_circumstances ⟵ “Each Special Circumstance Review is different, and the Financial Aid Office may request additional documents at their discretion.”
  - sentence: need_based_special_circumstances ⟵ “Failure to provide requested documentation may result in a Special Circumstance Review Request being denied.”
### `1eec669121436f89` Mercer County Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.mccc.edu/pdf/financial-aid/2025-26/2025-26%20Special%20Circumstances%20Review%20Guidelines.pdf (sha256 52dfdaac077d)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.mccc.edu/pdf/financial-aid/2025-26/2025-26%20Special%20Circumstances%20Review%20Request.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “2025-2026 Special Circumstance Review Request A.”
  - sentence: need_based_special_circumstances ⟵ “Guidelines for Special Circumstances Review Requests The Free Application for Federal Student Aid (FAFSA) requires students and parents of dependent students to provide financial information from a prior year.”
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office recognizes that special circumstances may arise that result in the reduction of a household’s income or the addition of or increase in extraordinary expenses and that the financial information provided may no longer accurately reflect a household’s current ability to finance a student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Students have the right to request a Special Circumstance Review if they believe one of these situations applies.”
  - sentence: need_based_special_circumstances ⟵ “The categories listed below are some examples of extenuating circumstances that may be sufficient to warrant a Special Circumstance Review.”
  - sentence: need_based_special_circumstances ⟵ “This chart is for informational purposes only; other valid circumstances may exist, and circumstances listed below may still be insufficient for a Special Circumstance Review to be approved.”
### `2cb012df509d3309` Mercer County Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.mccc.edu/pdf/financial-aid/2026-27/2026-27_Special-Circumstances-Review-Guidelines.pdf (sha256 b8f33bc74f02)
- issues: semantic_review_required, conflicting_sources:https://www.mccc.edu/pdf/financial-aid/2026-27/2026-27_Special-Circumstances-Review-Request.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstance Review Request A.”
  - sentence: need_based_special_circumstances ⟵ “Guidelines for Special Circumstances Review Requests The Free Application for Federal Student Aid (FAFSA) requires students and parents of dependent students to provide financial information from a prior year.”
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office recognizes that special circumstances may arise that result in the reduction of a household’s income or the addition of or increase in extraordinary expenses and that the financial information provided may no longer accurately reflect a household’s current ability to finance a student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Students have the right to request a Special Circumstance Review if they believe one of these situations applies.”
  - sentence: need_based_special_circumstances ⟵ “The categories listed below are some examples of extenuating circumstances that may be sufficient to warrant a Special Circumstance Review.”
  - sentence: need_based_special_circumstances ⟵ “This chart is for informational purposes only; other valid circumstances may exist, and circumstances listed below may still be insufficient for a Special Circumstance Review to be approved.”
### `47a10296180678d1` Mercer County Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.mccc.edu/pdf/financial-aid/2026-27/2026-27_Special-Circumstances-Review-Request.pdf (sha256 8187b78b948f)
- issues: semantic_review_required, conflicting_sources:https://www.mccc.edu/pdf/financial-aid/2026-27/2026-27_Special-Circumstances-Review-Guidelines.pdf
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstance Review Request The Free Application for Federal Student Aid (FAFSA) requires students and parents of dependent students to provide financial information from a prior year.”
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office recognizes that special circumstances may arise that result in the reduction of a household’s income or the addition of or increase in extraordinary expenses and that the financial information provided may no longer accurately reflect a household’s current ability to finance a student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Students have the right to request a Special Circumstance Review if they believe one of these situations applies.”
  - sentence: need_based_special_circumstances ⟵ “A student may only submit a Special Circumstance Review Request if they have satisfied all verification requirements for the award year.”
  - sentence: need_based_special_circumstances ⟵ “Each Special Circumstance Review is different, and the Financial Aid Office may request additional documents at their discretion.”
  - sentence: need_based_special_circumstances ⟵ “Failure to provide requested documentation may result in a Special Circumstance Review Request being denied.”
### `c1b0bebcd30f43dd` Mercer County Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.mccc.edu/admissions_financial.shtml (sha256 d6a565ba2975)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.mccc.edu/pdf/financial-aid/2026-27/2026-2027-sap-appeal-form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “The only modifications during a semester to a student’s SAP status will be the results of a SAP appeal.”
  - sentence: sap_appeal ⟵ “Appeal of Financial Aid / Academic Suspension 2026-2027 Satisfactory Academic Progress Appeal Form Appeal of Financial Aid / Academic Suspension can be granted only in instances in which extenuating circumstances occur.”
### `1e9fa043dcb32c00` Middlesex College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://middlesexcollege.edu/funding-your-education/tuition-and-fees/estimated-financial-aid-cost-of-attendance/ (sha256 6dfb2ece64c7)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition: 3072.0 ⟵ “Tuition | $3,072.00 | $3,312.00 | $5,712.00”
  - with_parents_or_family:Fees: 2172.0 ⟵ “Fees | $2,172.00 | $2,172.00 | $2,172.00”
  - with_parents_or_family:Books: 1570.0 ⟵ “Books | $1,570.00 | $1,570.00 | $1,570.00”
  - with_parents_or_family:Transportation: 2070.0 ⟵ “Transportation | $2,070.00 | $2,070.00 | $2,070.00”
  - with_parents_or_family:Housing and Meals: 10850.0 ⟵ “Housing and Meals | $10,850.00 | $10,850.00 | $10,850.00”
  - with_parents_or_family:Personal Expenses: 2680.0 ⟵ “Personal Expenses | $2,680.00 | $2,680.00 | $2,680.00”
  - with_parents_or_family:Loan Fees: 50.0 ⟵ “Loan Fees | $50.00 | $50.00 | $50.00”
  - with_parents_or_family:Total Budget*: 22464.0 ⟵ “Total Budget* | $22,464.00 | $22,704.00 | $25,104.00”
  - with_parents_or_family:Tuition: 3312.0 ⟵ “Tuition | $3,072.00 | $3,312.00 | $5,712.00”
  - with_parents_or_family:Fees: 2172.0 ⟵ “Fees | $2,172.00 | $2,172.00 | $2,172.00”
  - with_parents_or_family:Books: 1570.0 ⟵ “Books | $1,570.00 | $1,570.00 | $1,570.00”
  - with_parents_or_family:Transportation: 2070.0 ⟵ “Transportation | $2,070.00 | $2,070.00 | $2,070.00”
  - with_parents_or_family:Housing and Meals: 10850.0 ⟵ “Housing and Meals | $10,850.00 | $10,850.00 | $10,850.00”
  - with_parents_or_family:Personal Expenses: 2680.0 ⟵ “Personal Expenses | $2,680.00 | $2,680.00 | $2,680.00”
  - with_parents_or_family:Loan Fees: 50.0 ⟵ “Loan Fees | $50.00 | $50.00 | $50.00”
  - with_parents_or_family:Total Budget*: 22704.0 ⟵ “Total Budget* | $22,464.00 | $22,704.00 | $25,104.00”
### `79638401a58ad082` Monmouth University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.monmouth.edu/finaid/maintaining-your-aid/sap/ (sha256 57a3ca95b6e1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “All appeals must be submitted using the Satisfactory Academic Progress Etrieve form and must be received by the stated deadline.”
  - sentence: sap_appeal ⟵ “Students should note that the appeals process for Financial Aid Satisfactory Academic Progress is separate from the University’s Academic Standards Review process for academic reinstatement to the University.”
  - sentence: sap_appeal ⟵ “Additional appeals must include a description of what circumstances have changed that would enable the student to meet the requirements for satisfactory academic progress and the allowability of such appeals will be determined on a case by case basis by the Associate Director of Financial Aid.”
### `dc1b77a8464dbb90` Monmouth University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.monmouth.edu/finaid/maintaining-your-aid/sap/ (sha256 57a3ca95b6e1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Circumstances that might merit an appeal include, but are not limited to: serious illness or injury to the student or a member of the student’s immediate family, a death in the immediate family, or other special circumstances outside the student’s control.”
### `d401540ef69150ed` Monmouth University — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_url)
- source: https://catalog.monmouth.edu/pdf/2026-2027%20Undergraduate%20Catalog.pdf (sha256 68c81a1d3c4e)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 29, "equivalencies": 135, "rows_without_score": 0}
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese           3         FO-002           3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin (until       3         FL-002           3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American 3,4,5                  ADS-246            3               7/2021)”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art-Drawing          4, 5               AR-191             3               7/2021)”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin Literature   4, 5      FL-003           3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics 3, 4, 5       BE-202           3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology              3                  BY-104             3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics 3, 4, 5       BE-201           3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology              4, 5               BY-110             4”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory       4, 5      MU-221           3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB          3                  No Credit          0”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB          4, 5               MA-125             4”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1          3         PH-101           3”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC          3                  MA-125             4”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1          4, 5      PH-105 and       4”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2          3         PH-101           3”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry            3                  CE-101             3”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2          4, 5      PH-106 and       4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C Mech     3         PH-101           3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese              3                  FO-002             3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|5]:  ⟵ “Physics C Mech     4, 5      PH-211 and       5”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|6]:  ⟵ “Chinese              4, 5               FO-002             6                                            PH-211L”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|5]:  ⟵ “Physics C E & M    4, 5      PH-212 and       5”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Precalculus        4, 5      MA-109           4”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology         4, 5      PY-103           3”
  - … 110 more rows
### `1d1ed69beef097ec` Montclair State University — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://irdata.montclair.edu/institutionalresearch/CDS/Bloomfield%20CDS%202025-2026.pdf (sha256 fef42be6f7ae)
- issues: conflicting_sources:https://irdata.montclair.edu/institutionalresearch/CDS/CDS%202025-2026.pdf
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 1316 ⟵ “Total first-time, first-year (degree-seeking) who applied                                               1152                141            22             1           1316”
  - admits: 905 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                                          806                 87             9             3            905”
  - enrolled: 139 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                                               129                  4             2             4            139”
### `44d450bc6aab1a74` Montclair State University — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://irdata.montclair.edu/institutionalresearch/CDS/CDS%202025-2026.pdf (sha256 fb766f5faad8)
- issues: conflicting_sources:https://irdata.montclair.edu/institutionalresearch/CDS/Bloomfield%20CDS%202025-2026.pdf
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 26224 ⟵ “Total first-time, first-year (degree-seeking) who applied                                             21206                 3559          1459             0       26224”
  - admits: 23443 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                                       19137                 3086          1220             0       23443”
  - enrolled: 3816 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                                             3590                  175            51             0         3816”
  - sat_composite_25..75: [850, 1000, 1160] ⟵ “SAT Composite                                            850                   1000                  1160”
  - sat_reading_25..75: [430, 520, 600] ⟵ “SAT Evidence-Based Reading and   430                    520                  600”
  - sat_math_25..75: [418, 480, 560] ⟵ “SAT Math                                                 418                    480                  560”
### `58d77dee3ad8cb3a` Montclair State University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://irdata.montclair.edu/institutionalresearch/CDS/CDS%202024-2025.pdf (sha256 f339450adf77)
- issues: applications_breakdown_does_not_reconcile, admits_breakdown_does_not_reconcile, enrolled_breakdown_does_not_reconcile, stale_year_label:2024-25
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 0 ⟵ “Total first-time, first-year who applied                                                                 26257              21495          3602          1160             0”
  - admits: 0 ⟵ “Total first-time, first-year who were admitted                                                           23076              19005          3103           968             0”
  - enrolled: 0 ⟵ “Total first-time, first-year who enrolled                                                                 4109                3854          182            73             0”
  - sat_composite_25..75: [930, 1080, 1200] ⟵ “SAT Composite                                930                             1080                   1200”
  - sat_reading_25..75: [480, 550, 620] ⟵ “SAT Evidence-Based Reading and Writing       480                              550                    620”
  - sat_math_25..75: [430, 520, 590] ⟵ “SAT Math                                     430                              520                    590”
### `14726f8a55260bf6` Montclair State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office/appeals-and-special-circumstances (sha256 2b305fcca510)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “These cases may qualify for a dependency override.”
### `2275eedfe52ee9ff` Montclair State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.montclair.edu/admissions-aid/financial-aid (sha256 e157a268d49f)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office,https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office/appeals-and-special-circumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Complete the FAFSA with your information and indicate that you have unusual circumstances (there is a check-off box).”
### `8d918bda5f9409eb` Montclair State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office (sha256 afd7b553c6ef)
- issues: semantic_review_required, conflicting_sources:https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office/appeals-and-special-circumstances,https://www.montclair.edu/admissions-aid/financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “File Your FAFSA More in Financial Aid Office Appeals and Special Circumstances Federal Financial Aid Changes Financial Aid Checklist Financial Aid Eligibility Financial Aid for Study Abroad Grants and Scholarships HEERF Funding and Compliance Reporting Loan Information New Jersey Dream Act Student Handbook for Financial Aid Summer Financial Aid Types of Financial Aid Grants Grants are typically ne”
### `f3fd8238e45cfeef` Montclair State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office/appeals-and-special-circumstances (sha256 2b305fcca510)
- issues: semantic_review_required, conflicting_sources:https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office,https://www.montclair.edu/admissions-aid/financial-aid
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Changes to your family’s financial situation → Special Circumstances (SAI Appeal) Unable to provide parent information → Unusual Circumstances Appeal Not meeting academic progress requirements → Visit Financial Aid Eligibility (SAP) Special Circumstances (SAI Appeal) What Are Special Circumstances?”
  - sentence: need_based_special_circumstances ⟵ “Important to Know About Special Circumstances You must receive your initial financial aid offer before submitting a request Incoming students must: Be accepted Pay their deposit File a FAFSA Unusual Circumstances (Dependency Appeal) What Are Unusual Circumstances?”
  - sentence: need_based_special_circumstances ⟵ “Filing a Request for Review or Unusual Circumstances appeal will not change loan eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Important to Know About Unusual Circumstances Approval is not guaranteed.”
### `52074de999593e29` New Jersey Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.njit.edu/financialaid/SAP (sha256 7199f0ee26df)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP Appeals Process A student who fails the standards of SAP and has mitigating circumstances as mentioned below may submit an appeal by the deadline as per the policy and the appeal form.”
  - sentence: sap_appeal ⟵ “Below are the mitigating circumstance allowed under an appeal: Death in the family Illness Other special circumstances Completed SAP appeals will be reviewed within 15 business days (during peak times, the review may take longer).”
### `e1df56e1e5838562` Passaic County Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://pccc.edu/paying-for-college/financial-aid/ (sha256 a16faa966044)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “I Received a Letter Stating I Must Submit a SAP Appeal To Get Financial Aid, Will I Get Approved?”
  - sentence: sap_appeal ⟵ “Decisions regarding a SAP appeal are made by a SAP Appeal Committee.”
### `27f84b04a74c4899` Pillar College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.pillar.edu/admission-aid/financial-aid-policies-disclosures (sha256 14de0ef01654)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Appeal Policy If you have extenuating circumstances impacting your financial condition, or a situation you were unable to document when completing the FAFSA form, and if you believe the SAI calculated for you is too high or too low, please request a Financial Aid Professional Judgment form from the Financial Aid Office.”
### `0844d58d66a360cf` Ramapo College of New Jersey — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ramapo.edu/student-accounts/costinfo/2024-2025-cost-information/ (sha256 c640d56e1dcb)
- issues: residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (Per Semester): 7087.68 ⟵ “Tuition (Per Semester) | $7,087.68”
  - column:Estimated Fees (Per Semester): 1850.0 ⟵ “Estimated Fees (Per Semester) | $1,850.00”
  - column:One-time Criminal Background Check: 106.4 ⟵ “One-time Criminal Background Check | $106.40”
### `32d64106dccd8d11` Ramapo College of New Jersey — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ramapo.edu/student-accounts/costinfo/2024-2025-cost-information/ (sha256 c640d56e1dcb)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "rows": 4}
  - column:Tuition per-credit (Less than 12): 865.87 ⟵ “Tuition per-credit (Less than 12) | $524.27 | $865.87”
  - column:Tuition flat rate (12-18): 13853.92 ⟵ “Tuition flat rate (12-18) | $8,388.32 | $13,853.92”
  - column:Qualified Community College per-credit: 695.04 ⟵ “Qualified Community College per-credit | N/A | $695.04”
  - column:Qualified Community College flat rate: 11120.64 ⟵ “Qualified Community College flat rate | N/A | $11,120.64”
### `4415b5c62e09e785` Ramapo College of New Jersey — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ramapo.edu/student-accounts/costinfo/2025-2026-cost-information/ (sha256 799026ba9b5d)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 4}
  - column:Tuition per-credit (Less than 12): 909.16 ⟵ “Tuition per-credit (Less than 12) | $550.48 | $909.16”
  - column:Tuition flat rate (12-18): 14546.56 ⟵ “Tuition flat rate (12-18) | $8,807.68 | $14,546.56”
  - column:Qualified Community College per-credit: 729.79 ⟵ “Qualified Community College per-credit | N/A | $729.79”
  - column:Qualified Community College flat rate: 11676.64 ⟵ “Qualified Community College flat rate | N/A | $11,676.64”
### `44983bec64f80530` Ramapo College of New Jersey — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ramapo.edu/student-accounts/costinfo/ (sha256 a00bef3e7a6f)
- issues: residency_unknown, conflicting_sources:https://www.ramapo.edu/admissions/financial-aid-tuition/tuition-costs/
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (Per Semester): 7740.0 ⟵ “Tuition (Per Semester) | $7,740.00”
  - column:Estimated Fees (Per Semester): 1850.0 ⟵ “Estimated Fees (Per Semester) | $1,850.00”
  - column:One-time Criminal Background Check: 166.92 ⟵ “One-time Criminal Background Check | $166.92”
### `76350f8765b8b57c` Ramapo College of New Jersey — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.ramapo.edu/student-accounts/costinfo/2025-2026-cost-information/ (sha256 799026ba9b5d)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Tuition per-credit (Less than 12): 550.48 ⟵ “Tuition per-credit (Less than 12) | $550.48 | $909.16”
  - column:Tuition flat rate (12-18): 8807.68 ⟵ “Tuition flat rate (12-18) | $8,807.68 | $14,546.56”
### `8dfffd4304e0610c` Ramapo College of New Jersey — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ramapo.edu/student-accounts/costinfo/2025-2026-cost-information/ (sha256 799026ba9b5d)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (Per Semester): 7442.08 ⟵ “Tuition (Per Semester) | $7,442.08”
  - column:Estimated Fees (Per Semester): 1850.0 ⟵ “Estimated Fees (Per Semester) | $1,850.00”
  - column:One-time Criminal Background Check: 122.39 ⟵ “One-time Criminal Background Check | $122.39”
### `93e1bdeef3776abc` Ramapo College of New Jersey — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ramapo.edu/admissions/financial-aid-tuition/tuition-costs/ (sha256 6882f5626d9b)
- issues: residency_unknown, conflicting_sources:https://www.ramapo.edu/student-accounts/costinfo/
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Full-Time Student Tuition & Fees, Yearly: 24288.0 ⟵ “Full-Time Student Tuition & Fees, Yearly | $18,320.00 | $30,257.60 | $24,288.00”
  - column:Renewal & Restoration Fee: 208.0 ⟵ “Renewal & Restoration Fee | $208.00 | $208.00 | $208.00”
  - column:Room & Board, Yearly Average*: 16400.0 ⟵ “Room & Board, Yearly Average* | $16,400.00 | $16,400.00 | $16,400.00”
  - column:Total Cost For Residential Student, Yearly: 40896.0 ⟵ “Total Cost For Residential Student, Yearly | $34,928.00 | $46,865.60 | $40,896.00”
### `9b9afbed2d8d53c2` Ramapo College of New Jersey — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.ramapo.edu/student-accounts/costinfo/2024-2025-cost-information/ (sha256 c640d56e1dcb)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "rows": 2}
  - column:Tuition per-credit (Less than 12): 524.27 ⟵ “Tuition per-credit (Less than 12) | $524.27 | $865.87”
  - column:Tuition flat rate (12-18): 8388.32 ⟵ “Tuition flat rate (12-18) | $8,388.32 | $13,853.92”
### `a30f60d288aad98d` Ramapo College of New Jersey — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ramapo.edu/student-accounts/costinfo/ (sha256 a00bef3e7a6f)
- issues: conflicting_sources:https://www.ramapo.edu/admissions/financial-aid-tuition/tuition-costs/
- checks: {"columns": 1, "rows": 2}
  - column:Tuition per-credit (Less than 12): 572.5 ⟵ “Tuition per-credit (Less than 12) | $572.50 | $945.55”
  - column:Tuition flat rate (12-18): 9160.0 ⟵ “Tuition flat rate (12-18) | $9,160.00 | $15,128.80”
### `a6341bfe971a4be3` Ramapo College of New Jersey — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ramapo.edu/admissions/financial-aid-tuition/tuition-costs/ (sha256 6882f5626d9b)
- issues: conflicting_sources:https://www.ramapo.edu/student-accounts/costinfo/
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Full-Time Student Tuition & Fees, Yearly: 30257.6 ⟵ “Full-Time Student Tuition & Fees, Yearly | $18,320.00 | $30,257.60 | $24,288.00”
  - column:Renewal & Restoration Fee: 208.0 ⟵ “Renewal & Restoration Fee | $208.00 | $208.00 | $208.00”
  - column:Room & Board, Yearly Average*: 16400.0 ⟵ “Room & Board, Yearly Average* | $16,400.00 | $16,400.00 | $16,400.00”
  - column:Total Cost For Residential Student, Yearly: 46865.6 ⟵ “Total Cost For Residential Student, Yearly | $34,928.00 | $46,865.60 | $40,896.00”
### `b7ea78120859957c` Ramapo College of New Jersey — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ramapo.edu/student-accounts/costinfo/ (sha256 a00bef3e7a6f)
- issues: conflicting_sources:https://www.ramapo.edu/admissions/financial-aid-tuition/tuition-costs/
- checks: {"columns": 1, "rows": 4}
  - column:Tuition per-credit (Less than 12): 945.55 ⟵ “Tuition per-credit (Less than 12) | $572.50 | $945.55”
  - column:Tuition flat rate (12-18): 15128.8 ⟵ “Tuition flat rate (12-18) | $9,160.00 | $15,128.80”
  - column:Qualified Community College per-credit: 759.0 ⟵ “Qualified Community College per-credit | N/A | $759.00”
  - column:Qualified Community College flat rate: 12144.0 ⟵ “Qualified Community College flat rate | N/A | $12,144.00”
### `f292a900913bbd0b` Ramapo College of New Jersey — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ramapo.edu/admissions/financial-aid-tuition/tuition-costs/ (sha256 6882f5626d9b)
- issues: conflicting_sources:https://www.ramapo.edu/student-accounts/costinfo/
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Full-Time Student Tuition & Fees, Yearly: 18320.0 ⟵ “Full-Time Student Tuition & Fees, Yearly | $18,320.00 | $30,257.60 | $24,288.00”
  - column:Renewal & Restoration Fee: 208.0 ⟵ “Renewal & Restoration Fee | $208.00 | $208.00 | $208.00”
  - column:Room & Board, Yearly Average*: 16400.0 ⟵ “Room & Board, Yearly Average* | $16,400.00 | $16,400.00 | $16,400.00”
  - column:Total Cost For Residential Student, Yearly: 34928.0 ⟵ “Total Cost For Residential Student, Yearly | $34,928.00 | $46,865.60 | $40,896.00”
### `993085e076fc09b5` Raritan Valley Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.raritanval.edu/paying-for-college/tuition-fees/ (sha256 9ee5fa3cc7af)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “For assistance, please contact the Enrollment Center: 📞 (908) 526-1200 Option 2 📧 admissions@raritanval.edu 📍 Stop by Enrollment Center L32 See RVCC's 2025-26 Cost of Attendance Tuition Waivers and Special Circumstances Senior citizens Eligible unemployed residents National Guard Tuition Waiver Volunteer Tuition Credit Program Eligible family members of September 11 victims Students seeking charge”
### `6f2c4b50aa9b17cf` Raritan Valley Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.raritanval.edu/wp-content/uploads/2026/06/rvcc-cost-of-attendance-2025-2026.pdf (sha256 de810dc6dca7)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "rows": 73}
  - column:Tuition & Fees: 7350.0 ⟵ “Tuition & Fees | $7,350.00 | $7,350.00”
  - column:Books & Supplies: 2400.0 ⟵ “Books & Supplies | $2,400.00 | $2,400.00”
  - column:Living Expenses: 7500.0 ⟵ “Living Expenses | $7,500.00 | $15,000.00”
  - column:Transportation: 2025.0 ⟵ “Transportation | $2,025.00 | $2,025.00”
  - column:Matriculation Fee: 75.0 ⟵ “Matriculation Fee | $75.00 | $75.00”
  - column:Miscellaneous: 500.0 ⟵ “Miscellaneous | $500.00 | $500.00”
  - column:TOTAL: 19850.0 ⟵ “TOTAL | $19,850.00 | $27,350.00”
  - column:Tuition & Fees (2): 5390.0 ⟵ “Tuition & Fees | $5,390.00 | $5,390.00”
  - column:Books & Supplies (2): 1800.0 ⟵ “Books & Supplies | $1,800.00 | $1,800.00”
  - column:Living Expenses (2): 7500.0 ⟵ “Living Expenses | $7,500.00 | $15,000.00”
  - column:Transportation (2): 1518.0 ⟵ “Transportation | $1,518.00 | $1,518.00”
  - column:Miscellaneous (2): 500.0 ⟵ “Miscellaneous | $500.00 | $500.00”
  - column:Matriculation Fee (2): 75.0 ⟵ “Matriculation Fee | $75.00 | $75.00”
  - column:TOTAL (2): 16783.0 ⟵ “TOTAL | $16,783.00 | $24,283.00”
  - column:Tuition & Fees (3): 3980.0 ⟵ “Tuition & Fees | $3,980.00 | $3,920.00”
  - column:Books & Supplies (3): 1200.0 ⟵ “Books & Supplies | $1,200.00 | $1,200.00”
  - column:Living Expenses (3): 7500.0 ⟵ “Living Expenses | $7,500.00 | $15,000.00”
  - column:Transportation (3): 1013.0 ⟵ “Transportation | $1,013.00 | $1,013.00”
  - column:Miscellaneous (3): 500.0 ⟵ “Miscellaneous | $500.00 | $500.00”
  - column:Matriculation Fee (3): 75.0 ⟵ “Matriculation Fee | $75.00 | $75.00”
  - column:TOTAL (3): 12208.0 ⟵ “TOTAL | $12,208.00 | $21,708.00”
  - column:Tuition & Fees (4): 2450.0 ⟵ “Tuition & Fees | $2,450.00 | $2,450.00”
  - column:Books & Supplies (4): 600.0 ⟵ “Books & Supplies | $600.00 | $600.00”
  - column:Living Expenses (4): 0.0 ⟵ “Living Expenses | $0.00 | $0.00”
  - column:Transportation (4): 484.0 ⟵ “Transportation | $484.00 | $484.00”
  - … 121 more rows
### `56743dea9bc42aeb` Raritan Valley Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.raritanval.edu/admissions/placement-testing/ (sha256 b0fcb615b844)
- issues: conflicting_sources:https://www.raritanval.edu/admissions/placement-testing/alternative-academic-credit-options/
- checks: {"distinct_exams": 3, "equivalencies": 3, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50+]:  ⟵ “College Algebra | 50+ | MATH 113 – Precalculus II”
  - equivalencies[CLEP-PRECALCULUS|50+]:  ⟵ “Precalculus | 50+ | MATH 151 – Calculus I”
  - equivalencies[CLEP-CALCULUS|50+]:  ⟵ “Calculus with Elem Functions | 50+ | MATH 152 – Calculus II”
### `e5e5bc913667bc14` Raritan Valley Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.raritanval.edu/admissions/placement-testing/alternative-academic-credit-options/ (sha256 4924116012ef)
- issues: conflicting_sources:https://www.raritanval.edu/admissions/placement-testing/
- checks: {"distinct_exams": 12, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3+ 3+]:  ⟵ “Art Drawing Art 2D Design | 3+ 3+ | ARTS 110- Basic Drawing I ARTS 105- Two Dimensional Design”
  - equivalencies[AP-ART-HISTORY|3+ 3+]:  ⟵ “Art History | 3+ 3+ | ARTH 110- Art History I ARTH 111- Art History II”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3+ 3+]:  ⟵ “Computer Science A Computer Principles AP | 3+ 3+ | CSIT 105- Foundations of Computer CSIT 103 – Computer Concepts & Programming (must take an exam in Java)”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+ 3+]:  ⟵ “English Lit/Comp English Language | 3+ 3+ | ENGL 111- English I ENGL 112- English II ENGL 111- English I ENGL 112- English II”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4 or 5 3 4 or 5]:  ⟵ “Spanish French | 4 or 5 3 4 or 5 | Conversation and Composition I Conversation and Composition II Conversation and Composition I Conversation and Composition I Conversation and Composition II”
  - equivalencies[AP-UNITED-STATES-HISTORY|4 or 5 4 or 5]:  ⟵ “US History World History | 4 or 5 4 or 5 | HIST 201- US History- Beginnings to 1877 HIST 202- US History- 1877 to Present HIST 101- World Civilization I HIST 102- World Civilization II”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4 or 5]:  ⟵ “Human Geography | 4 or 5 | GEOG 102- Cultural Geography”
  - equivalencies[AP-CALCULUS-BC|3 4+3+ 3+ 3+3+]:  ⟵ “Precalculus PrecalculusCalculus AB Calculus BC, AB Subscore Calculus BC Statistics | 3 4+3+ 3+ 3+3+ | MATH 112 – Precalculus I MATH 112 – Precalculus I MATH 113 – Precalculus II MATH 151 – Calculus I MATH 151 – Calculus I MATH 151 – Calculus I MATH 152 – Calculus II MATH 110 – Statistics I”
  - equivalencies[AP-MUSIC-THEORY|4 or 5]:  ⟵ “Music Theory | 4 or 5 | MUSC 101- Fundamentals of Music”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4+]:  ⟵ “US Government & Politics | 4+ | POLI 121- American Government & Politics”
  - equivalencies[AP-PSYCHOLOGY|3+]:  ⟵ “Psychology | 3+ | PSYC 103- Introduction to Psychology”
  - equivalencies[AP-BIOLOGY|3+ 3+ 3+ 3+ 3+ 3+ 3+]:  ⟵ “Biology Chemistry Env. Science Physics 1 Physics 2 Physics C (Mechanics) Physics C (Elec. and Mag.) | 3+ 3+ 3+ 3+ 3+ 3+ 3+ | BIOL 101- General Biology I BIOL 102- General Biology II CHEM 103- General Chemistry I CHEM 104- General Chemistry II ENVI 101- Introduction to Environmental Studies PHYS 101-”
### `f371a2ccfe61864e` Raritan Valley Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.raritanval.edu/admissions/placement-testing/alternative-academic-credit-options/ (sha256 4924116012ef)
- issues: course_column_missing, conflicting_sources:https://www.raritanval.edu/admissions/placement-testing/
- checks: {"distinct_exams": 25, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 cr. American Literature I or II”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 cr. 200 Level English Literature”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology, General | 50 | 8 cr. General Biology I & II”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business Law, Introductory | 50 | 3 cr. Business Law I”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus w/Elementary Functions | 50 | 4 cr. Calculus I”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry, General | 50 | 8 cr. General Chemistry I & II”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 6 cr. English Composition I & II”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Educational Psychology, Introduction to | 50 | 3 cr. Educational Psychology”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 cr. 200 Level English Literature”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, College Level4 | 59 | 3 – 6 cr. Intermediate French I & II”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Math | 50 | 3 cr. Number Systems”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “German Language, College Level4 | 63 | 3 – 6 cr. Intermediate German I & II”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | 3 cr. Child Development OR Psychology elective”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer App.5 | 50 | 5 cr. Comp Concepts & Programming & JAVA Programming”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Principles of | 50 | 3 cr. Macroeconomics”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Principles of | 50 | 3 cr. Principles of Management”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of | 50 | 3 cr. Principles of Marketing I”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Principles of | 50 | 3 cr. Microeconomics”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-calculus | 50 | 6 cr. Precalculus I and II”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory | 50 | 3 cr. Introduction to Psychology”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences – History3 | 50 | 6 cr. General Education elective”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introductory | 50 | 3 cr. Introduction to Sociology”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language, College Level4 | 63 | 3 – 6 cr. Intermediate Spanish I & II”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East-1648 | 50 | 3 cr. World Civilization I”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648-Present | 50 | 3 cr. World Civilization II”
### `fd4dd2077411476f` Raritan Valley Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.raritanval.edu/admissions/placement-testing/ (sha256 b0fcb615b844)
- issues: conflicting_sources:https://www.raritanval.edu/admissions/placement-testing/alternative-academic-credit-options/
- checks: {"distinct_exams": 4, "equivalencies": 6, "rows_without_score": 0}
  - equivalencies[AP-STATISTICS|3+]:  ⟵ “Statistics | 3+ | MATH 111 – Statistics II”
  - equivalencies[AP-PRECALCULUS|3+]:  ⟵ “Precalculus | 3+ | MATH 113 – Precalculus II”
  - equivalencies[AP-PRECALCULUS|4+]:  ⟵ “Precalculus | 4+ | MATH 151 – Calculus I”
  - equivalencies[AP-CALCULUS-AB|3+]:  ⟵ “Calculus AB | 3+ | MATH 152 – Calculus II”
  - equivalencies[AP-CALCULUS-BC|3+]:  ⟵ “Calculus BC (AB) | 3+ | Same as above”
  - equivalencies[AP-CALCULUS-BC|3+]:  ⟵ “Calculus BC | 3+ | MATH 251 – Calculus III MATH 254 – Differential Equations MATH 255 – Discrete Mathematics MATH 256 – Linear Algebra”
### `00eac415dfca0fa6` Rider University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rider.edu/tuition-aid/financial-aid/aid-guide/fafsa-reminder (sha256 4156e7058003)
- issues: semantic_review_required, conflicting_sources:https://www.rider.edu/tuition-aid/financial-aid/professional-judgment-request
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “I have special circumstances that may not be reported on my FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Sometimes, special circumstances not reflected on your FAFSA can affect your ability to pay for your education.”
  - sentence: need_based_special_circumstances ⟵ “If you believe you have a qualifying special circumstance, please contact the One Stop Office after completing your FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Students who cannot contact a parent or for whom contact would be unsafe should instead contact the Office of Financial Aid about an unusual circumstances review.”
  - sentence: need_based_special_circumstances ⟵ “Students who cannot contact their parents, or for whom contact would present a risk, may be able to request a review of their dependency status based on unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Submit the FAFSA using the unusual circumstances option and contact Rider’s Office of Financial Aid for information about the documentation and review process.”
### `0c3357030615959c` Rider University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.rider.edu/tuition-aid/financial-aid/aid-guide (sha256 88b905427c5a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Review your Unsatisfied Requirements on the Home Tab and ensure all requirements are completed Select the “Award Offer” Tab Review your award offer “Accept” or “Decline” any offered Federal Direct Loans Scroll to the bottom of the page and select “Submit” or “Confirm” Review and check off the acknowledge button for your Terms and Conditions, and select “Accept Award” Federal Direct Loan Checklist ”
### `56829d0f2c5c5028` Rider University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rider.edu/tuition-aid/financial-aid/professional-judgment-request (sha256 15cab6882ef5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustment Request (PDF) For eligible educational expenses not adequately reflected in Rider's standard cost of attendance.”
### `a24ade5c9616b453` Rider University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rider.edu/tuition-aid/financial-aid/professional-judgment-request (sha256 15cab6882ef5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “The following circumstances do not, by themselves, qualify a student for a dependency override: A parent refuses to contribute toward the student's education or provide FAFSA information; A parent does not claim the student as a federal income tax dependent; or The student is financially self-supporting.”
  - sentence: dependency_override ⟵ “Requests for a dependency override or homeless youth determination will be reviewed as quickly as practicable.”
  - sentence: dependency_override ⟵ “Prior Determinations of Independence Students who previously received a dependency override or homeless youth determination from Rider will generally continue to be treated as independent in future award years unless the student's circumstances change or Rider receives conflicting information.”
  - sentence: dependency_override ⟵ “Rider may also consider a documented dependency override or homeless youth determination made by a financial aid administrator at another institution. 2026-27 Special Financial Circumstances Request Deadline Students should submit a complete Special Financial Circumstances Request by April 1, 2027, to allow sufficient time for review and processing.”
### `a359f3a5dc89dd7c` Rider University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rider.edu/tuition-aid/financial-aid/aid-guide/fafsa-reminder (sha256 4156e7058003)
- issues: semantic_review_required, conflicting_sources:https://www.rider.edu/tuition-aid/financial-aid,https://www.rider.edu/tuition-aid/financial-aid/professional-judgment-request
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “In these situations, federal regulations allow financial aid administrators to use professional judgment on a case-by-case basis, with documentation, to adjust the data elements on your FAFSA that may impact your Student Aid Index (SAI).”
  - sentence: professional_judgment ⟵ “Visit Rider’s Professional Judgment Request page for more information.”
### `d60b9eb32b0b0168` Rider University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rider.edu/tuition-aid/financial-aid/professional-judgment-request (sha256 15cab6882ef5)
- issues: semantic_review_required, conflicting_sources:https://www.rider.edu/tuition-aid/financial-aid,https://www.rider.edu/tuition-aid/financial-aid/aid-guide/fafsa-reminder
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Contact Us: 609-896-5360 Office Location Bart Luedeke Center 1st Floor 609-896-5360 finaid@rider.edu Prospective Students Office of Admission 609-896-5042 800-257-9026 admissions@rider.edu Facebook Professional Judgment Requests The information reported on the Free Application for Federal Student Aid, FAFSA, may not always reflect a student's current financial or personal circumstances.”
  - sentence: professional_judgment ⟵ “Federal regulations allow Rider University financial aid administrators to review certain circumstances on a case-by-case basis through professional judgment.”
  - sentence: professional_judgment ⟵ “Professional judgment decisions require appropriate documentation and are made on a case-by-case basis.”
### `e5244e93c0aafa9b` Rider University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rider.edu/tuition-aid/financial-aid (sha256 54410043045c)
- issues: semantic_review_required, conflicting_sources:https://www.rider.edu/tuition-aid/financial-aid/aid-guide/fafsa-reminder,https://www.rider.edu/tuition-aid/financial-aid/professional-judgment-request
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Learn More Professional Judgment Request Form These adjustments can help to more accurately assess your financial need and may increase your eligibility for federal and/or state need-based financial aid.”
### `fddcfa1e5c3606e5` Rider University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rider.edu/tuition-aid/financial-aid/professional-judgment-request (sha256 15cab6882ef5)
- issues: semantic_review_required, conflicting_sources:https://www.rider.edu/tuition-aid/financial-aid/aid-guide/fafsa-reminder
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Special circumstances are financial situations that may not be accurately reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “However, you should still contact Rider if you have unusual circumstances or expenses that may affect your cost of attendance or other financial aid options.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances / Dependency Override Unusual circumstances may prevent a dependent student from contacting a parent or make contact with a parent unsafe.”
  - sentence: need_based_special_circumstances ⟵ “Students may request a dependency override by completing the 2026-27 Unusual Circumstances Dependency Override Request Form.”
  - sentence: need_based_special_circumstances ⟵ “Complete special circumstance requests are generally reviewed within 14 business days after all required documentation is received.”
  - sentence: need_based_special_circumstances ⟵ “Students experiencing unusual circumstances, homelessness, an unsafe family situation, or an inability to provide parental information should contact One Stop Services immediately, even after the special financial circumstances deadline. 2026-27 Request Forms Special Financial Circumstances Request (PDF) For significant changes in income, employment, family finances, medical or dependent care expe”
### `9cf65a6591bd180d` Rowan College at Burlington County — appeals 2026-27 [new] (source_unlabeled)
- source: https://rcbc.edu/financial-aid (sha256 42c17ccbcbaa)
- issues: semantic_review_required, conflicting_sources:https://rcbc.edu/financial-aid/sap
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If a student is wrongly reported as never attending a class, they can fill out this form to correct it. | Satisfactory Academic Progress (SAP) Appeal & Academic Plan | To appeal your Satisfactory Academic Progress (SAP) status, you must submit the SAP Appeal/Academic Plan form.”
### `c05cc9d0253999bb` Rowan College at Burlington County — appeals 2026-27 [new] (source_unlabeled)
- source: https://rcbc.edu/financial-aid/sap (sha256 0e6318901a2f)
- issues: semantic_review_required, conflicting_sources:https://rcbc.edu/financial-aid
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Important Financial Aid Forms | Satisfactory Academic Progress (SAP) Appeal & Academic Plan | To appeal your Satisfactory Academic Progress (SAP) status, you must submit the SAP Appeal/Academic Plan form.”
  - sentence: sap_appeal ⟵ “Appealing a Financial Aid Suspension If your financial aid is suspended due to not meeting Satisfactory Academic Progress (SAP) standards, you can appeal to get it reinstated.”
  - sentence: sap_appeal ⟵ “Here's what you need to know: Submitting an Appeal: Fill out the SAP Appeal Form found on the Financial Aid page.”
  - sentence: sap_appeal ⟵ “Therefore, if you are filing a Satisfactory Academic Progress (SAP) appeal, you may need to submit those documents again directly to the Financial Aid office.”
  - sentence: sap_appeal ⟵ “If a student is in a SAP suspended status, and is granted academic amnesty, they may file a SAP appeal to have their aid reinstated.”
  - sentence: sap_appeal ⟵ “If you've lost federal student aid eligibility due to unsatisfactory academic progress, you can file a Satisfactory Academic Progress (SAP) appeal.”
### `17951ce2de80c3f7` Rowan College of South Jersey-Cumberland Campus — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/RCSJ-25-26-Dependency-Override-Appeal.pdf (sha256 52a374e4f0df)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “2025-2026 Academic Year Dependency Override Appeal Name: Student ID: Address: Phone: What is a Dependency Override?”
  - sentence: dependency_override ⟵ “In such cases a Dependency Override might be warranted.”
  - sentence: dependency_override ⟵ “What Will Not Qualify for a Dependency Override The following situations will not qualify a student as independent, as per federal regulations set forth by the U.S.”
  - sentence: dependency_override ⟵ “Students submitting a Dependency Override appeal must include all of the following. (Use the check boxes to keep yourself organized.) Your custodial parent has died and the other natural parent is still living or your family situation is unattainable.”
### `4e4024f1e41199ed` Rowan College of South Jersey-Cumberland Campus — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/RCSJ-25-26-Unsatisfactory-Academic-Progress-Status-Appeal.pdf (sha256 edc2e2176308)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students submitting a SAP appeal must include all of the following. 0 Submit a detailed, typed letter outlining the reasons for your appeal; verbal appeals will not be accepted.”
### `83aee969ee3275a0` Rowan College of South Jersey-Cumberland Campus — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/26-27-Dependency-Override-Appeal.pdf (sha256 5bdba50212ca)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Department of Education allows students who are experiencing unusual circumstances to apply for a Dependency Override through an appeal process.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances include abandonment by parents, an abusive family environment that threatens the student’s health or safety, or the student being unable to locate the parents.”
### `923028ee56bc0bc9` Rowan College of South Jersey-Cumberland Campus — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/26-27-Unsatisfactory-Academic-Progress-Appeal.pdf (sha256 e7b44d4ba0e6)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/satisfactory-academic-progress/,https://www.rcsj.edu/wp-content/uploads/Form-26-27-SAP-Academic-Plan.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “2026–2027 Unsatisfactory Academic Progress Appeal Office of Financial Aid Name: _______________________________________________ Student ID: ______________________________ Term: __________________________ What is Satisfactory Academic Progress?”
  - sentence: sap_appeal ⟵ “For a detailed version of the College’s SAP policy 8402 , visit RCSJ.edu/Policies and search “Satisfactory Academic Progress” Instructions for Appeal Process The Office of Financial Aid will review only one appeal per student, per circumstance.”
  - sentence: sap_appeal ⟵ “Students submitting a SAP appeal must include all of the following. 0 Submit a detailed, typed letter outlining the reasons for your appeal; verbal appeals will not be accepted.”
### `a7ffab8ae88331c0` Rowan College of South Jersey-Cumberland Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/satisfactory-academic-progress/ (sha256 9e09d0ef8c42)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/wp-content/uploads/26-27-Unsatisfactory-Academic-Progress-Appeal.pdf,https://www.rcsj.edu/wp-content/uploads/Form-26-27-SAP-Academic-Plan.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Applying for a Satisfactory Academic Appeal Comprehensive instructions are included on the SAP appeal cover letter.”
  - sentence: sap_appeal ⟵ “Expand All + Collapse All - SAP Appeal Cover Letter Detailed, written statement outlining the reasons for the appeal.”
  - sentence: sap_appeal ⟵ “Denied Appeals Students whose SAP appeals are denied will need to use an alternative method of payment for the semester because they are ineligible to receive federal and state aid.”
  - sentence: sap_appeal ⟵ “SAP Appeal form For More Information Contact Financial Aid 856-415-2210 (phone & text) [email protected] Connect with RCSJ Contact Us Access Resources Accreditation and Effectiveness Compliance and Safety Human Resources and Career Opportunities OPRA Legal and Public Notices Direct Links Safety and Security Site Map Find Us Gloucester Campus 1400 Tanyard Road Sewell, NJ 08080 Cumberland Campus 332”
### `afcff35d32529ad7` Rowan College of South Jersey-Cumberland Campus — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/26-27-Dependency-Override-Appeal.pdf (sha256 5bdba50212ca)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “2026-2027 Dependency Override Appeal Office of Financial Aid Name: Student ID: What is a Dependency Override?”
  - sentence: dependency_override ⟵ “In such cases a Dependency Override might be warranted.”
  - sentence: dependency_override ⟵ “What Will Not Qualify for a Dependency Override The following situations will not qualify a student as independent, as per federal regulations set forth by the U.S.”
  - sentence: dependency_override ⟵ “Students submitting a Dependency Override Appeal must include all of the following. (Use the check boxes to keep yourself organized.) Your custodial parent has died and the other natural parent is still living or your family situation is unattainable.”
### `b48c64a5256b24de` Rowan College of South Jersey-Cumberland Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/ (sha256 0939eea08729)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/wp-content/uploads/26-27-Dependency-Override-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Learn More Unusual Circumstances Assistance available for students experiencing unusual financial hardships.”
### `c6f2c38214cd4d41` Rowan College of South Jersey-Cumberland Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rcsj.edu/wp-content/uploads/Form-26-27-SAP-Academic-Plan.pdf (sha256 b7a15d0732f1)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/satisfactory-academic-progress/,https://www.rcsj.edu/wp-content/uploads/26-27-Unsatisfactory-Academic-Progress-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (S.A.P) Plan Office of Financial Aid Student Name: ____________________________ Student ID #: _____________ Phone #: ________________________ The Rowan College of South Jersey’s Office of Financial Aid has approved your SAP Appeal.”
### `dfc034f3e67cd41a` Rowan College of South Jersey-Cumberland Campus — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/RCSJ-25-26-Dependency-Override-Appeal.pdf (sha256 52a374e4f0df)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Department of Education allows students who are experiencing unusual circumstances to apply for a Dependency Override through an appeal process.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances include abandonment by parents, an abusive family environment that threatens the student’s health or safety, or the student being unable to locate the parents.”
### `5356f37398aa1448` Rowan College of South Jersey-Cumberland Campus — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_url)
- source: https://www.rcsj.edu/wp-content/uploads/AP-Exam-Course-Equivalency-2025-2026.pdf (sha256 d4f500498dc7)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"distinct_exams": 36, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art & Design                          ARTS 129 - 2-Dimensional Design                      3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art & Design                          ARTS 209 - 3-Dimensional Design                      3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                                   ARTS 105 - Drawing I                                 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                               ARTS 103 - Art History I                             3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                              MUSI 120 - Music Theory I                            3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition            ENGL 101 - English Composition I                     3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition          ENGL 102 - English Composition II                    3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies                  HIST 117 - African American History                  3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics         POLS 201 - Introduction to Comparative Politics      3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                           GEGR 102 - Cultural Geography                        3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                            ECON 101 - Principles of Economics: Macro            3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                            ECON 102 - Principles of Economics: Micro            3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                PSYC 101 - General Psychology                        3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government & Politics       POLS 101 - American Federal Government               3”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB                               MATH 130 - Calculus I                                4”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                               MATH 140 - Calculus II                               4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A                        CSCI 121 - Introduction to Programming               4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles               CSCI 111 - Computer Science I                        4”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Pre-Calculus                              MATH 120 - Pre-Calculus & Mathematical Analysis      4”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                                MATH 103 - Statistics I                              3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                                   BIOL 101 - General Biology I                         4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                                 CHEM 101 - General Chemistry I                       4”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science                     ENVS 101 - Environmental Science                     4”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1: Algebra-Based                  PHYS 123 - General Physics I                         4”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2: Algebra-Based                  PHYS 124 - General Physics II                        4”
  - … 11 more rows
### `fa15a0f5ae53a4a2` Rowan College of South Jersey-Cumberland Campus — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.rcsj.edu/wp-content/uploads/AP-Exam-course-equivalencies.pdf (sha256 6d3a6971b014)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 33, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art & Design                          ARTS 129 - 2-Dimensional Design                      3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art & Design                          ARTS 209 - 3-Dimensional Design                      3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                                   ARTS 105 - Drawing I                                 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                               ARTS 103 - Art History I                             3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                              MUSI 120 - Music Theory I                            3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition            ENGL 101 - English Composition I                     3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition          ENGL 102 - English Composition II                    3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies                  HIST 117 - African American History                  3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics         POLS 201 - Introduction to Comparative Politics      3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                           GEGR 102 - Cultural Geography                        3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                            ECON 101 - Principles of Economics: Macro            3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                            ECON 102 - Principles of Economics: Micro            3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                PSYC 101 - General Psychology                        3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government & Politics       POLS 101 - American Federal Government               3”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB                               MATH 130 - Calculus I                                4”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                               MATH 140 - Calculus II                               4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A                        CSCI 121 - Introduction to Programming               4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles               CSCI 111 - Computer Science I                        4”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Pre-Calculus                              MATH 120 - Pre-Calculus & Mathematical Analysis      4”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                                MATH 103 - Statistics I                              3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                                   BIOL 101 - General Biology I                         4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                                 CHEM 101 - General Chemistry I                       4”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science                     ENVS 101 - Environmental Science                     4”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1: Algebra-Based                  PHYS 123 - General Physics I                         4”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2: Algebra-Based                  PHYS 124 - General Physics II                        4”
  - … 8 more rows
### `0246361a47a1a7fc` Rowan College of South Jersey-Gloucester Campus — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/RCSJ-25-26-Unsatisfactory-Academic-Progress-Status-Appeal.pdf (sha256 edc2e2176308)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students submitting a SAP appeal must include all of the following. 0 Submit a detailed, typed letter outlining the reasons for your appeal; verbal appeals will not be accepted.”
### `10381fd1da827753` Rowan College of South Jersey-Gloucester Campus — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/RCSJ-25-26-Dependency-Override-Appeal.pdf (sha256 52a374e4f0df)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Department of Education allows students who are experiencing unusual circumstances to apply for a Dependency Override through an appeal process.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances include abandonment by parents, an abusive family environment that threatens the student’s health or safety, or the student being unable to locate the parents.”
### `39af3503d6b4eef5` Rowan College of South Jersey-Gloucester Campus — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/26-27-Unsatisfactory-Academic-Progress-Appeal.pdf (sha256 e7b44d4ba0e6)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/satisfactory-academic-progress/,https://www.rcsj.edu/wp-content/uploads/Form-26-27-SAP-Academic-Plan.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “2026–2027 Unsatisfactory Academic Progress Appeal Office of Financial Aid Name: _______________________________________________ Student ID: ______________________________ Term: __________________________ What is Satisfactory Academic Progress?”
  - sentence: sap_appeal ⟵ “For a detailed version of the College’s SAP policy 8402 , visit RCSJ.edu/Policies and search “Satisfactory Academic Progress” Instructions for Appeal Process The Office of Financial Aid will review only one appeal per student, per circumstance.”
  - sentence: sap_appeal ⟵ “Students submitting a SAP appeal must include all of the following. 0 Submit a detailed, typed letter outlining the reasons for your appeal; verbal appeals will not be accepted.”
### `562a8c2b28d348ad` Rowan College of South Jersey-Gloucester Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/satisfactory-academic-progress/ (sha256 b7148a22e870)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/wp-content/uploads/26-27-Unsatisfactory-Academic-Progress-Appeal.pdf,https://www.rcsj.edu/wp-content/uploads/Form-26-27-SAP-Academic-Plan.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Applying for a Satisfactory Academic Appeal Comprehensive instructions are included on the SAP appeal cover letter.”
  - sentence: sap_appeal ⟵ “Expand All + Collapse All - SAP Appeal Cover Letter Detailed, written statement outlining the reasons for the appeal.”
  - sentence: sap_appeal ⟵ “Denied Appeals Students whose SAP appeals are denied will need to use an alternative method of payment for the semester because they are ineligible to receive federal and state aid.”
  - sentence: sap_appeal ⟵ “SAP Appeal form For More Information Contact Financial Aid 856-415-2210 (phone & text) [email protected] Connect with RCSJ Contact Us Access Resources Accreditation and Effectiveness Compliance and Safety Human Resources and Career Opportunities OPRA Legal and Public Notices Direct Links Safety and Security Site Map Find Us Gloucester Campus 1400 Tanyard Road Sewell, NJ 08080 Cumberland Campus 332”
### `6af6e027a3c12e9b` Rowan College of South Jersey-Gloucester Campus — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/26-27-Dependency-Override-Appeal.pdf (sha256 5bdba50212ca)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “2026-2027 Dependency Override Appeal Office of Financial Aid Name: Student ID: What is a Dependency Override?”
  - sentence: dependency_override ⟵ “In such cases a Dependency Override might be warranted.”
  - sentence: dependency_override ⟵ “What Will Not Qualify for a Dependency Override The following situations will not qualify a student as independent, as per federal regulations set forth by the U.S.”
  - sentence: dependency_override ⟵ “Students submitting a Dependency Override Appeal must include all of the following. (Use the check boxes to keep yourself organized.) Your custodial parent has died and the other natural parent is still living or your family situation is unattainable.”
### `9c96f616cbb7dbe8` Rowan College of South Jersey-Gloucester Campus — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/RCSJ-25-26-Dependency-Override-Appeal.pdf (sha256 52a374e4f0df)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “2025-2026 Academic Year Dependency Override Appeal Name: Student ID: Address: Phone: What is a Dependency Override?”
  - sentence: dependency_override ⟵ “In such cases a Dependency Override might be warranted.”
  - sentence: dependency_override ⟵ “What Will Not Qualify for a Dependency Override The following situations will not qualify a student as independent, as per federal regulations set forth by the U.S.”
  - sentence: dependency_override ⟵ “Students submitting a Dependency Override appeal must include all of the following. (Use the check boxes to keep yourself organized.) Your custodial parent has died and the other natural parent is still living or your family situation is unattainable.”
### `cc165c7e28c0b8a5` Rowan College of South Jersey-Gloucester Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rcsj.edu/wp-content/uploads/Form-26-27-SAP-Academic-Plan.pdf (sha256 b7a15d0732f1)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/satisfactory-academic-progress/,https://www.rcsj.edu/wp-content/uploads/26-27-Unsatisfactory-Academic-Progress-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (S.A.P) Plan Office of Financial Aid Student Name: ____________________________ Student ID #: _____________ Phone #: ________________________ The Rowan College of South Jersey’s Office of Financial Aid has approved your SAP Appeal.”
### `cdbc2ebef0e51634` Rowan College of South Jersey-Gloucester Campus — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.rcsj.edu/wp-content/uploads/26-27-Dependency-Override-Appeal.pdf (sha256 5bdba50212ca)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Department of Education allows students who are experiencing unusual circumstances to apply for a Dependency Override through an appeal process.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances include abandonment by parents, an abusive family environment that threatens the student’s health or safety, or the student being unable to locate the parents.”
### `f5ed3ec23b7e39c2` Rowan College of South Jersey-Gloucester Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rcsj.edu/admissions-aid/paying-for-college/financial-aid/ (sha256 5c4846b22088)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.rcsj.edu/wp-content/uploads/26-27-Dependency-Override-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Learn More Unusual Circumstances Assistance available for students experiencing unusual financial hardships.”
### `43fb6da49a01c942` Rowan College of South Jersey-Gloucester Campus — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.rcsj.edu/wp-content/uploads/AP-Exam-course-equivalencies.pdf (sha256 6d3a6971b014)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 33, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art & Design                          ARTS 129 - 2-Dimensional Design                      3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art & Design                          ARTS 209 - 3-Dimensional Design                      3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                                   ARTS 105 - Drawing I                                 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                               ARTS 103 - Art History I                             3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                              MUSI 120 - Music Theory I                            3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition            ENGL 101 - English Composition I                     3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition          ENGL 102 - English Composition II                    3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies                  HIST 117 - African American History                  3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics         POLS 201 - Introduction to Comparative Politics      3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                           GEGR 102 - Cultural Geography                        3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                            ECON 101 - Principles of Economics: Macro            3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                            ECON 102 - Principles of Economics: Micro            3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                PSYC 101 - General Psychology                        3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government & Politics       POLS 101 - American Federal Government               3”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB                               MATH 130 - Calculus I                                4”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                               MATH 140 - Calculus II                               4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A                        CSCI 121 - Introduction to Programming               4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles               CSCI 111 - Computer Science I                        4”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Pre-Calculus                              MATH 120 - Pre-Calculus & Mathematical Analysis      4”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                                MATH 103 - Statistics I                              3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                                   BIOL 101 - General Biology I                         4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                                 CHEM 101 - General Chemistry I                       4”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science                     ENVS 101 - Environmental Science                     4”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1: Algebra-Based                  PHYS 123 - General Physics I                         4”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2: Algebra-Based                  PHYS 124 - General Physics II                        4”
  - … 8 more rows
### `a9f1df6a8cd22948` Rowan College of South Jersey-Gloucester Campus — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_url)
- source: https://www.rcsj.edu/wp-content/uploads/AP-Exam-Course-Equivalency-2025-2026.pdf (sha256 d4f500498dc7)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"distinct_exams": 36, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art & Design                          ARTS 129 - 2-Dimensional Design                      3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art & Design                          ARTS 209 - 3-Dimensional Design                      3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                                   ARTS 105 - Drawing I                                 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                               ARTS 103 - Art History I                             3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                              MUSI 120 - Music Theory I                            3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition            ENGL 101 - English Composition I                     3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition          ENGL 102 - English Composition II                    3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies                  HIST 117 - African American History                  3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics         POLS 201 - Introduction to Comparative Politics      3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                           GEGR 102 - Cultural Geography                        3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                            ECON 101 - Principles of Economics: Macro            3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                            ECON 102 - Principles of Economics: Micro            3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                PSYC 101 - General Psychology                        3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government & Politics       POLS 101 - American Federal Government               3”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB                               MATH 130 - Calculus I                                4”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                               MATH 140 - Calculus II                               4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A                        CSCI 121 - Introduction to Programming               4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles               CSCI 111 - Computer Science I                        4”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Pre-Calculus                              MATH 120 - Pre-Calculus & Mathematical Analysis      4”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                                MATH 103 - Statistics I                              3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                                   BIOL 101 - General Biology I                         4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                                 CHEM 101 - General Chemistry I                       4”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science                     ENVS 101 - Environmental Science                     4”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1: Algebra-Based                  PHYS 123 - General Physics I                         4”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2: Algebra-Based                  PHYS 124 - General Physics II                        4”
  - … 11 more rows
### `0161362164a5e8df` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/sap-policy.html (sha256 8f9865e74483)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/appeal.html,https://sites.rowan.edu/financial-aid/tuition-free/faq.html,https://www.rowan.edu/tbes/admissions-and-aid/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Probation Continuing students are placed on financial aid probation after having a SAP appeal completed and approved.”
### `02faf4ad646f67c3` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/tuition-free/faq.html (sha256 49276c6f0b3c)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/appeals/dependency.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “If you meet one of the criteria to be considered an independent student on the FAFSA, and so were not required to include parental information on the FAFSA; or you are approved for a dependency status appeal, then we will use your AGI to determine eligibility.”
### `0ebad99004ec04a0` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/appeals/ (sha256 eb53b1f5b9e3)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/appeal.html,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/sap-policy.html,https://sites.rowan.edu/financial-aid/tuition-free/faq.html,https://www.rowan.edu/tbes/admissions-and-aid/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Students who have been notified by our office that are not meeting Satisfactory Academic Progress (SAP), should consider this appeal.”
### `1a5821896db59524` Rowan University — appeals 2026-27 [new] (labeled_in_source)
- source: https://svm.rowan.edu/admissions-menu/financial-aid/cost-of-attendance.html (sha256 1b4b91fb262d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Cost of Attendance Appeals (Budget Adjustment Appeal) What is a Cost of Attendance (COA) Appeal?”
  - sentence: budget_increase ⟵ “Important Notes Budget adjustments are based on educational necessity, not lifestyle preferences.”
### `4167dd88147165f0` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/tuition-free/faq.html (sha256 49276c6f0b3c)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/appeal.html,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/sap-policy.html,https://www.rowan.edu/tbes/admissions-and-aid/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “When you re-establish eligibility for financial aid by meeting the standards for Satisfactory Academic Progress (SAP) or successfully appeal your SAP aid suspension, you will regain eligibility for the Rowan Opportunity Program/Garden State Guarantee as well.”
### `7263a2514f7c8c47` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/appeals/dependency.html (sha256 2b11c9850a47)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Federal guidelines stipulate the following conditions do not solely qualify as circumstances meriting a dependency override: Parent refusal to contribute to the student’s education Parent unwillingness to provide information on the FAFSA or to provide required verification documentation Parent does not claim the student as a dependent for income tax purposes Student demonstrates total self-suffici”
### `80876dc92681b696` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/appeal.html (sha256 264c49121118)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/sap-policy.html,https://sites.rowan.edu/financial-aid/tuition-free/faq.html,https://www.rowan.edu/tbes/admissions-and-aid/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Select the Reason for your Appeal SAP Appeal for GPA and/or PACE The appeal process requires the student to explain the circumstances that prevented you from meeting SAP requirements.”
  - sentence: sap_appeal ⟵ “SAP Appeal for Maximum Timeframe The appeal process requires a personal statement explaining why you have not yet completed your degree program.”
  - sentence: sap_appeal ⟵ “This form must be uploaded to your SAP appeal in your online portal.”
### `8ff0d2491bd5428b` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/appeals/ (sha256 eb53b1f5b9e3)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/dependency.html,https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency Status Appeal Students who are unable to provide parents' information on their FAFSA, should consider this appeal.”
### `969c06706005d81b` Rowan University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rowan.edu/tbes/admissions-and-aid/financial-aid/ (sha256 8fdd06c2c584)
- issues: semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/appeal.html,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/sap-policy.html,https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Complete your FAFSA at studentaid.gov now! 2026-2027 Financial Aid Disbursement Dates - TBES | Term | Disbursement Date | Fall 2026 | August 23, 2026 | Spring 2027 | January 10, 2027 | Summer 2027 | May 2, 2027 Policies and Procedures Satisfactory Academic Progress Policy Satisfactory Academic Progress Academic Plan Appealing Your Financial Aid Suspension Copyright ©2026.”
### `be3980bfc3ebc0c5` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/tuition-free/faq.html (sha256 49276c6f0b3c)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/income-adjustment.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “When the family circumstances change, you may qualify to have your aid eligibility reconsidered through an appeal process known as professional judgment.”
### `ebbb1f3e3bb88e10` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/appeals/income-adjustment.html (sha256 92c5feef44d8)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “These types of adjustments are made in accordance with our Professional Judgment Policy on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “Once in the system, click on “Request” at the top, right corner of the page then select "Professional Judgment: Special Circumstance EFC/SAI Appeal." If multiple award years are open, please pay special attention to the award year for which you are submitting an appeal.”
### `0415811e3f85ae46` Rowan University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://cmsru.rowan.edu/admissions/financial-aid-services/cost-of-attendance.html (sha256 737ad8fe0c1d)
- issues: conflicting_sources:https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2627.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition*: 50680 ⟵ “Tuition* | $50,680 | $78,086 | ”
  - on_campus:Student Fees*: 2641 ⟵ “Student Fees* | $2,641 | $2,641 | ”
  - on_campus:Direct Loan Origination Fee: 528 ⟵ “Direct Loan Origination Fee | $528 | $528 | ”
  - on_campus:Books & Supplies: 1600 ⟵ “Books & Supplies | $1,600 | $1,600 | ”
  - on_campus:Food & Housing**: 24200 ⟵ “Food & Housing** | $24,200 | $24,200 | ”
  - on_campus:Transportation: 4950 ⟵ “Transportation | $4,950 | $4,950 | ”
  - on_campus:Personal: 2200 ⟵ “Personal | $2,200 | $2,200 | ”
  - on_campus:Total: 86799 ⟵ “Total | $86,799 | $114,205 | ”
### `26f28739d2bc9bd4` Rowan University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2627.html (sha256 86f2496805f3)
- issues: conflicting_sources:https://cmsru.rowan.edu/admissions/financial-aid-services/cost-of-attendance.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition & Fees: 18300 ⟵ “Tuition & Fees | $18,300”
  - column:Books, Course Materials, Supplies, Equipment: 1330 ⟵ “Books, Course Materials, Supplies, Equipment | $1,330”
  - column:Housing: 11897 ⟵ “Housing | $11,897”
  - column:Food: 5693 ⟵ “Food | $5,693”
  - column:Personal Spending: 3080 ⟵ “Personal Spending | $3,080”
  - column:Transportation Expenses: 2322 ⟵ “Transportation Expenses | $2,322”
  - column:Federal Loan Fees: 44 ⟵ “Federal Loan Fees | $44”
  - column:TOTAL: 42666 ⟵ “TOTAL | $42,666”
### `8724e4ed3321ad80` Rowan University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2526.html (sha256 48a4c47a67df)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 8}
  - column:Tuition & Fees: 28252 ⟵ “Tuition & Fees | 28,252”
  - column:Books, Course Materials, Supplies, Equipment: 1330 ⟵ “Books, Course Materials, Supplies, Equipment | 1,330”
  - column:Housing: 11550 ⟵ “Housing | 11,550”
  - column:Food: 5474 ⟵ “Food | 5,474”
  - column:Personal Spending: 2993 ⟵ “Personal Spending | 2,993”
  - column:Transportation Expenses: 3549 ⟵ “Transportation Expenses | 3,549”
  - column:Federal Loan Fees: 44 ⟵ “Federal Loan Fees | 44”
  - column:TOTALS: 53192 ⟵ “TOTALS | 53,192”
### `dbcabeb1e11cba21` Rowan University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2526.html (sha256 48a4c47a67df)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition & Fees: 17428 ⟵ “Tuition & Fees | 17,428”
  - column:Books, Course Materials, Supplies, Equipment: 1330 ⟵ “Books, Course Materials, Supplies, Equipment | 1,330”
  - column:Housing: 11550 ⟵ “Housing | 11,550”
  - column:Food: 5474 ⟵ “Food | 5,474”
  - column:Personal Spending: 2993 ⟵ “Personal Spending | 2,993”
  - column:Transportation Expenses: 2345 ⟵ “Transportation Expenses | 2,345”
  - column:Federal Loan Fees: 44 ⟵ “Federal Loan Fees | 44”
  - column:TOTAL: 41164 ⟵ “TOTAL | 41,164”
### `efed38a72b840ae6` Rowan University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://cmsru.rowan.edu/admissions/financial-aid-services/cost-of-attendance.html (sha256 737ad8fe0c1d)
- issues: conflicting_sources:https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2627.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition*: 78086 ⟵ “Tuition* | $50,680 | $78,086 | ”
  - on_campus:Student Fees*: 2641 ⟵ “Student Fees* | $2,641 | $2,641 | ”
  - on_campus:Direct Loan Origination Fee: 528 ⟵ “Direct Loan Origination Fee | $528 | $528 | ”
  - on_campus:Books & Supplies: 1600 ⟵ “Books & Supplies | $1,600 | $1,600 | ”
  - on_campus:Food & Housing**: 24200 ⟵ “Food & Housing** | $24,200 | $24,200 | ”
  - on_campus:Transportation: 4950 ⟵ “Transportation | $4,950 | $4,950 | ”
  - on_campus:Personal: 2200 ⟵ “Personal | $2,200 | $2,200 | ”
  - on_campus:Total: 114205 ⟵ “Total | $86,799 | $114,205 | ”
### `fe80f915312f5d3a` Rowan University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2627.html (sha256 86f2496805f3)
- issues: conflicting_sources:https://cmsru.rowan.edu/admissions/financial-aid-services/cost-of-attendance.html
- checks: {"columns": 1, "rows": 8}
  - column:Tuition & Fees: 29664 ⟵ “Tuition & Fees | $29,664”
  - column:Books, Course Materials, Supplies, Equipment: 1330 ⟵ “Books, Course Materials, Supplies, Equipment | $1,330”
  - column:Housing: 11897 ⟵ “Housing | $11,897”
  - column:Food: 5693 ⟵ “Food | $5,693”
  - column:Personal Spending: 3080 ⟵ “Personal Spending | $3,080”
  - column:Transportation Expenses: 2922 ⟵ “Transportation Expenses | $2,922”
  - column:Federal Loan Fees: 44 ⟵ “Federal Loan Fees | $44”
  - column:TOTALS: 54630 ⟵ “TOTALS | $54,630”
### `3a32698f4cd897ac` Rutgers University-Camden — appeals 2026-27 [new] (source_unlabeled)
- source: https://scarlethub.rutgers.edu/financial-services/eligibility/satisfactory-academic-progress-sap/ (sha256 5b2d18c2d771)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If the student was not meeting satisfactory academic progress when they last attended Rutgers, they must (if qualified) file an appeal and obtain an academic plan.”
  - sentence: sap_appeal ⟵ “Second SAP Appeal Guidelines A second Satisfactory Academic Progress (SAP) appeal is considered only for extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Approval of a second SAP appeal is not guaranteed and is reviewed on a case-by-case basis.”
  - sentence: sap_appeal ⟵ “Eligibility for a Second SAP Appeal For consideration of a second SAP appeal, the student’s circumstances must meet the threshold for extenuating circumstances.”
### `1d10257c02935c32` Rutgers University-Camden — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000. ⟵ “Raptor Achievement | Arts and Sciences, School of Business | Up to $1,000. | Up to $4,000.”
### `4631559faf1c71ad` Rutgers University-Camden — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $6,000. ⟵ “Outstanding Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $6,000. | Up to $24,000.”
### `46a8c483f17fb253` Rutgers University-Camden — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,500. ⟵ “Academic Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $2,500. | Up to $10,000.”
### `489b89a67d6cafd2` Rutgers University-Camden — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000. ⟵ “Meritorious Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $5,000. | Up to $20,000.”
### `9dba502b979e21e3` Rutgers University-Camden — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,500. ⟵ “Honorable Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $3,500. | Up to $14,000.”
### `f34ead8dc44640db` Rutgers University-Camden — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $7,500. ⟵ “Distinguished Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $7,500. | Up to $30,000.”
### `187967173b16adec` Rutgers University-Camden — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://scarlethub.rutgers.edu/financial-services/cost-of-attendance/rutgers-students-cost-of-attendance-2025-2026/ (sha256 056c84239516)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 14933 ⟵ “Tuition | $14,933 | $14,933 | $14,933”
  - on_campus:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - on_campus:Room & Board: 15332 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - on_campus:Sub-total of direct charges*: 34156 ⟵ “Sub-total of direct charges* | $34,156 | $24,650 | $37,982”
  - on_campus:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - on_campus:Travel: 986 ⟵ “Travel | $986 | $3,580 | $2,864”
  - on_campus:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - on_campus:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - on_campus:Total: 40260 ⟵ “Total | $40,260 | $33,348 | $51,774”
  - with_parents_or_family:Tuition: 14933 ⟵ “Tuition | $14,933 | $14,933 | $14,933”
  - with_parents_or_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - with_parents_or_family:Room & Board: 5826 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - with_parents_or_family:Sub-total of direct charges*: 24650 ⟵ “Sub-total of direct charges* | $34,156 | $24,650 | $37,982”
  - with_parents_or_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - with_parents_or_family:Travel: 3580 ⟵ “Travel | $986 | $3,580 | $2,864”
  - with_parents_or_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - with_parents_or_family:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - with_parents_or_family:Total: 33348 ⟵ “Total | $40,260 | $33,348 | $51,774”
  - off_campus_not_with_family:Tuition: 14933 ⟵ “Tuition | $14,933 | $14,933 | $14,933”
  - off_campus_not_with_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - off_campus_not_with_family:Room & Board: 19158 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - off_campus_not_with_family:Sub-total of direct charges*: 37982 ⟵ “Sub-total of direct charges* | $34,156 | $24,650 | $37,982”
  - off_campus_not_with_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - off_campus_not_with_family:Travel: 2864 ⟵ “Travel | $986 | $3,580 | $2,864”
  - off_campus_not_with_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - … 2 more rows
### `6cf6664dfd646a09` Rutgers University-Camden — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://scarlethub.rutgers.edu/financial-services/cost-of-attendance/rutgers-students-cost-of-attendance-2025-2026/ (sha256 056c84239516)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 35758 ⟵ “Tuition | $35,758 | $35,758 | $35,758”
  - on_campus:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - on_campus:Room & Board: 15332 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - on_campus:Sub-total of direct charges*: 54981 ⟵ “Sub-total of direct charges* | $54,981 | $45,475 | $58,807”
  - on_campus:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - on_campus:Travel: 1536 ⟵ “Travel | $1,536 | $3,580 | $2,864”
  - on_campus:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - on_campus:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - on_campus:Total: 61635 ⟵ “Total | $61,635 | $54,173 | $72,599”
  - with_parents_or_family:Tuition: 35758 ⟵ “Tuition | $35,758 | $35,758 | $35,758”
  - with_parents_or_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - with_parents_or_family:Room & Board: 5826 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - with_parents_or_family:Sub-total of direct charges*: 45475 ⟵ “Sub-total of direct charges* | $54,981 | $45,475 | $58,807”
  - with_parents_or_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - with_parents_or_family:Travel: 3580 ⟵ “Travel | $1,536 | $3,580 | $2,864”
  - with_parents_or_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - with_parents_or_family:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - with_parents_or_family:Total: 54173 ⟵ “Total | $61,635 | $54,173 | $72,599”
  - off_campus_not_with_family:Tuition: 35758 ⟵ “Tuition | $35,758 | $35,758 | $35,758”
  - off_campus_not_with_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - off_campus_not_with_family:Room & Board: 19158 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - off_campus_not_with_family:Sub-total of direct charges*: 58807 ⟵ “Sub-total of direct charges* | $54,981 | $45,475 | $58,807”
  - off_campus_not_with_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - off_campus_not_with_family:Travel: 2864 ⟵ “Travel | $1,536 | $3,580 | $2,864”
  - off_campus_not_with_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - … 2 more rows
### `ed0ae2ee90ac28d2` Rutgers University-Camden — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.rutgers.edu/costs-and-aid/tuition-fees (sha256 6402463b2be6)
- issues: shared_site_attribution_review
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - with_parents_or_family:Tuition: 15381 ⟵ “Tuition | $15,381 | $15,381”
  - with_parents_or_family:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - with_parents_or_family:Food and Housing: 6060 ⟵ “Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total: 25270 ⟵ “Total | $25,270 | $41,153”
  - on_campus:Tuition: 15381 ⟵ “Tuition | $15,381 | $15,381”
  - on_campus:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - on_campus:Food and Housing: 21943 ⟵ “Food and Housing | $6,060 | $21,943”
  - on_campus:Total: 41153 ⟵ “Total | $25,270 | $41,153”
### `fa117989cd7ec2e0` Rutgers University-Camden — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/sites/default/files/2026-08/2026%20Financing%20Your%20Education%20Brochure.pdf (sha256 18bb1cc4c48e)
- issues: ambiguous_year_labels, arrangement_unlabeled, multiple_total_rows, residency_unknown, shared_site_attribution_review
- checks: {"columns": 4, "rows": 12}
  - with_parents_or_family:Tuition*: 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - with_parents_or_family:Fees*: 3829 ⟵ “Fees* | $3,829 | $3,829 | Fees*^ | $3,829 | $3,829”
  - with_parents_or_family:Food and Housing: 6060 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total: 25270 ⟵ “Total | $25,270 | $41,153 | Total | $46,720 | $62,603”
  - with_parents_or_family:Tuition* (2): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - with_parents_or_family:Fees* (2): 3275 ⟵ “Fees* | $3,275 | $3,275 | Fees*^ | $3,275 | $3,275”
  - with_parents_or_family:Food and Housing (2): 6060 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total (2): 24716 ⟵ “Total | $24,716 | $40,599 | Total | $46,166 | $62,049”
  - with_parents_or_family:Tuition* (3): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - with_parents_or_family:Fees* (3): 4008 ⟵ “Fees* | $4,008 | $4,008 | Fees*^ | $4,008 | $4,008”
  - with_parents_or_family:Food and Housing (3): 6060 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total (3): 25449 ⟵ “Total | $25,449 | $41,332 | Total | $46,899 | $62,782”
  - on_campus:Tuition*: 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - on_campus:Fees*: 3829 ⟵ “Fees* | $3,829 | $3,829 | Fees*^ | $3,829 | $3,829”
  - on_campus:Food and Housing: 21943 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - on_campus:Total: 41153 ⟵ “Total | $25,270 | $41,153 | Total | $46,720 | $62,603”
  - on_campus:Tuition* (2): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - on_campus:Fees* (2): 3275 ⟵ “Fees* | $3,275 | $3,275 | Fees*^ | $3,275 | $3,275”
  - on_campus:Food and Housing (2): 21943 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - on_campus:Total (2): 40599 ⟵ “Total | $24,716 | $40,599 | Total | $46,166 | $62,049”
  - on_campus:Tuition* (3): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - on_campus:Fees* (3): 4008 ⟵ “Fees* | $4,008 | $4,008 | Fees*^ | $4,008 | $4,008”
  - on_campus:Food and Housing (3): 21943 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - on_campus:Total (3): 41332 ⟵ “Total | $25,449 | $41,332 | Total | $46,899 | $62,782”
  - on_campus:Tuition*: 36831 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - … 23 more rows
### `m36776aae63fbdb8` Rutgers University-Camden — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/transfer-students (sha256 8fc93682f6a0)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Transfer credit is awarded for courses completed at accredited colleges and institutions with a grade of C or better.”
  - min_grade: C ⟵ “Transfer credit is awarded for courses completed at accredited colleges and institutions with a grade of C or better.”
### `20bbd4e1e6d501a1` Rutgers University-New Brunswick — appeals 2026-27 [new] (source_unlabeled)
- source: https://scarlethub.rutgers.edu/financial-services/eligibility/satisfactory-academic-progress-sap/ (sha256 5b2d18c2d771)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If the student was not meeting satisfactory academic progress when they last attended Rutgers, they must (if qualified) file an appeal and obtain an academic plan.”
  - sentence: sap_appeal ⟵ “Second SAP Appeal Guidelines A second Satisfactory Academic Progress (SAP) appeal is considered only for extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Approval of a second SAP appeal is not guaranteed and is reviewed on a case-by-case basis.”
  - sentence: sap_appeal ⟵ “Eligibility for a Second SAP Appeal For consideration of a second SAP appeal, the student’s circumstances must meet the threshold for extenuating circumstances.”
### `00ba6f1e24771905` Rutgers University-New Brunswick — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $7,500. ⟵ “Distinguished Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $7,500. | Up to $30,000.”
### `1be9ef5c520f2b2c` Rutgers University-New Brunswick — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,500. ⟵ “Academic Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $2,500. | Up to $10,000.”
### `a60a01a46b4ef279` Rutgers University-New Brunswick — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $6,000. ⟵ “Outstanding Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $6,000. | Up to $24,000.”
### `b64be4eb13581e2a` Rutgers University-New Brunswick — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,500. ⟵ “Honorable Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $3,500. | Up to $14,000.”
### `b8dcbf035fe24f80` Rutgers University-New Brunswick — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000. ⟵ “Raptor Achievement | Arts and Sciences, School of Business | Up to $1,000. | Up to $4,000.”
### `f1c9e09fa2eba0ae` Rutgers University-New Brunswick — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000. ⟵ “Meritorious Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $5,000. | Up to $20,000.”
### `00b41849acf749f6` Rutgers University-New Brunswick — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.rutgers.edu/costs-and-aid/tuition-fees (sha256 6402463b2be6)
- issues: shared_site_attribution_review
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - with_parents_or_family:Tuition: 15381 ⟵ “Tuition | $15,381 | $15,381”
  - with_parents_or_family:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - with_parents_or_family:Food and Housing: 6060 ⟵ “Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total: 25270 ⟵ “Total | $25,270 | $41,153”
  - on_campus:Tuition: 15381 ⟵ “Tuition | $15,381 | $15,381”
  - on_campus:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - on_campus:Food and Housing: 21943 ⟵ “Food and Housing | $6,060 | $21,943”
  - on_campus:Total: 41153 ⟵ “Total | $25,270 | $41,153”
### `180d5dbfa34c70a6` Rutgers University-New Brunswick — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/sites/default/files/2026-08/2026%20Financing%20Your%20Education%20Brochure.pdf (sha256 18bb1cc4c48e)
- issues: ambiguous_year_labels, arrangement_unlabeled, multiple_total_rows, residency_unknown, shared_site_attribution_review
- checks: {"columns": 4, "rows": 12}
  - with_parents_or_family:Tuition*: 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - with_parents_or_family:Fees*: 3829 ⟵ “Fees* | $3,829 | $3,829 | Fees*^ | $3,829 | $3,829”
  - with_parents_or_family:Food and Housing: 6060 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total: 25270 ⟵ “Total | $25,270 | $41,153 | Total | $46,720 | $62,603”
  - with_parents_or_family:Tuition* (2): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - with_parents_or_family:Fees* (2): 3275 ⟵ “Fees* | $3,275 | $3,275 | Fees*^ | $3,275 | $3,275”
  - with_parents_or_family:Food and Housing (2): 6060 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total (2): 24716 ⟵ “Total | $24,716 | $40,599 | Total | $46,166 | $62,049”
  - with_parents_or_family:Tuition* (3): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - with_parents_or_family:Fees* (3): 4008 ⟵ “Fees* | $4,008 | $4,008 | Fees*^ | $4,008 | $4,008”
  - with_parents_or_family:Food and Housing (3): 6060 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total (3): 25449 ⟵ “Total | $25,449 | $41,332 | Total | $46,899 | $62,782”
  - on_campus:Tuition*: 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - on_campus:Fees*: 3829 ⟵ “Fees* | $3,829 | $3,829 | Fees*^ | $3,829 | $3,829”
  - on_campus:Food and Housing: 21943 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - on_campus:Total: 41153 ⟵ “Total | $25,270 | $41,153 | Total | $46,720 | $62,603”
  - on_campus:Tuition* (2): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - on_campus:Fees* (2): 3275 ⟵ “Fees* | $3,275 | $3,275 | Fees*^ | $3,275 | $3,275”
  - on_campus:Food and Housing (2): 21943 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - on_campus:Total (2): 40599 ⟵ “Total | $24,716 | $40,599 | Total | $46,166 | $62,049”
  - on_campus:Tuition* (3): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - on_campus:Fees* (3): 4008 ⟵ “Fees* | $4,008 | $4,008 | Fees*^ | $4,008 | $4,008”
  - on_campus:Food and Housing (3): 21943 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - on_campus:Total (3): 41332 ⟵ “Total | $25,449 | $41,332 | Total | $46,899 | $62,782”
  - on_campus:Tuition*: 36831 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - … 23 more rows
### `3d788dd4eac9113a` Rutgers University-New Brunswick — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://scarlethub.rutgers.edu/financial-services/cost-of-attendance/rutgers-students-cost-of-attendance-2025-2026/ (sha256 056c84239516)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 35758 ⟵ “Tuition | $35,758 | $35,758 | $35,758”
  - on_campus:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - on_campus:Room & Board: 15332 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - on_campus:Sub-total of direct charges*: 54981 ⟵ “Sub-total of direct charges* | $54,981 | $45,475 | $58,807”
  - on_campus:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - on_campus:Travel: 1536 ⟵ “Travel | $1,536 | $3,580 | $2,864”
  - on_campus:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - on_campus:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - on_campus:Total: 61635 ⟵ “Total | $61,635 | $54,173 | $72,599”
  - with_parents_or_family:Tuition: 35758 ⟵ “Tuition | $35,758 | $35,758 | $35,758”
  - with_parents_or_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - with_parents_or_family:Room & Board: 5826 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - with_parents_or_family:Sub-total of direct charges*: 45475 ⟵ “Sub-total of direct charges* | $54,981 | $45,475 | $58,807”
  - with_parents_or_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - with_parents_or_family:Travel: 3580 ⟵ “Travel | $1,536 | $3,580 | $2,864”
  - with_parents_or_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - with_parents_or_family:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - with_parents_or_family:Total: 54173 ⟵ “Total | $61,635 | $54,173 | $72,599”
  - off_campus_not_with_family:Tuition: 35758 ⟵ “Tuition | $35,758 | $35,758 | $35,758”
  - off_campus_not_with_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - off_campus_not_with_family:Room & Board: 19158 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - off_campus_not_with_family:Sub-total of direct charges*: 58807 ⟵ “Sub-total of direct charges* | $54,981 | $45,475 | $58,807”
  - off_campus_not_with_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - off_campus_not_with_family:Travel: 2864 ⟵ “Travel | $1,536 | $3,580 | $2,864”
  - off_campus_not_with_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - … 2 more rows
### `4221d8f0e27941ce` Rutgers University-New Brunswick — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://scarlethub.rutgers.edu/financial-services/cost-of-attendance/rutgers-students-cost-of-attendance-2025-2026/ (sha256 056c84239516)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 14933 ⟵ “Tuition | $14,933 | $14,933 | $14,933”
  - on_campus:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - on_campus:Room & Board: 15332 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - on_campus:Sub-total of direct charges*: 34156 ⟵ “Sub-total of direct charges* | $34,156 | $24,650 | $37,982”
  - on_campus:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - on_campus:Travel: 986 ⟵ “Travel | $986 | $3,580 | $2,864”
  - on_campus:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - on_campus:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - on_campus:Total: 40260 ⟵ “Total | $40,260 | $33,348 | $51,774”
  - with_parents_or_family:Tuition: 14933 ⟵ “Tuition | $14,933 | $14,933 | $14,933”
  - with_parents_or_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - with_parents_or_family:Room & Board: 5826 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - with_parents_or_family:Sub-total of direct charges*: 24650 ⟵ “Sub-total of direct charges* | $34,156 | $24,650 | $37,982”
  - with_parents_or_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - with_parents_or_family:Travel: 3580 ⟵ “Travel | $986 | $3,580 | $2,864”
  - with_parents_or_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - with_parents_or_family:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - with_parents_or_family:Total: 33348 ⟵ “Total | $40,260 | $33,348 | $51,774”
  - off_campus_not_with_family:Tuition: 14933 ⟵ “Tuition | $14,933 | $14,933 | $14,933”
  - off_campus_not_with_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - off_campus_not_with_family:Room & Board: 19158 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - off_campus_not_with_family:Sub-total of direct charges*: 37982 ⟵ “Sub-total of direct charges* | $34,156 | $24,650 | $37,982”
  - off_campus_not_with_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - off_campus_not_with_family:Travel: 2864 ⟵ “Travel | $986 | $3,580 | $2,864”
  - off_campus_not_with_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - … 2 more rows
### `ca375dce74719831` Rutgers University-New Brunswick — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.rutgers.edu/costs-and-aid/tuition-fees (sha256 6402463b2be6)
- issues: shared_site_attribution_review
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - with_parents_or_family:Tuition: 36831 ⟵ “Tuition | $36,831 | $36,831”
  - with_parents_or_family:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - with_parents_or_family:Food and Housing: 6060 ⟵ “Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total: 46720 ⟵ “Total | $46,720 | $62,603”
  - on_campus:Tuition: 36831 ⟵ “Tuition | $36,831 | $36,831”
  - on_campus:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - on_campus:Food and Housing: 21943 ⟵ “Food and Housing | $6,060 | $21,943”
  - on_campus:Total: 62603 ⟵ “Total | $46,720 | $62,603”
### `mc13f641e4f820dc` Rutgers University-New Brunswick — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/transfer-students (sha256 8fc93682f6a0)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “Transfer credit is awarded for courses completed at accredited colleges and institutions with a grade of C or better.”
  - min_grade: C ⟵ “Transfer credit is awarded for courses completed at accredited colleges and institutions with a grade of C or better.”
  - min_grade: C ⟵ “Transfer credits may be awarded for courses taken at a regionally accredited college or university with a grade of C or better and are found equivalent to courses offered by Rutgers–Camden.”
### `93d3e99b73edf7fc` Rutgers University-Newark — appeals 2026-27 [new] (source_unlabeled)
- source: https://scarlethub.rutgers.edu/financial-services/eligibility/satisfactory-academic-progress-sap/ (sha256 5b2d18c2d771)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If the student was not meeting satisfactory academic progress when they last attended Rutgers, they must (if qualified) file an appeal and obtain an academic plan.”
  - sentence: sap_appeal ⟵ “Second SAP Appeal Guidelines A second Satisfactory Academic Progress (SAP) appeal is considered only for extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Approval of a second SAP appeal is not guaranteed and is reviewed on a case-by-case basis.”
  - sentence: sap_appeal ⟵ “Eligibility for a Second SAP Appeal For consideration of a second SAP appeal, the student’s circumstances must meet the threshold for extenuating circumstances.”
### `0be6c114b8523421` Rutgers University-Newark — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,500. ⟵ “Academic Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $2,500. | Up to $10,000.”
### `21f2d08b85faea22` Rutgers University-Newark — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $7,500. ⟵ “Distinguished Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $7,500. | Up to $30,000.”
### `68744d77abf9dc4e` Rutgers University-Newark — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,500. ⟵ “Honorable Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $3,500. | Up to $14,000.”
### `8b820bbfc493156e` Rutgers University-Newark — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $6,000. ⟵ “Outstanding Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $6,000. | Up to $24,000.”
### `bf3e50617e8cb9f3` Rutgers University-Newark — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000. ⟵ “Meritorious Achievement | Arts and Sciences, School of Business, School of Nursing | Up to $5,000. | Up to $20,000.”
### `ca5beba78135d75c` Rutgers University-Newark — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/camden-merit-scholarships (sha256 0ac78c099c0e)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000. ⟵ “Raptor Achievement | Arts and Sciences, School of Business | Up to $1,000. | Up to $4,000.”
### `3a6f1531b0bd02a7` Rutgers University-Newark — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/sites/default/files/2026-08/2026%20Financing%20Your%20Education%20Brochure.pdf (sha256 18bb1cc4c48e)
- issues: ambiguous_year_labels, arrangement_unlabeled, multiple_total_rows, residency_unknown, shared_site_attribution_review
- checks: {"columns": 4, "rows": 12}
  - with_parents_or_family:Tuition*: 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - with_parents_or_family:Fees*: 3829 ⟵ “Fees* | $3,829 | $3,829 | Fees*^ | $3,829 | $3,829”
  - with_parents_or_family:Food and Housing: 6060 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total: 25270 ⟵ “Total | $25,270 | $41,153 | Total | $46,720 | $62,603”
  - with_parents_or_family:Tuition* (2): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - with_parents_or_family:Fees* (2): 3275 ⟵ “Fees* | $3,275 | $3,275 | Fees*^ | $3,275 | $3,275”
  - with_parents_or_family:Food and Housing (2): 6060 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total (2): 24716 ⟵ “Total | $24,716 | $40,599 | Total | $46,166 | $62,049”
  - with_parents_or_family:Tuition* (3): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - with_parents_or_family:Fees* (3): 4008 ⟵ “Fees* | $4,008 | $4,008 | Fees*^ | $4,008 | $4,008”
  - with_parents_or_family:Food and Housing (3): 6060 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total (3): 25449 ⟵ “Total | $25,449 | $41,332 | Total | $46,899 | $62,782”
  - on_campus:Tuition*: 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - on_campus:Fees*: 3829 ⟵ “Fees* | $3,829 | $3,829 | Fees*^ | $3,829 | $3,829”
  - on_campus:Food and Housing: 21943 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - on_campus:Total: 41153 ⟵ “Total | $25,270 | $41,153 | Total | $46,720 | $62,603”
  - on_campus:Tuition* (2): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - on_campus:Fees* (2): 3275 ⟵ “Fees* | $3,275 | $3,275 | Fees*^ | $3,275 | $3,275”
  - on_campus:Food and Housing (2): 21943 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - on_campus:Total (2): 40599 ⟵ “Total | $24,716 | $40,599 | Total | $46,166 | $62,049”
  - on_campus:Tuition* (3): 15381 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - on_campus:Fees* (3): 4008 ⟵ “Fees* | $4,008 | $4,008 | Fees*^ | $4,008 | $4,008”
  - on_campus:Food and Housing (3): 21943 ⟵ “Food and Housing | $6,060 | $21,943 | Food and Housing | $6,060 | $21,943”
  - on_campus:Total (3): 41332 ⟵ “Total | $25,449 | $41,332 | Total | $46,899 | $62,782”
  - on_campus:Tuition*: 36831 ⟵ “Tuition* | $15,381 | $15,381 | Tuition*^ | $36,831 | $36,831”
  - … 23 more rows
### `6d1c7746064c09bb` Rutgers University-Newark — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://scarlethub.rutgers.edu/financial-services/cost-of-attendance/rutgers-students-cost-of-attendance-2025-2026/ (sha256 056c84239516)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 14933 ⟵ “Tuition | $14,933 | $14,933 | $14,933”
  - on_campus:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - on_campus:Room & Board: 15332 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - on_campus:Sub-total of direct charges*: 34156 ⟵ “Sub-total of direct charges* | $34,156 | $24,650 | $37,982”
  - on_campus:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - on_campus:Travel: 986 ⟵ “Travel | $986 | $3,580 | $2,864”
  - on_campus:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - on_campus:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - on_campus:Total: 40260 ⟵ “Total | $40,260 | $33,348 | $51,774”
  - with_parents_or_family:Tuition: 14933 ⟵ “Tuition | $14,933 | $14,933 | $14,933”
  - with_parents_or_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - with_parents_or_family:Room & Board: 5826 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - with_parents_or_family:Sub-total of direct charges*: 24650 ⟵ “Sub-total of direct charges* | $34,156 | $24,650 | $37,982”
  - with_parents_or_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - with_parents_or_family:Travel: 3580 ⟵ “Travel | $986 | $3,580 | $2,864”
  - with_parents_or_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - with_parents_or_family:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - with_parents_or_family:Total: 33348 ⟵ “Total | $40,260 | $33,348 | $51,774”
  - off_campus_not_with_family:Tuition: 14933 ⟵ “Tuition | $14,933 | $14,933 | $14,933”
  - off_campus_not_with_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - off_campus_not_with_family:Room & Board: 19158 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - off_campus_not_with_family:Sub-total of direct charges*: 37982 ⟵ “Sub-total of direct charges* | $34,156 | $24,650 | $37,982”
  - off_campus_not_with_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - off_campus_not_with_family:Travel: 2864 ⟵ “Travel | $986 | $3,580 | $2,864”
  - off_campus_not_with_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - … 2 more rows
### `8226394ef6962cf9` Rutgers University-Newark — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://scarlethub.rutgers.edu/financial-services/cost-of-attendance/rutgers-students-cost-of-attendance-2025-2026/ (sha256 056c84239516)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 35758 ⟵ “Tuition | $35,758 | $35,758 | $35,758”
  - on_campus:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - on_campus:Room & Board: 15332 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - on_campus:Sub-total of direct charges*: 54981 ⟵ “Sub-total of direct charges* | $54,981 | $45,475 | $58,807”
  - on_campus:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - on_campus:Travel: 1536 ⟵ “Travel | $1,536 | $3,580 | $2,864”
  - on_campus:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - on_campus:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - on_campus:Total: 61635 ⟵ “Total | $61,635 | $54,173 | $72,599”
  - with_parents_or_family:Tuition: 35758 ⟵ “Tuition | $35,758 | $35,758 | $35,758”
  - with_parents_or_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - with_parents_or_family:Room & Board: 5826 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - with_parents_or_family:Sub-total of direct charges*: 45475 ⟵ “Sub-total of direct charges* | $54,981 | $45,475 | $58,807”
  - with_parents_or_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - with_parents_or_family:Travel: 3580 ⟵ “Travel | $1,536 | $3,580 | $2,864”
  - with_parents_or_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - with_parents_or_family:Miscellaneous: 3562 ⟵ “Miscellaneous | $3,562 | $3,562 | $9,372”
  - with_parents_or_family:Total: 54173 ⟵ “Total | $61,635 | $54,173 | $72,599”
  - off_campus_not_with_family:Tuition: 35758 ⟵ “Tuition | $35,758 | $35,758 | $35,758”
  - off_campus_not_with_family:Fees: 3891 ⟵ “Fees | $3,891 | $3,891 | $3,891”
  - off_campus_not_with_family:Room & Board: 19158 ⟵ “Room & Board | $15,332 | $5,826 | $19,158”
  - off_campus_not_with_family:Sub-total of direct charges*: 58807 ⟵ “Sub-total of direct charges* | $54,981 | $45,475 | $58,807”
  - off_campus_not_with_family:Books: 1446 ⟵ “Books | $1,446 | $1,446 | $1,446”
  - off_campus_not_with_family:Travel: 2864 ⟵ “Travel | $1,536 | $3,580 | $2,864”
  - off_campus_not_with_family:Loans Fees: 110 ⟵ “Loans Fees | $110 | $110 | $110”
  - … 2 more rows
### `8eaa43428c5a00f8` Rutgers University-Newark — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.rutgers.edu/costs-and-aid/tuition-fees (sha256 6402463b2be6)
- issues: shared_site_attribution_review
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - with_parents_or_family:Tuition: 15381 ⟵ “Tuition | $15,381 | $15,381”
  - with_parents_or_family:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - with_parents_or_family:Food and Housing: 6060 ⟵ “Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total: 25270 ⟵ “Total | $25,270 | $41,153”
  - on_campus:Tuition: 15381 ⟵ “Tuition | $15,381 | $15,381”
  - on_campus:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - on_campus:Food and Housing: 21943 ⟵ “Food and Housing | $6,060 | $21,943”
  - on_campus:Total: 41153 ⟵ “Total | $25,270 | $41,153”
### `b13a37492cbc3ca0` Rutgers University-Newark — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.rutgers.edu/costs-and-aid/tuition-fees (sha256 6402463b2be6)
- issues: shared_site_attribution_review
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - with_parents_or_family:Tuition: 36831 ⟵ “Tuition | $36,831 | $36,831”
  - with_parents_or_family:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - with_parents_or_family:Food and Housing: 6060 ⟵ “Food and Housing | $6,060 | $21,943”
  - with_parents_or_family:Total: 46720 ⟵ “Total | $46,720 | $62,603”
  - on_campus:Tuition: 36831 ⟵ “Tuition | $36,831 | $36,831”
  - on_campus:Fees: 3829 ⟵ “Fees | $3,829 | $3,829”
  - on_campus:Food and Housing: 21943 ⟵ “Food and Housing | $6,060 | $21,943”
  - on_campus:Total: 62603 ⟵ “Total | $46,720 | $62,603”
### `mfc340c4561fbdc8` Rutgers University-Newark — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.rutgers.edu/admitted-students/camden (sha256 b3efb1c07763)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “Transfer credit is awarded for courses completed at accredited colleges and institutions with a grade of C or better.”
  - min_grade: C ⟵ “Transfer credit is awarded for courses completed at accredited colleges and institutions with a grade of C or better.”
  - min_grade: C ⟵ “Transfer credits may be awarded for courses taken at a regionally accredited college or university with a grade of C or better and are found equivalent to courses offered by Rutgers–Camden.”
### `4bb7299c33492ba5` Saint Elizabeth University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.steu.edu/admissions/financial-aid/financial-aid-handbook/financial-aid-eligibility-sap.html (sha256 f17f3d19f23f)
- issues: semantic_review_required, conflicting_sources:https://www.steu.edu/admissions/financial-aid/secure-file-upload.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Extenuating circumstances can include, but are not limited to, illness or injury; death of a family member, or other special circumstances.”
### `91564b2388559fe8` Saint Elizabeth University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.steu.edu/admissions/financial-aid/secure-file-upload.html (sha256 b73fc3e4ec61)
- issues: semantic_review_required, conflicting_sources:https://www.steu.edu/admissions/financial-aid/financial-aid-handbook/financial-aid-eligibility-sap.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of documents that can be uploaded: Verification Worksheets Tax Documents Special Circumstances Requests Loan Adjustment Forms Note: files must be in either .pdf, .doc, or .jpg formats.”
### `aef6d301cf3b072e` Saint Elizabeth University — appeals 2024-25 [new] (labeled_in_title)
- source: https://www.steu.edu/files/Special%20Circumstances%20Form%2024-25.pdf (sha256 458a7bc718d6)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “2024-2025 Special Circumstances Request Form Please note that completion of this form does not guarantee a revision of your financial aid award.”
### `f0576104df038292` Saint Elizabeth University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.steu.edu/admissions/tuition-and-fees/undergraduate/tuition.html (sha256 06a654ca38f1)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition*: 35610 ⟵ “Tuition* | $35,610 | $35,610 | $35,610”
  - on_campus:Food & Housing: 14200 ⟵ “Food & Housing | $14,200 | $7,000 | $14,000”
  - on_campus:Books & Supplies***: 1700 ⟵ “Books & Supplies*** | $1,700 | $1,700 | $1,700”
  - on_campus:Personal Expenses***: 2000 ⟵ “Personal Expenses*** | $2,000 | $2,000 | $2,000”
  - on_campus:Transportation***: 2000 ⟵ “Transportation*** | $2,000 | $4,000 | $4,000”
  - on_campus:Fees: 2112 ⟵ “Fees | $2,112 | $2,112 | $2,112”
  - on_campus:Health Insurance**: 2738 ⟵ “Health Insurance** | $2,738 | $2,738 | $2,738”
  - on_campus:Total: 60360 ⟵ “Total | $60,360 | $55,160 | $62,160”
  - with_parents_or_family:Tuition*: 35610 ⟵ “Tuition* | $35,610 | $35,610 | $35,610”
  - with_parents_or_family:Food & Housing: 7000 ⟵ “Food & Housing | $14,200 | $7,000 | $14,000”
  - with_parents_or_family:Books & Supplies***: 1700 ⟵ “Books & Supplies*** | $1,700 | $1,700 | $1,700”
  - with_parents_or_family:Personal Expenses***: 2000 ⟵ “Personal Expenses*** | $2,000 | $2,000 | $2,000”
  - with_parents_or_family:Transportation***: 4000 ⟵ “Transportation*** | $2,000 | $4,000 | $4,000”
  - with_parents_or_family:Fees: 2112 ⟵ “Fees | $2,112 | $2,112 | $2,112”
  - with_parents_or_family:Health Insurance**: 2738 ⟵ “Health Insurance** | $2,738 | $2,738 | $2,738”
  - with_parents_or_family:Total: 55160 ⟵ “Total | $60,360 | $55,160 | $62,160”
  - off_campus_not_with_family:Tuition*: 35610 ⟵ “Tuition* | $35,610 | $35,610 | $35,610”
  - off_campus_not_with_family:Food & Housing: 14000 ⟵ “Food & Housing | $14,200 | $7,000 | $14,000”
  - off_campus_not_with_family:Books & Supplies***: 1700 ⟵ “Books & Supplies*** | $1,700 | $1,700 | $1,700”
  - off_campus_not_with_family:Personal Expenses***: 2000 ⟵ “Personal Expenses*** | $2,000 | $2,000 | $2,000”
  - off_campus_not_with_family:Transportation***: 4000 ⟵ “Transportation*** | $2,000 | $4,000 | $4,000”
  - off_campus_not_with_family:Fees: 2112 ⟵ “Fees | $2,112 | $2,112 | $2,112”
  - off_campus_not_with_family:Health Insurance**: 2738 ⟵ “Health Insurance** | $2,738 | $2,738 | $2,738”
  - off_campus_not_with_family:Total: 62160 ⟵ “Total | $60,360 | $55,160 | $62,160”
### `525726e51d82d589` Salem Community College — appeals 2017-18 [new] (labeled_in_source)
- source: https://salemcc.edu/paying-for-college/financial-aid (sha256 86f3a654df2c)
- issues: stale_year_label:2017-18, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Get Tax Return Transcript Special Circumstances Loss of a job or benefits, death in the family, divorce or separation, or extreme medical bills are examples of special circumstances that can change your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “You will need to complete a Request for Review of Special Circumstances form and provide documentation of the circumstance to the financial aid office.”
  - sentence: need_based_special_circumstances ⟵ “What is a special circumstance and how do I report it?”
  - sentence: need_based_special_circumstances ⟵ “Loss of a job or benefits, death in the family, divorce or separation, or extreme medical bills are examples of special circumstances that can change your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “You will need to complete a Request for Review of Special Circumstances form and provide documentation to the financial aid office.”
### `81ba8ff27bc0acc3` Salem Community College — appeals 2017-18 [new] (labeled_in_source)
- source: https://salemcc.edu/paying-for-college/financial-aid (sha256 86f3a654df2c)
- issues: stale_year_label:2017-18, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Under certain extenuating circumstances, you can be considered for a dependency override.”
  - sentence: dependency_override ⟵ “You will need to complete a Request for Dependency Override form and supply documentation from at least two third-party sources to support your dependency appeal.”
### `57b1817bb0588291` Seton Hall University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.shu.edu/financial-aid/ (sha256 8345d9df0431)
- issues: semantic_review_required, conflicting_sources:https://www.shu.edu/undergraduate-admissions/frequently-asked-questions.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “FAFSA is available online at: www.studentaid.gov/h/apply-for-aid/fafsa Special Circumstance Application Process: Please use the following link to submit your request for review of a Special Circumstance by completing the application and submitting the applicable documentation as indicated: 2026-27 PJ Advisor Link: https://inceptia.org/pjadvisor/shu2027 Note: Beginning March 20, 2026, the Special C”
  - sentence: need_based_special_circumstances ⟵ “Here is a helpful video that will walk you through the process of submitting a Special Circumstance application to Seton Hall.”
### `5c16c10a4d9eac37` Seton Hall University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.shu.edu/undergraduate-admissions/frequently-asked-questions.html (sha256 dc57b5bdebd3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “At this time, you will also receive an e-mail notification about the loss of your scholarship, and you will be informed about our appeal process.”
### `bc106e3d7790d18a` Seton Hall University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.shu.edu/undergraduate-admissions/frequently-asked-questions.html (sha256 dc57b5bdebd3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If there has been a change in your financial information or circumstances since you filed your FAFSA, you may be entitled to a special circumstances/professional judgment review.”
### `e75afc3b886a70cc` Seton Hall University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.shu.edu/undergraduate-admissions/frequently-asked-questions.html (sha256 dc57b5bdebd3)
- issues: semantic_review_required, conflicting_sources:https://www.shu.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: need_based_special_circumstances ⟵ “We cannot perform a special circumstances evaluation based on the fact that you want more aid and do not agree with results of your FAFSA and the SAI (student aid index) provided by the federal government.”
  - sentence: need_based_special_circumstances ⟵ “If indeed there has been a significant change in your financial circumstances and it was not represented in the data you provided on your FAFSA, then you will need to submit a Special Circumstances Application which can be found on the Documents and Forms tab of the Seton Hall Financial Aid website.”
  - sentence: need_based_special_circumstances ⟵ “When completing the form you must indicate the reason for your special circumstance and provide the required documentation indicated on the form; required documentation will vary based on the reason for your request.”
  - sentence: need_based_special_circumstances ⟵ “Review of special circumstances requests begins in February, and it generally takes 4-6 weeks to process these requests if all required information is on file.”
  - sentence: need_based_special_circumstances ⟵ “The special circumstances review allows the financial aid office to reassess your information while taking these new circumstances into consideration.”
  - sentence: need_based_special_circumstances ⟵ “Your SAI is the driver of need-based aid; therefore, a special circumstances review will only impact need-based aid and will have no bearing on any scholarships or merit-based aid.”
### `277de2f2f4f1de4f` Stevens Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stevens.edu/admission-aid/tuition-financial-aid/student-resources (sha256 c613ac536d09)
- issues: semantic_review_required, conflicting_sources:https://www.stevens.edu/page-chapter/terms-and-conditions,https://www.stevens.edu/page-chapter/terms-and-conditions
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Learn about resources for international students Special Circumstances & Unusual Circumstances Special Circumstances & Unusual Circumstances Food Insecurity Resources At Stevens, we are committed to supporting our students.”
### `3491e10464e7eec2` Stevens Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stevens.edu/page-chapter/terms-and-conditions (sha256 0561f311fd1c)
- issues: semantic_review_required, conflicting_sources:https://www.stevens.edu/admission-aid/tuition-financial-aid/student-resources,https://www.stevens.edu/page-chapter/terms-and-conditions
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You may, however, have an opportunity to appeal the denial of financial aid if you have faced special circumstances that prevented you from attaining SAP standards.”
### `7c4a5c6efeaf2e7f` Stevens Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stevens.edu/page-chapter/terms-and-conditions (sha256 371b6cb9fd5c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “SAP Definitions Appeal: A process by which a student who is not meeting SAP standards petitions the university for reconsideration of his/her eligibility for financial aid funds.”
  - sentence: sap_appeal ⟵ “You have the right to appeal the decision by submitting a SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “Generally, the SAP Appeals Committee will consider appeals that involve circumstances beyond your control that have had an impact on your academic performance.”
  - sentence: sap_appeal ⟵ “SAP Appeal Deadline Fall Semester: July 15 Spring Semester: January 17 You may submit your appeals by the deadline to the Office of Financial Aid.”
  - sentence: sap_appeal ⟵ “SAP Appeals Committee and Decision A committee will review the appeal and a response will be provided within 15 business days.”
### `eab6d30fd447c23c` Stevens Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stevens.edu/page-chapter/terms-and-conditions (sha256 371b6cb9fd5c)
- issues: semantic_review_required, conflicting_sources:https://www.stevens.edu/admission-aid/tuition-financial-aid/student-resources,https://www.stevens.edu/page-chapter/terms-and-conditions
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You may, however, have an opportunity to appeal the denial of financial aid if you have faced special circumstances that prevented you from attaining SAP standards.”
### `ae36ae763749d5e6` Stevens Institute of Technology — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.stevens.edu/admission-aid/undergraduate-admissions/accepted-students/ap-ib-and-college-transfer-credit (sha256 0acd1a59c9f6)
- issues: score_column_not_scores
- checks: {"distinct_exams": 15, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|HL Biology w/Lab (6/7)]:  ⟵ “Biology w/Lab (6/7) | HL | BIO 181 and BIO 182 | 4”
  - equivalencies[IB-CHEMISTRY|HL Chemistry w/Lab (6/7)]:  ⟵ “Chemistry w/Lab (6/7) | HL | CH 115, 116, 117, and 118 | 8”
  - equivalencies[IB-COMPUTER-SCIENCE|SL Computer Science (6/7)]:  ⟵ “Computer Science (6/7) | SL | Computer Science (CS) majors and minors will receive credit for one technical elective and Cybersecurity (CyS) majors and minors will receive credit for a computer science elective. All other majors will receive credit for CS 105. | 3”
  - equivalencies[IB-COMPUTER-SCIENCE|HL Computer Science (6/7)]:  ⟵ “Computer Science (6/7) | HL | Computer Science (CS) and Cybersecurity (CyS) majors and minors will receive credit for one general elective and are exempt from CS 115, CS 284 and start in CS 385. All other majors will receive credit for CS 105. | 3”
  - equivalencies[IB-ECONOMICS|HL Economics (6/7)]:  ⟵ “Economics (6/7) | HL | BT 243 and 244 | 6”
  - equivalencies[IB-HISTORY|HL History (6/7)]:  ⟵ “History (6/7) | HL | 100 Level Humanities | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|HL Mathematical Analysis and Approaches (6/7)]:  ⟵ “Mathematical Analysis and Approaches (6/7) | HL | MA 121/122 | 4”
  - equivalencies[IB-PHILOSOPHY|HL Philosophy (6/7)]:  ⟵ “Philosophy (6/7) | HL | HPL 111 or 112; (class for credit chosen with consultationof faculty advisor) | 3”
  - equivalencies[IB-PHYSICS|HL Physics (6/7)]:  ⟵ “Physics (6/7) | HL | PEP 123 and 124 (for Business and Humanities majors) | 6”
  - equivalencies[IB-PSYCHOLOGY|HL Psychology (6/7)]:  ⟵ “Psychology (6/7) | HL | HQSS 175 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|HL Social and Cultural Anthropology (6/7)]:  ⟵ “Social and Cultural Anthropology (6/7) | HL | General Elective | 3”
  - equivalencies[IB-THEATRE-HL|Theater HL (6/7)]:  ⟵ “Theater HL (6/7) | HL | General Elective | 3”
  - equivalencies[IB-BIOLOGY|Biology (A/B)]:  ⟵ “Biology (A/B) | BIO 181 and BIO 182 | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business (A/B)]:  ⟵ “Business (A/B) | BT 100 | 3”
  - equivalencies[IB-CHEMISTRY|Chemistry (A/B)]:  ⟵ “Chemistry (A/B) | CH 115, CH 116, CH 117 & CH 118 | 8”
  - equivalencies[IB-ECONOMICS|Economics (A/B)]:  ⟵ “Economics (A/B) | BT 243 & BT 244 | 6”
  - equivalencies[IB-ECONOMICS|Economics (A/B)]:  ⟵ “Economics (A/B) | ECON 242 for Quantitative Finance majors | 3”
  - equivalencies[IB-FRENCH|French (A/B)]:  ⟵ “French (A/B) | GE 100 | 3”
  - equivalencies[IB-GERMAN|German (A/B)]:  ⟵ “German (A/B) | GE 100 | 3”
  - equivalencies[IB-GERMAN|German Language & Literature (A/B)]:  ⟵ “German Language & Literature (A/B) | GE 100 | 3”
  - equivalencies[IB-MUSIC|Music (A/B)]:  ⟵ “Music (A/B) | HMU 101 | 3”
  - equivalencies[IB-PHYSICS|Physics (A/B)]:  ⟵ “Physics (A/B) | PEP 123 (for School of Business and School of Humanities majors) | 3”
### `f539ee23843abd45` Stockton University — appeals 2026-27 [new] (source_unlabeled)
- source: https://stockton.edu/financial-aid/appeals.html (sha256 6cf7de71f885)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If you have been notified that you are not maintaining SAP, are eligible to file an appeal and have extenuating circumstances, learn more below and follow the directions to submit an SAP appeal.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Satisfactory Academic Progress (SAP) is evaluated for federal and state financial aid recipients annually.”
  - sentence: sap_appeal ⟵ “Learn more about how SAP is evaluated and how to complete an SAP appeal below.”
### `6f12f2d5e6cb8eb3` Stockton University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://stockton.edu/admissions/costs.html (sha256 a58807dc00ac)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - column:Tuition: 23196 ⟵ “Tuition | $7,218 | $14,436 | $11,598 | $23,196”
  - column:Fees: 2820 ⟵ “Fees | $1,410 | $2,820 | $1,410 | $2,820”
  - column:Tuition & Fees: 26016 ⟵ “Tuition & Fees | $8,628 | $17,256 | $13,008 | $26,016”
  - column:Housing: 9510 ⟵ “Housing | $4,755 | $9,510 | $4,755 | $9,510”
  - column:Food (meal plan): 6310 ⟵ “Food (meal plan) | $3,155 | $6,310 | $3,155 | $6,310”
  - column:Housing & Food: 15820 ⟵ “Housing & Food | $7,910 | $15,820 | $7,910 | $15,820”
  - column:Total: 41836 ⟵ “Total | $16,538 | $33,076 | $20,918 | $41,836”
### `75987d75abfcfefd` Stockton University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://stockton.edu/admissions/costs.html (sha256 a58807dc00ac)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - column:Tuition: 14436 ⟵ “Tuition | $7,218 | $14,436 | $11,598 | $23,196”
  - column:Fees: 2820 ⟵ “Fees | $1,410 | $2,820 | $1,410 | $2,820”
  - column:Tuition & Fees: 17256 ⟵ “Tuition & Fees | $8,628 | $17,256 | $13,008 | $26,016”
  - column:Housing: 9510 ⟵ “Housing | $4,755 | $9,510 | $4,755 | $9,510”
  - column:Food (meal plan): 6310 ⟵ “Food (meal plan) | $3,155 | $6,310 | $3,155 | $6,310”
  - column:Housing & Food: 15820 ⟵ “Housing & Food | $7,910 | $15,820 | $7,910 | $15,820”
  - column:Total: 33076 ⟵ “Total | $16,538 | $33,076 | $20,918 | $41,836”
### `01b295728cdd925f` Sussex County Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/ (sha256 8128a4469486)
- issues: semantic_review_required, conflicting_sources:https://sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/,https://sussex.edu/media/qwgdydfy/2026-27-sap-appeal-form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Probation is a status assigned to a student who fails to make satisfactory academic progress and who has appealed and has had eligibility for aid reinstated.”
### `1519a5aa6c018b58` Sussex County Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://sussex.edu/admissions/paying-for-college/financial-aid/accessing-your-financial-aid/ (sha256 2f50086f98ee)
- issues: semantic_review_required, conflicting_sources:https://sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/,https://sussex.edu/media/c4fas0g3/2026-27-professional-judgment-request-form.pdf,https://sussex.edu/media/qwgdydfy/2026-27-sap-appeal-form.pdf,https://www.sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances: If a student's or family financial situation has changed since filing the FAFSA, a student may request a Special Circumstance Review.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances/Dependency Override: If you have extraordinary reasons for not being able to provide parent information on your FAFSA, you may request a Dependency Override.”
### `23ddd65c00e33f24` Sussex County Community College — appeals 2026-27 [new] (labeled_in_url)
- source: https://sussex.edu/media/qwgdydfy/2026-27-sap-appeal-form.pdf (sha256 385b174b32f8)
- issues: semantic_review_required, conflicting_sources:https://sussex.edu/admissions/paying-for-college/financial-aid/accessing-your-financial-aid/,https://sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/,https://sussex.edu/media/c4fas0g3/2026-27-professional-judgment-request-form.pdf,https://www.sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The circumstances under which a student would be permitted to submit an appeal are: death of a relative, injury or illness of the student or other special circumstances which you must document.”
### `6894abf4e19725d8` Sussex County Community College — appeals 2026-27 [new] (labeled_in_url)
- source: https://sussex.edu/media/qwgdydfy/2026-27-sap-appeal-form.pdf (sha256 385b174b32f8)
- issues: semantic_review_required, conflicting_sources:https://sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/,https://www.sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “FINANCIAL AID OFFICE Satisfactory Academic Progress Appeal Form You are no longer eligible to receive financial assistance at Sussex County Community College because you did not meet the standards of Satisfactory Academic Progress (SAP).”
### `956312e56683be99` Sussex County Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/ (sha256 5b07aae0819a)
- issues: semantic_review_required, conflicting_sources:https://sussex.edu/media/qwgdydfy/2026-27-sap-appeal-form.pdf,https://www.sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Probation is a status assigned to a student who fails to make satisfactory academic progress and who has appealed and has had eligibility for aid reinstated.”
### `b36a58a669f3e85a` Sussex County Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://sussex.edu/media/c4fas0g3/2026-27-professional-judgment-request-form.pdf (sha256 3654b049a8f2)
- issues: semantic_review_required, conflicting_sources:https://sussex.edu/admissions/paying-for-college/financial-aid/accessing-your-financial-aid/,https://sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/,https://sussex.edu/media/qwgdydfy/2026-27-sap-appeal-form.pdf,https://www.sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Complete the following steps: • Write a detailed letter of explanation outlining your unusual circumstances, sign and date the letter and submit with this form. • Submit non-returnable copies of required documentation listed for each item you checked below.”
### `cdb74e8848205191` Sussex County Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://sussex.edu/media/c4fas0g3/2026-27-professional-judgment-request-form.pdf (sha256 3654b049a8f2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “2026-2027 Professional Judgment Request Form Student’s Name: ________________________________________ Sussex ID#: _________________ The Financial Aid Office may consider a student’s unusual circumstances to adjust FAFSA data elements used to calculate the Student Aid Index (SAI) according to federal regulations set forth by the US Department of Education.”
  - sentence: professional_judgment ⟵ “This can be copies of paystubs showing earnings, proof of WIC benefits, SNAP benefits, etc.  Other extenuating circumstances: ______________________________________________________ o Submit complete documentation to support your reason(s) for requesting consideration. o We will not consider consumer debt (e.g., auto loans, credit card payments, mortgage, etc.) as a reason for professional judgmen”
  - sentence: professional_judgment ⟵ “Students who have been selected for Federal Verification must complete that process before their Professional Judgment Request can be reviewed.”
### `da962728af7e4c0b` Sussex County Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/ (sha256 5b07aae0819a)
- issues: semantic_review_required, conflicting_sources:https://sussex.edu/admissions/paying-for-college/financial-aid/accessing-your-financial-aid/,https://sussex.edu/media/c4fas0g3/2026-27-professional-judgment-request-form.pdf,https://sussex.edu/media/qwgdydfy/2026-27-sap-appeal-form.pdf,https://www.sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The Appeals Process The circumstances under which a student would be permitted to submit an appeal are the death of a relative, injury or illness of the student, or other special circumstances.”
### `f0e346d0d8c99837` Sussex County Community College — appeals 2025-26 [new] (labeled_in_url)
- source: https://sussex.edu/media/euuedldz/2025-26-sap-appeal-form.pdf (sha256 340b31c12836)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The circumstances under which a student would be permitted to submit an appeal are: death of a relative, injury or illness of the student or other special circumstances which you must document.”
### `fb77dbac893abbbf` Sussex County Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/ (sha256 8128a4469486)
- issues: semantic_review_required, conflicting_sources:https://sussex.edu/admissions/paying-for-college/financial-aid/accessing-your-financial-aid/,https://sussex.edu/admissions/paying-for-college/financial-aid/satisfactory-academic-progress/,https://sussex.edu/media/c4fas0g3/2026-27-professional-judgment-request-form.pdf,https://sussex.edu/media/qwgdydfy/2026-27-sap-appeal-form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The Appeals Process The circumstances under which a student would be permitted to submit an appeal are the death of a relative, injury or illness of the student, or other special circumstances.”
### `fbfb1146e29262d7` Sussex County Community College — appeals 2025-26 [new] (labeled_in_url)
- source: https://sussex.edu/media/euuedldz/2025-26-sap-appeal-form.pdf (sha256 340b31c12836)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “FINANCIAL AID OFFICE Satisfactory Academic Progress Appeal Form You are no longer eligible to receive financial assistance at Sussex County Community College because you did not meet the standards of Satisfactory Academic Progress (SAP).”
### `904c82baf6cef792` Sussex County Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://sussex.edu/admissions/paying-for-college/financial-aid/ (sha256 74728f6c47fc)
- issues: components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - column:Tuition: 7248 ⟵ “Tuition | $3,648 | $5,448 | $7,248”
  - column:Fees: 2112 ⟵ “Fees | $2,112 | $2,112 | $2,112”
  - column:Books: 1481 ⟵ “Books | $1,481 | $1,481 | $1,481”
  - column:Food & Housing: 5307 ⟵ “Food & Housing | $5,307* | $5,307* | $5,307”
  - column:Transportation: 2948 ⟵ “Transportation | $2,456 | $2,948 | $2,948”
  - column:Miscellaneous: 3000 ⟵ “Miscellaneous | $2,400 | $2,400 | $3,000”
  - column:Total: 21832 ⟵ “Total | $17,260 | $19,480 | $21,832”
### `a82e22433d6ee603` Sussex County Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sussex.edu/admissions/paying-for-college/financial-aid/ (sha256 33d33c973a93)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": false, "rows": 7}
  - column:Tuition: 3648 ⟵ “Tuition | $3,648 | $5,448 | $7,248”
  - column:Fees: 2112 ⟵ “Fees | $2,112 | $2,112 | $2,112”
  - column:Books: 1481 ⟵ “Books | $1,481 | $1,481 | $1,481”
  - column:Food & Housing: 5307 ⟵ “Food & Housing | $5,307* | $5,307* | $5,307”
  - column:Transportation: 2456 ⟵ “Transportation | $2,456 | $2,948 | $2,948”
  - column:Miscellaneous: 2400 ⟵ “Miscellaneous | $2,400 | $2,400 | $3,000”
  - column:Total: 17260 ⟵ “Total | $17,260 | $19,480 | $21,832”
  - column:Tuition: 5448 ⟵ “Tuition | $3,648 | $5,448 | $7,248”
  - column:Fees: 2112 ⟵ “Fees | $2,112 | $2,112 | $2,112”
  - column:Books: 1481 ⟵ “Books | $1,481 | $1,481 | $1,481”
  - column:Food & Housing: 5307 ⟵ “Food & Housing | $5,307* | $5,307* | $5,307”
  - column:Transportation: 2948 ⟵ “Transportation | $2,456 | $2,948 | $2,948”
  - column:Miscellaneous: 2400 ⟵ “Miscellaneous | $2,400 | $2,400 | $3,000”
  - column:Total: 19480 ⟵ “Total | $17,260 | $19,480 | $21,832”
### `dcbc292c961aade7` The College of New Jersey — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.tcnj.edu/ (sha256 7b57ac04732d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “View All Announcements Resources Sources of Financial Aid Undergraduate Graduate Transfer International Federal and State Programs Garden State Guarantee TEACH Grant Federal Work-Study (FWS) Program TCNJ Policies and Prodecures Satisfactory Academic Progres Withdrawal Policy Special Circumstances Unusual Circumstances See also: Summer Financial Aid | Winter Financial Aid | Veterans | Study Abroad/”
### `07d231033c76371d` The College of New Jersey — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/ (sha256 5ed0000ad267)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true,https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/,https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/?full-site=true
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition and Fees: 20986 ⟵ “Tuition and Fees | $20,986 | $27,520”
  - column:Housing and Food*: 17208 ⟵ “Housing and Food* | $17,208 | $17,208”
  - column:TCNJ Book Bundle: 694 ⟵ “TCNJ Book Bundle | $694 | $694”
  - column:Total Cost Per Year: 38888 ⟵ “Total Cost Per Year | $38,888 | $45,422”
### `30372ce1a5661008` The College of New Jersey — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.tcnj.edu/coa-undergrad-in-state-2025-26/?full-site=true (sha256 97a0eb5b9d7a)
- issues: stale_year_label:2025-26, conflicting_sources:https://financialaid.tcnj.edu/coa-undergrad-in-state-2025-26/,https://financialaid.tcnj.edu/wp-content/uploads/sites/79/2025/07/COA-25_26-IS-Students.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 15906 ⟵ “Tuition | $15,906”
  - column:Mandatory Fees: 4492 ⟵ “Mandatory Fees | $4,492”
  - column:Housing (On campus): 10714 ⟵ “Housing (On campus) | $10,714”
  - column:Food (Meal plan): 6578 ⟵ “Food (Meal plan) | $6,578”
  - column:Books/Supplies: 1200 ⟵ “Books/Supplies | $1,200”
  - column:Personal/Misc.: 3000 ⟵ “Personal/Misc. | $3,000”
  - column:Transportation: 1400 ⟵ “Transportation | $1,400”
  - column:Federal Student Loan fees: 40 ⟵ “Federal Student Loan fees | $40”
  - column:Total COA*: 43330 ⟵ “Total COA* | $43,330”
### `32bd56700e27cf62` The College of New Jersey — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false (sha256 6affc041b89e)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true,https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/,https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/?full-site=true
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition and Fees: 27520 ⟵ “Tuition and Fees | $20,986 | $27,520”
  - column:Housing and Food*: 17208 ⟵ “Housing and Food* | $17,208 | $17,208”
  - column:TCNJ Book Bundle: 694 ⟵ “TCNJ Book Bundle | $694 | $694”
  - column:Total Cost Per Year: 45422 ⟵ “Total Cost Per Year | $38,888 | $45,422”
### `43b50240eb8213f4` The College of New Jersey — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/ (sha256 5ed0000ad267)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true,https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/,https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/?full-site=true
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition and Fees: 27520 ⟵ “Tuition and Fees | $20,986 | $27,520”
  - column:Housing and Food*: 17208 ⟵ “Housing and Food* | $17,208 | $17,208”
  - column:TCNJ Book Bundle: 694 ⟵ “TCNJ Book Bundle | $694 | $694”
  - column:Total Cost Per Year: 45422 ⟵ “Total Cost Per Year | $38,888 | $45,422”
### `4ca58f674190141f` The College of New Jersey — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true (sha256 2371eb1537a8)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false,https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/,https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/?full-site=true
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition and Fees: 27520 ⟵ “Tuition and Fees | $20,986 | $27,520”
  - column:Housing and Food*: 17208 ⟵ “Housing and Food* | $17,208 | $17,208”
  - column:TCNJ Book Bundle: 694 ⟵ “TCNJ Book Bundle | $694 | $694”
  - column:Total Cost Per Year: 45422 ⟵ “Total Cost Per Year | $38,888 | $45,422”
### `4f722ad9537395e4` The College of New Jersey — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.tcnj.edu/wp-content/uploads/sites/79/2025/07/COA-25_26-IS-Students.pdf (sha256 9b21d421b31c)
- issues: stale_year_label:2025-26, conflicting_sources:https://financialaid.tcnj.edu/coa-undergrad-in-state-2025-26/,https://financialaid.tcnj.edu/coa-undergrad-in-state-2025-26/?full-site=true
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition:: 15906 ⟵ “Tuition: | $15,906”
  - column:Mandatory Fees:: 4492 ⟵ “Mandatory Fees: | $4,492”
  - column:Housing (On campus):: 10714 ⟵ “Housing (On campus): | $10,714”
  - column:Food (Meal plan):: 6578 ⟵ “Food (Meal plan): | $6,578”
  - column:Books/Supplies:: 1200 ⟵ “Books/Supplies: | $1,200”
  - column:Personal/Misc.:: 3000 ⟵ “Personal/Misc.: | $3,000”
  - column:Transportation:: 1400 ⟵ “Transportation: | $1,400”
  - column:Federal Student Loan fees:: 40 ⟵ “Federal Student Loan fees: | $40”
  - column:Total COA:: 43330 ⟵ “Total COA: | $43,330*”
### `5f2670db2b7d370f` The College of New Jersey — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/?full-site=true (sha256 ca2be39fa2e5)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true,https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 22938 ⟵ “Tuition | $22,938”
  - column:Mandatory Fees: 4582 ⟵ “Mandatory Fees | $4,582”
  - column:Housing (On campus): 11034 ⟵ “Housing (On campus) | $11,034”
  - column:Food (Meal plan): 6174 ⟵ “Food (Meal plan) | $6,174”
  - column:Books/Supplies: 694 ⟵ “Books/Supplies | $694”
  - column:Personal/Misc.: 3674 ⟵ “Personal/Misc. | $3,674”
  - column:Transportation: 2000 ⟵ “Transportation | $2,000”
  - column:Federal Student Loan Fees: 78 ⟵ “Federal Student Loan Fees | $78”
  - column:Total COA*: 51174 ⟵ “Total COA* | $51,174”
### `65f12a4938b35329` The College of New Jersey — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/?full-site=true (sha256 485a31b697c1)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true,https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 16384 ⟵ “Tuition | $16,384”
  - column:Mandatory Fees: 4602 ⟵ “Mandatory Fees | $4,602”
  - column:Housing (On campus): 11034 ⟵ “Housing (On campus) | $11,034”
  - column:Food (Meal plan): 6174 ⟵ “Food (Meal plan) | $6,174”
  - column:Books/Supplies: 694 ⟵ “Books/Supplies | $694”
  - column:Personal/Misc.: 3674 ⟵ “Personal/Misc. | $3,674”
  - column:Transportation: 2000 ⟵ “Transportation | $2000”
  - column:Federal Student Loan fees: 78 ⟵ “Federal Student Loan fees | $78”
  - column:Total COA*: 44640 ⟵ “Total COA* | $44,640”
### `6bd0a30f225ec0e3` The College of New Jersey — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.tcnj.edu/coa-undergrad-out-of-state-2025-26/?full-site=true (sha256 99904b60100a)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 22270 ⟵ “Tuition | $22,270”
  - column:Mandatory Fees: 4492 ⟵ “Mandatory Fees | $4,492”
  - column:Housing (On campus): 10714 ⟵ “Housing (On campus) | $10,714”
  - column:Food (Meal plan): 6578 ⟵ “Food (Meal plan) | $6,578”
  - column:Books/Supplies: 1200 ⟵ “Books/Supplies | $1,200”
  - column:Personal/Misc.: 3000 ⟵ “Personal/Misc. | $3,000”
  - column:Transportation: 1400 ⟵ “Transportation | $1,400”
  - column:Federal Student Loan Fees: 40 ⟵ “Federal Student Loan Fees | $40”
  - column:Total COA*: 49694 ⟵ “Total COA* | $49,694”
### `81a9db1a78f8611c` The College of New Jersey — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/ (sha256 c58880296f57)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true,https://financialaid.tcnj.edu/undergraduate-out-of-state-cost-of-attendance-for-2026-27/?full-site=true
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 22938 ⟵ “Tuition | $22,938”
  - column:Mandatory Fees: 4582 ⟵ “Mandatory Fees | $4,582”
  - column:Housing (On campus): 11034 ⟵ “Housing (On campus) | $11,034”
  - column:Food (Meal plan): 6174 ⟵ “Food (Meal plan) | $6,174”
  - column:Books/Supplies: 694 ⟵ “Books/Supplies | $694”
  - column:Personal/Misc.: 3674 ⟵ “Personal/Misc. | $3,674”
  - column:Transportation: 2000 ⟵ “Transportation | $2,000”
  - column:Federal Student Loan Fees: 78 ⟵ “Federal Student Loan Fees | $78”
  - column:Total COA*: 51174 ⟵ “Total COA* | $51,174”
### `839e40830f080ddb` The College of New Jersey — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.tcnj.edu/coa-undergrad-in-state-2025-26/ (sha256 0e51d16a0e74)
- issues: stale_year_label:2025-26, conflicting_sources:https://financialaid.tcnj.edu/coa-undergrad-in-state-2025-26/?full-site=true,https://financialaid.tcnj.edu/wp-content/uploads/sites/79/2025/07/COA-25_26-IS-Students.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 15906 ⟵ “Tuition | $15,906”
  - column:Mandatory Fees: 4492 ⟵ “Mandatory Fees | $4,492”
  - column:Housing (On campus): 10714 ⟵ “Housing (On campus) | $10,714”
  - column:Food (Meal plan): 6578 ⟵ “Food (Meal plan) | $6,578”
  - column:Books/Supplies: 1200 ⟵ “Books/Supplies | $1,200”
  - column:Personal/Misc.: 3000 ⟵ “Personal/Misc. | $3,000”
  - column:Transportation: 1400 ⟵ “Transportation | $1,400”
  - column:Federal Student Loan fees: 40 ⟵ “Federal Student Loan fees | $40”
  - column:Total COA*: 43330 ⟵ “Total COA* | $43,330”
### `9792f6a86eecc790` The College of New Jersey — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true (sha256 2371eb1537a8)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false,https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/,https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/?full-site=true
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition and Fees: 20986 ⟵ “Tuition and Fees | $20,986 | $27,520”
  - column:Housing and Food*: 17208 ⟵ “Housing and Food* | $17,208 | $17,208”
  - column:TCNJ Book Bundle: 694 ⟵ “TCNJ Book Bundle | $694 | $694”
  - column:Total Cost Per Year: 38888 ⟵ “Total Cost Per Year | $38,888 | $45,422”
### `a35b8a32423a1352` The College of New Jersey — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false (sha256 6affc041b89e)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true,https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/,https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/?full-site=true
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition and Fees: 20986 ⟵ “Tuition and Fees | $20,986 | $27,520”
  - column:Housing and Food*: 17208 ⟵ “Housing and Food* | $17,208 | $17,208”
  - column:TCNJ Book Bundle: 694 ⟵ “TCNJ Book Bundle | $694 | $694”
  - column:Total Cost Per Year: 38888 ⟵ “Total Cost Per Year | $38,888 | $45,422”
### `b0c32fa32223f964` The College of New Jersey — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/ (sha256 4a3ca50beb90)
- issues: conflicting_sources:https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=false,https://admissions.tcnj.edu/about-tcnj/costs-financial-aid/?full-site=true,https://financialaid.tcnj.edu/undergraduate-in-state-cost-of-attendance-for-2026-27/?full-site=true
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 16384 ⟵ “Tuition | $16,384”
  - column:Mandatory Fees: 4602 ⟵ “Mandatory Fees | $4,602”
  - column:Housing (On campus): 11034 ⟵ “Housing (On campus) | $11,034”
  - column:Food (Meal plan): 6174 ⟵ “Food (Meal plan) | $6,174”
  - column:Books/Supplies: 694 ⟵ “Books/Supplies | $694”
  - column:Personal/Misc.: 3674 ⟵ “Personal/Misc. | $3,674”
  - column:Transportation: 2000 ⟵ “Transportation | $2000”
  - column:Federal Student Loan fees: 78 ⟵ “Federal Student Loan fees | $78”
  - column:Total COA*: 44640 ⟵ “Total COA* | $44,640”
### `86f4791d5a76f779` UCNJ Union College of Union County, NJ — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ucc.edu/admissions/paying-for-college/special-or-unusual-circumstances/ (sha256 de07f2fc9c39)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Once your request is complete, you can expect a response in 3-10 days, Unusual Circumstances/Dependency Override If you have extraordinary reasons for not being able to provide parent information on your FAFSA, you may request a Dependency Override.”
### `917e5554a92632c9` UCNJ Union College of Union County, NJ — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ucc.edu/documents/financial-aid/forms/UCC_Satisfactory-Academic-Progress-Appeal-Guidelines.Revised.pdf (sha256 1f2e2ba689ba)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Definition of Terms Financial aid probation is defined as a status assigned by an institution to a student who fails to make satisfactory academic progress and who has appealed and has had eligibility for aid reinstated.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal is defined as a process by which a student who is not meeting the institution’s standards petitions the institution for reconsideration of the student’s eligibility for Title IV, HEA program funds.”
  - sentence: sap_appeal ⟵ “If a student who was previously not meeting SAP criteria brings his/her academic progress back into compliance prior to the next time SAP is calculated, no appeal is required.”
### `4b6f49a0c2058c89` UCNJ Union College of Union County, NJ — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ucc.edu/documents/financial-aid/Tuition-and-Fees-2025-2026-2025-04-14-2.pdf (sha256 b19074bafb5e)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26, conflicting_sources:https://www.ucc.edu/administration/institutional-research/common-data-set/annual-expenses/
- checks: {"columns": 2, "rows": 90}
  - column:Tuition: 7000 ⟵ “Tuition | $7,000”
  - column:Platform Fee: 500 ⟵ “Platform Fee | $500”
  - column:1: 218 ⟵ “1 | $218 | $415”
  - column:2: 436 ⟵ “2 | $436 | $830”
  - column:3: 654 ⟵ “3 | $654 | $1,245”
  - column:4: 872 ⟵ “4 | $872 | $1,660”
  - column:5: 1090 ⟵ “5 | $1,090 | $2,075”
  - column:6: 1308 ⟵ “6 | $1,308 | $2,490”
  - column:7: 1526 ⟵ “7 | $1,526 | $2,905”
  - column:8: 1744 ⟵ “8 | $1,744 | $3,320”
  - column:9: 1962 ⟵ “9 | $1,962 | $3,735”
  - column:10: 2180 ⟵ “10 | $2,180 | $4,150”
  - column:11: 2398 ⟵ “11 | $2,398 | $4,565”
  - column:12-18: 2695 ⟵ “12-18 | $2,695 | $5,130”
  - column:Application Fee: 10 ⟵ “Application Fee | $10”
  - column:(no refund after semester/term start): 155 ⟵ “(no refund after semester/term start) | $155”
  - column:Diploma Replacement Fee: 30 ⟵ “Diploma Replacement Fee | $30”
  - column:ESL Program Fee (per semester): 35 ⟵ “ESL Program Fee (per semester) | $35”
  - column:I.D. Replacement Fee: 5 ⟵ “I.D. Replacement Fee | $5”
  - column:International Student Registration Fee: 250 ⟵ “International Student Registration Fee | $250”
  - column:Refundable Bollwage Tag Fee: 35 ⟵ “Refundable Bollwage Tag Fee | $35”
  - column:Payment Plan Fee: 35 ⟵ “Payment Plan Fee | $35”
  - column:Return Check Fee: 40 ⟵ “Return Check Fee | $40”
  - column:Senior Registration Fee: 15 ⟵ “Senior Registration Fee | $15”
  - column:(Optional One-Time Fee — Laptop): 600 ⟵ “(Optional One-Time Fee — Laptop) | $600”
  - … 77 more rows
### `8b7974d7ff2f8118` UCNJ Union College of Union County, NJ — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ucc.edu/administration/institutional-research/common-data-set/annual-expenses/ (sha256 0763f8911f1d)
- issues: arrangement_unlabeled, residency_unknown, stacked_header_unparsed, stale_year_label:2025-26, conflicting_sources:https://www.ucc.edu/documents/financial-aid/Tuition-and-Fees-2025-2026-2025-04-14-2.pdf
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - column:Tuition: 5390 ⟵ “Tuition | 5,390 | 2,695 | 5,390 | 2,695”
  - column:Food and Housing: 4450 ⟵ “Food and Housing | 4,450 | 2,225 | 13,088 | 6,544”
  - column:Book/Supplies: 1080 ⟵ “Book/Supplies | 1,080 | 540 | 1,080 | 540”
  - column:Transportation: 2666 ⟵ “Transportation | 2,666 | 1,333 | 2,666 | 1,333”
  - column:Loan Fees: 62 ⟵ “Loan Fees | 62 | 31 | 62 | 31”
  - column:Miscellaneous: 2314 ⟵ “Miscellaneous | 2,314 | 1,157 | 2,314 | 1,157”
  - column:Total: 15962 ⟵ “Total | $ 15,962 | $ 7,981 | $ 24,600 | $ 12,300”
  - column:Tuition: 2695 ⟵ “Tuition | 5,390 | 2,695 | 5,390 | 2,695”
  - column:Food and Housing: 2225 ⟵ “Food and Housing | 4,450 | 2,225 | 13,088 | 6,544”
  - column:Book/Supplies: 540 ⟵ “Book/Supplies | 1,080 | 540 | 1,080 | 540”
  - column:Transportation: 1333 ⟵ “Transportation | 2,666 | 1,333 | 2,666 | 1,333”
  - column:Loan Fees: 31 ⟵ “Loan Fees | 62 | 31 | 62 | 31”
  - column:Miscellaneous: 1157 ⟵ “Miscellaneous | 2,314 | 1,157 | 2,314 | 1,157”
  - column:Total: 7981 ⟵ “Total | $ 15,962 | $ 7,981 | $ 24,600 | $ 12,300”
  - column:Tuition: 5390 ⟵ “Tuition | 5,390 | 2,695 | 5,390 | 2,695”
  - column:Food and Housing: 13088 ⟵ “Food and Housing | 4,450 | 2,225 | 13,088 | 6,544”
  - column:Book/Supplies: 1080 ⟵ “Book/Supplies | 1,080 | 540 | 1,080 | 540”
  - column:Transportation: 2666 ⟵ “Transportation | 2,666 | 1,333 | 2,666 | 1,333”
  - column:Loan Fees: 62 ⟵ “Loan Fees | 62 | 31 | 62 | 31”
  - column:Miscellaneous: 2314 ⟵ “Miscellaneous | 2,314 | 1,157 | 2,314 | 1,157”
  - column:Total: 24600 ⟵ “Total | $ 15,962 | $ 7,981 | $ 24,600 | $ 12,300”
  - column:Tuition: 2695 ⟵ “Tuition | 5,390 | 2,695 | 5,390 | 2,695”
  - column:Food and Housing: 6544 ⟵ “Food and Housing | 4,450 | 2,225 | 13,088 | 6,544”
  - column:Book/Supplies: 540 ⟵ “Book/Supplies | 1,080 | 540 | 1,080 | 540”
  - column:Transportation: 1333 ⟵ “Transportation | 2,666 | 1,333 | 2,666 | 1,333”
  - … 3 more rows
### `dae9bc93191076d8` UCNJ Union College of Union County, NJ — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ucc.edu/admissions/paying-for-college/tuition-and-fees/ (sha256 261a2e785290)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition: 5490.0 ⟵ “Tuition | $5,490.00 | $2,745.00”
  - with_parents_or_family:Clinical: 19728.0 ⟵ “Clinical | $19,728.00 | $9,864.00”
  - with_parents_or_family:Food and Housing: 4450.0 ⟵ “Food and Housing | $4,450.00 | $2,225.00”
  - with_parents_or_family:Book/Supplies: 1440.0 ⟵ “Book/Supplies | $1,440.00 | $720.00”
  - with_parents_or_family:Transportation: 2666.0 ⟵ “Transportation | $2,666.00 | $1,333.00”
  - with_parents_or_family:Loan Fees: 62.0 ⟵ “Loan Fees | $62.00 | $31.00”
  - with_parents_or_family:Miscellaneous: 2314.0 ⟵ “Miscellaneous | $2,314.00 | $1,157.00”
  - with_parents_or_family:Total: 36150.0 ⟵ “Total | $36,150.00 | $18,075.00”
  - with_parents_or_family:Tuition: 2745.0 ⟵ “Tuition | $5,490.00 | $2,745.00”
  - with_parents_or_family:Clinical: 9864.0 ⟵ “Clinical | $19,728.00 | $9,864.00”
  - with_parents_or_family:Food and Housing: 2225.0 ⟵ “Food and Housing | $4,450.00 | $2,225.00”
  - with_parents_or_family:Book/Supplies: 720.0 ⟵ “Book/Supplies | $1,440.00 | $720.00”
  - with_parents_or_family:Transportation: 1333.0 ⟵ “Transportation | $2,666.00 | $1,333.00”
  - with_parents_or_family:Loan Fees: 31.0 ⟵ “Loan Fees | $62.00 | $31.00”
  - with_parents_or_family:Miscellaneous: 1157.0 ⟵ “Miscellaneous | $2,314.00 | $1,157.00”
  - with_parents_or_family:Total: 18075.0 ⟵ “Total | $36,150.00 | $18,075.00”
### `072a4e948bf96c9b` Warren County Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.warren.edu/wp-content/uploads/2026/07/Cost-of-Attendance-Budget-2026-2027-for-web.pdf (sha256 5f4f66ab1204)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown
- checks: {"columns": 4, "components_reconcile": false, "rows": 21}
  - column:Tuition & Fees: 4752 ⟵ “Tuition & Fees | 4,752 | 4,992 | 5,712 | 3,564 | 3,744 | 4,284”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses: 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation: 2000 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - column:Personal: 1000 ⟵ “Personal | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000”
  - column:Tuition & Fees (2): 2376 ⟵ “Tuition & Fees | 2,376 | 2,496 | 2,856 | 1,188 | 1,248 | 1,428”
  - column:Books & Supplies (2): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (2): 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation (2): 1000 ⟵ “Transportation | 1,000 | 1,200 | 1,500 | 500 | 600 | 750”
  - column:Personal (2): 1000 ⟵ “Personal | 1,000 | 1,000 | 1,000 | 0 | 0 | 0”
  - column:Tuition & Fees (3): 4752 ⟵ “Tuition & Fees | 4,752 | 4,992 | 5,712 | 3,564 | 3,744 | 4,284”
  - column:Books & Supplies (3): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (3): 8000 ⟵ “Living Expenses | 8,000 | 8,000 | 8,000 | 8,000 | 8,000 | 8,000”
  - column:Transportation (3): 2000 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - column:Personal (3): 2000 ⟵ “Personal | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000”
  - column:Tuition & Fees (4): 2376 ⟵ “Tuition & Fees | 2,376 | 2,496 | 2,856 | 1,188 | 1,248 | 1,428”
  - column:Books & Supplies (4): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (4): 8000 ⟵ “Living Expenses | 8,000 | 8,000 | 8,000 | 8,000 | 8,000 | 8,000”
  - column:Transportation (4): 1000 ⟵ “Transportation | 1,000 | 1,200 | 1,500 | 500 | 600 | 750”
  - column:Personal (4): 2000 ⟵ “Personal | 2,000 | 2,000 | 2,000 | 0 | 0 | 0”
  - column:Total for Full-year: 12152 ⟵ “Total for Full-year | 12,152 | 12,792 | 14,112 | 10,464 | 10,944 | 11,934”
  - column:Tuition & Fees: 5712 ⟵ “Tuition & Fees | 4,752 | 4,992 | 5,712 | 3,564 | 3,744 | 4,284”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses: 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation: 3000 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - … 59 more rows
### `2227f8579ab2894e` Warren County Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.warren.edu/wp-content/uploads/2025/07/Cost-of-Attendance-Budget-2025-2026-for-web.pdf (sha256 b5d8f999a689)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": false, "rows": 21}
  - column:Tuition & Fees: 4560 ⟵ “Tuition & Fees | 4,560 | 4,800 | 5,520 | 3,420 | 3,600 | 4,140”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses: 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation: 2000 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - column:Personal: 1000 ⟵ “Personal | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000”
  - column:Tuition & Fees (2): 2280 ⟵ “Tuition & Fees | 2,280 | 2,400 | 2,760 | 1,140 | 1,200 | 1,380”
  - column:Books & Supplies (2): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (2): 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation (2): 1000 ⟵ “Transportation | 1,000 | 1,200 | 1,500 | 500 | 600 | 750”
  - column:Personal (2): 1000 ⟵ “Personal | 1,000 | 1,000 | 1,000 | 0 | 0 | 0”
  - column:Tuition & Fees (3): 4560 ⟵ “Tuition & Fees | 4,560 | 4,800 | 5,520 | 3,420 | 3,600 | 4,140”
  - column:Books & Supplies (3): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (3): 8000 ⟵ “Living Expenses | 8,000 | 8,000 | 8,000 | 8,000 | 8,000 | 8,000”
  - column:Transportation (3): 2000 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - column:Personal (3): 2000 ⟵ “Personal | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000”
  - column:Tuition & Fees (4): 2280 ⟵ “Tuition & Fees | 2,280 | 2,400 | 2,760 | 1,140 | 1,200 | 1,380”
  - column:Books & Supplies (4): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (4): 8000 ⟵ “Living Expenses | 8,000 | 8,000 | 8,000 | 8,000 | 8,000 | 8,000”
  - column:Transportation (4): 1000 ⟵ “Transportation | 1,000 | 1,200 | 1,500 | 500 | 600 | 750”
  - column:Personal (4): 2000 ⟵ “Personal | 2,000 | 2,000 | 2,000 | 0 | 0 | 0”
  - column:Total for Full-year: 11960 ⟵ “Total for Full-year | 11,960 | 12,600 | 13,920 | 10,320 | 10,800 | 11,790”
  - column:Tuition & Fees: 5520 ⟵ “Tuition & Fees | 4,560 | 4,800 | 5,520 | 3,420 | 3,600 | 4,140”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses: 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation: 3000 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - … 59 more rows
### `5680b5ebd6042dd3` Warren County Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.warren.edu/wp-content/uploads/2025/07/Cost-of-Attendance-Budget-2025-2026-for-web.pdf (sha256 b5d8f999a689)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": false, "rows": 21}
  - column:Tuition & Fees: 4800 ⟵ “Tuition & Fees | 4,560 | 4,800 | 5,520 | 3,420 | 3,600 | 4,140”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses: 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation: 2400 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - column:Personal: 1000 ⟵ “Personal | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000”
  - column:Tuition & Fees (2): 2400 ⟵ “Tuition & Fees | 2,280 | 2,400 | 2,760 | 1,140 | 1,200 | 1,380”
  - column:Books & Supplies (2): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (2): 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation (2): 1200 ⟵ “Transportation | 1,000 | 1,200 | 1,500 | 500 | 600 | 750”
  - column:Personal (2): 1000 ⟵ “Personal | 1,000 | 1,000 | 1,000 | 0 | 0 | 0”
  - column:Tuition & Fees (3): 4800 ⟵ “Tuition & Fees | 4,560 | 4,800 | 5,520 | 3,420 | 3,600 | 4,140”
  - column:Books & Supplies (3): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (3): 8000 ⟵ “Living Expenses | 8,000 | 8,000 | 8,000 | 8,000 | 8,000 | 8,000”
  - column:Transportation (3): 2400 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - column:Personal (3): 2000 ⟵ “Personal | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000”
  - column:Tuition & Fees (4): 2400 ⟵ “Tuition & Fees | 2,280 | 2,400 | 2,760 | 1,140 | 1,200 | 1,380”
  - column:Books & Supplies (4): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (4): 8000 ⟵ “Living Expenses | 8,000 | 8,000 | 8,000 | 8,000 | 8,000 | 8,000”
  - column:Transportation (4): 1200 ⟵ “Transportation | 1,000 | 1,200 | 1,500 | 500 | 600 | 750”
  - column:Personal (4): 2000 ⟵ “Personal | 2,000 | 2,000 | 2,000 | 0 | 0 | 0”
  - column:Total for Full-year: 12600 ⟵ “Total for Full-year | 11,960 | 12,600 | 13,920 | 10,320 | 10,800 | 11,790”
  - column:Tuition & Fees: 3600 ⟵ “Tuition & Fees | 4,560 | 4,800 | 5,520 | 3,420 | 3,600 | 4,140”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses: 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation: 1800 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - … 17 more rows
### `76edfdbf7eded96a` Warren County Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.warren.edu/wp-content/uploads/2026/07/Cost-of-Attendance-Budget-2026-2027-for-web.pdf (sha256 5f4f66ab1204)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 21}
  - column:Tuition & Fees: 4992 ⟵ “Tuition & Fees | 4,752 | 4,992 | 5,712 | 3,564 | 3,744 | 4,284”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses: 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation: 2400 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - column:Personal: 1000 ⟵ “Personal | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000”
  - column:Tuition & Fees (2): 2496 ⟵ “Tuition & Fees | 2,376 | 2,496 | 2,856 | 1,188 | 1,248 | 1,428”
  - column:Books & Supplies (2): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (2): 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation (2): 1200 ⟵ “Transportation | 1,000 | 1,200 | 1,500 | 500 | 600 | 750”
  - column:Personal (2): 1000 ⟵ “Personal | 1,000 | 1,000 | 1,000 | 0 | 0 | 0”
  - column:Tuition & Fees (3): 4992 ⟵ “Tuition & Fees | 4,752 | 4,992 | 5,712 | 3,564 | 3,744 | 4,284”
  - column:Books & Supplies (3): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (3): 8000 ⟵ “Living Expenses | 8,000 | 8,000 | 8,000 | 8,000 | 8,000 | 8,000”
  - column:Transportation (3): 2400 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - column:Personal (3): 2000 ⟵ “Personal | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000”
  - column:Tuition & Fees (4): 2496 ⟵ “Tuition & Fees | 2,376 | 2,496 | 2,856 | 1,188 | 1,248 | 1,428”
  - column:Books & Supplies (4): 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses (4): 8000 ⟵ “Living Expenses | 8,000 | 8,000 | 8,000 | 8,000 | 8,000 | 8,000”
  - column:Transportation (4): 1200 ⟵ “Transportation | 1,000 | 1,200 | 1,500 | 500 | 600 | 750”
  - column:Personal (4): 2000 ⟵ “Personal | 2,000 | 2,000 | 2,000 | 0 | 0 | 0”
  - column:Total for Full-year: 12792 ⟵ “Total for Full-year | 12,152 | 12,792 | 14,112 | 10,464 | 10,944 | 11,934”
  - column:Tuition & Fees: 3744 ⟵ “Tuition & Fees | 4,752 | 4,992 | 5,712 | 3,564 | 3,744 | 4,284”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | 400 | 400 | 400 | 400 | 400 | 400”
  - column:Living Expenses: 4000 ⟵ “Living Expenses | 4,000 | 4,000 | 4,000 | 4,000 | 4,000 | 4,000”
  - column:Transportation: 1800 ⟵ “Transportation | 2,000 | 2,400 | 3,000 | 1,500 | 1,800 | 2,250”
  - … 17 more rows
### `09c7712712969844` Warren County Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.warren.edu/wp-content/uploads/2026/07/Belvidere-Approved-Dual-Enrollment-Courses-with-Logo-revised-2025_7.22.2026.pdf (sha256 aeb609913935)
- issues: conflicting_sources:https://www.warren.edu/wp-content/uploads/2026/07/Hackettstown-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/North-Warren-HS-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Phillipsburg-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Warren-Hills-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf
- checks: {"distinct_exams": 9, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[AP-STATISTICS|3]:  ⟵ “AP Statistics              MAT 151 Statistics                      3            Fall 2012            2025”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2D Design                  ART 116 2D Design                       3            Fall 2018            2025”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “AP US History I            HIS 113 American History                3           Fall 2025”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “AP US History II           HIS 114 American History II             3           Fall 2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish 3 Honors           FOR 101 Beginning Spanish I             3           Fall 2019             2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish 4 Honors           FOR 151 Beginning Spanish II            3           Fall 2019             2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “AP Spanish Language        FOR 201 Int. Span I                     3           Fall 2019             2025”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “AP Biology                 BIO 162 Gen Bio I                       4           Fall 2019             2025”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “AP Calculus AB             MAT 201 Calculus                        4           Fall 2019             2025”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Honors Biology             BIO 145 Principles of Biology           4           Fall 2020             2025”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Honors Chemistry                 CHE 110 Intro to Chemistry              4           Fall 2021             2025”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “AP English Literature            ENG 141 English Composition II          3           Fall 2025”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “AP Psychology                    PSY 101 Intro to Psychology             3           Fall 2011             2025”
### `0fefc7619fc1ccb7` Warren County Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.warren.edu/wp-content/uploads/2026/07/Warren-Hills-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf (sha256 c31ba608e72e)
- issues: score_scale_mismatch, conflicting_sources:https://www.warren.edu/wp-content/uploads/2026/07/Belvidere-Approved-Dual-Enrollment-Courses-with-Logo-revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Hackettstown-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/North-Warren-HS-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Phillipsburg-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf
- checks: {"distinct_exams": 18, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “AP English Literature           ENG 140 English Composition I                  3             Fall 2001          2025”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “AP English Language & Comp      ENG 140 English Composition I                  3             Fall 2001          2025”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “AP European History             HIS 101 Western Civilization I                 3             Fall 2001          2025”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “AP Calculus AB                  MAT 201 Calculus I                             4             Fall 2001          2025”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “AP Biology                      BIO 162 General Biology I                      4             Fall 2002          2025”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “AP Statistics                   MAT 151 Statistics                             3             Fall 2010          2025”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “AP Physics I                    PHY 111 College Physics I                      4             Fall 2011          2025”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “AP Physics II                   PHY 112 College Physics II                     4             Fall 2011          2025”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “AP US History II                HIS 114 American History II                    3             Fall 2012          2025”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “AP Environmental Science          BIO 165 Environmental Studies                   4            Fall 2016          2025”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French III                        FOR 103 Beginning French I                      3            Fall 2019          2025”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “Hon French IV                     FOR 133 Beginning French II                     3            Fall 2019          2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish III                       FOR 101 Beginning Spanish I                     3            Fall 2019          2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Hon Spanish IV                    FOR 151 Beginning Spanish II                    3            Fall 2019          2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|6]:  ⟵ “AP Spanish V                      FOR 201 & FOR 251 Intermed Spanish I & I        6            Fall 2019          2025”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory & Technology         MUS 195 Fundamentals of Music theory            3            Fall 2019          2025”
  - equivalencies[AP-WORLD-HISTORY-MODERN|6]:  ⟵ “AP World History                  HIS 101 & HIS 102 Western Civ I and II          6            Fall 2019          2025”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Hon Biology                       BIO 145 Principles of Biology                   4            Fall 2020          2025”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “AP US Government & Politics       POL 101 Intro to American Government            3            Fall 2020          2025”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “AP & Hon Pre-Calculus             MAT 141 Pre-Calculus                            3            Fall 2021          2025”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Hon Chemistry                     CHE 110 Intro to Chemistry                      4            Fall 2021          2025”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “AP African American Studies       HIS 210 African/American History                3            Fall 2026”
### `ab6a915935f5ffe1` Warren County Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.warren.edu/wp-content/uploads/2026/07/North-Warren-HS-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf (sha256 14d771995efb)
- issues: conflicting_sources:https://www.warren.edu/wp-content/uploads/2026/07/Belvidere-Approved-Dual-Enrollment-Courses-with-Logo-revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Hackettstown-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Phillipsburg-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Warren-Hills-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf
- checks: {"distinct_exams": 13, "equivalencies": 16, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Honors Biology             BIO 145 Principles of Biology               4             Fall 2014          2025”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Honors Chemistry           CHE 110 Intro to Chemistry                  4             Fall 2024”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “AP Biology                 BIO 162 General Biology I                   4             Fall 2014          2025”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “AP European History        HIS 102 Western Civilization II             3             Fall 2014          2025”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “AP US History              HIS 113 American History I                  3             Fall 2014          2025”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “AP Psychology              PSY 101 Introduction to Psychology          3             Fall 2014          2025”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “AP Chemistry               CHE 164 General Chemisry I                  4             Fall 2015          2025”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing and Painting I     ART 118 Drawing                             3             Fall 2015          2025”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “AP Physics I               PHY 111 College Physics I                   4             Fall 2019          2025”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “AP Calculus AB             MAT 201 Calculus I                          4             Fall 2018          2025”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “AP Macroeconomics          ECO 188 Macroeconomics                      3             Fall 2019          2025”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                         MAT 150 Elements of Statistics                         3           Fall 2019            2025”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “AP Environmental Science           BIO 165 Environmental Studies                          4           Fall 2019            2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Hon Spanish III                    FOR 101 Beginning Spanish I                            3           Fall 2022            2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Hon Spanish IV                     FOR 151 Beginning Spanish II                           3           Fall 2022            2025”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “AP English Language & Comp         ENG 140 English Comp I                                 3           Fall 2022            2025”
### `b8a53e31ea91e604` Warren County Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.warren.edu/wp-content/uploads/2026/07/Hackettstown-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf (sha256 2326b1412fca)
- issues: conflicting_sources:https://www.warren.edu/wp-content/uploads/2026/07/Belvidere-Approved-Dual-Enrollment-Courses-with-Logo-revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/North-Warren-HS-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Phillipsburg-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Warren-Hills-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf
- checks: {"distinct_exams": 16, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “AP Biology                       BIO 162 General Biology I                   4             Fall 2022             2025”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “AP US History II                 HIS 114 American History II                 3             Fall 2001             2025”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “AP Calculus AB                   MAT 201 Calculus I                          4             Fall 2001             2025”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “AP Calculus BC                   MAT 201 Calculus I                          4             Fall 2018             2025”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “AP English Literature and Comp   ENG 140 English Composition I               3             Fall 2003             2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Honors Spanish III               FOR 201 Intermediate Spanish I              3             Fall 2003             2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Honors Spanish IV                FOR 251 Intermediate Spanish II             3             Fall 2003             2025”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “AP Chemistry                     CHE 164 General Chemistry I                 4             Fall 2022             2025”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Honors Statistics                MAT 151 Statistics                          3             Fall 2005             2025”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “AP World History                 HIS 101 Western Civilization I              3             Fall 2014             2025”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “AP Physics 1                        PHY 111 College Physics I                           4          Fall 2024”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “AP Physics 2                        PHY 112 College Physics II                          4          Fall 2024”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “AP European History                 HIS 102 Western Civilization II                     3          Fall 2013             2025”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Honors Pre-Calculus                 MAT 141 Pre-Calculus                                4          Fall 2014             2025”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “AP Environmental Science            BIO 165 Environmental Science                       4          Fall 2018             2025”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Honors Biology                      BIO 145 Principles of Biology                       4          Fall 2022             2025”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Honors Chemistry                    CHE 110 Introduction to Chemistry                   4          Fall 2022             2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Hon Spanish 2 for Native Speakers   FOR 101 Beginning Spanish I                         3          Fall 2022             2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Hon Spanish 3 for Native Speakers   FOR 151 Beginning Spanish II                        3          Fall 2022             2025”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “AP Computer Science Principles      CSC 103 Introduction to Computing                   3          Fall 2024”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “AP Computer Science A               CSC 122 Programming II                              3          Fall 2025”
### `e0e2b7e49e6d3c04` Warren County Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.warren.edu/wp-content/uploads/2026/07/Phillipsburg-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf (sha256 e4896e4dfe45)
- issues: conflicting_sources:https://www.warren.edu/wp-content/uploads/2026/07/Belvidere-Approved-Dual-Enrollment-Courses-with-Logo-revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Hackettstown-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/North-Warren-HS-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf,https://www.warren.edu/wp-content/uploads/2026/07/Warren-Hills-Approved-Dual-Enrollment-Courses-with-Logo-Revised-2025_7.22.2026.pdf
- checks: {"distinct_exams": 18, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “AP Biology                     BIO 162 General Biology I                   4          Fall 2012           2025”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing & Sketching            ART 118 Drawing                             3          Fall 2016           2025”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “AP Studio Art-2D Design        ART 116 2D Design                           3          Fall 2014           2025”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “AP Environmental Science       BIO 165 Environmental Studies               4          Fall 2002           2025”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “AP Chemistry                   CHE 164 General Chemistry I                 4          Fall 2002           2025”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “AP English Literature          ENG 140 English Composition I               3          Fall 2001           2025”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “Hon World History              HIS 101 Western Civilization I              3          Fall 2025”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “AP World History Modern        HIS 102 Western Civilization II             3          Fall 2014           2025”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “AP European History            HIS 102 Western Civilization II             3          Fall 2012           2025”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “Hon and Pre AP US History      HIS 113 American History I                  3          Fall 2024           2025”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “AP US History                  HIS 114 American History II                 3          Fall 2001           2025”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Honors Pre-Calculus            MAT 141 Pre-Calculus                        3          Fall 2014           2025”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “AP Statistics                  MAT 151 Statistics                          3          Fall 2001           2025”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “AP Calculus AB                 MAT 201 Calculus I                          4          Fall 2001           2025”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “AP Physics 1                   PHY 112 College Physics II                  4          Fall 2013           2025”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “CP Biology                     BIO 145 Principles of Biology               4          Fall 2016           2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “AP Spanish                     FOR 201 Intermediate Spanish I              3          Fall 2016           2025”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “AP Microeconomics             ECO 189 Microeconomics                        3         Fall 2018             2025”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “AP Calculus BC                MAT 202 Calculus II                           4         Fall 2018             2025”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “Hon French 2                  FOR 103 Beginning French I                    3         Fall 2018             2025”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “Hon French 3                  FOR 133 Beginning French II                   3         Fall 2018             2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Hon Spanish 2                 FOR 101 Beginning Spanish I                   3         Fall 2019             2025”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Hon Spanish 3                 FOR 151 Beginning Spanish II                  3         Fall 2019             2025”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Hon Chemistry                 CHE 110 Introduction to Chemistry             4         Fall 2022             2025”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “AP Psychology                 PSY 101 Intro to Psychology                   3         Fall 2021             2025”
### `14ea874fe2eef778` William Paterson University of New Jersey — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wpunj.edu/financial-aid/assets/Financial-Aid-Satisfactory-Academic-Progress-Appeal-Tips.pdf (sha256 c29960485560)
- issues: semantic_review_required, conflicting_sources:https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-appeal-policy,https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-faq,https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-policy.html
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Appeal Tips Many students have unexpected events that may cause them to have a difficult time during their education.”
  - sentence: sap_appeal ⟵ “The Financial Aid Satisfactory Academic Progress Appeal is an online form and has five parts and ALL of them MUST BE COMPLETED.”
  - sentence: sap_appeal ⟵ “Since your entire academic history MUST be taken into account, please explain your academic progress completely. • Review your academic transcript and contact an academic advisor or academic dean (if you have also been dismissed from the University) and get help planning your future classes and examining strategies for academic progress. • Think about what circumstances/events occurred that preven”
### `5bba0274dd31dca5` William Paterson University of New Jersey — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-policy.html (sha256 3bed08b7acc9)
- issues: semantic_review_required, conflicting_sources:https://www.wpunj.edu/financial-aid/assets/Financial-Aid-Satisfactory-Academic-Progress-Appeal-Tips.pdf,https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-appeal-policy,https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-faq
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Credit Hours Attempted Minimum Percentage Minimum Cumulative Greater than 12 70% 3.0 Part IV: SAP Definitions Appeal—A process by which a student who is not meeting SAP standards petitions the school for reconsideration of his eligibility for financial aid funds.”
  - sentence: sap_appeal ⟵ “Generally, the SAP Appeals Committee will consider appeals that involve circumstances beyond the student’s control that have had an impact upon the student’s academic performance.”
  - sentence: sap_appeal ⟵ “We also strongly recommend that the student evaluate your educational plans with their academic advisor on an ongoing basis SAP Appeal Deadlines: | Fall 2026 | August 17, 2026 | Spring 2027 | December 15, 2026 SAP Appeals Committee and Decision: A committee will review the appeal and a response will be provided within fifteen (15) business days.”
  - sentence: sap_appeal ⟵ “The decision of the SAP Appeals Committee is final.”
### `6c9e8427d7efe875` William Paterson University of New Jersey — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-appeal-policy (sha256 fcd43d99612a)
- issues: semantic_review_required, conflicting_sources:https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-policy.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “There are three distinct dimensions to the satisfactory academic progress standards: Grade Point Average (Qualitative Measure) Maximum Time Frame Measure Credit Completion Ratio or Calculating Pace (Quantitative Measure) These standards also include an opportunity to appeal the denial of financial aid if the student has faced special circumstances, which prevented the student from attaining the mi”
### `6f0d34828010bc63` William Paterson University of New Jersey — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-appeal-policy (sha256 fcd43d99612a)
- issues: semantic_review_required, conflicting_sources:https://www.wpunj.edu/financial-aid/assets/Financial-Aid-Satisfactory-Academic-Progress-Appeal-Tips.pdf,https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-faq,https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-policy.html
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Credit Hours Attempted Minimum Percentage Minimum Cumulative Greater than 12 70% 3.0 Part IV: SAP Definitions Appeal—A process by which a student who is not meeting SAP standards petitions the school for reconsideration of his eligibility for financial aid funds.”
  - sentence: sap_appeal ⟵ “Generally, the SAP Appeals Committee will consider appeals that involve circumstances beyond the student’s control that have had an impact upon the student’s academic performance.”
  - sentence: sap_appeal ⟵ “SAP Appeal Deadlines: | Fall Semester | August 17th | Spring Semester | December 15th SAP Appeals Committee and Decision: A committee will review the appeal and a response will be provided within fifteen (15) business days.”
  - sentence: sap_appeal ⟵ “The decision of the SAP Appeals Committee is final.”
### `f768aae35bbeb5c7` William Paterson University of New Jersey — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-policy.html (sha256 3bed08b7acc9)
- issues: semantic_review_required, conflicting_sources:https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-appeal-policy
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “There are three distinct dimensions to the satisfactory academic progress standards: Grade Point Average (Qualitative Measure) Maximum Time Frame Measure Credit Completion Ratio or Calculating Pace (Quantitative Measure) These standards also include an opportunity to appeal the denial of financial aid if the student has faced special circumstances that prevented the student from attaining the mini”
### `fd85d5cd02ca9e71` William Paterson University of New Jersey — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-faq (sha256 d1ff3d0e4051)
- issues: semantic_review_required, conflicting_sources:https://www.wpunj.edu/financial-aid/assets/Financial-Aid-Satisfactory-Academic-Progress-Appeal-Tips.pdf,https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-appeal-policy,https://www.wpunj.edu/financial-aid/satisfactory-academic-progress/sap-policy.html
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Are there any tips to help understand the SAP appeal process?”
  - sentence: sap_appeal ⟵ “Yes, students can view the financial aid Satisfactory Academic Progress Appeal pointers here under Satisfactory Academic Progress Appeal Tips. 8.”
  - sentence: sap_appeal ⟵ “Appeal letters, documents and academic plans are stored in a secure website that is only viewable by the SAP Appeals Committee members. 29.”
### `558c052d473a0019` William Paterson University of New Jersey — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.wpunj.edu/admissions/undergraduate/accepted-students/international-baccalaureate-equivalencies (sha256 beff6f4ac93c)
- issues: score_column_not_scores
- checks: {"distinct_exams": 20, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[IB-VISUAL-ARTS|High]:  ⟵ “Arts | Visual Arts | High | 4,5,6,7 | Arth 1010 & Arts 1200 | Understanding Art 2-D design | 6”
  - equivalencies[IB-FILM|High]:  ⟵ “Arts | Film | High | 5,6,7,4 | Comm 2340 & 2390 Comm 2340 | Film as a Medium & Film Production I Film Production II | 6”
  - equivalencies[IB-MUSIC|High]:  ⟵ “Arts | Music | High | 4,5,6,7 | MUSI 1150 & 1240 | Understanding Music & Music Fundamentals | 6”
  - equivalencies[IB-CHEMISTRY|High]:  ⟵ “Science | Chemistry | High | 4,5 | BIO 1620,1630 | General Biology:EEB &CMG | 8”
  - equivalencies[IB-CHEMISTRY|High]:  ⟵ “Science | Chemistry | High | 6,7 | BIO 1620,1630,2040 | Biology:EEB, CMG, PHYSC | 12”
  - equivalencies[IB-CHEMISTRY|High]:  ⟵ “Sciences | Chemistry | High | 5,6,7 | Chem 1600 & 1610 Chem 1600 | General Chemistry I & II | 8”
  - equivalencies[IB-CHEMISTRY|High]:  ⟵ “Sciences | Chemistry | High | 4 | Chem 1600 | General Chemistry | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|High]:  ⟵ “Sciences | Computer Science | High | 4,5,6,7 | CS 2010 | Computer and Information Technology | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|High]:  ⟵ “Sciences | Environmental Systems and Societies | High | 4,5,6,7 | ENV 1100 | Environmnetal Sustanability | 4”
  - equivalencies[IB-PHYSICS|High]:  ⟵ “Sciences | Physics | High | 5,6,7 | PHYS 2550 &2560 | College Physics | 8”
  - equivalencies[IB-PHYSICS|High]:  ⟵ “Sciences | Physics | High | 4 | PHYSC 2550 | College Physics I | 4”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|High]:  ⟵ “Mathematics | Analysis & Approaches | High | 5,6,7 | Math 1160,1600 & 1610 | Pre-Calc, Calculus I & II | 11”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|High]:  ⟵ “Mathematics | Analysis & Approaches | High | 4 | Math 1160 &1600 | Pre-Calculus & Calculus I | 7”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|High]:  ⟵ “Mathematics | Applications and Interpretations | High | 5,6,7 | Math 1170 &1600 | Math 1170 and Calc I | 7”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|High]:  ⟵ “Mathematics | Applications and Interpretations | High | 4 | Math 1170 | Business Mathematics | 3”
  - equivalencies[IB-BUSINESS-MANAGEMENT|High]:  ⟵ “Individuals and Societies | Business Management | High | 4,5,6,7 | MGT 2000 | Principles of Management | 3”
  - equivalencies[IB-ECONOMICS|High]:  ⟵ “Individual and Societies | Economics | High | 5,6,7 | ECON 2010 &2020 | Macro-econ.Prin.& Micro.econ.Prin. | 6”
  - equivalencies[IB-ECONOMICS|High]:  ⟵ “Individual and Societies | Economics | High | 4 | ECON 2010 | Macro-economic Principles | 3”
  - equivalencies[IB-GEOGRAPHY|High]:  ⟵ “Individual and Societies | Geography | High | 5,6,7 | GEO 1500 &2100 | World Regional and Human Geography | 6”
  - equivalencies[IB-GEOGRAPHY|High]:  ⟵ “Individual and Societies | Geography | High | 4 | GEO 1500 | World Regional Geography | 6”
  - equivalencies[IB-GLOBAL-POLITICS|High]:  ⟵ “Individual and Societies | Global Politics | High | 5,6,7 | POL 1100 &2400 | Introduction to Politics & International Relations | 6”
  - equivalencies[IB-GLOBAL-POLITICS|High]:  ⟵ “Individual and Societies | Global Politics | High | 4 | POL 1100 | Introduction to Politics | 3”
  - equivalencies[IB-HISTORY|High]:  ⟵ “Individuals and Societies | History | High | 5,6,7 | HIST 1040 & 1050 | Early Modern World & Modern World | 6”
  - equivalencies[IB-HISTORY|High]:  ⟵ “Individuals and Societies | History | High | 4 | HIST 1040 | Early Modern World | 3”
  - equivalencies[IB-PHILOSOPHY|High]:  ⟵ “Individuals and Societies | Philosophy | High | 4,5,6,7 | PHIL 1100 & 1600 | Introduction to Philosophy & Being Human | 6”
  - … 6 more rows

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 19; pages by category: admissions_tests 1, aid_appeals 1, merit_scholarships 3, residency 1, tuition_fees 9

## Blocked by the site (every request refused; needs the browser fallback)

- Princeton University (`ipeds-186131`)
- Rabbinical College of America (`ipeds-186186`)
- Talmudical Academy-New Jersey (`ipeds-186900`)
- Rabbi Jacob Joseph School (`ipeds-384421`)
- Yeshiva Toras Chaim (`ipeds-451398`)
- Yeshiva Yesodei Hatorah (`ipeds-481438`)
- Beth Medrash of Asbury Park (`ipeds-488314`)
- Yeshiva Gedolah Shaarei Shmuel (`ipeds-488350`)
- Yeshiva Bais Aharon (`ipeds-490319`)
- Bais Medrash Mayan Hatorah (`ipeds-490513`)
- Yeshiva Gedolah Tiferes Boruch (`ipeds-491613`)
- Yeshiva Chemdas Hatorah (`ipeds-491622`)
- Yeshiva Gedolah Keren Hatorah (`ipeds-491640`)
- Yeshiva Gedolah of Cliffwood (`ipeds-491710`)
- Yeshivas Emek Hatorah (`ipeds-491765`)
- Seminary Bnos Chaim (`ipeds-491817`)
- Yeshiva Gedola Tiferes Yerachmiel (`ipeds-491914`)
- Yeshiva Gedolah of Woodlake Village (`ipeds-493707`)
- Yeshiva Gedola Tiferes Yaakov Yitzchok (`ipeds-493716`)

## Leads: official pages found with no extracted record

- Assumption College for Sisters: tuition_fees, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, aid_appeals
- Atlantic Cape Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, statewide_articulation, degree_requirements
- Bais Medrash Toras Chesed: tuition_fees, transfer_credit
- Bergen Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, statewide_articulation, residency, degree_requirements
- Bloomfield College: cost_of_attendance, admissions_tests
- Brookdale Community College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Caldwell University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, statewide_articulation
- Centenary University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, degree_requirements
- County College of Morris: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Drew University: admissions_tests, common_data_set, merit_scholarships, transfer_credit, degree_requirements
- Essex County College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, dual_enrollment, statewide_articulation, degree_requirements
- Fairleigh Dickinson University-Florham Campus: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Fairleigh Dickinson University-Metropolitan Campus: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Felician University: cost_of_attendance, admissions_tests, common_data_set, ap_credit, dual_enrollment, transfer_credit, degree_requirements
- Georgian Court University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, ib_credit, transfer_credit, statewide_articulation
- Hudson County Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, statewide_articulation, degree_requirements, aid_appeals
- Kean University: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Keser Torah-Mayan Hatalmud: admissions_tests
- Mercer County Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Middlesex College: admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency, aid_appeals
- Monmouth University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- Montclair State University: tuition_fees, cost_of_attendance, merit_scholarships, clep_credit, dual_enrollment, residency
- New Jersey City University: tuition_fees
- New Jersey Institute of Technology: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency
- Ocean County College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency, degree_requirements
- Passaic County Community College: tuition_fees, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit
- Pillar College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- Ramapo College of New Jersey: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Raritan Valley Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- Rider University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Rowan College at Burlington County: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- Rowan College of South Jersey-Cumberland Campus: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Rowan College of South Jersey-Gloucester Campus: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Rowan University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Rutgers University-Camden: admissions_tests, ap_credit, dual_enrollment, residency, degree_requirements
- Rutgers University-New Brunswick: admissions_tests, ap_credit, dual_enrollment, residency
- Rutgers University-Newark: admissions_tests, ap_credit, dual_enrollment, residency
- Saint Elizabeth University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Saint Peter's University: tuition_fees, cost_of_attendance, admissions_tests, aid_appeals
- Salem Community College: tuition_fees, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Seton Hall University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit
- Stevens Institute of Technology: admissions_tests, common_data_set, merit_scholarships, statewide_articulation, degree_requirements
- Stockton University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Sussex County Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- The College of New Jersey: admissions_tests, merit_scholarships, ap_credit, ib_credit, residency, degree_requirements
- Thomas Edison State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- UCNJ Union College of Union County, NJ: admissions_tests, common_data_set, merit_scholarships, ap_credit, residency, degree_requirements
- Warren County Community College: tuition_fees, admissions_tests, merit_scholarships, dual_enrollment, degree_requirements, aid_appeals
- William Paterson University of New Jersey: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Yeshivas Be'er Yitzchok: admissions_tests
