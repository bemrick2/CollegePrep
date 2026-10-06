# Review queue — RI (2026-27)

Pages fetched: 912; failures: 33. Candidates: 189 (115 without issues, 74 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 4 | 6 | 2 | 0 | 1 |
| cost_of_attendance | 0 | 0 | 1 | 2 | 8 | 1 | 1 |
| admissions_tests | 0 | 0 | 1 | 0 | 11 | 0 | 1 |
| common_data_set | 0 | 0 | 1 | 0 | 0 | 11 | 1 |
| merit_scholarships | 0 | 0 | 1 | 0 | 9 | 2 | 1 |
| ap_credit | 0 | 0 | 0 | 1 | 5 | 6 | 1 |
| clep_credit | 0 | 0 | 0 | 1 | 3 | 8 | 1 |
| ib_credit | 0 | 0 | 0 | 0 | 1 | 11 | 1 |
| dual_enrollment | 0 | 0 | 2 | 0 | 4 | 6 | 1 |
| transfer_credit | 0 | 0 | 6 | 0 | 5 | 1 | 1 |
| statewide_articulation | 0 | 0 | 0 | 0 | 5 | 7 | 1 |
| residency | 0 | 0 | 0 | 0 | 9 | 3 | 1 |
| degree_requirements | 0 | 0 | 1 | 0 | 4 | 7 | 1 |
| aid_appeals | 0 | 0 | 0 | 7 | 1 | 4 | 1 |

## Ready for review (115)

### `68e221be7287e974` Brown University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://finaid.brown.edu/estimate-cost-aid/cost (sha256 664bea1ac1c2)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 74568 ⟵ “Tuition | $74,568”
  - column:Fees (includes $100 Academic record fee for first time students): 3084 ⟵ “Fees (includes $100 Academic record fee for first time students) | $3,084”
  - column:Housing: 10710 ⟵ “Housing | $10,710”
  - column:Food: 8754 ⟵ “Food | $8,754”
  - column:Subtotal - Direct Charges: 97116 ⟵ “Subtotal - Direct Charges | $97,116”
  - column:Miscellaneous Personal Expenses: 2878 ⟵ “Miscellaneous Personal Expenses | $2,878”
  - column:Total Direct and Indirect Charges: 99994 ⟵ “Total Direct and Indirect Charges | $99,994”
### `8be38460ecf7e1f4` Bryant University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.bryant.edu/undergraduate/undergraduate-admission/applying-bryant/transfer-students (sha256 ff881f6ad858)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “You may transfer up to 62 credits for courses in which you’ve received a grade of “C” or better and that fit into the Bryant curriculum.”
### `038b07f83ede89c3` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-sustainable-agriculture-and-food-systems-ba [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/sustainable-agriculture-ba-uri/ (sha256 1474287cf798)
- checks: {"courses": 13, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Sustainable Agriculture and Food Systems BA ⟵ “Biology Transfer, Sustainable Agriculture and Food Systems BA - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `05653ed27cd98197` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-kinesiology-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/kinesiology-bs-uri/ (sha256 614447811fe6)
- checks: {"courses": 12, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Kinesiology BS ⟵ “Biology Transfer, Kinesiology BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `08e062097e59c06a` Community College of Rhode Island — academic_programs 2026-27 · program_key=business-transfer-management-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/management-bs-ric/ (sha256 cbb8e25da914)
- checks: {"courses": 12, "groups": 5, "groups_skipped": 0}
  - program_name: Business Transfer, Management BS ⟵ “Business Transfer, Management BS - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `0a4b40e8a5d5bbdb` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-marine-affairs-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/marine-affairs-bs-uri/ (sha256 74fadf8fb7a1)
- checks: {"courses": 10, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Marine Affairs BS ⟵ “Biology Transfer, Marine Affairs BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `0d868092e9efc58e` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-environmental-and-natural-resource-economics-green-markets-and- [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/green-markets-sustainability-bs-uri/ (sha256 4b533cc04506)
- checks: {"courses": 7, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Environmental and Natural Resource Economics, Green Markets and Sustainability BS ⟵ “Biology Transfer, Environmental and Natural Resource Economics, Green Markets and Sustainability BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `17d8fe0d5b532b2c` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-biological-sciences-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biological-sciences-bs-uri/ (sha256 fca4c3399416)
- checks: {"courses": 10, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Biological Sciences BS ⟵ “Biology Transfer, Biological Sciences BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `1881b95b9c696442` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-nutrition-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/nutrition-bs-uri/ (sha256 8e3825b82880)
- checks: {"courses": 11, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Nutrition BS ⟵ “Biology Transfer, Nutrition BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `246fb82c729fbc43` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-biology-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biology-bs-ric/ (sha256 ddc4de17d78e)
- checks: {"courses": 12, "groups": 5, "groups_skipped": 0}
  - program_name: Biology Transfer, Biology BS ⟵ “Biology Transfer, Biology BS - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `3ce1c48fcd014ce5` Community College of Rhode Island — academic_programs 2026-27 · program_key=chemistry-transfer-chemistry-ba [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/chemistry/transfer/chemistry-ba-ric/ (sha256 2949e38ee62c)
- checks: {"courses": 10, "groups": 5, "groups_skipped": 0}
  - program_name: Chemistry Transfer, Chemistry BA ⟵ “Chemistry Transfer, Chemistry BA - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `5073b248167eb362` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-environmental-science-and-management-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/environmental-management-bs-uri/ (sha256 55d52b6fbd6b)
- checks: {"courses": 13, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Environmental Science and Management BS ⟵ “Biology Transfer, Environmental Science and Management BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `5415ed8b8a2a85a1` Community College of Rhode Island — academic_programs 2026-27 · program_key=business-transfer-healthcare-administration-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/healthcare-administration-bs-ric/ (sha256 c1825bc4dca0)
- checks: {"courses": 12, "groups": 5, "groups_skipped": 0}
  - program_name: Business Transfer, Healthcare Administration BS ⟵ “Business Transfer, Healthcare Administration BS - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `58933ec4794d4573` Community College of Rhode Island — academic_programs 2026-27 · program_key=business-transfer-business-administration-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/business-bs-uri/ (sha256 8243c584dd06)
- checks: {"courses": 13, "groups": 2, "groups_skipped": 0}
  - program_name: Business Transfer, Business Administration BS ⟵ “Business Transfer, Business Administration BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `5cf9b98639154d90` Community College of Rhode Island — academic_programs 2026-27 · program_key=business-transfer-computer-information-systems-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/computer-info-systems-bs-ric/ (sha256 91a16ec027ec)
- checks: {"courses": 12, "groups": 5, "groups_skipped": 0}
  - program_name: Business Transfer, Computer Information Systems BS ⟵ “Business Transfer, Computer Information Systems BS - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `606c2a6b3f98f255` Community College of Rhode Island — academic_programs 2026-27 · program_key=communication-and-media-transfer-film-ba [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/communication-film/transfer/film-ba-ric/ (sha256 e19cee71070e)
- checks: {"courses": 13, "groups": 4, "groups_skipped": 0}
  - program_name: Communication and Media Transfer, Film BA ⟵ “Communication and Media Transfer, Film BA - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `6515a477b40dd020` Community College of Rhode Island — academic_programs 2026-27 · program_key=performing-arts-transfer-theatre-acting-bfa [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/performing-arts/transfer/theatre-acting-bfa-uri/ (sha256 0a1d1cce541c)
- checks: {"courses": 8, "groups": 2, "groups_skipped": 0}
  - program_name: Performing Arts Transfer, Theatre: Acting BFA ⟵ “Performing Arts Transfer, Theatre: Acting BFA - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `6e5c1d105bee314b` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-environmental-and-natural-resource-economics-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/natural-resource-econ-bs-uri/ (sha256 1152f915a353)
- checks: {"courses": 12, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Environmental and Natural Resource Economics BS ⟵ “Biology Transfer, Environmental and Natural Resource Economics BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `7b88398f8fd6bfd8` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-plant-sciences-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/plant-sciences-bs-uri/ (sha256 03a8e0d23743)
- checks: {"courses": 10, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Plant Sciences BS ⟵ “Biology Transfer, Plant Sciences BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `83a52eca30d21345` Community College of Rhode Island — academic_programs 2026-27 · program_key=business-transfer-marketing-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/marketing-bs-ric/ (sha256 c65863c42c46)
- checks: {"courses": 11, "groups": 5, "groups_skipped": 0}
  - program_name: Business Transfer, Marketing BS ⟵ “Business Transfer, Marketing BS - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `88b9c90d71d0c940` Community College of Rhode Island — academic_programs 2026-27 · program_key=chemistry-transfer-chemistry-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/chemistry/transfer/chemistry-bs-uri/ (sha256 04cd8e9c3993)
- checks: {"courses": 10, "groups": 2, "groups_skipped": 0}
  - program_name: Chemistry Transfer, Chemistry BS ⟵ “Chemistry Transfer, Chemistry BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `8f17371f64378f46` Community College of Rhode Island — academic_programs 2026-27 · program_key=communication-and-media-transfer-communication-studies-ba [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/communication-film/transfer/communication-studies-ba-uri/ (sha256 b7deae2fc987)
- checks: {"courses": 18, "groups": 2, "groups_skipped": 0}
  - program_name: Communication and Media Transfer, Communication Studies BA ⟵ “Communication and Media Transfer, Communication Studies BA - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `8f774b50da78b076` Community College of Rhode Island — academic_programs 2026-27 · program_key=business-transfer-finance-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/finance-bs-ric/ (sha256 9f62715990c2)
- checks: {"courses": 11, "groups": 5, "groups_skipped": 0}
  - program_name: Business Transfer, Finance BS ⟵ “Business Transfer, Finance BS - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `8f8e8393473f8855` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-marine-biology-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/marine-biology-bs-uri/ (sha256 91c7f851715a)
- checks: {"courses": 13, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Marine Biology BS ⟵ “Biology Transfer, Marine Biology BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `93198b574e83ef50` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-biology-ba [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biology-ba-uri/ (sha256 1755df1c854b)
- checks: {"courses": 7, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Biology BA ⟵ “Biology Transfer, Biology BA - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `93f941595fa6ea7c` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-marine-affairs-ba [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/marine-affairs-ba-uri/ (sha256 9c36d448eff3)
- checks: {"courses": 8, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Marine Affairs BA ⟵ “Biology Transfer, Marine Affairs BA - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `96a6a0dbe2ddf0b1` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-animal-science-and-technology-pre-vet-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/animal-science-pre-vet-bs-uri/ (sha256 336cf72f3d56)
- checks: {"courses": 11, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Animal Science and Technology Pre-Vet BS ⟵ “Biology Transfer, Animal Science and Technology Pre-Vet BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `98d16e7e295f2bfb` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-aquaculture-and-fisheries-science-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/aquaculture-fisheries-bs-uri/ (sha256 26cd4814a7d5)
- checks: {"courses": 14, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Aquaculture and Fisheries Science BS ⟵ “Biology Transfer, Aquaculture and Fisheries Science BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `b161b02e7e7cf359` Community College of Rhode Island — academic_programs 2026-27 · program_key=business-transfer-accounting-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/accounting-bs-ric/ (sha256 fae0d52330f5)
- checks: {"courses": 13, "groups": 5, "groups_skipped": 0}
  - program_name: Business Transfer, Accounting BS ⟵ “Business Transfer, Accounting BS - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `b9ca4bf255402799` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-wildlife-and-conservation-biology-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/wildlife-conservation-bs-uri/ (sha256 6d916bd43b2a)
- checks: {"courses": 13, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Wildlife and Conservation Biology BS ⟵ “Biology Transfer, Wildlife and Conservation Biology BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `e1f72ff841821af5` Community College of Rhode Island — academic_programs 2026-27 · program_key=business-transfer-textile-marketing-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/textile-marketing-bs-uri/ (sha256 dc81c3c1711b)
- checks: {"courses": 17, "groups": 2, "groups_skipped": 0}
  - program_name: Business Transfer, Textile Marketing BS ⟵ “Business Transfer, Textile Marketing BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `e3d15068d412d3b0` Community College of Rhode Island — academic_programs 2026-27 · program_key=business-transfer-human-resource-management-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/human-resource-management-bs-ric/ (sha256 c8b4d404817f)
- checks: {"courses": 13, "groups": 5, "groups_skipped": 0}
  - program_name: Business Transfer, Human Resource Management BS ⟵ “Business Transfer, Human Resource Management BS - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `f65f4566b0f6a5a9` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-cell-and-molecular-biology-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/cell-molecular-biology-bs-uri/ (sha256 96b53d119c60)
- checks: {"courses": 11, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Cell and Molecular Biology BS ⟵ “Biology Transfer, Cell and Molecular Biology BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `d5b1d6748618894c` Community College of Rhode Island — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ccri.edu/onestop/admissions/early-college/accelerate.html (sha256 0810364b98ae)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.7 ⟵ “To be eligible for the Accelerate program, a student must have a 2.7 GPA and demonstrated”
### `04310e3b258bc3c7` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-business-administration-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/business-bs-uri/ (sha256 8243c584dd06)
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics”
  - courses: ECON 2040 ⟵ “ECON 2040 - Principles of Macroeconomics”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I”
### `044100ed401aff41` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-marketing-bs · requirement_key=requirements-theatre-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/marketing-bs-ric/ (sha256 c65863c42c46)
  - section: requirements-theatre-elective-humn ⟵ “Requirements — Theatre Elective HUMN”
### `0727df14cd569464` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biology-bs · requirement_key=requirements-philosophy-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biology-bs-ric/ (sha256 ddc4de17d78e)
  - section: requirements-philosophy-elective ⟵ “Requirements — Philosophy Elective”
### `0a7323c777bb14a4` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-environmental-and-natural-resource-economics-green-markets-and- · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/green-markets-sustainability-bs-uri/ (sha256 4b533cc04506)
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics MSCI; Scientific Reasoning; Quantitative Literacy”
### `0b35b2ebc2bac638` Community College of Rhode Island — degree_requirements 2026-27 · program_key=chemistry-transfer-chemistry-ba · requirement_key=requirements-theatre-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/chemistry/transfer/chemistry-ba-ric/ (sha256 2949e38ee62c)
  - section: requirements-theatre-elective ⟵ “Requirements — Theatre Elective”
### `0ccd26c125ba5ea8` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-accounting-bs · requirement_key=requirements-philosophy-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/accounting-bs-ric/ (sha256 fae0d52330f5)
  - section: requirements-philosophy-elective-humn ⟵ “Requirements — Philosophy Elective HUMN”
### `0f35c55f583eb707` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-marketing-bs · requirement_key=requirements-world-languages-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/marketing-bs-ric/ (sha256 c65863c42c46)
  - section: requirements-world-languages-elective-humn ⟵ “Requirements — World Languages Elective HUMN”
### `11258d94336b80c3` Community College of Rhode Island — degree_requirements 2026-27 · program_key=chemistry-transfer-chemistry-ba · requirement_key=requirements-philosophy-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/chemistry/transfer/chemistry-ba-ric/ (sha256 2949e38ee62c)
  - section: requirements-philosophy-elective ⟵ “Requirements — Philosophy Elective”
### `1193e7fd3ca48698` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biotechnology-bs · requirement_key=requirements-philosophy-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-ric/ (sha256 4e43a8549318)
  - section: requirements-philosophy-elective ⟵ “Requirements — Philosophy Elective”
### `149db190df07c02d` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-accounting-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/accounting-bs-ric/ (sha256 fae0d52330f5)
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: ACCT 1020 ⟵ “ACCT 1020 - Managerial Accounting”
  - courses: BUSN 1015 ⟵ “BUSN 1015 - Business Computing Applications”
  - courses: BUSN 2050 ⟵ “BUSN 2050 - Principles of Management^”
  - courses: BUSN 2060 ⟵ “BUSN 2060 - Principles of Marketing”
  - courses: ENGL 1410 ⟵ “ENGL 1410 - Business Writing”
  - courses: MATH 2077 ⟵ “MATH 2077 - Quantitative Business Analysis I MSCI; Scientific Reasoning; Quantitative Literacy”
### `14e39a343d657c13` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-finance-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/finance-bs-ric/ (sha256 9f62715990c2)
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: BUSN 1015 ⟵ “BUSN 1015 - Business Computing Applications”
  - courses: BUSN 2050 ⟵ “BUSN 2050 - Principles of Management^”
  - courses: BUSN 2060 ⟵ “BUSN 2060 - Principles of Marketing”
  - courses: ECON 2040 ⟵ “ECON 2040 - Principles of Macroeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ENGL 1410 ⟵ “ENGL 1410 - Business Writing”
### `16535b2940f14646` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-healthcare-administration-bs · requirement_key=requirements-theatre-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/healthcare-administration-bs-ric/ (sha256 c1825bc4dca0)
  - section: requirements-theatre-elective-humn ⟵ “Requirements — Theatre Elective HUMN”
### `1c135478ebc9f972` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-nutrition-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/nutrition-bs-uri/ (sha256 8e3825b82880)
  - courses: BIOL 2202 ⟵ “BIOL 2202 - Human Anatomy & Physiology II”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: MATH 1200 ⟵ “MATH 1200 - College Algebra (or MATH 1200C)”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
### `1cb5d4ca606ced8d` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-computer-information-systems-bs · requirement_key=requirements-theatre-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/computer-info-systems-bs-ric/ (sha256 91a16ec027ec)
  - section: requirements-theatre-elective ⟵ “Requirements — Theatre Elective”
### `1cedbd57206811e8` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-cell-and-molecular-biology-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/cell-molecular-biology-bs-uri/ (sha256 96b53d119c60)
  - courses: BIOL 2480 ⟵ “BIOL 2480 - General Microbiology”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: CHEM 2270 ⟵ “CHEM 2270 - Organic Chemistry I”
  - courses: CHEM 2280 ⟵ “CHEM 2280 - Organic Chemistry II”
  - courses: MATH 2131 ⟵ “MATH 2131 - Applied Calculus”
### `2cb54a280867b4fa` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-wildlife-and-conservation-biology-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/wildlife-conservation-bs-uri/ (sha256 6d916bd43b2a)
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I”
### `2f3c493a70d5a5e2` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-kinesiology-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/kinesiology-bs-uri/ (sha256 614447811fe6)
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I”
  - courses: PSYC 2010 ⟵ “PSYC 2010 - General Psychology”
  - courses: PSYC 2030 ⟵ “PSYC 2030 - Developmental Psychology”
### `36e03b9fa673ff12` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biology-bs · requirement_key=requirements-world-languages-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biology-bs-ric/ (sha256 ddc4de17d78e)
  - section: requirements-world-languages-elective ⟵ “Requirements — World Languages Elective”
### `3b0797b92ebb2877` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-plant-sciences-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/plant-sciences-bs-uri/ (sha256 03a8e0d23743)
  - courses: BIOL 2410 ⟵ “BIOL 2410 - Biology of Insects”
  - courses: BIOL 2420 ⟵ “BIOL 2420 - Introduction to Soil Science”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: COMM 2020 ⟵ “COMM 2020 - The Art of Public Speaking: Romancing the Room”
### `427520d3d0c8455b` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-animal-science-and-technology-pre-vet-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/animal-science-pre-vet-bs-uri/ (sha256 336cf72f3d56)
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
### `44075f6b7337d5fb` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biology-ba · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biology-ba-uri/ (sha256 1755df1c854b)
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
### `4433574800175574` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-marine-affairs-ba · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/marine-affairs-ba-uri/ (sha256 9c36d448eff3)
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: OCEN 1040 ⟵ “OCEN 1040 - Introduction to Oceanography (Formerly OCEN 1010 and 1030)”
### `47730c5a4c903199` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-marketing-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/marketing-bs-ric/ (sha256 c65863c42c46)
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: ACCT 1020 ⟵ “ACCT 1020 - Managerial Accounting”
  - courses: BUSN 1015 ⟵ “BUSN 1015 - Business Computing Applications”
  - courses: BUSN 2050 ⟵ “BUSN 2050 - Principles of Management^”
  - courses: BUSN 2060 ⟵ “BUSN 2060 - Principles of Marketing”
  - courses: MATH 1241 ⟵ “MATH 1241 - Statistical Analysis II”
### `51c993e18a7ff3da` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-management-bs · requirement_key=requirements-theatre-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/management-bs-ric/ (sha256 cbb8e25da914)
  - section: requirements-theatre-elective-humn ⟵ “Requirements — Theatre Elective HUMN”
### `549022ea8d77d0ff` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-sustainable-agriculture-and-food-systems-ba · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/sustainable-agriculture-ba-uri/ (sha256 1474287cf798)
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: BIOL 1005 ⟵ “BIOL 1005 - Biology in the Modern World”
  - courses: BIOL 1050 ⟵ “BIOL 1050 - Humans and the Environment”
  - courses: BIOL 1310 ⟵ “BIOL 1310 - Introduction to Biotechnology Laboratory Skills”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
### `55b21c40f3faa0b4` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-human-resource-management-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/human-resource-management-bs-ric/ (sha256 c8b4d404817f)
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: ACCT 1020 ⟵ “ACCT 1020 - Managerial Accounting”
  - courses: BUSN 1015 ⟵ “BUSN 1015 - Business Computing Applications”
  - courses: BUSN 2050 ⟵ “BUSN 2050 - Principles of Management^”
  - courses: BUSN 2060 ⟵ “BUSN 2060 - Principles of Marketing”
  - courses: BUSN 2350 ⟵ “BUSN 2350 - Human Resources Management”
  - courses: ENGL 1410 ⟵ “ENGL 1410 - Business Writing”
  - courses: MATH 1241 ⟵ “MATH 1241 - Statistical Analysis II”
### `5ed04bfd897bda22` Community College of Rhode Island — degree_requirements 2026-27 · program_key=chemistry-transfer-chemistry-ba · requirement_key=requirements-world-languages-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/chemistry/transfer/chemistry-ba-ric/ (sha256 2949e38ee62c)
  - courses: MATH 2111 ⟵ “MATH 2111 - ”
  - courses: MATH 2141 ⟵ “MATH 2141 - ”
### `5fd3afc6ba5db0f7` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biotechnology-bs · requirement_key=requirements-theatre-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-ric/ (sha256 4e43a8549318)
  - section: requirements-theatre-elective ⟵ “Requirements — Theatre Elective”
### `652474ab22b9f254` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-computer-information-systems-bs · requirement_key=requirements-world-languages-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/computer-info-systems-bs-ric/ (sha256 91a16ec027ec)
  - section: requirements-world-languages-elective ⟵ “Requirements — World Languages Elective”
### `7082ec68b4e25454` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biology-ba · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biology-ba-uri/ (sha256 1755df1c854b)
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
### `7097e22d52bdcf6e` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biology-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biology-bs-ric/ (sha256 ddc4de17d78e)
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: CHEM 2270 ⟵ “CHEM 2270 - Organic Chemistry I”
  - courses: CHEM 2280 ⟵ “CHEM 2280 - Organic Chemistry II”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
  - courses: PHYS 1030 ⟵ “PHYS 1030 - General Physics I”
  - courses: PHYS 1040 ⟵ “PHYS 1040 - General Physics II”
### `714fcbe57ca58c4a` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-kinesiology-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/kinesiology-bs-uri/ (sha256 614447811fe6)
  - courses: BIOL 1200 ⟵ “BIOL 1200 - The Human in Health & Disease”
  - courses: BIOL 2201 ⟵ “BIOL 2201 - Human Anatomy & Physiology I”
  - courses: BIOL 2202 ⟵ “BIOL 2202 - Human Anatomy & Physiology II”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: MATH 1200 ⟵ “MATH 1200 - College Algebra (or MATH 1200C)”
  - courses: PHED 1610 ⟵ “PHED 1610 - Essentials of Physical Fitness”
### `717c74e54fa1a406` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biology-bs · requirement_key=requirements-theatre-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biology-bs-ric/ (sha256 ddc4de17d78e)
  - section: requirements-theatre-elective ⟵ “Requirements — Theatre Elective”
### `7798fdd928b9ee53` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-animal-science-and-technology-pre-vet-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/animal-science-pre-vet-bs-uri/ (sha256 336cf72f3d56)
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: BIOL 2480 ⟵ “BIOL 2480 - General Microbiology”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: MATH 2131 ⟵ “MATH 2131 - Applied Calculus”
  - courses: PHYS 1030 ⟵ “PHYS 1030 - General Physics I”
  - courses: PHYS 1040 ⟵ “PHYS 1040 - General Physics II”
### `794f1281712e9628` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-healthcare-administration-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/healthcare-administration-bs-ric/ (sha256 c1825bc4dca0)
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: BUSN 1015 ⟵ “BUSN 1015 - Business Computing Applications”
  - courses: BUSN 2050 ⟵ “BUSN 2050 - Principles of Management^”
  - courses: BUSN 2060 ⟵ “BUSN 2060 - Principles of Marketing”
  - courses: BUSN 2350 ⟵ “BUSN 2350 - Human Resources Management”
  - courses: ENGL 1410 ⟵ “ENGL 1410 - Business Writing”
### `7ae3acb675f1cf91` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biotechnology-bs · requirement_key=requirements-world-languages-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-ric/ (sha256 4e43a8549318)
  - section: requirements-world-languages-elective ⟵ “Requirements — World Languages Elective”
### `7b568d3578f077f9` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-aquaculture-and-fisheries-science-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/aquaculture-fisheries-bs-uri/ (sha256 26cd4814a7d5)
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: BIOL 1005 ⟵ “BIOL 1005 - Biology in the Modern World”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
### `7beec8f4624c1db6` Community College of Rhode Island — degree_requirements 2026-27 · program_key=performing-arts-transfer-theatre-acting-bfa · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/performing-arts/transfer/theatre-acting-bfa-uri/ (sha256 0a1d1cce541c)
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: THEA 1130 ⟵ “THEA 1130 - Origins of Theatre”
### `7cef14d5fabf937d` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-human-resource-management-bs · requirement_key=requirements-philosophy-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/human-resource-management-bs-ric/ (sha256 c8b4d404817f)
  - section: requirements-philosophy-elective-humn ⟵ “Requirements — Philosophy Elective HUMN”
### `7d6e326924327703` Community College of Rhode Island — degree_requirements 2026-27 · program_key=communication-and-media-transfer-communication-studies-ba · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/communication-film/transfer/communication-studies-ba-uri/ (sha256 b7deae2fc987)
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: ENGL 1200 ⟵ “ENGL 1200 - Introduction to Literature”
  - courses: FILM 1010 ⟵ “FILM 1010 - Principles of Film and Media”
  - courses: JOUR 1050 ⟵ “JOUR 1050 - Introduction to Mass Media”
  - courses: MATH 1139 ⟵ “MATH 1139 - Mathematics for Liberal Arts Students (or MATH 1139C)”
### `7f9bf39417b761a3` Community College of Rhode Island — degree_requirements 2026-27 · program_key=chemistry-transfer-chemistry-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/chemistry/transfer/chemistry-bs-uri/ (sha256 04cd8e9c3993)
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
  - courses: MATH 2141 ⟵ “MATH 2141 - Calculus I”
  - courses: PSYC 2010 ⟵ “PSYC 2010 - General Psychology”
### `8579223a46d62740` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-finance-bs · requirement_key=requirements-world-languages-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/finance-bs-ric/ (sha256 9f62715990c2)
  - section: requirements-world-languages-elective-humn ⟵ “Requirements — World Languages Elective HUMN”
### `85ca857e3a0f8568` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-computer-information-systems-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/computer-info-systems-bs-ric/ (sha256 91a16ec027ec)
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: BUSN 2050 ⟵ “BUSN 2050 - Principles of Management^ (Work-Based Learning Course)”
  - courses: BUSN 2060 ⟵ “BUSN 2060 - Principles of Marketing”
  - courses: COMI 1150 ⟵ “COMI 1150 - Programming Concepts”
  - courses: ENGL 1410 ⟵ “ENGL 1410 - Business Writing”
  - courses: MATH 2077 ⟵ “MATH 2077 - Quantitative Business Analysis I”
  - courses: MATH 2138 ⟵ “MATH 2138 - Quantitative Business Analysis II”
### `880b4e2a8e3a2dea` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-accounting-bs · requirement_key=requirements-theatre-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/accounting-bs-ric/ (sha256 fae0d52330f5)
  - section: requirements-theatre-elective-humn ⟵ “Requirements — Theatre Elective HUMN”
### `89b23f5757ba1874` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-healthcare-administration-bs · requirement_key=requirements-world-languages-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/healthcare-administration-bs-ric/ (sha256 c1825bc4dca0)
  - section: requirements-world-languages-elective-humn ⟵ “Requirements — World Languages Elective HUMN”
### `8e678ee319214ad3` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-management-bs · requirement_key=requirements-philosophy-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/management-bs-ric/ (sha256 cbb8e25da914)
  - section: requirements-philosophy-elective-humn ⟵ “Requirements — Philosophy Elective HUMN”
### `96c298eb338ffb6a` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-environmental-science-and-management-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/environmental-management-bs-uri/ (sha256 55d52b6fbd6b)
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal MSCI; Critical Thinking; Social and Professional Responsibilities”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular MSCI; Non-Written Communication; Scientific Reasoning”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN, WBL requirement”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication; Information Literacy”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I MSCI; Scientific Reasoning; Quantitative Literacy”
### `a1df082dd7387f57` Community College of Rhode Island — degree_requirements 2026-27 · program_key=communication-and-media-transfer-film-ba · requirement_key=requirements-world-languages-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/communication-film/transfer/film-ba-ric/ (sha256 e19cee71070e)
  - section: requirements-world-languages-elective-humn ⟵ “Requirements — World Languages Elective HUMN”
### `a615e1a091ec94ca` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-business-administration-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/business-bs-uri/ (sha256 8243c584dd06)
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: ACCT 1020 ⟵ “ACCT 1020 - Managerial Accounting”
  - courses: BUSN 1010 ⟵ “BUSN 1010 - Introduction to Business”
  - courses: BUSN 2050 ⟵ “BUSN 2050 - Principles of Management^ (Work-based learning course)”
  - courses: BUSN 2060 ⟵ “BUSN 2060 - Principles of Marketing”
  - courses: ENGL 1410 ⟵ “ENGL 1410 - Business Writing”
  - courses: MATH 2077 ⟵ “MATH 2077 - Quantitative Business Analysis I”
  - courses: MATH 2138 ⟵ “MATH 2138 - Quantitative Business Analysis II”
### `a6b3a7efc9917f86` Community College of Rhode Island — degree_requirements 2026-27 · program_key=communication-and-media-transfer-film-ba · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/communication-film/transfer/film-ba-ric/ (sha256 e19cee71070e)
  - courses: COMM 1005 ⟵ “COMM 1005 - Careers and Academic Success for Communication and Media”
  - courses: COMM 1400 ⟵ “COMM 1400 - Social Media Communication”
  - courses: FILM 1010 ⟵ “FILM 1010 - Principles of Film and Media HUMN; Critical Thinking; Diverse Perspectives”
  - courses: FILM 1020 ⟵ “FILM 1020 - Film and Media Production”
  - courses: FILM 1205 ⟵ “FILM 1205 - History of Film II: 1950s to Present HUMN; Critical Thinking; Diverse Perspectives”
  - courses: FILM 2110 ⟵ “FILM 2110 - Crafting the Short Film”
  - courses: FILM 2210 ⟵ “FILM 2210 - Film Theory HUMN; Information Literacy; Social and Professional Responsibilities”
  - courses: FILM 2370 ⟵ “FILM 2370 - Digital Content Creation”
### `aa3a92423ad17d76` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-human-resource-management-bs · requirement_key=requirements-world-languages-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/human-resource-management-bs-ric/ (sha256 c8b4d404817f)
  - section: requirements-world-languages-elective-humn ⟵ “Requirements — World Languages Elective HUMN”
### `b448067815f54f0d` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-marketing-bs · requirement_key=requirements-philosophy-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/marketing-bs-ric/ (sha256 c65863c42c46)
  - section: requirements-philosophy-elective-humn ⟵ “Requirements — Philosophy Elective HUMN”
### `c1f162372d8d02cb` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-computer-information-systems-bs · requirement_key=requirements-philosophy-elective [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/computer-info-systems-bs-ric/ (sha256 91a16ec027ec)
  - section: requirements-philosophy-elective ⟵ “Requirements — Philosophy Elective”
### `c802406e86a20a42` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-accounting-bs · requirement_key=requirements-world-languages-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/accounting-bs-ric/ (sha256 fae0d52330f5)
  - section: requirements-world-languages-elective-humn ⟵ “Requirements — World Languages Elective HUMN”
### `c8b4bafaba3ce070` Community College of Rhode Island — degree_requirements 2026-27 · program_key=performing-arts-transfer-theatre-acting-bfa · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/performing-arts/transfer/theatre-acting-bfa-uri/ (sha256 0a1d1cce541c)
  - courses: THEA 1080 ⟵ “THEA 1080 - Introduction to Costuming”
  - courses: THEA 1120 ⟵ “THEA 1120 - Stagecraft^ (Work-based learning course)”
  - courses: THEA 1125 ⟵ “THEA 1125 - Play Analysis for Production”
  - courses: THEA 1140 ⟵ “THEA 1140 - Acting I”
  - courses: THEA 2140 ⟵ “THEA 2140 - Acting II”
### `c8bb527d7dd56eef` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-marine-affairs-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/marine-affairs-bs-uri/ (sha256 74fadf8fb7a1)
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I”
### `cf0bec97cbf94872` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-healthcare-administration-bs · requirement_key=requirements-philosophy-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/healthcare-administration-bs-ric/ (sha256 c1825bc4dca0)
  - section: requirements-philosophy-elective-humn ⟵ “Requirements — Philosophy Elective HUMN”
### `d1a009164d680e93` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-management-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/management-bs-ric/ (sha256 cbb8e25da914)
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: ACCT 1020 ⟵ “ACCT 1020 - Managerial Accounting”
  - courses: BUSN 1015 ⟵ “BUSN 1015 - Business Computing Applications”
  - courses: BUSN 2050 ⟵ “BUSN 2050 - Principles of Management^”
  - courses: BUSN 2060 ⟵ “BUSN 2060 - Principles of Marketing”
  - courses: BUSN 2350 ⟵ “BUSN 2350 - Human Resources Management”
  - courses: MATH 1241 ⟵ “MATH 1241 - Statistical Analysis II”
### `d9b3e7e7037cc990` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-cell-and-molecular-biology-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/cell-molecular-biology-bs-uri/ (sha256 96b53d119c60)
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
### `dce892229d104a60` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-nutrition-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/nutrition-bs-uri/ (sha256 8e3825b82880)
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: BIOL 2201 ⟵ “BIOL 2201 - Human Anatomy & Physiology I”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 1175 ⟵ “MATH 1175 - Statistics for the Health and Social Sciences (or MATH 1175C)”
  - courses: PSYC 2010 ⟵ “PSYC 2010 - General Psychology”
### `deadeb163dabdc03` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-environmental-and-natural-resource-economics-green-markets-and- · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/green-markets-sustainability-bs-uri/ (sha256 4b533cc04506)
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibilities”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication, Information Literacy”
  - courses: GEOL 1010 ⟵ “GEOL 1010 - Introduction to Geology - How the Earth Works MSCI; Critical Thinking; Scientific Reasoning”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I MSCI; Scientific Reasoning; Quantitative Literacy”
### `e06ebc5c96fa029d` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-management-bs · requirement_key=requirements-world-languages-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/management-bs-ric/ (sha256 cbb8e25da914)
  - section: requirements-world-languages-elective-humn ⟵ “Requirements — World Languages Elective HUMN”
### `e7e31b8b8a9a8e63` Community College of Rhode Island — degree_requirements 2026-27 · program_key=chemistry-transfer-chemistry-ba · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/chemistry/transfer/chemistry-ba-ric/ (sha256 2949e38ee62c)
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: CHEM 2270 ⟵ “CHEM 2270 - Organic Chemistry I”
  - courses: CHEM 2280 ⟵ “CHEM 2280 - Organic Chemistry II”
  - courses: PHYS 1030 ⟵ “PHYS 1030 - General Physics I”
  - courses: PHYS 1040 ⟵ “PHYS 1040 - General Physics II”
### `eb70388fadc7648a` Community College of Rhode Island — degree_requirements 2026-27 · program_key=communication-and-media-transfer-film-ba · requirement_key=requirements-philosophy-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/communication-film/transfer/film-ba-ric/ (sha256 e19cee71070e)
  - section: requirements-philosophy-elective-humn ⟵ “Requirements — Philosophy Elective HUMN”
### `f602e57c52e12f08` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-finance-bs · requirement_key=requirements-theatre-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/finance-bs-ric/ (sha256 9f62715990c2)
  - section: requirements-theatre-elective-humn ⟵ “Requirements — Theatre Elective HUMN”
### `f8cb26cbb0b76b5d` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-finance-bs · requirement_key=requirements-philosophy-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/finance-bs-ric/ (sha256 9f62715990c2)
  - section: requirements-philosophy-elective-humn ⟵ “Requirements — Philosophy Elective HUMN”
### `ff42d2c84f886f23` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-human-resource-management-bs · requirement_key=requirements-theatre-elective-humn [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/human-resource-management-bs-ric/ (sha256 c8b4d404817f)
  - section: requirements-theatre-elective-humn ⟵ “Requirements — Theatre Elective HUMN”
### `8a2be2dc84556e76` Community College of Rhode Island — transfer_policies 2026-27 [new] (labeled_in_title)
- source: https://catalog.ccri.edu/about-community-college/transfer-information/ (sha256 a263a2fc0d84)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Grades of C- or better in courses required by the CCRI program of study are required for transfer.”
### `e310f8e497ce6e56` Johnson & Wales University-Providence — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.jwu.edu/admissions-aid/cost-aid/undergraduate-tuition-fees/ (sha256 aebdbe86f5ba)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 45408 ⟵ “Tuition | $45,408”
  - column:Typical first-year housing (See housing rates): 11500 ⟵ “Typical first-year housing (See housing rates) | $11,500”
  - column:Gold meal plan (See meal plan rates): 7360 ⟵ “Gold meal plan (See meal plan rates) | $7,360”
  - column:New student fee (first year only): 476 ⟵ “New student fee (first year only) | $476”
  - column:Student activity fee: 250 ⟵ “Student activity fee | $250”
  - column:Total direct costs* for tuition, fees and living expenses: 64994 ⟵ “Total direct costs* for tuition, fees and living expenses | $64,994”
### `0ea88802730dc63a` New England Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.neit.edu/admissions-aid/financial-aid-scholarships (sha256 89c7027d8ab6)
- checks: {"thresholds": null}
  - test_requirement: Email Jason ⟵ “Jason Martin | Financial Aid Officer | G-N | Email Jason”
### `bbcca49ad44c4f76` New England Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.neit.edu/admissions-aid/financial-aid-scholarships (sha256 89c7027d8ab6)
- checks: {"thresholds": null}
  - test_requirement: Email Dawn ⟵ “Dawn Tanzi | Financial Aid Officer | A-F | Email Dawn”
### `fe858be2dde726c0` New England Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.neit.edu/admissions-aid/financial-aid-scholarships (sha256 89c7027d8ab6)
- checks: {"thresholds": null}
  - test_requirement: Email Kassy ⟵ “Kassy Anico | Financial Aid Officer | O-Z | Email Kassy”
### `mfa8cc2bb0ebea0d` New England Institute of Technology — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.neit.edu/highschool/dual-enrollment (sha256 9c01a4fc9e59)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 1}
  - eligibility_tier: 2.7 ⟵ “Students must have a minimum high school GPA of 2.7 to be eligible.”
  - eligibility_tier: 2.7 ⟵ “Students must have a minimum high school GPA of 2.7 to be eligible.”
  - eligibility_tier: 2.7 ⟵ “Students must have a minimum high school GPA of 2.7 to be eligible.”
### `b88427bb1cbb17bf` Rhode Island College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ric.edu/admissions-financial-aid/full-time-undergraduate-cost-attendance (sha256 88f60ad9af85)
- checks: {"columns": 3, "rows": 2}
  - with_parents_or_family:Tuition & Fees: 29261.0 ⟵ “Tuition & Fees | $29,261.00 | $29,261.00 | $29,261.00”
  - with_parents_or_family:Housing & Meals: 5158.0 ⟵ “Housing & Meals | $5,158.00 | $15,108.00 | $12,216.00”
  - on_campus:Tuition & Fees: 29261.0 ⟵ “Tuition & Fees | $29,261.00 | $29,261.00 | $29,261.00”
  - on_campus:Housing & Meals: 15108.0 ⟵ “Housing & Meals | $5,158.00 | $15,108.00 | $12,216.00”
  - off_campus_not_with_family:Tuition & Fees: 29261.0 ⟵ “Tuition & Fees | $29,261.00 | $29,261.00 | $29,261.00”
  - off_campus_not_with_family:Housing & Meals: 12216.0 ⟵ “Housing & Meals | $5,158.00 | $15,108.00 | $12,216.00”
### `ce22972364693241` Rhode Island College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ric.edu/admissions-financial-aid/full-time-undergraduate-cost-attendance (sha256 88f60ad9af85)
- checks: {"columns": 3, "rows": 2}
  - with_parents_or_family:Tuition & Fees: 12123.0 ⟵ “Tuition & Fees | $12,123.00 | $12,123.00 | $12,123.00”
  - with_parents_or_family:Housing & Meals: 5158.0 ⟵ “Housing & Meals | $5,158.00 | $15,108.00 | $12,216.00”
  - on_campus:Tuition & Fees: 12123.0 ⟵ “Tuition & Fees | $12,123.00 | $12,123.00 | $12,123.00”
  - on_campus:Housing & Meals: 15108.0 ⟵ “Housing & Meals | $5,158.00 | $15,108.00 | $12,216.00”
  - off_campus_not_with_family:Tuition & Fees: 12123.0 ⟵ “Tuition & Fees | $12,123.00 | $12,123.00 | $12,123.00”
  - off_campus_not_with_family:Housing & Meals: 12216.0 ⟵ “Housing & Meals | $5,158.00 | $15,108.00 | $12,216.00”
### `7d5e6debc9a54cd5` Rhode Island College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ric.edu/admissions-financial-aid/undergraduate-admission/transfer-student-admission (sha256 ce0facd02dda)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Next Transfer Credits arrow_drop_down_circle Transfer Credits Transfer Credits You may transfer up to 90 credits from a regionally accredited college or university for courses in which you have earned a grade of C or higher, as long as the courses are comparable to what is taught at RIC.”
### `d138e62865353602` Rhode Island School of Design — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://sfs.risd.edu/student-accounts/billing-payment (sha256 8b51b2da9ed0)
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 66460 ⟵ “Tuition | $66,460 | $33,230”
  - column:Student activity fee: 308 ⟵ “Student activity fee | $308 | $154”
  - column:Academic and technology fee: 908 ⟵ “Academic and technology fee | $908 | $454”
### `bd514fa788fa6d0e` Rhode Island School of Design — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.risd.edu/admissions/transfer/apply (sha256 bdacefbc3d6a)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “In order for us to accept transfer credits from other institutions, you must receive a grade of C or higher.”
### `6efbabb6a62b492e` Salve Regina University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://salve.edu/admissions/transfer-and-non-traditional-applicants (sha256 7790e914f5a1)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Only courses submitted on an official transcript with a grade of C or higher, from a regionally accredited institution, are eligible for transfer.”
### `a915deefbfe79a2f` University of Rhode Island — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://web.uri.edu/ir/wp-content/uploads/sites/276/CDS-PDF-2025-2026_fillablePDF.pdf (sha256 21bd459ce8a5)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 28021 ⟵ “Total first-time, first-year (degree-seeking) who applied           4368     23100            553                 0   28021”
  - admits: 20892 ⟵ “Total first-time, first-year (degree-seeking) who were admitted     3179     17302            411                 0   20892”
  - enrolled: 3431 ⟵ “Total first-time, first-year (degree-seeking) enrolled              1284        2113           34                 0   3431”
  - sat_composite_25..75: [1090, 1210, 1310] ⟵ “SAT Composite                     1090                      1210                       1310”
  - sat_math_25..75: [520, 590, 645] ⟵ “SAT Math                           520                       590                       645”
  - act_25..75: [25, 28, 31] ⟵ “ACT Composite                      25                        28                         31”
### `2d6bddab501553ea` University of Rhode Island — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://web.uri.edu/admission/transfer/transfer-resources/ (sha256 7bddff6b42a0)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “You will need to earn a grade of “C” or better in order for a class to be considered for transfer.”

## Exceptions (74)

### `424f9fde0e28291d` Brown University — appeals 2023-24 [new] (labeled_in_source)
- source: https://finaid.med.brown.edu/cost-budgeting (sha256 248e61b929d2)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Generally, budget adjustments are covered with the Unsubsidized Direct Loan or Graduate Plus Loan.”
  - sentence: budget_increase ⟵ “Residency application and related expenses where fourth-year students may request a budget increase to cover application fees, interview travel and hotel accommodations.”
### `62205400d3a59e4a` Brown University — appeals 2026-27 [new] (source_unlabeled)
- source: https://finaid.brown.edu/apply/appeal-aid-awards (sha256 3c6ef0d38c85)
- issues: semantic_review_required, conflicting_sources:https://finaid.brown.edu/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Changes in Financial Circumstances Back to Top If your family experiences a significant or unexpected change after receiving your initial financial aid offer for the academic year, or if you believe there are special circumstances that were not considered in the initial review of your financial aid application, please notify us in writing.”
  - sentence: need_based_special_circumstances ⟵ “Use the Appeal Form to help you explain and document special circumstances such as a significant and unexpected change in income due to job loss, salary reduction, change in benefits and/or other financial changes as indicated on page one of the appeal form .”
### `e97281d26b63ba7e` Brown University — appeals 2026-27 [new] (source_unlabeled)
- source: https://finaid.brown.edu/ (sha256 713306aa7259)
- issues: semantic_review_required, conflicting_sources:https://finaid.brown.edu/apply/appeal-aid-awards
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Current Students Learn about applying for aid, campus employment and other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “More Ways to Estimate Cost & Aid Plan ahead with information about the cost of attendance and special circumstances.”
### `3e38a2c71d660ca6` Brown University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://admission.brown.edu/tuition-aid/tuition-fees (sha256 b73893254963)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 71700 ⟵ “Tuition | $35,850 | $35,850 | $71,700”
  - column:Fees: 2950 ⟵ “Fees | $1,475 | $1,475 | $2,950”
  - column:Housing: 10410 ⟵ “Housing | $5,205 | $5,205 | $10,410”
  - column:Food: 8104 ⟵ “Food | $4,052 | $4,052 | $8,104”
  - column:Books& Materials: 1300 ⟵ “Books& Materials | $650 | $650 | $1,300”
  - column:Personal: 2820 ⟵ “Personal | $1,410 | $1,410 | $2,820”
  - column:Total Cost: 97284 ⟵ “Total Cost | $48,642 | $48,642 | $97,284”
### `5ef84503979134b0` Bryant University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bryant.edu/undergraduate/undergraduate-admission/tuition-and-financial-aid/tuition (sha256 fc7bf1f4b799)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 54404 ⟵ “Tuition & Fees | $54,404 | $54,404 | $56,238 | $56,238”
  - on_campus:Housing & Food: 18260 ⟵ “Housing & Food | $18,260 | $5,600 | $19,004 | $6,000”
  - on_campus:Books & Supplies: 1400 ⟵ “Books & Supplies | $1,400 | $1,400 | $1,200 | $1,200”
  - on_campus:Transportation: 450 ⟵ “Transportation | $450 | $2,400 | $450 | $2,400”
  - on_campus:Miscellaneous: 1100 ⟵ “Miscellaneous | $1,100 | $1,100 | $1,100 | $1,100”
  - on_campus:Total Cost of Attendance:: 75614 ⟵ “Total Cost of Attendance: | $75,614 | $64,904 | $77,992 | $66,938”
  - with_parents_or_family:Tuition & Fees: 54404 ⟵ “Tuition & Fees | $54,404 | $54,404 | $56,238 | $56,238”
  - with_parents_or_family:Housing & Food: 5600 ⟵ “Housing & Food | $18,260 | $5,600 | $19,004 | $6,000”
  - with_parents_or_family:Books & Supplies: 1400 ⟵ “Books & Supplies | $1,400 | $1,400 | $1,200 | $1,200”
  - with_parents_or_family:Transportation: 2400 ⟵ “Transportation | $450 | $2,400 | $450 | $2,400”
  - with_parents_or_family:Miscellaneous: 1100 ⟵ “Miscellaneous | $1,100 | $1,100 | $1,100 | $1,100”
  - with_parents_or_family:Total Cost of Attendance:: 64904 ⟵ “Total Cost of Attendance: | $75,614 | $64,904 | $77,992 | $66,938”
### `78c512ffaa8d7108` Bryant University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.bryant.edu/undergraduate/undergraduate-admission/tuition-and-financial-aid/tuition (sha256 fc7bf1f4b799)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "rows": 17}
  - column:Tuition: 54934.0 ⟵ “Tuition | $27,467.00 | $54,934.00”
  - column:Apartment Suites - Single: 16636.0 ⟵ “Apartment Suites - Single | $8,318.00 | $16,636.00”
  - column:Residence Halls 1-17 - Single: 15120.0 ⟵ “Residence Halls 1-17 - Single | $7,560.00 | $15,120.00”
  - column:Residence Halls 1-17 - Double: 11570.0 ⟵ “Residence Halls 1-17 - Double | $5,785.00 | $11,570.00”
  - column:Townhouse - Single: 15120.0 ⟵ “Townhouse - Single | $7,560.00 | $15,120.00”
  - column:Townhouse - Double: 14076.0 ⟵ “Townhouse - Double | $7,038.00 | $14,076.00”
  - column:Unlimited Meal Plan: 7800.0 ⟵ “Unlimited Meal Plan | $3,900.00 | $7,800.00”
  - column:210 Block Meal Plan: 7434.0 ⟵ “210 Block Meal Plan | $3,717.00 | $7,434.00”
  - column:150 Block Meal Plan: 7300.0 ⟵ “150 Block Meal Plan | $3,650.00 | $7,300.00”
  - column:105 Block Meal Plan: 6584.0 ⟵ “105 Block Meal Plan | $3,292.00 | $6,584.00”
  - column:75 Townhouse/Commuter Meal Plan: 2310.0 ⟵ “75 Townhouse/Commuter Meal Plan | $1,155.00 | $2,310.00”
  - column:30 Block Meal Plan: 1050.0 ⟵ “30 Block Meal Plan | $535.00 | $1,050.00”
  - column:Student Involvement Fee: 600.0 ⟵ “Student Involvement Fee | $300.00 | $600.00”
  - column:Experiential Learning Fee: 200.0 ⟵ “Experiential Learning Fee | $100.00 | $200.00”
  - column:Technology Fee: 504.0 ⟵ “Technology Fee | $252.00 | $504.00”
  - column:Studio Art Fee (for creative art classes): 60.0 ⟵ “Studio Art Fee (for creative art classes) |  | $60.00”
  - column:Study Abroad Fee (for participants only): 515.0 ⟵ “Study Abroad Fee (for participants only) |  | $515.00”
### `07bda4dc53e2e775` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-biotechnology-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-uri/ (sha256 9c0a64f1f174)
- issues: conflicting_sources:https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-ric/
- checks: {"courses": 15, "groups": 2, "groups_skipped": 0}
  - program_name: Biology Transfer, Biotechnology BS ⟵ “Biology Transfer, Biotechnology BS - Associate in Arts (URI) | 2026-2027 CCRI Academic Catalog”
### `dedebda3e1a67a26` Community College of Rhode Island — academic_programs 2026-27 · program_key=biology-transfer-biotechnology-bs [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-ric/ (sha256 4e43a8549318)
- issues: conflicting_sources:https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-uri/
- checks: {"courses": 13, "groups": 5, "groups_skipped": 0}
  - program_name: Biology Transfer, Biotechnology BS ⟵ “Biology Transfer, Biotechnology BS - Associate in Arts (RIC) | 2026-2027 CCRI Academic Catalog”
### `21821fa95d605df3` Community College of Rhode Island — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.ccri.edu/onestop/fa/receiving-aid/maintaining-aid/academic_progress.html (sha256 b4474c0b3b1f)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Fall 2026 SAP Appeal Form Requirements: The following chart details the measures that are used to determine whether a student is maintaining SAP: | Attempted Credits | Cumulative Financial Aid GPA Required | Completion Rate (PACE) Required | 0-9 | No Evaluation | | 10-15 | 1.25 | 60%* | 16-30 | 1.50 | 60%* | 31-45 | 1.75 | 67% | 46-90 | 2.00 | 67% (*Students in a certificate program of less than 3”
  - sentence: sap_appeal ⟵ “Fall 2026 SAP Appeal Form Have a Question?”
### `1cef0fc9da919ae1` Community College of Rhode Island — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.ccri.edu/about-community-college/tuition-fees/ (sha256 1fc5469f0544)
- issues: cost_period_semester, residency_unknown
- checks: {"columns": 1, "rows": 6}
  - column:General Tuition Fee: 4186 ⟵ “General Tuition Fee | $2,792 | $4186 | $7900”
  - column:Registration Fee: 75 ⟵ “Registration Fee | $75 | $75 | $75”
  - column:Student Activity Fee: 47 ⟵ “Student Activity Fee | $47 | $47 | $47”
  - column:Learning Resource Fee: 40 ⟵ “Learning Resource Fee | $40 | $40 | $40”
  - column:Technology Fee: 60 ⟵ “Technology Fee | $60 | $60 | $60”
  - column:Campus Service Fee: 15 ⟵ “Campus Service Fee | $15 | $15 | $15”
### `bce25b1517966e25` Community College of Rhode Island — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://catalog.ccri.edu/about-community-college/tuition-fees/ (sha256 1fc5469f0544)
- issues: cost_period_semester
- checks: {"columns": 1, "rows": 6}
  - column:General Tuition Fee: 7900 ⟵ “General Tuition Fee | $2,792 | $4186 | $7900”
  - column:Registration Fee: 75 ⟵ “Registration Fee | $75 | $75 | $75”
  - column:Student Activity Fee: 47 ⟵ “Student Activity Fee | $47 | $47 | $47”
  - column:Learning Resource Fee: 40 ⟵ “Learning Resource Fee | $40 | $40 | $40”
  - column:Technology Fee: 60 ⟵ “Technology Fee | $60 | $60 | $60”
  - column:Campus Service Fee: 15 ⟵ “Campus Service Fee | $15 | $15 | $15”
### `c225ce954e9c49db` Community College of Rhode Island — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://catalog.ccri.edu/about-community-college/tuition-fees/ (sha256 1fc5469f0544)
- issues: cost_period_semester
- checks: {"columns": 1, "rows": 6}
  - column:General Tuition Fee: 2792 ⟵ “General Tuition Fee | $2,792 | $4186 | $7900”
  - column:Registration Fee: 75 ⟵ “Registration Fee | $75 | $75 | $75”
  - column:Student Activity Fee: 47 ⟵ “Student Activity Fee | $47 | $47 | $47”
  - column:Learning Resource Fee: 40 ⟵ “Learning Resource Fee | $40 | $40 | $40”
  - column:Technology Fee: 60 ⟵ “Technology Fee | $60 | $60 | $60”
  - column:Campus Service Fee: 15 ⟵ “Campus Service Fee | $15 | $15 | $15”
### `1cc7b70ace6b4a3f` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-accounting-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/accounting-bs-ric/ (sha256 fae0d52330f5)
- issues: mixed_required_and_choice
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibilities”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ECON 2040 ⟵ “ECON 2040 - Principles of Macroeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication; Information Literacy”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: MATH 2138 ⟵ “MATH 2138 - Quantitative Business Analysis II MSCI; Scientific Reasoning; Quantitative Literacy”
### `2a3014cad8998409` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-environmental-and-natural-resource-economics-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/natural-resource-econ-bs-uri/ (sha256 1152f915a353)
- issues: mixed_required_and_choice
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular MSCI; Non-Written Communication; Scientific Reasoning”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibilities”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication, Information Literacy”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics MSCI; Scientific Reasoning; Quantitative Literacy”
### `3a50560414b37407` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-computer-information-systems-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/computer-info-systems-bs-ric/ (sha256 91a16ec027ec)
- issues: mixed_required_and_choice
  - courses: BUSN 1010 ⟵ “BUSN 1010 - Introduction to Business”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-Based Learning Course)”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I”
### `3cc9e81730ee789b` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-marine-biology-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/marine-biology-bs-uri/ (sha256 91c7f851715a)
- issues: mixed_required_and_choice
  - courses: BIOL 2480 ⟵ “BIOL 2480 - General Microbiology”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: MATH 2131 ⟵ “MATH 2131 - Applied Calculus”
  - courses: MATH 2141 ⟵ “MATH 2141 - Calculus I”
  - courses: PHYS 1030 ⟵ “PHYS 1030 - General Physics I”
  - courses: PHYS 1040 ⟵ “PHYS 1040 - General Physics II”
### `402cb0dfa51613d2` Community College of Rhode Island — degree_requirements 2026-27 · program_key=chemistry-transfer-chemistry-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/chemistry/transfer/chemistry-bs-uri/ (sha256 04cd8e9c3993)
- issues: course_alternatives_in_rule_text
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: CHEM 2270 ⟵ “CHEM 2270 - Organic Chemistry I”
  - courses: CHEM 2280 ⟵ “CHEM 2280 - Organic Chemistry II”
  - courses: MATH 2142 ⟵ “MATH 2142 - Calculus II”
### `43d9afc16575290a` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biological-sciences-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biological-sciences-bs-uri/ (sha256 fca4c3399416)
- issues: mixed_required_and_choice
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
### `47b92d62d87c341b` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-textile-marketing-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/textile-marketing-bs-uri/ (sha256 dc81c3c1711b)
- issues: mixed_required_and_choice
  - courses: BIOL 1005 ⟵ “BIOL 1005 - Biology in the Modern World”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics”
  - courses: ECON 2040 ⟵ “ECON 2040 - Principles of Macroeconomics”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I”
  - courses: PSYC 2010 ⟵ “PSYC 2010 - General Psychology”
  - courses: SOCS 1010 ⟵ “SOCS 1010 - General Sociology”
### `4965cc0830c09ea8` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-finance-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/finance-bs-ric/ (sha256 9f62715990c2)
- issues: mixed_required_and_choice
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibilities”
  - courses: ECON 1000 ⟵ “ECON 1000 - Introduction to Economics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication; Information Literacy”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I MSCI; Scientific Reasoning; Quantitative Literacy”
### `4b85e25ce7875213` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-environmental-and-natural-resource-economics-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/natural-resource-econ-bs-uri/ (sha256 1152f915a353)
- issues: mixed_required_and_choice
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal MSCI; Critical Thinking; Social and Professional Responsibilities”
  - courses: BIOL 1005 ⟵ “BIOL 1005 - Biology in the Modern World MSCI; Scientific Reasoning; Social and Professional Responsibilities”
  - courses: BIOL 1050 ⟵ “BIOL 1050 - Humans and the Environment MSCI; Written Communication; Critical Thinking”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: GEOL 1010 ⟵ “GEOL 1010 - Introduction to Geology - How the Earth Works MSCI; Critical Thinking; Scientific Reasoning”
  - courses: MATH 2131 ⟵ “MATH 2131 - Applied Calculus MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: MATH 2141 ⟵ “MATH 2141 - Calculus I MSCI; Scientific Reasoning; Quantitative Literacy”
### `503c0b9fac75c95d` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-healthcare-administration-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/healthcare-administration-bs-ric/ (sha256 c1825bc4dca0)
- issues: mixed_required_and_choice
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular MSCI; Non-Written Communication; Scientific Reasoning”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibilities”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication; Information Literacy”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: PSYC 2010 ⟵ “PSYC 2010 - General Psychology SSCI; Critical Thinking; Scientific Reasoning”
### `5a2a8e64e2d1608c` Community College of Rhode Island — degree_requirements 2026-27 · program_key=communication-and-media-transfer-film-ba · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/communication-film/transfer/film-ba-ric/ (sha256 e19cee71070e)
- issues: mixed_required_and_choice, choice_rule_unparsed
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibiities”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication; Information Literacy”
  - courses: FILM 1204 ⟵ “FILM 1204 - History of Film I: Early Cinema to 1950s HUMN; Critical Thinking; Diverse Perspectives”
  - courses: JOUR 1050 ⟵ “JOUR 1050 - Introduction to Mass Media HUMN; Written Communication; Critical Thinking”
  - courses: MATH 1139 ⟵ “MATH 1139 - Mathematics for Liberal Arts Students (or MATH 1139C) MSCI; Scientific Reasoning; Quantitative Literacy”
### `5b22f4f839c02279` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-plant-sciences-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/plant-sciences-bs-uri/ (sha256 03a8e0d23743)
- issues: mixed_required_and_choice
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal MSCI; Critical Thinking; Social and Professional Responsibilities”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular MSCI; Non-Written Communication; Scientific Reasoning”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibilities”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication, Information Literacy”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics MSCI; Scientific Reasoning; Quantitative Literacy”
### `63c4eb0585681937` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-textile-marketing-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/textile-marketing-bs-uri/ (sha256 dc81c3c1711b)
- issues: mixed_required_and_choice
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: ACCT 1020 ⟵ “ACCT 1020 - Managerial Accounting”
  - courses: BUSN 1015 ⟵ “BUSN 1015 - Business Computing Applications”
  - courses: BUSN 2050 ⟵ “BUSN 2050 - Principles of Management^ (Work-based learning course)”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: MATH 2077 ⟵ “MATH 2077 - Quantitative Business Analysis I”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
  - courses: MATH 2138 ⟵ “MATH 2138 - Quantitative Business Analysis II”
  - courses: MATH 2141 ⟵ “MATH 2141 - Calculus I”
### `6f25664ca563a888` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-environmental-science-and-management-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/environmental-management-bs-uri/ (sha256 55d52b6fbd6b)
- issues: mixed_required_and_choice
  - courses: BIOL 1005 ⟵ “BIOL 1005 - Biology in the Modern World MSCI; Scientific Reasoning; Social and Professional Responsibilities”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: GEOL 1010 ⟵ “GEOL 1010 - Introduction to Geology - How the Earth Works MSCI; Critical Thinking; Scientific Reasoning”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
  - courses: MATH 2131 ⟵ “MATH 2131 - Applied Calculus MSCI; Scientific Reasoning; Quantitative Literacy”
  - courses: MATH 2141 ⟵ “MATH 2141 - Calculus I MSCI; Scientific Reasoning; Quantitative Literacy”
### `761227294852847b` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-management-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/management-bs-ric/ (sha256 cbb8e25da914)
- issues: mixed_required_and_choice
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibilities”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ECON 2040 ⟵ “ECON 2040 - Principles of Macroeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication; Information Literacy”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I MSCI; Scientific Reasoning; Quantitative Literacy”
### `8edd57fcf8788e31` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biotechnology-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-uri/ (sha256 9c0a64f1f174)
- issues: mixed_required_and_choice, conflicting_sources:https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-ric/
  - courses: BIOL 1300 ⟵ “BIOL 1300 - Orientation to Biotechnology”
  - courses: BIOL 1310 ⟵ “BIOL 1310 - Introduction to Biotechnology Laboratory Skills”
  - courses: BIOL 2480 ⟵ “BIOL 2480 - General Microbiology”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: MATH 2131 ⟵ “MATH 2131 - Applied Calculus”
  - courses: MATH 2141 ⟵ “MATH 2141 - Calculus I”
  - courses: PHYS 1030 ⟵ “PHYS 1030 - General Physics I”
### `9b5c0d006e30d8e9` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biotechnology-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-ric/ (sha256 4e43a8549318)
- issues: mixed_required_and_choice, conflicting_sources:https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-uri/
  - courses: BIOL 1000 ⟵ “BIOL 1000 - Cell Biology for Technology”
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-Based Learning Course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or 1010A)”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
### `a24524a317319a38` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biological-sciences-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biological-sciences-bs-uri/ (sha256 fca4c3399416)
- issues: mixed_required_and_choice
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: MATH 2131 ⟵ “MATH 2131 - Applied Calculus”
  - courses: MATH 2141 ⟵ “MATH 2141 - Calculus I”
### `b50f7fed6a89f699` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-human-resource-management-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/human-resource-management-bs-ric/ (sha256 c8b4d404817f)
- issues: mixed_required_and_choice
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibilities”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ECON 2040 ⟵ “ECON 2040 - Principles of Macroeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication; Information Literacy”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I MSCI; Scientific Reasoning; Quantitative Literacy”
### `c20b82ff8a99952d` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-wildlife-and-conservation-biology-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/wildlife-conservation-bs-uri/ (sha256 6d916bd43b2a)
- issues: mixed_required_and_choice
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: BIOL 1005 ⟵ “BIOL 1005 - Biology in the Modern World”
  - courses: BIOL 1050 ⟵ “BIOL 1050 - Humans and the Environment”
  - courses: GEOL 1010 ⟵ “GEOL 1010 - Introduction to Geology - How the Earth Works”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
  - courses: MATH 2131 ⟵ “MATH 2131 - Applied Calculus”
  - courses: MATH 2141 ⟵ “MATH 2141 - Calculus I”
### `c4a6b765ad12a368` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biotechnology-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-ric/ (sha256 4e43a8549318)
- issues: conflicting_sources:https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-uri/
  - courses: BIOL 1300 ⟵ “BIOL 1300 - Orientation to Biotechnology”
  - courses: BIOL 1310 ⟵ “BIOL 1310 - Introduction to Biotechnology Laboratory Skills”
  - courses: BIOL 2480 ⟵ “BIOL 2480 - General Microbiology”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: CHEM 1100 ⟵ “CHEM 1100 - General Chemistry II”
  - courses: CHMT 1121 ⟵ “CHMT 1121 - Chemistry for Biotechnology”
  - courses: COMI 1150 ⟵ “COMI 1150 - Programming Concepts”
  - courses: INST 1010 ⟵ “INST 1010 - Introduction to Instrumentation Technology”
### `cd959a7f5eaa3665` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biology-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biology-bs-ric/ (sha256 ddc4de17d78e)
- issues: mixed_required_and_choice, choice_rule_unparsed
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-Based Learning Course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I”
### `d742d8234c32a345` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-sustainable-agriculture-and-food-systems-ba · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/sustainable-agriculture-ba-uri/ (sha256 1474287cf798)
- issues: mixed_required_and_choice
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: BUSN 1010 ⟵ “BUSN 1010 - Introduction to Business”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
### `d89e0183859517c7` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-marine-affairs-ba · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/marine-affairs-ba-uri/ (sha256 9c36d448eff3)
- issues: mixed_required_and_choice
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
### `d8aeaacb4b9361fe` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-marine-affairs-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/marine-affairs-bs-uri/ (sha256 74fadf8fb7a1)
- issues: mixed_required_and_choice
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: PHYS 1030 ⟵ “PHYS 1030 - General Physics I”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
  - courses: OCEN 1040 ⟵ “OCEN 1040 - Introduction to Oceanography (Formerly OCEN 1010 and 1030)”
### `dd4d17ec605cebe6` Community College of Rhode Island — degree_requirements 2026-27 · program_key=communication-and-media-transfer-communication-studies-ba · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/communication-film/transfer/communication-studies-ba-uri/ (sha256 b7deae2fc987)
- issues: mixed_required_and_choice
  - courses: COMM 1005 ⟵ “COMM 1005 - Careers and Academic Success for Communication and Media”
  - courses: COMM 1075 ⟵ “COMM 1075 - Digital, Civic, and Media Literacy”
  - courses: COMM 1201 ⟵ “COMM 1201 - Radio Production^”
  - courses: COMM 1300 ⟵ “COMM 1300 - Media Production and Presentation”
  - courses: COMM 1600 ⟵ “COMM 1600 - Introduction to Public Relations^”
  - courses: COMM 2020 ⟵ “COMM 2020 - The Art of Public Speaking: Romancing the Room”
  - courses: COMM 2025 ⟵ “COMM 2025 - Interpersonal Communication”
  - courses: COMM 2030 ⟵ “COMM 2030 - Small Group Communication”
  - courses: COMM 1013 ⟵ “COMM 1013 - Celebrity Communication (Taylor's Version)”
  - courses: COMM 1203 ⟵ “COMM 1203 - Sports Media Communication”
  - courses: COMM 1400 ⟵ “COMM 1400 - Social Media Communication”
  - courses: COMM 2010 ⟵ “COMM 2010 - Persuasion”
### `e20c3ad4d139befc` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-biotechnology-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-uri/ (sha256 9c0a64f1f174)
- issues: mixed_required_and_choice, conflicting_sources:https://catalog.ccri.edu/programs-study/biology/transfer/biotechnology-bs-ric/
  - courses: BIOL 1000 ⟵ “BIOL 1000 - Cell Biology for Technology”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
### `e2ddb1bd61eb35ac` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-marine-biology-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/marine-biology-bs-uri/ (sha256 91c7f851715a)
- issues: mixed_required_and_choice
  - courses: BIOL 1001 ⟵ “BIOL 1001 - Introductory Biology: Organismal”
  - courses: BIOL 1002 ⟵ “BIOL 1002 - Introductory Biology: Cellular”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-based learning course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
  - courses: MATH 2103 ⟵ “MATH 2103 - Applied Precalculus”
  - courses: MATH 2111 ⟵ “MATH 2111 - Pre-Calculus Mathematics”
### `f0e1e539f1739aad` Community College of Rhode Island — degree_requirements 2026-27 · program_key=biology-transfer-aquaculture-and-fisheries-science-bs · requirement_key=requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/biology/transfer/aquaculture-fisheries-bs-uri/ (sha256 26cd4814a7d5)
- issues: mixed_required_and_choice
  - courses: ACCT 1010 ⟵ “ACCT 1010 - Financial Accounting”
  - courses: BIOL 2130 ⟵ “BIOL 2130 - Food from the Sea”
  - courses: BUSN 1010 ⟵ “BUSN 1010 - Introduction to Business”
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: GEOL 1010 ⟵ “GEOL 1010 - Introduction to Geology - How the Earth Works”
  - courses: GEOL 1020 ⟵ “GEOL 1020 - The Earth Through Time”
  - courses: GEOL 1030 ⟵ “GEOL 1030 - Natural Disasters”
  - courses: GEOL 1050 ⟵ “GEOL 1050 - Urban and Environmental Geology”
### `f63da847c83c90c5` Community College of Rhode Island — degree_requirements 2026-27 · program_key=business-transfer-marketing-bs · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/business-administration/transfer/marketing-bs-ric/ (sha256 c65863c42c46)
- issues: mixed_required_and_choice
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ HUMN; Non-Written Communication; Social and Professional Responsibilities”
  - courses: ECON 2030 ⟵ “ECON 2030 - Principles of Microeconomics SSCI; Critical Thinking; Quantitative Literacy”
  - courses: ECON 2040 ⟵ “ECON 2040 - Principles of Macroeconomics MSCI; Critical Thinking; Quantitative Literacy”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A) HUMN; Written Communication; Information Literacy”
  - courses: MATH 1240 ⟵ “MATH 1240 - Statistical Analysis I MSIC; Scientific Reasoning; Quantitative Literacy”
### `ff509f573ea1c51e` Community College of Rhode Island — degree_requirements 2026-27 · program_key=chemistry-transfer-chemistry-ba · requirement_key=requirements-general-education-requirements [new] (labeled_in_source)
- source: https://catalog.ccri.edu/programs-study/chemistry/transfer/chemistry-ba-ric/ (sha256 2949e38ee62c)
- issues: mixed_required_and_choice
  - courses: CHEM 1030 ⟵ “CHEM 1030 - General Chemistry I”
  - courses: COMM 1010 ⟵ “COMM 1010 - Communication Fundamentals^ (Work-Based Learning Course)”
  - courses: ENGL 1010 ⟵ “ENGL 1010 - Composition I (or ENGL 1010A)”
### `ce76b3c396a6cd46` Johnson & Wales University-Providence — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.jwu.edu/admissions-aid/cost-aid/student-financial-services/offer-letter/ (sha256 97f51781b29f)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If there are any substantial changes to the family/student’s income (e.g., change in income, unemployment, etc.) the student must contact Student Financial Services directly.”
  - sentence: need_based_special_circumstances ⟵ “If there are any substantial changes to the family/student’s income (e.g., change in income, unemployment, etc.) the student must contact Student Financial Services directly.”
### `305e58461ef381e7` New England Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.neit.edu/transfer (sha256 ac20c721df6f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students may petition the Enrollment Management Office for consideration of special circumstances.”
### `12c67a2c86a1f291` New England Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.neit.edu/financial-aid/award-terms-and-conditions (sha256 5d00f790ee95)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $3,500 ⟵ “Freshman | $3,500 | $3,462”
### `17fa2d0282c62f71` New England Institute of Technology — awards 2025-26 [new] (labeled_in_source)
- source: https://www.neit.edu/admissions-aid/financial-aid-scholarships/how-to-apply-for-fafsa (sha256 a9323be47a8e)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - test_requirement: Email Dawn ⟵ “Dawn Tanzi | Financial Aid Officer | A-F | Email Dawn”
### `271d2d7a0a0ef687` New England Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.neit.edu/financial-aid/award-terms-and-conditions (sha256 5d00f790ee95)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $5,500 ⟵ “Junior or Senior | $5,500 | $5,441”
### `8cc5f8ba670d73aa` New England Institute of Technology — awards 2025-26 [new] (labeled_in_source)
- source: https://www.neit.edu/admissions-aid/financial-aid-scholarships/how-to-apply-for-fafsa (sha256 a9323be47a8e)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - test_requirement: Email Kassy ⟵ “Kassy Anico | Financial Aid Officer | O-Z | Email Kassy”
### `8dd7f407ea328cb5` New England Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.neit.edu/financial-aid/award-terms-and-conditions (sha256 5d00f790ee95)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $4,500 ⟵ “Sophomore | $4,500 | $4,452”
### `c8e644e0805ec879` New England Institute of Technology — awards 2025-26 [new] (labeled_in_source)
- source: https://www.neit.edu/admissions-aid/financial-aid-scholarships/how-to-apply-for-fafsa (sha256 a9323be47a8e)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - test_requirement: Email Jason ⟵ “Jason Martin | Financial Aid Officer | G-N | Email Jason”
### `f22aac5a0d45c7f5` New England Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.neit.edu/financial-aid/award-terms-and-conditions (sha256 5d00f790ee95)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $20,500 ⟵ “Graduate | $20,500 | $20,281”
### `508a4c5f40c07675` Providence College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://financial-aid.providence.edu/types-of-assistance/ (sha256 54ed602eb17f)
- issues: arrangement_unlabeled, stacked_header_unparsed
- checks: {"columns": 5, "rows": 5}
  - column:Tuition and Fees*: 68630 ⟵ “Tuition and Fees* | $68,630 | $68,480 | $1,065 per credit | $655 per credit | $690 per credit”
  - column:Misc.: 1590 ⟵ “Misc. | $1,590 | $1,590 | $210 | $210 | $210”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $2,300 | $5,400 | $5,400 | $5,400”
  - column:Books: 450 ⟵ “Books | $450 | $450 | $1,200 | $1,200 | $1,200”
  - column:Living Expenses: 0 ⟵ “Living Expenses | $0 | $4,670 | $9,620 | $9,620 | $9,620”
  - column:Tuition and Fees*: 68480 ⟵ “Tuition and Fees* | $68,630 | $68,480 | $1,065 per credit | $655 per credit | $690 per credit”
  - column:Misc.: 1590 ⟵ “Misc. | $1,590 | $1,590 | $210 | $210 | $210”
  - column:Transportation: 2300 ⟵ “Transportation | $800 | $2,300 | $5,400 | $5,400 | $5,400”
  - column:Books: 450 ⟵ “Books | $450 | $450 | $1,200 | $1,200 | $1,200”
  - column:Living Expenses: 4670 ⟵ “Living Expenses | $0 | $4,670 | $9,620 | $9,620 | $9,620”
  - column:Misc.: 210 ⟵ “Misc. | $1,590 | $1,590 | $210 | $210 | $210”
  - column:Transportation: 5400 ⟵ “Transportation | $800 | $2,300 | $5,400 | $5,400 | $5,400”
  - column:Books: 1200 ⟵ “Books | $450 | $450 | $1,200 | $1,200 | $1,200”
  - column:Living Expenses: 9620 ⟵ “Living Expenses | $0 | $4,670 | $9,620 | $9,620 | $9,620”
  - column:Misc.: 210 ⟵ “Misc. | $1,590 | $1,590 | $210 | $210 | $210”
  - column:Transportation: 5400 ⟵ “Transportation | $800 | $2,300 | $5,400 | $5,400 | $5,400”
  - column:Books: 1200 ⟵ “Books | $450 | $450 | $1,200 | $1,200 | $1,200”
  - column:Living Expenses: 9620 ⟵ “Living Expenses | $0 | $4,670 | $9,620 | $9,620 | $9,620”
  - column:Misc.: 210 ⟵ “Misc. | $1,590 | $1,590 | $210 | $210 | $210”
  - column:Transportation: 5400 ⟵ “Transportation | $800 | $2,300 | $5,400 | $5,400 | $5,400”
  - column:Books: 1200 ⟵ “Books | $450 | $450 | $1,200 | $1,200 | $1,200”
  - column:Living Expenses: 9620 ⟵ “Living Expenses | $0 | $4,670 | $9,620 | $9,620 | $9,620”
### `1cd7c65593096572` Rhode Island College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ric.edu/admissions-financial-aid/scholarship-opportunities/hope-scholarship/ric-hope-scholarship-policy-manual (sha256 8bb31059ec71)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “See Section V of this manual for these “Special Circumstances.” V.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The following may be exceptions to the eligibility requirements for students with special circumstances: Leave of Absence.”
  - sentence: need_based_special_circumstances ⟵ “This Appeals Form should also be submitted by any students who believe they should be eligible for the Hope Scholarship due to Special Circumstances as described in Section V of this policy manual.”
### `cb691960913e3c6e` Rhode Island College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ric.edu/admissions-financial-aid/scholarship-opportunities/hope-scholarship/ric-hope-scholarship-policy-manual (sha256 8bb31059ec71)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: scholarship_retention_appeal ⟵ “Students who have one of these circumstances and are otherwise eligible for the Hope Scholarship, but have not received notification of award, should follow the appeals process outlined in Section VII of this manual and should email hope@ric.edu if they have any questions about the appeals process.”
  - sentence: scholarship_retention_appeal ⟵ “Appeals Processes Any student who believes they have met all of the eligibility criteria under the Hope Scholarship program but has been denied may submit a Hope Scholarship Eligibility Appeals Form.”
  - sentence: scholarship_retention_appeal ⟵ “The Hope Appeals Committee will review appeals and make decisions regarding approval or denial.”
### `1122fa6d853ee9d4` Rhode Island College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ric.edu/admissions-financial-aid/credits-prior-learning-and-experience/gain-college-credit-clep-and-ap-exams (sha256 4d59883afc33)
- issues: score_column_not_scores, score_scale_mismatch
- checks: {"distinct_exams": 17, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|American Literature]:  ⟵ “American Literature | Elective (6)”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|Analyzing & Interpreting Literature]:  ⟵ “Analyzing & Interpreting Literature | Elective (6)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|College Composition]:  ⟵ “College Composition | FYW 100 (4)* plus Elective (2)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|College Composition Modular]:  ⟵ “College Composition Modular | Elective (6)”
  - equivalencies[CLEP-ENGLISH-LITERATURE|English Literature]:  ⟵ “English Literature | Elective (6)”
  - equivalencies[CLEP-HUMANITIES|Humanities]:  ⟵ “Humanities | Elective (6)”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French Language]:  ⟵ “French Language | FREN 101 Elementary French and FREN 102 Elementary French II (8)*”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French Language (score of 60)]:  ⟵ “French Language (score of 60) | FREN 113 Intermediate French I and FREN 114 Intermediate French II (8)*”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German Language]:  ⟵ “German Language | GRMN 101 Elementary French and GRMN 102 Elementary German II (8)*”
  - equivalencies[CLEP-SPANISH-LANGUAGE|Spanish Language]:  ⟵ “Spanish Language | SPAN 101 Elementary French and SPAN 102 Elementary Spanish II (8)*”
  - equivalencies[CLEP-SPANISH-LANGUAGE|Spanish Language (score of 60)]:  ⟵ “Spanish Language (score of 60) | SPAN 113 Intermediate French I and SPAN 114 Intermediate Spanish II (8)*”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|American Government]:  ⟵ “American Government | POL 202 American Government (4)*”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|Human Growth and Development]:  ⟵ “Human Growth and Development | Elective (3)”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|Introduction to Educational Psychology]:  ⟵ “Introduction to Educational Psychology | Elective (3)”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|Introductory Psychology]:  ⟵ “Introductory Psychology | PSYC 110 Introduction to Psychology (4)*”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|Introductory Sociology]:  ⟵ “Introductory Sociology | SOC 200 Society & Social Behavior (4)*”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|Social Sciences and History]:  ⟵ “Social Sciences and History | SB 175 Gen Ed Social and Behavioral Science (4)* plus Elective (2)”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|Western Civilization I: Ancient Near East to 1648Western Civilization II: 1648 to Present Western Civilization]:  ⟵ “Western Civilization I: Ancient Near East to 1648Western Civilization II: 1648 to Present Western Civilization | HIST 175 Gen Ed History (4)* plus Elective (2)”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|Western Civilization I: Ancient Near East to 1648]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | Elective (3)”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|Western Civilization II: 1648 to Present]:  ⟵ “Western Civilization II: 1648 to Present | Elective (3)”
### `45753ca004224946` Rhode Island College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ric.edu/admissions-financial-aid/credits-prior-learning-and-experience/gain-college-credit-clep-and-ap-exams (sha256 4d59883afc33)
- issues: score_column_not_scores
- checks: {"distinct_exams": 34, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|African American Studies]:  ⟵ “African American Studies | AFRI 200 Introduction to Africana Studies (4)*”
  - equivalencies[AP-ART-HISTORY|Art History]:  ⟵ “Art History | Art 231 Prehistoric to Renaissance Art andArt 232 Renaissance to Modern Art (8)*”
  - equivalencies[AP-BIOLOGY|Biology]:  ⟵ “Biology | BIOL 111 Introductory Biology I andBIOL 112 Introductory Biology II (8)*”
  - equivalencies[AP-CALCULUS-AB|Calculus AB]:  ⟵ “Calculus AB | MATH 209 Precalculus Mathematics andMATH 212 Calculus I (8)*”
  - equivalencies[AP-CALCULUS-BC|Calculus BC]:  ⟵ “Calculus BC | MATH 212 Calculus I andMATH 213 Calculus II (8)*”
  - equivalencies[AP-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | CHEM 103 General Chemistry I andCHEM 104 General Chemistry II (8)*”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|Chinese Language & Culture]:  ⟵ “Chinese Language & Culture | MLANG 199 (4)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|Computer Science A]:  ⟵ “Computer Science A | CSCI 211 Computer Programming and Design (4)”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|Computer Science Principles]:  ⟵ “Computer Science Principles | CSCI 157 Introduction to Algorithmic Thinking in Python (4)”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|English Language and Composition]:  ⟵ “English Language and Composition | FYW 100 Introduction to Academic Writing (4)*Elective (2)”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|English Literature and Composition]:  ⟵ “English Literature and Composition | GENLIT 175 Gen Ed Literature (4)*”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|Environmental Science]:  ⟵ “Environmental Science | NS 175 Gen Ed Natural Science (4)*”
  - equivalencies[AP-EUROPEAN-HISTORY|European History]:  ⟵ “European History | HIST 175 Gen Ed History (4)*Elective (2)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|French Language and Culture]:  ⟵ “French Language and Culture | FREN 113 Intermediate French I (4)*”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|German Language and Culture]:  ⟵ “German Language and Culture | GRMN 113 Intermediate German I (4)*”
  - equivalencies[AP-HUMAN-GEOGRAPHY|Human Geography]:  ⟵ “Human Geography | Elective (4)”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|Italian Language and Culture]:  ⟵ “Italian Language and Culture | ITAL 113 Intermediate Italian (4)*”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|Japanese Language and Culture]:  ⟵ “Japanese Language and Culture | JPAN 101 Elementary Japanese I andJPAN 102 Elementary Japanese II (8)*”
  - equivalencies[AP-LATIN|Latin]:  ⟵ “Latin | LATN 101 Elementary Latin I andLATN 102 Elementary Latin II (8)*”
  - equivalencies[AP-MACROECONOMICS|Macroeconomics]:  ⟵ “Macroeconomics | ECON 215 Principles of Macroeconomics (3)”
  - equivalencies[AP-MICROECONOMICS|Microeconomics]:  ⟵ “Microeconomics | ECON 214 Principles of Microeconomics (3)”
  - equivalencies[AP-MUSIC-THEORY|Music Theory]:  ⟵ “Music Theory | MUS 203 Elementary Music Theory (4)*”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|Physics C: Electricity and Magnetism]:  ⟵ “Physics C: Electricity and Magnetism | PHYS 102 Physics for Science and Mathematics II (4)*”
  - equivalencies[AP-PHYSICS-C-MECHANICS|Physics C: Mechanics]:  ⟵ “Physics C: Mechanics | Elective (4)”
  - equivalencies[AP-CALCULUS-AB|Precalculus AB]:  ⟵ “Precalculus AB | MATH 209 Precalculus Mathematics (4)* and MATH 212 Calculus (4)*”
  - … 11 more rows
### `97084d79e7a62915` Rhode Island School of Design — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://sfs.risd.edu/student-accounts/billing-payment (sha256 8b51b2da9ed0)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 63966 ⟵ “Tuition | $63,966 | $31,983”
  - column:Student activity fee: 296 ⟵ “Student activity fee | $296 | $148”
  - column:Academic and technology fee: 874 ⟵ “Academic and technology fee | $874 | $437”
### `2cd0c6fe497fcde8` Roger Williams University — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.rwu.edu/admission/financial-aid/forms-and-resources (sha256 d305ea8866d2)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: professional_judgment ⟵ “Scholarships are renewable for the student's full four years of study at RWU Student must maintain full time enrollment term (minimum of 12 credits) Professional Judgment Policy Click to Open On a case-by-case basis and consistent with federal guidelines, Roger Williams University Financial Aid may consider a student’s special circumstances to either increase or decrease data elements used to calc”
  - sentence: professional_judgment ⟵ “The Financial Aid Office is expected and required to make reasonable decisions that support the intent of the federal guidelines regarding professional judgment.”
  - sentence: professional_judgment ⟵ “Roger Williams University is held accountable for all professional judgment decisions made, and for fully documenting each decision.”
  - sentence: professional_judgment ⟵ “This policy sets forth guidelines regarding how professional judgment in financial aid will be exercised at Roger Williams University.”
  - sentence: professional_judgment ⟵ “Professional Judgment cannot be exercised to: circumvent the law or regulations; waive general student eligibility requirements; change a student’s status from independent to dependent; adjust the EFC directly; alter the need analysis formula or change table values; create a new category in the cost of attendance.”
  - sentence: professional_judgment ⟵ “Exercise of professional judgment is neither limited to nor required for the situations mentioned.”
### `52db37d291292825` Roger Williams University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rwu.edu/admission/financial-aid/applying-aid/appeals (sha256 1af207986c91)
- issues: semantic_review_required, conflicting_sources:https://connect.rwu.edu/register/2627SpecCircReturning
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Common reasons (Special Circumstances) students file a need-based appeal: Loss of income: A parent or family member lost a job, retired, became disabled, or passed away.”
  - sentence: need_based_special_circumstances ⟵ “How to apply for Special Circumstance Appeals Fill out the Special Circumstance Appeals Form.”
  - sentence: need_based_special_circumstances ⟵ “If your appeal is approved, you'll receive a revised aid offer in the mail. 27 Spring Start New Students Only:Complete the Special Circumstance Appeals Form Currently Enrolled RWU Students:Complete the Special Circumstance Appeals Form All decisions are final.”
### `5564f03af6b861a4` Roger Williams University — appeals 2026-27 [new] (labeled_in_title)
- source: https://connect.rwu.edu/register/2627SpecCircReturning (sha256 a738d5e900c7)
- issues: semantic_review_required, conflicting_sources:https://www.rwu.edu/admission/financial-aid/applying-aid/appeals
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstances Form for Returning Students This website uses resources that are being blocked by your network.”
  - sentence: need_based_special_circumstances ⟵ “Skip to main content 2026-2027 Special Circumstances Form for Returning Students Loading... 2026-2027 Special Circumstances Form for Returning Students We appreciate that the Free Application for Student Aid (FAFSA) may not present an accurate picture of your unique financial situation and resources available.”
  - sentence: need_based_special_circumstances ⟵ “This Special Circumstances Consideration form allows you to supplement your FAFSA information or document any financial circumstances that have changed or arisen since your FAFSA was filed.”
  - sentence: need_based_special_circumstances ⟵ “Yes No Special Circumstances for Consideration Please review and indicate below which special circumstance applies to you based on your status as a dependent or independent student.”
  - sentence: need_based_special_circumstances ⟵ “Important notes about submitting an appeal due to special circumstances If you filed your 2026-2027 FAFSA and received an SAI equal to or less than zero (0), you already received the maximum in federal aid.”
### `9a699a842b3095e4` Roger Williams University — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.rwu.edu/admission/financial-aid/forms-and-resources (sha256 d305ea8866d2)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Since the Free Application for Federal Student Aid (FAFSA) does not afford the opportunity to provide details about any special circumstances that could impact a student’s ability to pay costs associated with a program of study.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Special circumstances are ones that differentiate the student’s finances from those of other students.”
  - sentence: need_based_special_circumstances ⟵ “The Special Circumstance form, available from the Office of Admissions and Financial Aid, includes a more information and documentation requirements.”
  - sentence: need_based_special_circumstances ⟵ “We encourage you to complete the Special Circumstance Appeal Form.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance Consideration Completing a Special Circumstance Appeal form allows students/families to address income changes in the current calendar year versus the prior year.”
### `a8e55e3314a326fe` Roger Williams University — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.rwu.edu/admission/financial-aid/forms-and-resources (sha256 d305ea8866d2)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “A student that has failed to make SAP, who has appealed and has been granted an appeal, will be on Financial Aid Probation as stated on their approval letter.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals Any student who believes that mitigating circumstances prevented him or her from achieving the minimum requirement should complete a Satisfactory Academic Progress Appeal Form with Elizabeth Niemeyer, Senior Retention Advisor, located in the library, room 204.”
  - sentence: sap_appeal ⟵ “The form should be addressed to: SAP Appeals Committee Roger Williams University One Old Ferry Road Bristol, RI 02809-2921 Unusual Circumstances Policy Click to Open We recognize that the Free Application for Student Aid (FAFSA) may not always portray a clear picture of your financial situation.”
### `251912b102d23e7c` Roger Williams University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.rwu.edu/tuition-fees-2026-27/undergraduate-day-student-rates-2026-27 (sha256 f01eb5d21e81)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.rwu.edu/admission/financial-aid/undergraduate-cost-attendance
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition: 23964 ⟵ “Tuition | $23,964 | $47,928”
  - column:Activity Fee: 200 ⟵ “Activity Fee | $200 | $400”
  - column:Tuition & Fees: 24164 ⟵ “Tuition & Fees | $24,164 | $48,328”
  - column:Room (Double): 4982 ⟵ “Room (Double) | $4,982 | $9,964”
  - column:Meal Plan: 4284 ⟵ “Meal Plan | $4,284 | $8,568”
  - column:Laundry Fee: 50 ⟵ “Laundry Fee | $50 | $100”
  - column:Room & Meals: 9316 ⟵ “Room & Meals | $9,316 | $18,632”
  - column:Total Charges: 33480 ⟵ “Total Charges | $33,480 | $66,960”
  - column:Tuition: 47928 ⟵ “Tuition | $23,964 | $47,928”
  - column:Activity Fee: 400 ⟵ “Activity Fee | $200 | $400”
  - column:Tuition & Fees: 48328 ⟵ “Tuition & Fees | $24,164 | $48,328”
  - column:Room (Double): 9964 ⟵ “Room (Double) | $4,982 | $9,964”
  - column:Meal Plan: 8568 ⟵ “Meal Plan | $4,284 | $8,568”
  - column:Laundry Fee: 100 ⟵ “Laundry Fee | $50 | $100”
  - column:Room & Meals: 18632 ⟵ “Room & Meals | $9,316 | $18,632”
  - column:Total Charges: 66960 ⟵ “Total Charges | $33,480 | $66,960”
### `fbe46ada8256700f` Roger Williams University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.rwu.edu/admission/financial-aid/undergraduate-cost-attendance (sha256 cf265fbdf6e6)
- issues: conflicting_sources:https://www.rwu.edu/tuition-fees-2026-27/undergraduate-day-student-rates-2026-27
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - on_campus:Comprehensive Tuition: 47928 ⟵ “Comprehensive Tuition | $47,928 | $47,928 | $47,928”
  - on_campus:Student Activity Fee: 400 ⟵ “Student Activity Fee | 400 | 400 | 400”
  - on_campus:Housing (Standard Double): 9964 ⟵ “Housing (Standard Double) | 9,964 | N/A | N/A”
  - on_campus:Food: 8568 ⟵ “Food | 8,568 | N/A | N/A”
  - on_campus:Laundry Fee: 100 ⟵ “Laundry Fee | 100 | N/A | N/A”
  - on_campus:Total Direct Costs:: 66960 ⟵ “Total Direct Costs: | $66,960 | $48,328 | $48,328”
  - with_parents_or_family:Comprehensive Tuition: 47928 ⟵ “Comprehensive Tuition | $47,928 | $47,928 | $47,928”
  - with_parents_or_family:Student Activity Fee: 400 ⟵ “Student Activity Fee | 400 | 400 | 400”
  - with_parents_or_family:Total Direct Costs:: 48328 ⟵ “Total Direct Costs: | $66,960 | $48,328 | $48,328”
  - off_campus_not_with_family:Comprehensive Tuition: 47928 ⟵ “Comprehensive Tuition | $47,928 | $47,928 | $47,928”
  - off_campus_not_with_family:Student Activity Fee: 400 ⟵ “Student Activity Fee | 400 | 400 | 400”
  - off_campus_not_with_family:Total Direct Costs:: 48328 ⟵ “Total Direct Costs: | $66,960 | $48,328 | $48,328”
### `29c61099213181d4` Salve Regina University — appeals 2025-26 [new] (labeled_in_source)
- source: https://salve.edu/admissions/financial-aid/undergraduate-financial-aid-process (sha256 fd183cfa1139)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances If your family's financial situation changes considerably from one year to the next due to extenuating circumstances such as the death of a parent, unemployment, retirement or significant out-of-pocket medical expenses, please contact our office for guidance.”
  - sentence: need_based_special_circumstances ⟵ “All requested documentation must be submitted prior to a review for special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “If your parents are divorced or separated, any additional documentation requested to support a reconsideration due to special circumstances must be submitted by the parent who provided more financial support during the last 12-month period prior to filing the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances To apply for funding as an independent student, you must meet one of the qualifications listed on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “There are times when unusual circumstances (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration) allow a financial administrator to adjust your dependency status on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “In some instances, you may have both special and unusual circumstances.”
### `50648c8f8d582bf8` Salve Regina University — appeals 2026-27 [new] (source_unlabeled)
- source: https://salve.edu/admissions/financial-aid/satisfactory-academic-progress (sha256 aa333502d01e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals Students who do not meet the requirements for satisfactory academic progress may appeal when special circumstances exist.”
### `bbb5f6573f2e8d47` Salve Regina University — appeals 2026-27 [new] (source_unlabeled)
- source: https://salve.edu/admissions/financial-aid/frequently-asked-questions (sha256 e2d976511efb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Families who experience a significant change in income, marital status, loss of job or encounter special circumstances from one year to the next are encouraged to contact their financial aid counselor regarding the specific changes.”
  - sentence: need_based_special_circumstances ⟵ “In some cases there are ways that we can assist families who experience financial setbacks or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “If you move off campus, there will be a change in your financial aid offer.”
### `2d1f87fec3c89455` Salve Regina University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://salve.edu/documents/financial-aid-understanding-your-award (sha256 5ac794c3f17c)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://salve.edu/admissions/financial-aid/cost-attendance,https://salve.edu/our-mission/campus-offices-and-services/bursars-office/tuition-and-fees
- checks: {"columns": 3, "components_reconcile": false, "rows": 9}
  - column:Tuition and fees: 54270 ⟵ “Tuition and fees | $54,270 | $54,270 | $54,270”
  - column:On-campus: 20280 ⟵ “On-campus | $20,280 | comparable coverage by logging on to universityhealthplans.”
  - column:Direct billed: 74550 ⟵ “Direct billed | $74,550 | $54,270 | $54,270 | received by this date.”
  - column:Off-campus: 15340 ⟵ “Off-campus | $15,340 | $9,892 | DEWAR TUITION INSURANCE”
  - column:Books and: 1600 ⟵ “Books and | $1,600 | $1,600 | $1,600”
  - column:Personal: 2300 ⟵ “Personal | $2,300 | $2,300 | $2,300 | independent of the University. The cost is $175 per semester”
  - column:Transportation*: 1500 ⟵ “Transportation* | $1,500 | $1,500 | $1,700 | salve.”
  - column:Loan Fees: 86 ⟵ “Loan Fees | $86 | $86 | $86”
  - column:Total estimated: 80536 ⟵ “Total estimated | $80,536 | $75,596 | $70,348”
  - column:Tuition and fees: 54270 ⟵ “Tuition and fees | $54,270 | $54,270 | $54,270”
  - column:Direct billed: 54270 ⟵ “Direct billed | $74,550 | $54,270 | $54,270 | received by this date.”
  - column:Off-campus: 9892 ⟵ “Off-campus | $15,340 | $9,892 | DEWAR TUITION INSURANCE”
  - column:Books and: 1600 ⟵ “Books and | $1,600 | $1,600 | $1,600”
  - column:Personal: 2300 ⟵ “Personal | $2,300 | $2,300 | $2,300 | independent of the University. The cost is $175 per semester”
  - column:Transportation*: 1500 ⟵ “Transportation* | $1,500 | $1,500 | $1,700 | salve.”
  - column:Loan Fees: 86 ⟵ “Loan Fees | $86 | $86 | $86”
  - column:Total estimated: 75596 ⟵ “Total estimated | $80,536 | $75,596 | $70,348”
  - column:Tuition and fees: 54270 ⟵ “Tuition and fees | $54,270 | $54,270 | $54,270”
  - column:Direct billed: 54270 ⟵ “Direct billed | $74,550 | $54,270 | $54,270 | received by this date.”
  - column:Books and: 1600 ⟵ “Books and | $1,600 | $1,600 | $1,600”
  - column:Personal: 2300 ⟵ “Personal | $2,300 | $2,300 | $2,300 | independent of the University. The cost is $175 per semester”
  - column:Transportation*: 1700 ⟵ “Transportation* | $1,500 | $1,500 | $1,700 | salve.”
  - column:Loan Fees: 86 ⟵ “Loan Fees | $86 | $86 | $86”
  - column:Total estimated: 70348 ⟵ “Total estimated | $80,536 | $75,596 | $70,348”
### `4045c916c69495c6` Salve Regina University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://salve.edu/our-mission/campus-offices-and-services/bursars-office/tuition-and-fees (sha256 3061aaf91226)
- issues: conflicting_sources:https://salve.edu/admissions/financial-aid/cost-attendance,https://salve.edu/documents/financial-aid-understanding-your-award
- checks: {"columns": 1, "rows": 7}
  - column:Tuition, per semester (12-17 credits): 26800 ⟵ “Tuition, per semester (12-17 credits) | $26,800”
  - column:Application to the University: 50 ⟵ “Application to the University | $50”
  - column:New Seahawk Orientation program fee: 335 ⟵ “New Seahawk Orientation program fee | $335”
  - column:Student services fee** (per semester, students enrolled for 6+ credits): 500 ⟵ “Student services fee** (per semester, students enrolled for 6+ credits) | $500”
  - column:Student health insurance (per year): 2050 ⟵ “Student health insurance (per year) | $2,050”
  - column:Student refund insurance (tuition, room and board, per semester): 177 ⟵ “Student refund insurance (tuition, room and board, per semester) | $177”
  - column:Student refund insurance (tuition only, per semester): 133 ⟵ “Student refund insurance (tuition only, per semester) | $133”
### `cefcf97ac9f836f8` Salve Regina University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://salve.edu/admissions/financial-aid/cost-attendance (sha256 b99f92ce95ad)
- issues: conflicting_sources:https://salve.edu/documents/financial-aid-understanding-your-award,https://salve.edu/our-mission/campus-offices-and-services/bursars-office/tuition-and-fees
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 53600 ⟵ “Tuition | $53,600 | $53,600 | $53,600”
  - on_campus:Comprehensive fee: 1000 ⟵ “Comprehensive fee | $1,000 | $1,000 | $1,000”
  - on_campus:Housing and food: 20300 ⟵ “Housing and food | $20,300 |  | ”
  - on_campus:Books and supplies: 2000 ⟵ “Books and supplies | $2,000 | $2,000 | $2,000”
  - on_campus:Personal expenses: 2400 ⟵ “Personal expenses | $2,400 | $2,400 | $2,400”
  - on_campus:Transportation: 1500 ⟵ “Transportation | $1,500 | $1,500 | $1,700”
  - on_campus:Loan fees: 86 ⟵ “Loan fees | $86 | $86 | $86”
  - on_campus:Total estimated cost of attendance: 80886 ⟵ “Total estimated cost of attendance | $80,886 | $76,282 | $70,678”
  - off_campus_not_with_family:Tuition: 53600 ⟵ “Tuition | $53,600 | $53,600 | $53,600”
  - off_campus_not_with_family:Comprehensive fee: 1000 ⟵ “Comprehensive fee | $1,000 | $1,000 | $1,000”
  - off_campus_not_with_family:Off-campus living allowance: 15696 ⟵ “Off-campus living allowance |  | $15,696 | $9,892”
  - off_campus_not_with_family:Books and supplies: 2000 ⟵ “Books and supplies | $2,000 | $2,000 | $2,000”
  - off_campus_not_with_family:Personal expenses: 2400 ⟵ “Personal expenses | $2,400 | $2,400 | $2,400”
  - off_campus_not_with_family:Transportation: 1500 ⟵ “Transportation | $1,500 | $1,500 | $1,700”
  - off_campus_not_with_family:Loan fees: 86 ⟵ “Loan fees | $86 | $86 | $86”
  - off_campus_not_with_family:Total estimated cost of attendance: 76282 ⟵ “Total estimated cost of attendance | $80,886 | $76,282 | $70,678”
  - with_parents_or_family:Tuition: 53600 ⟵ “Tuition | $53,600 | $53,600 | $53,600”
  - with_parents_or_family:Comprehensive fee: 1000 ⟵ “Comprehensive fee | $1,000 | $1,000 | $1,000”
  - with_parents_or_family:Off-campus living allowance: 9892 ⟵ “Off-campus living allowance |  | $15,696 | $9,892”
  - with_parents_or_family:Books and supplies: 2000 ⟵ “Books and supplies | $2,000 | $2,000 | $2,000”
  - with_parents_or_family:Personal expenses: 2400 ⟵ “Personal expenses | $2,400 | $2,400 | $2,400”
  - with_parents_or_family:Transportation: 1700 ⟵ “Transportation | $1,500 | $1,500 | $1,700”
  - with_parents_or_family:Loan fees: 86 ⟵ “Loan fees | $86 | $86 | $86”
  - with_parents_or_family:Total estimated cost of attendance: 70678 ⟵ “Total estimated cost of attendance | $80,886 | $76,282 | $70,678”
### `63190f917d968c98` University of Rhode Island — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://web.uri.edu/ir/wp-content/uploads/sites/276/CDS-2024-2025-fillable.pdf (sha256 1c923b2db732)
- issues: stale_year_label:2024-25
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 26987 ⟵ “Total first-time, first-year (degree-seeking) who applied          4410      22040            537                  26987”
  - admits: 19475 ⟵ “Total first-time, first-year (degree-seeking) who were admitted    3289      15824            362                  19475”
  - enrolled: 2995 ⟵ “Total first-time, first-year (degree-seeking) enrolled             1287         1679           29                  2995”
  - sat_composite_25..75: [1020, 1170, 1260] ⟵ “SAT Composite                     1020                      1170                       1260”
  - sat_math_25..75: [500, 570, 630] ⟵ “SAT Math                           500                       570                       630”
### `9bed3a01428d44ae` University of Rhode Island — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://web.uri.edu/tuition-billing/annual-undergraduate-tuition-and-fees-2024-25/ (sha256 d442485f3072)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": true, "rows": 3}
  - column:Tuition: 14630 ⟵ “Tuition | $14,630 | $34,834 | $25,604”
  - column:Required Fees: 2312 ⟵ “Required Fees | $2,312 | $2,312 | $2,312”
  - column:Total: 16942 ⟵ “Total | $16,942 | $37,146 | $27,916”
  - column:Tuition: 34834 ⟵ “Tuition | $14,630 | $34,834 | $25,604”
  - column:Required Fees: 2312 ⟵ “Required Fees | $2,312 | $2,312 | $2,312”
  - column:Total: 37146 ⟵ “Total | $16,942 | $37,146 | $27,916”
  - column:Tuition: 25604 ⟵ “Tuition | $14,630 | $34,834 | $25,604”
  - column:Required Fees: 2312 ⟵ “Required Fees | $2,312 | $2,312 | $2,312”
  - column:Total: 27916 ⟵ “Total | $16,942 | $37,146 | $27,916”
### `a119c35b178ee71c` University of Rhode Island — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://web.uri.edu/admission/regional-tuition-majors/ (sha256 952d68ef3fe6)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees:: 29844 ⟵ “Tuition and Fees: | $29,844”
  - column:Housing and Food:: 16704 ⟵ “Housing and Food: | $16,704”
  - column:Total:: 46548 ⟵ “Total: | $46,548*”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 1; pages by category: tuition_fees 1

## Blocked by the site (every request refused; needs the browser fallback)

- Johnson & Wales University-Online (`ipeds-460349`)

## Leads: official pages found with no extracted record

- Brown University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Bryant University: admissions_tests, merit_scholarships
- College Unbound: tuition_fees, admissions_tests
- Community College of Rhode Island: cost_of_attendance, admissions_tests, ap_credit, statewide_articulation, residency
- Johnson & Wales University-Providence: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency
- New England Institute of Technology: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit
- Providence College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Rhode Island College: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Rhode Island School of Design: cost_of_attendance, admissions_tests, merit_scholarships, residency
- Roger Williams University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Salve Regina University: admissions_tests, merit_scholarships, statewide_articulation, residency
- University of Rhode Island: cost_of_attendance, merit_scholarships, ap_credit, clep_credit, dual_enrollment, residency, degree_requirements, aid_appeals
