# Review queue — OR (2026-27)

Pages fetched: 1528; failures: 91. Candidates: 228 (46 without issues, 182 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 4 | 15 | 18 | 1 | 3 |
| cost_of_attendance | 0 | 0 | 2 | 10 | 24 | 2 | 3 |
| admissions_tests | 0 | 0 | 0 | 1 | 32 | 5 | 3 |
| common_data_set | 0 | 0 | 0 | 1 | 1 | 36 | 3 |
| merit_scholarships | 0 | 0 | 3 | 1 | 32 | 2 | 3 |
| ap_credit | 0 | 0 | 3 | 1 | 15 | 19 | 3 |
| clep_credit | 0 | 0 | 2 | 2 | 9 | 25 | 3 |
| ib_credit | 0 | 0 | 2 | 2 | 5 | 29 | 3 |
| dual_enrollment | 0 | 0 | 0 | 0 | 21 | 17 | 3 |
| transfer_credit | 0 | 0 | 5 | 2 | 30 | 1 | 3 |
| statewide_articulation | 0 | 0 | 0 | 0 | 12 | 26 | 3 |
| residency | 0 | 0 | 0 | 0 | 19 | 19 | 3 |
| degree_requirements | 0 | 0 | 0 | 0 | 29 | 9 | 3 |
| aid_appeals | 0 | 0 | 0 | 22 | 6 | 10 | 3 |

## Ready for review (46)

### `0b5120edecaba06d` Blue Mountain Community College — costs 2026-27 [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/tuition-fees/ (sha256 c922497ee779)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition & Required Fees: 9936 ⟵ “Tuition & Required Fees | $7,211 | $7,211 | $9,936”
  - column:Books & Supplies: 1105 ⟵ “Books & Supplies | $1,105 | $1,105 | $1,105”
  - column:Living Expenses: 10800 ⟵ “Living Expenses | $6,450 | $10,800 | $10,800”
  - column:Misc./Personal Expenses: 1200 ⟵ “Misc./Personal Expenses | $1,200 | $1,200 | $1,200”
  - column:Transportation: 1974 ⟵ “Transportation | $1,974 | $1,974 | $1,974”
  - column:TOTAL: 25015 ⟵ “TOTAL | $17,940 | $22,290 | $25,015”
### `0787c596375bacd5` Bushnell University — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://bushnell.edu/wp-content/uploads/2026/06/Bushnell-University-AP-Transfer-Guide.pdf (sha256 7959fa09e4e4)
- checks: {"distinct_exams": 38, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3+]:  ⟵ “2-D Art & Design                                         3+       DMG 200                                                     3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design                                         3+       DMG 200                                                     3”
  - equivalencies[AP-ART-HISTORY|3+]:  ⟵ “Art History                                              3+       Pick 2 of History, Social Science, or Diversity Gen Ed      6”
  - equivalencies[AP-DRAWING|3+]:  ⟵ “Drawing                                                  3+       General Elective                                            3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                                              3       MUS 100                                                     2”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition*                           3       WR 121                                                      3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition*                        3+       WR 121 & ENG 201                                            6”
  - equivalencies[AP-RESEARCH|3+]:  ⟵ “Research                                                 3+       General Elective                                            3”
  - equivalencies[AP-SEMINAR|3+]:  ⟵ “Seminar                                                  3+       General Elective                                            3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3+]:  ⟵ “Computer Science A                                       3+       SFTE Elective                                               3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3+]:  ⟵ “Computer Science Principles                              3+       SFTE Elective                                               3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                                               3       Math Gen Ed                                                 3”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                                               3       MATH 251                                                    4”
  - equivalencies[AP-PRECALCULUS|3+]:  ⟵ “Precalculus                                              3+       MATH 130                                                    3”
  - equivalencies[AP-STATISTICS|3+]:  ⟵ “Statistics                                               3+       MATH 315                                                    3”
  - equivalencies[AP-BIOLOGY|3+]:  ⟵ “Biology                                                  3+       BIOL 111 & 111L & 112 & 112L                                8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                                 3       CHEM 121 & 121L                                             5”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “Environmental Science                                    3+       General Elective                                            3”
  - equivalencies[AP-PHYSICS-1|3+]:  ⟵ “Physics 1                                                3+       PHYS 201 & 201L                                             5”
  - equivalencies[AP-PHYSICS-2|3+]:  ⟵ “Physics 2                                                3+       PHYS 202 & 202L                                             4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3+]:  ⟵ “Physics C: Mechanics                                     3+       PHYS 201 & 201L                                             5”
  - equivalencies[AP-MACROECONOMICS|3+]:  ⟵ “Macroeconomics                         3+   ECON 202                                                  3”
  - equivalencies[AP-MICROECONOMICS|3+]:  ⟵ “Microeconomics                         3+   ECON 201                                                  3”
  - equivalencies[AP-PSYCHOLOGY|3+]:  ⟵ “Psychology                             3+   PSY 200                                                   3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies               3    History Gen Ed                                            3”
  - … 13 more rows
### `m7609dc4b3306dc5` Bushnell University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://bushnell.edu/admissions/undergraduate-admissions/transfer-students/accepted-credit/ (sha256 1486072bcfe3)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “Transferrable courses must be at the 100-level or above, taken at a regionally accredited college (up to 30 transfer credits from a non-regionally accredited college will be accepted), and with a grade of C- or higher.”
  - min_grade: C- ⟵ “College and University Credit Transferrable courses must be at the 100-level or above, taken at a regionally accredited college (up to 30 transfer credits from a non-regionally accredited college may be accepted), and completed with a grade of C- or higher.”
### `3b1f280bf2ac51f7` Clackamas Community College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- checks: {"thresholds": null}
  - award_amount_text: $192.00 ⟵ “Transportation | $575.00 | $192.00”
### `c6a265c312b7465d` Clackamas Community College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- checks: {"thresholds": null}
  - award_amount_text: $200.00 ⟵ “Books/Supplies | $600.00 | $200.00”
### `e26fdfa2c26a4d01` Clackamas Community College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- checks: {"thresholds": null}
  - award_amount_text: $150.00 ⟵ “Personal expenses (entertainment, clothes, etc.) | $450.00 | $150.00”
### `6aca751e6f5687a1` George Fox University — costs 2026-27 [new] (labeled_in_source)
- source: https://www.georgefox.edu/college-admissions/scholarships/index.html (sha256 a5cfbc3144c9)
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition (12 to 18 credits): 45154 ⟵ “Tuition (12 to 18 credits) | $45,154”
  - column:Housing and Meals: 15080 ⟵ “Housing and Meals | $15,080”
  - column:Standard Fees: 720 ⟵ “Standard Fees | $720”
  - column:Total Tuition and Costs: 60954 ⟵ “Total Tuition and Costs | $60,954”
### `0965a34d739c4fb3` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 2 credits ⟵ “2 credits | 2 credits”
### `141bcd921120c743` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 9 credits ⟵ “13 credits | 9 credits”
### `1973ec7cfe4ad34f` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 7 credits ⟵ “10 credits | 7 credits”
### `65350132b22db686` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 3 credits ⟵ “4 credits | 3 credits”
### `7072ff732935a9bb` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 13 credits ⟵ “19 credits | 13 credits”
### `74717ef54f81d700` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 8 credits ⟵ “12 credits | 8 credits”
### `7f3d3bcee4a5f631` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 2 credits ⟵ “3 credits | 2 credits”
### `865f9af25563df4a` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 11 credits ⟵ “16 credits | 11 credits”
### `ae00a78e98920b50` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 4 credits ⟵ “5 credits | 4 credits”
### `b28bfb159299a788` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 8 credits ⟵ “11 credits | 8 credits”
### `b4a3a4fb9e29c0e6` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 12 credits ⟵ “17 credits | 12 credits”
### `b8eafc6af618fc6c` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 5 credits ⟵ “7 credits | 5 credits”
### `bc29496c453c52ee` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 1 credit ⟵ “1 credit | 1 credit”
### `c0bb6b706a8c2e8c` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 10 credits ⟵ “15 credits | 10 credits”
### `c50871f75a989055` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 6 credits ⟵ “8 credits | 6 credits”
### `cced199f9ec1d974` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 4 credits ⟵ “6 credits | 4 credits”
### `d5fa3643f1ccd0e5` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 14 credits ⟵ “20 credits | 14 credits”
### `dffedc557809be52` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 10 credits ⟵ “14 credits | 10 credits”
### `ec15ee125e1ef64c` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 12 credits ⟵ “18 credits | 12 credits”
### `f2558d85126724b8` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 6 credits ⟵ “9 credits | 6 credits”
### `4e8fb2d090c981d9` Lewis & Clark College — costs 2026-27 [new] (labeled_in_source)
- source: https://www.lclark.edu/offices/account_services/student_statements/costs/college/ (sha256 3136274029e7)
- checks: {"columns": 1, "rows": 13}
  - column:Tuition*: 70658 ⟵ “Tuition* | $35,329 | $70,658”
  - column:Student Body Fee*: 360 ⟵ “Student Body Fee* | $180 | $360”
  - column:Health Insurance: 5655 ⟵ “Health Insurance | $2827.50 | $5,655”
  - column:Room (on campus): 9578 ⟵ “Room (on campus) | $4,789 | $9,578”
  - column:Single Room Premium: 10930 ⟵ “Single Room Premium | $5,465 | $10,930”
  - column:Apartment Premium: 12310 ⟵ “Apartment Premium | $6,155 | $12,310”
  - column:Board (14 Meals plus $200 Flex): 7314 ⟵ “Board (14 Meals plus $200 Flex) | $3,657 | $7,314”
  - column:Board (100 Block plus $250 Flex)*****: 4976 ⟵ “Board (100 Block plus $250 Flex)***** | $2,488 | $4,976”
  - column:Flex Only******: 1708 ⟵ “Flex Only****** | $854 | $1,708”
  - column:Health and Wellness Fee: 74 ⟵ “Health and Wellness Fee | $37 | $74”
  - column:New Student Orientation Fee (Fall incoming first-year & transfer students only): 215 ⟵ “New Student Orientation Fee (Fall incoming first-year & transfer students only) |  | $215”
  - column:Green Power Fee: 20 ⟵ “Green Power Fee | $20 (Fall only) | $20”
  - column:Media Fee: 70 ⟵ “Media Fee | $35 | $70”
### `a17767e3fd493258` Linn-Benton Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.linnbenton.edu/future-students/explore-lb/transfer-center/osu.php (sha256 521849cbccde)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “If it turns out that you are not yet eligible, it's easy to get started at LBCC and then apply to DPP after completing: 24 graded transferable credits WR 121Z with a grade of C or higher MTH 105Z or MTH 111Z with a grade of C or better Earning a minimum GPA of 2.25 Apply Now This application will require the regular OSU application fee (currently $65).”
  - min_grade: C ⟵ “If it turns out that you are not yet eligible, it's easy to get started at LBCC and then apply to DPP after completing: 24 graded transferable credits WR 121Z with a grade of C or higher MTH 105Z or MTH 111Z with a grade of C or better Earning a minimum GPA of 2.25 Apply Now This application will require the regular OSU application fee (currently $65).”
  - min_grade: C ⟵ “For transfer students, OSU is looking at the following criteria: Completed 24 transferable, college-level credits Completed WR 121Z with a grade of C or better Completed MTH 105Z or MTH 111Z with a grade of C or better* Earn a GPA of 2.25 or higher *While completion of college-level math is strongly recommended, transfer students may be admitted to OSU without math if they have met all other requi”
### `f176cfad3a94cb1d` Oregon Coast Community College — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://oregoncoast.edu/cpl/ (sha256 4f160ecefa3f)
- checks: {"distinct_exams": 15, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | PS 201 | 4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introduction to Sociology | 50 | SOC 204, 205 | 8”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|60]:  ⟵ “Principles of Macroeconomics | 60 | EC 202 | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|60]:  ⟵ “Principles of Microeconomics | 60 | EC 201 | 4”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | HST 101 | 4”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | HST 103 | 4”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50 x 2]:  ⟵ “Western Civilization I and II | 50 x 2 | HST 101, 102, 103 | 12”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 2xx | 8”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG 2xx | 8”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | WR 121z | 4”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MTH 251 | 4”
  - equivalencies[CLEP-CALCULUS|64]:  ⟵ “Calculus | 64 | MTH 251, 252 | 8”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MTH 105z | 4”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MTH 111z | 4”
  - equivalencies[CLEP-PRECALCULUS|61]:  ⟵ “Precalculus | 61 | MTH 111z, 112z | 8”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language: Levels 1 & 2 | 50 | FR 1xx | 12”
  - equivalencies[CLEP-FRENCH-LANGUAGE|60]:  ⟵ “French Language: Levels 1 & 2 | 60 | FR 2xx | 12”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language: Levels 1 & 2 | 50 | GER 1xx | 12”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language: Levels 1 & 2 | 60 | GER 2xx | 12”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language: Levels 1 & 2 | 50 | SPA 1xx | 12”
  - equivalencies[CLEP-SPANISH-LANGUAGE|60]:  ⟵ “Spanish Language: Levels 1 & 2 | 60 | SPA 2xx | 12”
### `ef798fcc8b74a783` Oregon State University-Cascades Campus — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://osucascades.edu/admissions/apply-now/transfer-students/transfer-degrees (sha256 aa07494afbae)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “For transfer students graduating from high school in 1997 and thereafter, OSU has a second language admission requirement: two terms of a college-level second language with an average grade of C- or above, OR two years of the same high school level second language with an average grade of C- or above OR satisfactory performance on an approved second language assessment of proficiency.”
  - min_grade: C- ⟵ “For transfer students graduating from high school in 1997 and thereafter, OSU has a second language admission requirement: two terms of a college-level second language with an average grade of C- or above, OR two years of the same high school level second language with an average grade of C- or above OR satisfactory performance on an approved second language assessment of proficiency.”
### `124b556d6ef31063` Portland State University — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://www.pdx.edu/admissions/international-baccalaureate (sha256 71dae76fdf81)
- checks: {"distinct_exams": 25, "equivalencies": 62, "rows_without_score": 0}
  - equivalencies[IB-FILM|4,5,6,7]:  ⟵ “Film | 4,5,6,7 | 4 | FILM LD | 8 | FILM LD”
  - equivalencies[IB-MUSIC|4,5,6,7]:  ⟵ “Music | 4,5,6,7 | 4 | MUS LD | 8 | MUS LD”
  - equivalencies[IB-THEATRE|4,5,6,7]:  ⟵ “Theatre | 4,5,6,7 | 4 | TA LD | 4 | TA LD”
  - equivalencies[IB-VISUAL-ARTS|4,5,6,7]:  ⟵ “Visual Arts | 4,5,6,7 | 4 | ART LD | 4 | ART 131, LD”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4,5,6,7]:  ⟵ “Business and Management | 4,5,6,7 | 4 | BA LD | 4 | BA 101Z”
  - equivalencies[IB-ECONOMICS|4,5,6,7]:  ⟵ “Economics | 4,5,6,7 | 4 | EC 200 | 8 | EC 201Z, 202Z”
  - equivalencies[IB-GEOGRAPHY|4,5,6,7]:  ⟵ “Geography | 4,5,6,7 | 4 | GEOG LD | 8 | GEOG 230, LD”
  - equivalencies[IB-GLOBAL-POLITICS|4]:  ⟵ “Global Politics | 4 | 4 | PS LD | 4 | PS LD”
  - equivalencies[IB-GLOBAL-POLITICS|5,6,7]:  ⟵ “Global Politics | 5,6,7 | 4 | PS LD | 7 | PS 205, LD”
  - equivalencies[IB-HISTORY-SL|4,5,6,7]:  ⟵ “History SL | 4,5,6,7 | 4 | HST LD | --- | ---”
  - equivalencies[IB-HISTORY-HL|4,5,6,7]:  ⟵ “History: Africa & Middle East HL | 4,5,6,7 | --- | --- | 12 | HST LD”
  - equivalencies[IB-PHILOSOPHY|4,5,6,7]:  ⟵ “Philosophy | 4,5,6,7 | 4 | PHL LD | 8 | PHL 201, LD”
  - equivalencies[IB-PSYCHOLOGY|4,5,6,7]:  ⟵ “Psychology | 4,5,6,7 | 4 | PSY LD | 8 | PSY 201Z, 202Z”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4,5,6,7]:  ⟵ “Social and Cultural Anthropology | 4,5,6,7 | 4 | ANTH LD | 4 | ANTH LD”
  - equivalencies[IB-LATIN|4,5,6,7]:  ⟵ “Classical Languages: Latin | 4,5,6,7 | 4 | LAT 103 | 16 | LAT 101, 102, 103, 201”
  - equivalencies[IB-LATIN|Language AB Initio- Any language]:  ⟵ “Classical Languages: Latin | Language AB Initio- Any language | No Second Language credits are awarded for Ab initio IB Language exams”
  - equivalencies[IB-FRENCH|4,5]:  ⟵ “French B | 4,5 | 4 | FR 203 | 12 | 4 FR UD*, 8 FR LD”
  - equivalencies[IB-FRENCH|6,7]:  ⟵ “French B | 6,7 | 4 | FR UD* | 12 | 8 FR UD*, 4 FR LD”
  - equivalencies[IB-GERMAN|4,5]:  ⟵ “German B | 4,5 | 4 | GER 203 | 12 | 4 GER UD*, 8 GER LD”
  - equivalencies[IB-GERMAN|6,7]:  ⟵ “German B | 6,7 | 4 | GER UD* | 12 | 8 GER UD*, 4 GER LD”
  - equivalencies[IB-SPANISH|4,5]:  ⟵ “Spanish B | 4,5 | 4 | SPAN 203 | 12 | 4 SPAN UD*, 8 SPAN LD”
  - equivalencies[IB-SPANISH|6,7]:  ⟵ “Spanish B | 6,7 | 4 | SPAN UD* | 12 | 8 SPAN UD*, 4 SPAN LD”
  - equivalencies[IB-FRENCH|4,5,6,7]:  ⟵ “Literature & Performance (Spanish or French) | 4,5,6,7 | 4 | SPAN UD or FR UD | --- | ---”
  - equivalencies[IB-COMPUTER-SCIENCE|4,5,6,7]:  ⟵ “Computer Science | 4,5,6,7 | 4 | CS 161 [CS LD prior to 202502] | 8 | CS 160, 161[CS LD prior to 202502]”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4,5,6,7]:  ⟵ “Mathematics: Analysis & Approaches | 4,5,6,7 | 4 | MTH 251Z | 12 | MTH 251Z, 252Z, LD”
  - … 37 more rows
### `4abd864163ee951d` Portland State University — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://www.pdx.edu/admissions/advanced-placement (sha256 808842f2f04f)
- checks: {"distinct_exams": 27, "equivalencies": 53, "rows_without_score": 0}
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French, German, Italian, or Spanish | 3 | 12 | A score of 3 in French, German, Italian or Spanish confers 12 credits for the first-year sequence (101, 102, 103).”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French, German, Italian, or Spanish | 4 | 12 | A score of 4 in each of these exams confers 12 credits for the second-year sequence (201, 202, 203).”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French, German, Italian, or Spanish | 5 | 12 | A score of 5 in each of these exams confers 12 upper-division credits per exam as follows: French: FR 301, 302, 303; German: GER 301, 302, UD; Italian IT UD; Spanish: SPAN 301, 302, 303.”
  - equivalencies[AP-LATIN|3+]:  ⟵ “Latin | 3+ | 12 | A score of 3 or higher in Latin confers 12 credits for the second-year Latin sequence (201, 202, 203).”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese or Japanese | 3 | 15 | A score of 3 in Chinese or Japanese confers 15 credits for the first-year sequence (101, 102, 103).”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese or Japanese | 4 | 15 | A score of 4 in Chinese or Japanese confers 15 credits for the second-year sequence (201, 202, 203).”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese or Japanese | 5 | 15 | A score of 5 in Chinese or Japanese confers 15 upper-division elective credits.”
  - equivalencies[AP-BIOLOGY|4+]:  ⟵ “Biology | 4+ | 12 | BI LD”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 4 | MTH 251”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 4 | 8 | MTH 251, 252”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 8 | MTH 251, 252”
  - equivalencies[AP-CALCULUS-BC|4+]:  ⟵ “Calculus BC | 4+ | 12 | MTH 251, 252, 253”
  - equivalencies[AP-CHEMISTRY|4+]:  ⟵ “Chemistry | 4+ | 15 | CH 221, 222, 223, 227, 228, 229”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4+]:  ⟵ “Computer Science A | 4+ | 4 | CS LD”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4+]:  ⟵ “Computer Science Principles | 4+ | 4 | CS LD”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “Environmental Science | 3+ | 4 | ESM LD”
  - equivalencies[AP-PHYSICS-1|4+]:  ⟵ “Physics 1: Algebra-based | 4+ | 5 | PH 201, 214”
  - equivalencies[AP-PHYSICS-2|4+]:  ⟵ “Physics 2: Algebra-based | 4+ | 5 | PH 202, 215”
  - equivalencies[AP-PHYSICS-1|4+ (on both exams)]:  ⟵ “Physics 1: Algebra-based AND Physics 2: Algebra-based | 4+ (on both exams) | 15 | PH 201, 202, 203, 214, 215, 216”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4+]:  ⟵ “Physics C - Electricity & Magnetism | 4+ | 4 | PH 222, 215”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4+]:  ⟵ “Physics C - Mechanics | 4+ | 4 | PH 221, 214”
  - equivalencies[AP-STATISTICS|4+]:  ⟵ “Statistics | 4+ | 4 | STAT 243”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Language & Composition | 3+ | 4 | WR 121”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition | 3+ | 4 | ENG100”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French, German, Italian, or Spanish | 3 | 12 | A score of 3 in French, German, Italian or Spanish confers 12 credits for the first year sequence (101, 102, 103).”
  - … 28 more rows
### `a587ab661fc0621d` Portland State University — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://www.pdx.edu/admissions/college-level-exam-program (sha256 6dc69bba543e)
- checks: {"distinct_exams": 22, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 9 Arts and Letters (AL) elective credits | 50 | Closed to students with more than 90 credits”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French | 12 | 50 | Awards FR 101, 102, 103”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French | 12 | 59 | Awards FR 201, 202, 203”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German | 12 | 50 | Awards GER 101, 102, 103”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German | 12 | 60 | Awards GER 201, 202, 203”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language | 12 | 50 | Awards SPAN 101, 102, 103”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language | 12 | 63 | Awards SPAN 201, 202, 203”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing | 12 | 50 | Awards SPAN 101, 102, 103”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|65]:  ⟵ “Spanish with Writing | 12 | 65 | Awards SPAN 201, 202, 203”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I | 2; Maximum 4 total from any combination of CLP History exam | 50 | Awards History lower division elective”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II | 2; Maximum 4 total from any combination of CLP History exam | 50 | Awards History lower division elective”
  - equivalencies[CLEP-BIOLOGY|49]:  ⟵ “Biology | 0 | 49 | Waives BI 221Z, 222Z, 223Z”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 8 | 50 | Awards MTH 251Z, 252Z”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 4 | 50 | Awards MTH 111Z”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-Calculus | 4 | 50 | Awards MTH 112Z”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 4 | 50 | Awards Math lower division credit (starting 7/2001)”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 8 | 50 | Awards PS 101, 102”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 8 | 50 | Awards PSY 201Z, 202Z”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Introductory Microeconomics | 4 | 50 | Awards EC 201Z”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Introductory Macroeconomics | 4 | 50 | Awards EC 202Z”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology | 0 | 50 | Waives prerequisite for upper division courses”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 4 | 50 | Awards BA 211Z”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 4 | 50 | Awards Business lower division elective credit”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 4 | 50 | Awards Business lower division elective credit”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 4 | 50 | Awards Business lower division elective credit”
  - … 1 more rows
### `m368a2bcb9a86893` Portland State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.pdx.edu/admissions/international/transfer (sha256 4b87ef3d539c)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “If you are transferring from a U.S. institution of higher education you must complete Writing 121 or its equivalent with a grade of C- or better.”
  - min_grade: C- ⟵ “Completion of 30 or more transferable college quarter credits (20 semester credits) Cumulative grade point average (GPA) of at least 2.25, or 2.00 if you present a transferable associate degree or an Oregon Transfer Module (OTM) Completion of WR121 or equivalent with a grade of C- or better.”
### `76ea581610cbf920` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount $250 ⟵ “Scholarship Douglas County Gay Archives Scholarship | Amount $250 | Application Deadline Ongoing | Download Application”
### `807ed881d7ad7216` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount $500 ⟵ “Scholarship Vera Shukle Nursing Scholarship | Amount $500 | Application Deadline Ongoing | Download Application”
### `8b6f8665b8c91e6b` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount Varies ⟵ “Scholarship Addictions.com College Scholarship | Amount Varies | Application Deadline July 31 | Apply”
### `d3ce144f9619ea09` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount Up to $2,000 ⟵ “Scholarship Southern Oregon Viticulture & Enology Scholarship | Amount Up to $2,000 | Application Deadline Ongoing | Download Application”
### `e4f45f95082c06d2` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount Varies ⟵ “Scholarship Ford Family Foundation | Amount Varies | Application Deadline TBA | Apply”
### `fc3db0f09e9790ba` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount Up to $5,000 ⟵ “Scholarship Ford Auto Tech Scholarship | Amount Up to $5,000 | Application Deadline Ongoing | Apply”
### `0b42aba4066789ec` University of Portland — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://ww1.up.edu/admissions/files/ib-equivalents-2025.pdf (sha256 cca432bbd5f9)
- checks: {"distinct_exams": 19, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|5]:  ⟵ “Biology HL                                                         5           3           100 Level Biology Elective          Science & Problem Solving”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|3]:  ⟵ “Business & Management HL                                       5, 6 or 7       3           100 Level General Elective                     n/a”
  - equivalencies[IB-CHEMISTRY-HL|5]:  ⟵ “Chemistry HL                                                       5           3          100 Level Chemistry Elective         Science & Problem Solving”
  - equivalencies[IB-ECONOMICS-HL|5]:  ⟵ “Economics HL                                                       5           3                     ECN 120                    Science & Problem Solving”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|5]:  ⟵ “English A: Language or English A: Language & Literature HL         5           3                     ENG 112                        Literacy & Dialogue”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French, German, Spanish Language A & B                            4            3                        101                                 n/a”
  - equivalencies[IB-FILM-HL|3]:  ⟵ “Film HL                                                        5, 6 or 7       3                      FA 108                      Aesthetics & Creativity”
  - equivalencies[IB-GEOGRAPHY-HL|3]:  ⟵ “Geography HL                                                   5, 6 or 7       3            100 Level General Elective                      n/a”
  - equivalencies[IB-GLOBAL-POLITICS-HL|3]:  ⟵ “Global Politics HL                                             5, 6 or 7       3                     POL 205                 Global & Historical Consciousness”
  - equivalencies[IB-HISTORY-HL|5]:  ⟵ “History: Americas HL                                               5           3            200 Level History Elective                      n/a”
  - equivalencies[IB-HISTORY-HL|3]:  ⟵ “History: Asia/Oceana HL                                        5, 6 or 7       3            200 Level History Elective       Global & Historical Consciousness”
  - equivalencies[IB-HISTORY-HL|5]:  ⟵ “History: Europe HL                                                 5           3                     HST 221                 Global & Historical Consciousness”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|5]:  ⟵ “Mathematics: Analysis and Approaches HL                            5           3                     MTH 121                    Science & Problem Solving”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|5]:  ⟵ “Mathematics: Applications and Interpretations HL                   5           3                     MTH 161                    Science & Problem Solving”
  - equivalencies[IB-MUSIC-HL|3]:  ⟵ “Music HL                                                       5, 6 or 7       3                      FA 108                      Aesthetics & Creativity”
  - equivalencies[IB-PHILOSOPHY-HL|3]:  ⟵ “Philosophy HL                                                  5, 6, or 7      3                     PHL 150                        Literacy & Dialogue”
  - equivalencies[IB-PHYSICS-HL|5]:  ⟵ “Physics HL                                                         5           4                  PHY 201 & 271                 Science & Problem Solving”
  - equivalencies[IB-PSYCHOLOGY-HL|3]:  ⟵ “Psychology HL                                                  5, 6 or 7       3                     PSY 101                    Science & Problem Solving”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|3]:  ⟵ “Social Anthropology HL                                         5, 6 or 7       3            100 Level General Elective       Global & Historical Consciousness”
  - equivalencies[IB-THEATRE-HL|3]:  ⟵ “Theatre Arts HL                                                 5, 6, 7        3                      FA 108                      Aesthetics & Creativity”
  - equivalencies[IB-VISUAL-ARTS-HL|3]:  ⟵ “Visual Arts HL                                                  5, 6, 7        3                      FA 107                      Aesthetics & Creativity”
### `dcd88a4f12619fc4` University of Portland — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://ww1.up.edu/admissions/files/ap-equivalents-2025.pdf (sha256 96b0706f01ae)
- checks: {"distinct_exams": 35, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4 or 5]:  ⟵ “African American Studies                   4 or 5      3             100 Level Ethnic Studies Elective             Diversity & the Common Good”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History                                4 or 5      3                           FA 107                              Aesthetics & Creativity”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                                      4         4                 100 Level Biology Elective                  Science & Problem Solving”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “Calculus AB                                4 or 5      4                         MTH 201                             Science & Problem Solving”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                                  4         4                         MTH 201                             Science & Problem Solving”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “Calculus BC Subgrade                       4 or 5      4                         MTH 201                             Science & Problem Solving”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                                    4         4               100 Level Chemistry Elective                  Science & Problem Solving”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language and Culture                 4         6                      CHN 101 & 102                                      n/a”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4 or 5]:  ⟵ “Computer Science A                         4 or 5      4                       CS 203 & 273                                      n/a”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4 or 5]:  ⟵ “Computer Science Principles                4 or 5      3           200 Level Computer Science Elective                           n/a”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4 or 5]:  ⟵ “English Language and Composition           4 or 5      3                         ENG 107                                         n/a”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4 or 5]:  ⟵ “English Literature and Composition         4 or 5      3                         ENG 112                                 Literacy & Dialogue”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4 or 5]:  ⟵ “Environmental Science                      4 or 5      3                         ENV 182                             Science & Problem Solving”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History                             4         3                         HST 221                          Global & Historical Consciousness”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture                  4         6                      FRN 101 & 102                                      n/a”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Literature                            5         3                 300 Level English Elective               Global & Historical Consciousness”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language and Culture                  4         6                      GRM 101 & 102                                      n/a”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4 or 5]:  ⟵ “Human Geography                            4 or 5      3               100 Level Sociology Elective               Global & Historical Consciousness”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|5]:  ⟵ “(Japanese, Italian)                          5        12                   101, 102, 201 & 202                    Global & Historical Consciousness”
  - equivalencies[AP-LATIN|4 or 5]:  ⟵ “Latin Literature                           4 or 5      3           100 Level Foreign Language Elective                           n/a”
  - equivalencies[AP-LATIN|4 or 5]:  ⟵ “Latin: Vergil                              4 or 5      3           200 Level Foreign Language Elective                           n/a”
  - equivalencies[AP-MACROECONOMICS|4 or 5]:  ⟵ “Macroeconomics                             4 or 5      3                         ECN 120                             Science & Problem Solving”
  - equivalencies[AP-MICROECONOMICS|4 or 5]:  ⟵ “Microeconomics                             4 or 5      3                         ECN 121                             Science & Problem Solving”
  - equivalencies[AP-MUSIC-THEORY|4 or 5]:  ⟵ “Music Theory                               4 or 5      3                         MUS 101                                         n/a”
  - equivalencies[AP-PHYSICS-1|4 or 5]:  ⟵ “Physics 1                                  4 or 5      4                      PHY 201 & 271                          Science & Problem Solving”
  - … 13 more rows
### `846ac8544bb2d4ab` University of Portland — transfer_policies 2027-28 [new] (labeled_in_source)
- source: https://www.up.edu/admissions-aid/transfer-students.html (sha256 a7cb2832f14b)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “University of Portland will evaluate your college coursework for transfer credit if it’s 100-level or above and completed with a grade of C or higher.”
### `1f5f2a40a7bfa757` Western Oregon University — costs 2026-27 [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 a9e06917b93d)
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 30600 ⟵ “Tuition | $30,600 | $30,600 | $30,600”
  - on_campus:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - on_campus:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - on_campus:Housing: 7597 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - on_campus:Food: 5387 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - on_campus:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - on_campus:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - on_campus:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - on_campus:Total: 50904 ⟵ “Total | $50,904 | $53,942 | $42,662”
  - off_campus_not_with_family:Tuition: 30600 ⟵ “Tuition | $30,600 | $30,600 | $30,600”
  - off_campus_not_with_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - off_campus_not_with_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - off_campus_not_with_family:Housing: 7805 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - off_campus_not_with_family:Food: 8217 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - off_campus_not_with_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - off_campus_not_with_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - off_campus_not_with_family:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - off_campus_not_with_family:Total: 53942 ⟵ “Total | $50,904 | $53,942 | $42,662”
  - with_parents_or_family:Tuition: 30600 ⟵ “Tuition | $30,600 | $30,600 | $30,600”
  - with_parents_or_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - with_parents_or_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - with_parents_or_family:Housing: 2501 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - with_parents_or_family:Food: 2241 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - with_parents_or_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - with_parents_or_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - … 2 more rows
### `20cf43bd6250e5ad` Western Oregon University — costs 2026-27 [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 a9e06917b93d)
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 10350 ⟵ “Tuition | $10,350 | $10,350 | $10,350”
  - on_campus:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - on_campus:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - on_campus:Housing: 7597 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - on_campus:Food: 5387 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - on_campus:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - on_campus:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - on_campus:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - on_campus:Total: 30654 ⟵ “Total | $30,654 | $33,692 | $22,412”
  - off_campus_not_with_family:Tuition: 10350 ⟵ “Tuition | $10,350 | $10,350 | $10,350”
  - off_campus_not_with_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - off_campus_not_with_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - off_campus_not_with_family:Housing: 7805 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - off_campus_not_with_family:Food: 8217 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - off_campus_not_with_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - off_campus_not_with_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - off_campus_not_with_family:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - off_campus_not_with_family:Total: 33692 ⟵ “Total | $30,654 | $33,692 | $22,412”
  - with_parents_or_family:Tuition: 10350 ⟵ “Tuition | $10,350 | $10,350 | $10,350”
  - with_parents_or_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - with_parents_or_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - with_parents_or_family:Housing: 2501 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - with_parents_or_family:Food: 2241 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - with_parents_or_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - with_parents_or_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - … 2 more rows

## Exceptions (182)

### `042480e03d3c21b5` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf (sha256 a67795237f61)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 3, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Cochairs Rachel Knighten (LCC) and Patricia Gimenez-Eguibar (WOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participa”
  - statements.effective: 3 ⟵ “Beginning Fall 2027, only SPA/SPA/SPAN 101Z, 102Z, and 103Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `151fedb5806c8ca9` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf (sha256 22dd3a949d6e)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Physiology I                                                                                          1 Cochairs Lindsay Biga (OSU) and Jonathan Christie (Chemeketa) **715-025-0070 institutions that do not offer an equivalent of this course are not required ”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `1662bf2e57f07e44` state-OR — state_policies 2027-28 [new] (labeled_in_heading)
- source: https://www.oregon.gov/highered/about/transfer/Pages/common-course-numbering.aspx (sha256 93ac57493011)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Pages/transfer-maps.aspx
- checks: {"exceptions": 1, "guarantees": 1, "requirements": 12}
  - statements.requirements: 12 ⟵ “SB 233 requires the HECC to establish, by rule, a CCN system and system of transfer and articulation, based on recommendations from the Transfer Council.”
  - statements.guarantees: 1 ⟵ “When transferring to an Oregon public college or university, CCN courses will be accepted as if they were taken at the institution students transfer to (that is, the receiving institution).”
  - statements.exceptions: 1 ⟵ “However, we continue to post the schedule of upcoming CCN meetings and video links on the page linked to below.Attend a Transfer Council public meeting or a CCN Subcommittee meeting.”
### `18b1d1169a423c8d` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf (sha256 17e08e38bba8)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf
- checks: {"effective": 3, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Cochairs Rachel Knighten (LCC) and Patricia Gimenez-Eguibar (WOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participa”
  - statements.effective: 3 ⟵ “Beginning Fall 2027, only SPA/SPN/SPAN 101Z, 102Z, and 103Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `1c4a76809143c17c` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf (sha256 e58e0082ee0c)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 3, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Cochairs Rachel Knighten (LCC) and Patricia Gimenez-Eguibar (WOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participa”
  - statements.effective: 3 ⟵ “Beginning Fall 2027, only SPA/SPN/SPAN 101Z, 102Z, and 103Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `1e776707314ba412` state-OR — state_policies 2024-25 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/MTM-Guide-2024-2025.pdf (sha256 4ebf220e2e81)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"effective": 4, "exceptions": 4, "guarantees": 9, "requirements": 51}
  - statements.requirements: 51 ⟵ “All participating community colleges must submit a student facing document, as part of the Transfer Council required MTM documentation; 2.”
  - statements.exceptions: 4 ⟵ “In practice, most faculty subcommittees have 14 or 16 members; however, when university participation in a major is fewer than six universities, the composition of the subcommittee will be smaller.”
  - statements.guarantees: 9 ⟵ “V1. 2024                                   MTM Faculty Subcommittee Guide                                                           16 MTM CURRICULUM ARTICULATION POLICY (CAP) FRAMEWORK A Major Transfer Map (MTM) creates a statewide curriculum agreement that guarantees a student following the MTM wi”
  - statements.effective: 4 ⟵ “The Core Transfer Map (CTM) embedded in the Course Development Template ensures that students will complete at least 30 general education credits, and all universities have updated the CTM crosswalk illustrating how courses from the AAOT approved list will apply towards their general education It is”
### `204307c89d7302f8` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf (sha256 27ca61cd7045)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation Government                                                                                                1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `28817cf273640312` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf (sha256 846504ec6fac)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 2, "exceptions": 2, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Professions                                                                                                1 Cochairs Kenneth Friedrich (PCC) and Christopher Walsh (EOU) **715-025-0070 institutions that do not offer an equivalent of this course are not requi”
  - statements.effective: 2 ⟵ “Annual CCN Chemistry Subcommittee check-ins beginning in Winter 2028 to gather qualitative and/or quantitative data on faculty and student experiences, make requests for institutional and statewide data, discuss challenges, and raise concerns to review the transfer effectiveness of the CCN CH/CHE/CH”
  - statements.exceptions: 2 ⟵ “The scope of annual check-ins will focus on the statewide and collaborative nature of this work to facilitate inclusive and equitable conversations and to identify potential issues that may require future modifications of the CCN recommendations or framework every third year, starting in 2031. 2.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | October 23, 2025 outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-0”
### `28eeb7fa6ada44f9` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf (sha256 61c78404c2d1)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 1, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN History Subcommittee                                                             1 Chairs Niki Theis Coulter and Mason Tattersall **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Communicate historical knowledge and analysis effectively in written and/or verbal forms. 5.”
  - statements.guarantees: 1 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `3f9c9bce4e967362` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Pages/transfer-maps.aspx (sha256 3cddb33da5d0)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Pages/common-course-numbering.aspx
- checks: {"effective": 3, "guarantees": 4, "requirements": 5}
  - statements.guarantees: 4 ⟵ “If students complete a Major Transfer Map and meet public university admissions requirements, they are guaranteed transfer to a participating Oregon four-year public university with junior standing, and their coursework will count toward a bachelor’s degree in that specific major.”
  - statements.requirements: 5 ⟵ “Many Major Transfer Maps will require students to take specific courses to complete the Core portion of the Major Transfer Map.”
  - statements.effective: 3 ⟵ “This tool is updated annually.”
### `42da04c8aae777d6` state-OR — state_policies 2018-19 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Elementary%20Education%20MOU%20Updates%204.28.22.pdf (sha256 3a51480106eb)
- issues: stale_year_label:2018-19, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English%20MOU%204.28.22.pdf
- checks: {"effective": 2, "exceptions": 7, "guarantees": 12, "requirements": 16}
  - statements.guarantees: 12 ⟵ “In contrast to other statewide transfer tools that prioritize university general education requirements (i.e., AAOT and ASOT), MTMs specify clear course-taking paths necessary for on-track progress towards a specific major/bachelor’s degree, with a guarantee of transfer from any Oregon community col”
  - statements.requirements: 16 ⟵ “MTMs build on the 30- credit general education foundation defined by the generic Core Transfer Map (CTM), although MTMs may specify particular relevant/required General Education courses as part of the 30-credit CTM The statewide Elementary Education Major Transfer Map (MTM) will use the Associate o”
  - statements.exceptions: 7 ⟵ “However, while CTM-related courses are guaranteed to transfer into general education, degree, or major requirements, students completing an MTM will Students who want to transfer prior to completing the MTM should talk with their community college advisor and an advisor at their target university pr”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the degree/major requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the MTM.”
### `42fdd47f49756454` state-OR — state_policies 2026-27 [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/Pages/initiatives.aspx (sha256 ee22eb5e393b)
- issues: semantic_review_required
- checks: {"requirements": 5}
  - statements.requirements: 5 ⟵ “Learn more about the structure and requirements for the programs below in the Community College Program Approval section of our site.”
### `433a81fc5a627d23` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf (sha256 04c8f864b19f)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 24}
  - statements.requirements: 24 ⟵ “2026 Common Course Numbering Articulation and Communication                                                                                               1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | November 20, 2025 exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `4998a23e1a28d29a` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf (sha256 7a7199dc9673)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 24}
  - statements.requirements: 24 ⟵ “2026 Common Course Numbering Articulation Communication                                                                                       1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | November 20, 2025 exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `5a4cc49ec6e9d488` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf (sha256 8530be925fd0)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 1, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN History Subcommittee                                                             1 Chairs Niki Theis Coulter and Mason Tattersall **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Communicate historical knowledge and analysis effectively in written and/or verbal forms. 5.”
  - statements.guarantees: 1 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `66ce4923c841a553` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf (sha256 a6931e365a33)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 2, "exceptions": 2, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation 2025 CCN Chemistry Subcommittee                                                             1 Cochairs Kenneth Friedrich (PCC) and Christopher Walsh (EOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to particip”
  - statements.effective: 2 ⟵ “Annual CCN Chemistry Subcommittee check-ins beginning in Winter 2028 to gather qualitative Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | October 23, 2025 and/or quantitative data on faculty and student experiences, make requests for institutional and statewi”
  - statements.exceptions: 2 ⟵ “The scope of annual check-ins will focus on the statewide and collaborative nature of this work to facilitate inclusive and equitable conversations and to identify potential issues that may require future modifications of the CCN recommendations or framework every third year, starting in 2031. 2.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
### `6797bba827b76634` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf (sha256 22e573da3b7a)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Physiology III                                                                                         1 Cochairs Lindsay Biga (OSU) and Jonathan Christie (Chemeketa) **715-025-0070 institutions that do not offer an equivalent of this course are not required”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `69c90c15b924e1a6` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf (sha256 585a89e50b3d)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Physiology II                                                                                         1 Cochairs Lindsay Biga (OSU) and Jonathan Christie (Chemeketa) **715-025-0070 institutions that do not offer an equivalent of this course are not required ”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `6cabf45116ff3c76` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf (sha256 1ac2b8fe59f2)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 2, "exceptions": 2, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation CH/CHE/CHEM 104Z Introduction to Chemistry Cochairs Kenneth Friedrich (PCC) and Christopher Walsh (EOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Annual CCN Chemistry Subcommittee check-ins beginning in Winter 2028 to gather qualitative and/or quantitative data on faculty and student experiences, make requests for institutional Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | October 23, 2025 and statewi”
  - statements.exceptions: 2 ⟵ “The scope of annual check-ins will focus on the statewide and collaborative nature of this work to facilitate inclusive and equitable conversations and to identify potential issues that may require future modifications of the CCN recommendations or framework every third year, starting in 2031. 2.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
### `735649a1876d3e3a` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf (sha256 3b0127cf08db)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation Relations                                                                                             1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `7920678b609f0e06` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf (sha256 ab39640fff75)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation POL/POLS/POSC/PS 204Z Comparative Politics and Government                                                                                                 1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to partici”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `7a090788c46cb0f9` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf (sha256 a8edbd45cdac)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 1, "requirements": 24}
  - statements.requirements: 24 ⟵ “2026 Common Course Numbering Articulation Communication                                                                                       1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 1 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning     ”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `83cf7848cf6ab7ca` state-OR — state_policies 2020-21 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/FINAL%20CS%20MOU%204.28.22.pdf (sha256 5eea5f1a861a)
- issues: stale_year_label:2020-21, semantic_review_required
- checks: {"effective": 2, "exceptions": 4, "guarantees": 15, "requirements": 21}
  - statements.requirements: 21 ⟵ “In contrast to other statewide transfer tools that prioritize university general education requirements (i.e.”
  - statements.guarantees: 15 ⟵ “AAOT and ASOT), MTMs specify clear course-taking paths necessary for on-track progress towards a specific major/bachelor’s degree, with a guarantee of transfer from any Oregon community college to any Oregon public university.”
  - statements.exceptions: 4 ⟵ “However, while CTM-related courses are guaranteed to transfer into general education, degree, or major requirements, students completing an MTM will not be awarded a CTM Students who want to transfer prior to completing the MTM should talk with their community college advisor and an advisor at their”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the degree/major requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the MTM.”
### `8e08aecf9f313e9d` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf (sha256 d9e10c2e7a1b)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Chairs Rachel Knighten, Patricia Giménez-Eguíbar **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Beginning Fall 2028, only SPA/SPA/SPAN 201Z, 202Z, and 203Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | June 18, 2026 exception.”
### `9e74aa9cc3f3c12c` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf (sha256 773af631fa3a)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 1, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN History Subcommittee                                                             1 Chairs Niki Theis Coulter and Mason Tattersall **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Communicate historical knowledge and analysis effectively in written and/or verbal forms. 5.”
  - statements.guarantees: 1 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `ad37cf9518d58221` state-OR — state_policies 2026-27 [new] (ambiguous_year_labels)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-MOU.pdf (sha256 e1bb609999bd)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"effective": 6, "exceptions": 5, "guarantees": 12, "requirements": 26}
  - statements.requirements: 26 ⟵ “In contrast to other statewide transfer tools that prioritize university general education requirements (i.e.”
  - statements.guarantees: 12 ⟵ “AAOT and ASOT), MTMs specify clear course-taking paths necessary for on-track progress towards a specific major/bachelor’s degree, with a guarantee of transfer from any Oregon community college to any Oregon public university.”
  - statements.exceptions: 5 ⟵ “However, while CTM-related courses are guaranteed to transfer into general education, degree, or major requirements, students completing an MTM will not be awarded a CTM Students who want to transfer prior to completing the MTM should talk with their community college advisor and an advisor at their”
  - statements.effective: 6 ⟵ “Eligibility to graduate following the degree/major requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the MTM.”
### `b982623e0a8d0c59` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf (sha256 a3c5469c06e6)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Chairs Rachel Knighten, Patricia Giménez-Eguíbar **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Beginning Fall 2028, only SPA/SPA/SPAN 201Z, 202Z, and 203Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | June 18, 2026 exception.”
### `c2915cacaa8a552d` state-OR — state_policies 2026-27 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf (sha256 3d4597e422af)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 2, "exceptions": 2, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Cochairs Kenneth Friedrich (PCC) and Christopher Walsh (EOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Annual CCN Chemistry Subcommittee check-ins beginning in Winter 2028 to gather qualitative and/or quantitative data on faculty and student experiences, make requests for institutional and statewide data, discuss challenges, and raise concerns to review the transfer effectiveness of the CCN CH/CHE/CH”
  - statements.exceptions: 2 ⟵ “The scope of annual check-ins will focus on the statewide and Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | October 23, 2025 collaborative nature of this work to facilitate inclusive and equitable conversations and to identify potential issues that may requi”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
### `d4ec890abaabdb44` state-OR — state_policies 2018-19 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English%20MOU%204.28.22.pdf (sha256 07d72801cbee)
- issues: stale_year_label:2018-19, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Elementary%20Education%20MOU%20Updates%204.28.22.pdf
- checks: {"effective": 2, "exceptions": 4, "guarantees": 13, "requirements": 20}
  - statements.requirements: 20 ⟵ “In contrast to other statewide transfer tools that prioritize university general education requirements (i.e.”
  - statements.guarantees: 13 ⟵ “AAOT and ASOT), MTMs specify clear course-taking paths necessary for on-track progress towards a specific major/bachelor’s degree, with a guarantee of transfer from any Oregon community college to any Oregon public university.”
  - statements.exceptions: 4 ⟵ “However, while CTM-related courses are guaranteed to transfer into general education, degree, or major requirements, students completing an MTM will Students who want to transfer prior to completing the MTM should talk with their community college advisor and an advisor at their target university pr”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the degree/major requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the MTM.”
### `e4339a85939e3877` state-OR — state_policies 2027-28 [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf (sha256 e7d371c57e48)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation SPA/SPN/SPAN 203Z Second-year Spanish III CCN Spanish Subcommittee                                                              1 Chairs Rachel Knighten, Patricia Giménez-Eguíbar **715-025-0070 institutions that do not offer an equivalent of this course are ”
  - statements.effective: 2 ⟵ “Beginning Fall 2028, only SPA/SPA/SPAN 201Z, 202Z, and 203Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `f37beb8096e3fd0b` state-OR — state_policies 2026-27 [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/CCNAP-Template.pdf (sha256 b1bc136f5582)
- issues: semantic_review_required
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “[Year] Common Course Numbering Articulation Course Number and Subject Code Course Title **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `fe80056966bd884d` state-OR — state_policies 2026-27 [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Core-Transfer-Maps-One-pager.pdf (sha256 c6ed72a42b75)
- issues: semantic_review_required
- checks: {"requirements": 9}
  - statements.requirements: 9 ⟵ “The Core Transfer Maps are broad descriptions of course requirements for students at any Oregon community college or public university.”
### `3928eb933611fff7` Blue Mountain Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/financial-aid/ (sha256 5668159329dc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “FAFSA Resources Dependency Override Petition: If extenuating family circumstances prevent the student from providing parental information, and the student meets certain criteria, the student can complete a Dependency Override Petition form listed on our website here under Financial Aid.”
### `519b433dc90dcd11` Blue Mountain Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/financial-aid/ (sha256 5668159329dc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have questions or special circumstances, contact our office to meet with a Financial Aid Advisor.”
### `e851f9b3084cda7e` Blue Mountain Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/financial-aid/ (sha256 5668159329dc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Financial Aid How it Works Apply Complete the FAFSA FAFSA Help Find answers to common Questions By completing the FAFSA you will have access to the following types of federal financial aid: Pell, FSEOG, Federal Stafford Loans, Federal Work-Study, and the option for a Professional Judgement (if needed).”
  - sentence: professional_judgment ⟵ “Professional Judgements Professional Judgment (PJ): When submitting the FAFSA, the student’s household income and asset information are used to calculate the Student Aid Index (SAI).”
  - sentence: professional_judgment ⟵ “If your household income and financial situation has changed significantly from the previous year, you may submit a Professional Judgment to request that your current income be used to determine your eligibility.”
  - sentence: professional_judgment ⟵ “BMCC retains the right to refuse certification based on professional judgment.”
### `d7b32c9b874585cf` Blue Mountain Community College — costs 2026-27 [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/tuition-fees/ (sha256 c922497ee779)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition & Required Fees: 7211 ⟵ “Tuition & Required Fees | $7,211 | $7,211 | $9,936”
  - column:Books & Supplies: 1105 ⟵ “Books & Supplies | $1,105 | $1,105 | $1,105”
  - column:Living Expenses: 6450 ⟵ “Living Expenses | $6,450 | $10,800 | $10,800”
  - column:Misc./Personal Expenses: 1200 ⟵ “Misc./Personal Expenses | $1,200 | $1,200 | $1,200”
  - column:Transportation: 1974 ⟵ “Transportation | $1,974 | $1,974 | $1,974”
  - column:TOTAL: 17940 ⟵ “TOTAL | $17,940 | $22,290 | $25,015”
  - column:Tuition & Required Fees: 7211 ⟵ “Tuition & Required Fees | $7,211 | $7,211 | $9,936”
  - column:Books & Supplies: 1105 ⟵ “Books & Supplies | $1,105 | $1,105 | $1,105”
  - column:Living Expenses: 10800 ⟵ “Living Expenses | $6,450 | $10,800 | $10,800”
  - column:Misc./Personal Expenses: 1200 ⟵ “Misc./Personal Expenses | $1,200 | $1,200 | $1,200”
  - column:Transportation: 1974 ⟵ “Transportation | $1,974 | $1,974 | $1,974”
  - column:TOTAL: 22290 ⟵ “TOTAL | $17,940 | $22,290 | $25,015”
### `313c8920f56cdd3a` Bushnell University — appeals 2026-27 [new] (source_unlabeled)
- source: https://bushnell.edu/admissions/undergraduate-admissions/transfer-students/ (sha256 b5d64da507cf)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “However, students may qualify for a housing exemption if they live with a parent or guardian (with a signed housing agreement), are married, turn 21 by September 1, are enrolled in an online, Professional Studies, or Graduate program, are the parent or legal guardian of a dependent child, or qualify for a medical, financial, or special circumstance exemption.”
### `4e9081dc7a1f2ec6` Chemeketa Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_satisfactoryacademicprogress.pdf (sha256 173dc324d4f5)
- issues: semantic_review_required, conflicting_sources:https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_SAPAppealfillableform.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students will not have eligibility for any further federal aid at Chemeketa until they have met Standards of Satisfactory Academic Progress or have been granted an appeal approval. ●​ Incomplete grades have no effect on GPA but do count as attempted coursework for pace of progression standards.”
  - sentence: sap_appeal ⟵ “The decision on the Satisfactory Academic Progress Appeal is FINAL and there are no appeals to this decision unless you wish to provide additional documentation to support your Appeal.”
### `87049a4048e6428d` Chemeketa Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.chemeketa.edu/cost-aid/financial-aid/ (sha256 c1bbd3389261)
- issues: semantic_review_required, conflicting_sources:https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_SAPAppealfillableform.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have special circumstances and can provide documentation that something occurred that severed the relationship with your parent(s), and you can provide documentation that you have no contact with your parent(s), contact the Financial Aid Office.”
### `901fccdc91e3de18` Chemeketa Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_SAPAppealfillableform.pdf (sha256 65ee1e2524b2)
- issues: semantic_review_required, conflicting_sources:https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_satisfactoryacademicprogress.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Box 14007 ● Salem, OR 97309 503.399.5018 ● Fax 503.399.5528 financialaid@chemeketa.edu Satisfactory Academic Progress (SAP) Appeal Name: Chemeketa ID#: K ______________________ Degree or certificate you are currently seeking at Chemeketa: _____________________ All appeal requests must be completed in full.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Page 2 of 3 When completing the questions you must be complete in your answers.”
  - sentence: sap_appeal ⟵ “If available, attach documentation of your circumstances and/or explain why you do not have documentation. ________________________________________________________________________ Satisfactory Academic Progress (SAP) Appeal Page 3 of 3 2.”
### `947bff027e18d6f3` Chemeketa Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_SAPAppealfillableform.pdf (sha256 65ee1e2524b2)
- issues: semantic_review_required, conflicting_sources:https://www.chemeketa.edu/cost-aid/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow appeals to be approved only if you can demonstrate mitigating circumstances, emergencies, or other unusual circumstances that led to your academic difficulties. 1.”
### `14f9f1f96bcfbbe3` Chemeketa Community College — costs 2025-26 [new] (labeled_in_source)
- source: https://www.chemeketa.edu/cost-aid/tuition-fees/ (sha256 ff76a1a01e96)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees (based on 12 credits): 1752 ⟵ “Tuition & Fees (based on 12 credits) | $1,752 | $3,504 | $5,256 | $7,008”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | $400 | $800 | $1,200 | $1,600”
  - column:Food & Housing: 7060 ⟵ “Food & Housing | $7,060 | $14,120 | $21,180 | $28,240”
  - column:Transportation: 616 ⟵ “Transportation | $616 | $1,232 | $1,848 | $2,464”
  - column:Personal: 636 ⟵ “Personal | $636 | $1,272 | $1,908 | $2,544”
  - column:Loan Fees: 22 ⟵ “Loan Fees | $22 | $44 | $66 | $88”
  - column:Total Expenses: 10486 ⟵ “Total Expenses | $10,486 | $20,972 | $31,458 | $41,944”
  - column:Tuition & Fees (based on 12 credits): 3504 ⟵ “Tuition & Fees (based on 12 credits) | $1,752 | $3,504 | $5,256 | $7,008”
  - column:Books & Supplies: 800 ⟵ “Books & Supplies | $400 | $800 | $1,200 | $1,600”
  - column:Food & Housing: 14120 ⟵ “Food & Housing | $7,060 | $14,120 | $21,180 | $28,240”
  - column:Transportation: 1232 ⟵ “Transportation | $616 | $1,232 | $1,848 | $2,464”
  - column:Personal: 1272 ⟵ “Personal | $636 | $1,272 | $1,908 | $2,544”
  - column:Loan Fees: 44 ⟵ “Loan Fees | $22 | $44 | $66 | $88”
  - column:Total Expenses: 20972 ⟵ “Total Expenses | $10,486 | $20,972 | $31,458 | $41,944”
  - column:Tuition & Fees (based on 12 credits): 5256 ⟵ “Tuition & Fees (based on 12 credits) | $1,752 | $3,504 | $5,256 | $7,008”
  - column:Books & Supplies: 1200 ⟵ “Books & Supplies | $400 | $800 | $1,200 | $1,600”
  - column:Food & Housing: 21180 ⟵ “Food & Housing | $7,060 | $14,120 | $21,180 | $28,240”
  - column:Transportation: 1848 ⟵ “Transportation | $616 | $1,232 | $1,848 | $2,464”
  - column:Personal: 1908 ⟵ “Personal | $636 | $1,272 | $1,908 | $2,544”
  - column:Loan Fees: 66 ⟵ “Loan Fees | $22 | $44 | $66 | $88”
  - column:Total Expenses: 31458 ⟵ “Total Expenses | $10,486 | $20,972 | $31,458 | $41,944”
  - column:Tuition & Fees (based on 12 credits): 7008 ⟵ “Tuition & Fees (based on 12 credits) | $1,752 | $3,504 | $5,256 | $7,008”
  - column:Books & Supplies: 1600 ⟵ “Books & Supplies | $400 | $800 | $1,200 | $1,600”
  - column:Food & Housing: 28240 ⟵ “Food & Housing | $7,060 | $14,120 | $21,180 | $28,240”
  - column:Transportation: 2464 ⟵ “Transportation | $616 | $1,232 | $1,848 | $2,464”
  - … 3 more rows
### `7e4c23d6cae2a428` Chemeketa Community College — costs 2026-27 [new] (labeled_in_source)
- source: https://www.chemeketa.edu/cost-aid/financial-aid/ (sha256 c1bbd3389261)
- issues: residency_unknown, conflicting_sources:https://www.chemeketa.edu/admission/international/estimated-costs/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition & Fees: 1752 ⟵ “Tuition & Fees | $1,752 | $1,752”
  - off_campus_not_with_family:Books & Supplies: 400 ⟵ “Books & Supplies | $400 | $400”
  - off_campus_not_with_family:Housing & Food: 7060 ⟵ “Housing & Food | $7,060 | $2,356”
  - off_campus_not_with_family:Transportation & Personal: 1252 ⟵ “Transportation & Personal | $1,252 | $1,252”
  - off_campus_not_with_family:Loan fees (if borrowing): 22 ⟵ “Loan fees (if borrowing) | $22 | $22”
  - off_campus_not_with_family:Total: 10486 ⟵ “Total | $10,486 | $5,282”
  - with_parents_or_family:Tuition & Fees: 1752 ⟵ “Tuition & Fees | $1,752 | $1,752”
  - with_parents_or_family:Books & Supplies: 400 ⟵ “Books & Supplies | $400 | $400”
  - with_parents_or_family:Housing & Food: 2356 ⟵ “Housing & Food | $7,060 | $2,356”
  - with_parents_or_family:Transportation & Personal: 1252 ⟵ “Transportation & Personal | $1,252 | $1,252”
  - with_parents_or_family:Loan fees (if borrowing): 22 ⟵ “Loan fees (if borrowing) | $22 | $22”
  - with_parents_or_family:Total: 5282 ⟵ “Total | $10,486 | $5,282”
### `f0454cf65f19ecbb` Chemeketa Community College — costs 2026-27 [new] (source_unlabeled)
- source: https://www.chemeketa.edu/admission/international/estimated-costs/ (sha256 0c1e43dcdaf7)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.chemeketa.edu/cost-aid/financial-aid/
- checks: {"columns": 2, "rows": 5}
  - column:Tuition & Fees: 3950 ⟵ “Tuition & Fees | $3,950 | $11,850”
  - column:Books & Supplies*: 280 ⟵ “Books & Supplies* | $280 | $840”
  - column:Housing & Food**: 2400 ⟵ “Housing & Food** | $2,400 | $7,200”
  - column:Health Insurance: 495 ⟵ “Health Insurance | $495 | $1,980”
  - column:TOTALS: 7125 ⟵ “TOTALS | $7,125 | $21,870”
  - column:Tuition & Fees: 11850 ⟵ “Tuition & Fees | $3,950 | $11,850”
  - column:Books & Supplies*: 840 ⟵ “Books & Supplies* | $280 | $840”
  - column:Housing & Food**: 7200 ⟵ “Housing & Food** | $2,400 | $7,200”
  - column:Health Insurance: 1980 ⟵ “Health Insurance | $495 | $1,980”
  - column:TOTALS: 21870 ⟵ “TOTALS | $7,125 | $21,870”
### `c94138bc69ad6470` Chemeketa Community College — credit_policies 2025-26 [new] (labeled_in_source)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/students/enrollment-services/enrollmentservices_IBEquivalencies2025_26.pdf (sha256 8791548eea41)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 4, "equivalencies": 4, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|5+]:  ⟵ “Art History                            5+              ART 2XX                4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5+]:  ⟵ “Business                 Level          5+              BA 1XX                 4”
  - equivalencies[IB-MUSIC|5+]:  ⟵ “Music            Level      5+         MUS 161           3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4]:  ⟵ “Anthropology                    4          ATH 2XX          4”
### `ec795a52447e0866` Chemeketa Community College — credit_policies 2025-26 [new] (labeled_in_source)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/students/enrollment-services/enrollmentservices_CLEPExamEquivalencies2025_26.pdf (sha256 12746bfcd2d0)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 11, "equivalencies": 11, "rows_without_score": 0}
  - equivalencies[CLEP-HUMANITIES|50+]:  ⟵ “Humanities                      50+                             12               HUM 1XX”
  - equivalencies[CLEP-NATURAL-SCIENCES|50+]:  ⟵ “Natural Sciences                50+                             12               GS LAB”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50+]:  ⟵ “Social Sciences & History       50+                             12               SSC 1XX”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50+]:  ⟵ “American Literature             50+                             8                ENG 253, 254*”
  - equivalencies[CLEP-CALCULUS|50+]:  ⟵ “Calculus                        50+                             10               MTH 251Z, 252Z”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50+]:  ⟵ “College Algebra                 50+                             5                MTH 111Z”
  - equivalencies[CLEP-PRECALCULUS|50+]:  ⟵ “Precalculus                     50+                             4                MTH 241”
  - equivalencies[CLEP-ENGLISH-LITERATURE|54+]:  ⟵ “English Literature              54+                             8                ENG 204, 205*”
  - equivalencies[CLEP-BIOLOGY|50+]:  ⟵ “General Biology                 50+                             12               BI 101, 102, 103”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50+]:  ⟵ “Intro. Business Law             50+                             4                BA 226Z”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50+]:  ⟵ “Western Civilization 1 &        50+                             12               HST 1XX, 1XX, 1XX”
### `196e96f1bc969086` Clackamas Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships/financial-aid-rights-and-responsibilities (sha256 374b5ef6a8f5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “REPORT ANY CHANGES IN YOUR FINANCIAL SITUATION If the information provided on your FAFSA has changed significantly for reasons beyond your control since you applied, contact the Office of Financial Aid and Scholarships to find out if you are eligible to submit a Change In Financial Situation appeal.”
  - sentence: need_based_special_circumstances ⟵ “Changes may include: Loss of employment Loss of untaxed income Death of a parent Unusual medical/dental expenses not covered by insurance We do not accept or review Change in Financial Situation appeals until after your current year financial aid eligibility has been determined.”
### `3d86eae4d05c5b96` Clackamas Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships/financial-aid-rights-and-responsibilities (sha256 374b5ef6a8f5)
- issues: semantic_review_required, conflicting_sources:https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Review your Award Offer and accept any loans you wish to borrow Complete the Entrance Counseling requirement if you're a first time borrower, submit a Master Promissory Note (one time requirement every 10 years). 3.”
### `66bac4cda0204e79` Clackamas Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- issues: semantic_review_required, conflicting_sources:https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships/financial-aid-rights-and-responsibilities
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “To access financial aid: Submit all requested documents listed in Self Service Watch your student email and Self Service for award offer notification Review your award offer.”
### `e0cff2a377df9216` Clackamas Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships/financial-aid-satisfactory-academic-progress-standards (sha256 6a5ad104c55a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Expand all Collapse all Satisfactory Academic Progress Appeal (SAP) process Satisfactory Academic Progress Appeal (SAP) process If students are in disqualified status: They are not eligible for federal financial aid.”
  - sentence: sap_appeal ⟵ “A student may appeal by completing a Satisfactory Academic Progress (SAP) Appeal form.”
### `2360494c54fb0d9b` Clackamas Community College — costs 2024-25 [new] (labeled_in_source)
- source: https://www.clackamas.edu/docs/default-source/admissions-and-financial-aid/financial-aid-forms/2024-25/24-25-cost-of-attendance.pdf?sfvrsn=b6269c68_3 (sha256 d3c887eb6358)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 4, "rows": 12}
  - column:Tuition/fees: 2115 ⟵ “Tuition/fees | $2,115 | $4,230 | $6,345 | $8,460”
  - column:Books: 600 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 575 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 450 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:$3,740: 7480 ⟵ “$3,740 | $7,480 | $11,220 | $14,960”
  - column:Living Expenses: 3618 ⟵ “Living Expenses | $3,618 | $7,236 | $10,854 | $14,472”
  - column:Living Expenses (not: 6699 ⟵ “Living Expenses (not | $6,699 | $13,398 | $20,097 | $26,796”
  - column:Living with parent: 7358 ⟵ “Living with parent | $7,358 | $14,716 | $22,074 | $29,432”
  - column:Not living with parent: 10439 ⟵ “Not living with parent | $10,439 | $20,878 | $31,317 | $41,756”
  - column:Tuition and fees: 2115.0 ⟵ “Tuition and fees | 2115.00 | 705.00”
  - column:Books/Supplies: 600.0 ⟵ “Books/Supplies | 600.00 | 200.00”
  - column:Transportation: 575.0 ⟵ “Transportation | 575.00 | 192.00”
  - column:Personal expenses (entertainment,: 450.0 ⟵ “Personal expenses (entertainment, | 450.00 | 150.00”
  - column:Living Expenses: 3618 ⟵ “Living Expenses | $3,618”
  - column:Living Expenses (not: 6699 ⟵ “Living Expenses (not | $6,699”
  - column:Tuition/fees: 4230 ⟵ “Tuition/fees | $2,115 | $4,230 | $6,345 | $8,460”
  - column:Books: 1200 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 1150 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 900 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:$3,740: 11220 ⟵ “$3,740 | $7,480 | $11,220 | $14,960”
  - column:Living Expenses: 7236 ⟵ “Living Expenses | $3,618 | $7,236 | $10,854 | $14,472”
  - column:Living Expenses (not: 13398 ⟵ “Living Expenses (not | $6,699 | $13,398 | $20,097 | $26,796”
  - column:Living with parent: 14716 ⟵ “Living with parent | $7,358 | $14,716 | $22,074 | $29,432”
  - column:Not living with parent: 20878 ⟵ “Not living with parent | $10,439 | $20,878 | $31,317 | $41,756”
  - column:Tuition and fees: 705.0 ⟵ “Tuition and fees | 2115.00 | 705.00”
  - … 20 more rows
### `36d85d48295e79e2` Clackamas Community College — costs 2026-27 [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 4, "components_reconcile": true, "rows": 5}
  - column:Tuition/Fees: 2175 ⟵ “Tuition/Fees | $2,175 | $4,350 | $6,525 | $8,700”
  - column:Books: 600 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 575 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 450 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:Total: 3800 ⟵ “Total | $3,800 | $7,600 | $11,400 | $15,200”
  - column:Tuition/Fees: 4350 ⟵ “Tuition/Fees | $2,175 | $4,350 | $6,525 | $8,700”
  - column:Books: 1200 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 1150 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 900 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:Total: 7600 ⟵ “Total | $3,800 | $7,600 | $11,400 | $15,200”
  - column:Tuition/Fees: 6525 ⟵ “Tuition/Fees | $2,175 | $4,350 | $6,525 | $8,700”
  - column:Books: 1800 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 1725 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 1350 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:Total: 11400 ⟵ “Total | $3,800 | $7,600 | $11,400 | $15,200”
  - column:Tuition/Fees: 8700 ⟵ “Tuition/Fees | $2,175 | $4,350 | $6,525 | $8,700”
  - column:Books: 2400 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 2300 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 1800 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:Total: 15200 ⟵ “Total | $3,800 | $7,600 | $11,400 | $15,200”
### `15d071a0c30d26ad` Clatsop Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.clatsopcc.edu/financial-aid-scholarships/applying-for-aid/ (sha256 6e04fede841a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Dependency Override information for extenuating circumstances: The federal government’s regulations on dependency overrides are strict; however, there may be extenuating circumstances when a student should be considered independent.”
  - sentence: dependency_override ⟵ “Please note that dependency overrides are NOT considered for the following reasons: Parents’ refusal to contribute to student’s education.”
### `93e7b701a1e96546` Clatsop Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.clatsopcc.edu/financial-aid-scholarships/applying-for-aid/ (sha256 6e04fede841a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The formula used to determine eligibility for federal student aid is basically the same for all applicants.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances form – This form is used to request a review of your financial aid eligibility as a result of changes in financial circumstances which occurred after you filed your FAFSA.”
### `2bfef158f49733dd` Clatsop Community College — costs 2026-27 [new] (labeled_in_source)
- source: https://www.clatsopcc.edu/tuition-fees/ (sha256 5d19509a49cc)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Tuition and fees: 5418 ⟵ “Tuition and fees | $5,418”
  - column:Books and Supplies: 2800 ⟵ “Books and Supplies | $2,800”
  - column:Living, Personal, Travel: 25362 ⟵ “Living, Personal, Travel | $25,362”
  - column:Total Expenses: 33680 ⟵ “Total Expenses | $33,680”
### `ab7f38124ad293c1` Clatsop Community College — costs 2024-25 [new] (labeled_in_source)
- source: https://www.clatsopcc.edu/financial-aid-scholarships/award-information/ (sha256 103144dc6ef1)
- issues: components_do_not_reconcile, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Tuition and fees: 5103 ⟵ “Tuition and fees | $ 5,103”
  - column:Books, Supplies & Computer: 2800 ⟵ “Books, Supplies & Computer | $ 2,800”
  - column:Living, Personal, Travel: 23081 ⟵ “Living, Personal, Travel | $ 23,081”
  - column:Total Expenses: 31084 ⟵ “Total Expenses | $ 31,084”
### `2f2829e99e58af27` Corban University — appeals 2025-26 [new] (labeled_in_source)
- source: https://engage.corban.edu/register/specialcircumstances (sha256 f04b4a9bc1c0)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://media.corban.edu/hydra/media/files/2025/03/10/special-circumstances-form-25-26.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Federal regulations allow the Financial Aid Office to use professional judgment to make changes to the original information reported on the FAFSA, when a valid reason for the change exists.”
### `313a2e94793fce15` Corban University — appeals 2026-27 [new] (labeled_in_source)
- source: https://media.corban.edu/hydra/media/files/2025/10/09/special-circumstances-paper-form-26-27.pdf (sha256 b585e1db03bf)
- issues: semantic_review_required, conflicting_sources:https://engage.corban.edu/register/specialcircumstances26-27
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Your Special Circumstances appeal cannot be processed without an explanation of your situation.”
### `808a79274d0087cb` Corban University — appeals 2025-26 [new] (labeled_in_source)
- source: https://media.corban.edu/hydra/media/files/2025/03/10/special-circumstances-form-25-26.pdf (sha256 d3a7368ffee7)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://engage.corban.edu/register/specialcircumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Your Special Circumstances appeal cannot be processed without an explanation of your situation.”
### `9e03fcbe407ada7d` Corban University — appeals 2025-26 [new] (labeled_in_source)
- source: https://media.corban.edu/hydra/media/files/2025/03/10/special-circumstances-form-25-26.pdf (sha256 d3a7368ffee7)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://engage.corban.edu/register/specialcircumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Circumstances Form 2025-2026 Academic Year RETURN THIS FORM TO: Corban University Financial Aid Office|5000 Deer Park Drive SE | Salem, OR 97317| Phone: 503.375.7006 |Fax: 503.585.4316|Email: financialaid@corban.edu Federal regulations allow the Financial Aid Office to use professional judgment to make changes to the original information reported on the FAFSA, when a valid reason for the c”
### `a4eaa37d105a4921` Corban University — appeals 2025-26 [new] (labeled_in_source)
- source: https://engage.corban.edu/register/specialcircumstances (sha256 f04b4a9bc1c0)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://media.corban.edu/hydra/media/files/2025/03/10/special-circumstances-form-25-26.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form 25-26 This website uses resources that are being blocked by your network.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form 25-26 IF YOU HAVE ANY QUESTIONS, PLEASE DIRECT THEM TO: Corban University Financial Aid Office | 5000 Deer Park Drive SE | Salem, OR 97317| Phone: 503.375.7006 |Fax: 503.585.4316|Email: financialaid@corban.edu.”
  - sentence: need_based_special_circumstances ⟵ “Student Information & Circumstance Student First Name Student Last Name Please select the special circumstance(s) that applies: Student’s (and/or spouse’s) income will change significantly from the income listed on the FAFSA.”
### `bcd80e4090cc177c` Corban University — appeals 2026-27 [new] (labeled_in_source)
- source: https://engage.corban.edu/register/specialcircumstances26-27 (sha256 837e96fcac5d)
- issues: semantic_review_required, conflicting_sources:https://media.corban.edu/hydra/media/files/2025/10/09/special-circumstances-paper-form-26-27.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form 26-27 This website uses resources that are being blocked by your network.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form 26-27 IF YOU HAVE ANY QUESTIONS, PLEASE DIRECT THEM TO: Corban University Financial Aid Office | 5000 Deer Park Drive SE | Salem, OR 97317| Phone: 503.375.7006 |Fax: 503.585.4316|Email: financialaid@corban.edu.”
  - sentence: need_based_special_circumstances ⟵ “Student Information & Circumstance Student First Name Student Last Name Please select the special circumstance(s) that applies: Student’s (and/or spouse’s) income will change significantly from the income listed on the FAFSA.”
### `f3150c931fa3f2f6` Corban University — appeals 2026-27 [new] (labeled_in_source)
- source: https://media.corban.edu/hydra/media/files/2025/10/09/special-circumstances-paper-form-26-27.pdf (sha256 b585e1db03bf)
- issues: semantic_review_required, conflicting_sources:https://engage.corban.edu/register/specialcircumstances26-27
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Circumstances Form 2026-2027 Academic Year RETURN THIS FORM TO: Corban University Financial Aid Office|5000 Deer Park Drive SE | Salem, OR 97317| Phone: 503.375.7006 |Fax: 503.585.4316|Email: financialaid@corban.edu Federal regulations allow the Financial Aid Office to use professional judgment to make changes to the original information reported on the FAFSA, when a valid reason for the c”
### `fc7e45c189dc155d` Corban University — appeals 2026-27 [new] (labeled_in_source)
- source: https://engage.corban.edu/register/specialcircumstances26-27 (sha256 837e96fcac5d)
- issues: semantic_review_required, conflicting_sources:https://media.corban.edu/hydra/media/files/2025/10/09/special-circumstances-paper-form-26-27.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Federal regulations allow the Financial Aid Office to use professional judgment to make changes to the original information reported on the FAFSA, when a valid reason for the change exists.”
### `0c92c33ed1c7f1bf` Corban University — costs 2026-27 [new] (source_unlabeled)
- source: https://www.corban.edu/admissions-aid/apply/real-cost-of-corban-education/ (sha256 0fc4df9c42b0)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.corban.edu/admissions-aid/tuition-fees/
- checks: {"columns": 2, "components_reconcile": false, "rows": 5}
  - column:Tuition and Fees: 17475 ⟵ “Tuition and Fees | $17,475 | $40,130”
  - column:Room and Board: 18183 ⟵ “Room and Board | $18,183 | $13,960”
  - column:Total Cost: 35658 ⟵ “Total Cost | $35,658 | $54,090”
  - column:Average Financial Aid: 10305 ⟵ “Average Financial Aid | $10,305** | $28,565”
  - column:FINAL COST: 25353 ⟵ “FINAL COST | $25,353 | $25,525”
  - column:Tuition and Fees: 40130 ⟵ “Tuition and Fees | $17,475 | $40,130”
  - column:Room and Board: 13960 ⟵ “Room and Board | $18,183 | $13,960”
  - column:Total Cost: 54090 ⟵ “Total Cost | $35,658 | $54,090”
  - column:Average Financial Aid: 28565 ⟵ “Average Financial Aid | $10,305** | $28,565”
  - column:FINAL COST: 25525 ⟵ “FINAL COST | $25,353 | $25,525”
### `5f2cff721c37aa93` Corban University — costs 2026-27 [new] (labeled_in_source)
- source: https://www.corban.edu/admissions-aid/tuition-fees/ (sha256 443ddeefd999)
- issues: conflicting_sources:https://www.corban.edu/admissions-aid/apply/real-cost-of-corban-education/
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition (12-18 Credits): 38864 ⟵ “Tuition (12-18 Credits) | $38,864”
  - column:+ Housing (with average housing cost): 7860 ⟵ “+ Housing (with average housing cost) | $7,860”
  - column:+ Food (with largest meal plan): 6100 ⟵ “+ Food (with largest meal plan) | $6,100”
  - column:+ Student Activity Fee*: 1156 ⟵ “+ Student Activity Fee* | $1,156”
  - column:+ Technology Fee: 110 ⟵ “+ Technology Fee | $110”
  - column:= Total Tuition, Food & Housing, and Fees: 54090 ⟵ “= Total Tuition, Food & Housing, and Fees | $54,090”
### `8f7695172bd84393` George Fox University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.georgefox.edu/nursing-practice/crna/tuition/index.html (sha256 c909015e6cf8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “No changes will be made during a semester, nor, unless special circumstances make such action necessary, will changes be made during a given academic year.”
### `1353718e02bc680e` Klamath Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Limitations A student is not limited on the number of times they can appeal due to not meeting Satisfactory Academic Progress standard.”
### `373de39074f2a7a9` Klamath Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/Special-Circumstance-Appeal.pdf (sha256 fc34caf4a842)
- issues: semantic_review_required, conflicting_sources:https://www.klamathcc.edu/en-US/admissions/financial-aid/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstance Appeal This form initiates an appeal process to request a recalculation of financial need based on special conditions.”
### `f9c303863ee74e54` Klamath Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/special-circumstances.html (sha256 d03023c079ff)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.klamathcc.edu/en-US/admissions/financial-aid/Special-Circumstance-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special circumstance appeals will be considered after you receive your initial award notification for the current aid year.”
  - sentence: need_based_special_circumstances ⟵ “After reviewing your verified special circumstance documentation, your aid package may remain the same, be increased, or reduced according to the financial information that has been submitted.”
  - sentence: need_based_special_circumstances ⟵ “As all files requesting special circumstance consideration will be verified, tax documents and other documents pertaining to the circumstance are required.”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special circumstance request does not guarantee an adjustment will be made to your aid package. 2026-2027 Special Circumstance Appeal Once you have completed the above form you may submit it to Financial Aid in Founder Hall (building 9) or be email at [email protected].”
### `46aa1b327722254b` Lane Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/financial-aid/satisfactory-academic-progress (sha256 a8a34778f7f0)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Probation Status means that your SAP Appeal is approved.”
  - sentence: sap_appeal ⟵ “SAP Appeal forms are available online.”
### `0915c2b4117d4ea6` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “11/30 | American Welding Society | $1,000 | Welding”
### `13c55b0f5f2ea321` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “10/01 | Benjamin Gilman | $Varies | Study Abroad”
### `19ec1f55cdfbf2f3` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “11/30 | Cappex Easy Money | $1,000 | Open”
### `1c002e579643ae87` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “10/15 | American Muscle | $2,500 | Automotive”
### `1e5f195c78f6a969` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “10/01 | Busy Bee's Bee You | $1,500 | US Citizen”
### `2811b8145179d981` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “10/15 | CJ Pony Parts Scholarship | $500 | Open”
### `645e8c53e23f0561` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/31 | American Bullion | $1,000 | Full Time /Trades”
### `69f6cfbd4f59de2a` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “10/31 | Financial Goals | $2,000 | Legal Resident”
### `6b806e6dd437cc51` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/04 | Lounge Lizard Scholarship | $1,000 | Web Design”
### `7aa8f91d9edad4fa` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “10/31 | Alma Exley Scholarship | $6,000 | Education/minority”
### `8050efa91c2117d0` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/16 | Prevounce Preventive Health | $1,000 | Health Care”
### `8520c51c6b32f6ef` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “10/31 | American Culinary Federation | $Varies | Culinary”
### `87ce37c72c485085` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “11/15 | 10 Words or Less Scholarship | $1,500 | Open”
### `8b3bb7621a7edc3e` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “11/15 | Sport Clips Help a Hero | $Varies | US Citizen/Military”
### `8f3a9a51288be6b8` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “11/01 | Nick and Helena Patti Scholarship | $Varies | Italian Extraction”
### `9e52465e94644282` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “10/30 | USBank Scholarship | $Varies | US Resident”
### `a0054537bb50dc51` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/01 | SGS Scholarship | $1,000 | Legal Resident”
### `a359cc09fd903096` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/31 | Delete Cyberbullying | $1,000 | Open”
### `b0f44052ef4fbc9c` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/01 | Custom Patches San Diego | $1,000 | Age 18+”
### `be057fc821749994` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “11/01 | Waggle Human Pet Bond | $1,000 | Full Time”
### `c1e5c6e5bcc18dbf` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “11/29 | ServiceScape | $1,000 | Open”
### `c4103c30989d1208` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “11/15 | Bloom Nation | $1,500 | US Citizen/3.0+GPA”
### `c7df0428ed39d591` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “11/01 | American Indian Services | $2,000 | Native American”
### `cf964e04b067e879` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “10/15 | Extreme Terrain's Student | $2,500 | Science”
### `d712fea551975774` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “10/15 | American Trucks | $2,500 | Full Time /Trades”
### `dbf83b88fd797fdf` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “11/30 | Education Matters | $5,000 | Open”
### `e39d6666838007fe` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “10/31 | Zombie Apocalypse | $2,000 | US Resident”
### `e4007d046b370404` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “11/15 | James Allen Cox | $2,500 | Sophomore”
### `e584d6e9174c1ab5` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/31 | Chemistry Scholarship | $1,000 | Full Time”
### `eb875b3fd08c3b51` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “11/15 | Geneva Rock Scholarship | $2,000 | Construction”
### `ed25749df776d7e2` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “11/15 | Live Your Dream | $Varies | Women”
### `feda5deb25e0445f` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 73a96d858ab9)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “11/01 | Chafee ETV Grant | $Varies | Foster Care”
### `2e2e2c7f18ac1337` Lane Community College — credit_policies 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/transferring-prior-college-credit-lane/credit-prior-learning (sha256 bcc6a339ca6f)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 38, "equivalencies": 56, "rows_without_score": 0}
  - equivalencies[IB-HISTORY-SL|Art History - SL]:  ⟵ “Art History - SL | 4+ | ARH 1XX | 3 | AL”
  - equivalencies[IB-BIOLOGY-SL|Biology - SL]:  ⟵ “Biology - SL | 4 | BI 101 | 4 | LSCI”
  - equivalencies[IB-BIOLOGY-SL|Biology - SL]:  ⟵ “Biology - SL | 5+ | BI 221Z | 5 | LSCI”
  - equivalencies[IB-BIOLOGY-HL|Biology - HL]:  ⟵ “Biology - HL | 4 | BI 221Z, 222Z | 10 | LSCI”
  - equivalencies[IB-BIOLOGY-HL|Biology - HL]:  ⟵ “Biology - HL | 5+ | BI 221Z, 222Z, 223Z | 15 | LSCI”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|Business Management SL/HL]:  ⟵ “Business Management SL/HL | 4+ | BA 1XX | 4 | NONE”
  - equivalencies[IB-CHEMISTRY-SL|Chemistry - SL]:  ⟵ “Chemistry - SL | 4 | CH 104Z, 124Z | 5 | LSCI”
  - equivalencies[IB-CHEMISTRY-SL|Chemistry - SL]:  ⟵ “Chemistry - SL | 5+ | CH 221Z, 227Z | 5 | LSCI”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry - HL]:  ⟵ “Chemistry - HL | 4 | CH 221Z, 222Z, 227Z, 228Z | 12 | LSCI”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry - HL]:  ⟵ “Chemistry - HL | 5+ | CH 221Z, 222Z, 223Z, 227Z, 228Z, 229Z | 15 | LSCI”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|Computer Science - SL]:  ⟵ “Computer Science - SL | 4+ | CS 161 | 4 | SCI”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|Computer Science - HL]:  ⟵ “Computer Science - HL | 4+ | CS 161, 162 | 8 | SCI”
  - equivalencies[IB-ECONOMICS-SL|Economics- SL]:  ⟵ “Economics- SL | 4+ | ECON 201Z | 4 | SOSC”
  - equivalencies[IB-ECONOMICS-HL|Economics-HL]:  ⟵ “Economics-HL | 4+ | ECON 201Z, 202Z | 8 | SOSC”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|Environmental Systems & Societies - SL]:  ⟵ “Environmental Systems & Societies - SL | 4+ | ENSC 181 | 4 | LSCI”
  - equivalencies[IB-FILM-SL|Film - SL]:  ⟵ “Film - SL | 4+ | FA 264 | 4 | AL, CL”
  - equivalencies[IB-FILM-HL|Film - HL]:  ⟵ “Film - HL | 4+ | FA 264, 276 | 8 | AL, CL”
  - equivalencies[IB-GEOGRAPHY-SL|Geography - SL/HL]:  ⟵ “Geography - SL/HL | 4+ | GEOG 142 | 4 | SOSC; CL”
  - equivalencies[IB-GLOBAL-POLITICS-SL|Global Politics - SL/HL]:  ⟵ “Global Politics - SL/HL | 4+ | PS 205 | 4 | SOSC; CL”
  - equivalencies[IB-HISTORY-SL|History SL/HL]:  ⟵ “History SL/HL | 4+ | HST 2XX | 4 | SOSC”
  - equivalencies[IB-HISTORY-HL|History: Africa - HL]:  ⟵ “History: Africa - HL | 4+ | HST 2XX | 4 | SOSC; CL”
  - equivalencies[IB-HISTORY-HL|History: Americas - HL]:  ⟵ “History: Americas - HL | 4+ | HST 201Z, 202Z, 203Z | 12 | SOSC: CL”
  - equivalencies[IB-HISTORY-HL|History: Asia/Oceania - HL]:  ⟵ “History: Asia/Oceania - HL | 4+ | HST 2XX | 4 | SOSC; CL”
  - equivalencies[IB-HISTORY-HL|History: Europe & Middle East - HL]:  ⟵ “History: Europe & Middle East - HL | 4+ | HST 104, 105, 106 | 12 | SOSC; CL”
  - equivalencies[IB-HISTORY-SL|History: Modern World - SL]:  ⟵ “History: Modern World - SL | 4+ | HST 2XX | 4 | SOSC”
  - … 31 more rows
### `4111259470651d2f` Lane Community College — credit_policies 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/transferring-prior-college-credit-lane/credit-prior-learning (sha256 bcc6a339ca6f)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 35, "equivalencies": 59, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3+]:  ⟵ “2-D Art and Design | 3+ | ART 115 | 4 | AL”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art and Design | 3+ | ART 117 | 4 | AL”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARH 206 | 3 | AL”
  - equivalencies[AP-ART-HISTORY|4+]:  ⟵ “Art History | 4+ | ARH 204, 206 | 6 | AL”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BI 101, BI 1XX | 8 | LSCI for BI 101; SCI for BI 1XX”
  - equivalencies[AP-BIOLOGY|4+]:  ⟵ “Biology | 4+ | BI 221Z, BI 223Z | 10 | LSCI”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MTH 251Z | 4 | SCI”
  - equivalencies[AP-CALCULUS-AB|4+]:  ⟵ “Calculus AB | 4+ | MTH 251Z, 252Z | 8 | SCI”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MTH 251Z, 252Z | 8 | SCI”
  - equivalencies[AP-CALCULUS-BC|4+]:  ⟵ “Calculus BC | 4+ | MTH 251Z, 252Z, 253Z | 12 | SCI”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CH 104Z, 124Z | 5 | LSCI”
  - equivalencies[AP-CHEMISTRY|4+]:  ⟵ “Chemistry | 4+ | CH 221Z, 222Z, 223Z, 227Z, 228Z, 229Z | 15 | LSCI”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | CHN 101, 102, 103 | 12 | NONE”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4+]:  ⟵ “Chinese Language & Culture | 4+ | YFL 2X1, 2X2, 2X3 | 12 | AL”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CS 1XX | 4 | NONE”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4+]:  ⟵ “Computer Science A | 4+ | CS 161 | 4 | SCI”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | CS 1XX | 4 | NONE”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4+]:  ⟵ “Computer Science Principles | 4+ | CS 160 | 4 | SCI”
  - equivalencies[AP-DRAWING|3+]:  ⟵ “Drawing | 3+ | ART 131 | 4 | AL”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Language & Composition | 3+ | WR 121Z | 4 | NONE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition | 3+ | ENG 104Z | 4 | AL”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “Environmental Science | 3+ | ENSC 181 | 4 | LSCI”
  - equivalencies[AP-EUROPEAN-HISTORY|3+]:  ⟵ “European History | 3+ | HST 101, 102 | 8 | SOSC”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3+]:  ⟵ “French: Language & Culture | 3+ | FR 201, 202, 203 | 12 | AL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3+]:  ⟵ “French: Literature | 3+ | FR 2XX | 4 | AL”
  - … 34 more rows
### `e23a46772dfcfe7c` Lane Community College — credit_policies 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/transferring-prior-college-credit-lane/credit-prior-learning (sha256 bcc6a339ca6f)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 18, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|55+]:  ⟵ “American Literature | 55+ | ENG 253 | 4 | AL”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50+]:  ⟵ “Analyzing & Interpreting Literature | 50+ | ENG 104Z | 4 | AL”
  - equivalencies[CLEP-BIOLOGY|50+]:  ⟵ “Biology | 50+ | BI 101, 102, 103 | 12 | LSCI”
  - equivalencies[CLEP-CALCULUS|50+]:  ⟵ “Calculus: Elementary | 50+ | MTH 251Z | 4 | SCI”
  - equivalencies[CLEP-CALCULUS|50+]:  ⟵ “Calculus w/ Elementary Functions | 50+ | MTH 251Z, 252Z | 8 | SCI”
  - equivalencies[CLEP-CHEMISTRY|50+]:  ⟵ “Chemistry: General | 50+ | CH 221Z, 222Z, 223Z, 227Z, 228Z, 229Z | 15 | LSCI”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|47+]:  ⟵ “College Algebra | 47+ | MTH 111Z | 4 | SCI”
  - equivalencies[CLEP-ENGLISH-LITERATURE|55+]:  ⟵ “English Literature | 55+ | ENG 204 | 4 | AL”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50+]:  ⟵ “French: College French I & II | 50+ | FR 103 | 5 | NONE”
  - equivalencies[CLEP-FRENCH-LANGUAGE|54+]:  ⟵ “French: College French I & II | 54+ | FR 103, 201 | 9 | AL (201 ONLY)”
  - equivalencies[CLEP-FRENCH-LANGUAGE|56+]:  ⟵ “French: College French I & II | 56+ | FR 201, 202 | 8 | AL”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59+]:  ⟵ “French: College French I & II | 59+ | FR 201, 202, 203 | 12 | AL”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60+]:  ⟵ “German: College German I & II | 60+ | YFL 2X1, 2X2, 2X3 | 12 | AL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50+]:  ⟵ “History of the United States I (American History) | 50+ | HST 201Z | 4 | SOSC; CL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50+]:  ⟵ “History of the United States II (American History) | 50+ | HST 203Z | 4 | SOSC; CL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50+ each]:  ⟵ “History of the United States I & II (Both tests) | 50+ each | HST 201Z, 202Z, 203Z | 12 | SOSC; CL”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50+]:  ⟵ “Macroeconomics | 50+ | ECON 202Z | 4 | SOSC”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50+]:  ⟵ “Microeconomics | 50+ | ECON 201Z | 4 | SOSC”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50+]:  ⟵ “Psychology | 50+ | PSY 201Z, 202Z | 8 | SOSC”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|74+]:  ⟵ “Sociology | 74+ | SOC 204Z | 4 | SOSC”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50+]:  ⟵ “Spanish: College Spanish I & II | 50+ | SPAN 103Z | 4 | NONE”
  - equivalencies[CLEP-SPANISH-LANGUAGE|55+]:  ⟵ “Spanish: College Spanish I & II | 55+ | SPAN 103Z, 201 | 8 | AL; CL (201 ONLY)”
  - equivalencies[CLEP-SPANISH-LANGUAGE|59+]:  ⟵ “Spanish: College Spanish I & II | 59+ | SPAN 201, 202 | 8 | AL; CL”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63+]:  ⟵ “Spanish: College Spanish I & II | 63+ | SPAN 201, 202, 203 | 12 | AL; CL”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50+]:  ⟵ “Western Civilization I | 50+ | HST 101 | 4 | SOSC”
  - … 2 more rows
### `569651ea4f72a128` Linfield University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.linfield.edu/assets/files/institutional-research/2025-2026-Common-Data-Set-6-2-2026.pdf (sha256 aa8e0b58fb19)
- issues: c1_totals_incomplete, stale_year_label:2024-25, conflicting_sources:https://www.linfield.edu/assets/files/institutional-research/CDS-2024-2025-PDF-Linfield-04.21.2025.pdf
- checks: {"fields": ["applications", "enrolled", "entering_fall_year"]}
  - applications: 2522 ⟵ “Total first-time, first-year (degree-seeking) who applied                  1424                 992                   74         32          2522”
  - enrolled: 383 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                     244              135                    4             0           383”
### `b778a6eade73a955` Linfield University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.linfield.edu/assets/files/institutional-research/CDS-2024-2025-PDF-Linfield-04.21.2025.pdf (sha256 4e35684e7047)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.linfield.edu/assets/files/institutional-research/2025-2026-Common-Data-Set-6-2-2026.pdf
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 2629 ⟵ “Total first-time, first-year (degree-seeking) who applied          1374       1152             89          14      2629”
  - admits: 2239 ⟵ “Total first-time, first-year (degree-seeking) who were admitted    1213         995            20          11      2239”
  - enrolled: 381 ⟵ “Total first-time, first-year (degree-seeking) enrolled              240         137              4          0       381”
### `32f93abc32bf3f21` Oregon Coast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.oregoncoast.edu/financial-aid-satisfactory-academic-progress-sap-policy (sha256 bb0e4726f33f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The Financial Aid Probation status is based on the professional judgment of the financial aid office where it is determined the student is likely to meet financial aid SAP standards by the end of the next term.”
### `f1e2ea0747b888d1` Oregon Coast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.oregoncoast.edu/financial-aid-satisfactory-academic-progress-sap-policy (sha256 bb0e4726f33f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students who have their financial aid suspended have the right to file a Satisfactory Academic Progress Appeal with the financial aid office.”
  - sentence: sap_appeal ⟵ “Appeal Process In order to complete a financial aid SAP appeal, a student must first meet with their student success coach.”
### `0b4f2c10b709aa62` Oregon Institute of Technology — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.oit.edu/sites/default/files/2026/documents/Financial%20Aid%20Award%20Guide%202026-27_0.pdf (sha256 bbd183b8d61a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “For Fall 541-885-1280 (phone) SUMMER AID term, SAP appeals must be submitted by the end of the business day, 541-885-1024 (fax) Summer is the beginning of the award year.”
### `4d5bc970e13e362b` Oregon Institute of Technology — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.oit.edu/sites/default/files/2026/documents/Financial%20Aid%20Award%20Guide%202026-27_0.pdf (sha256 bbd183b8d61a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “There is an origination fee, and the interest rate Direct Stafford Unsubsidized Loans for Graduate Students aid and bill. academic progress due to special circumstances for the 2025-2026 school year was 6.39%.”
### `52f61a34acb4c047` Oregon Institute of Technology — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.oit.edu/college-costs/financial-aid/resources/verification-requests (sha256 8fc2fdb240f2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Verification, Special Circumstances and Additional Info Requests | Oregon Tech Skip to main content Prev Prev Apply Visit Give Quicklinks TECHweb Directory Course Search Current Students Academic Calendar Faculty & Staff Foundation Alumni Library Tech Nest Store (Bookstore) Cashier's Office Search Search About Toggle submenu Oregon's Polytechnic Oregon Tech is a public university recognized as Ore”
### `6e2709b40a85d26d` Oregon Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.oit.edu/sites/default/files/2025/documents/25-26%20SAP%20Appeal%20Form.pdf (sha256 8bfff7fb95d6)
- issues: semantic_review_required, conflicting_sources:https://www.oit.edu/college-costs/financial-aid/resources/satisfactory-academic-progress-sap,https://www.oit.edu/sites/default/files/2026/documents/26-27%20SAP%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL FORM SAP Appeal Deadlines are as follows: Summer Term 2025 -July 1,2025, Fall Term 2025 - October 9, 2026, Winter Term 2026 - January 13, 2026, and Spring Term 2026 - April 7, 2026.”
  - sentence: sap_appeal ⟵ “Standard Repayment amount: ____________________ The outcome of your Satisfactory Academic Progress Appeal will be communicated to you in writing and sent to your OIT e-mail address.”
  - sentence: sap_appeal ⟵ “Second SAP appeals that cite the same reasons as your first appeal will not be approved.”
### `9e26c6bbf8d5e905` Oregon Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.oit.edu/sites/default/files/2026/documents/26-27%20SAP%20Appeal%20Form.pdf (sha256 da2b26062940)
- issues: semantic_review_required, conflicting_sources:https://www.oit.edu/college-costs/financial-aid/resources/satisfactory-academic-progress-sap,https://www.oit.edu/sites/default/files/2025/documents/25-26%20SAP%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL FORM SAP Appeal Deadlines are as follows: Summer Term 2026 –June 30, 2026, Fall Term 2026 - October 9, 2027, Winter Term 2027 - January 12, 2027, and Spring Term 2027 - April 6, 2027.”
  - sentence: sap_appeal ⟵ “Standard Repayment amount: ____________________ The outcome of your Satisfactory Academic Progress Appeal will be communicated to you in writing and sent to your OIT e-mail address.”
  - sentence: sap_appeal ⟵ “Second SAP appeals that cite the same reasons as your first appeal will not be approved.”
### `ab206fe3607729fa` Oregon Institute of Technology — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.oit.edu/college-costs/financial-aid/resources/satisfactory-academic-progress-sap (sha256 130f7e7db0b9)
- issues: semantic_review_required, conflicting_sources:https://www.oit.edu/sites/default/files/2025/documents/25-26%20SAP%20Appeal%20Form.pdf,https://www.oit.edu/sites/default/files/2026/documents/26-27%20SAP%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Eligibility may be reinstated if student can reestablish satisfactory academic progress without benefit of financial aid (2.0 and making pace) or appeal and be approved by the financial aid appeal committee.”
  - sentence: sap_appeal ⟵ “Holds may be appealed using a SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “Financial Aid Appeals Process and Timeline If you wish to appeal a hold on your financial aid based on extenuating circumstances, please follow these steps: Obtain a Satisfactory Academic Progress Appeal Form (www.oit.edu/faid/forms) Complete the appeal form according to instructions.”
### `0267fd83bd12aa9d` Oregon State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.oregonstate.edu/satisfactory-academic-progress (sha256 3a9d17902975)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “You will find the link to complete a SAP appeal through your portal.”
### `cd383890d95ca2a2` Oregon State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.oregonstate.edu/admission-appeals (sha256 620c317e1215)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Your statement must specifically address: The extraordinary circumstances why you did not meet and exceed Oregon State’s minimum admissions requirements What you have done or are doing to mitigate the impact of your extraordinary circumstances What are your strengths and how they will result in your success at Oregon State Why you have chosen Oregon State University Your academic and/or career goa”
### `3e364e8e66fa856b` Oregon State University-Cascades Campus — costs 2025-26 [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 36db51e827d2)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (12 CR)1: 14958 ⟵ “Tuition and Fees (12 CR)1 | $14,958 | $4,986”
  - column:Estimated Billable Cost Total: 14958 ⟵ “Estimated Billable Cost Total | $14,958 | $4,986”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Living Expenses (Food and Housing)2: 17205 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Personal and Miscellaneous: 2817 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 879 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 21501 ⟵ “Estimated Non-Billable Cost Total | $21,501 | $7,167”
  - column:Estimated TOTAL: 36459 ⟵ “Estimated TOTAL | $36,459 | $12,153”
  - column:Tuition and Fees (12 CR)1: 4986 ⟵ “Tuition and Fees (12 CR)1 | $14,958 | $4,986”
  - column:Estimated Billable Cost Total: 4986 ⟵ “Estimated Billable Cost Total | $14,958 | $4,986”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Living Expenses (Food and Housing)2: 5735 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Personal and Miscellaneous: 939 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 293 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 7167 ⟵ “Estimated Non-Billable Cost Total | $21,501 | $7,167”
  - column:Estimated TOTAL: 12153 ⟵ “Estimated TOTAL | $36,459 | $12,153”
### `61441485612c1381` Oregon State University-Cascades Campus — costs 2025-26 [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 36db51e827d2)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (15 CR)1: 40392 ⟵ “Tuition and Fees (15 CR)1 | $40,392 | $13,464”
  - column:Living Expenses (Food and Housing)2: 17205 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Estimated Billable Cost Total: 57597 ⟵ “Estimated Billable Cost Total | $57,597 | $19,199”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 2817 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 879 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 4296 ⟵ “Estimated Non-Billable Cost Total | $4,296 | $1,432”
  - column:Estimated TOTAL: 61893 ⟵ “Estimated TOTAL | $61,893 | $20,631”
  - column:Tuition and Fees (15 CR)1: 13464 ⟵ “Tuition and Fees (15 CR)1 | $40,392 | $13,464”
  - column:Living Expenses (Food and Housing)2: 5735 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Estimated Billable Cost Total: 19199 ⟵ “Estimated Billable Cost Total | $57,597 | $19,199”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 939 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 293 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 1432 ⟵ “Estimated Non-Billable Cost Total | $4,296 | $1,432”
  - column:Estimated TOTAL: 20631 ⟵ “Estimated TOTAL | $61,893 | $20,631”
### `6278cdcb63131146` Oregon State University-Cascades Campus — costs 2026-27 [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 36db51e827d2)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (15 CR)1: 42459 ⟵ “Tuition and Fees (15 CR)1 | $42,459 | $14,153”
  - column:Living Expenses (Food and Housing)2: 18066 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Estimated Billable Cost Total: 60525 ⟵ “Estimated Billable Cost Total | $60,525 | $20,175”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 2958 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 930 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 4488 ⟵ “Estimated Non-Billable Cost Total | $4,488 | $1,496”
  - column:Estimated TOTAL: 65013 ⟵ “Estimated TOTAL | $65,013 | $21,671”
  - column:Tuition and Fees (15 CR)1: 14153 ⟵ “Tuition and Fees (15 CR)1 | $42,459 | $14,153”
  - column:Living Expenses (Food and Housing)2: 6022 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Estimated Billable Cost Total: 20175 ⟵ “Estimated Billable Cost Total | $60,525 | $20,175”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 986 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 310 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 1496 ⟵ “Estimated Non-Billable Cost Total | $4,488 | $1,496”
  - column:Estimated TOTAL: 21671 ⟵ “Estimated TOTAL | $65,013 | $21,671”
### `8b18f0c4933c8595` Oregon State University-Cascades Campus — costs 2025-26 [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 36db51e827d2)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (15 CR)1: 15246 ⟵ “Tuition and Fees (15 CR)1 | $15,246 | $5,082”
  - column:Living Expenses (Food and Housing)2: 17205 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Estimated Billable Cost Total: 32451 ⟵ “Estimated Billable Cost Total | $32,451 | $10,817”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 2817 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 879 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 4296 ⟵ “Estimated Non-Billable Cost Total | $4,296 | $1,432”
  - column:Estimated TOTAL: 36747 ⟵ “Estimated TOTAL | $36,747 | $12,249”
  - column:Tuition and Fees (15 CR)1: 5082 ⟵ “Tuition and Fees (15 CR)1 | $15,246 | $5,082”
  - column:Living Expenses (Food and Housing)2: 5735 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Estimated Billable Cost Total: 10817 ⟵ “Estimated Billable Cost Total | $32,451 | $10,817”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 939 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 293 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 1432 ⟵ “Estimated Non-Billable Cost Total | $4,296 | $1,432”
  - column:Estimated TOTAL: 12249 ⟵ “Estimated TOTAL | $36,747 | $12,249”
### `8b973baa9a38f3c9` Oregon State University-Cascades Campus — costs 2026-27 [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 36db51e827d2)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (12 CR)1: 15726 ⟵ “Tuition and Fees (12 CR)1 | $15,726 | $5,242”
  - column:Estimated Billable Cost Total: 15726 ⟵ “Estimated Billable Cost Total | $15,726 | $5,242”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Living Expenses (Food and Housing)2: 18066 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Personal and Miscellaneous: 2958 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 930 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 22554 ⟵ “Estimated Non-Billable Cost Total | $22,554 | $7,518”
  - column:Estimated TOTAL: 38280 ⟵ “Estimated TOTAL | $38,280 | $12,760”
  - column:Tuition and Fees (12 CR)1: 5242 ⟵ “Tuition and Fees (12 CR)1 | $15,726 | $5,242”
  - column:Estimated Billable Cost Total: 5242 ⟵ “Estimated Billable Cost Total | $15,726 | $5,242”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Living Expenses (Food and Housing)2: 6022 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Personal and Miscellaneous: 986 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 310 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 7518 ⟵ “Estimated Non-Billable Cost Total | $22,554 | $7,518”
  - column:Estimated TOTAL: 12760 ⟵ “Estimated TOTAL | $38,280 | $12,760”
### `f26aae5464d96b92` Oregon State University-Cascades Campus — costs 2026-27 [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 36db51e827d2)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (15 CR)1: 16014 ⟵ “Tuition and Fees (15 CR)1 | $16,014 | $5,338”
  - column:Living Expenses (Food and Housing)2: 18066 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Estimated Billable Cost Total: 34080 ⟵ “Estimated Billable Cost Total | $34,080 | $11,360”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 2958 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 930 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 4488 ⟵ “Estimated Non-Billable Cost Total | $4,488 | $1,496”
  - column:Estimated TOTAL: 38568 ⟵ “Estimated TOTAL | $38,568 | $12,856”
  - column:Tuition and Fees (15 CR)1: 5338 ⟵ “Tuition and Fees (15 CR)1 | $16,014 | $5,338”
  - column:Living Expenses (Food and Housing)2: 6022 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Estimated Billable Cost Total: 11360 ⟵ “Estimated Billable Cost Total | $34,080 | $11,360”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 986 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 310 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 1496 ⟵ “Estimated Non-Billable Cost Total | $4,488 | $1,496”
  - column:Estimated TOTAL: 12856 ⟵ “Estimated TOTAL | $38,568 | $12,856”
### `03c5f58f88564756` Pacific Bible College — appeals 2026-27 [new] (source_unlabeled)
- source: https://pacificbible.edu/admissions/financial-aid (sha256 7e7c2fa8fcee)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: professional_judgment ⟵ “Guide to: studentaid.gov/apply-for-aid/fafsa/filling-out/help/before-starting Program Facts Important Links & Information Free Application for Federal Student Aid (FAFSA) Satisfactory Academic Progress Policy Budgeting for Students fastweb Professional Judgement If a student’s income has significantly changed impacting their ability to pay for college (for example: Job loss or layoff due to COVID,”
  - sentence: professional_judgment ⟵ “For more information about Professional Judgments, please see the Financial Aid Coordinator.”
  - sentence: professional_judgment ⟵ “So what IS Professional Judgement?”
  - sentence: professional_judgment ⟵ “FAFSA pulls information from 2 years prior, so if that student has had a job change and their income is significantly less than it was on the tax forms used for their FAFSA, the Financial Aid Coordinator can perform what is called a “Professional Judgement”.”
  - sentence: professional_judgment ⟵ “A Professional Judgment is a process Financial Aid offices perform that provides the ability to make adjustments to information provided by students in their Free Application for Financial Student Aid (FAFSA) applications.”
  - sentence: professional_judgment ⟵ “Professional Judgements are reserved for Special Circumstances that affect the student’s financial situation (such as a job loss/layoff), and for Unusual circumstances that affect the student’s dependency status (such as parental abandonment, etc.).”
### `21e7576773a80877` Pacific Northwest College of Art — costs 2026-27 [new] (labeled_in_source)
- source: https://willamette.edu/cost-aid/tuition (sha256 a63d47dd4885)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "rows": 7}
  - column:Tuition: 28320 ⟵ “Tuition | $28,320 | Per semester”
  - column:Student Activity Fee1: 146 ⟵ “Student Activity Fee1 | $146 | Per semester”
  - column:Meal Plan – Living on campus (14-meal plan): 4270 ⟵ “Meal Plan – Living on campus (14-meal plan) | $4,270 | Per semester”
  - column:Housing – Living on campus3 (Standard double room): 4595 ⟵ “Housing – Living on campus3 (Standard double room) | $4,595 | Per semester”
  - column:Residence Hall Fee: 75 ⟵ “Residence Hall Fee | $75 | Per semester”
  - column:Sub-Total: 37406 ⟵ “Sub-Total | $37,406 | Per semester”
  - column:ANNUAL COST (2 semesters): 74812 ⟵ “ANNUAL COST (2 semesters) | $74,812 | Per Year”
### `a531e8d0145b1607` Pacific University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.pacificu.edu/directory/student-affairs/office-financial-aid/undergrad-financial-aid-policies/satisfactory-academic-progress (sha256 0fec719744c9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Probation If students fail to meet satisfactory academic progress standards for a second consecutive term, they may appeal their financial aid suspension.”
  - sentence: sap_appeal ⟵ “Academic Plan If students fail to meet satisfactory academic progress at the end of the probationary period, they may appeal the Financial Aid Suspension.”
### `0737432f46b3a9a9` Pacific University — costs 2025-26 [new] (labeled_in_source)
- source: https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships/cost-attendance (sha256 baa59eadd31a)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 58348 ⟵ “Tuition & Fees | $58,348”
  - column:Room & Meals*: 16272 ⟵ “Room & Meals* | $16,272”
  - column:Books & Supplies: 1050 ⟵ “Books & Supplies | $1,050”
  - column:Personal Expenses: 1000 ⟵ “Personal Expenses | $1,000”
  - column:Transportation: 800 ⟵ “Transportation | $800”
  - column:Loan Fees: 72 ⟵ “Loan Fees | $72”
  - column:Total: 77542 ⟵ “Total | $77,542”
### `650cba9a8d554bb7` Pacific University — costs 2026-27 [new] (labeled_in_source)
- source: https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships (sha256 589722718aee)
- issues: conflicting_sources:https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships/cost-attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition & Fees: 60100 ⟵ “Tuition & Fees | $60,100”
  - column:Room & Board: 16834 ⟵ “Room & Board | $16,834”
  - column:Total Direct Cost: 76934 ⟵ “Total Direct Cost | $76,934”
### `b2b3dad0bb41b4df` Pacific University — costs 2026-27 [new] (labeled_in_source)
- source: https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships/cost-attendance (sha256 baa59eadd31a)
- issues: conflicting_sources:https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 60100 ⟵ “Tuition & Fees | $60,100”
  - column:Room & Meals*: 16834 ⟵ “Room & Meals* | $16,834”
  - column:Books & Supplies: 1050 ⟵ “Books & Supplies | $1,050”
  - column:Personal Expenses: 1000 ⟵ “Personal Expenses | $1,000”
  - column:Transportation: 800 ⟵ “Transportation | $800”
  - column:Loan Fees: 72 ⟵ “Loan Fees | $72”
  - column:Total: 79856 ⟵ “Total | $79,856”
### `13072604383e8e6a` Portland Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.pcc.edu/enroll/paying-for-college/financial-aid/review-award/change-in-situation/ (sha256 9c70dddd953c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Change in income appeal | Enroll at PCC Skip to page content Portland Community College | Portland, Oregon Menu Get Started Programs Class Schedule About Student Life Search Resources Contacts Calendars Give Log in to MyPCC Enroll at PCC PCC / Enroll at PCC / Paying for college / Financial aid / 3.”
  - sentence: need_based_special_circumstances ⟵ “Review and accept award / Change in income appeal If your income has changed since you submitted the FAFSA, let us know.”
  - sentence: need_based_special_circumstances ⟵ “The appeal process Review and complete the Change in Income Appeal.”
### `0d4685c1965d11be` Portland Community College — costs 2026-27 [new] (source_unlabeled)
- source: https://www.pcc.edu/international-students/student-resources/tuition-financial/ (sha256 82bb8c78da90)
- issues: residency_unknown, conflicting_sources:https://www.pcc.edu/enroll/paying-for-college/financial-aid/review-award/cost-of-attendance/,https://www.pcc.edu/international-students/admissions/required-documents/
- checks: {"columns": 1, "rows": 5}
  - column:Tuition*: 13410 ⟵ “Tuition* | $13,410”
  - column:Medical Insurance**: 2960 ⟵ “Medical Insurance** | $2,960”
  - column:Food and Housing PCC does not provide house. More information: 15453 ⟵ “Food and Housing PCC does not provide house. More information | $15,453”
  - column:Books and Supplies: 1700 ⟵ “Books and Supplies | $1,700”
  - column:Transportation: 910 ⟵ “Transportation | $910”
### `dece5156c3f23320` Portland Community College — costs 2026-27 [new] (source_unlabeled)
- source: https://www.pcc.edu/international-students/admissions/required-documents/ (sha256 3becff22c1e9)
- issues: residency_unknown, conflicting_sources:https://www.pcc.edu/enroll/paying-for-college/financial-aid/review-award/cost-of-attendance/,https://www.pcc.edu/international-students/student-resources/tuition-financial/
- checks: {"columns": 1, "rows": 6}
  - column:Tuition*: 13410 ⟵ “Tuition* | $13,410”
  - column:Class and activity fees*: 567 ⟵ “Class and activity fees* | $567”
  - column:Medical insurance**: 2960 ⟵ “Medical insurance** | $2,960”
  - column:Food and lodging PCC does not provide housing. More info: 15453 ⟵ “Food and lodging PCC does not provide housing. More info | $15,453”
  - column:Books and supplies: 1700 ⟵ “Books and supplies | $1,700”
  - column:Transportation: 910 ⟵ “Transportation | $910”
### `f804b119cbbd4e89` Portland Community College — costs 2026-27 [new] (labeled_in_source)
- source: https://www.pcc.edu/enroll/paying-for-college/financial-aid/review-award/cost-of-attendance/ (sha256 8122c1dafb84)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.pcc.edu/international-students/admissions/required-documents/,https://www.pcc.edu/international-students/student-resources/tuition-financial/
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - column:Tuition & fees: 1870 ⟵ “Tuition & fees | $1,870 | $3,740 | $5,610 | $7,480”
  - column:Books & supplies: 596 ⟵ “Books & supplies | $596 | $1,192 | $1,788 | $2,384”
  - column:Food & housing: 5324 ⟵ “Food & housing | $5,324 | $10,648 | $15,972 | $21,296”
  - column:Transportation: 319 ⟵ “Transportation | $319 | $638 | $957 | $1,276”
  - column:Personal: 762 ⟵ “Personal | $762 | $1,524 | $2,286 | $3,048”
  - column:Total expenses: 8871 ⟵ “Total expenses | $8,871 | $17,742 | $26,613 | $35,484”
  - column:Tuition & fees: 3740 ⟵ “Tuition & fees | $1,870 | $3,740 | $5,610 | $7,480”
  - column:Books & supplies: 1192 ⟵ “Books & supplies | $596 | $1,192 | $1,788 | $2,384”
  - column:Food & housing: 10648 ⟵ “Food & housing | $5,324 | $10,648 | $15,972 | $21,296”
  - column:Transportation: 638 ⟵ “Transportation | $319 | $638 | $957 | $1,276”
  - column:Personal: 1524 ⟵ “Personal | $762 | $1,524 | $2,286 | $3,048”
  - column:Total expenses: 17742 ⟵ “Total expenses | $8,871 | $17,742 | $26,613 | $35,484”
  - column:Tuition & fees: 5610 ⟵ “Tuition & fees | $1,870 | $3,740 | $5,610 | $7,480”
  - column:Books & supplies: 1788 ⟵ “Books & supplies | $596 | $1,192 | $1,788 | $2,384”
  - column:Food & housing: 15972 ⟵ “Food & housing | $5,324 | $10,648 | $15,972 | $21,296”
  - column:Transportation: 957 ⟵ “Transportation | $319 | $638 | $957 | $1,276”
  - column:Personal: 2286 ⟵ “Personal | $762 | $1,524 | $2,286 | $3,048”
  - column:Total expenses: 26613 ⟵ “Total expenses | $8,871 | $17,742 | $26,613 | $35,484”
  - column:Tuition & fees: 7480 ⟵ “Tuition & fees | $1,870 | $3,740 | $5,610 | $7,480”
  - column:Books & supplies: 2384 ⟵ “Books & supplies | $596 | $1,192 | $1,788 | $2,384”
  - column:Food & housing: 21296 ⟵ “Food & housing | $5,324 | $10,648 | $15,972 | $21,296”
  - column:Transportation: 1276 ⟵ “Transportation | $319 | $638 | $957 | $1,276”
  - column:Personal: 3048 ⟵ “Personal | $762 | $1,524 | $2,286 | $3,048”
  - column:Total expenses: 35484 ⟵ “Total expenses | $8,871 | $17,742 | $26,613 | $35,484”
### `m89feec56beef9f3` Portland Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.pcc.edu/university-transfer/transfer-agreements/psu/ (sha256 ff5ed3fbb969)
- issues: conflicting_sources:min_grade
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “A grade of C- or better must be earned in order for a class to transfer.”
  - min_grade: B ⟵ “To be eligible for transfer to PSU as part of this agreement, a grade of B or higher must be earned in all courses used toward the Physical Activity/Exercise All other courses must have a grade of at least a C or above. (See Credit Transfer Guide).”
### `250dd373e6ce6aef` Reed College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html (sha256 4efbcbe29aa1)
- issues: semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html,https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Reconsideration Requests See our guidelines for requesting a special circumstances review.”
### `2ea565557d7c6d95` Reed College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html (sha256 1d82e675707b)
- issues: semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html,https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Reconsideration Requests Guidelines for requesting a special circumstances review.”
### `7ad47fe6ba8bde7b` Reed College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html (sha256 94b650f62d2b)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html,https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Separation or divorce after the current financial aid applications are filed Death of a parent Non-discretionary expenses, such as: Unreimbursed medical expenses not already accounted for in the need analysis formulas If any of these special circumstances apply to you or your family, you may download and complete one of the forms below, as applicable, for the corresponding aid year for which you a”
### `ac809274f717db58` Reed College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html (sha256 94b650f62d2b)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Budget Adjustment Requests Federal regulations govern the items that may be included in the cost of attendance (budget).”
  - sentence: budget_increase ⟵ “Allowable budget increases are typically funded with additional student loan funds or Parent PLUS loans.”
### `df7dae4abe7492c8` Reed College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html (sha256 16825df1ab3f)
- issues: semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html,https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples may include a death in the family, student injury or illness, or other special circumstances include an explanation of the special, unusual, or extenuating circumstances causing undue hardship that prevented you from making SAP. include an explanation of what has changed in your situation that would allow you to demonstrate SAP by the end of the next semester.”
### `e3a7a8689bea4a44` Reed College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html (sha256 36ad40c7f637)
- issues: semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances - Admission & Aid - Reed College Skip to site navigation.”
### `570ba43f8a912e3e` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.socc.edu/wp-content/uploads/2026/06/SWOCC-2026-27-Satisfactory-Academic-Progress-SAP-Appeal.pdf (sha256 286f588ddc4f)
- issues: semantic_review_required, conflicting_sources:https://www.socc.edu/get-started/pay-for-college/financial-aid/,https://www.socc.edu/get-started/pay-for-college/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “2026-2027 Satisfactory Academic Progress (SAP) Appeal Student Information Student’s Last Name Student’s First Name Student’s M.I.”
  - sentence: sap_appeal ⟵ “Email: -fao@socc.edu Fax: (541) 888-7492 Page 1 | 6 2026-2027 Satisfactory Academic Progress (SAP) Appeal Writing The Appeal Submit your appeal as soon as possible once you become aware of your status change.”
  - sentence: sap_appeal ⟵ “Email: -fao@socc.edu Fax: (541) 888-7492 Page 2 | 6 2026-2027 Satisfactory Academic Progress (SAP) Appeal Completing The Appeal Please indicate the term and year for which you would like to have your financial aid reinstated: □ Summer 2025_____ □ Fall 2025 ________ □ Winter 2026 _______ □ Spring 2026 _______ Use additional paper, if needed, when answering questions. • You will only be granted two ”
  - sentence: sap_appeal ⟵ “Page 3 | 6 Email: -fao@socc.edu Fax: (541) 888-7492 2026-2027 Satisfactory Academic Progress (SAP) Appeal Include a detailed personal statement (refer to page 2 for details).”
  - sentence: sap_appeal ⟵ “Email: -fao@socc.edu Fax: (541) 888-7492 Page 4 | 6 2026-2027 Satisfactory Academic Progress (SAP) Appeal APPEAL DEADLINES The complete appeal package should include this form, your personal statement and supporting documentation.”
  - sentence: sap_appeal ⟵ “Email: -fao@socc.edu Fax: (541) 888-7492 Page 5 | 6 2026-2027 Satisfactory Academic Progress (SAP) Appeal Statement of Understanding I understand that decisions on appeals are processed on a case-by-case basis.”
### `8323b051e73ad9d2` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 bbd869c00d8b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The adjustments for a Reconsideration Request Appeal only affect need-based aid. · Dependency Override Appeal A dependency override occurs when a financial aid administrator exercises professional judgment and overrides the Department of Education’s criteria for dependent students.”
### `8507737be762c83a` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 bbd869c00d8b)
- issues: semantic_review_required, conflicting_sources:https://www.socc.edu/get-started/pay-for-college/financial-aid/,https://www.socc.edu/wp-content/uploads/2026/06/SWOCC-2026-27-Satisfactory-Academic-Progress-SAP-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Success Plan If you are placed on suspension and successfully appeal the decision, but your academic situation is such that it would be mathematically impossible for you to regain satisfactory academic progress eligibility during the next semester as required by federal satisfactory academic progress guidelines, the Financial Aid office may, at its sole”
  - sentence: sap_appeal ⟵ “If the "incomplete" grade results in your being placed on financial aid probation or suspension, once completed, you may appeal for a re-evaluation of Satisfactory Academic Progress by submitting the Satisfactory Academic Progress appeal form to the Financial Aid Office at Southwestern Oregon.”
  - sentence: sap_appeal ⟵ “Federal Work-Study Students If you participate in the Federal Work-Study program, are suspended from financial aid due to satisfactory academic progress or maximum timeframe, and your appeal has been denied, you will be ineligible for financial aid and cannot continue working until satisfactory academic progress is re-established.”
### `a278b682c51ec149` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 84982251f3ba)
- issues: semantic_review_required, conflicting_sources:https://www.socc.edu/get-started/pay-for-college/financial-aid/,https://www.socc.edu/wp-content/uploads/2026/06/SWOCC-2026-27-Satisfactory-Academic-Progress-SAP-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Success Plan If you are placed on suspension and successfully appeal the decision, but your academic situation is such that it would be mathematically impossible for you to regain satisfactory academic progress eligibility during the next semester as required by federal satisfactory academic progress guidelines, the Financial Aid office may, at its sole”
  - sentence: sap_appeal ⟵ “If the "incomplete" grade results in your being placed on financial aid probation or suspension, once completed, you may appeal for a re-evaluation of Satisfactory Academic Progress by submitting the Satisfactory Academic Progress appeal form to the Financial Aid Office at Southwestern Oregon.”
  - sentence: sap_appeal ⟵ “Federal Work-Study Students If you participate in the Federal Work-Study program, are suspended from financial aid due to satisfactory academic progress or maximum timeframe, and your appeal has been denied, you will be ineligible for financial aid and cannot continue working until satisfactory academic progress is re-established.”
### `a955b234372b05e9` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 84982251f3ba)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “You are required to have earned academic credit during the award year in which you received Pell Grant or Federal Direct Loan funds at each previously attended institution. · Reconsideration Request Appeal Southwestern Oregon’s Financial Aid office may take your special circumstances into account to make adjustments to your Student Aid Index (SAI) for educational expenses, standard budget, and fin”
  - sentence: need_based_special_circumstances ⟵ “You must have very unusual circumstances to warrant a second appeal.”
### `9e5baf9b5c8f2e83` Southwestern Oregon Community College — costs 2026-27 [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 84982251f3ba)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 5, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - with_parents_or_family:Books, Course Materials, Supplies and Equipment: 1500 ⟵ “Books, Course Materials, Supplies and Equipment | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - with_parents_or_family:Food and Housing: 7695 ⟵ “Food and Housing | $7,695 | $7,977 | $10,977 | $11,622 | $10,221”
  - with_parents_or_family:Misc. Personal Expenses: 1535 ⟵ “Misc. Personal Expenses | $1,535 | $1,535 | $1,535 | $1,535 | $1,535”
  - with_parents_or_family:Transportation Expenses: 1705 ⟵ “Transportation Expenses | $1,705 | $1,705 | $1,705 | $1,240 | $1,240”
  - with_parents_or_family:Total Cost of Attendance: 20160 ⟵ “Total Cost of Attendance | $20,160 | $20,442 | $23,442 | $23,622 | $22,221”
  - column:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - column:Books, Course Materials, Supplies and Equipment: 1500 ⟵ “Books, Course Materials, Supplies and Equipment | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - column:Food and Housing: 7977 ⟵ “Food and Housing | $7,695 | $7,977 | $10,977 | $11,622 | $10,221”
  - column:Misc. Personal Expenses: 1535 ⟵ “Misc. Personal Expenses | $1,535 | $1,535 | $1,535 | $1,535 | $1,535”
  - column:Transportation Expenses: 1705 ⟵ “Transportation Expenses | $1,705 | $1,705 | $1,705 | $1,240 | $1,240”
  - column:Total Cost of Attendance: 20442 ⟵ “Total Cost of Attendance | $20,160 | $20,442 | $23,442 | $23,622 | $22,221”
  - column:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - column:Books, Course Materials, Supplies and Equipment: 1500 ⟵ “Books, Course Materials, Supplies and Equipment | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - column:Food and Housing: 10977 ⟵ “Food and Housing | $7,695 | $7,977 | $10,977 | $11,622 | $10,221”
  - column:Misc. Personal Expenses: 1535 ⟵ “Misc. Personal Expenses | $1,535 | $1,535 | $1,535 | $1,535 | $1,535”
  - column:Transportation Expenses: 1705 ⟵ “Transportation Expenses | $1,705 | $1,705 | $1,705 | $1,240 | $1,240”
  - column:Total Cost of Attendance: 23442 ⟵ “Total Cost of Attendance | $20,160 | $20,442 | $23,442 | $23,622 | $22,221”
  - column:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - column:Books, Course Materials, Supplies and Equipment: 1500 ⟵ “Books, Course Materials, Supplies and Equipment | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - column:Food and Housing: 11622 ⟵ “Food and Housing | $7,695 | $7,977 | $10,977 | $11,622 | $10,221”
  - column:Misc. Personal Expenses: 1535 ⟵ “Misc. Personal Expenses | $1,535 | $1,535 | $1,535 | $1,535 | $1,535”
  - column:Transportation Expenses: 1240 ⟵ “Transportation Expenses | $1,705 | $1,705 | $1,705 | $1,240 | $1,240”
  - column:Total Cost of Attendance: 23622 ⟵ “Total Cost of Attendance | $20,160 | $20,442 | $23,442 | $23,622 | $22,221”
  - column:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - … 5 more rows
### `1433ca05fd80591b` Tillamook Bay Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/ (sha256 afc858298cbd)
- issues: semantic_review_required, conflicting_sources:https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/appeal-process/,https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/determining-satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students will receive notification via TBCC email within 2-4 weeks of appeal submission with one of the following results: Reinstatement on probation Reinstatement on an academic plan with requirements Denial of financial aid Probation Probation is granted upon the approval of a financial aid Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “Probation with an Academic Plan Probation with an Academic Plan is granted upon the approval of a Satisfactory Academic Progress Appeal with the condition the student follows an academic plan.”
### `21edeeb5c2323fc1` Tillamook Bay Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/appeal-process/ (sha256 05f3a7c31534)
- issues: semantic_review_required, conflicting_sources:https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/,https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/determining-satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students will receive notification via TBCC email within 2-4 weeks of appeal submission with one of the following results: Reinstatement on probation Reinstatement on an academic plan with requirements Denial of financial aid Probation Probation is granted upon the approval of a financial aid Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “Probation with an Academic Plan Probation with an Academic Plan is granted upon the approval of a Satisfactory Academic Progress Appeal with the condition the student follows an academic plan.”
### `c38d993236662f15` Tillamook Bay Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://tillamookbaycc.edu/wp-content/uploads/2025/11/25-26_SAP_Appeal.pdf (sha256 09b5be4a1e51)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “2025-2026 Satisfactory Academic Progress Appeal Please complete this form using blue or black ink Student Name: _________________________________________ ___________________ Last Name First Name/MI Student ID# Address: _____________________________________________ Phone: __________________ Street Address Apt # ______________________________________________________________________ City State Zip Co”
### `e92fa59571c5703d` Tillamook Bay Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/determining-satisfactory-academic-progress/ (sha256 3470cdc81c32)
- issues: semantic_review_required, conflicting_sources:https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/,https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/appeal-process/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Process Students may request financial aid reinstatement by completing a Satisfactory Academic Progress Appeal form.”
### `c85d3fcd718db39a` Treasure Valley Community College — costs 2026-27 [new] (source_unlabeled)
- source: https://www.tvcc.cc/admissions/international_students.cfm (sha256 6ab90709dd0a)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - column:Tuition and Fees*: 12000 ⟵ “Tuition and Fees* | $12,000”
  - column:Books and Supplies: 1500 ⟵ “Books and Supplies | $1,500”
  - column:Personal Expenditures: 1000 ⟵ “Personal Expenditures | $1,000”
  - column:International Student Insurance: 1000 ⟵ “International Student Insurance | $1,000”
  - column:Total Expenses: 24058 ⟵ “Total Expenses | $24,058”
### `23d41a50aaf4ac4e` Umpqua Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://umpqua.edu/become-a-student/financial-aid/ (sha256 301c2711d1c6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Visit ECMC Solutions Special Circumstances Has your family’s financial situation faced an extenuating loss in income compared to what was reported on the FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Request using 2025 income Special Circumstance Request using 2026 income Helpful Links Financial Aid Forms Ask Us Financial Aid Resources FAFSA Resources Financial Wellness Consumer Information Online Drop Box Physical Drop Box FAQ Financial Aid Handbook Loan Facts HEERF Cohort Default Rate Contact Office of Financial Aid 541-440-4602 541-440-4612 financialaid@umpqua.edu 8 a.m”
### `dcd8b5375a0cae20` Umpqua Community College — costs 2026-27 [new] (labeled_in_source)
- source: https://umpqua.edu/become-a-student/cost-of-attendance/ (sha256 e11d148d73b1)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "rows": 6}
  - column:Tuition and Fees: 7077 ⟵ “Tuition and Fees | $7,077 | $7,077”
  - column:Textbooks and Supplies: 1956 ⟵ “Textbooks and Supplies | $1,956 | $1,956”
  - column:Housing and Food: 8955 ⟵ “Housing and Food | $8,955 | $12,726”
  - column:Transportation: 2430 ⟵ “Transportation | $2,430 | $2,430”
  - column:Miscellaneous/Personal: 1740 ⟵ “Miscellaneous/Personal | $1,740 | $1,740”
  - column:Loan Fees*: 50 ⟵ “Loan Fees* | $50 | $50”
  - column:Tuition and Fees: 7077 ⟵ “Tuition and Fees | $7,077 | $7,077”
  - column:Textbooks and Supplies: 1956 ⟵ “Textbooks and Supplies | $1,956 | $1,956”
  - column:Housing and Food: 12726 ⟵ “Housing and Food | $8,955 | $12,726”
  - column:Transportation: 2430 ⟵ “Transportation | $2,430 | $2,430”
  - column:Miscellaneous/Personal: 1740 ⟵ “Miscellaneous/Personal | $1,740 | $1,740”
  - column:Loan Fees*: 50 ⟵ “Loan Fees* | $50 | $50”
### `925b276649d8e177` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/appeals (sha256 67ca02b93d00)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “In cases that impact federal student aid, HEA Sec. 479(a) authorizes the financial aid administrator to make adjustments on a case-by-case basis to the cost of attendance or the values of the data items required to calculate the student aid index to allow for treatment of special circumstances of an individual eligible applicant.”
### `a1b27cf191179ec7` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/satisfactory_academic_progress (sha256 a45f6aa74736)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uoregon.edu/appeals
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Petitions to cancel disqualification and to be reinstated academically to the University are completely separate processes from a SAP appeal.”
  - sentence: sap_appeal ⟵ “If your disqualification is cancelled or if you are reinstated academically and not meeting SAP requirements, you will still need to separately complete a SAP appeal for consideration of reinstating your financial aid.”
  - sentence: sap_appeal ⟵ “Additionally, we are unable to retroactively review a SAP appeal once a term is complete.”
  - sentence: sap_appeal ⟵ “Appeal Process If you are not making satisfactory academic progress, you will receive a notification at your UO e-mail address.”
  - sentence: sap_appeal ⟵ “We recommend submitting your SAP appeal as soon as possible, preferably well before the term begins; in order to give us time to review, process, and notify you of the decision.”
  - sentence: sap_appeal ⟵ “We are unable to retroactively review a SAP appeal once a term is complete.”
### `a2ee874bcb67904d` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/ (sha256 36ea279c9380)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Our evaluation of transfer applications is largely focused on determining if students meet our minimum admission requirements through cumulative GPA and coursework, though we also consider additional factors including special circumstances statements, application materials, grade trends, and academic potential for success.”
  - sentence: need_based_special_circumstances ⟵ “For applicants who do not meet our minimum requirements, we ask that you provide a personal statement (either included in the Special Circumstances portion of your application or uploaded in your UO application status portal) to share how/why you do not meet this requirement, and we will consider this information as part of our evaluation.”
  - sentence: need_based_special_circumstances ⟵ “We encourage transfers to share any relevant information or context if your academic performance was affected by special circumstances like serious illness or documented disability, or to otherwise provide us with information that we would not otherwise gather from your application materials.”
### `b336adf72cd0059b` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/ (sha256 f41e83a028b5)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Our evaluation of transfer applications is largely focused on determining if students meet our minimum admission requirements through cumulative GPA and coursework, though we also consider additional factors including special circumstances statements, application materials, grade trends, and academic potential for success.”
  - sentence: need_based_special_circumstances ⟵ “For applicants who do not meet our minimum requirements, we ask that you provide a personal statement (either included in the Special Circumstances portion of your application or uploaded in your UO application status portal) to share how/why you do not meet this requirement, and we will consider this information as part of our evaluation.”
  - sentence: need_based_special_circumstances ⟵ “We encourage transfers to share any relevant information or context if your academic performance was affected by special circumstances like serious illness or documented disability, or to otherwise provide us with information that we would not otherwise gather from your application materials.”
### `c8e8c22a579e2734` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/satisfactory_academic_progress (sha256 a45f6aa74736)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/appeals,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You are allowed to submit an appeal if you have mitigating circumstances, such as: a death of a relative, an injury or illness, or other special circumstances.”
### `cf3b5e1fb2a89510` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/ (sha256 3bea5295c708)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Personal statements and letters of recommendation (optional): You may send a personal statement with your application to explain special circumstances in your life that have affected you or your education.”
### `e7c86d34558e3529` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/appeals (sha256 67ca02b93d00)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uoregon.edu/satisfactory_academic_progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Information and the appeal process regarding failure to meet Satisfactory Academic Progress standards can be found on this webpage.”
### `eae441e970fc60b7` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.uoregon.edu/admissiontograduation/aidscholarships/ (sha256 96f1781a11eb)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Forbearance may be granted for up to 12 months for reasons such as: experiencing financial difficulties, such as medical expenses or change in income serving in AmeriCorps performing service that would qualify for partial loan forgiveness through the Department of Defense working in a medical or dental internship or residency program having student loan payments that are high in relation to your i”
### `0f31b35d7c3f2904` University of Portland — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/deadlines/index.html (sha256 3ca900e4fb0e)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.up.edu/admissions-aid/office-of-financial-aid/apply/special-circumstance.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “The Department of Education does not permit processing special circumstance appeals past the period of enrollment.”
  - sentence: need_based_special_circumstances ⟵ “The Department of Education does not permit processing special circumstance appeals past the period of enrollment.”
### `4fc488cfeae70056` University of Portland — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/deadlines/index.html (sha256 3ca900e4fb0e)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “The final deadline to submit loan applications and/or changes for the summer semester is 7 business days before your last scheduled summer class | April 24, 2026 | Deadline for Financial Aid Satisfactory Academic Progress appeals for summer semester | May 11, 2026 | Summer semester tuition due | May 18, 2026 Fall 2027 + Spring 2028 The 2027-2028 academic year includes summer 2027, fall 2027, and s”
  - sentence: sap_appeal ⟵ “The final deadline to submit loan applications and/or changes for the summer semester is 7 business days before your last scheduled summer class | April 23, 2027 | Summer semester tuition due | May 7, 2027 | Deadline for Financial Aid Satisfactory Academic Progress appeals for summer semester | May 10, 2027 Questions?”
### `7647aae25937a6b8` University of Portland — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/apply/special-circumstance.html (sha256 cf8ebc29d97c)
- issues: semantic_review_required, conflicting_sources:https://www.up.edu/admissions-aid/office-of-financial-aid/deadlines/index.html
- checks: {"negative_sentences": 0, "sentences": 14}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations that justify an aid administrator adjusting data elements in the Cost of Attendance or in the SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation, more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal Special Circumstance Appeals will be considered after you receive your initial award notification for the current aid year.”
  - sentence: need_based_special_circumstances ⟵ “After reviewing your special circumstance documentation, your aid package may remain the same, be increased, or reduced according to the financial information that has been submitted.”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special circumstance request does not guarantee an adjustment will be made to your aid package.”
### `8c817edda22cb126` University of Portland — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/apply/special-circumstance.html (sha256 cf8ebc29d97c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “A dependency override does not guarantee an adjustment will be made to your aid package.”
### `e4fbe2cdc9ff468c` University of Portland — costs 2025-26 [new] (labeled_in_source)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/costs/2526graduate-cost-of-attendance.html (sha256 da4e80483afb)
- issues: implausible_amount, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Professional Tuition (graduate level nursing, engineering, and business classes): 105 ⟵ “Professional Tuition (graduate level nursing, engineering, and business classes) | $105 | Credit”
  - column:Health Insurance: 1807 ⟵ “Health Insurance | $1,807 * | Semester”
### `43f1faa3cb52cb8b` Warner Pacific University — costs 2025-26 [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/wp-content/uploads/2025/01/2025-26-Cost-of-Attendance.pdf (sha256 3eccb3b2775b)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 2, "rows": 8}
  - column:Tuition and fees: 23500.0 ⟵ “Tuition and fees | $23,500.00 | $23,500.00”
  - column:Living Expenses: 14674.0 ⟵ “Living Expenses | $14,674.00 | $17,849.00”
  - column:& Equipment*: 58.0 ⟵ “& Equipment* | $58.00 | $58.00”
  - column:Miscellaneous Personal Expenses: 2377.0 ⟵ “Miscellaneous Personal Expenses | $2,377.00 | $2,377.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 41581.0 ⟵ “Total | $41,581.00 | $45,120.00”
  - column:Tuition and fees: 28860.0 ⟵ “Tuition and fees | $28,860.00 | $28,860.00”
  - column:Living Expenses: 14674.0 ⟵ “Living Expenses | $14,674.00 | $17,849.00”
  - column:& Equipment*: 58.0 ⟵ “& Equipment* | $58.00 | $58.00”
  - column:Miscellaneous Personal Expenses: 2377.0 ⟵ “Miscellaneous Personal Expenses | $2,377.00 | $2,377.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 46941.0 ⟵ “Total | $46,941.00 | $50,480.00”
  - column:Tuition and fees: 8160.0 ⟵ “Tuition and fees | $8,160.00 | $8,160.00”
  - column:Living Expenses: 15648.0 ⟵ “Living Expenses | $15,648.00 | $19,032.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 2544.0 ⟵ “Miscellaneous Personal Expenses | $2,544.00 | $2,544.00”
  - column:Federal Loan Fees: 132.0 ⟵ “Federal Loan Fees | $132.00 | $132.00”
  - column:Transportation: 960.0 ⟵ “Transportation | $960.00 | $1,296.00”
  - column:Total: 27564.0 ⟵ “Total | $27,564.00 | $31,284.00”
  - column:Tuition and fees: 15480.0 ⟵ “Tuition and fees | $15,480.00 | $15,480.00”
  - column:Living Expenses: 15648.0 ⟵ “Living Expenses | $15,648.00 | $19,032.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 2544.0 ⟵ “Miscellaneous Personal Expenses | $2,544.00 | $2,544.00”
  - … 38 more rows
### `63a313f743d1e9d8` Warner Pacific University — costs 2026-27 [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/wp-content/uploads/2025/12/2026-27-Cost-of-Attendance.pdf (sha256 780e28b2954b)
- issues: arrangement_unlabeled, multiple_total_rows, shared_site_attribution_review, conflicting_sources:https://www.warnerpacific.edu/admissions-aid/financial-aid/cost-of-attendance/
- checks: {"columns": 2, "rows": 8}
  - column:Tuition and fees: 24850.0 ⟵ “Tuition and fees | $24,850.00 | $24,850.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00 | $19,060.00”
  - column:& Equipment*: 70.0 ⟵ “& Equipment* | $70.00 | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00 | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 43390.0 ⟵ “Total | $43,390.00 | $47,146.00”
  - column:Tuition and fees: 30530.0 ⟵ “Tuition and fees | $30,530.00 | $30,530.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00 | $19,060.00”
  - column:& Equipment*: 70.0 ⟵ “& Equipment* | $70.00 | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00 | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 49070.0 ⟵ “Total | $49,070.00 | $52,826.00”
  - column:Tuition and fees: 14400.0 ⟵ “Tuition and fees | $14,400.00 | $14,400.00”
  - column:Living Expenses: 16704.0 ⟵ “Living Expenses | $16,704.00 | $20,328.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 1944.0 ⟵ “Miscellaneous Personal Expenses | $1,944.00 | $1,944.00”
  - column:Federal Loan Fees: 132.0 ⟵ “Federal Loan Fees | $132.00 | $132.00”
  - column:Transportation: 960.0 ⟵ “Transportation | $960.00 | $1,296.00”
  - column:Total: 34260.0 ⟵ “Total | $34,260.00 | $38,220.00”
  - column:Tuition and fees: 21840.0 ⟵ “Tuition and fees | $21,840.00”
  - column:Living Expenses: 20328.0 ⟵ “Living Expenses | $20,328.00”
  - column:Equipment*: 120.0 ⟵ “Equipment* | $120.00”
  - column:Miscellaneous Personal Expenses: 1944.0 ⟵ “Miscellaneous Personal Expenses | $1,944.00”
  - … 24 more rows
### `b55914932d9d9348` Warner Pacific University — costs 2026-27 [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/admissions-aid/financial-aid/cost-of-attendance/ (sha256 4fcf2beb2c2d)
- issues: shared_site_attribution_review, conflicting_sources:https://www.warnerpacific.edu/wp-content/uploads/2025/12/2026-27-Cost-of-Attendance.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and fees: 24850.0 ⟵ “Tuition and fees | $24,850.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00”
  - column:Books, Course Materials, Supplies & Equipment*: 70.0 ⟵ “Books, Course Materials, Supplies & Equipment* | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00”
  - column:Total: 43390.0 ⟵ “Total | $43,390.00”
### `m2c86ef937de539e` Warner Pacific University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.warnerpacific.edu/wp-content/uploads/2024/11/Columbia-Gorge-WPU-GE-Core-Transfer-Guide.pdf (sha256 729d506132d5)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"], "merged_pages": 8}
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
### `93273a111662d976` Warner Pacific University Professional and Graduate Studies — costs 2026-27 [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/admissions-aid/financial-aid/cost-of-attendance/ (sha256 4fcf2beb2c2d)
- issues: shared_site_attribution_review, conflicting_sources:https://www.warnerpacific.edu/wp-content/uploads/2025/12/2026-27-Cost-of-Attendance.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and fees: 24850.0 ⟵ “Tuition and fees | $24,850.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00”
  - column:Books, Course Materials, Supplies & Equipment*: 70.0 ⟵ “Books, Course Materials, Supplies & Equipment* | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00”
  - column:Total: 43390.0 ⟵ “Total | $43,390.00”
### `a4f30b46895d351f` Warner Pacific University Professional and Graduate Studies — costs 2025-26 [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/wp-content/uploads/2025/01/2025-26-Cost-of-Attendance.pdf (sha256 3eccb3b2775b)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 2, "rows": 8}
  - column:Tuition and fees: 23500.0 ⟵ “Tuition and fees | $23,500.00 | $23,500.00”
  - column:Living Expenses: 14674.0 ⟵ “Living Expenses | $14,674.00 | $17,849.00”
  - column:& Equipment*: 58.0 ⟵ “& Equipment* | $58.00 | $58.00”
  - column:Miscellaneous Personal Expenses: 2377.0 ⟵ “Miscellaneous Personal Expenses | $2,377.00 | $2,377.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 41581.0 ⟵ “Total | $41,581.00 | $45,120.00”
  - column:Tuition and fees: 28860.0 ⟵ “Tuition and fees | $28,860.00 | $28,860.00”
  - column:Living Expenses: 14674.0 ⟵ “Living Expenses | $14,674.00 | $17,849.00”
  - column:& Equipment*: 58.0 ⟵ “& Equipment* | $58.00 | $58.00”
  - column:Miscellaneous Personal Expenses: 2377.0 ⟵ “Miscellaneous Personal Expenses | $2,377.00 | $2,377.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 46941.0 ⟵ “Total | $46,941.00 | $50,480.00”
  - column:Tuition and fees: 8160.0 ⟵ “Tuition and fees | $8,160.00 | $8,160.00”
  - column:Living Expenses: 15648.0 ⟵ “Living Expenses | $15,648.00 | $19,032.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 2544.0 ⟵ “Miscellaneous Personal Expenses | $2,544.00 | $2,544.00”
  - column:Federal Loan Fees: 132.0 ⟵ “Federal Loan Fees | $132.00 | $132.00”
  - column:Transportation: 960.0 ⟵ “Transportation | $960.00 | $1,296.00”
  - column:Total: 27564.0 ⟵ “Total | $27,564.00 | $31,284.00”
  - column:Tuition and fees: 15480.0 ⟵ “Tuition and fees | $15,480.00 | $15,480.00”
  - column:Living Expenses: 15648.0 ⟵ “Living Expenses | $15,648.00 | $19,032.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 2544.0 ⟵ “Miscellaneous Personal Expenses | $2,544.00 | $2,544.00”
  - … 38 more rows
### `e49f4911176690dc` Warner Pacific University Professional and Graduate Studies — costs 2026-27 [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/wp-content/uploads/2025/12/2026-27-Cost-of-Attendance.pdf (sha256 780e28b2954b)
- issues: arrangement_unlabeled, multiple_total_rows, shared_site_attribution_review, conflicting_sources:https://www.warnerpacific.edu/admissions-aid/financial-aid/cost-of-attendance/
- checks: {"columns": 2, "rows": 8}
  - column:Tuition and fees: 24850.0 ⟵ “Tuition and fees | $24,850.00 | $24,850.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00 | $19,060.00”
  - column:& Equipment*: 70.0 ⟵ “& Equipment* | $70.00 | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00 | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 43390.0 ⟵ “Total | $43,390.00 | $47,146.00”
  - column:Tuition and fees: 30530.0 ⟵ “Tuition and fees | $30,530.00 | $30,530.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00 | $19,060.00”
  - column:& Equipment*: 70.0 ⟵ “& Equipment* | $70.00 | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00 | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 49070.0 ⟵ “Total | $49,070.00 | $52,826.00”
  - column:Tuition and fees: 14400.0 ⟵ “Tuition and fees | $14,400.00 | $14,400.00”
  - column:Living Expenses: 16704.0 ⟵ “Living Expenses | $16,704.00 | $20,328.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 1944.0 ⟵ “Miscellaneous Personal Expenses | $1,944.00 | $1,944.00”
  - column:Federal Loan Fees: 132.0 ⟵ “Federal Loan Fees | $132.00 | $132.00”
  - column:Transportation: 960.0 ⟵ “Transportation | $960.00 | $1,296.00”
  - column:Total: 34260.0 ⟵ “Total | $34,260.00 | $38,220.00”
  - column:Tuition and fees: 21840.0 ⟵ “Tuition and fees | $21,840.00”
  - column:Living Expenses: 20328.0 ⟵ “Living Expenses | $20,328.00”
  - column:Equipment*: 120.0 ⟵ “Equipment* | $120.00”
  - column:Miscellaneous Personal Expenses: 1944.0 ⟵ “Miscellaneous Personal Expenses | $1,944.00”
  - … 24 more rows
### `mb3ab929d5ef2aae` Warner Pacific University Professional and Graduate Studies — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.warnerpacific.edu/wp-content/uploads/2024/11/Columbia-Gorge-WPU-GE-Core-Transfer-Guide.pdf (sha256 729d506132d5)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"], "merged_pages": 8}
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
### `6d0e5af82bbac8a5` Western Oregon University — appeals 2026-27 [new] (labeled_in_source)
- source: https://wou.edu/finaid/managing-my-aid/satisfactory-academic-progress/ (sha256 162481acef6d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If a SAP Appeal is requested it will also appear on your Home tab.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeals must be submitted by the census date each term to be considered for Financial Aid for that term.”
### `88c7ec87bf6a99e3` Western Oregon University — appeals 2024-25 [new] (labeled_in_title)
- source: https://cdn.wou.edu/finaid/files/2025/07/Financial-Aid-Eligibility-and-SAP-Policy-GR-rev-01.02.2025.pdf (sha256 911c80938c06)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “WOU Financial Aid Office Welcome Center 140, 345 Monmouth Ave N  Monmouth, OR 97361  Tel: 503-838-8475  Fax: 503-838-8200  wou.edu/finaid  finaid@wou.edu Satisfactory Academic Progress Appeal Process If you encounter circumstances that prevent you from making any of the SAP standards listed above, you may submit an appeal to our office.”
  - sentence: sap_appeal ⟵ “Your appeal should include: 1) The Satisfactory Academic Progress Appeal Form 2) Documentation of your circumstance (e.g. medical records). 3) For GPA (Qualitative) or Pace (Quantitative): For Excessive Credit Hours (Max.”
  - sentence: sap_appeal ⟵ “Submit a new SAP appeal detailing the extenuating circumstances that were beyond your control, and which interfered with your ability to academically perform.”
  - sentence: sap_appeal ⟵ “You will be notified of the outcome of your SAP appeal in writing via your WOU e-mail account.”
  - sentence: sap_appeal ⟵ “SAP Appeal Deadline SAP appeals must be submitted and approved two weeks prior to the start of the term for which you are requesting federal aid.”
### `ddb4e1f5e567338d` Western Oregon University — appeals 2025-26 [new] (labeled_in_source)
- source: https://cdn.wou.edu/finaid/files/2025/11/Financial-Aid-Eligibility-and-SAP-Policy-UG-rev-10.22.2025.pdf (sha256 466493864223)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “WOU Financial Aid Office Welcome Center 140, 345 Monmouth Ave N  Monmouth, OR 97361  Tel: 503-838-8475  wou.edu/finaid  finaid@wou.edu Satisfactory Academic Progress Appeal Process If you fail to make SAP, you may submit the Satisfactory Academic Progress Appeal Form and supporting documents to the Financial Aid Office to be considered for additional aid eligibility.”
  - sentence: sap_appeal ⟵ “SAP Appeal forms with complete documentation must be received by Census Date (second Friday each term).”
  - sentence: sap_appeal ⟵ “Appeals received after Census Date will not be considered until the following term (after grades post), and aid will not be paid retroactively upon review of your SAP Appeal.”
  - sentence: sap_appeal ⟵ “You will be notified of the outcome of your SAP appeal in writing via your WOU email account.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeal Form 2.”
### `39a98ab94361a1c9` Western Oregon University — costs 2025-26 [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 a9e06917b93d)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Tuition: 36640 ⟵ “Tuition | $27,480 | $36,640 | $36,640”
  - column:Fees: 1472 ⟵ “Fees | $1,110 | $1,472 | $1,472”
  - column:Loan Origination Fees: 2232 ⟵ “Loan Origination Fees | $1,164 | $2,232 | $2,232”
  - column:Housing: 10408 ⟵ “Housing | $7,806 | $10,408 | $10,408”
  - column:Food: 10956 ⟵ “Food | $8,217 | $10,956 | $10,956”
  - column:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,200 | $1,000 | $300”
  - column:Transportation: 1916 ⟵ “Transportation | $1,437 | $1,916 | $1,916”
  - column:Miscellaneous: 3000 ⟵ “Miscellaneous | $2,250 | $3,000 | $3,000”
  - column:Clinical Expenses: 100 ⟵ “Clinical Expenses | $1,750 | $100 | $1,750”
  - column:Total: 67724 ⟵ “Total | $52,414 | $67,724 | $68,674”
### `cab5b5a2f40f9d58` Western Oregon University — costs 2026-27 [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 a9e06917b93d)
- issues: residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 15525 ⟵ “Tuition | $15,525 | $15,525 | $15,525”
  - on_campus:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - on_campus:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - on_campus:Housing: 7597 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - on_campus:Food: 5387 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - on_campus:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - on_campus:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - on_campus:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - on_campus:Total: 35829 ⟵ “Total | $35,829 | $38,867 | $27,587”
  - off_campus_not_with_family:Tuition: 15525 ⟵ “Tuition | $15,525 | $15,525 | $15,525”
  - off_campus_not_with_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - off_campus_not_with_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - off_campus_not_with_family:Housing: 7805 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - off_campus_not_with_family:Food: 8217 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - off_campus_not_with_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - off_campus_not_with_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - off_campus_not_with_family:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - off_campus_not_with_family:Total: 38867 ⟵ “Total | $35,829 | $38,867 | $27,587”
  - with_parents_or_family:Tuition: 15525 ⟵ “Tuition | $15,525 | $15,525 | $15,525”
  - with_parents_or_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - with_parents_or_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - with_parents_or_family:Housing: 2501 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - with_parents_or_family:Food: 2241 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - with_parents_or_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - with_parents_or_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - … 2 more rows
### `e0370d7ffc0ad613` Western Oregon University — costs 2024-25 [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 a9e06917b93d)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Tuition: 36640 ⟵ “Tuition | $27,480 | $36,640 | $36,640”
  - column:Fees: 1472 ⟵ “Fees | $1,110 | $1,472 | $1,472”
  - column:Loan Origination Fees: 2232 ⟵ “Loan Origination Fees | $1,164 | $2,232 | $2,232”
  - column:Housing: 10408 ⟵ “Housing | $7,806 | $10,408 | $10,408”
  - column:Food: 10956 ⟵ “Food | $8,217 | $10,956 | $10,956”
  - column:Books & Supplies: 300 ⟵ “Books & Supplies | $1,200 | $1,000 | $300”
  - column:Transportation: 1916 ⟵ “Transportation | $1,437 | $1,916 | $1,916”
  - column:Miscellaneous: 3000 ⟵ “Miscellaneous | $2,250 | $3,000 | $3,000”
  - column:Clinical Expenses: 1750 ⟵ “Clinical Expenses | $1,750 | $100 | $1,750”
  - column:Total: 68674 ⟵ “Total | $52,414 | $67,724 | $68,674”
### `7dee7d2502e35879` Willamette University — costs 2026-27 [new] (labeled_in_source)
- source: https://willamette.edu/cost-aid/tuition (sha256 a63d47dd4885)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "rows": 7}
  - column:Tuition: 28320 ⟵ “Tuition | $28,320 | Per semester”
  - column:Student Activity Fee1: 146 ⟵ “Student Activity Fee1 | $146 | Per semester”
  - column:Meal Plan – Living on campus (14-meal plan): 4270 ⟵ “Meal Plan – Living on campus (14-meal plan) | $4,270 | Per semester”
  - column:Housing – Living on campus3 (Standard double room): 4595 ⟵ “Housing – Living on campus3 (Standard double room) | $4,595 | Per semester”
  - column:Residence Hall Fee: 75 ⟵ “Residence Hall Fee | $75 | Per semester”
  - column:Sub-Total: 37406 ⟵ “Sub-Total | $37,406 | Per semester”
  - column:ANNUAL COST (2 semesters): 74812 ⟵ “ANNUAL COST (2 semesters) | $74,812 | Per Year”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 135; pages by category: admissions_tests 39, ap_credit 16, cost_of_attendance 5, degree_requirements 28, dual_enrollment 1, ib_credit 14, merit_scholarships 16, residency 3, statewide_articulation 30, transfer_credit 28, tuition_fees 3

## Blocked by the site (every request refused; needs the browser fallback)

- New Hope Christian College-Eugene (`ipeds-208725`)
- Mt Hood Community College (`ipeds-209250`)
- Rogue Community College (`ipeds-209940`)

## Leads: official pages found with no extracted record

- Blue Mountain Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Bushnell University: tuition_fees, cost_of_attendance, merit_scholarships, clep_credit, statewide_articulation, degree_requirements
- Central Oregon Community College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Chemeketa Community College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Clackamas Community College: admissions_tests, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Clatsop Community College: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Columbia Gorge Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Corban University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit
- Eastern Oregon University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- George Fox University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, degree_requirements
- Klamath Community College: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, degree_requirements
- Lane Community College: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit
- Lewis & Clark College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Linfield University: tuition_fees, cost_of_attendance, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Linn-Benton Community College: tuition_fees, merit_scholarships
- Mount Angel Seminary: admissions_tests, degree_requirements
- Multnomah University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation
- Oregon Coast Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Oregon Institute of Technology: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Oregon State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency, degree_requirements
- Oregon State University-Cascades Campus: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, statewide_articulation, residency, degree_requirements
- Pacific Bible College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit
- Pacific Northwest College of Art: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements, aid_appeals
- Pacific University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Portland Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Portland State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- Reed College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Southern Oregon University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Southwestern Oregon Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, degree_requirements
- Tillamook Bay Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Treasure Valley Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, aid_appeals
- Umpqua Community College: cost_of_attendance, common_data_set, dual_enrollment, transfer_credit, residency, degree_requirements
- University of Oregon: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- University of Portland: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment
- Warner Pacific University: merit_scholarships, degree_requirements, aid_appeals
- Warner Pacific University Professional and Graduate Studies: merit_scholarships, degree_requirements, aid_appeals
- Western Oregon University: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Willamette University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements, aid_appeals
