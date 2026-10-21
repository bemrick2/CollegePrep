# Research checkpoint

This file is how a new Research session resumes the national program-research workstream without redoing finished work. It is updated with every batch PR.

- **Main at the last refresh:** `b30d6765b7` (after #216, #223 and Deep Dive's #225 UNL/Utah readers).
- **Branch carrying this checkpoint:** `research/batch-05`.
- **Ranking:** `docs/coverage/research_priority.json`, written by `python3 scripts/research_priority.py`. CI (validate-data) checks that it is current.

## Numbers

Three separate measures, never mixed: **program coverage** (bachelor's programs listed in the official catalog, docs/PROGRAM_DEPTH_COMPLETION.md), **degree-requirement depth** (requirement groups and plans of verified bachelor's programs) and **reference-data breadth** (costs, aid, admissions and the other domains in docs/coverage/coverage.json).

| | main `b30d676` | research/batch-05 |
|---|---|---|
| Registered four-year institutions | 2,119 | 2,119 |
| Covered (program coverage) | 65 | 66 |
| Researched | 673 | 675 |
| Verified bachelor's program records | 10,320 | 10,341 |

All figures are counted from `docs/coverage/programs/STATUS.json` and from the `academic_programs` files with `verification_status == "verified"` and `credential_level == "bachelor"`. The batch-05 change is -4 (corrections below) +25 (ODU); main's 10,320 includes Deep Dive's UNL and Utah records (#225).

## Completed in batch 5 (research/batch-05)

**Integrity corrections (owner-approved 2026-10-21).** Each record keeps its evidence and requirement rows, is `unverified` with a `verification_correction_reason`, has the correction appended to its notes, and is listed in `supabase/corrections.json` with the owner's instruction quoted.
- Roosevelt: 'Digital Marketing, Advertising and Public Relations, BA to Marketing Communications, MSIMC' and 'Health Science Administration, BA/MPA Public Administration' are accelerated bachelor's-to-master's pathways (stored pages filed under 'Accelerated'); both bachelor's degrees are recorded separately. 74/79, still covered.
- SF State: 'Ethnic Studies, BA' and 'Criminal Justice Studies, BA' took their names from list lines that link the extended-learning BA pages; the pages cited are department overviews. 108/118, still covered.
- `programs/status.py`: `requirement_groups` now counts only groups of verified bachelor's programs (47 of 14,128 verified major groups belonged to associate degrees or the removed pathways; no school's dimension changed).

| Institution | Run | Result |
|---|---|---|
| ODU | VA/2026-10-06-cl (re-extracted) | 180/186, **covered**. 25 majors from pages titled 'X with a Major in Y (BSBA)' (also BSET, BSHS, BSPH, BSCS, BSDH, BSMLS) are now read. Seven programs reviewed 2026-10-08 keep their records. Not recorded: Chemistry Pre-Med (page not fetched), Cybersecurity AI (title prints no award), Music Sound Recording Technology emphasis, two Nursing BSN tracks (department-section records collide), HSA (Professional) BSPH (held as a name variant of the HSA BSPH program, '(Professional)' qualifier; listed separately, so counted and unrecorded). The re-extraction also added verified requirement rows for about 12 programs already on file (ODU: 96 to 148 requirement groups). The count is reproducible with `python3 -m programs.catalog_counts --run programs/runs/VA/2026-10-06-cl --on-file odu ...`. |
| UTC (TN pilot, #191) | pipeline TN/2026-10-21 | IB table re-read: level and printed scores in `minimum_score` ('HL 5,6, OR 7'), still partially verified (no year printed). CR-17 billing basis answered on #191 from the FY 2026-2027 bursar fee schedule (by credit hour to 11 hours, one '12+' row; per-credit differential fees). AP/CLEP/IB pages and renewable awards re-read: still no printed year. |

Reader changes (each with tests and mutants): `pipeline/extractors/catalog.py` (a parenthesized undotted award ends a bachelor's name), `programs/catalog_counts.py` (list rows that run the award on to filter labels; 'BS-MBA' combined; NROTC), `pipeline/extractors/credit.py` (an IB 'Levels Offered' column is not the score column).

**Near-tier recounts not adopted.** Recounting CU Denver, JHU, ESU, YSU, Ashland, Johnstown, La Salle and Greensburg under `catalog_counts` gave lower, less accurate counts than their reviewed entries: those lists print tracks as 'Base - X Track, BS', rural-partnership variants, spelled-out 'Bachelor of Arts/Master of Arts' combined entries and Peabody's instrument curricula. The reviewed entries stand. ESU's missing entries are Kuali pages that print no year; JHU's are the BM in Performance instrument curricula (all titled 'Bachelor of Music in Performance').

**Catalog discovery (diagnose runs `program-run/*-diag-2026-10-21`, search-surfaced URLs only):**
- SNHU: www.snhu.edu/admission/academic-catalogs embeds a Kuali catalog (snhu.kuali.co, catalogId 69e917a2592741290eff3c61). Configured as a rendered Kuali catalog; run `program-run/nh-k01-2026-10-21` keeps the page's own feed.
- Lone Star: www.lonestar.edu/catalog/ is a JavaScript catalog (hash routes); the 2019-20 PDF configuration is superseded. Run `program-run/tx-k01-2026-10-21`.
- ASU: degrees.asu.edu/curriculum lists every bachelor's plan (/bachelors/major/ASU00/<code>) with its latest major map year ('2026 - 2027'). Round 2 (`program-run/az-diag2-2026-10-21`) fetches a major page and its map.
- Michigan State: reg.msu.edu Academic Programs links 'Undergraduate Degrees' (Programs.aspx?PType=UGRD); fee sections print '2026-27'. Round 2 fetches the degree list.
- Indiana: separate 2026-2027 school bulletins on three hosts; queued `layout_not_readable` with every bulletin URL.
- Ohio State: no current catalog surfaced; cse.osu.edu answered 403. Cincinnati: only a 2025-2026 program catalog PDF (queued `not_published`).

## Completed in batch 4 (research/batch-04, merged as #215)

| Institution | Run | Result |
|---|---|---|
| Roosevelt | IL/2026-10-08-e01 | 74/79, covered again. The re-run read the undotted-award programs. The two combined BA/MPA and BA-to-MSIMC records from pipeline run IL/2026-10-05 were corrected in batch 5. |
| UT Dallas | TX/2026-10-08-b02 (re-extracted) | 64 verified records; no list count. New `edition_year_from_home` / `edition_program/v1`: pages print only the edition name '2026 Undergraduate Catalog', so the year is quoted from the edition home page. All 87 candidates were checked; double majors are held. Not yet recorded: Mechanical Engineering BS (heading too deep) and Visual and Performing Arts BA (concentration pages only); the seven Education certification focuses are two degrees. |

## Completed in batch 3 (research/batch-03, merged as #214)

| Institution | Run | Result |
|---|---|---|
| Colorado State | CO/2026-10-08-c02 | 68 verified records; no completeness count yet. New reader `award_link_major/v1` reads 'Major in X' pages that the Programs A-Z degree column links as 'B.A.' / 'B.S.'; all 60 first-extraction records were checked against the table rows. The table links concentrations and dual degrees by award only, so the count waits for a reader of its program column (queued). |
| SF State | recount of CA/2026-10-07-cat | 108/118, covered. Options of a listed degree are not counted. Nursing (Accelerated-Prelicensure) is no longer credited through another program's record. No record changed. |
| Roosevelt | recount of IL/2026-10-07-cat | 56/79, **no longer covered**. 18 undotted-award entries (BSBA, BAE, BMA, BSHTM, BAOL) had been left out of the 10-07 count. A re-run is in flight. |
| UTRGV | TX/2026-10-08-d03 | Queued `no_year_label`: the SmartCatalog pages print no catalog year. |

**Recount check.** Every covered school whose entry follows the `catalog_counts` format was recounted from stored runs with the current readers. All stay at or above 90% except Roosevelt. Recount decisions (`*-recount.json`) approve nothing. They map approvals that the current reader re-identifies on the same page, for counting only.

## Completed in batch 2 (research/batch-02, merged as #213)

| Institution | Run | Result |
|---|---|---|
| Oklahoma State | OK/2026-10-08-r2 | 170/184, covered. Re-run with a 900-page cap, superseding b01. Undotted awards (BSBA, BSCH, BSET, BPS, ...) are read in list entries and page names. |
| Missouri | MO/2026-10-08-r2 | 97/100, covered. Re-run with an 800-page cap, superseding b02. Pages named 'BSAcc in Accountancy' and 'BHS in ...' are read. |
| UIC | IL/2026-10-08-b04 | 95/128, partial. The walk starts at /ucat/colleges-depts/. |
| BYU | UT/2026-10-08-b03 | 118/169, partial (secondary majors listed but not counted). New reader `kuali_page/v1` for pages titled '<code> Program'; the year comes from the site header 'Undergraduate Catalog' / 'BYU' / '2026-2027'. |

Blockers queued in batch 2:
- **bot challenge:** Pitt; State College of Florida.
- **robots.txt unreachable:** Weber; Ole Miss.
- **Coursedog 401, no year label:** Ensign; K-State.
- **layout not readable:**
  - UWM; SHSU.
  - Colorado State and UNL: major pages print no award in the heading.
  - Utah: titles print only the field.

## Completed in batch 1 (research/batch-01, merged as #211)

| Institution | Run | Result |
|---|---|---|
| Oklahoma State | OK/2026-10-08-b01 | 127/184, partial. The 2026-2027 catalog had been misread as 2025-26 because of the print link 'Full 2025-2026 Catalog'. Options printed as 'Major: Option, AWARD' beside their major are held and not counted. The run hit the 450-page cap before reaching most BSBA/BSET/engineering pages; a re-run with a 900-page cap is in flight. |
| Missouri | MO/2026-10-08-b02 | 86/99, partial. Award-only entries ('BA', 'BS*', 'BSAcc') are identified by their own page. The entries whose awards the list reader missed were never crawled; a re-run with an 800-page cap is in flight. |
| UTEP | TX/2026-10-08-b04 | 83/87, covered. List cards run the name or award on to category labels. |
| Georgia Tech | GA/2026-10-08-b03 | 41/42, covered. Thread and concentration pages are variants of the degree's page. Electrical Engineering is held because of a misspelled thread URL (queued). |
| VCU | VA/2026-10-08-b02 | 120 verified records (#209's 57 kept as on main, b02 adds 63); 120/151 listed (A-Z list /azprograms/, fetched under robots; #210's robots_disallowed entry for /azindex/ is superseded). Concentration lines with no degree line are read as the degree. |
| UTSA | TX/2026-10-08-b03 | 82 degree sections. The '2026-28 Undergraduate Catalog' period label is kept. There is no program list page, so no completeness count (queued). |

Reader and checker changes in this batch each come with tests and mutants: `programs/extract.py`, `programs/catalog_counts.py`, `programs/autoreview.py`, `pipeline/extractors/catalog.py` and `pipeline/extractors/common.py`.

## Unresolved (queued in programs/queue; the reason is in each entry)

- **bot_challenge (never evaded):** LSU, UKY, plus the earlier set (Purdue, Kennesaw, Dallas College, HCC, Michigan, Texas Tech, UNT and others).
- **fetch_failed (robots.txt unreachable):** UConn, Montclair, UH, CSU Fullerton (also Virginia Tech, earlier).
- **no_year_label (a year is never inferred):**
  - Coursedog catalogs whose API answered 401: Arizona, UCSB, Illinois State, USU, FIU. CSUN: its pages print no year label.
  - Alabama: the only label printed is the print-menu link 'Download 2026-27 Undergraduate PDF'. This is a shared reader request.
- **layout_not_readable:** UNL, Utah, SHSU, UWM and UCR (Deep Dive took these readers on #153, 2026-10-21); Indiana (separate school bulletins).
- **not_published:** Cincinnati (only a 2025-2026 program catalog PDF).
- **Stale configured catalogs (find the 2026-27 catalog by web search before running):**
  - CSULB (2015-16 PDF)
  - UNM (2009-10 PDF)
  - Modesto JC (2020-21 PDF)
  - St. Petersburg College (2025-26 PDF)
- **Pending owner decision:** the UTK downgrade of 7 records (#191, #218 C4).
- **TN pilot (#191):** UTC AP/CLEP/IB tables and renewable awards print no year (partially verified); CR-19 applicability not published; Entrepreneurship and Economics: International Public Policy plan rows are truncated in the source PDF text itself.

## Known reader limits

- `UNDOTTED_LIST_AWARD` reads UMD's 'SDSB - Social Data Science, BSOS' (a college code) as a bachelor's entry; review such entries by hand.

## In flight

- `program-run/nh-k02-2026-10-21` (SNHU) and `program-run/tx-k02-2026-10-21` (Lone Star): rendered Kuali/JavaScript catalogs (k01 was requested with `adapters_only`, which crawls only state adapters, and fetched nothing). Next: read the kept catalog feeds (a Kuali feed reader is needed; `programs/feeds.py` already requests the public program list) and check that the catalog title prints the year.
- Discovery: `program-run/az-diag3-2026-10-21` (ASU checksheet and major map, MSU program detail, IU College majors, Kelley degree page) and `program-run/fl-diag4-2026-10-21` (UCF, UW, UGA, FSU catalog pages).
- Round 2 found: MSU's 'Undergraduate Degrees' list prints 185 entries such as 'Accounting (BS)' (ProgramDetail.aspx?PType=UGRD&Program=ACCOUN_BS1); ASU's degree pages print 'Accountancy, BS' but no year, and link a 2026 curriculum checksheet and major maps; IU's College bulletin prints 'Bulletin Year 2026-27'.

## Next prioritized batch

1. **Kuali feed reader** (SNHU, Lone Star; also Vanderbilt in TN): program identity from the catalog's public program list, the year from the catalog's own title, never inferred.
2. **ASU and Michigan State** once round 2 shows their program pages: configure, run, review.
3. **Near tier:** ESU (Kuali pages without a year: read the Kuali feed), JHU (decide whether the BM in Performance instrument curricula are listed programs), CU Denver, YSU.
4. **Reader work kept by Research:**
   - Colorado State program column: the Programs A-Z table (Program | Department | College | Level | Campus | Degree type) gives about 85 bachelor's programs (69 plain majors, plus majors listed only as 'Major, X Concentration' rows); 66 match the 68 records by name. Implement as a table count.
   - BYU emphases: all 51 unrecorded entries are emphases of 13 degrees that have no line of their own ('Statistics (BS): Data Science Emphasis'). Counting such a degree once would put BYU at about 118/131, but the same rule would regroup 92 OSU, 45 SF State, 43 UVU and 22 UNH entries that are credited one by one today, so it needs a recount of those schools and agreement with Deep Dive (UVU, UNH) first.
   - Alabama print-link label.
   - UT Dallas: the edition's program list (catalog.utdallas.edu/2026/undergraduate/programs) is configured; run `program-run/tx-u01-2026-10-21`.
   - UTSA: catalog.utsa.edu/undergraduate/azindex lists department pages, not degrees; no degree list found yet.
5. **Configured tier:** UT Austin and Texas State (coordinate with Deep Dive), Penn State, Illinois, UCI, UC Davis, Arkansas.
6. **Unconfigured tier:** UCF (www.ucf.edu/catalog/?catoid=12), Rutgers, Washington, UCSD (catalog.ucsd.edu/undergraduate/degrees-offered/), Minnesota (Coursedog), UGA, FSU, NAU, UMass.

## How to resume

1. `git fetch origin`. Read this file, then run `python3 scripts/research_priority.py --batch 25`.
2. Process the in-flight runs:
   - Fetch: `git fetch origin '+refs/heads/program-run/*:refs/remotes/origin/program-run/*'`.
   - Extract with `python -m programs extract`, then `python -m programs.verify`, then `python -m programs autoreview`.
   - Review the auto decision against the official program list.
   - Write the reviewed decision, deduplicated, with its catalog entries from `python3 -m programs.catalog_counts`.
   - Promote, then run `python3 scripts/retain_evidence.py --push`.
   - Regenerate `python -m programs status`, `scripts/update_coverage.py` and `scripts/research_priority.py`.
3. Queue every blocker in `programs/queue/<ST>.json` with its reason, detail and next action, then move to the next institution.
4. Open the batch PR, get an independent review, merge main, re-run checks, and merge on green CI. Update this file in the same PR.

Hosted imports and deployments stay on hold while Supabase is paused.
