# Research checkpoint

This file is how a new Research session resumes the national program-research workstream without redoing finished work. It is updated with every batch PR.

- **Main at the last refresh:** `7451caf822e6f709da8a8fd9a136e2fc7c40823c` (merge of #213, batch 2).
- **Branch carrying this checkpoint:** `research/batch-03`.
- **Ranking:** `docs/coverage/research_priority.json`, written by `python3 scripts/research_priority.py`. CI (validate-data) checks that it is current.

## Numbers

| | main `7451caf` (batch 2 merged) | research/batch-03 |
|---|---|---|
| Registered four-year institutions | 2,119 | 2,119 |
| Covered (docs/PROGRAM_DEPTH_COMPLETION.md) | 64 | 65 |
| Researched | 672 | 673 |
| Verified bachelor's program records | 10,012 | 10,071 |

All figures are counted from `docs/coverage/programs/STATUS.json` and from the `academic_programs` files with `verification_status == "verified"` and `credential_level == "bachelor"`.

## Completed in batch 3 (research/batch-03)

| Institution | Run | Result |
|---|---|---|
| Colorado State | CO/2026-10-08-c02 | 63/68, covered. New reader `award_link_major/v1`: 'Major in X' pages that the Programs A-Z degree column links as 'B.A.' / 'B.S.' (20 of 60 records checked by hand). Concentration rows are not counted. |
| SF State | recount of CA/2026-10-07-cat | 108/118, covered. Options of a listed degree are not counted. No record changed. |
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
  - UT Dallas: pages print the edition name '2026 Undergraduate Catalog', and the edition's home page prints '2026-2027 Undergraduate Catalog'. Reader work for the Research session: read the year from the edition home page and cite that page.
- **layout_not_readable:** UCR (its catalog PDF gives no program records).
- **Stale configured catalogs (find the 2026-27 catalog by web search before running):**
  - Lone Star (2019-20 PDF)
  - Cincinnati (2025-26 PDF)
  - CSULB (2015-16 PDF)
  - UNM (2009-10 PDF)
  - Modesto JC (2020-21 PDF)
  - St. Petersburg College (2025-26 PDF)
- **Pending owner decision:** the UTK downgrade of 7 records (#191).

## Known reader limits

- `UNDOTTED_LIST_AWARD` reads UMD's 'SDSB - Social Data Science, BSOS' (a college code) as a bachelor's entry; review such entries by hand.

## In flight (run branches pushed, not yet reviewed)

- `program-run/il-e01-2026-10-08`: Roosevelt re-run (700-page cap) for its undotted-award programs.

## Next prioritized batch

From `research_priority.json`, excluding blocked institutions:

1. **Near tier** (catalog share 75-90%): ODU, CU Denver, JHU, ESU, YSU, Johnstown, Greensburg.
   - JHU's MD/2026-10-07-cat2 run no longer reproduces 17 approved candidates, so a recount there needs a fresh review.
   - Recounts under the current rules: ESU 65/75, Johnstown 41/48, Greensburg 28/32 (unchanged); YSU 54/75, Ashland 51/76, La Salle 35/56 (their undotted BSBA entries are now counted). Find which listed programs are unrecorded and why: held variants, unread pages, or a reader rule.
2. **Reader work that would unlock large schools:**
   - UNL: major pages with the award only in the text. The majors list prints no award.
   - Utah: the award from the program code or text.
   - UT Dallas: the edition-home year.
   - BYU: emphases whose degree has no list line.
3. **Configured tier, largest first:**
   - Stale catalogs first: Lone Star, Cincinnati.
   - UT Austin and Texas State: coordinate with Deep Dive before re-running.
   - Penn State, Illinois, UCI, UC Davis, Arkansas: configure each official list.
4. **Unconfigured tier, largest first:** SNHU, ASU, Indiana, Michigan State, Ohio State, UCF, Rutgers, Washington, UCSD, Minnesota, UGA, FSU, NAU, UMass.
   - Searches on 2026-10-08 did not surface a configurable current catalog for these. Leads:
     - UCF: www.ucf.edu/catalog/?catoid=12
     - Minnesota: umtc.catalog.prod.coursedog.com (Coursedog)
     - Rutgers: catalogs.rutgers.edu/generated/nb-ug_* (no current edition surfaced)
     - UCSD: catalog.ucsd.edu/undergraduate/degrees-offered/
   - Use only search-surfaced URLs, or links seen on stored official pages.

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
