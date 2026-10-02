# Review queue — TN (2026-27)

Pages fetched: 2034; failures: 178. Candidates: 265 (9 without issues, 256 exceptions). Re-verification upgrades proposed: 19.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 1 | 1 | 1 | 23 | 25 | 1 | 7 |
| cost_of_attendance | 1 | 1 | 1 | 23 | 25 | 1 | 7 |
| admissions_tests | 1 | 0 | 0 | 1 | 50 | 0 | 7 |
| common_data_set | 1 | 0 | 0 | 1 | 6 | 44 | 7 |
| merit_scholarships | 1 | 0 | 0 | 0 | 49 | 2 | 7 |
| ap_credit | 1 | 1 | 3 | 1 | 12 | 34 | 7 |
| clep_credit | 1 | 1 | 1 | 2 | 5 | 42 | 7 |
| ib_credit | 1 | 0 | 1 | 1 | 3 | 46 | 7 |
| dual_enrollment | 1 | 0 | 0 | 0 | 36 | 15 | 7 |
| transfer_credit | 0 | 2 | 0 | 0 | 45 | 5 | 7 |
| statewide_articulation | 0 | 2 | 0 | 0 | 18 | 32 | 7 |
| residency | 0 | 2 | 0 | 0 | 20 | 30 | 7 |
| degree_requirements | 1 | 1 | 0 | 0 | 45 | 5 | 7 |
| aid_appeals | 1 | 1 | 0 | 0 | 36 | 14 | 7 |

## Ready for review (9)

### `0fd9a93f60222c60` Jackson State Community College — credit_policies 2026-27 [new] (source_unlabeled)
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
### `bcf8154da1a1d5cb` Jackson State Community College — credit_policies 2026-27 [new] (source_unlabeled)
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
### `b15934c508f94b72` Lincoln Memorial University — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://cvmcatalog.lmunet.edu/dvm-admissions-policies (sha256 6238ef1e301d)
- checks: {"distinct_exams": 2, "equivalencies": 3, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|Biology]:  ⟵ “Biology | 8 | 12 | General biology series; lecture & lab.”
  - equivalencies[AP-CHEMISTRY|Organic Chemistry]:  ⟵ “Organic Chemistry | 3 | 5 | Lecture & Lab”
  - equivalencies[AP-CHEMISTRY|General Chemistry]:  ⟵ “General Chemistry | 6 | 9 | Lecture & Lab”
### `e91522fb6c3f2cdd` Lipscomb University — credit_policies 2026-27 [new] (source_unlabeled)
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
### `2270d7083ae06bce` The University of Tennessee-Chattanooga — credit_policies 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/ap-exam (sha256 be309e3b1af6)
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
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/clep (sha256 683c5d105873)
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
### `ea6639e0ddc93928` The University of Tennessee-Chattanooga — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/ib-exam (sha256 7f478fa1ecfe)
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
### `a12145c8c6f928a6` University of Memphis — costs 2026-27 [new] (labeled_in_source)
- source: https://www.memphis.edu/law/admissions/tuition-and-costs.php (sha256 33c0a92f4d02)
- checks: {"columns": 1, "components": ["books_supplies", "food_housing", "personal", "total", "transportation", "tuition_and_fees"], "components_reconcile": true}
  - column:tuition_and_fees: 28642 ⟵ “Tuition & Fees* | $22,658 | $28,642”
  - column:food_housing: 14568 ⟵ “Room & Board | $14,568 | $14,568”
  - column:books_supplies: 1995 ⟵ “Books/Supplies | $1,995 | $1,995”
  - column:transportation: 3770 ⟵ “Transportation | $3,770 | $3,770”
  - column:personal: 4514 ⟵ “Misc./Personal | $4,514 | $4,514”
  - column:total: 53489 ⟵ “Total | $47,505 | $53,489”
### `acc19b10653b9a67` University of Memphis — costs 2026-27 [new] (labeled_in_source)
- source: https://www.memphis.edu/law/admissions/tuition-and-costs.php (sha256 33c0a92f4d02)
- checks: {"columns": 1, "components": ["books_supplies", "food_housing", "personal", "total", "transportation", "tuition_and_fees"], "components_reconcile": true}
  - column:tuition_and_fees: 22658 ⟵ “Tuition & Fees* | $22,658 | $28,642”
  - column:food_housing: 14568 ⟵ “Room & Board | $14,568 | $14,568”
  - column:books_supplies: 1995 ⟵ “Books/Supplies | $1,995 | $1,995”
  - column:transportation: 3770 ⟵ “Transportation | $3,770 | $3,770”
  - column:personal: 4514 ⟵ “Misc./Personal | $4,514 | $4,514”
  - column:total: 47505 ⟵ “Total | $47,505 | $53,489”

## Exceptions (256)

### `error-pipeline.extractors.costs-0d9fd197fce3567635f3.json.gz` Austin Peay State University — None  [?] ()
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/transfer-scholarship-opportunities.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-2bf535ffbbedeea9fc45.json.gz` Austin Peay State University — None  [?] ()
- source: https://www.apsu.edu/financialaid/cost-of-attendance/coa.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-1779bd51fb77e35b3510.json.gz` Baptist Health Sciences University — None  [?] ()
- source: https://www.baptistu.edu/tuition-financial-aid
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-379ad26493c9bd544080.json.gz` Belmont University — None  [?] ()
- source: https://www.belmont.edu/admissions/first-year/apply.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-56a9e3d1a3649270a010.json.gz` Belmont University — None  [?] ()
- source: https://www.belmont.edu/admissions/transfer/apply.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-685e10103cd83f606d17.json.gz` Belmont University — None  [?] ()
- source: https://www.belmont.edu/admissions/non-degree.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-b3bb6601569c8c019350.json.gz` Belmont University — None  [?] ()
- source: https://www.belmont.edu/admissions/graduate-professional/tuition-aid.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-00af70346bbbe53d9c2b.json.gz` Bryan College-Dayton — None  [?] ()
- source: https://www.bryan.edu/admissions/financial-aid/loans/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-0bd98cdc668b2a317254.json.gz` Bryan College-Dayton — None  [?] ()
- source: https://www.bryan.edu/admissions/financial-aid/federal-state-aid/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `f9bca7ab0896d19d` Bryan College-Dayton — costs 2026-27 [new] (labeled_in_source)
- source: https://www.bryan.edu/admissions/tuition-fees/ (sha256 b49675eb727d)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "components": ["food", "housing", "total", "tuition"], "components_reconcile": true}
  - column:tuition: 10850 ⟵ “Tuition (12-17 hours) | $10,850 | $21,700”
  - column:food: 1950 ⟵ “Board | $1,950 | $3,900”
  - column:housing: 2825 ⟵ “Room (traditional dorms) | $2,825 | $5,650”
  - column:total: 15625 ⟵ “Total traditional (tuition, room & board) | $15,625 | $31,250”
  - column:tuition: 21700 ⟵ “Tuition (12-17 hours) | $10,850 | $21,700”
  - column:food: 3900 ⟵ “Board | $1,950 | $3,900”
  - column:housing: 5650 ⟵ “Room (traditional dorms) | $2,825 | $5,650”
  - column:total: 31250 ⟵ “Total traditional (tuition, room & board) | $15,625 | $31,250”
### `error-pipeline.extractors.costs-6ed84ccd01d1779066a2.json.gz` Carson-Newman University — None  [?] ()
- source: https://www.cn.edu/admissions-and-aid/financial-aid/tuition-costs/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-e5af19a24945515d8b9a.json.gz` Carson-Newman University — None  [?] ()
- source: https://admissions.cn.edu/register/requestinfo
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-fe55d218dbe01bf30ed4.json.gz` Carson-Newman University — None  [?] ()
- source: https://www.cn.edu/admissions-and-aid/dual-enrollment/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `6a36358930c20152` Carson-Newman University — costs 2026-27 [new] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/ (sha256 44c136e71d64)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "components": ["food", "housing", "total", "tuition"], "components_reconcile": true}
  - column:tuition: 21250 ⟵ “Tuition | $21,250 | $42,500”
  - column:food: 3150 ⟵ “Meal Plan* | 3,150 | 6,300”
  - column:housing: 3150 ⟵ “Room** | 3,150 | 6,300”
  - column:total: 27550 ⟵ “Total | $27,550 | $55,300”
  - column:tuition: 42500 ⟵ “Tuition | $21,250 | $42,500”
  - column:food: 6300 ⟵ “Meal Plan* | 3,150 | 6,300”
  - column:housing: 6300 ⟵ “Room** | 3,150 | 6,300”
  - column:total: 55300 ⟵ “Total | $27,550 | $55,300”
### `error-pipeline.extractors.costs-02ae851c68a85e98be83.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/financial-aid-forms/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-0b7c2f61d1e029bf8a5c.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-17c8a8f0d826d69d3935.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/application-resources/application-checklist/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-23b88d63d75d9f0e1556.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/save-your-spot/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-282902f603f6ea80092a.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/tuition-fees/business-office/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-30c00316ddde9934b0e9.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/application-resources/homeschool/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-4dd41eec5940e5572fd1.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-53c7154a3d9c95f3a551.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/meet-your-counselor/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-571801ac63cca95c0f0a.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/student-life/student-activities/welcome/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-5cf3e742fe8b5b842462.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/tuition-fees/international-students-and-us-taxes/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-6b2ffb570a4c7f81dc0d.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/leadership-scholarship
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-7021adddbade8af93629.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-709c44c5dc9d2cb808b1.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/applying-for-financial-aid/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-71bd9e77bc3d07f5f6fe.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/course-program-of-study-cpos/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-71fac1a61f29f044acc0.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-722a715f8930c284b709.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/viewbook/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-8466b27d8c4d00c23ef7.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/graduate-admissions/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-84d2a838d4caca155f40.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/tuition-fees/business-office/tuition-payment/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-8cb304d47cb67bef7412.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/student-rights-and-responsibilities/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-8ebd6b757f194e18e531.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/day-foundation-la-salle-scholars-program/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-900424c6317efcde5c3c.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/eligibility-for-financial-aid/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-93f2a8153b9933680ba1.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/tuition-fees/tuition-fees-2025-2026/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-b0f596334ee0a7f164df.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/information-for/community/summer-at-cbu/summer-courses/summer-registration-tuition-aid/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-b1ab07e7d824e2de4417.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/tuition-fees/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-b317b9955c83ae8a11f3.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/partner-tuition-discount/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-b5cf0477695dc514debd.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/pascal-fellowship
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-bd2c8d1c024f7734fcc8.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/net-price-calculator/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-c0fa6293e58f06a4f1bd.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/transfer-scholarships/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-c605db077ad597ef8f0d.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-ca43ea74c2fc7440a4e9.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/application-resources/international/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-e24df5794f66415ad7fd.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/tuition-fees/tuition-insurance/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-e76378e3649514a5982a.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/student-life/student-activities/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-e76df48065ff263b2148.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/application-resources/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-e7e5eb58ed085880db5b.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/application-resources/transfer/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-eec18b8edf607a77cc1b.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/gadomski-triangle-scholarship/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-f176d4b777a61f75575f.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/tuition-fees/2024-2025-tuition-fees/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-f8b556c2f1e6a6f39fa3.json.gz` Christian Brothers University — None  [?] ()
- source: https://www.cbu.edu/admissions-aid/financial-aid/financial-aid-resources/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-6a277dd27d00f96c00ae.json.gz` Columbia State Community College — None  [?] ()
- source: https://www.columbiastate.edu/contact-us/index.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-d119b48f34ed8dc80d05.json.gz` Columbia State Community College — None  [?] ()
- source: https://www.columbiastate.edu/catalog-student-handbook/index.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-4b72506c435760764014.json.gz` Dyersburg State Community College — None  [?] ()
- source: https://catalog.dscc.edu
- issues: extractor_error:ValueError: max() iterable argument is empty
### `9be9c9a8e09ddea1` Dyersburg State Community College — costs 2025-26 [new] (labeled_in_source)
- source: https://www.dscc.edu/wp-content/uploads/2026/07/DSCC-COA-26-27.pdf (sha256 aa97e088a8b6)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "components": ["books_supplies", "food_housing", "personal", "total", "transportation", "tuition_and_fees"], "components_reconcile": true}
  - column:tuition_and_fees: 2542 ⟵ “Tuition & Fees                                               $2,542.00        $4,282.00          $5,084.00           $8,564.00”
  - column:books_supplies: 785 ⟵ “Books, Course Materials, Supplies, and Equipment              $785.00          $785.00           $1,570.00           $1,570.00”
  - column:food_housing: 5425 ⟵ “Living Expenses (Food and Housing)                           $5,425.00        $5,425.00         $10,850.00          $10,850.00”
  - column:personal: 1340 ⟵ “Personal/Miscellaneous Expenses                              $1,340.00        $1,340.00          $2,680.00           $2,680.00”
  - column:transportation: 1035 ⟵ “Transportation                                               $1,035.00        $1,035.00          $2,070.00           $2,070.00”
  - column:total: 11127 ⟵ “Total                                                         $11,127          $12,867            $22,254             $25,734”
  - column:tuition_and_fees: 1951 ⟵ “Tuition & Fees                                       $1,951.00          $3,256.00            $3,902.00           $6,512.00”
  - column:books_supplies: 588 ⟵ “Books, Course Materials, Supplies, and Equipment      $588.00            $588.00             $1,177.00           $1,177.00”
  - column:food_housing: 5425 ⟵ “Living Expenses (Food and Housing)                   $5,425.00          $5,425.00           $10,850.00          $10,850.00”
  - column:personal: 1340 ⟵ “Personal/Miscellaneous Expenses                      $1,340.00          $1,340.00            $2,680.00           $2,680.00”
  - column:transportation: 1035 ⟵ “Transportation                                       $1,035.00          $1,035.00            $2,070.00           $2,070.00”
  - column:total: 10339 ⟵ “Total                                                 $10,339            $11,644              $20,679             $23,289”
  - column:tuition_and_fees: 1360 ⟵ “Tuition & Fees                         $1,360.00          $2,230.00           $2,720.00           $4,460.00”
  - column:food_housing: 5425 ⟵ “Living Expenses (Food and Housing)     $5,425.00          $5,425.00          $10,850.00          $10,850.00”
  - column:personal: 1340 ⟵ “Personal/Miscellaneous Expenses        $1,340.00          $1,340.00           $2,680.00           $2,680.00”
  - column:transportation: 1035 ⟵ “Transportation                         $1,035.00          $1,035.00           $2,070.00           $2,070.00”
  - column:total: 9552 ⟵ “Total                                   $9,552             $10,422             $19,105             $20,845”
  - column:tuition_and_fees: 691.5 ⟵ “Tuition & Fees                                  $691.50           $1,111.50           $1,383.00           $2,223.00”
  - column:food_housing: 0 ⟵ “Living Expenses (Food and Housing)                $0.00             $0.00               $0.00               $0.00”
  - column:personal: 0 ⟵ “Personal/Miscellaneous Expenses                   $0.00             $0.00               $0.00               $0.00”
  - column:transportation: 1035 ⟵ “Transportation                                  $1,035.00         $1,035.00           $2,070.00           $2,070.00”
  - column:total: 1922.5 ⟵ “Total                                           $1,922.50         $2,342.50           $3,845.00           $4,685.00”
  - column:tuition_and_fees: 2542 ⟵ “Tuition & Fees                                                                $2,542.00            $4,282.00”
  - column:food_housing: 3255 ⟵ “Living Expenses (Food and Housing)                                            $3,255.00            $3,255.00”
  - column:personal: 804 ⟵ “Personal/Miscellaneous Expenses                                                $804.00              $804.00”
  - … 91 more rows
### `error-pipeline.extractors.costs-0d57982a71044edd2faf.json.gz` East Tennessee State University — None  [?] ()
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/hope/appeals.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-1c8b6a0cbbbaf1ebd62f.json.gz` East Tennessee State University — None  [?] ()
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-336707b1138589b402d9.json.gz` East Tennessee State University — None  [?] ()
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/transfer.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-4cb91f9b9fb1a01b677a.json.gz` East Tennessee State University — None  [?] ()
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-840a7a0530cc9e665e66.json.gz` East Tennessee State University — None  [?] ()
- source: https://www.etsu.edu/universitygovernance/governancecommittees/res_appeal.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-d6cd59862403f97f8664.json.gz` East Tennessee State University — None  [?] ()
- source: https://www.etsu.edu/financial-aid-and-scholarships/policies/satisfactorypro.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-22e6b4c15f6937234382.json.gz` Fisk University — None  [?] ()
- source: https://www.fisk.edu/contact/general-campus-directory/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-030cbe33bcd3d72312ed.json.gz` Herzing University-Nashville — None  [?] ()
- source: https://www.herzing.edu/nursing/practical-nursing-lpn-prep-program
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-0edc1e0f18de2145d4ba.json.gz` Herzing University-Nashville — None  [?] ()
- source: http://catalog.herzing.edu/index.php?catoid=14
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-1ffeaedba4211094fbd4.json.gz` Herzing University-Nashville — None  [?] ()
- source: https://www.herzing.edu/nursing/msn-family-nurse-practitioner-program
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-2d2349eba5c0128e2b91.json.gz` Herzing University-Nashville — None  [?] ()
- source: http://catalog.herzing.edu/index.php?catoid=13
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-7bec6c347a7e40cd319b.json.gz` Herzing University-Nashville — None  [?] ()
- source: http://catalog.herzing.edu/index.php?catoid=11
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-85b511c417256396324c.json.gz` Herzing University-Nashville — None  [?] ()
- source: https://www.herzing.edu/military/tuition-education-benefits
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-957c0ec29a0b483f0d92.json.gz` Herzing University-Nashville — None  [?] ()
- source: http://catalog.herzing.edu/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-b64a4fb78d8bb61ef053.json.gz` Herzing University-Nashville — None  [?] ()
- source: http://catalog.herzing.edu/index.php?catoid=15
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-ce2cf573403a219cf8a2.json.gz` Herzing University-Nashville — None  [?] ()
- source: http://catalog.herzing.edu/index.php?catoid=16
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-f8e39e477f99a7a0fe26.json.gz` Herzing University-Nashville — None  [?] ()
- source: http://catalog.herzing.edu/index.php?catoid=21
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-fdcd6ca7485c9fb6de16.json.gz` Herzing University-Nashville — None  [?] ()
- source: http://catalog.herzing.edu/index.php?catoid=12
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-08de0c13a6ef1fdeb08f.json.gz` Jackson State Community College — None  [?] ()
- source: https://jscc.edu/academics/academic-services/course-catalog/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-6994832800fbd93e208e.json.gz` Jackson State Community College — None  [?] ()
- source: https://jscc.edu/costs-and-aid/satisfactory-academic-progress-sap/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-69ace405655ca7123e39.json.gz` Jackson State Community College — None  [?] ()
- source: https://jscc.edu/admissions/prior-learning/industry-workplace-credit/industry-workplace-credit
- issues: extractor_error:ValueError: max() iterable argument is empty
### `081b6d403b386d33` Jackson State Community College — costs 2026-27 [new] (ambiguous_year_labels)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: ambiguous_year_labels, arrangement_unlabeled, residency_unknown
- checks: {"columns": 3, "components": ["books_supplies", "food_housing", "personal", "total", "transportation", "tuition_and_fees"], "components_reconcile": true}
  - column:tuition_and_fees: 2535 ⟵ “TUITION & FEES* | $2,535 | $2,535 | $2,535”
  - column:books_supplies: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - column:food_housing: 3841 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - column:personal: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - column:transportation: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - column:total: 10659 ⟵ “TOTAL (PER SEMESTER) | $10,659 | $14,656 | $9,326”
  - column:total: 21318 ⟵ “TOTAL: (FOR FALL AND SPRING) | $21,318 | $29,312 | $18,652”
  - column:tuition_and_fees: 4275 ⟵ “TUITION & FEES* | $4,275 | $4,275 | $4,275”
  - column:books_supplies: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - column:food_housing: 3841 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - column:personal: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - column:transportation: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - column:total: 12398 ⟵ “TOTAL (PER SEMESTER) | $12,398 | $16,396 | $11,066”
  - column:total: 24796 ⟵ “TOTAL: (FOR FALL AND SPRING) | $24,796 | $32,791 | $22,131”
  - column:tuition_and_fees: 2535 ⟵ “TUITION & FEES* | $2,535 | $2,535 | $2,535”
  - column:books_supplies: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - column:food_housing: 7838 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - column:personal: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - column:transportation: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - column:total: 14656 ⟵ “TOTAL (PER SEMESTER) | $10,659 | $14,656 | $9,326”
  - column:total: 29312 ⟵ “TOTAL: (FOR FALL AND SPRING) | $21,318 | $29,312 | $18,652”
  - column:tuition_and_fees: 4275 ⟵ “TUITION & FEES* | $4,275 | $4,275 | $4,275”
  - column:books_supplies: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - column:food_housing: 7838 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - column:personal: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - … 17 more rows
### `0d2184c92ea1763b` Jackson State Community College — costs 2009-10 [new] (labeled_in_source)
- source: https://jscc.edu/media/jackson-state/content-assets/documents/academics-/academic-catalogs/catalog09-10.pdf (sha256 1c90ff5480f4)
- issues: stale_year_label:2009-10
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "tuition"]}
  - column:tuition: 75 ⟵ “of tuition charges or registration fees. A service fee of $75 will be charged          student’s first birthday. The following categories of students are”
  - column:mandatory_fees: 4 ⟵ “Activity Fee (non-refundable)...........................................$4.00                         up or down to the nearest whole day.”
  - column:mandatory_fees: 9 ⟵ “Technology Fee per credit hour........................................$9.00”
  - column:books_supplies: 1200 ⟵ “basis. Each scholarship pays full tuition, books (up to $1,200 yearly),”
### `38849b9875247ff3` Jackson State Community College — costs 2007-08 [new] (labeled_in_source)
- source: https://jscc.edu/media/jackson-state/content-assets/documents/academics-/academic-catalogs/catalog07-08.pdf (sha256 a241946120dc)
- issues: column_alignment_uncertain, residency_unknown, stale_year_label:2007-08
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "tuition"]}
  - column:tuition: 75 ⟵ “of tuition charges or registration fees. A service fee of $75 will be charged         first birthday. The following categories of students are exempt from”
  - column:mandatory_fees: 9 ⟵ “Technology Fee per credit hour .......................................$9.00”
  - column:books_supplies: 900 ⟵ “basis. Each scholarship pays full tuition, books (up to $900 yearly),”
### `7a07e5a1e2a6c242` Jackson State Community College — costs 2008-09 [new] (labeled_in_source)
- source: https://jscc.edu/media/jackson-state/content-assets/documents/academics-/academic-catalogs/catalog08-09.pdf (sha256 53f9e2c9b6e3)
- issues: column_alignment_uncertain, residency_unknown, stale_year_label:2008-09
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "tuition"]}
  - column:tuition: 75 ⟵ “of tuition charges or registration fees. A service fee of $75 will be charged         student’s first birthday. The following categories of students are”
  - column:mandatory_fees: 4 ⟵ “Activity Fee (non-refundable)...........................................$4.00                        When the calculation produces a fractional day, rounding will be”
  - column:mandatory_fees: 9 ⟵ “Technology Fee per credit hour........................................$9.00                        the refund.”
  - column:books_supplies: 900 ⟵ “basis. Each scholarship pays full tuition, books (up to $900 yearly),”
### `b0239ba641fb8662` Jackson State Community College — costs 2006-07 [new] (labeled_in_source)
- source: https://jscc.edu/media/jackson-state/content-assets/documents/academics-/academic-catalogs/catalog06-07.pdf (sha256 8da8f1ab681d)
- issues: column_alignment_uncertain, residency_unknown, stale_year_label:2006-07
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "tuition"]}
  - column:tuition: 75 ⟵ “of tuition charges or registration fees. A service fee of $75 will be charged         exam or 500 on non-computerized version.”
  - column:mandatory_fees: 9 ⟵ “Technology Fee per credit hour .......................................$9.00”
  - column:books_supplies: 900 ⟵ “basis. Each scholarship pays full tuition, books (up to $900 yearly),”
### `error-pipeline.extractors.costs-38e8d4c2887b61e0dbd7.json.gz` Johnson University — None  [?] ()
- source: https://johnsonu.edu/admissions/tuition/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `505fbfd601a49d9e` Johnson University — costs 2021-22 [new] (labeled_in_title)
- source: https://johnsonu.edu/wp-content/uploads/2021/06/2021-2022-Johnson-University-Academic-Catalog-approved-2021-06-23.pdf (sha256 054b9338ecb3)
- issues: stale_year_label:2021-22
- checks: {"columns": 1, "components": ["mandatory_fees", "tuition"]}
  - column:mandatory_fees: 225 ⟵ “Activity Fee                                  $225      COUN 6100 Clinical Practicum                    80”
  - column:tuition: 1800 ⟵ “Undergraduate Tuition Charges                           2-Bedroom Apartment                           $1,800”
  - column:tuition: 2000 ⟵ “tuition. If aid exceeds $2,000, the student will receive 1/3 off tuition.”
### `14b3791bccc3befe` King University — costs 2026-27 [new] (ambiguous_year_labels)
- source: https://media.king.edu/2018/10/AcademicCatalog_2015-2016_Complete.pdf (sha256 5a31f6820f47)
- issues: ambiguous_year_labels, arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components": ["books_supplies", "food", "housing", "total", "tuition"], "components_reconcile": false}
  - column:housing: 2054 ⟵ “Room                                                 *$2,054       *$4,108”
  - column:housing: 2154 ⟵ “Room Hyde Hall                                        $2,154        $4,308”
  - column:food: 2036 ⟵ “Board                                                 $2,036        $4,072”
  - column:total: 16944 ⟵ “Total                                                $16,944       $33,888”
  - column:tuition: 125 ⟵ “Tuition (per semester hour) ......................... $125”
  - column:housing: 340 ⟵ “Room ........................................................... $340”
  - column:books_supplies: 850 ⟵ “electronic testing, and course materials. The fees are $850 for traditional”
  - column:housing: 4108 ⟵ “Room                                                 *$2,054       *$4,108”
  - column:housing: 4308 ⟵ “Room Hyde Hall                                        $2,154        $4,308”
  - column:food: 4072 ⟵ “Board                                                 $2,036        $4,072”
  - column:total: 33888 ⟵ “Total                                                $16,944       $33,888”
### `170cfdec4d6bed2d` King University — costs 2018-19 [new] (labeled_in_source)
- source: https://media.king.edu/2019/05/2018-19-catalog.pdf (sha256 9729dc05d257)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2018-19
- checks: {"columns": 2, "components": ["books_supplies", "food", "housing", "mandatory_fees", "total", "tuition"], "components_reconcile": false}
  - column:housing: 2200 ⟵ “Room*                    $2,200                                  $4,400”
  - column:food: 2181 ⟵ “Board                    $2,181                                  $4,362”
  - column:total: 19238 ⟵ “Total                $19,238                                  $38,476”
  - column:tuition: 125 ⟵ “Tuition (per semester hour) .................................. $125                    $600 per semester hour for all hours up to but not”
  - column:housing: 340 ⟵ “Room ..................................................................... $340        including twelve hours. Part-time students pay a $120”
  - column:books_supplies: 300 ⟵ “A course materials fee of $300 is charged to”
  - column:mandatory_fees: 200 ⟵ “fee of $200 for the NURS 5004 Advanced Health”
  - column:housing: 4400 ⟵ “Room*                    $2,200                                  $4,400”
  - column:food: 4362 ⟵ “Board                    $2,181                                  $4,362”
  - column:total: 38476 ⟵ “Total                $19,238                                  $38,476”
  - column:tuition: 600 ⟵ “Tuition (per semester hour) .................................. $125                    $600 per semester hour for all hours up to but not”
  - column:housing: 120 ⟵ “Room ..................................................................... $340        including twelve hours. Part-time students pay a $120”
### `21d7b20078fe1e40` King University — costs 2010-11 [new] (labeled_in_source)
- source: https://media.king.edu/2018/10/AcademicCatalog2010-2011.pdf (sha256 58086cb445c5)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2010-11
- checks: {"columns": 2, "components": ["food", "housing", "mandatory_fees", "total", "tuition"], "components_reconcile": false}
  - column:housing: 1956 ⟵ “Room                                                              *$1,956                                    *$3,912”
  - column:housing: 2056 ⟵ “Room Hyde Hall                                                     $2,056                                     $4,112”
  - column:food: 1939 ⟵ “Board                                                              $1,939                                     $3,878”
  - column:total: 15349 ⟵ “Total                                                                $15,349                                    $30,698”
  - column:tuition: 125 ⟵ “Tuition (per semester hour)                                         $125”
  - column:housing: 340 ⟵ “Room                                                                $340”
  - column:mandatory_fees: 100 ⟵ “fees of a full-time student. Audit fees are not refundable.         always be a $100 deposit on the account. Upon final”
  - column:housing: 3912 ⟵ “Room                                                              *$1,956                                    *$3,912”
  - column:housing: 4112 ⟵ “Room Hyde Hall                                                     $2,056                                     $4,112”
  - column:food: 3878 ⟵ “Board                                                              $1,939                                     $3,878”
  - column:total: 30698 ⟵ “Total                                                                $15,349                                    $30,698”
### `2488666d65ca843a` King University — costs 2013-14 [new] (labeled_in_title)
- source: https://media.king.edu/2018/10/AcademicCatalog2013-2014.pdf (sha256 7584dfa6e20c)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2013-14
- checks: {"columns": 2, "components": ["food", "housing", "total", "tuition"], "components_reconcile": false}
  - column:housing: 2054 ⟵ “Room                                            *$2,054       *$4,108”
  - column:housing: 2154 ⟵ “Room Hyde Hall                                   $2,154        $4,308”
  - column:food: 2036 ⟵ “Board                                            $2,036        $4,072”
  - column:total: 16570 ⟵ “Total                                           $16,570       $33,140”
  - column:tuition: 125 ⟵ “Tuition (per semester hour) ......................... $125”
  - column:housing: 340 ⟵ “Room ........................................................... $340”
  - column:housing: 4108 ⟵ “Room                                            *$2,054       *$4,108”
  - column:housing: 4308 ⟵ “Room Hyde Hall                                   $2,154        $4,308”
  - column:food: 4072 ⟵ “Board                                            $2,036        $4,072”
  - column:total: 33140 ⟵ “Total                                           $16,570       $33,140”
### `3cb0a0807b034c9c` King University — costs 2016-17 [new] (labeled_in_title)
- source: https://media.king.edu/2018/09/2016_2017_catalog.pdf (sha256 777d67f19043)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2016-17
- checks: {"columns": 2, "components": ["books_supplies", "food", "housing", "total", "tuition"], "components_reconcile": false}
  - column:housing: 2054 ⟵ “Room                                                         $2,054*            $4,108 *”
  - column:housing: 2154 ⟵ “Room Hyde Hall                                               $2,154             $4,308”
  - column:food: 2036 ⟵ “Board                                                        $2,036             $4,072”
  - column:total: 19882 ⟵ “Total                                                       $19,882            $39,764”
  - column:tuition: 125 ⟵ “Tuition (per semester hour) ................................ $125”
  - column:housing: 340 ⟵ “Room .................................................................. $340”
  - column:books_supplies: 920 ⟵ “and course materials. The fees are $920 for traditional students and $75 for health”
  - column:housing: 4108 ⟵ “Room                                                         $2,054*            $4,108 *”
  - column:housing: 4308 ⟵ “Room Hyde Hall                                               $2,154             $4,308”
  - column:food: 4072 ⟵ “Board                                                        $2,036             $4,072”
  - column:total: 39764 ⟵ “Total                                                       $19,882            $39,764”
  - column:books_supplies: 75 ⟵ “and course materials. The fees are $920 for traditional students and $75 for health”
### `6924ee8ce9b98f49` King University — costs 2012-13 [new] (labeled_in_source)
- source: https://media.king.edu/2018/10/AcademicCatalog2012-2013.pdf (sha256 139a8263fbad)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2012-13
- checks: {"columns": 2, "components": ["food", "housing", "total", "tuition"], "components_reconcile": false}
  - column:housing: 2054 ⟵ “Room                                                              *$2,054                                    *$4,108”
  - column:housing: 2154 ⟵ “Room Hyde Hall                                                     $2,154                                     $4,308”
  - column:food: 2036 ⟵ “Board                                                              $2,036                                     $4,072”
  - column:total: 16570 ⟵ “Total                                                                $16,570                                    $33,140”
  - column:tuition: 125 ⟵ “Tuition (per semester hour)                                         $125”
  - column:housing: 340 ⟵ “Room                                                                $340”
  - column:housing: 4108 ⟵ “Room                                                              *$2,054                                    *$4,108”
  - column:housing: 4308 ⟵ “Room Hyde Hall                                                     $2,154                                     $4,308”
  - column:food: 4072 ⟵ “Board                                                              $2,036                                     $4,072”
  - column:total: 33140 ⟵ “Total                                                                $16,570                                    $33,140”
### `733a6031120aed08` King University — costs 2014-15 [new] (labeled_in_title)
- source: https://media.king.edu/2018/10/AcademicCatalog2014-2015.pdf (sha256 bf9553899fc4)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2014-15
- checks: {"columns": 2, "components": ["food", "housing", "total", "tuition"], "components_reconcile": false}
  - column:housing: 2054 ⟵ “Room                                            *$2,054       *$4,108”
  - column:housing: 2154 ⟵ “Room Hyde Hall                                   $2,154        $4,308”
  - column:food: 2036 ⟵ “Board                                            $2,036        $4,072”
  - column:total: 16944 ⟵ “Total                                           $16,944       $33,888”
  - column:tuition: 125 ⟵ “Tuition (per semester hour) ......................... $125”
  - column:housing: 340 ⟵ “Room ........................................................... $340”
  - column:housing: 4108 ⟵ “Room                                            *$2,054       *$4,108”
  - column:housing: 4308 ⟵ “Room Hyde Hall                                   $2,154        $4,308”
  - column:food: 4072 ⟵ “Board                                            $2,036        $4,072”
  - column:total: 33888 ⟵ “Total                                           $16,944       $33,888”
### `7b307240591cbcb1` King University — costs 2021-22 [new] (labeled_in_source)
- source: https://media.king.edu/2021/05/academic-catalog.pdf (sha256 bf120f2f3920)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2021-22
- checks: {"columns": 3, "components": ["food", "housing", "total", "tuition"], "components_reconcile": false}
  - column:housing: 2428 ⟵ “Room*                    $2,428                                  $4,856               Students working towards a degree will be charged”
  - column:food: 2406 ⟵ “Board                    $2,406                                  $4,812               $600 per semester hour for all hours up to but not”
  - column:total: 21233 ⟵ “Total                $21,233                                  $42,466               including 12 hours. Part-time students pay a $120”
  - column:tuition: 125 ⟵ “Tuition (per semester hour) .................................. $125”
  - column:housing: 340 ⟵ “Room ..................................................................... $340”
  - column:housing: 350 ⟵ “room occupancy and $350 per semester for                   supplies and resources. Program fees are”
  - column:housing: 4856 ⟵ “Room*                    $2,428                                  $4,856               Students working towards a degree will be charged”
  - column:food: 4812 ⟵ “Board                    $2,406                                  $4,812               $600 per semester hour for all hours up to but not”
  - column:total: 42466 ⟵ “Total                $21,233                                  $42,466               including 12 hours. Part-time students pay a $120”
  - column:food: 600 ⟵ “Board                    $2,406                                  $4,812               $600 per semester hour for all hours up to but not”
  - column:total: 120 ⟵ “Total                $21,233                                  $42,466               including 12 hours. Part-time students pay a $120”
### `9e7da78a4c6cb351` King University — costs 2024-25 [new] (labeled_in_source)
- source: https://media.king.edu/2024/07/24-25-Catalog-1.pdf (sha256 b653dfcee802)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 2, "components": ["books_supplies", "food", "housing", "total", "tuition"], "components_reconcile": false}
  - column:books_supplies: 290 ⟵ “a comprehensive fee, the cost of books and course                                                                         $290/face-to-face”
  - column:housing: 2732 ⟵ “Room*                     $2,732                               $5,464”
  - column:food: 2708 ⟵ “Board                     $2,708                               $5,416”
  - column:total: 23537 ⟵ “Total                  $23,537                              $47,074”
  - column:tuition: 300 ⟵ “Tuition (per semester hour) ....................................... $300            Psychiatric Mental Health Nurse       $680”
  - column:housing: 340 ⟵ “Room (per month)....................................................... $340        Practitioner”
  - column:housing: 5464 ⟵ “Room*                     $2,732                               $5,464”
  - column:food: 5416 ⟵ “Board                     $2,708                               $5,416”
  - column:total: 47074 ⟵ “Total                  $23,537                              $47,074”
  - column:tuition: 680 ⟵ “Tuition (per semester hour) ....................................... $300            Psychiatric Mental Health Nurse       $680”
### `a58c7b233e4869a5` King University — costs 2025-26 [new] (labeled_in_source)
- source: https://media.king.edu/2025/07/2025-2026-Academic-Catalog-1.pdf (sha256 c9ea888bf746)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 3, "components": ["food", "housing", "mandatory_fees", "total", "tuition"], "components_reconcile": false}
  - column:housing: 2842 ⟵ “Room*                     $2,842                            $5,684             Professional MBA                            $605”
  - column:food: 2871 ⟵ “Board                     $2,871                            $5,742             Traditional MBA                        $6500/semester”
  - column:total: 24495 ⟵ “Total                  $24,495                           $48,990             MED: Curriculum and Instruction             $365”
  - column:tuition: 400 ⟵ “Tuition (per semester hour) ....................................... $400        Post-Grad Certificate: Psychiatric          $680”
  - column:housing: 350 ⟵ “room occupancy and $350 per semester for”
  - column:mandatory_fees: 25 ⟵ “fee of $25 on any returned check. Repeated returned”
  - column:housing: 5684 ⟵ “Room*                     $2,842                            $5,684             Professional MBA                            $605”
  - column:food: 5742 ⟵ “Board                     $2,871                            $5,742             Traditional MBA                        $6500/semester”
  - column:total: 48990 ⟵ “Total                  $24,495                           $48,990             MED: Curriculum and Instruction             $365”
  - column:tuition: 680 ⟵ “Tuition (per semester hour) ....................................... $400        Post-Grad Certificate: Psychiatric          $680”
  - column:housing: 605 ⟵ “Room*                     $2,842                            $5,684             Professional MBA                            $605”
  - column:food: 6500 ⟵ “Board                     $2,871                            $5,742             Traditional MBA                        $6500/semester”
  - column:total: 365 ⟵ “Total                  $24,495                           $48,990             MED: Curriculum and Instruction             $365”
### `b0ea9d26c9d22a5e` King University — costs 2011-12 [new] (labeled_in_source)
- source: https://media.king.edu/2018/10/AcademicCatalog2011-2012.pdf (sha256 04f43386132f)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2011-12
- checks: {"columns": 2, "components": ["food", "housing", "total", "tuition"], "components_reconcile": false}
  - column:housing: 2054 ⟵ “Room                                                              *$2,054                                    *$4,108”
  - column:housing: 2154 ⟵ “Room Hyde Hall                                                     $2,154                                     $4,308”
  - column:food: 2036 ⟵ “Board                                                              $2,036                                     $4,072”
  - column:total: 16116 ⟵ “Total                                                                $16,116                                    $32,232”
  - column:tuition: 125 ⟵ “Tuition (per semester hour)                                         $125”
  - column:housing: 340 ⟵ “Room                                                                $340”
  - column:housing: 4108 ⟵ “Room                                                              *$2,054                                    *$4,108”
  - column:housing: 4308 ⟵ “Room Hyde Hall                                                     $2,154                                     $4,308”
  - column:food: 4072 ⟵ “Board                                                              $2,036                                     $4,072”
  - column:total: 32232 ⟵ “Total                                                                $16,116                                    $32,232”
### `b71b9e055a85678f` King University — costs 2009-10 [new] (labeled_in_title)
- source: https://media.king.edu/2018/10/AcademicCatalog2009-2010.pdf (sha256 d3b57b3f6c95)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2009-10
- checks: {"columns": 2, "components": ["food", "housing", "total", "tuition"], "components_reconcile": false}
  - column:housing: 1863 ⟵ “Room                                                              *$1,863                                    *$3,726”
  - column:housing: 1963 ⟵ “Room Hyde Hall                                                     $1,963                                     $3,926”
  - column:food: 1846 ⟵ “Board                                                              $1,846                                     $3,692”
  - column:total: 14649 ⟵ “Total                                                                $14,649                                    $29,298”
  - column:tuition: 125 ⟵ “Tuition (per semester hour)                                         $125”
  - column:housing: 340 ⟵ “Room                                                                $340”
  - column:housing: 3726 ⟵ “Room                                                              *$1,863                                    *$3,726”
  - column:housing: 3926 ⟵ “Room Hyde Hall                                                     $1,963                                     $3,926”
  - column:food: 3692 ⟵ “Board                                                              $1,846                                     $3,692”
  - column:total: 29298 ⟵ “Total                                                                $14,649                                    $29,298”
### `07bc16af35733de1` Lane College — costs 2025-26 [new] (labeled_in_source)
- source: https://www.lanecollege.edu/financial-aid-tuition/college-costs (sha256 22afe0ea1866)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 3, "components": ["food", "housing", "mandatory_fees", "total", "tuition"], "components_reconcile": false}
  - column:tuition: 5099.0 ⟵ “Tuition (12-16 hours) | $5,099.00 | $5,099.00 | $10,198.00”
  - column:mandatory_fees: 350.0 ⟵ “Technology Fee | $350.00 | $350.00 | $700.00”
  - column:housing: 2620.0 ⟵ “Housing (9-Month) | $2,620.00 | $2,620.00 | $5,240.00”
  - column:food: 1570.0 ⟵ “Meal Plan (9-Month) | $1,570.00 | $1,570.00 | $3,140.00”
  - column:total: 10724.0 ⟵ “Total | $10,724.00 | $10,724.00 | $21,448.00”
  - column:tuition: 5099.0 ⟵ “Tuition (12-16 hours) | $5,099.00 | $5,099.00 | $10,198.00”
  - column:mandatory_fees: 350.0 ⟵ “Technology Fee | $350.00 | $350.00 | $700.00”
  - column:housing: 2620.0 ⟵ “Housing (9-Month) | $2,620.00 | $2,620.00 | $5,240.00”
  - column:food: 1570.0 ⟵ “Meal Plan (9-Month) | $1,570.00 | $1,570.00 | $3,140.00”
  - column:total: 10724.0 ⟵ “Total | $10,724.00 | $10,724.00 | $21,448.00”
  - column:tuition: 10198.0 ⟵ “Tuition (12-16 hours) | $5,099.00 | $5,099.00 | $10,198.00”
  - column:mandatory_fees: 700.0 ⟵ “Technology Fee | $350.00 | $350.00 | $700.00”
  - column:housing: 5240.0 ⟵ “Housing (9-Month) | $2,620.00 | $2,620.00 | $5,240.00”
  - column:food: 3140.0 ⟵ “Meal Plan (9-Month) | $1,570.00 | $1,570.00 | $3,140.00”
  - column:total: 21448.0 ⟵ “Total | $10,724.00 | $10,724.00 | $21,448.00”
### `error-pipeline.extractors.costs-3f191625e6a132cc0ceb.json.gz` Lee University — None  [?] ()
- source: https://www.leeuniversity.edu/admissions/tn-transfer-pathways/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-43fb6fc1aae95baf66b2.json.gz` Lee University — None  [?] ()
- source: https://www.leeuniversity.edu/financial-aid/cost/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-59e16aa97b873fb7ea6d.json.gz` Lee University — None  [?] ()
- source: https://www.leeuniversity.edu/admissions/area-hotels/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-a56b031a1c1a7c0e19b6.json.gz` Lee University — None  [?] ()
- source: https://www.leeuniversity.edu/financial-aid/scholarships/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-ba82047778278dd3d5d3.json.gz` Lee University — None  [?] ()
- source: http://catalog.leeuniversity.edu
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-bc68a0f9773617120482.json.gz` Lee University — None  [?] ()
- source: https://www.leeuniversity.edu/institutional-research/common-data-sets/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `047c2a4e9bbe4386` Lee University — admissions_metrics 2014-15 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2014-2015.pdf (sha256 569b57232897)
- issues: c1_totals_incomplete, stale_year_label:2014-15
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [420, 540] ⟵ “SAT Math                               420                    540”
  - act_25..75: [21, 27] ⟵ “ACT Composite                              21                    27”
### `08a301c0a3c3471c` Lee University — admissions_metrics 2011-12 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2011-2012.pdf (sha256 1b8fdc801466)
- issues: c1_totals_incomplete, stale_year_label:2011-12
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [460, 610] ⟵ “SAT Math                      460                610”
  - act_25..75: [21, 27] ⟵ “ACT Composite                 21                 27”
### `0f4abb547162d2f3` Lee University — admissions_metrics 2010-11 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2010-2011.pdf (sha256 520232927ab3)
- issues: c1_totals_incomplete, stale_year_label:2010-11
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [440, 590] ⟵ “SAT Math                      440                 590”
  - act_25..75: [20, 27] ⟵ “ACT Composite                 20                  27”
### `25a069a0df2c4f92` Lee University — admissions_metrics 2023-24 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/2023-2024-CDS-1-1.pdf (sha256 7b8ceafe4c73)
- issues: applications_multiple_numbers, admits_multiple_numbers, enrolled_multiple_numbers, c1_totals_incomplete, stale_year_label:2023-24
- checks: {"fields": ["act_25", "act_50", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - sat_composite_25..75: [1020, 1120, 1220] ⟵ “SAT Composite                                                        1020                               1120                               1220”
  - sat_reading_25..75: [520, 580, 630] ⟵ “SAT Evidence-Based Reading and Writing                               520                                580                                630”
  - sat_math_25..75: [500, 540, 610] ⟵ “SAT Math                                                             500                                540                                610”
  - act_25..75: [20, 23, 26] ⟵ “ACT Composite                                                         20                                 23                                 26”
### `3c25808744676efe` Lee University — admissions_metrics 2018-19 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2018-2019.pdf (sha256 14980acfc22e)
- issues: c1_totals_incomplete, stale_year_label:2018-19
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [480, 590] ⟵ “SAT Math                              480                    590”
  - act_25..75: [21, 28] ⟵ “ACT Composite                          21                     28”
### `3ccbe9ddbff39fee` Lee University — admissions_metrics 2017-18 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2017-2018.pdf (sha256 a4eb271f1be7)
- issues: c1_totals_incomplete, stale_year_label:2017-18
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75", "sat_reading_25", "sat_reading_75"]}
  - sat_reading_25..75: [510, 630] ⟵ “SAT Evidence-Based Reading and Writing                        510                            630”
  - sat_math_25..75: [490, 610] ⟵ “SAT Math                                                      490                            610”
  - act_25..75: [21, 28] ⟵ “ACT Composite                                                    21                             28”
### `7309d5d479485a69` Lee University — admissions_metrics 2019-20 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2019-2020.pdf (sha256 d7448822a3d0)
- issues: c1_totals_incomplete, stale_year_label:2019-20
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_75", "sat_math_25", "sat_math_75"]}
  - sat_composite_25..75: [1000, 1240] ⟵ “SAT Composite                      1000                1240”
  - sat_math_25..75: [450, 610] ⟵ “SAT Math                           450                  610”
  - act_25..75: [21, 28] ⟵ “ACT Composite                       21                  28”
### `798a861b32f16209` Lee University — admissions_metrics 2021-22 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2021-2022.pdf (sha256 583c5af2a52d)
- issues: c1_totals_incomplete, stale_year_label:2021-22
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_75", "sat_math_25", "sat_math_75", "sat_reading_25", "sat_reading_75"]}
  - sat_composite_25..75: [1000, 1230] ⟵ “SAT Composite                                           1000                      1230”
  - sat_reading_25..75: [500, 630] ⟵ “SAT Evidence-Based Reading and Writing                        500                         630”
  - sat_math_25..75: [500, 600] ⟵ “SAT Math                                                      500                         600”
  - act_25..75: [20, 28] ⟵ “ACT Composite                                                 20                          28”
### `831e72f1ed8ebba2` Lee University — admissions_metrics 2007-08 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2007-2008.pdf (sha256 838a37477ad0)
- issues: c1_totals_incomplete, stale_year_label:2007-08
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [450, 620] ⟵ “SAT Math                      450                 620”
  - act_25..75: [20, 27] ⟵ “ACT Composite                 20                  27”
### `899983cbb9e94348` Lee University — admissions_metrics 2022-23 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2022-2023.pdf (sha256 eca78d8e31f4)
- issues: c1_totals_incomplete, stale_year_label:2022-23
- checks: {"fields": ["act_25", "act_50", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - sat_composite_25..75: [1000, 1140, 1240] ⟵ “SAT Composite                                           1000                      1140                       1240”
  - sat_reading_25..75: [520, 580, 630] ⟵ “SAT Evidence-Based Reading and Writing                  520                        580                       630”
  - sat_math_25..75: [490, 550, 610] ⟵ “SAT Math                                                490                        550                       610”
  - act_25..75: [19, 24, 27] ⟵ “ACT Composite                                            19                        24                         27”
### `9a4c1ebd42cbceef` Lee University — admissions_metrics 2016-17 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2016-2017.pdf (sha256 1e9c2ecba91e)
- issues: c1_totals_incomplete, stale_year_label:2016-17
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [450, 580] ⟵ “SAT Math                               450                   580”
  - act_25..75: [21, 28] ⟵ “ACT Composite                              21                    28”
### `9dfd7dc38c082643` Lee University — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/2025-2026-CDS-1-1.pdf (sha256 2789690c4071)
- issues: applications_multiple_numbers, admits_multiple_numbers, c1_totals_incomplete
- checks: {"fields": ["act_25", "act_50", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - sat_composite_25..75: [1030, 1120, 1230] ⟵ “SAT Composite                                                        1030                               1120                               1230”
  - sat_reading_25..75: [530, 570, 640] ⟵ “SAT Evidence-Based Reading and Writing                               530                                570                                640”
  - sat_math_25..75: [490, 540, 600] ⟵ “SAT Math                                                             490                                540                                600”
  - act_25..75: [20, 23, 27] ⟵ “ACT Composite                                                         20                                 23                                 27”
### `b8e96d319dbacbd5` Lee University — admissions_metrics 2015-16 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2015-2016.pdf (sha256 59b6dbeaa937)
- issues: c1_totals_incomplete, stale_year_label:2015-16
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [440, 570] ⟵ “SAT Math                      440                 570”
  - act_25..75: [21, 27] ⟵ “ACT Composite                 21                  27”
### `d1f50fb0b6a724e3` Lee University — admissions_metrics 2008-09 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2008-2009.pdf (sha256 4651d1e1e1c7)
- issues: c1_totals_incomplete, stale_year_label:2008-09
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [460, 580] ⟵ “SAT Math                      460                 580”
  - act_25..75: [20, 27] ⟵ “ACT Composite                 20                  27”
### `e340c37c900a0e76` Lee University — admissions_metrics 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2020-2021.pdf (sha256 805c07f42e33)
- issues: c1_totals_incomplete, stale_year_label:2020-21
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_75", "sat_math_25", "sat_math_75", "sat_reading_25", "sat_reading_75"]}
  - sat_composite_25..75: [980, 1210] ⟵ “SAT Composite                                           980                       1210”
  - sat_reading_25..75: [500, 620] ⟵ “SAT Evidence-Based Reading and Writing                       500                          620”
  - sat_math_25..75: [470, 580] ⟵ “SAT Math                                                     470                          580”
  - act_25..75: [21, 27] ⟵ “ACT Composite                                                 21                          27”
### `e5a51cc9dbe74092` Lee University — admissions_metrics 2009-10 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2009-2010.pdf (sha256 c606f98ce2d1)
- issues: c1_totals_incomplete, stale_year_label:2009-10
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [460, 600] ⟵ “SAT Math                      460                 600”
  - act_25..75: [20, 27] ⟵ “ACT Composite                 20                  27”
### `ea116ce9577c80c3` Lee University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/2024-2025-CDS.pdf (sha256 0e1d4e31cec3)
- issues: applications_multiple_numbers, admits_multiple_numbers, c1_totals_incomplete, stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - sat_composite_25..75: [1020, 1140, 1210] ⟵ “SAT Composite                                                        1020                               1140                               1210”
  - sat_reading_25..75: [540, 580, 630] ⟵ “SAT Evidence-Based Reading and Writing                               540                                580                                630”
  - sat_math_25..75: [500, 550, 600] ⟵ “SAT Math                                                             500                                550                                600”
  - act_25..75: [20, 23, 27] ⟵ “ACT Composite                                                         20                                 23                                 27”
### `f400f843becf506b` Lee University — admissions_metrics 2012-13 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2012-2013.pdf (sha256 c648c2a638e2)
- issues: c1_totals_incomplete, stale_year_label:2012-13
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [440, 600] ⟵ “SAT Math                      440                600”
  - act_25..75: [21, 28] ⟵ “ACT Composite                 21                 28”
### `2dcc444ff566a527` Lee University — costs 2008-09 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2008-2009.pdf (sha256 4651d1e1e1c7)
- issues: column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2008-09
- checks: {"columns": 1, "components": ["books_supplies", "food", "food_housing", "housing", "mandatory_fees", "total", "transportation", "tuition"], "components_reconcile": false}
  - column:mandatory_fees: 560 ⟵ “REQUIRED FEES:                                                $560                              $560”
  - column:food_housing: 5650 ⟵ “ROOM AND BOARD:                                             $5,650                            $5,650”
  - column:housing: 2720 ⟵ “ROOM ONLY:                                                  $2,720                            $2,720”
  - column:food: 2930 ⟵ “BOARD ONLY:                                                 $2,930                            $2,930”
  - column:books_supplies: 900 ⟵ “Books and supplies:               $900            $900                $900”
  - column:housing: 3270 ⟵ “Room only:                        $3270           $1550               $5960”
  - column:food: 2930 ⟵ “Board only:                       $2930           $1300               $3900”
  - column:transportation: 1630 ⟵ “Transportation:                   $1630           $1400               $2490”
  - column:total: 10868029 ⟵ “Total Scholarships/Grants                       $10,868,029                $5,460,670”
  - column:total: 11617518 ⟵ “Total Self-Help                                 $11,617,518                $4,716,860”
  - column:tuition: 572456 ⟵ “Tuition Waivers                                   $572,456                   $1,283,053”
### `3de701a5b19d2804` Lee University — costs 2025-26 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/2025-2026-CDS-1-1.pdf (sha256 2789690c4071)
- issues: arrangement_unlabeled, column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 2, "components": ["books_supplies", "total"], "components_reconcile": false}
  - column:books_supplies: 1355 ⟵ “Books and supplies:                       $ 1,355               $ 1,355                        $ 1,355”
  - column:total: 7797969 ⟵ “Total Scholarships/Grants                                                                $23,954,631          $7,797,969”
  - column:total: 4803754 ⟵ “Total Self-Help                                                                          $8,709,748           $4,803,754”
  - column:books_supplies: 1355 ⟵ “Books and supplies:                       $ 1,355               $ 1,355                        $ 1,355”
### `51aa03c40878d3cb` Lee University — costs 2025-26 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/2025-2026-CDS-1-1.pdf (sha256 2789690c4071)
- issues: column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 1, "components": ["books_supplies", "total", "tuition"], "components_reconcile": false}
  - column:tuition: 25440 ⟵ “Tuition:                                                                                             $ 25,440”
  - column:books_supplies: 1355 ⟵ “Books and supplies:                       $ 1,355               $ 1,355                        $ 1,355”
  - column:total: 23954631 ⟵ “Total Scholarships/Grants                                                                $23,954,631          $7,797,969”
  - column:total: 8709748 ⟵ “Total Self-Help                                                                          $8,709,748           $4,803,754”
### `683ef6fcb9a2af71` Lee University — costs 2021-22 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2021-2022.pdf (sha256 583c5af2a52d)
- issues: arrangement_unlabeled, column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2021-22
- checks: {"columns": 2, "components": ["books_supplies", "total"], "components_reconcile": false}
  - column:books_supplies: 1250 ⟵ “Books and supplies:                       $ 1,250               $ 1,250                        $ 1,250”
  - column:total: 7578356 ⟵ “Total Scholarships/Grants                                                                    $23,603,980           $7,578,356”
  - column:total: 5351394 ⟵ “Total Self-Help                                                                              $13,127,464           $5,351,394”
  - column:books_supplies: 1250 ⟵ “Books and supplies:                       $ 1,250               $ 1,250                        $ 1,250”
### `803e7d471277fa56` Lee University — costs 2007-08 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2007-2008.pdf (sha256 838a37477ad0)
- issues: arrangement_unlabeled, column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2007-08
- checks: {"columns": 2, "components": ["books_supplies", "food", "food_housing", "housing", "mandatory_fees", "total", "transportation", "tuition"], "components_reconcile": false}
  - column:mandatory_fees: 270 ⟵ “REQUIRED FEES:                                                $270                              $270”
  - column:food_housing: 5470 ⟵ “ROOM AND BOARD:                                             $5,470                            $5,470”
  - column:housing: 2640 ⟵ “ROOM ONLY:                                                  $2,640                            $2,640”
  - column:food: 2830 ⟵ “BOARD ONLY:                                                 $2,830                            $2,830”
  - column:books_supplies: 900 ⟵ “Books and supplies:               $900             $900                $900”
  - column:housing: 1400 ⟵ “Room only:                        $3,050           $1,400              $5,650”
  - column:food: 1260 ⟵ “Board only:                       $2,830           $1,260              $3,750”
  - column:food_housing: 2660 ⟵ “Room and board total (if          $5,880           $2,660              $9,400”
  - column:transportation: 1300 ⟵ “Transportation:                   $1,456           $1,300              $2,380”
  - column:total: 5310896 ⟵ “Total Scholarships/Grants                       $10,166,926                $5,310,896”
  - column:total: 4046555 ⟵ “Total Self-Help                                 $10,998,124                $4,046,555”
  - column:tuition: 990575 ⟵ “Tuition Waivers                                   $684,908                   $990,575”
  - column:books_supplies: 900 ⟵ “Books and supplies:               $900             $900                $900”
  - column:housing: 5650 ⟵ “Room only:                        $3,050           $1,400              $5,650”
  - column:food: 3750 ⟵ “Board only:                       $2,830           $1,260              $3,750”
  - column:food_housing: 9400 ⟵ “Room and board total (if          $5,880           $2,660              $9,400”
  - column:transportation: 2380 ⟵ “Transportation:                   $1,456           $1,300              $2,380”
### `9d8f02c901ef5906` Lee University — costs 2021-22 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2021-2022.pdf (sha256 583c5af2a52d)
- issues: column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2021-22
- checks: {"columns": 1, "components": ["books_supplies", "total", "tuition"], "components_reconcile": false}
  - column:tuition: 21000 ⟵ “Tuition:                                                                                              $ 21,000”
  - column:books_supplies: 1250 ⟵ “Books and supplies:                       $ 1,250               $ 1,250                        $ 1,250”
  - column:total: 23603980 ⟵ “Total Scholarships/Grants                                                                    $23,603,980           $7,578,356”
  - column:total: 13127464 ⟵ “Total Self-Help                                                                              $13,127,464           $5,351,394”
### `b41e6b66bf1e42d4` Lee University — costs 2008-09 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2008-2009.pdf (sha256 4651d1e1e1c7)
- issues: arrangement_unlabeled, column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2008-09
- checks: {"columns": 2, "components": ["books_supplies", "food", "food_housing", "housing", "mandatory_fees", "total", "transportation", "tuition"], "components_reconcile": false}
  - column:mandatory_fees: 560 ⟵ “REQUIRED FEES:                                                $560                              $560”
  - column:food_housing: 5650 ⟵ “ROOM AND BOARD:                                             $5,650                            $5,650”
  - column:housing: 2720 ⟵ “ROOM ONLY:                                                  $2,720                            $2,720”
  - column:food: 2930 ⟵ “BOARD ONLY:                                                 $2,930                            $2,930”
  - column:books_supplies: 900 ⟵ “Books and supplies:               $900            $900                $900”
  - column:housing: 1550 ⟵ “Room only:                        $3270           $1550               $5960”
  - column:food: 1300 ⟵ “Board only:                       $2930           $1300               $3900”
  - column:transportation: 1400 ⟵ “Transportation:                   $1630           $1400               $2490”
  - column:total: 5460670 ⟵ “Total Scholarships/Grants                       $10,868,029                $5,460,670”
  - column:total: 4716860 ⟵ “Total Self-Help                                 $11,617,518                $4,716,860”
  - column:tuition: 1283053 ⟵ “Tuition Waivers                                   $572,456                   $1,283,053”
  - column:books_supplies: 900 ⟵ “Books and supplies:               $900            $900                $900”
  - column:housing: 5960 ⟵ “Room only:                        $3270           $1550               $5960”
  - column:food: 3900 ⟵ “Board only:                       $2930           $1300               $3900”
  - column:transportation: 2490 ⟵ “Transportation:                   $1630           $1400               $2490”
### `beeb00991cb45bf5` Lee University — costs 2009-10 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2009-2010.pdf (sha256 c606f98ce2d1)
- issues: column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2009-10
- checks: {"columns": 1, "components": ["total", "tuition"], "components_reconcile": false}
  - column:total: 14034390 ⟵ “Total Scholarships/Grants                       $14,034,390                $5,857,920”
  - column:total: 13043694 ⟵ “Total Self-Help                                 $13,043,694                $4,962,987”
  - column:tuition: 727757 ⟵ “Tuition Waivers                                   $727,757                   $648,184”
### `d35b3daec7e8c9ab` Lee University — costs 2007-08 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2007-2008.pdf (sha256 838a37477ad0)
- issues: column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2007-08
- checks: {"columns": 1, "components": ["books_supplies", "food", "food_housing", "housing", "mandatory_fees", "total", "transportation", "tuition"], "components_reconcile": false}
  - column:mandatory_fees: 270 ⟵ “REQUIRED FEES:                                                $270                              $270”
  - column:food_housing: 5470 ⟵ “ROOM AND BOARD:                                             $5,470                            $5,470”
  - column:housing: 2640 ⟵ “ROOM ONLY:                                                  $2,640                            $2,640”
  - column:food: 2830 ⟵ “BOARD ONLY:                                                 $2,830                            $2,830”
  - column:books_supplies: 900 ⟵ “Books and supplies:               $900             $900                $900”
  - column:housing: 3050 ⟵ “Room only:                        $3,050           $1,400              $5,650”
  - column:food: 2830 ⟵ “Board only:                       $2,830           $1,260              $3,750”
  - column:food_housing: 5880 ⟵ “Room and board total (if          $5,880           $2,660              $9,400”
  - column:transportation: 1456 ⟵ “Transportation:                   $1,456           $1,300              $2,380”
  - column:total: 10166926 ⟵ “Total Scholarships/Grants                       $10,166,926                $5,310,896”
  - column:total: 10998124 ⟵ “Total Self-Help                                 $10,998,124                $4,046,555”
  - column:tuition: 684908 ⟵ “Tuition Waivers                                   $684,908                   $990,575”
### `d85c1d611583b782` Lee University — costs 2010-11 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2010-2011.pdf (sha256 520232927ab3)
- issues: column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2010-11
- checks: {"columns": 1, "components": ["books_supplies", "food", "food_housing", "housing", "mandatory_fees", "total", "transportation", "tuition"], "components_reconcile": false}
  - column:mandatory_fees: 560 ⟵ “REQUIRED FEES:                                                $560                              $560”
  - column:food_housing: 6010 ⟵ “ROOM AND BOARD:                                             $6,010                            $6,010”
  - column:housing: 2900 ⟵ “ROOM ONLY:                                                  $2,900                            $2,900”
  - column:food: 3110 ⟵ “BOARD ONLY:                                                 $3,110                            $3,110”
  - column:books_supplies: 1000 ⟵ “Books and supplies:               $1,000            $1,000              $1,000”
  - column:housing: 6460 ⟵ “Room only:                                                              $6,460”
  - column:food: 1500 ⟵ “Board only:                                         $1,500              $4,260”
  - column:transportation: 1760 ⟵ “Transportation:                   $1,760            $1,450              $2,700”
  - column:total: 22054886 ⟵ “Total Scholarships/Grants                       $22,054,886                $8,482,749”
  - column:total: 4383307 ⟵ “Total Self-Help                                 16,095,809                 $4,383,307”
  - column:tuition: 882865 ⟵ “Tuition Waivers                                   $882,865                   $610,801”
### `fcdf046c86771783` Lee University — costs 2010-11 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2010-2011.pdf (sha256 520232927ab3)
- issues: arrangement_unlabeled, column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2010-11
- checks: {"columns": 2, "components": ["books_supplies", "food", "food_housing", "housing", "mandatory_fees", "total", "transportation", "tuition"], "components_reconcile": false}
  - column:mandatory_fees: 560 ⟵ “REQUIRED FEES:                                                $560                              $560”
  - column:food_housing: 6010 ⟵ “ROOM AND BOARD:                                             $6,010                            $6,010”
  - column:housing: 2900 ⟵ “ROOM ONLY:                                                  $2,900                            $2,900”
  - column:food: 3110 ⟵ “BOARD ONLY:                                                 $3,110                            $3,110”
  - column:books_supplies: 1000 ⟵ “Books and supplies:               $1,000            $1,000              $1,000”
  - column:food: 4260 ⟵ “Board only:                                         $1,500              $4,260”
  - column:transportation: 1450 ⟵ “Transportation:                   $1,760            $1,450              $2,700”
  - column:total: 8482749 ⟵ “Total Scholarships/Grants                       $22,054,886                $8,482,749”
  - column:tuition: 610801 ⟵ “Tuition Waivers                                   $882,865                   $610,801”
  - column:books_supplies: 1000 ⟵ “Books and supplies:               $1,000            $1,000              $1,000”
  - column:transportation: 2700 ⟵ “Transportation:                   $1,760            $1,450              $2,700”
### `ffb76c3be135527f` Lee University — costs 2009-10 [new] (labeled_in_title)
- source: https://www.leeuniversity.edu/wp-content/uploads/CDS-2009-2010.pdf (sha256 c606f98ce2d1)
- issues: column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2009-10
- checks: {"columns": 1, "components": ["total", "tuition"], "components_reconcile": false}
  - column:total: 5857920 ⟵ “Total Scholarships/Grants                       $14,034,390                $5,857,920”
  - column:total: 4962987 ⟵ “Total Self-Help                                 $13,043,694                $4,962,987”
  - column:tuition: 648184 ⟵ “Tuition Waivers                                   $727,757                   $648,184”
### `0cae40622b659e70` Lincoln Memorial University — costs 2022-23 [new] (labeled_in_source)
- source: https://cdmcatalog.lmunet.edu/sites/default/files/cdm_college-of-dental-medicine-catalog-20232024.pdf (sha256 93b407e2f648)
- issues: stale_year_label:2022-23
- checks: {"columns": 1, "components": ["books_supplies", "tuition"]}
  - column:books_supplies: 3500 ⟵ “second series of 3 injections needs to be             Supplies                                            $3500”
  - column:books_supplies: 500 ⟵ “weeks following completion                            Textbooks                                           $500”
  - column:tuition: 69500 ⟵ “Tuition                                             $69,500”
  - column:books_supplies: 3500 ⟵ “ray and/or QuantiFERON-TB Gold test within 6          Supplies                                            $3500”
  - column:books_supplies: 300 ⟵ “Textbooks                                           $300”
  - column:tuition: 69500 ⟵ “Tuition                                             $69,500”
  - column:books_supplies: 14500 ⟵ “Instrument, Loupes, and Supplies                    $14,500”
  - column:books_supplies: 1650 ⟵ “Textbooks                                           $1650        Acceptance/Matriculation Fee”
  - column:tuition: 69500 ⟵ “Tuition                                             $69,500      Curriculum - DMD”
  - column:books_supplies: 3500 ⟵ “Instruments and Supplies                            $3500        program consisting of 270.5/280.5 credit hours culminating”
  - column:books_supplies: 1000 ⟵ “Textbooks                                           $1000”
  - column:books_supplies: 5200 ⟵ “Instruments, Loupes, and Supplies                   $5200”
  - column:books_supplies: 1650 ⟵ “has a cumulative GPA of 2.4 or higher on all previous            Textbooks                                           $1650”
  - column:books_supplies: 1650 ⟵ “transferable seated, college-level course work at an             Textbooks                                           $1650”
  - column:books_supplies: 1000 ⟵ “Textbooks                                           $1000”
### `2f93a881f6ee3bf7` Lincoln Memorial University — costs 2026-27 [new] (source_unlabeled)
- source: https://cvmorangeparkcatalog.lmunet.edu/tuition-and-fees (sha256 06196f5fd734)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components": ["books_supplies", "food", "housing", "loan_fees", "mandatory_fees", "personal", "total", "transportation", "tuition"], "components_reconcile": false}
  - column:tuition: 12420 ⟵ “Tuition*($690 per credit hour) | $12,420”
  - column:mandatory_fees: 314 ⟵ “Fees | $314”
  - column:total: 12734 ⟵ “Total Direct Costs | $12,734”
  - column:books_supplies: 1350 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,350”
  - column:food: 5000 ⟵ “Food | $5,000”
  - column:housing: 6600 ⟵ “Housing | $6,600”
  - column:transportation: 3900 ⟵ “Transportation | $3,900”
  - column:personal: 1600 ⟵ “Miscellaneous Personal Expenses | $1,600”
  - column:loan_fees: 700 ⟵ “Loan Fees | $700”
  - column:total: 19150 ⟵ “Total Indirect Costs | $19,150”
### `0bf785413c1a432b` Lipscomb University — costs 2026-27 [new] (ambiguous_year_labels)
- source: https://lipscomb.edu/admission/tuition-and-financial-aid/cost-attendance (sha256 4fe1468ec981)
- issues: ambiguous_year_labels, arrangement_unlabeled, cost_period_semester
- checks: {"columns": 4, "components": ["books_supplies", "food_housing", "personal", "total", "transportation", "tuition_and_fees"], "components_reconcile": true}
  - column:tuition_and_fees: 44938 ⟵ “Tuition & Fees | $44,938 | $36,300 | $45,500 | $48,844”
  - column:food_housing: 33720 ⟵ “Housing & Food | $33,720 | $33,720 | $33,720 | $33,720”
  - column:books_supplies: 2105 ⟵ “Books & Supplies | $2,105 | $2,004 | $2,004 | $2,004”
  - column:personal: 6005 ⟵ “Personal Expenses | $6,005 | $6,612 | $3,162 | $6,612”
  - column:transportation: 6320 ⟵ “Transportation | $6,320 | $4,420 | $3,162 | $4,420”
  - column:total: 93088 ⟵ “Total | $93,088 | $83,056 | $85,400 | $95,610”
  - column:tuition_and_fees: 36300 ⟵ “Tuition & Fees | $44,938 | $36,300 | $45,500 | $48,844”
  - column:food_housing: 33720 ⟵ “Housing & Food | $33,720 | $33,720 | $33,720 | $33,720”
  - column:books_supplies: 2004 ⟵ “Books & Supplies | $2,105 | $2,004 | $2,004 | $2,004”
  - column:personal: 6612 ⟵ “Personal Expenses | $6,005 | $6,612 | $3,162 | $6,612”
  - column:transportation: 4420 ⟵ “Transportation | $6,320 | $4,420 | $3,162 | $4,420”
  - column:total: 83056 ⟵ “Total | $93,088 | $83,056 | $85,400 | $95,610”
  - column:tuition_and_fees: 45500 ⟵ “Tuition & Fees | $44,938 | $36,300 | $45,500 | $48,844”
  - column:food_housing: 33720 ⟵ “Housing & Food | $33,720 | $33,720 | $33,720 | $33,720”
  - column:books_supplies: 2004 ⟵ “Books & Supplies | $2,105 | $2,004 | $2,004 | $2,004”
  - column:personal: 3162 ⟵ “Personal Expenses | $6,005 | $6,612 | $3,162 | $6,612”
  - column:transportation: 3162 ⟵ “Transportation | $6,320 | $4,420 | $3,162 | $4,420”
  - column:total: 85400 ⟵ “Total | $93,088 | $83,056 | $85,400 | $95,610”
  - column:tuition_and_fees: 48844 ⟵ “Tuition & Fees | $44,938 | $36,300 | $45,500 | $48,844”
  - column:food_housing: 33720 ⟵ “Housing & Food | $33,720 | $33,720 | $33,720 | $33,720”
  - column:books_supplies: 2004 ⟵ “Books & Supplies | $2,105 | $2,004 | $2,004 | $2,004”
  - column:personal: 6612 ⟵ “Personal Expenses | $6,005 | $6,612 | $3,162 | $6,612”
  - column:transportation: 4420 ⟵ “Transportation | $6,320 | $4,420 | $3,162 | $4,420”
  - column:total: 95610 ⟵ “Total | $93,088 | $83,056 | $85,400 | $95,610”
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
### `error-pipeline.extractors.costs-14a14b1ab7ae9b8a56b1.json.gz` Maryville College — None  [?] ()
- source: https://www.maryvillecollege.edu/academics/registrar/transfer-pathways
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-40071359e06d3b8075dd.json.gz` Maryville College — None  [?] ()
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/transfer-students/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-7f63cd7585d6979cbf63.json.gz` Maryville College — None  [?] ()
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `56ba42638e7fe37c` Maryville College — costs 2026-27 [new] (labeled_in_source)
- source: https://www.maryvillecollege.edu/admissions/tuition-and-fees/ (sha256 6406d4e60d2c)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components": ["food", "housing", "mandatory_fees", "total", "tuition"], "components_reconcile": false}
  - column:tuition: 20650 ⟵ “Tuition (Full-Time) | $20,650 | $41,300”
  - column:mandatory_fees: 256 ⟵ “Activity Fee | $256 | $512”
  - column:housing: 3440 ⟵ “Room (Basic rate – See all rates) | $3,440 | $6,880”
  - column:food: 3696 ⟵ “Meals (Scots Unlimited – See all plans) | $3,696 | $7,392”
  - column:total: 28603 ⟵ “TOTAL | $28,603 | $56,881”
  - column:tuition: 41300 ⟵ “Tuition (Full-Time) | $20,650 | $41,300”
  - column:mandatory_fees: 512 ⟵ “Activity Fee | $256 | $512”
  - column:housing: 6880 ⟵ “Room (Basic rate – See all rates) | $3,440 | $6,880”
  - column:food: 7392 ⟵ “Meals (Scots Unlimited – See all plans) | $3,696 | $7,392”
  - column:total: 56881 ⟵ “TOTAL | $28,603 | $56,881”
### `cec13ff73747acbe` Mid-South Christian College — costs 2024-25 [new] (labeled_in_source)
- source: https://eb5b4353-e09d-499e-a0dc-26e7bd94531c.filesusr.com/ugd/20f14a_0797a8f3297644a7b44017913d04b8b0.pdf (sha256 2a2f93a237fc)
- issues: column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 1, "components": ["books_supplies", "food_housing", "total", "tuition"], "components_reconcile": false}
  - column:tuition: 42000 ⟵ “Tuition ($350 per credit hour)                                    $ 42,000.00”
  - column:books_supplies: 1600 ⟵ “Books (estimated at $200 per semester)                     $ 1,600.00”
  - column:food_housing: 20000 ⟵ “Room and Board ($2,500 per semester)                                     $ 20,000.00”
  - column:total: 64025 ⟵ “Total cost of program if completed in 4 years or 8 semesters      $ 43,725.00    $ 64,025.00”
  - column:tuition: 46550 ⟵ “Tuition ($350 per credit hour)                                    $ 46,550.00”
  - column:books_supplies: 1600 ⟵ “Books (estimated at $200 per semester)                     $ 1,600.00”
  - column:food_housing: 20000 ⟵ “Room and Board ($2,500 per semester)                                     $ 20,000.00”
  - column:total: 68575 ⟵ “Total cost of program if completed in 4 years or 8 semesters      $ 48,275.00    $ 68,575.00”
  - column:tuition: 46550 ⟵ “Tuition ($350 per credit hour)                                    $ 46,550.00”
  - column:books_supplies: 1600 ⟵ “Books (estimated at $200 per semester)                     $ 1,600.00”
  - column:food_housing: 20000 ⟵ “Room and Board ($2,500 per semester)                                     $ 20,000.00”
  - column:total: 68575 ⟵ “Total cost of program if completed in 4 years or 8 semesters      $ 48,275.00    $ 68,575.00”
  - column:tuition: 46550 ⟵ “Tuition ($350 per credit hour)                                        $ 46,550.00”
  - column:books_supplies: 1600 ⟵ “Books (estimated at $200 per semester)                         $ 1,600.00”
  - column:food_housing: 20000 ⟵ “Room and Board ($2,500 per semester)                                        $ 20,000.00”
  - column:total: 68575 ⟵ “Total cost of program if completed in 4 years or 8 semesters          $ 48,275.00   $ 68,575.00”
  - column:tuition: 43050 ⟵ “Tuition ($350 per credit hour)                                        $ 43,050.00”
  - column:books_supplies: 1600 ⟵ “Books (estimated at $200 per semester)                        $ 1,600.00”
  - column:food_housing: 20000 ⟵ “Room and Board ($2,500 per semester)                                       $ 20,000.00”
  - column:total: 65075 ⟵ “Total cost of program if completed in 4 years or 8 semesters          $ 44,775.00   $ 65,075.00”
  - column:tuition: 43050 ⟵ “Tuition ($350 per credit hour)                                        $ 43,050.00”
  - column:books_supplies: 1600 ⟵ “Books (estimated at $200 per semester)                        $ 1,600.00”
  - column:food_housing: 20000 ⟵ “Room and Board ($2,500 per semester)                                       $ 20,000.00”
  - column:total: 65075 ⟵ “Total cost of program if completed in 4 years or 8 semesters          $ 44,775.00   $ 65,075.00”
  - column:tuition: 43050 ⟵ “Tuition ($350 per credit hour)                                 $ 43,050.00”
  - … 35 more rows
### `dbd4be1cba9b530b` Mid-South Christian College — costs 2024-25 [new] (labeled_in_source)
- source: https://eb5b4353-e09d-499e-a0dc-26e7bd94531c.filesusr.com/ugd/20f14a_0797a8f3297644a7b44017913d04b8b0.pdf (sha256 2a2f93a237fc)
- issues: column_alignment_uncertain, components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 1, "components": ["books_supplies", "food_housing", "mandatory_fees", "total", "tuition"], "components_reconcile": false}
  - column:total: 8025 ⟵ “Total per semester                                                                           $8,025.00”
  - column:tuition: 350 ⟵ “Tuition ($350 per credit hour)                                    $ 42,000.00”
  - column:books_supplies: 200 ⟵ “Books (estimated at $200 per semester)                     $ 1,600.00”
  - column:food_housing: 2500 ⟵ “Room and Board ($2,500 per semester)                                     $ 20,000.00”
  - column:total: 43725 ⟵ “Total cost of program if completed in 4 years or 8 semesters      $ 43,725.00    $ 64,025.00”
  - column:tuition: 350 ⟵ “Tuition ($350 per credit hour)                                    $ 46,550.00”
  - column:books_supplies: 200 ⟵ “Books (estimated at $200 per semester)                     $ 1,600.00”
  - column:food_housing: 2500 ⟵ “Room and Board ($2,500 per semester)                                     $ 20,000.00”
  - column:total: 48275 ⟵ “Total cost of program if completed in 4 years or 8 semesters      $ 48,275.00    $ 68,575.00”
  - column:tuition: 350 ⟵ “Tuition ($350 per credit hour)                                    $ 46,550.00”
  - column:books_supplies: 200 ⟵ “Books (estimated at $200 per semester)                     $ 1,600.00”
  - column:food_housing: 2500 ⟵ “Room and Board ($2,500 per semester)                                     $ 20,000.00”
  - column:total: 48275 ⟵ “Total cost of program if completed in 4 years or 8 semesters      $ 48,275.00    $ 68,575.00”
  - column:tuition: 350 ⟵ “Tuition ($350 per credit hour)                                        $ 46,550.00”
  - column:books_supplies: 200 ⟵ “Books (estimated at $200 per semester)                         $ 1,600.00”
  - column:food_housing: 2500 ⟵ “Room and Board ($2,500 per semester)                                        $ 20,000.00”
  - column:total: 48275 ⟵ “Total cost of program if completed in 4 years or 8 semesters          $ 48,275.00   $ 68,575.00”
  - column:tuition: 350 ⟵ “Tuition ($350 per credit hour)                                        $ 43,050.00”
  - column:books_supplies: 200 ⟵ “Books (estimated at $200 per semester)                        $ 1,600.00”
  - column:food_housing: 2500 ⟵ “Room and Board ($2,500 per semester)                                       $ 20,000.00”
  - column:total: 44775 ⟵ “Total cost of program if completed in 4 years or 8 semesters          $ 44,775.00   $ 65,075.00”
  - column:tuition: 350 ⟵ “Tuition ($350 per credit hour)                                        $ 43,050.00”
  - column:books_supplies: 200 ⟵ “Books (estimated at $200 per semester)                        $ 1,600.00”
  - column:food_housing: 2500 ⟵ “Room and Board ($2,500 per semester)                                       $ 20,000.00”
  - column:total: 44775 ⟵ “Total cost of program if completed in 4 years or 8 semesters          $ 44,775.00   $ 65,075.00”
  - … 37 more rows
### `error-pipeline.extractors.costs-112e273978aace5b05ee.json.gz` Middle Tennessee State University — None  [?] ()
- source: https://www.mtsu.edu/financial-aid/appeals/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-53d6aa65519c8cf4dbd0.json.gz` Middle Tennessee State University — None  [?] ()
- source: https://www.mtsu.edu/contact/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-74e61805a9b085c14950.json.gz` Middle Tennessee State University — None  [?] ()
- source: https://www.mtsu.edu/financial-aid/forms/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-7e9afaee02154017415e.json.gz` Middle Tennessee State University — None  [?] ()
- source: https://www.mtsu.edu/tuition/fee-discounts/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-b327b318e0b89dbc95c0.json.gz` Middle Tennessee State University — None  [?] ()
- source: https://www.mtsu.edu/tuition/dates/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-f4bf87d8a4e3dac54039.json.gz` Middle Tennessee State University — None  [?] ()
- source: http://w1.mtsu.edu/tuition/fee-discounts.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `0ac9e710a7a1df19` Middle Tennessee State University — credit_policies 2010-11 [new] (labeled_in_source)
- source: https://www.mtsu.edu/how-to-apply/credit-by-examination/ (sha256 4affe9ee6718)
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
- source: https://www.mtsu.edu/how-to-apply/credit-by-examination/ (sha256 4affe9ee6718)
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
- source: https://www.mtsu.edu/how-to-apply/credit-by-examination/ (sha256 4affe9ee6718)
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
### `error-pipeline.extractors.costs-b00ef12e63ef1a5fa774.json.gz` Motlow State Community College — None  [?] ()
- source: https://www.mscc.edu/about/awards.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-f241d62feb0de29ae1f9.json.gz` Motlow State Community College — None  [?] ()
- source: http://catalog.mscc.edu
- issues: extractor_error:ValueError: max() iterable argument is empty
### `02329e3d62a5a2ce` Motlow State Community College — costs 2015-16 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2015-16.pdf (sha256 e0491b23201f)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2015-16
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:books_supplies: 1851 ⟵ “Books & Supplies:       $ 1,851”
  - column:mandatory_fees: 152 ⟵ “Fees are assessed at a rate of $152/hour up to 12 hours. Hours above 12 are assessed at additional $30/hour for in-state and $95/hour for out-of-state.”
  - column:tuition_and_fees: 13518994 ⟵ “Tuition and Fees      $13,518,994   38.9%     $13,974,068   41.3%     $13,658,783       39.2%    $14,204,711   41.5%      $14,847,766    42.5%”
  - column:total: 34758969 ⟵ “Total                 $34,758,969             $33,874,552             $34,813,924                $34,227,761              $34,929,075”
  - column:total: 29680708 ⟵ “Total                 $29,680,708             $30,558,162                 $31,961,617            $31,810,349              $32,376,700”
  - column:total: 12084734 ⟵ “Total                      3,882   $12,084,734         5,049       $12,896,664          4,638   $11,373,854        4,738      $11,782,288           4,824    $12,318,054”
  - column:total: 115658 ⟵ “Total Event Fundraisers                            $115,658”
  - column:total: 397699 ⟵ “Total In-Kind                                     $397,699”
  - column:total: 649550 ⟵ “Total Cash & Marketable Securities                $649,550”
### `0433ef2edd26fc69` Motlow State Community College — costs 2018-19 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2018-19.pdf (sha256 191dcae9e4b0)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2018-19
- checks: {"columns": 1, "components": ["mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:mandatory_fees: 34 ⟵ “Fees are assessed at a rate of $164/hour up to 12 hours. Hours above 12 are assessed at additional $34/hour for in-state and $103/hour for out-of-state.”
  - column:tuition_and_fees: 14847766 ⟵ “Tuition and Fees      $14,204,711    41.5%   $14,847,766    42.5%         $17,803,694   41.1%    $19,976,905    41.3%       $21,519,691   40.5%”
  - column:total: 34929075 ⟵ “Total                 $34,227,761            $34,929,075                   43,365,659             48,306,689                 53,329,607”
  - column:total: 32376700 ⟵ “Total                  $31,810,349            $32,376,700             38,745,490                 43,565,118                48,146,385”
  - column:total: 12318054 ⟵ “Total                        4,738        $11,782,288    4,824        $12,318,054        5,551       $16,267,871        6,427          $19,219,743       7,530       $21,769,355”
### `1029963b48cd8f87` Motlow State Community College — costs 2013-14 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2013-14.pdf (sha256 e560bfc19d1e)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2013-14
- checks: {"columns": 1, "components": ["mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:mandatory_fees: 28 ⟵ “Fees are assessed at a rate of $139/hour up to 12 hours. Hours above 12 are assessed at additional $28/hour for in-state and $87/hour for out-of-state.”
  - column:tuition_and_fees: 12658124 ⟵ “Tuition and Fees      $10,648,038   35.0%    $12,658,124   40.8%    $13,518,994      38.9%   $13,974,068   41.3%      $13,658,783    39.2%”
  - column:total: 31013836 ⟵ “Total                 $30,388,564            $31,013,836            $34,758,969              $33,874,552              $34,813,924”
  - column:total: 28377922 ⟵ “Total                 $28,639,137            $28,377,922            $29,680,708              $30,558,162              $31,961,617”
  - column:total: 12851018 ⟵ “Total                      5,943       $9,663,041       4,956       $12,851,018      3,882     $12,084,734       5,049      $12,896,664           4,638   $11,373,854”
### `2e2d8508691345d1` Motlow State Community College — costs 2016-17 [new] (labeled_in_source)
- source: https://www.mscc.edu/documents/fact-book-2016-17.pdf (sha256 6e4350f5156e)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2016-17
- checks: {"columns": 1, "components": ["mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:mandatory_fees: 31 ⟵ “Fees are assessed at a rate of $156/hour up to 12 hours. Hours above 12 are assessed at additional $31/hour for in-state and $97/hour for out-of-state.”
  - column:tuition_and_fees: 13658783 ⟵ “Tuition and Fees      $13,974,068   41.3%     $13,658,783   39.2%     $14,204,711       41.5%    $14,847,766    42.5%      $17,803,694    41.1%”
  - column:total: 34813924 ⟵ “Total                 $33,874,552             $34,813,924             $34,227,761                $34,929,075                 43,365,659”
  - column:total: 31961617 ⟵ “Total                 $30,558,162             $31,961,617                 $31,810,349            $32,376,700                38,745,490”
  - column:total: 11373854 ⟵ “Total                     5,049    $12,896,664           4,638       $11,373,854          4,738   $11,782,288        4,824    $12,318,054           5,551    $16,267,871”
### `4b58d5ae6e42ab83` Motlow State Community College — costs 2016-17 [new] (labeled_in_source)
- source: https://www.mscc.edu/documents/fact-book-2016-17.pdf (sha256 6e4350f5156e)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2016-17
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:books_supplies: 1851 ⟵ “Books & Supplies:       $ 1,851                                          •    Motlow’s F15 to F16 headcount increase of 11.1% was”
  - column:mandatory_fees: 156 ⟵ “Fees are assessed at a rate of $156/hour up to 12 hours. Hours above 12 are assessed at additional $31/hour for in-state and $97/hour for out-of-state.”
  - column:tuition_and_fees: 13974068 ⟵ “Tuition and Fees      $13,974,068   41.3%     $13,658,783   39.2%     $14,204,711       41.5%    $14,847,766    42.5%      $17,803,694    41.1%”
  - column:total: 33874552 ⟵ “Total                 $33,874,552             $34,813,924             $34,227,761                $34,929,075                 43,365,659”
  - column:total: 30558162 ⟵ “Total                 $30,558,162             $31,961,617                 $31,810,349            $32,376,700                38,745,490”
  - column:total: 12896664 ⟵ “Total                     5,049    $12,896,664           4,638       $11,373,854          4,738   $11,782,288        4,824    $12,318,054           5,551    $16,267,871”
  - column:total: 105159 ⟵ “Total Event Fundraisers                            $105,159”
  - column:total: 402256 ⟵ “Total In-Kind                                     $402,256”
  - column:total: 463097 ⟵ “Total Cash & Marketable Securities                $463,097”
### `4d8467297e401e47` Motlow State Community College — costs 2018-19 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2018-19.pdf (sha256 191dcae9e4b0)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2018-19
- checks: {"columns": 1, "components": ["total", "tuition_and_fees"], "components_reconcile": false}
  - column:tuition_and_fees: 19976905 ⟵ “Tuition and Fees      $14,204,711    41.5%   $14,847,766    42.5%         $17,803,694   41.1%    $19,976,905    41.3%       $21,519,691   40.5%”
  - column:total: 19219743 ⟵ “Total                        4,738        $11,782,288    4,824        $12,318,054        5,551       $16,267,871        6,427          $19,219,743       7,530       $21,769,355”
### `671303cb0606ebb4` Motlow State Community College — costs 2014-15 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2014-15.pdf (sha256 27131b3b2e34)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2014-15
- checks: {"columns": 1, "components": ["mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:mandatory_fees: 29 ⟵ “Fees are assessed at a rate of $147/hour up to 12 hours. Hours above 12 are assessed at additional $29/hour for in-state and $92/hour for out-of-state.”
  - column:tuition_and_fees: 13518994 ⟵ “Tuition and Fees      $12,658,124   40.8%    $13,518,994   38.9%        $13,974,068   41.3%   $13,658,783   39.2%      $14,204,711     41.5%”
  - column:total: 34758969 ⟵ “Total                 $31,013,836            $34,758,969            $33,874,552               $34,813,924              $34,227,761”
  - column:total: 29680708 ⟵ “Total                 $28,377,922            $29,680,708                $30,558,162           $31,961,617               $31,810,349”
  - column:total: 12084734 ⟵ “Total                      4,956     $12,851,018          3,882   $12,084,734         5,049   $12,896,664        4,638      $11,373,854           4,738    $11,782,288”
### `7195f3d4d5b20e47` Motlow State Community College — costs 2014-15 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2014-15.pdf (sha256 27131b3b2e34)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2014-15
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:books_supplies: 1851 ⟵ “Books & Supplies:       $ 1,851”
  - column:mandatory_fees: 147 ⟵ “Fees are assessed at a rate of $147/hour up to 12 hours. Hours above 12 are assessed at additional $29/hour for in-state and $92/hour for out-of-state.”
  - column:tuition_and_fees: 12658124 ⟵ “Tuition and Fees      $12,658,124   40.8%    $13,518,994   38.9%        $13,974,068   41.3%   $13,658,783   39.2%      $14,204,711     41.5%”
  - column:total: 31013836 ⟵ “Total                 $31,013,836            $34,758,969            $33,874,552               $34,813,924              $34,227,761”
  - column:total: 28377922 ⟵ “Total                 $28,377,922            $29,680,708                $30,558,162           $31,961,617               $31,810,349”
  - column:total: 12851018 ⟵ “Total                      4,956     $12,851,018          3,882   $12,084,734         5,049   $12,896,664        4,638      $11,373,854           4,738    $11,782,288”
  - column:total: 401472 ⟵ “Total In-Kind                                     $401,472”
  - column:total: 432754 ⟵ “Total Cash & Marketable Securities                $432,754”
### `beead77bb414cdd4` Motlow State Community College — costs 2019-20 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2019-20.pdf (sha256 016c3ef794f0)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2019-20
- checks: {"columns": 1, "components": ["mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:mandatory_fees: 34 ⟵ “Fees are assessed at a rate of $164/hour up to 12 hours. Hours above 12 are assessed at additional $34/hour for in-state and $103/hour for out-of-state.”
  - column:tuition_and_fees: 17803694 ⟵ “Tuition and Fees      $14,847,766   42.5%   $17,803,694   41.1%    $19,976,905    41.3%   $21,519,691    40.5%   $23,643,239      39.4%”
  - column:total: 16267871 ⟵ “Total                   4,824           $12,318,054   5,551      $16,267,871   6,427       $19,219,743       7,530       $21,769,355      8,910        $24,502,225”
### `c4cc0c57ac580c19` Motlow State Community College — costs 2019-20 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2019-20.pdf (sha256 016c3ef794f0)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2019-20
- checks: {"columns": 1, "components": ["total", "tuition_and_fees"], "components_reconcile": false}
  - column:tuition_and_fees: 21519691 ⟵ “Tuition and Fees      $14,847,766   42.5%   $17,803,694   41.1%    $19,976,905    41.3%   $21,519,691    40.5%   $23,643,239      39.4%”
  - column:total: 21769355 ⟵ “Total                   4,824           $12,318,054   5,551      $16,267,871   6,427       $19,219,743       7,530       $21,769,355      8,910        $24,502,225”
### `c878324378d2a278` Motlow State Community College — costs 2015-16 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2015-16.pdf (sha256 e0491b23201f)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2015-16
- checks: {"columns": 1, "components": ["mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:mandatory_fees: 30 ⟵ “Fees are assessed at a rate of $152/hour up to 12 hours. Hours above 12 are assessed at additional $30/hour for in-state and $95/hour for out-of-state.”
  - column:tuition_and_fees: 13974068 ⟵ “Tuition and Fees      $13,518,994   38.9%     $13,974,068   41.3%     $13,658,783       39.2%    $14,204,711   41.5%      $14,847,766    42.5%”
  - column:total: 33874552 ⟵ “Total                 $34,758,969             $33,874,552             $34,813,924                $34,227,761              $34,929,075”
  - column:total: 30558162 ⟵ “Total                 $29,680,708             $30,558,162                 $31,961,617            $31,810,349              $32,376,700”
  - column:total: 12896664 ⟵ “Total                      3,882   $12,084,734         5,049       $12,896,664          4,638   $11,373,854        4,738      $11,782,288           4,824    $12,318,054”
### `d574d575b9bd2ea2` Motlow State Community College — costs 2012-13 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2012-13.pdf (sha256 447d49453f1a)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2012-13
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:books_supplies: 1200 ⟵ “Books & Supplies:       $1,200”
  - column:mandatory_fees: 135 ⟵ “Fees are assessed at a rate of $135/hour up to 12 hours. Hours above 12 are assessed at additional $27/hour for in-state and $84/hour for out-of-state.”
  - column:tuition_and_fees: 9251226 ⟵ “Tuition and Fees       $9,251,226   34.0%    $10,648,038   35.0%    $12,658,124      40.8%   $13,518,994   38.9%      $13,974,068    41.3%”
  - column:total: 27219435 ⟵ “Total                 $27,219,435            $30,388,564            $31,013,836              $34,758,969              $33,874,552”
  - column:total: 24871033 ⟵ “Total                 $24,871,033            $28,639,137            $28,377,922              $29,680,708              $30,558,162”
  - column:total: 7687454 ⟵ “Total                      4,053        $7,687,454        5,943        $9,663,041    4,956     $12,851,018       3,882     $12,084,734           5,049   $12,896,664”
  - column:total: 73852 ⟵ “Total In-Kind                                      $73,852”
  - column:total: 595723 ⟵ “Total Cash & Marketable Securities                $595,723”
### `dd871515f39ce0b8` Motlow State Community College — costs 2013-14 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2013-14.pdf (sha256 e560bfc19d1e)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2013-14
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:books_supplies: 1200 ⟵ “Books & Supplies:       $1,200”
  - column:mandatory_fees: 139 ⟵ “Fees are assessed at a rate of $139/hour up to 12 hours. Hours above 12 are assessed at additional $28/hour for in-state and $87/hour for out-of-state.”
  - column:tuition_and_fees: 10648038 ⟵ “Tuition and Fees      $10,648,038   35.0%    $12,658,124   40.8%    $13,518,994      38.9%   $13,974,068   41.3%      $13,658,783    39.2%”
  - column:total: 30388564 ⟵ “Total                 $30,388,564            $31,013,836            $34,758,969              $33,874,552              $34,813,924”
  - column:total: 28639137 ⟵ “Total                 $28,639,137            $28,377,922            $29,680,708              $30,558,162              $31,961,617”
  - column:total: 9663041 ⟵ “Total                      5,943       $9,663,041       4,956       $12,851,018      3,882     $12,084,734       5,049      $12,896,664           4,638   $11,373,854”
  - column:total: 136558 ⟵ “Total In-Kind                                      $136,558”
  - column:total: 1135907 ⟵ “Total Cash & Marketable Securities                $1,135,907”
### `e0b206694599a9a9` Motlow State Community College — costs 2017-18 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2017-18.pdf (sha256 6e959074ae52)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2017-18
- checks: {"columns": 1, "components": ["mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:mandatory_fees: 32 ⟵ “Fees are assessed at a rate of $160/hour up to 12 hours. Hours above 12 are assessed at additional $32/hour for in-state and $100/hour for out-of-state.”
  - column:tuition_and_fees: 14204711 ⟵ “Tuition and Fees      $13,658,783   39.2%    $14,204,711    41.5%     $14,847,766       42.5%   $17,803,694    41.1%     $19,976,905    41.3%”
  - column:total: 34227761 ⟵ “Total                 $34,813,924            $34,227,761              $34,929,075                43,365,659               48,306,689”
  - column:total: 31810349 ⟵ “Total                 $31,961,617             $31,810,349             $32,376,700               38,745,490               43,565,118”
  - column:total: 11782288 ⟵ “Total                     4,638   $11,373,854         4,738      $11,782,288         4,824   $12,318,054      5,551      $16,267,871           6,427    $19,219,743”
### `f0bd0515a3ce4cb3` Motlow State Community College — costs 2012-13 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2012-13.pdf (sha256 447d49453f1a)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2012-13
- checks: {"columns": 1, "components": ["mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:mandatory_fees: 27 ⟵ “Fees are assessed at a rate of $135/hour up to 12 hours. Hours above 12 are assessed at additional $27/hour for in-state and $84/hour for out-of-state.”
  - column:tuition_and_fees: 10648038 ⟵ “Tuition and Fees       $9,251,226   34.0%    $10,648,038   35.0%    $12,658,124      40.8%   $13,518,994   38.9%      $13,974,068    41.3%”
  - column:total: 30388564 ⟵ “Total                 $27,219,435            $30,388,564            $31,013,836              $34,758,969              $33,874,552”
  - column:total: 28639137 ⟵ “Total                 $24,871,033            $28,639,137            $28,377,922              $29,680,708              $30,558,162”
  - column:total: 9663041 ⟵ “Total                      4,053        $7,687,454        5,943        $9,663,041    4,956     $12,851,018       3,882     $12,084,734           5,049   $12,896,664”
### `f6b2891bdeb70772` Motlow State Community College — costs 2017-18 [new] (labeled_in_title)
- source: https://www.mscc.edu/documents/fact-book-2017-18.pdf (sha256 6e959074ae52)
- issues: column_alignment_uncertain, components_do_not_reconcile, residency_unknown, stale_year_label:2017-18
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "total", "tuition_and_fees"], "components_reconcile": false}
  - column:books_supplies: 758 ⟵ “Books & Supplies:       $ 758                                            Did You Know?”
  - column:mandatory_fees: 160 ⟵ “Fees are assessed at a rate of $160/hour up to 12 hours. Hours above 12 are assessed at additional $32/hour for in-state and $100/hour for out-of-state.”
  - column:tuition_and_fees: 13658783 ⟵ “Tuition and Fees      $13,658,783   39.2%    $14,204,711    41.5%     $14,847,766       42.5%   $17,803,694    41.1%     $19,976,905    41.3%”
  - column:total: 34813924 ⟵ “Total                 $34,813,924            $34,227,761              $34,929,075                43,365,659               48,306,689”
  - column:total: 31961617 ⟵ “Total                 $31,961,617             $31,810,349             $32,376,700               38,745,490               43,565,118”
  - column:total: 11373854 ⟵ “Total                     4,638   $11,373,854         4,738      $11,782,288         4,824   $12,318,054      5,551      $16,267,871           6,427    $19,219,743”
  - column:total: 138638 ⟵ “Total Event Fundraisers                            $138,638”
  - column:total: 412379 ⟵ “Total In-Kind                                      $412,379”
  - column:total: 1046909 ⟵ “Total Cash & Marketable Securities                $1,046,909”
### `error-pipeline.extractors.costs-22ac77e86506f7d85226.json.gz` Nashville State Community College — None  [?] ()
- source: https://nscc.edu/current-students/transfer-options.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-7a6012be17c5e843fa77.json.gz` Nashville State Community College — None  [?] ()
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-e14cc9e14b6fc36cd3a8.json.gz` Nashville State Community College — None  [?] ()
- source: https://www.nscc.edu/tuition-and-aid/tuition-and-fees.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `cb4204a475dddbe0` Nashville State Community College — costs 2001-02 [new] (labeled_in_source)
- source: https://www.nscc.edu/documents/catalogs/Catalog_2001-02.pdf (sha256 9a2745e174db)
- issues: residency_unknown, stale_year_label:2001-02
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "tuition"]}
  - column:tuition: 2585 ⟵ “tuition), maximum of $2,585 per semester ($647                  summer term will be the same as for the other two”
  - column:mandatory_fees: 1938 ⟵ “fee plus $1,938 tuition) in the academic year.                  semesters. Fees for auditing a course will be the”
  - column:books_supplies: 300 ⟵ “of books and supplies is approximately $300-$450                             catalog price. The Bookstore Manager will”
### `d3262370c93f4e1d` Nashville State Community College — costs 2002-03 [new] (labeled_in_source)
- source: https://www.nscc.edu/documents/catalogs/Catalog_2002-03.pdf (sha256 85107eb95a90)
- issues: residency_unknown, stale_year_label:2002-03
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "tuition"]}
  - column:tuition: 2973 ⟵ “tuition), maximum of $2,973 per semester ($744                  summer term will be the same as for the other two”
  - column:mandatory_fees: 2229 ⟵ “fee plus $2,229 tuition) in the academic year.                  semesters. Fees for auditing a course will be the”
  - column:mandatory_fees: 10 ⟵ “fee of $10.00 will also be assessed for any                     Unsubsidized Stafford Loan and FPLUS are”
  - column:books_supplies: 300 ⟵ “of books and supplies is approximately $300-$450               Back” policy below.”
### `f352ee8c33f1351f` Nashville State Community College — costs 2000-01 [new] (labeled_in_source)
- source: https://www.nscc.edu/documents/catalogs/Catalog_2000-01.pdf (sha256 3db5ea8c34fa)
- issues: residency_unknown, stale_year_label:2000-01
- checks: {"columns": 1, "components": ["books_supplies", "mandatory_fees", "tuition"]}
  - column:tuition: 2393 ⟵ “tuition), maximum of $2,393 per semester ($599             summer term will be the same as for the other two”
  - column:mandatory_fees: 1794 ⟵ “fee plus $1,794 tuition) in the academic year.             semesters. Fees for auditing a course will be the”
  - column:books_supplies: 300 ⟵ “of books and supplies is approximately $300-$450                                                                   catalog price. The Bookstore Manager will”
### `error-pipeline.extractors.costs-3e127dded4ae5b79fae0.json.gz` Northeast State Community College — None  [?] ()
- source: https://catalog.northeaststate.edu/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-e38d4dd8609e219ab826.json.gz` Northeast State Community College — None  [?] ()
- source: https://www.northeaststate.edu/financial-aid-tuition/heerf/index.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `979dfddac99d690c` Northeast State Community College — costs 2026-27 [new] (ambiguous_year_labels)
- source: https://www.northeaststate.edu/financial-aid-tuition/cost-of-attendance.html (sha256 883da26037d6)
- issues: ambiguous_year_labels
- checks: {"columns": 2, "components": ["books_supplies", "food_housing", "personal", "total", "transportation", "tuition_and_fees"], "components_reconcile": true}
  - with_parents_or_family:tuition_and_fees: 5280 ⟵ “Tuition and Fees* | $5,280 | $5,280”
  - with_parents_or_family:food_housing: 7532 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - with_parents_or_family:books_supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - with_parents_or_family:transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - with_parents_or_family:personal: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - with_parents_or_family:total: 20304 ⟵ “Total | $20,304 | $28,143”
  - off_campus_not_with_family:tuition_and_fees: 5280 ⟵ “Tuition and Fees* | $5,280 | $5,280”
  - off_campus_not_with_family:food_housing: 15371 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - off_campus_not_with_family:books_supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - off_campus_not_with_family:transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - off_campus_not_with_family:personal: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - off_campus_not_with_family:total: 28143 ⟵ “Total | $20,304 | $28,143”
### `error-pipeline.extractors.costs-480eb749f08ccfea22fa.json.gz` Rhodes College — None  [?] ()
- source: https://www.rhodes.edu/admission-aid/cost-affordability/first-year
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-a076189db8fb04b79c83.json.gz` Rhodes College — None  [?] ()
- source: https://www.rhodes.edu/admission-aid/apply-rhodes/college-credit-transfer-policies
- issues: extractor_error:ValueError: max() iterable argument is empty
### `a1ac6e2806b69324` Rhodes College — costs 2018-19 [new] (labeled_in_source)
- source: https://www.rhodes.edu/sites/default/files/2018-19_Rhodes_College_Catalog_with_Courses_of_Instruction.pdf (sha256 02a48cf49404)
- issues: column_alignment_uncertain, stale_year_label:2018-19
- checks: {"columns": 1, "components": ["mandatory_fees", "tuition"]}
  - column:tuition: 47580 ⟵ “Tuition                                                                 $23,790.00   $47,580.00”
  - column:mandatory_fees: 3000 ⟵ “fees (Type 2); (2) up to $9,000 towards tuition and fees (Type 3); and up to $3,000 towards tuition and”
### `a755b01be9f75121` Rhodes College — costs 2018-19 [new] (labeled_in_source)
- source: https://www.rhodes.edu/sites/default/files/2018-19_Rhodes_College_Catalog_with_Courses_of_Instruction.pdf (sha256 02a48cf49404)
- issues: column_alignment_uncertain, stale_year_label:2018-19
- checks: {"columns": 1, "components": ["mandatory_fees", "tuition"]}
  - column:tuition: 23790 ⟵ “Tuition                                                                 $23,790.00   $47,580.00”
  - column:tuition: 600 ⟵ “college tuition and educational fees. Awardees also receive a book allowance of $600 per semester and”
  - column:mandatory_fees: 9000 ⟵ “fees (Type 2); (2) up to $9,000 towards tuition and fees (Type 3); and up to $3,000 towards tuition and”
  - column:tuition: 36000 ⟵ “The Tuition Exchange. The 2018-19 beneﬁt is $36,000 or full tuition, whichever is less. Tuition”
  - column:tuition: 25000 ⟵ “Tuition charges for the Master of Arts in Urban Education program is set at $25,000. This tuition”
### `ec01d2c52b865650` Rhodes College — costs 2026-27 [new] (ambiguous_year_labels)
- source: https://www.rhodes.edu/sites/default/files/2017-18_Complete_Rhodes_College_Catalog.pdf (sha256 aa07b7ecc59d)
- issues: ambiguous_year_labels, column_alignment_uncertain
- checks: {"columns": 1, "components": ["tuition", "tuition_and_fees"]}
  - column:tuition: 23097 ⟵ “Tuition                                                                         $23,097.00     $46,194.00”
  - column:tuition: 600 ⟵ “tuition and educational fees. Awardees also receive a book allowance of $600 per semester and a stipend”
  - column:tuition_and_fees: 9000 ⟵ “towards tuition and fees (Type 2); and (3) up to $9,000 per year towards tuition and fees (Type 7). Students not”
### `fe1a61a8159df717` Rhodes College — costs 2026-27 [new] (ambiguous_year_labels)
- source: https://www.rhodes.edu/sites/default/files/2017-18_Complete_Rhodes_College_Catalog.pdf (sha256 aa07b7ecc59d)
- issues: ambiguous_year_labels, column_alignment_uncertain
- checks: {"columns": 1, "components": ["tuition"]}
  - column:tuition: 46194 ⟵ “Tuition                                                                         $23,097.00     $46,194.00”
### `error-pipeline.extractors.costs-86b95d1254c6347e4cd4.json.gz` Roane State Community College — None  [?] ()
- source: https://www.roanestate.edu/?12415-CARES-Act-Emergency-Assistance-for-Students
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-893d0c1916a36489704f.json.gz` Roane State Community College — None  [?] ()
- source: https://www.roanestate.edu/catalog/?id=591
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-895a0f1ff2535212a915.json.gz` Roane State Community College — None  [?] ()
- source: https://www.roanestate.edu/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-d159554393becd74ba84.json.gz` Roane State Community College — None  [?] ()
- source: https://www.roanestate.edu/catalog/?id=188
- issues: extractor_error:ValueError: max() iterable argument is empty
### `af65bc05cbf74aa2` Roane State Community College — costs 2004-05 [new] (labeled_in_title)
- source: https://www.roanestate.edu/catalog/previousCatalogs/2004-2005.pdf (sha256 ba8e3e017e7b)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, stale_year_label:2004-05
- checks: {"columns": 2, "components": ["books_supplies", "mandatory_fees", "personal", "total", "tuition"], "components_reconcile": false}
  - column:total: 15025 ⟵ “total $15,025. (This figure is an estimate and is subject to change.) Additional”
  - column:tuition: 78 ⟵ “tuition fee rate for the 2003-2004 academic year is $78 per semester hour, not to ex-”
  - column:mandatory_fees: 5 ⟵ “fee of $5.”
  - column:mandatory_fees: 15 ⟵ “Technology Fee (Refundable). A fee of $15 per credit hour not to exceed $112.50 per”
  - column:mandatory_fees: 75 ⟵ “fee per semester hour, up to a maximum of $75. This rate applies to tuition fees, tech-”
  - column:books_supplies: 250 ⟵ “supplies is $250-$400 per semester. The College Bookstore will buy back used books”
  - column:personal: 10 ⟵ “Personal checks may be cashed for any amount up to $10 for students and up to $20”
  - column:mandatory_fees: 5 ⟵ “fee of $5.”
  - column:mandatory_fees: 112.5 ⟵ “Technology Fee (Refundable). A fee of $15 per credit hour not to exceed $112.50 per”
  - column:books_supplies: 400 ⟵ “supplies is $250-$400 per semester. The College Bookstore will buy back used books”
  - column:personal: 20 ⟵ “Personal checks may be cashed for any amount up to $10 for students and up to $20”
### `error-pipeline.extractors.costs-0bed690a79e9a219b195.json.gz` Southern Adventist University — None  [?] ()
- source: https://www.southern.edu/undergrad/finances/financial-assistance.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-1fad4ed07eb73c0c96f7.json.gz` Southern Adventist University — None  [?] ()
- source: https://admissions.e.southern.edu/register/?id=864f7a03-804c-4166-bed1-e9bf4088a9d4&sys:app:non_degree_type=5fcd3f99-bf60-4ede-80c3-ee97bcbe1ecc&utm_source=apply_page&utm_campaign=nd_redirect&utm_medium=form
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-31af54b88a3e86288774.json.gz` Southern Adventist University — None  [?] ()
- source: https://admissions.e.southern.edu/register/non-degree-app
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-4d190811cb129d1b55db.json.gz` Southern Adventist University — None  [?] ()
- source: https://www.southern.edu/contact.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-f52a6485f57b8a3d6fb4.json.gz` Southern Adventist University — None  [?] ()
- source: https://www.southern.edu/undergrad/admissions/transfer-students.html
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-fb91c59b1d025daa7a22.json.gz` Southern Adventist University — None  [?] ()
- source: https://admissions.e.southern.edu/account/register?r=https%3a%2f%2fadmissions.e.southern.edu%2fapply%2f
- issues: extractor_error:ValueError: max() iterable argument is empty
### `4ca6ba8fe38e8b16` Southern Adventist University — costs 2026-27 [new] (ambiguous_year_labels)
- source: https://www.southern.edu/undergrad/finances/tuition.html (sha256 cc56cec75708)
- issues: ambiguous_year_labels, arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components": ["mandatory_fees", "total", "tuition"], "components_reconcile": false}
  - on_campus:tuition: 28900 ⟵ “Undergraduate Tuition (12-16 hours) | $28,900 | $28,900”
  - on_campus:mandatory_fees: 1500 ⟵ “General Fee | $1,500 | $1,500”
  - on_campus:total: 40300 ⟵ “Total | $40,300 | $30,400”
  - column:tuition: 28900 ⟵ “Undergraduate Tuition (12-16 hours) | $28,900 | $28,900”
  - column:mandatory_fees: 1500 ⟵ “General Fee | $1,500 | $1,500”
  - column:total: 30400 ⟵ “Total | $40,300 | $30,400”
### `error-pipeline.extractors.costs-24e42127f89a4c6f666e.json.gz` Southwest Tennessee Community College — None  [?] ()
- source: https://www.southwest.tn.edu/financial-aid/sap-form.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-2abcf9a116b361fc44b6.json.gz` Southwest Tennessee Community College — None  [?] ()
- source: https://catalog.southwest.tn.edu/index.php?catoid=38
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-31250caa150e730ef457.json.gz` Southwest Tennessee Community College — None  [?] ()
- source: https://catalog.southwest.tn.edu/index.php?catoid=36
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-441869028f1b4bd7376b.json.gz` Southwest Tennessee Community College — None  [?] ()
- source: https://www.southwest.tn.edu/admissions/hours.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-713be68212f055940744.json.gz` Southwest Tennessee Community College — None  [?] ()
- source: http://catalog.southwest.tn.edu/index.php?catoid=24
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-841622d29a1371e0698a.json.gz` Southwest Tennessee Community College — None  [?] ()
- source: https://catalog.southwest.tn.edu/index.php?catoid=41
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-8cb1a66bd83391956a0c.json.gz` Southwest Tennessee Community College — None  [?] ()
- source: https://catalog.southwest.tn.edu/index.php?catoid=33
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-c4548e8e570e1df7a1ab.json.gz` Southwest Tennessee Community College — None  [?] ()
- source: https://www.southwest.tn.edu/admissions/contact-us.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-ffbcbc491c2b3a279196.json.gz` Southwest Tennessee Community College — None  [?] ()
- source: http://catalog.southwest.tn.edu/index.php?catoid=29
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-5c02b1ea0208b55b71f3.json.gz` Tennessee State University — None  [?] ()
- source: https://www.tnstate.edu/admin/scholarships/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-99437f6f1d1ff55ef69d.json.gz` Tennessee State University — None  [?] ()
- source: https://www.tnstate.edu/admissions/financial-aid/federal-stafford/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-f0c3890510acc8e4f36f.json.gz` Tennessee State University — None  [?] ()
- source: https://www.tnstate.edu/admissions/financial-aid/financial-aid-forms/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-123d8c21a4d6efe41ddd.json.gz` Tennessee Technological University — None  [?] ()
- source: https://www.tntech.edu/scholarships/transfer-grad-timeline.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-81555f265edf19f0e21f.json.gz` Tennessee Wesleyan University — None  [?] ()
- source: https://www.tnwesleyan.edu/academics/executive-programs/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-e78e6a8ea0d0b0c467da.json.gz` Tennessee Wesleyan University — None  [?] ()
- source: http://tnwesleyan.edu/admissions/undergraduate-admissions/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `4018d479e61d59a5` Tennessee Wesleyan University — costs 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/ (sha256 ac7fd1406789)
- issues: ambiguous_year_labels, arrangement_unlabeled
- checks: {"columns": 3, "components": ["mandatory_fees", "tuition"]}
  - column:tuition: 30590 ⟵ “Tuition | $30,590 | $31,820 | $15,910”
  - column:mandatory_fees: 1460 ⟵ “Fees | $1,460 | $1,560 | $780”
  - column:tuition: 31820 ⟵ “Tuition | $30,590 | $31,820 | $15,910”
  - column:mandatory_fees: 1560 ⟵ “Fees | $1,460 | $1,560 | $780”
  - column:tuition: 15910 ⟵ “Tuition | $30,590 | $31,820 | $15,910”
  - column:mandatory_fees: 780 ⟵ “Fees | $1,460 | $1,560 | $780”
### `04d51c17ba459224` The University of Tennessee Southern — costs 2026-27 [new] (labeled_in_title)
- source: https://utsouthern.edu/wp-content/uploads/2026/09/2026-2027-Standard-cost-of-attendance-002.docx.pdf (sha256 690886045400)
- issues: residency_unknown
- checks: {"columns": 1, "components": ["books_supplies", "food", "housing", "loan_fees", "mandatory_fees", "personal", "total", "transportation", "tuition"], "components_reconcile": true}
  - column:tuition: 10228 ⟵ “Tuition                             $10,228.00”
  - column:mandatory_fees: 1374 ⟵ “Required Fees                        $1,374.00”
  - column:housing: 5877 ⟵ “Housing                              $5,877.00”
  - column:food: 4867 ⟵ “Meals                                $4,867.00”
  - column:books_supplies: 1500 ⟵ “Books & Supplies                     $1,500.00”
  - column:loan_fees: 95 ⟵ “Loan Fees                                $95.00”
  - column:personal: 2000 ⟵ “Personal Expenses                    $2,000.00”
  - column:transportation: 2500 ⟵ “Transportation                       $2,500.00”
  - column:total: 28441 ⟵ “Grand Total                                       $28,441.00”
  - column:tuition: 10228 ⟵ “Tuition                 $10,228.00”
  - column:mandatory_fees: 1374 ⟵ “Required Fees            $1,374.00”
  - column:food: 4867 ⟵ “Food/Meals               $4,867.00”
  - column:books_supplies: 1500 ⟵ “Books & Supplies         $1,500.00”
  - column:loan_fees: 95 ⟵ “Loan Fees                  $95.00”
  - column:personal: 2000 ⟵ “Personal Expenses        $2,000.00”
  - column:transportation: 2500 ⟵ “Transportation           $2,500.00”
  - column:total: 31924 ⟵ “Grand Total                          $31,924.00”
  - column:tuition: 10228 ⟵ “Tuition                 $10,228.00”
  - column:mandatory_fees: 1374 ⟵ “Required Fees            $1,374.00”
  - column:food: 4867 ⟵ “Food/Meals               $4,867.00”
  - column:books_supplies: 1500 ⟵ “Books & Supplies         $1,500.00”
  - column:loan_fees: 95 ⟵ “Loan Fees                  $95.00”
  - column:personal: 2000 ⟵ “Personal Expenses        $2,000.00”
  - column:transportation: 2500 ⟵ “Transportation           $2,500.00”
  - column:total: 25684 ⟵ “Grand Total                          $25,684.00”
  - … 8 more rows
### `error-pipeline.extractors.costs-089beaaa668ff0cd81fc.json.gz` The University of Tennessee-Chattanooga — None  [?] ()
- source: https://www.utc.edu/about/admissions/future-transfer-students
- issues: extractor_error:ValueError: max() iterable argument is empty
### `364a46a55349ba98` The University of Tennessee-Chattanooga — costs 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/estimating-your-cost (sha256 9a6e46775b1e)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "components": ["books_supplies", "food", "housing", "personal", "transportation", "tuition_and_fees"]}
- change student_population: `full_time_undergraduate` → `undergraduate`
  - with_parents_or_family:tuition_and_fees: 11084 ⟵ “Enrollment Fees | $11,084 | $11,084 | $11,084 | $11,789”
  - with_parents_or_family:books_supplies: 1400 ⟵ “Books, Course Materials, Supplies and Equipment | $1,400 | $1,400 | $1,400 | $1,200”
  - with_parents_or_family:housing: 2600 ⟵ “Housing | $2,600 | $8,800 | $9,204 | $9,450”
  - with_parents_or_family:food: 4552 ⟵ “Food | $4,552 | $4,552 | $4,552 | $4,552”
  - with_parents_or_family:transportation: 2300 ⟵ “Transportation | $2,300 | $2,300 | $2,300 | $3,200”
  - with_parents_or_family:personal: 1800 ⟵ “Miscellaneous Personal Expenses | $1,800 | $1,800 | $1,800 | $2,600”
  - off_campus_not_with_family:tuition_and_fees: 11084 ⟵ “Enrollment Fees | $11,084 | $11,084 | $11,084 | $11,789”
  - off_campus_not_with_family:books_supplies: 1400 ⟵ “Books, Course Materials, Supplies and Equipment | $1,400 | $1,400 | $1,400 | $1,200”
  - off_campus_not_with_family:housing: 8800 ⟵ “Housing | $2,600 | $8,800 | $9,204 | $9,450”
  - off_campus_not_with_family:food: 4552 ⟵ “Food | $4,552 | $4,552 | $4,552 | $4,552”
  - off_campus_not_with_family:transportation: 2300 ⟵ “Transportation | $2,300 | $2,300 | $2,300 | $3,200”
  - off_campus_not_with_family:personal: 1800 ⟵ “Miscellaneous Personal Expenses | $1,800 | $1,800 | $1,800 | $2,600”
  - on_campus:tuition_and_fees: 11084 ⟵ “Enrollment Fees | $11,084 | $11,084 | $11,084 | $11,789”
  - on_campus:books_supplies: 1400 ⟵ “Books, Course Materials, Supplies and Equipment | $1,400 | $1,400 | $1,400 | $1,200”
  - on_campus:housing: 9204 ⟵ “Housing | $2,600 | $8,800 | $9,204 | $9,450”
  - on_campus:food: 4552 ⟵ “Food | $4,552 | $4,552 | $4,552 | $4,552”
  - on_campus:transportation: 2300 ⟵ “Transportation | $2,300 | $2,300 | $2,300 | $3,200”
  - on_campus:personal: 1800 ⟵ “Miscellaneous Personal Expenses | $1,800 | $1,800 | $1,800 | $2,600”
  - column:tuition_and_fees: 11789 ⟵ “Enrollment Fees | $11,084 | $11,084 | $11,084 | $11,789”
  - column:books_supplies: 1200 ⟵ “Books, Course Materials, Supplies and Equipment | $1,400 | $1,400 | $1,400 | $1,200”
  - column:housing: 9450 ⟵ “Housing | $2,600 | $8,800 | $9,204 | $9,450”
  - column:food: 4552 ⟵ “Food | $4,552 | $4,552 | $4,552 | $4,552”
  - column:transportation: 3200 ⟵ “Transportation | $2,300 | $2,300 | $2,300 | $3,200”
  - column:personal: 2600 ⟵ “Miscellaneous Personal Expenses | $1,800 | $1,800 | $1,800 | $2,600”
### `error-pipeline.extractors.costs-3783cbacd87a284bb106.json.gz` The University of Tennessee-Knoxville — None  [?] ()
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-87a984c1972410b9ff94.json.gz` The University of Tennessee-Knoxville — None  [?] ()
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/next-chapter-scholarship-next-chapter-scholar-of-the-year-award/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-ea37b91e6e74320ed7dc.json.gz` The University of Tennessee-Knoxville — None  [?] ()
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/tri-star-scholarships/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `143b9cc54c51ce3f` The University of Tennessee-Knoxville — admissions_metrics 2025-26 [same] (labeled_in_source)
- source: https://irsa.utk.edu/wp-content/uploads/sites/5/2026/06/CDS_2025-26_C_.pdf (sha256 432ea71922ec)
- issues: admits_multiple_numbers, enrolled_multiple_numbers, c1_totals_incomplete
- checks: {"fields": ["act_25", "act_50", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - sat_composite_25..75: [1280, 1330, 1380] ⟵ “SAT Composite                                1280            1330          1380”
  - sat_math_25..75: [630, 660, 700] ⟵ “SAT Math                                      630            660           700”
  - act_25..75: [26, 29, 31] ⟵ “ACT Composite                                 26              29            31”
### `1bf2d293934fe7f1` The University of Tennessee-Knoxville — costs 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/billing-payments/cost-of-attending-ut-undergraduate-student/ (sha256 f81e0fa4d378)
- issues: components_do_not_reconcile, conflicts_with_verified_record
- checks: {"columns": 1, "components": ["food", "total", "tuition"], "components_reconcile": false}
- change cost_period: `fall_and_spring_semesters` → `academic_year`
- change student_population: `full_time_undergraduate` → `undergraduate`
  - column:tuition: 11560 ⟵ “Tuition | $11,560 | $31,672”
  - column:food: 5166 ⟵ “Food | $5,166 | $5,166”
  - column:total: 36994 ⟵ “Total, with on-campus housing(Direct costs plus estimated indirect costs) | $36,994 | $57,448”
### `5b64d3c07b56d4aa` The University of Tennessee-Knoxville — costs 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/billing-payments/cost-of-attending-ut-undergraduate-student/ (sha256 f81e0fa4d378)
- issues: components_do_not_reconcile, conflicts_with_verified_record
- checks: {"columns": 1, "components": ["food", "total", "tuition"], "components_reconcile": false}
- change cost_period: `fall_and_spring_semesters` → `academic_year`
- change student_population: `full_time_undergraduate` → `undergraduate`
  - column:tuition: 31672 ⟵ “Tuition | $11,560 | $31,672”
  - column:food: 5166 ⟵ “Food | $5,166 | $5,166”
  - column:total: 57448 ⟵ “Total, with on-campus housing(Direct costs plus estimated indirect costs) | $36,994 | $57,448”
### `error-pipeline.extractors.costs-11f5a2e468cf16f91501.json.gz` The University of the South — None  [?] ()
- source: https://new.sewanee.edu/admission-aid/application-process/application-review/transfer-applicants/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-24bbed224247f7a8bae2.json.gz` The University of the South — None  [?] ()
- source: https://new.sewanee.edu/admission-aid/application-process/application-review/homeschool-applicants/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-9461ebf8b665e65dd1a0.json.gz` The University of the South — None  [?] ()
- source: https://new.sewanee.edu/admission-aid/your-domain/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-bdc0a8b2cfb3a8e02956.json.gz` The University of the South — None  [?] ()
- source: https://new.sewanee.edu/admission-aid/application-process/application-review/international-applicant/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-02397d6d5a574bbede39.json.gz` Trevecca Nazarene University — None  [?] ()
- source: https://www.trevecca.edu/admissions/admissions-information
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-29226870ff98b47d96b6.json.gz` Trevecca Nazarene University — None  [?] ()
- source: https://www.trevecca.edu/admissions/becoming-a-student
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-6424787ddc2edf0dabb7.json.gz` Trevecca Nazarene University — None  [?] ()
- source: https://www.trevecca.edu/admissions/tennessee-transfer-pathway
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-b4fa606769d87af90f24.json.gz` Trevecca Nazarene University — None  [?] ()
- source: https://www.trevecca.edu/admissions/dual-enrollment
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-d1219a55fc35359fe4fa.json.gz` Trevecca Nazarene University — None  [?] ()
- source: https://www.trevecca.edu/admissions/financial-aid/scholarships
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-03a86b218b8a7b15c6bc.json.gz` Tusculum University — None  [?] ()
- source: https://catalog.tusculum.edu/index.php?amp;print
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-639dfdb7d5fa0138adcf.json.gz` Tusculum University — None  [?] ()
- source: http://catalog.tusculum.edu
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-40a7cbe0feb527691361.json.gz` Union University — None  [?] ()
- source: https://www.uu.edu/admissions/financial-aid/policies-practices/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `675f66c4667dd161` Union University — costs 2026-27 [new] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/ (sha256 0f756388efd5)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components": ["books_supplies", "food", "housing", "loan_fees", "mandatory_fees", "personal", "total", "transportation", "tuition"], "components_reconcile": false}
  - column:tuition: 41170 ⟵ “Tuition | $41,170 | 12-16 hours per semester as a block rate”
  - column:mandatory_fees: 1520 ⟵ “Mandatory Fees | $1,520 | This does not include a one-time $185 Orientation fee for first-time Union students.”
  - column:housing: 10800 ⟵ “Housing | $10,800 | This is the cost for The Quads Apartments; your costs could differ depending on your housing option.”
  - column:food: 6636 ⟵ “Food/Meals | $6,636 | This is the 285 meal-plan; your costs could differ depending on your meal-plan selection.”
  - column:total: 60126 ⟵ “Total Direct Costs | $60,126 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:books_supplies: 750 ⟵ “Books, Course Materials, Supplies, and Equipment | $750 | This is an estimate using the Buster Book Bundle; your costs could differ depending on how you purchase your books”
  - column:transportation: 3316 ⟵ “Transportation | $3,316 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:loan_fees: 130 ⟵ “Loan Fees | $130 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFP for more information.”
  - column:personal: 11154 ⟵ “Personal Expenses | $11,154 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:total: 15350 ⟵ “Total Indirect Costs | $15,350 | ”
  - column:total: 75476 ⟵ “Total COA | $75,476 | Total allowable Cost of Attendance for on-campus, traditional undergraduate students (prior to application of any financial aid eligibility)”
### `error-pipeline.extractors.costs-0b5caf45ee21711ce3a6.json.gz` University of Memphis — None  [?] ()
- source: https://www.memphis.edu/admissions/basics/residency.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-25e016dd73ee73fffc00.json.gz` University of Memphis — None  [?] ()
- source: https://www.memphis.edu/admissions/connect/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-41639f4d74f4454f3bc0.json.gz` University of Memphis — None  [?] ()
- source: https://www.memphis.edu/admissions/basics/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-ba18a1575cbd697d81f9.json.gz` University of Memphis — None  [?] ()
- source: https://www.memphis.edu/admissions/basics/index.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-c758ce888b855734db32.json.gz` University of Memphis — None  [?] ()
- source: https://catalog.memphis.edu/?catoid=40
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-ca5b22fc9ae35423a756.json.gz` University of Memphis — None  [?] ()
- source: https://catalog.memphis.edu/?catoid=39
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-fae27737be686d61532b.json.gz` University of Memphis — None  [?] ()
- source: https://www.memphis.edu/admissions/connect/index.php
- issues: extractor_error:ValueError: max() iterable argument is empty
### `017d786f1ba748bf` Vanderbilt University — costs 2026-27 [new] (labeled_in_source)
- source: https://admissions.vanderbilt.edu/affordability/ (sha256 a80f3d79c819)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components": ["books_supplies", "food", "housing", "personal", "total", "tuition"], "components_reconcile": false}
  - column:tuition: 69822 ⟵ “Tuition | $69,822”
  - column:housing: 15170 ⟵ “Housing | $15,170”
  - column:food: 8520 ⟵ “Food | $8,520”
  - column:total: 96896 ⟵ “Total Direct Cost of Attendance – Mandatory | $96,896”
  - column:books_supplies: 1100 ⟵ “Books, Course Materials, Supplies, & Equipment Allowance | $1,100”
  - column:personal: 1998 ⟵ “Personal Expenses Allowance | $1,998”
  - column:total: 3098 ⟵ “Total Indirect Costs – Discretionary/Elective | $3,098”
### `error-pipeline.extractors.costs-2b55647b6d37c2dc459a.json.gz` Walters State Community College — None  [?] ()
- source: https://ws.edu/cost-aid/tuition-fees/index.aspx
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-6a0ec8df95499a8c1b1b.json.gz` Walters State Community College — None  [?] ()
- source: https://ws.edu/admissions/prior-learning/dual-credit/index.aspx
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-97933273664a9ee77a61.json.gz` Walters State Community College — None  [?] ()
- source: https://www.ws.edu/financial-aid/
- issues: extractor_error:ValueError: max() iterable argument is empty
### `error-pipeline.extractors.costs-ac416d761ab487b13b21.json.gz` Walters State Community College — None  [?] ()
- source: https://ws.edu/admissions/prior-learning/exams/dsst/index.aspx
- issues: extractor_error:ValueError: max() iterable argument is empty
### `1f62a6f08d546737` Williamson Christian College — costs 2022-23 [new] (labeled_in_source)
- source: https://williamsoncc.edu/wp-content/uploads/2016/08/FINAL-WC-Catalog-2022-23-1.pdf (sha256 94492ca9e196)
- issues: stale_year_label:2022-23
- checks: {"columns": 1, "components": ["mandatory_fees", "transportation", "tuition", "tuition_and_fees"]}
  - column:tuition: 825 ⟵ “Monthly Tuition                                             $825”
  - column:mandatory_fees: 220 ⟵ “Technology Fee: $220                           • Populi Learning Management system”
  - column:tuition_and_fees: 25 ⟵ “Dual Enrollment Fees (includes             $25 per course”
  - column:tuition: 625 ⟵ “Tuition                                 $625 per credit hour”
  - column:transportation: 5500 ⟵ “Travel                                  $5,500 international travel”
  - column:mandatory_fees: 220 ⟵ “Technology Fee                          $220 (per term)”
  - column:tuition: 625 ⟵ “Tuition Rate                                 $625 per semester credit hour”
  - column:mandatory_fees: 220 ⟵ “Technology Fee: $220                         One Time Fee due at initial registration”
### `3220a1482dd6ef0a` Williamson Christian College — costs 2026-27 [new] (labeled_in_source)
- source: https://williamsoncc.edu/wp-content/uploads/2026/07/2026-27-Catalog_Final.pdf (sha256 6ef64cd5e6ea)
- issues: column_alignment_uncertain
- checks: {"columns": 1, "components": ["mandatory_fees", "transportation", "tuition"]}
  - column:mandatory_fees: 230 ⟵ “Technology Fee: $230                          • Populi Learning Management System”
  - column:tuition: 775 ⟵ “Tuition                                           $775 per credit hour (MAOL)”
  - column:transportation: 7000 ⟵ “Travel – International (required)                 $7,000 (WC reserves the right to charge up to $7,000 should”
  - column:mandatory_fees: 230 ⟵ “Technology Fee                                 $230”
  - column:tuition: 775 ⟵ “Tuition Rate                                 $775 per semester credit hour”
  - column:mandatory_fees: 230 ⟵ “Technology Fee                             $230”
### `3735b7c998fc83eb` Williamson Christian College — costs 2014-15 [new] (labeled_in_title)
- source: https://williamsoncc.edu/wp-content/uploads/2018/11/Catalog-2018-19-draft.pdf (sha256 67d72daa5b73)
- issues: stale_year_label:2014-15
- checks: {"columns": 1, "components": ["mandatory_fees", "personal", "transportation", "tuition"]}
  - column:tuition: 825 ⟵ “Monthly Tuition                                         $825”
  - column:mandatory_fees: 200 ⟵ “Technology Fee: $200                            • Populi Learning Management system”
  - column:tuition: 200 ⟵ “Tuition Rate                                 $200 per semester credit hour”
  - column:mandatory_fees: 200 ⟵ “Technology Fee: $200                         Each enrollment term”
  - column:tuition: 550 ⟵ “Tuition Rate                                 $550 per semester credit hour”
  - column:mandatory_fees: 200 ⟵ “Technology Fee: $200                         One Time Fee due at initial registration”
  - column:tuition: 550 ⟵ “Tuition                                       $550 per credit hour”
  - column:transportation: 1800 ⟵ “Travel                                        $1,800 national travel”
  - column:mandatory_fees: 200 ⟵ “Technology Fee                                $200 (per term)”
  - column:personal: 1500 ⟵ “Not-for-credit MAOL class (personal           $1,500 per class”
### `37c8262ca79b66c4` Williamson Christian College — costs 2025-26 [new] (labeled_in_source)
- source: https://williamsoncc.edu/wp-content/uploads/2025/09/8.18.25-Updated-Catalog-Final-for-Publication.pdf (sha256 ee8b52f9009e)
- issues: column_alignment_uncertain, stale_year_label:2025-26
- checks: {"columns": 1, "components": ["transportation"]}
  - column:transportation: 6200 ⟵ “Travel – International (required)                 $6,200 (WC reserves the right to charge up to $6,200 should”
### `3c05693609de34c6` Williamson Christian College — costs 2026-27 [new] (labeled_in_source)
- source: https://williamsoncc.edu/wp-content/uploads/2026/07/2026-27-Catalog_Final.pdf (sha256 6ef64cd5e6ea)
- issues: column_alignment_uncertain
- checks: {"columns": 1, "components": ["transportation"]}
  - column:transportation: 7000 ⟵ “Travel – International (required)                 $7,000 (WC reserves the right to charge up to $7,000 should”
### `43a0111e46878cdf` Williamson Christian College — costs 2025-26 [new] (labeled_in_source)
- source: https://williamsoncc.edu/wp-content/uploads/2025/09/8.18.25-Updated-Catalog-Final-for-Publication.pdf (sha256 ee8b52f9009e)
- issues: column_alignment_uncertain, stale_year_label:2025-26
- checks: {"columns": 1, "components": ["mandatory_fees", "transportation", "tuition"]}
  - column:mandatory_fees: 220 ⟵ “Technology Fee: $220                          • Populi Learning Management System”
  - column:tuition: 750 ⟵ “Tuition                                           $750 per credit hour (MAOL)”
  - column:transportation: 6200 ⟵ “Travel – International (required)                 $6,200 (WC reserves the right to charge up to $6,200 should”
  - column:mandatory_fees: 225 ⟵ “Technology Fee                                 $225”
  - column:tuition: 750 ⟵ “Tuition Rate                                $750 per semester credit hour”
  - column:mandatory_fees: 225 ⟵ “Technology Fee                            $225”
### `56101a1a9ae58e16` Williamson Christian College — costs 2023-24 [changed] (labeled_in_source)
- source: https://williamsoncc.edu/wp-content/uploads/2016/08/Revised-WC-Catalog-2023-24-FINAL.pdf (sha256 bf86bbbd57b3)
- issues: stale_year_label:2023-24, conflicts_with_verified_record
- checks: {"columns": 1, "components": ["mandatory_fees", "transportation", "tuition", "tuition_and_fees"]}
- change tuition: `13560` → `655`
- change mandatory_fees: `1450` → `220`
- change student_population: `full_time_first_time_undergraduate` → `undergraduate`
  - column:mandatory_fees: 220 ⟵ “Technology Fee: $220                              • Populi Learning Management system”
  - column:tuition_and_fees: 25 ⟵ “Dual Enrollment Fees (includes technology,   $25 per course”
  - column:tuition: 655 ⟵ “Tuition                                 $655 per credit hour”
  - column:transportation: 5500 ⟵ “Travel                                  $5,500 international travel”
  - column:mandatory_fees: 220 ⟵ “Technology Fee                          $220 (per term)”
  - column:tuition: 655 ⟵ “Tuition Rate                                   $655 per semester credit hour”
  - column:mandatory_fees: 220 ⟵ “Technology Fee: $220                           One Time Fee due at initial registration”
### `5c59bfc917f4f425` Williamson Christian College — costs 2019-20 [new] (labeled_in_source)
- source: https://williamsoncc.edu/wp-content/uploads/2019/11/Catalog-2019-20-4.pdf (sha256 9e6f19cab16d)
- issues: stale_year_label:2019-20
- checks: {"columns": 1, "components": ["mandatory_fees", "personal", "transportation", "tuition"]}
  - column:tuition: 825 ⟵ “Monthly Tuition                                         $825”
  - column:mandatory_fees: 200 ⟵ “Technology Fee: $200                           • Populi Learning Management system”
  - column:tuition: 200 ⟵ “Tuition Rate                                 $200 per semester credit hour”
  - column:mandatory_fees: 200 ⟵ “Technology Fee: $200                         Each enrollment term”
  - column:tuition: 575 ⟵ “Tuition Rate                                 $575 per semester credit hour”
  - column:mandatory_fees: 200 ⟵ “Technology Fee: $200                         One Time Fee due at initial registration”
  - column:tuition: 575 ⟵ “Tuition                                               $575 per credit hour”
  - column:transportation: 2000 ⟵ “Travel                                                $2,000 national travel”
  - column:mandatory_fees: 200 ⟵ “Technology Fee                                        $200 (per term)”
  - column:personal: 1500 ⟵ “Not-for-credit MAOL class (personal enrichment)       $1,500 per class”
  - column:tuition: 4800 ⟵ “towards tuition only, after federal aid is awarded, up to $4800 per term. The scholarship requires a”
### `7fe3283588ff343a` Williamson Christian College — costs 2021-22 [new] (labeled_in_source)
- source: https://williamsoncc.edu/wp-content/uploads/2016/08/WC-Catalog-2021-22-FINAL-1.pdf (sha256 4df0e8f6b1c9)
- issues: stale_year_label:2021-22
- checks: {"columns": 1, "components": ["mandatory_fees", "transportation", "tuition", "tuition_and_fees"]}
  - column:mandatory_fees: 200 ⟵ “Technology Fee: $200                           • Populi Learning Management system”
  - column:tuition_and_fees: 25 ⟵ “Dual Enrollment Fees (includes             $25 per course”
  - column:tuition: 595 ⟵ “Tuition                                 $595 per credit hour (MAOL & MATS)”
  - column:transportation: 5500 ⟵ “Travel                                  $5,500 international travel”
  - column:mandatory_fees: 200 ⟵ “Technology Fee                          $200 (per term)”
  - column:tuition: 595 ⟵ “Tuition Rate                                 $595 per semester credit hour”
  - column:mandatory_fees: 200 ⟵ “Technology Fee: $200                         One Time Fee due at initial registration”
### `bb94362eab5dca35` Williamson Christian College — costs 2024-25 [new] (labeled_in_title)
- source: https://williamsoncc.edu/wp-content/uploads/2025/02/Catalog-24-25-revised-02.10.25.pdf (sha256 a637ed9464c8)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components": ["mandatory_fees", "transportation", "tuition", "tuition_and_fees"]}
  - column:mandatory_fees: 220 ⟵ “Technology Fee: $220                                • Populi Learning Management system”
  - column:tuition_and_fees: 25 ⟵ “Dual Enrollment Fees (includes technology,     $25 per course”
  - column:tuition: 710 ⟵ “Tuition                                 $710 per credit hour”
  - column:transportation: 5500 ⟵ “Travel                                  $5,500 international travel”
  - column:mandatory_fees: 220 ⟵ “Technology Fee                          $220 (per term)”
  - column:tuition: 710 ⟵ “Tuition Rate                                $710 per semester credit hour”
  - column:mandatory_fees: 220 ⟵ “Technology Fee                              $220 (per term)”

## Re-verification of existing records (38)

- all_values_found_year_labeled: data/institutions/utc/academic_programs/2026-27.json ["academic_programs", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/academic_programs/2026-27.json ["academic_programs", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/academic_programs/2026-27.json ["academic_programs", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs"}] year=2026-27
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "sap_appeal"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "scholarship_retention_appeal"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "merit_reconsideration"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "competing_offer_review"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "need_based_special_circumstances"}]
- all_values_found_year_not_labeled: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Chancellor's Scholarship"}] year=2025-26
- all_values_found_year_not_labeled: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Provost's Scholarship"}] year=2025-26
- all_values_found_year_not_labeled: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Mocs Scholarship"}] year=2025-26
- all_values_found_year_not_labeled: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Academic Service Scholars Program"}]
- values_not_found_verbatim: data/institutions/utc/costs/2026-27.json ["costs", "ipeds-221740", null, "2026-27", {"residency": "in_state"}] missing=['on_campus_food_housing', 'on_campus_other_expenses'] year=2026-27
- values_not_found_verbatim: data/institutions/utc/costs/2026-27.json ["costs", "ipeds-221740", null, "2026-27", {"residency": "out_of_state"}] missing=['on_campus_food_housing', 'on_campus_other_expenses'] year=2026-27
- all_values_found_year_not_labeled: data/institutions/utc/credit_policies/2026-27.json ["credit_policies", "ipeds-221740", null, "2026-27", {"policy_kind": "AP"}]
- all_values_found_year_not_labeled: data/institutions/utc/credit_policies/2026-27.json ["credit_policies", "ipeds-221740", null, "2026-27", {"policy_kind": "CLEP"}]
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "program-total"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "upper-division-hours"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "residency-hours"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "gen-ed-hours"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "major-hours"}] year=2026-27
- nothing_to_check: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "four-year-plan"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "program-total"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "upper-division-hours"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "residency-hours"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "gen-ed-hours"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "major-hours"}] year=2026-27
- nothing_to_check: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "four-year-plan"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "program-total"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "upper-division-hours"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "residency-hours"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "gen-ed-hours"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "major-hours"}] year=2026-27
- nothing_to_check: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "four-year-plan"}] year=2026-27
- values_not_found_verbatim: data/institutions/utc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-221740", null, "2026-27", {}] missing=['residency_requirement_credits']
- nothing_to_check: data/institutions/utk/awards/2026-27.json ["awards", "utk", null, "2026-27", {"award_name": "Manning Scholars"}] year=2026-27
- all_values_found_year_labeled: data/institutions/utk/awards/2026-27.json ["awards", "utk", null, "2026-27", {"award_name": "Out-of-State Volunteer Scholarship"}] year=2026-27
- source_not_fetched: data/institutions/utk/transfer_policies/2026-27.json ["transfer_policies", "utk", null, "2026-27", {}]

## Leads: official pages found with no extracted record

- American Baptist College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements, aid_appeals
- Austin Peay State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Baptist Health Sciences University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Belmont University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, degree_requirements
- Bethel University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Bryan College-Dayton: admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Carson-Newman University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Christian Brothers University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Columbia State Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Dyersburg State Community College: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- East Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Fisk University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Freed-Hardeman University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Herzing University-Nashville: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, degree_requirements
- Jackson State Community College: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- John A Gupton College: tuition_fees, cost_of_attendance, admissions_tests, degree_requirements, aid_appeals
- Johnson University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- King University: admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements, aid_appeals
- Lane College: admissions_tests, common_data_set, merit_scholarships, transfer_credit, degree_requirements, aid_appeals
- Le Moyne-Owen College: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit
- Lee University: merit_scholarships, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Lincoln Memorial University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Lipscomb University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Maryville College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, aid_appeals
- Mid-South Christian College: admissions_tests, merit_scholarships, transfer_credit
- Middle Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Motlow State Community College: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Nashville State Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Northeast State Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Remington College-Memphis Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- Remington College-Nashville Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- Rhodes College: admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Roane State Community College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Southern Adventist University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Southwest Tennessee Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Tennessee Technological University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Tennessee Wesleyan University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- The University of Tennessee Southern: admissions_tests, merit_scholarships, dual_enrollment, degree_requirements, aid_appeals
- The University of Tennessee-Chattanooga: admissions_tests, merit_scholarships, dual_enrollment
- The University of the South: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Trevecca Nazarene University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Tusculum University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Union University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- University of Memphis: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Vanderbilt University: admissions_tests, merit_scholarships, transfer_credit, degree_requirements, aid_appeals
- Visible Music College: cost_of_attendance, admissions_tests, merit_scholarships
- Walters State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Welch College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- William R Moore College of Technology: tuition_fees, admissions_tests, merit_scholarships
- Williamson Christian College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
