# Review queue — MD (2026-27)

Pages fetched: 270; failures: 12. Candidates: 31 (5 without issues, 26 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 6 | 1 | 1 | 2 | 0 | 0 | 37 |
| cost_of_attendance | 4 | 1 | 0 | 1 | 2 | 0 | 39 |
| admissions_tests | 2 | 0 | 0 | 0 | 3 | 0 | 42 |
| common_data_set | 2 | 0 | 0 | 0 | 1 | 2 | 42 |
| merit_scholarships | 0 | 0 | 0 | 0 | 3 | 0 | 44 |
| ap_credit | 0 | 5 | 0 | 0 | 2 | 0 | 40 |
| clep_credit | 0 | 3 | 0 | 0 | 2 | 0 | 42 |
| ib_credit | 0 | 2 | 0 | 1 | 1 | 1 | 42 |
| dual_enrollment | 0 | 6 | 0 | 0 | 2 | 0 | 39 |
| transfer_credit | 0 | 7 | 0 | 0 | 2 | 0 | 38 |
| statewide_articulation | 0 | 0 | 0 | 0 | 1 | 2 | 44 |
| residency | 0 | 0 | 0 | 0 | 3 | 0 | 44 |
| degree_requirements | 3 | 0 | 0 | 0 | 1 | 0 | 43 |
| aid_appeals | 0 | 0 | 0 | 3 | 0 | 0 | 44 |

## Ready for review (5)

### `edfedbd8aa1cb4e7` Towson University — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.towson.edu/admissions/undergrad/nondegree/highschool.html (sha256 b4218c9c203a)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.5 ⟵ “average GPA of an A or higher, or a weighted GPA of 3.5 or higher. Submitting test”
### `4b8d860b762d16ca` University of Maryland Global Campus — credit_policies 2026-27 · policy_kind=CLEP [same] (source_unlabeled)
- source: https://www.umgc.edu/transfers-and-credits/fast-paths-to-credit/credit-by-exam/clep (sha256 d150980c8618)
- checks: {"distinct_exams": 33, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | GVPT 170 | 50 | 3 LL”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | Literature Elective (satisfies Arts & Humanities Gen Ed Requirement) | 50 | 3 LL”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | Literature Elective (satisfies Arts & Humanities Gen Ed Requirement) | 50 | 3 LL”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | BIOL 101 and BIOL Lecture (3 Credits, satisfies Biological & Physical Sciences Gen Ed Requirement) | 50 | 6 LL”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | MATH 140 | 50 | 4 LL”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | CHEM 121 and CHEM Lecture (3 Credits, satisfies Biological & Physical Sciences Gen Ed Requirement) | 50 | 6 LL”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | MATH 107 | 50 | 3 LL”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | WRTG 111 and Elective (3 Credits) | 50 | 6 LL”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | Elective | 50 | 3 LL”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | MATH 105 | 50 | 3 LL”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | Literature Elective (satisfies Arts & Humanities Gen Ed Requirement) | 50 | 6 LL”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | ACCT 220 | 50 | 3 LL”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language (Level 1) | FREN 111 and FREN 112 | 50 | 6 LL”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language (Level 2) | FREN 111, FREN 112, and FREN 211 | 59 | 9 LL”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language (Level 1) | GERM 111 and GERM 112 | 50 | 6 LL”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language (Level 2) | GERM 111, GERM 112, and GERM 211 | 60 | 9 LL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | HIST 156 | 50 | 3 LL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present | HIST 157 | 50 | 3 LL”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | PSYC 351 | 50 | 3 LL”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | HUMN 100 | 50 | 3 LL”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | IFSM 201 | 50 | 3 LL”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | PSYC Elective (satisfies Behavioral & Social Sciences Gen Ed Requirement) | 50 | 3 LL”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | BMGT 380 | 50 | 3 LL”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PSYC 100 | 50 | 3 LL”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | SOCY 100 | 50 | 3 LL”
  - … 12 more rows
### `a7be96ca30547ca7` University of Maryland Global Campus — credit_policies 2026-27 · policy_kind=AP [same] (source_unlabeled)
- source: https://www.umgc.edu/transfers-and-credits/fast-paths-to-credit/credit-by-exam/ap (sha256 65d9f3d2cc6a)
- checks: {"distinct_exams": 39, "equivalencies": 60, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “AP 2D Art & Design | ARTT Elective | 3, 4, 5 | 3 LL”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, 5]:  ⟵ “AP 3D Art & Design | ARTT Elective | 3, 4, 5 | 3 LL”
  - equivalencies[AP-ART-HISTORY|3, 4, 5]:  ⟵ “AP Art History | ARTH Elective | 3, 4, 5 | 6 LL”
  - equivalencies[AP-BIOLOGY|3, 4, 5]:  ⟵ “AP Biology | BIOL 103 (Satisfies Lecture w/ Lab requirement) | 3, 4, 5 | 4 LL”
  - equivalencies[AP-CALCULUS-AB|3, 4, 5]:  ⟵ “AP Calculus AB | MATH 140 | 3, 4, 5 | 4 LL”
  - equivalencies[AP-CALCULUS-BC|3, 4, 5]:  ⟵ “AP Calculus BC | MATH 140 and MATH 141 | 3, 4, 5 | 8 LL”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “AP Chemistry | CHEM 103 (Satisfies Lecture w/ Lab requirement) | 3 | 4 LL”
  - equivalencies[AP-CHEMISTRY|4, 5]:  ⟵ “AP Chemistry | CHEM 103 and CHEM Elective (Satisfies Lecture w/ Lab requirement) | 4, 5 | 8 LL”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “AP Chinese Language and Culture | CHIN 114, CHIN 115, and CHIN Elective | 3 | 8 LL”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “AP Chinese Language and Culture | CHIN 114, CHIN 115, and CHIN Elective | 4 | 12 LL”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “AP Chinese Language and Culture | CHIN 114, CHIN 115, and CHIN Elective | 5 | 16 LL”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “AP Comparative Government and Politics | GVPT 280 | 3, 4, 5 | 3 LL”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, 5]:  ⟵ “AP Computer Science A | CMIS 141 | 3, 4, 5 | 4 LL”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “AP Computer Science Principles | CMIS 102 | 3, 4, 5 | 3 LL”
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “AP Drawing | ARTT 110 | 3, 4, 5 | 3 LL”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “AP English Language and Composition | WRTG 111 and Elective | 3 | 6 LL”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4, 5]:  ⟵ “AP English Language and Composition | WRTG 112 and Elective | 4, 5 | 6 LL”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “AP English Literature and Composition | ENGL 102 | 3 | 3 LL”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4, 5]:  ⟵ “AP English Literature and Composition | ENGL 102 and ENGL 240 | 4, 5 | 6 LL”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3, 4, 5]:  ⟵ “AP Environmental Science | Science Elective (Satisfies Lecture requirement) | 3, 4, 5 | 3 LL”
  - equivalencies[AP-EUROPEAN-HISTORY|3, 4, 5]:  ⟵ “AP European History | HIST 141 and HIST 142 | 3, 4, 5 | 6 LL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “AP French Language | FREN 211 and FREN Elective | 3 | 6 LL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “AP French Language | FREN 211, FREN 212, and FREN Elective | 4 | 9 LL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “AP French Language | FREN 211, FREN 212, and FREN Elective | 5 | 12 LL”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “AP German Language | GERM 211 and GERM Elective | 3 | 12 LL”
  - … 35 more rows
### `0edc08cda7c2a508` University of Maryland-College Park — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/tuition-fees/ (sha256 bc797311f4c8)
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 42266.0 ⟵ “Tuition | $42,266.00”
  - column:Additional Differential Tuition for full-time juniors and seniors who are majoring in Business, Engineering, or Computer Science (regardless of residency classification): 3375.0 ⟵ “Additional Differential Tuition for full-time juniors and seniors who are majoring in Business, Engineering, or Computer Science (regardless of residency classification) | $3,375.00”
  - column:Mandatory Fees (includes Tech fee). Maximum charged to all students registered for 9 or more credits: 1820.0 ⟵ “Mandatory Fees (includes Tech fee). Maximum charged to all students registered for 9 or more credits | $1,820.00”
  - column:Board Contract (Resident Dining Plan - Base Plan): 6820.0 ⟵ “Board Contract (Resident Dining Plan - Base Plan) | $6,820.00”
  - column:Room (Standard 2-person w/AC, includes Telecom fee): 10290.0 ⟵ “Room (Standard 2-person w/AC, includes Telecom fee) | $10,290.00”
### `5f9a3a1c98239e89` University of Maryland-College Park — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://academiccatalog.umd.edu/undergraduate/registration-academic-requirements-regulations/transfer-credit/transfer-credit.pdf (sha256 5371db41fc88)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Generally, college-level courses completed at regionally-accredited institutions will be acceptable and awarded transfer credit, provided the course is similar in level, scope, content and expected learning outcomes Applicability of Transfer Courses to to courses offered at the University of Maryland and a grade of "C-" or higher is earned.”

## Exceptions (26)

### `1db5d0733129503c` Towson University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.towson.edu/admissions/financialaid/forms/2026-forms.html (sha256 59a7b76ff6f9)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Nancy Grasmick Leadership Institute Sponsorship & Advertising Opportunities Hiring TU Students Visit TUApply NowRequest Information Give to TU Calendars & Events Directories HomeAdmissions & AidFinancial AidForms & Online Services2025-2026 Forms 2025-2026 Forms Sub-menu Forms & Online Services 2026-2027 Forms 2025-2026 Forms FAFSA Verification Identity Verification Satisfactory Academic Progress (”
### `a665ac89cd8744ba` Towson University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.towson.edu/admissions/financialaid/forms/ (sha256 c723b6424b68)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.towson.edu/admissions/financialaid/forms/2027-forms.html,https://www.towson.edu/admissions/financialaid/forms/sap-appeal.html,https://www.towson.edu/admissions/financialaid/guide/requirements/sap.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Nancy Grasmick Leadership Institute Sponsorship & Advertising Opportunities Hiring TU Students Visit TUApply NowRequest Information Give to TU Calendars & Events Directories HomeAdmissions & AidFinancial AidForms & Online Services Forms & Online Services Sub-menu Forms & Online Services 2026-2027 Forms 2025-2026 Forms FAFSA Verification Identity Verification Satisfactory Academic Progress (SAP) Ap”
### `adf099b1591ea3bb` Towson University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.towson.edu/admissions/financialaid/forms/2027-forms.html (sha256 40994fbf285f)
- issues: semantic_review_required, conflicting_sources:https://www.towson.edu/admissions/financialaid/forms/,https://www.towson.edu/admissions/financialaid/forms/sap-appeal.html,https://www.towson.edu/admissions/financialaid/guide/requirements/sap.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Nancy Grasmick Leadership Institute Sponsorship & Advertising Opportunities Hiring TU Students Visit TUApply NowRequest Information Give to TU Calendars & Events Directories HomeAdmissions & AidFinancial AidForms & Online Services2026-2027 Forms 2026-2027 Forms Sub-menu Forms & Online Services 2026-2027 Forms 2025-2026 Forms FAFSA Verification Identity Verification Satisfactory Academic Progress (”
### `b25f1ff63330dda2` Towson University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.towson.edu/admissions/financialaid/forms/documents/2627depappealr.pdf (sha256 cc3646c774cc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you can answer yes to question 7 about Unusual Circumstances, the online form won’t require your parent’s data, and they will forward your request for independent status to us for our review and approval.”
### `d2116354c694f99c` Towson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.towson.edu/admissions/financialaid/guide/requirements/sap.html (sha256 205e83a38d4b)
- issues: semantic_review_required, conflicting_sources:https://www.towson.edu/admissions/financialaid/forms/,https://www.towson.edu/admissions/financialaid/forms/2027-forms.html,https://www.towson.edu/admissions/financialaid/forms/sap-appeal.html
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Appeal Process Suspended students may appeal to request aid for additional terms.”
  - sentence: sap_appeal ⟵ “If you have received a financial aid SAP suspension notice from the TU Financial Aid Office, to appeal your suspension, you must use this Online SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “Denied SAP Appeals If your appeal is denied, you will remain permanently ineligible for financial aid at TU unless you continue to attend TU without aid and improve your overall record enough to meet all the required cumulative SAP standards.”
### `e30daea7f8631769` Towson University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.towson.edu/admissions/financialaid/forms/sap-appeal.html (sha256 d4eca6744372)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.towson.edu/admissions/financialaid/forms/,https://www.towson.edu/admissions/financialaid/forms/2027-forms.html,https://www.towson.edu/admissions/financialaid/guide/requirements/sap.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “To appeal to continue receiving aid for additional terms, suspended students must submit this Online SAP Appeal Form.”
### `5b5f5a8c5174ab1d` Towson University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/financialaid/forms/documents/priorcoa.pdf (sha256 7fb8a0f0be3c)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "rows": 52}
  - column:Total Units Count: 24 ⟵ “Total Units Count | 24 | 18 | 12”
  - column:Tuition & Fees: 12186 ⟵ “Tuition & Fees | 12,186 | 9,342 | 6,228”
  - column:Room & Board: 16666 ⟵ “Room & Board | 16,666 | 16,666 | 16,666”
  - column:Books: 960 ⟵ “Books | 960 | 720 | 480”
  - column:Personal: 970 ⟵ “Personal | 970 | 970 | 970”
  - column:Transportation: 2460 ⟵ “Transportation | 2,460 | 2,460 | 2,460”
  - column:Loan Fees: 280 ⟵ “Loan Fees | 280 | 280 | 280”
  - column:Total: 33522 ⟵ “Total | 33,522 | 30,438 | 27,084”
  - column:Tuition & Fees (2): 31332 ⟵ “Tuition & Fees | 31,332 | 23,724 | 15,816”
  - column:Room & Board (2): 16666 ⟵ “Room & Board | 16,666 | 16,666 | 16,666”
  - column:Books (2): 960 ⟵ “Books | 960 | 720 | 480”
  - column:Personal (2): 970 ⟵ “Personal | 970 | 970 | 970”
  - column:Transportation (2): 2460 ⟵ “Transportation | 2,460 | 2,460 | 2,460”
  - column:Loan Fees (2): 280 ⟵ “Loan Fees | 280 | 280 | 280”
  - column:Total (2): 52668 ⟵ “Total | 52,668 | 44,820 | 36,672”
  - column:Tuition & Fees (3): 12186 ⟵ “Tuition & Fees | 12,186 | 9,342 | 6,228”
  - column:Room & Board (3): 3170 ⟵ “Room & Board | 3,170 | 3,170 | 3,170”
  - column:Books (3): 960 ⟵ “Books | 960 | 720 | 480”
  - column:Personal (3): 970 ⟵ “Personal | 970 | 970 | 970”
  - column:Transportation (3): 2460 ⟵ “Transportation | 2,460 | 2,460 | 2,460”
  - column:Loan Fees (3): 280 ⟵ “Loan Fees | 280 | 280 | 280”
  - column:Total (3): 20026 ⟵ “Total | 20,026 | 16,942 | 13,588”
  - column:Total Units Count (2): 18 ⟵ “Total Units Count | 18 | 12”
  - column:Tuition & Fees (4): 13302 ⟵ “Tuition & Fees | 13,302 | 8,868”
  - column:Books (4): 720 ⟵ “Books | 720 | 480”
  - … 101 more rows
### `5d22bb48e6f269e3` Towson University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/tuition/cost.html (sha256 612997865ff6)
- issues: arrangement_unlabeled, conflicting_sources:https://www.towson.edu/admissions/tuition/,https://www.towson.edu/student-university-billing/tuition/projected.html
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 32948 ⟵ “Tuition and Fees | $12,690 | $32,948 | $12,690 | $32,948”
  - column:Housing and Food Allowance: 16366 ⟵ “Housing and Food Allowance | $16,366 | $16,366 | $3,182 | $3,182”
  - column:Books and Supplies: 960 ⟵ “Books and Supplies | $ 960 | $ 960 | $ 960 | $ 960”
  - column:Transportation Expenses: 2534 ⟵ “Transportation Expenses | $ 2,534 | $ 2,534 | $2,534 | $2,534”
  - column:Personal Expenses: 970 ⟵ “Personal Expenses | $ 970 | $ 970 | $ 970 | $ 970”
  - column:Loan Fees Allowance: 262 ⟵ “Loan Fees Allowance | $ 262 | $ 262 | $ 262 | $ 262”
  - column:Total: 54040 ⟵ “Total | $ 33,782 | $54,040 | $20,598 | $40,856”
  - with_parents_or_family:Tuition and Fees: 32948 ⟵ “Tuition and Fees | $12,690 | $32,948 | $12,690 | $32,948”
  - with_parents_or_family:Housing and Food Allowance: 3182 ⟵ “Housing and Food Allowance | $16,366 | $16,366 | $3,182 | $3,182”
  - with_parents_or_family:Books and Supplies: 960 ⟵ “Books and Supplies | $ 960 | $ 960 | $ 960 | $ 960”
  - with_parents_or_family:Transportation Expenses: 2534 ⟵ “Transportation Expenses | $ 2,534 | $ 2,534 | $2,534 | $2,534”
  - with_parents_or_family:Personal Expenses: 970 ⟵ “Personal Expenses | $ 970 | $ 970 | $ 970 | $ 970”
  - with_parents_or_family:Loan Fees Allowance: 262 ⟵ “Loan Fees Allowance | $ 262 | $ 262 | $ 262 | $ 262”
  - with_parents_or_family:Total: 40856 ⟵ “Total | $ 33,782 | $54,040 | $20,598 | $40,856”
### `667257dfaaefce92` Towson University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/tuition/ (sha256 93193d131900)
- issues: conflicting_sources:https://www.towson.edu/admissions/tuition/cost.html,https://www.towson.edu/student-university-billing/tuition/projected.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Full-time Tuition and Fees (12-15 units/term): 12690 ⟵ “Full-time Tuition and Fees (12-15 units/term) | $12,690 | $32,948”
  - on_campus:Premium On-Campus Housing: 10076 ⟵ “Premium On-Campus Housing | $10,076 | $10,076”
  - on_campus:Silver Dining Plan Cost: 6290 ⟵ “Silver Dining Plan Cost | $ 6,290 | $ 6,290”
  - on_campus:Total Estimated TU Costs: 29056 ⟵ “Total Estimated TU Costs | $29,056 | $49,314”
### `6672d05b4aee01a3` Towson University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/tuition/ (sha256 93193d131900)
- issues: conflicting_sources:https://www.towson.edu/admissions/tuition/cost.html,https://www.towson.edu/student-university-billing/tuition/projected.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Full-time Tuition and Fees (12-15 units/term): 32948 ⟵ “Full-time Tuition and Fees (12-15 units/term) | $12,690 | $32,948”
  - column:Premium On-Campus Housing: 10076 ⟵ “Premium On-Campus Housing | $10,076 | $10,076”
  - column:Silver Dining Plan Cost: 6290 ⟵ “Silver Dining Plan Cost | $ 6,290 | $ 6,290”
  - column:Total Estimated TU Costs: 49314 ⟵ “Total Estimated TU Costs | $29,056 | $49,314”
### `8176bb8b88190d23` Towson University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.towson.edu/student-university-billing/tuition/projected.html (sha256 53b2eb362e0a)
- issues: arrangement_unlabeled, cost_period_semester, conflicting_sources:https://www.towson.edu/admissions/tuition/,https://www.towson.edu/admissions/tuition/cost.html
- checks: {"columns": 4, "rows": 4}
  - column:Tuition and Mandatory Fees¹: 6092 ⟵ “Tuition and Mandatory Fees¹ | $6,092 | $6,276 | $6,483 | $6,697”
  - column:Housing (multiple occupancy): 4336 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3455 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 14426 ⟵ “Total³ (student residing on campus) | $14,426 | $14,378 | $14,910 | $15,414”
  - column:Tuition and Mandatory Fees¹: 6276 ⟵ “Tuition and Mandatory Fees¹ | $6,092 | $6,276 | $6,483 | $6,697”
  - column:Housing (multiple occupancy): 4509 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3593 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 14378 ⟵ “Total³ (student residing on campus) | $14,426 | $14,378 | $14,910 | $15,414”
  - column:Tuition and Mandatory Fees¹: 6483 ⟵ “Tuition and Mandatory Fees¹ | $6,092 | $6,276 | $6,483 | $6,697”
  - column:Housing (multiple occupancy): 4690 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3737 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 14910 ⟵ “Total³ (student residing on campus) | $14,426 | $14,378 | $14,910 | $15,414”
  - column:Tuition and Mandatory Fees¹: 6697 ⟵ “Tuition and Mandatory Fees¹ | $6,092 | $6,276 | $6,483 | $6,697”
  - column:Housing (multiple occupancy): 4831 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3886 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 15414 ⟵ “Total³ (student residing on campus) | $14,426 | $14,378 | $14,910 | $15,414”
### `9b7f9ef4e0aeb63b` Towson University — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.towson.edu/student-university-billing/tuition/projected.html (sha256 53b2eb362e0a)
- issues: arrangement_unlabeled, cost_period_semester, conflicting_sources:https://www.towson.edu/admissions/tuition/,https://www.towson.edu/admissions/tuition/cost.html
- checks: {"columns": 4, "rows": 4}
  - column:Tuition and Mandatory Fees¹: 15666 ⟵ “Tuition and Mandatory Fees¹ | $15,666 | $16,465 | $17,305 | $18,188”
  - column:Housing (multiple occupancy): 4336 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3455 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 23457 ⟵ “Total³ (student residing on campus) | $23,457 | $24,567 | $25,732 | $26,905”
  - column:Tuition and Mandatory Fees¹: 16465 ⟵ “Tuition and Mandatory Fees¹ | $15,666 | $16,465 | $17,305 | $18,188”
  - column:Housing (multiple occupancy): 4509 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3593 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 24567 ⟵ “Total³ (student residing on campus) | $23,457 | $24,567 | $25,732 | $26,905”
  - column:Tuition and Mandatory Fees¹: 17305 ⟵ “Tuition and Mandatory Fees¹ | $15,666 | $16,465 | $17,305 | $18,188”
  - column:Housing (multiple occupancy): 4690 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3737 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 25732 ⟵ “Total³ (student residing on campus) | $23,457 | $24,567 | $25,732 | $26,905”
  - column:Tuition and Mandatory Fees¹: 18188 ⟵ “Tuition and Mandatory Fees¹ | $15,666 | $16,465 | $17,305 | $18,188”
  - column:Housing (multiple occupancy): 4831 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3886 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 26905 ⟵ “Total³ (student residing on campus) | $23,457 | $24,567 | $25,732 | $26,905”
### `d3fcc8dbd465dc7e` Towson University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/tuition/cost.html (sha256 612997865ff6)
- issues: arrangement_unlabeled, conflicting_sources:https://www.towson.edu/admissions/tuition/,https://www.towson.edu/student-university-billing/tuition/projected.html
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 12690 ⟵ “Tuition and Fees | $12,690 | $32,948 | $12,690 | $32,948”
  - column:Housing and Food Allowance: 16366 ⟵ “Housing and Food Allowance | $16,366 | $16,366 | $3,182 | $3,182”
  - column:Books and Supplies: 960 ⟵ “Books and Supplies | $ 960 | $ 960 | $ 960 | $ 960”
  - column:Transportation Expenses: 2534 ⟵ “Transportation Expenses | $ 2,534 | $ 2,534 | $2,534 | $2,534”
  - column:Personal Expenses: 970 ⟵ “Personal Expenses | $ 970 | $ 970 | $ 970 | $ 970”
  - column:Loan Fees Allowance: 262 ⟵ “Loan Fees Allowance | $ 262 | $ 262 | $ 262 | $ 262”
  - column:Total: 33782 ⟵ “Total | $ 33,782 | $54,040 | $20,598 | $40,856”
  - with_parents_or_family:Tuition and Fees: 12690 ⟵ “Tuition and Fees | $12,690 | $32,948 | $12,690 | $32,948”
  - with_parents_or_family:Housing and Food Allowance: 3182 ⟵ “Housing and Food Allowance | $16,366 | $16,366 | $3,182 | $3,182”
  - with_parents_or_family:Books and Supplies: 960 ⟵ “Books and Supplies | $ 960 | $ 960 | $ 960 | $ 960”
  - with_parents_or_family:Transportation Expenses: 2534 ⟵ “Transportation Expenses | $ 2,534 | $ 2,534 | $2,534 | $2,534”
  - with_parents_or_family:Personal Expenses: 970 ⟵ “Personal Expenses | $ 970 | $ 970 | $ 970 | $ 970”
  - with_parents_or_family:Loan Fees Allowance: 262 ⟵ “Loan Fees Allowance | $ 262 | $ 262 | $ 262 | $ 262”
  - with_parents_or_family:Total: 20598 ⟵ “Total | $ 33,782 | $54,040 | $20,598 | $40,856”
### `064f298d26526045` University of Maryland Global Campus — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.umgc.edu/current-students/finances/financial-aid/financial-aid-policies/satisfactory-academic-progress (sha256 5e8efcac9c3a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “She would not be eligible to submit a SAP appeal because she would not be able to meet SAP requirements by the end of her next term of half-time enrollment. (For an appeal to be considered, students must be able to reach the minimum SAP requirements within 6 credits.”
  - sentence: sap_appeal ⟵ “She would be eligible to submit a SAP appeal, since she would be able to meet SAP requirements by the end of her next term of half-time enrollment. (If this student successfully completed her next 6 credits, her cumulative completion rate would be above the 50% requirement: 15/27 = 55%) If the student submits a SAP appeal and it is approved, she would be placed on probation status and eligible to ”
  - sentence: sap_appeal ⟵ “Please note: SAP appeals are only accepted from students who will be able to meet all cumulative SAP requirements within one probationary term of half-time enrollment, including being mathematically capable of completing their academic program within the maximum timeframe limit.”
  - sentence: sap_appeal ⟵ “SAP appeals should be submitted via our secure document submission page.”
  - sentence: sap_appeal ⟵ “Please note: SAP appeals are separate from and unrelated to academic appeals seeking grade changes or refunds, which are not processed by the Financial Aid Office.”
### `0b0b7b4169607d51` University of Maryland Global Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umgc.edu/admission/requirements (sha256 c9d698bf815e)
- issues: semantic_review_required, conflicting_sources:https://www.umgc.edu/admission/requirements/special-circumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Admission for Special Circumstances Get admission advice for special circumstances before applying to UMGC.”
### `5d7c2d2d73cf468d` University of Maryland Global Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umgc.edu/admission/requirements/special-circumstances (sha256 d992251881e0)
- issues: semantic_review_required, conflicting_sources:https://www.umgc.edu/admission/requirements
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Admission for Special Circumstances | UMGC Skip Navigation Current Students Locations U.S.”
### `ec28627b8fc04d29` University of Maryland Global Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umgc.edu/tuition-financial-assistance/scholarships/maryland-completion (sha256 6f32e9451964)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If you lose continuing eligibility for the Completion Scholarship due to extenuating circumstances you may submit an appeal to request reinstatement of your eligibility.”
### `556caba8717fd390` University of Maryland Global Campus — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umgc.edu/tuition-financial-assistance/tuition/cost-of-attendance (sha256 67d9fe13a313)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition + Fees: Undergraduate, Maryland Resident: 4140 ⟵ “Tuition + Fees: Undergraduate, Maryland Resident | $4,140”
  - column:Annual Allowances: Amount for Undergraduate Living on Own: 28392 ⟵ “Annual Allowances: Amount for Undergraduate Living on Own | $28,392”
  - column:John's Annual Cost of Attendance: 32532 ⟵ “John's Annual Cost of Attendance | $32,532”
### `ae0c3826ca5d016c` University of Maryland Global Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.umgc.edu/transfers-and-credits/fast-paths-to-credit/credit-by-exam/international-baccalaureate (sha256 1fde09f93cf7)
- issues: score_column_not_scores
- checks: {"distinct_exams": 19, "equivalencies": 47, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology (Higher-Level)]:  ⟵ “Biology (Higher-Level) | 5 | 4 lower-level elective credits”
  - equivalencies[IB-BIOLOGY|Biology (Higher-Level)]:  ⟵ “Biology (Higher-Level) | 6 or 7 | BIOL 103 and 4 lower-level biology elective credits”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business Management (Higher-Level)]:  ⟵ “Business Management (Higher-Level) | 5, 6, or 7 | BMGT 110”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business Management (Standard-Level)]:  ⟵ “Business Management (Standard-Level) | 5, 6, or 7 | BMGT 110”
  - equivalencies[IB-CHEMISTRY|Chemistry (Higher-Level)]:  ⟵ “Chemistry (Higher-Level) | 5 | CHEM 103”
  - equivalencies[IB-CHEMISTRY|Chemistry (Higher-Level)]:  ⟵ “Chemistry (Higher-Level) | 6 or 7 | CHEM 103 and 2 lower-level chemistry elective credits”
  - equivalencies[IB-CHEMISTRY|Chemistry (Standard-Level)]:  ⟵ “Chemistry (Standard-Level) | 5 | CHEM 103”
  - equivalencies[IB-CHEMISTRY|Chemistry (Standard-Level)]:  ⟵ “Chemistry (Standard-Level) | 6 or 7 | CHEM 103 and 2 lower-level chemistry elective credits”
  - equivalencies[IB-LATIN|Classical Languages: Latin (Higher-Level)]:  ⟵ “Classical Languages: Latin (Higher-Level) | 5, 6, or 7 | 4 lower-level LATN elective credits”
  - equivalencies[IB-LATIN|Classical Languages: Latin (Standard-Level)]:  ⟵ “Classical Languages: Latin (Standard-Level) | 5, 6, or 7 | 4 lower-level LATN elective credits”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science (Higher-Level)]:  ⟵ “Computer Science (Higher-Level) | 6 or 7 | 3 lower-level computing elective credits”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science (Standard-Level)]:  ⟵ “Computer Science (Standard-Level) | N/A | Not transferable”
  - equivalencies[IB-ECONOMICS|Economics (Higher-Level)]:  ⟵ “Economics (Higher-Level) | 6 or 7 | ECON 201 and ((course.econ.203!id))”
  - equivalencies[IB-ECONOMICS|Economics (Standard-Level)]:  ⟵ “Economics (Standard-Level) | 6 or 7 | ECON 201”
  - equivalencies[IB-ENGLISH-A-LITERATURE|English A: Literature (Higher-Level)]:  ⟵ “English A: Literature (Higher-Level) | N/A | Not transferable”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|Environmental Systems and Societies (Standard-Level)]:  ⟵ “Environmental Systems and Societies (Standard-Level) | N/A | Not transferable”
  - equivalencies[IB-FILM|Film (Higher-Level)]:  ⟵ “Film (Higher-Level) | 5, 6, or 7 | 3 lower-level humanities elective credits”
  - equivalencies[IB-FILM|Film (Standard-Level)]:  ⟵ “Film (Standard-Level) | N/A | Not transferable”
  - equivalencies[IB-GEOGRAPHY|Geography (Higher-Level)]:  ⟵ “Geography (Higher-Level) | 5, 6, or 7 | GEOG 100”
  - equivalencies[IB-GEOGRAPHY|Geography (Standard-Level)]:  ⟵ “Geography (Standard-Level) | 5, 6, or 7 | GEOG 100”
  - equivalencies[IB-GLOBAL-POLITICS|Global Politics (Higher-Level)]:  ⟵ “Global Politics (Higher-Level) | 6 or 7 | 3 lower-level political science elective credits”
  - equivalencies[IB-GLOBAL-POLITICS|Global Politics (Standard-Level)]:  ⟵ “Global Politics (Standard-Level) | 6 or 7 | 3 lower-level political science elective credits”
  - equivalencies[IB-HISTORY|History (Higher-Level)]:  ⟵ “History (Higher-Level) | 5, 6, or 7 | 3 lower-level history elective credits”
  - equivalencies[IB-HISTORY|History (Standard-Level)]:  ⟵ “History (Standard-Level) | N/A | Not transferable”
  - equivalencies[IB-HISTORY|History: Africa (Higher-Level)]:  ⟵ “History: Africa (Higher-Level) | 5 | 3 lower-level history elective credits”
  - … 22 more rows
### `0144661584a456b2` University of Maryland-College Park — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.umd.edu/resources-policies/satisfactory-academic-progress (sha256 ecd111e424ca)
- issues: semantic_review_required, conflicting_sources:https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/,https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/office-student-financial-aid.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The Committee may waive these guidelines and consider cases of unusual hardship, personal injury, death of a relative, or other special circumstances.”
### `0b79cf4f12472ce5` University of Maryland-College Park — appeals 2026-27 [new] (labeled_in_source)
- source: https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/ (sha256 6d019794e6a1)
- issues: semantic_review_required, conflicting_sources:https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/office-student-financial-aid.pdf,https://financialaid.umd.edu/resources-policies/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Change in Financial Situation Students are responsible for notifying the Office of Student Financial Aid of any changes to their financial circumstances during the year.”
### `6842f7af4514ffca` University of Maryland-College Park — appeals 2026-27 [new] (labeled_in_source)
- source: https://admissions.umd.edu/tuition/transfer-merit-scholarships (sha256 880767b02ff4)
- issues: semantic_review_required, conflicting_sources:https://admissions.umd.edu/tuition/freshman-merit-scholarships
- checks: {"negative_sentences": 1, "sentences": 1}
  - sentence: competing_offer_review ⟵ “Students cannot appeal their merit scholarship decisions, and the university does not match scholarship offers from other institutions.”
### `9296ec4a5fcc569b` University of Maryland-College Park — appeals 2026-27 [new] (source_unlabeled)
- source: https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/office-student-financial-aid.pdf (sha256 15602a46a326)
- issues: semantic_review_required, conflicting_sources:https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/,https://financialaid.umd.edu/resources-policies/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Ofﬁce of Student Financial Aid 1 OFFICE OF STUDENT Change in Financial Situation Students are responsible for notifying the Ofﬁce of Student Financial Aid FINANCIAL AID of any changes to their ﬁnancial circumstances during the year.”
### `a737583588986894` University of Maryland-College Park — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.umd.edu/resources-policies/satisfactory-academic-progress (sha256 ecd111e424ca)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “Students on SAP suspension may re-establish eligibility by submitting an SAP appeal form for reconsideration.”
  - sentence: sap_appeal ⟵ “This letter will include instructions on how to submit a SAP appeal.”
  - sentence: sap_appeal ⟵ “The SAP appeal should describe the unusual circumstances that caused you not to meet the SAP requirements and must detail what has changed that will allow you to meet these requirements in the future.”
  - sentence: sap_appeal ⟵ “Please review the SAP Appeal Form for details.”
  - sentence: sap_appeal ⟵ “If you believe you should have received the SAP appeal letter from our office but did not, please review the SAP Appeal Form, which must be submitted along with the SAP Academic Plan and a letter from a third party.”
  - sentence: sap_appeal ⟵ “Once completed, you can submit these documents via email (umdfinaid@umd.edu), in-person, or by mail: 0115 Mitchell Building Attn: Satisfactory Academic Progress Committee 7999 Regents Drive University of Maryland College Park, MD 20742 Appeal Outcomes SAP Appeals may be approved, approved with conditions or denied.”
### `dd056e2e10661a3e` University of Maryland-College Park — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.umd.edu/tuition/freshman-merit-scholarships (sha256 da73b15a780f)
- issues: semantic_review_required, conflicting_sources:https://admissions.umd.edu/tuition/transfer-merit-scholarships
- checks: {"negative_sentences": 1, "sentences": 1}
  - sentence: competing_offer_review ⟵ “Students cannot appeal their merit scholarship decisions and the university does not match offers from other institutions.”
### `237a5e765bc907a2` University of Maryland-College Park — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/tuition-fees/ (sha256 bc797311f4c8)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 11015.0 ⟵ “Tuition | $11,015.00”
  - column:Additional Differential Tuition for full-time juniors and seniors who are majoring in Business, Engineering, or Computer Science (regardless of residency classification): 3375.0 ⟵ “Additional Differential Tuition for full-time juniors and seniors who are majoring in Business, Engineering, or Computer Science (regardless of residency classification) | $3,375.00”
  - column:Mandatory Fees (includes Tech fee). Maximum charged to all students registered for 9 or more credits: 1820.0 ⟵ “Mandatory Fees (includes Tech fee). Maximum charged to all students registered for 9 or more credits | $1,820.00”
  - column:Board (Resident Dining Plan - Base Plan): 6820.0 ⟵ “Board (Resident Dining Plan - Base Plan) | $6,820.00”
  - column:Room (Standard 2-person w/AC, includes Telecom fee): 10290.0 ⟵ “Room (Standard 2-person w/AC, includes Telecom fee) | $10,290.00”

## Re-verification of existing records (57)

- source_not_fetched: data/institutions/carrollcc/credit_policies/2026-27.json ["credit_policies", "ipeds-405872", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/carrollcc/credit_policies/2026-27.json ["credit_policies", "ipeds-405872", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/cecil/credit_policies/2026-27.json ["credit_policies", "ipeds-162104", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/chesapeake/credit_policies/2026-27.json ["credit_policies", "ipeds-162168", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/csmd/credit_policies/2026-27.json ["credit_policies", "ipeds-162122", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/csmd/credit_policies/2026-27.json ["credit_policies", "ipeds-162122", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/ccbcmd/costs/2026-27.json ["costs", "ipeds-434672", null, "2026-27", {"residency": "out_of_state"}]
- source_not_fetched: data/institutions/garrettcollege/credit_policies/2026-27.json ["credit_policies", "ipeds-162609", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/garrettcollege/credit_policies/2026-27.json ["credit_policies", "ipeds-162609", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/garrettcollege/credit_policies/2026-27.json ["credit_policies", "ipeds-162609", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/garrettcollege/transfer_policies/2026-27.json ["transfer_policies", "ipeds-162609", null, "2026-27", {}]
- source_not_fetched: data/institutions/hagerstowncc/credit_policies/2026-27.json ["credit_policies", "ipeds-162690", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/hood/credit_policies/2026-27.json ["credit_policies", "ipeds-162760", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/jhu/academic_programs/2026-27.json ["academic_programs", "ipeds-162928", null, "2026-27", {"program_key": "requirements-for-a-bachelor-s-degree"}]
- source_not_fetched: data/institutions/jhu/academic_programs/2026-27.json ["academic_programs", "ipeds-162928", null, "2026-27", {"program_key": "five-year-bm-mm-program"}]
- source_not_fetched: data/institutions/mica/transfer_policies/2026-27.json ["transfer_policies", "ipeds-163295", null, "2026-27", {}]
- source_not_fetched: data/institutions/mcdaniel/transfer_policies/2026-27.json ["transfer_policies", "ipeds-164270", null, "2026-27", {}]
- source_not_fetched: data/institutions/montgomerycollege/credit_policies/2026-27.json ["credit_policies", "ipeds-163426", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/morgan/transfer_policies/2026-27.json ["transfer_policies", "ipeds-163453", null, "2026-27", {}]
- source_not_fetched: data/institutions/salisbury/credit_policies/2026-27.json ["credit_policies", "ipeds-163851", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/salisbury/transfer_policies/2026-27.json ["transfer_policies", "ipeds-163851", null, "2026-27", {}]
- source_not_fetched: data/institutions/stevenson/credit_policies/2025-26.json ["credit_policies", "ipeds-164173", null, "2025-26", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/stevenson/transfer_policies/2026-27.json ["transfer_policies", "ipeds-164173", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/towson/credit_policies/2026-27.json ["credit_policies", "ipeds-164076", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/umes/transfer_policies/2026-27.json ["transfer_policies", "ipeds-163338", null, "2026-27", {}]
- nothing_to_check: data/institutions/umgc/credit_policies/2026-27.json ["credit_policies", "ipeds-163204", null, "2026-27", {"policy_kind": "AP"}]
- nothing_to_check: data/institutions/umgc/credit_policies/2026-27.json ["credit_policies", "ipeds-163204", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "fermentation-science-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "classical-languages-and-literatures-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "communication-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "english-language-and-literature-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "history-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "jewish-studies-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "religions-of-the-ancient-middle-east-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "arabic-studies-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "chinese-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "french-language-and-literature-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "global-culture-and-thought-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "italian-studies-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "japanese-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "romance-languages-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "russian-language-and-literature-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "philosophy-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "philosophy-politics-and-economics-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "accounting-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "information-systems-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "finance-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "international-business-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "supply-chain-management-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "management-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "marketing-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "biochemistry-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "computer-science-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "physics-major"}]
- source_not_fetched: data/institutions/umd/academic_programs/2026-27.json ["academic_programs", "ipeds-163286", null, "2026-27", {"program_key": "biological-sciences-major"}]
- nothing_to_check: data/institutions/umd/transfer_policies/2026-27.json ["transfer_policies", "ipeds-163286", null, "2026-27", {}]
- source_not_fetched: data/institutions/washcoll/transfer_policies/2026-27.json ["transfer_policies", "ipeds-164216", null, "2026-27", {}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Towson University: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency
- University of Maryland Global Campus: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- University of Maryland-College Park: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, residency
