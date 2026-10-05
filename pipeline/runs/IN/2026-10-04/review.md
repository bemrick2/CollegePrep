# Review queue — IN (2026-27)

Pages fetched: 3475; failures: 260. Candidates: 753 (410 without issues, 343 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 9 | 11 | 26 | 3 | 4 |
| cost_of_attendance | 0 | 0 | 3 | 6 | 34 | 6 | 4 |
| admissions_tests | 0 | 0 | 0 | 1 | 42 | 6 | 4 |
| common_data_set | 0 | 0 | 0 | 1 | 4 | 44 | 4 |
| merit_scholarships | 0 | 0 | 5 | 4 | 35 | 5 | 4 |
| ap_credit | 0 | 0 | 8 | 7 | 12 | 22 | 4 |
| clep_credit | 0 | 0 | 2 | 6 | 11 | 30 | 4 |
| ib_credit | 0 | 0 | 6 | 3 | 8 | 32 | 4 |
| dual_enrollment | 0 | 0 | 8 | 6 | 19 | 16 | 4 |
| transfer_credit | 0 | 0 | 11 | 5 | 26 | 7 | 4 |
| statewide_articulation | 0 | 0 | 0 | 0 | 21 | 28 | 4 |
| residency | 0 | 0 | 0 | 0 | 23 | 26 | 4 |
| degree_requirements | 0 | 0 | 2 | 0 | 29 | 18 | 4 |
| aid_appeals | 0 | 0 | 0 | 30 | 4 | 15 | 4 |

## Ready for review (410)

### `b1dc34b90864a7d9` Bethel University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://betheluniversity.edu/admissions-aid/reach/ (sha256 de66d4424890)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 100 ⟵ “The REACH program gives you the option to pay reduced tuition of $100 per credit hour for the first 24 credit hours (limited to six credit hours per semester). You could save up to $12,000 off the full-time traditional student rate! Payment for courses is due at the time of registration. Most course”
### `4534ee2e19672804` Butler University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.butler.edu/registrar/transferring-credits-to-butler/credit-through-testing/advanced-placement-credit/ (sha256 38514b872c0f)
- checks: {"distinct_exams": 35, "equivalencies": 40, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|—]:  ⟵ “African American Studies | — | No credit awarded”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History | 4 or 5 | 3 hrs, ART 105”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4 or 5]:  ⟵ “Computer Science Principles | 4 or 5 | 3 hrs, AR 220 CS”
  - equivalencies[AP-BIOLOGY|4 or 5]:  ⟵ “Biology | 4 or 5 | 5 hrs, NW 204-BI (or BI 105, if in College of Pharmacy and Health Sciences)”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “Calculus AB | 4 or 5 | 4 hrs, MA 106 (fulfills AR core)”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “Calculus BC | 4 or 5 | 4 hrs, MA 106 (fulfills AR core) and 4 hrs, MA 107(Calculus AB Subscore 4 or 5, 4 hrs, MA 106)”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “Chemistry | 4 or 5 | 4 hrs, CH 105 (Recommend placement in CH 107 if additional Chemistry is required for program of study) (or NUR 107 if Nursing major)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Chinese Language and Culture | 4 or 5 | 3 hrs, 300-level Chinese skills elective (must begin in 300-level CN course or above)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4 or 5]:  ⟵ “Computer Science A | 4 or 5 | 3 hrs, CS 142”
  - equivalencies[AP-MACROECONOMICS|4 or 5]:  ⟵ “Economics—Macro | 4 or 5 | 3 hrs, SW 220 EC or EC elective(or EC 232, if in Lacy School of Business or Healthcare and Business major or if Economics major in LAS)”
  - equivalencies[AP-MICROECONOMICS|4 or 5]:  ⟵ “Economics—Micro | 4 or 5 | 3 hrs, SW 220 EC or EC elective(or EC 231, if in Lacy School of Business or Healthcare and Business major or if Economics major in LAS)”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4 or 5]:  ⟵ “English Language & Composition | 4 or 5 | 3 hrs, EN 200-level elective”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4 or 5]:  ⟵ “English Literature & Composition | 4 or 5 | 3 hrs, EN 200-level elective”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4 or 5]:  ⟵ “Environmental Science | 4 or 5 | 5 hrs, NW 225-ENV”
  - equivalencies[AP-EUROPEAN-HISTORY|4 or 5]:  ⟵ “European History | 4 or 5 | 3 hrs, 100-level history elective (and exemption from corresponding 200-level European History requirement for History majors)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4 or 5]:  ⟵ “French Language and Culture | 4 or 5 | 3 hrs, 300-level French skills elective (must begin in 300-level FR course or above)”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4 or 5]:  ⟵ “German Language and Culture | 4 or 5 | 3 hrs, 300-level German skills elective (must begin in 300-level GR course or above)”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4 or 5]:  ⟵ “Human Geography | 4 or 5 | 3 hrs, GE 109”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Italian Language and Culture | 4 or 5 | Refer to Department Chair”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4 or 5]:  ⟵ “Japanese Language and Culture | 4 or 5 | Refer to Department Chair”
  - equivalencies[AP-LATIN|4 or 5]:  ⟵ “Latin | 4 or 5 | 3 hrs, LT 204 (must begin in 300-level LT course or above)”
  - equivalencies[AP-MUSIC-THEORY|4 or 5]:  ⟵ “Music Theory* | 4 or 5 | 3 hrs, MT 100”
  - equivalencies[AP-PHYSICS-1|4 or 5]:  ⟵ “Physics 1 | 4 or 5 | 4 hrs, PH 107 or 5 hrs, NW 262-PH”
  - equivalencies[AP-PHYSICS-2|4 or 5]:  ⟵ “Physics 2 | 4 or 5 | 4 hrs, PH 108 or 5 hrs, NW 262-PH”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4 or 5]:  ⟵ “Physics C Electricity and Magnetism | 4 or 5 | 5 hrs, NW 262-PH or PH elective”
  - … 15 more rows
### `f6ca5df4073a7289` Butler University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.butler.edu/registrar/transferring-credits-to-butler/credit-through-testing/international-baccalaureate-credit/ (sha256 97e01e08df39)
- checks: {"distinct_exams": 27, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|HL 5–7]:  ⟵ “Biology HL | 5–7 | 5 hrs, NW 204-BI (or BI 105, if in College of Health Professions)”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 5–7]:  ⟵ “Business Management HL | 5–7 | 3 hrs, MG 100 level elective”
  - equivalencies[IB-CHEMISTRY-HL|HL 5–7]:  ⟵ “Chemistry HL | 5–7 | 8 hrs, CH 105 and CH 106 (fulfills NW core; placement in CH 321 or CH 351 if additional chemistry is required for program of study), or 4hrs, NUR 107 if admitted to the Nursing program”
  - equivalencies[IB-CHEMISTRY-SL|SL 5–7]:  ⟵ “Chemistry SL | 5–7 | 4 hrs, CH 105 (recommend placement in CH 107 if additional chemistry is required for program of study)”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 5–7]:  ⟵ “Computer Science HL | 5–7 | 3 hrs, CS 142 or SE 132”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|SL 5–7]:  ⟵ “Computer Science SL | 5–7 | 3 hrs, AR 220 CS”
  - equivalencies[IB-ECONOMICS-HL|HL 5–7]:  ⟵ “Economics HL | 5–7 | 3 hrs, SW 220 EC”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-HL|HL 5–7]:  ⟵ “Environmental Systems and Societies HL | 5–7 | 5 hrs, NW 225-ENV”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|SL 5–7]:  ⟵ “Environmental Systems and Societies SL | 5–7 | 3 hrs, ENV 200-level elective”
  - equivalencies[IB-GEOGRAPHY-HL|HL 5–7]:  ⟵ “Geography HL | 5–7 | 3 hrs, GE 109”
  - equivalencies[IB-GLOBAL-POLITICS-HL|HL 5–7]:  ⟵ “Global Politics HL | 5–7 | 3 hrs, PO 100 level elective”
  - equivalencies[IB-HISTORY-HL|HL 5–7]:  ⟵ “History HL | 5–7 | 3 hrs, HST 100 level elective and exemption from corresponding 200 level requirement (European or World History) for history major or minors”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-SL|SL 5–7]:  ⟵ “Mathematics: Applications& Interpretation SL | 5–7 | 3 hrs, AR elective (fulfills AR core)”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|SL 5–7]:  ⟵ “Mathematics: Analysis & Approaches SL | 5–7 | 3 hrs, AR elective (fulfills AR core)”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|HL 5–7]:  ⟵ “Mathematics: Analysis & Approaches HL | 5–7 | 4 hrs, MA 106 (fulfills AR core)”
  - equivalencies[IB-MUSIC-HL|HL 5–7]:  ⟵ “Music HL | 5–7 | 2 hrs, MT 200 level elective + 2 hrs, MH 200 level elective + 2 hrs, AM 200 level elective”
  - equivalencies[IB-MUSIC-SL|SL 5–7]:  ⟵ “Music SL | 5–7 | 1 hr, MT 200 level elective + 2 hrs, MH 200 level elective + 1 hr, AM 200 level elective”
  - equivalencies[IB-PHILOSOPHY-HL|HL 5–7]:  ⟵ “Philosophy HL | 5–7 | 3 hrs, TI 244 PL”
  - equivalencies[IB-PHILOSOPHY-SL|SL 5–7]:  ⟵ “Philosophy SL | 5–7 | 3 hrs, PL 100 level elective”
  - equivalencies[IB-PHYSICS-HL|HL 5–7]:  ⟵ “Physics HL | 5–7 | 5 hrs, NW 262 PH or PH 100 level elective”
  - equivalencies[IB-PSYCHOLOGY-HL|HL 5–7]:  ⟵ “Psychology HL | 5–7 | 3 hrs, SW 250 PS + 3 hrs, PS 200 level elective”
  - equivalencies[IB-PSYCHOLOGY-SL|SL 5–7]:  ⟵ “Psychology SL | 5–7 | 3 hrs, SW 250 PS”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|HL 5–7]:  ⟵ “Social and Cultural Anthropology HL | 5–7 | 3 hrs, AN 100 level elective and exemption from SW 215 AN for anthropology majors and minors”
  - equivalencies[IB-THEATRE-HL|HL 5–7]:  ⟵ “Theatre HL | 5–7 | 3 hrs, PCA 255 TH, PCA 250 TH, PCA 225 TH, or TH 382”
  - equivalencies[IB-THEATRE-SL|SL 5–7]:  ⟵ “Theatre SL | 5–7 | 3 hrs, PCA 255 TH, PCA 250 TH, PCA 225 TH, or TH 382”
  - … 4 more rows
### `734324e7b9461b57` Calumet College of Saint Joseph — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ccsj.edu/admissions/overview/transfer/ (sha256 f01f727d1303)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “Students can ordinarily satisfy the College’s residency requirements for bachelor’s degrees by registering and passing the final 30 semester hours of scheduled coursework at Calumet College of St.”
### `m783377c82af4837` Earlham College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://earlham.edu/admissions/how-to-apply/transfer-admissions/ (sha256 a188e98ed1d7)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Earlham College transfers credit on a course-by-course basis using the following guidelines: The coursework falls within the scope of a liberal arts curriculum You have received a grade of C or better An official transcript is received by the Office of the Registrar directly from a fully accredited college or university after the coursework is completed A course description and syllabus are provid”
  - min_grade: C ⟵ “Earlham College transfers credit on a course-by-course basis using the following guidelines: The coursework falls within the scope of a liberal arts curriculum You have received a grade of C or better An official transcript is received by the Office of the Registrar directly from a fully accredited college or university after the coursework is completed A course description and syllabus are provid”
### `1f734e89abdbf2f0` Grace College and Theological Seminary — awards 2026-27 [new] (source_unlabeled)
- source: https://www.grace.edu/admissions/financial-aid-scholarships/scholarships-and-grants/ (sha256 7561f6752f68)
- checks: {"thresholds": null}
  - award_amount_text: $12,000 per year ⟵ “Under 3.25 | $12,000 per year | Achievement Scholarship”
  - gpa_requirement: Under 3.25 ⟵ “Under 3.25 | $12,000 per year | Achievement Scholarship”
### `e5ada6726c82090f` Grace College and Theological Seminary — awards 2026-27 [new] (source_unlabeled)
- source: https://www.grace.edu/admissions/financial-aid-scholarships/scholarships-and-grants/ (sha256 7561f6752f68)
- checks: {"thresholds": null}
  - award_amount_text: $14,000 per year ⟵ “3.75 - 3.99 | $14,000 per year | Dean's Scholarship”
  - gpa_requirement: 3.75 - 3.99 ⟵ “3.75 - 3.99 | $14,000 per year | Dean's Scholarship”
### `ec52665675f49f00` Grace College and Theological Seminary — awards 2026-27 [new] (source_unlabeled)
- source: https://www.grace.edu/admissions/financial-aid-scholarships/scholarships-and-grants/ (sha256 7561f6752f68)
- checks: {"thresholds": null}
  - award_amount_text: $13,000 per year ⟵ “3.25 - 3.74 | $13,000 per year | Honors Scholarship”
  - gpa_requirement: 3.25 - 3.74 ⟵ “3.25 - 3.74 | $13,000 per year | Honors Scholarship”
### `fa813bc7c5837393` Grace College and Theological Seminary — awards 2026-27 [new] (source_unlabeled)
- source: https://www.grace.edu/admissions/financial-aid-scholarships/scholarships-and-grants/ (sha256 7561f6752f68)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $15,000 per year ⟵ “4.0+ | $15,000 per year | Provost's Scholarship”
  - gpa_requirement: 4.0+ ⟵ “4.0+ | $15,000 per year | Provost's Scholarship”
### `9d26ca4f6706260e` Grace College and Theological Seminary — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.grace.edu/admissions/tuition-costs/ (sha256 67f6903206a0)
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - on_campus:Undergraduate Tuition - 12-18 hour block (Freshman, Transfer): 32458 ⟵ “Undergraduate Tuition - 12-18 hour block (Freshman, Transfer) | $32,458 | $32,458”
  - on_campus:Food and Housing - First Year Students: 11198 ⟵ “Food and Housing - First Year Students | $11,198 | $0”
  - on_campus:Comprehensive Student Fee: 900 ⟵ “Comprehensive Student Fee | $900 | $900”
  - on_campus:Total Direct Costs: 44556 ⟵ “Total Direct Costs | $44,556 | $33,358”
  - with_parents_or_family:Undergraduate Tuition - 12-18 hour block (Freshman, Transfer): 32458 ⟵ “Undergraduate Tuition - 12-18 hour block (Freshman, Transfer) | $32,458 | $32,458”
  - with_parents_or_family:Food and Housing - First Year Students: 0 ⟵ “Food and Housing - First Year Students | $11,198 | $0”
  - with_parents_or_family:Comprehensive Student Fee: 900 ⟵ “Comprehensive Student Fee | $900 | $900”
  - with_parents_or_family:Total Direct Costs: 33358 ⟵ “Total Direct Costs | $44,556 | $33,358”
### `11f49349568aa959` Hanover College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.hanover.edu/admission/financialaid/ (sha256 402b7734e7b8)
- checks: {"thresholds": null}
  - award_amount_text: $31,000 ⟵ “Founder’s | 3.75-3.99 | $31,000”
  - gpa_requirement: 3.75-3.99 ⟵ “Founder’s | 3.75-3.99 | $31,000”
### `212c27b73fdc813e` Hanover College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.hanover.edu/admission/financialaid/ (sha256 402b7734e7b8)
- checks: {"thresholds": null}
  - award_amount_text: $23,000 ⟵ “Dean’s | 3.24 and below | $23,000”
  - gpa_requirement: 3.24 and below ⟵ “Dean’s | 3.24 and below | $23,000”
### `22a52c46e9b3fe15` Hanover College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.hanover.edu/admission/financialaid/ (sha256 402b7734e7b8)
- checks: {"thresholds": null}
  - award_amount_text: $29,000 ⟵ “Presidential | 3.50-3.74 | $29,000”
  - gpa_requirement: 3.50-3.74 ⟵ “Presidential | 3.50-3.74 | $29,000”
### `26f1f6763609b602` Hanover College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.hanover.edu/admission/financialaid/ (sha256 402b7734e7b8)
- checks: {"thresholds": null}
  - award_amount_text: $25,000 ⟵ “Trustee | 3.25-3.49 | $25,000”
  - gpa_requirement: 3.25-3.49 ⟵ “Trustee | 3.25-3.49 | $25,000”
### `54ea9dc2293253a8` Hanover College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.hanover.edu/admission/financialaid/ (sha256 402b7734e7b8)
- checks: {"thresholds": null}
  - award_amount_text: $34,000 ⟵ “Bicentennial | 4.0-4.24 | $34,000”
  - gpa_requirement: 4.0-4.24 ⟵ “Bicentennial | 4.0-4.24 | $34,000”
### `ed08f814715f2b0d` Hanover College — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.hanover.edu/admission/financialaid/ (sha256 402b7734e7b8)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 48082 ⟵ “Tuition | $48,082 | Your rate is locked for four years!”
  - column:Avg. Housing: 8664 ⟵ “Avg. Housing | $8,664 | This is the average cost of Hanover housing. Your cost might be a little higher or lower based on the type of room selected.”
  - column:Food (meal plan): 8163 ⟵ “Food (meal plan) | $8,163 | This is the cost of any meal plan we offer. May change slightly based on the final dining vendor contract.”
  - column:General Fee: 1245 ⟵ “General Fee | $1,245 | The general fee covers the student activity fee, health services, IT support, etc.”
  - column:Books: 750 ⟵ “Books | $750 | This fee covers required textbooks (printed and/or electronic).”
  - column:Other Charges: 590 ⟵ “Other Charges | $590 | These charges include orientation ($350 – first year only); Tenant Insurance to cover potential incident-related damage to room or belongings ($120); and Laundry ($120).”
  - column:TOTAL: 67494 ⟵ “TOTAL | $67,494 | This total reflects the costs directly charged by Hanover College to all incoming first-year students before applying scholarships and aid.”
### `69559aacf0c2c3c7` Huntington University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.huntington.edu/academics/academic-catalog/undergraduate-catalog/admissions-information/transfer-students (sha256 4acee95530ff)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Only courses with a grade of C or higher will transfer, and applicability to specific majors is determined by the registrar.”
### `12fef3ad8d1c6372` Indiana University-East — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://east.iu.edu/admissions/apply/ap-exam.html (sha256 2221b1ec5c73)
- checks: {"distinct_exams": 42, "equivalencies": 62, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, 5]:  ⟵ “African American Studies | 3, 4, 5 | 3 Hours | HIST UNDI 100”
  - equivalencies[AP-ART-HISTORY|3, 4, 5]:  ⟵ “Art History | 3, 4, 5 | 3 Hours | FINA-A 101”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 Hours | BIOL UNDI 100”
  - equivalencies[AP-BIOLOGY|4, 5]:  ⟵ “Biology | 4, 5 | 8 Hours | BIOL-L 101 & L 102”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3, 4, 5]:  ⟵ “Business with Personal Finance | 3, 4, 5 | 6 Hours | BUS-W 100 & BUS-F 260”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 3 Hours | MATH-M 119”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “Calculus AB | 4, 5 | 5 Hours | MATH-M 215”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 3 Hours | MATH-M 119”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC | 4, 5 | 10 Hours | MATH-M 215 & M 216”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 5 Hours | CHEM-C 101 & C 121”
  - equivalencies[AP-CHEMISTRY|4,5]:  ⟵ “Chemistry | 4,5 | 5 Hours | CHEM-C 105 & C 125”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | 3 Hours | LANG UNDI 200”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4, 5]:  ⟵ “Chinese Language and Culture | 4, 5 | 6 Hours | LANG UNDI 200 & 250”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “Comparative Government and Politics | 3, 4, 5 | 3 Hours | POLS-Y 107”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, 5]:  ⟵ “Computer Science A | 3, 4, 5 | 4 Hours | INFO-I 210”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | 3 Hours | CSCI UNDI 100”
  - equivalencies[AP-CYBERSECURITY|3, 4, 5]:  ⟵ “Cybersecurity | 3, 4, 5 | 3 Hours | CSCI UNDI 100”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | 3 Hours | ENG-UNDI 100”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4, 5]:  ⟵ “English Language and Composition | 4, 5 | 3 Hours | ENG-W 131”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, 5]:  ⟵ “English Literature and Composition | 3, 4, 5 | 3 Hours | ENG-L 202”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3, 4, 5]:  ⟵ “Environmental Science | 3, 4, 5 | 3 Hours | BIOL-L 108”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 3 Hours | HIST-H 103”
  - equivalencies[AP-EUROPEAN-HISTORY|4, 5]:  ⟵ “European History | 4, 5 | 6 Hours | HIST-H 103 & H 104”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | 3 | 3 Hours | FREN-F 200”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4, 5]:  ⟵ “French Language and Culture | 4, 5 | 6 Hours | FREN-F 200 & F 250”
  - … 37 more rows
### `75fa466a7ae7d2ec` Indiana University-East — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://east.iu.edu/admissions/apply/credit-prior-learning.html (sha256 64067a286440)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 21.5 ⟵ “The fee to transcribe your prior learning credit onto your transcript from departmental exams or a portfolio is $21.50 per credit hour. The fees become part of a student’s current bursar bill and can be satisfied using financial aid. Students are not expected to pay the fees before the credit is pos”
### `a71366bb7fec0e2b` Indiana University-East — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://east.iu.edu/admissions/apply/clep-exam.html (sha256 18ae19e033af)
- checks: {"distinct_exams": 29, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 6 Hours | ENG-L 250 & L 251”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 Hours | ENG-L 202”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 Hours | ENG UNDI 100”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 6 Hours | HUMA UNDI 100”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 Hours | MATH-M 123”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 Hours | MATH-H 111”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 3 Hours | BIOL-L 104”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 3 Hours | CHEM-C 101”
  - equivalencies[CLEP-CHEMISTRY|65]:  ⟵ “Chemistry | 65 | 3 Hours | CHEM-C 105”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 5 Hours | MATH-M 215”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 6 Hours | MATH-M 125/M 126”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level 1 | 50 | 8 Hours | GER-G 100/G 150”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “German Language, Level 2 | 63 | 14 Hours | GER-G 100/G 150/G 200/G 250”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level 1 | 50 | 8 Hours | FREN-F 100/F 150”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, Level 2 | 59 | 14 Hours | FREN-F 100/F 150/F 200/F 250”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1 | 50 | 8 Hours | SPAN-S 100/S 150”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language, Level 2 | 63 | 14 Hours | SPAN-S 100/S 150/S 200/S 250”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing, Levels 1 and 2 | 50 | 8 Hours | SPAN-S 100/S 150”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|57]:  ⟵ “Spanish with Writing, Levels 1 and 2 | 57 | 11 Hours | SPAN-S 100/S 150/S 200”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|63]:  ⟵ “Spanish with Writing, Levels 1 and 2 | 63 | 14 Hours | SPAN-S 100/S 150/S 200/S 250”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 Hours | POLS-Y 103”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States 1: Early Colonization to 1877 | 50 | 3 Hours | HIST-H 105”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States 2 | 50 | 3 Hours | HIST-H 106”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | 3 Hours | HIST-H 108”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | 3 Hours | HIST-H 109”
  - … 10 more rows
### `d45883177f43bd9f` Indiana University-East — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://east.iu.edu/admissions/apply/ib-exam.html (sha256 6d9276d699a1)
- checks: {"distinct_exams": 43, "equivalencies": 63, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-SL|SL 5, 6, or 7]:  ⟵ “Biology SL | 5, 6, or 7 | 5 Hours | BIOL-L 100”
  - equivalencies[IB-BIOLOGY-HL|HL 4]:  ⟵ “Biology HL | 4 | 5 Hours | BIOL-L 100”
  - equivalencies[IB-BIOLOGY-HL|HL 5, 6, or 7]:  ⟵ “Biology HL | 5, 6, or 7 | 8 Hours | BIOL-L 101 & L 102”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|SL 4, 5, 6, or 7]:  ⟵ “Business and Management SL | 4, 5, 6, or 7 | 3 Hours | BUS UNDI 100”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 4, 5, 6, or 7]:  ⟵ “Business and Management HL | 4, 5, 6, or 7 | 3 Hours | BUS-W 100”
  - equivalencies[IB-CHEMISTRY-SL|SL 5, 6, or 7]:  ⟵ “Chemistry SL | 5, 6, or 7 | 5 Hours | CHEM-C 101 & CHEM-C 121”
  - equivalencies[IB-CHEMISTRY-HL|HL 4]:  ⟵ “Chemistry HL | 4 | 5 Hours | CHEM-C 101 & CHEM-C 121”
  - equivalencies[IB-CHEMISTRY-HL|HL 5, 6, or 7]:  ⟵ “Chemistry HL | 5, 6, or 7 | 10 Hours | CHEM-C 105, CHEM-C 106, CHEM-C 125 & CHEM-C 126”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|SL 4, 5, 6, or 7]:  ⟵ “Computer Science SL | 4, 5, 6, or 7 | 3 Hours | CSCI UNDI 100”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 4, 5, 6, or 7]:  ⟵ “Computer Science HL | 4, 5, 6, or 7 | 3 Hours | INFO-I 101”
  - equivalencies[IB-ECONOMICS-SL|SL 4, 5, 6, or 7]:  ⟵ “Economics SL | 4, 5, 6, or 7 | 6 Hours | ECON-E 103 & ECON-E 104”
  - equivalencies[IB-ECONOMICS-HL|HL 4, 5, 6, or 7]:  ⟵ “Economics HL | 4, 5, 6, or 7 | 6 Hours | ECON-E 103 & ECON-E 104”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-SL|SL 4, 5]:  ⟵ “English A: language and literature SL | 4, 5 | 3 Hours | ENG UNDI 100”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-SL|SL 6, 7]:  ⟵ “English A: language and literature SL | 6, 7 | 3 Hours | ENG-G 205”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|HL 4, 5, 6, or 7]:  ⟵ “English A: language and literature HL | 4, 5, 6, or 7 | 3 Hours | ENG-G 205”
  - equivalencies[IB-ENGLISH-A-LITERATURE-SL|SL 4, 5]:  ⟵ “English A: literature SL | 4, 5 | 3 Hours | ENG UNDI 100”
  - equivalencies[IB-ENGLISH-A-LITERATURE-SL|SL 6, 7]:  ⟵ “English A: literature SL | 6, 7 | 3 Hours | ENG-L 260”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|HL 4, 5, 6, or 7]:  ⟵ “English A: literature HL | 4, 5, 6, or 7 | 3 Hours | ENG-L 260”
  - equivalencies[IB-FILM-HL|HL 4, 5, 6, or 7]:  ⟵ “Film HL | 4, 5, 6, or 7 | 3 Hours | TEL UNDI 100”
  - equivalencies[IB-FRENCH-HL|HL 4, 5, 6, or 7]:  ⟵ “French A HL | 4, 5, 6, or 7 | 3 Hours | LANG UNDI 100”
  - equivalencies[IB-FRENCH-SL|SL 4]:  ⟵ “French B SL | 4 | 4 Hours | FREN-F 100”
  - equivalencies[IB-FRENCH-SL|SL 5]:  ⟵ “French B SL | 5 | 8 Hours | FREN-F 100 & FREN-F 150”
  - equivalencies[IB-FRENCH-SL|SL 6]:  ⟵ “French B SL | 6 | 3 Hours | FREN-F 200”
  - equivalencies[IB-FRENCH-SL|SL 7]:  ⟵ “French B SL | 7 | 6 Hours | FREN-F 200 & FREN-F 250”
  - equivalencies[IB-FRENCH-HL|HL 4, 5, 6, or 7]:  ⟵ “French B HL | 4, 5, 6, or 7 | 6 Hours | FREN-F 200 & FREN-F 250”
  - … 38 more rows
### `cc130c5869e13f1e` Indiana University-East — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://east.iu.edu/admissions/apply/transferring-credits.html (sha256 d730a6cfc2b9)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Only courses with a grade of C or better are considered for awarding of transfer credit.”
  - min_grade: C ⟵ “See how your credits could transfer to IU East If you've received a grade of C or better in a class at a regionally accredited university, that coursework will usually transfer to IU.”
### `0ccecdbc7490de0c` Indiana University-Indianapolis — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://indianapolis.iu.edu/cost-aid/cost-of-attendance/ (sha256 277eb86dc844)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and mandatory fees (after MSEP is applied): 15520 ⟵ “Tuition and mandatory fees (after MSEP is applied) | $15,520 | $15,520 | $15,520”
  - on_campus:Housing and Food: 14006 ⟵ “Housing and Food | $14,006 | $14,006 | $4,474”
  - on_campus:Books and supplies: 1320 ⟵ “Books and supplies | $1,320 | $1,320 | $1,320”
  - on_campus:Transportation: 378 ⟵ “Transportation | $378 | $1,770 | $1,770”
  - on_campus:Personal: 2430 ⟵ “Personal | $2,430 | $2,430 | $2,430”
  - on_campus:Total: 33654 ⟵ “Total | $33,654 | $35,046 | $25,514”
  - on_campus:Total direct costs: 29526 ⟵ “Total direct costs | $29,526 | $29,526 | $19,994”
  - off_campus_not_with_family:Tuition and mandatory fees (after MSEP is applied): 15520 ⟵ “Tuition and mandatory fees (after MSEP is applied) | $15,520 | $15,520 | $15,520”
  - off_campus_not_with_family:Housing and Food: 14006 ⟵ “Housing and Food | $14,006 | $14,006 | $4,474”
  - off_campus_not_with_family:Books and supplies: 1320 ⟵ “Books and supplies | $1,320 | $1,320 | $1,320”
  - off_campus_not_with_family:Transportation: 1770 ⟵ “Transportation | $378 | $1,770 | $1,770”
  - off_campus_not_with_family:Personal: 2430 ⟵ “Personal | $2,430 | $2,430 | $2,430”
  - off_campus_not_with_family:Total: 35046 ⟵ “Total | $33,654 | $35,046 | $25,514”
  - off_campus_not_with_family:Total direct costs: 29526 ⟵ “Total direct costs | $29,526 | $29,526 | $19,994”
  - with_parents_or_family:Tuition and mandatory fees (after MSEP is applied): 15520 ⟵ “Tuition and mandatory fees (after MSEP is applied) | $15,520 | $15,520 | $15,520”
  - with_parents_or_family:Housing and Food: 4474 ⟵ “Housing and Food | $14,006 | $14,006 | $4,474”
  - with_parents_or_family:Books and supplies: 1320 ⟵ “Books and supplies | $1,320 | $1,320 | $1,320”
  - with_parents_or_family:Transportation: 1770 ⟵ “Transportation | $378 | $1,770 | $1,770”
  - with_parents_or_family:Personal: 2430 ⟵ “Personal | $2,430 | $2,430 | $2,430”
  - with_parents_or_family:Total: 25514 ⟵ “Total | $33,654 | $35,046 | $25,514”
  - with_parents_or_family:Total direct costs: 19994 ⟵ “Total direct costs | $29,526 | $29,526 | $19,994”
### `2687d90c9a104107` Indiana University-Indianapolis — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://indianapolis.iu.edu/cost-aid/cost-of-attendance/ (sha256 277eb86dc844)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and mandatory fees: 10760 ⟵ “Tuition and mandatory fees | $10,760 | $10,760 | $10,760”
  - on_campus:Housing and Food: 14006 ⟵ “Housing and Food | $14,006 | $14,006 | $4,474”
  - on_campus:Books and supplies: 1320 ⟵ “Books and supplies | $1,320 | $1,320 | $1,320”
  - on_campus:Transportation: 378 ⟵ “Transportation | $378 | $1,770 | $1,770”
  - on_campus:Personal: 2430 ⟵ “Personal | $2,430 | $2,430 | $2,430”
  - on_campus:Total: 28894 ⟵ “Total | $28,894 | $30,286 | $20,754”
  - on_campus:Total direct costs: 24766 ⟵ “Total direct costs | $24,766 | $24,766 | $15,234”
  - off_campus_not_with_family:Tuition and mandatory fees: 10760 ⟵ “Tuition and mandatory fees | $10,760 | $10,760 | $10,760”
  - off_campus_not_with_family:Housing and Food: 14006 ⟵ “Housing and Food | $14,006 | $14,006 | $4,474”
  - off_campus_not_with_family:Books and supplies: 1320 ⟵ “Books and supplies | $1,320 | $1,320 | $1,320”
  - off_campus_not_with_family:Transportation: 1770 ⟵ “Transportation | $378 | $1,770 | $1,770”
  - off_campus_not_with_family:Personal: 2430 ⟵ “Personal | $2,430 | $2,430 | $2,430”
  - off_campus_not_with_family:Total: 30286 ⟵ “Total | $28,894 | $30,286 | $20,754”
  - off_campus_not_with_family:Total direct costs: 24766 ⟵ “Total direct costs | $24,766 | $24,766 | $15,234”
  - with_parents_or_family:Tuition and mandatory fees: 10760 ⟵ “Tuition and mandatory fees | $10,760 | $10,760 | $10,760”
  - with_parents_or_family:Housing and Food: 4474 ⟵ “Housing and Food | $14,006 | $14,006 | $4,474”
  - with_parents_or_family:Books and supplies: 1320 ⟵ “Books and supplies | $1,320 | $1,320 | $1,320”
  - with_parents_or_family:Transportation: 1770 ⟵ “Transportation | $378 | $1,770 | $1,770”
  - with_parents_or_family:Personal: 2430 ⟵ “Personal | $2,430 | $2,430 | $2,430”
  - with_parents_or_family:Total: 20754 ⟵ “Total | $28,894 | $30,286 | $20,754”
  - with_parents_or_family:Total direct costs: 15234 ⟵ “Total direct costs | $24,766 | $24,766 | $15,234”
### `3687d50aea778a19` Indiana University-Kokomo — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.iuk.edu/cost-aid/cost-of-attendance/tuition-and-fees/index.html (sha256 9286851fbd50)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition: 22547.78 ⟵ “Tuition | $11,273.89 | $22,547.78”
  - column:Mandatory Fees: 707.34 ⟵ “Mandatory Fees | $353.67 | $707.34”
  - column:Total Tuition and Fees: 23255.12 ⟵ “Total Tuition and Fees | $11,627.56 | $23,255.12”
### `e8836fb75f4074d5` Indiana University-Kokomo — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.iuk.edu/cost-aid/cost-of-attendance/tuition-and-fees/index.html (sha256 9286851fbd50)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition: 7716.78 ⟵ “Tuition | $3,858.39 | $7,716.78”
  - column:Mandatory Fees: 707.34 ⟵ “Mandatory Fees | $353.67 | $707.34”
  - column:Total Tuition and Fees: 8424.12 ⟵ “Total Tuition and Fees | $4,212.06 | $8,424.12”
### `25d9546121e3ca6c` Indiana University-Kokomo — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.iuk.edu/admissions/transfer-credit/international-baccalaureate-articulation.html (sha256 85bdf7fd8a45)
- checks: {"distinct_exams": 17, "equivalencies": 18, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|HL 4, 5, 6, 7]:  ⟵ “Biology HL | 4, 5, 6, 7 | BIO-L | 121, 122 | 5, 5”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 4, 5, 6, 7]:  ⟵ “Business and Management HL | 4, 5, 6, 7 | BUS-UN | 100 | 3”
  - equivalencies[IB-CHEMISTRY-HL|HL 4, 5, 6, 7]:  ⟵ “Chemistry HL | 4, 5, 6, 7 | CHEM-C | 105, 106, 125 | 3, 3, 2”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 4, 5, 6, 7]:  ⟵ “Computer Science HL | 4, 5, 6, 7 | CSCI-B, CSCI-C | 100, 101 | 4, 4,”
  - equivalencies[IB-ECONOMICS-HL|HL 4, 5, 6, 7]:  ⟵ “Economics HL | 4, 5, 6, 7 | ECON-E | 201, 202 | 3, 3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|HL 4, 5, 6, 7]:  ⟵ “English A Language and Literature HL | 4, 5, 6, 7 | ENG-W, ENG-UN | 131, 100 | 3, 3”
  - equivalencies[IB-FILM-HL|HL 4, 5, 6, 7]:  ⟵ “Film HL | 4, 5, 6, 7 | CMLT-C | 190 | 3”
  - equivalencies[IB-FRENCH-HL|HL 4, 5, 6, 7]:  ⟵ “French B HL | 4, 5, 6, 7 | FREN-F | 203, 204 | 3, 3”
  - equivalencies[IB-GEOGRAPHY|4, 5, 6, 7]:  ⟵ “Geography | 4, 5, 6, 7 | GEOG-G, GEOG-UN | 107, 110, 100 | 3, 3, 2”
  - equivalencies[IB-GERMAN|4, 5, 6, 7]:  ⟵ “German B | 4, 5, 6, 7 | GERM-G | 203, 204 | 3, 3”
  - equivalencies[IB-HISTORY-HL|HL 4, 5, 6, 7]:  ⟵ “History, Americans HL | 4, 5, 6, 7 | HIST-H | 105, 106 | 3, 3”
  - equivalencies[IB-HISTORY-HL|HL 4, 5, 6, 7]:  ⟵ “History, Europe HL | 4, 5, 6, 7 | HIST-H | 113, 114 | 3, 3”
  - equivalencies[IB-MUSIC-HL|HL 4, 5, 6, 7]:  ⟵ “Music HL | 4, 5, 6, 7 | MUS-M | 174 | 3”
  - equivalencies[IB-PHYSICS-HL|HL 4, 5, 6, 7]:  ⟵ “Physics HL | 4, 5, 6, 7 | PHYS-P | 201, 202 | 5, 5”
  - equivalencies[IB-PSYCHOLOGY-HL|HL 5, 6, 7]:  ⟵ “Psychology HL | 5, 6, 7 | PSY-P | 103 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|HL 5, 6, 7]:  ⟵ “Social/Cultural Anthropology HL | 5, 6, 7 | ANTH-UN | 100 | 8”
  - equivalencies[IB-SPANISH-HL|HL 4, 5, 6, 7]:  ⟵ “Spanish B HL | 4, 5, 6, 7 | SPAN-S | 203, 204 | 3, 3”
  - equivalencies[IB-VISUAL-ARTS-HL|HL 5, 6, 7]:  ⟵ “Visual Arts HL | 5, 6, 7 | NMAT-F | 101, 102 | 3, 3”
### `60c6fd8f2549bf34` Indiana University-Kokomo — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.iuk.edu/admissions/transfer-credit/advanced-placement-articulations.html (sha256 b007ef8de0c1)
- checks: {"distinct_exams": 37, "equivalencies": 60, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | FINA-A | 101 | 3”
  - equivalencies[AP-ART-HISTORY|4, 5]:  ⟵ “Art History | 4, 5 | FINA-A | 101, 102 | 6”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “Studio Art: 2-D Design | 3, 4, 5 | FINA-F | 102 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, 5]:  ⟵ “Studio Art: 3-D Design | 3, 4, 5 | NMAT-F | 103 | 3”
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “Studio Art: Drawing | 3, 4, 5 | NMAT-F | 103 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL-UN | 100 | 3”
  - equivalencies[AP-BIOLOGY|4, 5]:  ⟵ “Biology | 4, 5 | BIOL-L | 121 | 5”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH-M | 119 | 3”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “Calculus AB | 4, 5 | MATH-M | 215 | 5”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MATH-M | 119 | 3”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC | 4, 5 | MATH-M | 215, 216 | 10”
  - equivalencies[AP-CHEMISTRY|3, 4]:  ⟵ “Chemistry | 3, 4 | CHEM-C | 101 | 3”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM-C | 105/125 | 5”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | 3 | LANG-UNDI | 200 | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4, 5]:  ⟵ “Chinese | 4, 5 | LANG-UNDI | 200 | 6”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CSCI-B | 100 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4, 5]:  ⟵ “Computer Science A | 4, 5 | CSCI-B & CSCI-C | 100, 101 | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CSCI-B | 100 | 4”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macroeconomics | 3 | ECON-E | 104 | 3”
  - equivalencies[AP-MACROECONOMICS|4, 5]:  ⟵ “Economics: Macroeconomics | 4, 5 | ECON-E | 202 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Microeconomics | 3 | ECON-E | 103 | 3”
  - equivalencies[AP-MICROECONOMICS|4, 5]:  ⟵ “Economics: Microeconomics | 4, 5 | ECON-E | 201 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | GEOG-UN | 100 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4, 5]:  ⟵ “Environmental Science | 4, 5 | GEOG-UN | 100 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | FREN-F | 203 | 3”
  - … 35 more rows
### `bd4458bf60b8261d` Indiana University-Kokomo — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.iuk.edu/admissions/transfer-credit/clepscores.html (sha256 983bd3748122)
- checks: {"distinct_exams": 30, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG-L209 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | ENG-L202 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENG-W131 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|59]:  ⟵ “College Composition | 59 | ENG-W131 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG-E301 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | HUMA-U102 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language Level 1 | 50 | FREN-F111 | 4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|64]:  ⟵ “French Language Level 1 | 64 | FREN-F111 | 4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|69]:  ⟵ “French Language Level 2 | 69 | FREN-F111 | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language Level 1 | 50 | GER-G111 | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|59]:  ⟵ “German Language Level 1 | 59 | GER-G111 | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|67]:  ⟵ “German Language Level 2 | 67 | GER-G111 | 4”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language Level 1 | 50 | SPAN-S111 | 4”
  - equivalencies[CLEP-SPANISH-LANGUAGE|56]:  ⟵ “Spanish Language Level 1 | 56 | SPAN-S111 | 4”
  - equivalencies[CLEP-SPANISH-LANGUAGE|68]:  ⟵ “Spanish Language Level 2 | 68 | SPAN-S111 | 4”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS-Y103 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | PSY-P216 | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro Educational Psych | 50 | EDUC-P251 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | BUS-E202 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | BUS-E201 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSY-P103 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOC-S100 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | HIST-UN100 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization 1 | 50 | HIST-H113 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization 2 | 50 | HIST-H114 | 3”
  - … 12 more rows
### `fdb390b065abda53` Indiana University-Kokomo — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.iuk.edu/admissions/apply-now/dual-credit/credits-to-college.html (sha256 7b54be3a9f60)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.3 ⟵ “High School students looking to enroll in dual credit courses must maintain a high school GPA of 2.3 or higher on a 4.0 scale and receive a counselor’s recommendation.”
### `mc3b33836f225c1e` Indiana University-Kokomo — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.iuk.edu/admissions/transfer-credit/index.html (sha256 8d1e42b2e3d9)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - min_grade: C ⟵ “You should also note: Only courses with a grade of "C" or better will be considered for transfer credit.”
  - max_transfer_credits: 64 ⟵ “Up to 64 credit hours from a community college or 90 credit hours from a four-year university can be transferred to IU Kokomo.”
### `523695d2b0c6aec7` Indiana University-South Bend — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://admissions.iusb.edu/apply/high-school.html (sha256 2eb7bb8baecd)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Official high school transcript showing at least a 3.0 GPA on a 4.0 scale”
### `f86f668b66fd1bc3` Indiana University-South Bend — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admissions.iusb.edu/apply/ib-equivalency-chart.html (sha256 615a9fd46116)
- checks: {"distinct_exams": 44, "equivalencies": 200, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-SL|SL 4]:  ⟵ “IU South Bend | Biology SL | 4 | N/A | 0 |  | ”
  - equivalencies[IB-BIOLOGY-SL|SL 5]:  ⟵ “IU South Bend | Biology SL | 5 | BIOL-L 104 | 3 |  | ”
  - equivalencies[IB-BIOLOGY-SL|SL 6]:  ⟵ “IU South Bend | Biology SL | 6 | BIOL-L 104 | 3 |  | ”
  - equivalencies[IB-BIOLOGY-SL|SL 7]:  ⟵ “IU South Bend | Biology SL | 7 | BIOL-L 104 | 3 |  | ”
  - equivalencies[IB-BIOLOGY-HL|HL 4]:  ⟵ “IU South Bend | Biology HL | 4 | BIOL-L 101 or 102 | 5 |  | ”
  - equivalencies[IB-BIOLOGY-HL|HL 5]:  ⟵ “IU South Bend | Biology HL | 5 | BIOL-L 101 or 102 | 5 |  | ”
  - equivalencies[IB-BIOLOGY-HL|HL 6]:  ⟵ “IU South Bend | Biology HL | 6 | BIOL-L 101 or 102 | 5 |  | ”
  - equivalencies[IB-BIOLOGY-HL|HL 7]:  ⟵ “IU South Bend | Biology HL | 7 | BIOL-L 101 or 102 | 5 |  | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|SL 4]:  ⟵ “IU South Bend | Business Management SL | 4 | BUS-UN 100 BUS UNDISTRIBUTED-100 LEVEL | 3 |  | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|SL 5]:  ⟵ “IU South Bend | Business Management SL | 5 | BUS-UN 100 BUS UNDISTRIBUTED-100 LEVEL | 3 |  | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|SL 6]:  ⟵ “IU South Bend | Business Management SL | 6 | BUS-UN 100 BUS UNDISTRIBUTED-100 LEVEL | 3 |  | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|SL 7]:  ⟵ “IU South Bend | Business Management SL | 7 | BUS-UN 100 BUS UNDISTRIBUTED-100 LEVEL | 3 |  | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 4]:  ⟵ “IU South Bend | Business Management HL | 4 | BUS-B 190 | 3 |  | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 5]:  ⟵ “IU South Bend | Business Management HL | 5 | BUS-B 190 | 3 |  | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 6]:  ⟵ “IU South Bend | Business Management HL | 6 | BUS-B 190 | 3 |  | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 7]:  ⟵ “IU South Bend | Business Management HL | 7 | BUS-B 190 | 3 |  | ”
  - equivalencies[IB-CHEMISTRY-SL|SL 4]:  ⟵ “IU South Bend | Chemistry SL | 4 | CHEM-UN 100 | 3 |  | ”
  - equivalencies[IB-CHEMISTRY-SL|SL 5]:  ⟵ “IU South Bend | Chemistry SL | 5 | CHEM-UN 100 | 3 |  | ”
  - equivalencies[IB-CHEMISTRY-SL|SL 6]:  ⟵ “IU South Bend | Chemistry SL | 6 | CHEM-C 101/121 | 3/2 |  | ”
  - equivalencies[IB-CHEMISTRY-SL|SL 7]:  ⟵ “IU South Bend | Chemistry SL | 7 | CHEM-C 101/122 | 3/3 |  | ”
  - equivalencies[IB-CHEMISTRY-HL|HL 4]:  ⟵ “IU South Bend | Chemistry HL | 4 | CHEM-C 105/125 | 3/2 |  | ”
  - equivalencies[IB-CHEMISTRY-HL|HL 5]:  ⟵ “IU South Bend | Chemistry HL | 5 | CHEM-C 105/125 | 3/3 |  | ”
  - equivalencies[IB-CHEMISTRY-HL|HL 6]:  ⟵ “IU South Bend | Chemistry HL | 6 | CHEM-C 105/106/125/126 | 3/3/2/2 |  | ”
  - equivalencies[IB-CHEMISTRY-HL|HL 7]:  ⟵ “IU South Bend | Chemistry HL | 7 | CHEM-C 105/106/125/126 | 3/3/2/3 |  | ”
  - equivalencies[IB-LATIN-SL|SL 4]:  ⟵ “IU South Bend | Classical Languages: Latin SL | 4 | CLAS-UN 100 | 3 |  | ”
  - … 175 more rows
### `m7d9af39f39a0acc` Indiana University-South Bend — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.iusb.edu/oiss/admissions/apply/transfer-ctr.html (sha256 409b250d1115)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - min_grade: C ⟵ “Generally, you must earn a grade of "C" or higher in order to transfer a course and you will need to submit an official transcript from each college or university at which you completed coursework.”
  - max_transfer_credits: 90 ⟵ “Up to 90 semester hours or 135 quarter hours of transferred credit can be applied from a four-year institution toward a Bachelor’s degree.”
### `6e81c36c8b37819f` Ivy Tech Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ivytech.edu/admissions/transfer-pathways/ (sha256 575815518560)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “You may also have your previous college mail your official transcripts to: Ivy Tech Community College Transcript Processing 9301 E. 59th Street Indianapolis, IN 46216 Only courses with grades of C- or higher are eligible for review for credit transfer.”
### `23581a0c320f40bf` Manchester University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.manchester.edu/admissions-aid/financial-aid/scholarships-grants/ (sha256 375ac2a716eb)
- checks: {"thresholds": null}
  - award_tiers: [{'gpa requirement': '3.75 – 3.99', 'amount_text': '$18,000'}, {'gpa requirement': '3.50 – 3.74', 'amount_text': '$16,000'}, {'gpa requirement': '3.25 – 3.49', 'amount_text': '$14,000'}, {'gpa requirement': '3.00 – 3.24', 'amount_text': '$12,000'}, {'gpa requirement': '2.75 – 2.99', 'amount_text': '$10,000'}, {'gpa requirement': '2.50 – 2.74', 'amount_text': '$8,000'}] ⟵ “GPA Requirement | Scholarship Award || 3.75 – 3.99 | $18,000 || 3.50 – 3.74 | $16,000 || 3.25 – 3.49 | $14,000 || 3.00 – 3.24 | $12,000 || 2.75 – 2.99 | $10,000 || 2.50 – 2.74 | $8,000”
  - gpa_requirement: Tiered by GPA Requirement: 3.75 – 3.99 → $18,000; 3.50 – 3.74 → $16,000; 3.25 – 3.49 → $14,000; 3.00 – 3.24 → $12,000; 2.75 – 2.99 → $10,000; 2.50 – 2.74 → $8,000 ⟵ “GPA Requirement | Scholarship Award || 3.75 – 3.99 | $18,000 || 3.50 – 3.74 | $16,000 || 3.25 – 3.49 | $14,000 || 3.00 – 3.24 | $12,000 || 2.75 – 2.99 | $10,000 || 2.50 – 2.74 | $8,000”
### `2efa52a7aafb0de2` Manchester University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.manchester.edu/admissions-aid/tuition-fees/ (sha256 21226a4d9de9)
- checks: {"columns": 2, "rows": 7}
  - off_campus_not_with_family:Tuition: 23924 ⟵ “Tuition | $23,924 | $23,924”
  - off_campus_not_with_family:Program Fee: 2474 ⟵ “Program Fee | $2,474 | $2,474”
  - off_campus_not_with_family:Housing/Food Allowance: 12780 ⟵ “Housing/Food Allowance | $12,780 | $6,390”
  - off_campus_not_with_family:Books/Supplies: 1000 ⟵ “Books/Supplies | $1,000 | $1,000”
  - off_campus_not_with_family:Transportation: 2200 ⟵ “Transportation | $2,200 | $3,600”
  - off_campus_not_with_family:Personal/Miscellaneous: 2340 ⟵ “Personal/Miscellaneous | $2,340 | $746”
  - off_campus_not_with_family:Loan Fees: 132 ⟵ “Loan Fees | $132 | $132”
  - with_parents_or_family:Tuition: 23924 ⟵ “Tuition | $23,924 | $23,924”
  - with_parents_or_family:Program Fee: 2474 ⟵ “Program Fee | $2,474 | $2,474”
  - with_parents_or_family:Housing/Food Allowance: 6390 ⟵ “Housing/Food Allowance | $12,780 | $6,390”
  - with_parents_or_family:Books/Supplies: 1000 ⟵ “Books/Supplies | $1,000 | $1,000”
  - with_parents_or_family:Transportation: 3600 ⟵ “Transportation | $2,200 | $3,600”
  - with_parents_or_family:Personal/Miscellaneous: 746 ⟵ “Personal/Miscellaneous | $2,340 | $746”
  - with_parents_or_family:Loan Fees: 132 ⟵ “Loan Fees | $132 | $132”
### `eeb28e04f063f707` Manchester University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.manchester.edu/admissions-aid/tuition-fees/ (sha256 21226a4d9de9)
- checks: {"columns": 1, "rows": 2}
  - on_campus:Tuition (Full-time, Fall/Spring + January Term): 36484 ⟵ “Tuition (Full-time, Fall/Spring + January Term) | $37,232 | $36,484”
  - on_campus:Non-Residential Programming Fee (Student-Assessed): 220 ⟵ “Non-Residential Programming Fee (Student-Assessed) | $220 | $220”
### `b6fcfe120684c3bb` Manchester University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.manchester.edu/admissions-aid/undergraduate-admissions/early-college-experience/ (sha256 2d0302ea4581)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “GPA of 2.5 or higher”
  - per_credit_hour_charge: 50 ⟵ “Online: $50 per credit hour”
  - per_credit_hour_charge: 85 ⟵ “On-Campus: $85 per credit hour”
### `57839347a99087dc` Mid-America College of Funeral Service — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://mid-america.edu/funeral-service-program-admissions/advanced-placement-exam/ (sha256 40e923d2d63d)
- checks: {"distinct_exams": 8, "equivalencies": 8, "rows_without_score": 0}
  - equivalencies[AP-PRECALCULUS|3+]:  ⟵ “Precalculus | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-CALCULUS-AB|3+]:  ⟵ “Calculus AB | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-CALCULUS-BC|3+]:  ⟵ “Calculus BC | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-STATISTICS|3+]:  ⟵ “Statistics | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Language & Composition | 3+ | ENG 100 – English Grammar and Composition | 4”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition | 3+ | ENG 100 – English Grammar and Composition | 4”
  - equivalencies[AP-RESEARCH|3+]:  ⟵ “Research | 3+ | ENG 100 – English Grammar and Composition | 4”
  - equivalencies[AP-SEMINAR|3+]:  ⟵ “Seminar | 3+ | ENG 100 – English Grammar and Composition | 4”
### `b7867100fe896cb4` Purdue University Fort Wayne — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.pfw.edu/admissions-financial-aid/financial-aid/tuition-and-fees (sha256 802caa0b9d02)
- checks: {"columns": 1, "rows": 8}
  - on_campus:Tuition & mandatory fees: 24280.8 ⟵ “Tuition & mandatory fees | $9,532.20** | $14,298.30** | $24,280.80** | $25,160.10**”
  - on_campus:food: 4402 ⟵ “food | $4,402*** | $4,402*** | $4,402*** | $4,402***”
  - on_campus:housing: 8705.62 ⟵ “housing | $8,705.62 | $8,705.62 | $8,705.62 | $8,705.62”
  - on_campus:Subtotal:: 37388.42 ⟵ “Subtotal: | $22,639.82 | $27,405.92 | $37,388.42 | $38,267.72”
  - on_campus:books/course materials/supplies/equipment: 3180 ⟵ “books/course materials/supplies/equipment | $3,180 | $3,180 | $3,180 | $3,180”
  - on_campus:transportation: 1586 ⟵ “transportation | $1,586 | $1,586 | $1,586 | $1,586”
  - on_campus:miscellaneous: 2430 ⟵ “miscellaneous | $2,430 | $2,430 | $2,430 | $2,430”
  - on_campus:subtotal:: 7196 ⟵ “subtotal: | $7,196 | $7,196 | $7,196 | $7,196”
### `0659ab03a8c566e4` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-communication [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
- checks: {"courses": 32, "groups": 6, "groups_skipped": 0}
  - program_name: Bachelor of Science in Communication ⟵ “Bachelor of Science in Communication | Purdue University Global Academic Catalog”
### `0bf53f8cb77fdb7c` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-organizational-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
- checks: {"courses": 79, "groups": 17, "groups_skipped": 0}
  - program_name: Bachelor of Science in Organizational Management ⟵ “Bachelor of Science in Organizational Management | Purdue University Global Academic Catalog”
### `1192716bfbcbe1d0` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-applied-computer-science [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-computer-science-bs/ (sha256 49600e5d901a)
- checks: {"courses": 25, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Applied Computer Science ⟵ “Bachelor of Science in Applied Computer Science | Purdue University Global Academic Catalog”
### `130c105111fa9122` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/environmental-policy-management-bs/ (sha256 10dc519623e0)
- checks: {"courses": 24, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Environmental Policy and Management ⟵ “Bachelor of Science in Environmental Policy and Management | Purdue University Global Academic Catalog”
### `23f0f1fb4980dfbe` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-care-administration [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-care-administration-bs/ (sha256 f6b640a6f508)
- checks: {"courses": 13, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health Care Administration ⟵ “Bachelor of Science in Health Care Administration | Purdue University Global Academic Catalog”
### `2627f9392ab4950a` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-education-and-promotion [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-education-promotion-bs/ (sha256 5e9167680106)
- checks: {"courses": 11, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health Education and Promotion ⟵ “Bachelor of Science in Health Education and Promotion | Purdue University Global Academic Catalog”
### `27ffa17700c696dc` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-science-in-nursing [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
- checks: {"courses": 37, "groups": 6, "groups_skipped": 0}
  - program_name: Associate of Science in Nursing ⟵ “Associate of Science in Nursing | Purdue University Global Academic Catalog”
### `3045ec0a456f04ab` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-information-technology [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-bs/ (sha256 6d6bdb1e9c45)
- checks: {"courses": 28, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Information Technology ⟵ “Bachelor of Science in Information Technology | Purdue University Global Academic Catalog”
### `30e68aac7bd18023` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-cybersecurity [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
- checks: {"courses": 49, "groups": 9, "groups_skipped": 0}
  - program_name: Bachelor of Science in Cybersecurity ⟵ “Bachelor of Science in Cybersecurity | Purdue University Global Academic Catalog”
### `426e3fbee165f899` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-analytics [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
- checks: {"courses": 73, "groups": 13, "groups_skipped": 0}
  - program_name: Bachelor of Science in Analytics ⟵ “Bachelor of Science in Analytics | Purdue University Global Academic Catalog”
### `458e8b58110accbf` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-criminal-justice [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
- checks: {"courses": 40, "groups": 9, "groups_skipped": 0}
  - program_name: Bachelor of Science in Criminal Justice ⟵ “Bachelor of Science in Criminal Justice | Purdue University Global Academic Catalog”
### `4a68d42b9f81662b` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-information-technology [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-aas/ (sha256 071358cda74e)
- checks: {"courses": 16, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Information Technology ⟵ “Associate of Applied Science in Information Technology | Purdue University Global Academic Catalog”
### `4bcea1d01d116251` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-professional-studies [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
- checks: {"courses": 16, "groups": 6, "groups_skipped": 0}
  - program_name: Bachelor of Science in Professional Studies ⟵ “Bachelor of Science in Professional Studies | Purdue University Global Academic Catalog”
### `4cda5620ae51f3d5` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-applied-manufacturing [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-manufacturing-bs/ (sha256 ed13b75cad34)
- checks: {"courses": 22, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Applied Manufacturing ⟵ “Bachelor of Science in Applied Manufacturing | Purdue University Global Academic Catalog”
### `578a8bd161e32871` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-science-in-health-science [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
- checks: {"courses": 21, "groups": 4, "groups_skipped": 0}
  - program_name: Associate of Science in Health Science ⟵ “Associate of Science in Health Science | Purdue University Global Academic Catalog”
### `5972910569ee43dc` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-early-childhood-development [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-development-aas/ (sha256 fdad375265a0)
- checks: {"courses": 12, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Early Childhood Development ⟵ “Associate of Applied Science in Early Childhood Development | Purdue University Global Academic Catalog”
### `6239c0a615959440` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-small-group-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/small-group-management-aas/ (sha256 0411c2728524)
- checks: {"courses": 6, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Small Group Management ⟵ “Associate of Applied Science in Small Group Management | Purdue University Global Academic Catalog”
### `73cf339f1f9695a8` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-cloud-computing-and-solutions [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cloud-computing-solutions-bs/ (sha256 77b0e54d770a)
- checks: {"courses": 24, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Cloud Computing and Solutions ⟵ “Bachelor of Science in Cloud Computing and Solutions | Purdue University Global Academic Catalog”
### `7a0556089107853e` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-criminal-justice [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-aas/ (sha256 f7068e07e87b)
- checks: {"courses": 7, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Criminal Justice ⟵ “Associate of Applied Science in Criminal Justice | Purdue University Global Academic Catalog”
### `7c99bc4818416129` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-health-science [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
- checks: {"courses": 20, "groups": 4, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Health Science ⟵ “Associate of Applied Science in Health Science | Purdue University Global Academic Catalog”
### `7eb8d2781e2c170a` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-nutrition [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/nutrition-bs/ (sha256 dd1592b09484)
- checks: {"courses": 25, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Nutrition ⟵ “Bachelor of Science in Nutrition | Purdue University Global Academic Catalog”
### `801121f894cde9a3` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-aviation-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/aviation-management-bs/ (sha256 1ca153298e79)
- checks: {"courses": 21, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Aviation Management ⟵ “Bachelor of Science in Aviation Management | Purdue University Global Academic Catalog”
### `83f8e619155dc137` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-information-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-information-management-bs/ (sha256 0d8e9e812759)
- checks: {"courses": 25, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health Information Management ⟵ “Bachelor of Science in Health Information Management | Purdue University Global Academic Catalog”
### `8516c774344fa43e` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
- checks: {"courses": 37, "groups": 8, "groups_skipped": 0}
  - program_name: Bachelor of Science in Accounting and Analytics ⟵ “Bachelor of Science in Accounting and Analytics | Purdue University Global Academic Catalog”
### `8a0c3795163b6db4` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-emergency-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/emergency-management-bs/ (sha256 54adfba134ed)
- checks: {"courses": 25, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Emergency Management ⟵ “Bachelor of Science in Emergency Management | Purdue University Global Academic Catalog”
### `8ba26435b5a5050a` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-science-in-professional-studies [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-as/ (sha256 8d08aa71b244)
- checks: {"courses": 4, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Science in Professional Studies ⟵ “Associate of Science in Professional Studies | Purdue University Global Academic Catalog”
### `9823fbde79025f7b` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-finance [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
- checks: {"courses": 36, "groups": 7, "groups_skipped": 0}
  - program_name: Bachelor of Science in Finance ⟵ “Bachelor of Science in Finance | Purdue University Global Academic Catalog”
### `9defd0d0f8f3674d` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/fire-emergency-management-bs/ (sha256 afedb45fd8c0)
- checks: {"courses": 25, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Fire and Emergency Management ⟵ “Bachelor of Science in Fire and Emergency Management | Purdue University Global Academic Catalog”
### `a5b3f510cca961ce` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-nursing-rn-to-bsn [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-rn-bsn-bs/ (sha256 4d33147a4129)
- checks: {"courses": 13, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Nursing—RN-to-BSN ⟵ “Bachelor of Science in Nursing—RN-to-BSN | Purdue University Global Academic Catalog”
### `b583c9bd93ac7ac7` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-business-administration [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
- checks: {"courses": 90, "groups": 20, "groups_skipped": 0}
  - program_name: Bachelor of Science in Business Administration ⟵ “Bachelor of Science in Business Administration | Purdue University Global Academic Catalog”
### `b6dce59e373c857b` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-human-resource-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/human-resource-management-bs/ (sha256 8c3efdbb3966)
- checks: {"courses": 21, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Human Resource Management ⟵ “Bachelor of Science in Human Resource Management | Purdue University Global Academic Catalog”
### `be51101b5524f629` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-accounting [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-aas/ (sha256 eb162f849b86)
- checks: {"courses": 14, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Accounting ⟵ “Associate of Applied Science in Accounting | Purdue University Global Academic Catalog”
### `c64bf5937caa299d` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-and-wellness [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-wellness-bs/ (sha256 ae3f65d930b4)
- checks: {"courses": 23, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health and Wellness ⟵ “Bachelor of Science in Health and Wellness | Purdue University Global Academic Catalog”
### `cad10d024ce69993` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-science [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
- checks: {"courses": 31, "groups": 5, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health Science ⟵ “Bachelor of Science in Health Science | Purdue University Global Academic Catalog”
### `cb2f44db909c0320` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-business-administration [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
- checks: {"courses": 56, "groups": 14, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Business Administration ⟵ “Associate of Applied Science in Business Administration | Purdue University Global Academic Catalog”
### `db13fb919ec6c394` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-applied-supply-chain-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-supply-chain-management-bs/ (sha256 803bc6bd7b23)
- checks: {"courses": 25, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Applied Supply Chain Management ⟵ “Bachelor of Science in Applied Supply Chain Management | Purdue University Global Academic Catalog”
### `de886984b644cdef` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-professional-flight [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/professional-flight-bs/ (sha256 a564dfddbaa1)
- checks: {"courses": 19, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Professional Flight ⟵ “Bachelor of Science in Professional Flight | Purdue University Global Academic Catalog”
### `ecfdb9d7eec67d0b` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-early-childhood-administration [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-administration-bs/ (sha256 39b3c395f5ac)
- checks: {"courses": 22, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Early Childhood Administration ⟵ “Bachelor of Science in Early Childhood Administration | Purdue University Global Academic Catalog”
### `fc3e94df81293b29` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-marketing [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/marketing-bs/ (sha256 f769649697ce)
- checks: {"courses": 21, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Marketing ⟵ “Bachelor of Science in Marketing | Purdue University Global Academic Catalog”
### `fc485f604a21c85a` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-sustainability [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
- checks: {"courses": 52, "groups": 10, "groups_skipped": 0}
  - program_name: Bachelor of Science in Sustainability ⟵ “Bachelor of Science in Sustainability | Purdue University Global Academic Catalog”
### `007d5be160b437b0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=supply-chain-logistics [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
### `022ac661fd233929` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=wealth-management-and-financial-planning [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 421 ⟵ “MT 421 - Financial Planning”
  - courses: MT 422 ⟵ “MT 422 - Portfolio Management”
  - courses: MT 423 ⟵ “MT 423 - Asset Allocation and Risk Management”
  - courses: MT 483 ⟵ “MT 483 - Investments”
### `02996a71117e21f7` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 114 ⟵ “AC 114 - 🌐 Accounting I”
  - courses: AC 116 ⟵ “AC 116 - 🌐 Accounting II”
  - courses: AC 239 ⟵ “AC 239 - Managerial Accounting”
  - courses: AC 256 ⟵ “AC 256 - Federal Tax”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 217 ⟵ “MT 217 - 🌐 Finance”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: AC 300 ⟵ “AC 300 - Intermediate Accounting I”
  - courses: AC 301 ⟵ “AC 301 - Intermediate Accounting II”
  - courses: AC 302 ⟵ “AC 302 - Intermediate Accounting III”
  - courses: AC 312 ⟵ “AC 312 - Fundamentals of Accounting Analytics”
  - courses: AC 410 ⟵ “AC 410 - Auditing”
  - courses: AC 450 ⟵ “AC 450 - Advanced Accounting”
  - courses: LS 311 ⟵ “LS 311 - 🌐 Business Law”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: AC 499 ⟵ “AC 499 - Bachelor's Capstone in Accounting”
### `036e207d88b6d440` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `0397b6a1af538b2f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `03f9319c031c97c7` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-health-science · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
  - courses: HS 290 ⟵ “HS 290 - Associate's Capstone in Health Science”
### `0490547f1e7d9895` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-information-management · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-information-management-bs/ (sha256 0d8e9e812759)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SC 116 ⟵ “SC 116 - Survey of Human Structure and Function”
### `05fbb4aeb0f3059e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=game-development [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IN 240 ⟵ “IN 240 - 🌐 Game Design and Mechanics”
  - courses: IN 241 ⟵ “IN 241 - 🌐 Game Programming”
  - courses: IN 242 ⟵ “IN 242 - 🌐 Game Art and Animation”
  - courses: IN 251 ⟵ “IN 251 - 🌐 Software Development Concepts Using C#”
  - courses: IN 255 ⟵ “IN 255 - 🌐 Software Design and Development Concepts Using C#”
### `069c1384bf21d288` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=supply-chain-management-and-logistics [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `06de1e807e49a3a5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `084799a7bb7a12a5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=forensic-psychology [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 325 ⟵ “CJ 325 - 🌐 Psychology for Law Enforcement”
  - courses: CJ 440 ⟵ “CJ 440 - Crisis Intervention”
  - courses: PS 440 ⟵ “PS 440 - Psychopathology”
### `0947d60a8c187660` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=network-administration [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 203 ⟵ “IN 203 - 🌐 Networking With Microsoft Technologies”
  - courses: IN 205 ⟵ “IN 205 - 🌐 Routing and Switching I”
  - courses: IN 206 ⟵ “IN 206 - 🌐 Routing and Switching II”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 278 ⟵ “IT 278 - 🌐 Windows Administration”
  - courses: IT 375 ⟵ “IT 375 - 🌐 Windows Enterprise Administration”
### `0bd7620f10383636` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aviation-management · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/aviation-management-bs/ (sha256 1ca153298e79)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `138486b5915d2d4e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-flight · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/professional-flight-bs/ (sha256 a564dfddbaa1)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `14091068d6bd5838` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=decision-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: IN 302 ⟵ “IN 302 - 🌐 Reporting and Visualization”
  - courses: MM 305 ⟵ “MM 305 - 🌐 Business Statistics and Quantitative Analysis”
  - courses: MM 330 ⟵ “MM 330 - Probability With Business Applications”
  - courses: MM 340 ⟵ “MM 340 - Decision Modeling”
  - courses: MM 341 ⟵ “MM 341 - Decision Management”
### `155c189e501c238c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=supply-chain-management-and-logistics [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `1686ea20297b5a3f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-computer-science · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-computer-science-bs/ (sha256 49600e5d901a)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 165 ⟵ “MM 165 - Advanced Algebra and Geometry”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
### `176a875a2612a5aa` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-emergency-management · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/emergency-management-bs/ (sha256 54adfba134ed)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SS 236 ⟵ “SS 236 - 🌐 American Government”
### `193c6546493160bf` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=artificial-intelligence-ai [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IN 200 ⟵ “IN 200 - 🌐 Data Governance - Policy and Ethics”
  - courses: IN 245 ⟵ “IN 245 - Introduction to Artificial Intelligence and Its Impact”
  - courses: IN 246 ⟵ “IN 246 - The Human Side of Artificial Intelligence: Understanding Interaction and Design”
  - courses: IN 305 ⟵ “IN 305 - Artificial Intelligence, Society, and the Future of Work”
  - courses: IT 421 ⟵ “IT 421 - AI-Powered Cybersecurity: Tools and Techniques”
### `1a7f1cec591b66c8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-education-and-promotion · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-education-promotion-bs/ (sha256 5e9167680106)
  - courses: HS 305 ⟵ “HS 305 - Research Methods for Health Sciences”
  - courses: HW 315 ⟵ “HW 315 - Models for Health and Wellness”
  - courses: HW 320 ⟵ “HW 320 - Contemporary Diet and Nutrition”
  - courses: HD 420 ⟵ “HD 420 - Social Determinants of Health and Health Behavior”
  - courses: HD 440 ⟵ “HD 440 - Health Education Program Assessment and Planning”
  - courses: HD 460 ⟵ “HD 460 - Health Education Program Implementation and Evaluation”
  - courses: HD 480 ⟵ “HD 480 - Health Communication, Social Marketing, and Advocacy”
  - courses: HD 499 ⟵ “HD 499 - Bachelor's Capstone in Health Education and Promotion”
### `1a9767941281d4f0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=global-marketing-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 450 ⟵ “MT 450 - 🌐 Brand Management Strategy”
  - courses: MT 455 ⟵ “MT 455 - Strategic Management of Sales”
### `1b0ded1da9f9bfb0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: PR 150 ⟵ “PR 150 - You and Professional Studies - Creating Pathways to Success”
  - courses: PR 499 ⟵ “PR 499 - Bachelor's Capstone in Professional Studies”
### `1bdf2fe2e770647c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=managerial-accountancy [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 314 ⟵ “AC 314 - Accounting Information Systems and Enterprise Risk Management”
  - courses: AC 420 ⟵ “AC 420 - Cost Accounting”
  - courses: MT 482 ⟵ “MT 482 - 🌐 Financial Statement Analysis”
### `1fe3b4d71db66d4c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=game-development [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 240 ⟵ “IN 240 - 🌐 Game Design and Mechanics”
  - courses: IN 241 ⟵ “IN 241 - 🌐 Game Programming”
  - courses: IN 242 ⟵ “IN 242 - 🌐 Game Art and Animation”
  - courses: IN 251 ⟵ “IN 251 - 🌐 Software Development Concepts Using C#”
  - courses: IN 255 ⟵ “IN 255 - 🌐 Software Design and Development Concepts Using C#”
### `20780da0a5cae66d` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-criminal-justice · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-aas/ (sha256 f7068e07e87b)
  - courses: CJ 100 ⟵ “CJ 100 - 🌐 Preparing for a Career in Public Safety”
  - courses: CJ 101 ⟵ “CJ 101 - 🌐 Introduction to the Criminal Justice System”
  - courses: CJ 210 ⟵ “CJ 210 - 🌐 Criminal Investigation”
  - courses: CJ 227 ⟵ “CJ 227 - 🌐 Criminal Procedure”
  - courses: CJ 299 ⟵ “CJ 299 - Associate's Capstone in Criminal Justice”
### `221674d307e75859` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=small-group-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 260 ⟵ “MT 260 - Group and Organization Dynamics”
  - courses: MT 262 ⟵ “MT 262 - Leading Global Teams”
### `235fadc9b3a8cee0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=real-estate [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 361 ⟵ “MT 361 - Foundations of Real Estate Practice”
  - courses: MT 431 ⟵ “MT 431 - Real Estate Finance and Ethics”
  - courses: MT 432 ⟵ “MT 432 - Real Estate Law”
  - courses: MT 453 ⟵ “MT 453 - Professional Selling”
### `249fe50466908cde` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `25432585f21cb396` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-early-childhood-development · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-development-aas/ (sha256 fdad375265a0)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `2552a225812a70cc` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-marketing · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/marketing-bs/ (sha256 f769649697ce)
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `264142165319ccc5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-flight · requirement_key=program-requirements-instrument-rating [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/professional-flight-bs/ (sha256 a564dfddbaa1)
  - courses: AV 498 ⟵ “AV 498 - Aviation Technology Capstone”
### `26945449356fec03` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `297c645c1774fc75` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: AC 114 ⟵ “AC 114 - 🌐 Accounting I”
  - courses: AC 116 ⟵ “AC 116 - 🌐 Accounting II”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: CS 113 ⟵ “CS 113 - Academic Strategies for the Business Professional”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
  - courses: MT 106 ⟵ “MT 106 - Foundations for Success in Business and Management Careers”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 217 ⟵ “MT 217 - 🌐 Finance”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: MT 299 ⟵ “MT 299 - Associate's Capstone in Management”
### `2cd0643a25f31dcd` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=cloud-computing [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IT 222 ⟵ “IT 222 - 🌐 Introduction to Cloud Computing”
  - courses: IT 227 ⟵ “IT 227 - 🌐 Cloud Infrastructure Administration”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 303 ⟵ “IT 303 - 🌐 Cloud Architecture Concepts and Design”
  - courses: IT 304 ⟵ “IT 304 - 🌐 Application Development and Scripting in the Cloud”
  - courses: IT 403 ⟵ “IT 403 - 🌐 Cloud Security”
### `2d258ebd411e7b8d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=homeland-security [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 307 ⟵ “CJ 307 - Crisis Management in Terrorist Attacks and Disasters”
  - courses: CJ 355 ⟵ “CJ 355 - 🌐 Homeland Security”
  - courses: CJ 407 ⟵ “CJ 407 - Crisis Negotiation”
  - courses: CJ 440 ⟵ “CJ 440 - Crisis Intervention”
### `2ed20331514e439d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=global-business [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: CM 305 ⟵ “CM 305 - Communicating in a Diverse Society”
  - courses: MT 220 ⟵ “MT 220 - 🌐 Global Business”
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
### `310a7742061adc7f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-care-administration · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-care-administration-bs/ (sha256 f6b640a6f508)
  - courses: HA 255 ⟵ “HA 255 - 🌐 Human Resources for Health Care Organizations”
  - courses: HS 230 ⟵ “HS 230 - 🌐 Health Care Administration”
  - courses: HA 400 ⟵ “HA 400 - 🌐 Health Care Ethics, Law, and Governance”
  - courses: HA 410 ⟵ “HA 410 - 🌐 Health Care Leadership”
  - courses: HA 415 ⟵ “HA 415 - 🌐 Health Care Policy and Economics”
  - courses: HA 425 ⟵ “HA 425 - 🌐 Operational Analysis and Quality Improvement”
  - courses: HI 300 ⟵ “HI 300 - 🌐 Information Systems for Health Care”
  - courses: HS 440 ⟵ “HS 440 - 🌐 Finance for Health Care”
  - courses: HS 450 ⟵ “HS 450 - 🌐 Strategic Planning and Change Management for Health Care”
  - courses: HA 499 ⟵ “HA 499 - 🌐 Bachelor's Capstone in Health Care Administration”
### `313aca60c48ab712` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=business-intelligence [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 314 ⟵ “AC 314 - Accounting Information Systems and Enterprise Risk Management”
  - courses: AC 442 ⟵ “AC 442 - Data Management and Analysis”
  - courses: AC 444 ⟵ “AC 444 - Accounting Visualization and Business Intelligence”
### `31d63a77724f037b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nursing-rn-to-bsn · requirement_key=program-requirements-prior-learning-licensure-credits [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-rn-bsn-bs/ (sha256 4d33147a4129)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `33202c7290dbb25f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 180 ⟵ “SC 180 - General Chemistry I”
  - courses: SC 235 ⟵ “SC 235 - 🌐 Human Biology”
### `33560c8b53d8c122` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-early-childhood-administration · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-administration-bs/ (sha256 39b3c395f5ac)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: PS 124 ⟵ “PS 124 - 🌐 Introduction to Psychology”
  - courses: PS 220 ⟵ “PS 220 - Child and Adolescent Psychology”
### `3401c28801f42962` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-early-childhood-administration · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-administration-bs/ (sha256 39b3c395f5ac)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `3500ee04a01ab4c1` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-information-technology · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-aas/ (sha256 071358cda74e)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `359d66bae53466c8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=supply-chain-management-and-logistics [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `3690982f38177117` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `38fd27d28414b18b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IT 104 ⟵ “IT 104 - 🌐 Introduction to Cybersecurity”
  - courses: IN 203 ⟵ “IN 203 - 🌐 Networking With Microsoft Technologies”
  - courses: IN 205 ⟵ “IN 205 - 🌐 Routing and Switching I”
  - courses: IN 206 ⟵ “IN 206 - 🌐 Routing and Switching II”
  - courses: IT 244 ⟵ “IT 244 - 🌐 Python Programming”
  - courses: IT 262 ⟵ “IT 262 - 🌐 Certified Ethical Hacking I”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 275 ⟵ “IT 275 - 🌐 Linux System Administration”
  - courses: IT 286 ⟵ “IT 286 - 🌐 Network Security Concepts”
  - courses: IT 374 ⟵ “IT 374 - 🌐 Linux Security”
  - courses: IT 390 ⟵ “IT 390 - 🌐 Intrusion Detection and Incident Response”
  - courses: IT 395 ⟵ “IT 395 - 🌐 Certified Ethical Hacking II”
  - courses: IT 400 ⟵ “IT 400 - 🌐 Ethics in Cybersecurity”
  - courses: IT 411 ⟵ “IT 411 - 🌐 Digital Forensics”
  - courses: IT 484 ⟵ “IT 484 - 🌐 Cybersecurity Policies”
  - courses: IT 497 ⟵ “IT 497 - Bachelor's Capstone in Cybersecurity”
### `397d7b1ff9c855e5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: SS 290 ⟵ “SS 290 - 🌐 Data in Our World - Introduction to Data Literacy”
### `3b5e8e349454e46a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=juvenile-justice [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 150 ⟵ “CJ 150 - 🌐 Juvenile Delinquency”
  - courses: CJ 333 ⟵ “CJ 333 - 🌐 Family and Domestic Violence”
  - courses: CJ 420 ⟵ “CJ 420 - 🌐 Juvenile Justice”
  - courses: CJ 445 ⟵ “CJ 445 - Juvenile Justice Case Management”
  - courses: PS 440 ⟵ “PS 440 - Psychopathology”
### `3bb25d30f7302b93` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `3ce961ca60ae3591` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-supply-chain-management · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-supply-chain-management-bs/ (sha256 803bc6bd7b23)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `3db2fa5753bb5cac` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=business-development [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 359 ⟵ “MT 359 - Integrated Marketing Communications”
  - courses: MT 453 ⟵ “MT 453 - Professional Selling”
  - courses: MT 459 ⟵ “MT 459 - Consumer Behavior”
### `3e09767dcb13c9c0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-and-wellness · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-wellness-bs/ (sha256 ae3f65d930b4)
  - courses: EF 205 ⟵ “EF 205 - Principles of Exercise Science”
  - courses: HW 106 ⟵ “HW 106 - Health and Wellness Profession and Career Planning”
  - courses: NS 105 ⟵ “NS 105 - Fundamentals of Nutrition”
  - courses: HW 300 ⟵ “HW 300 - Disease Prevention and Lifestyle Medicine”
  - courses: HW 310 ⟵ “HW 310 - Complementary and Integrative Medicine”
  - courses: HW 315 ⟵ “HW 315 - Models for Health and Wellness”
  - courses: HW 350 ⟵ “HW 350 - Principles of Health Coaching”
  - courses: HW 410 ⟵ “HW 410 - The Science of Stress and Resilience”
  - courses: HW 420 ⟵ “HW 420 - Psychological and Spiritual Aspects of Wellness”
  - courses: HW 425 ⟵ “HW 425 - Health and Wellness Programming - Design and Administration”
  - courses: HW 450 ⟵ “HW 450 - Applied Health Coaching”
  - courses: HW 499 ⟵ “HW 499 - Bachelor's Capstone in Health and Wellness”
### `3ee0d8a93c811a40` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-professional-studies · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-as/ (sha256 8d08aa71b244)
  - courses: PR 150 ⟵ “PR 150 - You and Professional Studies - Creating Pathways to Success”
  - courses: PR 299 ⟵ “PR 299 - Associate's Capstone in Professional Studies”
### `3fc103d906f277de` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=fintech [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: FI 310 ⟵ “FI 310 - FinTech Principles and Concepts”
  - courses: FI 311 ⟵ “FI 311 - FinTech Law and Ethics”
  - courses: FI 410 ⟵ “FI 410 - Blockchain for the Financial Industry”
### `40592cf61adeac17` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-early-childhood-development · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-development-aas/ (sha256 fdad375265a0)
  - courses: CE 100 ⟵ “CE 100 - Preparing for a Career in Early Childhood”
  - courses: CE 101 ⟵ “CE 101 - Introduction to Early Childhood Education”
  - courses: CE 114 ⟵ “CE 114 - Early Childhood Development”
  - courses: CE 215 ⟵ “CE 215 - Early Childhood Curriculum Planning”
  - courses: CE 220 ⟵ “CE 220 - Child Safety, Nutrition, and Health”
  - courses: CE 230 ⟵ “CE 230 - Creative Activities for Young Children”
  - courses: CE 240 ⟵ “CE 240 - Young Children With Special Needs”
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: PS 124 ⟵ “PS 124 - 🌐 Introduction to Psychology”
  - courses: CE 299 ⟵ “CE 299 - Associate's Capstone for Early Childhood Development”
### `42c1071e7646251d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-information-technology · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-bs/ (sha256 6d6bdb1e9c45)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
### `4335fcae3027f638` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `46c8430682707dcf` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=data-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IT 163 ⟵ “IT 163 - 🌐 Database Concepts Using Microsoft Access”
  - courses: IT 234 ⟵ “IT 234 - 🌐 Database Concepts”
  - courses: IN 303 ⟵ “IN 303 - 🌐 Data Mining and Data Warehousing”
  - courses: IT 350 ⟵ “IT 350 - 🌐 Advanced Database Concepts”
### `495c96db5cb551e9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=software-development-using-python [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IN 250 ⟵ “IN 250 - 🌐 Software Development Concepts Using Python”
  - courses: IN 254 ⟵ “IN 254 - 🌐 Software Design and Development Concepts Using Python”
  - courses: IN 300 ⟵ “IN 300 - 🌐 Programming for Data Analysis (Python, R, and Java)”
  - courses: IN 304 ⟵ “IN 304 - 🌐 Advanced Programming for Data Analysis”
  - courses: IN 400 ⟵ “IN 400 - 🌐 Artificial Intelligence (AI) - Deep Learning and Machine Learning”
### `4bf371e5503a9d55` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cloud-computing-and-solutions · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cloud-computing-solutions-bs/ (sha256 77b0e54d770a)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
### `4d98184be6b6f86a` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-accounting · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-aas/ (sha256 eb162f849b86)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `4e1ee406b08cf17c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-emergency-management · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/emergency-management-bs/ (sha256 54adfba134ed)
  - courses: EG 100 ⟵ “EG 100 - Foundations of the Emergency Management Profession”
  - courses: FS 120 ⟵ “FS 120 - Introduction to Emergency Management”
  - courses: FS 202 ⟵ “FS 202 - Principles of Emergency Services”
  - courses: FS 220 ⟵ “FS 220 - Preparedness and Planning for Emergency Management”
  - courses: FS 225 ⟵ “FS 225 - Emergency Management Response”
  - courses: PP 220 ⟵ “PP 220 - Socially Responsible Leadership”
  - courses: EG 401 ⟵ “EG 401 - Strategies for Intergovernmental Effectiveness in Emergency Management”
  - courses: EG 402 ⟵ “EG 402 - Emergency Management Exercise Design and Evaluation”
  - courses: EG 403 ⟵ “EG 403 - Socio-Psychological Dimensions of an Emergency Event”
  - courses: EG 404 ⟵ “EG 404 - Grants Management in Emergency Management”
  - courses: FS 320 ⟵ “FS 320 - Recovery Practices in Emergency Management”
  - courses: FS 413 ⟵ “FS 413 - Research Analysis for Fire Emergency Services”
  - courses: FS 420 ⟵ “FS 420 - Mitigation and Risk Assessment in Emergency Management”
  - courses: FS 425 ⟵ “FS 425 - Disaster Policy in Emergency Management”
  - courses: PP 310 ⟵ “PP 310 - Finance and Budgeting in the Public Sector”
  - courses: EG 498 ⟵ “EG 498 - Bachelor's Capstone in Emergency Management”
### `4f14f3642b7c18a8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=aviation-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: AV 102 ⟵ “AV 102 - Aviation History”
  - courses: AV 203 ⟵ “AV 203 - Aviation Operations Management”
  - courses: AV 412 ⟵ “AV 412 - Aviation Finance”
  - courses: AV 438 ⟵ “AV 438 - Airline Operations”
  - courses: AV 475 ⟵ “AV 475 - Aviation Law”
### `4fe8d086dec529ec` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cloud-computing-and-solutions · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cloud-computing-solutions-bs/ (sha256 77b0e54d770a)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `5068581703414e65` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=general-finance [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: MT 361 ⟵ “MT 361 - Foundations of Real Estate Practice”
  - courses: MT 421 ⟵ “MT 421 - Financial Planning”
  - courses: MT 422 ⟵ “MT 422 - Portfolio Management”
  - courses: MT 423 ⟵ “MT 423 - Asset Allocation and Risk Management”
  - courses: MT 431 ⟵ “MT 431 - Real Estate Finance and Ethics”
  - courses: MT 432 ⟵ “MT 432 - Real Estate Law”
  - courses: MT 445 ⟵ “MT 445 - 🌐 Managerial Economics”
  - courses: MT 453 ⟵ “MT 453 - Professional Selling”
### `514e4f1f037ebd66` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=customer-service [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: CM 214 ⟵ “CM 214 - Public Speaking for the Professional”
  - courses: MT 202 ⟵ “MT 202 - Building Customer Sales and Loyalty”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
### `5282e3dbc49154f8` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-health-science · requirement_key=preprofessional [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: PS 124 ⟵ “PS 124 - 🌐 Introduction to Psychology”
  - courses: SC 115 ⟵ “SC 115 - Principles of Nutrition”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 180 ⟵ “SC 180 - General Chemistry I”
  - courses: SC 190 ⟵ “SC 190 - General Chemistry II”
  - courses: SS 144 ⟵ “SS 144 - Sociology”
  - courses: HS 305 ⟵ “HS 305 - Research Methods for Health Sciences”
  - courses: HS 315 ⟵ “HS 315 - 🌐 Practices in Public Health”
  - courses: HS 340 ⟵ “HS 340 - Epidemiology”
  - courses: HW 310 ⟵ “HW 310 - Complementary and Integrative Medicine”
  - courses: SC 320 ⟵ “SC 320 - Microbiology for Health Professions”
  - courses: SC 335 ⟵ “SC 335 - Survey of Biochemistry”
  - courses: SC 415 ⟵ “SC 415 - Environmental Health”
  - courses: SC 435 ⟵ “SC 435 - 🌐 Genetics”
### `5291ba1af7f68232` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=financial-analysis [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: BU 204 ⟵ “BU 204 - 🌐 Macroeconomics”
  - courses: MT 445 ⟵ “MT 445 - 🌐 Managerial Economics”
  - courses: MT 480 ⟵ “MT 480 - 🌐 Corporate Finance”
  - courses: MT 481 ⟵ “MT 481 - Financial Markets”
  - courses: MT 482 ⟵ “MT 482 - 🌐 Financial Statement Analysis”
### `546cc8892cb7533b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-supply-chain-management · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-supply-chain-management-bs/ (sha256 803bc6bd7b23)
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
  - courses: SS 255 ⟵ “SS 255 - Digital Citizenship”
### `55cc153ad5fc2953` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: HU 245 ⟵ “HU 245 - 🌐 Ethics”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 246 ⟵ “SC 246 - 🌐 Fundamentals of Microbiology”
### `57bf713edf5871e5` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-health-science · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `57f9460f739c13ac` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - courses: CM 111 ⟵ “CM 111 - Communication Program and Profession”
  - courses: CM 115 ⟵ “CM 115 - Communication - Concepts and Skills”
  - courses: CM 202 ⟵ “CM 202 - Mass Media and Society”
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: CM 208 ⟵ “CM 208 - Communication Research Skills”
  - courses: CM 214 ⟵ “CM 214 - Public Speaking for the Professional”
  - courses: CM 305 ⟵ “CM 305 - Communicating in a Diverse Society”
  - courses: CM 310 ⟵ “CM 310 - Communication and Conflict”
  - courses: CM 313 ⟵ “CM 313 - Digital Tools and Society”
  - courses: CM 315 ⟵ “CM 315 - Group Dynamics and Team Building”
  - courses: CM 405 ⟵ “CM 405 - Communicating Persuasively”
  - courses: CM 410 ⟵ “CM 410 - Organizational Communication”
  - courses: CM 460 ⟵ “CM 460 - Strategic Communication”
  - courses: CM 499 ⟵ “CM 499 - Bachelor's Capstone in Communication”
### `58cd0f7c29a064b0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=applied-artificial-intelligence-ai-systems-development [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IT 321 ⟵ “IT 321 - Artificial Intelligence Fundamentals and Python for Data”
  - courses: IT 341 ⟵ “IT 341 - Core Machine Learning Algorithms”
  - courses: IT 440 ⟵ “IT 440 - Neural Networks and Deep Learning Foundations”
  - courses: IT 451 ⟵ “IT 451 - Specialized Deep Learning and Applied Artificial Intelligence Systems”
### `58d4097eb28b1503` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `59516fafd4c4a51a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=wealth-management-and-financial-planning [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: MT 421 ⟵ “MT 421 - Financial Planning”
  - courses: MT 422 ⟵ “MT 422 - Portfolio Management”
  - courses: MT 423 ⟵ “MT 423 - Asset Allocation and Risk Management”
### `5bcc2d4d20cae3f8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=business-development [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 359 ⟵ “MT 359 - Integrated Marketing Communications”
  - courses: MT 453 ⟵ “MT 453 - Professional Selling”
  - courses: MT 459 ⟵ “MT 459 - Consumer Behavior”
### `5cce8f46cdc7331e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-education-and-promotion · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-education-promotion-bs/ (sha256 5e9167680106)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `5d5b4e5e6803a7d2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=law-enforcement [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 333 ⟵ “CJ 333 - 🌐 Family and Domestic Violence”
  - courses: CJ 355 ⟵ “CJ 355 - 🌐 Homeland Security”
  - courses: CJ 370 ⟵ “CJ 370 - 🌐 Crime Scene Investigation II”
  - courses: CJ 411 ⟵ “CJ 411 - Drugs and Alcohol in the Criminal Justice System”
### `5e46cdde37a7c4d3` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=crime-scene-investigation [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 328 ⟵ “CJ 328 - 🌐 Forensic Fingerprint Analysis”
  - courses: CJ 345 ⟵ “CJ 345 - 🌐 Supervisory Practices in Criminal Justice”
  - courses: CJ 370 ⟵ “CJ 370 - 🌐 Crime Scene Investigation II”
  - courses: CJ 385 ⟵ “CJ 385 - 🌐 Forensic Chemistry and Trace Evidence Analysis”
### `61510d93f562258c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management · requirement_key=business-foundations [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/fire-emergency-management-bs/ (sha256 afedb45fd8c0)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `6196e142322448eb` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=progression-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 246 ⟵ “SC 246 - 🌐 Fundamentals of Microbiology”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
### `6247b62201c4abe8` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=lvn-lpn-to-asn-pathway [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: NU 104 ⟵ “NU 104 - Pathophysiology for Nursing”
  - courses: NU 140 ⟵ “NU 140 - Nursing Fundamentals”
  - courses: NU 141 ⟵ “NU 141 - Pharmacology for Nursing”
### `64362c92734f1346` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/environmental-policy-management-bs/ (sha256 10dc519623e0)
  - courses: LS 100 ⟵ “LS 100 - Introduction to the Law and Legal Profession”
  - courses: EM 101 ⟵ “EM 101 - Introduction to Environmental Policy and Management”
  - courses: EM 205 ⟵ “EM 205 - The Politics of Managing the Environment”
  - courses: PP 110 ⟵ “PP 110 - Ethics and Public Administration”
  - courses: PP 220 ⟵ “PP 220 - Socially Responsible Leadership”
  - courses: EM 305 ⟵ “EM 305 - The Economics of Environmental Management”
  - courses: EM 410 ⟵ “EM 410 - The Global Environment”
  - courses: EM 430 ⟵ “EM 430 - Environmental Policy Analysis”
  - courses: LS 302 ⟵ “LS 302 - Environmental Law and Policy”
  - courses: LS 305 ⟵ “LS 305 - Constitutional Law”
  - courses: PA 301 ⟵ “PA 301 - Administrative Law”
  - courses: PP 310 ⟵ “PP 310 - Finance and Budgeting in the Public Sector”
  - courses: PP 420 ⟵ “PP 420 - Private and Public Sector Partnerships”
  - courses: PP 450 ⟵ “PP 450 - Program Evaluation”
  - courses: EM 499 ⟵ “EM 499 - Bachelor's Capstone in Environmental Policy and Management”
### `64a8bfd3abccd412` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nutrition · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/nutrition-bs/ (sha256 dd1592b09484)
  - courses: NS 105 ⟵ “NS 105 - Fundamentals of Nutrition”
  - courses: NS 106 ⟵ “NS 106 - Nutrition Profession and Career Planning”
  - courses: NS 230 ⟵ “NS 230 - Macronutrient Metabolism”
  - courses: NS 235 ⟵ “NS 235 - Micronutrient Metabolism”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 190 ⟵ “SC 190 - General Chemistry II”
  - courses: NS 305 ⟵ “NS 305 - Food Safety”
  - courses: NS 310 ⟵ “NS 310 - Nutritional Assessment”
  - courses: NS 325 ⟵ “NS 325 - Nutrition Through the Life Cycle”
  - courses: NS 410 ⟵ “NS 410 - Integrative Nutrition Planning and Management”
  - courses: NS 420 ⟵ “NS 420 - Nutritional Counseling”
  - courses: NS 480 ⟵ “NS 480 - Medical Nutrition Therapy I”
  - courses: NS 490 ⟵ “NS 490 - Medical Nutrition Therapy II”
  - courses: SC 320 ⟵ “SC 320 - Microbiology for Health Professions”
  - courses: SC 335 ⟵ “SC 335 - Survey of Biochemistry”
  - courses: NS 499 ⟵ “NS 499 - Bachelor's Capstone in Nutrition”
### `64f7c5473868efe6` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=business-foundations [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `650179de55cf7e63` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-manufacturing · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-manufacturing-bs/ (sha256 ed13b75cad34)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `65b07f474f6d4ede` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-professional-studies · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-as/ (sha256 8d08aa71b244)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `6607ff47169a9bb0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-information-management · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-information-management-bs/ (sha256 0d8e9e812759)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `668598a3b325092c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-manufacturing · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-manufacturing-bs/ (sha256 ed13b75cad34)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
  - courses: MM 260 ⟵ “MM 260 - Linear Algebra”
### `680f8a42082225ed` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `6862bf254dc337ef` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=entrepreneurship [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: MT 202 ⟵ “MT 202 - Building Customer Sales and Loyalty”
  - courses: MT 207 ⟵ “MT 207 - Starting a Business”
  - courses: MT 209 ⟵ “MT 209 - Small Business Management”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
### `6a018e3d5b820fb5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=sport-entertainment-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 240 ⟵ “MT 240 - Sport in Society”
  - courses: MT 241 ⟵ “MT 241 - Sport Analytics”
  - courses: MT 242 ⟵ “MT 242 - Managing Sport Programs”
  - courses: MT 243 ⟵ “MT 243 - Sport Sponsorships and Sales”
### `6b24ef0eaad69cb9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-information-technology · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-bs/ (sha256 6d6bdb1e9c45)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `6ca0ac099c24f2cc` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=digital-and-social-media-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 355 ⟵ “MT 355 - 🌐 Marketing Research and Analytics”
  - courses: MT 357 ⟵ “MT 357 - Digital Marketing Platforms and Strategy”
  - courses: MT 358 ⟵ “MT 358 - Social Media Marketing and AI Optimization”
  - courses: MT 359 ⟵ “MT 359 - Integrated Marketing Communications”
### `6e6135a0984b87be` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-marketing · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/marketing-bs/ (sha256 f769649697ce)
  - courses: AC 114 ⟵ “AC 114 - 🌐 Accounting I”
  - courses: AC 116 ⟵ “AC 116 - 🌐 Accounting II”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 217 ⟵ “MT 217 - 🌐 Finance”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: CM 410 ⟵ “CM 410 - Organizational Communication”
  - courses: LS 311 ⟵ “LS 311 - 🌐 Business Law”
  - courses: MT 355 ⟵ “MT 355 - 🌐 Marketing Research and Analytics”
  - courses: MT 357 ⟵ “MT 357 - Digital Marketing Platforms and Strategy”
  - courses: MT 358 ⟵ “MT 358 - Social Media Marketing and AI Optimization”
  - courses: MT 359 ⟵ “MT 359 - Integrated Marketing Communications”
  - courses: MT 362 ⟵ “MT 362 - Artificial Intelligence Applications for the Marketing Professional”
  - courses: MT 450 ⟵ “MT 450 - 🌐 Brand Management Strategy”
  - courses: MT 453 ⟵ “MT 453 - Professional Selling”
  - courses: MT 459 ⟵ “MT 459 - Consumer Behavior”
  - courses: MT 494 ⟵ “MT 494 - Bachelor's Capstone in Marketing”
### `74ccba38edaac350` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-computer-science · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-computer-science-bs/ (sha256 49600e5d901a)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `750597cd6195e4ed` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-care-administration · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-care-administration-bs/ (sha256 f6b640a6f508)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `7566482971b6057f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nursing-rn-to-bsn · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-rn-bsn-bs/ (sha256 4d33147a4129)
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: SC 246 ⟵ “SC 246 - 🌐 Fundamentals of Microbiology”
### `769311c359537d9a` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-criminal-justice · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-aas/ (sha256 f7068e07e87b)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `786566da1722799d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=global-marketing-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 450 ⟵ “MT 450 - 🌐 Brand Management Strategy”
  - courses: MT 455 ⟵ “MT 455 - Strategic Management of Sales”
### `7a8a65c71c38e66f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=business-foundations [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `7ab77b9edfdf400b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `7f4e9534bb42bcff` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=software-development-using-python [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 250 ⟵ “IN 250 - 🌐 Software Development Concepts Using Python”
  - courses: IN 254 ⟵ “IN 254 - 🌐 Software Design and Development Concepts Using Python”
  - courses: IN 304 ⟵ “IN 304 - 🌐 Advanced Programming for Data Analysis”
### `7f69616ca0deba79` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aviation-management · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/aviation-management-bs/ (sha256 1ca153298e79)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `8153f225e00a2996` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=procurement [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 300 ⟵ “MT 300 - 🌐 Management of Information Systems”
  - courses: MT 435 ⟵ “MT 435 - 🌐 Operations Management”
  - courses: MT 475 ⟵ “MT 475 - Quality Management”
  - courses: MT 482 ⟵ “MT 482 - 🌐 Financial Statement Analysis”
### `815e47df3770f37a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
  - courses: HS 106 ⟵ “HS 106 - Health Science Profession and Career Planning”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 190 ⟵ “SC 190 - General Chemistry II”
  - courses: SC 225 ⟵ “SC 225 - Environmental Science”
  - courses: SC 226 ⟵ “SC 226 - Environmental Science Lab”
  - courses: SC 236 ⟵ “SC 236 - Human Biology Lab”
  - courses: HD 420 ⟵ “HD 420 - Social Determinants of Health and Health Behavior”
  - courses: HS 345 ⟵ “HS 345 - Biostatistics”
  - courses: HW 300 ⟵ “HW 300 - Disease Prevention and Lifestyle Medicine”
  - courses: PU 335 ⟵ “PU 335 - Global Health”
  - courses: SC 320 ⟵ “SC 320 - Microbiology for Health Professions”
  - courses: SC 335 ⟵ “SC 335 - Survey of Biochemistry”
  - courses: HS 499 ⟵ “HS 499 - Bachelor's Capstone in Health Science”
### `81857f96cb23ff5e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `84d3ac90faa4484d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=leadership [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: CM 460 ⟵ “CM 460 - Strategic Communication”
  - courses: LI 410 ⟵ “LI 410 - Leadership in Practice”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 340 ⟵ “MT 340 - 🌐 Conflict Management and Team Dynamics”
### `86a58f0afd97abef` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-early-childhood-administration · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-administration-bs/ (sha256 39b3c395f5ac)
  - courses: AC 114 ⟵ “AC 114 - 🌐 Accounting I”
  - courses: CE 100 ⟵ “CE 100 - Preparing for a Career in Early Childhood”
  - courses: CE 101 ⟵ “CE 101 - Introduction to Early Childhood Education”
  - courses: CE 114 ⟵ “CE 114 - Early Childhood Development”
  - courses: CE 215 ⟵ “CE 215 - Early Childhood Curriculum Planning”
  - courses: CE 220 ⟵ “CE 220 - Child Safety, Nutrition, and Health”
  - courses: CE 240 ⟵ “CE 240 - Young Children With Special Needs”
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: CE 300 ⟵ “CE 300 - Observation and Assessment in Early Childhood”
  - courses: CE 370 ⟵ “CE 370 - Funding Development and Financial Planning in Early Childhood Programs”
  - courses: CE 371 ⟵ “CE 371 - Early Childhood Administration”
  - courses: CE 401 ⟵ “CE 401 - Current Issues and Trends in Early Childhood”
  - courses: CE 402 ⟵ “CE 402 - Early Childhood Family, Community, and Advocacy”
  - courses: CM 410 ⟵ “CM 410 - Organizational Communication”
  - courses: LI 410 ⟵ “LI 410 - Leadership in Practice”
  - courses: CE 490 ⟵ “CE 490 - Bachelor's Capstone in Early Childhood Administration”
### `8876d5e1eb7fe6a3` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-health-science · requirement_key=preprofessional [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: PS 124 ⟵ “PS 124 - 🌐 Introduction to Psychology”
  - courses: SC 115 ⟵ “SC 115 - Principles of Nutrition”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 180 ⟵ “SC 180 - General Chemistry I”
  - courses: SC 190 ⟵ “SC 190 - General Chemistry II”
  - courses: SS 144 ⟵ “SS 144 - Sociology”
  - courses: HS 305 ⟵ “HS 305 - Research Methods for Health Sciences”
  - courses: HS 315 ⟵ “HS 315 - 🌐 Practices in Public Health”
  - courses: HS 340 ⟵ “HS 340 - Epidemiology”
  - courses: HW 310 ⟵ “HW 310 - Complementary and Integrative Medicine”
  - courses: SC 320 ⟵ “SC 320 - Microbiology for Health Professions”
  - courses: SC 335 ⟵ “SC 335 - Survey of Biochemistry”
  - courses: SC 415 ⟵ “SC 415 - Environmental Health”
  - courses: SC 435 ⟵ “SC 435 - 🌐 Genetics”
### `8c51bbb1b30edfe1` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-human-resource-management · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/human-resource-management-bs/ (sha256 8c3efdbb3966)
  - courses: AC 114 ⟵ “AC 114 - 🌐 Accounting I”
  - courses: AC 116 ⟵ “AC 116 - 🌐 Accounting II”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 217 ⟵ “MT 217 - 🌐 Finance”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: HR 400 ⟵ “HR 400 - 🌐 Talent Acquisition and Management”
  - courses: HR 410 ⟵ “HR 410 - Talent Development and Learning”
  - courses: HR 420 ⟵ “HR 420 - Workplace Law, Labor Relations, and HR Risk Management”
  - courses: HR 435 ⟵ “HR 435 - Total Rewards and Compensation Strategy”
  - courses: HR 485 ⟵ “HR 485 - 🌐 Strategic HRM: Analytics and Business Decision-Making”
  - courses: LS 311 ⟵ “LS 311 - 🌐 Business Law”
  - courses: MM 305 ⟵ “MM 305 - 🌐 Business Statistics and Quantitative Analysis”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 340 ⟵ “MT 340 - 🌐 Conflict Management and Team Dynamics”
  - courses: HR 499 ⟵ “HR 499 - Bachelor's Capstone in Human Resource Management”
### `8c678fec3416d1a9` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-small-group-management · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/small-group-management-aas/ (sha256 0411c2728524)
  - courses: CS 126 ⟵ “CS 126 - Academic Strategies for the Military Professional”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 297 ⟵ “MT 297 - Associate's Capstone in Small Group Management”
### `8d1efc5847a57989` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=financial-analysis [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 445 ⟵ “MT 445 - 🌐 Managerial Economics”
  - courses: MT 480 ⟵ “MT 480 - 🌐 Corporate Finance”
  - courses: MT 481 ⟵ “MT 481 - Financial Markets”
  - courses: MT 482 ⟵ “MT 482 - 🌐 Financial Statement Analysis”
### `912b948d96766525` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=hospitality-and-tourism-services [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: TH 116 ⟵ “TH 116 - Introduction to Hospitality, Event Management, and Tourism”
  - courses: TH 206 ⟵ “TH 206 - Hotel Management and Operations”
  - courses: TH 213 ⟵ “TH 213 - Food and Beverage Management”
  - courses: TH 230 ⟵ “TH 230 - Foundations of Conference and Event Planning”
### `920aa2fbd19db91d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=project-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 401 ⟵ “IT 401 - Project Management II”
  - courses: MT 400 ⟵ “MT 400 - 🌐 Business Process Management”
  - courses: MT 475 ⟵ “MT 475 - Quality Management”
### `93f060b80550cefd` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=office-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: IT 133 ⟵ “IT 133 - 🌐 Microsoft Office Applications on Demand”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
  - courses: TH 230 ⟵ “TH 230 - Foundations of Conference and Event Planning”
### `955b256faee64bf7` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-health-science · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
  - courses: HS 290 ⟵ “HS 290 - Associate's Capstone in Health Science”
### `970d15090a3cb83a` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=sport-entertainment-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: MT 240 ⟵ “MT 240 - Sport in Society”
  - courses: MT 241 ⟵ “MT 241 - Sport Analytics”
  - courses: MT 242 ⟵ “MT 242 - Managing Sport Programs”
  - courses: MT 243 ⟵ “MT 243 - Sport Sponsorships and Sales”
### `9957754f4effbd33` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nutrition · requirement_key=holistic-nutrition [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/nutrition-bs/ (sha256 dd1592b09484)
  - courses: HW 310 ⟵ “HW 310 - Complementary and Integrative Medicine”
  - courses: NS 455 ⟵ “NS 455 - Current Trends in Nutrition”
  - courses: NS 460 ⟵ “NS 460 - Dietary Supplements and Nutraceuticals”
  - courses: NS 465 ⟵ “NS 465 - Functional Nutrition”
### `997c41c7a447e62c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=information-systems-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 332 ⟵ “IT 332 - 🌐 Principles of Information Systems Architecture”
  - courses: IT 402 ⟵ “IT 402 - 🌐 IT Consulting Skills”
  - courses: MT 451 ⟵ “MT 451 - Managing Technological Innovation”
### `9a4bed5732dfd276` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=decision-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: IN 302 ⟵ “IN 302 - 🌐 Reporting and Visualization”
  - courses: MM 305 ⟵ “MM 305 - 🌐 Business Statistics and Quantitative Analysis”
  - courses: MM 330 ⟵ “MM 330 - Probability With Business Applications”
  - courses: MM 340 ⟵ “MM 340 - Decision Modeling”
  - courses: MM 341 ⟵ “MM 341 - Decision Management”
  - courses: MT 313 ⟵ “MT 313 - Corporate Sustainability and Social Responsibility”
### `9ab4cfafba91195d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `9b04e88b27ae33fc` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=real-estate [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: MT 361 ⟵ “MT 361 - Foundations of Real Estate Practice”
  - courses: MT 431 ⟵ “MT 431 - Real Estate Finance and Ethics”
  - courses: MT 432 ⟵ “MT 432 - Real Estate Law”
### `9c511f1fc9baf5b0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-supply-chain-management · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-supply-chain-management-bs/ (sha256 803bc6bd7b23)
  - courses: AC 114 ⟵ “AC 114 - 🌐 Accounting I”
  - courses: IT 153 ⟵ “IT 153 - 🌐 Spreadsheet Applications”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 217 ⟵ “MT 217 - 🌐 Finance”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: MT 236 ⟵ “MT 236 - Introduction to Supply Chain Management”
  - courses: MT 237 ⟵ “MT 237 - Supply Chain Systems”
  - courses: MT 296 ⟵ “MT 296 - Supply Chain Management Applications”
  - courses: LS 311 ⟵ “LS 311 - 🌐 Business Law”
  - courses: MM 305 ⟵ “MM 305 - 🌐 Business Statistics and Quantitative Analysis”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 435 ⟵ “MT 435 - 🌐 Operations Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
  - courses: MT 460 ⟵ “MT 460 - 🌐 Management Strategy and Policy”
  - courses: MT 498 ⟵ “MT 498 - Bachelor's Capstone in Supply Chain Management”
### `9e05a7bb2b3d3b09` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=industrial-organizational-psychology [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: PS 390 ⟵ “PS 390 - Introduction to Industrial/Organizational Psychology”
  - courses: PS 391 ⟵ “PS 391 - Psychology of Leadership”
  - courses: PS 392 ⟵ “PS 392 - Attitudes and Motivation in the Workplace”
  - courses: PS 451 ⟵ “PS 451 - Selection and Assessment in Organizations”
### `9fa4f0e2929e8fe1` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=public-relations [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - courses: CM 350 ⟵ “CM 350 - Public Relations Strategies”
  - courses: CM 355 ⟵ “CM 355 - Public Relations Case Studies”
  - courses: CM 455 ⟵ “CM 455 - Digital Public Relations and Communication”
  - courses: CM 465 ⟵ “CM 465 - Communication Law and Ethics”
### `a05da22fcc264b66` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: AC 114 ⟵ “AC 114 - 🌐 Accounting I”
  - courses: AC 116 ⟵ “AC 116 - 🌐 Accounting II”
  - courses: BU 204 ⟵ “BU 204 - 🌐 Macroeconomics”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 217 ⟵ “MT 217 - 🌐 Finance”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: LS 311 ⟵ “LS 311 - 🌐 Business Law”
  - courses: MM 305 ⟵ “MM 305 - 🌐 Business Statistics and Quantitative Analysis”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 480 ⟵ “MT 480 - 🌐 Corporate Finance”
  - courses: MT 481 ⟵ “MT 481 - Financial Markets”
  - courses: MT 482 ⟵ “MT 482 - 🌐 Financial Statement Analysis”
  - courses: MT 483 ⟵ “MT 483 - Investments”
  - courses: FI 499 ⟵ “FI 499 - Bachelor's Capstone in Finance”
### `a10cd915a4a97bd9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nutrition · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/nutrition-bs/ (sha256 dd1592b09484)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 180 ⟵ “SC 180 - General Chemistry I”
### `a291414fa28245a7` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a2bf473521816f84` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=military-physician-assistant-preparation-mpap [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 180 ⟵ “SC 180 - General Chemistry I”
  - courses: SC 190 ⟵ “SC 190 - General Chemistry II”
  - courses: SC 335 ⟵ “SC 335 - Survey of Biochemistry”
### `a405970033b62a81` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-information-management · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-information-management-bs/ (sha256 0d8e9e812759)
  - courses: HA 255 ⟵ “HA 255 - 🌐 Human Resources for Health Care Organizations”
  - courses: HI 135 ⟵ “HI 135 - Legal Aspects of Health Information”
  - courses: HI 150 ⟵ “HI 150 - Automation of Health Information”
  - courses: HI 215 ⟵ “HI 215 - Reimbursement Methodologies”
  - courses: HI 230 ⟵ “HI 230 - 🌐 Quality Assurance and Statistics in Health Information”
  - courses: HI 253 ⟵ “HI 253 - Medical Coding I”
  - courses: HI 255 ⟵ “HI 255 - Medical Coding II”
  - courses: HS 111 ⟵ “HS 111 - 🌐 Medical Terminology”
  - courses: HS 140 ⟵ “HS 140 - Pharmacology”
  - courses: HS 200 ⟵ “HS 200 - Diseases of the Human Body”
  - courses: HS 230 ⟵ “HS 230 - 🌐 Health Care Administration”
  - courses: HA 425 ⟵ “HA 425 - 🌐 Operational Analysis and Quality Improvement”
  - courses: HI 300 ⟵ “HI 300 - 🌐 Information Systems for Health Care”
  - courses: HI 305 ⟵ “HI 305 - Management of Health Information”
  - courses: HI 410 ⟵ “HI 410 - Advanced Reimbursement Methodology”
  - courses: HS 305 ⟵ “HS 305 - Research Methods for Health Sciences”
  - courses: HS 345 ⟵ “HS 345 - Biostatistics”
  - courses: HS 420 ⟵ “HS 420 - Health Informatics”
  - courses: HS 450 ⟵ “HS 450 - 🌐 Strategic Planning and Change Management for Health Care”
  - courses: HS 460 ⟵ “HS 460 - 🌐 Project Design and Management for Health Care”
  - courses: HI 499 ⟵ “HI 499 - Bachelor's Capstone in Health Information Management”
### `a42e45c945d11730` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nutrition · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/nutrition-bs/ (sha256 dd1592b09484)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a4e0172d957dddfe` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a5e5f8b79a1500c9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=cissp-certification-preparation [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IT 277 ⟵ “IT 277 - 🌐 Certified Information Systems Security Professional I”
  - courses: IT 279 ⟵ “IT 279 - 🌐 Certified Information Systems Security Professional II”
  - courses: IT 410 ⟵ “IT 410 - 🌐 Certified Information Systems Security Professional III”
### `a74c4be524a26f60` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-emergency-management · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/emergency-management-bs/ (sha256 54adfba134ed)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a86bee267855127b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-education-and-promotion · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-education-promotion-bs/ (sha256 5e9167680106)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a8ad7a8aa499f3f1` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ab56f51a88d41050` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-emergency-management · requirement_key=business-foundations [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/emergency-management-bs/ (sha256 54adfba134ed)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `abadf5347acdc4e2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=economics [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: MT 313 ⟵ “MT 313 - Corporate Sustainability and Social Responsibility”
  - courses: MT 314 ⟵ “MT 314 - Social Innovation and Entrepreneurship”
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: SS 359 ⟵ “SS 359 - Sustainable and Resilient Communities”
### `aea46225296b26db` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=software-development-using-java [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IT 117 ⟵ “IT 117 - 🌐 Website Development”
  - courses: IN 252 ⟵ “IN 252 - 🌐 Software Development Concepts Using Java”
  - courses: IN 256 ⟵ “IN 256 - 🌐 Software Design and Development Concepts Using Java”
  - courses: IN 352 ⟵ “IN 352 - 🌐 Advanced Software Development Including Web and Mobility Using Java”
  - courses: IN 452 ⟵ “IN 452 - 🌐 Advanced Software Development Using Java”
  - courses: IT 488 ⟵ “IT 488 - 🌐 Software Product Development Using Agile”
### `af949c8645d20ee2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=construction-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 281 ⟵ “MT 281 - Fundamentals of Construction Management”
  - courses: MT 282 ⟵ “MT 282 - Construction Methods and Materials”
  - courses: MT 381 ⟵ “MT 381 - Construction Planning and Scheduling”
  - courses: MT 382 ⟵ “MT 382 - Construction Cost Estimating”
  - courses: MT 383 ⟵ “MT 383 - Construction Law”
### `b2713b28b85584c0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-flight · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/professional-flight-bs/ (sha256 a564dfddbaa1)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `b346240f3c71b8c4` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `b3ffe887fcfcc70b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=supply-chain-and-logistics [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `b41bf4dc53bb2c05` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
### `b656b27b6bd3a5b7` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=construction-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 281 ⟵ “MT 281 - Fundamentals of Construction Management”
  - courses: MT 282 ⟵ “MT 282 - Construction Methods and Materials”
  - courses: MT 381 ⟵ “MT 381 - Construction Planning and Scheduling”
  - courses: MT 382 ⟵ “MT 382 - Construction Cost Estimating”
  - courses: MT 383 ⟵ “MT 383 - Construction Law”
### `b7806094e49d208c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=software-development-using-c [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IT 117 ⟵ “IT 117 - 🌐 Website Development”
  - courses: IN 251 ⟵ “IN 251 - 🌐 Software Development Concepts Using C#”
  - courses: IN 255 ⟵ “IN 255 - 🌐 Software Design and Development Concepts Using C#”
  - courses: IN 351 ⟵ “IN 351 - 🌐 Advanced Software Development Including Web and Mobility Using C#”
  - courses: IN 451 ⟵ “IN 451 - 🌐 Advanced Software Development Using C#”
  - courses: IT 488 ⟵ “IT 488 - 🌐 Software Product Development Using Agile”
### `b9fc89219767f8d1` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-accounting · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-aas/ (sha256 eb162f849b86)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ba2f2e7521b9b055` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-and-wellness · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-wellness-bs/ (sha256 ae3f65d930b4)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ba84e1057889532d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=forensic-accountancy [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 465 ⟵ “AC 465 - Fraud and Forensic Accounting”
  - courses: AC 466 ⟵ “AC 466 - Fraud Detection and Financial Statement Analysis”
  - courses: AC 468 ⟵ “AC 468 - Digital Forensics and Investigative Techniques”
### `c0e69e84cd0f5b09` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-and-wellness · requirement_key=exercise-science [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-wellness-bs/ (sha256 ae3f65d930b4)
  - courses: EF 300 ⟵ “EF 300 - Principles of Kinesiology”
  - courses: EF 305 ⟵ “EF 305 - Exercise Physiology”
  - courses: EF 310 ⟵ “EF 310 - Applied Exercise Science for Healthy Aging and Special Conditions”
  - courses: EF 400 ⟵ “EF 400 - Psychosocial Aspects of Exercise”
  - courses: NS 425 ⟵ “NS 425 - Sports Nutrition”
### `c2244807f897c2a7` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=environmental-science [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: SC 325 ⟵ “SC 325 - Environmental Risk Assessment”
  - courses: SC 340 ⟵ “SC 340 - The Biology of Pollution”
  - courses: SC 350 ⟵ “SC 350 - Conservation of Natural Resources”
  - courses: SC 362 ⟵ “SC 362 - Our Changing Climate”
  - courses: SC 415 ⟵ “SC 415 - Environmental Health”
### `c22a4d3668768ac6` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=information-processing [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 115 ⟵ “CM 115 - Communication - Concepts and Skills”
  - courses: IT 133 ⟵ “IT 133 - 🌐 Microsoft Office Applications on Demand”
  - courses: IT 153 ⟵ “IT 153 - 🌐 Spreadsheet Applications”
  - courses: IT 163 ⟵ “IT 163 - 🌐 Database Concepts Using Microsoft Access”
### `c29921c2c1852356` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-health-science · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `c5873e69d19033a8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-and-wellness · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-wellness-bs/ (sha256 ae3f65d930b4)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 235 ⟵ “SC 235 - 🌐 Human Biology”
### `c62e974af2a4d442` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-human-resource-management · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/human-resource-management-bs/ (sha256 8c3efdbb3966)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ca335173370414e8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=project-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 401 ⟵ “IT 401 - Project Management II”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 400 ⟵ “MT 400 - 🌐 Business Process Management”
  - courses: MT 475 ⟵ “MT 475 - Quality Management”
### `caacbb12d496450b` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-health-science · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `cc525465f9a419ed` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=social-issues [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: CM 305 ⟵ “CM 305 - Communicating in a Diverse Society”
  - courses: HU 375 ⟵ “HU 375 - Social Justice and Sustainability”
  - courses: SC 361 ⟵ “SC 361 - Population and Society”
  - courses: SS 359 ⟵ “SS 359 - Sustainable and Resilient Communities”
  - courses: SC 415 ⟵ “SC 415 - Environmental Health”
### `cce91badae07cc71` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-information-technology · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-aas/ (sha256 071358cda74e)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
### `d1dbf0a192da22a2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=sport-entertainment-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 240 ⟵ “MT 240 - Sport in Society”
  - courses: MT 241 ⟵ “MT 241 - Sport Analytics”
  - courses: MT 242 ⟵ “MT 242 - Managing Sport Programs”
  - courses: MT 243 ⟵ “MT 243 - Sport Sponsorships and Sales”
### `d45cd7a4a24c0339` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=artificial-intelligence-ai [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 245 ⟵ “IN 245 - Introduction to Artificial Intelligence and Its Impact”
  - courses: IN 246 ⟵ “IN 246 - The Human Side of Artificial Intelligence: Understanding Interaction and Design”
  - courses: IN 304 ⟵ “IN 304 - 🌐 Advanced Programming for Data Analysis”
  - courses: IN 305 ⟵ “IN 305 - Artificial Intelligence, Society, and the Future of Work”
### `d6733ddd7a5115a2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/fire-emergency-management-bs/ (sha256 afedb45fd8c0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `d75a16702c74f34d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SC 156 ⟵ “SC 156 - Principles of Chemistry”
  - courses: SS 270 ⟵ “SS 270 - Social Problems”
### `d89fbbb5924734e2` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=retail-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: MT 102 ⟵ “MT 102 - Principles of Retailing”
  - courses: MT 202 ⟵ “MT 202 - Building Customer Sales and Loyalty”
  - courses: MT 209 ⟵ “MT 209 - Small Business Management”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
### `d98482956e12c9d6` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IT 153 ⟵ “IT 153 - 🌐 Spreadsheet Applications”
  - courses: IT 163 ⟵ “IT 163 - 🌐 Database Concepts Using Microsoft Access”
  - courses: IN 200 ⟵ “IN 200 - 🌐 Data Governance - Policy and Ethics”
  - courses: IT 234 ⟵ “IT 234 - 🌐 Database Concepts”
  - courses: IT 286 ⟵ “IT 286 - 🌐 Network Security Concepts”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
  - courses: IN 300 ⟵ “IN 300 - 🌐 Programming for Data Analysis (Python, R, and Java)”
  - courses: IN 301 ⟵ “IN 301 - 🌐 Securing Data”
  - courses: IN 302 ⟵ “IN 302 - 🌐 Reporting and Visualization”
  - courses: IT 350 ⟵ “IT 350 - 🌐 Advanced Database Concepts”
  - courses: IN 400 ⟵ “IN 400 - 🌐 Artificial Intelligence (AI) - Deep Learning and Machine Learning”
  - courses: IN 401 ⟵ “IN 401 - 🌐 Data Curation Concepts”
  - courses: IN 402 ⟵ “IN 402 - 🌐 Modeling and Predictive Analysis”
  - courses: MM 325 ⟵ “MM 325 - 🌐 Statistical Data Analysis”
  - courses: IN 498 ⟵ “IN 498 - Bachelor's Capstone in Analytics”
### `d9be703f6d48a9a2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `d9f1995012b4740a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=public-accountancy [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 314 ⟵ “AC 314 - Accounting Information Systems and Enterprise Risk Management”
  - courses: AC 430 ⟵ “AC 430 - Advanced Tax - Corporate”
  - courses: AC 444 ⟵ “AC 444 - Accounting Visualization and Business Intelligence”
### `dae8ba2bb98c0b1d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-marketing · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/marketing-bs/ (sha256 f769649697ce)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `dc563d760c7fdbba` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-early-childhood-development · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-development-aas/ (sha256 fdad375265a0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `dd3176ec070e018b` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: NU 104 ⟵ “NU 104 - Pathophysiology for Nursing”
  - courses: NU 140 ⟵ “NU 140 - Nursing Fundamentals”
  - courses: NU 141 ⟵ “NU 141 - Pharmacology for Nursing”
  - courses: NU 142 ⟵ “NU 142 - Medical-Surgical Nursing I”
  - courses: NU 143 ⟵ “NU 143 - Maternal Infant Nursing”
  - courses: NU 144 ⟵ “NU 144 - Medical-Surgical Nursing II”
  - courses: NU 145 ⟵ “NU 145 - Psychology Across the Lifespan”
  - courses: NU 225 ⟵ “NU 225 - Pediatric Nursing”
  - courses: NU 245 ⟵ “NU 245 - Mental Health Nursing”
  - courses: NU 263 ⟵ “NU 263 - Medical-Surgical Nursing III”
  - courses: NU 300 ⟵ “NU 300 - Professional Leadership Transitions”
  - courses: NU 298 ⟵ “NU 298 - Capstone”
### `dd61ec18c6de63ff` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=information-security-and-assurance [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 203 ⟵ “IN 203 - 🌐 Networking With Microsoft Technologies”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 278 ⟵ “IT 278 - 🌐 Windows Administration”
  - courses: IT 316 ⟵ “IT 316 - 🌐 Computer Forensics”
  - courses: IT 390 ⟵ “IT 390 - 🌐 Intrusion Detection and Incident Response”
  - courses: IT 411 ⟵ “IT 411 - 🌐 Digital Forensics”
  - courses: IT 484 ⟵ “IT 484 - 🌐 Cybersecurity Policies”
### `deb6d5b8c196e770` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=supply-chain-management-and-logistics [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `dfa12011deb88491` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=emt-to-asn-and-paramedic-to-asn-pathways-2 [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: NU 104 ⟵ “NU 104 - Pathophysiology for Nursing”
  - courses: NU 140 ⟵ “NU 140 - Nursing Fundamentals”
  - courses: NU 141 ⟵ “NU 141 - Pharmacology for Nursing”
### `e1c47b3059f90bdf` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=digital-communication [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - courses: CM 270 ⟵ “CM 270 - Writing for Multimedia”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: CM 455 ⟵ “CM 455 - Digital Public Relations and Communication”
  - courses: MT 357 ⟵ “MT 357 - Digital Marketing Platforms and Strategy”
  - courses: MT 358 ⟵ “MT 358 - Social Media Marketing and AI Optimization”
### `e21238cfc7e1e8bb` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=emt-to-asn-and-paramedic-to-asn-pathways [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: NU 104 ⟵ “NU 104 - Pathophysiology for Nursing”
### `e33bd8cd7eace64a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `e3c9440b7d2e9389` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=health-sciences [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: HD 420 ⟵ “HD 420 - Social Determinants of Health and Health Behavior”
  - courses: NS 430 ⟵ “NS 430 - Whole Foods Production”
  - courses: SC 361 ⟵ “SC 361 - Population and Society”
  - courses: SC 362 ⟵ “SC 362 - Our Changing Climate”
  - courses: SC 415 ⟵ “SC 415 - Environmental Health”
### `e4cb72720310c957` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-health-science · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `e7d1049c7065edc7` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-small-group-management · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/small-group-management-aas/ (sha256 0411c2728524)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `e886900fecb5112e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-flight · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/professional-flight-bs/ (sha256 a564dfddbaa1)
  - courses: AV 203 ⟵ “AV 203 - Aviation Operations Management”
  - courses: AV 298 ⟵ “AV 298 - Aviation Technology Practicum”
  - courses: AV 325 ⟵ “AV 325 - Advanced Aviation Meteorology”
  - courses: AV 327 ⟵ “AV 327 - Advanced Transport Flight Operations”
  - courses: AV 338 ⟵ “AV 338 - Business Aviation Management”
  - courses: AV 340 ⟵ “AV 340 - Aerospace Business Statistics”
  - courses: AV 346 ⟵ “AV 346 - Transport Category Aircraft Systems I”
  - courses: AV 354 ⟵ “AV 354 - Advanced Flight Path Management”
  - courses: AV 388 ⟵ “AV 388 - Transport Category Aircraft Systems II”
  - courses: AV 412 ⟵ “AV 412 - Aviation Finance”
  - courses: AV 421 ⟵ “AV 421 - Managerial Economics in Aviation”
  - courses: AV 438 ⟵ “AV 438 - Airline Operations”
  - courses: AV 454 ⟵ “AV 454 - Human Factors in Aviation”
  - courses: AV 475 ⟵ “AV 475 - Aviation Law”
  - courses: AV 481 ⟵ “AV 481 - Safety Management Systems”
### `e95d4d0a3f9fe572` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/fire-emergency-management-bs/ (sha256 afedb45fd8c0)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ea66445f72975fc9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-care-administration · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-care-administration-bs/ (sha256 f6b640a6f508)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `ed4d163045193186` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=information-system-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 402 ⟵ “IT 402 - 🌐 IT Consulting Skills”
  - courses: MT 300 ⟵ “MT 300 - 🌐 Management of Information Systems”
  - courses: MT 451 ⟵ “MT 451 - Managing Technological Innovation”
### `ee777757d28ebc8c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=military-physician-assistant-preparation-mpap-2 [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
  - courses: HS 111 ⟵ “HS 111 - 🌐 Medical Terminology”
  - courses: PS 124 ⟵ “PS 124 - 🌐 Introduction to Psychology”
  - courses: PS 200 ⟵ “PS 200 - Introduction to Cognitive Psychology”
### `ee7eb526753eefbc` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/environmental-policy-management-bs/ (sha256 10dc519623e0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: SC 225 ⟵ “SC 225 - Environmental Science”
### `eff597452bf65e6b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=fintech [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: FI 310 ⟵ “FI 310 - FinTech Principles and Concepts”
  - courses: FI 311 ⟵ “FI 311 - FinTech Law and Ethics”
  - courses: FI 410 ⟵ “FI 410 - Blockchain for the Financial Industry”
### `f08a22590581f2bb` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=leadership [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: CM 460 ⟵ “CM 460 - Strategic Communication”
  - courses: LI 410 ⟵ “LI 410 - Leadership in Practice”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 340 ⟵ “MT 340 - 🌐 Conflict Management and Team Dynamics”
### `f0eb0732e191a4cf` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-professional-studies · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-as/ (sha256 8d08aa71b244)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `f20a84efa3a6109c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management · requirement_key=business-foundations [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/environmental-policy-management-bs/ (sha256 10dc519623e0)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `f22ab647e940088c` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-information-technology · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-aas/ (sha256 071358cda74e)
  - courses: CS 114 ⟵ “CS 114 - Academic Strategies for the IT Professional”
  - courses: IT 117 ⟵ “IT 117 - 🌐 Website Development”
  - courses: IN 150 ⟵ “IN 150 - Foundations for Success in Information Technology (IT) Careers”
  - courses: IT 163 ⟵ “IT 163 - 🌐 Database Concepts Using Microsoft Access”
  - courses: IT 190 ⟵ “IT 190 - 🌐 Information Technology Concepts”
  - courses: IT 234 ⟵ “IT 234 - 🌐 Database Concepts”
  - courses: IN 250 ⟵ “IN 250 - 🌐 Software Development Concepts Using Python”
  - courses: IN 251 ⟵ “IN 251 - 🌐 Software Development Concepts Using C#”
  - courses: IN 252 ⟵ “IN 252 - 🌐 Software Development Concepts Using Java”
  - courses: IN 253 ⟵ “IN 253 - 🌐 Software Development Concepts Using JavaScript and PHP”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 299 ⟵ “IT 299 - IT Integrative Project”
### `f42c883adc44b413` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=tax-accountancy [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 314 ⟵ “AC 314 - Accounting Information Systems and Enterprise Risk Management”
  - courses: AC 430 ⟵ “AC 430 - Advanced Tax - Corporate”
  - courses: MT 421 ⟵ “MT 421 - Financial Planning”
  - courses: MT 483 ⟵ “MT 483 - Investments”
### `f471cf82b1f943ea` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cloud-computing-and-solutions · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cloud-computing-solutions-bs/ (sha256 77b0e54d770a)
  - courses: IT 222 ⟵ “IT 222 - 🌐 Introduction to Cloud Computing”
  - courses: IT 227 ⟵ “IT 227 - 🌐 Cloud Infrastructure Administration”
  - courses: IT 234 ⟵ “IT 234 - 🌐 Database Concepts”
  - courses: IN 250 ⟵ “IN 250 - 🌐 Software Development Concepts Using Python”
  - courses: IN 251 ⟵ “IN 251 - 🌐 Software Development Concepts Using C#”
  - courses: IN 252 ⟵ “IN 252 - 🌐 Software Development Concepts Using Java”
  - courses: IN 253 ⟵ “IN 253 - 🌐 Software Development Concepts Using JavaScript and PHP”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 278 ⟵ “IT 278 - 🌐 Windows Administration”
  - courses: IT 286 ⟵ “IT 286 - 🌐 Network Security Concepts”
  - courses: IT 303 ⟵ “IT 303 - 🌐 Cloud Architecture Concepts and Design”
  - courses: IT 304 ⟵ “IT 304 - 🌐 Application Development and Scripting in the Cloud”
  - courses: IT 306 ⟵ “IT 306 - 🌐 Cloud Services Management”
  - courses: IT 403 ⟵ “IT 403 - 🌐 Cloud Security”
  - courses: IT 404 ⟵ “IT 404 - 🌐 Advanced Cloud Security”
  - courses: IT 413 ⟵ “IT 413 - 🌐 Migrating Data and Applications to the Cloud”
  - courses: IT 414 ⟵ “IT 414 - 🌐 Software Development Operations in Cloud Environments”
  - courses: IT 460 ⟵ “IT 460 - 🌐 Systems Analysis and Design”
  - courses: IT 473 ⟵ “IT 473 - Bachelor's Capstone in Cloud Computing and Solutions”
### `f821ffc2c79cb502` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/fire-emergency-management-bs/ (sha256 afedb45fd8c0)
  - courses: FS 100 ⟵ “FS 100 - Introduction to Fire and Emergency Services”
  - courses: FS 105 ⟵ “FS 105 - Fire Prevention Practices”
  - courses: FS 120 ⟵ “FS 120 - Introduction to Emergency Management”
  - courses: FS 202 ⟵ “FS 202 - Principles of Emergency Services”
  - courses: FS 205 ⟵ “FS 205 - Ethics for the Fire and Emergency Services”
  - courses: FS 208 ⟵ “FS 208 - Legal Aspects of Emergency Services”
  - courses: FS 220 ⟵ “FS 220 - Preparedness and Planning for Emergency Management”
  - courses: FS 225 ⟵ “FS 225 - Emergency Management Response”
  - courses: CJ 307 ⟵ “CJ 307 - Crisis Management in Terrorist Attacks and Disasters”
  - courses: FS 304 ⟵ “FS 304 - Community Risk Reduction for Fire and EMS”
  - courses: FS 320 ⟵ “FS 320 - Recovery Practices in Emergency Management”
  - courses: FS 401 ⟵ “FS 401 - Fire Prevention Organization and Management”
  - courses: FS 402 ⟵ “FS 402 - Political, Ethical, and Legal Foundations of Emergency Services”
  - courses: FS 403 ⟵ “FS 403 - Leadership and Management”
  - courses: FS 414 ⟵ “FS 414 - Personnel Management for Fire and EMS”
  - courses: FS 420 ⟵ “FS 420 - Mitigation and Risk Assessment in Emergency Management”
  - courses: FS 425 ⟵ “FS 425 - Disaster Policy in Emergency Management”
  - courses: FS 499 ⟵ “FS 499 - Bachelor's Capstone in Fire and Emergency Management”
### `f9d19b8da8968c9d` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-accounting · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-aas/ (sha256 eb162f849b86)
  - courses: AC 114 ⟵ “AC 114 - 🌐 Accounting I”
  - courses: AC 116 ⟵ “AC 116 - 🌐 Accounting II”
  - courses: AC 239 ⟵ “AC 239 - Managerial Accounting”
  - courses: AC 256 ⟵ “AC 256 - Federal Tax”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: CS 113 ⟵ “CS 113 - Academic Strategies for the Business Professional”
  - courses: IT 133 ⟵ “IT 133 - 🌐 Microsoft Office Applications on Demand”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 217 ⟵ “MT 217 - 🌐 Finance”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: AC 298 ⟵ “AC 298 - Associate's Capstone in Accounting”
### `fa4e32f066b232e4` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-criminal-justice · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-aas/ (sha256 f7068e07e87b)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `fa78913d73469136` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management · requirement_key=program-requirements-open-elective-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/environmental-policy-management-bs/ (sha256 10dc519623e0)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `fc568ca909ef3fbd` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CM 240 ⟵ “CM 240 - Technical Communication”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: PS 124 ⟵ “PS 124 - 🌐 Introduction to Psychology”
### `fd220d8f069f7c89` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=sales [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: CM 214 ⟵ “CM 214 - Public Speaking for the Professional”
  - courses: IT 133 ⟵ “IT 133 - 🌐 Microsoft Office Applications on Demand”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
### `ff21436b8d96262e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-human-resource-management · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/human-resource-management-bs/ (sha256 8c3efdbb3966)
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `795ceba2118a3960` Purdue University Global — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.purdueglobal.edu/transfer-students/ (sha256 a3db18e414b2)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Undergraduate courses with a grade of “C-” or better are eligible for transfer evaluation.”
### `9dfa9a404e9ebd9b` Purdue University-Main Campus — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://admissions.purdue.edu/become-student/transfer/credit/dual/ (sha256 6671a16a4b23)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - per_credit_hour_charge: 25 ⟵ “One of the benefits of taking dual credit courses in high school is tuition assistance. Tuition for the dual credit enrollment program is $25 per credit hour with no additional fees. A 3-4 credit hour dual credit program course will cost $75-100. A comparable course taken as a Purdue undergraduate c”
  - eligibility_tier: 2.5 ⟵ “Minimum GPA of 2.5 on a 4.0 scale”
### `d40d96df7d5130e9` Purdue University-Main Campus — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.purdue.edu/become-student/transfer/credit/ (sha256 f95da144f032)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 32 ⟵ “However, at least 32 credit hours of upper-division courses must be earned at Purdue for a degree from the university.”
### `ac85ed279b3d2c33` Rose-Hulman Institute of Technology — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.rose-hulman.edu/admissions-and-aid/tuition-and-fees.html (sha256 4ae9619c9a60)
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition and Fees: 59772 ⟵ “Tuition and Fees | $59,772”
  - column:Housing and Food: 18534 ⟵ “Housing and Food | $18,534”
  - column:Laptop Fee (one-time student expense): 2800 ⟵ “Laptop Fee (one-time student expense) | $2,800”
  - column:Total Estimated Direct Net Cost: 81106 ⟵ “Total Estimated Direct Net Cost | $81,106”
### `015516028fcd5ddc` Saint Mary's College — academic_programs 2026-27 · program_key=physics-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/physics-bachelor-science/ (sha256 02ceb5788497)
- checks: {"courses": 14, "groups": 3, "groups_skipped": 0}
  - program_name: Physics, Bachelor of Science ⟵ “Physics, Bachelor of Science - PHYS | Saint Mary's College, Notre Dame, IN”
### `0ceb8bcea08a03c4` Saint Mary's College — academic_programs 2026-27 · program_key=design-concentration-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-concentration-bachelor-arts---arsd/ (sha256 9292668dde12)
- checks: {"courses": 67, "groups": 2, "groups_skipped": 0}
  - program_name: Design Concentration, Bachelor of Arts ⟵ “Design Concentration, Bachelor of Arts - ARSD | Saint Mary's College, Notre Dame, IN”
### `175ce25c51e8dc3d` Saint Mary's College — academic_programs 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-fine-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-fine-arts/ (sha256 4cd810a6ea34)
- checks: {"courses": 101, "groups": 6, "groups_skipped": 0}
  - program_name: Applied Arts and Design Concentration, Bachelor of Fine Arts ⟵ “Applied Arts and Design Concentration, Bachelor of Fine Arts - AADE | Saint Mary's College, Notre Dame, IN”
### `19633ae56947d53e` Saint Mary's College — academic_programs 2026-27 · program_key=physics-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/physics-bachelor-arts/ (sha256 a792cff99ffc)
- checks: {"courses": 14, "groups": 2, "groups_skipped": 0}
  - program_name: Physics, Bachelor of Arts ⟵ “Physics, Bachelor of Arts - PHYS | Saint Mary's College, Notre Dame, IN”
### `2794352607ec78d4` Saint Mary's College — academic_programs 2026-27 · program_key=exercise-science-health-and-fitness-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/exercise-science/health-fitness-bachelor-arts/ (sha256 4448a4c853a9)
- checks: {"courses": 21, "groups": 3, "groups_skipped": 0}
  - program_name: Exercise Science, Health and Fitness, Bachelor of Arts ⟵ “Exercise Science, Health and Fitness, Bachelor of Arts - EXHF | Saint Mary's College, Notre Dame, IN”
### `2a7c1db9372d6101` Saint Mary's College — academic_programs 2026-27 · program_key=education-elementary-education-non-licensure-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/education/elementary-non-licensure-bachelor-arts/ (sha256 66d51d63686e)
- checks: {"courses": 19, "groups": 2, "groups_skipped": 0}
  - program_name: Education, Elementary Education Non-Licensure, Bachelor of Arts ⟵ “Education, Elementary Education Non-Licensure, Bachelor of Arts - ELNL | Saint Mary's College, Notre Dame, IN”
### `2b4005326c96b58e` Saint Mary's College — academic_programs 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
- checks: {"courses": 105, "groups": 12, "groups_skipped": 0}
  - program_name: Applied Arts and Design and Art History Double Concentration, Bachelor of Arts ⟵ “Applied Arts and Design and Art History Double Concentration, Bachelor of Arts - ASHA | Saint Mary's College, Notre Dame, IN”
### `31b9406c3b8c636d` Saint Mary's College — academic_programs 2026-27 · program_key=biochemistry-concentration-chemistry-major-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/biochemistry-concentration-bachelor-science/ (sha256 cf495d786a6d)
- checks: {"courses": 10, "groups": 2, "groups_skipped": 0}
  - program_name: Biochemistry Concentration, Chemistry Major, Bachelor of Science ⟵ “Biochemistry Concentration, Chemistry Major, Bachelor of Science - BIOC | Saint Mary's College, Notre Dame, IN”
### `3b142d2b8aafce2d` Saint Mary's College — academic_programs 2026-27 · program_key=cellular-molecular-biology-concentration-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/cellular-molecular-biology-concentration-bachelor-science/ (sha256 345f5d902b16)
- checks: {"courses": 27, "groups": 4, "groups_skipped": 0}
  - program_name: Cellular/Molecular Biology Concentration, Bachelor of Science ⟵ “Cellular/Molecular Biology Concentration, Bachelor of Science - CELL | Saint Mary's College, Notre Dame, IN”
### `3babe952a6818c35` Saint Mary's College — academic_programs 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
- checks: {"courses": 86, "groups": 9, "groups_skipped": 0}
  - program_name: Design and Art History Double Concentration, Bachelor of Arts ⟵ “Design and Art History Double Concentration, Bachelor of Arts - ASHD | Saint Mary's College, Notre Dame, IN”
### `3fa5c3a66fe23ca1` Saint Mary's College — academic_programs 2026-27 · program_key=studio-art-concentration-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
- checks: {"courses": 91, "groups": 12, "groups_skipped": 0}
  - program_name: Studio Art Concentration, Bachelor of Arts ⟵ “Studio Art Concentration, Bachelor of Arts - ARTS | Saint Mary's College, Notre Dame, IN”
### `5ddb2c588ecda171` Saint Mary's College — academic_programs 2026-27 · program_key=economics-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/economics-bachelor-arts/ (sha256 3fba044b4348)
- checks: {"courses": 15, "groups": 2, "groups_skipped": 0}
  - program_name: Economics, Bachelor of Arts ⟵ “Economics, Bachelor of Arts - ECON | Saint Mary's College, Notre Dame, IN”
### `6c56cf83b0294c77` Saint Mary's College — academic_programs 2026-27 · program_key=ecology-evolution-and-environmental-biology-concentration-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/ecology-evolution-environmental-biology-concentration-bachelor-science/ (sha256 2bd059a8e87e)
- checks: {"courses": 28, "groups": 5, "groups_skipped": 0}
  - program_name: Ecology, Evolution and Environmental Biology Concentration, Bachelor of Science ⟵ “Ecology, Evolution and Environmental Biology Concentration, Bachelor of Science - EEEB | Saint Mary's College, Notre Dame, IN”
### `75ae4f477f6c9037` Saint Mary's College — academic_programs 2026-27 · program_key=theatre-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/communication-studies-dance-theatre/theatre-bachelor-arts/ (sha256 3b6ed8625657)
- checks: {"courses": 26, "groups": 1, "groups_skipped": 0}
  - program_name: Theatre, Bachelor of Arts ⟵ “Theatre, Bachelor of Arts - THTR | Saint Mary's College, Notre Dame, IN”
### `84baeb3b9d5b3821` Saint Mary's College — academic_programs 2026-27 · program_key=art-history-concentration-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-concentration-bachelor-arts/ (sha256 2674d7047df7)
- checks: {"courses": 74, "groups": 8, "groups_skipped": 0}
  - program_name: Art History Concentration, Bachelor of Arts ⟵ “Art History Concentration, Bachelor of Arts - ARTH | Saint Mary's College, Notre Dame, IN”
### `87a95a27f856994e` Saint Mary's College — academic_programs 2026-27 · program_key=education-elementary-k-6-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/education/elementary-k-6-bachelor-arts/ (sha256 fcf6cdecb2c0)
- checks: {"courses": 19, "groups": 2, "groups_skipped": 0}
  - program_name: Education, Elementary K-6, Bachelor of Arts ⟵ “Education, Elementary K-6, Bachelor of Arts - ELED | Saint Mary's College, Notre Dame, IN”
### `9065a586d46edc55` Saint Mary's College — academic_programs 2026-27 · program_key=design-concentration-bachelor-of-fine-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-concentration-bachelor-fine-arts/ (sha256 83cfddcbe154)
- checks: {"courses": 81, "groups": 3, "groups_skipped": 0}
  - program_name: Design Concentration, Bachelor of Fine Arts ⟵ “Design Concentration, Bachelor of Fine Arts - DESN | Saint Mary's College, Notre Dame, IN”
### `999a67a4891dc3fe` Saint Mary's College — academic_programs 2026-27 · program_key=art-history-minor-for-b-a-studio-art-majors [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-minor-studio-art-majors/ (sha256 50dfbae04f79)
- checks: {"courses": 13, "groups": 2, "groups_skipped": 0}
  - program_name: Art History, Minor for B.A. Studio Art Majors ⟵ “Art History, Minor for B.A. Studio Art Majors - ARHI | Saint Mary's College, Notre Dame, IN”
### `99c48b5f7179bb65` Saint Mary's College — academic_programs 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-arts---arad/ (sha256 d11b8e1fa54c)
- checks: {"courses": 43, "groups": 5, "groups_skipped": 0}
  - program_name: Applied Arts and Design Concentration, Bachelor of Arts ⟵ “Applied Arts and Design Concentration, Bachelor of Arts - ARAD | Saint Mary's College, Notre Dame, IN”
### `9f1dff34beb410c6` Saint Mary's College — academic_programs 2026-27 · program_key=accounting-bachelor-of-business-administration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/accounting-bachelor-business-administration/ (sha256 1d4de509536d)
- checks: {"courses": 27, "groups": 2, "groups_skipped": 0}
  - program_name: Accounting, Bachelor of Business Administration ⟵ “Accounting, Bachelor of Business Administration - ACCT | Saint Mary's College, Notre Dame, IN”
### `a1156c068cbd0673` Saint Mary's College — academic_programs 2026-27 · program_key=chemistry-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/chemistry-bachelor-science/ (sha256 5d09474a83b4)
- checks: {"courses": 13, "groups": 2, "groups_skipped": 0}
  - program_name: Chemistry, Bachelor of Science ⟵ “Chemistry, Bachelor of Science - CHEM | Saint Mary's College, Notre Dame, IN”
### `a7ae41be2e5425e2` Saint Mary's College — academic_programs 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
- checks: {"courses": 111, "groups": 13, "groups_skipped": 0}
  - program_name: Studio Art Concentration, Bachelor of Fine Arts ⟵ “Studio Art Concentration, Bachelor of Fine Arts - ART | Saint Mary's College, Notre Dame, IN”
### `a9cf9e878477835b` Saint Mary's College — academic_programs 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
- checks: {"courses": 129, "groups": 17, "groups_skipped": 0}
  - program_name: Studio Art and Art History Double Concentration, Bachelor of Arts ⟵ “Studio Art and Art History Double Concentration, Bachelor of Arts - ARSH | Saint Mary's College, Notre Dame, IN”
### `bc34cbfc68bd9965` Saint Mary's College — academic_programs 2026-27 · program_key=exercise-science-rehabilitative-science-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/exercise-science/rehabilitative-science-bachelor-science/ (sha256 46ecbe960958)
- checks: {"courses": 19, "groups": 2, "groups_skipped": 0}
  - program_name: Exercise Science, Rehabilitative Science, Bachelor of Science ⟵ “Exercise Science, Rehabilitative Science, Bachelor of Science - EXRS | Saint Mary's College, Notre Dame, IN”
### `c4eedf7a2c05daf0` Saint Mary's College — academic_programs 2026-27 · program_key=marketing-bachelor-of-business-administration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/marketing-bachelor-business-administration/ (sha256 04ed39ef8fcb)
- checks: {"courses": 25, "groups": 2, "groups_skipped": 0}
  - program_name: Marketing, Bachelor of Business Administration ⟵ “Marketing, Bachelor of Business Administration - MKT | Saint Mary's College, Notre Dame, IN”
### `fc55207a0ce6650c` Saint Mary's College — academic_programs 2026-27 · program_key=communication-studies-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/communication-studies-dance-theatre/communication-studies-bachelor-arts/ (sha256 52cca075fded)
- checks: {"courses": 40, "groups": 2, "groups_skipped": 0}
  - program_name: Communication Studies, Bachelor of Arts ⟵ “Communication Studies, Bachelor of Arts - COMM | Saint Mary's College, Notre Dame, IN”
### `6926793d7b86ee38` Saint Mary's College — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/academic-guide-first-year-students/credit-examination-policies/ (sha256 448f770b907a)
- checks: {"distinct_exams": 34, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4]:  ⟵ “African American Studies | 4 | HIST 205 | Historical Inquiry | 3 hrs”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | ART 241 | Historical Inquiry | 3 hrs”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | BIO 110 | Natural Science | 4 hrs”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | 5 | BIO 155-158 | Natural Science | 8 hrs”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 | MATH 131- MATH 132 | Mathematics | 8 hrs”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language and Culture | 4 | MLCH 111-112 | Modern Languages | 6 hrs”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|4]:  ⟵ “Comparative Gov't & Politics3 | 4 | POSC 207 | Social Science | 3 hrs”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CPSC 207 | none | 3 hrs”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles | 4 | CPSC 103 | none | 2 hrs”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Lang and Comp | 4 | ENWR 100 level | none | 3 hrs”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Lit and Comp | 4 | ENLT 100 level | Literary Inquiry | 3 hrs”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science | 4 | ENVS 171 | Natural Science | 3 hrs”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | HIST 102 | Historical Inquiry | 3 hrs”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture | 4 | MLFR 111-112 | Modern Languages | 6 hrs”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language and Culture | 4 | MLGR 111-112 | Modern Languages | 6 hrs”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography | 4 | ANTH 100 | none | 3 hrs”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4]:  ⟵ “Italian Language and Culture | 4 | MLIT 111-MLIT 210 | Modern Languages | 6 hrs”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4]:  ⟵ “Japanese Language and Culture | 4 | MLJA 111-112 | Modern Languages | 6 hrs”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin | 4 | LATN 111-112 | none | 6 hrs”
  - equivalencies[AP-MACROECONOMICS|4]:  ⟵ “Macroeconomics | 4 | ECON 251 | Social Science | 3 hrs”
  - equivalencies[AP-MICROECONOMICS|4]:  ⟵ “Microeconomics | 4 | ECON 252 | Social Science | 3 hrs”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory4 | 4 | MUS 181 | none | 3 hrs”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1 | 4 | PHYS 111 | Natural Science | 4 hrs”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C: Mechanics | 4 | PHYS 121 | Natural Science | 4 hrs”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Precalculus | 4 | MATH 103 | none | 3 hrs”
  - … 10 more rows
### `026b5024c8f78284` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-studio-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
  - section: major-requirements-66-hours-studio-electives ⟵ “Major Requirements (66 Hours) — Studio Electives”
### `04e3db236387f5ab` Saint Mary's College — degree_requirements 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-core-requirements-in-art-history-and-studio-art-desi [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
### `084670076b9cc982` Saint Mary's College — degree_requirements 2026-27 · program_key=theatre-bachelor-of-arts · requirement_key=major-requirements-30-hours-required-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/communication-studies-dance-theatre/theatre-bachelor-arts/ (sha256 3b6ed8625657)
  - courses: THTR 205 ⟵ “THTR 205 - Introduction to Acting”
  - courses: THTR 245 ⟵ “THTR 245 - Stagecraft”
  - courses: THTR 265 ⟵ “THTR 265 - Play Analysis for the Theatre”
  - courses: THTR 375 ⟵ “THTR 375 - Rehearsal, Performance, and Production”
  - courses: THTR 380 ⟵ “THTR 380 - History of Theatre and Dramatic Literature”
  - courses: THTR 475 ⟵ “THTR 475 - Stage Directing”
  - courses: THTR 480 ⟵ “THTR 480 - Production Projects”
  - courses: THTR 387 ⟵ “THTR 387 - Hair and Makeup for the Stage”
  - courses: THTR 445 ⟵ “THTR 445 - Scenic and Prop Design and Scenic Painting”
  - courses: THTR 455 ⟵ “THTR 455 - Costume Design”
  - courses: THTR 135 ⟵ “THTR 135 - Introduction to Theatre”
  - courses: THTR 305 ⟵ “THTR 305 - Intermediate Acting”
  - courses: THTR 325 ⟵ “THTR 325 - Playwriting I”
  - courses: THTR 335 ⟵ “THTR 335 - History of Western European Cultural Performance”
  - courses: THTR 355 ⟵ “THTR 355 - Voice and Movement”
  - courses: THTR 365 ⟵ “THTR 365 - Fashion and Costume History”
  - courses: THTR 375 ⟵ “THTR 375 - Rehearsal, Performance, and Production”
  - courses: THTR 378 ⟵ “THTR 378 - Contemporary Women’s Drama”
  - courses: THTR 385 ⟵ “THTR 385 - Beginning Fashion and Costume Construction and Flat Patterning”
  - courses: THTR 387 ⟵ “THTR 387 - Hair and Makeup for the Stage”
  - courses: THTR 430 ⟵ “THTR 430 - Theatre Management”
  - courses: THTR 445 ⟵ “THTR 445 - Scenic and Prop Design and Scenic Painting”
  - courses: THTR 455 ⟵ “THTR 455 - Costume Design”
  - courses: THTR 490 ⟵ “THTR 490 - Special Topics in Theatre Studies”
  - courses: THTR 497 ⟵ “THTR 497 - Independent Study”
  - … 1 more rows
### `094160b1554f2c53` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-media-specific [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
  - courses: ART 343 ⟵ “ART 343 - History of Photography”
  - courses: ART 344 ⟵ “ART 344 - Film History and Analysis”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `107cd719f3c66b92` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-100-200-level-studio-course [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
### `14aef4993bea2765` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-ancient-medieval [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-concentration-bachelor-arts/ (sha256 2674d7047df7)
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `18e6dd7d26d35aab` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-eighteenth-nineteenth-century [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `1b00ab0f7094f062` Saint Mary's College — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration · requirement_key=major-requirements-63-hours-other-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/accounting-bachelor-business-administration/ (sha256 1d4de509536d)
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `1f7591f40106238f` Saint Mary's College — degree_requirements 2026-27 · program_key=communication-studies-bachelor-of-arts · requirement_key=major-requirements-33-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/communication-studies-dance-theatre/communication-studies-bachelor-arts/ (sha256 52cca075fded)
  - courses: COMM 103 ⟵ “COMM 103 - Introduction to Communication (with a grade of B- or above)”
  - courses: COMM 210 ⟵ “COMM 210 - Mass Media and Society”
  - courses: COMM 330 ⟵ “COMM 330 - Critical Issues in Mass Communication”
### `1f9e890008d829fb` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-all-of-the-following-core-requirements [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
### `1fae9b9709ffa5e9` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-correlate-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
  - courses: BIO 213 ⟵ “BIO 213 - Introductory Human Anatomy”
  - courses: COMM 260 ⟵ “COMM 260 - Digital Video Production”
  - courses: COMM 383 ⟵ “COMM 383 - Art and Entertainment Law”
  - courses: COMM 486 ⟵ “COMM 486 - Broadcast Media Production”
  - courses: DANC 240 ⟵ “DANC 240 - Introduction to Dance”
  - courses: DANC 241 ⟵ “DANC 241 - Contemporary Issues in Dance”
  - courses: ENLT 278 ⟵ “ENLT 278 - From Fiction to Film”
  - courses: MLIT 320 ⟵ “MLIT 320 - Italian Cinema, 1945–1965”
  - courses: PHIL 245 ⟵ “PHIL 245 - Philosophy of World Cultures”
  - courses: PHIL 235 ⟵ “PHIL 235 - Philosophy of Human Existence”
  - courses: PHIL 252 ⟵ “PHIL 252 - Philosophy of Art”
  - courses: THTR 205 ⟵ “THTR 205 - Introduction to Acting”
  - courses: THTR 245 ⟵ “THTR 245 - Stagecraft”
  - courses: THTR 380 ⟵ “THTR 380 - History of Theatre and Dramatic Literature”
  - courses: THTR 445 ⟵ “THTR 445 - Scenic and Prop Design and Scenic Painting”
  - courses: THTR 455 ⟵ “THTR 455 - Costume Design”
### `232d21218eff0672` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 308 ⟵ “ART 308 - Advanced Printmedia/Drawing”
  - courses: ART 385 ⟵ “ART 385 - Design Research Methods”
  - courses: ART 499 ⟵ “ART 499 - Internship”
### `2f815a59803418ac` Saint Mary's College — degree_requirements 2026-27 · program_key=exercise-science-health-and-fitness-bachelor-of-arts · requirement_key=exercise-science-health-and-fitness-bachelor-of-arts-exhf-supporting-required-2 [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/exercise-science/health-fitness-bachelor-arts/ (sha256 4448a4c853a9)
  - courses: PHIL 255 ⟵ “PHIL 255 - Medical Ethics”
  - courses: PHYS 111 ⟵ “PHYS 111 - College Physics I: Mechanics and Waves”
  - courses: PHYS 112 ⟵ “PHYS 112 - College Physics II: Temperature, Electricity, and Light”
  - courses: PSYC 305 ⟵ “PSYC 305 - Lifespan Developmental Psychology”
### `37a25ebe070e724d` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art (in Area of Emphasis)”
### `399c4c7c509d1021` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-non-western-underrepresented-traditions [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `3f6f95f3d6d0d3c7` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-studio-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
  - section: major-requirements-78-hours-studio-electives ⟵ “MAJOR REQUIREMENTS (78 HOURS) — Studio Electives”
### `400d92a3f2783200` Saint Mary's College — degree_requirements 2026-27 · program_key=education-elementary-education-non-licensure-bachelor-of-arts · requirement_key=major-requirements-65-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/education/elementary-non-licensure-bachelor-arts/ (sha256 66d51d63686e)
  - courses: EDUC 201 ⟵ “EDUC 201 - Foundations for Teaching in a Multicultural Society”
  - courses: EDUC 213 ⟵ “EDUC 213 - American Mosaic: Integrative Approaches to the Arts in Elementary/Middle School”
  - courses: EDUC 215 ⟵ “EDUC 215 - Teaching Wellness in Elementary/Middle School”
  - courses: EDUC 220 ⟵ “EDUC 220 - Applied Media and Instructional Technology”
  - courses: EDUC 230 ⟵ “EDUC 230 - Educational Psychology: Foundations of Special Education in Elementary/Middle School”
  - courses: EDUC 240 ⟵ “EDUC 240 - General Methods for Elementary/Middle School”
  - courses: EDUC 301 ⟵ “EDUC 301 - Teaching Language Arts in Elementary/Middle School”
  - courses: EDUC 302 ⟵ “EDUC 302 - Teaching Social Studies in Elementary/Middle School”
  - courses: EDUC 303 ⟵ “EDUC 303 - Teaching Science in Elementary/Middle School”
  - courses: EDUC 304 ⟵ “EDUC 304 - Teaching Reading in Elementary/Middle School”
  - courses: EDUC 305 ⟵ “EDUC 305 - Teaching Mathematics in Elementary/Middle School”
  - courses: EDUC 308 ⟵ “EDUC 308 - Children’s Literature in Elementary/Middle School”
  - courses: EDUC 352 ⟵ “EDUC 352 - Educational Psychology: Human Growth & Development of the Pre-School/Elementary/Middle School Studen”
  - courses: EDUC 406 ⟵ “EDUC 406 - Reading Assessment and Intervention in Elementary/Middle School”
  - courses: EDUC 499 ⟵ “EDUC 499 - Internship (or 3 Courses related to Education that have been approved by the department chair)”
### `4498784ed8000c67` Saint Mary's College — degree_requirements 2026-27 · program_key=design-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-all-of-the-following-core-requirements [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-concentration-bachelor-arts---arsd/ (sha256 9292668dde12)
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
### `472eaf666e0d255a` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-contemporary [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
  - courses: ART 302 ⟵ “ART 302 - Curatorial Studies: Theory + Practice”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
### `4cb31005a4bc007d` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-non-western-underrepresented-traditions [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `4fe79aba437566b7` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-contemporary [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-concentration-bachelor-arts/ (sha256 2674d7047df7)
  - courses: ART 302 ⟵ “ART 302 - Curatorial Studies: Theory + Practice”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
### `524402b7e016930d` Saint Mary's College — degree_requirements 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-ancient-medieval [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `53b1ca28aea6ab7e` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 308 ⟵ “ART 308 - Advanced Printmedia/Drawing”
  - courses: ART 385 ⟵ “ART 385 - Design Research Methods”
  - courses: ART 499 ⟵ “ART 499 - Internship”
### `5a9b2e3da9e9754b` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-upper-level-art-history-elective [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
  - courses: ART 343 ⟵ “ART 343 - History of Photography”
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
### `5e7c8996a55ce653` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-eighteenth-nineteenth-century [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-concentration-bachelor-arts/ (sha256 2674d7047df7)
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `5e85f8bc8422aba4` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-upper-level-art-history-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
  - section: major-requirements-66-hours-upper-level-art-history-electives ⟵ “Major Requirements (66 Hours) — Upper Level Art History Electives”
### `6313f94d5bd834e7` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-minor-for-b-a-studio-art-majors · requirement_key=minor-requirements-21-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-minor-studio-art-majors/ (sha256 50dfbae04f79)
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
### `699b2776c16fc900` Saint Mary's College — degree_requirements 2026-27 · program_key=physics-bachelor-of-science · requirement_key=major-requirements-61-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/physics-bachelor-science/ (sha256 02ceb5788497)
  - courses: PHYS 121 ⟵ “PHYS 121 - General Physics I: Mechanics and Waves”
  - courses: PHYS 122 ⟵ “PHYS 122 - General Physics II: Temperature, Electricity, and Light”
  - courses: PHYS 253 ⟵ “PHYS 253 - General Physics III: Modern Physics”
  - courses: PHYS 323 ⟵ “PHYS 323 - Classical Mechanics”
  - courses: PHYS 343 ⟵ “PHYS 343 - Thermodynamics”
  - courses: PHYS 424 ⟵ “PHYS 424 - Quantum Mechanics”
  - courses: PHYS 444 ⟵ “PHYS 444 - Electricity and Magnetism”
  - courses: PHYS 495 ⟵ “PHYS 495 - Senior Seminar”
  - courses: PHYS 272L ⟵ “PHYS 272L - Computational Physics Laboratory”
  - courses: PHYS 282L ⟵ “PHYS 282L - Modern Experimental Laboratory”
  - courses: PHYS 292L ⟵ “PHYS 292L - Wave Mechanics Laboratory”
### `6a11006f35f64f30` Saint Mary's College — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration · requirement_key=major-requirements-63-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/accounting-bachelor-business-administration/ (sha256 1d4de509536d)
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 202 ⟵ “BUAD 202 - Principles of Managerial Accounting”
  - courses: BUAD 212 ⟵ “BUAD 212 - Principles of Finance”
  - courses: BUAD 221 ⟵ “BUAD 221 - Principles of Management”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 245 ⟵ “BUAD 245 - Business Communication”
  - courses: BUAD 247 ⟵ “BUAD 247 - Introduction to Excel, Statistics, and Business Analytics”
  - courses: BUAD 301 ⟵ “BUAD 301 - Intermediate Accounting I”
  - courses: BUAD 302 ⟵ “BUAD 302 - Intermediate Accounting II”
  - courses: BUAD 303 ⟵ “BUAD 303 - Cost Accounting”
  - courses: BUAD 304 ⟵ “BUAD 304 - Personal Income Tax”
  - courses: BUAD 344 ⟵ “BUAD 344 - Business Law I”
  - courses: BUAD 346 ⟵ “BUAD 346 - Business & Organizational Ethics”
  - courses: BUAD 402 ⟵ “BUAD 402 - Auditing”
  - courses: BUAD 446 ⟵ “BUAD 446 - Strategic Management”
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
  - courses: BUAD 305 ⟵ “BUAD 305 - Accounting for Not-for-Profit Organizations”
  - courses: BUAD 306 ⟵ “BUAD 306 - Fraud Examination”
  - courses: BUAD 317 ⟵ “BUAD 317 - Financial Statement Analysis”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 401 ⟵ “BUAD 401 - Advanced Accounting”
  - courses: BUAD 404 ⟵ “BUAD 404 - Advanced Topics in Income Tax”
  - courses: BUAD 405 ⟵ “BUAD 405 - Partnerships, S-Corporations, Trusts -- Entity Taxation”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
  - … 1 more rows
### `6ed4cffddc96f307` Saint Mary's College — degree_requirements 2026-27 · program_key=economics-bachelor-of-arts · requirement_key=major-requirements-34-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/economics-bachelor-arts/ (sha256 3fba044b4348)
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
  - courses: ECON 351 ⟵ “ECON 351 - Intermediate Macroeconomics”
  - courses: ECON 352 ⟵ “ECON 352 - Intermediate Microeconomics”
  - courses: ECON 457 ⟵ “ECON 457 - Introduction to Econometrics”
  - courses: ECON 354 ⟵ “ECON 354 - Economic Development”
  - courses: ECON 355 ⟵ “ECON 355 - Economics of Crime and Punishment”
  - courses: ECON 356 ⟵ “ECON 356 - Comparative Economic Systems”
  - courses: ECON 375 ⟵ “ECON 375 - Game Theory: Strategic Decision Making”
  - courses: ECON 390 ⟵ “ECON 390 - Topics in Economics”
  - courses: ECON 451 ⟵ “ECON 451 - History of Economic Thought”
  - courses: ECON 452 ⟵ “ECON 452 - International Trade and Finance”
  - courses: ECON 497 ⟵ “ECON 497 - Independent Study”
### `6f74b646c765df8b` Saint Mary's College — degree_requirements 2026-27 · program_key=exercise-science-health-and-fitness-bachelor-of-arts · requirement_key=exercise-science-health-and-fitness-bachelor-of-arts-exhf-required-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/exercise-science/health-fitness-bachelor-arts/ (sha256 4448a4c853a9)
  - courses: BIO 141 ⟵ “BIO 141 - Human Anatomy and Physiology I”
  - courses: BIO 142 ⟵ “BIO 142 - Human Anatomy and Physiology II”
  - courses: BIO 245 ⟵ “BIO 245 - We Like to Move It (Move it): Introduction to Kinesiology”
  - courses: BIO 329 ⟵ “BIO 329 - Exercise Physiology”
  - courses: EXSC 110 ⟵ “EXSC 110 - Strength and Conditioning”
  - courses: EXSC 330 ⟵ “EXSC 330 - Exercise Testing and Prescription”
  - courses: EXSC 340 ⟵ “EXSC 340 - Exercise Programming for Special Populations”
  - courses: EXSC 480 ⟵ “EXSC 480 - Exercise Science Practicum”
  - courses: EXSC 485 ⟵ “EXSC 485 - Research Methods in Exercise Science”
### `70a556d0bfb168e2` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-twentieth-century [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-concentration-bachelor-arts/ (sha256 2674d7047df7)
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `7659ed0a3a84bd0b` Saint Mary's College — degree_requirements 2026-27 · program_key=exercise-science-rehabilitative-science-bachelor-of-science · requirement_key=major-requirements-60-credits-required-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/exercise-science/rehabilitative-science-bachelor-science/ (sha256 46ecbe960958)
  - courses: BIO 155 ⟵ “BIO 155 - Foundations of Molecular Biology”
  - courses: BIO 156 ⟵ “BIO 156 - Foundations of Ecology and Evolution”
  - courses: BIO 157 ⟵ “BIO 157 - Foundations of Cellular Biology”
  - courses: BIO 158 ⟵ “BIO 158 - Foundations of Form and Function”
  - courses: BIO 228 ⟵ “BIO 228 - General Physiology”
  - courses: BIO 245 ⟵ “BIO 245 - We Like to Move It (Move it): Introduction to Kinesiology”
  - courses: BIO 321 ⟵ “BIO 321 - Comparative Vertebrate and Human Anatomy”
  - courses: BIO 329 ⟵ “BIO 329 - Exercise Physiology”
  - courses: EXSC 110 ⟵ “EXSC 110 - Strength and Conditioning”
  - courses: EXSC 330 ⟵ “EXSC 330 - Exercise Testing and Prescription”
  - courses: EXSC 340 ⟵ “EXSC 340 - Exercise Programming for Special Populations”
  - courses: EXSC 480 ⟵ “EXSC 480 - Exercise Science Practicum”
  - courses: EXSC 485 ⟵ “EXSC 485 - Research Methods in Exercise Science”
### `7859cfcd523489ba` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-twentieth-century [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `8886f0a774a0488f` Saint Mary's College — degree_requirements 2026-27 · program_key=physics-bachelor-of-science · requirement_key=major-requirements-61-hours-elective-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/physics-bachelor-science/ (sha256 02ceb5788497)
  - section: major-requirements-61-hours-elective-courses ⟵ “Major Requirements (61 Hours) — Elective Courses”
### `8f8906cda85efb4e` Saint Mary's College — degree_requirements 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-twentieth-century [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `9c982013123b7d47` Saint Mary's College — degree_requirements 2026-27 · program_key=marketing-bachelor-of-business-administration · requirement_key=major-requirements-60-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/marketing-bachelor-business-administration/ (sha256 04ed39ef8fcb)
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 202 ⟵ “BUAD 202 - Principles of Managerial Accounting”
  - courses: BUAD 212 ⟵ “BUAD 212 - Principles of Finance”
  - courses: BUAD 221 ⟵ “BUAD 221 - Principles of Management”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 245 ⟵ “BUAD 245 - Business Communication”
  - courses: BUAD 247 ⟵ “BUAD 247 - Introduction to Excel, Statistics, and Business Analytics”
  - courses: BUAD 331 ⟵ “BUAD 331 - Advertising and Promotion”
  - courses: BUAD 333 ⟵ “BUAD 333 - Market Research”
  - courses: BUAD 334 ⟵ “BUAD 334 - Consumer Behavior”
  - courses: BUAD 346 ⟵ “BUAD 346 - Business & Organizational Ethics”
  - courses: BUAD 433 ⟵ “BUAD 433 - Global Digital Marketing”
  - courses: BUAD 446 ⟵ “BUAD 446 - Strategic Management”
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
  - courses: BUAD 332 ⟵ “BUAD 332 - Social Media Marketing”
  - courses: BUAD 335 ⟵ “BUAD 335 - Supply Chain Marketing”
  - courses: BUAD 336 ⟵ “BUAD 336 - Brand Management”
  - courses: BUAD 342 ⟵ “BUAD 342 - New Venture”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business”
  - courses: BUAD 434 ⟵ “BUAD 434 - Sales Management and Professional Selling”
  - courses: BUAD 437 ⟵ “BUAD 437 - Artificial Intelligence Marketing”
  - courses: BUAD 438 ⟵ “BUAD 438 - Service Marketing”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
### `9d751afa78fd6e59` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art *”
### `a27149bf928e1ff4` Saint Mary's College — degree_requirements 2026-27 · program_key=physics-bachelor-of-arts · requirement_key=major-requirements-38-42-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/physics-bachelor-arts/ (sha256 a792cff99ffc)
  - courses: PHYS 121 ⟵ “PHYS 121 - General Physics I: Mechanics and Waves”
  - courses: PHYS 122 ⟵ “PHYS 122 - General Physics II: Temperature, Electricity, and Light”
  - courses: PHYS 253 ⟵ “PHYS 253 - General Physics III: Modern Physics”
  - courses: PHYS 495 ⟵ “PHYS 495 - Senior Seminar”
  - courses: PHYS 272L ⟵ “PHYS 272L - Computational Physics Laboratory”
  - courses: PHYS 282L ⟵ “PHYS 282L - Modern Experimental Laboratory”
  - courses: PHYS 292L ⟵ “PHYS 292L - Wave Mechanics Laboratory”
  - courses: PHYS 323 ⟵ “PHYS 323 - Classical Mechanics”
  - courses: PHYS 343 ⟵ “PHYS 343 - Thermodynamics”
  - courses: PHYS 424 ⟵ “PHYS 424 - Quantum Mechanics”
  - courses: PHYS 444 ⟵ “PHYS 444 - Electricity and Magnetism”
### `a7bd0e1c345d10f1` Saint Mary's College — degree_requirements 2026-27 · program_key=design-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-all-of-the-following-core-requirements [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-concentration-bachelor-fine-arts/ (sha256 83cfddcbe154)
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
### `ae3fdf60631a2c4b` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-upper-level-art-history-elective [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-concentration-bachelor-arts/ (sha256 2674d7047df7)
  - section: major-requirements-42-hours-upper-level-art-history-elective ⟵ “Major Requirements (42 Hours) — Upper Level Art History Elective”
### `af77642c0f65113d` Saint Mary's College — degree_requirements 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-media-specific [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
  - courses: ART 343 ⟵ “ART 343 - History of Photography”
  - courses: ART 344 ⟵ “ART 344 - Film History and Analysis”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `b8dedda845736b18` Saint Mary's College — degree_requirements 2026-27 · program_key=economics-bachelor-of-arts · requirement_key=major-requirements-34-hours-required-supporting-course [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/economics-bachelor-arts/ (sha256 3fba044b4348)
  - courses: MATH 113 ⟵ “MATH 113 - Survey of Calculus (or higher calculus)”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `bb36c691d646ef92` Saint Mary's College — degree_requirements 2026-27 · program_key=ecology-evolution-and-environmental-biology-concentration-bachelor-of-science · requirement_key=major-requirements-60-hours-one-of-the-following-to-fulfill-upper-level-research [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/ecology-evolution-environmental-biology-concentration-bachelor-science/ (sha256 2bd059a8e87e)
  - courses: BIO 209 ⟵ “BIO 209 - Marine Biology”
  - courses: BIO 230 ⟵ “BIO 230 - Molecular Cell Biology”
  - courses: BIO 232 ⟵ “BIO 232 - Animal Behavior”
  - courses: BIO 316 ⟵ “BIO 316 - Conservation Biology”
  - courses: BIO 323 ⟵ “BIO 323 - Ecology”
  - courses: BIO 335 ⟵ “BIO 335 - Plant-Animal Interactions”
### `bc43905c99816d11` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-all-of-the-following-core-requirements [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-fine-arts/ (sha256 4cd810a6ea34)
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
### `bd81c2528a672f70` Saint Mary's College — degree_requirements 2026-27 · program_key=education-elementary-k-6-bachelor-of-arts · requirement_key=major-requirements-65-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/education/elementary-k-6-bachelor-arts/ (sha256 fcf6cdecb2c0)
  - courses: EDUC 201 ⟵ “EDUC 201 - Foundations for Teaching in a Multicultural Society (field)”
  - courses: EDUC 213 ⟵ “EDUC 213 - American Mosaic: Integrative Approaches to the Arts in Elementary/Middle School”
  - courses: EDUC 215 ⟵ “EDUC 215 - Teaching Wellness in Elementary/Middle School”
  - courses: EDUC 220 ⟵ “EDUC 220 - Applied Media and Instructional Technology”
  - courses: EDUC 230 ⟵ “EDUC 230 - Educational Psychology: Foundations of Special Education in Elementary/Middle School (field)”
  - courses: EDUC 240 ⟵ “EDUC 240 - General Methods for Elementary/Middle School”
  - courses: EDUC 301 ⟵ “EDUC 301 - Teaching Language Arts in Elementary/Middle School (field)”
  - courses: EDUC 302 ⟵ “EDUC 302 - Teaching Social Studies in Elementary/Middle School (field)”
  - courses: EDUC 303 ⟵ “EDUC 303 - Teaching Science in Elementary/Middle School (field)”
  - courses: EDUC 304 ⟵ “EDUC 304 - Teaching Reading in Elementary/Middle School (field)”
  - courses: EDUC 305 ⟵ “EDUC 305 - Teaching Mathematics in Elementary/Middle School (field)”
  - courses: EDUC 308 ⟵ “EDUC 308 - Children’s Literature in Elementary/Middle School (field)”
  - courses: EDUC 352 ⟵ “EDUC 352 - Educational Psychology: Human Growth & Development of the Pre-School/Elementary/Middle School Studen (field)”
  - courses: EDUC 406 ⟵ “EDUC 406 - Reading Assessment and Intervention in Elementary/Middle School (field)”
  - courses: EDUC 472 ⟵ “EDUC 472 - Student Teaching in Elementary School”
### `cbdff4a4a4228aad` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-contemporary [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
  - courses: ART 302 ⟵ “ART 302 - Curatorial Studies: Theory + Practice”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
### `d39b1127b52f4f7c` Saint Mary's College — degree_requirements 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-contemporary [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
  - courses: ART 302 ⟵ “ART 302 - Curatorial Studies: Theory + Practice”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
### `d4bd59bfbd7f3028` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-twentieth-century [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `d86ea6dea700de75` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-100-200-level-studio-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art (selected topics)”
### `db77665abfb57664` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-ancient-medieval [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `dcc3d40d92448fe7` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-eighteenth-nineteenth-century [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `e860d0da1fe4050a` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-all-of-the-following-core-requirements [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-arts---arad/ (sha256 d11b8e1fa54c)
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
### `ee9c7576165cc665` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art”
### `f412e53d7b089370` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 308 ⟵ “ART 308 - Advanced Printmedia/Drawing”
  - courses: ART 385 ⟵ “ART 385 - Design Research Methods”
  - courses: ART 499 ⟵ “ART 499 - Internship”
### `f48fcaabb21e90f0` Saint Mary's College — degree_requirements 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-non-western-underrepresented-traditions [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `f6d82ddb925dc437` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-non-western-underrepresented-traditions [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-concentration-bachelor-arts/ (sha256 2674d7047df7)
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `f7a50b8d4a7e73a2` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-studio-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
  - section: major-requirements-42-hours-studio-electives ⟵ “Major Requirements (42 hours) — Studio Electives”
### `fb13a16275000e91` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-ancient-medieval [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `fd0b73391853a0e6` Saint Mary's College — degree_requirements 2026-27 · program_key=marketing-bachelor-of-business-administration · requirement_key=major-requirements-60-hours-other-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/marketing-bachelor-business-administration/ (sha256 04ed39ef8fcb)
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `fe5498cbc9268288` Saint Mary's College — degree_requirements 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-eighteenth-nineteenth-century [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
### `609e08ef920253cf` Saint Mary's College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.saintmarys.edu/admission-aid/transfer/transfer-requirements (sha256 726f06ae7433)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “As a general rule, college-level courses from an accredited institution that you received a grade of C or better in may be transferable.”
### `m330a8b3c0b68bc9` Taylor University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.taylor.edu/_docs/admissions/guidance-counselor-recommendation.pdf (sha256 4432a59b50a6)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 3, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “3.0 or higher grade point average”
  - per_credit_hour_charge: 50 ⟵ “Upon acceptance, pay the course tuition fee of $50 per credit hour.”
  - per_credit_hour_charge: 200 ⟵ “Tuition for high school and homeschool students is $200 per credit hour (50% less than the undergraduate rate). Take up to 24 credit hours at this discounted rate!”
  - eligibility_tier: 3.0 ⟵ “Limited to high school juniors and seniors who have at least a 3.0 grade point average, rank in the top 20% of their class,”
  - per_credit_hour_charge: 50 ⟵ “5. The course tuition fee of $50.00 per credit hour upon acceptance”
  - per_credit_hour_charge: 50 ⟵ “interterm or summer terms. Upon acceptance, a course tuition fee of $50.00 per credit hour will be charged.”
### `0b1a18b88acd0baf` University of Evansville — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.evansville.edu/student-financial-services/tuition-and-direct-costs-special-and-miscellaneous-fees-2026-2027.cfm (sha256 35298ff0e66c)
- checks: {"columns": 1, "rows": 4}
  - column:Co-op (per period): 465 ⟵ “Co-op (per period) | $465”
  - column:Late Registration: 205 ⟵ “Late Registration | $205”
  - column:Music Therapy Internship: 465 ⟵ “Music Therapy Internship | $465”
  - column:Tuition Exchange (per year): 300 ⟵ “Tuition Exchange (per year) | $300”
### `53e611b60220c5ec` University of Evansville — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.evansville.edu/admission/downloads/credits-ib.pdf (sha256 2e6fd950c565)
- checks: {"distinct_exams": 21, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|5]:  ⟵ “Social & Cultural Anthropology HL                  5           Anthropology 207               3”
  - equivalencies[IB-BIOLOGY-HL|5]:  ⟵ “Biology HL                                         5           Biology 107                    4”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|5]:  ⟵ “Business & Management HL                           5           ID 150                         3”
  - equivalencies[IB-CHEMISTRY-SL|5]:  ⟵ “Chemistry SL                                       5           Chemistry 100                  4”
  - equivalencies[IB-CHEMISTRY-HL|5]:  ⟵ “Chemistry HL                                       5           Chemistry 118                  4”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|6]:  ⟵ “Computer Science SL                                6           Computer Science 210           3”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|5]:  ⟵ “Computer Science HL                                5           Computer Science 210           3”
  - equivalencies[IB-ECONOMICS-HL|5]:  ⟵ “Economics HL                                       5           Economics 101-102              6”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French ab initio                              5           French 111                              3”
  - equivalencies[IB-FRENCH-SL|5]:  ⟵ “French B SL                                   5           French 111-112                          6”
  - equivalencies[IB-FRENCH-HL|5]:  ⟵ “French B HL                                   5           French 111-112-211                      9”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German ab initio                              5           German 111                              3”
  - equivalencies[IB-GERMAN-SL|5]:  ⟵ “German B SL                                   5           German 111-112                          6”
  - equivalencies[IB-GERMAN-HL|5]:  ⟵ “German B HL                                   5           German 111-112-211                      9”
  - equivalencies[IB-PHYSICS-HL|5]:  ⟵ “Physics HL                                   5           Physics 121-122                   8”
  - equivalencies[IB-PSYCHOLOGY-SL|6]:  ⟵ “Psychology SL                                6           Psychology 121                    3”
  - equivalencies[IB-PSYCHOLOGY-HL|5]:  ⟵ “Psychology HL                                5           Psychology 121-205                6”
  - equivalencies[IB-SPANISH|5]:  ⟵ “Spanish ab initio                            5           Spanish 111                       3”
  - equivalencies[IB-SPANISH-SL|5]:  ⟵ “Spanish B SL                                 5           Spanish 111-112                   6”
  - equivalencies[IB-SPANISH-HL|5]:  ⟵ “Spanish B HL                                 5           Spanish 111-112-211               9”
  - equivalencies[IB-THEATRE-HL|5]:  ⟵ “Theatre HL                                   5           Theatre 110                       3”
### `e4cbc9e34429e81b` University of Evansville — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.evansville.edu/admission/downloads/credits-table-advanced-placement-exam-2026.pdf (sha256 1c3651786f9f)
- checks: {"distinct_exams": 13, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Art: Drawing**                              4/5         Art 220 or Art Elective                            3”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Studio Art: 2D Design**                            4/5         Art 210 or Art Elective                            3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Studio Art: 3D Design                              4/5         Art Elective                                       3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                                         3          Art 105                                            3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                             3          Biology 100                                        4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                           3          Chemistry 100                                      4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French                                3     French 111-112             6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German                                3     German 111-112             6”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin                                 3     Latin 111-112              6”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language and Culture          3     Spanish 111-112            6”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3]:  ⟵ “Spanish Literature                   4/5    Elective                   3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB or BC                     3     Math 134                  3”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1                             3     Physics 100               3”
### `ec9033181e8ff55c` University of Notre Dame — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.nd.edu/costs-and-affordability/ (sha256 af72abb36932)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 69280 ⟵ “Tuition | $69,280”
  - column:Mandatory Fees: 514 ⟵ “Mandatory Fees | $514”
  - column:Housing and Food: 18992 ⟵ “Housing and Food | $18,992”
  - column:Books and Supplies: 1250 ⟵ “Books and Supplies | $1,250”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200”
  - column:Transportation: 750 ⟵ “Transportation | $750”
  - column:Total Estimated Cost: 91986 ⟵ “Total Estimated Cost | $91,986”
### `68f56bf80be75393` University of Saint Francis-Fort Wayne — awards 2026-27 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 d3f8da568d16)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $22,000 ⟵ “President’s Scholarship | $22,000 | 4.0”
  - gpa_requirement: 4.0 ⟵ “President’s Scholarship | $22,000 | 4.0”
### `6a5f20c1c6ecbfc2` University of Saint Francis-Fort Wayne — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 b64f9978f7fd)
- checks: {"thresholds": null}
  - award_amount_text: $15,000 ⟵ “St. Bonaventure Scholarship | $15,000 | <2.75”
  - gpa_requirement: <2.75 ⟵ “St. Bonaventure Scholarship | $15,000 | <2.75”
### `969fd8f3676119a4` University of Saint Francis-Fort Wayne — awards 2026-27 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 d3f8da568d16)
- checks: {"thresholds": {"gpa_min": 3.75}}
  - award_amount_text: $20,000 ⟵ “Trustee’s Scholarship | $20,000 | 3.75”
  - gpa_requirement: 3.75 ⟵ “Trustee’s Scholarship | $20,000 | 3.75”
### `986b023a2360eb88` University of Saint Francis-Fort Wayne — awards 2026-27 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 b64f9978f7fd)
- checks: {"thresholds": null}
  - award_amount_text: $13,000 ⟵ “St. Clare Scholarship | $13,000 | <2.5”
  - gpa_requirement: <2.5 ⟵ “St. Clare Scholarship | $13,000 | <2.5”
### `ad49589d14813b1f` University of Saint Francis-Fort Wayne — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 d3f8da568d16)
- checks: {"thresholds": {"gpa_min": 2.75}}
  - award_amount_text: $16,000 ⟵ “Achievement Scholarship | $16,000 | 2.75”
  - gpa_requirement: 2.75 ⟵ “Achievement Scholarship | $16,000 | 2.75”
### `b4a0da76acf8eb00` University of Saint Francis-Fort Wayne — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 d3f8da568d16)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - award_amount_text: $17,000 ⟵ “Dean’s Scholarship | $17,000 | 3.0”
  - gpa_requirement: 3.0 ⟵ “Dean’s Scholarship | $17,000 | 3.0”
### `c00c9ea2209d1305` University of Saint Francis-Fort Wayne — awards 2026-27 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 a51a77fdf3d4)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $14,000 ⟵ “St. Bonaventure Scholarship | $14,000 | 2.5”
  - gpa_requirement: 2.5 ⟵ “St. Bonaventure Scholarship | $14,000 | 2.5”
### `cf929e158ac9e043` University of Saint Francis-Fort Wayne — awards 2026-27 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 a51a77fdf3d4)
- checks: {"thresholds": {"gpa_min": 2.75}}
  - award_amount_text: $15,000 ⟵ “Achievement Scholarship | $15,000 | 2.75”
  - gpa_requirement: 2.75 ⟵ “Achievement Scholarship | $15,000 | 2.75”
### `d319ed57294dd023` University of Saint Francis-Fort Wayne — awards 2026-27 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 a51a77fdf3d4)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $18,000 ⟵ “Regent’s Scholarship | $18,000 | 3.5”
  - gpa_requirement: 3.5 ⟵ “Regent’s Scholarship | $18,000 | 3.5”
### `dd1050c1ffabfc4a` University of Saint Francis-Fort Wayne — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 a51a77fdf3d4)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $20,000 ⟵ “Regent’s Scholarship | $20,000 | 3.5”
  - gpa_requirement: 3.5 ⟵ “Regent’s Scholarship | $20,000 | 3.5”
### `e8fcfe3e5ac5bd69` University of Saint Francis-Fort Wayne — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 b64f9978f7fd)
- checks: {"thresholds": {"gpa_min": 3.75}}
  - award_amount_text: $22,000 ⟵ “Trustee’s Scholarship | $22,000 | 3.75”
  - gpa_requirement: 3.75 ⟵ “Trustee’s Scholarship | $22,000 | 3.75”
### `f440bbe78e67f835` University of Saint Francis-Fort Wayne — awards 2026-27 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 b64f9978f7fd)
- checks: {"thresholds": {"gpa_min": 3.25}}
  - award_amount_text: $17,000 ⟵ “Founder’s Scholarship | $17,000 | 3.25”
  - gpa_requirement: 3.25 ⟵ “Founder’s Scholarship | $17,000 | 3.25”
### `f7c8ed0d9bfa65c4` University of Saint Francis-Fort Wayne — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 b64f9978f7fd)
- checks: {"thresholds": {"gpa_min": 3.25}}
  - award_amount_text: $18,000 ⟵ “Founder’s Scholarship | $18,000 | 3.25”
  - gpa_requirement: 3.25 ⟵ “Founder’s Scholarship | $18,000 | 3.25”
### `f9309b331449c515` University of Saint Francis-Fort Wayne — awards 2026-27 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 a51a77fdf3d4)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - award_amount_text: $16,000 ⟵ “Dean’s Scholarship | $16,000 | 3.0”
  - gpa_requirement: 3.0 ⟵ “Dean’s Scholarship | $16,000 | 3.0”
### `feeb423410e79992` University of Saint Francis-Fort Wayne — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/undergraduate/scholarships/ (sha256 d3f8da568d16)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $24,000 ⟵ “President’s Scholarship | $24,000 | 4.0”
  - gpa_requirement: 4.0 ⟵ “President’s Scholarship | $24,000 | 4.0”
### `73da996e57daaffa` University of Saint Francis-Fort Wayne — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.sf.edu/about/offices-and-departments/the-registrars-office/transferring-to-saint-francis/advanced-placement-and-dual-credit/saint-francis-ap-course-equivalencies/ (sha256 fda7f15092d1)
- checks: {"distinct_exams": 40, "equivalencies": 40, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | IFC BEHSOC | 3 | ”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | IFC BEHSOC | 3 | ”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 131 | 4 | ”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH 223 | 4 | ”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MATH 223 & MATH 224 | 8 | ”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 141 & 142 | 8 | ”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | Elective | 3 | ”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | 3 | IFC BEHSOC | 3 | ”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CSCI 102 | 3 | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | CSCI 102 | 3 | ”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing | 3 | ART 107 | 3 | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | ENGL 110 | 3 | ”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | ENGL 206 | 3 | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVS 232 | 3 | ”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | GE History Elective | 3 | ”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | 3 | Elective | 3 | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture | 3 | Elective | 3 | ”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | IFC BEHSOC | 3 | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture | 3 | Elective | 3 | ”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture | 3 | Elective | 3 | ”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | 3 | LATN 141 | 3 | ”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | ECON 207 | 3 | ”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | ECON 208 | 3 | ”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | MUSC 136 | 3 | ”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C: Electricity and Magnetism | 3 | SCIE 258 | 4 | ”
  - … 15 more rows
### `9715ead9cd83ca44` University of Saint Francis-Fort Wayne — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.sf.edu/about/offices-and-departments/the-registrars-office/transferring-to-saint-francis/ (sha256 877f0e53bd0b)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “For Students Transferring to Saint Francis If you completed coursework at a regionally accredited institution, Saint Francis will evaluate and post the credits to your Saint Francis transcript, provided you earned a grade of “C” or better.”
### `a01d6aa6d751703e` University of Southern Indiana — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.usi.edu/registrar/transfer-credit/prior-learning-assessment (sha256 b5ae896c22a5)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 12 ⟵ “Graduate Studies may accept up to 12 credit hours of eligible graduate-level transfer credit for coursework completed at another regionally accredited college or university.”
### `m02f1be91151e7c7` Vincennes University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.vinu.edu/_resources/docs/pdf/project-excel/vu-dual-credit-policies-and-procedures-6-1-25.pdf (sha256 8f620f43f365)
- checks: {"fields": ["per_credit_hour_charges"], "merged_pages": 5, "tiers": 0}
  - per_credit_hour_charge: 100 ⟵ “The cost of the program is $100 per credit hour, making it an incredible value for students. In addition, textbooks are offered at”
  - per_credit_hour_charge: 25 ⟵ “●​   Courses taught by a VU-approved high school instructor: $25 per credit hour*”
  - per_credit_hour_charge: 75 ⟵ “●​   Courses taught by a VU adjunct: $75 per credit hour”
  - per_credit_hour_charge: 100 ⟵ “●​   Courses offered online: $100 per credit hour plus current textbook cost”
  - per_credit_hour_charge: 25 ⟵ “●​   Courses taught by a VU-approved high school instructor: $25 per credit hour*”
  - per_credit_hour_charge: 75 ⟵ “●​   Courses taught by a VU adjunct: $75 per credit hour”
  - per_credit_hour_charge: 100 ⟵ “●​   Courses offered online: $100 per credit hour plus current textbook cost”
  - per_credit_hour_charge: 25 ⟵ “Credit course one time; however, a $25 per credit hour fee applies for retakes, regardless of waiver”
  - per_credit_hour_charge: 25 ⟵ “Courses taught by a VU approved high school instructor: $25 per credit hour*”
  - per_credit_hour_charge: 75 ⟵ “Courses taught by a VU adjunct: $75 per credit hour”
  - per_credit_hour_charge: 75 ⟵ “Courses offered online: $75 per credit hour**”
  - per_credit_hour_charge: 25 ⟵ “Courses taught by a VU approved high school instructor: $25 per credit hour*”
### `07035ca034b005ea` Wabash College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.wabash.edu/admissions/finances/sources (sha256 0d0afeb0c651)
- checks: {"thresholds": null}
  - award_amount_text: Up to $10,000 added to amount received in scholarship grid above. Awards are annually renewable for 4 years. ⟵ “Snodell Scholarships | Up to $10,000 added to amount received in scholarship grid above. Awards are annually renewable for 4 years. | Complete application for admission. Complete the FAFSA by March 1, 2027. | Based on residence in Chicago, northern Illinois, southern Wisconsin, and eastern Iowa. Aca”
  - eligibility_summary: Based on residence in Chicago, northern Illinois, southern Wisconsin, and eastern Iowa. Academically qualified Federal Pell Grant recipients will receive grants to cover the balance of all tuition and fees not covered by government grants. ⟵ “Snodell Scholarships | Up to $10,000 added to amount received in scholarship grid above. Awards are annually renewable for 4 years. | Complete application for admission. Complete the FAFSA by March 1, 2027. | Based on residence in Chicago, northern Illinois, southern Wisconsin, and eastern Iowa. Aca”
### `3da0fdd211644b53` Wabash College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.wabash.edu/admissions/finances/sources (sha256 0d0afeb0c651)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 in addition to your merit scholarship. ⟵ “Early Decision Scholarship | $2,000 in addition to your merit scholarship. | Apply Early Decision to the College by November 15, 2026. | A holistic review of your academic achievements, including grade trend, strength of curriculum, test scores (if submitted), and class rank (if available).”
  - eligibility_summary: A holistic review of your academic achievements, including grade trend, strength of curriculum, test scores (if submitted), and class rank (if available). ⟵ “Early Decision Scholarship | $2,000 in addition to your merit scholarship. | Apply Early Decision to the College by November 15, 2026. | A holistic review of your academic achievements, including grade trend, strength of curriculum, test scores (if submitted), and class rank (if available).”
### `423f7efc114c8e2a` Wabash College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.wabash.edu/admissions/finances/sources (sha256 0d0afeb0c651)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 scholarship in addition to merit. ⟵ “File Your FAFSA | $1,000 scholarship in addition to merit. | Complete application for admission and file a FAFSA by April 15, 2026. | Must be admitted to the college. No additional selection criteria.”
  - eligibility_summary: Must be admitted to the college. No additional selection criteria. ⟵ “File Your FAFSA | $1,000 scholarship in addition to merit. | Complete application for admission and file a FAFSA by April 15, 2026. | Must be admitted to the college. No additional selection criteria.”
### `51e7ad85f16244a1` Wabash College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.wabash.edu/admissions/finances/sources (sha256 0d0afeb0c651)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 scholarship guaranteed (renewable for 4 yrs) with possibility of up to a full-tuition scholarship. ⟵ “Honors Scholarships | $3,000 scholarship guaranteed (renewable for 4 yrs) with possibility of up to a full-tuition scholarship. | Must apply for admission to the College by December 1, 2026. | Attend Scarlet Honors Weekend, December 4-5, 2026 OR February 21-22, 2027.”
  - eligibility_summary: Attend Scarlet Honors Weekend, December 4-5, 2026 OR February 21-22, 2027. ⟵ “Honors Scholarships | $3,000 scholarship guaranteed (renewable for 4 yrs) with possibility of up to a full-tuition scholarship. | Must apply for admission to the College by December 1, 2026. | Attend Scarlet Honors Weekend, December 4-5, 2026 OR February 21-22, 2027.”
### `66d9d71b31f28120` Wabash College — awards 2026-27 [new] (labeled_in_source)
- source: https://bulletin.wabash.edu/academic-policies/academic-honors-awards/ (sha256 e2ee71c536f8)
- checks: {"thresholds": null}
  - gpa_requirement: 3.600 and up ⟵ “Distinction | 3.600 and up | A.B. Summa Cum Laude”
### `970bb930e9db09d0` Wabash College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.wabash.edu/admissions/finances/sources (sha256 0d0afeb0c651)
- checks: {"thresholds": null}
  - award_amount_text: Tuition, standard fees, on-campus housing and food each year. More than $240,000 over four years. ⟵ “Wabash College Lilly Awards | Tuition, standard fees, on-campus housing and food each year. More than $240,000 over four years. | Apply for admission and submit the Lilly Award application by January 3, 2027. | Based on character, creativity, and academic accomplishment. Applicants must meet 1 out o”
  - eligibility_summary: Based on character, creativity, and academic accomplishment. Applicants must meet 1 out of 3 of following criteria to apply: a GPA of 3.5 (4.0 scale) rank within the top 10 percent of your senior class an SAT score of at least 1240 (EBR + M), or an ACT composite of 26 Finalists interviewed February 21-22, 2027. Please read the application carefully for all requirements. ⟵ “Wabash College Lilly Awards | Tuition, standard fees, on-campus housing and food each year. More than $240,000 over four years. | Apply for admission and submit the Lilly Award application by January 3, 2027. | Based on character, creativity, and academic accomplishment. Applicants must meet 1 out o”
### `a86dda8a7b447c5d` Wabash College — awards 2026-27 [new] (labeled_in_source)
- source: https://bulletin.wabash.edu/academic-policies/academic-honors-awards/ (sha256 e2ee71c536f8)
- checks: {"thresholds": null}
  - gpa_requirement: 3.600 and up ⟵ “High Pass | 3.600 and up | A.B. Magna Cum Laude”
### `ec04f62e364d6e2c` Wabash College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.wabash.edu/admissions/finances/sources (sha256 0d0afeb0c651)
- checks: {"thresholds": null}
  - award_tiers: [{'weightedhigh school gpa': '3.8+', 'amount_text': "$36,000–$39,000 PRESIDENT'S SCHOLARSHIP"}, {'weightedhigh school gpa': '3.25–3.79', 'amount_text': "$30,000–$33,000 DEAN'S SCHOLARSHIP"}, {'weightedhigh school gpa': '3.20–3.24', 'amount_text': 'up to $27,000 ALUMNI AWARD'}] ⟵ “weightedHigh School GPA |  || 3.8+ | $36,000–$39,000 PRESIDENT'S SCHOLARSHIP || 3.25–3.79 | $30,000–$33,000 DEAN'S SCHOLARSHIP || 3.20–3.24 | up to $27,000 ALUMNI AWARD”
  - gpa_requirement: Tiered by weightedHigh School GPA: 3.8+ → $36,000–$39,000 PRESIDENT'S SCHOLARSHIP; 3.25–3.79 → $30,000–$33,000 DEAN'S SCHOLARSHIP; 3.20–3.24 → up to $27,000 ALUMNI AWARD ⟵ “weightedHigh School GPA |  || 3.8+ | $36,000–$39,000 PRESIDENT'S SCHOLARSHIP || 3.25–3.79 | $30,000–$33,000 DEAN'S SCHOLARSHIP || 3.20–3.24 | up to $27,000 ALUMNI AWARD”
### `f43841e9e917d38f` Wabash College — awards 2026-27 [new] (labeled_in_source)
- source: https://bulletin.wabash.edu/academic-policies/academic-honors-awards/ (sha256 e2ee71c536f8)
- checks: {"thresholds": null}
  - gpa_requirement: 3.800 and up ⟵ “Pass | 3.800 and up | A.B. Magna Cum Laude”
### `726db22411a466cb` Wabash College — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://bulletin.wabash.edu/academic-policies/transfer-credit/ (sha256 c4a1204ec09a)
- checks: {"distinct_exams": 6, "equivalencies": 6, "rows_without_score": 0}
  - equivalencies[IB-CHEMISTRY|5, 6, 7]:  ⟵ “Chemistry | 5, 6, 7 | CHE-111 upon completion of CHE-111 labs at Wabash | 1”
  - equivalencies[IB-ECONOMICS|5, 6, 7]:  ⟵ “Economics | 5, 6, 7 | ECO-101 | 1”
  - equivalencies[IB-HISTORY|5, 6, 7]:  ⟵ “History - Americas | 5, 6, 7 | HIS-200 | 1”
  - equivalencies[IB-SPANISH|5, 6, 7]:  ⟵ “Spanish | 5, 6, 7 | SPA-101 | 1”
  - equivalencies[IB-PHYSICS|5, 6, 7]:  ⟵ “Physics | 5, 6, 7 | PHY-111 upon completion of PHY-111 labs at Wabash | 1”
  - equivalencies[IB-PSYCHOLOGY|5, 6, 7]:  ⟵ “Psychology | 5, 6, 7 | Psychology elective, or PSY-101 if the student takes a 200 level Psychology course and earns a B- or higher | 1”
### `bec343309f12e3ef` Wabash College — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://bulletin.wabash.edu/academic-policies/transfer-credit/ (sha256 c4a1204ec09a)
- checks: {"distinct_exams": 21, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4, 5]:  ⟵ “African American Studies | 4, 5 | Black Studies elective | 1”
  - equivalencies[AP-ART-HISTORY|4, 5]:  ⟵ “Art History | 4, 5 | ART-101 | 1”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | 5 | Non-lab elective | 1”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “Calculus AB | 4, 5 | MAT-111 | 1”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC | 4, 5 | MAT-111 and MAT-112 | 2”
  - equivalencies[AP-CHEMISTRY|4, 5]:  ⟵ “Chemistry | 4, 5 | Non-lab elective | 1”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4, 5]:  ⟵ “Computer Science A | 4, 5 | CSC-111 | 1”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4, 5]:  ⟵ “Computer Science Principles | 4, 5 | CSC-101 | 1”
  - equivalencies[AP-MACROECONOMICS|4, 5]:  ⟵ “Economics - Micro & Macro (must take both) | 4, 5 | ECO-101 | 1”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4, 5]:  ⟵ “English Language/Composition | 4, 5 | Language Studies elective | 1”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4, 5]:  ⟵ “English Literature/Composition | 4, 5 | Literature elective | 1”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4, 5]:  ⟵ “Environmental Science | 4, 5 | Non-lab elective | 1”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4, 5]:  ⟵ “French Language | 4, 5 | FRE-101 | 1”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4, 5]:  ⟵ “German Language | 4, 5 | GER-101 | 1”
  - equivalencies[AP-MUSIC-THEORY|4, 5]:  ⟵ “Music Theory | 4, 5 | MUS-130 | 1”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4, 5]:  ⟵ “Physics 1 OR Physics C (Mechanics) | 4, 5 | PHY-177 (non-lab), or PHY-109 if the student completes the labs for PHY-109 at Wabash | 1”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4, 5]:  ⟵ “Physics 2 OR Physics C (Electricity & Magnetism) | 4, 5 | PHY-178 (non-lab), or PHY-110 if the student completes the labs for PHY-110 at Wabash | 1”
  - equivalencies[AP-PRECALCULUS|4, 5]:  ⟵ “Precalculus | 4, 5 | MAT-100 | 1”
  - equivalencies[AP-PSYCHOLOGY|4, 5]:  ⟵ “Psychology | 4, 5 | Psychology elective, or PSY-101 if the student takes a 200 level Psychology course (other than PSY-201) and earns a B- or higher. Exam credit or back credit cannot be applied to a major or minor in Psychology. | 1”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|4, 5]:  ⟵ “Spanish Language | 4, 5 | SPA-101 | 1”
  - equivalencies[AP-STATISTICS|4, 5]:  ⟵ “Statistics | 4, 5 | MAT-103, MAT-104 | 1 (0.5 for MAT-103 and 0.5 for MAT-104)”
### `a186d8c55cea7aed` Wabash College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://bulletin.wabash.edu/academic-policies/transfer-credit/transfer-credit.pdf (sha256 5b1df7a9f4f2)
- checks: {"fields": ["min_grade"]}
  - min_grade: B- ⟵ “Credit is including transfer credit, Course Share credit, and credit by examination awarded upon earning a grade of B- or higher in the Wabash course. other than Wabash exams — may apply toward a Wabash degree.”

## Exceptions (343)

### `626cc7113d7c19b1` Ball State University — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships (sha256 8011541cff17)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “A dependency override does not guarantee an adjustment will be made to your aid package.”
### `650c3acaa2b6b7c9` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/types/scholarships/scholarship-appeals-for-returning-students (sha256 2b0035154680)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You can access the scholarship appeal form and instructions here.”
### `6650e53cc5f36ead` Ball State University — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships (sha256 8011541cff17)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 16}
  - sentence: need_based_special_circumstances ⟵ “Special and Unusual Circumstances We recognize that the FAFSA may not always accurately reflect your financial situation and/or dependency status.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations that justify an aid administrator adjusting data elements in the Cost of Attendance or in the EFC calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation, more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Special Circumstance Requests will be considered after you receive your initial award notification for the current aid year.”
  - sentence: need_based_special_circumstances ⟵ “After reviewing your special circumstance documentation, your aid package may remain the same, be increased, or reduced according to the financial information that has been submitted.”
### `77b001b6281a65ad` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans (sha256 61c5bd34af1f)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `85e995e9a7166f65` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview (sha256 2e6244321f17)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `8c9fa87330f819c4` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview (sha256 2e6244321f17)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Any cost of attendance adjustment may require the return of loan funds or the necessity to repay other types of assistance already received.”
### `a1c6937d73084172` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility (sha256 d34a71c57c6a)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `c2b28510156a3783` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility (sha256 d34a71c57c6a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If the student regains pace prior to the next evaluation period, they must submit a satisfactory academic progress appeal in order to have their eligibility reviewed.”
  - sentence: sap_appeal ⟵ “Select "Satisfactory Academic Progress Appeal" in the "Start a New Request" section.”
### `c4302cecedfdffd3` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances (sha256 c86dedfbd2f5)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Contact Our Office Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `e350ec78cd744ceb` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure (sha256 1a2d40805624)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `16292e8cab7ed765` Ball State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bsu.edu/admissions/tuition-and-fees (sha256 e768198276b0)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 16}
  - column:Tuition: 8948 ⟵ “Tuition | $8,948”
  - column:Student Services Fee: 0 ⟵ “Student Services Fee | $0”
  - column:Health Fee: 0 ⟵ “Health Fee | $0”
  - column:University Technology Fee: 300 ⟵ “University Technology Fee | $300”
  - column:Recreation Center Fee: 0 ⟵ “Recreation Center Fee | $0”
  - column:Online Fees: 600 ⟵ “Online Fees | $600”
  - column:Course Fees: 160 ⟵ “Course Fees | 160”
  - column:Books and Supplies: 782 ⟵ “Books and Supplies | $782”
  - column:Living Expenses (Housing and Food): 12832 ⟵ “Living Expenses (Housing and Food) | $12,832”
  - column:Transportation: 436 ⟵ “Transportation | $436”
  - column:Personal/Miscellaneous: 2366 ⟵ “Personal/Miscellaneous | $2,366”
  - column:Total Standard Cost of Attendance: 26424 ⟵ “Total Standard Cost of Attendance | $26,424”
  - column:Direct Loan Fees: 68 ⟵ “Direct Loan Fees | $68”
  - column:Total Tuition and Fees: 10008 ⟵ “Total Tuition and Fees | $10,008”
  - column:Total Books to Personal: 16416 ⟵ “Total Books to Personal | $16,416”
  - column:Total with Direct Loan Fees: 26492 ⟵ “Total with Direct Loan Fees | $26,492”
### `206c3006c18020ac` Bethel University — appeals 2026-27 [new] (labeled_in_source)
- source: https://betheluniversity.edu/admissions-aid/scholarships-and-aid/grants/pilot-promise/ (sha256 40b84a8d89fa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If your family’s circumstances have changed, such as job loss, death of parent/spouse, or change in parent’s marital status, please contact the Financial Aid Office to review for a professional judgment review.”
### `6579cf19a5be98ae` Bethel University — appeals 2026-27 [new] (source_unlabeled)
- source: https://betheluniversity.edu/admissions-aid/scholarships-and-aid/faqs/ (sha256 1b4ec5423e20)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If, after a semester on SAP Warning, the student does not make SAP, he or she will lose any Title IV eligibility and must submit a SAP Appeal.”
  - sentence: sap_appeal ⟵ “In order to regain eligibility the student must submit an SAP Appeal and it must be approved/granted by the financial aid committee.”
  - sentence: sap_appeal ⟵ “If a student reenrolls at Bethel University after a status of SAP Unmet, he or she has the option to submit a SAP appeal, if the limit of two appeals has not been reached.”
  - sentence: sap_appeal ⟵ “SAP Status | Status | Description | Duration | Title IV Eligibility | Notification | SAP Met | Qualitative and quantitative measure met | Applicable as long as standards are met | Yes | None | SAP Warning | Qualitative and/or quantitative measure not met | One term | Yes | Letter | SAP Probation | Appeal submitted and after review, approved | One term | Yes | Letter | SAP Unmet | Qualitative and/o”
### `254d11f739c1d268` Butler University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/financial-aid-scholarships/handbook/ (sha256 3566feaf5dc1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “The appeal must be in writing on the SAP Appeal Form provided by the Office of Financial Aid.”
  - sentence: sap_appeal ⟵ “SAP Appeal Form Regaining Eligibility Students who failed to meet these Satisfactory Academic Progress Standards and who choose to enroll without benefit of student financial aid may request a review of their academic record after any term in which they are enrolled without the receipt of financial aid.”
### `30e68c5a5a6f0889` Butler University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.butler.edu/admission-aid/financial-aid-scholarships/heerf/ (sha256 a8d7d06b49c2)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.butler.edu/admission-aid/financial-aid-scholarships/emergency-fund/,https://www.butler.edu/admission-aid/financial-aid-scholarships/fafsa/,https://www.butler.edu/admission-aid/financial-aid-scholarships/faqs/,https://www.butler.edu/admission-aid/financial-aid-scholarships/financial-aid-cycle/,https://www.butler.edu/admission-aid/financial-aid-scholarships/handbook/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Reminded students to contact the Office of Financial Aid about a special circumstance if COVID-19 has caused a job loss.”
### `4c91f681585cec69` Butler University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.butler.edu/admission-aid/financial-aid-scholarships/heerf/ (sha256 a8d7d06b49c2)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “HEERF III Resources & Communications Website butler.edu/financial-aid/heerf – HEERF III Information and Reporting Communications Award Recipients Student receives personalized email with award amount Email includes reminder that student can request review for professional judgement.”
  - sentence: professional_judgment ⟵ “Letter includes reminder that student can request review for professional judgement.”
  - sentence: professional_judgment ⟵ “Professional judgement communication Postcard was mailed to all 21–22 FAFSA filers on October 8, 2021.”
### `88d83411ff595734` Butler University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/financial-aid-scholarships/handbook/ (sha256 3566feaf5dc1)
- issues: semantic_review_required, conflicting_sources:https://www.butler.edu/admission-aid/financial-aid-scholarships/emergency-fund/,https://www.butler.edu/admission-aid/financial-aid-scholarships/fafsa/,https://www.butler.edu/admission-aid/financial-aid-scholarships/faqs/,https://www.butler.edu/admission-aid/financial-aid-scholarships/financial-aid-cycle/,https://www.butler.edu/admission-aid/financial-aid-scholarships/heerf/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Open If a significant loss of income is projected resulting in circumstances that restrict your parents’ ability to contribute to your education, please write a letter explaining the circumstances and the Office of Financial Aid will review your situation.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are defined as situations that the family has minimal control over: death, disability, loss of income due to lay-off and unemployment.”
  - sentence: need_based_special_circumstances ⟵ “Additional aid for special circumstances will consist of increased loan eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Application for loans and payment plans must not be delayed while waiting for a decision on a special circumstance.”
### `ba3ec9b5e9a21a82` Butler University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.butler.edu/admission-aid/financial-aid-scholarships/fafsa/ (sha256 daba480d27e6)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.butler.edu/admission-aid/financial-aid-scholarships/emergency-fund/,https://www.butler.edu/admission-aid/financial-aid-scholarships/faqs/,https://www.butler.edu/admission-aid/financial-aid-scholarships/financial-aid-cycle/,https://www.butler.edu/admission-aid/financial-aid-scholarships/handbook/,https://www.butler.edu/admission-aid/financial-aid-scholarships/heerf/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Contact the Office of Financial Aid if you have special circumstances not reflected on the FAFSA.”
### `d1a9d36c6e4887f7` Butler University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/financial-aid-scholarships/financial-aid-cycle/ (sha256 210c75609462)
- issues: semantic_review_required, conflicting_sources:https://www.butler.edu/admission-aid/financial-aid-scholarships/emergency-fund/,https://www.butler.edu/admission-aid/financial-aid-scholarships/fafsa/,https://www.butler.edu/admission-aid/financial-aid-scholarships/faqs/,https://www.butler.edu/admission-aid/financial-aid-scholarships/handbook/,https://www.butler.edu/admission-aid/financial-aid-scholarships/heerf/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Identify Special or Unusual Circumstances If a student or family anticipates a significant loss of income after filing the FAFSA, the Office of Financial Aid can review the situation and determine if a formal review of financial aid is warranted.”
### `f456d0137a29b3bf` Butler University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/financial-aid-scholarships/emergency-fund/ (sha256 72339a985b3a)
- issues: semantic_review_required, conflicting_sources:https://www.butler.edu/admission-aid/financial-aid-scholarships/fafsa/,https://www.butler.edu/admission-aid/financial-aid-scholarships/faqs/,https://www.butler.edu/admission-aid/financial-aid-scholarships/financial-aid-cycle/,https://www.butler.edu/admission-aid/financial-aid-scholarships/handbook/,https://www.butler.edu/admission-aid/financial-aid-scholarships/heerf/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Our team will carefully evaluate your situation, which may include exploring options like a special circumstance appeal, reviewing federal loan eligibility, or connecting you with additional financial guidance to help keep you on track to graduate.”
### `fd64de107562af5f` Butler University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/financial-aid-scholarships/faqs/ (sha256 2883f5bf5bb4)
- issues: semantic_review_required, conflicting_sources:https://www.butler.edu/admission-aid/financial-aid-scholarships/emergency-fund/,https://www.butler.edu/admission-aid/financial-aid-scholarships/fafsa/,https://www.butler.edu/admission-aid/financial-aid-scholarships/financial-aid-cycle/,https://www.butler.edu/admission-aid/financial-aid-scholarships/handbook/,https://www.butler.edu/admission-aid/financial-aid-scholarships/heerf/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you believe you have unusual circumstances that prevent you from listing parent information on the FAFSA, you may request treatment as a provisional independent student when completing the FAFSA.”
### `3c49eef9a8d3db75` Butler University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/tuition-costs/ (sha256 22d87d992695)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition:: 48900 ⟵ “Tuition: | $48,900”
  - column:Estimated Housing and Food:: 17090 ⟵ “Estimated Housing and Food: | $17,090*”
  - column:Fees:: 990 ⟵ “Fees: | $990”
  - column:Total Direct Costs:: 66980 ⟵ “Total Direct Costs: | $66,980”
### `4df4ab45e53b54e7` Butler University — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/tuition-costs/ (sha256 22d87d992695)
- issues: stale_year_label:2023-24
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition:: 44990 ⟵ “Tuition: | $44,990”
  - column:Estimated Housing and Food:: 15870 ⟵ “Estimated Housing and Food: | $15,870*”
  - column:Fees:: 990 ⟵ “Fees: | $990”
  - column:Total Direct Costs:: 61850 ⟵ “Total Direct Costs: | $61,850”
### `ce05e4ce52dac1b9` Butler University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.butler.edu/founders/admission-and-aid/tuition-scholarships-and-financial-aid/ (sha256 e4a1b07b449f)
- issues: conflicting_sources:https://www.butler.edu/admission-aid/tuition-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition: 17000 ⟵ “Tuition | $17,000”
  - column:Fees: 990 ⟵ “Fees | $990”
  - column:Total Direct Costs: 17990 ⟵ “Total Direct Costs | $17,990”
### `df4cb71641cc1f5e` Butler University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/tuition-costs/ (sha256 22d87d992695)
- issues: conflicting_sources:https://www.butler.edu/founders/admission-and-aid/tuition-scholarships-and-financial-aid/
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition:: 50860 ⟵ “Tuition: | $50,860”
  - column:Estimated Housing and Food:: 17730 ⟵ “Estimated Housing and Food: | $17,730*”
  - column:Fees:: 990 ⟵ “Fees: | $990”
  - column:Total Direct Costs:: 69580 ⟵ “Total Direct Costs: | $69,580”
### `e7ccd2428c4060c1` Butler University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/tuition-costs/ (sha256 22d87d992695)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition:: 46570 ⟵ “Tuition: | $46,570”
  - column:Estimated Housing and Food:: 16430 ⟵ “Estimated Housing and Food: | $16,430*”
  - column:Fees:: 990 ⟵ “Fees: | $990”
  - column:Total Direct Costs:: 63990 ⟵ “Total Direct Costs: | $63,990”
### `f9ba7465c084f15c` Butler University — costs 2022-23 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.butler.edu/admission-aid/tuition-costs/ (sha256 22d87d992695)
- issues: stale_year_label:2022-23
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition:: 43470 ⟵ “Tuition: | $43,470”
  - column:Estimated Housing and Meals:: 15260 ⟵ “Estimated Housing and Meals: | $15,260*”
  - column:Fees:: 990 ⟵ “Fees: | $990”
  - column:Total Direct Costs:: 59720 ⟵ “Total Direct Costs: | $59,720”
### `192ee2476de638f6` Calumet College of Saint Joseph — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.ccsj.edu/admissions/financial-aid/ (sha256 133a8c7d56d2)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “CCSJ does not package or disburse financial aid or process special circumstances (professional judgements) prior to verification completion.”
### `6b62733eb845d2fa` Calumet College of Saint Joseph — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ccsj.edu/admissions/financial-aid/sap-appeal-form/ (sha256 7c86e9ae0fd0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeal Form - Calumet College of St.”
### `d45a2391abd0b721` Calumet College of Saint Joseph — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.ccsj.edu/admissions/financial-aid/ (sha256 133a8c7d56d2)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “SAP Appeal Process Upon completion of a warning term for students who still have GPA or Pace issues, and in rare instances where there are maximum timeframe issues, students will meet with their Academic Advisor to discuss their options to remain at CCSJ.”
  - sentence: sap_appeal ⟵ “Student will print and sign/date the appeal form and deliver via email or in person the full SAP appeal packet containing the signed/dated appeal and documentation to support the statements made in their appeal form.”
  - sentence: sap_appeal ⟵ “Students will have 2 opportunities to file a SAP appeal over their lifetime at CCSJ.”
  - sentence: sap_appeal ⟵ “An appeal cannot be approved for the same reason multiple times. https://www.ccsj.edu/admissions/financial-aid/sap-appeal-form/ Remember to file your FAFSA!”
### `e1e4ba09baf188f8` Calumet College of Saint Joseph — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.ccsj.edu/admissions/financial-aid/ (sha256 133a8c7d56d2)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “The estimate is subject to the accuracy of the information you provide, may change if financial or family characteristics change, and does not incorporate any special circumstances, which are reviewed after you officially apply for aid.”
  - sentence: need_based_special_circumstances ⟵ “Your Senior Year Tuition Paid In Full The Calumet Commitment SPECIAL CIRCUMSTANCES VERIFICATION SATISFACTORY ACADEMIC PROGRESS SPECIAL CIRCUMSTANCES If you or your family have encountered personal or financial hardships that were not accurately reflected at the time you filled out your FAFSA, our Financial Aid Department can review your file for consideration of special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Below are examples of situations that are considered to be special circumstances: Loss or reduction of employment, wages, or unemployment compensation Loss of untaxed income or benefits e.g.”
  - sentence: need_based_special_circumstances ⟵ “Social Security benefits or child support Separation or divorce Death of a student’s parent (or independent student’s spouse) Unusual expenses (such as medical costs) If you feel you have an extreme situation that may allow for a Special Circumstances Review, visit the campus Financial Aid Office to determine if you should complete the Special Circumstances Review Form.”
  - sentence: need_based_special_circumstances ⟵ “For financial aid purposes, a student is considered “dependent” if he or she is under 24, unmarried, and has no legal dependents at the time the Free Application for Federal Student Aid is submitted. (Exceptions are made for veterans, wards of court, and other special circumstances.) If a student is considered dependent, then the income and the assets of the parent have to be reported on the FAFSA”
### `4b2924cfab35388b` DePauw University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.depauw.edu/admission-aid/scholarships-aid/policies-and-procedures/ (sha256 6bb1c2750823)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals of Suspensions Students who are suspended for failing to meet SAP guidelines may appeal their suspension in writing to the Academic Standing Committee, which includes representatives from the faculty, Academic Affairs, Student Affairs and Financial Aid.”
### `699a77706e801e47` DePauw University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.depauw.edu/admission-aid/scholarships-aid/apply-for-aid/current-students/ (sha256 1fc9d7bc8608)
- issues: semantic_review_required, conflicting_sources:https://www.depauw.edu/admission-aid/scholarships-aid/policies-and-procedures/,https://www.depauw.edu/admission-aid/scholarships-aid/types-of-aid/grants/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If special circumstances prevent you from meeting these deadlines, please contact the Financial Aid Office.”
### `78c31ac4a822e652` DePauw University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.depauw.edu/admission-aid/scholarships-aid/policies-and-procedures/ (sha256 6bb1c2750823)
- issues: semantic_review_required, conflicting_sources:https://www.depauw.edu/admission-aid/scholarships-aid/apply-for-aid/current-students/,https://www.depauw.edu/admission-aid/scholarships-aid/types-of-aid/grants/
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Students and their families may face situations where the original application information does not accurately reflect their current circumstances and ability to pay for college.”
  - sentence: need_based_special_circumstances ⟵ “Students may submit a special circumstances request by emailing financialaid@depauw.edu and detailing your family's extenuating circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances: Dependent or Independent?”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student's dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration), more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Students with unusual circumstances should contact the financial aid office at financialaid@depauw.edu or 765-658-4030.”
  - sentence: need_based_special_circumstances ⟵ “The student will be put in touch with their financial aid counselor to review their unusual circumstance.”
### `b1a1534bf3648d8a` DePauw University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.depauw.edu/admission-aid/scholarships-aid/types-of-aid/grants/ (sha256 283971c897d0)
- issues: semantic_review_required, conflicting_sources:https://www.depauw.edu/admission-aid/scholarships-aid/apply-for-aid/current-students/,https://www.depauw.edu/admission-aid/scholarships-aid/policies-and-procedures/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Grants are typically the same from year to year, although they may fluctuate if there are significant changes to family circumstances (such as a change in income, etc.).”
### `2cbf9662027f9546` DePauw University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.depauw.edu/admission-aid/scholarships-aid/tuition-and-fees/ (sha256 9677c9418815)
- issues: conflicting_sources:https://www.depauw.edu/academics/catalog/tuition-fees-and-expenses/,https://www.depauw.edu/offices/finance-administration/student-and-parent-information/payment-services/tuition-and-fees/
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 62710 ⟵ “Tuition | $62,710”
  - column:Housing and meals: 16240 ⟵ “Housing and meals | $16,240”
  - column:Mandatory fees: 1170 ⟵ “Mandatory fees | $1,170”
  - column:Total direct expenses: 80120 ⟵ “Total direct expenses | $80,120”
### `a1af2d55826e76bf` DePauw University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.depauw.edu/offices/finance-administration/student-and-parent-information/payment-services/tuition-and-fees/ (sha256 fbe78569eb2f)
- issues: arrangement_unlabeled, conflicting_sources:https://www.depauw.edu/academics/catalog/tuition-fees-and-expenses/,https://www.depauw.edu/admission-aid/scholarships-aid/tuition-and-fees/
- checks: {"columns": 2, "components_reconcile": true, "rows": 5}
  - column:Total Cost of Attendance: 77220 ⟵ “Total Cost of Attendance | $77,220 | $80,120”
  - column:Tuition: 60310 ⟵ “Tuition | $60,310 | $62,710”
  - column:Housing: 8116 ⟵ “Housing | $8,116 | $8,390”
  - column:Meals(18-swipe plan): 7674 ⟵ “Meals(18-swipe plan) | $7,674 | $7,850”
  - column:Comprehensive Fee: 1120 ⟵ “Comprehensive Fee | $1,120 | $1,170”
  - column:Total Cost of Attendance: 80120 ⟵ “Total Cost of Attendance | $77,220 | $80,120”
  - column:Tuition: 62710 ⟵ “Tuition | $60,310 | $62,710”
  - column:Housing: 8390 ⟵ “Housing | $8,116 | $8,390”
  - column:Meals(18-swipe plan): 7850 ⟵ “Meals(18-swipe plan) | $7,674 | $7,850”
  - column:Comprehensive Fee: 1170 ⟵ “Comprehensive Fee | $1,120 | $1,170”
### `b58bb8ec41c4a6ff` DePauw University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.depauw.edu/academics/catalog/tuition-fees-and-expenses/ (sha256 32c4324d8f6f)
- issues: conflicting_sources:https://www.depauw.edu/admission-aid/scholarships-aid/tuition-and-fees/,https://www.depauw.edu/offices/finance-administration/student-and-parent-information/payment-services/tuition-and-fees/
- checks: {"columns": 1, "rows": 3}
  - column:Tuition, per semester (including Winter Term in Semester I or May Term in Semester II): 31355.0 ⟵ “Tuition, per semester (including Winter Term in Semester I or May Term in Semester II) | $31,355.00”
  - column:Room in residence halls and alternative housing (per semester): 4196.0 ⟵ “Room in residence halls and alternative housing (per semester) | $4,196.00”
  - column:Board (meal plan) (per semester): 3924.0 ⟵ “Board (meal plan) (per semester) | $3,924.00”
### `33f1e11a9d1f9bc1` Earlham College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.earlham.edu/financial-aid-satisfactory-academic-progress-sap (sha256 83bc46825380)
- issues: semantic_review_required, conflicting_sources:https://earlham.edu/wp-content/uploads/2025/11/20080_FinancialAidForms_2026-27_RequestForReview.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The student may appeal that result on the basis of injury or illness, the death of a relative, or other special circumstances.”
### `510c9c35e3bb3070` Earlham College — appeals 2026-27 [new] (labeled_in_title)
- source: https://earlham.edu/wp-content/uploads/2025/11/20080_FinancialAidForms_2026-27_RequestForReview.pdf (sha256 c4ec1ed964db)
- issues: semantic_review_required, conflicting_sources:https://catalog.earlham.edu/financial-aid-satisfactory-academic-progress-sap
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “EARLHAM COLLEGE 2026-27 FINANCIAL AID REQUEST FOR REVIEW OF FINANCIAL AID AWARD If you have unusual circumstances, please complete this form and submit it to our office with the specified documentation.”
  - sentence: need_based_special_circumstances ⟵ “Please complete the section(s) that most closely describe(s) your unusual circumstances.”
### `babe552f59472ff1` Earlham College — appeals 2025-26 [new] (labeled_in_title)
- source: https://earlham.edu/wp-content/uploads/2025/11/20080_FinancialAidForms_2025-26_RequestForReview.pdf (sha256 3cb3496d68c3)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “EARLHAM COLLEGE 2025-26 FINANCIAL AID REQUEST FOR REVIEW OF FINANCIAL AID AWARD If you have unusual circumstances, please complete this form and submit it to our office with the specified documentation.”
  - sentence: need_based_special_circumstances ⟵ “Please complete the section(s) that most closely describe(s) your unusual circumstances.”
### `68cd037bffc83206` Earlham College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.earlham.edu/academic-catalog-2026-27/2026-2027-tuition-and-fees (sha256 38ad532877eb)
- issues: conflicting_sources:https://earlham.edu/cost-affordability/tuition-and-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 56784 ⟵ “Tuition | $56,784”
  - column:Room: 8300 ⟵ “Room | $8,300”
  - column:Board: 7462 ⟵ “Board | $7,462”
  - column:Fees: 980 ⟵ “Fees | $980”
  - column:Total: 73526 ⟵ “Total | $73,526”
### `8116d0011b652791` Earlham College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://earlham.edu/cost-affordability/tuition-and-costs/ (sha256 adbf5a18c701)
- issues: conflicting_sources:https://catalog.earlham.edu/academic-catalog-2026-27/2026-2027-tuition-and-fees
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - on_campus:Tuition: 56784 ⟵ “Tuition | $56,784”
  - on_campus:Housing: 8300 ⟵ “Housing | $8,300”
  - on_campus:Meal Plan: 7462 ⟵ “Meal Plan | $7,462”
  - on_campus:Fees: 980 ⟵ “Fees | $980”
  - on_campus:Total: 73526 ⟵ “Total | $73,526”
### `87bdfa56849ac3cd` Earlham College — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.earlham.edu/academic-catalog-2026-27/transferring-credits (sha256 8538d400eb8a)
- issues: credits_implausible, score_scale_mismatch
- checks: {"distinct_exams": 36, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|4, 5]:  ⟵ “2-D Art and Design | 4, 5 | 3 | Elective”
  - equivalencies[AP-3-D-ART-DESIGN|4, 5]:  ⟵ “3-D Art and Design | 4, 5 | 3 | Elective”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4, 5]:  ⟵ “African American Studies | 4, 5 | 3 | AAAS 368 or AAAS 369”
  - equivalencies[AP-ART-HISTORY|45]:  ⟵ “Art History | 45 | 36 | Elective”
  - equivalencies[AP-BIOLOGY|45]:  ⟵ “Biology | 45 | 36 | Elective”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “Calculus AB * | 4, 5 | 3 | Elective”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC * | 4, 5 | 6 | MATH 180”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC: AB Subscore * | 4, 5 | 3 | Elective”
  - equivalencies[AP-CHEMISTRY|45]:  ⟵ “Chemistry | 45 | 36 | CHEM 111”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|45]:  ⟵ “Chinese Language and Culture | 45 | 36 | Elective”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|4, 5]:  ⟵ “Comparative Government and Politics | 4, 5 | 3 | Elective”
  - equivalencies[AP-COMPUTER-SCIENCE-A|45]:  ⟵ “Computer Science A | 45 | 36 | Consult Department Convener”
  - equivalencies[AP-DRAWING|4, 5]:  ⟵ “Drawing | 4, 5 | 3 | Elective”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|45]:  ⟵ “English Language and Composition | 45 | 36 | Elective”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|45]:  ⟵ “English Literature and Composition | 45 | 36 | Elective”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4, 5]:  ⟵ “Environmental Science | 4, 5 | 3 | Consult Department Convener”
  - equivalencies[AP-EUROPEAN-HISTORY|45]:  ⟵ “European History | 45 | 36 | Elective”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|45]:  ⟵ “French Language and Culture | 45 | 36 | Elective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|45]:  ⟵ “German Language and Culture | 45 | 36 | Elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4, 5]:  ⟵ “Human Geography | 4, 5 | 3 | Elective”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|45]:  ⟵ “Italian Language and Culture | 45 | 36 | Elective”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|45]:  ⟵ “Japanese Language and Culture | 45 | 36 | Elective”
  - equivalencies[AP-LATIN|45]:  ⟵ “Latin | 45 | 36 | Elective”
  - equivalencies[AP-MACROECONOMICS|4, 5]:  ⟵ “Macroeconomics | 4, 5 | 3 | ECON 101”
  - equivalencies[AP-MICROECONOMICS|4, 5]:  ⟵ “Microeconomics | 4, 5 | 3 | ECON 103”
  - … 12 more rows
### `3fb7ae7ab4d9b7e4` Grace College and Theological Seminary — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.grace.edu/admissions/financial-aid-scholarships/ (sha256 873e6c4e00c9)
- issues: semantic_review_required, conflicting_sources:https://connect.grace.edu/register/?id=8e709766-fe65-4d9e-90d0-44ea1f066966,https://www.grace.edu/admissions/financial-aid-scholarships/,https://www.grace.edu/admissions/financial-aid-scholarships/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances will be reviewed on an individual basis when they are submitted in writing.”
  - sentence: need_based_special_circumstances ⟵ “Graduate Scholarship Search Special Circumstances PJ Advisor Student Connections Questions?”
### `46b777fd951c91bc` Grace College and Theological Seminary — appeals 2026-27 [new] (source_unlabeled)
- source: https://connect.grace.edu/register/?id=8e709766-fe65-4d9e-90d0-44ea1f066966 (sha256 e041bfcbf854)
- issues: semantic_review_required, conflicting_sources:https://www.grace.edu/admissions/financial-aid-scholarships/,https://www.grace.edu/admissions/financial-aid-scholarships/,https://www.grace.edu/admissions/financial-aid-scholarships/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Request This website uses resources that are being blocked by your network.”
  - sentence: need_based_special_circumstances ⟵ “Request for Additional Financial Aid Due to Special Circumstances You have indicated that you have special circumstances that could not be included on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “Instructions Click here to download the Special Circumstances form to your device.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form* Letter of Explanation* Supporting Documentation* (optional) Supporting Documentation (optional) Supporting Documentation STEP 3: Submit your documentation below.”
### `5d7f56a84f50a52c` Grace College and Theological Seminary — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.grace.edu/admissions/financial-aid-scholarships/ (sha256 921c31f6a312)
- issues: semantic_review_required, conflicting_sources:https://connect.grace.edu/register/?id=8e709766-fe65-4d9e-90d0-44ea1f066966,https://www.grace.edu/admissions/financial-aid-scholarships/,https://www.grace.edu/admissions/financial-aid-scholarships/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances will be reviewed on an individual basis when they are submitted in writing.”
  - sentence: need_based_special_circumstances ⟵ “Graduate Scholarship Search Special Circumstances PJ Advisor Student Connections Questions?”
### `a3d5d560032da2bf` Grace College and Theological Seminary — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.grace.edu/admissions/financial-aid-scholarships/ (sha256 ebee134b0522)
- issues: semantic_review_required, conflicting_sources:https://connect.grace.edu/register/?id=8e709766-fe65-4d9e-90d0-44ea1f066966,https://www.grace.edu/admissions/financial-aid-scholarships/,https://www.grace.edu/admissions/financial-aid-scholarships/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances will be reviewed on an individual basis when they are submitted in writing.”
  - sentence: need_based_special_circumstances ⟵ “Graduate Scholarship Search Special Circumstances PJ Advisor Student Connections Questions?”
### `032b8b38f2cd6674` Hanover College — appeals 2021-22 [new] (labeled_in_source)
- source: https://www.hanover.edu/admission/financialaid/faqs/ (sha256 185b60145e31)
- issues: stale_year_label:2021-22, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you cannot answer yes to one of these questions but feel you have extenuating/special circumstances that may qualify you as an independent student then you may request a review of your dependency status.”
### `34a571a35242fe21` Hanover College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hanover.edu/admission/financialaid/professionaljudgement/ (sha256 7443b653d487)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “My SAI is greater than -1500 If your SAI is greater than “-1500” please read the information below about the conditions which do/do not qualify for a Professional Judgement.”
  - sentence: professional_judgment ⟵ “If your SAI is greater than -1500 and you have experienced these circumstances, please completely fill out the Pre-Screen for Professional Judgement form below.”
  - sentence: professional_judgment ⟵ “The Professional Judgement Process If the student qualifies to begin the Special Circumstance Review process they will be contacted and be asked to submit the following: Special Circumstance petition All required supporting documentation of the special circumstance Verification Worksheet Possible Outcomes from a Professional Judgement No change: The change in circumstances did not impact your Stud”
  - sentence: professional_judgment ⟵ “Contact Us For additional questions regarding the Professional Judgement for Special Circumstance process please contact our office.”
  - sentence: professional_judgment ⟵ “EST Phone: 1-800-213-2178 Email: financialservices@hanover.edu Pre-Screen for Professional Judgements The Professional Judgement recalculation process allows the Office of Student Financial Services to look at additional financial information not captured on the FAFSA to better assess a family’s ability to pay for the upcoming year.”
  - sentence: professional_judgment ⟵ “This form will assist us in determining if a student and family could possibly benefit from the Professional Judgment process.”
### `3792c7e67896b863` Hanover College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hanover.edu/docs/Graduate%20Satisfactory%20Academic%20Progress%20(SAP)%20Appeal%20Form.pdf (sha256 b4768c978f42)
- issues: semantic_review_required, conflicting_sources:https://www.hanover.edu/docs/SAP.pdf,https://www.hanover.edu/docs/SAPAppealForm.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Important Dates: • SAP Appeal Deadlines: 5 pm on the first day of the class start for the term for which the appeal is associated.”
  - sentence: sap_appeal ⟵ “If my appeal is denied, I understand that I must reestablish my aid eligibility by attending at my own expense and raising my cumulative academic record to the minimums listed in the Hanover College student financial aid satisfactory academic progress standards, and that I am responsible for any charges incurred if my appeal is not approved.”
### `92997eb16bc318ff` Hanover College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hanover.edu/docs/SAP.pdf (sha256 72ff49aa9a8a)
- issues: semantic_review_required, conflicting_sources:https://www.hanover.edu/docs/Graduate%20Satisfactory%20Academic%20Progress%20(SAP)%20Appeal%20Form.pdf,https://www.hanover.edu/docs/SAPAppealForm.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “A student who is denied Federal aid because of a failure to meet Financial Aid SAP standards after the Warning Term has concluded may appeal this determination to the Satisfactory Academic Progress Appeals Committee of the Office of Student Financial Services.”
  - sentence: sap_appeal ⟵ “Please note that merely filing a Financial Aid SAP appeal does NOT guarantee continued eligibility for Federal aid, as an appeal may be denied.”
  - sentence: sap_appeal ⟵ “If the standards are met at the time of review, eligibility may be regained for subsequent terms of enrollment in the academic year. *In some cases, a Financial Aid SAP appeal will be denied automatically without going to the SAP Appeal Committee.”
  - sentence: sap_appeal ⟵ “For example, a Financial Aid SAP appeal must be completed by the deadline; otherwise, the appeal will be automatically denied.”
  - sentence: sap_appeal ⟵ “The deadline for submission of a Financial Aid SAP appeal to the student’s Hanover College Office of Student Financial Services is by 5 pm on the Hanover College Registrar’s published “Classes Begin” date for the specific term with which the appeal is associated. **Notification of the Committee’s decision should take place within ten business days of the receipt of the appeal in the Hanover Colleg”
### `aff39df9d5f026a2` Hanover College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hanover.edu/docs/SAPAppealForm.pdf (sha256 855f328d5a06)
- issues: semantic_review_required, conflicting_sources:https://www.hanover.edu/docs/Graduate%20Satisfactory%20Academic%20Progress%20(SAP)%20Appeal%20Form.pdf,https://www.hanover.edu/docs/SAP.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Important Dates: • SAP Appeal Deadlines: 5 pm of the first day of the class start for the term for which the appeal is associated.”
  - sentence: sap_appeal ⟵ “If my appeal is denied, I understand that I must reestablish my aid eligibility by attending at my own expense and raising my cumulative academic record to the minimums listed in the Hanover College student financial aid satisfactory academic progress standards, and that I am responsible for any charges incurred if my appeal is not approved.”
### `bac5175c5da64e9c` Hanover College — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.hanover.edu/admission/financialaid/ (sha256 50a907b91f8a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “StudentAid.gov article: What should I do if I have an unusual circumstance and can’t provide parent information?”
  - sentence: need_based_special_circumstances ⟵ “Read this article to determine if you may have an unusual circumstance.”
### `c4f992e4a0d82012` Hanover College — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.hanover.edu/admission/financialaid/ (sha256 50a907b91f8a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Additional Hanover Financial Aid Resources Net Price Calculator Class of 2030 Billing Estimator (TBD) Student Accounts Professional Judgement for Special Circumstances External Scholarships for New and Returning Students Hanover College publicizes information from various businesses, foundations, and civic organizations about scholarships offered to students.”
### `d0ed527ddfd6c833` Hanover College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hanover.edu/docs/SAPAppealForm.pdf (sha256 855f328d5a06)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Other Unusual Circumstances – Supporting documents must include academic advisor, counselor, tutor, professor and/or professional who is familiar with the student’s extenuating circumstances.”
### `12e5f816f06ac8be` Hanover College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://dptprogram.hanover.edu/admission-overview/tuition-financial-aid/ (sha256 c471104891a4)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": false, "rows": 4}
  - column:Hanover Tuition Cost*: 50000 ⟵ “Hanover Tuition Cost* | $50,000 | $50,000 | $100,000”
  - column:Annual Institutional Fees for full time student ( general fees, health insurance, recreation, etc.): 4170 ⟵ “Annual Institutional Fees for full time student ( general fees, health insurance, recreation, etc.) | $4,170 | $4,170 | $8,340”
  - column:Total expected costs of other program-related expenses (required texts, lab fees, and other program costs for entire program): 5465 ⟵ “Total expected costs of other program-related expenses (required texts, lab fees, and other program costs for entire program) | $5,465 | $3,315 | $8,780”
  - column:Total Cost of Program: 59635 ⟵ “Total Cost of Program | $59,635 | $57,485 | $117,120”
  - column:Hanover Tuition Cost*: 50000 ⟵ “Hanover Tuition Cost* | $50,000 | $50,000 | $100,000”
  - column:Annual Institutional Fees for full time student ( general fees, health insurance, recreation, etc.): 4170 ⟵ “Annual Institutional Fees for full time student ( general fees, health insurance, recreation, etc.) | $4,170 | $4,170 | $8,340”
  - column:Total expected costs of other program-related expenses (required texts, lab fees, and other program costs for entire program): 3315 ⟵ “Total expected costs of other program-related expenses (required texts, lab fees, and other program costs for entire program) | $5,465 | $3,315 | $8,780”
  - column:Total Cost of Program: 57485 ⟵ “Total Cost of Program | $59,635 | $57,485 | $117,120”
  - column:Hanover Tuition Cost*: 100000 ⟵ “Hanover Tuition Cost* | $50,000 | $50,000 | $100,000”
  - column:Annual Institutional Fees for full time student ( general fees, health insurance, recreation, etc.): 8340 ⟵ “Annual Institutional Fees for full time student ( general fees, health insurance, recreation, etc.) | $4,170 | $4,170 | $8,340”
  - column:Total expected costs of other program-related expenses (required texts, lab fees, and other program costs for entire program): 8780 ⟵ “Total expected costs of other program-related expenses (required texts, lab fees, and other program costs for entire program) | $5,465 | $3,315 | $8,780”
  - column:Total Cost of Program: 117120 ⟵ “Total Cost of Program | $59,635 | $57,485 | $117,120”
### `7e8783c7e1b071ad` Huntington University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.huntington.edu/financial-aid (sha256 b9bdd4725264)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You may complete a request for a special circumstance adjustment by submitting a Special Circumstance Adjustment form along with the appropriate documentation.”
### `d7e7c3e4175535c2` Huntington University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.huntington.edu/financial-aid (sha256 b9bdd4725264)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “In some cases, we may be able to adjust your FAFSA due to loss of income, death of a parent or spouse, divorce, or natural disaster damage to your family’s residence through a process called "Professional Judgement".”
### `01a0d344414c535f` Indiana Institute of Technology — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.indianatech.edu/transfer/transfer-agreement/clep-and-dantes/ (sha256 dc8ccbdae8c7)
- issues: score_scale_mismatch, conflicting_sources:https://www.indianatech.edu/transfer/transfer-agreement/clep-and-dantes/?as_pdf
- checks: {"distinct_exams": 33, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “Human Resource Management | 3 | BA 2410 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|3]:  ⟵ “Management Information Systems | 3 | MIS 1300 | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “Fundamentals of College Algebra | 3 | SCI EL | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Lifespan Developmental Psychology | 3 | PSY 1750 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|3]:  ⟵ “Financial Accounting | 3 | ACC 1010 | ”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|3]:  ⟵ “Introductory Business Law | 3 | BA 3080 | ”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “Principles of Management | 3 | BA 2010 | ”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|3]:  ⟵ “Principles of Marketing | 3 | BA 2500 | ”
  - equivalencies[CLEP-AMERICAN-LITERATURE|3]:  ⟵ “American Literature | 3 | HUM LIT | ”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|3]:  ⟵ “Analyzing & Interpreting Literature | 3 | HUM LIT | ”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|6]:  ⟵ “College Composition (Requires Essay) | 6 | ENG 1100 & ENG 1252 | ”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|3]:  ⟵ “College Composition Modular | 3 | ENG 1272 | ”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature | 3 | HUM LIT | ”
  - equivalencies[CLEP-HUMANITIES|3]:  ⟵ “Humanities | 3 | HUM EL | ”
  - equivalencies[CLEP-SPANISH-LANGUAGE|6]:  ⟵ “Spanish Language - Level I | 6 | HUM EL | ”
  - equivalencies[CLEP-SPANISH-LANGUAGE|9]:  ⟵ “Spanish Language - Level II | 9 | HUM EL (6 Credits) & APP EL (3 Credits) | ”
  - equivalencies[CLEP-FRENCH-LANGUAGE|6]:  ⟵ “French Language - Level I | 6 | HUM EL | ”
  - equivalencies[CLEP-FRENCH-LANGUAGE|9]:  ⟵ “French Language - Level II | 9 | HUM EL (6 Credits) & APP EL (3 Credits) | ”
  - equivalencies[CLEP-GERMAN-LANGUAGE|6]:  ⟵ “German Language - Level I | 6 | HUM EL | ”
  - equivalencies[CLEP-GERMAN-LANGUAGE|9]:  ⟵ “German Language - Level II | 9 | HUM EL (6 Credits) & APP EL (3 Credits) | ”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “American Government | 3 | SS 1110 | ”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|3]:  ⟵ “History of the United States I: Early Colonization to 1877 | 3 | SS 2430 | ”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|3]:  ⟵ “History of the United States II: 1865 to Present | 3 | SS 2440 | ”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|3]:  ⟵ “Human Growth & Development | 3 | PSY 1750 | ”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|3]:  ⟵ “Introduction to Educational Psychology | 3 | PSY 2010 | ”
  - … 14 more rows
### `51dd2a8fecabefd8` Indiana Institute of Technology — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.indianatech.edu/transfer/transfer-agreement/clep-and-dantes/?as_pdf (sha256 4d1814eaf233)
- issues: score_scale_mismatch, conflicting_sources:https://www.indianatech.edu/transfer/transfer-agreement/clep-and-dantes/
- checks: {"distinct_exams": 23, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “Human Resource Management               3     BA 2410                    3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|3]:  ⟵ “Management Information Systems          3     MIS 1300                   3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “Fundamentals of College Algebra         3     SCI EL                     3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Lifespan Developmental Psychology       3     PSY 1750                   3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|3]:  ⟵ “Financial Accounting                                 3     ACC 1010”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|3]:  ⟵ “Introductory Business Law                            3     BA 3080”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “Principles of Management                             3     BA 2010”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|3]:  ⟵ “Principles of Marketing                              3     BA 2500”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|6]:  ⟵ “College Composition (Requires Essay)                 6     ENG 1100 & ENG 1252”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|3]:  ⟵ “College Composition Modular                          3     ENG 1272”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “American Government                                  3     SS 1110”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|3]:  ⟵ “History of the United States I: Early Colonization   3     SS 2430”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|3]:  ⟵ “History of the United States II: 1865 to Present     3     SS 2440”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|3]:  ⟵ “Human Growth & Development                           3     PSY 1750”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|3]:  ⟵ “Introduction to Educational Psychology               3     PSY 2010”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Introduction to Psychology                           3     PSY 1700”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|3]:  ⟵ “Introduction to Sociology                            3     SS 2800”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3]:  ⟵ “Principles of Macroeconomics                         3     ECON 2200”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|3]:  ⟵ “Principles of Microeconomics                         3     ECON 2210”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|6]:  ⟵ “Social Sciences and History                          6     SS EL (6 credits)”
  - equivalencies[CLEP-BIOLOGY|6]:  ⟵ “Biology                                              6     BIO 1000 & APP EL”
  - equivalencies[CLEP-CALCULUS|4]:  ⟵ “Calculus                                             4     MA 1100 or MA 1200”
  - equivalencies[CLEP-CHEMISTRY|6]:  ⟵ “Chemistry                                            6     CH 1000 & CH 1100”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “College Algebra                                      3     MA 1030”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|6]:  ⟵ “College Mathematics                                  6     MA 1005 & MA 1020”
  - … 1 more rows
### `m42c5c20a52615ed` Indiana Institute of Technology — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.indianatech.edu/transfer/ (sha256 df30d027e2d5)
- issues: conflicting_values:max_transfer_credits
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “Evaluate Your Credits on TES Other ways you can transfer credit to Indiana Tech Alternative Credit Providers AP and Dual Credit CLEP and DANTES Community College Transfers Credit for Prior Learning Ivy Tech Pathways Project Lead the Way Transfer Credit Basics Undergraduate Transfer Credit: Courses completed with grades of “C-” or higher No more than 90 credit hours can be transferred to be applied”
  - max_transfer_credits: 90 ⟵ “A maximum of 90 credit hours of transfer credit can be applied toward a Bachelor’s degree.”
### `049b782ae12ee709` Indiana University-East — appeals 2026-27 [new] (source_unlabeled)
- source: https://east.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal.html (sha256 c69a23b2ce85)
- issues: semantic_review_required, conflicting_sources:https://east.iu.edu/cost-aid/financial-aid/manage-aid/maintain-eligibility.html
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “A complete SAP appeal includes the following components: A typed statement explaining the circumstances that contributed to your unsatisfactory academic progress during all periods of enrollment regardless of whether or not you received financial aid for those terms.”
  - sentence: sap_appeal ⟵ “All completed SAP appeals must be received by the office at least 30 days before the end of the semester you are appealing for.”
  - sentence: sap_appeal ⟵ “Online Satisfactory Academic Progress (SAP) Appeal form If your appeal is denied You must reestablish your eligibility to receive financial aid.”
### `0efecebdd781ef1b` Indiana University-East — appeals 2026-27 [new] (source_unlabeled)
- source: https://east.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal.html (sha256 c69a23b2ce85)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Types of appeals You have special circumstances that were not documented on your FAFSA If your family’s financial status has changed since you filed your FAFSA or if you had an expense that was not considered as part of the FAFSA, you may be able to file a special circumstance appeal.”
  - sentence: need_based_special_circumstances ⟵ “You want to be classified as an independent If you do not meet the federal criteria for independent status on your FAFSA but feel you have unusual circumstances and should be considered independent, you can complete a dependency status appeal.”
  - sentence: need_based_special_circumstances ⟵ “The following do not count as unusual circumstances that will qualify you for an appeal: Your parents refuse to contribute to your education.”
### `c6defcbafc5b69a9` Indiana University-East — appeals 2026-27 [new] (source_unlabeled)
- source: https://east.iu.edu/cost-aid/financial-aid/manage-aid/maintain-eligibility.html (sha256 3cec4ff5cb3f)
- issues: semantic_review_required, conflicting_sources:https://east.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Once you have attempted 160 credit hours, you will need to complete a satisfactory academic progress appeal to help outline your plans for graduation to make sure you’re completing your degree requirements before you reach the 150% limit.”
### `e4ed127d75241e95` Indiana University-East — appeals 2026-27 [new] (source_unlabeled)
- source: https://east.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal.html (sha256 c69a23b2ce85)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency Status Appeal Forms Dependency status appeals may be completed electronically or by submitting a copy of the appeal form and supporting documentation.”
### `22de88c1381a3227` Indiana University-East — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://east.iu.edu/cost-aid/cost-of-attendance/index.html (sha256 5f741740528a)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and required fees: 23032 ⟵ “Tuition and required fees | $8,602 | $12,282 | $23,032”
  - column:Books and supplies: 1166 ⟵ “Books and supplies | $1,166 | $1,166 | $1,166”
  - column:Housing and food: 10972 ⟵ “Housing and food | $10,972 | $10,972 | $10,972”
  - column:Personal expenses: 2270 ⟵ “Personal expenses | $2,270 | $2,270 | $2,270”
  - column:Transportation: 2466 ⟵ “Transportation | $2,466 | $2,466 | $2,466”
  - column:Total typical cost of attendance: 39906 ⟵ “Total typical cost of attendance | $25,476 | $29,156 | $39,906”
### `2af7b4d6c0fc0820` Indiana University-East — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://east.iu.edu/cost-aid/cost-of-attendance/index.html (sha256 5f741740528a)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition and required fees: 8602 ⟵ “Tuition and required fees | $8,602 | $12,282 | $23,032”
  - column:Books and supplies: 1166 ⟵ “Books and supplies | $1,166 | $1,166 | $1,166”
  - column:Housing and food: 10972 ⟵ “Housing and food | $10,972 | $10,972 | $10,972”
  - column:Personal expenses: 2270 ⟵ “Personal expenses | $2,270 | $2,270 | $2,270”
  - column:Transportation: 2466 ⟵ “Transportation | $2,466 | $2,466 | $2,466”
  - column:Total typical cost of attendance: 25476 ⟵ “Total typical cost of attendance | $25,476 | $29,156 | $39,906”
  - column:Tuition and required fees: 12282 ⟵ “Tuition and required fees | $8,602 | $12,282 | $23,032”
  - column:Books and supplies: 1166 ⟵ “Books and supplies | $1,166 | $1,166 | $1,166”
  - column:Housing and food: 10972 ⟵ “Housing and food | $10,972 | $10,972 | $10,972”
  - column:Personal expenses: 2270 ⟵ “Personal expenses | $2,270 | $2,270 | $2,270”
  - column:Transportation: 2466 ⟵ “Transportation | $2,466 | $2,466 | $2,466”
  - column:Total typical cost of attendance: 29156 ⟵ “Total typical cost of attendance | $25,476 | $29,156 | $39,906”
### `14c3b48064393ea2` Indiana University-Indianapolis — appeals 2024-25 [new] (labeled_in_source)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/eligibility-appeal.html (sha256 57196653ec45)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “What special circumstances may be considered for an appeal?”
  - sentence: need_based_special_circumstances ⟵ “If you have previously submitted a special circumstances appeal, you should not file another for the same reason unless instructed to do so by this office.”
### `2656cc623eb425b8` Indiana University-Indianapolis — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/ (sha256 aee81c602cde)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://indianapolis.iu.edu/cost-aid/scholarships/renew/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Other situations If you feel you have a special circumstance that isn’t covered by a change to your Student Aid Index or cost of attendance, contact the Office of Financial Aid and Scholarships for assistance.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstance appeal forms Please contact the Office of Financial Aid and Scholarships with questions or to request these forms in an accessible format. 2025-26 aid year (Fall 2025, Spring 2026, Summer 2026) Submit the special circumstance COA appeal form 2026-27 aid year (Fall 2026, Spring 2027, and Summer 2027) Submit the special circumstance COA appeal form You want to be classified as i”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances that may qualify you include an abusive family environment or being abandoned by your parents.”
### `2f0b6c84bf4af6ad` Indiana University-Indianapolis — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/ (sha256 aee81c602cde)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Scholarship appeal To appeal our decision that resulted in the revocation of your scholarship, you’ll need to fill out a scholarship appeal form.”
### `61a280da071a6c4c` Indiana University-Indianapolis — appeals 2026-27 [new] (source_unlabeled)
- source: https://indianapolis.iu.edu/cost-aid/scholarships/renew/ (sha256 90d5e0596de6)
- issues: semantic_review_required, conflicting_sources:https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you believe that you have additional education-related expenses, you can submit a Special Circumstances form to have your specific expenses reviewed.”
### `9ee8144912e015d2` Indiana University-Indianapolis — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/ (sha256 aee81c602cde)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “The following circumstances do not qualify students to be eligible as an Independent status and will not be approved when submitting a Dependency Override appeal: Your parents refuse to contribute to your education Your parents are unwilling to provide information on the FAFSA or for verification Your parents don’t claim you as a dependent for income tax purposes You demonstrate total self-suffici”
### `e3c3f495887d681d` Indiana University-Indianapolis — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/ (sha256 aee81c602cde)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “File a SAP appeal form You have special circumstances that weren’t documented on your FAFSA If your family’s financial status has changed since you filed your FAFSA or if you had an expense that was not considered as part of the FAFSA, you may be able to file a special circumstance appeal.”
  - sentence: sap_appeal ⟵ “Please contact the Office of Financial Aid and Scholarships with questions or to request this form in an accessible format. 2025-26 aid year (Fall 2025, Spring 2026, Summer 2026) IU Indianapolis parent refusal form 2026-27 aid year (Fall 2026, Spring 2027, and Summer 2027) IU Indianapolis parent refusal form Quick links Academic progress appeal To appeal our decision that you aren’t making satisfa”
### `2ca85b98c8bc5d57` Indiana University-Kokomo — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.iuk.edu/cost-aid/financial-aid/manage-aid/file-appeal/special-circumstances.html (sha256 490276b74b82)
- issues: semantic_review_required, conflicting_sources:https://www.iuk.edu/cost-aid/financial-aid/manage-aid/file-appeal/index.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress appeal We recognize that the FAFSA may not always accurately reflect your financial situation and/or dependency status.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal IU Kokomo SAP Appeal FAFSA Parent Refusal Federal law states the family has the primary responsibility for meeting the educational costs of students.”
### `9202f8824491d641` Indiana University-Kokomo — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.iuk.edu/cost-aid/financial-aid/manage-aid/file-appeal/special-circumstances.html (sha256 490276b74b82)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 20}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances have significantly affected your financial situation since you filed your FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations that justify an aid administrator adjusting data elements in the Cost of Attendance or in the SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstancesrefer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation, more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstance appeal Special Circumstance Appeals will be considered after you receive your initial award notification for the current aid year.”
  - sentence: need_based_special_circumstances ⟵ “After reviewing your special circumstance documentation, your aid package may remain the same, be increased, or reduced according to the financial information that has been submitted.”
### `9341bf604890a54f` Indiana University-Kokomo — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.iuk.edu/cost-aid/financial-aid/manage-aid/file-appeal/index.html (sha256 8b78fc2bfce1)
- issues: semantic_review_required, conflicting_sources:https://www.iuk.edu/cost-aid/financial-aid/manage-aid/file-appeal/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Reasons you might want to file an appeal There are several reasons you might want to file an appeal: You’re not making satisfactory academic progress Special circumstances have significantly affected your financial situation since you filed your FAFSA or you can document expenses greater than your estimated cost of attendance Unusual enrollment history Contact the Office of Financial Aid and Schol”
### `baa2389f32a7d477` Indiana University-Kokomo — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.iuk.edu/cost-aid/financial-aid/manage-aid/file-appeal/special-circumstances.html (sha256 490276b74b82)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “A dependency override does not guarantee an adjustment will be made to your aid package.”
  - sentence: dependency_override ⟵ “The following circumstances do not qualify for a dependency override (not a complete list): Your parents refuse to contribute to your education Your parents are unwilling to provide information on the FAFSA or for verification Your parents don’t claim you as a dependent for income tax purposes You demonstrate total self-sufficiency Your parent(s) no longer live in the same city, state, or country.”
### `3c09215f75f636e9` Indiana University-Kokomo — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.iuk.edu/cost-aid/cost-of-attendance/index.html (sha256 80e0cea961c0)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 7}
  - on_campus:Food and Housing *: 4230 ⟵ “Food and Housing * | $4,230 | $4,230”
  - on_campus:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290”
  - on_campus:Transportation: 1640 ⟵ “Transportation | $1,640 | $1,640”
  - on_campus:Personal: 2360 ⟵ “Personal | $2,360 | $2,360”
  - on_campus:Subtotal: 9520 ⟵ “Subtotal | $9,520 | $16,614”
  - on_campus:Tuition and Fees (est): 8616 ⟵ “Tuition and Fees (est) | $8,616 | $23,222”
  - on_campus:Budget: 18136 ⟵ “Budget | $18,136 | $39,836”
### `b440ed9f537245ba` Indiana University-Kokomo — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.iuk.edu/cost-aid/cost-of-attendance/index.html (sha256 80e0cea961c0)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 7}
  - on_campus:Food and Housing *: 4230 ⟵ “Food and Housing * | $4,230 | $4,230”
  - on_campus:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290”
  - on_campus:Transportation: 1640 ⟵ “Transportation | $1,640 | $1,640”
  - on_campus:Personal: 2360 ⟵ “Personal | $2,360 | $2,360”
  - on_campus:Subtotal: 16614 ⟵ “Subtotal | $9,520 | $16,614”
  - on_campus:Tuition and Fees (est): 23222 ⟵ “Tuition and Fees (est) | $8,616 | $23,222”
  - on_campus:Budget: 39836 ⟵ “Budget | $18,136 | $39,836”
### `b58fed52520903b6` Indiana University-South Bend — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://admissions.iusb.edu/apply/advanced-placement.html (sha256 6cbb08e1aed6)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 31, "equivalencies": 52, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, 5]:  ⟵ “AfricanAmericanStudies | 3, 4, 5 | AFAM-A 150 | 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | AHST-A 101 | 3”
  - equivalencies[AP-ART-HISTORY|4, 5]:  ⟵ “Art History | 4, 5 | AHST-A 101AHST-A 102 | 6 (3 & 3)”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL-L 100 | 3”
  - equivalencies[AP-BIOLOGY|4, 5]:  ⟵ “Biology* | 4, 5 | BIOL-L 101 orBIOL-L 102 | 5”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “CalculusAB | 3 | MATH-M 119 | 3”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “CalculusAB | 4, 5 | MATH-M 215 | 5”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “CalculusBC | 3 | MATH-M 119 | 3”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “CalculusBC | 4, 5 | MATH-M 215MATH-M 216 | 10 (5 & 5)”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM-C 101CHEM-C 121 | 5”
  - equivalencies[AP-CHEMISTRY|4, 5]:  ⟵ “Chemistry | 4, 5 | CHEM-C 105CHEM-C 125 | 5”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “ComparativeGovernmentandPolitics | 3, 4, 5 | POLS-Y 107 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CSCI-B 100 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4, 5]:  ⟵ “Computer Science A | 4, 5 | CSCI-C 101 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | CSCI-UN 100 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4, 5]:  ⟵ “Computer Science Principles | 4, 5 | CSCI-B 100 | 4”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “EnglishLanguageandComposition | 3 | ENG-W 130 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4, 5]:  ⟵ “EnglishLanguageandComposition | 4, 5 | ENG-W 131 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, 5]:  ⟵ “English Literature and Composition | 3, 4, 5 | ENG-L 198 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3, 4, 5]:  ⟵ “EnvironmentalScience | 3, 4, 5 | GEOL-UNDI | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “EuropeanHistory | 3 | HIST-H 103 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4, 5]:  ⟵ “EuropeanHistory | 4, 5 | HIST-H 103HIST-H 104 | 6 (3 & 3)”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|2]:  ⟵ “German LanguageandCulture | 2 | GER-G 101 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “German LanguageandCulture | 3, 4, 5 | GER-G 203GER-G 204 | 6 (3 & 3)”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3, 4, 5]:  ⟵ “HumanGeography | 3, 4, 5 | GEOG-G 110 | 3”
  - … 27 more rows
### `74fdcb818b1129c5` Indiana Wesleyan University-National & Global — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.indwes.edu/admissions/tuition-aid/church-matching/ (sha256 c1270f5a0f3d)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: competing_offer_review ⟵ “Once a student is enrolled in the program, he or she may continue to benefit as long as: the student meets all the eligibility guidelines the student's church submits an official application to IWU by the CMS deadline each year scholarship funds are received at IWU by any required deadlines Students of IWU employees are not eligible to receive the IWU Matching award; however, they may receive CMS ”
### `3d2c89ebd2088de9` Ivy Tech Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ivytech.edu/tuition-aid/financial-aid/fafsa-101/ (sha256 ab43b5dd2282)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.ivytech.edu/tuition-aid/financial-aid-forms/,https://www.ivytech.edu/tuition-aid/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Parent Information MORE FAFSA RESOURCES Reviews for Special and Unusual Circumstances Special Or Unusual Circumstances Review: We understand that sometimes a student’s financial situation or dependency status isn’t fully reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “In these cases, students may qualify for a Special or Unusual Circumstances Review.”
  - sentence: need_based_special_circumstances ⟵ “Learn More Reviews for Special and Unusual Circumstances Summer Semester Financial Aid Information from your most recent FAFSA will be used to determine your financial aid eligibility for the summer semester.”
### `64cab37110610a21` Ivy Tech Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ivytech.edu/tuition-aid/financial-aid/ (sha256 727d33c17d4f)
- issues: semantic_review_required, conflicting_sources:https://www.ivytech.edu/tuition-aid/financial-aid-forms/,https://www.ivytech.edu/tuition-aid/financial-aid/fafsa-101/
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “How to submit documents to the Financial Aid office View All Financial Aid Forms Forms Special and Unusual Circumstances Special Circumstances Review: We understand that there may be situations when a student's true financial situation is not fully reflected by the questions on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “These students may be considered on a case-by-case basis for a Special Circumstances Review.”
  - sentence: need_based_special_circumstances ⟵ “Reasons that MAY be considered for a Special Circumstances Review: Loss of employment Loss of other income Death of student's spouse (or dependent student's parent) Unusual expenses (such as medical costs) Reasons that CAN NOT be used for a Special Circumstances Review: Charitable giving Vacation expenses Tax bills You already qualify for the maximum Pell Grant and loan amounts If you feel you hav”
  - sentence: need_based_special_circumstances ⟵ “Complete 25-26 Special Circumstance Form Complete 26-27 Special Circumstances Form Submit to campus Financial Aid Office Supply any additional documentation if necessary Monitor Ivy Tech email address for response Unusual Circumstances Review: We understand that there may be situations when a student does not meet the federal financial aid requirements to be considered independent on the FAFSA and”
  - sentence: need_based_special_circumstances ⟵ “If you feel you have an extreme situation that may allow for a Review, visit your campus Financial Aid Office to determine if you should complete the Unusual Circumstances Review Form.”
  - sentence: need_based_special_circumstances ⟵ “Complete 25-26 Unusual Circumstances Form Submit to campus Financial Aid Office Supply any additional documentation if necessary Monitor Ivy Tech email address for response Special and Unusual Circumstances Summer Semester Financial Aid FAFSA Information from your most recent FAFSA will be used to determine your financial aid eligibility for the summer semester.”
### `909d3f2de6083a9d` Ivy Tech Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ivytech.edu/tuition-aid/financial-aid/satisfactory-academic-progress-sap/ (sha256 7dd430865b49)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Students may also self-pay and continue to enroll to attempt to regain Good standing or complete program. | No | Probation | Student is on approved SAP appeal.”
  - sentence: sap_appeal ⟵ “Students in termination status for not meeting Satisfactory Academic Progress (SAP) standards who have extenuating circumstances may appeal their Financial Aid eligibility.”
  - sentence: sap_appeal ⟵ “Appealing for Financial Aid SAP Termination Students in termination status for not meeting Satisfactory Academic Progress (SAP) standards who have extenuating circumstances may appeal their Financial Aid eligibility.”
  - sentence: sap_appeal ⟵ “SAP Appeal Form Video Resources Below are videos that can help you understand SAP.”
### `fb848bb29a993d35` Ivy Tech Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.ivytech.edu/tuition-aid/financial-aid-forms/ (sha256 68d45f651c68)
- issues: semantic_review_required, conflicting_sources:https://www.ivytech.edu/tuition-aid/financial-aid/,https://www.ivytech.edu/tuition-aid/financial-aid/fafsa-101/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “These students may be considered on a case-by-case basis for a Special Circumstances Review.”
  - sentence: need_based_special_circumstances ⟵ “Reasons that MAY be considered for a Special Circumstances Review: Loss of employment Loss of other income Death of student's spouse (or dependent student's parent) Unusual expenses (such as medical costs) Reasons that CANNOT be used for a Special Circumstances Review: Charitable giving Vacation expenses Tax bills You already qualify for the maximum Pell Grant and loan amounts (-1500 SAI) If you f”
### `dfd843ee213ab89d` Ivy Tech Community College — credit_policies 2023-24 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.ivytech.edu/programs/signature-opportunities-for-students/high-school-programs/dual-credit/ (sha256 8d4401ccc219)
- issues: stale_year_label:2023-24
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 2.6 ⟵ “A cumulative GPA of 2.6 or higher for juniors and seniors”
  - per_credit_hour_charge: 178.38 ⟵ “$178.38 per credit hour (or $2,577.11 per semester for a full-time, in-state student)”
  - per_credit_hour_charge: 18 ⟵ “All required textbooks are $18 per credit hour”
### `m188b8585c4c152d` Ivy Tech Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ivytech.edu/programs/signature-opportunities-for-students/high-school-programs/dual-enrollment/ (sha256 ba7068a5bbe0)
- issues: multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 2.6 ⟵ “the application as well as their parents'                 ii.   Have a minimum GPA of 2.6 with a Core 40”
  - per_credit_hour_charge: 178.38 ⟵ “At just $178.38 per credit hour—or $2,577.11 per semester—Ivy Tech Community College is the lowest-cost higher education option in Indiana.”
  - eligibility_tier: 2.6 ⟵ “A cumulative GPA of 2.6 or higher for juniors and seniors”
  - per_credit_hour_charge: 178.38 ⟵ “$178.38 per credit hour (or $2,577.11 per semester for a full-time, in-state student)”
  - per_credit_hour_charge: 16.5 ⟵ “All required textbooks are $16.50 per credit hour”
### `477fa447df853627` Manchester University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.manchester.edu/admissions-aid/financial-aid/award-notification/ (sha256 785472ce413f)
- issues: semantic_review_required, conflicting_sources:https://www.manchester.edu/wp-content/uploads/2026/05/Change-in-Circumstance-Appeal-Form-2026-2027.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If special circumstances arise which impact a student’s ability to pay for school, they may qualify to undergo a financial aid review process.”
### `eabeb7403e07278d` Manchester University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.manchester.edu/wp-content/uploads/2025/07/SAP-Policy.pdf (sha256 f75cb1335347)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeal Procedures: Students who fail to meet one or more of the requirements for Satisfactory Academic Progress and have mitigating circumstances may request reinstatement of their financial aid eligibility by submitting a written letter of appeal.”
### `f528c404d225cc88` Manchester University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.manchester.edu/wp-content/uploads/2026/05/Change-in-Circumstance-Appeal-Form-2026-2027.pdf (sha256 b17b66c482ba)
- issues: semantic_review_required, conflicting_sources:https://www.manchester.edu/admissions-aid/financial-aid/award-notification/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Student Financial Services 604 East College Avenue North Manchester, IN 46962 Phone: 260-982-5066 Fax: 260-982-5121 Email: sfs@manchester.edu Student Name: Student ID or SSN: Section III: Your Special Circumstance Check the circumstance(s) A-F, for your appeal and submit the following to Student Financial Services: 1. completed Special Circumstance Appeal form, 2. a descriptive, detailed letter of”
  - sentence: need_based_special_circumstances ⟵ “Other unusual circumstances-Due to other unusual circumstances, my family’s income will be significantly less in 2026 than it was in 2024.”
  - sentence: need_based_special_circumstances ⟵ “Copy of documentation supporting your unusual circumstance Complete Section IV: 2026 Projected Income Section IV: 2025 Projected Income Student: estimated income for the period January 1 to December 31, 2026 $ Parent 1: estimated income for the period January 1 to December 31, 2026 $ Parent 2: estimated income for the period January 1 to December 31, 2026 $ Other estimated taxable and non-taxable ”
### `86942d50d232937b` Manchester University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.manchester.edu/admissions-aid/tuition-fees/ (sha256 21226a4d9de9)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - on_campus:Tuition (Full-time, Fall/Spring + January Term): 37232 ⟵ “Tuition (Full-time, Fall/Spring + January Term) | $37,232 | $36,484”
  - on_campus:Non-Residential Programming Fee (Student-Assessed): 220 ⟵ “Non-Residential Programming Fee (Student-Assessed) | $220 | $220”
### `dcac698390d90db4` Manchester University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.manchester.edu/admissions-aid/tuition-fees/ (sha256 21226a4d9de9)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Tuition (Full-time, Fall/Spring + January Term): 37232 ⟵ “Tuition (Full-time, Fall/Spring + January Term) | $37,232 | $36,484”
  - column:Programming Fee (Student-Assessed): 260 ⟵ “Programming Fee (Student-Assessed) | $260 | $260”
### `285d4edaa34c50a3` Manchester University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.manchester.edu/wp-content/uploads/2025/07/Advanced-Placement-Credit-Equivalencies.pdf (sha256 e509e9786790)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 18, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History               4, 5   ART UNC                   elective hours                         3       LA-EAH”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                  3, 4, 5 BIOL 108 & 108L           Principles of Biology II & Lab         4       LA-ENS”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB               4, 5   MATH 121                  Calculus I                             4       LA-FQR”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                3     MATH 121                  Calculus I                             4       LA-FQR”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                  3     CHEM 105 & 105L           Intro to Inorganic Chem I & Lab        4       LA-ENS”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                  4     CHEM 111 & 111L           General Chemistry I & Lab              4       LA-ENS”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry                  5     CHEM 111/L & 113/L        General Chemistry I & II & Labs        8       LA-ENS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A        3, 4   CPTR 105                  Computer Programming I                 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|5]:  ⟵ “Computer Science A         5     CPTR 105 & 205            Computer Programming I & II            6”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macro          4, 5   ECON 222                  Macroeconomics                         3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Micro          4, 5   ECON 221                  Microeconomics                         3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Lit               4, 5   ENG 115                   Intro to Literature                    3       LA-EAH”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science     4, 5   ENVS 130                  Intro to Environmental Studies         3       LA-ENS”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History          4, 5   HIST 105                  Intro to European History I            3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory              4, 5   MUS 125                   Music Theory I                         3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                 3     PSYC ESS                  Exploration of Social Sciences         3       LA-ESS”
  - equivalencies[AP-PSYCHOLOGY|4]:  ⟵ “Psychology                4, 5   PSYC 110                  Intro to Psychology                    4       LA-ESS”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “Research                 3, 4, 5 GEN UNC                   elective hours                         3”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “Seminar         3, 4, 5 GEN UNC          elective hours                        3”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics        3     MATH 115         Elementary Probability & Statistics   3   LA-FQR”
  - equivalencies[AP-STATISTICS|4]:  ⟵ “Statistics       4, 5   MATH 210         Statistical Analysis                  4   LA-FQR”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “US History        3     HIST UNC         elective hours                        3”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “US History        4     HIST 113         American History I                    3”
  - equivalencies[AP-UNITED-STATES-HISTORY|5]:  ⟵ “US History        5     HIST 113 & 114   American History I & II               6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History     4     HIST 121         World History I                       3   LA-FCG”
  - … 1 more rows
### `0d38c1f22a824709` Marian University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.marian.edu/_documents/admissions/Satisfactory-Academic-Progress-SAP.pdf (sha256 9be44cd9d8c0)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If you are allowed to enroll at Marian University during any subsequent semester, you must do so at your own expense until you once again meet the SAP criteria or submit an SAP Appeal that’s approved.”
### `3b33055d2a5a2723` Marian University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.marian.edu/plymouth/admissions/scholarships (sha256 d481576d8a86)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 3.9}}
  - award_amount_text: $18,000 ⟵ “Marian Scholar | $18,000 | 3.90+ | Awarded at time of admission offer.”
  - gpa_requirement: 3.90+ ⟵ “Marian Scholar | $18,000 | 3.90+ | Awarded at time of admission offer.”
### `a1af17fd70749429` Marian University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.marian.edu/admissions/academics-and-special-programs/advanced-study-program (sha256 eac0a6d2b440)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a minimum 3.00 cumulative GPA”
  - per_credit_hour_charge: 25 ⟵ “| $25 per credit hour.  Students are billed directly once course registration is completed.”
  - per_credit_hour_charge: 25 ⟵ “|  $25 per credit hour.  Student's high school is billed directly.”
  - eligibility_tier: 3.0 ⟵ “Have a minimum 3.00 cumulative GPA”
  - per_credit_hour_charge: 25 ⟵ “Tuition rates for high school students interested in the Advanced Study or Dual Credit Programs are offered at a discount. The cost is $25 per credit hour, which means a standard three-credit Advanced Study or Dual Credit Program course costs $75. Students may take up to 36 hours of dual credit cour”
### `20fdaf828a63fc4e` Marian University-Ancilla — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.marian.edu/_documents/admissions/Satisfactory-Academic-Progress-SAP.pdf (sha256 9be44cd9d8c0)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If you are allowed to enroll at Marian University during any subsequent semester, you must do so at your own expense until you once again meet the SAP criteria or submit an SAP Appeal that’s approved.”
### `e8f2d27d9a0ccb14` Marian University-Ancilla — awards 2026-27 [new] (source_unlabeled)
- source: https://www.marian.edu/plymouth/admissions/scholarships (sha256 7df6574b778f)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 3.9}}
  - award_amount_text: $18,000 ⟵ “Marian Scholar | $18,000 | 3.90+ | Awarded at time of admission offer.”
  - gpa_requirement: 3.90+ ⟵ “Marian Scholar | $18,000 | 3.90+ | Awarded at time of admission offer.”
### `68d313f4491e49cc` Marian University-Ancilla — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.marian.edu/admissions/academics-and-special-programs/advanced-study-program (sha256 5ac91648e2bd)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a minimum 3.00 cumulative GPA”
  - per_credit_hour_charge: 25 ⟵ “| $25 per credit hour.  Students are billed directly once course registration is completed.”
  - per_credit_hour_charge: 25 ⟵ “|  $25 per credit hour.  Student's high school is billed directly.”
  - eligibility_tier: 3.0 ⟵ “Have a minimum 3.00 cumulative GPA”
  - per_credit_hour_charge: 25 ⟵ “Tuition rates for high school students interested in the Advanced Study or Dual Credit Programs are offered at a discount. The cost is $25 per credit hour, which means a standard three-credit Advanced Study or Dual Credit Program course costs $75. Students may take up to 36 hours of dual credit cour”
### `278bca5f699ce037` Purdue University Fort Wayne — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.pfw.edu/admissions-financial-aid/financial-aid/fafsa (sha256 8007b6682671)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: merit_reconsideration ⟵ “Take time to review your award offer with your family.”
  - sentence: merit_reconsideration ⟵ “Take time to review your award offer with your family.”
### `327dba03115c0209` Purdue University Fort Wayne — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.pfw.edu/sites/default/files/documents-2025/11/2627%20Special%20Circumstance%20Appeal.pdf (sha256 bbd6fd7bce83)
- issues: semantic_review_required, conflicting_sources:https://www.pfw.edu/admissions-financial-aid/financial-aid/faq,https://www.pfw.edu/sites/default/files/documents-2025/11/2627%20Unusual%20Circumstance%20Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstance Appeal Student Name:__________________________________________ Student ID: _____________________________________________ Under certain circumstances, the Department of Education permits Purdue University Fort Wayne (PFW) to update information on the student’s FAFSA to recalculate their eligibility for grants.”
### `3c51c2007e55fbff` Purdue University Fort Wayne — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.pfw.edu/admissions-financial-aid/financial-aid/faq (sha256 9d1b81713144)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.pfw.edu/sites/default/files/documents-2025/11/2627%20Special%20Circumstance%20Appeal.pdf,https://www.pfw.edu/sites/default/files/documents-2025/11/2627%20Unusual%20Circumstance%20Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: need_based_special_circumstances ⟵ “What are Special & Unusual Circumstance Appeals?”
  - sentence: need_based_special_circumstances ⟵ “Special and Unusual Circumstance appeals are formal requests submitted to the Office of Financial Aid (OFA) by a student asking OFA to review the student’s FAFSA information to determine if their financial aid eligibility can be adjusted.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances (SC) include any changes in the student's, or parent of dependent students, information that could cause a change to the student’s FAFSA SAI (Student Aid Index).”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances (UC) are unique situations that may justify updating the student’s FAFSA dependency status from dependent to independent.”
  - sentence: need_based_special_circumstances ⟵ “What are Special & Unusual Circumstance Appeals?”
  - sentence: need_based_special_circumstances ⟵ “Special and Unusual Circumstance appeals are formal requests submitted to the Office of Financial Aid (OFA) by a student asking OFA to review the student’s FAFSA information to determine if their financial aid eligibility can be adjusted.”
### `5968ef9388a6a769` Purdue University Fort Wayne — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.pfw.edu/admissions-financial-aid/financial-aid/policies-procedures-and-forms (sha256 5bf8187a6507)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If a SAP appeal is approved students will be placed on a SAPPLAN where they are unable to withdraw (W), receive an F or an Incomplete (I) or they will be moved back into a suspended status.”
  - sentence: sap_appeal ⟵ “If a SAP appeal is approved students will be placed on a SAPPLAN where they are unable to withdraw (W), receive an F or an Incomplete (I) or they will be moved back into a suspended status.”
### `7e0b6d6082c93831` Purdue University Fort Wayne — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.pfw.edu/admissions-financial-aid/financial-aid/policies-procedures-and-forms (sha256 5bf8187a6507)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “If you would like assistance, have a special circumstance that you would like to discuss, or want to make sure you are completing the proper forms, please contact the Office of Financial Aid at 260.481.6820 or [email protected].”
  - sentence: need_based_special_circumstances ⟵ “If you would like assistance, have a special circumstance that you would like to discuss, or want to make sure you are completing the proper forms, please contact the Office of Financial Aid at 260.481.6820 or [email protected]. 2025-2026 V1 Standard Verification 2025-2026 V4 Custom Verification 2025-2026 V5 Aggregate Verification Independent Verification Process and Worksheets Students are consid”
  - sentence: need_based_special_circumstances ⟵ “If you would like assistance, have a special circumstance that you would like to discuss, or want to make sure you are completing the proper forms, please contact the Office of Financial Aid at 260.481.6820 or [email protected]. 2025-2026 V1 Standard Verification 2025-2026 V4 Custom Verification 2025-2026 V5 Aggregate Verification Learn before ever stepping foot in a classroom Financial Aid Litera”
### `a41408fe280f1aa6` Purdue University Fort Wayne — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.pfw.edu/sites/default/files/documents-2025/11/2627%20SAP%20Appeal-updated.pdf (sha256 4155b7df88aa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Student Name:__________________________________________ Student ID: __________________ Term: ____________________ SAP Suspension for:  Completion Rate (CR)  Grade Point Average (GPA)  Maximum Timeframe (MTF) You have been placed on financial aid suspension for failing to meet one or more of the standards for Satisfactory Academic Progress (SAP).”
### `f6a775ce587c4411` Purdue University Fort Wayne — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.pfw.edu/sites/default/files/documents-2025/11/2627%20Unusual%20Circumstance%20Appeal.pdf (sha256 fd7bbfd20ab2)
- issues: semantic_review_required, conflicting_sources:https://www.pfw.edu/admissions-financial-aid/financial-aid/faq,https://www.pfw.edu/sites/default/files/documents-2025/11/2627%20Special%20Circumstance%20Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Unusual Circumstance Dependency Appeal Student Name:__________________________________________ Student ID: _____________________________________________ Under certain circumstances, the Department of Education permits Purdue University Fort Wayne (PFW) to update information on the student’s FAFSA to recalculate their eligibility for grants.”
### `9bf1675bb4b84ecf` Purdue University Fort Wayne — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.pfw.edu/admissions-financial-aid/financial-aid/tuition-and-fees (sha256 ba571bab1a81)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "rows": 8}
  - column:Tuition & mandatory fees: 14298.3 ⟵ “Tuition & mandatory fees | $9,532.20** | $14,298.30** | $24,280.80** | $25,160.10**”
  - column:food: 4402 ⟵ “food | $4,402*** | $4,402*** | $4,402*** | $4,402***”
  - column:housing: 8705.62 ⟵ “housing | $8,705.62 | $8,705.62 | $8,705.62 | $8,705.62”
  - column:Subtotal:: 27405.92 ⟵ “Subtotal: | $22,639.82 | $27,405.92 | $37,388.42 | $38,267.72”
  - column:books/course materials/supplies/equipment: 3180 ⟵ “books/course materials/supplies/equipment | $3,180 | $3,180 | $3,180 | $3,180”
  - column:transportation: 1586 ⟵ “transportation | $1,586 | $1,586 | $1,586 | $1,586”
  - column:miscellaneous: 2430 ⟵ “miscellaneous | $2,430 | $2,430 | $2,430 | $2,430”
  - column:subtotal:: 7196 ⟵ “subtotal: | $7,196 | $7,196 | $7,196 | $7,196”
  - column:Tuition & mandatory fees: 25160.1 ⟵ “Tuition & mandatory fees | $9,532.20** | $14,298.30** | $24,280.80** | $25,160.10**”
  - column:food: 4402 ⟵ “food | $4,402*** | $4,402*** | $4,402*** | $4,402***”
  - column:housing: 8705.62 ⟵ “housing | $8,705.62 | $8,705.62 | $8,705.62 | $8,705.62”
  - column:Subtotal:: 38267.72 ⟵ “Subtotal: | $22,639.82 | $27,405.92 | $37,388.42 | $38,267.72”
  - column:books/course materials/supplies/equipment: 3180 ⟵ “books/course materials/supplies/equipment | $3,180 | $3,180 | $3,180 | $3,180”
  - column:transportation: 1586 ⟵ “transportation | $1,586 | $1,586 | $1,586 | $1,586”
  - column:miscellaneous: 2430 ⟵ “miscellaneous | $2,430 | $2,430 | $2,430 | $2,430”
  - column:subtotal:: 7196 ⟵ “subtotal: | $7,196 | $7,196 | $7,196 | $7,196”
### `74b730b94d4efda2` Purdue University Global — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.purdueglobal.edu/tuition-financial-aid/frequently-asked-questions/ (sha256 052beacb8938)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Armed Forces or currently in active duty Been in foster care, an orphan (because both parents are deceased), or a ward of the court at any time since you turned age 13 Been legally emancipated or in a legal guardianship, as determined by a court in your state of residence Been determined to be an unaccompanied homeless youth or at risk of homelessness Have documented unusual circumstances and have”
### `6fbfbb0f7f06e603` Purdue University Global — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.purdueglobal.edu/paying-for-school/tuition-fees/cost-of-attendance.pdf (sha256 5616f2d77f5a)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.purdueglobal.edu/paying-for-school/tuition-fees/active-military-tuition.pdf
- checks: {"columns": 5, "rows": 20}
  - column:Fees: 1053 ⟵ “Fees | $1,053 | $960 | $960 | $960 | $960”
  - column:Books & Supplies: 0 ⟵ “Books & Supplies | $0 | $450 | $450 | $450 | $450”
  - column:Housing & Food: 6870 ⟵ “Housing & Food | $6,870 | $6,870 | $6,870 | $6,870 | $6,870”
  - column:Transportation: 720 ⟵ “Transportation | $720 | $720 | $720 | $720 | $720”
  - column:Personal Expenses: 1860 ⟵ “Personal Expenses | $1,860 | $1,860 | $1,860 | $1,860 | $1,860”
  - column:Fees (2): 1053 ⟵ “Fees | $1,053 | $960 | $960 | $960 | $960”
  - column:Books & Supplies (2): 0 ⟵ “Books & Supplies | $0 | $450 | $450 | $450 | $450”
  - column:Housing & Food (2): 3435 ⟵ “Housing & Food | $3,435 | $3,435 | $3,435 | $3,435 | $3,435”
  - column:Transportation (2): 720 ⟵ “Transportation | $720 | $720 | $720 | $720 | $720”
  - column:Personal Expenses (2): 930 ⟵ “Personal Expenses | $930 | $930 | $930 | $930 | $930”
  - column:Fees (3): 885 ⟵ “Fees | $885 | $885”
  - column:Books & Supplies (3): 1200 ⟵ “Books & Supplies | $1,200 | $1,200”
  - column:Housing & Food (3): 10992 ⟵ “Housing & Food | $10,992 | $10,992”
  - column:Transportation (3): 1152 ⟵ “Transportation | $1,152 | $1,152”
  - column:Personal Expenses (3): 2976 ⟵ “Personal Expenses | $2,976 | $2,976”
  - column:Fees (4): 885 ⟵ “Fees | $885 | $885”
  - column:Books & Supplies (4): 1200 ⟵ “Books & Supplies | $1,200 | $1,200”
  - column:Housing & Food (4): 5496 ⟵ “Housing & Food | $5,496 | $5,496”
  - column:Transportation (4): 1152 ⟵ “Transportation | $1,152 | $1,152”
  - column:Personal Expenses (4): 1488 ⟵ “Personal Expenses | $1,488 | $1,488”
  - column:Fees: 960 ⟵ “Fees | $1,053 | $960 | $960 | $960 | $960”
  - column:Books & Supplies: 450 ⟵ “Books & Supplies | $0 | $450 | $450 | $450 | $450”
  - column:Housing & Food: 6870 ⟵ “Housing & Food | $6,870 | $6,870 | $6,870 | $6,870 | $6,870”
  - column:Transportation: 720 ⟵ “Transportation | $720 | $720 | $720 | $720 | $720”
  - column:Personal Expenses: 1860 ⟵ “Personal Expenses | $1,860 | $1,860 | $1,860 | $1,860 | $1,860”
  - … 47 more rows
### `ff6b7c345c88adf2` Purdue University Global — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.purdueglobal.edu/paying-for-school/tuition-fees/active-military-tuition.pdf (sha256 c90f05c045f4)
- issues: residency_unknown, conflicting_sources:https://www.purdueglobal.edu/paying-for-school/tuition-fees/cost-of-attendance.pdf
- checks: {"columns": 3, "rows": 55}
  - other:Tuition: 90 ⟵ “Tuition | 90 | $165 | $14,850”
  - other:Tuition: Standard: 180 ⟵ “Tuition: Standard | 180 | $165 | $29,700”
  - other:Nursing: 21450 ⟵ “Nursing | $21,450”
  - other:Applied Behavior: 35 ⟵ “Applied Behavior | 35 | $165 | $5,775”
  - other:Crime Scene: 41 ⟵ “Crime Scene | 41 | $165 | $6,765”
  - other:General Education: 45 ⟵ “General Education | 45 | $165 | $7,425”
  - other:Human Resources: 30 ⟵ “Human Resources | 30 | $165 | $4,950”
  - other:Human Services: 43 ⟵ “Human Services | 43 | $165 | $7,095”
  - other:Human Services (2): 43 ⟵ “Human Services | 43 | $165 | $7,095”
  - other:Legal Secretary: 31 ⟵ “Legal Secretary | 31 | $165 | $5,115”
  - other:Management and: 36 ⟵ “Management and | 36 | $165 | $5,940”
  - other:Medical Assistant: 58 ⟵ “Medical Assistant | 58 | $165 | $9,570”
  - other:Medical: 44 ⟵ “Medical | 44 | $165 | $7,260”
  - other:Medical Office: 57 ⟵ “Medical Office | 57 | $165 | $9,405”
  - other:Pathway to: 36 ⟵ “Pathway to | 36 | $165 | $5,940”
  - other:LRC100: 1500 ⟵ “LRC100 | $1,500 | $1,500 | Noncredit”
  - other:Master of Business Administration: 60 ⟵ “Master of Business Administration | 60 | $320 | $19,200”
  - other:Master of Health Care: 52 ⟵ “Master of Health Care | 52 | $320 | $16,640”
  - other:Master of Health Informatics: 48 ⟵ “Master of Health Informatics | 48 | $320 | $15,360”
  - other:Master of Health Information: 48 ⟵ “Master of Health Information | 48 | $320 | $15,360”
  - other:Master of Public Administration: 55 ⟵ “Master of Public Administration | 55 | $320 | $17,600”
  - other:Master of Public Health: 56 ⟵ “Master of Public Health | 56 | $320 | $17,920”
  - other:Master of Science in Accounting: 52 ⟵ “Master of Science in Accounting | 52 | $320 | $16,640”
  - other:Master of Science in Applied: 45 ⟵ “Master of Science in Applied | 45 | $320 | $14,400”
  - other:Master of Science in Criminal: 55 ⟵ “Master of Science in Criminal | 55 | $320 | $17,600”
  - … 141 more rows
### `2ccd0cc5fd31adf9` Purdue University Global — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.purdueglobal.edu/transfer-students/credit-by-exam-course/ (sha256 e9fe61a54f26)
- issues: rows_without_score
- checks: {"distinct_exams": 33, "equivalencies": 33, "rows_without_score": 33}
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “Art History | 100/200 Humanities Elective | 9”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology | SC235 Human Biology and 100/200 Life Science Elective | 12”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Calculus AB | 100/200 Mathematics Elective | 6”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “Calculus BC | 100/200 Mathematics Elective | 12”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry | SC156 Principles of Chemistry and 100/200 Chemistry Elective | 12”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “Chinese Language and Culture | 100/200 Humanities Elective | 9*”
  - equivalencies[AP-COMPUTER-SCIENCE-A|None]:  ⟵ “Computer Science A | 100/200 Information Technology Elective | 5”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “English Language and Composition | CM107 College Composition I and CM220 College Composition II | 10”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “English Literature and Composition | 100/200 Humanities Elective | 9”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “Environmental Science | SC225 Environmental Science - Ecosystems, Resources, and Carbon Footprints | 5”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “European History | 100/200 Social Science Elective | 9”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “French Language | 100/200 Humanities Elective | 9*”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “German Language | 100/200 Humanities Elective | 9*”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Human Geography | 100/200 Social Science Elective | 5”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|None]:  ⟵ “Italian Language and Culture | 100/200 Humanities Elective | 12*”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|None]:  ⟵ “Japanese Language and Culture | 100/200 Humanities Elective | 9*”
  - equivalencies[AP-LATIN|None]:  ⟵ “Latin | 100/200 Humanities Elective | 12*”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “Macroeconomics | BU204 Macroeconomics | 5”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Microeconomics | BU224 Microeconomics | 5”
  - equivalencies[AP-MUSIC-THEORY|None]:  ⟵ “Music Theory | 100/200 Humanities Elective | 5*”
  - equivalencies[AP-PHYSICS-1|None]:  ⟵ “Physics 1 | 100/200 Science Elective | 6”
  - equivalencies[AP-PHYSICS-2|None]:  ⟵ “Physics 2: Algebra Based | 100/200 Science Elective | 6”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|None]:  ⟵ “Physics C: Electricity and Magnetism | 100/200 Science Elective | 6”
  - equivalencies[AP-PHYSICS-C-MECHANICS|None]:  ⟵ “Physics C: Mechanics | 100/200 Science Elective | 6”
  - equivalencies[AP-PRECALCULUS|None]:  ⟵ “Precalculus | 100/200 Mathematics Elective | 6”
  - … 8 more rows
### `a2c6440c27358a96` Purdue University Global — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.purdueglobal.edu/transfer-students/credit-by-exam-course/ (sha256 e9fe61a54f26)
- issues: rows_without_score
- checks: {"distinct_exams": 42, "equivalencies": 42, "rows_without_score": 42}
  - equivalencies[IB-BIOLOGY-SL|None]:  ⟵ “Biology SL | SC235 Human Biology | 5”
  - equivalencies[IB-BIOLOGY-HL|None]:  ⟵ “Biology HL | SC235 Human Biology and 100/200 Level Life Science Elective | 10”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|None]:  ⟵ “Business Management SL | 100/200 Level Management Elective | 5”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|None]:  ⟵ “Business Management HL | 100/200 Level Management Elective | 10”
  - equivalencies[IB-CHEMISTRY-SL|None]:  ⟵ “Chemistry SL | SC156 Principles of Chemistry | 5”
  - equivalencies[IB-CHEMISTRY-HL|None]:  ⟵ “Chemistry HL | SC156 Principles of Chemistry and 100/200 Level Chemistry Elective | 10”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|None]:  ⟵ “Computer Science SL | 100/200 Level Information Technology Elective | 5”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|None]:  ⟵ “Computer Science HL | 100/200 Level Information Technology Elective | 10”
  - equivalencies[IB-ECONOMICS-SL|None]:  ⟵ “Economics SL | 100/200 Level Social Science Elective | 5”
  - equivalencies[IB-ECONOMICS-HL|None]:  ⟵ “Economics HL | 100/200 Level Social Science Elective | 10”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-SL|None]:  ⟵ “English A: Language and Literature SL | 100/200 Level Humanities Elective | 5”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|None]:  ⟵ “English A: Language and Literature HL | 100/200 Level Humanities Elective | 10”
  - equivalencies[IB-ENGLISH-A-LITERATURE-SL|None]:  ⟵ “English A: Literature SL | 100/200 Level Humanities Elective | 5”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|None]:  ⟵ “English A: Literature HL | 100/200 Level Humanities Elective | 10”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|None]:  ⟵ “Environmental Systems and Societies SL | 100/200 Level Science Elective | 5”
  - equivalencies[IB-FRENCH-SL|None]:  ⟵ “French AB SL | 100/200 Level Humanities Elective | 5”
  - equivalencies[IB-FRENCH-HL|None]:  ⟵ “French AB HL | 100/200 Level Humanities Elective | 10”
  - equivalencies[IB-GEOGRAPHY-SL|None]:  ⟵ “Geography SL | 100/200 Level Social Science Elective | 5”
  - equivalencies[IB-GEOGRAPHY-HL|None]:  ⟵ “Geography HL | 100/200 Level Social Science Elective | 10”
  - equivalencies[IB-GERMAN-SL|None]:  ⟵ “German AB SL | 100/200 Level Humanities Elective | 5”
  - equivalencies[IB-GERMAN-HL|None]:  ⟵ “German B HL | 100/200 Level Humanities Elective | 10”
  - equivalencies[IB-GLOBAL-POLITICS-SL|None]:  ⟵ “Global Politics SL | 100/200 Level Social Science Elective | 5”
  - equivalencies[IB-GLOBAL-POLITICS-HL|None]:  ⟵ “Global Politics HL | 100/200 Level Social Science Elective | 10”
  - equivalencies[IB-HISTORY-HL|None]:  ⟵ “History Africa and Middle East HL | 100/200 Level Social Science Elective | 10”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|None]:  ⟵ “Mathematics: Analysis and Approaches SL | 100/200 Level Mathematics Elective | 5”
  - … 17 more rows
### `dbf970bffbd1a12e` Purdue University Global — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.purdueglobal.edu/transfer-students/credit-by-exam-course/ (sha256 e9fe61a54f26)
- issues: rows_without_score
- checks: {"distinct_exams": 33, "equivalencies": 34, "rows_without_score": 34}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|None]:  ⟵ “American Government | SS236 American Government | 5”
  - equivalencies[CLEP-AMERICAN-LITERATURE|None]:  ⟵ “American Literature | 100/200 Humanities Elective | 5*”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|None]:  ⟵ “Analyzing and Interpreting Literature | 100/200 Humanities Elective | 5*”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “Biology | SC235 Human Biology and100/200 Life Science Elective | 9”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | 100/200 Mathematics Elective | 5*”
  - equivalencies[CLEP-CHEMISTRY|None]:  ⟵ “Chemistry | SC156 Principles of Chemistry and 100/200 Chemistry Elective | 9”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “College Algebra - Trigonometry | 100/200 Mathematics Elective | 5”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “College Algebra | MM212 College Algebra | 5”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | CM107 College Composition I and CM220 College Composition II | 10”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|None]:  ⟵ “College Composition Modular | CM107 College Composition I | 5”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|None]:  ⟵ “College Mathematics | MM150 Survey of Mathematics and 100/200 Mathematics Elective | 9”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “English Literature | 100/200 Humanities Elective | 5*”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|None]:  ⟵ “Financial Accounting | AC114 Accounting I and (Waiver) AC116 Accounting II | 5”
  - equivalencies[CLEP-FRENCH-LANGUAGE|None]:  ⟵ “French Language | 100/200 Humanities Elective | 9*”
  - equivalencies[CLEP-GERMAN-LANGUAGE|None]:  ⟵ “German Language | 100/200 Humanities Elective | 9*”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|None]:  ⟵ “History of the United States I: Early Colonization to 1877 | 100/200 Social Science Elective | 5”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|None]:  ⟵ “History of the United States II: 1865 to the Present | 100/200 Social Science Elective | 5”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|None]:  ⟵ “Human Growth and Development | 100/200 Social Science Elective | 5”
  - equivalencies[CLEP-HUMANITIES|None]:  ⟵ “Humanities | 100/200 Humanities Elective | 5*”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|None]:  ⟵ “Information Systems | 100/200 Information Technology Elective | 5*”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|None]:  ⟵ “Introduction to Educational Psychology | 100/200 Psychology Elective | 5”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “Introductory Business Law | 100/200 Legal Studies Elective or 100/200 Business Elective | 5”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “Introductory Psychology | PS124 Introduction to Psychology | 5*”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Introductory Sociology | SS144 Sociology | 5”
  - equivalencies[CLEP-NATURAL-SCIENCES|None]:  ⟵ “Natural Sciences | 100/200 Science Elective | 9”
  - … 9 more rows
### `0177a7eccfe2ea27` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=hospitality-sustainability [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
- issues: course_alternatives_in_rule_text
  - courses: TH 116 ⟵ “TH 116 - Introduction to Hospitality, Event Management, and Tourism”
  - courses: TH 206 ⟵ “TH 206 - Hotel Management and Operations”
  - courses: MT 313 ⟵ “MT 313 - Corporate Sustainability and Social Responsibility”
  - courses: MT 314 ⟵ “MT 314 - Social Innovation and Entrepreneurship”
  - courses: TH 311 ⟵ “TH 311 - Sustainable Hospitality Management”
### `07cb024fc369460d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-computer-science · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-computer-science-bs/ (sha256 49600e5d901a)
- issues: course_alternatives_in_rule_text
  - courses: IT 200 ⟵ “IT 200 - Software Engineering”
  - courses: IT 234 ⟵ “IT 234 - 🌐 Database Concepts”
  - courses: IN 252 ⟵ “IN 252 - 🌐 Software Development Concepts Using Java”
  - courses: IN 256 ⟵ “IN 256 - 🌐 Software Design and Development Concepts Using Java”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 286 ⟵ “IT 286 - 🌐 Network Security Concepts”
  - courses: MM 260 ⟵ “MM 260 - Linear Algebra”
  - courses: MM 265 ⟵ “MM 265 - Trigonometry”
  - courses: IN 300 ⟵ “IN 300 - 🌐 Programming for Data Analysis (Python, R, and Java)”
  - courses: IT 310 ⟵ “IT 310 - Data Structures and Algorithms”
  - courses: IN 315 ⟵ “IN 315 - Computer Architecture”
  - courses: IT 320 ⟵ “IT 320 - Operating Systems”
  - courses: IN 317 ⟵ “IN 317 - Compilers”
  - courses: IT 350 ⟵ “IT 350 - 🌐 Advanced Database Concepts”
  - courses: IN 352 ⟵ “IN 352 - 🌐 Advanced Software Development Including Web and Mobility Using Java”
  - courses: IN 452 ⟵ “IN 452 - 🌐 Advanced Software Development Using Java”
  - courses: MM 365 ⟵ “MM 365 - Calculus I”
  - courses: MM 555 ⟵ “MM 555 - Applied Statistics”
  - courses: IT 488 ⟵ “IT 488 - 🌐 Software Product Development Using Agile”
### `0fe587a5a4232879` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=sustainable-hospitality [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
- issues: course_alternatives_in_rule_text
  - courses: TH 116 ⟵ “TH 116 - Introduction to Hospitality, Event Management, and Tourism”
  - courses: TH 206 ⟵ “TH 206 - Hotel Management and Operations”
  - courses: MT 313 ⟵ “MT 313 - Corporate Sustainability and Social Responsibility”
  - courses: MT 314 ⟵ “MT 314 - Social Innovation and Entrepreneurship”
  - courses: TH 311 ⟵ “TH 311 - Sustainable Hospitality Management”
### `114c401965b06e11` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=human-resources [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
- issues: course_alternatives_in_rule_text
  - courses: HR 400 ⟵ “HR 400 - 🌐 Talent Acquisition and Management”
  - courses: HR 410 ⟵ “HR 410 - Talent Development and Learning”
  - courses: HR 420 ⟵ “HR 420 - Workplace Law, Labor Relations, and HR Risk Management”
  - courses: HR 435 ⟵ “HR 435 - Total Rewards and Compensation Strategy”
### `1a5dbdc736af06c1` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
- issues: course_alternatives_in_rule_text
  - courses: HR 400 ⟵ “HR 400 - 🌐 Talent Acquisition and Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 340 ⟵ “MT 340 - 🌐 Conflict Management and Team Dynamics”
  - courses: MT 435 ⟵ “MT 435 - 🌐 Operations Management”
  - courses: MT 450 ⟵ “MT 450 - 🌐 Brand Management Strategy”
### `32149de5b1a348d2` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-small-group-management · requirement_key=program-requirements-core-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/small-group-management-aas/ (sha256 0411c2728524)
- issues: course_alternatives_in_rule_text
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
### `4af4d3d908be3cbc` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
- issues: course_alternatives_in_rule_text
  - courses: CJ 100 ⟵ “CJ 100 - 🌐 Preparing for a Career in Public Safety”
  - courses: CJ 101 ⟵ “CJ 101 - 🌐 Introduction to the Criminal Justice System”
  - courses: CJ 102 ⟵ “CJ 102 - 🌐 Criminology I”
  - courses: CJ 210 ⟵ “CJ 210 - 🌐 Criminal Investigation”
  - courses: CJ 212 ⟵ “CJ 212 - 🌐 Crime Prevention”
  - courses: CJ 216 ⟵ “CJ 216 - 🌐 Computers, Technology, and Criminal Justice Information Systems”
  - courses: CJ 227 ⟵ “CJ 227 - 🌐 Criminal Procedure”
  - courses: CJ 230 ⟵ “CJ 230 - 🌐 Criminal Law for Criminal Justice”
  - courses: CJ 340 ⟵ “CJ 340 - 🌐 Applied Criminal Justice Ethics”
  - courses: CJ 345 ⟵ “CJ 345 - 🌐 Supervisory Practices in Criminal Justice”
  - courses: CJ 346 ⟵ “CJ 346 - 🌐 Cultural Awareness in Public Safety”
  - courses: CJ 490 ⟵ “CJ 490 - 🌐 Research Methods in Criminal Justice”
  - courses: CJ 499 ⟵ “CJ 499 - Bachelor's Capstone in Criminal Justice”
### `5d45ea4ec5b8a670` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=business [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
- issues: course_alternatives_in_rule_text
  - courses: AC 256 ⟵ “AC 256 - Federal Tax”
  - courses: BU 204 ⟵ “BU 204 - 🌐 Macroeconomics”
  - courses: IT 133 ⟵ “IT 133 - 🌐 Microsoft Office Applications on Demand”
  - courses: MT 209 ⟵ “MT 209 - Small Business Management”
### `76d5e1fe8c579ade` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
- issues: course_alternatives_in_rule_text
  - courses: HR 400 ⟵ “HR 400 - 🌐 Talent Acquisition and Management”
  - courses: MT 340 ⟵ “MT 340 - 🌐 Conflict Management and Team Dynamics”
  - courses: MT 355 ⟵ “MT 355 - 🌐 Marketing Research and Analytics”
  - courses: MT 400 ⟵ “MT 400 - 🌐 Business Process Management”
### `79061a1462739713` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nursing-rn-to-bsn · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-rn-bsn-bs/ (sha256 4d33147a4129)
- issues: course_alternatives_in_rule_text
  - courses: NU 300 ⟵ “NU 300 - Professional Leadership Transitions”
  - courses: NU 325 ⟵ “NU 325 - Evidence-Based Nursing”
  - courses: NU 333 ⟵ “NU 333 - Health Assessment for the Nursing Professional”
  - courses: NU 425 ⟵ “NU 425 - Transforming Leadership and Management in Nursing”
  - courses: NU 465 ⟵ “NU 465 - Public Health Nursing - Evidence for Practice”
  - courses: NU 470 ⟵ “NU 470 - Regenerative and Restorative Care Spheres - A Wellness and Prevention Focus”
  - courses: NU 475 ⟵ “NU 475 - Providing Transition Care - Chronic Disease and Palliative/Hospice Spheres”
  - courses: NU 480 ⟵ “NU 480 - Four Spheres BSN Capstone”
### `7a448e5af12fccbd` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
- issues: course_alternatives_in_rule_text
  - courses: CM 240 ⟵ “CM 240 - Technical Communication”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: PP 220 ⟵ “PP 220 - Socially Responsible Leadership”
  - courses: SC 206 ⟵ “SC 206 - Introduction to Sustainability”
  - courses: SC 225 ⟵ “SC 225 - Environmental Science”
  - courses: SC 226 ⟵ “SC 226 - Environmental Science Lab”
  - courses: SC 255 ⟵ “SC 255 - Research Methodology”
  - courses: EM 410 ⟵ “EM 410 - The Global Environment”
  - courses: SC 302 ⟵ “SC 302 - Topics in Sustainability”
  - courses: SC 499 ⟵ “SC 499 - Bachelor's Capstone in Sustainability”
### `9acc4a7ea98f3714` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aviation-management · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/aviation-management-bs/ (sha256 1ca153298e79)
- issues: course_alternatives_in_rule_text
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: AV 102 ⟵ “AV 102 - Aviation History”
  - courses: AV 203 ⟵ “AV 203 - Aviation Operations Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: AV 327 ⟵ “AV 327 - Advanced Transport Flight Operations”
  - courses: AV 338 ⟵ “AV 338 - Business Aviation Management”
  - courses: AV 340 ⟵ “AV 340 - Aerospace Business Statistics”
  - courses: AV 412 ⟵ “AV 412 - Aviation Finance”
  - courses: AV 421 ⟵ “AV 421 - Managerial Economics in Aviation”
  - courses: AV 438 ⟵ “AV 438 - Airline Operations”
  - courses: AV 475 ⟵ “AV 475 - Aviation Law”
  - courses: AV 481 ⟵ “AV 481 - Safety Management Systems”
  - courses: LI 410 ⟵ “LI 410 - Leadership in Practice”
  - courses: LS 311 ⟵ “LS 311 - 🌐 Business Law”
  - courses: MT 300 ⟵ “MT 300 - 🌐 Management of Information Systems”
  - courses: AV 499 ⟵ “AV 499 - Bachelor's Capstone in Aviation Management”
### `adb1b5c612e56ee8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-manufacturing · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-manufacturing-bs/ (sha256 ed13b75cad34)
- issues: course_alternatives_in_rule_text
  - courses: BI 100 ⟵ “BI 100 - Introduction to the Workplace and Safety”
  - courses: BI 150 ⟵ “BI 150 - Introduction to Plant Floor and Computer Numerical Control (CNC) Principles”
  - courses: BI 200 ⟵ “BI 200 - Introduction to Print Reading”
  - courses: BI 250 ⟵ “BI 250 - Manufacturing Automation”
  - courses: BI 260 ⟵ “BI 260 - Production Machine Tooling”
  - courses: BI 270 ⟵ “BI 270 - Computer-Aided Design Fundamentals”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: BI 400 ⟵ “BI 400 - Industry 4.0 Principles and Technologies”
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 333 ⟵ “IT 333 - Emerging Technologies and the Future”
  - courses: MM 555 ⟵ “MM 555 - Applied Statistics”
  - courses: MT 313 ⟵ “MT 313 - Corporate Sustainability and Social Responsibility”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 435 ⟵ “MT 435 - 🌐 Operations Management”
  - courses: MT 475 ⟵ “MT 475 - Quality Management”
  - courses: BI 499 ⟵ “BI 499 - Bachelor's Capstone in Applied Manufacturing”
### `c03ed4a1a3611b3b` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=small-business-management [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
- issues: course_alternatives_in_rule_text
  - courses: AC 239 ⟵ “AC 239 - Managerial Accounting”
  - courses: IT 133 ⟵ “IT 133 - 🌐 Microsoft Office Applications on Demand”
  - courses: MT 209 ⟵ “MT 209 - Small Business Management”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
### `c0fbc452c2f97baa` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
- issues: course_alternatives_in_rule_text
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 217 ⟵ “MT 217 - 🌐 Finance”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: LS 311 ⟵ “LS 311 - 🌐 Business Law”
  - courses: MT 300 ⟵ “MT 300 - 🌐 Management of Information Systems”
  - courses: CM 410 ⟵ “CM 410 - Organizational Communication”
  - courses: MT 304 ⟵ “MT 304 - Leading the 21st Century Organization”
  - courses: MT 497 ⟵ “MT 497 - Bachelor's Capstone in Organizational Management”
### `c9d91ee4a3e8c9e2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-information-technology · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-bs/ (sha256 6d6bdb1e9c45)
- issues: course_alternatives_in_rule_text
  - courses: CS 114 ⟵ “CS 114 - Academic Strategies for the IT Professional”
  - courses: IT 117 ⟵ “IT 117 - 🌐 Website Development”
  - courses: IN 150 ⟵ “IN 150 - Foundations for Success in Information Technology (IT) Careers”
  - courses: IT 163 ⟵ “IT 163 - 🌐 Database Concepts Using Microsoft Access”
  - courses: IT 190 ⟵ “IT 190 - 🌐 Information Technology Concepts”
  - courses: IT 234 ⟵ “IT 234 - 🌐 Database Concepts”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IN 250 ⟵ “IN 250 - 🌐 Software Development Concepts Using Python”
  - courses: IN 251 ⟵ “IN 251 - 🌐 Software Development Concepts Using C#”
  - courses: IN 252 ⟵ “IN 252 - 🌐 Software Development Concepts Using Java”
  - courses: IN 253 ⟵ “IN 253 - 🌐 Software Development Concepts Using JavaScript and PHP”
  - courses: IN 254 ⟵ “IN 254 - 🌐 Software Design and Development Concepts Using Python”
  - courses: IN 255 ⟵ “IN 255 - 🌐 Software Design and Development Concepts Using C#”
  - courses: IN 256 ⟵ “IN 256 - 🌐 Software Design and Development Concepts Using Java”
  - courses: IN 257 ⟵ “IN 257 - 🌐 Software Design and Development Concepts Using JavaScript and PHP”
  - courses: IT 286 ⟵ “IT 286 - 🌐 Network Security Concepts”
  - courses: IT 299 ⟵ “IT 299 - IT Integrative Project”
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 331 ⟵ “IT 331 - 🌐 Technology Infrastructure”
  - courses: IT 332 ⟵ “IT 332 - 🌐 Principles of Information Systems Architecture”
  - courses: IT 460 ⟵ “IT 460 - 🌐 Systems Analysis and Design”
  - courses: MM 555 ⟵ “MM 555 - Applied Statistics”
  - courses: IT 499 ⟵ “IT 499 - Bachelor's Capstone in Information Technology”
### `d964919bd1be3f67` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=hospitality-sustainability [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
- issues: course_alternatives_in_rule_text
  - courses: TH 116 ⟵ “TH 116 - Introduction to Hospitality, Event Management, and Tourism”
  - courses: TH 206 ⟵ “TH 206 - Hotel Management and Operations”
  - courses: MT 313 ⟵ “MT 313 - Corporate Sustainability and Social Responsibility”
  - courses: MT 314 ⟵ “MT 314 - Social Innovation and Entrepreneurship”
  - courses: TH 311 ⟵ “TH 311 - Sustainable Hospitality Management”
### `d9dc755b0b273456` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=program-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
- issues: course_alternatives_in_rule_text
  - courses: AC 114 ⟵ “AC 114 - 🌐 Accounting I”
  - courses: AC 116 ⟵ “AC 116 - 🌐 Accounting II”
  - courses: BU 204 ⟵ “BU 204 - 🌐 Macroeconomics”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 217 ⟵ “MT 217 - 🌐 Finance”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: LS 311 ⟵ “LS 311 - 🌐 Business Law”
  - courses: MM 305 ⟵ “MM 305 - 🌐 Business Statistics and Quantitative Analysis”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 400 ⟵ “MT 400 - 🌐 Business Process Management”
  - courses: MT 445 ⟵ “MT 445 - 🌐 Managerial Economics”
  - courses: MT 460 ⟵ “MT 460 - 🌐 Management Strategy and Policy”
  - courses: MT 499 ⟵ “MT 499 - Bachelor's Capstone in Management”
### `fdde2d5cd278772f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=human-resources [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
- issues: course_alternatives_in_rule_text
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: HR 400 ⟵ “HR 400 - 🌐 Talent Acquisition and Management”
  - courses: HR 410 ⟵ “HR 410 - Talent Development and Learning”
  - courses: HR 420 ⟵ “HR 420 - Workplace Law, Labor Relations, and HR Risk Management”
  - courses: HR 485 ⟵ “HR 485 - 🌐 Strategic HRM: Analytics and Business Decision-Making”
### `c277abe78e9ed8d0` Purdue University Northwest — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.pnw.edu/financial-aid/resources/satisfactory-academic-progress/ (sha256 a7d3d7f25503)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Students on Satisfactory Academic Progress Probation must update their Academic Advisor Verification each semester with your Academic Advisor and submit it to the Office of Financial Aid; Ineligible – you are not eligible for financial aid until you once again meet all Satisfactory Academic Progress requirements or have an approved appeal and academic plan.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals Students who need to appeal an ineligible status may use the Satisfactory Academic Progress packet which includes the Appeal Procedures, Appeal Form, Academic Plan Success Contract and Academic Advisor Verification.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Packet – for students appealing an ineligible Satisfactory Academic Progress status (available on request from the Office of Financial Aid) Satisfactory Academic Progress Academic Advisor Verification– for students currently on Satisfactory Academic Progress probation.”
  - sentence: sap_appeal ⟵ “Students on Satisfactory Academic Progress Probation must update their Academic Advisor Verification each semester with your Academic Advisor and submit it to the Office of Financial Aid (available on request from the Office of Financial Aid) Written statements submitted with the Satisfactory Academic Progress appeal should follow the format below: Explain the situation which affected your academi”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Process Student financial aid recipients who fail to maintain the Quantitative and/or Qualitative component(s) of the Satisfactory Academic Progress policy due to circumstances beyond their control may submit an appeal to the Office of Financial Aid explaining their situation.”
  - sentence: sap_appeal ⟵ “A student may submit only ONE Satisfactory Academic Progress appeal as an undergraduate and ONE as a graduate student, per instance of ineligibility.”
### `m6195447aa1bdf8e` Purdue University Northwest — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.pnw.edu/admissions/undergraduate/transfer-to-pnw/transfer-partners/transferring-from-ivy-tech/ivy-tech-to-pnw-transfer-guide-baking-and-pastry-arts/ (sha256 17b4235bd254)
- issues: conflicting_sources:min_grade
- checks: {"fields": ["min_grade"], "merged_pages": 4}
  - min_grade: C ⟵ “A course grade of “C” or better must be earned to be accepted for transfer.”
  - min_grade: C ⟵ “For Engr. (3 credits) PHIL 32400 – Ethics for the Professions (3 credits) ECE 42900 – Senior Engineering Design I (3 credits) ECE 43900 – Senior Engineering Design II (3 credits) Total Technology Credits to be taken at PNW: 62 Additional Transfer Guidelines Students must have earned a course grade of “C” or better on every course accepted for transfer Students also must have achieved a 2.5 or grea”
  - min_grade: C- ⟵ “For Engr. (3 credits) PHIL 32400 – Ethics for the Professions (3 credits) ECE 42900 – Senior Engineering Design I (3 credits) ECE 43900 – Senior Engineering Design II (3 credits) Total Technology Credits to be taken at PNW: 57 Minimum Required Credits to Complete Bachelor of Science in Electrical Engineering Degree: 120 Additional Transfer Guidelines Students must have earned a course grade of “C-”
  - min_grade: C ⟵ “A course grade of “C” or better must be earned to be accepted for transfer.”
### `48f33d5fb4b2adda` Purdue University-Main Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/contact/policiesappeals/ (sha256 6133134e4016)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: need_based_special_circumstances ⟵ “Provisionally Independent Students who indicate that they have other circumstances or unusual circumstances on the FAFSA will be considered provisionally independent.”
  - sentence: need_based_special_circumstances ⟵ “Student Unusual Circumstances Students may be considered independent if a financial aid administrator determines and documents the student’s independent status based on unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances may include: Leaving home due to an abusive or threatening environment.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances DO NOT include: Parents refuse to contribute to the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “If a student has unusual circumstances and did not answer “Yes” to question 7 on the FAFSA, they may still appeal dependency status.”
  - sentence: need_based_special_circumstances ⟵ “Students with unusual circumstances should contact a Division of Financial Aid (DFA) counselor at (765) 494-5050 to discuss their unusual circumstance and the dependency status appeal (DSA) process, how to obtain an appeal form, and what documentation to provide based on their circumstances.”
### `740f0c899128f3f4` Purdue University-Main Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/contact/policiesappeals/ (sha256 6133134e4016)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: budget_increase ⟵ “Budget Adjustment The Division of Financial Aid (DFA) calculates an estimated Cost of Attendance (COA), or budget, for financial aid applicants based on federal guidelines.”
  - sentence: budget_increase ⟵ “We cannot consider the following types of expenses: Those incurred or paid by roommates Those incurred for spouses, children or other family members Car payments or credit card payments Expenses incurred outside of the current enrollment period Medical expenses Timeframes Summer Budget Adjustment Appeals will be available in May and should be submitted 3 weeks prior to your last day of summer enro”
  - sentence: budget_increase ⟵ “Academic Year Budget Adjustment Appeals will be available in July.”
  - sentence: budget_increase ⟵ “For fall-only enrollment, Budget Adjustment Appeals should be submitted by the third Friday in November to ensure adequate time to process additional financial aid.”
  - sentence: budget_increase ⟵ “For spring-only or academic year enrollment, Budget Adjustments Appeals should be submitted by the first Friday in April to ensure adequate time to process additional financial aid.”
  - sentence: budget_increase ⟵ “Important Notes All expenses submitted for a Budget Adjustment Appeal must be incurred and paid during your enrollment period.”
### `85db374d7fa465e2` Purdue University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.purdue.edu/cost-financial-aid/scholarships/ (sha256 2a5ebc736485)
- issues: semantic_review_required
- checks: {"negative_sentences": 1, "sentences": 1}
  - sentence: competing_offer_review ⟵ “Purdue does not match offers from other institutions and does not consider appeals for merit aid.”
### `9dd9687bf8fe1031` Purdue University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.purdue.edu/dfa/manage/ (sha256 b9695172bf56)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal Process A student denied financial aid based on the satisfactory academic progress policy may submit a written appeal through Purdue’s verification portal.”
  - sentence: sap_appeal ⟵ “Students must submit their completed SAP appeal and all documentation by the following deadline of the applicable term for the SAP appeal: For Summer Terms: July 15th For Fall Terms: November 15th For Spring Terms: April 15th *If this date falls on a weekend, the deadline is end of business on the first business day after it.”
### `a1971abb82510ee4` Purdue University-Main Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/contact/policiesappeals/ (sha256 6133134e4016)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Unusual circumstances are circumstances which, in the professional judgment of a financial aid administrator, warrant the student to be considered independent.”
### `de1f5b43a9c5b7b0` Purdue University-Main Campus — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/ (sha256 75815e2cda3d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you experience income loss, such as a job change or job loss due to COVID-19, contact the Division of Financial Aid to see if a special circumstance appeal is a possibility.”
  - sentence: need_based_special_circumstances ⟵ “Please note that you must be out of work or experiencing an income loss for at least 8 weeks for us to be able to consider it a special circumstance.”
### `e8fec55da453c29e` Purdue University-Main Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/contact/policiesappeals/ (sha256 6133134e4016)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Students must participate in a homeless youth determination interview or complete the Dependency Status Appeal (DSA) process for a final determination of dependency.”
### `83ec4c839c97f88e` Rose-Hulman Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-basics/understanding-financial-aid/satisfactory-academic-progress.html (sha256 6b09851654be)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP Appeals A student may appeal the termination of aid eligibility if extenuating circumstances existed that prevented normal academic success of successful completion of the terms of SAP.”
  - sentence: sap_appeal ⟵ “To appeal, the student must complete the SAP Appeal Form, which allows the student to explain and document extenuating circumstance and develop an Academic Plan in consultation with an academic advisor.”
### `88567d33accabe17` Rose-Hulman Institute of Technology — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/pdfs/2025-2026_Special_Circumstances.pdf (sha256 11e9a38e8705)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “OFFICE OF FINANCIAL AID 2025-2026 Request for Consideration of Special Circumstances Student Name: ID: Sometimes families experience special circumstances which merit recalculation of their financial aid eligibility based on the 2024 or 2025 information rather than the federally required 2023 information.”
  - sentence: need_based_special_circumstances ⟵ “Complete and submit this Special Circumstance Form to the Financial Aid Office. 3.”
### `9116fb9f3f36566e` Rose-Hulman Institute of Technology — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/pdfs/2026-2027_Special_Circumstances.pdf (sha256 35312da55f46)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Please be advised that all professional judgment appeal decisions are final.”
### `923af6d7adc23ec4` Rose-Hulman Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-basics/financial-aid-faqs.html (sha256 300d92bd4377)
- issues: semantic_review_required, conflicting_sources:https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-basics/understanding-financial-aid/special-circumstances.html,https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/index.html,https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/pdfs/2026-2027_Special_Circumstances.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Open Close This is a need-based grant that can be re-evaluated each year or with every change in your financial need.”
### `9c7a6dae9370e952` Rose-Hulman Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-basics/understanding-financial-aid/special-circumstances.html (sha256 52285757386b)
- issues: semantic_review_required, conflicting_sources:https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-basics/financial-aid-faqs.html,https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/index.html,https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/pdfs/2026-2027_Special_Circumstances.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances | Rose-Hulman Special Circumstances Home Admissions & Aid Financial Aid Financial Aid Basics Understanding Financial Aid Special Circumstances Special Circumstances Have Your Family’s Finances Changed?”
  - sentence: need_based_special_circumstances ⟵ “If your family has had special circumstances, you may be eligible to request a review of your financial aid using updated information instead of the federally required data used for the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “If your Student Aid Index (SAI) is 0 or below, you are already receiving the maximum need-based aid available from Rose-Hulman and do not need to complete the Special Circumstance process.”
  - sentence: need_based_special_circumstances ⟵ “Complete the Special Circumstance Form and submit the required documentation to the Financial Aid Office via fax, postal mail, or in person.”
  - sentence: need_based_special_circumstances ⟵ “Rose-Hulman Institute of Technology 5500 Wabash Avenue CM 5 Terre Haute, IN 47803 Fax: 812-877-8672 You may request a special circumstance review at any point in the academic year, as circumstances may change at any time.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance submissions for the upcoming school year will not be reviewed until after Financial Aid Notifications are released to returning students in mid-June.”
### `cc3f83d6f70a452f` Rose-Hulman Institute of Technology — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/pdfs/2025-2026_Special_Circumstances.pdf (sha256 11e9a38e8705)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Please be advised that all professional judgment appeal decisions are final.”
### `cdcb85a22a423ef1` Rose-Hulman Institute of Technology — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/pdfs/2026-2027_Special_Circumstances.pdf (sha256 35312da55f46)
- issues: semantic_review_required, conflicting_sources:https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-basics/financial-aid-faqs.html,https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-basics/understanding-financial-aid/special-circumstances.html,https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/index.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “OFFICE OF FINANCIAL AID 2026-2027 Request for Consideration of Special Circumstances Student Name: ID: Sometimes families experience special circumstances which merit recalculation of their financial aid eligibility based on the 2025 or 2026 information rather than the federally required 2024 information.”
  - sentence: need_based_special_circumstances ⟵ “Complete and submit this Special Circumstance Form to the Financial Aid Office. 3.”
### `f87246cd104e9651` Rose-Hulman Institute of Technology — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/index.html (sha256 fae9de38ca8a)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-basics/financial-aid-faqs.html,https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-basics/understanding-financial-aid/special-circumstances.html,https://www.rose-hulman.edu/admissions-and-aid/financial-aid/financial-aid-forms/pdfs/2026-2027_Special_Circumstances.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A pre-transfer credit approval is required in addition to this form. 2025-2026 Financial Aid Forms 2025-2026 Special Circumstances This form is used if your family incurs a loss of income or benefits or incurs unusual medical expenses that will affect your ability to pay for college tuition.”
### `0cac555314665b95` Saint Mary's College — academic_programs 2026-27 · program_key=business-administration-bachelor-of-business-administration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/business-administration-bba/ (sha256 02555618d0ed)
- issues: requirement_groups_skipped
- checks: {"courses": 68, "groups": 8, "groups_skipped": 1}
  - program_name: Business Administration, Bachelor of Business Administration ⟵ “Business Administration, Bachelor of Business Administration - Concentrations in Accounting, Finance, International Business, Management, Management Information Systems, or Marketing - BUAD | Saint Ma”
### `30488634dca14186` Saint Mary's College — academic_programs 2026-27 · program_key=management-concentration-bachelor-of-business-administration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/management-concentration-bba/ (sha256 97110e2334f3)
- issues: requirement_groups_skipped
- checks: {"courses": 20, "groups": 3, "groups_skipped": 1}
  - program_name: Management Concentration, Bachelor of Business Administration ⟵ “Management Concentration, Bachelor of Business Administration - MGMT | Saint Mary's College, Notre Dame, IN”
### `61d8373b6a437789` Saint Mary's College — academic_programs 2026-27 · program_key=biology-integrative-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/integrative-biology-bachelor-science/ (sha256 6545a284081e)
- issues: requirement_groups_skipped
- checks: {"courses": 29, "groups": 7, "groups_skipped": 1}
  - program_name: Biology, Integrative, Bachelor of Science ⟵ “Biology, Integrative, Bachelor of Science - BIO | Saint Mary's College, Notre Dame, IN”
### `6a525dcab13287f0` Saint Mary's College — academic_programs 2026-27 · program_key=finance-concentration-bachelor-of-business-administration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/finance-concentration-bba/ (sha256 be6114dba02d)
- issues: requirement_groups_skipped
- checks: {"courses": 21, "groups": 3, "groups_skipped": 1}
  - program_name: Finance Concentration, Bachelor of Business Administration ⟵ “Finance Concentration, Bachelor of Business Administration - FIN | Saint Mary's College, Notre Dame, IN”
### `7444e0bc0cc9c50b` Saint Mary's College — academic_programs 2026-27 · program_key=management-information-systems-concentration-bachelor-of-business-administration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/management-information-systems-concentration-bba/ (sha256 928076ac397a)
- issues: requirement_groups_skipped
- checks: {"courses": 19, "groups": 3, "groups_skipped": 1}
  - program_name: Management Information Systems Concentration, Bachelor of Business Administration ⟵ “Management Information Systems Concentration, Bachelor of Business Administration - MIS | Saint Mary's College, Notre Dame, IN”
### `a6f0bd807e3ca1b9` Saint Mary's College — academic_programs 2026-27 · program_key=accounting-concentration-bachelor-of-business-administration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/accounting-concentration-bba/ (sha256 12db7a8bc572)
- issues: requirement_groups_skipped
- checks: {"courses": 24, "groups": 3, "groups_skipped": 1}
  - program_name: Accounting Concentration, Bachelor of Business Administration ⟵ “Accounting Concentration, Bachelor of Business Administration - ACTC | Saint Mary's College, Notre Dame, IN”
### `abfc7e93b00e2066` Saint Mary's College — academic_programs 2026-27 · program_key=marketing-concentration-bachelor-of-business-administration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/marketing-concentration-bba/ (sha256 64d2fe51df8a)
- issues: requirement_groups_skipped
- checks: {"courses": 25, "groups": 3, "groups_skipped": 1}
  - program_name: Marketing Concentration, Bachelor of Business Administration ⟵ “Marketing Concentration, Bachelor of Business Administration - MKT | Saint Mary's College, Notre Dame, IN”
### `f16cda00c03de412` Saint Mary's College — academic_programs 2026-27 · program_key=international-business-concentration-bachelor-of-business-administration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/international-business-concentration-bba/ (sha256 4b6124cea0c8)
- issues: requirement_groups_skipped
- checks: {"courses": 19, "groups": 3, "groups_skipped": 1}
  - program_name: International Business Concentration, Bachelor of Business Administration ⟵ “International Business Concentration, Bachelor of Business Administration - INTB | Saint Mary's College, Notre Dame, IN”
### `ddcbfa2c1c5000ea` Saint Mary's College — appeals 2025-26 [new] (labeled_in_heading)
- source: https://www.saintmarys.edu/admission-aid/financial-aid/faq (sha256 dc16f1d8f2cf)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Deadline for verification paperwork is April 1. *Awards under appeal for special circumstances may take longer.”
  - sentence: need_based_special_circumstances ⟵ “These students will receive a paper letter mailed to their permanent addresses. *Awards under appeal, for special circumstances or other reviews, may take longer. **Grades from spring or year-long study abroad programs are sometimes delayed in reaching the College.”
### `d7c4fc08a994fe05` Saint Mary's College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.saintmarys.edu/admission-aid/financial-aid/veteran-benefits (sha256 a84088142740)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - column:Chapter 33: 30908.34 ⟵ “Chapter 33 | $28,573.00 | $ 2,335.34 | $30,908.34”
  - column:SMC Yellow Ribbon: 13018.83 ⟵ “SMC Yellow Ribbon | $0 | $ 13,018.83 | $ 13,018.83”
  - column:VA Yellow Ribbon Match: 13018.83 ⟵ “VA Yellow Ribbon Match | $0 | $ 13,018.83 | $ 13,018.83”
  - column:Total Chapter 33 + Yellow Ribbon: 56946.0 ⟵ “Total Chapter 33 + Yellow Ribbon | $28,573.00 | $28,373.00 | $56,946.00”
  - column:Tuition and Fees: 56946.0 ⟵ “Tuition and Fees | $28,573.00 | $28,373.00 | $56,946.00”
### `f769e5173e815401` Saint Mary's College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.saintmarys.edu/admission-aid/financial-aid/faq (sha256 dc16f1d8f2cf)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 4}
  - on_campus:Tuition & Fees: 55093 ⟵ “Tuition & Fees | $55,093”
  - on_campus:Orientation Fee: 200 ⟵ “Orientation Fee | $200”
  - on_campus:Food & Housing(weighted average cost of all housing options): 15026 ⟵ “Food & Housing(weighted average cost of all housing options) | $15,026”
  - on_campus:Estimated Direct Expenses: 70119 ⟵ “Estimated Direct Expenses | $70,119”
### `018b3d4384585d66` Saint Mary's College — degree_requirements 2026-27 · program_key=ecology-evolution-and-environmental-biology-concentration-bachelor-of-science · requirement_key=major-requirements-60-hours-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/ecology-evolution-environmental-biology-concentration-bachelor-science/ (sha256 2bd059a8e87e)
- issues: course_alternatives_in_rule_text
  - courses: BIO 160 ⟵ “BIO 160 - Science Writing and Communication”
  - courses: BIO 235 ⟵ “BIO 235 - Foundations of Neuroscience”
  - courses: BIO 240 ⟵ “BIO 240 - Cats’ Paws and Catapults: Animal Biomechanics”
  - courses: BIO 245 ⟵ “BIO 245 - We Like to Move It (Move it): Introduction to Kinesiology”
  - courses: BIO 270 ⟵ “BIO 270 - Environments of Ecuador”
  - courses: BIO 318 ⟵ “BIO 318 - Immunology”
  - courses: BIO 330 ⟵ “BIO 330 - Seminar in Molecular/Cellular Biology”
  - courses: BIO 410 ⟵ “BIO 410 - Pathophysiology”
  - courses: BIO 412 ⟵ “BIO 412 - Emerging Infectious Diseases and Their Impact on Global Health”
  - courses: BIO 417 ⟵ “BIO 417 - Cancer Biology”
  - courses: BIO 497 ⟵ “BIO 497 - Independent Study”
  - courses: BIO 499 ⟵ “BIO 499 - Internship”
  - courses: NEUR 340 ⟵ “NEUR 340 - Neurophysiology”
### `063799eab7a9bde4` Saint Mary's College — degree_requirements 2026-27 · program_key=cellular-molecular-biology-concentration-bachelor-of-science · requirement_key=major-requirements-60-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/cellular-molecular-biology-concentration-bachelor-science/ (sha256 345f5d902b16)
- issues: course_alternatives_in_rule_text
  - courses: BIO 330 ⟵ “BIO 330 - Seminar in Molecular/Cellular Biology”
  - courses: BIO 385 ⟵ “BIO 385 - Introduction to Research”
  - courses: BIO 485 ⟵ “BIO 485 - Research in Biology”
### `075010b405150ff5` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-fibers-textiles [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
- issues: course_alternatives_in_rule_text
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 338 ⟵ “ART 338 - Advanced Fiber: Surface Design”
  - courses: ART 339 ⟵ “ART 339 - Advanced Fibers: Fabric Printing + Needle Arts”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
### `0fa3138d8009d0b5` Saint Mary's College — degree_requirements 2026-27 · program_key=international-business-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-other-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/international-business-concentration-bba/ (sha256 4b6124cea0c8)
- issues: requirement_groups_skipped
  - courses: BUAD 202 ⟵ “BUAD 202 - Principles of Managerial Accounting”
  - courses: BUAD 346 ⟵ “BUAD 346 - Business & Organizational Ethics”
  - courses: BUAD 446 ⟵ “BUAD 446 - Strategic Management”
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `108eb66cecaa349a` Saint Mary's College — degree_requirements 2026-27 · program_key=biology-integrative-bachelor-of-science · requirement_key=major-requirements-60-hours-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/integrative-biology-bachelor-science/ (sha256 6545a284081e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIO 160 ⟵ “BIO 160 - Science Writing and Communication”
  - courses: BIO 235 ⟵ “BIO 235 - Foundations of Neuroscience”
  - courses: BIO 240 ⟵ “BIO 240 - Cats’ Paws and Catapults: Animal Biomechanics”
  - courses: BIO 248 ⟵ “BIO 248 - Issues in Environmental Biology”
  - courses: BIO 270 ⟵ “BIO 270 - Environments of Ecuador”
  - courses: BIO 315 ⟵ “BIO 315 - Statistical Methods for Biologists”
  - courses: BIO 318 ⟵ “BIO 318 - Immunology”
  - courses: BIO 330 ⟵ “BIO 330 - Seminar in Molecular/Cellular Biology”
  - courses: BIO 340 ⟵ “BIO 340 - Medical Terminology”
  - courses: BIO 410 ⟵ “BIO 410 - Pathophysiology”
  - courses: BIO 412 ⟵ “BIO 412 - Emerging Infectious Diseases and Their Impact on Global Health”
  - courses: BIO 417 ⟵ “BIO 417 - Cancer Biology”
  - courses: BIO 497 ⟵ “BIO 497 - Independent Study”
  - courses: BIO 499 ⟵ “BIO 499 - Internship”
  - courses: NEUR 340 ⟵ “NEUR 340 - Neurophysiology”
### `10e0087cf0a37ff7` Saint Mary's College — degree_requirements 2026-27 · program_key=business-administration-bachelor-of-business-administration · requirement_key=finance-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/business-administration-bba/ (sha256 02555618d0ed)
- issues: requirement_groups_skipped
  - courses: BUAD 311 ⟵ “BUAD 311 - Corporate Financial Decision Making”
  - courses: BUAD 313 ⟵ “BUAD 313 - Investments”
  - courses: BUAD 314 ⟵ “BUAD 314 - Personal Financial Planning”
  - courses: BUAD 315 ⟵ “BUAD 315 - Management of Financial Institutions”
  - courses: BUAD 316 ⟵ “BUAD 316 - Financial Strategy with Computer Applications”
  - courses: BUAD 317 ⟵ “BUAD 317 - Financial Statement Analysis”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 416 ⟵ “BUAD 416 - International Financial Management”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
### `12dccf3172e5efe0` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-fibers-textiles [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-fine-arts/ (sha256 4cd810a6ea34)
- issues: course_alternatives_in_rule_text
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 338 ⟵ “ART 338 - Advanced Fiber: Surface Design”
  - courses: ART 339 ⟵ “ART 339 - Advanced Fibers: Fabric Printing + Needle Arts”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
### `1928e71c7c87aa0f` Saint Mary's College — degree_requirements 2026-27 · program_key=exercise-science-health-and-fitness-bachelor-of-arts · requirement_key=exercise-science-health-and-fitness-bachelor-of-arts-exhf-supporting-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/exercise-science/health-fitness-bachelor-arts/ (sha256 4448a4c853a9)
- issues: course_alternatives_in_rule_text
  - courses: CHEM 118 ⟵ “CHEM 118 - Integrated General, Organic and Bio-Chemistry”
  - courses: NURS 310 ⟵ “NURS 310 - Nutrition for Health and Healing”
  - courses: PSYC 156 ⟵ “PSYC 156 - Introduction to Psychology: Culture and Systems”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
  - courses: BIO 240 ⟵ “BIO 240 - Cats’ Paws and Catapults: Animal Biomechanics”
  - courses: BIO 318 ⟵ “BIO 318 - Immunology”
  - courses: BIO 340 ⟵ “BIO 340 - Medical Terminology”
  - courses: BIO 417 ⟵ “BIO 417 - Cancer Biology”
### `1e880f92fb97839f` Saint Mary's College — degree_requirements 2026-27 · program_key=physics-bachelor-of-arts · requirement_key=major-requirements-38-42-hours-required-supporting-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/physics-bachelor-arts/ (sha256 a792cff99ffc)
- issues: course_alternatives_in_rule_text
  - courses: MATH 133 ⟵ “MATH 133 - Theory and Application of Calculus”
  - courses: MATH 231 ⟵ “MATH 231 - Calculus III”
  - courses: MATH 326 ⟵ “MATH 326 - Linear Algebra and Differential Equations”
### `1ea5768c56399769` Saint Mary's College — degree_requirements 2026-27 · program_key=marketing-concentration-bachelor-of-business-administration · requirement_key=marketing-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/marketing-concentration-bba/ (sha256 64d2fe51df8a)
- issues: requirement_groups_skipped
  - courses: BUAD 331 ⟵ “BUAD 331 - Advertising and Promotion”
  - courses: BUAD 332 ⟵ “BUAD 332 - Social Media Marketing”
  - courses: BUAD 333 ⟵ “BUAD 333 - Market Research”
  - courses: BUAD 334 ⟵ “BUAD 334 - Consumer Behavior”
  - courses: BUAD 335 ⟵ “BUAD 335 - Supply Chain Marketing”
  - courses: BUAD 336 ⟵ “BUAD 336 - Brand Management”
  - courses: BUAD 342 ⟵ “BUAD 342 - New Venture”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 433 ⟵ “BUAD 433 - Global Digital Marketing”
  - courses: BUAD 434 ⟵ “BUAD 434 - Sales Management and Professional Selling”
  - courses: BUAD 437 ⟵ “BUAD 437 - Artificial Intelligence Marketing”
  - courses: BUAD 438 ⟵ “BUAD 438 - Service Marketing”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
### `20bfb5a233933c63` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-minor-for-b-a-studio-art-majors · requirement_key=minor-requirements-21-hours-upper-level-art-history [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-minor-studio-art-majors/ (sha256 50dfbae04f79)
- issues: course_alternatives_in_rule_text
  - courses: ART 343 ⟵ “ART 343 - History of Photography”
  - courses: ART 344 ⟵ “ART 344 - Film History and Analysis”
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
  - courses: ART 499 ⟵ “ART 499 - Internship”
### `23d88b30473c0abb` Saint Mary's College — degree_requirements 2026-27 · program_key=chemistry-bachelor-of-science · requirement_key=major-requirements-56-hours-required-supporting-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/chemistry-bachelor-science/ (sha256 5d09474a83b4)
- issues: course_alternatives_in_rule_text
  - courses: MATH 131 ⟵ “MATH 131 - Calculus I (or equivalent)”
  - courses: MATH 132 ⟵ “MATH 132 - Calculus II (or equivalent)”
### `24ba5969f1596b74` Saint Mary's College — degree_requirements 2026-27 · program_key=management-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-other-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/management-concentration-bba/ (sha256 97110e2334f3)
- issues: requirement_groups_skipped
  - courses: BUAD 202 ⟵ “BUAD 202 - Principles of Managerial Accounting”
  - courses: BUAD 346 ⟵ “BUAD 346 - Business & Organizational Ethics”
  - courses: BUAD 446 ⟵ “BUAD 446 - Strategic Management”
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `25021085e1997187` Saint Mary's College — degree_requirements 2026-27 · program_key=finance-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/finance-concentration-bba/ (sha256 be6114dba02d)
- issues: requirement_groups_skipped
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 212 ⟵ “BUAD 212 - Principles of Finance”
  - courses: BUAD 221 ⟵ “BUAD 221 - Principles of Management”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 245 ⟵ “BUAD 245 - Business Communication”
  - courses: BUAD 247 ⟵ “BUAD 247 - Introduction to Excel, Statistics, and Business Analytics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
### `2858dfdc7eb3a768` Saint Mary's College — degree_requirements 2026-27 · program_key=business-administration-bachelor-of-business-administration · requirement_key=management-information-systems-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/business-administration-bba/ (sha256 02555618d0ed)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CPSC 207 ⟵ “CPSC 207 - Computer Programming”
  - courses: CPSC 417 ⟵ “CPSC 417 - Systems Analysis and Design”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
  - courses: CPSC 308 ⟵ “CPSC 308 - Electronic Communications”
  - courses: CPSC 315 ⟵ “CPSC 315 - Simulation: Theory and Application”
  - courses: CPSC 417 ⟵ “CPSC 417 - Systems Analysis and Design (if not taken above)”
### `29461505db188017` Saint Mary's College — degree_requirements 2026-27 · program_key=cellular-molecular-biology-concentration-bachelor-of-science · requirement_key=major-requirements-60-hours-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/cellular-molecular-biology-concentration-bachelor-science/ (sha256 345f5d902b16)
- issues: course_alternatives_in_rule_text
  - courses: BIO 160 ⟵ “BIO 160 - Science Writing and Communication”
  - courses: BIO 240 ⟵ “BIO 240 - Cats’ Paws and Catapults: Animal Biomechanics”
  - courses: BIO 245 ⟵ “BIO 245 - We Like to Move It (Move it): Introduction to Kinesiology”
  - courses: BIO 248 ⟵ “BIO 248 - Issues in Environmental Biology”
  - courses: BIO 270 ⟵ “BIO 270 - Environments of Ecuador”
  - courses: BIO 312 ⟵ “BIO 312 - Evolution”
  - courses: BIO 315 ⟵ “BIO 315 - Statistical Methods for Biologists”
  - courses: BIO 318 ⟵ “BIO 318 - Immunology”
  - courses: BIO 340 ⟵ “BIO 340 - Medical Terminology”
  - courses: BIO 410 ⟵ “BIO 410 - Pathophysiology”
  - courses: BIO 412 ⟵ “BIO 412 - Emerging Infectious Diseases and Their Impact on Global Health”
  - courses: BIO 417 ⟵ “BIO 417 - Cancer Biology”
  - courses: BIO 497 ⟵ “BIO 497 - Independent Study”
  - courses: BIO 499 ⟵ “BIO 499 - Internship”
  - courses: NEUR 340 ⟵ “NEUR 340 - Neurophysiology”
### `2c069361f3b24d0f` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-ceramics [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-arts---arad/ (sha256 d11b8e1fa54c)
- issues: course_alternatives_in_rule_text
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 311 ⟵ “ART 311 - Advanced Ceramics: Hand Building and Slip Casting”
  - courses: ART 411 ⟵ “ART 411 - Alternative Processes in Ceramics”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
### `2c7ebbad6b1daa06` Saint Mary's College — degree_requirements 2026-27 · program_key=biology-integrative-bachelor-of-science · requirement_key=major-requirements-60-hours-one-of-the-following-to-fulfill-upper-level-research [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/integrative-biology-bachelor-science/ (sha256 6545a284081e)
- issues: requirement_groups_skipped
  - courses: BIO 209 ⟵ “BIO 209 - Marine Biology”
  - courses: BIO 230 ⟵ “BIO 230 - Molecular Cell Biology”
  - courses: BIO 232 ⟵ “BIO 232 - Animal Behavior”
  - courses: BIO 316 ⟵ “BIO 316 - Conservation Biology”
  - courses: BIO 323 ⟵ “BIO 323 - Ecology”
  - courses: BIO 335 ⟵ “BIO 335 - Plant-Animal Interactions”
### `2e0bec5996bf7080` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-photo-media [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
- issues: course_alternatives_in_rule_text
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 321 ⟵ “ART 321 - Photography II: Lighting Workshop”
  - courses: ART 323 ⟵ “ART 323 - Photo-Silkscreen”
  - courses: ART 357 ⟵ “ART 357 - Holography Workshop”
  - courses: ART 421 ⟵ “ART 421 - Photography III: Beyond the Frame”
### `32398a03bd8eb370` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-ceramics [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
- issues: course_alternatives_in_rule_text
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 311 ⟵ “ART 311 - Advanced Ceramics: Hand Building and Slip Casting”
  - courses: ART 411 ⟵ “ART 411 - Alternative Processes in Ceramics”
### `32c1ac2fab08f40a` Saint Mary's College — degree_requirements 2026-27 · program_key=design-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-studio-requirements-in-design [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-concentration-bachelor-fine-arts/ (sha256 83cfddcbe154)
- issues: course_alternatives_in_rule_text
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 385 ⟵ “ART 385 - Design Research Methods”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art”
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - … 15 more rows
### `36af47aac6b73968` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-studio-requirements-in-applied-arts-design [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-arts---arad/ (sha256 d11b8e1fa54c)
- issues: course_alternatives_in_rule_text
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 385 ⟵ “ART 385 - Design Research Methods”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art”
### `38212034e396b581` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-sculpture [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
- issues: course_alternatives_in_rule_text
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 374 ⟵ “ART 374 - Landscape Architecture II”
  - courses: ART 417 ⟵ “ART 417 - Advanced Sculpture”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
### `395097e91dc1b3b8` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-furniture-sculpture [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-arts---arad/ (sha256 d11b8e1fa54c)
- issues: course_alternatives_in_rule_text
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 374 ⟵ “ART 374 - Landscape Architecture II”
  - courses: ART 417 ⟵ “ART 417 - Advanced Sculpture”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
  - courses: ART 343 ⟵ “ART 343 - History of Photography”
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
### `3ed834a433e43e4e` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-studio-requirements-in-applied-arts-design [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-fine-arts/ (sha256 4cd810a6ea34)
- issues: course_alternatives_in_rule_text
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 385 ⟵ “ART 385 - Design Research Methods”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art (Double majors who elect to complete the Sr Comp in their other major must take an additional 3 hours in studio in place of ART 495)”
### `4ad8b6706e22ba5d` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-furniture-sculpture [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
- issues: course_alternatives_in_rule_text
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 374 ⟵ “ART 374 - Landscape Architecture II”
  - courses: ART 417 ⟵ “ART 417 - Advanced Sculpture”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
### `50e0df4152aced9d` Saint Mary's College — degree_requirements 2026-27 · program_key=business-administration-bachelor-of-business-administration · requirement_key=accounting-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/business-administration-bba/ (sha256 02555618d0ed)
- issues: requirement_groups_skipped
  - courses: BUAD 301 ⟵ “BUAD 301 - Intermediate Accounting I”
  - courses: BUAD 302 ⟵ “BUAD 302 - Intermediate Accounting II”
  - courses: BUAD 303 ⟵ “BUAD 303 - Cost Accounting”
  - courses: BUAD 304 ⟵ “BUAD 304 - Personal Income Tax”
  - courses: BUAD 305 ⟵ “BUAD 305 - Accounting for Not-for-Profit Organizations”
  - courses: BUAD 306 ⟵ “BUAD 306 - Fraud Examination”
  - courses: BUAD 344 ⟵ “BUAD 344 - Business Law I”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 401 ⟵ “BUAD 401 - Advanced Accounting”
  - courses: BUAD 402 ⟵ “BUAD 402 - Auditing”
  - courses: BUAD 404 ⟵ “BUAD 404 - Advanced Topics in Income Tax”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
### `538e4cc4614746c4` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-ceramics [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-fine-arts/ (sha256 4cd810a6ea34)
- issues: course_alternatives_in_rule_text
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 311 ⟵ “ART 311 - Advanced Ceramics: Hand Building and Slip Casting”
  - courses: ART 411 ⟵ “ART 411 - Alternative Processes in Ceramics”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
### `595fe863c7fbab3a` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-fibers [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
- issues: course_alternatives_in_rule_text
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 338 ⟵ “ART 338 - Advanced Fiber: Surface Design”
  - courses: ART 339 ⟵ “ART 339 - Advanced Fibers: Fabric Printing + Needle Arts”
### `5b3705c8d50e1cfa` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-photo-media [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
- issues: course_alternatives_in_rule_text
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 321 ⟵ “ART 321 - Photography II: Lighting Workshop”
  - courses: ART 323 ⟵ “ART 323 - Photo-Silkscreen”
  - courses: ART 357 ⟵ “ART 357 - Holography Workshop”
  - courses: ART 421 ⟵ “ART 421 - Photography III: Beyond the Frame”
### `5b72d9cbdbb571d6` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-photo-media [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
- issues: course_alternatives_in_rule_text
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 321 ⟵ “ART 321 - Photography II: Lighting Workshop”
  - courses: ART 323 ⟵ “ART 323 - Photo-Silkscreen”
  - courses: ART 357 ⟵ “ART 357 - Holography Workshop”
  - courses: ART 421 ⟵ “ART 421 - Photography III: Beyond the Frame”
### `5bbb531b2d742a85` Saint Mary's College — degree_requirements 2026-27 · program_key=biology-integrative-bachelor-of-science · requirement_key=major-requirements-60-hours-ecological-and-evolutionary-course [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/integrative-biology-bachelor-science/ (sha256 6545a284081e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIO 312 ⟵ “BIO 312 - Evolution”
### `5c4c6bde4d930ea5` Saint Mary's College — degree_requirements 2026-27 · program_key=business-administration-bachelor-of-business-administration · requirement_key=management-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/business-administration-bba/ (sha256 02555618d0ed)
- issues: requirement_groups_skipped
  - courses: BUAD 321 ⟵ “BUAD 321 - Human Resource Management”
  - courses: BUAD 322 ⟵ “BUAD 322 - Organizational Behavior”
  - courses: BUAD 329 ⟵ “BUAD 329 - Gender and Race Issues in Management”
  - courses: BUAD 342 ⟵ “BUAD 342 - New Venture”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 422 ⟵ “BUAD 422 - International Management”
  - courses: BUAD 427 ⟵ “BUAD 427 - Principles of Operations Research”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
### `5c834c6bab5f0bae` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-furniture-sculpture [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-fine-arts/ (sha256 4cd810a6ea34)
- issues: course_alternatives_in_rule_text
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 374 ⟵ “ART 374 - Landscape Architecture II”
  - courses: ART 417 ⟵ “ART 417 - Advanced Sculpture”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - … 15 more rows
### `6562cacd1344c15e` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-fibers-textiles [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-arts---arad/ (sha256 d11b8e1fa54c)
- issues: course_alternatives_in_rule_text
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 338 ⟵ “ART 338 - Advanced Fiber: Surface Design”
  - courses: ART 339 ⟵ “ART 339 - Advanced Fibers: Fabric Printing + Needle Arts”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
### `6d3d6b7df9bdf137` Saint Mary's College — degree_requirements 2026-27 · program_key=management-information-systems-concentration-bachelor-of-business-administration · requirement_key=management-information-systems-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/management-information-systems-concentration-bba/ (sha256 928076ac397a)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CPSC 207 ⟵ “CPSC 207 - Computer Programming”
  - courses: CPSC 417 ⟵ “CPSC 417 - Systems Analysis and Design”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
  - courses: CPSC 308 ⟵ “CPSC 308 - Electronic Communications”
  - courses: CPSC 315 ⟵ “CPSC 315 - Simulation: Theory and Application”
  - courses: CPSC 417 ⟵ “CPSC 417 - Systems Analysis and Design (if not taken above)”
### `6d9d90546c792f7f` Saint Mary's College — degree_requirements 2026-27 · program_key=education-elementary-k-6-bachelor-of-arts · requirement_key=major-requirements-65-hours-additional-required-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/education/elementary-k-6-bachelor-arts/ (sha256 fcf6cdecb2c0)
- issues: course_alternatives_in_rule_text
  - courses: HIST 103 ⟵ “HIST 103 - World History I”
  - courses: HIST 201 ⟵ “HIST 201 - United States History to 1865”
  - courses: MATH 118 ⟵ “MATH 118 - Patterns in Mathematics for Elementary Teachers”
  - courses: MATH 302 ⟵ “MATH 302 - Mathematics for Elementary School Teachers”
### `72e3bd7dc700e782` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-also-available-for-students-concentrating-in-art-des [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
- issues: course_alternatives_in_rule_text
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
  - courses: ART 499 ⟵ “ART 499 - Internship”
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - … 15 more rows
### `7553c65d1b1b6f7a` Saint Mary's College — degree_requirements 2026-27 · program_key=biology-integrative-bachelor-of-science · requirement_key=major-requirements-60-hours-cellular-physiological-course [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/integrative-biology-bachelor-science/ (sha256 6545a284081e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIO 417 ⟵ “BIO 417 - Cancer Biology”
### `7915fe61c708c354` Saint Mary's College — degree_requirements 2026-27 · program_key=education-elementary-education-non-licensure-bachelor-of-arts · requirement_key=major-requirements-65-hours-additional-required-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/education/elementary-non-licensure-bachelor-arts/ (sha256 66d51d63686e)
- issues: course_alternatives_in_rule_text
  - courses: HIST 103 ⟵ “HIST 103 - World History I”
  - courses: HIST 201 ⟵ “HIST 201 - United States History to 1865”
  - courses: MATH 118 ⟵ “MATH 118 - Patterns in Mathematics for Elementary Teachers”
  - courses: MATH 302 ⟵ “MATH 302 - Mathematics for Elementary School Teachers”
### `7a096eb77f6a5a84` Saint Mary's College — degree_requirements 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-studio-requirements-in-design [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
- issues: course_alternatives_in_rule_text
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art”
  - courses: ART 499 ⟵ “ART 499 - Internship”
### `7c818b02d3d09f4d` Saint Mary's College — degree_requirements 2026-27 · program_key=design-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-studio-requirements-in-design [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-concentration-bachelor-arts---arsd/ (sha256 9292668dde12)
- issues: course_alternatives_in_rule_text
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 499 ⟵ “ART 499 - Internship”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art *”
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - … 15 more rows
### `7fc4db2b11b66ac7` Saint Mary's College — degree_requirements 2026-27 · program_key=ecology-evolution-and-environmental-biology-concentration-bachelor-of-science · requirement_key=major-requirements-60-hours-for-students-who-could-use-college-calculus-prep-to- [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/ecology-evolution-environmental-biology-concentration-bachelor-science/ (sha256 2bd059a8e87e)
- issues: course_alternatives_in_rule_text
  - courses: MATH 103 ⟵ “MATH 103 - Precalculus”
### `83ba3418af13027c` Saint Mary's College — degree_requirements 2026-27 · program_key=international-business-concentration-bachelor-of-business-administration · requirement_key=international-business-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/international-business-concentration-bba/ (sha256 4b6124cea0c8)
- issues: requirement_groups_skipped
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 416 ⟵ “BUAD 416 - International Financial Management”
  - courses: BUAD 422 ⟵ “BUAD 422 - International Management”
  - courses: BUAD 433 ⟵ “BUAD 433 - Global Digital Marketing”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
  - courses: ECON 354 ⟵ “ECON 354 - Economic Development”
  - courses: ECON 452 ⟵ “ECON 452 - International Trade and Finance”
### `8488fd469cb59661` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-ceramics [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
- issues: course_alternatives_in_rule_text
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 311 ⟵ “ART 311 - Advanced Ceramics: Hand Building and Slip Casting”
  - courses: ART 411 ⟵ “ART 411 - Alternative Processes in Ceramics”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
### `848e352b71cb07e9` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-studio-requirements-in-applied-arts-design [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-art-history-double-concentration-bachelor-arts---asha/ (sha256 ffd9b7b155bd)
- issues: course_alternatives_in_rule_text
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 385 ⟵ “ART 385 - Design Research Methods”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art”
### `855058974d3c167f` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-sculpture [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
- issues: course_alternatives_in_rule_text
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 374 ⟵ “ART 374 - Landscape Architecture II”
  - courses: ART 417 ⟵ “ART 417 - Advanced Sculpture”
### `8d0d80a255ccf650` Saint Mary's College — degree_requirements 2026-27 · program_key=biology-integrative-bachelor-of-science · requirement_key=major-requirements-60-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/integrative-biology-bachelor-science/ (sha256 6545a284081e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIO 221 ⟵ “BIO 221 - Introduction to Genetics”
  - courses: BIO 385 ⟵ “BIO 385 - Introduction to Research”
  - courses: BIO 485 ⟵ “BIO 485 - Research in Biology”
### `8e1b01a478a7d336` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-fibers [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
- issues: course_alternatives_in_rule_text
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 338 ⟵ “ART 338 - Advanced Fiber: Surface Design”
  - courses: ART 339 ⟵ “ART 339 - Advanced Fibers: Fabric Printing + Needle Arts”
### `8e63afc2120de15c` Saint Mary's College — degree_requirements 2026-27 · program_key=accounting-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/accounting-concentration-bba/ (sha256 12db7a8bc572)
- issues: requirement_groups_skipped
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 212 ⟵ “BUAD 212 - Principles of Finance”
  - courses: BUAD 221 ⟵ “BUAD 221 - Principles of Management”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 245 ⟵ “BUAD 245 - Business Communication”
  - courses: BUAD 247 ⟵ “BUAD 247 - Introduction to Excel, Statistics, and Business Analytics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
### `9648782d58715c41` Saint Mary's College — degree_requirements 2026-27 · program_key=applied-arts-and-design-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-supporting-correlate-course-requirements [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/applied-arts-design-concentration-bachelor-fine-arts/ (sha256 4cd810a6ea34)
- issues: course_alternatives_in_rule_text
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 331 ⟵ “BUAD 331 - Advertising and Promotion”
  - courses: BUAD 342 ⟵ “BUAD 342 - New Venture”
  - courses: ENVS 161 ⟵ “ENVS 161 - Introduction to Environmental Studies”
  - courses: JUST 250 ⟵ “JUST 250 - Introduction to Justice Studies”
  - courses: PHIL 254 ⟵ “PHIL 254 - Social Justice”
  - courses: PHIL 256 ⟵ “PHIL 256 - Environmental Ethics”
  - courses: ART 343 ⟵ “ART 343 - History of Photography”
  - courses: ART 344 ⟵ “ART 344 - Film History and Analysis”
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
  - courses: ART 499 ⟵ “ART 499 - Internship”
### `978e5c1b7f1bca2c` Saint Mary's College — degree_requirements 2026-27 · program_key=business-administration-bachelor-of-business-administration · requirement_key=marketing-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/business-administration-bba/ (sha256 02555618d0ed)
- issues: requirement_groups_skipped
  - courses: BUAD 331 ⟵ “BUAD 331 - Advertising and Promotion”
  - courses: BUAD 332 ⟵ “BUAD 332 - Social Media Marketing”
  - courses: BUAD 333 ⟵ “BUAD 333 - Market Research”
  - courses: BUAD 334 ⟵ “BUAD 334 - Consumer Behavior”
  - courses: BUAD 335 ⟵ “BUAD 335 - Supply Chain Marketing”
  - courses: BUAD 336 ⟵ “BUAD 336 - Brand Management”
  - courses: BUAD 342 ⟵ “BUAD 342 - New Venture”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 433 ⟵ “BUAD 433 - Global Digital Marketing”
  - courses: BUAD 434 ⟵ “BUAD 434 - Sales Management and Professional Selling”
  - courses: BUAD 437 ⟵ “BUAD 437 - Artificial Intelligence Marketing”
  - courses: BUAD 438 ⟵ “BUAD 438 - Service Marketing”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
### `981890409e385359` Saint Mary's College — degree_requirements 2026-27 · program_key=business-administration-bachelor-of-business-administration · requirement_key=international-business-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/business-administration-bba/ (sha256 02555618d0ed)
- issues: requirement_groups_skipped
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 416 ⟵ “BUAD 416 - International Financial Management”
  - courses: BUAD 422 ⟵ “BUAD 422 - International Management”
  - courses: BUAD 433 ⟵ “BUAD 433 - Global Digital Marketing”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
  - courses: ECON 354 ⟵ “ECON 354 - Economic Development”
  - courses: ECON 452 ⟵ “ECON 452 - International Trade and Finance”
### `98f9bf93b118cd3d` Saint Mary's College — degree_requirements 2026-27 · program_key=cellular-molecular-biology-concentration-bachelor-of-science · requirement_key=major-requirements-60-hours-for-students-who-could-use-college-calculus-prep-to- [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/cellular-molecular-biology-concentration-bachelor-science/ (sha256 345f5d902b16)
- issues: course_alternatives_in_rule_text
  - courses: MATH 103 ⟵ “MATH 103 - Precalculus”
  - courses: BIO 209 ⟵ “BIO 209 - Marine Biology”
  - courses: BIO 230 ⟵ “BIO 230 - Molecular Cell Biology”
  - courses: BIO 232 ⟵ “BIO 232 - Animal Behavior”
  - courses: BIO 316 ⟵ “BIO 316 - Conservation Biology”
  - courses: BIO 323 ⟵ “BIO 323 - Ecology”
  - courses: BIO 335 ⟵ “BIO 335 - Plant-Animal Interactions”
### `992fa11c040ab35f` Saint Mary's College — degree_requirements 2026-27 · program_key=accounting-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-other-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/accounting-concentration-bba/ (sha256 12db7a8bc572)
- issues: requirement_groups_skipped
  - courses: BUAD 202 ⟵ “BUAD 202 - Principles of Managerial Accounting”
  - courses: BUAD 346 ⟵ “BUAD 346 - Business & Organizational Ethics”
  - courses: BUAD 446 ⟵ “BUAD 446 - Strategic Management”
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `9d4cfe38b34314a2` Saint Mary's College — degree_requirements 2026-27 · program_key=communication-studies-bachelor-of-arts · requirement_key=major-requirements-33-hours-senior-comprehensive-sequence [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/communication-studies-dance-theatre/communication-studies-bachelor-arts/ (sha256 52cca075fded)
- issues: course_alternatives_in_rule_text
  - courses: COMM 200 ⟵ “COMM 200 - Interpersonal Communication”
  - courses: COMM 307 ⟵ “COMM 307 - Organizational Communication”
  - courses: COMM 350 ⟵ “COMM 350 - Intercultural Communication”
  - courses: COMM 369 ⟵ “COMM 369 - Public Communication”
  - courses: COMM 202 ⟵ “COMM 202 - Introduction to Rhetoric Through Pop Culture”
  - courses: COMM 308 ⟵ “COMM 308 - Persuasion”
  - courses: COMM 312 ⟵ “COMM 312 - Argumentation”
  - courses: COMM 370 ⟵ “COMM 370 - Political Communication”
  - courses: COMM 200 ⟵ “COMM 200 - Interpersonal Communication”
  - courses: COMM 202 ⟵ “COMM 202 - Introduction to Rhetoric Through Pop Culture”
  - courses: COMM 203 ⟵ “COMM 203 - Small Group Communication”
  - courses: COMM 204 ⟵ “COMM 204 - Social Media”
  - courses: COMM 255 ⟵ “COMM 255 - Magazine Writing”
  - courses: COMM 257 ⟵ “COMM 257 - Introduction to Journalism”
  - courses: COMM 260 ⟵ “COMM 260 - Digital Video Production”
  - courses: COMM 266 ⟵ “COMM 266 - Introduction to New Media”
  - courses: COMM 290 ⟵ “COMM 290 - Special Topics”
  - courses: COMM 303 ⟵ “COMM 303 - Advertising in Consumer Society”
  - courses: COMM 304 ⟵ “COMM 304 - Public Relations”
  - courses: COMM 307 ⟵ “COMM 307 - Organizational Communication”
  - courses: COMM 308 ⟵ “COMM 308 - Persuasion”
  - courses: COMM 312 ⟵ “COMM 312 - Argumentation”
  - courses: COMM 350 ⟵ “COMM 350 - Intercultural Communication”
  - courses: COMM 360 ⟵ “COMM 360 - Oral Interpretation”
  - courses: COMM 369 ⟵ “COMM 369 - Public Communication”
  - … 12 more rows
### `a0186a1782f19c22` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-fibers [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
- issues: course_alternatives_in_rule_text
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 338 ⟵ “ART 338 - Advanced Fiber: Surface Design”
  - courses: ART 339 ⟵ “ART 339 - Advanced Fibers: Fabric Printing + Needle Arts”
### `a28c67849a1f25d7` Saint Mary's College — degree_requirements 2026-27 · program_key=design-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-supporting-correlate-course-requirements [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-concentration-bachelor-fine-arts/ (sha256 83cfddcbe154)
- issues: course_alternatives_in_rule_text
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 336 ⟵ “BUAD 336 - Brand Management”
  - courses: BUAD 342 ⟵ “BUAD 342 - New Venture”
  - courses: COMM 204 ⟵ “COMM 204 - Social Media”
  - courses: COMM 210 ⟵ “COMM 210 - Mass Media and Society”
  - courses: COMM 260 ⟵ “COMM 260 - Digital Video Production”
  - courses: COMM 303 ⟵ “COMM 303 - Advertising in Consumer Society”
  - courses: COMM 304 ⟵ “COMM 304 - Public Relations”
  - courses: COMM 383 ⟵ “COMM 383 - Art and Entertainment Law”
  - courses: COMM 404 ⟵ “COMM 404 - Non-Profit Public Relations Campaigns and Theory”
  - courses: COMM 406 ⟵ “COMM 406 - Marketing Communication”
  - courses: COMM 486 ⟵ “COMM 486 - Broadcast Media Production”
  - courses: ART 344 ⟵ “ART 344 - Film History and Analysis”
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
  - courses: ART 499 ⟵ “ART 499 - Internship”
### `a2b9a722630c1826` Saint Mary's College — degree_requirements 2026-27 · program_key=finance-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-other-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/finance-concentration-bba/ (sha256 be6114dba02d)
- issues: requirement_groups_skipped
  - courses: BUAD 202 ⟵ “BUAD 202 - Principles of Managerial Accounting”
  - courses: BUAD 346 ⟵ “BUAD 346 - Business & Organizational Ethics”
  - courses: BUAD 446 ⟵ “BUAD 446 - Strategic Management”
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `a36914fbaf7497a0` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-new-media-art [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
- issues: course_alternatives_in_rule_text
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 310 ⟵ “ART 310 - Web Design and Development II”
  - courses: ART 321 ⟵ “ART 321 - Photography II: Lighting Workshop”
  - courses: ART 325 ⟵ “ART 325 - Video Art II”
  - courses: ART 335 ⟵ “ART 335 - Animation Workshop”
  - courses: ART 357 ⟵ “ART 357 - Holography Workshop”
### `a7d8ccf776b162db` Saint Mary's College — degree_requirements 2026-27 · program_key=cellular-molecular-biology-concentration-bachelor-of-science · requirement_key=major-requirements-60-hours-required-supporting-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/cellular-molecular-biology-concentration-bachelor-science/ (sha256 345f5d902b16)
- issues: course_alternatives_in_rule_text
  - courses: CHEM 221 ⟵ “CHEM 221 - Organic Chemistry I”
  - courses: CHEM 221L ⟵ “CHEM 221L - Organic Chemistry I Laboratory”
### `aa5121009acdb741` Saint Mary's College — degree_requirements 2026-27 · program_key=management-concentration-bachelor-of-business-administration · requirement_key=management-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/management-concentration-bba/ (sha256 97110e2334f3)
- issues: requirement_groups_skipped
  - courses: BUAD 321 ⟵ “BUAD 321 - Human Resource Management”
  - courses: BUAD 322 ⟵ “BUAD 322 - Organizational Behavior”
  - courses: BUAD 329 ⟵ “BUAD 329 - Gender and Race Issues in Management”
  - courses: BUAD 342 ⟵ “BUAD 342 - New Venture”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 422 ⟵ “BUAD 422 - International Management”
  - courses: BUAD 427 ⟵ “BUAD 427 - Principles of Operations Research”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
### `aac583e611581a90` Saint Mary's College — degree_requirements 2026-27 · program_key=physics-bachelor-of-science · requirement_key=major-requirements-61-hours-required-supporting-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/physics-bachelor-science/ (sha256 02ceb5788497)
- issues: course_alternatives_in_rule_text
  - courses: CPSC 207 ⟵ “CPSC 207 - Computer Programming”
  - courses: MATH 231 ⟵ “MATH 231 - Calculus III”
  - courses: MATH 326 ⟵ “MATH 326 - Linear Algebra and Differential Equations”
### `ac60f497aa48db91` Saint Mary's College — degree_requirements 2026-27 · program_key=design-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-also-available-for-students-concentrating-in-art-des [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/design-art-history-double-concentration-bachelor-arts---ashd/ (sha256 f9838a7b0cf4)
- issues: course_alternatives_in_rule_text
  - courses: ART 397 ⟵ “ART 397 - Independent Study”
  - courses: ART 499 ⟵ “ART 499 - Internship”
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 301 ⟵ “ART 301 - Advanced Drawing”
  - courses: ART 305 ⟵ “ART 305 - Advanced Painting”
  - … 15 more rows
### `acd7a26564292171` Saint Mary's College — degree_requirements 2026-27 · program_key=marketing-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/marketing-concentration-bba/ (sha256 64d2fe51df8a)
- issues: requirement_groups_skipped
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 212 ⟵ “BUAD 212 - Principles of Finance”
  - courses: BUAD 221 ⟵ “BUAD 221 - Principles of Management”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 245 ⟵ “BUAD 245 - Business Communication”
  - courses: BUAD 247 ⟵ “BUAD 247 - Introduction to Excel, Statistics, and Business Analytics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
### `ad2a035f71a76d4d` Saint Mary's College — degree_requirements 2026-27 · program_key=business-administration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-other-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/business-administration-bba/ (sha256 02555618d0ed)
- issues: requirement_groups_skipped
  - courses: BUAD 202 ⟵ “BUAD 202 - Principles of Managerial Accounting”
  - courses: BUAD 346 ⟵ “BUAD 346 - Business & Organizational Ethics”
  - courses: BUAD 446 ⟵ “BUAD 446 - Strategic Management”
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `ade6f57f1fb2f0cf` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-new-media-art [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
- issues: course_alternatives_in_rule_text
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 310 ⟵ “ART 310 - Web Design and Development II”
  - courses: ART 321 ⟵ “ART 321 - Photography II: Lighting Workshop”
  - courses: ART 325 ⟵ “ART 325 - Video Art II”
  - courses: ART 335 ⟵ “ART 335 - Animation Workshop”
  - courses: ART 357 ⟵ “ART 357 - Holography Workshop”
### `b0189779fc3a2af4` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-painting [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
- issues: course_alternatives_in_rule_text
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 301 ⟵ “ART 301 - Advanced Drawing”
  - courses: ART 305 ⟵ “ART 305 - Advanced Painting”
### `b10db5d8a5a9739e` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-media-specific [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
- issues: course_alternatives_in_rule_text
  - courses: ART 343 ⟵ “ART 343 - History of Photography”
  - courses: ART 344 ⟵ “ART 344 - Film History and Analysis”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - … 15 more rows
### `b36a0f63f1489cf4` Saint Mary's College — degree_requirements 2026-27 · program_key=ecology-evolution-and-environmental-biology-concentration-bachelor-of-science · requirement_key=major-requirements-60-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/ecology-evolution-environmental-biology-concentration-bachelor-science/ (sha256 2bd059a8e87e)
- issues: course_alternatives_in_rule_text
  - courses: BIO 221 ⟵ “BIO 221 - Introduction to Genetics”
  - courses: BIO 248 ⟵ “BIO 248 - Issues in Environmental Biology”
  - courses: BIO 312 ⟵ “BIO 312 - Evolution”
  - courses: BIO 315 ⟵ “BIO 315 - Statistical Methods for Biologists”
  - courses: BIO 385 ⟵ “BIO 385 - Introduction to Research”
  - courses: BIO 485 ⟵ “BIO 485 - Research in Biology”
### `b5c611960333d81f` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-sculpture [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
- issues: course_alternatives_in_rule_text
  - courses: ART 112 ⟵ “ART 112 - Earth Art”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 272 ⟵ “ART 272 - Installation Art: Activating Spaces”
  - courses: ART 274 ⟵ “ART 274 - Introduction to Landscape Architecture”
  - courses: ART 374 ⟵ “ART 374 - Landscape Architecture II”
  - courses: ART 417 ⟵ “ART 417 - Advanced Sculpture”
  - courses: ART 499 ⟵ “ART 499 - Internship”
### `b6b31727048ce54b` Saint Mary's College — degree_requirements 2026-27 · program_key=ecology-evolution-and-environmental-biology-concentration-bachelor-of-science · requirement_key=major-requirements-60-hours-required-supporting-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/ecology-evolution-environmental-biology-concentration-bachelor-science/ (sha256 2bd059a8e87e)
- issues: course_alternatives_in_rule_text
  - courses: CHEM 221 ⟵ “CHEM 221 - Organic Chemistry I”
  - courses: CHEM 221L ⟵ “CHEM 221L - Organic Chemistry I Laboratory”
### `c37dec5822d3755b` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-concentration-bachelor-arts/ (sha256 2674d7047df7)
- issues: course_alternatives_in_rule_text
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 103 ⟵ “ART 103 - Design Lab”
  - courses: ART 241 ⟵ “ART 241 - Art History Survey I”
  - courses: ART 242 ⟵ “ART 242 - Art History Survey II”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
  - courses: ART 495 ⟵ “ART 495 - Senior Comprehensive in Art History or Studio Art”
### `c64220160798ab9c` Saint Mary's College — degree_requirements 2026-27 · program_key=international-business-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/international-business-concentration-bba/ (sha256 4b6124cea0c8)
- issues: requirement_groups_skipped
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 212 ⟵ “BUAD 212 - Principles of Finance”
  - courses: BUAD 221 ⟵ “BUAD 221 - Principles of Management”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 245 ⟵ “BUAD 245 - Business Communication”
  - courses: BUAD 247 ⟵ “BUAD 247 - Introduction to Excel, Statistics, and Business Analytics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
### `c8555f435404332e` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-printmaking [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
- issues: course_alternatives_in_rule_text
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 290 ⟵ “ART 290 - Topics in Art”
  - courses: ART 308 ⟵ “ART 308 - Advanced Printmedia/Drawing”
  - courses: ART 323 ⟵ “ART 323 - Photo-Silkscreen”
### `c9d3a502ff748a48` Saint Mary's College — degree_requirements 2026-27 · program_key=biology-integrative-bachelor-of-science · requirement_key=major-requirements-60-hours-for-students-who-could-use-college-calculus-prep-to- [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/integrative-biology-bachelor-science/ (sha256 6545a284081e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 103 ⟵ “MATH 103 - Precalculus”
### `c9fbd3528631bb72` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-new-media-art [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
- issues: course_alternatives_in_rule_text
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 223 ⟵ “ART 223 - Introduction to Digital Photography”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 266 ⟵ “ART 266 - Introduction to New Media”
  - courses: ART 310 ⟵ “ART 310 - Web Design and Development II”
  - courses: ART 321 ⟵ “ART 321 - Photography II: Lighting Workshop”
  - courses: ART 325 ⟵ “ART 325 - Video Art II”
  - courses: ART 335 ⟵ “ART 335 - Animation Workshop”
  - courses: ART 357 ⟵ “ART 357 - Holography Workshop”
### `cbf4e28d948504b9` Saint Mary's College — degree_requirements 2026-27 · program_key=management-information-systems-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-other-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/management-information-systems-concentration-bba/ (sha256 928076ac397a)
- issues: requirement_groups_skipped
  - courses: BUAD 202 ⟵ “BUAD 202 - Principles of Managerial Accounting”
  - courses: BUAD 346 ⟵ “BUAD 346 - Business & Organizational Ethics”
  - courses: BUAD 446 ⟵ “BUAD 446 - Strategic Management”
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `ce2e1d0aef701468` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-printmaking [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
- issues: course_alternatives_in_rule_text
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 308 ⟵ “ART 308 - Advanced Printmedia/Drawing”
  - courses: ART 323 ⟵ “ART 323 - Photo-Silkscreen”
### `d6708ce1619c1022` Saint Mary's College — degree_requirements 2026-27 · program_key=exercise-science-rehabilitative-science-bachelor-of-science · requirement_key=major-requirements-60-credits-supporting-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/exercise-science/rehabilitative-science-bachelor-science/ (sha256 46ecbe960958)
- issues: course_alternatives_in_rule_text
  - courses: NURS 310 ⟵ “NURS 310 - Nutrition for Health and Healing”
  - courses: PSYC 156 ⟵ “PSYC 156 - Introduction to Psychology: Culture and Systems”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
  - courses: CHEM 121 ⟵ “CHEM 121 - Principles of Chemistry I”
  - courses: CHEM 122 ⟵ “CHEM 122 - Principles of Chemistry II”
  - courses: PHYS 111 ⟵ “PHYS 111 - College Physics I: Mechanics and Waves”
### `d76307b4546e3722` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-printmaking [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
- issues: course_alternatives_in_rule_text
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - courses: ART 308 ⟵ “ART 308 - Advanced Printmedia/Drawing”
  - courses: ART 323 ⟵ “ART 323 - Photo-Silkscreen”
### `da09bd7e2ce64500` Saint Mary's College — degree_requirements 2026-27 · program_key=biochemistry-concentration-chemistry-major-bachelor-of-science · requirement_key=major-requirements-64-hours-required-supporting-courses [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/biochemistry-concentration-bachelor-science/ (sha256 cf495d786a6d)
- issues: course_alternatives_in_rule_text
  - courses: MATH 131 ⟵ “MATH 131 - Calculus I”
  - courses: MATH 132 ⟵ “MATH 132 - Calculus II”
### `dde9b424449793b4` Saint Mary's College — degree_requirements 2026-27 · program_key=business-administration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/business-administration-bba/ (sha256 02555618d0ed)
- issues: requirement_groups_skipped
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 212 ⟵ “BUAD 212 - Principles of Finance”
  - courses: BUAD 221 ⟵ “BUAD 221 - Principles of Management”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 245 ⟵ “BUAD 245 - Business Communication”
  - courses: BUAD 247 ⟵ “BUAD 247 - Introduction to Excel, Statistics, and Business Analytics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
### `deaff137bf9196fe` Saint Mary's College — degree_requirements 2026-27 · program_key=marketing-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-other-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/marketing-concentration-bba/ (sha256 64d2fe51df8a)
- issues: requirement_groups_skipped
  - courses: BUAD 202 ⟵ “BUAD 202 - Principles of Managerial Accounting”
  - courses: BUAD 346 ⟵ “BUAD 346 - Business & Organizational Ethics”
  - courses: BUAD 446 ⟵ “BUAD 446 - Strategic Management”
  - courses: ECON 251 ⟵ “ECON 251 - Principles of Macroeconomics”
  - courses: MATH 214 ⟵ “MATH 214 - Introduction to Statistics”
### `e220488bc4be87ea` Saint Mary's College — degree_requirements 2026-27 · program_key=art-history-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-media-specific [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/art-history-concentration-bachelor-arts/ (sha256 2674d7047df7)
- issues: course_alternatives_in_rule_text
  - courses: ART 343 ⟵ “ART 343 - History of Photography”
  - courses: ART 344 ⟵ “ART 344 - Film History and Analysis”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 101 ⟵ “ART 101 - Drawing I”
  - courses: ART 102 ⟵ “ART 102 - Drawing II”
  - courses: ART 125 ⟵ “ART 125 - Silkscreen”
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 208 ⟵ “ART 208 - Relief Printmaking: Traditional & Contemporary Approaches”
  - courses: ART 209 ⟵ “ART 209 - Intro to Printmedia: Intaglio”
  - courses: ART 210 ⟵ “ART 210 - Web Design and Development I”
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 216 ⟵ “ART 216 - Introduction to Furniture Design”
  - courses: ART 218 ⟵ “ART 218 - Modeling and Replication”
  - courses: ART 219 ⟵ “ART 219 - Sculptural Knitting and Crochet”
  - courses: ART 221 ⟵ “ART 221 - Photography I”
  - courses: ART 224 ⟵ “ART 224 - Video Art”
  - courses: ART 225 ⟵ “ART 225 - Typography”
  - courses: ART 226 ⟵ “ART 226 - Graphic Design”
  - courses: ART 236 ⟵ “ART 236 - Sustainable Textiles”
  - courses: ART 237 ⟵ “ART 237 - Handmade Paper and Felt”
  - courses: ART 238 ⟵ “ART 238 - Fiber: Surface Design”
  - courses: ART 239 ⟵ “ART 239 - Fiber: Fabric Printing”
  - … 15 more rows
### `e9437ffbc74fd699` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-ceramics [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
- issues: course_alternatives_in_rule_text
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 311 ⟵ “ART 311 - Advanced Ceramics: Hand Building and Slip Casting”
  - courses: ART 411 ⟵ “ART 411 - Alternative Processes in Ceramics”
### `ea58f2a4d84ada71` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-arts · requirement_key=major-requirements-42-hours-painting [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-arts/ (sha256 78e38216d129)
- issues: course_alternatives_in_rule_text
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 301 ⟵ “ART 301 - Advanced Drawing”
  - courses: ART 305 ⟵ “ART 305 - Advanced Painting”
### `eaaf213b66bdb3b9` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-ceramics [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
- issues: course_alternatives_in_rule_text
  - courses: ART 211 ⟵ “ART 211 - Ceramics: Introduction to Clay”
  - courses: ART 212 ⟵ “ART 212 - Throwing on the Wheel”
  - courses: ART 214 ⟵ “ART 214 - The Sustainable Cup”
  - courses: ART 311 ⟵ “ART 311 - Advanced Ceramics: Hand Building and Slip Casting”
  - courses: ART 411 ⟵ “ART 411 - Alternative Processes in Ceramics”
### `ee86099567a4fb54` Saint Mary's College — degree_requirements 2026-27 · program_key=accounting-concentration-bachelor-of-business-administration · requirement_key=accounting-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/accounting-concentration-bba/ (sha256 12db7a8bc572)
- issues: requirement_groups_skipped
  - courses: BUAD 301 ⟵ “BUAD 301 - Intermediate Accounting I”
  - courses: BUAD 302 ⟵ “BUAD 302 - Intermediate Accounting II”
  - courses: BUAD 303 ⟵ “BUAD 303 - Cost Accounting”
  - courses: BUAD 304 ⟵ “BUAD 304 - Personal Income Tax”
  - courses: BUAD 305 ⟵ “BUAD 305 - Accounting for Not-for-Profit Organizations”
  - courses: BUAD 306 ⟵ “BUAD 306 - Fraud Examination”
  - courses: BUAD 344 ⟵ “BUAD 344 - Business Law I”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 401 ⟵ “BUAD 401 - Advanced Accounting”
  - courses: BUAD 402 ⟵ “BUAD 402 - Auditing”
  - courses: BUAD 404 ⟵ “BUAD 404 - Advanced Topics in Income Tax”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
### `eec1f0e91ef5b9c6` Saint Mary's College — degree_requirements 2026-27 · program_key=biology-integrative-bachelor-of-science · requirement_key=major-requirements-60-hours-organismal-course [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/biology/integrative-biology-bachelor-science/ (sha256 6545a284081e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIO 240 ⟵ “BIO 240 - Cats’ Paws and Catapults: Animal Biomechanics”
  - courses: BIO 245 ⟵ “BIO 245 - We Like to Move It (Move it): Introduction to Kinesiology”
### `ef78277a9d6284ef` Saint Mary's College — degree_requirements 2026-27 · program_key=management-information-systems-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/management-information-systems-concentration-bba/ (sha256 928076ac397a)
- issues: requirement_groups_skipped
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 212 ⟵ “BUAD 212 - Principles of Finance”
  - courses: BUAD 221 ⟵ “BUAD 221 - Principles of Management”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 245 ⟵ “BUAD 245 - Business Communication”
  - courses: BUAD 247 ⟵ “BUAD 247 - Introduction to Excel, Statistics, and Business Analytics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
### `f3d979bc86ea25dd` Saint Mary's College — degree_requirements 2026-27 · program_key=management-concentration-bachelor-of-business-administration · requirement_key=major-requirements-51-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/management-concentration-bba/ (sha256 97110e2334f3)
- issues: requirement_groups_skipped
  - courses: BUAD 201 ⟵ “BUAD 201 - Principles of Financial Accounting”
  - courses: BUAD 212 ⟵ “BUAD 212 - Principles of Finance”
  - courses: BUAD 221 ⟵ “BUAD 221 - Principles of Management”
  - courses: BUAD 231 ⟵ “BUAD 231 - Principles of Marketing”
  - courses: BUAD 245 ⟵ “BUAD 245 - Business Communication”
  - courses: BUAD 247 ⟵ “BUAD 247 - Introduction to Excel, Statistics, and Business Analytics”
  - courses: ECON 252 ⟵ “ECON 252 - Principles of Microeconomics”
### `f6be4802bc2b6150` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-concentration-bachelor-of-fine-arts · requirement_key=major-requirements-78-hours-upper-level-art-history-electives [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-concentration-bachelor-fine-arts---art/ (sha256 37a833e1fa35)
- issues: course_alternatives_in_rule_text
  - courses: ART 343 ⟵ “ART 343 - History of Photography”
  - courses: ART 344 ⟵ “ART 344 - Film History and Analysis”
  - courses: ART 345 ⟵ “ART 345 - Modern Art and Design”
  - courses: ART 350 ⟵ “ART 350 - Alternative Media: Art from 1945 to 1989”
  - courses: ART 353 ⟵ “ART 353 - Asian Art: Buddhist, Hindu, and Islamic Traditions”
  - courses: ART 354 ⟵ “ART 354 - Picturing Biodiversity: The Art of Natural History”
  - courses: ART 356 ⟵ “ART 356 - Environment in Contemporary Art”
  - courses: ART 390 ⟵ “ART 390 - Topics in Art”
  - courses: ART 486 ⟵ “ART 486 - Dark Romanticism: The Gothic Imagination in Art”
  - courses: ART 490 ⟵ “ART 490 - Topics in Art”
  - courses: ART 499 ⟵ “ART 499 - Internship”
### `f73f4716a4d5987d` Saint Mary's College — degree_requirements 2026-27 · program_key=biochemistry-concentration-chemistry-major-bachelor-of-science · requirement_key=major-requirements-64-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/biochemistry-concentration-bachelor-science/ (sha256 cf495d786a6d)
- issues: course_alternatives_in_rule_text
  - courses: CHEM 311 ⟵ “CHEM 311 - Thermodynamics”
  - courses: CHEM 324 ⟵ “CHEM 324 - Biochemistry”
  - courses: CHEM 332 ⟵ “CHEM 332 - Analytical Chemistry”
  - courses: CHEM 342 ⟵ “CHEM 342 - Bio-Inorganic Chemistry”
  - courses: CHEM 361 ⟵ “CHEM 361 - Advanced Laboratory I”
  - courses: CHEM 362 ⟵ “CHEM 362 - Advanced Laboratory II”
  - courses: CHEM 424 ⟵ “CHEM 424 - Advanced Biochemistry”
  - courses: CHEM 495 ⟵ “CHEM 495 - Senior Seminar”
### `f7ebb65f0138ce0f` Saint Mary's College — degree_requirements 2026-27 · program_key=chemistry-bachelor-of-science · requirement_key=major-requirements-56-hours-required [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/chemistry-physics/chemistry-bachelor-science/ (sha256 5d09474a83b4)
- issues: course_alternatives_in_rule_text
  - courses: CHEM 311 ⟵ “CHEM 311 - Thermodynamics”
  - courses: CHEM 324 ⟵ “CHEM 324 - Biochemistry”
  - courses: CHEM 332 ⟵ “CHEM 332 - Analytical Chemistry”
  - courses: CHEM 342 ⟵ “CHEM 342 - Bio-Inorganic Chemistry”
  - courses: CHEM 361 ⟵ “CHEM 361 - Advanced Laboratory I”
  - courses: CHEM 362 ⟵ “CHEM 362 - Advanced Laboratory II”
  - courses: CHEM 495 ⟵ “CHEM 495 - Senior Seminar”
  - courses: CHEM 311 ⟵ “CHEM 311 - Thermodynamics”
  - courses: CHEM 312 ⟵ “CHEM 312 - Quantum Chemistry”
  - courses: CHEM 424 ⟵ “CHEM 424 - Advanced Biochemistry”
  - courses: CHEM 431 ⟵ “CHEM 431 - Advanced Inorganic Chemistry”
### `fbdefa9d5721b722` Saint Mary's College — degree_requirements 2026-27 · program_key=finance-concentration-bachelor-of-business-administration · requirement_key=finance-concentration [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/business-administration-economics/finance-concentration-bba/ (sha256 be6114dba02d)
- issues: requirement_groups_skipped
  - courses: BUAD 311 ⟵ “BUAD 311 - Corporate Financial Decision Making”
  - courses: BUAD 313 ⟵ “BUAD 313 - Investments”
  - courses: BUAD 314 ⟵ “BUAD 314 - Personal Financial Planning”
  - courses: BUAD 315 ⟵ “BUAD 315 - Management of Financial Institutions”
  - courses: BUAD 316 ⟵ “BUAD 316 - Financial Strategy with Computer Applications”
  - courses: BUAD 317 ⟵ “BUAD 317 - Financial Statement Analysis”
  - courses: BUAD 390 ⟵ “BUAD 390 - Topics in Business (approved topics)”
  - courses: BUAD 416 ⟵ “BUAD 416 - International Financial Management”
  - courses: BUAD 441 ⟵ “BUAD 441 - Advanced Business Analytics”
### `fd072817e5ecc0cc` Saint Mary's College — degree_requirements 2026-27 · program_key=studio-art-and-art-history-double-concentration-bachelor-of-arts · requirement_key=major-requirements-66-hours-painting [new] (labeled_in_source)
- source: https://catalog.saintmarys.edu/undergraduate/programs/art/studio-art-history-double-concentration-bachelor-arts/ (sha256 726ed1509da9)
- issues: course_alternatives_in_rule_text
  - courses: ART 205 ⟵ “ART 205 - Painting: Oil”
  - courses: ART 207 ⟵ “ART 207 - Water-based Media”
  - courses: ART 301 ⟵ “ART 301 - Advanced Drawing”
  - courses: ART 305 ⟵ “ART 305 - Advanced Painting”
### `0a8183c06bd2e94f` Saint Mary-of-the-Woods College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smwc.edu/offices-resources/offices/financial-aid/tuition-and-fees/ (sha256 a059082a44c4)
- issues: implausible_amount, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 6}
  - column:General: 800 ⟵ “General | $400 | $400 | $800”
  - column:Student-Athlete Fee*: 350 ⟵ “Student-Athlete Fee* | $350 |  | $350”
  - column:Student-Athlete (Equine) Fee**: 350 ⟵ “Student-Athlete (Equine) Fee** | $350 |  | $350”
  - column:Club Sports Fee***: 300 ⟵ “Club Sports Fee*** | $300 |  | $300”
  - column:Pomeroy BookBundle: 873 ⟵ “Pomeroy BookBundle | $436.50 | $436.50 | $873”
  - column:Tuition Exchange Fee: 200 ⟵ “Tuition Exchange Fee | $100 | $100 | $200”
### `28bd777e2b354f3c` Saint Mary-of-the-Woods College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smwc.edu/offices-resources/offices/financial-aid/tuition-and-fees/ (sha256 a059082a44c4)
- issues: implausible_amount
- checks: {"columns": 1, "rows": 5}
  - column:General: 1500 ⟵ “General | $750 | $750 | $1,500”
  - column:Student-Athlete Fee*: 350 ⟵ “Student-Athlete Fee* | $350 |  | $350”
  - column:Student-Athlete (Equine) Fee**: 350 ⟵ “Student-Athlete (Equine) Fee** | $350 |  | $350”
  - column:Club Sports Fee***: 300 ⟵ “Club Sports Fee*** | $300 |  | $300”
  - column:Tuition Exchange Fee: 200 ⟵ “Tuition Exchange Fee | $100 | $100 | $200”
### `cb2b8a43c52078c4` Taylor University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.taylor.edu/admissions/tuition-funding/scholarships (sha256 66248dd7b7cb)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: 19,000 ⟵ “Dean* | 19,000 | 3.70+ | 1270 | 27 | 90”
  - test_requirement: 3.70+ ⟵ “Dean* | 19,000 | 3.70+ | 1270 | 27 | 90”
### `dd65d8a7a89a7c7f` Taylor University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.taylor.edu/admissions/tuition-funding/scholarships (sha256 cec6f049b71a)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: 17,000 ⟵ “Faculty* | 17,000 | 3.70+ | ⁠—⁠No Scores Required⁠—⁠”
  - test_requirement: 3.70+ ⟵ “Faculty* | 17,000 | 3.70+ | ⁠—⁠No Scores Required⁠—⁠”
### `e06989aedb1dca2c` Taylor University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.taylor.edu/admissions/tuition-funding/scholarships (sha256 cec6f049b71a)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: 15,000 ⟵ “Trustee | 15,000 | 3.30–3.69 | ⁠—⁠No Scores Required⁠—⁠”
  - test_requirement: 3.30–3.69 ⟵ “Trustee | 15,000 | 3.30–3.69 | ⁠—⁠No Scores Required⁠—⁠”
### `e6e2e9aad4bd36ee` Taylor University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.taylor.edu/admissions/tuition-funding/scholarships (sha256 cec6f049b71a)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: 21,000 ⟵ “President* | 21,000 | 3.70+ | 1430 | 32 | 103”
  - test_requirement: 3.70+ ⟵ “President* | 21,000 | 3.70+ | 1430 | 32 | 103”
### `003d0874aad8598a` Taylor University — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_url)
- source: https://www.taylor.edu/_docs/admissions/clep-information-sheet-2026_2027.pdf (sha256 41b72cc31a68)
- issues: score_scale_mismatch, conflicting_sources:https://www.taylor.edu/_docs/admissions/ap-information-sheet-2026_2027.pdf
- checks: {"distinct_exams": 20, "equivalencies": 24, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                         50                   POS 100                   American Politics                         3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                                    50                   MAT 140                   Fundamental Calculus for Applications     3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|3]:  ⟵ “College Composition Modular            50 + Dept Test            ENG 110                   College Composition                       3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Dev                          50                      PSY 240                Child Psychology                          3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology (Intro)                           50                   SOC 100                   Intro to Sociology                        3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                50                   ECO 199                   Civic Engagement-Foundational Core        3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                50                   ECO 199                   Civic Engagement-Foundational Core        3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                         50                   ENG 199                   Literature-Foundational Core              3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                          50                   ENG 199                   Literature-Foundational Core              3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introduction to Psychology                  50                      PSY 100                Introduction to Psychology                3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|57]:  ⟵ “Financial Accounting (Intro)           57                 ACC 241             Accounting Principles I                                    3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|59]:  ⟵ “Financial Accounting (Intro)           59                 ACC 242             Accounting Principles II                                   3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|55]:  ⟵ “Business Law (Intro)                   55                MGT 311              Business Law                                               3”
  - equivalencies[CLEP-CALCULUS|62]:  ⟵ “Calculus                               62                 MAT 151             Calculus I                                                 4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language                        59               FRE 201, 202          Intermediate French                                        6”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|66]:  ⟵ “Management                             66                MGT 352              Principles of Management                                   3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|62]:  ⟵ “Marketing                              62                 MKT 231             Principles of Marketing                                    3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|62]:  ⟵ “Macroeconomics (Intro)                 62                 ECO 202             Principles of Macroeconomics                               3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|60]:  ⟵ “Microeconomics (Intro)                 60                 ECO 201             Principles of Microeconomics                               3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language                       63               SPA 201, 202          Intermediate Spanish                                       6”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|3]:  ⟵ “U.S. History I                    54 + Dept Test          HIS 124             History of the U.S. I                                      3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|3]:  ⟵ “U.S. History II                   55 + Dept Test          HIS 125             History of the U.S. II                                     3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|3]:  ⟵ “Western Civilization I            56 + Dept Test          HIS 103             World History I                                            3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|3]:  ⟵ “Western Civilization II           56 + Dept Test          HIS 104             World History II                                           3”
### `6e0efcf1ba1af993` Taylor University — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_url)
- source: https://www.taylor.edu/_docs/admissions/ap-information-sheet-2026_2027.pdf (sha256 aa3816c19183)
- issues: score_scale_mismatch, conflicting_sources:https://www.taylor.edu/_docs/admissions/clep-information-sheet-2026_2027.pdf
- checks: {"distinct_exams": 9, "equivalencies": 14, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|3]:  ⟵ “Biology                                      3              BIO 100             General Biology w/Lab                                   4”
  - equivalencies[CLEP-BIOLOGY|4]:  ⟵ “Biology                                      4              BIO 201             Biology I: Foundations of Cell Biology & Genetics       4”
  - equivalencies[CLEP-CALCULUS|3]:  ⟵ “Calculus AB                                3                MAT 140             Fundamental Calculus for Applications                   3”
  - equivalencies[CLEP-CALCULUS|4]:  ⟵ “Calculus AB                                4                MAT 151             Calculus I                                              4”
  - equivalencies[CLEP-CALCULUS|5]:  ⟵ “Calculus AB                                 5               MAT 151, 230        Calculus I, II                                          8”
  - equivalencies[CLEP-CHEMISTRY|3]:  ⟵ “Chemistry                                   3               CHE 201             General, Organic and Biochemistry 1 w/Lab               4”
  - equivalencies[CLEP-CHEMISTRY|4]:  ⟵ “Chemistry                                   4               CHE 201, 202        General, Organic and Biochemistry I, II w/Lab           8”
  - equivalencies[CLEP-CHEMISTRY|5]:  ⟵ “Chemistry                                   5               CHE 201,202         General, Organic and Biochemistry I, II w/Lab           8”
  - equivalencies[CLEP-ENGLISH-LITERATURE|5]:  ⟵ “English Literature/Comp                     5               ENG 299             Survey Literature                                       3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|4]:  ⟵ “French Language                             4               FRE 201, 202        Intermediate French                                     6”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|4]:  ⟵ “Macroeconomics                              4               ECO 202             Principles of Macroeconomics                            3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|4]:  ⟵ “Microeconomics                              4               ECO 201             Principles of Microeconomics                            3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Psychology (General)                        3               PSY 100             Intro to Psychology                                     3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|4]:  ⟵ “Spanish Language                            4               SPA 201, 202        Intermediate Spanish                                    6”
### `927ac6db7e908791` Taylor University — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.taylor.edu/admissions/apply/transfer (sha256 b693c0d9702c)
- issues: stale_year_label:2025-26
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 64 ⟵ “A maximum of 64 hours of credits may be transferred from regionally accredited colleges.”
### `510ffd401f48dc79` Trine University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2026-27-special-conditions-appeal-form.pdf (sha256 66540435d150)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Conditions Appeal Form 2026-27 Section I: Student Information Student Name: ______________________________________________________ SSN: XXX-XX-___________________ Phone Number: ______________________________ Email: ________________________________________________ Sometimes the information filed on the FAFSA does not reflect the current financial situation or consider a special circumstance”
### `85701492abbeae4c` Trine University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2025-26-special-conditions-appeal-form..pdf (sha256 53c5fd57dc4d)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Conditions Appeal Form 2025-26 Section I: Student Information Student Name: ______________________________________________________ SSN: XXX-XX-___________________ Phone Number: ______________________________ Email: ________________________________________________ Sometimes the information filed on the FAFSA does not reflect the current financial situation or consider a special circumstance”
### `baa96218390b3cb0` Trine University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2025-26-special-conditions-appeal-form..pdf (sha256 53c5fd57dc4d)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “In certain circumstances, Trine University’s Office of Financial Aid may use professional judgment, on a case-by-case basis, to adjust the information you filed on your FAFSA, so it better reflects your current situation.”
### `d4239372d8466e67` Trine University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2025-26-sap-appeal-form.pdf (sha256 2080b0cdbc09)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal for Reinstatement Form Main Campus 2025-26 Student Name: ______________________________________________ Student ID #: ______________________ Trine email: ________________________ @my.trine.edu__ Phone #: (________) _______--__________ Federal regulations require that schools monitor the academic progress of each applicant for financial assistance and tha”
### `dbd97bdd5b2c2f9c` Trine University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2026-27-special-conditions-appeal-form.pdf (sha256 66540435d150)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “In certain circumstances, Trine University’s Office of Financial Aid may use professional judgment, on a case-by-case basis, to adjust the information you filed on your FAFSA, so it better reflects your current situation.”
### `fb1196817c1258a8` Trine University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2026-27-sap-appeal-form.pdf (sha256 4a9b26c0b968)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal for Reinstatement Form Main Campus 2026-27 Student Name: ______________________________________________ Student ID #: ______________________ Trine email: ________________________ @my.trine.edu__ Phone #: (________) _______--__________ Federal regulations require that schools monitor the academic progress of each applicant for financial assistance and tha”
### `5ccc9a053b888d8d` Trine University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/dual-enrollment/ (sha256 da409d991dbb)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “To qualify, students must have a minimum 3.0 GPA or receive a recommendation from”
  - per_credit_hour_charge: 95 ⟵ “$95 per credit hour”
  - per_credit_hour_charge: 50 ⟵ “$50 per credit hour”
  - per_credit_hour_charge: 25 ⟵ “$25 per credit hour”
### `93e2923727a0dad9` Trine University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-credit-resources/clep-transfer-credits.aspx (sha256 1bc89e9e20c1)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 31, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | AC 203 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | BA 113 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Intro Business Law | 50 | LAW 203 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Princ Management | 50 | Elective | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Princ Marketing | 50 | MK 203 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 2113 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | ENG 153 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENG 143 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | ENG 143 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG 2013 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | Humanities Elective | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Lang, Level 1 | 50 | Humanities Elective | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Lang, Level 2 | 59 | Humanities Elective | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Lang, Level 1 | 50 | Humanities Elective | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Lang, Level 2 | 60 | Humanities | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Lang, Level 1 | 50 | SPN 113 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Lang, Level 2 | 63 | SPN 113 and SPN 123 | 6”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS 113 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | Psychology Elective | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro Educational Psychology | 50 | Psychology Elective | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Intro Psychology | 50 | PSY 113 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Intro Sociology | 50 | SOC 103 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Princ Macroeconomics | 50 | ECO 223 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Princ Microeconomics | 50 | ECO 213 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences & History | 50 | Social Science Elective | 6”
  - … 9 more rows
### `b86805702606c561` Trine University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-credit-resources/ib-high-level-transfer-credits.aspx (sha256 f79d73d225c9)
- issues: score_column_not_scores, shared_site_attribution_review
- checks: {"distinct_exams": 19, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[IB-FILM-HL|Film HL]:  ⟵ “Film HL | 5, 6, 7 | FLM 203 | 3”
  - equivalencies[IB-MUSIC-HL|Music HL]:  ⟵ “Music HL | 5, 6, 7 | Humanities Elective | 3”
  - equivalencies[IB-THEATRE-HL|Theatre HL]:  ⟵ “Theatre HL | 5, 6, 7 | THE 103 | 3”
  - equivalencies[IB-VISUAL-ARTS-HL|Visual Arts HL]:  ⟵ “Visual Arts HL | 5, 6, 7 | ART 253 | 3”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|Business Mgt HL]:  ⟵ “Business Mgt HL | 5, 6, 7 | BA 123 | 3”
  - equivalencies[IB-ECONOMICS-HL|Economics HL]:  ⟵ “Economics HL | 5, 6, 7 | ECO 203 and ECO 213 | 3”
  - equivalencies[IB-GEOGRAPHY-HL|Geography HL]:  ⟵ “Geography HL | 5, 6, 7 | GEO 213 or EAS 213 | 3”
  - equivalencies[IB-GLOBAL-POLITICS-HL|Global Politics HL]:  ⟵ “Global Politics HL | 5, 6, 7 | Social Science Elective | 3”
  - equivalencies[IB-HISTORY-HL|History HL]:  ⟵ “History HL | 5, 6, 7 | Social Science Elective | 3”
  - equivalencies[IB-HISTORY|History of Africa and Middle East]:  ⟵ “History of Africa and Middle East | 5, 6, 7 | HIS 203 and HIS 213 | 6”
  - equivalencies[IB-HISTORY-HL|History Americas HL]:  ⟵ “History Americas HL | 5, 6, 7 | HIS 103 and HIS 113 | 6”
  - equivalencies[IB-HISTORY|History Asia and Oceania]:  ⟵ “History Asia and Oceania | 5, 6, 7 | HIS 203 and HIS 213 | 6”
  - equivalencies[IB-HISTORY|History Europe]:  ⟵ “History Europe | 5, 6, 7 | HIS 203 and HIS 213 | 6”
  - equivalencies[IB-PHILOSOPHY|Philosophy]:  ⟵ “Philosophy | 5, 6, 7 | PHL 203 | 3”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | 5, 6, 7 | PSY 113 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|Social & Cultural Anthropology HL]:  ⟵ “Social & Cultural Anthropology HL | 5, 6, 7 | Social Science Elective | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|Math: Analysis & Approaches HL]:  ⟵ “Math: Analysis & Approaches HL | 5, 6, 7 | MA 113 | 3”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|Math: Applications & Interpretations HL]:  ⟵ “Math: Applications & Interpretations HL | 5, 6, 7 | MA 113 | 3”
  - equivalencies[IB-BIOLOGY-HL|Biology HL]:  ⟵ “Biology HL | 5, 6, 7 | BIO 114 | 4”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry HL]:  ⟵ “Chemistry HL | 5, 6, 7 | CH 104 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|Computer Science HL]:  ⟵ “Computer Science HL | 5, 6, 7 | Electives | 3”
  - equivalencies[IB-PHYSICS-HL|Physics HL]:  ⟵ “Physics HL | 5, 6, 7 | PH 104 | 4”
### `e63297c26962746e` Trine University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-credit-resources/ap-transfer-credits.aspx (sha256 05581f388538)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 37, "equivalencies": 44, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3, 4, 5]:  ⟵ “Art History | 3, 4, 5 | Humanities Elective | 3”
  - equivalencies[AP-MUSIC-THEORY|3, 4, 5]:  ⟵ “Music Theory | 3, 4, 5 | MUS 103 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “2-D Art and Design | 3, 4, 5 | Humanities Elective | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, 5]:  ⟵ “3-D Art and Design | 3, 4, 5 | Humanities Elective | 3”
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “Drawing | 3, 4, 5 | Humanities Elective | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3, 4, 5]:  ⟵ “English Language & Composition | 3, 4, 5 | ENG 143 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, 5]:  ⟵ “English Literature & Composition | 3, 4, 5 | ENG 153 | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “Comparative Govern. & Politics | 3, 4, 5 | POLS 313 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3, 4, 5]:  ⟵ “European History | 3, 4, 5 | Social Science Elective | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3, 4, 5]:  ⟵ “Human Geography | 3, 4, 5 | GEO 303 | 3”
  - equivalencies[AP-MACROECONOMICS|3, 4, 5]:  ⟵ “Macroeconomics | 3, 4, 5 | ECO 223 | 3”
  - equivalencies[AP-MICROECONOMICS|3, 4, 5]:  ⟵ “Microeconomics | 3, 4, 5 | ECO 213 | 3”
  - equivalencies[AP-PSYCHOLOGY|3, 4, 5]:  ⟵ “Psychology | 3, 4, 5 | PSY 113 | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “U.S. Govern. & Politics | 3, 4, 5 | POLS 113 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3, 4, 5]:  ⟵ “U.S. History | 3, 4, 5 | HIS 103 and HIS 113 | 6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3, 4, 5]:  ⟵ “World History: Modern | 3, 4, 5 | HIS 213 | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MA 173 | 3”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “Calculus AB | 4, 5 | MA 134 | 4”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC | 4, 5 | MA 134 and MA 164 | 8”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC subscore | 4, 5 | MA 134 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CSIT 103 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, 5]:  ⟵ “Computer Science A | 3, 4, 5 | CS 1113 or INF 143 | 3”
  - equivalencies[AP-PRECALCULUS|3, 4, 5]:  ⟵ “Precalculus | 3, 4, 5 | MA 124 | 4”
  - equivalencies[AP-STATISTICS|3, 4, 5]:  ⟵ “Statistics | 3, 4, 5 | MA 253 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | Science Gen. Ed. Elective | 4”
  - … 19 more rows
### `1141ba4ea763ca67` Trine University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-credit-resources/index.aspx (sha256 dbe41d91b107)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade", "residency_requirement_credits"]}
  - min_grade: C ⟵ “Degree level coursework from a college or university where work completed is of similar rigor and content to the course offerings available at Trine University A grade of "C" or higher must have been earned in the course An official transcript or exam scores sent from the institution directly to Trine University, where upon an official evaluation of transfer credit shall be processed.”
  - residency_requirement_credits: 15 ⟵ “The final 15 credit hours must be received within Trine University.”
### `3a343efe72bcf465` Trine University — transfer_policies 2027-28 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-students.aspx (sha256 c9d330ee6bfb)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Admission requirements for transfer students Transfer students applying to the Allen School of Engineering and Computing must have a minimum cumulative grade point average of 2.75 and a grade of “C” or better in Calculus I and Chemistry I.”
  - min_grade: C ⟵ “Transferring Credits Credits earned from a regionally accredited institution and completed with a grade of "C" or better may be transferred.”
### `258af6f2b8b66839` Trine University-Regional/Non-Traditional Campuses — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2025-26-special-conditions-appeal-form..pdf (sha256 53c5fd57dc4d)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Conditions Appeal Form 2025-26 Section I: Student Information Student Name: ______________________________________________________ SSN: XXX-XX-___________________ Phone Number: ______________________________ Email: ________________________________________________ Sometimes the information filed on the FAFSA does not reflect the current financial situation or consider a special circumstance”
### `2ca2c728f8a5915c` Trine University-Regional/Non-Traditional Campuses — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2026-27-sap-appeal-form.pdf (sha256 4a9b26c0b968)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal for Reinstatement Form Main Campus 2026-27 Student Name: ______________________________________________ Student ID #: ______________________ Trine email: ________________________ @my.trine.edu__ Phone #: (________) _______--__________ Federal regulations require that schools monitor the academic progress of each applicant for financial assistance and tha”
### `4f911c0d1f57f51e` Trine University-Regional/Non-Traditional Campuses — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2025-26-special-conditions-appeal-form..pdf (sha256 53c5fd57dc4d)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “In certain circumstances, Trine University’s Office of Financial Aid may use professional judgment, on a case-by-case basis, to adjust the information you filed on your FAFSA, so it better reflects your current situation.”
### `5b877fccb0d6bb74` Trine University-Regional/Non-Traditional Campuses — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2026-27-special-conditions-appeal-form.pdf (sha256 66540435d150)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Conditions Appeal Form 2026-27 Section I: Student Information Student Name: ______________________________________________________ SSN: XXX-XX-___________________ Phone Number: ______________________________ Email: ________________________________________________ Sometimes the information filed on the FAFSA does not reflect the current financial situation or consider a special circumstance”
### `cf1cef82071996e3` Trine University-Regional/Non-Traditional Campuses — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2026-27-special-conditions-appeal-form.pdf (sha256 66540435d150)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “In certain circumstances, Trine University’s Office of Financial Aid may use professional judgment, on a case-by-case basis, to adjust the information you filed on your FAFSA, so it better reflects your current situation.”
### `fc4fc6cf44656eb2` Trine University-Regional/Non-Traditional Campuses — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/tuition-aid/documents/2025-26-sap-appeal-form.pdf (sha256 2080b0cdbc09)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal for Reinstatement Form Main Campus 2025-26 Student Name: ______________________________________________ Student ID #: ______________________ Trine email: ________________________ @my.trine.edu__ Phone #: (________) _______--__________ Federal regulations require that schools monitor the academic progress of each applicant for financial assistance and tha”
### `144746a77bc23ab5` Trine University-Regional/Non-Traditional Campuses — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/dual-enrollment/ (sha256 da409d991dbb)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “To qualify, students must have a minimum 3.0 GPA or receive a recommendation from”
  - per_credit_hour_charge: 95 ⟵ “$95 per credit hour”
  - per_credit_hour_charge: 50 ⟵ “$50 per credit hour”
  - per_credit_hour_charge: 25 ⟵ “$25 per credit hour”
### `3a8ebc9e751688b5` Trine University-Regional/Non-Traditional Campuses — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-credit-resources/ap-transfer-credits.aspx (sha256 05581f388538)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 37, "equivalencies": 44, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3, 4, 5]:  ⟵ “Art History | 3, 4, 5 | Humanities Elective | 3”
  - equivalencies[AP-MUSIC-THEORY|3, 4, 5]:  ⟵ “Music Theory | 3, 4, 5 | MUS 103 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “2-D Art and Design | 3, 4, 5 | Humanities Elective | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, 5]:  ⟵ “3-D Art and Design | 3, 4, 5 | Humanities Elective | 3”
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “Drawing | 3, 4, 5 | Humanities Elective | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3, 4, 5]:  ⟵ “English Language & Composition | 3, 4, 5 | ENG 143 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, 5]:  ⟵ “English Literature & Composition | 3, 4, 5 | ENG 153 | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “Comparative Govern. & Politics | 3, 4, 5 | POLS 313 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3, 4, 5]:  ⟵ “European History | 3, 4, 5 | Social Science Elective | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3, 4, 5]:  ⟵ “Human Geography | 3, 4, 5 | GEO 303 | 3”
  - equivalencies[AP-MACROECONOMICS|3, 4, 5]:  ⟵ “Macroeconomics | 3, 4, 5 | ECO 223 | 3”
  - equivalencies[AP-MICROECONOMICS|3, 4, 5]:  ⟵ “Microeconomics | 3, 4, 5 | ECO 213 | 3”
  - equivalencies[AP-PSYCHOLOGY|3, 4, 5]:  ⟵ “Psychology | 3, 4, 5 | PSY 113 | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “U.S. Govern. & Politics | 3, 4, 5 | POLS 113 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3, 4, 5]:  ⟵ “U.S. History | 3, 4, 5 | HIS 103 and HIS 113 | 6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3, 4, 5]:  ⟵ “World History: Modern | 3, 4, 5 | HIS 213 | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MA 173 | 3”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “Calculus AB | 4, 5 | MA 134 | 4”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC | 4, 5 | MA 134 and MA 164 | 8”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC subscore | 4, 5 | MA 134 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CSIT 103 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, 5]:  ⟵ “Computer Science A | 3, 4, 5 | CS 1113 or INF 143 | 3”
  - equivalencies[AP-PRECALCULUS|3, 4, 5]:  ⟵ “Precalculus | 3, 4, 5 | MA 124 | 4”
  - equivalencies[AP-STATISTICS|3, 4, 5]:  ⟵ “Statistics | 3, 4, 5 | MA 253 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | Science Gen. Ed. Elective | 4”
  - … 19 more rows
### `4d0519b32c594648` Trine University-Regional/Non-Traditional Campuses — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-credit-resources/clep-transfer-credits.aspx (sha256 1bc89e9e20c1)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 31, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | AC 203 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | BA 113 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Intro Business Law | 50 | LAW 203 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Princ Management | 50 | Elective | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Princ Marketing | 50 | MK 203 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 2113 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | ENG 153 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENG 143 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | ENG 143 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG 2013 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | Humanities Elective | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Lang, Level 1 | 50 | Humanities Elective | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Lang, Level 2 | 59 | Humanities Elective | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Lang, Level 1 | 50 | Humanities Elective | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Lang, Level 2 | 60 | Humanities | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Lang, Level 1 | 50 | SPN 113 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Lang, Level 2 | 63 | SPN 113 and SPN 123 | 6”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS 113 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | Psychology Elective | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro Educational Psychology | 50 | Psychology Elective | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Intro Psychology | 50 | PSY 113 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Intro Sociology | 50 | SOC 103 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Princ Macroeconomics | 50 | ECO 223 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Princ Microeconomics | 50 | ECO 213 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences & History | 50 | Social Science Elective | 6”
  - … 9 more rows
### `5f9cf4a54676415b` Trine University-Regional/Non-Traditional Campuses — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-credit-resources/ib-high-level-transfer-credits.aspx (sha256 f79d73d225c9)
- issues: score_column_not_scores, shared_site_attribution_review
- checks: {"distinct_exams": 19, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[IB-FILM-HL|Film HL]:  ⟵ “Film HL | 5, 6, 7 | FLM 203 | 3”
  - equivalencies[IB-MUSIC-HL|Music HL]:  ⟵ “Music HL | 5, 6, 7 | Humanities Elective | 3”
  - equivalencies[IB-THEATRE-HL|Theatre HL]:  ⟵ “Theatre HL | 5, 6, 7 | THE 103 | 3”
  - equivalencies[IB-VISUAL-ARTS-HL|Visual Arts HL]:  ⟵ “Visual Arts HL | 5, 6, 7 | ART 253 | 3”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|Business Mgt HL]:  ⟵ “Business Mgt HL | 5, 6, 7 | BA 123 | 3”
  - equivalencies[IB-ECONOMICS-HL|Economics HL]:  ⟵ “Economics HL | 5, 6, 7 | ECO 203 and ECO 213 | 3”
  - equivalencies[IB-GEOGRAPHY-HL|Geography HL]:  ⟵ “Geography HL | 5, 6, 7 | GEO 213 or EAS 213 | 3”
  - equivalencies[IB-GLOBAL-POLITICS-HL|Global Politics HL]:  ⟵ “Global Politics HL | 5, 6, 7 | Social Science Elective | 3”
  - equivalencies[IB-HISTORY-HL|History HL]:  ⟵ “History HL | 5, 6, 7 | Social Science Elective | 3”
  - equivalencies[IB-HISTORY|History of Africa and Middle East]:  ⟵ “History of Africa and Middle East | 5, 6, 7 | HIS 203 and HIS 213 | 6”
  - equivalencies[IB-HISTORY-HL|History Americas HL]:  ⟵ “History Americas HL | 5, 6, 7 | HIS 103 and HIS 113 | 6”
  - equivalencies[IB-HISTORY|History Asia and Oceania]:  ⟵ “History Asia and Oceania | 5, 6, 7 | HIS 203 and HIS 213 | 6”
  - equivalencies[IB-HISTORY|History Europe]:  ⟵ “History Europe | 5, 6, 7 | HIS 203 and HIS 213 | 6”
  - equivalencies[IB-PHILOSOPHY|Philosophy]:  ⟵ “Philosophy | 5, 6, 7 | PHL 203 | 3”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | 5, 6, 7 | PSY 113 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|Social & Cultural Anthropology HL]:  ⟵ “Social & Cultural Anthropology HL | 5, 6, 7 | Social Science Elective | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|Math: Analysis & Approaches HL]:  ⟵ “Math: Analysis & Approaches HL | 5, 6, 7 | MA 113 | 3”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|Math: Applications & Interpretations HL]:  ⟵ “Math: Applications & Interpretations HL | 5, 6, 7 | MA 113 | 3”
  - equivalencies[IB-BIOLOGY-HL|Biology HL]:  ⟵ “Biology HL | 5, 6, 7 | BIO 114 | 4”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry HL]:  ⟵ “Chemistry HL | 5, 6, 7 | CH 104 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|Computer Science HL]:  ⟵ “Computer Science HL | 5, 6, 7 | Electives | 3”
  - equivalencies[IB-PHYSICS-HL|Physics HL]:  ⟵ “Physics HL | 5, 6, 7 | PH 104 | 4”
### `5565a0f01d5d7878` Trine University-Regional/Non-Traditional Campuses — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-credit-resources/index.aspx (sha256 dbe41d91b107)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade", "residency_requirement_credits"]}
  - min_grade: C ⟵ “Degree level coursework from a college or university where work completed is of similar rigor and content to the course offerings available at Trine University A grade of "C" or higher must have been earned in the course An official transcript or exam scores sent from the institution directly to Trine University, where upon an official evaluation of transfer credit shall be processed.”
  - residency_requirement_credits: 15 ⟵ “The final 15 credit hours must be received within Trine University.”
### `a10d3d632b02852d` Trine University-Regional/Non-Traditional Campuses — transfer_policies 2027-28 [new] (labeled_in_source)
- source: https://www.trine.edu/admission-aid/transfer-resources/transfer-students.aspx (sha256 c9d330ee6bfb)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Admission requirements for transfer students Transfer students applying to the Allen School of Engineering and Computing must have a minimum cumulative grade point average of 2.75 and a grade of “C” or better in Calculus I and Chemistry I.”
  - min_grade: C ⟵ “Transferring Credits Credits earned from a regionally accredited institution and completed with a grade of "C" or better may be transferred.”
### `2fa478d1e9b78318` University of Evansville — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.evansville.edu/student-financial-services/tuition-and-direct-costs-special-and-miscellaneous-fees-2025-2026.cfm (sha256 7cf153749707)
- issues: implausible_amount, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 4}
  - column:Co-op (per period): 460 ⟵ “Co-op (per period) | $460”
  - column:Late Registration: 200 ⟵ “Late Registration | $200”
  - column:Music Therapy Internship: 460 ⟵ “Music Therapy Internship | $460”
  - column:Tuition Exchange (per year): 290 ⟵ “Tuition Exchange (per year) | $290”
### `ba1a67ffc9a75be7` University of Evansville — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.evansville.edu/registrar/transfercredits.cfm (sha256 0a6cfd5af9f0)
- issues: conflicting_values:residency_requirement_credits
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C- ⟵ “Courses with a grade of C- or higher will be considered for transfer credit.”
  - max_transfer_credits: 90 ⟵ “No more than 90 hours may be transferred from an institution to the University of Evansville except in cases where an articulation agreement (transfer plan between UE and another college) has been established.”
### `1474aa65f0f9adce` University of Indianapolis — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://uindy.edu/financial-aid/costs-for-adult-learners (sha256 2183644f5324)
- issues: conflicting_sources:https://uindy.edu/financial-aid/costs-for-undergraduate-students
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 10320 ⟵ “Tuition | $10,320”
  - on_campus:Fees: 352 ⟵ “Fees | $352”
  - on_campus:Housing: 8746 ⟵ “Housing | $8,746”
  - on_campus:Food: 7780 ⟵ “Food | $7,780”
  - on_campus:Transportation: 738 ⟵ “Transportation | $738”
  - on_campus:Miscellaneous: 2392 ⟵ “Miscellaneous | $2,392”
  - on_campus:Loan Fees: 78 ⟵ “Loan Fees | $78”
  - on_campus:Total: 30406 ⟵ “Total | $30,406”
### `5772c7c5ad743bb0` University of Indianapolis — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://uindy.edu/financial-aid/costs-for-undergraduate-students (sha256 a6b998f5ee6b)
- issues: conflicting_sources:https://uindy.edu/financial-aid/costs-for-adult-learners
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 37864 ⟵ “Tuition | $37,864”
  - on_campus:Fees: 1804 ⟵ “Fees | $1,804”
  - on_campus:Housing: 8746 ⟵ “Housing | $8,746”
  - on_campus:Food: 7780 ⟵ “Food | $7,780”
  - on_campus:Transportation: 738 ⟵ “Transportation | $738”
  - on_campus:Miscellaneous: 2392 ⟵ “Miscellaneous | $2,392”
  - on_campus:Loan Fees: 78 ⟵ “Loan Fees | $78”
  - on_campus:Total: 59402 ⟵ “Total | $59,402”
### `8933abf49f0d4f25` University of Notre Dame — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.nd.edu/apply-or-renew/special-circumstances/ (sha256 0f887f300431)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Change in Circumstances review process Students admitted in the Early Action program are reviewed on a rolling basis Students admitted in the Regular Decision program will be reviewed in April Continuing students will begin in mid-July Requests will be reviewed in the order they were received Notification regarding the outcome of the review will be sent to the student's email Unusual Circumstance ”
  - sentence: need_based_special_circumstances ⟵ “To learn more on the federal criteria for dependency and Unusual Circumstances visit Federal Student Aid.”
  - sentence: need_based_special_circumstances ⟵ “The following situations will not be considered Unusual Circumstances: Parents refuse to contribute to the student’s education Parents are unwilling to provide information on the FAFSA or for verification Parents do not claim the student as a dependent for income tax purposes Student demonstrates total self-sufficiency Students who believe they may qualify should contact our office directly for ad”
  - sentence: need_based_special_circumstances ⟵ “Review Process Unusual Circumstances are determined on a case-by-case basis to otherwise dependent students who can demonstrate a complete and total breakdown of the parental relationship.”
### `e1b2d7cbde24c5d0` University of Notre Dame — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.nd.edu/contact/resources/policies/study-abroad/ (sha256 b536d097b670)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Cost of Attendance Increases Students may request an increase in their cost of attendance if their expenses exceed the average amount.”
### `29f8d5347a09816a` University of Saint Francis-Fort Wayne — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sf.edu/cost-and-aid/undergraduate/applying-for-aid/ (sha256 cc530f896b02)
- issues: semantic_review_required, conflicting_sources:https://www.sf.edu/cost-and-aid/financial-aid-forms-and-processes/,https://www.sf.edu/wp-content/uploads/2025/08/sap-appeal-r2-1-Aug-Update.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students will be notified in writing and will be directed to a SAP appeal form.”
  - sentence: sap_appeal ⟵ “Appeals are submitted via the SAP Appeal Form along with supporting documentation prior to the beginning of the next term of attendance.”
### `bbab46145561b487` University of Saint Francis-Fort Wayne — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sf.edu/cost-and-aid/financial-aid-forms-and-processes/ (sha256 2c49949267a3)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.sf.edu/cost-and-aid/undergraduate/applying-for-aid/,https://www.sf.edu/wp-content/uploads/2025/08/sap-appeal-r2-1-Aug-Update.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP Appeal Process Students who fail to make satisfactory academic progress and who are suspended must appeal to have their financial aid reinstated.”
  - sentence: sap_appeal ⟵ “Appeals are submitted via the SAP Appeal Form along with supporting documentation prior to the beginning of the next term of attendance.”
### `d40ab6f6fc3deab6` University of Saint Francis-Fort Wayne — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sf.edu/wp-content/uploads/2025/08/sap-appeal-r2-1-Aug-Update.pdf (sha256 c53669daaf30)
- issues: semantic_review_required, conflicting_sources:https://www.sf.edu/cost-and-aid/financial-aid-forms-and-processes/,https://www.sf.edu/cost-and-aid/undergraduate/applying-for-aid/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form Name Student ID Number Address Phone ( ) Current Email Address Anticipated Graduation Date Semester appealing to have aid reinstated A student who has lost his/her eligibility for financial aid due to lack of satisfactory academic progress may appeal for reinstatement of his/her eligibility if circumstances beyond his/her control prevented him/her from me”
  - sentence: sap_appeal ⟵ “I am; therefore; submitting my completed SAP appeal.”
### `35021c08d9b63e05` University of Saint Francis-Fort Wayne — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sf.edu/wp-content/uploads/2024/10/25-26-undergrad-coa.pdf (sha256 55d5a605dc40)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 8, "rows": 18}
  - column:Tuition/fees: 18775 ⟵ “Tuition/fees | 18,775 | 12,016 | 8,449 | 4,882 | 37,550 | 24,032 | 16,898 | 9,763”
  - column:Food/Housing: 6128 ⟵ “Food/Housing | 6,128 | 4,596 | 3,064 | 0 | 12,256 | 9,192 | 6,128 | 0”
  - column:Bks/Prog/Ln Fees: 940 ⟵ “Bks/Prog/Ln Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal: 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation: 624 ⟵ “Transportation | 624 | 468 | 312 | 156 | 1,248 | 936 | 624 | 312”
  - column:Total: 27347 ⟵ “Total | 27,347 | 18,445 | 12,735 | 5,273 | 54,694 | 36,890 | 25,470 | 10,545”
  - column:Tuition/fees (2): 18775 ⟵ “Tuition/fees | 18,775 | 12,016 | 8,449 | 4,882 | 37,550 | 24,032 | 16,898 | 9,763”
  - column:Food/Housing (2): 6384 ⟵ “Food/Housing | 6,384 | 4,788 | 3,192 | 0 | 12,768 | 9,576 | 6,384 | 0”
  - column:Bks/Prog/Ln Fees (2): 940 ⟵ “Bks/Prog/Ln Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal (2): 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation (2): 880 ⟵ “Transportation | 880 | 660 | 440 | 220 | 1,760 | 1,320 | 880 | 440”
  - column:Total (2): 27859 ⟵ “Total | 27,859 | 18,829 | 12,991 | 5,337 | 55,718 | 37,658 | 25,982 | 10,673”
  - column:Tuition/fees (3): 18775 ⟵ “Tuition/fees | 18,775 | 12,016 | 8,449 | 4,882 | 37,550 | 24,032 | 16,898 | 9,763”
  - column:Food/Housing (3): 1072 ⟵ “Food/Housing | 1,072 | 804 | 536 | 0 | 2,144 | 1,608 | 1,072 | 0”
  - column:Bks/Prog/Ln Fees (3): 940 ⟵ “Bks/Prog/Ln Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal (3): 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation (3): 880 ⟵ “Transportation | 880 | 660 | 440 | 220 | 1,760 | 1,320 | 880 | 440”
  - column:Total (3): 22547 ⟵ “Total | 22,547 | 14,845 | 10,335 | 5,337 | 45,094 | 29,690 | 20,670 | 10,673”
  - column:Tuition/fees: 12016 ⟵ “Tuition/fees | 18,775 | 12,016 | 8,449 | 4,882 | 37,550 | 24,032 | 16,898 | 9,763”
  - column:Food/Housing: 4596 ⟵ “Food/Housing | 6,128 | 4,596 | 3,064 | 0 | 12,256 | 9,192 | 6,128 | 0”
  - column:Bks/Prog/Ln Fees: 705 ⟵ “Bks/Prog/Ln Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal: 660 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation: 468 ⟵ “Transportation | 624 | 468 | 312 | 156 | 1,248 | 936 | 624 | 312”
  - column:Total: 18445 ⟵ “Total | 27,347 | 18,445 | 12,735 | 5,273 | 54,694 | 36,890 | 25,470 | 10,545”
  - column:Tuition/fees (2): 12016 ⟵ “Tuition/fees | 18,775 | 12,016 | 8,449 | 4,882 | 37,550 | 24,032 | 16,898 | 9,763”
  - … 119 more rows
### `3eba1948f0905782` University of Saint Francis-Fort Wayne — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sf.edu/wp-content/uploads/2024/09/2425_graduatecoa.pdf (sha256 57ec047ab40e)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2024-25, conflicting_sources:https://www.sf.edu/cost-and-aid/previous-years-tuition-and-fees/,https://www.sf.edu/wp-content/uploads/2024/04/2425_undergradcoa.pdf
- checks: {"columns": 8, "rows": 18}
  - column:Tuition/fees: 8680 ⟵ “Tuition/fees | 8,680 | 8,680 | 5,642 | 3,038 | 17,360 | 17,360 | 11,284 | 6,076”
  - column:Food/Housing: 5945 ⟵ “Food/Housing | 5,945 | 4,459 | 2,973 | 0 | 11,890 | 8,918 | 5,945 | 0”
  - column:Books/Prog Fees: 850 ⟵ “Books/Prog Fees | 850 | 638 | 425 | 213 | 1,700 | 1,275 | 850 | 425”
  - column:Personal: 875 ⟵ “Personal | 875 | 656 | 438 | 0 | 1,750 | 1,313 | 875 | 0”
  - column:Transportation: 625 ⟵ “Transportation | 625 | 469 | 313 | 156 | 1,250 | 938 | 625 | 313”
  - column:Total: 16975 ⟵ “Total | 16,975 | 14,901 | 9,790 | 3,407 | 33,950 | 29,803 | 19,579 | 6,814”
  - column:Tuition/fees (2): 8680 ⟵ “Tuition/fees | 8,680 | 8,680 | 5,642 | 3,038 | 17,360 | 17,360 | 11,284 | 6,076”
  - column:Food/Housing (2): 5945 ⟵ “Food/Housing | 5,945 | 4,459 | 2,973 | 0 | 11,890 | 8,918 | 5,945 | 0”
  - column:Books/Prog Fees (2): 850 ⟵ “Books/Prog Fees | 850 | 638 | 425 | 213 | 1,700 | 1,275 | 850 | 425”
  - column:Personal (2): 750 ⟵ “Personal | 750 | 563 | 375 | 0 | 1,500 | 1,125 | 750 | 0”
  - column:Transportation (2): 750 ⟵ “Transportation | 750 | 563 | 375 | 188 | 1,500 | 1,125 | 750 | 375”
  - column:Total (2): 16975 ⟵ “Total | 16,975 | 14,901 | 9,790 | 3,407 | 33,950 | 29,803 | 19,579 | 6,814”
  - column:Tuition/fees (3): 8680 ⟵ “Tuition/fees | 8,680 | 8,680 | 5,642 | 3,038 | 17,360 | 17,360 | 11,284 | 6,076”
  - column:Food/Housing (3): 1065 ⟵ “Food/Housing | 1,065 | 799 | 533 | 0 | 2,130 | 1,598 | 1,065 | 0”
  - column:Books/Prog Fees (3): 850 ⟵ “Books/Prog Fees | 850 | 638 | 425 | 213 | 1,700 | 1,275 | 850 | 425”
  - column:Personal (3): 875 ⟵ “Personal | 875 | 656 | 438 | 0 | 1,750 | 1,313 | 875 | 0”
  - column:Transportation (3): 875 ⟵ “Transportation | 875 | 656 | 438 | 219 | 1,750 | 1,313 | 875 | 438”
  - column:Total (3): 12345 ⟵ “Total | 12,345 | 11,429 | 7,475 | 3,469 | 24,690 | 22,858 | 14,949 | 6,939”
  - column:Tuition/fees: 8680 ⟵ “Tuition/fees | 8,680 | 8,680 | 5,642 | 3,038 | 17,360 | 17,360 | 11,284 | 6,076”
  - column:Food/Housing: 4459 ⟵ “Food/Housing | 5,945 | 4,459 | 2,973 | 0 | 11,890 | 8,918 | 5,945 | 0”
  - column:Books/Prog Fees: 638 ⟵ “Books/Prog Fees | 850 | 638 | 425 | 213 | 1,700 | 1,275 | 850 | 425”
  - column:Personal: 656 ⟵ “Personal | 875 | 656 | 438 | 0 | 1,750 | 1,313 | 875 | 0”
  - column:Transportation: 469 ⟵ “Transportation | 625 | 469 | 313 | 156 | 1,250 | 938 | 625 | 313”
  - column:Total: 14901 ⟵ “Total | 16,975 | 14,901 | 9,790 | 3,407 | 33,950 | 29,803 | 19,579 | 6,814”
  - column:Tuition/fees (2): 8680 ⟵ “Tuition/fees | 8,680 | 8,680 | 5,642 | 3,038 | 17,360 | 17,360 | 11,284 | 6,076”
  - … 119 more rows
### `4af2c536913fe114` University of Saint Francis-Fort Wayne — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sf.edu/cost-and-aid/previous-years-tuition-and-fees/ (sha256 76abd0680606)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.sf.edu/wp-content/uploads/2024/04/2425_undergradcoa.pdf,https://www.sf.edu/wp-content/uploads/2024/09/2425_graduatecoa.pdf
- checks: {"columns": 1, "rows": 8}
  - column:Tuition: Physician Assistant Studies per semester (includes semester and technology fees): 17320 ⟵ “Tuition: Physician Assistant Studies per semester (includes semester and technology fees) | $17,320”
  - column:Semester Fee (1-5 hours): 130 ⟵ “Semester Fee (1-5 hours) | $130”
  - column:Semester Fee (6-8 hours): 180 ⟵ “Semester Fee (6-8 hours) | $180”
  - column:Semester Fee (9-11 hours): 225 ⟵ “Semester Fee (9-11 hours) | $225”
  - column:Semester Fee (12+ hours): 270 ⟵ “Semester Fee (12+ hours) | $270”
  - column:DNP Advanced Practice RN Program Fee: 125 ⟵ “DNP Advanced Practice RN Program Fee | $125”
  - column:Technology Fee – Full-time per semester: 355 ⟵ “Technology Fee – Full-time per semester | $355”
  - column:Clinical Health Sciences Technology Fee: 250 ⟵ “Clinical Health Sciences Technology Fee | $250”
### `6d4662f7a02f78ee` University of Saint Francis-Fort Wayne — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sf.edu/wp-content/uploads/2024/04/2425_undergradcoa.pdf (sha256 1c971bd402ee)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2024-25, conflicting_sources:https://www.sf.edu/cost-and-aid/previous-years-tuition-and-fees/,https://www.sf.edu/wp-content/uploads/2024/09/2425_graduatecoa.pdf
- checks: {"columns": 8, "rows": 18}
  - column:Tuition/fees: 18230 ⟵ “Tuition/fees | 18,230 | 11,850 | 8,204 | 4,740 | 36,460 | 23,699 | 16,407 | 9,480”
  - column:Food/Housing: 5936 ⟵ “Food/Housing | 5,936 | 4,452 | 2,968 | 0 | 11,872 | 8,904 | 5,936 | 0”
  - column:Bks/Prog/Ln Fees: 890 ⟵ “Bks/Prog/Ln Fees | 890 | 668 | 445 | 213 | 1,780 | 1,335 | 890 | 445”
  - column:Personal: 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation: 624 ⟵ “Transportation | 624 | 468 | 312 | 156 | 1,248 | 936 | 624 | 312”
  - column:Total: 26560 ⟵ “Total | 26,560 | 18,097 | 12,351 | 5,109 | 53,120 | 36,194 | 24,737 | 10,237”
  - column:Tuition/fees (2): 18230 ⟵ “Tuition/fees | 18,230 | 11,850 | 8,204 | 4,740 | 36,460 | 23,699 | 16,407 | 9,480”
  - column:Food/Housing (2): 5936 ⟵ “Food/Housing | 5,936 | 4,452 | 2,968 | 0 | 11,872 | 8,904 | 5,936 | 0”
  - column:Bks/Prog/Ln Fees (2): 890 ⟵ “Bks/Prog/Ln Fees | 890 | 668 | 445 | 223 | 1,780 | 1,335 | 890 | 445”
  - column:Personal (2): 752 ⟵ “Personal | 752 | 564 | 376 | 0 | 1,504 | 1,128 | 752 | 0”
  - column:Transportation (2): 752 ⟵ “Transportation | 752 | 564 | 376 | 188 | 1,504 | 1,128 | 752 | 376”
  - column:Total (2): 26560 ⟵ “Total | 26,560 | 18,097 | 12,369 | 5,150 | 53,120 | 36,194 | 24,737 | 10,301”
  - column:Tuition/fees (3): 18230 ⟵ “Tuition/fees | 18,230 | 11,850 | 8,204 | 4,740 | 36,460 | 23,699 | 16,407 | 9,480”
  - column:Food/Housing (3): 1056 ⟵ “Food/Housing | 1,056 | 792 | 528 | 0 | 2,112 | 1,584 | 1,056 | 0”
  - column:Bks/Prog/Ln Fees (3): 890 ⟵ “Bks/Prog/Ln Fees | 890 | 668 | 445 | 223 | 1,780 | 1,335 | 890 | 445”
  - column:Personal (3): 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation (3): 880 ⟵ “Transportation | 880 | 660 | 440 | 220 | 1,760 | 1,320 | 880 | 440”
  - column:Total (3): 21936 ⟵ “Total | 21,936 | 14,629 | 10,036 | 5,182 | 43,872 | 29,258 | 20,113 | 10,365”
  - column:Tuition/fees: 11850 ⟵ “Tuition/fees | 18,230 | 11,850 | 8,204 | 4,740 | 36,460 | 23,699 | 16,407 | 9,480”
  - column:Food/Housing: 4452 ⟵ “Food/Housing | 5,936 | 4,452 | 2,968 | 0 | 11,872 | 8,904 | 5,936 | 0”
  - column:Bks/Prog/Ln Fees: 668 ⟵ “Bks/Prog/Ln Fees | 890 | 668 | 445 | 213 | 1,780 | 1,335 | 890 | 445”
  - column:Personal: 660 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation: 468 ⟵ “Transportation | 624 | 468 | 312 | 156 | 1,248 | 936 | 624 | 312”
  - column:Total: 18097 ⟵ “Total | 26,560 | 18,097 | 12,351 | 5,109 | 53,120 | 36,194 | 24,737 | 10,237”
  - column:Tuition/fees (2): 11850 ⟵ “Tuition/fees | 18,230 | 11,850 | 8,204 | 4,740 | 36,460 | 23,699 | 16,407 | 9,480”
  - … 119 more rows
### `99fd54cb3298334f` University of Saint Francis-Fort Wayne — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sf.edu/wp-content/uploads/2026/04/2627_graduatecoa.pdf (sha256 149d106287f7)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.sf.edu/wp-content/uploads/2026/04/2627_undergradcoa.pdf
- checks: {"columns": 8, "rows": 18}
  - column:Tuition/fees: 8710 ⟵ “Tuition/fees | 8,710 | 8,710 | 5,662 | 3,049 | 17,420 | 17,420 | 11,323 | 6,097”
  - column:Food/Housing: 6128 ⟵ “Food/Housing | 6,128 | 4,596 | 3,064 | 0 | 12,256 | 9,192 | 6,128 | 0”
  - column:Books/Prog Fees: 940 ⟵ “Books/Prog Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal: 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation: 624 ⟵ “Transportation | 624 | 468 | 312 | 156 | 1,248 | 936 | 624 | 312”
  - column:Total: 17282 ⟵ “Total | 17,282 | 15,139 | 9,948 | 3,434 | 34,564 | 30,278 | 19,895 | 6,879”
  - column:Tuition/fees (2): 8710 ⟵ “Tuition/fees | 8,710 | 8,710 | 5,662 | 3,049 | 17,420 | 17,420 | 11,323 | 6,097”
  - column:Food/Housing (2): 6384 ⟵ “Food/Housing | 6,384 | 4,788 | 3,192 | 0 | 12,768 | 9,576 | 6,384 | 0”
  - column:Books/Prog Fees (2): 940 ⟵ “Books/Prog Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal (2): 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation (2): 880 ⟵ “Transportation | 880 | 660 | 440 | 220 | 1,760 | 1,320 | 880 | 440”
  - column:Total (2): 17794 ⟵ “Total | 17,794 | 15,523 | 10,204 | 3,504 | 35,588 | 31,046 | 20,407 | 7,007”
  - column:Tuition/fees (3): 8710 ⟵ “Tuition/fees | 8,710 | 8,710 | 5,662 | 3,049 | 17,420 | 17,420 | 11,323 | 6,097”
  - column:Food/Housing (3): 1072 ⟵ “Food/Housing | 1,072 | 804 | 536 | 0 | 2,144 | 1,608 | 1,072 | 0”
  - column:Books/Prog Fees (3): 940 ⟵ “Books/Prog Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal (3): 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation (3): 880 ⟵ “Transportation | 880 | 660 | 440 | 220 | 1,760 | 1,320 | 880 | 440”
  - column:Total (3): 12482 ⟵ “Total | 12,482 | 11,539 | 7,548 | 3,504 | 24,964 | 24,078 | 15,095 | 7,007”
  - column:Tuition/fees: 8710 ⟵ “Tuition/fees | 8,710 | 8,710 | 5,662 | 3,049 | 17,420 | 17,420 | 11,323 | 6,097”
  - column:Food/Housing: 4596 ⟵ “Food/Housing | 6,128 | 4,596 | 3,064 | 0 | 12,256 | 9,192 | 6,128 | 0”
  - column:Books/Prog Fees: 705 ⟵ “Books/Prog Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal: 660 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation: 468 ⟵ “Transportation | 624 | 468 | 312 | 156 | 1,248 | 936 | 624 | 312”
  - column:Total: 15139 ⟵ “Total | 17,282 | 15,139 | 9,948 | 3,434 | 34,564 | 30,278 | 19,895 | 6,879”
  - column:Tuition/fees (2): 8710 ⟵ “Tuition/fees | 8,710 | 8,710 | 5,662 | 3,049 | 17,420 | 17,420 | 11,323 | 6,097”
  - … 119 more rows
### `a0fa8fc960248e79` University of Saint Francis-Fort Wayne — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sf.edu/wp-content/uploads/2026/04/2627_undergradcoa.pdf (sha256 6bbeeef5b2c5)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.sf.edu/wp-content/uploads/2026/04/2627_graduatecoa.pdf
- checks: {"columns": 8, "rows": 18}
  - column:Tuition/fees: 19340 ⟵ “Tuition/fees | 19,340 | 12,378 | 8,703 | 5,028 | 38,680 | 24,755 | 17,406 | 10,057”
  - column:Food/Housing: 6240 ⟵ “Food/Housing | 6,240 | 4,680 | 3,120 | 0 | 12,480 | 9,360 | 6,240 | 0”
  - column:Bks/Prog/Ln Fees: 940 ⟵ “Bks/Prog/Ln Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal: 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation: 624 ⟵ “Transportation | 624 | 468 | 312 | 156 | 1,248 | 936 | 624 | 312”
  - column:Total: 28024 ⟵ “Total | 28,024 | 18,891 | 13,045 | 5,419 | 56,048 | 37,781 | 26,090 | 10,839”
  - column:Tuition/fees (2): 19340 ⟵ “Tuition/fees | 19,340 | 12,378 | 8,703 | 5,028 | 38,680 | 24,755 | 17,406 | 10,057”
  - column:Food/Housing (2): 6384 ⟵ “Food/Housing | 6,384 | 4,788 | 3,192 | 0 | 12,768 | 9,576 | 6,384 | 0”
  - column:Bks/Prog/Ln Fees (2): 940 ⟵ “Bks/Prog/Ln Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal (2): 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation (2): 880 ⟵ “Transportation | 880 | 660 | 440 | 220 | 1,760 | 1,320 | 880 | 440”
  - column:Total (2): 28424 ⟵ “Total | 28,424 | 19,191 | 13,245 | 5,483 | 56,848 | 38,381 | 26,490 | 10,967”
  - column:Tuition/fees (3): 19340 ⟵ “Tuition/fees | 19,340 | 12,378 | 8,703 | 5,028 | 38,680 | 24,755 | 17,406 | 10,057”
  - column:Food/Housing (3): 1072 ⟵ “Food/Housing | 1,072 | 804 | 536 | 0 | 2,144 | 1,608 | 1,072 | 0”
  - column:Bks/Prog/Ln Fees (3): 940 ⟵ “Bks/Prog/Ln Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal (3): 880 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation (3): 880 ⟵ “Transportation | 880 | 660 | 440 | 220 | 1,760 | 1,320 | 880 | 440”
  - column:Total (3): 23112 ⟵ “Total | 23,112 | 15,207 | 10,589 | 5,483 | 46,224 | 30,413 | 21,178 | 10,967”
  - column:Tuition/fees: 12378 ⟵ “Tuition/fees | 19,340 | 12,378 | 8,703 | 5,028 | 38,680 | 24,755 | 17,406 | 10,057”
  - column:Food/Housing: 4680 ⟵ “Food/Housing | 6,240 | 4,680 | 3,120 | 0 | 12,480 | 9,360 | 6,240 | 0”
  - column:Bks/Prog/Ln Fees: 705 ⟵ “Bks/Prog/Ln Fees | 940 | 705 | 470 | 235 | 1,880 | 1,410 | 940 | 470”
  - column:Personal: 660 ⟵ “Personal | 880 | 660 | 440 | 0 | 1,760 | 1,320 | 880 | 0”
  - column:Transportation: 468 ⟵ “Transportation | 624 | 468 | 312 | 156 | 1,248 | 936 | 624 | 312”
  - column:Total: 18891 ⟵ “Total | 28,024 | 18,891 | 13,045 | 5,419 | 56,048 | 37,781 | 26,090 | 10,839”
  - column:Tuition/fees (2): 12378 ⟵ “Tuition/fees | 19,340 | 12,378 | 8,703 | 5,028 | 38,680 | 24,755 | 17,406 | 10,057”
  - … 119 more rows
### `0deeb7187823de78` University of Southern Indiana — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.usi.edu/financial-aid/apply-for-aid/professional-judgment (sha256 0de3f7ffd06a)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.usi.edu/financial-aid/types-of-aid/scholarships/outside
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The Free Application for Federal Student Aid (FAFSA) uses income information from two year's prior and does not allow students the opportunity to explain if there has been a change in circumstances.”
  - sentence: need_based_special_circumstances ⟵ “IRA or Pension Distribution) Graduate/Professional students do not qualify for need-based grants or loans and would not likely benefit from the Special Circumstance process.”
  - sentence: need_based_special_circumstances ⟵ “Please contact USI Financial Assistance to discuss if a Special Circumstance would still benefit you.”
  - sentence: need_based_special_circumstances ⟵ “You may download and complete the Special Circumstance Form online in the Student Financial Assistance forms library for the application.”
  - sentence: need_based_special_circumstances ⟵ “Incomplete Special Circumstances will not be processed.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances/Dependency Overrides Many students feel they are independent because they currently live on their own or because their parents no longer claim them on their income taxes.”
### `2d5f6322baa46761` University of Southern Indiana — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.usi.edu/financial-aid/apply-for-aid/professional-judgment (sha256 0de3f7ffd06a)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Dependency Overrides may only be performed when adequate documentation of extenuating family circumstances exists.”
  - sentence: dependency_override ⟵ “Incomplete Dependency Overrides will not be processed.”
### `6611e58094feb79e` University of Southern Indiana — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.usi.edu/financial-aid/apply-for-aid/professional-judgment (sha256 0de3f7ffd06a)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “When there are unusual situations or circumstances that impact your federal student aid eligibility, federal regulations give a financial aid administrator discretion or professional judgment on a case-by-case basis and with adequate documentation to make adjustments to the data elements on the Free Application for Federal Student Aid (FAFSA®) form that impact your Student Aid Index (SAI) to gain ”
  - sentence: professional_judgment ⟵ “The Department of Education does not have the authority to override a school's professional judgment decision.”
  - sentence: professional_judgment ⟵ “It is important to note that we cannot process professional judgments after the student is no longer enrolled for the academic year for which the request has been submitted.”
  - sentence: professional_judgment ⟵ “There are 3 main types of professional judgments.”
### `6ca02a782d744ffd` University of Southern Indiana — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.usi.edu/financial-aid/types-of-aid/scholarships/outside (sha256 a683e1c5e899)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.usi.edu/financial-aid/apply-for-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Outside Scholarships for students pursuing degrees in: Business Education Nursing and Health Professions Liberal Arts Science and Engineering Graduate degrees Scholarships for: Students with Disabilities or Special Circumstances Government and Military Sponsored Scholarships Other Outside Scholarship Resources: BestColleges Scholarships for International Students Collegeboard.org's Free Scholarshi”
### `f6cf0c991f8fc291` University of Southern Indiana — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.usi.edu/financial-aid/apply-for-aid/professional-judgment (sha256 0de3f7ffd06a)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: budget_increase ⟵ “Budget/Cost of Attendance Adjustments The Financial Aid Budget, also known as the Cost of Attendance (COA), includes allowances for tuition and fees, housing and food, books and supplies, and other miscellaneous expenses.”
  - sentence: budget_increase ⟵ “Approval of a Budget Adjustment Appeal only adjusts the budget, not your billed costs.”
  - sentence: budget_increase ⟵ “Incomplete Budget Adjustment Appeals will not be processed.”
### `408c71482996d64d` University of Southern Indiana — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.usi.edu/financial-aid/manage-your-aid/scholarship-guidelines/2024-2025-presidential-scholarship (sha256 85cd0fedd91b)
- issues: residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Estimated tuition: 8975.7 ⟵ “Estimated tuition | $8,975.70 | $4,487.85”
  - on_campus:One time fees (Matriculation, Assessment, Enrollment)*: 475 ⟵ “One time fees (Matriculation, Assessment, Enrollment)* | $475 | $475”
  - on_campus:Estimated Lab Fees: 150 ⟵ “Estimated Lab Fees | $150 | $75”
  - on_campus:USI campus housing allowance: 5228 ⟵ “USI campus housing allowance | $5,228 | $2,614”
  - on_campus:Housing pre-payment allowance (Paid fall only): 200 ⟵ “Housing pre-payment allowance (Paid fall only) | $200 | $200”
  - on_campus:Food allowance: 5232 ⟵ “Food allowance | $5,232 | $2,616”
  - on_campus:Books/Supplies allowance: 1200 ⟵ “Books/Supplies allowance | $1,200 | $600”
  - on_campus:TOTAL: 21460.7 ⟵ “TOTAL | $21,460.70 | $11,067.85”
### `47ea774c9f69dfc9` University of Southern Indiana — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.usi.edu/financial-aid/manage-your-aid/scholarship-guidelines/2025-2026-presidential-scholarship (sha256 481b0100f0b6)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Estimated tuition: 8975.7 ⟵ “Estimated tuition | $8,975.70 | $4,487.85”
  - on_campus:One time fees (Matriculation, Assessment, Enrollment)*: 475 ⟵ “One time fees (Matriculation, Assessment, Enrollment)* | $475 | $475”
  - on_campus:Comprehensive Learning Fees: 400 ⟵ “Comprehensive Learning Fees | $400 | $200”
  - on_campus:USI campus housing allowance: 5408 ⟵ “USI campus housing allowance | $5,408 | $2,704”
  - on_campus:Housing pre-payment allowance (Paid fall only): 200 ⟵ “Housing pre-payment allowance (Paid fall only) | $200 | $200”
  - on_campus:Food allowance: 5700 ⟵ “Food allowance | $5,700 | $2,850”
  - on_campus:Books/Supplies allowance: 1200 ⟵ “Books/Supplies allowance | $1,200 | $600”
  - on_campus:TOTAL: 22358.7 ⟵ “TOTAL | $22,358.70 | $11,516.85”
### `613d5ea4592817be` University of Southern Indiana — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.usi.edu/financial-aid/manage-your-aid/scholarship-guidelines/2026-2027-presidential-scholarship (sha256 96bfbe5a0144)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Estimated tuition: 8975.7 ⟵ “Estimated tuition | $8,975.70 | $4,487.85”
  - on_campus:One time fees (Matriculation, Assessment, Enrollment)*: 475 ⟵ “One time fees (Matriculation, Assessment, Enrollment)* | $475 | $475”
  - on_campus:Comprehensive Learning Fees: 400 ⟵ “Comprehensive Learning Fees | $400 | $200”
  - on_campus:USI Campus Housing (Standard 4-Person Unit): 5772 ⟵ “USI Campus Housing (Standard 4-Person Unit) | $5,772 | $2,886”
  - on_campus:Housing pre-payment (Paid fall only): 300 ⟵ “Housing pre-payment (Paid fall only) | $300 | $300”
  - on_campus:USI Meal Plan: 5872 ⟵ “USI Meal Plan | $5,872 | $2,936”
  - on_campus:Archies Book Bundle: 720 ⟵ “Archies Book Bundle | $720 | $360”
  - on_campus:TOTAL: 22514.7 ⟵ “TOTAL | $22,514.7 | $11,644.85”
### `ac3cfa68dae25c7e` University of Southern Indiana — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.usi.edu/media/qtrdjr4g/clepcredit.pdf (sha256 3f2d77f3302a)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 25, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50+]:  ⟵ “American Government                                       50+       POLS 102                                   3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|51+]:  ⟵ “Analyzing and Interpreting Literature                     51+       ENG 105                                    3”
  - equivalencies[CLEP-BIOLOGY|50+]:  ⟵ “Biology                                                   50+       BIOL 1-EL (100-Level Elective, non-lab)    3”
  - equivalencies[CLEP-CALCULUS|53+]:  ⟵ “Calculus                                                  53+       MATH 230                                   4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|53+]:  ⟵ “College Algebra                                           53+       MATH 111                                   4”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50+]:  ⟵ “College Composition (includes essay)                      50+       ENG 101                                    3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50+]:  ⟵ “College Composition Modular (no essay)                    50+       ENG 1-EL (100-Level Elective)              3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|53+]:  ⟵ “College Mathematics                                       53+       MATH 115                                   4”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50+]:  ⟵ “Educational Psychology                                    50+       PSY 1-EL (100-Level Elective)              3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|52+]:  ⟵ “Financial Accounting                                      52+       ACCT 201                                   3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|49+]:  ⟵ “History of the United States I                            49+       HIST 101                                   3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|49+]:  ⟵ “History of the United States II                           49+       HIST 102                                   3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50+]:  ⟵ “Human Growth and Development                              50+       PSY 261                                    3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|53+]:  ⟵ “Information Systems                                       53+       CIS 101                                    1”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|51+]:  ⟵ “Introductory Business Law                                 51+       BLAW 263                                   3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50+]:  ⟵ “Introductory Psychology                                   50+       PSY 201                                    3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50+]:  ⟵ “Introductory Sociology                                    50+       SOC 121                                    3”
  - equivalencies[CLEP-PRECALCULUS|57+]:  ⟵ “Precalculus                                               57+       MATH 115                                   4”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|49+]:  ⟵ “Principles of Macroeconomics                              49+       ECON 209                                   3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50+]:  ⟵ “Principles of Management                                  50+       MNGT 305                                   3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50+]:  ⟵ “Principles of Marketing                                   50+       MKTG 305                                   3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|47+]:  ⟵ “Principles of Microeconomics                              47+       ECON 208                                   3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|6]:  ⟵ “Spanish w/ Writing: Level 1, 2 and 3                     57-62      SPAN 101, 102                              6”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50+]:  ⟵ “Western Civilization I: Ancient Near East to 1648         50+       HIST 140                                   3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50+]:  ⟵ “Western Civilization II: 1648 to the Present              50+       HIST 140 x2                                6”
### `1800cc04e1f7399d` Valparaiso University — admissions_metrics 2021-22 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/CDS_2021-2022_withdisclaimer_without_scores_012225.pdf (sha256 192c51bdd52e)
- issues: stale_year_label:2021-22
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 7013 ⟵ “Total first-time, first-year (degree-seeking) who applied                                  7013”
  - admits: 5675 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                            5675”
  - enrolled: 601 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                                  601”
### `195e66b9731892c4` Valparaiso University — admissions_metrics 2006-07 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/cds06-07-revised2.pdf (sha256 62dffbb7f9d8)
- issues: c1_totals_incomplete, stale_year_label:2006-07
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [520, 650] ⟵ “SAT Math                          520                   650”
  - act_25..75: [22, 28] ⟵ “ACT Composite                         22                   28”
### `249f81417039099f` Valparaiso University — admissions_metrics 2007-08 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/cds07-08-revised2.pdf (sha256 8ae79d589095)
- issues: c1_totals_incomplete, stale_year_label:2007-08
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [500, 640] ⟵ “SAT Math                              500                 640”
  - act_25..75: [22, 28] ⟵ “ACT Composite                          22                  28”
### `314cc5a3edd5828c` Valparaiso University — admissions_metrics 2002-03 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/cds02-03-revised.pdf (sha256 13846bb33b04)
- issues: c1_totals_incomplete, stale_year_label:2002-03
- checks: {"fields": ["act_25", "act_75", "entering_fall_year"]}
  - act_25..75: [23, 29] ⟵ “ACT Composite              23                    29”
### `322721f1f5f5f5cb` Valparaiso University — admissions_metrics 2016-17 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/CDS_2016-2017-FINAL-corrected.pdf (sha256 e4ac3150b91a)
- issues: c1_totals_incomplete, stale_year_label:2016-17
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [490, 600] ⟵ “SAT Math                      490                 600”
  - act_25..75: [23, 29] ⟵ “ACT Composite                 23                  29”
### `3c5d60dfbb1c3e18` Valparaiso University — admissions_metrics 2017-18 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/CDS_2017-2018_CORRECTED11.16.18.pdf (sha256 6b3f0a0ff450)
- issues: c1_totals_incomplete, stale_year_label:2017-18
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [530, 640] ⟵ “SAT Math                    530                  640”
  - act_25..75: [23, 29] ⟵ “ACT Composite               23                   29”
### `405aa81af1d5e169` Valparaiso University — admissions_metrics 2005-06 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/cds05-06-revised2.pdf (sha256 5c1ea319d1df)
- issues: c1_totals_incomplete, stale_year_label:2005-06
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [520, 640] ⟵ “SAT Math                     520                    640”
  - act_25..75: [23, 28] ⟵ “ACT Composite                 23                    28”
### `60f95467c181b606` Valparaiso University — admissions_metrics 2008-09 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/cds08-09-revised2.pdf (sha256 96d927bb1679)
- issues: c1_totals_incomplete, stale_year_label:2008-09
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [500, 630] ⟵ “SAT Math                              500                 630”
  - act_25..75: [22, 28] ⟵ “ACT Composite                          22                  28”
### `70113f7a17cd0ddb` Valparaiso University — admissions_metrics 2018-19 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/CDS_2018-2019.version7submit.06.30.21.pdf (sha256 54c2d3fdc95a)
- issues: c1_totals_incomplete, stale_year_label:2018-19
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [530, 640] ⟵ “SAT Math                    530                  640”
  - act_25..75: [23, 29] ⟵ “ACT Composite               23                   29”
### `7427d99f0307060d` Valparaiso University — admissions_metrics 2004-05 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/cds04-05-revised.pdf (sha256 4ecd37721231)
- issues: c1_totals_incomplete, stale_year_label:2004-05
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [530, 640] ⟵ “SAT Math                      530                    640”
  - act_25..75: [23, 29] ⟵ “ACT Composite                  23                    29”
### `784054cabf26ccdd` Valparaiso University — admissions_metrics 2019-20 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/CDS_2019-2020.submit.v7.pdf (sha256 ab4f0e3ce4d5)
- issues: c1_totals_incomplete, stale_year_label:2019-20
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_75", "sat_math_25", "sat_math_75"]}
  - sat_composite_25..75: [1090, 1290] ⟵ “SAT Composite                     1090                   1290”
  - sat_math_25..75: [530, 650] ⟵ “SAT Math                            530                    650”
  - act_25..75: [22, 29] ⟵ “ACT Composite                        22                     29”
### `863cb1adb067e79b` Valparaiso University — admissions_metrics 2020-21 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/CDS_2020-2021.web_.rev012225.pdf (sha256 0fd6aa98374d)
- issues: c1_totals_incomplete, stale_year_label:2020-21
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_75", "sat_math_25", "sat_math_75"]}
  - sat_composite_25..75: [1090, 1270] ⟵ “SAT Composite                         1090                       1270”
  - sat_math_25..75: [530, 640] ⟵ “SAT Math                              530                         640”
  - act_25..75: [22, 29] ⟵ “ACT Composite                          22                          29”
### `c178c553e995404d` Valparaiso University — admissions_metrics 2009-10 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/cds09-10-revised2.pdf (sha256 18f25de8207e)
- issues: c1_totals_incomplete, stale_year_label:2009-10
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_math_25", "sat_math_75"]}
  - sat_math_25..75: [500, 620] ⟵ “SAT Math                              500                 620”
  - act_25..75: [22, 29] ⟵ “ACT Composite                          22                  29”
### `e933a8dc4d8185c1` Valparaiso University — admissions_metrics 2001-02 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/cds01-02-revised.pdf (sha256 ef37b42316e2)
- issues: c1_totals_incomplete, stale_year_label:2001-02
- checks: {"fields": ["act_25", "act_75", "entering_fall_year"]}
  - act_25..75: [24, 29] ⟵ “ACT Composite              24                    29”
### `f42ecaf57e444ea5` Valparaiso University — admissions_metrics 2003-04 [new] (labeled_in_source)
- source: https://www.valpo.edu/wp-content/uploads/2025/06/cds03-04-revised.pdf (sha256 fc181870e39c)
- issues: c1_totals_incomplete, stale_year_label:2003-04
- checks: {"fields": ["act_25", "act_75", "entering_fall_year"]}
  - act_25..75: [23, 29] ⟵ “ACT Composite                 23                     29”
### `1dcf1306277e0a6b` Valparaiso University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.valpo.edu/aid/scholarships/freshman/ (sha256 2c5f4fb0fa9b)
- issues: ambiguous_year_labels, duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $30,000 ⟵ “3.0 to 3.39 | Beacon Scholarship | $30,000”
  - gpa_requirement: 3.0 to 3.39 ⟵ “3.0 to 3.39 | Beacon Scholarship | $30,000”
### `2e45c2f727fbbedc` Valparaiso University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.valpo.edu/aid/scholarships/freshman/ (sha256 2c5f4fb0fa9b)
- issues: ambiguous_year_labels, duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $25,000 ⟵ “2.8 to 2.99 | Leadership Award | $25,000”
  - gpa_requirement: 2.8 to 2.99 ⟵ “2.8 to 2.99 | Leadership Award | $25,000”
### `769f7eefcc2610e1` Valparaiso University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.valpo.edu/aid/scholarships/freshman/ (sha256 2c5f4fb0fa9b)
- issues: ambiguous_year_labels, duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $31,000-$33000 ⟵ “3.40 to 4.19 | Presidential Scholarship | $31,000-$33000”
  - gpa_requirement: 3.40 to 4.19 ⟵ “3.40 to 4.19 | Presidential Scholarship | $31,000-$33000”
### `661ff1a4ca0e7467` Valparaiso University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.valpo.edu/admission/transfer/community-college-partners/shoreline-community-college/ (sha256 f57b77b87b7d)
- issues: rows_without_score
- checks: {"distinct_exams": 2, "equivalencies": 6, "rows_without_score": 6}
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “CHEM 121 General Chemistry I |  | 4 | CHEM 181 | 4 | 0”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “CHEM 122 General Chemistry II |  | 4 | CHEM 182 | 4 | 0”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “CHEM 221 Organic Chemistry I |  | 4 | CHEM&241 | 4 | 0”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “CHEM 222 Organic Chemistry II |  | 4 | CHEM&242 | 4 | 0”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “BIO 450 Molecular Biology |  | 4 | BIOL 270 + BIOL 274 | 4 | 0”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry 115 Essentials of Chemistry |  | 4 | CHEM 171 | 4 | 0”
### `mf2339f959157d73` Valparaiso University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.valpo.edu/admission/undergraduate/dual-enrollment/ (sha256 caec9a9a6980)
- issues: conflicting_sources:tuition_per_credit_hour
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have at least sophomore standing at their high school with a cumulative grade point average of 3.0 or higher”
  - per_credit_hour_charge: 104 ⟵ “Dual Enrollment Tuition: $104 per credit”
  - per_credit_hour_charge: 100 ⟵ “•   Dual Enrollment tuition is $100/credit hour. The cost of course materials, or any course-”
  - eligibility_tier: 4.0 ⟵ “The university operates on a 4.0 grade point scale; however, the high school may calculate the high”
  - eligibility_tier: 3.0 ⟵ “cumulative GPA of 3.0/4.0, and be ranked in the top half of the graduating class. Exceptions may”
### `d6db23eb4861e989` Vincennes University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.vinu.edu/financial-services/financial-aid.html (sha256 372aaaaee647)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “FAFSA Information FAFSA Information | Category | Topic | Definition | FAFSA Information | FAFSA | The FAFSA (Free Application for Federal Student Aid) must be filed annually to determine a student's eligibility for federal financial aid and state grants, additional data can be found here. | Special & Unusual Circumstances | A Special Circumstance is when a student or their family's financial situa”
  - sentence: need_based_special_circumstances ⟵ “An Unusual Circumstance is a unique situation, such as parental abandonment or human trafficking, that impacts a dependent student's dependency status on the FAFSA, requiring them to either request a change in status, add parent information, or opt for a Parent Disavowal of Support to be eligible for aid. | Verification | Sometimes the FAFSA system selects students for a verification process, whic”
### `155644359395dbff` Wabash College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wabash.edu/admissions/docs/PJ-Policy-for-Publication-092724.pdf (sha256 c1b56a9e5e3e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment Policy The Higher Education Act of 1965 (HEA), as amended, provides the authority for financial aid administrators to exercise discretion in a number of areas when a student has special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “This authority is known as Professional Judgment (PJ).”
### `a3b3e6cff6521a69` Wabash College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.wabash.edu/admissions/finances/aid (sha256 18becfc7a026)
- issues: semantic_review_required, conflicting_sources:https://www.wabash.edu/admissions/current,https://www.wabash.edu/admissions/docs/PJ-Policy-for-Publication-092724.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances When determining your financial aid package, we make every effort to offer you the maximum amount of assistance you are eligible to receive from the resources available.”
### `c8be7df1024a80dd` Wabash College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wabash.edu/admissions/docs/SAP-Policy-Handout-updated-08-12-25.pdf (sha256 57388f5192af)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Extenuating circumstances eligible for consideration include: • Death of an immediate family member • Student injury or illness • Other special circumstances All appeals are reviewed by the SAP Appeals Committee and all decisions are final.”
### `ea6ac85176662419` Wabash College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wabash.edu/admissions/current (sha256 64e70a88ea2e)
- issues: semantic_review_required, conflicting_sources:https://www.wabash.edu/admissions/docs/PJ-Policy-for-Publication-092724.pdf,https://www.wabash.edu/admissions/finances/aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances When determining your financial aid package, we make every effort to offer you the maximum amount of assistance you are eligible to receive from the resources available.”
### `fabda52cabc5a6ca` Wabash College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wabash.edu/admissions/docs/PJ-Policy-for-Publication-092724.pdf (sha256 c1b56a9e5e3e)
- issues: semantic_review_required, conflicting_sources:https://www.wabash.edu/admissions/current,https://www.wabash.edu/admissions/finances/aid
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Generally speaking, circumstances beyond a family’s control that impact their ability to pay for current educational costs may be considered.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances (Dependency Status) A student is considered to be independent if they can answer “yes” to any of the dependency questions on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Documentation of unusual circumstances may allow us to perform a “dependency override” to make the student independent for financial aid purposes.”
  - sentence: need_based_special_circumstances ⟵ “Our office will contact such students to request documentation to support their unusual circumstances.”
### `522153d6dc6a7d0d` Wabash College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wabash.edu/admissions/docs/Virtual-FA-Night-2025-.pdf (sha256 cfef78d9d2a5)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.wabash.edu/admissions/finances/costs
- checks: {"columns": 2, "rows": 6}
  - column:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300”
  - column:Tuition & Fees: 54100 ⟵ “Tuition & Fees | $54,100 | Personal Expenses | $1,600”
  - column:Campus Housing: 7700 ⟵ “Campus Housing | $7,700 | Transportation* | $650”
  - column:15 Meal Plan: 7000 ⟵ “15 Meal Plan | $7,000 | Federal Loan Fees | $70”
  - column:TOTAL: 68800 ⟵ “TOTAL | $68,800 | Additional Food | $750”
  - column:TOTAL (2): 4370 ⟵ “TOTAL | $4,370”
  - column:Tuition & Fees: 1600 ⟵ “Tuition & Fees | $54,100 | Personal Expenses | $1,600”
  - column:Campus Housing: 650 ⟵ “Campus Housing | $7,700 | Transportation* | $650”
  - column:15 Meal Plan: 70 ⟵ “15 Meal Plan | $7,000 | Federal Loan Fees | $70”
  - column:TOTAL: 750 ⟵ “TOTAL | $68,800 | Additional Food | $750”
### `5434636526255277` Wabash College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wabash.edu/admissions/finances/costs (sha256 210b533351ce)
- issues: conflicting_sources:https://www.wabash.edu/admissions/docs/Virtual-FA-Night-2025-.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Tuition: 52900 ⟵ “Tuition | $52,900”
  - column:Student Activities Fee: 500 ⟵ “Student Activities Fee | $500”
  - column:Health Center Fee: 700 ⟵ “Health Center Fee | $700”
  - column:On-Campus Housing & Food (15 meals): 14700 ⟵ “On-Campus Housing & Food (15 meals) | $14,700”
  - column:Books, Course Materials, Supplies, & Equipment (Estimated): 1300 ⟵ “Books, Course Materials, Supplies, & Equipment (Estimated) | $1,300”
  - column:Personal Expenses (Estimated): 1600 ⟵ “Personal Expenses (Estimated) | $1,600”
  - column:Additional Meals (Estimated: 750 ⟵ “Additional Meals (Estimated | $750”
  - column:Federal Student Loan Fees (Estimated): 70 ⟵ “Federal Student Loan Fees (Estimated) | $70”
  - column:Indiana Resident Travel Expenses (Estimated) **travel expenses vary outside of Indiana: 650 ⟵ “Indiana Resident Travel Expenses (Estimated) **travel expenses vary outside of Indiana | $650”
  - column:Total Cost: 73170 ⟵ “Total Cost | $73,170”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 1; pages by category: 

## Blocked by the site (every request refused; needs the browser fallback)

- Anderson University (`ipeds-150066`)
- Franklin College (`ipeds-150604`)
- Oakland City University (`ipeds-152099`)
- Horizon University (`ipeds-457226`)

## Leads: official pages found with no extracted record

- Ball State University: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Bethel University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- Butler University: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Calumet College of Saint Joseph: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- DePauw University: admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Earlham College: cost_of_attendance, admissions_tests, merit_scholarships, ib_credit, dual_enrollment, statewide_articulation, degree_requirements
- Goshen College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency
- Grace College and Theological Seminary: cost_of_attendance, admissions_tests, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Hanover College: admissions_tests, ap_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Holy Cross College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Huntington University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- Indiana Institute of Technology: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, statewide_articulation
- Indiana Institute of Technology-College of Professional Studies: transfer_credit
- Indiana State University: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit
- Indiana University-Bloomington: cost_of_attendance, merit_scholarships
- Indiana University-East: admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Indiana University-Indianapolis: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- Indiana University-Kokomo: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency
- Indiana University-Northwest: tuition_fees, cost_of_attendance, merit_scholarships
- Indiana University-South Bend: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Indiana Wesleyan University-Marion: tuition_fees, transfer_credit, statewide_articulation, degree_requirements
- Indiana Wesleyan University-National & Global: tuition_fees, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- Ivy Tech Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, statewide_articulation, residency, degree_requirements
- Manchester University: cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, residency, degree_requirements
- Marian University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, residency, degree_requirements
- Marian University-Ancilla: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, residency
- Martin University: tuition_fees
- Mid-America College of Funeral Service: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements, aid_appeals
- Purdue University Fort Wayne: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Purdue University Global: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency
- Purdue University Northwest: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Purdue University-Main Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Rose-Hulman Institute of Technology: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit
- Saint Mary's College: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, ib_credit, dual_enrollment
- Saint Mary-of-the-Woods College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Taylor University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, ib_credit, aid_appeals
- Trine University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships
- Trine University-Regional/Non-Traditional Campuses: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships
- Union Bible College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, degree_requirements
- University of Evansville: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation
- University of Indianapolis: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- University of Notre Dame: admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit
- University of Saint Francis-Fort Wayne: cost_of_attendance, admissions_tests, clep_credit, dual_enrollment, residency, degree_requirements
- University of Southern Indiana: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, residency, degree_requirements
- Valparaiso University: tuition_fees, cost_of_attendance, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Veritas Baptist College: tuition_fees, admissions_tests, merit_scholarships
- Vincennes University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Wabash College: admissions_tests, clep_credit, dual_enrollment, degree_requirements
