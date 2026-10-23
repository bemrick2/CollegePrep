# Review queue — UT (2026-27)

Pages fetched: 180; failures: 17. Candidates: 3 (1 without issues, 2 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 1 | 0 | 0 | 0 | 2 | 0 | 10 |
| cost_of_attendance | 1 | 0 | 0 | 0 | 2 | 0 | 10 |
| admissions_tests | 0 | 0 | 0 | 0 | 2 | 0 | 11 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 2 | 11 |
| merit_scholarships | 0 | 1 | 0 | 0 | 2 | 0 | 10 |
| ap_credit | 1 | 2 | 0 | 0 | 1 | 1 | 8 |
| clep_credit | 0 | 1 | 0 | 1 | 0 | 1 | 10 |
| ib_credit | 1 | 1 | 0 | 1 | 0 | 1 | 9 |
| dual_enrollment | 0 | 1 | 0 | 0 | 0 | 1 | 11 |
| transfer_credit | 0 | 1 | 0 | 0 | 2 | 0 | 10 |
| statewide_articulation | 0 | 0 | 0 | 0 | 1 | 1 | 11 |
| residency | 0 | 0 | 0 | 0 | 1 | 1 | 11 |
| degree_requirements | 1 | 0 | 0 | 0 | 2 | 0 | 10 |
| aid_appeals | 0 | 0 | 0 | 0 | 1 | 1 | 11 |

## Ready for review (1)

### `16163222917ed58a` Weber State University — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.weber.edu/dual-enrollment/early-college.html (sha256 770da9605f16)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a cumulative high school and WSU GPA of 3.00 or higher.”

## Exceptions (2)

### `2204243d6fdf2aa5` Weber State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.weber.edu/Admissions/International_Baccalaureate.html (sha256 732c26efcb54)
- issues: score_column_not_scores
- checks: {"distinct_exams": 29, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-SL|Biology SL]:  ⟵ “ | Biology SL | 4+ | ZOOL 1010 LS (3cr) | 3”
  - equivalencies[IB-BIOLOGY-HL|Biology HL]:  ⟵ “ | Biology HL | 4+ | ZOOL 1610 LS (4cr) | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|Business Management SL]:  ⟵ “ | Business Management SL | 4+ | BSAD 1XXX (3cr) | 3”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|Business Management HL]:  ⟵ “ | Business Management HL | 4+ | BSAD 1XXX (6cr) | 6”
  - equivalencies[IB-CHEMISTRY-SL|Chemistry SL]:  ⟵ “ | Chemistry SL | 4+ | CHEM 1XXX (3cr) | 3”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry HL]:  ⟵ “ | Chemistry HL | 4+ | CHEM 1010 PS (3cr) | 3”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|Computer Science SL]:  ⟵ “ | Computer Science SL | 4+ | CS 1030 (4cr) | 4”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|Computer Science HL]:  ⟵ “ | Computer Science HL | 4+ | CS 1030 (4cr) | 4”
  - equivalencies[IB-ECONOMICS-SL|Economics SL]:  ⟵ “ | Economics SL | 4+ | ECON 1010 SS (3cr) | 3”
  - equivalencies[IB-ECONOMICS-HL|Economics HL]:  ⟵ “ | Economics HL | 4+ | ECON 2010 SS (3cr) & ECON SS 2020 (3cr) | 6”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|Environmental Systems and Tech SL]:  ⟵ “ | Environmental Systems and Tech SL | 4+ | BTNY 1XXX (3cr) | 3”
  - equivalencies[IB-FILM-SL|Film SL]:  ⟵ “ | Film SL | 4+ | THEA 1023 CA (3cr) | 3”
  - equivalencies[IB-FILM-HL|Film HL]:  ⟵ “ | Film HL | 4+ | THEA 1023 CA (3cr) and THEA 1XXX (2cr) | 5”
  - equivalencies[IB-GEOGRAPHY-SL|Geography SL]:  ⟵ “ | Geography SL | 4+ | GEOG 1300 SS/CC (3cr) | 3”
  - equivalencies[IB-GEOGRAPHY-HL|Geography HL]:  ⟵ “ | Geography HL | 4+ | GEOG 1000 PS (3cr) & GEOG 1300 SS/CC (3cr) | 6”
  - equivalencies[IB-HISTORY-SL|History SL]:  ⟵ “ | History SL | 4+ | HIST 1XXX (3cr) | 3”
  - equivalencies[IB-HISTORY-HL|History HL]:  ⟵ “ | History HL | 4+ | HIST 1XXX (3cr) and HIST 1510 SS/CC GLB (3cr) | 6”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|Math: Analysis & Approaches SL]:  ⟵ “ | Math: Analysis & Approaches SL | 4+ | MATH 1050 QL (4cr) | 4”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|Math: Analysis & Approaches HL]:  ⟵ “ | Math: Analysis & Approaches HL | 4 | MATH 1080 QL (5cr) | 5”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|Math: Analysis & Approaches HL]:  ⟵ “ | Math: Analysis & Approaches HL | 5+ | MATH 1210 (4cr) | 4”
  - equivalencies[IB-MUSIC-SL|Music SL]:  ⟵ “ | Music SL | 4+ | MUSC 1XXX (3cr) | 3”
  - equivalencies[IB-MUSIC-HL|Music HL]:  ⟵ “ | Music HL | 4+ | MUSC 1010 CA (3cr) | 3”
  - equivalencies[IB-PHYSICS-SL|Physics SL]:  ⟵ “ | Physics SL | 4+ | PHYS 1010 PS (3cr) | 3”
  - equivalencies[IB-PHYSICS-HL|Physics HL]:  ⟵ “ | Physics HL | 4+ | PHYS 2010 PS (5cr) & PHYS 2020 (5cr) | 10”
  - equivalencies[IB-PSYCHOLOGY-SL|Psychology SL]:  ⟵ “ | Psychology SL | 4+ | PSY 1010 SS (3cr) | 3”
  - … 5 more rows
### `46a4f9b851e0bcba` Weber State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.weber.edu/Admissions/cleptest.html (sha256 e779ecf49810)
- issues: score_column_not_scores, score_scale_mismatch
- checks: {"distinct_exams": 27, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|American Government]:  ⟵ “ | American Government | 50+ | POLS 1100 AI | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|American Literature]:  ⟵ “ | American Literature | 50+ | ENGL 2200 HU/CC | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|Analyzing & Interpreting Literature]:  ⟵ “ | Analyzing & Interpreting Literature | 50+ | ENGL 2200 HU/CC | 3”
  - equivalencies[CLEP-BIOLOGY|Biology]:  ⟵ “ | Biology | 50+ | ZOOL 1010 LS (No lab credit awarded) | 3”
  - equivalencies[CLEP-CALCULUS|Calculus]:  ⟵ “ | Calculus | 64+ | MATH 1210 | 4”
  - equivalencies[CLEP-CHEMISTRY|General Chemistry]:  ⟵ “ | General Chemistry | 50+ | CHEM 1010 PS | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|College Algebra]:  ⟵ “ | College Algebra | 63+ | MATH 1050 QL | 4”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|College Composition]:  ⟵ “ | College Composition | 50+ | ENGL 1010 EN | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|College Mathematics]:  ⟵ “ | College Mathematics | 55+ | MATH 1030 QL | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|English Literature]:  ⟵ “ | English Literature | 50+ | ENGL 2200 HU/CC | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|Financial Accounting]:  ⟵ “ | Financial Accounting | 50+ | ACTG 2010 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French Language, Level 1]:  ⟵ “ | French Language, Level 1 | 50-58 | FRCH 1010 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French Language, Level 2]:  ⟵ “ | French Language, Level 2 | 59+ | FRCH 1020 & FRCH 2010 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German Language, Level 1]:  ⟵ “ | German Language, Level 1 | 50-58 | GRMN 1010 | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German Language, Level 2]:  ⟵ “ | German Language, Level 2 | 59+ | GRMN 1020 & GRMN 2010 | 6”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|Human Growth & Development]:  ⟵ “ | Human Growth & Development | 50+ | CHF 1500 SS | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|Information Systems]:  ⟵ “ | Information Systems | 50+ | MIS 2XXX | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|Introductory Business Law]:  ⟵ “ | Introductory Business Law | 50+ | BSAD 2XXX | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|Introductory Psychology]:  ⟵ “ | Introductory Psychology | 50+ | PSY 1010 SS | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|Introductory Sociology]:  ⟵ “ | Introductory Sociology | 50+ | SOC 1010 SS/CC | 3”
  - equivalencies[CLEP-PRECALCULUS|Pre-Calculus]:  ⟵ “ | Pre-Calculus | 61+ | MATH 1060 QL | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|Principles of Macroeconomics]:  ⟵ “ | Principles of Macroeconomics | 50+ | ECON 2020 SS | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|Principles of Management]:  ⟵ “ | Principles of Management | 50+ | MGMT 2XXX | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|Principles of Marketing]:  ⟵ “ | Principles of Marketing | 50+ | MTKG 2XXX | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|Principles of Microeconomics]:  ⟵ “ | Principles of Microeconomics | 50+ | ECON 2010 SS | 3”
  - … 6 more rows

## Re-verification of existing records (32)

- source_not_fetched: data/institutions/ensign/credit_policies/2026-27.json ["credit_policies", "ipeds-230418", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/ensign/credit_policies/2026-27.json ["credit_policies", "ipeds-230418", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/ensign/transfer_policies/2026-27.json ["transfer_policies", "ipeds-230418", null, "2026-27", {}]
- source_not_fetched: data/institutions/suu/credit_policies/2026-27.json ["credit_policies", "ipeds-230603", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/suu/credit_policies/2026-27.json ["credit_policies", "ipeds-230603", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/utah/awards/2026-27.json ["awards", "ipeds-230764", null, "2026-27", {"award_name": "Provost\u2019s Scholarship"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "dance-b-s", "requirement_key": "program-requirements-distribution-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "dance-b-s", "requirement_key": "program-requirements-ballroom-dance-track"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "dance-b-s", "requirement_key": "program-requirements-strongly-recommended-3"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "music-a-s", "requirement_key": "program-requirements-distribution-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "music-b-a", "requirement_key": "program-requirements-distribution-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "music-b-a", "requirement_key": "program-requirements-musicianship-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "music-b-s", "requirement_key": "program-requirements-distribution-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "music-b-s", "requirement_key": "program-requirements-musicianship-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "music-b-s", "requirement_key": "program-requirements-ensembles"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "music-education-b-s", "requirement_key": "program-requirements-performance-skills-development-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "performance-b-m", "requirement_key": "program-requirements-music-industry-and-technology"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "performance-b-m", "requirement_key": "program-requirements-large-ensembles"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-directing-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-performance-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-capstone-course"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-design-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-technical-production-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-capstone-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-dramaturgy-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-film-studies-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-scriptwriting-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-theatre-administration-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-theatre-for-children-and-youth-courses"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "theatre-studies-b-a", "requirement_key": "program-requirements-capstone-courses-2"}]
- source_not_fetched: data/institutions/uvu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-230737", null, "2026-27", {"program_key": "nursing-b-s", "requirement_key": "sample-plan"}]
- all_values_found_year_not_labeled: data/institutions/weber/credit_policies/2026-27.json ["credit_policies", "ipeds-230782", null, "2026-27", {"policy_kind": "dual_enrollment"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Weber State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Western Governors University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
