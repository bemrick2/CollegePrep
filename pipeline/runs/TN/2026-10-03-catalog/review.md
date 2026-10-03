# Review queue — TN (2026-27)

Pages fetched: 420; failures: 13. Candidates: 67 (13 without issues, 54 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 10 | 0 | 0 | 0 | 3 | 0 | 46 |
| cost_of_attendance | 6 | 1 | 0 | 0 | 4 | 0 | 48 |
| admissions_tests | 2 | 0 | 0 | 1 | 5 | 0 | 51 |
| common_data_set | 2 | 0 | 0 | 1 | 0 | 5 | 51 |
| merit_scholarships | 3 | 3 | 1 | 0 | 2 | 1 | 49 |
| ap_credit | 1 | 3 | 0 | 1 | 2 | 2 | 50 |
| clep_credit | 1 | 2 | 0 | 0 | 1 | 4 | 51 |
| ib_credit | 1 | 1 | 0 | 0 | 1 | 4 | 52 |
| dual_enrollment | 1 | 0 | 4 | 0 | 1 | 1 | 52 |
| transfer_credit | 0 | 7 | 0 | 0 | 6 | 0 | 46 |
| statewide_articulation | 0 | 0 | 0 | 0 | 2 | 4 | 53 |
| residency | 0 | 0 | 0 | 0 | 3 | 3 | 53 |
| degree_requirements | 1 | 1 | 0 | 0 | 5 | 0 | 52 |
| aid_appeals | 1 | 1 | 0 | 5 | 0 | 0 | 52 |

## Ready for review (13)

### `01d1376b53b7d3db` Carson-Newman University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/types-of-aid/scholarships/ (sha256 83a27b205766)
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '<2.5', 'amount_text': '$10,000'}, {'gpa': '2.5', 'amount_text': '$12,000'}, {'gpa': '3.0', 'amount_text': '$14,000'}, {'gpa': '3.5', 'amount_text': '$16,000'}, {'gpa': '3.9', 'amount_text': '$18,000'}] ⟵ “GPA | Merit || <2.5 | $10,000 || 2.5 | $12,000 || 3.0 | $14,000 || 3.5 | $16,000 || 3.9 | $18,000”
  - gpa_requirement: Tiered by GPA: <2.5 → $10,000; 2.5 → $12,000; 3.0 → $14,000; 3.5 → $16,000; 3.9 → $18,000 ⟵ “GPA | Merit || <2.5 | $10,000 || 2.5 | $12,000 || 3.0 | $14,000 || 3.5 | $16,000 || 3.9 | $18,000”
### `93af76cc253f8e9f` Carson-Newman University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.cn.edu/wp-content/uploads/2025/11/2025-26-Dual-Enrollment-Agreement-Form.pdf (sha256 19f76c79a5f9)
- checks: {"fields": ["max_credit_hours_per_term", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - max_credit_hours_per_term: 14 ⟵ “•   Students may take up to a maximum of 14 hours of Dual Enrollment courses in each semester at the current Dual”
  - per_credit_hour_charge: 174 ⟵ “Enrollment tuition rate of $174 per credit hour with a $10 per credit hour technology fee. In addition to the tuition and”
  - per_credit_hour_charge: 10 ⟵ “Enrollment tuition rate of $174 per credit hour with a $10 per credit hour technology fee. In addition to the tuition and”
### `585a7b789ef7b7d1` East Tennessee State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php (sha256 1c8b6a0cbbba)
- checks: {"thresholds": null}
  - award_amount_text: Provides In-StateTuition Rate ⟵ “More Info | Public Service Corps Scholarship | Provides In-StateTuition Rate | N/A | See Requirements”
### `c48e22b72c8c2caa` East Tennessee State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php (sha256 1c8b6a0cbbba)
- checks: {"thresholds": {"gpa_min": 3.2}}
  - award_amount_text: Provides In-StateTuition Rate ⟵ “More Info | STEM Community Outreach Scholarship | Provides In-StateTuition Rate | 3.2 | See Requirements”
  - gpa_requirement: 3.2 ⟵ “More Info | STEM Community Outreach Scholarship | Provides In-StateTuition Rate | 3.2 | See Requirements”
### `e51adf3359bfad02` East Tennessee State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php (sha256 1c8b6a0cbbba)
- checks: {"thresholds": null}
  - award_amount_text: Provides In-StateTuition Rate ⟵ “More Info | Creative Arts Scholarship | Provides In-StateTuition Rate | See Requirements | See Requirements”
### `fbf7ce5c78359ff1` East Tennessee State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.etsu.edu/admissions/dual_enrollment/ (sha256 f50a621e2adf)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted"], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “3.0 or higher high school GPA on a 4.0 scale”
  - per_credit_hour_charge: 100 ⟵ “enrollment grant. After the first five free classes, the grant will provide $100/credit”
  - eligibility_tier: 3.0 ⟵ “Dual Enrollment students who present a 3.0 or higher high school GPA, may qualify”
  - state_grant_accepted: True ⟵ “Students admitted as dual enrollment students may be eligible for the Dual Enrollment Grant. In addition, students may qualify for an ETSU Dual Enrollment Scholarship. Consult”
### `26804fbd6793034d` Tennessee Technological University — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
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
### `e0f3f4396a8b9c8f` Tennessee Technological University — costs 2026-27 · residency=in_state [same] (labeled_in_source)
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
### `f22e1a0d94616e57` Tennessee Technological University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.tntech.edu/admissions/dualenrollment/cost.php (sha256 cbf78e500fea)
- checks: {"fields": ["state_grant_accepted"], "tiers": 0}
  - state_grant_accepted: True ⟵ “To be eligible for the TSAC Dual Enrollment Grant, you must:”
### `1da2fc639dfb100a` The University of Tennessee-Chattanooga — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/admissions/dual-enrollment (sha256 139bc7b18e3f)
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Is your high school grade point average 3.0 or higher?”
  - state_grant_accepted: True ⟵ “3. Apply for Tennessee Dual Enrollment Grant”
  - state_grant_accepted: True ⟵ “Apply for TN DE Grant”
### `609e1d0d6734ed54` The University of Tennessee-Chattanooga — credit_policies 2026-27 · policy_kind=CLEP [changed] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/clep (sha256 c0c418fe6480)
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
### `c17e3bae072922f6` The University of Tennessee-Chattanooga — credit_policies 2026-27 · policy_kind=IB [same] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/ib-exam (sha256 b54b162a3739)
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
### `ccd5bfe7cf47f469` The University of Tennessee-Chattanooga — credit_policies 2026-27 · policy_kind=AP [changed] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/ap-exam (sha256 40643fcb6247)
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

## Exceptions (54)

### `3722e673f34c337e` Carson-Newman University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cn.edu/wp-content/uploads/2024/06/SAP-Appeal-Form97.pdf (sha256 2c19589aa0af)
- issues: semantic_review_required, conflicting_sources:https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-important-dates/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Carson-Newman University Financial Aid Office • 1645 Russell Avenue • Jefferson City, TN 37760 Financial Aid Office • (800) 678-9061 • (865) 471-3247 • Fax (865) 471-2035 financialaid@cn.edu • www.cn.edu Satisfactory Academic Progress Appeal Form Satisfactory Academic Progress (SAP) Overview Federal regulations require that all students meet minimum qualitative (grades) and minimum quantitative (h”
  - sentence: sap_appeal ⟵ “SAP Appeal Process If extenuating circumstances precluded you from meeting the standards, you may file an appeal.”
### `4252ea3a3d97cc31` Carson-Newman University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-forms/ (sha256 ca72f296f2d5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “Dependency Override Appeal Application – A student may need to request an override to their dependency status due to unusual and unavoidable circumstances.”
  - sentence: dependency_override ⟵ “A Dependency Status Appeal Application is considered on a case-by-case basis depending on the situation and supporting documentation provided.”
  - sentence: dependency_override ⟵ “Dependency Override Appeal Application – A student may need to request an override to their dependency status due to unusual and unavoidable circumstances.”
  - sentence: dependency_override ⟵ “A Dependency Status Appeal Application is considered on a case-by-case basis depending on the situation and supporting documentation provided.”
### `4682cf577334df3f` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Independent-Appeal.pdf (sha256 ca619c461fc9)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Carson-Newman University 2025-2026 Special Circumstance Appeal for Independent Students ______________________________________________________________ ___________________________________ Student’s Last Name Student’s First Name Student’s M.I.”
  - sentence: need_based_special_circumstances ⟵ “Student’s Identification (ID) Number ______________________________________________________________ ___________________________________ Student’s E-Mail Address Student’s Home/Cell Phone Number This Appeal is a request for a review of special circumstances that you feel may change your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Please note: Loss of income for the 2023 IRS Tax Return calendar year will NOT be considered for special circumstances ___ Copy of 2024 IRS Tax Return Transcript or signed copy of 2024 appeal as this process will be based on current year data only.”
### `90cb605425d821b5` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf (sha256 485c9c14b0e0)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Independent-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Carson-Newman University 2025-2026 Special Circumstances Appeal for Dependent Students ______________________________________________________________ ___________________________________ Student’s Last Name Student’s First Name Student’s M.I.”
  - sentence: need_based_special_circumstances ⟵ “Student’s Identification (ID) Number ______________________________________________________________ ___________________________________ Student’s E-Mail Address Student’s Home/Cell Phone Number This Appeal is a request for a review of special circumstances that you feel may change your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Please note: Loss of income for the 2023 IRS Tax Return calendar year will NOT be considered for special circumstances ___ Copy of 2024 IRS Tax Return Transcript or signed copy of 2024 appeal as this process will be based on current year data only.”
### `b06b5e871156aace` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Independent-Appeal.pdf (sha256 ca619c461fc9)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment refers to the school’s authority to make adjustments to the data elements reported on the Free Application for Federal Student Aid (FAFSA) so that the Department of Education can recalculate the Student Aid Index (SAI).”
### `ccde3144671b080f` Carson-Newman University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-important-dates/ (sha256 fc82be26a5fa)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2024/06/SAP-Appeal-Form97.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Complete verification (if required) by May 2, 2025 Accept/reject aid by May 5, 2025 New loan borrowers and TEACH Grant recipients need to complete loan and/or TEACH paperwork by May 5, 2025 Notify Financial Aid about any housing and/or enrollment changes by May 2, 2025 Satisfactory Academic Progress Appeal deadline is May 2, 2025, or ASAP after Spring grades are reported and SAP status is calculat”
### `d6fcec6916eb8e2f` Carson-Newman University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-forms/ (sha256 ca72f296f2d5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Verification paperwork is attached to the Special Circumstances Appeal form.”
  - sentence: need_based_special_circumstances ⟵ “Keep in mind that in order to submit a Special Circumstance Appeal for the 2026-27 academic year, the 2025 taxes must be complete to attach to the appeal, and the student must have already received his/her original aid offer.”
  - sentence: need_based_special_circumstances ⟵ “Independent Special Circumstance Appeal Form – Please complete this form along with supporting documentation if you have suffered a loss of income.”
  - sentence: need_based_special_circumstances ⟵ “Verification paperwork is attached to the Special Circumstances Appeal form.”
  - sentence: need_based_special_circumstances ⟵ “Fall 2025, Spring 2026 & Summer 2026 Dependent Verification Worksheet Independent Verification Worksheet Dependent Special Circumstance Appeal Form – Please complete this form along with supporting documentation if you have suffered a loss of income.”
  - sentence: need_based_special_circumstances ⟵ “Verification paperwork is attached to the Special Circumstances Appeal form.”
### `fdd1747b66a80035` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf (sha256 485c9c14b0e0)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Independent-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment refers to the school’s authority to make adjustments to the data elements reported on the Free Application for Federal Student Aid (FAFSA) so that the Department of Education can recalculate the Expected Family Contribution (SAI).”
### `c452bfcc01addb12` Carson-Newman University — awards 2025-26 [same] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/types-of-aid/scholarships/ (sha256 83a27b205766)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '2.2', 'amount_text': '$8,000'}, {'gpa': '2.75', 'amount_text': '$10,000'}, {'gpa': '3.5', 'amount_text': '$12,000'}, {'gpa': '3.75', 'amount_text': '$14,000'}, {'gpa': '3.9', 'amount_text': '$16,000'}] ⟵ “GPA | Merit || 2.2 | $8,000 || 2.75 | $10,000 || 3.5 | $12,000 || 3.75 | $14,000 || 3.9 | $16,000”
  - gpa_requirement: Tiered by GPA: 2.2 → $8,000; 2.75 → $10,000; 3.5 → $12,000; 3.75 → $14,000; 3.9 → $16,000 ⟵ “GPA | Merit || 2.2 | $8,000 || 2.75 | $10,000 || 3.5 | $12,000 || 3.75 | $14,000 || 3.9 | $16,000”
### `666d72c4faf3dbbb` Carson-Newman University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/tuition-costs/ (sha256 4daabe57bedc)
- issues: components_do_not_reconcile, conflicting_sources:https://www.cn.edu/admissions-and-aid/financial-aid/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": false, "rows": 2}
- change total_direct_cost: `55300` → `55100`
  - column:Tuition & Fees: 42500 ⟵ “Tuition & Fees | $42,500”
  - column:Total Estimated Direct (billable) costs:: 55100 ⟵ “Total Estimated Direct (billable) costs: | $55,100”
### `f06dee3d7094e419` Carson-Newman University — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/ (sha256 ed693223d0c2)
- issues: conflicting_sources:https://www.cn.edu/admissions-and-aid/financial-aid/tuition-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 42500 ⟵ “Tuition | $21,250 | $42,500”
  - column:Residential Student Fee: 200 ⟵ “Residential Student Fee |  | 200”
  - column:Meal Plan*: 6300 ⟵ “Meal Plan* | 3,150 | 6,300”
  - column:Room**: 6300 ⟵ “Room** | 3,150 | 6,300”
  - column:Total: 55300 ⟵ “Total | $27,550 | $55,300”
### `753e4dc4760da76a` Carson-Newman University — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/dual-enrollment/ (sha256 9bfd656a8683)
- issues: stale_year_label:2025-26
- checks: {"fields": ["alt_min_act", "alt_min_sat", "max_credit_hours_per_term", "min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Minimum GPA of 3.0 (on 4.0 scale) OR minimum GPA of 2.0 with 19+ ACT composite score, 1030 SAT (combined Evidence-Based Reading and Writing and Math), or 63 Classical Learning Test (CLT)”
  - max_credit_hours_per_term: 14 ⟵ “Allowed to take a maximum of 14 credit hours per semester”
  - per_credit_hour_charge: 190 ⟵ “Dual Enrollment is $190 per credit hour (an additional $10 per credit hour Technology Fee.) Tennessee resident students may qualify for the Tennessee Dual Enrollment Grant. Most dual enrollment courses are covered by the grant if students qualify, complete all appropriate paperwork, and meet all eli”
  - per_credit_hour_charge: 10 ⟵ “Dual Enrollment is $190 per credit hour (an additional $10 per credit hour Technology Fee.) Tennessee resident students may qualify for the Tennessee Dual Enrollment Grant. Most dual enrollment courses are covered by the grant if students qualify, complete all appropriate paperwork, and meet all eli”
  - per_credit_hour_charge: 100 ⟵ “For 2025-26 school year, the TN Dual Enrollment grant covers full tuition and technology fees toward your first (5) courses. Additional six – ten courses are $100 per credit hour. Students must maintain a minimum 2.0 GPA to keep the grant.”
  - state_grant_accepted: True ⟵ “For 2025-26 school year, the TN Dual Enrollment grant covers full tuition and technology fees toward your first (5) courses. Additional six – ten courses are $100 per credit hour. Students must maintain a minimum 2.0 GPA to keep the grant.”
  - per_credit_hour_charge: 174 ⟵ “$174/credit hour | $10/credit hour – Technology Fee. Tennessee residents are eligible for the TN Dual Enrollment Grant. Visit their website for information and application.”
  - per_credit_hour_charge: 10 ⟵ “$174/credit hour | $10/credit hour – Technology Fee. Tennessee residents are eligible for the TN Dual Enrollment Grant. Visit their website for information and application.”
  - state_grant_accepted: True ⟵ “$174/credit hour | $10/credit hour – Technology Fee. Tennessee residents are eligible for the TN Dual Enrollment Grant. Visit their website for information and application.”
  - max_credit_hours_per_term: 14 ⟵ “At Carson-Newman, students may take up to a maximum of 14 credit hours of Dual Enrollment per semester.”
### `072e7835fa8c7aea` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/hope/appeals.php (sha256 f6e32412720e)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/lottery-appeal-25.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If you receive notice that you have lost your eligibility for a TELS award, you will need to submit an appeal to the Office of Financial Aid and Scholarships as soon as possible.”
### `38fa467beca7b17f` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php (sha256 4cb91f9b9fb1)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “If your circumstances have not changed since last year, please provide the following to the Office of Financial Aid and Scholarships in person or via email at finaid@etsu.edu. · Signed 2026-27 Dependency Override Appeal form · Signed, dated statement outlining your circumstances and that they have not changed.”
  - sentence: dependency_override ⟵ “Dependency Override For financial aid purposes, a student is considered a dependent of their parents unless the student is: 24 years old married serving on active duty in the US Armed Forces a veteran a parent with dependents an emancipated minor homeless assigned a legal guardian before the age of 18 How to Appeal Contact our Assistant Director of Training and Service to discuss your circumstance”
### `4e0ed53c097b83fe` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf (sha256 e9dd7116362d)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: dependency_override ⟵ “Returning ETSU Students Only: If you were approved last year for a Dependency Override and have submitted your 2026-27 FAFSA application to ETSU, your process is different.”
  - sentence: dependency_override ⟵ “If your circumstances have not changed since last year, please provide the following to the Office of Financial Aid and Scholarships in person or via email at finaid@etsu.edu. • Signed 2026-27 Dependency Override Appeal form • Signed and dated statement outlining your circumstances and that they 2026-27 Dependency have not changed You do not need to submit any additional documentation to our offic”
  - sentence: dependency_override ⟵ “What is a Dependency Override?”
  - sentence: dependency_override ⟵ “What conditions COULD warrant What conditions DO NOT warrant a Dependency Override? a Dependency Override?”
  - sentence: dependency_override ⟵ “Please note the following: • Complete the 2026-27 FAFSA online at www.fafsa.gov prior to completing and submitting the Dependency Override Appeal. • Financial Aid Policy at the East Tennessee State University requires that a student seeking a Dependency Override must complete the Dependency Override Appeal.”
  - sentence: dependency_override ⟵ “Please schedule an appointment online through FASTPASS. • The determination of whether or not to approve a dependency override is made by Student Financial Aid— not the U.S.”
### `4fd258e67f7d9f52` East Tennessee State University — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/ (sha256 eba080aff84c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “General Assembly Merit Scholarship (GAMS) Aspire Award Non-Traditional Lottery Don’t Lose Hope Appeals Process for Hope Getting Help Cost of Attendance Financial Aid TV GoldLink Guide Bucky's Treasure Map Schedule an Appointment Financial Aid Steps School Code 003487 1 | Submit FAFSA 2 | Verification 3 | Check Status 4 | Aid Offers 5 | Confirm Registration 6 | Majors & MinorsCost EstimateRequest I”
### `767c95a2c75e87a4` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf (sha256 e9dd7116362d)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-change-of-circumstance-form.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you have any questions, please contact our Assistant Director of Training and Service by selecting the 'Special Circumstance Appeal' option on our website.”
  - sentence: need_based_special_circumstances ⟵ “Select the 'Special Circumstance Appeal' option.”
### `870cb21945b09ba2` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf (sha256 e9dd7116362d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “A dependency override occurs when a financial aid administrator exercises professional judgment and overrides the Department of Education’s criteria for dependent students.”
### `98c007b93a81e797` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php (sha256 4cb91f9b9fb1)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-change-of-circumstance-form.pdf,https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “There are two different appeal processes available to you and your family: Special Circumstances Appeal Dependency Override For ETSU to grant an appeal, there must be compelling reasons.”
  - sentence: need_based_special_circumstances ⟵ “The first step is to be sure to select the correct forms for the aid year in which you are submitting an appeal. 2026-2027 Forms Special Circumstance Appeal Dependency Override Returning ETSU Students Only: If you were approved last year for a Dependency Override and have submitted your 2026-27 FAFSA application to ETSU, your process is different.”
  - sentence: need_based_special_circumstances ⟵ “If you have any questions, please make an appointment with our Assistant Director of Training and Service by selecting the 'Special Circumstance Appeals' option.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Should I Appeal?”
  - sentence: need_based_special_circumstances ⟵ “What Special Circumstances We DO Consider: Loss or change of employment Loss or change in untaxed income (child support, Social Security, or other benefits) Divorce or separation of parents or student Death of parent(s) or spouse Unusual medical expenses (not covered by insurance) One-time taxable income used for life changing events (e.g.”
### `9ab6f32695eb276a` East Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/max-appeal-edited.pdf (sha256 bf6d4e23f8ed)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/gpa-pace-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php,https://www.etsu.edu/financial-aid-and-scholarships/policies/satisfactorypro.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “TENNESSEE STATE OFFIC OF UNIVERSITY Finan Satisfactory Academic Progress Form – Maximum Time Name ETSU ID Number E ETSU email Phone: IMPORTANT: SAP appeals are reviewed by Committee according to the published Appeals Review Committee Schedule.”
### `9b38d386567da31c` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/policies/satisfactorypro.php (sha256 cf5ae3ccedcc)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/gpa-pace-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/documents/max-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Students who fail to earn 100% of attempted hours due to extenuating circumstances have the opportunity to submit a SAP appeal.”
  - sentence: sap_appeal ⟵ “Students who choose to appeal, will be required to complete the Satisfactory Academic Progress Form – Maximum Time Appeal form (not the GPA and PACE appeal), since they will not be able to complete 100% of their program of study.”
  - sentence: sap_appeal ⟵ “Steps to file an appeal: Complete and submit the correct Satisfactory Academic Progress Appeal Form based on your situation (GPA/PACE or Max Hours).”
### `b1ffd266f97bcdf9` East Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/lottery-appeal-25.pdf (sha256 ffff37221745)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/scholarships/hope/appeals.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “9 EAST TENNESSEE STATE - UNIVERSITY ETSU Tennessee Education Lottery Scholarship Appeal Form How to submit: Complete the following information and submit your appeal (including your statement and supporting documentation) to the Office of Student Financial Aid and Scholarships, Box 70722, ETSU, Johnson City, TN; Fax: 423-439-5855; Room 105, Burgin Dossett Hall.”
### `c0f6aab38052f5ed` East Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-change-of-circumstance-form.pdf (sha256 69ee1b8c2787)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Appeal Form Name ETSU ID Number E _ Address City/State/Zip: _ _ The Office of Financial Aid and Scholarships recognizes that many families have changes in income or family situations that cannot be reflected in the 2024 tax return.”
  - sentence: need_based_special_circumstances ⟵ “A Special Circumstances Appeal may be filed if you or your family have extenuating circumstances, which you believe warrant a reevaluation of your financial aid.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeals received after 11/15/26 will not be considered until a signedcopy ofa2026 tax return, including all schedules, and 2026 W-2s and/or 1099s have been submitted.”
  - sentence: need_based_special_circumstances ⟵ “Student Signature Date Parent/Spouse Signature Date To submit the completed form, please make an appointment with our Assistant Director of Training and Service by selecting the 'Special Circumstance Appeal' option on our website.”
### `c895ecdfbf356436` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php (sha256 4cb91f9b9fb1)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/gpa-pace-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/documents/max-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/policies/satisfactorypro.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeals Academic Appeal Forms and Links In certain circumstances, students have the option to appeal based on their academic performance.”
### `f2b218ce6a04850b` East Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/gpa-pace-appeal-edited.pdf (sha256 9b5ac0691990)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/max-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php,https://www.etsu.edu/financial-aid-and-scholarships/policies/satisfactorypro.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “TENNESSEE STATE OFFIC UNIVERSITY Satisfactory Academic Progress Form – GPA and PACE Name ETSU ID Number E ETSU email Phone: IMPORTANT: SAP appeals are reviewed by Committee according to the published Appeals Review Committee Schedule.”
### `526d008253c66f25` Lincoln Memorial University — appeals 2026-27 [new] (source_unlabeled)
- source: https://undergraduatecatalog.lmunet.edu/financial-aid-satisfactory-academic-progress (sha256 1e1109d06349)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeals Students who are on Financial Aid Suspension may appeal this decision by contacting Student Financial Services.”
### `7255008b9adf3bd5` Lincoln Memorial University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://nursingtampacatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce (sha256 ac4a17206a2e)
- issues: conflicting_sources:https://graduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce,https://undergraduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce
- checks: {"distinct_exams": 27, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|45]:  ⟵ “Art History | 45 | ART 381ART 381, 382”
  - equivalencies[AP-2-D-ART-DESIGN|34-5]:  ⟵ “Studio Art: 2-D Design | 34-5 | ART electiveART 105”
  - equivalencies[AP-3-D-ART-DESIGN|34-5]:  ⟵ “Studio Art: 3-D Design | 34-5 | ART electiveART 110”
  - equivalencies[AP-DRAWING|34-5]:  ⟵ “Studio Art: Drawing | 34-5 | ART ElectiveART 110”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang. & Comp. | 4-5 | ENGL 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Lit. &Comp. | 4-5 | ENGL 102”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “European History | 3-5 | HIST elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4-5]:  ⟵ “Human Geography | 4-5 | GEOG 211”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics | 4-5 | ECON 212”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics | 4-5 | ECON 213”
  - equivalencies[AP-PSYCHOLOGY|4-5]:  ⟵ “Psychology | 4-5 | PYSC 100”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4-5]:  ⟵ “U.S. Gov. & Politics | 4-5 | POLS 100”
  - equivalencies[AP-UNITED-STATES-HISTORY|34-5]:  ⟵ “U.S. History | 34-5 | HIST 131HIST 131, 132”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4-5]:  ⟵ “World History: Modern | 4-5 | HIST 122”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB | 4-5 | MATH 150”
  - equivalencies[AP-CALCULUS-BC|34-5]:  ⟵ “Calculus BC | 34-5 | MATH 150MATH 150, 250”
  - equivalencies[AP-STATISTICS|4-5]:  ⟵ “Statistics | 4-5 | MATH 270”
  - equivalencies[AP-BIOLOGY|34-5]:  ⟵ “Biology* | 34-5 | BIOL 111BIOL 111, 112”
  - equivalencies[AP-CHEMISTRY|34-5]:  ⟵ “Chemistry* | 34-5 | CHEM 111CHEM 111, 112”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science * | 3-5 | ENVS 100”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics I* | 4 | PHYS 211”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics II* | 4 | PHYS 212”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3-5]:  ⟵ “Physics C: Mechanics* | 3-5 | PHYS 211”
  - equivalencies[AP-PRECALCULUS|345]:  ⟵ “Precalculus | 345 | MATH 110MATH 115MATH 120”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|34-5]:  ⟵ “French Lang. & Culture | 34-5 | FREN 111FREN 111, 112”
  - … 2 more rows
### `b2e33199d4031886` Lincoln Memorial University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://graduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce (sha256 94c6ba721b5c)
- issues: conflicting_sources:https://nursingtampacatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce,https://undergraduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce
- checks: {"distinct_exams": 27, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4 5]:  ⟵ “Art History | 4 5 | ART 381 ART 381, 382”
  - equivalencies[AP-MUSIC-THEORY|3 4-5]:  ⟵ “Music Theory | 3 4-5 | MUSC 111 MUSC 111, 112”
  - equivalencies[AP-2-D-ART-DESIGN|3 4-5]:  ⟵ “Studio Art: 2-D Design | 3 4-5 | ART elective ART 105”
  - equivalencies[AP-3-D-ART-DESIGN|3 4-5]:  ⟵ “Studio Art: 3-D Design | 3 4-5 | ART elective ART 110”
  - equivalencies[AP-DRAWING|3 4-5]:  ⟵ “Studio Art: Drawing | 3 4-5 | ART elective ART 110”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang. & Comp. | 4-5 | ENGL 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Lit. & Comp. | 4-5 | ENGL 102”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “European History | 3-5 | HIST elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4-5]:  ⟵ “Human Geography | 4-5 | GEOG 211”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics | 4-5 | ECON 212”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics | 4-5 | ECON 213”
  - equivalencies[AP-PSYCHOLOGY|4-5]:  ⟵ “Psychology | 4-5 | PSYC 100”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4-5]:  ⟵ “U. S. Gov. & Politics | 4-5 | POLS 211”
  - equivalencies[AP-UNITED-STATES-HISTORY|3 4-5]:  ⟵ “U. S. History | 3 4-5 | HIST 131 HIST 131, 132”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3 4-5]:  ⟵ “World History | 3 4-5 | HIST 121 HIST 121, 122”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB | 4-5 | MATH 150”
  - equivalencies[AP-CALCULUS-BC|3 4-5]:  ⟵ “Calculus BC | 3 4-5 | MATH 150 MATH 150, 250”
  - equivalencies[AP-STATISTICS|4-5]:  ⟵ “Statistics | 4-5 | MATH 270”
  - equivalencies[AP-BIOLOGY|3 4-5]:  ⟵ “Biology* | 3 4-5 | BIOL 111 BIOL 111, 112”
  - equivalencies[AP-CHEMISTRY|3 4-5]:  ⟵ “Chemistry* | 3 4-5 | CHEM 111 CHEM 111, 112”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science* | 3-5 | ENVS 100”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics I* | 4 | PHYS 211”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics II | 4 | PHYS 212”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3-5]:  ⟵ “Physics C: Mechanics* | 3-5 | PHYS 211”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 4-5]:  ⟵ “French Lang. & Culture | 3 4-5 | FREN 111 FREN 111, 112”
  - … 2 more rows
### `df2a54aa45737c95` Lincoln Memorial University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://undergraduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce (sha256 c1de449eb2d0)
- issues: conflicting_sources:https://graduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce,https://nursingtampacatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce
- checks: {"distinct_exams": 27, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|45]:  ⟵ “Art History | 45 | ART 381ART 381, 382”
  - equivalencies[AP-2-D-ART-DESIGN|34-5]:  ⟵ “Studio Art: 2-D Design | 34-5 | ART electiveART 105”
  - equivalencies[AP-3-D-ART-DESIGN|34-5]:  ⟵ “Studio Art: 3-D Design | 34-5 | ART electiveART 110”
  - equivalencies[AP-DRAWING|34-5]:  ⟵ “Studio Art: Drawing | 34-5 | ART ElectiveART 110”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang. & Comp. | 4-5 | ENGL 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Lit. &Comp. | 4-5 | ENGL 102”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “European History | 3-5 | HIST elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4-5]:  ⟵ “Human Geography | 4-5 | GEOG 211”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics | 4-5 | ECON 212”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics | 4-5 | ECON 213”
  - equivalencies[AP-PSYCHOLOGY|4-5]:  ⟵ “Psychology | 4-5 | PYSC 100”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4-5]:  ⟵ “U.S. Gov. & Politics | 4-5 | POLS 100”
  - equivalencies[AP-UNITED-STATES-HISTORY|34-5]:  ⟵ “U.S. History | 34-5 | HIST 131HIST 131, 132”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4-5]:  ⟵ “World History: Modern | 4-5 | HIST 122”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB | 4-5 | MATH 150”
  - equivalencies[AP-CALCULUS-BC|34-5]:  ⟵ “Calculus BC | 34-5 | MATH 150MATH 150, 250”
  - equivalencies[AP-STATISTICS|4-5]:  ⟵ “Statistics | 4-5 | MATH 270”
  - equivalencies[AP-BIOLOGY|34-5]:  ⟵ “Biology* | 34-5 | BIOL 111BIOL 111, 112”
  - equivalencies[AP-CHEMISTRY|34-5]:  ⟵ “Chemistry* | 34-5 | CHEM 111CHEM 111, 112”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science * | 3-5 | ENVS 100”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics I* | 4 | PHYS 211”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics II* | 4 | PHYS 212”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3-5]:  ⟵ “Physics C: Mechanics* | 3-5 | PHYS 211”
  - equivalencies[AP-PRECALCULUS|345]:  ⟵ “Precalculus | 345 | MATH 110MATH 115MATH 120”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|34-5]:  ⟵ “French Lang. & Culture | 34-5 | FREN 111FREN 111, 112”
  - … 2 more rows
### `e4e9699330324131` Rhodes College — admissions_metrics 2024-25 [same] (labeled_in_source)
- source: https://www.rhodes.edu/sites/default/files/2026-02/CDS_2024-2025%20_Rhodes_College_.pdf (sha256 1e6d625b330b)
- issues: stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 6365 ⟵ “Total first-time, first-year (degree-seeking) who applied          1103       2872            2390           0     6365”
  - admits: 3205 ⟵ “Total first-time, first-year (degree-seeking) who were admitted     708         2160          337            0     3205”
  - enrolled: 388 ⟵ “Total first-time, first-year (degree-seeking) enrolled              126         216            46            0      388”
  - sat_composite_25..75: [1352, 1420, 1478] ⟵ “SAT Composite                     1352                      1420                       1478”
  - sat_math_25..75: [670, 720, 740] ⟵ “SAT Math                           670                       720                       740”
  - act_25..75: [28, 31, 32] ⟵ “ACT Composite                      28                        31                         32”
### `388bf69f380e9a68` Rhodes College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/rhodes-institutional-aid (sha256 9a95f432930b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Exceptions to this are within the purview of the Financial Aid Office in response to extreme increases in demonstrated financial need documented through the completion of the Special Circumstance Request and other supporting documents that may be required.”
### `9bb9f34e2714a8da` Rhodes College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/faq (sha256 fdedb1e7cc08)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Yes, if your family has experienced a change in financial circumstances (such as loss of employment, separation or divorce, or death of a parent) that is not adequately reflected on your FAFSA application, you may complete our Change of Financial Circumstances Form.”
  - sentence: need_based_special_circumstances ⟵ “In an effort to determine the need of our families and to best distribute any available awards we are asking families to complete the attached Special Circumstance Form.”
  - sentence: need_based_special_circumstances ⟵ “What can I do if I have unusual circumstances that prevent me from reporting parent information on my FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “Students with unusual circumstances (such as parental abandonment, abuse, or incarceration) are encouraged to reach out to the Office of Student Financial Aid to explain their situation and provide supporting documentation.”
### `e5ebe3b59e74f90c` Rhodes College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/faq (sha256 fdedb1e7cc08)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Our committee will review each situation on a case-by-case basis to determine if a dependency override can be granted.”
### `6802b23c61c9e09f` Rhodes College — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://catalog.rhodes.edu/general-information/expenses (sha256 d9d73e75048d)
- issues: conflicting_sources:https://www.rhodes.edu/admission-aid/cost-affordability/tuition-fees
- checks: {"columns": 1, "rows": 5}
  - column:Tuition (Full Time): 60240.0 ⟵ “Tuition (Full Time) | 30,120.00 | 60,240.00”
  - column:Activity Fee: 320.0 ⟵ “Activity Fee | 160.00 | 320.00”
  - column:Health & Wellness Fee: 500.0 ⟵ “Health & Wellness Fee | 250.00 | 500.00”
  - column:Tuition Refund Plan Coverage (Resident): 435.0 ⟵ “Tuition Refund Plan Coverage (Resident) |  | 435.00”
  - column:Tuition Refund Plan Coverage (Commuter): 348.0 ⟵ “Tuition Refund Plan Coverage (Commuter) |  | 348.00”
### `a8e4516e86bbe2b5` Rhodes College — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/tuition-fees (sha256 13cfdc4a9137)
- issues: conflicting_sources:https://catalog.rhodes.edu/general-information/expenses
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 60240 ⟵ “Tuition | $60,240”
  - column:Mandatory Fees: 820 ⟵ “Mandatory Fees | $820”
  - column:Housing & Food (Unlimited, All-Access Meal Plan)*: 15196 ⟵ “Housing & Food (Unlimited, All-Access Meal Plan)* | $15,196”
  - column:Total: 76256 ⟵ “Total | $76,256”
### `454d9c726264dd61` Tennessee Technological University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/professional-judgement.php (sha256 984c0110a4a7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Circumstances Not Given Consideration The Department of Education has identified conditions that, individually or in combination with one another, DO NOT QUALIFY AS UNUSUAL CIRCUMSTANCES, or do not merit a change in dependency status.”
### `775567f8cb73d667` Tennessee Technological University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/professional-judgement.php (sha256 984c0110a4a7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: professional_judgment ⟵ “Click the links below to access the desired information. 26/27 Professional Judgment Forms 25/26 Professions Judgment Forms Appeal Examples Dependency Overrides Fall 2026, Spring 2027 and Summer 2027 Professional Judgment Form Use the link below to access the Professional Judgment form.”
  - sentence: professional_judgment ⟵ “Forms must be initiated by the student, who when prompted will add other individuals (parent or spouse) if needed. 2026-2027 Professional Judgment Form Fall 2025, Spring 2026 and Summer 2026 Professional Judgment Forms Use the links below to access the appropriate Professional Judgment form for your circumstances.”
  - sentence: professional_judgment ⟵ “The student will be prompted to add other individuals (parent or spouse) if needed. 2025-2026 Professional Judgment Appeal Form 2025-2026 Professional Judgment Appeal Form: Marital Status to Tax Return Filing Status Professional Judgment Appeal Examples Listed below are examples of circumstances for which a professional judgment may be considered at Tennessee Tech University.”
  - sentence: professional_judgment ⟵ “A Professional Judgment Appeal Form requesting a re-evaluation should be completed and submitted for review to determine documentation needed.”
  - sentence: professional_judgment ⟵ “Please note that prior to the Professional Judgment process, the FAFSA application considers prior-prior year tax return information.”
### `e4708a66562cc3c3` Tennessee Technological University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tntech.edu/financialaid/sap.php (sha256 dfa2f7a684f5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 21}
  - sentence: sap_appeal ⟵ “Click the links below to learn more about Satisfactory Academic Progress, Tech's SAP Policy, Financial Aid Termination, and submitting appeals!”
  - sentence: sap_appeal ⟵ “Financial Aid Termination The SAP Appeal Process SAP Policy What is SAP?”
  - sentence: sap_appeal ⟵ “Students who do not meet one of the three above requirements when evaluated at the end of any given spring semester are placed on Financial Aid Termination and must submit a SAP Appeal to potentially regain their aid for the upcoming semester.”
  - sentence: sap_appeal ⟵ “A student placed on Financial Aid Termination cannot utilize their eligible federal or state aid until they either return to 'Good Standing' by meeting the SAP requirements for future semesters or submit a SAP Appeal for review that is then approved.”
  - sentence: sap_appeal ⟵ “Students placed on FA Termination receive an email notification from the Office of Financial Aid titled "TTU Financial Aid Information" that directs them to Eagle Online to view their Financial Aid Termination status - selecting the status redirects students to the Satisfactory Academic Progress webpage to learn more about Financial Aid Termination and submit a SAP Appeal.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Process Students placed on FA Termination who wish to continue using their aid can complete and submit a SAP Appeal for review.”
### `efc201fc84459cd2` Tennessee Technological University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/professional-judgement.php (sha256 984c0110a4a7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency Overrides Students must communicate with the Financial Aid Office for assistance with a Dependency Override request.”
### `74a16798ae79d370` Tennessee Technological University — costs 2025-26 · residency=out_of_state [same] (labeled_in_source)
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
### `d44ab9350efe52cf` Tennessee Technological University — costs 2025-26 · residency=in_state [same] (labeled_in_source)
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
### `012a76f2994b044e` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/professional-judgment (sha256 26ff53a1752c)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap
- checks: {"negative_sentences": 0, "sentences": 5}
- change offered: `False` → `True`
- change process_summary: `The appeal-form guide lists no special-circumstances / professional-judgment appeal; financial aid forms pages were not fully reviewed.` → `What is considered special or unusual circumstance?`
  - sentence: need_based_special_circumstances ⟵ “What is considered special or unusual circumstance?”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are financial changes that have occurred to a student or parent since completing the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances refer to a student’s dependency status, also known as dependency override.”
  - sentence: need_based_special_circumstances ⟵ “None of the following conditions, singly or in combination, qualify as unusual circumstances meriting a dependency override: Parents refuse to contribute to the student's education.”
  - sentence: need_based_special_circumstances ⟵ “Submitting an explanation with supporting documentation does not guarantee a change in financial aid awards.”
### `0fb2b0a5cbcb9211` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap (sha256 73e70a498997)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/academic-service-scholars-program,https://www.utc.edu/enrollment-management-and-student-affairs/mocs-one-center/choose-correct-appeal-form
- checks: {"negative_sentences": 0, "sentences": 2}
- change process_summary: `Scholarship Appeal for students who lost a UTC scholarship or the Tennessee HOPE scholarship because of GPA, credit completion or enrollment status; online form; decision within 45 days.` → `The Financial Aid SAP Committee does not have authority to approve or deny University or TN HOPE Scholarship appeals.`
  - sentence: scholarship_retention_appeal ⟵ “The Financial Aid SAP Committee does not have authority to approve or deny University or TN HOPE Scholarship appeals.”
  - sentence: scholarship_retention_appeal ⟵ “The Financial Aid SAP Committee does not have authority to approve or deny University or TN HOPE scholarship appeals.”
### `16445bb5a0506695` The University of Tennessee-Chattanooga — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/professional-judgment (sha256 26ff53a1752c)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: professional_judgment ⟵ “Quick Links » Calendar Campus News Canvas Change Password Class Schedule Crisis Resources Library Google Workspace MocSync MyMocsNet Microsoft O365 GTranslate Special and Unusual Circumstances Professional Judgment What is a professional judgment?”
  - sentence: professional_judgment ⟵ “Such exceptions, known as professional judgment, are considered on a case-by-case basis with supporting documentation of your unique circumstances.”
  - sentence: professional_judgment ⟵ “Please note you must be currently enrolled in the aid year for which you are requesting the Professional Judgment for it to be considered.”
  - sentence: professional_judgment ⟵ “Professional judgments take 6-8 weeks for a decision once all documentation is submitted.”
  - sentence: professional_judgment ⟵ “Professional Judgment Special and Unusual Circumstances Appeal Instructions Complete your Professional Judgment Professional Judgment FAQs What documents should I submit with my Professional Judgment request?”
  - sentence: professional_judgment ⟵ “How long before I know the outcome of a Professional Judgment?”
### `24180d85816259ec` The University of Tennessee-Chattanooga — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships (sha256 293003b55d02)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Quick Links » Calendar Campus News Canvas Change Password Class Schedule Crisis Resources Library Google Workspace MocSync MyMocsNet Microsoft O365 GTranslate Financial Aid and Scholarships Dates Forms Accepting Aid Parents Faculty and Staff Professional Judgment Frequently Asked Questions Office of Financial Aid and Scholarships Student Employment FAFSA An affordable degree starts here UTC’s Offi”
### `2c01262a1a8edff2` The University of Tennessee-Chattanooga — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/mocs-scholarship (sha256 e533610a040a)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/chancellors-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/provosts-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/transfer-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable (i.e.”
### `33b6667858772a1a` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/academic-service-scholars-program (sha256 b9e5fbe44370)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap,https://www.utc.edu/enrollment-management-and-student-affairs/mocs-one-center/choose-correct-appeal-form
- checks: {"negative_sentences": 0, "sentences": 1}
- change process_summary: `Scholarship Appeal for students who lost a UTC scholarship or the Tennessee HOPE scholarship because of GPA, credit completion or enrollment status; online form; decision within 45 days.` → `Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable. • You did not maintain the required cumulative GPA; • You did not pass the required number of credit hours (or service/work hours); • You have taken a fall or spring semester off and not attended classes; • You have totally withdrawn from classes for the term, officially or unofficially.`
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable. • You did not maintain the required cumulative GPA; • You did not pass the required number of credit hours (or service/work hours); • You have taken a fall or spring semester off and not attended classes; • You have totally withdrawn from classes for the term, officia”
### `3600db53df5356c4` The University of Tennessee-Chattanooga — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/provosts-scholarship (sha256 760e71085018)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/chancellors-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/mocs-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/transfer-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable (i.e.”
### `4270465ca702361a` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap (sha256 73e70a498997)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 5}
- change offered: `False` → `True`
- change process_summary: `The appeal-form guide lists no special-circumstances / professional-judgment appeal; financial aid forms pages were not fully reviewed.` → `Appeal statements should include the following: Explain any unusual circumstances that led to your financial aid suspension.`
  - sentence: need_based_special_circumstances ⟵ “Appeal statements should include the following: Explain any unusual circumstances that led to your financial aid suspension.”
  - sentence: need_based_special_circumstances ⟵ “Be specific- indicate dates and time periods involved and how the unusual circumstances affected your academic performance.”
  - sentence: need_based_special_circumstances ⟵ “If UTC offers a service that helps mitigate your unusual circumstance, you may be required to document that you are using this service.”
  - sentence: need_based_special_circumstances ⟵ “Signed Statement, indicating rationale for app Statement must include an explanation of unusual circumstances that led to financial aid suspension.”
  - sentence: need_based_special_circumstances ⟵ “Sufficient documentation to support claim of unusual circumstances.”
### `66362de9def69e79` The University of Tennessee-Chattanooga — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/chancellors-scholarship (sha256 acec14bf0bd6)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/mocs-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/provosts-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/transfer-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable (i.e.”
### `bcff7a709a2a09da` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/mocs-one-center/choose-correct-appeal-form (sha256 4ac036e06e03)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/academic-service-scholars-program
- checks: {"negative_sentences": 0, "sentences": 1}
- change process_summary: `Scholarship Appeal for students who lost a UTC scholarship or the Tennessee HOPE scholarship because of GPA, credit completion or enrollment status; online form; decision within 45 days.` → `A Scholarship Appeal for the loss of your TN HOPE Scholarship can be submitted if you have extenuating circumstances have contributed to the following: You have totally withdrawn from classes for the term.`
  - sentence: scholarship_retention_appeal ⟵ “A Scholarship Appeal for the loss of your TN HOPE Scholarship can be submitted if you have extenuating circumstances have contributed to the following: You have totally withdrawn from classes for the term.”
### `e82414d62f16f1fc` The University of Tennessee-Chattanooga — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/transfer-scholarship (sha256 27f7be027aff)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/chancellors-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/mocs-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/provosts-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of this scholarship and Is Not appealable. • You did not maintain the required cumulative GPA; • You did not pass the required number of credit hours (or service/work hours); • You have taken a fall or spring semester off and not attended classes; • You have totally withdrawn from classes for the term, officially or unofficiall”
### `fb5f4a5c397287f7` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap (sha256 73e70a498997)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
- change process_summary: `Financial Aid / Satisfactory Academic Progress (SAP) Appeal for students who lost financial aid by not meeting SAP standards; online form; decision within 45 days.` → `Financial Aid Probation - If a student has a Satisfactory Academic Progress (SAP) Appeal approved, they will be placed on a one semester warning period if it will be possible to bring their Course Completion Rate and GPA to maintain SAP standards after the next semester.`
  - sentence: sap_appeal ⟵ “Financial Aid Probation - If a student has a Satisfactory Academic Progress (SAP) Appeal approved, they will be placed on a one semester warning period if it will be possible to bring their Course Completion Rate and GPA to maintain SAP standards after the next semester.”
  - sentence: sap_appeal ⟵ “Academic Plan - If a student has a Satisfactory Academic Progress (SAP) Appeal approved and it is NOT possible for them to maintain the required Course Completion Rate and GPA to maintain SAP after one semester of enrollment, they will be placed in a SAP Academic Plan.”
  - sentence: sap_appeal ⟵ “Notification of Status and right to appeal Students will be notified of changes to SAP status and any appeal decisions via UTC email.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals Process and Financial Aid Appeal Forms Students appealing their Satisfactory Academic Progress status are required to submit an appeals packet for review.”
  - sentence: sap_appeal ⟵ “The following are due in the SAP Appeals packet: Financial Aid Appeal Form.”
  - sentence: sap_appeal ⟵ “Review Process There are three levels of appeal in the SAP Appeals process.”
### `26063ed084e45178` The University of Tennessee-Chattanooga — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://www.utc.edu/sites/default/files/2026-09/2026-27-estimated-cost-of-attendance.pdf (sha256 4dc086460fb0)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "rows": 9}
  - with_parents_or_family:Enrollment Fees: 11084 ⟵ “Enrollment Fees | 11084 | 11084 | 11084 | 11789”
  - with_parents_or_family:Books: 1400 ⟵ “Books | 1400 | 1400 | 1400 | 1200”
  - with_parents_or_family:Housing: 2600 ⟵ “Housing | 2600 | 8800 | 9204 | 9450”
  - with_parents_or_family:Food: 4552 ⟵ “Food | 4552 | 4552 | 4552 | 4552”
  - with_parents_or_family:Transportation: 2300 ⟵ “Transportation | 2300 | 2300 | 2300 | 3200”
  - with_parents_or_family:Personal Expenses: 1800 ⟵ “Personal Expenses | 1800 | 1800 | 1800 | 2600”
  - with_parents_or_family:IN-STATE TOTAL: 23736 ⟵ “IN-STATE TOTAL | 23736 | 29936 | 30340 | 32791”
  - with_parents_or_family:Out-of-State Tuition: 8306 ⟵ “Out-of-State Tuition | 8306 | 8306 | 8306 | 8306”
  - with_parents_or_family:Out-of-State Total: 32042 ⟵ “Out-of-State Total | 32042 | 38242 | 38646 | 41097”
  - with_parents_or_family:Enrollment Fees: 11084 ⟵ “Enrollment Fees | 11084 | 11084 | 11084 | 11789”
  - with_parents_or_family:Books: 1400 ⟵ “Books | 1400 | 1400 | 1400 | 1200”
  - with_parents_or_family:Housing: 2600 ⟵ “Housing | 2600 | 8800 | 9204 | 9450”
  - with_parents_or_family:Food: 4552 ⟵ “Food | 4552 | 4552 | 4552 | 4552”
  - with_parents_or_family:Transportation: 2300 ⟵ “Transportation | 2300 | 2300 | 2300 | 3200”
  - with_parents_or_family:Personal Expenses: 1800 ⟵ “Personal Expenses | 1800 | 1800 | 1800 | 2600”
  - with_parents_or_family:IN-STATE TOTAL: 23736 ⟵ “IN-STATE TOTAL | 23736 | 29936 | 30340 | 32791”
  - with_parents_or_family:Out-of-State Tuition: 642 ⟵ “Out-of-State Tuition | 642 | 642 | 642 | 872”
  - with_parents_or_family:Out-of-State Total: 24378 ⟵ “Out-of-State Total | 24378 | 30578 | 30982 | 33663”
  - off_campus_not_with_family:Enrollment Fees: 11084 ⟵ “Enrollment Fees | 11084 | 11084 | 11084 | 11789”
  - off_campus_not_with_family:Books: 1400 ⟵ “Books | 1400 | 1400 | 1400 | 1200”
  - off_campus_not_with_family:Housing: 8800 ⟵ “Housing | 2600 | 8800 | 9204 | 9450”
  - off_campus_not_with_family:Food: 4552 ⟵ “Food | 4552 | 4552 | 4552 | 4552”
  - off_campus_not_with_family:Transportation: 2300 ⟵ “Transportation | 2300 | 2300 | 2300 | 3200”
  - off_campus_not_with_family:Personal Expenses: 1800 ⟵ “Personal Expenses | 1800 | 1800 | 1800 | 2600”
  - off_campus_not_with_family:IN-STATE TOTAL: 29936 ⟵ “IN-STATE TOTAL | 23736 | 29936 | 30340 | 32791”
  - … 47 more rows

## Re-verification of existing records (57)

- source_not_fetched: data/institutions/abcnash/transfer_policies/2026-27.json ["transfer_policies", "ipeds-219505", null, "2026-27", {}]
- source_not_fetched: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Academic Achievement"}]
- source_not_fetched: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Dean's"}]
- source_not_fetched: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Governor's Excellence"}]
- source_not_fetched: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Governor's Merit"}]
- source_not_fetched: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Presidential"}]
- source_not_fetched: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Presidents Emerging Leaders Program (PELP)Apply by 12/31"}]
- source_not_fetched: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Kimbrough (Limited Awards Available)"}]
- source_not_fetched: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Howell C. Smith (Limited Awards Available)"}]
- source_not_fetched: data/institutions/belmont/transfer_policies/2026-27.json ["transfer_policies", "ipeds-219709", null, "2026-27", {}]
- source_not_fetched: data/institutions/bryan/awards/2026-27.json ["awards", "ipeds-219790", null, "2026-27", {"award_name": "Platinum"}]
- source_not_fetched: data/institutions/bryan/awards/2026-27.json ["awards", "ipeds-219790", null, "2026-27", {"award_name": "Silver"}]
- source_not_fetched: data/institutions/bryan/awards/2026-27.json ["awards", "ipeds-219790", null, "2026-27", {"award_name": "Crimson"}]
- source_not_fetched: data/institutions/jscc/costs/2026-27.json ["costs", "ipeds-220400", null, "2026-27", {"residency": "out_of_state"}]
- source_not_fetched: data/institutions/jscc/credit_policies/2026-27.json ["credit_policies", "ipeds-220400", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/jscc/credit_policies/2026-27.json ["credit_policies", "ipeds-220400", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/johnsonu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-220473", null, "2026-27", {}]
- source_not_fetched: data/institutions/lanecollege/transfer_policies/2026-27.json ["transfer_policies", "ipeds-220598", null, "2026-27", {}]
- source_not_fetched: data/institutions/lipscomb/credit_policies/2026-27.json ["credit_policies", "ipeds-219976", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/lipscomb/transfer_policies/2026-27.json ["transfer_policies", "ipeds-219976", null, "2026-27", {}]
- source_not_fetched: data/institutions/midsouthchristian/transfer_policies/2026-27.json ["transfer_policies", "ipeds-481225", null, "2026-27", {}]
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
- source_not_fetched: data/institutions/utk/awards/2026-27.json ["awards", "utk", null, "2026-27", {"award_name": "Manning Scholars"}]
- source_not_fetched: data/institutions/utk/awards/2026-27.json ["awards", "utk", null, "2026-27", {"award_name": "Out-of-State Volunteer Scholarship"}]
- source_not_fetched: data/institutions/utk/transfer_policies/2026-27.json ["transfer_policies", "utk", null, "2026-27", {}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Carson-Newman University: cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- East Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Lincoln Memorial University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Rhodes College: cost_of_attendance, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, degree_requirements
- Tennessee Technological University: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- The University of Tennessee-Chattanooga: tuition_fees, admissions_tests, transfer_credit, statewide_articulation, residency
