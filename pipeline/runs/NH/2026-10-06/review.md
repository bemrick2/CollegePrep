# Review queue — NH (2026-27)

Pages fetched: 1590; failures: 168. Candidates: 100 (22 without issues, 78 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 2 | 5 | 12 | 1 | 2 |
| cost_of_attendance | 0 | 0 | 0 | 2 | 18 | 0 | 2 |
| admissions_tests | 0 | 0 | 0 | 0 | 19 | 1 | 2 |
| common_data_set | 0 | 0 | 0 | 0 | 1 | 19 | 2 |
| merit_scholarships | 0 | 0 | 1 | 2 | 17 | 0 | 2 |
| ap_credit | 0 | 0 | 5 | 0 | 9 | 6 | 2 |
| clep_credit | 0 | 0 | 3 | 1 | 8 | 8 | 2 |
| ib_credit | 0 | 0 | 1 | 0 | 2 | 17 | 2 |
| dual_enrollment | 0 | 0 | 1 | 0 | 12 | 7 | 2 |
| transfer_credit | 0 | 0 | 6 | 1 | 13 | 0 | 2 |
| statewide_articulation | 0 | 0 | 0 | 0 | 8 | 12 | 2 |
| residency | 0 | 0 | 0 | 0 | 14 | 6 | 2 |
| degree_requirements | 0 | 0 | 0 | 0 | 16 | 4 | 2 |
| aid_appeals | 0 | 0 | 0 | 12 | 4 | 4 | 2 |

## Ready for review (22)

### `3236e383ed79ee53` Colby-Sawyer College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.colby-sawyer.edu/undergraduate-program-annual-tuition-and-fees-20262027 (sha256 89aeb091a46b)
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 19000.0 ⟵ “Tuition | $19,000.00”
  - column:Housing and Food: 18750.0 ⟵ “Housing and Food | $18,750.00”
  - column:Mandatory Fees: 1100.0 ⟵ “Mandatory Fees | $1,100.00”
  - column:Total: 38850.0 ⟵ “Total | $38,850.00”
### `373d4154ac546469` Franklin Pierce University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://franklinpierce.edu/admissions/get-started/high-school/CLEP-equivalency-recommendations.html (sha256 a357d4e35b15)
- checks: {"distinct_exams": 33, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 | AC101 | ”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | 3 | CIT101 or CIT102 | ”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | BA213 or BA258 | ”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 | MN201 | ”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 3 | MK201 | ”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 | EN204 & 3 EN elective credits | ”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 | EN210 & 3 EN elective credits | ”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 6 | GLE110 plus 3 general elective credits | ”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 3 | GLE110 | ”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 | EN203 & 3 EN elective credits | ”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 | 3 Humanities GLE elective credits | ”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level 1 | 50 | 6 | LF101 & LF102 | Credit granted for one level or the other, not both.”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, Level 2 | 59 | 9 | LF101, LF102, LF201, LF202 | Credit granted for one level or the other, not both.”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level 1 | 50 | 6 | ML101 & ML102 | Credit granted for one level or the other, not both.”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language, Level 2 | 60 | 9 | ML101, ML102, ML201, ML202 | Credit granted for one level or the other, not both.”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1 | 50 | 6 | LS101 & LS102 | Credit granted for one level or the other, not both.”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language, Level 2 | 63 | 9 | LS101, LS102, LS201 | Credit granted for one level or the other, not both.”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish w/ Writing, Level 1 | 50 | 6 | LS101, LS102 | Credit granted for one level or the other, not both.”
  - equivalencies[CLEP-SPANISH-LANGUAGE|65]:  ⟵ “Spanish w/ Writing, Level 2 | 65 | 12 | LS101, LS102, LS201, LS202 | Credit granted for one level or the other, not both.”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | PO201 | ”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 | 3 | HS201 or HS202 | ”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present | 50 | 3 | HS203 or HS204 | ”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | PS234 or 3 PS elective credits | Fulfills developmental requirements for Human Services, Psychology, and Social Work/Counseling majors.”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | 3 | ED105 | ”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | PS101 | ”
  - … 13 more rows
### `d816d1ecf854cc6d` Franklin Pierce University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://franklinpierce.edu/admissions/advanced-placement-equivalancies.html (sha256 68b5c4bcf747)
- checks: {"distinct_exams": 40, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art and Design | FA101 | 3 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art and Design | FA102 | 3 | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | SS Elective | 3 | 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | FA183 + FA Elective | 3 | 6”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | BI102 | 3 | 4”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3]:  ⟵ “Business with Personal Finance | FM214 | 3 | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | MT221 | 3 | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | MT221 + MT222 | 3 | 8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | CH101 | 3 | 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | CH101 + CH102 | 4 | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | Elective | 3 | 6”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | PO206 | 3 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | CIT101 | 3 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | CIT102 | 3 | 3”
  - equivalencies[AP-CYBERSECURITY|3]:  ⟵ “Cybersecurity (Career Kickstart) | CIT247 | 3 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing | FA201 | 3 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | GLE110 + English General Elective | 3 | 6”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | GLE110 + English General Elective | 3 | 6”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | ES101 or ES103 | 3 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 6 credits of 200-level History, including HM GLE | 3 | 6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | Elective | 3 | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture | Elective | 3 | 6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | HS308 | 3 | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture | Elective | 3 | 6”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture | Elective | 3 | 6”
  - … 16 more rows
### `44843d89db565ad6` Franklin Pierce University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.franklinpierce.edu/undergraduate-transfer-credit-policy (sha256 2744337bef46)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Students from nationally accredited Associate-level colleges will receive transfer credit up to 75 semester hours for grades of C or higher in appropriate coursework.”
  - min_grade: C ⟵ “Students from nationally accredited Baccalaureate-level colleges/universities will receive transfer credit up to 90 semester hours for grades of C or higher in appropriate coursework.”
### `46d5976879e7e9fd` Great Bay Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.greatbay.edu/academics/credit-for-prior-learning/ (sha256 2cb7386ab606)
- checks: {"distinct_exams": 1, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-3-D-ART-DESIGN|ARTSXXX]:  ⟵ “3-D Art & Design | 3+ | ARTSXXX | Fine Arts or Humanities Elective | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Art History | 3+ | ARTS117G | Art History I | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Drawing | 3+ | ARTS123G | Drawing I | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Music Theory | 3+ | ARTS105G | Introduction to Music | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | English Language & Composition | 3+ | ENGL110G OR ENGLXXX | College Composition I OR English Elective | 4”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Chinese Language & Culture | 3+ | HUMAXXX | Humanities Elective | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art & Design | Spanish Language & Culture | 3 | HUMAXXX | Humanities Elective | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Spanish Language & Culture | 3+ | SPAN110G | Spanish I | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Calculus BC | 3+ | MATH230G | Calculus I | 4”
  - equivalencies[AP-3-D-ART-DESIGN|4+]:  ⟵ “3-D Art & Design | Calculus BC | 4+ | MATH230G & Math250G | Calculus I & Calculus II | 8”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Pre Calculus | 3+ | MATH210G | Precalculus | 4”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Statistics | 3+ | MATH106G | Statistics I: An Introduction to Statistical Reasoning | 4”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Chemistry | 3+ | CHEM115G | General Chemistry I | 4”
  - equivalencies[AP-3-D-ART-DESIGN|4+]:  ⟵ “3-D Art & Design | Chemistry | 4+ | CHEM115G & CHEM116G | General Chemistry I & General Chemistry II | 8”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Physics 1: Algebra Based | 3+ | PHYS135G | College Physics I | 4”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Physics 2: Algebra Based | 3+ | PHYS136G | College Physics II | 4”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Physics C: Electricity & Magnetism | 3+ | PHYS290G | University Physics I | 4”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Physics C: Mechanics | 3+ | PHYS295G | University Physics II | 4”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art & Design | European History | 3 | HIST130G | Western Civilization- 1500 to the Present | 3”
  - equivalencies[AP-3-D-ART-DESIGN|4+]:  ⟵ “3-D Art & Design | European History | 4+ | HIST120G & HIST130G | Western Civilization through 1500 & Western Civilization- 1500 to the Present | 6”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Geography | 3+ | GEOG110G | World Geography | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Macroeconomics | 3+ | ECON234G | Macroeconomics | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | Microeconomics | 3+ | ECON235G | Microeconomics | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art & Design | Psychology | 3 | SOCIXXX | Social Science Elective | 3”
  - equivalencies[AP-3-D-ART-DESIGN|4+]:  ⟵ “3-D Art & Design | Psychology | 4+ | PSYC110G | Introduction to Psychology | 3”
  - … 6 more rows
### `64dbd7ac9768c6e9` Great Bay Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.greatbay.edu/academics/credit-for-prior-learning/ (sha256 2cb7386ab606)
- checks: {"distinct_exams": 22, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL220G | American Literature after the Civil War | 3.00”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | ENGL117G | Introduction to Literature | 3.00”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGLXXXG | English Elective | 3.00”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language Level I & 2 | 50 | HUMAXXXG | Humanities Elective | 3.00”
  - equivalencies[CLEP-FRENCH-LANGUAGE|65]:  ⟵ “French Language Level I & 2 | 65 | HUMAXXXG | Humanities Elective | 6.00”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language Level 1 & 2 | 50 | HUMAXXXG | Humanities Elective | 3.00”
  - equivalencies[CLEP-GERMAN-LANGUAGE|65]:  ⟵ “German Language Level 1 & 2 | 65 | HUMAXXXG | Humanities Elective | 6.00”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language Level I & 2 | 50 | SPAN110G | Humanities Elective | 3.00”
  - equivalencies[CLEP-SPANISH-LANGUAGE|65]:  ⟵ “Spanish Language Level I & 2 | 65 | SPAN110G & SPAN120G | Humanities Elective | 6.00”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS110G | American Government | 3.00”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | PSYC210G | Human Growth & Development | 3.00”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introduction | 50 | PSYC110G | Introduction to Psychology | 3.00”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introduction | 50 | SOCI110G | Sociology | 3.00”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | HUMAXXXG | Humanities Elective | 3.00”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Principles of | 50 | ECON234G | Macroeconomics | 3.00”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Principles of | 50 | ECON235G | Microeconomics3.00 | 3.00”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | SCIXXXG (No lab) | Science Elective | 3.00”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | SCIXXXXG (No lab) | Science Elective | 3.00”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-Calculus | 50 | MATH210G | Pre-Calculus | 3.00”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH230G | Calculus I | 4.00”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT113G | Accounting & Financial Reporting I | 3.00”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|65]:  ⟵ “Financial Accounting | 65 | ACCT113G and ACCT123G | Accounting & Financial Reporting I and II | 6.00”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Principles of | 50 | BUS114G | Management | 3.00”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business Law | 50 | BIS211G | Business Law | 3.00”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of | 50 | MKTG101G | Principles of Marketing | 3.00”
  - … 1 more rows
### `1571c40a20c3a44b` Lakes Region Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.lrcc.edu/lrcc-admissions/receive-credit-for-prior-learning/ (sha256 9083536f5b5c)
- checks: {"distinct_exams": 21, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[AP-DRAWING|3+]:  ⟵ “Drawing | 3+ | ARTS 111L | Introduction to Drawing | 3.00”
  - equivalencies[AP-CHEMISTRY|3+]:  ⟵ “Chemistry | 3+ | CHEM 138L | General Chemistry I | 4.00”
  - equivalencies[AP-CHEMISTRY|4+]:  ⟵ “Chemistry | 4+ | CHEM 138L and 139L | General Chemistry I and General Chemistry II | 8.00”
  - equivalencies[AP-MACROECONOMICS|3+]:  ⟵ “Macroeconomics | 3+ | SOSC 232L | Macroeconomics | 3.00”
  - equivalencies[AP-MICROECONOMICS|3+]:  ⟵ “Microeconomics | 3+ | SOSC 231L | Microeconomics | 3.00”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Language and Composition | 3+ | ENG 101L | College Composition I | 4.00”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature and Composition | 3+ | ENG 251L | Introduction to Literature | 3.00”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3+]:  ⟵ “French Language and Culture | 3+ | FREN 121L | Elementary French II | 3.00”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3+]:  ⟵ “World History | 3+ | HIST 220L | World History II | 3.00”
  - equivalencies[AP-UNITED-STATES-HISTORY|3+]:  ⟵ “US History | 3+ | HUMA XXXL or SOSC XXXL | Humanities or Social Science Elective | 3.00”
  - equivalencies[AP-BIOLOGY|4+]:  ⟵ “Biology | 4+ | SCI XXXL | Lab Sci Elective | 4.00”
  - equivalencies[AP-STATISTICS|4+]:  ⟵ “Statistics | 4+ | MATH 106L | Statistics I | 4.00”
  - equivalencies[AP-CALCULUS-AB|3+]:  ⟵ “Calculus AB | 3+ | MATH 270L | Calculus I | 4.00”
  - equivalencies[AP-CALCULUS-BC|4+]:  ⟵ “Calculus BC | 4+ | MATH 270L and 271L | Calculus I and Calculus II | 8.00”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “Environmental Science | 3+ | ENVS 150L | Environmental Science | 4.00”
  - equivalencies[AP-2-D-ART-DESIGN|3+]:  ⟵ “2-D Art and Design | 3+ | ARTS 120L | 2-D Design | 3.00”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art and Design | 3+ | ARTS 125L | 3-D Design | 3.00”
  - equivalencies[AP-PSYCHOLOGY|3+]:  ⟵ “Psychology | 3+ | PSYC 125L | Intro to Psychology | 3.00”
  - equivalencies[AP-PHYSICS-1|3+]:  ⟵ “Physics I | 3+ | PHYS 220L | College Physics I | 4.00”
  - equivalencies[AP-PHYSICS-2|3+]:  ⟵ “Physics II | 3+ | PHYS 221L | College Physics II | 4.00”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3+]:  ⟵ “Physics C (Mechanics) | 3+ | SCI XXXL | Science Elective | 4.00”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3+]:  ⟵ “Spanish Language | 3+ | SPAN 120L | Spanish Language and Culture | 3.00”
### `mf7a8451ba5025c6` Lakes Region Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.lrcc.edu/lrcc-admissions/receive-credit-for-prior-learning/ (sha256 9083536f5b5c)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Transfer Credit Credits for college courses taken at another accredited institution or CCSNH campus with a grade of “C” or higher.”
  - min_grade: C ⟵ “Transfer Credit | Lakes Region Community College Skip to main content Course Catalog Search Main navigation Catalog Home Programs Courses Course Schedule Breadcrumb Home Transfer Credit Transfer Credit Download as PDF Students may transfer credits from other accredited colleges, including the colleges within the Community College System of New Hampshire provided they earned a grade of “C” or bette”
### `b5591dae5977623d` NHTI-Concord's Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.nhti.edu/admissions/how-to-apply/early-college/ (sha256 ba9022c4ffb4)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 107.5 ⟵ “Great news: The cost of taking an Early College course at NHTI is 50% the N.H. resident tuition rate – which means you’ll pay $107.50 per credit! You’re responsible for paying for your own books and/or materials and your own transportation to NHTI.”
### `65bbee81615fb403` River Valley Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.rivervalley.edu/wp-content/uploads/2026/08/Advanced-Placement-AP-Test-Acceptance-Policy-for-RVCC-October-2020.pdf (sha256 864d7d00ff95)
- checks: {"distinct_exams": 3, "equivalencies": 3, "rows_without_score": 0}
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “CHEMISTRY                          3                CHEM 140R                               4 S.H.”
  - equivalencies[AP-COMPUTER-SCIENCE-A|5]:  ⟵ “Computer Science A               5                CSCI 185R                               3 S.H.”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language              3        LANG105R                    3 S.H.”
### `e26b0c8cbcfb30b6` River Valley Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.rivervalley.edu/wp-content/uploads/2026/08/CLEP-Scores-Required-for-Transfer-Updated-June-2020.pdf (sha256 ade799c3d27b)
- checks: {"distinct_exams": 13, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                   3 credits                                   50        Non-specific English Elective”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                   4 credits                                   50       ENGL102 College Composition”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                            3 credits                                   50          HUMC110 Humanities in              HOLD”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language: I and II            6 credits                                   50           LNGC105 Spanish I and             HOLD”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and                      3 credits                                   50              PSYC 114 Human”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology               3 credits                                   50        PSYC101 Intro to Psychology”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology                3 credits                                    50        SOSC101 Intro to Sociology”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics          3 credits                                    50          ECOC102 Economics”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                               4 credits                                   50           MATH 210R Calculus I”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                        4 credits                                   50            MATH 1xxR Elective”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics                    6 credits                                   50            MATH 1xxR Elective”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-calculus                           4 credits                                   50          MATH 120R Functions &”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law             3 credits                                        50         BUSC240 Business Law”
### `cb618244c5cf20fd` River Valley Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.rivervalley.edu/transfer-of-credit (sha256 aa3ab6856447)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer of Credit | River Valley Community College Skip to main content College Catalog Fulltext search Main navigation Home Degrees Course Descriptions Course Schedule rivervalley.edu Breadcrumb Home Transfer of Credit Transfer of Credit Download as PDF Students may be admitted to a program with advanced standing if they have completed relevant coursework at another regionally accredited institu”
### `ad3a5fcfbfbf87b9` Saint Anselm College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.anselm.edu/admission/tuition-aid/cost-attendance (sha256 5ad209d48125)
- checks: {"columns": 1, "rows": 5}
  - on_campus:Tuition and Fees:: 52230 ⟵ “Tuition and Fees: | $52,230”
  - on_campus:Food and Housing:: 18400 ⟵ “Food and Housing: | $18,400”
  - on_campus:Books and Supplies:: 1000 ⟵ “Books and Supplies: | $ 1,000”
  - on_campus:Transportation:: 350 ⟵ “Transportation: | $ 350”
  - on_campus:Living Expenses:: 3990 ⟵ “Living Expenses: | $ 3,990”
### `m714f38b2bad1fc8` Saint Anselm College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.anselm.edu/admission/apply/international-applicants/international-transfer-applicants (sha256 a8cea3a35749)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Credit Evaluation Process Transfer credit is awarded for a course at a previous college/university if the student has earned a grade of C or higher, and there is an equivalent course offered at Saint Anselm College.”
  - min_grade: C ⟵ “Credit Evaluation Process Transfer credit is awarded for a course at a previous college/university if the student has earned a grade of C or higher, and there is an equivalent course offered here at Saint Anselm College.”
### `f147b2b85225f4cb` Southern New Hampshire University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.snhu.edu/-/media/files/pdfs/ap-exams-equivalencies.pdf (sha256 2612966b7ed5)
- checks: {"distinct_exams": 27, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                     FAS-201 & 202                FAS-201 & 202              3                   6”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art: 2-D Art & Design/3-D Art & FAS-110 & FAS-ELE            FAS-110 & FAS-ELE          3                   6”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                    MUS-211 & 212                MUS-211 & 212              3                   6”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition ENG-120 and ENG-ELE           ENG-122 and ENG-ELE        3                   6”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature &           LIT-100 and LIT-ELE           LIT-100 and LIT-ELE        3                   6”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                    MAT-225                         MAT-225                 3                    3”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                    MAT-225 & MAT-275               MAT-225 & MAT-275       3                    6”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A             GAM-110 for Game programs; IT- IT-145                   3*                   3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles    IT-ELE                        IT-ELE                     3                   3”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                     MAT-240                       MAT-240                    3                   3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                        BIO-120/120L/121/121L         BIO-120/120L/121/121L      3                   8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                      CHM-120/120L/121/121L         CHM-120/120L/121/121L      3                   8”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science          ENV-101 & ELE                 ENV-101 & ELE              3                   4”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1                      PHY-101/PHY-101L              PHY-101/PHY-101L           3                   4”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2                      PHY-150 & ELE                 PHY-150 & ELE              3                   4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C: Electricity &       PHY-ELE                       PHY-ELE                    3                   4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C: Mechanics           PHY-ELE                       PHY-ELE                    3                   4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Literature**            LFR-211 & LFR-212             LFR-211 & LFR-212         3                    6”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                   HIS-220 & ELE                   HIS-220 & ELE                        3                      6”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government &         POL-210                         POL-210                              3                      3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government &           POL-ELE                         POL-ELE                              3                      3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                    GEO-200                         GEO-200                              3                      3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                     ECO-202                         ECO-202                              3                      3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                     ECO-201                         ECO-201                              3                      3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                         PSY-108                         PSY-108                              3                      3”
  - … 2 more rows
### `95c323bb20d2896c` University of New Hampshire at Manchester — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://manchester.unh.edu/admissions/transfer-students/transferring-community-college (sha256 d44e5b93ded8)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Only courses completed with a grade of C or better will be accepted as transfer credits.”
### `69d01d0ec1d3896d` University of New Hampshire-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://www.unh.edu/financialaid/types-aid/scholarships (sha256 2dc2f36dfcb2)
- checks: {"thresholds": null}
  - award_amount_text: Up to $15,000.00 ⟵ “Chancellor's Scholarship | Up to $15,000.00”
### `7937d404272c159b` University of New Hampshire-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://www.unh.edu/financialaid/types-aid/scholarships (sha256 2dc2f36dfcb2)
- checks: {"thresholds": null}
  - award_amount_text: Up to $12,000.00 ⟵ “Presidential Scholarship | Up to $12,000.00”
### `bab58aae7403f4d9` University of New Hampshire-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://www.unh.edu/financialaid/types-aid/scholarships (sha256 2dc2f36dfcb2)
- checks: {"thresholds": null}
  - award_amount_text: Up to $20,000.00 ⟵ “Trustee's Scholarship | Up to $20,000.00”
### `bb69fae20705b14f` University of New Hampshire-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://www.unh.edu/financialaid/types-aid/scholarships (sha256 2dc2f36dfcb2)
- checks: {"thresholds": null}
  - award_amount_text: Up to $10,000.00 ⟵ “Dean's Scholarship | Up to $10,000.00”
### `732ee8330838342d` University of New Hampshire-Main Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admissions.unh.edu/sites/default/files/media/2026-08/Adm_UNHStanding_Flyer_8.5x11_FY27_web.pdf (sha256 63b338fc9709)
- checks: {"distinct_exams": 3, "equivalencies": 4, "rows_without_score": 0}
  - equivalencies[IB-COMPUTER-SCIENCE|5]:  ⟵ “Math & Computer Science                                                                                                                        5         HIST 421, HIST 422 (HP/WI)                   8 cr.”
  - equivalencies[IB-COMPUTER-SCIENCE|3]:  ⟵ “Computer Science Principles             3,4,5    CS 408 (ETS)                                4 cr.   German Language & Culture                 3         WC                                           4 cr.”
  - equivalencies[IB-LATIN|3]:  ⟵ “Latin                                     3         LATN 403 (E)                                 4 cr.”
  - equivalencies[IB-CHEMISTRY|3]:  ⟵ “Chemistry                               3        CHEM 403 (PS/D-LAB)                         4 cr.                                             4,5       SPAN 503 (WC/FLAN)                           4 cr.”
### `m8fe87cd1a387be3` White Mountains Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.wmcc.edu/transfer-credit (sha256 b497cfb5166d)
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “Transfer Credit | White Mountains Community College Skip to main content Course Catalog Search Main navigation Catalog Home Degrees & Certificates Courses Course Schedule Breadcrumb Home Transfer Credit Transfer Credit Download as PDF Credits earned through other regionally accredited institutions may be transferred to WMCC if students earned a grade of C or better and if the credits are equivalen”
  - min_grade: C ⟵ “Only grades of C or higher are considered for transfer credit.”
  - min_grade: C ⟵ “A grade of C or better is generally required for course transfer credit.”

## Exceptions (78)

### `1f36c20b9ecc2eeb` Colby-Sawyer College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment (sha256 cf65b9bd7534)
- issues: semantic_review_required, conflicting_sources:https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “There is a formal process called Professional Judgment for students with Special or Unusual Circumstances.”
  - sentence: professional_judgment ⟵ “Requests are reviewed on a case-by-case basis by the financial aid director after a Professional Judgement Request form is completed and submitted with all required statements and supporting documentation; students are notified via email of a decision within 30 days.”
### `8476eee60b4c3007` Colby-Sawyer College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.colby-sawyer.edu/admissions/financial-aid (sha256 2bdac86cdde6)
- issues: semantic_review_required, conflicting_sources:https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment,https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “LEARN MORE Professional Judgement Colby-Sawyer recognizes that sometimes the information provided on the FAFSA no longer accurately reflects your financial situation.”
### `a2b450fab27dce28` Colby-Sawyer College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.colby-sawyer.edu/admissions/financial-aid (sha256 c30732a91d04)
- issues: semantic_review_required, conflicting_sources:https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment,https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “LEARN MORE Professional Judgement Colby-Sawyer recognizes that sometimes the information provided on the FAFSA no longer accurately reflects your financial situation.”
### `a6e6fcb3b41d1980` Colby-Sawyer College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment (sha256 4fd7f63cdbb5)
- issues: semantic_review_required, conflicting_sources:https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “There is a formal process called Professional Judgment for students with Special or Unusual Circumstances.”
  - sentence: professional_judgment ⟵ “Requests are reviewed on a case-by-case basis by the financial aid director after a Professional Judgement Request form is completed and submitted with all required statements and supporting documentation; students are notified via email of a decision within 30 days.”
### `c26873ce1b9cfae6` Colby-Sawyer College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment (sha256 4fd7f63cdbb5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to financial situations such as job loss, divorce or the passing of a parent or spouse.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to unique situations such as human trafficking, refugee or asylee status, parental abuse or abandonment that may lead to changing a student’s dependency status, more commonly referred to as dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form Unusual Circumstances – please contact the financial aid office for guidance on next steps.”
### `dbf4d32702e72925` Colby-Sawyer College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.colby-sawyer.edu/admissions/financial-aid (sha256 5ac5fd02a1ec)
- issues: semantic_review_required, conflicting_sources:https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid,https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment,https://www.colby-sawyer.edu/admissions/financial-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “LEARN MORE Professional Judgement Colby-Sawyer recognizes that sometimes the information provided on the FAFSA no longer accurately reflects your financial situation.”
### `176ef6f98e448e12` Dartmouth College — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.dartmouth.edu/glossary-term/special-circumstances (sha256 e6f008d41916)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of Special Circumstances Moving multiple times during high school Care-giving responsibilities Significant out-of-the-home work responsibilities Significant educational interruptions Course offering limitations Other circumstances that have caused you to have a different course schedule or different academic options than your classmates It is up to you whether to share information about y”
### `183eaf714ea376ff` Franklin Pierce University — appeals 2025-26 [new] (labeled_in_source)
- source: https://franklinpierce.edu/admissions/tuition-fees-financial-aid/docs/Financial-Aid-Appeal_2025-2026.pdf (sha256 b45f73dfed8e)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Thus, requests for additional funding should be based on special circumstances of which the Student Financial Services staff might have been unaware of at the time the student’s financial aid application was reviewed.”
  - sentence: need_based_special_circumstances ⟵ “Some examples of special circumstances include the following: divorce; medical bills; loss of income; or death of a parent.”
  - sentence: need_based_special_circumstances ⟵ “Please note that home repairs, private school education, weddings, and major purchases will not be considered as special circumstances warranting an appeal.”
### `3a0afb0c80a75c83` Franklin Pierce University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://franklinpierce.edu/admissions/tuition-fees-financial-aid/forms.html (sha256 e1c974784450)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “FPU Preferred Lender List Professional Judgement: For need-based federal aid programs, financial aid administrators can adjust the Student Aid Index (SAI), adjust the cost of attendance (COA), or change the dependency status (with documentation) when extenuating circumstances exist (for example, if a parent becomes unemployed, disabled or deceased).”
### `42efc2d3403747a1` Franklin Pierce University — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.franklinpierce.edu/satisfactory-academic-progress-sap-for-financial-aid (sha256 68bf884f0ffb)
- issues: semantic_review_required, conflicting_sources:https://franklinpierce.edu/admissions/tuition-fees-financial-aid/docs/SAP_AppealForm.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal Process A student who loses aid eligibility due to failure to maintain SAP may appeal this status.”
  - sentence: sap_appeal ⟵ “To do so, the student must submit a Financial Aid SAP Appeal form and submit it to the OSFS for review.”
### `55b8200e24d30c68` Franklin Pierce University — appeals 2026-27 [new] (labeled_in_source)
- source: https://franklinpierce.edu/admissions/tuition-fees-financial-aid/docs/Financial-Aid-Appeal-2026-2027.pdf (sha256 b18fed1b1e40)
- issues: semantic_review_required, conflicting_sources:https://catalog.franklinpierce.edu/satisfactory-academic-progress-sap-for-financial-aid,https://franklinpierce.edu/admissions/tuition-fees-financial-aid/forms.html
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Thus, requests for additional funding should be based on special circumstances of which the Student Financial Services staff might have been unaware of at the time the student’s financial aid application was reviewed.”
  - sentence: need_based_special_circumstances ⟵ “Some examples of special circumstances include the following: divorce; medical bills; loss of income; or death of a parent.”
  - sentence: need_based_special_circumstances ⟵ “Please note that home repairs, private school education, weddings, and major purchases will not be considered as special circumstances warranting an appeal.”
### `acf9df1f7cae08a6` Franklin Pierce University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://franklinpierce.edu/admissions/tuition-fees-financial-aid/forms.html (sha256 e1c974784450)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://catalog.franklinpierce.edu/satisfactory-academic-progress-sap-for-financial-aid,https://franklinpierce.edu/admissions/tuition-fees-financial-aid/docs/Financial-Aid-Appeal-2026-2027.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal: An appeal process is available to any student who has had a change in financial circumstances or has been determined ineligible for continued aid if extenuating circumstances prevented them from maintaining satisfactory academic progress.”
### `b01878d683f1f5c4` Franklin Pierce University — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.franklinpierce.edu/satisfactory-academic-progress-sap-for-financial-aid (sha256 68bf884f0ffb)
- issues: semantic_review_required, conflicting_sources:https://franklinpierce.edu/admissions/tuition-fees-financial-aid/docs/Financial-Aid-Appeal-2026-2027.pdf,https://franklinpierce.edu/admissions/tuition-fees-financial-aid/forms.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The student’s appeal must address the following: The basis for the appeal – a description of the special circumstance and The reason why the student failed to meet the SAP standard(s) and What has changed in the student’s situation so that s/he will now be able to meet SAP standards.”
### `f36524f13e60dfc6` Franklin Pierce University — appeals 2026-27 [new] (source_unlabeled)
- source: https://franklinpierce.edu/admissions/tuition-fees-financial-aid/docs/SAP_AppealForm.pdf (sha256 8db39a023912)
- issues: semantic_review_required, conflicting_sources:https://catalog.franklinpierce.edu/satisfactory-academic-progress-sap-for-financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form FAX: 603-899-4372 E-mail: osfs@franklinpierce.edu / / Student’s Name Date ID # Request for Financial Aid Probation All students receiving financial assistance are required to make Satisfactory Academic Progress as a condition of receiving financial aid.”
### `31616933bd1430dd` Franklin Pierce University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.franklinpierce.edu/tuition-and-fees (sha256 d2382355f772)
- issues: conflicting_sources:https://franklinpierce.edu/admissions/tuition-fees-financial-aid/cost-of-attendence.html,https://franklinpierce.edu/admissions/tuition-fees-financial-aid/tuition-fees.html
- checks: {"columns": 1, "rows": 14}
  - column:ACH/Wire returned fee: 25 ⟵ “ACH/Wire returned fee | $25”
  - column:Returned check fee: 25 ⟵ “Returned check fee | $25”
  - column:Collection Fee, balances below $199: 125 ⟵ “Collection Fee, balances below $199 | $125”
  - column:Collection Fee, balances above $200: 225 ⟵ “Collection Fee, balances above $200 | $225”
  - column:Student ID replacement fee: 80 ⟵ “Student ID replacement fee | $80”
  - column:Replace P.O. Box key: 35 ⟵ “Replace P.O. Box key | $35”
  - column:Replace P.O. Lock: 35 ⟵ “Replace P.O. Lock | $35”
  - column:Late Payment fee: 225 ⟵ “Late Payment fee | $225”
  - column:Tuition Exchange fee: 700 ⟵ “Tuition Exchange fee | $700”
  - column:Private Music instruction fee: 275 ⟵ “Private Music instruction fee | $275”
  - column:Residential Administrative fee: 1225 ⟵ “Residential Administrative fee | $1,225”
  - column:Improper check-out fee: 100 ⟵ “Improper check-out fee | $100”
  - column:Unauthorized room change: 100 ⟵ “Unauthorized room change | $100”
  - column:Unauthorized room change during campus closure: 200 ⟵ “Unauthorized room change during campus closure | $200”
### `8bc97528b8ff2dad` Franklin Pierce University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://franklinpierce.edu/admissions/tuition-fees-financial-aid/tuition-fees.html (sha256 0a86474c5e36)
- issues: conflicting_sources:https://catalog.franklinpierce.edu/tuition-and-fees,https://franklinpierce.edu/admissions/tuition-fees-financial-aid/cost-of-attendence.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (Fulltime): 44276 ⟵ “Tuition (Fulltime) | $44,276 | $22,138 | $22,138”
  - column:Administrative Fee: 5024 ⟵ “Administrative Fee | $5,024 | $2,512 | $2,512”
  - column:Housing (Standard): 10700 ⟵ “Housing (Standard) | $10,700 | $5,350 | $5,350”
  - column:Meals (Standard): 7500 ⟵ “Meals (Standard) | $7,500 | $3,750 | $3,750”
  - column:Total Direct Costs: 67500 ⟵ “Total Direct Costs | $67,500 | $33,750 | $33,750”
### `ead031728ad80454` Franklin Pierce University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://franklinpierce.edu/admissions/tuition-fees-financial-aid/cost-of-attendence.html (sha256 199521806450)
- issues: conflicting_sources:https://catalog.franklinpierce.edu/tuition-and-fees,https://franklinpierce.edu/admissions/tuition-fees-financial-aid/tuition-fees.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition (Full-time): 44276 ⟵ “Tuition (Full-time) | $44,276 | $22,138 | $22,138”
  - column:Administrative Fee: 5024 ⟵ “Administrative Fee | $5,024 | $2,512 | $2,512”
  - column:Housing (Standard): 10700 ⟵ “Housing (Standard) | $10,700 | $5,350 | $5,350”
  - column:Meals (Standard): 7500 ⟵ “Meals (Standard) | $7,500 | $3,750 | $3,750”
  - column:Books & Supplies: 1200 ⟵ “Books & Supplies | $1,200 | $600 | $600”
  - column:Transportation: 1000 ⟵ “Transportation | $1,000 | $500 | $500”
  - column:Miscellaneous Expenses: 1000 ⟵ “Miscellaneous Expenses | $1,000 | $500 | $500”
  - column:Federal Loan Fees: 70 ⟵ “Federal Loan Fees | $70 | $35 | $35”
  - column:Total Cost of Attendance = Direct + Indirect Costs: 70770 ⟵ “Total Cost of Attendance = Direct + Indirect Costs | $70,770 | $35,385 | $35,385”
  - column:Total Direct Costs: 67500 ⟵ “Total Direct Costs | $67,500 | $33,750 | $33,750”
  - column:Total Indirect Costs: 3270 ⟵ “Total Indirect Costs | $3,270 | $1,635 | $1,635”
### `8684643acaf53081` Great Bay Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.greatbay.edu/paying-for-great-bay/financial-aid/ (sha256 b51e69ffd0bc)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress for Financial Aid (SAPFA) Satisfactory Academic Progress (SAP) appeal form Review the standards on our Financial Aid Policies page.”
### `03ff54bc79006c88` Keene State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/aid/award-conditions (sha256 eb3752aa31f9)
- issues: semantic_review_required, conflicting_sources:https://www.keene.edu/admissions/aid/applying-financial-aid,https://www.keene.edu/admissions/aid/applying-financial-aid/special-conditions,https://www.keene.edu/admissions/aid/award-conditions/satisfactory-academic-progress,https://www.keene.edu/admissions/aid/financial-aid/resources-administration/using-data-retrieval-tool-drt
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Conditions The US Department of Education gives the Student Financial Services Office (SFSO) latitude in considering special circumstances not reflected on the FAFSA.”
### `0689599dcc69953f` Keene State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/aid/award-conditions/satisfactory-academic-progress (sha256 2f5b6ce46fca)
- issues: semantic_review_required, conflicting_sources:https://www.keene.edu/admissions/aid/applying-financial-aid,https://www.keene.edu/admissions/aid/applying-financial-aid/special-conditions,https://www.keene.edu/admissions/aid/award-conditions,https://www.keene.edu/admissions/aid/financial-aid/resources-administration/using-data-retrieval-tool-drt
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal Process Students who do not meet the minimum SAP requirements for continuance of financial aid have the right to appeal when special circumstances exist.”
### `1ddfa889a7774c5e` Keene State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/aid/applying-financial-aid/special-conditions (sha256 b3897b975591)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Situations that might warrant a dependency override include: The student’s voluntary or involuntary removal from the parents’ home due to an abusive situation that threatened the student’s safety and/or health The student’s abandonment by parents A student’s inability to locate the parents.”
  - sentence: dependency_override ⟵ “Please note that a student applying for a dependency override will be asked to provide a personal statement along with documentation from two professional third parties confirming the circumstances.”
### `32235f9c0331a3d4` Keene State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/aid/award-conditions/satisfactory-academic-progress (sha256 2f5b6ce46fca)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Conditions when a student may appeal include: If you or an immediate family member experienced a serious injury, illness or mental health condition If you experienced the death of immediate family member If you experienced other circumstances beyond your control If you chose to appeal, you will need to: Complete an SAP Appeal Form: for the correct academic year or write a letter detailing the circ”
### `35611af049ae86a4` Keene State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/aid/award-conditions (sha256 eb3752aa31f9)
- issues: semantic_review_required, conflicting_sources:https://www.keene.edu/admissions/aid/applying-financial-aid/special-conditions
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special circumstances that might call for the Student Financial Services Office to use professional judgment include loss or reduction of income, changes in family dynamics not shown on tax returns, and unreimbursed medical expenses.”
### `501f19288373cbec` Keene State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/aid/applying-financial-aid (sha256 d497b2d59f80)
- issues: semantic_review_required, conflicting_sources:https://www.keene.edu/admissions/aid/applying-financial-aid/special-conditions,https://www.keene.edu/admissions/aid/award-conditions,https://www.keene.edu/admissions/aid/award-conditions/satisfactory-academic-progress,https://www.keene.edu/admissions/aid/financial-aid/resources-administration/using-data-retrieval-tool-drt
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Conditions The US Department of Education gives the College's Financial Aid Office latitude in considering special circumstances not reflected on the FAFSA.”
### `951c21edb764d07d` Keene State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/aid/financial-aid/resources-administration/using-data-retrieval-tool-drt (sha256 7dc2d366a3e4)
- issues: semantic_review_required, conflicting_sources:https://www.keene.edu/admissions/aid/applying-financial-aid,https://www.keene.edu/admissions/aid/applying-financial-aid/special-conditions,https://www.keene.edu/admissions/aid/award-conditions,https://www.keene.edu/admissions/aid/award-conditions/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Amended Returns & Special Circumstances Verification of 2016 IRS Income Tax Return Information for Individuals Who Filed an Amended IRS Income Tax Return If an individual filed an amended IRS income tax return for tax year 2016, provide both of the following: An IRS Tax Return Transcript (signature not required) for the 2016 tax year; and A signed copy of the 2016 IRS Form 1040X, “Amended U.S.”
### `9a8589b630b8f4ba` Keene State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/aid/applying-financial-aid/special-conditions (sha256 b3897b975591)
- issues: semantic_review_required, conflicting_sources:https://www.keene.edu/admissions/aid/award-conditions
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special circumstances that might call for the Student Financial Services Office’s professional judgment include loss or reduction of income, changes in family dynamics not shown on tax returns, and unreimbursed medical expenses.”
### `e21ba4954600f6e7` Keene State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/aid/applying-financial-aid/special-conditions (sha256 b3897b975591)
- issues: semantic_review_required, conflicting_sources:https://www.keene.edu/admissions/aid/applying-financial-aid,https://www.keene.edu/admissions/aid/award-conditions,https://www.keene.edu/admissions/aid/award-conditions/satisfactory-academic-progress,https://www.keene.edu/admissions/aid/financial-aid/resources-administration/using-data-retrieval-tool-drt
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The following conditions do not qualify as unusual circumstances, either individually or in combination: Parents who refuse to contribute, are unwilling to provide information, or do not claim the student as an income tax dependent A student who demonstrates total self-sufficiency A student whose parents live in another country.”
### `0b53b4c8fb7a189e` Keene State College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.keene.edu/admissions/tuition-cost (sha256 a7ba92fb88dc)
- issues: conflicting_sources:https://www.keene.edu/admissions/aid,https://www.keene.edu/admissions/aid/award
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (full-time): 12348 ⟵ “Tuition (full-time) | $12,348 | $25,016”
  - column:Room (Standard Double): 9040 ⟵ “Room (Standard Double) | $9,040 | $9,040”
  - column:Board (Owl Access): 5586 ⟵ “Board (Owl Access) | $5,586 | $5,586”
  - column:Mandatory Fees: 3184 ⟵ “Mandatory Fees | $3,184 | $3,184”
  - column:Total: 30158 ⟵ “Total | $30,158 | $42,826”
### `2ad088c8f38fd17a` Keene State College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.keene.edu/admissions/aid (sha256 1204ffa419dd)
- issues: conflicting_sources:https://www.keene.edu/admissions/aid/award,https://www.keene.edu/admissions/tuition-cost
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (full-time): 12348 ⟵ “Tuition (full-time) | $12,348 | $25,016”
  - column:Room (Standard Double): 9040 ⟵ “Room (Standard Double) | $9,040 | $9,040”
  - column:Board (Owl Access): 5586 ⟵ “Board (Owl Access) | $5,586 | $5,586”
  - column:Mandatory Fees: 3184 ⟵ “Mandatory Fees | $3,184 | $3,184”
  - column:Total: 30158 ⟵ “Total | $30,158 | $42,826”
### `8840f7f8ab957aac` Keene State College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.keene.edu/admissions/aid/award (sha256 933e770ad071)
- issues: conflicting_sources:https://www.keene.edu/admissions/aid,https://www.keene.edu/admissions/tuition-cost
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (full-time): 25016 ⟵ “Tuition (full-time) | $12,348 | $25,016”
  - column:Room (Standard Double): 9040 ⟵ “Room (Standard Double) | $9,040 | $9,040”
  - column:Board (Owl Access): 5586 ⟵ “Board (Owl Access) | $5,586 | $5,586”
  - column:Mandatory Fees: 3184 ⟵ “Mandatory Fees | $3,184 | $3,184”
  - column:Total: 42826 ⟵ “Total | $30,158 | $42,826”
### `a6cc1771057c501b` Keene State College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.keene.edu/admissions/tuition-cost (sha256 a7ba92fb88dc)
- issues: conflicting_sources:https://www.keene.edu/admissions/aid,https://www.keene.edu/admissions/aid/award
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (full-time): 25016 ⟵ “Tuition (full-time) | $12,348 | $25,016”
  - column:Room (Standard Double): 9040 ⟵ “Room (Standard Double) | $9,040 | $9,040”
  - column:Board (Owl Access): 5586 ⟵ “Board (Owl Access) | $5,586 | $5,586”
  - column:Mandatory Fees: 3184 ⟵ “Mandatory Fees | $3,184 | $3,184”
  - column:Total: 42826 ⟵ “Total | $30,158 | $42,826”
### `abbb47906f2f4f28` Keene State College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.keene.edu/admissions/aid/award (sha256 933e770ad071)
- issues: conflicting_sources:https://www.keene.edu/admissions/aid,https://www.keene.edu/admissions/tuition-cost
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (full-time): 12348 ⟵ “Tuition (full-time) | $12,348 | $25,016”
  - column:Room (Standard Double): 9040 ⟵ “Room (Standard Double) | $9,040 | $9,040”
  - column:Board (Owl Access): 5586 ⟵ “Board (Owl Access) | $5,586 | $5,586”
  - column:Mandatory Fees: 3184 ⟵ “Mandatory Fees | $3,184 | $3,184”
  - column:Total: 30158 ⟵ “Total | $30,158 | $42,826”
### `c1113a3d504b2b39` Keene State College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.keene.edu/admissions/aid (sha256 1204ffa419dd)
- issues: conflicting_sources:https://www.keene.edu/admissions/aid/award,https://www.keene.edu/admissions/tuition-cost
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (full-time): 25016 ⟵ “Tuition (full-time) | $12,348 | $25,016”
  - column:Room (Standard Double): 9040 ⟵ “Room (Standard Double) | $9,040 | $9,040”
  - column:Board (Owl Access): 5586 ⟵ “Board (Owl Access) | $5,586 | $5,586”
  - column:Mandatory Fees: 3184 ⟵ “Mandatory Fees | $3,184 | $3,184”
  - column:Total: 42826 ⟵ “Total | $30,158 | $42,826”
### `a5e37f8ec7454a62` Keene State College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.keene.edu/admissions/transfer-students (sha256 bb15201c3727)
- issues: conflicting_values:min_grade
- checks: {"fields": []}
### `fcfb3c09247ff6b6` Manchester Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://mccnh.edu/wp-content/uploads/2025/CLEP-Exams-Offered.pdf (sha256 103f66c04984)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 13, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature    50                English Elective        3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and          50                ENGL207M                3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|4]:  ⟵ “College Composition 50                   ENGL110M                4”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|3]:  ⟵ “College Composition 50                   ENGL110M                3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature     50                ENGL200M                3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities             50                Humanities Elective     3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language        50                FREN110M French I       Up to 4       Depending on score”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language       50                SPAN110M Spanish I      Up to 4       Depending on score”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish with           50                SPAN110M                6”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and       50                PSYC210M                3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus               50   MATH204M                4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry              50   CHEM140M                3 or 4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra        50   Math151M                4”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus            50   MATH171M                4”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|3]:  ⟵ “Financial Accounting 50     ACCT113M Intro to       3”
### `ed90fe80ba8e45e0` NHTI-Concord's Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nhti.edu/financial-aid/ (sha256 0f7512c0ee2c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Probation: A student who becomes ineligible for federal student aid may appeal for a review of that determination.”
### `7307b66eb2dd8164` NHTI-Concord's Community College — awards 2019-20 [new] (labeled_in_source)
- source: https://www.nhti.edu/financial-aid/scholarship-grants/ (sha256 c3dfc2cc040b)
- issues: stale_year_label:2019-20
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Dental Hygiene Second Year Student | $500”
### `809e9f698447ec55` NHTI-Concord's Community College — awards 2019-20 [new] (labeled_in_source)
- source: https://www.nhti.edu/financial-aid/scholarship-grants/ (sha256 c3dfc2cc040b)
- issues: stale_year_label:2019-20
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Dental Assisting Student | $500”
### `e0c5088a75aa0766` NHTI-Concord's Community College — awards 2019-20 [new] (labeled_in_source)
- source: https://www.nhti.edu/financial-aid/scholarship-grants/ (sha256 c3dfc2cc040b)
- issues: stale_year_label:2019-20
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Dental Hygiene First Year Student | $500”
### `4ae5fb0f0528fbfb` Plymouth State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/psu-policies/satisfactory-academic-progress-policy (sha256 754b9f048d52)
- issues: semantic_review_required, conflicting_sources:https://coursecatalog.plymouth.edu/financial-aid/undergraduate/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students who must remain enrolled beyond their maximum time frame due to a change of major will be required to submit an SAP appeal once they reach their maximum time frame.”
  - sentence: sap_appeal ⟵ “Please note: Students placed on a 2nd financial aid suspension are unlikely to have a second SAP appeal approved.”
### `70a1ae4bf1e12a77` Plymouth State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/psu-policies/satisfactory-academic-progress-policy (sha256 754b9f048d52)
- issues: semantic_review_required, conflicting_sources:https://coursecatalog.plymouth.edu/financial-aid/undergraduate/,https://www.plymouth.edu/student-financial-services/policies/residency-information-appeals
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal Process Students who do not meet the minimum SAP requirements for continuance of financial aid have the right to appeal when special circumstances exist.”
### `8c66d2d095d8d69e` Plymouth State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://coursecatalog.plymouth.edu/financial-aid/undergraduate/ (sha256 4c2fa8a7c1c1)
- issues: semantic_review_required, conflicting_sources:https://www.plymouth.edu/student-financial-services/policies/residency-information-appeals,https://www.plymouth.edu/student-financial-services/psu-policies/satisfactory-academic-progress-policy
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal Process Students who do not meet the minimum SAP requirements for continuance of financial aid have the right to appeal when special circumstances exist.”
### `96d6daeb06058a07` Plymouth State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://coursecatalog.plymouth.edu/financial-aid/undergraduate/ (sha256 4c2fa8a7c1c1)
- issues: semantic_review_required, conflicting_sources:https://www.plymouth.edu/student-financial-services/psu-policies/satisfactory-academic-progress-policy
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please note: Students placed on a second SAP ineligible status are unlikely to have a second SAP appeal approved.”
### `fd4578bb79da6e16` Plymouth State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/policies/residency-information-appeals (sha256 d82820edd769)
- issues: semantic_review_required, conflicting_sources:https://coursecatalog.plymouth.edu/financial-aid/undergraduate/,https://www.plymouth.edu/student-financial-services/psu-policies/satisfactory-academic-progress-policy
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Residency Officer Office of Student Financial Services Speare 1st Floor Plymouth State University Plymouth, NH 03264 A change in residency status could result in a change in your financial aid award, specifically your merit award.”
  - sentence: need_based_special_circumstances ⟵ “A change in residency status could result in a change in your financial aid award, specifically your merit award.”
### `04c56ab0a6daf5b5` Plymouth State University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.plymouth.edu/admissions/financial-assistance/scholarships (sha256 fff894c8b230)
- issues: ambiguous_year_labels, conflicting_sources:https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $4,000 ⟵ “2.50 – 2.74 | Promise | $4,000 | $8,000”
  - gpa_requirement: 2.50 – 2.74 ⟵ “2.50 – 2.74 | Promise | $4,000 | $8,000”
### `32f8abd141b3fa9f` Plymouth State University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.plymouth.edu/admissions/financial-assistance/scholarships (sha256 fff894c8b230)
- issues: ambiguous_year_labels, conflicting_sources:https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “<2.24 | Strive | $1,000 | $1,000”
  - gpa_requirement: <2.24 ⟵ “<2.24 | Strive | $1,000 | $1,000”
### `4c8ccb78238383da` Plymouth State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships (sha256 06b53b21c7a2)
- issues: duplicate_table_versions, conflicting_sources:https://www.plymouth.edu/admissions/financial-assistance/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “2.25 – 2.49 | Achieve | $2,000 | $4,000”
  - gpa_requirement: 2.25 – 2.49 ⟵ “2.25 – 2.49 | Achieve | $2,000 | $4,000”
### `5b863c2edb797071` Plymouth State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships (sha256 06b53b21c7a2)
- issues: duplicate_table_versions, conflicting_sources:https://www.plymouth.edu/admissions/financial-assistance/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “2.75 – 3.24 | Aspire | $5,000 | $12,000”
  - gpa_requirement: 2.75 – 3.24 ⟵ “2.75 – 3.24 | Aspire | $5,000 | $12,000”
### `5ecd18af381691fe` Plymouth State University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.plymouth.edu/admissions/financial-assistance/scholarships (sha256 fff894c8b230)
- issues: ambiguous_year_labels, conflicting_sources:https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “2.25 – 2.49 | Achieve | $2,000 | $4,000”
  - gpa_requirement: 2.25 – 2.49 ⟵ “2.25 – 2.49 | Achieve | $2,000 | $4,000”
### `7d93b7bebe903619` Plymouth State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships (sha256 06b53b21c7a2)
- issues: duplicate_table_versions, conflicting_sources:https://www.plymouth.edu/admissions/financial-assistance/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “3.25 – 3.74 | Dean’s | $6,000 | $13,000”
  - gpa_requirement: 3.25 – 3.74 ⟵ “3.25 – 3.74 | Dean’s | $6,000 | $13,000”
### `a243ab4974830c54` Plymouth State University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.plymouth.edu/admissions/financial-assistance/scholarships (sha256 fff894c8b230)
- issues: ambiguous_year_labels, conflicting_sources:https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “3.25 – 3.74 | Dean’s | $6,000 | $13,000”
  - gpa_requirement: 3.25 – 3.74 ⟵ “3.25 – 3.74 | Dean’s | $6,000 | $13,000”
### `a24d441121671f80` Plymouth State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships (sha256 06b53b21c7a2)
- issues: duplicate_table_versions, conflicting_sources:https://www.plymouth.edu/admissions/financial-assistance/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $4,000 ⟵ “2.50 – 2.74 | Promise | $4,000 | $8,000”
  - gpa_requirement: 2.50 – 2.74 ⟵ “2.50 – 2.74 | Promise | $4,000 | $8,000”
### `d3b9b3c6f0638cf3` Plymouth State University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.plymouth.edu/admissions/financial-assistance/scholarships (sha256 fff894c8b230)
- issues: ambiguous_year_labels, conflicting_sources:https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “2.75 – 3.24 | Aspire | $5,000 | $12,000”
  - gpa_requirement: 2.75 – 3.24 ⟵ “2.75 – 3.24 | Aspire | $5,000 | $12,000”
### `dfff4ce4a3c45d1d` Plymouth State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships (sha256 06b53b21c7a2)
- issues: duplicate_table_versions, conflicting_sources:https://www.plymouth.edu/admissions/financial-assistance/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $7,000 ⟵ “3.75 – 4.00 | Presidential | $7,000 | $14,000”
  - gpa_requirement: 3.75 – 4.00 ⟵ “3.75 – 4.00 | Presidential | $7,000 | $14,000”
### `e338381acdce80c6` Plymouth State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships (sha256 06b53b21c7a2)
- issues: duplicate_table_versions, conflicting_sources:https://www.plymouth.edu/admissions/financial-assistance/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “< 2.24 | Strive | $1,000 | $1,000”
  - gpa_requirement: < 2.24 ⟵ “< 2.24 | Strive | $1,000 | $1,000”
### `ea6ed31a7518fd22` Plymouth State University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.plymouth.edu/admissions/financial-assistance/scholarships (sha256 fff894c8b230)
- issues: ambiguous_year_labels, conflicting_sources:https://www.plymouth.edu/student-financial-services/financial-essentials/scholarships
- checks: {"thresholds": null}
  - award_amount_text: $7,000 ⟵ “3.75 – 4.00 | Presidential | $7,000 | $14,000”
  - gpa_requirement: 3.75 – 4.00 ⟵ “3.75 – 4.00 | Presidential | $7,000 | $14,000”
### `0ba5e9cdb828ecbd` Plymouth State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/billing-information/tuition-fees (sha256 dc2cac8a9e7e)
- issues: components_do_not_reconcile, conflicting_sources:https://www.plymouth.edu/sites/default/files/media/2026-03/FY27_Tuition-Fee-Rates.pdf
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - on_campus:Tuition: 12755 ⟵ “Tuition | $9,205 | $12,755”
  - on_campus:Mandatory Fees: 675 ⟵ “Mandatory Fees | $675 | $675”
  - on_campus:Enrollment Fees: 30 ⟵ “Enrollment Fees | $30 | $30”
  - on_campus:Per Term Total: 13460 ⟵ “Per Term Total | $9,910 | $13,460”
  - on_campus:Program Fees (MS in Athletic Training only): 430 ⟵ “Program Fees (MS in Athletic Training only) | $430 | $430”
  - on_campus:Total Annual Direct Billed Costs: 26920 ⟵ “Total Annual Direct Billed Costs | $19,820 | $26,920”
### `76f6ef051f680963` Plymouth State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/billing-information/tuition-fees (sha256 dc2cac8a9e7e)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.plymouth.edu/sites/default/files/media/2026-03/FY27_Tuition-Fee-Rates.pdf
- checks: {"columns": 2, "components_reconcile": true, "rows": 2}
  - with_parents_or_family:Tuition & Mandatory Fees2 (Full-time): 15444 ⟵ “Tuition & Mandatory Fees2 (Full-time) | $15,444 | $26,872 | $15,444 | $23,872”
  - with_parents_or_family:Total Billed Costs: 15444 ⟵ “Total Billed Costs | $29,452 | $40,880 | $15,444 | $37,880”
  - column:Tuition & Mandatory Fees2 (Full-time): 23872 ⟵ “Tuition & Mandatory Fees2 (Full-time) | $15,444 | $26,872 | $15,444 | $23,872”
  - column:Room & Meals3: 14008 ⟵ “Room & Meals3 | $14,008 | $14,008 | NA | $14,008”
  - column:Total Billed Costs: 37880 ⟵ “Total Billed Costs | $29,452 | $40,880 | $15,444 | $37,880”
### `9bc539abd94eb820` Plymouth State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.plymouth.edu/sites/default/files/media/2026-03/FY27_Tuition-Fee-Rates.pdf (sha256 6a7f64bd8d0b)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.plymouth.edu/student-financial-services/billing-information/tuition-fees
- checks: {"columns": 6, "rows": 3}
  - column:Tuition Full Time: 12536 ⟵ “Tuition Full Time | $ 12,536 $ | 23,964 $ | 20,964 | $ | 6,268 $ | 11,982 $ | 10,482”
  - column:Mandatory Fees: 2908 ⟵ “Mandatory Fees | $ 2,908 $ | 2,908 $ | 2,908 | $ | 1,454 $ | 1,454 $ | 1,454”
  - column:Reinstatement Activation Fee if dropped for non-payment $: 100 ⟵ “Reinstatement Activation Fee if dropped for non-payment $ | 100 $ | 100 | $ | 100”
  - column:Tuition Full Time: 20964 ⟵ “Tuition Full Time | $ 12,536 $ | 23,964 $ | 20,964 | $ | 6,268 $ | 11,982 $ | 10,482”
  - column:Mandatory Fees: 2908 ⟵ “Mandatory Fees | $ 2,908 $ | 2,908 $ | 2,908 | $ | 1,454 $ | 1,454 $ | 1,454”
  - column:Orientation Fee:: 335 ⟵ “Orientation Fee: | New Admits & Transfers $ | 335 $ | 335 $ | 335 | $ | 335 $ | 335 $ | 335”
  - column:Enrollment Fee:: 100 ⟵ “Enrollment Fee: | New and Re-Admits $ | 100 $ | 100 $ | 100 | $ | 100 $ | 100 $ | 100”
  - column:Tuition Full Time: 6268 ⟵ “Tuition Full Time | $ 12,536 $ | 23,964 $ | 20,964 | $ | 6,268 $ | 11,982 $ | 10,482”
  - column:Mandatory Fees: 1454 ⟵ “Mandatory Fees | $ 2,908 $ | 2,908 $ | 2,908 | $ | 1,454 $ | 1,454 $ | 1,454”
  - column:International Students: 435 ⟵ “International Students | ---- $ | 435 | ---- | ---- $ | 435 | ----”
  - column:Tuition Full Time: 11982 ⟵ “Tuition Full Time | $ 12,536 $ | 23,964 $ | 20,964 | $ | 6,268 $ | 11,982 $ | 10,482”
  - column:Mandatory Fees: 1454 ⟵ “Mandatory Fees | $ 2,908 $ | 2,908 $ | 2,908 | $ | 1,454 $ | 1,454 $ | 1,454”
  - column:Orientation Fee:: 335 ⟵ “Orientation Fee: | New Admits & Transfers $ | 335 $ | 335 $ | 335 | $ | 335 $ | 335 $ | 335”
  - column:Enrollment Fee:: 100 ⟵ “Enrollment Fee: | New and Re-Admits $ | 100 $ | 100 $ | 100 | $ | 100 $ | 100 $ | 100”
  - column:Tuition Full Time: 10482 ⟵ “Tuition Full Time | $ 12,536 $ | 23,964 $ | 20,964 | $ | 6,268 $ | 11,982 $ | 10,482”
  - column:Mandatory Fees: 1454 ⟵ “Mandatory Fees | $ 2,908 $ | 2,908 $ | 2,908 | $ | 1,454 $ | 1,454 $ | 1,454”
  - column:Orientation Fee:: 335 ⟵ “Orientation Fee: | New Admits & Transfers $ | 335 $ | 335 $ | 335 | $ | 335 $ | 335 $ | 335”
  - column:Enrollment Fee:: 100 ⟵ “Enrollment Fee: | New and Re-Admits $ | 100 $ | 100 $ | 100 | $ | 100 $ | 100 $ | 100”
  - column:Orientation Fee:: 335 ⟵ “Orientation Fee: | New Admits & Transfers $ | 335 $ | 335 $ | 335 | $ | 335 $ | 335 $ | 335”
  - column:Enrollment Fee:: 100 ⟵ “Enrollment Fee: | New and Re-Admits $ | 100 $ | 100 $ | 100 | $ | 100 $ | 100 $ | 100”
### `a36ecbdd886d8d43` Plymouth State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.plymouth.edu/student-financial-services/billing-information/tuition-fees (sha256 dc2cac8a9e7e)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - on_campus:Tuition: 9205 ⟵ “Tuition | $9,205 | $12,755”
  - on_campus:Mandatory Fees: 675 ⟵ “Mandatory Fees | $675 | $675”
  - on_campus:Enrollment Fees: 30 ⟵ “Enrollment Fees | $30 | $30”
  - on_campus:Per Term Total: 9910 ⟵ “Per Term Total | $9,910 | $13,460”
  - on_campus:Program Fees (MS in Athletic Training only): 430 ⟵ “Program Fees (MS in Athletic Training only) | $430 | $430”
  - on_campus:Total Annual Direct Billed Costs: 19820 ⟵ “Total Annual Direct Billed Costs | $19,820 | $26,920”
### `fc943e2e1a25bedf` Plymouth State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.plymouth.edu/sites/default/files/media/2026-03/FY27_Tuition-Fee-Rates.pdf (sha256 6a7f64bd8d0b)
- issues: conflicting_sources:https://www.plymouth.edu/student-financial-services/billing-information/tuition-fees
- checks: {"columns": 2, "rows": 8}
  - on_campus:Tuition Full Time: 23964 ⟵ “Tuition Full Time | $ 12,536 $ | 23,964 $ | 20,964 | $ | 6,268 $ | 11,982 $ | 10,482”
  - on_campus:Mandatory Fees: 2908 ⟵ “Mandatory Fees | $ 2,908 $ | 2,908 $ | 2,908 | $ | 1,454 $ | 1,454 $ | 1,454”
  - on_campus:Orientation Fee:: 335 ⟵ “Orientation Fee: | New Admits & Transfers $ | 335 $ | 335 $ | 335 | $ | 335 $ | 335 $ | 335”
  - on_campus:International Students: 435 ⟵ “International Students | ---- $ | 435 | ---- | ---- $ | 435 | ----”
  - on_campus:Enrollment Fee:: 100 ⟵ “Enrollment Fee: | New and Re-Admits $ | 100 $ | 100 $ | 100 | $ | 100 $ | 100 $ | 100”
  - on_campus:Reinstatement Activation Fee if dropped for non-payment $: 100 ⟵ “Reinstatement Activation Fee if dropped for non-payment $ | 100 $ | 100 | $ | 100”
  - on_campus:Tuition: 470 ⟵ “Tuition | $ | 470 | $ | 550 | Bill available online | November 6, 2026”
  - on_campus:Mandatory Fees (2): 98 ⟵ “Mandatory Fees | $ | 98 | $ | 98 | Bill due | December 4, 2026”
  - on_campus:Orientation Fee:: 335 ⟵ “Orientation Fee: | New Admits & Transfers $ | 335 $ | 335 $ | 335 | $ | 335 $ | 335 $ | 335”
  - on_campus:Enrollment Fee:: 100 ⟵ “Enrollment Fee: | New and Re-Admits $ | 100 $ | 100 $ | 100 | $ | 100 $ | 100 $ | 100”
  - on_campus:Reinstatement Activation Fee if dropped for non-payment $: 100 ⟵ “Reinstatement Activation Fee if dropped for non-payment $ | 100 $ | 100 | $ | 100”
  - on_campus:Tuition: 550 ⟵ “Tuition | $ | 470 | $ | 550 | Bill available online | November 6, 2026”
  - on_campus:Mandatory Fees: 98 ⟵ “Mandatory Fees | $ | 98 | $ | 98 | Bill due | December 4, 2026”
### `1794ba70df8e40a3` Saint Anselm College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.anselm.edu/about/leadership-initiatives/initiatives/consumer-information/undergraduate-satisfactory-academic-progress-policy (sha256 099fac00fe2e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Appeal Process Students who fail to meet SAP requirements at the end of the warning semester may submit a SAP appeal through Workday to the Office of Financial Aid if extenuating circumstances (such as the death of a close relative, an injury or sickness of student, or other extenuating circumstance) existed which negatively impacted the student’s ability to make SAP.”
  - sentence: sap_appeal ⟵ “Both the SAP appeal form and a copy of the Academic Plan must be submitted through Workday within thirty days of the SAP denial notification in order for the appeal to be considered.”
  - sentence: sap_appeal ⟵ “In evaluating a SAP appeal, the Office of Financial Aid considers both the extenuating circumstances that led to the failure to make SAP and whether the student will be able to meet SAP standards by (i) the end of the following academic term or (ii) a specific later date by adhering to an academic plan.”
### `543b76367e9d20a8` Saint Anselm College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.anselm.edu/admission/tuition-aid/new-students (sha256 bbf2f5e92eb1)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.anselm.edu/admission/tuition-aid/financial-aid-faq
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Unless you qualify as an independent student by federal standards, or you have highly unusual circumstances, you must file with your parents.”
### `da62ca940153484e` Saint Anselm College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.anselm.edu/admission/tuition-aid/financial-aid-faq (sha256 18e655565b81)
- issues: semantic_review_required, conflicting_sources:https://www.anselm.edu/admission/tuition-aid/new-students
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “What should I do if I have special circumstances not indicated in the FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances could be loss of employment, unusually high medical expenses, or reduced income.”
  - sentence: need_based_special_circumstances ⟵ “You may not file as an independent student unless you have highly unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances could be loss of employment, unusually high medical expenses, or reduced income.”
### `0edf8c30be1120c9` Southern New Hampshire University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.snhu.edu/tuition-and-financial-aid/paying-for-college/financial-aid-101 (sha256 3b920b746f92)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Glossary Terms Appeal An appeal is a formal request to have a financial aid administrator review your aid eligibility and possibly use Professional Judgment to adjust the figures.”
  - sentence: professional_judgment ⟵ “Professional Judgment refers to the authority of a school's financial aid administrator to make those adjustments.”
### `35ae431bbd1afcbc` Southern New Hampshire University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.snhu.edu/tuition-and-financial-aid/paying-for-college/financial-aid-101 (sha256 3b920b746f92)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “SAP Appeal Process Students who have been placed on financial aid suspension will be allowed to appeal their suspension.”
  - sentence: sap_appeal ⟵ “To be considered, SAP appeals must include the following elements: Reason(s) why the student failed to maintain SAP.”
  - sentence: sap_appeal ⟵ “SAP Appeal Approval and Academic Plan Students with an approved appeal who are placed on SAP probation will have their status reviewed after each payment period or applicable term following their successful appeal.”
  - sentence: sap_appeal ⟵ “Campus students who are SAP suspended may appeal this decision.”
  - sentence: sap_appeal ⟵ “Online students who are SAP suspended may appeal this decision after 2 terms (graduate) or 1 payment period (undergraduate).”
  - sentence: sap_appeal ⟵ “SAP Appeal Process Students who lose their aid may appeal, provided there are mitigating circumstances that inhibited their academic progress.”
### `6ca451a2b9999353` Southern New Hampshire University — transfer_policies 2026-27 [new] (ambiguous_year_labels)
- source: https://www.snhu.edu/admission/transferring-credits (sha256 b6ecc215dc8d)
- issues: ambiguous_year_labels
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Then you'll receive it upon acceptance to SNHU! "We'll transfer in any or all credits or experiences that fall within our transfer guidelines," said Brielle Amazeen, a transfer credit specialist at SNHU. "We compare course descriptions from other schools to SNHU courses to determine if they are equivalent to one of our courses or if they should transfer in as an elective." Courses with a grade of ”
### `0c8666eba9ab5fb7` Thomas More College of Liberal Arts — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://thomasmorecollege.edu/wp-content/uploads/COA-2026-2027.pdf (sha256 31978e99140b)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://thomasmorecollege.edu/apply/finances/
- checks: {"columns": 10, "rows": 26}
  - column:Tuition: 15500 ⟵ “Tuition | 15,500 | 15,500 | 31,000 | 15,500 | 15,500 | 31,000”
  - column:Food & Housing (On campus): 5970 ⟵ “Food & Housing (On campus) | 5,970 | 5,970 | 11,940 | 5,970 | 6,490 | 12,460”
  - column:Fees: 200 ⟵ “Fees | 200 | 200 | 400 | 200 | 700 | 900”
  - column:Books: 300 ⟵ “Books | 300 | 300 | 600 | 300 | 300 | 600”
  - column:Transportation: 400 ⟵ “Transportation | 400 | 400 | 800 | 400 | 0 | 400”
  - column:Study Abroad Expenses: 0 ⟵ “Study Abroad Expenses | 0 | 0 | 0 | 0 | 3,000 | 3,000”
  - column:Personal/Other**: 500 ⟵ “Personal/Other** | 500 | 500 | 1,000 | 500 | 0 | 500”
  - column:$: 22870 ⟵ “$ | 22,870 | $ | 23,770 | $ | 46,640”
  - column:Tuition (2): 15500 ⟵ “Tuition | 15,500 | 15,500 | 31,000 | 15,500 | 15,500 | 31,000”
  - column:Food & Housing (On campus) (2): 0 ⟵ “Food & Housing (On campus) | 0 | 0 | 0 | 0 | 6,490 | 6,490”
  - column:Meal Plan (Off campus/At home): 1085 ⟵ “Meal Plan (Off campus/At home) | 1,085 | 1,085 | 2,170 | 1,085 | 0 | 1,085”
  - column:Fees (2): 200 ⟵ “Fees | 200 | 200 | 400 | 200 | 700 | 900”
  - column:Living/Personal Expenses (Off campus)**: 7000 ⟵ “Living/Personal Expenses (Off campus)** | 7,000 | 7,000 | 14,000 | 7,000 | 0 | 7,000”
  - column:Books (2): 300 ⟵ “Books | 300 | 300 | 600 | 300 | 300 | 600”
  - column:Transportation (2): 600 ⟵ “Transportation | 600 | 600 | 1,200 | 600 | 0 | $ | 600”
  - column:Study Abroad Expenses (2): 0 ⟵ “Study Abroad Expenses | 0 | 0 | 0 | 0 | 3,000 | $ | 3,000”
  - column:$ (2): 24685 ⟵ “$ | 24,685 | $ | 25,585 | $ | 50,270”
  - column:Tuition (3): 15500 ⟵ “Tuition | 15,500 | 15,500 | 31,000 | 15,500 | 15,500 | 31,000”
  - column:Food & Housing (On campus) (3): 0 ⟵ “Food & Housing (On campus) | 0 | 0 | 0 | 0 | 6,490 | 6,490”
  - column:Meal Plan (Off campus/At home) (2): 1085 ⟵ “Meal Plan (Off campus/At home) | 1,085 | 1,085 | 2,170 | 1,085 | 0 | 1,085”
  - column:Fees (3): 200 ⟵ “Fees | 200 | 200 | 400 | 200 | 700 | 900”
  - column:Living/Personal Expenses (At home)**: 2250 ⟵ “Living/Personal Expenses (At home)** | 2,250 | 2,250 | 4,500 | 2,250 | 0 | 2,250”
  - column:Books (3): 300 ⟵ “Books | 300 | 300 | 600 | 300 | 300 | 600”
  - column:Transportation (3): 600 ⟵ “Transportation | 600 | 600 | 1,200 | 600 | 0 | 600”
  - column:Study Abroad Expenses (3): 0 ⟵ “Study Abroad Expenses | 0 | 0 | 0 | 0 | 3,000 | 3,000”
  - … 177 more rows
### `e5bc5f2d147eb1d1` Thomas More College of Liberal Arts — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://thomasmorecollege.edu/wp-content/uploads/COA-2025-2026-.pdf (sha256 0982ec2c34f9)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 10, "rows": 26}
  - column:Tuition: 15000 ⟵ “Tuition | 15,000 | 15,000 | 30,000 | 15,000 | 15,000 | 30,000”
  - column:Food & Housing (On campus): 5720 ⟵ “Food & Housing (On campus) | 5,720 | 5,720 | 11,440 | 5,720 | 6,240 | 11,960”
  - column:Fees: 200 ⟵ “Fees | 200 | 200 | 400 | 200 | 700 | 900”
  - column:Books: 300 ⟵ “Books | 300 | 300 | 600 | 300 | 300 | 600”
  - column:Transportation: 400 ⟵ “Transportation | 400 | 400 | 800 | 400 | 0 | 400”
  - column:Study Abroad Expenses: 0 ⟵ “Study Abroad Expenses | 0 | 0 | 0 | 0 | 3,000 | 3,000”
  - column:Personal/Other**: 500 ⟵ “Personal/Other** | 500 | 500 | 1,000 | 500 | 0 | 500”
  - column:$: 22120 ⟵ “$ | 22,120 | $ | 23,020 | $ | 45,140”
  - column:Tuition (2): 15000 ⟵ “Tuition | 15,000 | 15,000 | 30,000 | 15,000 | 15,000 | 30,000”
  - column:Food & Housing (On campus) (2): 0 ⟵ “Food & Housing (On campus) | 0 | 0 | 0 | 0 | 6,240 | 6,240”
  - column:Meal Plan (Off campus/At home): 1040 ⟵ “Meal Plan (Off campus/At home) | 1,040 | 1,040 | 2,080 | 1,040 | 0 | 1,040”
  - column:Fees (2): 200 ⟵ “Fees | 200 | 200 | 400 | 200 | 700 | 900”
  - column:Living/Personal Expenses (Off campus)**: 7000 ⟵ “Living/Personal Expenses (Off campus)** | 7,000 | 7,000 | 14,000 | 7,000 | 0 | 7,000”
  - column:Books (2): 300 ⟵ “Books | 300 | 300 | 600 | 300 | 300 | 600”
  - column:Transportation (2): 600 ⟵ “Transportation | 600 | 600 | 1,200 | 600 | 0 | $ | 600”
  - column:Study Abroad Expenses (2): 0 ⟵ “Study Abroad Expenses | 0 | 0 | 0 | 0 | 3,000 | $ | 3,000”
  - column:$ (2): 24140 ⟵ “$ | 24,140 | $ | 25,040 | $ | 49,180”
  - column:Tuition (3): 15000 ⟵ “Tuition | 15,000 | 15,000 | 30,000 | 15,000 | 15,000 | 30,000”
  - column:Food & Housing (On campus) (3): 0 ⟵ “Food & Housing (On campus) | 0 | 0 | 0 | 0 | 6,240 | 6,240”
  - column:Meal Plan (Off campus/At home) (2): 1040 ⟵ “Meal Plan (Off campus/At home) | 1,040 | 1,040 | 2,080 | 1,040 | 0 | 1,040”
  - column:Fees (3): 200 ⟵ “Fees | 200 | 200 | 400 | 200 | 700 | 900”
  - column:Living/Personal Expenses (At home)**: 2250 ⟵ “Living/Personal Expenses (At home)** | 2,250 | 2,250 | 4,500 | 2,250 | 0 | 2,250”
  - column:Books (3): 300 ⟵ “Books | 300 | 300 | 600 | 300 | 300 | 600”
  - column:Transportation (3): 600 ⟵ “Transportation | 600 | 600 | 1,200 | 600 | 0 | 600”
  - column:Study Abroad Expenses (3): 0 ⟵ “Study Abroad Expenses | 0 | 0 | 0 | 0 | 3,000 | 3,000”
  - … 176 more rows
### `e85f23ff52844769` Thomas More College of Liberal Arts — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://thomasmorecollege.edu/apply/finances/ (sha256 3dff32d04fa2)
- issues: ambiguous_year_labels, arrangement_unlabeled, conflicting_sources:https://thomasmorecollege.edu/wp-content/uploads/COA-2026-2027.pdf
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - with_parents_or_family:Tuition:: 31000 ⟵ “Tuition: | $31,000 | Tuition: | $31,000”
  - with_parents_or_family:Food/Housing:: 11940 ⟵ “Food/Housing: | $11,940* | Food (meal plan): | $2,170”
  - with_parents_or_family:Fees:: 400 ⟵ “Fees: | $400* | Fees: | $400*”
  - with_parents_or_family:Total:: 43340 ⟵ “Total: | $43,340 | Total: | $33,570”
  - column:Tuition:: 31000 ⟵ “Tuition: | $31,000 | Tuition: | $31,000”
  - column:Food/Housing:: 2170 ⟵ “Food/Housing: | $11,940* | Food (meal plan): | $2,170”
  - column:Fees:: 400 ⟵ “Fees: | $400* | Fees: | $400*”
  - column:Total:: 33570 ⟵ “Total: | $43,340 | Total: | $33,570”
### `1185a185b352b3c4` University of New Hampshire College of Professional Studies Online — appeals 2026-27 [new] (source_unlabeled)
- source: https://cps.unh.edu/online/tuition-aid/types-aid/satisfactory-academic-progress-sap (sha256 b2b57c5d02b0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Components of the Financial Aid Satisfactory Academic Progress Appeal If an extenuating circumstance exists that can be supported with documentation, then the student may complete the aid-year specific Financial Aid Satisfactory Academic Progress Appeal Form.”
  - sentence: sap_appeal ⟵ “Official deadlines will be published annually on the aid-year specific Financial Aid Satisfactory Academic Progress Appeal Form.”
  - sentence: sap_appeal ⟵ “Appeal Review All SAP appeals will be reviewed by the SAP Appeal Committee, which is made up of representatives from the Office of Financial Aid and the Registrar’s Office.”
  - sentence: sap_appeal ⟵ “If a student who submitted a SAP Appeal form does not meet SAP standards at the end of the probation period, he/she will be required to follow their academic plan.”
### `87535f86036d50d2` University of New Hampshire College of Professional Studies Online — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://cps.unh.edu/online/tuition-aid/fafsa (sha256 537411d9229a)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances We recognize that a student’s and/or family’s true circumstances may not be accurately portrayed in their FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Approved special circumstances allow the Office of Financial Aid to adjust a FAFSA accordingly which may increase financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Visit Financial Aid Forms to submit a Special Circumstance Request. quick links Academics Apply & Register Tuition & Aid Why UNH CPS Online More to Explore Student Success Blog Resources Take a Course View Course Schedule Copyright © 2026, University of New Hampshire.”
### `fb0b6ee93b111db3` University of New Hampshire at Manchester — appeals 2024-25 [new] (labeled_in_source)
- source: https://manchester.unh.edu/admissions/financial-aid/apply-aid (sha256 307890d24fc7)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Optional: Complete the Special Circumstance Form If you believe you have an unusual circumstance that is not reflected on the FAFSA, you may complete and submit the Special Circumstance Form to the UNH Manchester Financial Aid Office.”
### `359d91ba482ccb1a` University of New Hampshire-Main Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.unh.edu/financialaid/resources/conditions-award (sha256 7c87ceef35c1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Contact our office if you have special circumstances not addressed on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Or, you can download and complete a Special Circumstances Form found here for review.”
### `b24c469574626508` University of New Hampshire-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unh.edu/financialaid/resources/satisfactory-academic-progress (sha256 bcc1bfbcb099)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP Appeals A student not meeting the SAP requirements will not be eligible for financial aid and will be notified via their UNH email.”
  - sentence: sap_appeal ⟵ “Students will be permitted to submit one SAP appeal per academic year.”
### `1f9079b54ddfd812` University of New Hampshire-Main Campus — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.unh.edu/financialaid/resources/costs (sha256 0b1737913205)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 10}
  - on_campus:Tuition: 37996 ⟵ “Tuition | $16,304 | $37,996 | $28,532”
  - on_campus:Fees: 3868 ⟵ “Fees | $3,868 | $3,868 | $3,868”
  - on_campus:Housing: 9960 ⟵ “Housing | $9,960 | $9,960 | $9,960”
  - on_campus:Food: 5624 ⟵ “Food | $5,624 | $5,624 | $5,624”
  - on_campus:Direct Costs: 57448 ⟵ “Direct Costs | $35,756 | $57,448 | $47,984”
  - on_campus:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 | $1,000 | $1,000”
  - on_campus:Transportation: 550 ⟵ “Transportation | $300 | $550 | $450”
  - on_campus:Miscellaneous: 3796 ⟵ “Miscellaneous | $3,796 | $3,796 | $3,796”
  - on_campus:Loan Fee: 68 ⟵ “Loan Fee | $68 | $68 | $68”
  - on_campus:Cost of Attendance: 62862 ⟵ “Cost of Attendance | $40,920 | $62,862 | $53,298”
### `80e11744e869810e` University of New Hampshire-Main Campus — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.unh.edu/financialaid/resources/costs (sha256 0b1737913205)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 10}
  - on_campus:Tuition: 16304 ⟵ “Tuition | $16,304 | $37,996 | $28,532”
  - on_campus:Fees: 3868 ⟵ “Fees | $3,868 | $3,868 | $3,868”
  - on_campus:Housing: 9960 ⟵ “Housing | $9,960 | $9,960 | $9,960”
  - on_campus:Food: 5624 ⟵ “Food | $5,624 | $5,624 | $5,624”
  - on_campus:Direct Costs: 35756 ⟵ “Direct Costs | $35,756 | $57,448 | $47,984”
  - on_campus:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 | $1,000 | $1,000”
  - on_campus:Transportation: 300 ⟵ “Transportation | $300 | $550 | $450”
  - on_campus:Miscellaneous: 3796 ⟵ “Miscellaneous | $3,796 | $3,796 | $3,796”
  - on_campus:Loan Fee: 68 ⟵ “Loan Fee | $68 | $68 | $68”
  - on_campus:Cost of Attendance: 40920 ⟵ “Cost of Attendance | $40,920 | $62,862 | $53,298”
### `b11c112a009e9cd0` University of New Hampshire-Main Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.unh.edu/financialaid/resources/costs (sha256 0b1737913205)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 10}
  - column:Tuition: 28532 ⟵ “Tuition | $16,304 | $37,996 | $28,532”
  - column:Fees: 3868 ⟵ “Fees | $3,868 | $3,868 | $3,868”
  - column:Housing: 9960 ⟵ “Housing | $9,960 | $9,960 | $9,960”
  - column:Food: 5624 ⟵ “Food | $5,624 | $5,624 | $5,624”
  - column:Direct Costs: 47984 ⟵ “Direct Costs | $35,756 | $57,448 | $47,984”
  - column:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 | $1,000 | $1,000”
  - column:Transportation: 450 ⟵ “Transportation | $300 | $550 | $450”
  - column:Miscellaneous: 3796 ⟵ “Miscellaneous | $3,796 | $3,796 | $3,796”
  - column:Loan Fee: 68 ⟵ “Loan Fee | $68 | $68 | $68”
  - column:Cost of Attendance: 53298 ⟵ “Cost of Attendance | $40,920 | $62,862 | $53,298”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 6; pages by category: merit_scholarships 1

## Blocked by the site (every request refused; needs the browser fallback)

- Magdalen College (`ipeds-182917`)
- St Joseph School of Nursing (`ipeds-183248`)

## Leads: official pages found with no extracted record

- Colby-Sawyer College: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Dartmouth College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit
- Franklin Pierce University: admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements
- Great Bay Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Keene State College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Lakes Region Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, residency, degree_requirements, aid_appeals
- Manchester Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- NHTI-Concord's Community College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- Nashua Community College: tuition_fees, cost_of_attendance, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, residency
- New England College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ib_credit, transfer_credit, residency, degree_requirements
- Plymouth State University: cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, residency, degree_requirements
- River Valley Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements, aid_appeals
- Rivier University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- Saint Anselm College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, residency
- Southern New Hampshire University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- Thomas More College of Liberal Arts: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- University of New Hampshire College of Professional Studies Online: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- University of New Hampshire at Manchester: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, statewide_articulation, residency, degree_requirements
- University of New Hampshire-Main Campus: admissions_tests, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- White Mountains Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, residency, degree_requirements, aid_appeals
