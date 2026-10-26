# Plan re-read inventory (2026-10-23)

This file reconciles the plans on main `16ec809` with the plans re-read by the `programs/plan-notes` reader.

## Totals

- **On main `16ec809`:** 3,627 plan records: 3,221 verified and 406 partially verified.
- **Re-read: 3,512.** These are every plan whose evidence names a CourseLeaf plan reader (`courseleaf_plan/*`, `courseleaf_plangrid/v1`):
  - 2,588 read the same;
  - 339 gain only notes;
  - 295 change structurally;
  - 290 are held by the reader.
- **Not re-read: 115.** Their evidence names another reader, so the CourseLeaf reader cannot re-read them. They are listed below.

| Folder | Program key | Requirement key | Status | Reader | Evidence |
|---|---|---|---|---|---|
| eou | agriculture-entrepreneurship-major | agriculture-entrepreneurship-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#d10005e6560296e7 |
| eou | agriculture-entrepreneurship-major-bas | agriculture-entrepreneurship-bas-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#773bbb4ad437fe2b |
| eou | art-major | art-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#93ae190a43a9fd5b |
| eou | business-administration-major | business-administration-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#15eb1c303c26509c |
| eou | computer-science-major | computer-science-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#417c3e90d1021378 |
| eou | cyber-security-major | cyber-security-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#f26ca3883b9ba10a |
| eou | early-childhood-education-major | early-childhood-education-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#f998578c3778b3f8 |
| eou | emergency-medical-services-administration-major | emergency-medical-services-administration-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#ec030688cea80515 |
| eou | english-writing-major | english-writing-typical-four-year-curriculum-on-campus | verified | acalog_plan/v1 | OR/2026-10-05-b#d5694a397fa3d5dc |
| eou | english-writing-major | english-writing-typical-four-year-curriculum-online | verified | acalog_plan/v1 | OR/2026-10-05-b#03c601948db96601 |
| eou | fire-services-administration-major | fire-services-administration-typical-four-year-curriculum | partially_verified | acalog_plan/v1 | OR/2026-10-05-b#60f947d41aa83619 |
| eou | history-major | history-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#f8ac970e4e6fb78a |
| eou | information-technology-management-major | information-technology-management-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#76be458fbdd27c93 |
| eou | marketing-major | marketing-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#7e62069059df87c5 |
| eou | multidisciplinary-studies-major | multidisciplinary-studies-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#8d7beddde9b60457 |
| eou | music-major | music-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#f1276a7fa0c2677c |
| eou | theatre-major | theatre-design-and-production-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#7f2673ea7721f3ad |
| eou | theatre-major | theatre-general-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#cdd83a560de8a215 |
| eou | theatre-major | theatre-musical-theatre-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#c5107500f144d329 |
| eou | theatre-major | theatre-performance-and-directing-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#331fdbd1a385dd94 |
| eou | theatre-major | theatre-playwriting-and-dramaturgy-typical-four-year-curriculum | verified | acalog_plan/v1 | OR/2026-10-05-b#c942109c0330f609 |
| pdx | artificial-intelligence-b-s | recommended-sequence | verified | smartcatalog_program/v1 | OR/2026-10-05-b#000449454712aa95 |
| pdx | civil-engineering-b-s-bsce | recommended-sequence | verified | smartcatalog_program/v1 | OR/2026-10-05-b#66b943f2f22215ca |
| pdx | computer-engineering-b-s | recommended-sequence | verified | smartcatalog_program/v1 | OR/2026-10-05-b#39cec83b4e193f60 |
| pdx | computer-science-b-s | recommended-sequence | verified | smartcatalog_program/v1 | OR/2026-10-05-b#830ad09e980f690b |
| pdx | electrical-engineering-b-s | recommended-sequence | verified | smartcatalog_program/v1 | OR/2026-10-05-b#599d1f338c3d6657 |
| pdx | environmental-engineering-b-s-bsenve | recommended-sequence | verified | smartcatalog_program/v1 | OR/2026-10-05-b#5ad6cd4fa7b058da |
| pdx | mechanical-engineering-b-s | recommended-sequence | partially_verified | smartcatalog_program/v1 | OR/2026-10-05-b#c7cf87104f169bdb |
| utc | accounting-b-s-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#609db2d2495172c7 |
| utc | art-art-education-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#6f415e95ec022250 |
| utc | art-art-history-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#2d71dd7ea206df7b |
| utc | art-art-studio-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#c9499389bafce407 |
| utc | biology-general-biology-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#88d9d55ec35106e4 |
| utc | biology-preprofessional-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#c6e6564a0b7a0332 |
| utc | biology-stem-education-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#33fe77dbf440983d |
| utc | business-analytics-b-s-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#5a38b3410210fe4d |
| utc | chemical-engineering-b-s-ch-e | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#94785f2777ea9b8f |
| utc | chemistry-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#0787e293a36eb055 |
| utc | chemistry-biochemistry-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#2454a4419f2c7640 |
| utc | chemistry-preprofessional-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#9df903a2478d5b42 |
| utc | communication-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#1abd4560318220df |
| utc | computer-science-data-science-ai-bs | four-year-plan | verified | pilot_hand_review | TN/2026-10-05-i-utc#696550d76980b52a |
| utc | criminal-justice-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#162c696445bf5746 |
| utc | economics-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#205e8ad70efb846e |
| utc | economics-financial-economics-b-s-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#9e9bf3a4e9ca9ff2 |
| utc | economics-international-public-policy-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#6894db4b880d6698 |
| utc | english-creative-writing-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#34bd83d42d50ea5c |
| utc | english-literary-studies-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#1784de1fb0151960 |
| utc | english-public-and-professional-writing-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#02e054205b566197 |
| utc | entrepreneurship-b-s-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#31170264011afc95 |
| utc | environmental-science-biodiversity-conservation-and-natural-resources-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#d46d4cf0a0725305 |
| utc | environmental-science-environmental-compliance-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#0d7c0af3815d158f |
| utc | environmental-science-environmental-policy-and-planning-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#0afe798bbf038e14 |
| utc | environmental-science-geographic-and-cartographic-sciences-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#a976bcffd1e14bdb |
| utc | environmental-science-wildlife-natural-resource-administration-and-enforcement-b | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#d54f1c46262aa1b5 |
| utc | finance-business-finance-b-s-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#5398a00e53d76942 |
| utc | finance-investments-b-s-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#229317c30258f8d8 |
| utc | geology-environmental-geology-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#8875d79ae2a04e1b |
| utc | geology-geology-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#47d8e767a78a6796 |
| utc | geology-geospatial-science-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#45c567e46902b93b |
| utc | geology-hydrogeology-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#a38c4505c8b8512e |
| utc | geology-stem-education-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#7dbef9d454e7382f |
| utc | hhp-health-and-physical-education-k-12-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#8597b3a6e54fc806 |
| utc | history-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#e0b26f8a9c35286e |
| utc | humanities-international-studies-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#2fbed937c411cdb1 |
| utc | humanities-liberal-arts-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#54a4e1ce48928e92 |
| utc | humanities-women-gender-and-sexuality-studies-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#3f621815bfb9a554 |
| utc | management-b-s-b-a | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#eb2fc06bbe27d50d |
| utc | management-healthcare-management-b-s-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#b37729fbc1e75e94 |
| utc | marketing-b-s-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#813adb0016d9d84a |
| utc | marketing-professional-sales-b-s-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#f4775600b9dfa5df |
| utc | mathematics-actuarial-science-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#7b763fbb6063f9c0 |
| utc | mathematics-general-mathematics-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#867b8e15938e6b45 |
| utc | mathematics-stem-education-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#71a19755969ac63a |
| utc | middle-grades-education-english-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#98423fed9f63db16 |
| utc | middle-grades-education-mathematics-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#377b8d1022a48594 |
| utc | middle-grades-education-natural-sciences-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#9423007e39d1507d |
| utc | middle-grades-education-social-sciences-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#c51355be69900a76 |
| utc | modern-and-classical-languages-and-literatures-classics-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#b932318d308f4cde |
| utc | modern-and-classical-languages-and-literatures-french-and-francophone-studies-b- | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#c8c24f95fdad4f51 |
| utc | modern-and-classical-languages-and-literatures-languages-and-linguistics-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#7883eef6cb4f6be3 |
| utc | modern-and-classical-languages-and-literatures-latin-american-studies-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#92ab5d21e35e737f |
| utc | modern-and-classical-languages-and-literatures-spanish-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#b4e86ef025a1ca0a |
| utc | modern-and-classical-languages-and-literatures-spanish-for-the-professions-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#5245ec2b7c34af4c |
| utc | music-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#d088c735d934b0ff |
| utc | music-composition-b-m | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#0a2484b9facd87c1 |
| utc | music-instrumental-music-education-b-m | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#3d019efb42634aa6 |
| utc | music-instrumental-performance-b-m | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#db65007666bb32af |
| utc | music-vocal-performance-b-m | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#10a346aa99cc2899 |
| utc | nursing-bsn | four-year-plan | verified | pilot_hand_review | TN/2026-10-05-i-utc#40858ba857beeb05 |
| utc | philosophy-and-religion-philosophy-and-religion-combined-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#35ade6b27f045ce5 |
| utc | philosophy-and-religion-pre-law-ethics-and-justice-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#b77aa16eb52d0b67 |
| utc | philosophy-and-religion-religious-studies-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#2ff31adc5e9ddec8 |
| utc | physics-biophysics-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#002d36195bc3aab2 |
| utc | physics-quantum-physics-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#e1e4b2a806984f13 |
| utc | physics-stem-education-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#07f4735f1ce1d7db |
| utc | political-science-american-politics-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#ec2fdee4e0e28baa |
| utc | political-science-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#7bf08bc4d069e95c |
| utc | political-science-international-relations-and-comparative-politics-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#5559367771396869 |
| utc | political-science-public-policy-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#22eca1116c7ee9e5 |
| utc | psychology-bs | four-year-plan | partially_verified | pilot_hand_review | TN/2026-10-05-i-utc#73c046febc0ee3cf |
| utc | secondary-education-economics-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#2e7b9c0f65217005 |
| utc | secondary-education-english-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#748e21041ff6834c |
| utc | secondary-education-geography-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#ea8a350f372a96ba |
| utc | secondary-education-history-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#54234ed0fe8bca43 |
| utc | secondary-education-political-science-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#ec16feeb0295b896 |
| utc | sociology-and-anthropology-anthropology-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#0fa2c2d884406b83 |
| utc | sociology-and-anthropology-anthropology-b-s | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#483da1f0fcb5b8a9 |
| utc | sociology-and-anthropology-sociology-b-s | clear-path-four-year-plan | verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#213469aed0fd5ebe |
| utc | theatre-acting-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#19cb823dc2b49054 |
| utc | theatre-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#e29229acc9b30942 |
| utc | theatre-design-technology-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#91f5f0d648de55e5 |
| utc | theatre-theatre-education-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#b1b40ea921e54df1 |
| utc | theatre-theatre-entrepreneurship-b-a | clear-path-four-year-plan | partially_verified | clearpath_plan/v1 | TN/2026-10-05-i-utc#5df0803214c1e467 |
| utk | computer-science-bs | computer-science-bs | verified | no evidence ref | – |

Not re-read, by reader and status: eou acalog_plan/v1 partially_verified: 1, eou acalog_plan/v1 verified: 20, pdx smartcatalog_program/v1 partially_verified: 1, pdx smartcatalog_program/v1 verified: 6, utc clearpath_plan/v1 partially_verified: 69, utc clearpath_plan/v1 verified: 14, utc pilot_hand_review partially_verified: 1, utc pilot_hand_review verified: 2, utk no evidence ref verified: 1.

## Held reasons

The 290 held plans carry 302 reason labels, because 12 plans have two reasons each:

| Reason | Plans |
|---|---|
| plan_note_unclear | 110 |
| footnotes_not_read | 99 |
| plan_heading_label | 62 |
| plan_key_shared_by_pages | 16 |
| plan_note_scope_unclear | 5 |
| unread_label_row | 4 |
| subtotal_spans_terms | 4 |
| verify_finding | 2 |

Plans with two reasons:

- `467d954689c2bfbf` (colorado): plan_heading_label, plan_note_scope_unclear
- `f05864d59ae5250d` (marshall): plan_note_unclear, subtotal_spans_terms
- `0b3880578166c45d` (marshall): plan_key_shared_by_pages, plan_note_unclear
- `6d3b1abaa384098e` (uakron): plan_note_unclear, unread_label_row
- `2a5cce4c38ec3be9` (umt): footnotes_not_read, plan_key_shared_by_pages
- `7c5363a51659f706` (umt): footnotes_not_read, plan_key_shared_by_pages
- `b6a23d04d69ad6e4` (umt): footnotes_not_read, plan_key_shared_by_pages
- `8960ed68c90bfe07` (unomaha): plan_note_scope_unclear, plan_note_unclear
- `4590e7ddb50a3a5f` (unomaha): plan_note_scope_unclear, plan_note_unclear
- `ffcb2264f6637835` (unomaha): plan_note_scope_unclear, plan_note_unclear
- `9998978af55cc61e` (unomaha): plan_note_scope_unclear, plan_note_unclear
- `8a42047fe6b3b5fd` (wit): plan_key_shared_by_pages, plan_note_unclear

## The 103 verified plans the reader held

An independent audit (2026-10-23) read each stored page. **All 103 are downgraded in this PR.** For each plan, the page prints material requirements or notes that the record does not store, and each correction reason quotes them.

- The 4 shared-key plans were resolved: each matches its own page's grid. They are still downgraded for uncaptured notes.
- The 4 scope-unclear plans print notes once, after the last of two plans.


## Unchanged plans are not proven complete

The 2,588 plans the new reader reads the same way keep their earlier review evidence; nothing in their records changes. A reader that finds no change does not establish that a plan is complete.

The audit above found material notes printed elsewhere on some pages: before the grid, and in notes that name plan rows outside the text after the grid. The reader does not look there. The next step is an independent sampled audit of these plans, school by school, that downgrades any plan whose page prints uncaptured material notes.

## UWM incomplete groups: 36 vs 37

The UWM review held 40 groups as incomplete sections (its category F):
- **36** carry the reviewer's generated reason, "its own rows/block match the print".
- **4** carry reasons written by hand. One of them, `6e45918d5ae6fbdf` (animation-arts-ba, "this choose-one block (9 options) matches the print, but the section is incomplete"), also states its own rows match the print.

That makes 37 accurate-but-incomplete groups, promoted as partially verified in #271. The other 3 hand-written ones remain held:
- `03cb0762f2168fe8`;
- `c26bbc60ae2077e8`;
- `9e2ba5c697f3c37e`.

Their reasons do not state that their own rows match the print.
