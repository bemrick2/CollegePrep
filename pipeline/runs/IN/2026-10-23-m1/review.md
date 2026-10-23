# Review queue — IN (2026-27)

Pages fetched: 453; failures: 35. Candidates: 300 (243 without issues, 57 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 7 | 0 | 0 | 2 | 2 | 1 | 41 |
| cost_of_attendance | 3 | 0 | 0 | 1 | 4 | 0 | 45 |
| admissions_tests | 0 | 0 | 0 | 0 | 5 | 1 | 47 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 6 | 47 |
| merit_scholarships | 3 | 2 | 0 | 0 | 6 | 0 | 42 |
| ap_credit | 2 | 6 | 0 | 1 | 2 | 3 | 39 |
| clep_credit | 0 | 2 | 1 | 1 | 1 | 3 | 45 |
| ib_credit | 1 | 5 | 0 | 1 | 1 | 4 | 41 |
| dual_enrollment | 0 | 7 | 0 | 0 | 0 | 4 | 42 |
| transfer_credit | 0 | 10 | 0 | 0 | 4 | 1 | 38 |
| statewide_articulation | 0 | 0 | 0 | 0 | 4 | 2 | 47 |
| residency | 0 | 0 | 0 | 0 | 5 | 1 | 47 |
| degree_requirements | 2 | 0 | 0 | 0 | 4 | 1 | 46 |
| aid_appeals | 0 | 0 | 0 | 4 | 1 | 1 | 47 |

## Ready for review (243)

### `7d4ac816e1a26573` Indiana University-Indianapolis — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://indianapolis.iu.edu/cost-aid/cost-of-attendance/ (sha256 303229a54a3d)
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
### `d1d751e1cdc2bff2` Indiana University-Indianapolis — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://indianapolis.iu.edu/cost-aid/cost-of-attendance/ (sha256 303229a54a3d)
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
### `0659ab03a8c566e4` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-communication [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
- checks: {"courses": 32, "groups": 6, "groups_skipped": 0}
  - program_name: Bachelor of Science in Communication ⟵ “Bachelor of Science in Communication | Purdue University Global Academic Catalog”
### `0bf53f8cb77fdb7c` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-organizational-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
- checks: {"courses": 79, "groups": 17, "groups_skipped": 0}
  - program_name: Bachelor of Science in Organizational Management ⟵ “Bachelor of Science in Organizational Management | Purdue University Global Academic Catalog”
### `1192716bfbcbe1d0` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-applied-computer-science [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-computer-science-bs/ (sha256 49600e5d901a)
- checks: {"courses": 25, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Applied Computer Science ⟵ “Bachelor of Science in Applied Computer Science | Purdue University Global Academic Catalog”
### `130c105111fa9122` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/environmental-policy-management-bs/ (sha256 10dc519623e0)
- checks: {"courses": 24, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Environmental Policy and Management ⟵ “Bachelor of Science in Environmental Policy and Management | Purdue University Global Academic Catalog”
### `23f0f1fb4980dfbe` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-care-administration [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-care-administration-bs/ (sha256 f6b640a6f508)
- checks: {"courses": 13, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health Care Administration ⟵ “Bachelor of Science in Health Care Administration | Purdue University Global Academic Catalog”
### `2627f9392ab4950a` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-education-and-promotion [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-education-promotion-bs/ (sha256 5e9167680106)
- checks: {"courses": 11, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health Education and Promotion ⟵ “Bachelor of Science in Health Education and Promotion | Purdue University Global Academic Catalog”
### `27ffa17700c696dc` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-science-in-nursing [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
- checks: {"courses": 37, "groups": 6, "groups_skipped": 0}
  - program_name: Associate of Science in Nursing ⟵ “Associate of Science in Nursing | Purdue University Global Academic Catalog”
### `3045ec0a456f04ab` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-information-technology [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-bs/ (sha256 6d6bdb1e9c45)
- checks: {"courses": 28, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Information Technology ⟵ “Bachelor of Science in Information Technology | Purdue University Global Academic Catalog”
### `30e68aac7bd18023` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-cybersecurity [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
- checks: {"courses": 49, "groups": 9, "groups_skipped": 0}
  - program_name: Bachelor of Science in Cybersecurity ⟵ “Bachelor of Science in Cybersecurity | Purdue University Global Academic Catalog”
### `426e3fbee165f899` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-analytics [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
- checks: {"courses": 73, "groups": 13, "groups_skipped": 0}
  - program_name: Bachelor of Science in Analytics ⟵ “Bachelor of Science in Analytics | Purdue University Global Academic Catalog”
### `458e8b58110accbf` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-criminal-justice [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
- checks: {"courses": 40, "groups": 9, "groups_skipped": 0}
  - program_name: Bachelor of Science in Criminal Justice ⟵ “Bachelor of Science in Criminal Justice | Purdue University Global Academic Catalog”
### `4a68d42b9f81662b` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-information-technology [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-aas/ (sha256 071358cda74e)
- checks: {"courses": 16, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Information Technology ⟵ “Associate of Applied Science in Information Technology | Purdue University Global Academic Catalog”
### `4bcea1d01d116251` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-professional-studies [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
- checks: {"courses": 16, "groups": 6, "groups_skipped": 0}
  - program_name: Bachelor of Science in Professional Studies ⟵ “Bachelor of Science in Professional Studies | Purdue University Global Academic Catalog”
### `4cda5620ae51f3d5` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-applied-manufacturing [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-manufacturing-bs/ (sha256 ed13b75cad34)
- checks: {"courses": 22, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Applied Manufacturing ⟵ “Bachelor of Science in Applied Manufacturing | Purdue University Global Academic Catalog”
### `578a8bd161e32871` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-science-in-health-science [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
- checks: {"courses": 21, "groups": 4, "groups_skipped": 0}
  - program_name: Associate of Science in Health Science ⟵ “Associate of Science in Health Science | Purdue University Global Academic Catalog”
### `5972910569ee43dc` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-early-childhood-development [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-development-aas/ (sha256 fdad375265a0)
- checks: {"courses": 12, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Early Childhood Development ⟵ “Associate of Applied Science in Early Childhood Development | Purdue University Global Academic Catalog”
### `6239c0a615959440` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-small-group-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/small-group-management-aas/ (sha256 0411c2728524)
- checks: {"courses": 6, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Small Group Management ⟵ “Associate of Applied Science in Small Group Management | Purdue University Global Academic Catalog”
### `73cf339f1f9695a8` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-cloud-computing-and-solutions [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cloud-computing-solutions-bs/ (sha256 77b0e54d770a)
- checks: {"courses": 24, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Cloud Computing and Solutions ⟵ “Bachelor of Science in Cloud Computing and Solutions | Purdue University Global Academic Catalog”
### `7a0556089107853e` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-criminal-justice [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-aas/ (sha256 f7068e07e87b)
- checks: {"courses": 7, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Criminal Justice ⟵ “Associate of Applied Science in Criminal Justice | Purdue University Global Academic Catalog”
### `7c99bc4818416129` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-health-science [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
- checks: {"courses": 20, "groups": 4, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Health Science ⟵ “Associate of Applied Science in Health Science | Purdue University Global Academic Catalog”
### `7eb8d2781e2c170a` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-nutrition [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/nutrition-bs/ (sha256 dd1592b09484)
- checks: {"courses": 25, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Nutrition ⟵ “Bachelor of Science in Nutrition | Purdue University Global Academic Catalog”
### `801121f894cde9a3` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-aviation-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/aviation-management-bs/ (sha256 1ca153298e79)
- checks: {"courses": 21, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Aviation Management ⟵ “Bachelor of Science in Aviation Management | Purdue University Global Academic Catalog”
### `83f8e619155dc137` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-information-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-information-management-bs/ (sha256 0d8e9e812759)
- checks: {"courses": 25, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health Information Management ⟵ “Bachelor of Science in Health Information Management | Purdue University Global Academic Catalog”
### `8516c774344fa43e` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
- checks: {"courses": 37, "groups": 8, "groups_skipped": 0}
  - program_name: Bachelor of Science in Accounting and Analytics ⟵ “Bachelor of Science in Accounting and Analytics | Purdue University Global Academic Catalog”
### `8a0c3795163b6db4` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-emergency-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/emergency-management-bs/ (sha256 54adfba134ed)
- checks: {"courses": 25, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Emergency Management ⟵ “Bachelor of Science in Emergency Management | Purdue University Global Academic Catalog”
### `8ba26435b5a5050a` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-science-in-professional-studies [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-as/ (sha256 8d08aa71b244)
- checks: {"courses": 4, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Science in Professional Studies ⟵ “Associate of Science in Professional Studies | Purdue University Global Academic Catalog”
### `9823fbde79025f7b` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-finance [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
- checks: {"courses": 36, "groups": 7, "groups_skipped": 0}
  - program_name: Bachelor of Science in Finance ⟵ “Bachelor of Science in Finance | Purdue University Global Academic Catalog”
### `9defd0d0f8f3674d` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/fire-emergency-management-bs/ (sha256 afedb45fd8c0)
- checks: {"courses": 25, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Fire and Emergency Management ⟵ “Bachelor of Science in Fire and Emergency Management | Purdue University Global Academic Catalog”
### `a5b3f510cca961ce` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-nursing-rn-to-bsn [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-rn-bsn-bs/ (sha256 4d33147a4129)
- checks: {"courses": 13, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Nursing—RN-to-BSN ⟵ “Bachelor of Science in Nursing—RN-to-BSN | Purdue University Global Academic Catalog”
### `b583c9bd93ac7ac7` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-business-administration [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
- checks: {"courses": 90, "groups": 20, "groups_skipped": 0}
  - program_name: Bachelor of Science in Business Administration ⟵ “Bachelor of Science in Business Administration | Purdue University Global Academic Catalog”
### `b6dce59e373c857b` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-human-resource-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/human-resource-management-bs/ (sha256 8c3efdbb3966)
- checks: {"courses": 21, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Human Resource Management ⟵ “Bachelor of Science in Human Resource Management | Purdue University Global Academic Catalog”
### `be51101b5524f629` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-accounting [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-aas/ (sha256 eb162f849b86)
- checks: {"courses": 14, "groups": 3, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Accounting ⟵ “Associate of Applied Science in Accounting | Purdue University Global Academic Catalog”
### `c64bf5937caa299d` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-and-wellness [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-wellness-bs/ (sha256 ae3f65d930b4)
- checks: {"courses": 23, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health and Wellness ⟵ “Bachelor of Science in Health and Wellness | Purdue University Global Academic Catalog”
### `cad10d024ce69993` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-health-science [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
- checks: {"courses": 31, "groups": 5, "groups_skipped": 0}
  - program_name: Bachelor of Science in Health Science ⟵ “Bachelor of Science in Health Science | Purdue University Global Academic Catalog”
### `cb2f44db909c0320` Purdue University Global — academic_programs 2026-27 · program_key=associate-of-applied-science-in-business-administration [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
- checks: {"courses": 56, "groups": 14, "groups_skipped": 0}
  - program_name: Associate of Applied Science in Business Administration ⟵ “Associate of Applied Science in Business Administration | Purdue University Global Academic Catalog”
### `db13fb919ec6c394` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-applied-supply-chain-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-supply-chain-management-bs/ (sha256 803bc6bd7b23)
- checks: {"courses": 25, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Applied Supply Chain Management ⟵ “Bachelor of Science in Applied Supply Chain Management | Purdue University Global Academic Catalog”
### `de886984b644cdef` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-professional-flight [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/professional-flight-bs/ (sha256 a564dfddbaa1)
- checks: {"courses": 19, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor of Science in Professional Flight ⟵ “Bachelor of Science in Professional Flight | Purdue University Global Academic Catalog”
### `ecfdb9d7eec67d0b` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-early-childhood-administration [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-administration-bs/ (sha256 39b3c395f5ac)
- checks: {"courses": 22, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Early Childhood Administration ⟵ “Bachelor of Science in Early Childhood Administration | Purdue University Global Academic Catalog”
### `fc3e94df81293b29` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-marketing [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/marketing-bs/ (sha256 f769649697ce)
- checks: {"courses": 21, "groups": 3, "groups_skipped": 0}
  - program_name: Bachelor of Science in Marketing ⟵ “Bachelor of Science in Marketing | Purdue University Global Academic Catalog”
### `fc485f604a21c85a` Purdue University Global — academic_programs 2026-27 · program_key=bachelor-of-science-in-sustainability [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
- checks: {"courses": 52, "groups": 10, "groups_skipped": 0}
  - program_name: Bachelor of Science in Sustainability ⟵ “Bachelor of Science in Sustainability | Purdue University Global Academic Catalog”
### `007d5be160b437b0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=supply-chain-logistics [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
### `022ac661fd233929` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=wealth-management-and-financial-planning [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 421 ⟵ “MT 421 - Financial Planning”
  - courses: MT 422 ⟵ “MT 422 - Portfolio Management”
  - courses: MT 423 ⟵ “MT 423 - Asset Allocation and Risk Management”
  - courses: MT 483 ⟵ “MT 483 - Investments”
### `02996a71117e21f7` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `036e207d88b6d440` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `0397b6a1af538b2f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `03f9319c031c97c7` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-health-science · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
  - courses: HS 290 ⟵ “HS 290 - Associate's Capstone in Health Science”
### `0490547f1e7d9895` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-information-management · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-information-management-bs/ (sha256 0d8e9e812759)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SC 116 ⟵ “SC 116 - Survey of Human Structure and Function”
### `05fbb4aeb0f3059e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=game-development [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IN 240 ⟵ “IN 240 - 🌐 Game Design and Mechanics”
  - courses: IN 241 ⟵ “IN 241 - 🌐 Game Programming”
  - courses: IN 242 ⟵ “IN 242 - 🌐 Game Art and Animation”
  - courses: IN 251 ⟵ “IN 251 - 🌐 Software Development Concepts Using C#”
  - courses: IN 255 ⟵ “IN 255 - 🌐 Software Design and Development Concepts Using C#”
### `069c1384bf21d288` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=supply-chain-management-and-logistics [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `06de1e807e49a3a5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `084799a7bb7a12a5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=forensic-psychology [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 325 ⟵ “CJ 325 - 🌐 Psychology for Law Enforcement”
  - courses: CJ 440 ⟵ “CJ 440 - Crisis Intervention”
  - courses: PS 440 ⟵ “PS 440 - Psychopathology”
### `0947d60a8c187660` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=network-administration [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 203 ⟵ “IN 203 - 🌐 Networking With Microsoft Technologies”
  - courses: IN 205 ⟵ “IN 205 - 🌐 Routing and Switching I”
  - courses: IN 206 ⟵ “IN 206 - 🌐 Routing and Switching II”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 278 ⟵ “IT 278 - 🌐 Windows Administration”
  - courses: IT 375 ⟵ “IT 375 - 🌐 Windows Enterprise Administration”
### `0bd7620f10383636` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aviation-management · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/aviation-management-bs/ (sha256 1ca153298e79)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `138486b5915d2d4e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-flight · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/professional-flight-bs/ (sha256 a564dfddbaa1)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `14091068d6bd5838` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=decision-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: IN 302 ⟵ “IN 302 - 🌐 Reporting and Visualization”
  - courses: MM 305 ⟵ “MM 305 - 🌐 Business Statistics and Quantitative Analysis”
  - courses: MM 330 ⟵ “MM 330 - Probability With Business Applications”
  - courses: MM 340 ⟵ “MM 340 - Decision Modeling”
  - courses: MM 341 ⟵ “MM 341 - Decision Management”
### `155c189e501c238c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=supply-chain-management-and-logistics [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `1686ea20297b5a3f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-computer-science · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-computer-science-bs/ (sha256 49600e5d901a)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 165 ⟵ “MM 165 - Advanced Algebra and Geometry”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
### `176a875a2612a5aa` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-emergency-management · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/emergency-management-bs/ (sha256 54adfba134ed)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SS 236 ⟵ “SS 236 - 🌐 American Government”
### `193c6546493160bf` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=artificial-intelligence-ai [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IN 200 ⟵ “IN 200 - 🌐 Data Governance - Policy and Ethics”
  - courses: IN 245 ⟵ “IN 245 - Introduction to Artificial Intelligence and Its Impact”
  - courses: IN 246 ⟵ “IN 246 - The Human Side of Artificial Intelligence: Understanding Interaction and Design”
  - courses: IN 305 ⟵ “IN 305 - Artificial Intelligence, Society, and the Future of Work”
  - courses: IT 421 ⟵ “IT 421 - AI-Powered Cybersecurity: Tools and Techniques”
### `1a7f1cec591b66c8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-education-and-promotion · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-education-promotion-bs/ (sha256 5e9167680106)
  - courses: HS 305 ⟵ “HS 305 - Research Methods for Health Sciences”
  - courses: HW 315 ⟵ “HW 315 - Models for Health and Wellness”
  - courses: HW 320 ⟵ “HW 320 - Contemporary Diet and Nutrition”
  - courses: HD 420 ⟵ “HD 420 - Social Determinants of Health and Health Behavior”
  - courses: HD 440 ⟵ “HD 440 - Health Education Program Assessment and Planning”
  - courses: HD 460 ⟵ “HD 460 - Health Education Program Implementation and Evaluation”
  - courses: HD 480 ⟵ “HD 480 - Health Communication, Social Marketing, and Advocacy”
  - courses: HD 499 ⟵ “HD 499 - Bachelor's Capstone in Health Education and Promotion”
### `1a9767941281d4f0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=global-marketing-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 450 ⟵ “MT 450 - 🌐 Brand Management Strategy”
  - courses: MT 455 ⟵ “MT 455 - Strategic Management of Sales”
### `1b0ded1da9f9bfb0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: PR 150 ⟵ “PR 150 - You and Professional Studies - Creating Pathways to Success”
  - courses: PR 499 ⟵ “PR 499 - Bachelor's Capstone in Professional Studies”
### `1bdf2fe2e770647c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=managerial-accountancy [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 314 ⟵ “AC 314 - Accounting Information Systems and Enterprise Risk Management”
  - courses: AC 420 ⟵ “AC 420 - Cost Accounting”
  - courses: MT 482 ⟵ “MT 482 - 🌐 Financial Statement Analysis”
### `1fe3b4d71db66d4c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=game-development [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 240 ⟵ “IN 240 - 🌐 Game Design and Mechanics”
  - courses: IN 241 ⟵ “IN 241 - 🌐 Game Programming”
  - courses: IN 242 ⟵ “IN 242 - 🌐 Game Art and Animation”
  - courses: IN 251 ⟵ “IN 251 - 🌐 Software Development Concepts Using C#”
  - courses: IN 255 ⟵ “IN 255 - 🌐 Software Design and Development Concepts Using C#”
### `20780da0a5cae66d` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-criminal-justice · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-aas/ (sha256 f7068e07e87b)
  - courses: CJ 100 ⟵ “CJ 100 - 🌐 Preparing for a Career in Public Safety”
  - courses: CJ 101 ⟵ “CJ 101 - 🌐 Introduction to the Criminal Justice System”
  - courses: CJ 210 ⟵ “CJ 210 - 🌐 Criminal Investigation”
  - courses: CJ 227 ⟵ “CJ 227 - 🌐 Criminal Procedure”
  - courses: CJ 299 ⟵ “CJ 299 - Associate's Capstone in Criminal Justice”
### `221674d307e75859` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=small-group-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 260 ⟵ “MT 260 - Group and Organization Dynamics”
  - courses: MT 262 ⟵ “MT 262 - Leading Global Teams”
### `235fadc9b3a8cee0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=real-estate [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 361 ⟵ “MT 361 - Foundations of Real Estate Practice”
  - courses: MT 431 ⟵ “MT 431 - Real Estate Finance and Ethics”
  - courses: MT 432 ⟵ “MT 432 - Real Estate Law”
  - courses: MT 453 ⟵ “MT 453 - Professional Selling”
### `249fe50466908cde` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `25432585f21cb396` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-early-childhood-development · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-development-aas/ (sha256 fdad375265a0)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `2552a225812a70cc` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-marketing · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/marketing-bs/ (sha256 f769649697ce)
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `264142165319ccc5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-flight · requirement_key=program-requirements-instrument-rating [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/professional-flight-bs/ (sha256 a564dfddbaa1)
  - courses: AV 498 ⟵ “AV 498 - Aviation Technology Capstone”
### `26945449356fec03` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `297c645c1774fc75` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `2cd0643a25f31dcd` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=cloud-computing [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IT 222 ⟵ “IT 222 - 🌐 Introduction to Cloud Computing”
  - courses: IT 227 ⟵ “IT 227 - 🌐 Cloud Infrastructure Administration”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 303 ⟵ “IT 303 - 🌐 Cloud Architecture Concepts and Design”
  - courses: IT 304 ⟵ “IT 304 - 🌐 Application Development and Scripting in the Cloud”
  - courses: IT 403 ⟵ “IT 403 - 🌐 Cloud Security”
### `2d258ebd411e7b8d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=homeland-security [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 307 ⟵ “CJ 307 - Crisis Management in Terrorist Attacks and Disasters”
  - courses: CJ 355 ⟵ “CJ 355 - 🌐 Homeland Security”
  - courses: CJ 407 ⟵ “CJ 407 - Crisis Negotiation”
  - courses: CJ 440 ⟵ “CJ 440 - Crisis Intervention”
### `2ed20331514e439d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=global-business [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: CM 305 ⟵ “CM 305 - Communicating in a Diverse Society”
  - courses: MT 220 ⟵ “MT 220 - 🌐 Global Business”
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
### `310a7742061adc7f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-care-administration · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `313aca60c48ab712` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=business-intelligence [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 314 ⟵ “AC 314 - Accounting Information Systems and Enterprise Risk Management”
  - courses: AC 442 ⟵ “AC 442 - Data Management and Analysis”
  - courses: AC 444 ⟵ “AC 444 - Accounting Visualization and Business Intelligence”
### `31d63a77724f037b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nursing-rn-to-bsn · requirement_key=program-requirements-prior-learning-licensure-credits [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-rn-bsn-bs/ (sha256 4d33147a4129)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `33202c7290dbb25f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 180 ⟵ “SC 180 - General Chemistry I”
  - courses: SC 235 ⟵ “SC 235 - 🌐 Human Biology”
### `33560c8b53d8c122` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-early-childhood-administration · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-administration-bs/ (sha256 39b3c395f5ac)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: PS 124 ⟵ “PS 124 - 🌐 Introduction to Psychology”
  - courses: PS 220 ⟵ “PS 220 - Child and Adolescent Psychology”
### `3401c28801f42962` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-early-childhood-administration · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-administration-bs/ (sha256 39b3c395f5ac)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `3500ee04a01ab4c1` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-information-technology · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-aas/ (sha256 071358cda74e)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `359d66bae53466c8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=supply-chain-management-and-logistics [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `3690982f38177117` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `38fd27d28414b18b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `397d7b1ff9c855e5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: SS 290 ⟵ “SS 290 - 🌐 Data in Our World - Introduction to Data Literacy”
### `3b5e8e349454e46a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=juvenile-justice [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 150 ⟵ “CJ 150 - 🌐 Juvenile Delinquency”
  - courses: CJ 333 ⟵ “CJ 333 - 🌐 Family and Domestic Violence”
  - courses: CJ 420 ⟵ “CJ 420 - 🌐 Juvenile Justice”
  - courses: CJ 445 ⟵ “CJ 445 - Juvenile Justice Case Management”
  - courses: PS 440 ⟵ “PS 440 - Psychopathology”
### `3bb25d30f7302b93` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `3ce961ca60ae3591` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-supply-chain-management · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-supply-chain-management-bs/ (sha256 803bc6bd7b23)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `3db2fa5753bb5cac` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=business-development [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 359 ⟵ “MT 359 - Integrated Marketing Communications”
  - courses: MT 453 ⟵ “MT 453 - Professional Selling”
  - courses: MT 459 ⟵ “MT 459 - Consumer Behavior”
### `3e09767dcb13c9c0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-and-wellness · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `3ee0d8a93c811a40` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-professional-studies · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-as/ (sha256 8d08aa71b244)
  - courses: PR 150 ⟵ “PR 150 - You and Professional Studies - Creating Pathways to Success”
  - courses: PR 299 ⟵ “PR 299 - Associate's Capstone in Professional Studies”
### `3fc103d906f277de` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=fintech [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: FI 310 ⟵ “FI 310 - FinTech Principles and Concepts”
  - courses: FI 311 ⟵ “FI 311 - FinTech Law and Ethics”
  - courses: FI 410 ⟵ “FI 410 - Blockchain for the Financial Industry”
### `40592cf61adeac17` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-early-childhood-development · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `42c1071e7646251d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-information-technology · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-bs/ (sha256 6d6bdb1e9c45)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
### `4335fcae3027f638` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `46c8430682707dcf` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=data-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IT 163 ⟵ “IT 163 - 🌐 Database Concepts Using Microsoft Access”
  - courses: IT 234 ⟵ “IT 234 - 🌐 Database Concepts”
  - courses: IN 303 ⟵ “IN 303 - 🌐 Data Mining and Data Warehousing”
  - courses: IT 350 ⟵ “IT 350 - 🌐 Advanced Database Concepts”
### `495c96db5cb551e9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=software-development-using-python [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IN 250 ⟵ “IN 250 - 🌐 Software Development Concepts Using Python”
  - courses: IN 254 ⟵ “IN 254 - 🌐 Software Design and Development Concepts Using Python”
  - courses: IN 300 ⟵ “IN 300 - 🌐 Programming for Data Analysis (Python, R, and Java)”
  - courses: IN 304 ⟵ “IN 304 - 🌐 Advanced Programming for Data Analysis”
  - courses: IN 400 ⟵ “IN 400 - 🌐 Artificial Intelligence (AI) - Deep Learning and Machine Learning”
### `4bf371e5503a9d55` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cloud-computing-and-solutions · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cloud-computing-solutions-bs/ (sha256 77b0e54d770a)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
### `4d98184be6b6f86a` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-accounting · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-aas/ (sha256 eb162f849b86)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `4e1ee406b08cf17c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-emergency-management · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `4f14f3642b7c18a8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=aviation-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: AV 102 ⟵ “AV 102 - Aviation History”
  - courses: AV 203 ⟵ “AV 203 - Aviation Operations Management”
  - courses: AV 412 ⟵ “AV 412 - Aviation Finance”
  - courses: AV 438 ⟵ “AV 438 - Airline Operations”
  - courses: AV 475 ⟵ “AV 475 - Aviation Law”
### `4fe8d086dec529ec` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cloud-computing-and-solutions · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cloud-computing-solutions-bs/ (sha256 77b0e54d770a)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `5068581703414e65` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=general-finance [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: MT 361 ⟵ “MT 361 - Foundations of Real Estate Practice”
  - courses: MT 421 ⟵ “MT 421 - Financial Planning”
  - courses: MT 422 ⟵ “MT 422 - Portfolio Management”
  - courses: MT 423 ⟵ “MT 423 - Asset Allocation and Risk Management”
  - courses: MT 431 ⟵ “MT 431 - Real Estate Finance and Ethics”
  - courses: MT 432 ⟵ “MT 432 - Real Estate Law”
  - courses: MT 445 ⟵ “MT 445 - 🌐 Managerial Economics”
  - courses: MT 453 ⟵ “MT 453 - Professional Selling”
### `514e4f1f037ebd66` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=customer-service [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: CM 214 ⟵ “CM 214 - Public Speaking for the Professional”
  - courses: MT 202 ⟵ “MT 202 - Building Customer Sales and Loyalty”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
### `5291ba1af7f68232` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=financial-analysis [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: BU 204 ⟵ “BU 204 - 🌐 Macroeconomics”
  - courses: MT 445 ⟵ “MT 445 - 🌐 Managerial Economics”
  - courses: MT 480 ⟵ “MT 480 - 🌐 Corporate Finance”
  - courses: MT 481 ⟵ “MT 481 - Financial Markets”
  - courses: MT 482 ⟵ “MT 482 - 🌐 Financial Statement Analysis”
### `546cc8892cb7533b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-supply-chain-management · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-supply-chain-management-bs/ (sha256 803bc6bd7b23)
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
  - courses: SS 255 ⟵ “SS 255 - Digital Citizenship”
### `55cc153ad5fc2953` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: HU 245 ⟵ “HU 245 - 🌐 Ethics”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 246 ⟵ “SC 246 - 🌐 Fundamentals of Microbiology”
### `57bf713edf5871e5` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-health-science · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `57f9460f739c13ac` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `58cd0f7c29a064b0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=applied-artificial-intelligence-ai-systems-development [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IT 321 ⟵ “IT 321 - Artificial Intelligence Fundamentals and Python for Data”
  - courses: IT 341 ⟵ “IT 341 - Core Machine Learning Algorithms”
  - courses: IT 440 ⟵ “IT 440 - Neural Networks and Deep Learning Foundations”
  - courses: IT 451 ⟵ “IT 451 - Specialized Deep Learning and Applied Artificial Intelligence Systems”
### `58d4097eb28b1503` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `59516fafd4c4a51a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=wealth-management-and-financial-planning [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: MT 421 ⟵ “MT 421 - Financial Planning”
  - courses: MT 422 ⟵ “MT 422 - Portfolio Management”
  - courses: MT 423 ⟵ “MT 423 - Asset Allocation and Risk Management”
### `5bcc2d4d20cae3f8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=business-development [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 359 ⟵ “MT 359 - Integrated Marketing Communications”
  - courses: MT 453 ⟵ “MT 453 - Professional Selling”
  - courses: MT 459 ⟵ “MT 459 - Consumer Behavior”
### `5cce8f46cdc7331e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-education-and-promotion · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-education-promotion-bs/ (sha256 5e9167680106)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `5d5b4e5e6803a7d2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=law-enforcement [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 333 ⟵ “CJ 333 - 🌐 Family and Domestic Violence”
  - courses: CJ 355 ⟵ “CJ 355 - 🌐 Homeland Security”
  - courses: CJ 370 ⟵ “CJ 370 - 🌐 Crime Scene Investigation II”
  - courses: CJ 411 ⟵ “CJ 411 - Drugs and Alcohol in the Criminal Justice System”
### `5e46cdde37a7c4d3` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=crime-scene-investigation [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: CJ 328 ⟵ “CJ 328 - 🌐 Forensic Fingerprint Analysis”
  - courses: CJ 345 ⟵ “CJ 345 - 🌐 Supervisory Practices in Criminal Justice”
  - courses: CJ 370 ⟵ “CJ 370 - 🌐 Crime Scene Investigation II”
  - courses: CJ 385 ⟵ “CJ 385 - 🌐 Forensic Chemistry and Trace Evidence Analysis”
### `61510d93f562258c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management · requirement_key=business-foundations [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/fire-emergency-management-bs/ (sha256 afedb45fd8c0)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `6196e142322448eb` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=progression-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 246 ⟵ “SC 246 - 🌐 Fundamentals of Microbiology”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
### `6247b62201c4abe8` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=lvn-lpn-to-asn-pathway [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: NU 104 ⟵ “NU 104 - Pathophysiology for Nursing”
  - courses: NU 140 ⟵ “NU 140 - Nursing Fundamentals”
  - courses: NU 141 ⟵ “NU 141 - Pharmacology for Nursing”
### `64362c92734f1346` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `64a8bfd3abccd412` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nutrition · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `64f7c5473868efe6` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=business-foundations [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `650179de55cf7e63` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-manufacturing · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-manufacturing-bs/ (sha256 ed13b75cad34)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `65b07f474f6d4ede` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-professional-studies · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-as/ (sha256 8d08aa71b244)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `6607ff47169a9bb0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-information-management · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-information-management-bs/ (sha256 0d8e9e812759)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `668598a3b325092c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-manufacturing · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-manufacturing-bs/ (sha256 ed13b75cad34)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
  - courses: MM 260 ⟵ “MM 260 - Linear Algebra”
### `680f8a42082225ed` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `6862bf254dc337ef` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=entrepreneurship [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: MT 202 ⟵ “MT 202 - Building Customer Sales and Loyalty”
  - courses: MT 207 ⟵ “MT 207 - Starting a Business”
  - courses: MT 209 ⟵ “MT 209 - Small Business Management”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
### `6a018e3d5b820fb5` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=sport-entertainment-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 240 ⟵ “MT 240 - Sport in Society”
  - courses: MT 241 ⟵ “MT 241 - Sport Analytics”
  - courses: MT 242 ⟵ “MT 242 - Managing Sport Programs”
  - courses: MT 243 ⟵ “MT 243 - Sport Sponsorships and Sales”
### `6b24ef0eaad69cb9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-information-technology · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-bs/ (sha256 6d6bdb1e9c45)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `6ca0ac099c24f2cc` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=digital-and-social-media-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 355 ⟵ “MT 355 - 🌐 Marketing Research and Analytics”
  - courses: MT 357 ⟵ “MT 357 - Digital Marketing Platforms and Strategy”
  - courses: MT 358 ⟵ “MT 358 - Social Media Marketing and AI Optimization”
  - courses: MT 359 ⟵ “MT 359 - Integrated Marketing Communications”
### `6e6135a0984b87be` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-marketing · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `74ccba38edaac350` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-computer-science · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/applied-computer-science-bs/ (sha256 49600e5d901a)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `750597cd6195e4ed` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-care-administration · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-care-administration-bs/ (sha256 f6b640a6f508)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `7566482971b6057f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nursing-rn-to-bsn · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-rn-bsn-bs/ (sha256 4d33147a4129)
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: SC 246 ⟵ “SC 246 - 🌐 Fundamentals of Microbiology”
### `769311c359537d9a` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-criminal-justice · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-aas/ (sha256 f7068e07e87b)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `786566da1722799d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=global-marketing-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 450 ⟵ “MT 450 - 🌐 Brand Management Strategy”
  - courses: MT 455 ⟵ “MT 455 - Strategic Management of Sales”
### `7a8a65c71c38e66f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=business-foundations [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `7ab77b9edfdf400b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `7f4e9534bb42bcff` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=software-development-using-python [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 250 ⟵ “IN 250 - 🌐 Software Development Concepts Using Python”
  - courses: IN 254 ⟵ “IN 254 - 🌐 Software Design and Development Concepts Using Python”
  - courses: IN 304 ⟵ “IN 304 - 🌐 Advanced Programming for Data Analysis”
### `7f69616ca0deba79` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aviation-management · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/aviation-management-bs/ (sha256 1ca153298e79)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `8153f225e00a2996` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=procurement [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 300 ⟵ “MT 300 - 🌐 Management of Information Systems”
  - courses: MT 435 ⟵ “MT 435 - 🌐 Operations Management”
  - courses: MT 475 ⟵ “MT 475 - Quality Management”
  - courses: MT 482 ⟵ “MT 482 - 🌐 Financial Statement Analysis”
### `815e47df3770f37a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `81857f96cb23ff5e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `84d3ac90faa4484d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=leadership [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: CM 460 ⟵ “CM 460 - Strategic Communication”
  - courses: LI 410 ⟵ “LI 410 - Leadership in Practice”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 340 ⟵ “MT 340 - 🌐 Conflict Management and Team Dynamics”
### `86a58f0afd97abef` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-early-childhood-administration · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `8c51bbb1b30edfe1` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-human-resource-management · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `8c678fec3416d1a9` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-small-group-management · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/small-group-management-aas/ (sha256 0411c2728524)
  - courses: CS 126 ⟵ “CS 126 - Academic Strategies for the Military Professional”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 297 ⟵ “MT 297 - Associate's Capstone in Small Group Management”
### `8d1efc5847a57989` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=financial-analysis [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 445 ⟵ “MT 445 - 🌐 Managerial Economics”
  - courses: MT 480 ⟵ “MT 480 - 🌐 Corporate Finance”
  - courses: MT 481 ⟵ “MT 481 - Financial Markets”
  - courses: MT 482 ⟵ “MT 482 - 🌐 Financial Statement Analysis”
### `912b948d96766525` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=hospitality-and-tourism-services [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: TH 116 ⟵ “TH 116 - Introduction to Hospitality, Event Management, and Tourism”
  - courses: TH 206 ⟵ “TH 206 - Hotel Management and Operations”
  - courses: TH 213 ⟵ “TH 213 - Food and Beverage Management”
  - courses: TH 230 ⟵ “TH 230 - Foundations of Conference and Event Planning”
### `920aa2fbd19db91d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=project-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 401 ⟵ “IT 401 - Project Management II”
  - courses: MT 400 ⟵ “MT 400 - 🌐 Business Process Management”
  - courses: MT 475 ⟵ “MT 475 - Quality Management”
### `93f060b80550cefd` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=office-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: IT 133 ⟵ “IT 133 - 🌐 Microsoft Office Applications on Demand”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
  - courses: TH 230 ⟵ “TH 230 - Foundations of Conference and Event Planning”
### `955b256faee64bf7` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-health-science · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
  - courses: HS 290 ⟵ “HS 290 - Associate's Capstone in Health Science”
### `970d15090a3cb83a` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=sport-entertainment-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: MT 240 ⟵ “MT 240 - Sport in Society”
  - courses: MT 241 ⟵ “MT 241 - Sport Analytics”
  - courses: MT 242 ⟵ “MT 242 - Managing Sport Programs”
  - courses: MT 243 ⟵ “MT 243 - Sport Sponsorships and Sales”
### `9957754f4effbd33` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nutrition · requirement_key=holistic-nutrition [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/nutrition-bs/ (sha256 dd1592b09484)
  - courses: HW 310 ⟵ “HW 310 - Complementary and Integrative Medicine”
  - courses: NS 455 ⟵ “NS 455 - Current Trends in Nutrition”
  - courses: NS 460 ⟵ “NS 460 - Dietary Supplements and Nutraceuticals”
  - courses: NS 465 ⟵ “NS 465 - Functional Nutrition”
### `997c41c7a447e62c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=information-systems-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 332 ⟵ “IT 332 - 🌐 Principles of Information Systems Architecture”
  - courses: IT 402 ⟵ “IT 402 - 🌐 IT Consulting Skills”
  - courses: MT 451 ⟵ “MT 451 - Managing Technological Innovation”
### `9a4bed5732dfd276` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=decision-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: IN 302 ⟵ “IN 302 - 🌐 Reporting and Visualization”
  - courses: MM 305 ⟵ “MM 305 - 🌐 Business Statistics and Quantitative Analysis”
  - courses: MM 330 ⟵ “MM 330 - Probability With Business Applications”
  - courses: MM 340 ⟵ “MM 340 - Decision Modeling”
  - courses: MM 341 ⟵ “MM 341 - Decision Management”
  - courses: MT 313 ⟵ “MT 313 - Corporate Sustainability and Social Responsibility”
### `9ab4cfafba91195d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `9b04e88b27ae33fc` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=real-estate [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - courses: MT 361 ⟵ “MT 361 - Foundations of Real Estate Practice”
  - courses: MT 431 ⟵ “MT 431 - Real Estate Finance and Ethics”
  - courses: MT 432 ⟵ “MT 432 - Real Estate Law”
### `9c511f1fc9baf5b0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-applied-supply-chain-management · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `9e05a7bb2b3d3b09` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-studies · requirement_key=industrial-organizational-psychology [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-bs/ (sha256 5704276a3164)
  - courses: PS 390 ⟵ “PS 390 - Introduction to Industrial/Organizational Psychology”
  - courses: PS 391 ⟵ “PS 391 - Psychology of Leadership”
  - courses: PS 392 ⟵ “PS 392 - Attitudes and Motivation in the Workplace”
  - courses: PS 451 ⟵ “PS 451 - Selection and Assessment in Organizations”
### `9fa4f0e2929e8fe1` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=public-relations [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - courses: CM 350 ⟵ “CM 350 - Public Relations Strategies”
  - courses: CM 355 ⟵ “CM 355 - Public Relations Case Studies”
  - courses: CM 455 ⟵ “CM 455 - Digital Public Relations and Communication”
  - courses: CM 465 ⟵ “CM 465 - Communication Law and Ethics”
### `a05da22fcc264b66` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `a10cd915a4a97bd9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nutrition · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/nutrition-bs/ (sha256 dd1592b09484)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 180 ⟵ “SC 180 - General Chemistry I”
### `a291414fa28245a7` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a2bf473521816f84` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=military-physician-assistant-preparation-mpap [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 180 ⟵ “SC 180 - General Chemistry I”
  - courses: SC 190 ⟵ “SC 190 - General Chemistry II”
  - courses: SC 335 ⟵ “SC 335 - Survey of Biochemistry”
### `a405970033b62a81` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-information-management · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `a42e45c945d11730` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-nutrition · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/nutrition-bs/ (sha256 dd1592b09484)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a4e0172d957dddfe` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a5e5f8b79a1500c9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=cissp-certification-preparation [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: IT 277 ⟵ “IT 277 - 🌐 Certified Information Systems Security Professional I”
  - courses: IT 279 ⟵ “IT 279 - 🌐 Certified Information Systems Security Professional II”
  - courses: IT 410 ⟵ “IT 410 - 🌐 Certified Information Systems Security Professional III”
### `a74c4be524a26f60` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-emergency-management · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/emergency-management-bs/ (sha256 54adfba134ed)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a86bee267855127b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-education-and-promotion · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-education-promotion-bs/ (sha256 5e9167680106)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `a8ad7a8aa499f3f1` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-finance · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/finance-bs/ (sha256 8914c341ca60)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ab56f51a88d41050` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-emergency-management · requirement_key=business-foundations [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/emergency-management-bs/ (sha256 54adfba134ed)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `abadf5347acdc4e2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=economics [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: MT 313 ⟵ “MT 313 - Corporate Sustainability and Social Responsibility”
  - courses: MT 314 ⟵ “MT 314 - Social Innovation and Entrepreneurship”
  - courses: MT 330 ⟵ “MT 330 - International Marketing and Business Development”
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: SS 359 ⟵ “SS 359 - Sustainable and Resilient Communities”
### `aea46225296b26db` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=software-development-using-java [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IT 117 ⟵ “IT 117 - 🌐 Website Development”
  - courses: IN 252 ⟵ “IN 252 - 🌐 Software Development Concepts Using Java”
  - courses: IN 256 ⟵ “IN 256 - 🌐 Software Design and Development Concepts Using Java”
  - courses: IN 352 ⟵ “IN 352 - 🌐 Advanced Software Development Including Web and Mobility Using Java”
  - courses: IN 452 ⟵ “IN 452 - 🌐 Advanced Software Development Using Java”
  - courses: IT 488 ⟵ “IT 488 - 🌐 Software Product Development Using Agile”
### `af949c8645d20ee2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=construction-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 281 ⟵ “MT 281 - Fundamentals of Construction Management”
  - courses: MT 282 ⟵ “MT 282 - Construction Methods and Materials”
  - courses: MT 381 ⟵ “MT 381 - Construction Planning and Scheduling”
  - courses: MT 382 ⟵ “MT 382 - Construction Cost Estimating”
  - courses: MT 383 ⟵ “MT 383 - Construction Law”
### `b2713b28b85584c0` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-flight · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/aviation/professional-flight-bs/ (sha256 a564dfddbaa1)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `b346240f3c71b8c4` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `b3ffe887fcfcc70b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=supply-chain-and-logistics [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `b41bf4dc53bb2c05` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cybersecurity · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cybersecurity-bs/ (sha256 cf3240b74bd9)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
  - courses: MM 250 ⟵ “MM 250 - 🌐 Discrete Mathematics”
### `b656b27b6bd3a5b7` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=construction-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: MT 281 ⟵ “MT 281 - Fundamentals of Construction Management”
  - courses: MT 282 ⟵ “MT 282 - Construction Methods and Materials”
  - courses: MT 381 ⟵ “MT 381 - Construction Planning and Scheduling”
  - courses: MT 382 ⟵ “MT 382 - Construction Cost Estimating”
  - courses: MT 383 ⟵ “MT 383 - Construction Law”
### `b7806094e49d208c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=software-development-using-c [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IT 117 ⟵ “IT 117 - 🌐 Website Development”
  - courses: IN 251 ⟵ “IN 251 - 🌐 Software Development Concepts Using C#”
  - courses: IN 255 ⟵ “IN 255 - 🌐 Software Design and Development Concepts Using C#”
  - courses: IN 351 ⟵ “IN 351 - 🌐 Advanced Software Development Including Web and Mobility Using C#”
  - courses: IN 451 ⟵ “IN 451 - 🌐 Advanced Software Development Using C#”
  - courses: IT 488 ⟵ “IT 488 - 🌐 Software Product Development Using Agile”
### `b9fc89219767f8d1` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-accounting · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-aas/ (sha256 eb162f849b86)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ba2f2e7521b9b055` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-and-wellness · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-wellness-bs/ (sha256 ae3f65d930b4)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ba84e1057889532d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=forensic-accountancy [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 465 ⟵ “AC 465 - Fraud and Forensic Accounting”
  - courses: AC 466 ⟵ “AC 466 - Fraud Detection and Financial Statement Analysis”
  - courses: AC 468 ⟵ “AC 468 - Digital Forensics and Investigative Techniques”
### `c0e69e84cd0f5b09` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-and-wellness · requirement_key=exercise-science [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-wellness-bs/ (sha256 ae3f65d930b4)
  - courses: EF 300 ⟵ “EF 300 - Principles of Kinesiology”
  - courses: EF 305 ⟵ “EF 305 - Exercise Physiology”
  - courses: EF 310 ⟵ “EF 310 - Applied Exercise Science for Healthy Aging and Special Conditions”
  - courses: EF 400 ⟵ “EF 400 - Psychosocial Aspects of Exercise”
  - courses: NS 425 ⟵ “NS 425 - Sports Nutrition”
### `c2244807f897c2a7` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=environmental-science [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: SC 325 ⟵ “SC 325 - Environmental Risk Assessment”
  - courses: SC 340 ⟵ “SC 340 - The Biology of Pollution”
  - courses: SC 350 ⟵ “SC 350 - Conservation of Natural Resources”
  - courses: SC 362 ⟵ “SC 362 - Our Changing Climate”
  - courses: SC 415 ⟵ “SC 415 - Environmental Health”
### `c22a4d3668768ac6` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=information-processing [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 115 ⟵ “CM 115 - Communication - Concepts and Skills”
  - courses: IT 133 ⟵ “IT 133 - 🌐 Microsoft Office Applications on Demand”
  - courses: IT 153 ⟵ “IT 153 - 🌐 Spreadsheet Applications”
  - courses: IT 163 ⟵ “IT 163 - 🌐 Database Concepts Using Microsoft Access”
### `c29921c2c1852356` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-health-science · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `c5873e69d19033a8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-and-wellness · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-wellness-bs/ (sha256 ae3f65d930b4)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: SC 235 ⟵ “SC 235 - 🌐 Human Biology”
### `c62e974af2a4d442` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-human-resource-management · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/human-resource-management-bs/ (sha256 8c3efdbb3966)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ca335173370414e8` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=project-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 401 ⟵ “IT 401 - Project Management II”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 400 ⟵ “MT 400 - 🌐 Business Process Management”
  - courses: MT 475 ⟵ “MT 475 - Quality Management”
### `caacbb12d496450b` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-health-science · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `cc525465f9a419ed` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=social-issues [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: CM 305 ⟵ “CM 305 - Communicating in a Diverse Society”
  - courses: HU 375 ⟵ “HU 375 - Social Justice and Sustainability”
  - courses: SC 361 ⟵ “SC 361 - Population and Society”
  - courses: SS 359 ⟵ “SS 359 - Sustainable and Resilient Communities”
  - courses: SC 415 ⟵ “SC 415 - Environmental Health”
### `cce91badae07cc71` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-information-technology · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-aas/ (sha256 071358cda74e)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 212 ⟵ “MM 212 - 🌐 College Algebra”
### `d1dbf0a192da22a2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=sport-entertainment-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 240 ⟵ “MT 240 - Sport in Society”
  - courses: MT 241 ⟵ “MT 241 - Sport Analytics”
  - courses: MT 242 ⟵ “MT 242 - Managing Sport Programs”
  - courses: MT 243 ⟵ “MT 243 - Sport Sponsorships and Sales”
### `d45cd7a4a24c0339` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=artificial-intelligence-ai [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 245 ⟵ “IN 245 - Introduction to Artificial Intelligence and Its Impact”
  - courses: IN 246 ⟵ “IN 246 - The Human Side of Artificial Intelligence: Understanding Interaction and Design”
  - courses: IN 304 ⟵ “IN 304 - 🌐 Advanced Programming for Data Analysis”
  - courses: IN 305 ⟵ “IN 305 - Artificial Intelligence, Society, and the Future of Work”
### `d6733ddd7a5115a2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/fire-emergency-management-bs/ (sha256 afedb45fd8c0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `d75a16702c74f34d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: SC 156 ⟵ “SC 156 - Principles of Chemistry”
  - courses: SS 270 ⟵ “SS 270 - Social Problems”
### `d89fbbb5924734e2` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=retail-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: MT 102 ⟵ “MT 102 - Principles of Retailing”
  - courses: MT 202 ⟵ “MT 202 - Building Customer Sales and Loyalty”
  - courses: MT 209 ⟵ “MT 209 - Small Business Management”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
### `d98482956e12c9d6` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `d9be703f6d48a9a2` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-criminal-justice · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-bs/ (sha256 4bad073b5135)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `d9f1995012b4740a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=public-accountancy [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 314 ⟵ “AC 314 - Accounting Information Systems and Enterprise Risk Management”
  - courses: AC 430 ⟵ “AC 430 - Advanced Tax - Corporate”
  - courses: AC 444 ⟵ “AC 444 - Accounting Visualization and Business Intelligence”
### `dae8ba2bb98c0b1d` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-marketing · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/marketing-bs/ (sha256 f769649697ce)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `dc563d760c7fdbba` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-early-childhood-development · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/early-childhood-development-aas/ (sha256 fdad375265a0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `dd3176ec070e018b` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `dd61ec18c6de63ff` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-analytics · requirement_key=information-security-and-assurance [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/analytics-bs/ (sha256 09e640d0f8ba)
  - courses: IN 203 ⟵ “IN 203 - 🌐 Networking With Microsoft Technologies”
  - courses: IT 273 ⟵ “IT 273 - 🌐 Networking Concepts”
  - courses: IT 278 ⟵ “IT 278 - 🌐 Windows Administration”
  - courses: IT 316 ⟵ “IT 316 - 🌐 Computer Forensics”
  - courses: IT 390 ⟵ “IT 390 - 🌐 Intrusion Detection and Incident Response”
  - courses: IT 411 ⟵ “IT 411 - 🌐 Digital Forensics”
  - courses: IT 484 ⟵ “IT 484 - 🌐 Cybersecurity Policies”
### `deb6d5b8c196e770` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=supply-chain-management-and-logistics [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: MT 433 ⟵ “MT 433 - Global Supply Chain Management”
  - courses: MT 434 ⟵ “MT 434 - Logistics and Distribution Management”
  - courses: MT 436 ⟵ “MT 436 - Purchasing and Supply Chain Management”
  - courses: MT 437 ⟵ “MT 437 - Strategic Warehouse Management”
  - courses: MT 438 ⟵ “MT 438 - Analytics in the Digital Supply Chain”
### `dfa12011deb88491` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=emt-to-asn-and-paramedic-to-asn-pathways-2 [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: NU 104 ⟵ “NU 104 - Pathophysiology for Nursing”
  - courses: NU 140 ⟵ “NU 140 - Nursing Fundamentals”
  - courses: NU 141 ⟵ “NU 141 - Pharmacology for Nursing”
### `e1c47b3059f90bdf` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=digital-communication [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - courses: CM 270 ⟵ “CM 270 - Writing for Multimedia”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
  - courses: CM 455 ⟵ “CM 455 - Digital Public Relations and Communication”
  - courses: MT 357 ⟵ “MT 357 - Digital Marketing Platforms and Strategy”
  - courses: MT 358 ⟵ “MT 358 - Social Media Marketing and AI Optimization”
### `e21238cfc7e1e8bb` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-nursing · requirement_key=emt-to-asn-and-paramedic-to-asn-pathways [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/nursing/nursing-as/ (sha256 c91e66a2d143)
  - courses: SC 121 ⟵ “SC 121 - Human Anatomy and Physiology I”
  - courses: SC 131 ⟵ “SC 131 - Human Anatomy and Physiology II”
  - courses: NU 104 ⟵ “NU 104 - Pathophysiology for Nursing”
### `e33bd8cd7eace64a` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `e3c9440b7d2e9389` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-sustainability · requirement_key=health-sciences [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/sustainability-bs/ (sha256 040de9f49bec)
  - courses: HD 420 ⟵ “HD 420 - Social Determinants of Health and Health Behavior”
  - courses: NS 430 ⟵ “NS 430 - Whole Foods Production”
  - courses: SC 361 ⟵ “SC 361 - Population and Society”
  - courses: SC 362 ⟵ “SC 362 - Our Changing Climate”
  - courses: SC 415 ⟵ “SC 415 - Environmental Health”
### `e4cb72720310c957` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-health-science · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `e7d1049c7065edc7` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-small-group-management · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/small-group-management-aas/ (sha256 0411c2728524)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `e886900fecb5112e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-professional-flight · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `e95d4d0a3f9fe572` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/fire-emergency-management-bs/ (sha256 afedb45fd8c0)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `ea66445f72975fc9` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-care-administration · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-care-administration-bs/ (sha256 f6b640a6f508)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
### `ed4d163045193186` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=information-system-management [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: IT 301 ⟵ “IT 301 - 🌐 Project Management I”
  - courses: IT 402 ⟵ “IT 402 - 🌐 IT Consulting Skills”
  - courses: MT 300 ⟵ “MT 300 - 🌐 Management of Information Systems”
  - courses: MT 451 ⟵ “MT 451 - Managing Technological Innovation”
### `ee777757d28ebc8c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-health-science · requirement_key=military-physician-assistant-preparation-mpap-2 [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-bs/ (sha256 c7c3b90ce9a0)
  - courses: HS 111 ⟵ “HS 111 - 🌐 Medical Terminology”
  - courses: PS 124 ⟵ “PS 124 - 🌐 Introduction to Psychology”
  - courses: PS 200 ⟵ “PS 200 - Introduction to Cognitive Psychology”
### `ee7eb526753eefbc` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/environmental-policy-management-bs/ (sha256 10dc519623e0)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 207 ⟵ “MM 207 - 🌐 Statistics”
  - courses: SC 225 ⟵ “SC 225 - Environmental Science”
### `eff597452bf65e6b` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-business-administration · requirement_key=fintech [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-bs/ (sha256 867d30cbb1c8)
  - courses: FI 310 ⟵ “FI 310 - FinTech Principles and Concepts”
  - courses: FI 311 ⟵ “FI 311 - FinTech Law and Ethics”
  - courses: FI 410 ⟵ “FI 410 - Blockchain for the Financial Industry”
### `f08a22590581f2bb` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=leadership [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
  - courses: CM 460 ⟵ “CM 460 - Strategic Communication”
  - courses: LI 410 ⟵ “LI 410 - Leadership in Practice”
  - courses: MT 302 ⟵ “MT 302 - 🌐 Organizational Behavior”
  - courses: MT 340 ⟵ “MT 340 - 🌐 Conflict Management and Team Dynamics”
### `f0eb0732e191a4cf` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-professional-studies · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/multidisciplinary-professional-studies/professional-studies-as/ (sha256 8d08aa71b244)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
### `f20a84efa3a6109c` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management · requirement_key=business-foundations [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/environmental-policy-management-bs/ (sha256 10dc519623e0)
  - courses: AC 112 ⟵ “AC 112 - Accounting Fundamentals for Management”
  - courses: MT 140 ⟵ “MT 140 - 🌐 Introduction to Management”
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: MT 219 ⟵ “MT 219 - 🌐 Marketing”
### `f42c883adc44b413` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-accounting-and-analytics · requirement_key=tax-accountancy [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/accounting-bs/ (sha256 afa28b6f2d20)
  - courses: AC 314 ⟵ “AC 314 - Accounting Information Systems and Enterprise Risk Management”
  - courses: AC 430 ⟵ “AC 430 - Advanced Tax - Corporate”
  - courses: MT 421 ⟵ “MT 421 - Financial Planning”
  - courses: MT 483 ⟵ “MT 483 - Investments”
### `f821ffc2c79cb502` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-fire-and-emergency-management · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `f9d19b8da8968c9d` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-accounting · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
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
### `fa4e32f066b232e4` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-criminal-justice · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/criminal-justice-aas/ (sha256 f7068e07e87b)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `fa78913d73469136` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-policy-and-management · requirement_key=program-requirements-open-elective-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/environmental-policy-management-bs/ (sha256 10dc519623e0)
  - section: program-requirements-open-elective-requirements ⟵ “Program Requirements — Open Elective Requirements”
### `fc568ca909ef3fbd` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-communication · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/social-behavioral-sciences/communication-bs/ (sha256 a8750f212820)
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CM 240 ⟵ “CM 240 - Technical Communication”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: PS 124 ⟵ “PS 124 - 🌐 Introduction to Psychology”
### `fd220d8f069f7c89` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-business-administration · requirement_key=sales [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/business-administration-aas/ (sha256 28fbaecf2ab3)
  - courses: CM 206 ⟵ “CM 206 - Interpersonal Communication”
  - courses: CM 214 ⟵ “CM 214 - Public Speaking for the Professional”
  - courses: IT 133 ⟵ “IT 133 - 🌐 Microsoft Office Applications on Demand”
  - courses: MT 221 ⟵ “MT 221 - Customer Service”
### `ff21436b8d96262e` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-human-resource-management · requirement_key=program-requirements-core-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/human-resource-management-bs/ (sha256 8c3efdbb3966)
  - courses: BU 224 ⟵ “BU 224 - 🌐 Microeconomics”
  - courses: CM 107 ⟵ “CM 107 - 🌐 College Composition I”
  - courses: CM 220 ⟵ “CM 220 - 🌐 College Composition II”
  - courses: CS 212 ⟵ “CS 212 - 🌐 Communicating Professionalism”
  - courses: MM 255 ⟵ “MM 255 - 🌐 Business Math and Statistical Measures”
### `069bd838f448425f` Purdue University Global — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.purdueglobal.edu/transfer-students/ (sha256 1ef62a1d54a4)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Undergraduate courses with a grade of “C-” or better are eligible for transfer evaluation.”
### `c9b810e99be657ff` Purdue University-Main Campus — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://admissions.purdue.edu/become-student/transfer/credit/dual/ (sha256 d4daf8458c79)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - per_credit_hour_charge: 25 ⟵ “One of the benefits of taking dual credit courses in high school is tuition assistance. Tuition for the dual credit enrollment program is $25 per credit hour with no additional fees. A 3-4 credit hour dual credit program course will cost $75-100. A comparable course taken as a Purdue undergraduate c”
  - eligibility_tier: 2.5 ⟵ “Minimum GPA of 2.5 on a 4.0 scale”
### `d1e6540a9968479a` Purdue University-Main Campus — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://admissions.purdue.edu/become-student/transfer/credit/college-level-exam/ (sha256 cbb2956faf4e)
- checks: {"distinct_exams": 33, "equivalencies": 48, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50+]:  ⟵ “American Government | POL 10100 | 3 | 50+”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50+]:  ⟵ “American Literature | ENGL 25000 | 3 | 50+”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50+]:  ⟵ “Analyzing and Interpreting Literature (essay not required) | ENGL 23100 | 3 | 50+”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50+]:  ⟵ “College Algebra | MA 15300 | 3 | 50+”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50+]:  ⟵ “College Composition | UND 1XXXX | 3 | 50+”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50+]:  ⟵ “College Composition Modular | UND 1XXXX | 3 | 50+”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50+]:  ⟵ “College Mathematics | MA 1XXXX | 3 | 50+”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50+]:  ⟵ “English Literature | ENGL 1XXXX | 3 | 50+”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50+]:  ⟵ “Financial Accounting | MGMT 20000 | 3 | 50+”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50-58]:  ⟵ “French | FR 10100 | 3 | 50-58”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59-63]:  ⟵ “French | FR 10100 and 10200 | 6 | 59-63”
  - equivalencies[CLEP-FRENCH-LANGUAGE|64-68]:  ⟵ “French | FR 10100, 10200 and 20100 | 9 | 64-68”
  - equivalencies[CLEP-FRENCH-LANGUAGE|69+]:  ⟵ “French | FR 10100, 10200, 20100 and 20200 | 12 | 69+”
  - equivalencies[CLEP-BIOLOGY|55+]:  ⟵ “General Biology | BIOL 11000 | 4 | 55+”
  - equivalencies[CLEP-BIOLOGY|70+]:  ⟵ “General Biology | BIOL 11000 and 11100 | 8 | 70+”
  - equivalencies[CLEP-CHEMISTRY|50+]:  ⟵ “General Chemistry | CHM 11100 | 3 | 50+”
  - equivalencies[CLEP-CHEMISTRY|65+]:  ⟵ “General Chemistry | CHM 11510 | 3 | 65+”
  - equivalencies[CLEP-CHEMISTRY|70+]:  ⟵ “General Chemistry | CHM 11610 | 6 | 70+”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50-58]:  ⟵ “German | GER 10100 | 3 | 50-58”
  - equivalencies[CLEP-GERMAN-LANGUAGE|59-63]:  ⟵ “German | GER 10100 and 10200 | 6 | 59-63”
  - equivalencies[CLEP-GERMAN-LANGUAGE|64-68]:  ⟵ “German | GER 10100, 10200 and 20100 | 9 | 64-68”
  - equivalencies[CLEP-GERMAN-LANGUAGE|69+]:  ⟵ “German | GER 10100, 10200, 20100 and 20200 | 12 | 69+”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50+]:  ⟵ “History of the United States I | HIST 15100 | 3 | 50+”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50+]:  ⟵ “History of the United States II | HIST 15200 | 3 | 50+”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50+]:  ⟵ “Human Growth and Development | HDFS 21000 | 3 | 50+”
  - … 23 more rows
### `4b26943b0c426b29` Purdue University-Main Campus — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://admissions.purdue.edu/become-student/transfer/credit/ (sha256 e09e06a8989a)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 32 ⟵ “However, at least 32 credit hours of upper-division courses must be earned at Purdue for a degree from the university.”
### `m02f1be91151e7c7` Vincennes University — credit_policies 2026-27 · policy_kind=dual_enrollment [changed] (source_unlabeled)
- source: https://www.vinu.edu/_resources/docs/pdf/project-excel/vu-dual-credit-policies-and-procedures-6-1-25.pdf (sha256 8f620f43f365)
- checks: {"fields": ["per_credit_hour_charges"], "merged_pages": 5, "tiers": 0}
- change dual_enrollment: `{'per_credit_hour_charges': [{'amount': 100, 'kind': 'other', 'line': 'The cost of the program is $100 per credit hour, making it an incredible value for students. In addition, textbooks are offered at'}, {'amount': 25, 'kind': 'other', 'line': '●\u200b   Courses taught by a VU-approved high school instructor: $25 per credit hour*'}, {'amount': 75, 'kind': 'other', 'line': '●\u200b   Courses taught by a VU adjunct: $75 per credit hour'}, {'amount': 100, 'kind': 'other', 'line': '●\u200b   Courses offered online: $100 per credit hour plus current textbook cost'}, {'amount': 25, 'kind': 'fee', 'line': 'Credit course one time; however, a $25 per credit hour fee applies for retakes, regardless of waiver'}, {'amount': 25, 'kind': 'other', 'line': 'Courses taught by a VU approved high school instructor: $25 per credit hour*'}, {'amount': 75, 'kind': 'other', 'line': 'Courses taught by a VU adjunct: $75 per credit hour'}, {'amount': 75, 'kind': 'other', 'line': 'Courses offered online: $75 per credit hour**'}]}` → `{'per_credit_hour_charges': [{'amount': 25, 'kind': 'other', 'line': '●\u200b   Courses taught by a VU-approved high school instructor: $25 per credit hour*'}, {'amount': 75, 'kind': 'other', 'line': '●\u200b   Courses taught by a VU adjunct: $75 per credit hour'}, {'amount': 100, 'kind': 'other', 'line': '●\u200b   Courses offered online: $100 per credit hour plus current textbook cost'}, {'amount': 25, 'kind': 'fee', 'line': 'Credit course one time; however, a $25 per credit hour fee applies for retakes, regardless of waiver'}, {'amount': 100, 'kind': 'other', 'line': 'The cost of the program is $100 per credit hour, making it an incredible value for students. In addition, textbooks are offered at'}, {'amount': 25, 'kind': 'other', 'line': 'Courses taught by a VU approved high school instructor: $25 per credit hour*'}, {'amount': 75, 'kind': 'other', 'line': 'Courses taught by a VU adjunct: $75 per credit hour'}, {'amount': 75, 'kind': 'other', 'line': 'Courses offered online: $75 per credit hour**'}]}`
  - per_credit_hour_charge: 25 ⟵ “●​   Courses taught by a VU-approved high school instructor: $25 per credit hour*”
  - per_credit_hour_charge: 75 ⟵ “●​   Courses taught by a VU adjunct: $75 per credit hour”
  - per_credit_hour_charge: 100 ⟵ “●​   Courses offered online: $100 per credit hour plus current textbook cost”
  - per_credit_hour_charge: 25 ⟵ “Credit course one time; however, a $25 per credit hour fee applies for retakes, regardless of waiver”
  - per_credit_hour_charge: 100 ⟵ “The cost of the program is $100 per credit hour, making it an incredible value for students. In addition, textbooks are offered at”
  - per_credit_hour_charge: 25 ⟵ “●​   Courses taught by a VU-approved high school instructor: $25 per credit hour*”
  - per_credit_hour_charge: 75 ⟵ “●​   Courses taught by a VU adjunct: $75 per credit hour”
  - per_credit_hour_charge: 100 ⟵ “●​   Courses offered online: $100 per credit hour plus current textbook cost”
  - per_credit_hour_charge: 25 ⟵ “Courses taught by a VU approved high school instructor: $25 per credit hour*”
  - per_credit_hour_charge: 75 ⟵ “Courses taught by a VU adjunct: $75 per credit hour”
  - per_credit_hour_charge: 75 ⟵ “Courses offered online: $75 per credit hour**”
  - per_credit_hour_charge: 25 ⟵ “Courses taught by a VU approved high school instructor: $25 per credit hour*”

## Exceptions (57)

### `20bec63c4c2aac18` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances (sha256 ed67d0bcec13)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Contact Our Office Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `351991a544a42345` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure (sha256 75e862992d38)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `3cc223e850f3f483` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview (sha256 04ad9f21fd69)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `4a69d15ca3b6624e` Ball State University — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships (sha256 ded588b095f2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “A dependency override does not guarantee an adjustment will be made to your aid package.”
### `535b1bd3633d7ece` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/types/scholarships/scholarship-appeals-for-returning-students (sha256 78283b420a30)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You can access the scholarship appeal form and instructions here.”
### `53a6e704763758ca` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility (sha256 27394f708f87)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If the student regains pace prior to the next evaluation period, they must submit a satisfactory academic progress appeal in order to have their eligibility reviewed.”
  - sentence: sap_appeal ⟵ “Select "Satisfactory Academic Progress Appeal" in the "Start a New Request" section.”
### `63443fb16bfb8c2e` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans (sha256 d38a611fdc05)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `a0a74ef69d3d010e` Ball State University — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships (sha256 ded588b095f2)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 16}
  - sentence: need_based_special_circumstances ⟵ “Special and Unusual Circumstances We recognize that the FAFSA may not always accurately reflect your financial situation and/or dependency status.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations that justify an aid administrator adjusting data elements in the Cost of Attendance or in the EFC calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation, more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Special Circumstance Requests will be considered after you receive your initial award notification for the current aid year.”
  - sentence: need_based_special_circumstances ⟵ “After reviewing your special circumstance documentation, your aid package may remain the same, be increased, or reduced according to the financial information that has been submitted.”
### `a9e44425b17b5aa1` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/maintaining-financial-aid-eligibility (sha256 27394f708f87)
- issues: semantic_review_required, conflicting_sources:https://www.bsu.edu/admissions/financial-aid-and-scholarships,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/change-in-financial-circumstances,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/grievance-procedure,https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/managing-student-loans
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid and Scholarships Financial Aid Overview Managing Student Loans Change in Financial Circumstances Grievance Procedure Maintaining Financial Aid Eligibility Cardinal Central L.A.”
### `edb402d2b00a699c` Ball State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bsu.edu/admissions/financial-aid-and-scholarships/award/financial-aid-overview (sha256 04ad9f21fd69)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Any cost of attendance adjustment may require the return of loan funds or the necessity to repay other types of assistance already received.”
### `6ed1061e8e7eea13` Ball State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bsu.edu/admissions/tuition-and-fees (sha256 00411e17d4bf)
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
### `14c3b48064393ea2` Indiana University-Indianapolis — appeals 2024-25 [new] (labeled_in_source)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/eligibility-appeal.html (sha256 57196653ec45)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “What special circumstances may be considered for an appeal?”
  - sentence: need_based_special_circumstances ⟵ “If you have previously submitted a special circumstances appeal, you should not file another for the same reason unless instructed to do so by this office.”
### `3e5ce253ebfebb2a` Indiana University-Indianapolis — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/ (sha256 9c765f28613c)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Scholarship appeal To appeal our decision that resulted in the revocation of your scholarship, you’ll need to fill out a scholarship appeal form.”
### `8f58e56fa29aaf8f` Indiana University-Indianapolis — appeals 2026-27 [new] (source_unlabeled)
- source: https://indianapolis.iu.edu/cost-aid/scholarships/renew/ (sha256 83e4dbc6beef)
- issues: semantic_review_required, conflicting_sources:https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you believe that you have additional education-related expenses, you can submit a Special Circumstances form to have your specific expenses reviewed.”
### `9fc14ef56bf50899` Indiana University-Indianapolis — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/ (sha256 9c765f28613c)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “File a SAP appeal form You have special circumstances that weren’t documented on your FAFSA If your family’s financial status has changed since you filed your FAFSA or if you had an expense that was not considered as part of the FAFSA, you may be able to file a special circumstance appeal.”
  - sentence: sap_appeal ⟵ “Please contact the Office of Financial Aid and Scholarships with questions or to request this form in an accessible format. 2025-26 aid year (Fall 2025, Spring 2026, Summer 2026) IU Indianapolis parent refusal form 2026-27 aid year (Fall 2026, Spring 2027, and Summer 2027) IU Indianapolis parent refusal form Quick links Academic progress appeal To appeal our decision that you aren’t making satisfa”
### `d90fe792cbb00a42` Indiana University-Indianapolis — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/ (sha256 9c765f28613c)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “The following circumstances do not qualify students to be eligible as an Independent status and will not be approved when submitting a Dependency Override appeal: Your parents refuse to contribute to your education Your parents are unwilling to provide information on the FAFSA or for verification Your parents don’t claim you as a dependent for income tax purposes You demonstrate total self-suffici”
### `f7ecdf4bc9a5810d` Indiana University-Indianapolis — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://indianapolis.iu.edu/cost-aid/financial-aid/manage-aid/file-appeal/ (sha256 9c765f28613c)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://indianapolis.iu.edu/cost-aid/scholarships/renew/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Other situations If you feel you have a special circumstance that isn’t covered by a change to your Student Aid Index or cost of attendance, contact the Office of Financial Aid and Scholarships for assistance.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstance appeal forms Please contact the Office of Financial Aid and Scholarships with questions or to request these forms in an accessible format. 2025-26 aid year (Fall 2025, Spring 2026, Summer 2026) Submit the special circumstance COA appeal form 2026-27 aid year (Fall 2026, Spring 2027, and Summer 2027) Submit the special circumstance COA appeal form You want to be classified as i”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances that may qualify you include an abusive family environment or being abandoned by your parents.”
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
### `1e4abecbb8e227da` Purdue University Global — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.purdueglobal.edu/transfer-students/credit-by-exam-course/ (sha256 45fb41736f61)
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
### `86f086f635edd2e9` Purdue University Global — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.purdueglobal.edu/transfer-students/credit-by-exam-course/ (sha256 45fb41736f61)
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
### `c4c50c88575b9d06` Purdue University Global — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.purdueglobal.edu/transfer-students/credit-by-exam-course/ (sha256 45fb41736f61)
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
### `5282e3dbc49154f8` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-health-science · requirement_key=preprofessional [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-aas/ (sha256 e5fda4e45072)
- issues: mixed_required_and_choice
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
### `8876d5e1eb7fe6a3` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-science-in-health-science · requirement_key=preprofessional [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/health-sciences/health-science-as/ (sha256 cca0d111f7a1)
- issues: mixed_required_and_choice
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
- issues: course_alternatives_in_rule_text, mixed_required_and_choice
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
### `f22ab647e940088c` Purdue University Global — degree_requirements 2026-27 · program_key=associate-of-applied-science-in-information-technology · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/information-technology-aas/ (sha256 071358cda74e)
- issues: mixed_required_and_choice
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
### `f471cf82b1f943ea` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-cloud-computing-and-solutions · requirement_key=program-requirements-major-requirements [same] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/cloud-computing-solutions-bs/ (sha256 77b0e54d770a)
- issues: mixed_required_and_choice
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
### `fdde2d5cd278772f` Purdue University Global — degree_requirements 2026-27 · program_key=bachelor-of-science-in-organizational-management · requirement_key=human-resources [new] (labeled_in_source)
- source: https://catalog.purdueglobal.edu/undergraduate/business-information-technology/organizational-management-bs/ (sha256 a12f98479372)
- issues: course_alternatives_in_rule_text
  - courses: MT 203 ⟵ “MT 203 - 🌐 Human Resource Management”
  - courses: HR 400 ⟵ “HR 400 - 🌐 Talent Acquisition and Management”
  - courses: HR 410 ⟵ “HR 410 - Talent Development and Learning”
  - courses: HR 420 ⟵ “HR 420 - Workplace Law, Labor Relations, and HR Risk Management”
  - courses: HR 485 ⟵ “HR 485 - 🌐 Strategic HRM: Analytics and Business Decision-Making”
### `134b4579aa3fe199` Purdue University-Main Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/contact/policiesappeals/ (sha256 23e0e70a3751)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Unusual circumstances are circumstances which, in the professional judgment of a financial aid administrator, warrant the student to be considered independent.”
### `1365c6b7e6a91012` Purdue University-Main Campus — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/ (sha256 a37e1c4bfe42)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you experience income loss, such as a job change or job loss due to COVID-19, contact the Division of Financial Aid to see if a special circumstance appeal is a possibility.”
  - sentence: need_based_special_circumstances ⟵ “Please note that you must be out of work or experiencing an income loss for at least 8 weeks for us to be able to consider it a special circumstance.”
### `589169262f5421f5` Purdue University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.purdue.edu/dfa/manage/ (sha256 56a3a89a1bf9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal Process A student denied financial aid based on the satisfactory academic progress policy may submit a written appeal through Purdue’s verification portal.”
  - sentence: sap_appeal ⟵ “Students must submit their completed SAP appeal and all documentation by the following deadline of the applicable term for the SAP appeal: For Summer Terms: July 15th For Fall Terms: November 15th For Spring Terms: April 15th *If this date falls on a weekend, the deadline is end of business on the first business day after it.”
### `63a7070079e23d28` Purdue University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.purdue.edu/cost-financial-aid/scholarships/ (sha256 90c2ab2c10ee)
- issues: semantic_review_required
- checks: {"negative_sentences": 1, "sentences": 1}
  - sentence: competing_offer_review ⟵ “Purdue does not match offers from other institutions and does not consider appeals for merit aid.”
### `6aa93d5a65e1c292` Purdue University-Main Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/contact/policiesappeals/ (sha256 23e0e70a3751)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Students must participate in a homeless youth determination interview or complete the Dependency Status Appeal (DSA) process for a final determination of dependency.”
### `b947e1af00bfecf3` Purdue University-Main Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/contact/policiesappeals/ (sha256 23e0e70a3751)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: budget_increase ⟵ “Budget Adjustment The Division of Financial Aid (DFA) calculates an estimated Cost of Attendance (COA), or budget, for financial aid applicants based on federal guidelines.”
  - sentence: budget_increase ⟵ “We cannot consider the following types of expenses: Those incurred or paid by roommates Those incurred for spouses, children or other family members Car payments or credit card payments Expenses incurred outside of the current enrollment period Medical expenses Timeframes Summer Budget Adjustment Appeals will be available in May and should be submitted 3 weeks prior to your last day of summer enro”
  - sentence: budget_increase ⟵ “Academic Year Budget Adjustment Appeals will be available in July.”
  - sentence: budget_increase ⟵ “For fall-only enrollment, Budget Adjustment Appeals should be submitted by the third Friday in November to ensure adequate time to process additional financial aid.”
  - sentence: budget_increase ⟵ “For spring-only or academic year enrollment, Budget Adjustments Appeals should be submitted by the first Friday in April to ensure adequate time to process additional financial aid.”
  - sentence: budget_increase ⟵ “Important Notes All expenses submitted for a Budget Adjustment Appeal must be incurred and paid during your enrollment period.”
### `e45654a862765aaa` Purdue University-Main Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.purdue.edu/dfa/contact/policiesappeals/ (sha256 23e0e70a3751)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: need_based_special_circumstances ⟵ “Provisionally Independent Students who indicate that they have other circumstances or unusual circumstances on the FAFSA will be considered provisionally independent.”
  - sentence: need_based_special_circumstances ⟵ “Student Unusual Circumstances Students may be considered independent if a financial aid administrator determines and documents the student’s independent status based on unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances may include: Leaving home due to an abusive or threatening environment.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances DO NOT include: Parents refuse to contribute to the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “If a student has unusual circumstances and did not answer “Yes” to question 7 on the FAFSA, they may still appeal dependency status.”
  - sentence: need_based_special_circumstances ⟵ “Students with unusual circumstances should contact a Division of Financial Aid (DFA) counselor at (765) 494-5050 to discuss their unusual circumstance and the dependency status appeal (DSA) process, how to obtain an appeal form, and what documentation to provide based on their circumstances.”
### `673e64e9636e78af` Purdue University-Main Campus — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2025-2026/purdue-university-in-indianapolis-undergraduate-2025-2026/ (sha256 c82c12f163e3)
- issues: residency_unknown, stale_year_label:2025-26, conflicting_sources:https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2025-2026/undergraduate-tuition-and-fees-2025-2026/
- checks: {"columns": 1, "rows": 4}
  - column:Tuition*: 28794.0 ⟵ “Tuition* | $ 14,397.00 | $ 28,794.00”
  - column:1Engineering Differential 2Science Differential: 2050.0 ⟵ “1Engineering Differential 2Science Differential | $ 1,025.00 | $ 2,050.00”
  - column:International Fee: 3310.0 ⟵ “International Fee | $ 1,655.00 | $ 3,310.00”
  - column:Sub-Total Tuition:: 34154.0 ⟵ “Sub-Total Tuition: | $ 17,077.00 | $ 34,154.00”
### `894046dee7155c35` Purdue University-Main Campus — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2025-2026/undergraduate-tuition-and-fees-2025-2026/ (sha256 8e9e899b07f7)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26, conflicting_sources:https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2025-2026/purdue-university-in-indianapolis-undergraduate-2025-2026/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:General Service: 2429.5 ⟵ “General Service | $ 2,429.50 | $ 347.85”
  - column:Student Fitness and Wellness Fee3: 58.5 ⟵ “Student Fitness and Wellness Fee3 | $ 58.50 | $ 0.00”
  - column:Student Activity Fee 3: 10.0 ⟵ “Student Activity Fee 3 | $ 10.00 | $ 0.00”
  - column:Nonresident Tuition: 4700.5 ⟵ “Nonresident Tuition | $ 4,700.50 | $ 600.45”
  - column:International Student Tuition: 827.5 ⟵ “International Student Tuition | $ 827.50 | $ 110.00”
  - column:Total Tuition:: 8026.0 ⟵ “Total Tuition: | $ 8,026.00 | $ 1,058.30”
  - column:General Service: 347.85 ⟵ “General Service | $ 2,429.50 | $ 347.85”
  - column:Student Fitness and Wellness Fee3: 0.0 ⟵ “Student Fitness and Wellness Fee3 | $ 58.50 | $ 0.00”
  - column:Student Activity Fee 3: 0.0 ⟵ “Student Activity Fee 3 | $ 10.00 | $ 0.00”
  - column:Nonresident Tuition: 600.45 ⟵ “Nonresident Tuition | $ 4,700.50 | $ 600.45”
  - column:International Student Tuition: 110.0 ⟵ “International Student Tuition | $ 827.50 | $ 110.00”
  - column:Total Tuition:: 1058.3 ⟵ “Total Tuition: | $ 8,026.00 | $ 1,058.30”
### `b6dda991e4163886` Purdue University-Main Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/purdue-university-in-indianapolis-undergraduate-2026-2027/ (sha256 243145933279)
- issues: residency_unknown, conflicting_sources:https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/undergraduate-tuition-and-fees-2026-2027/
- checks: {"columns": 1, "rows": 6}
  - column:General Service: 9718.0 ⟵ “General Service | $ 4,859.00 | $ 9,718.00”
  - column:Student Activity Fee 3: 40.0 ⟵ “Student Activity Fee 3 | $ 20.00 | $ 40.00”
  - column:Nonresident Tuition: 18802.0 ⟵ “Nonresident Tuition | $ 9,401.00 | $ 18,802.00”
  - column:Differential General Service4,5,6: 4050.0 ⟵ “Differential General Service4,5,6 | $ 2,025.00 | $ 4,050.00”
  - column:International Fee: 3310.0 ⟵ “International Fee | $ 1,655.00 | $ 3,310.00”
  - column:Sub-Total Tuition:: 35920.0 ⟵ “Sub-Total Tuition: | $ 17,960.00 | $ 35,920.00”
### `e5201a23a1c564da` Purdue University-Main Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/undergraduate-tuition-and-fees-2026-2027/ (sha256 193af0db1fe4)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.purdue.edu/treasurer/finance/bursar-office/tuition/fee-rates-2026-2027/purdue-university-in-indianapolis-undergraduate-2026-2027/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:General Service: 2429.5 ⟵ “General Service | $ 2,429.50 | $ 347.85”
  - column:Student Fitness and Wellness Fee 3: 58.5 ⟵ “Student Fitness and Wellness Fee 3 | $ 58.50 | $ 0.00”
  - column:Student Activity Fee 3: 10.0 ⟵ “Student Activity Fee 3 | $ 10.00 | $ 0.00”
  - column:Nonresident Tuition: 4700.5 ⟵ “Nonresident Tuition | $ 4,700.50 | $ 600.45”
  - column:International Student Tuition: 827.5 ⟵ “International Student Tuition | $ 827.50 | $ 110.00”
  - column:Total Tuition:: 8026.0 ⟵ “Total Tuition: | $ 8,026.00 | $ 1,058.30”
  - column:General Service: 347.85 ⟵ “General Service | $ 2,429.50 | $ 347.85”
  - column:Student Fitness and Wellness Fee 3: 0.0 ⟵ “Student Fitness and Wellness Fee 3 | $ 58.50 | $ 0.00”
  - column:Student Activity Fee 3: 0.0 ⟵ “Student Activity Fee 3 | $ 10.00 | $ 0.00”
  - column:Nonresident Tuition: 600.45 ⟵ “Nonresident Tuition | $ 4,700.50 | $ 600.45”
  - column:International Student Tuition: 110.0 ⟵ “International Student Tuition | $ 827.50 | $ 110.00”
  - column:Total Tuition:: 1058.3 ⟵ “Total Tuition: | $ 8,026.00 | $ 1,058.30”
### `7bbe76f01a8dabfc` Vincennes University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.vinu.edu/financial-services/financial-aid.html (sha256 634ce66d7eb8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “FAFSA Information FAFSA Information | Category | Topic | Definition | FAFSA Information | FAFSA | The FAFSA (Free Application for Federal Student Aid) must be filed annually to determine a student's eligibility for federal financial aid and state grants, additional data can be found here. | Special & Unusual Circumstances | A Special Circumstance is when a student or their family's financial situa”
  - sentence: need_based_special_circumstances ⟵ “An Unusual Circumstance is a unique situation, such as parental abandonment or human trafficking, that impacts a dependent student's dependency status on the FAFSA, requiring them to either request a change in status, add parent information, or opt for a Parent Disavowal of Support to be eligible for aid. | Verification | Sometimes the FAFSA system selects students for a verification process, whic”

## Re-verification of existing records (60)

- source_not_fetched: data/institutions/betheluniversity/credit_policies/2026-27.json ["credit_policies", "ipeds-150145", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/butler/credit_policies/2026-27.json ["credit_policies", "ipeds-150163", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/butler/credit_policies/2026-27.json ["credit_policies", "ipeds-150163", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/ccsj/transfer_policies/2026-27.json ["transfer_policies", "ipeds-150172", null, "2026-27", {}]
- source_not_fetched: data/institutions/earlham/transfer_policies/2026-27.json ["transfer_policies", "ipeds-150455", null, "2026-27", {}]
- source_not_fetched: data/institutions/grace/awards/2026-27.json ["awards", "ipeds-150677", null, "2026-27", {"award_name": "Provost's Scholarship"}]
- source_not_fetched: data/institutions/grace/awards/2026-27.json ["awards", "ipeds-150677", null, "2026-27", {"award_name": "Dean's Scholarship"}]
- source_not_fetched: data/institutions/grace/awards/2026-27.json ["awards", "ipeds-150677", null, "2026-27", {"award_name": "Honors Scholarship"}]
- source_not_fetched: data/institutions/grace/awards/2026-27.json ["awards", "ipeds-150677", null, "2026-27", {"award_name": "Achievement Scholarship"}]
- source_not_fetched: data/institutions/huntington/transfer_policies/2026-27.json ["transfer_policies", "ipeds-150941", null, "2026-27", {}]
- source_not_fetched: data/institutions/east/credit_policies/2026-27.json ["credit_policies", "ipeds-151388", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/east/credit_policies/2026-27.json ["credit_policies", "ipeds-151388", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/east/credit_policies/2026-27.json ["credit_policies", "ipeds-151388", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/east/transfer_policies/2026-27.json ["transfer_policies", "ipeds-151388", null, "2026-27", {}]
- source_not_fetched: data/institutions/iuk/credit_policies/2026-27.json ["credit_policies", "ipeds-151333", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/iuk/credit_policies/2026-27.json ["credit_policies", "ipeds-151333", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/iuk/credit_policies/2026-27.json ["credit_policies", "ipeds-151333", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/iuk/credit_policies/2026-27.json ["credit_policies", "ipeds-151333", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/iuk/transfer_policies/2026-27.json ["transfer_policies", "ipeds-151333", null, "2026-27", {}]
- source_not_fetched: data/institutions/iusb/credit_policies/2026-27.json ["credit_policies", "ipeds-151342", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/iusb/credit_policies/2026-27.json ["credit_policies", "ipeds-151342", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/iusb/transfer_policies/2026-27.json ["transfer_policies", "ipeds-151342", null, "2026-27", {}]
- source_not_fetched: data/institutions/ivytech/transfer_policies/2026-27.json ["transfer_policies", "ipeds-150987", null, "2026-27", {}]
- source_not_fetched: data/institutions/manchester/awards/2026-27.json ["awards", "ipeds-151777", null, "2026-27", {"award_name": "Earning Merit-Based Academic Scholarships at Manchester University"}]
- source_not_fetched: data/institutions/manchester/credit_policies/2026-27.json ["credit_policies", "ipeds-151777", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/mid-america/credit_policies/2026-27.json ["credit_policies", "ipeds-151962", null, "2026-27", {"policy_kind": "AP"}]
- nothing_to_check: data/institutions/purdueglobal/degree_requirements/2026-27.json ["degree_requirements", "ipeds-489779", null, "2026-27", {"program_key": "bachelor-of-science-in-cloud-computing-and-solutions", "requirement_key": "program-requirements-major-requirements"}] year=2026-27
- nothing_to_check: data/institutions/purdueglobal/degree_requirements/2026-27.json ["degree_requirements", "ipeds-489779", null, "2026-27", {"program_key": "associate-of-applied-science-in-information-technology", "requirement_key": "program-requirements-major-requirements"}] year=2026-27
- nothing_to_check: data/institutions/purdueglobal/degree_requirements/2026-27.json ["degree_requirements", "ipeds-489779", null, "2026-27", {"program_key": "associate-of-applied-science-in-health-science", "requirement_key": "preprofessional"}] year=2026-27
- nothing_to_check: data/institutions/purdueglobal/degree_requirements/2026-27.json ["degree_requirements", "ipeds-489779", null, "2026-27", {"program_key": "associate-of-science-in-health-science", "requirement_key": "preprofessional"}] year=2026-27
- nothing_to_check: data/institutions/purdueglobal/transfer_policies/2026-27.json ["transfer_policies", "ipeds-489779", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/purdue/credit_policies/2026-27.json ["credit_policies", "ipeds-243780", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/purdue/transfer_policies/2026-27.json ["transfer_policies", "ipeds-243780", null, "2026-27", {}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-concentration-bachelor-of-arts", "requirement_key": "major-requirements-42-hours-studio-electives"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-concentration-bachelor-of-arts", "requirement_key": "major-requirements-42-hours-electives"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-concentration-bachelor-of-fine-arts", "requirement_key": "major-requirements-78-hours-studio-electives"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-concentration-bachelor-of-fine-arts", "requirement_key": "major-requirements-78-hours-electives"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-concentration-bachelor-of-fine-arts", "requirement_key": "major-requirements-78-hours-correlate-courses"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-and-art-history-double-concentration-bachelor-of-arts", "requirement_key": "major-requirements-66-hours-studio-electives"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-and-art-history-double-concentration-bachelor-of-arts", "requirement_key": "major-requirements-66-hours-electives"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-and-art-history-double-concentration-bachelor-of-arts", "requirement_key": "major-requirements-66-hours-upper-level-art-history-electives"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-and-art-history-double-concentration-bachelor-of-arts", "requirement_key": "major-requirements-66-hours-ancient-medieval"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-and-art-history-double-concentration-bachelor-of-arts", "requirement_key": "major-requirements-66-hours-eighteenth-nineteenth-century"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-and-art-history-double-concentration-bachelor-of-arts", "requirement_key": "major-requirements-66-hours-twentieth-century"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-and-art-history-double-concentration-bachelor-of-arts", "requirement_key": "major-requirements-66-hours-contemporary"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "studio-art-and-art-history-double-concentration-bachelor-of-arts", "requirement_key": "major-requirements-66-hours-non-western-underrepresented-traditions"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "ecology-evolution-and-environmental-biology-concentration-bachelor-of-science", "requirement_key": "major-requirements-60-hours-one-of-the-following-to-fulfill-upper-level-research"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "exercise-science-health-and-fitness-bachelor-of-arts", "requirement_key": "exercise-science-health-and-fitness-bachelor-of-arts-exhf-supporting-required-2"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "accounting-bachelor-of-business-administration", "requirement_key": "major-requirements-63-hours-required"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "economics-bachelor-of-arts", "requirement_key": "major-requirements-34-hours-required"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "physics-bachelor-of-arts", "requirement_key": "major-requirements-38-42-hours-required"}]
- source_not_fetched: data/institutions/saintmarys/degree_requirements/2026-27.json ["degree_requirements", "ipeds-152390", null, "2026-27", {"program_key": "physics-bachelor-of-science", "requirement_key": "major-requirements-61-hours-required"}]
- source_not_fetched: data/institutions/saintmarys/transfer_policies/2026-27.json ["transfer_policies", "ipeds-152390", null, "2026-27", {}]
- source_not_fetched: data/institutions/taylor/credit_policies/2026-27.json ["credit_policies", "ipeds-152530", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/evansville/credit_policies/2026-27.json ["credit_policies", "ipeds-150534", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/evansville/credit_policies/2026-27.json ["credit_policies", "ipeds-150534", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/sf/credit_policies/2026-27.json ["credit_policies", "ipeds-152336", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/sf/transfer_policies/2026-27.json ["transfer_policies", "ipeds-152336", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/vinu/credit_policies/2026-27.json ["credit_policies", "ipeds-152637", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/wabash/transfer_policies/2026-27.json ["transfer_policies", "ipeds-152673", null, "2026-27", {}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Ball State University: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Indiana University-Bloomington: cost_of_attendance, merit_scholarships
- Indiana University-Indianapolis: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- Purdue University Global: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, aid_appeals
- Purdue University-Main Campus: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Vincennes University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
