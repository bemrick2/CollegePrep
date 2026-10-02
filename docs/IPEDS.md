# Nationwide historical data

The pinned official NCES HD2023, ADM2023 and IC2023_AY downloads and their dictionaries are preserved under `sources/ipeds/2023-24`, with SHA-256 hashes. Normalized CSV records carry academic year, source URL, verification status and last verification date. Only active-as-reported institutions in the 50 states and DC are included. Historical activity is not a claim of current accreditation or operating status.

Normalized files are partitioned by state and academic year for manageable review. HD2023.zip is stored in ordered binary parts listed in the manifest; concatenate those bytes to reconstruct the exact archive before checking its full SHA-256. UT Knoxville is joined to the curated identity using official UNITID 221759.

Admissions describe fall 2023 first-time degree/certificate-seeking undergraduate students at reporting institutions. SAT section percentiles are kept separate: adding section percentiles does not produce a valid composite percentile. Open-admission institutions without survey records are unknown, not zero.

Costs use CHG1/2/3AT3 and AF3: published 2023–24 tuition and fees for full-time first-time undergraduates in district, in state and out of state. Books, on-campus food/housing and other expenses are retained separately. A total COA is not invented. Program-reporting schools without academic-year costs remain missing. Imputation flags other than `R` are not presented as verified measurements; those values stay null.

Reproduce with `python scripts/import_ipeds.py --archive-dir <download-directory> --verified-at <actual-review-date>`, then validate and update coverage. Existing curated identities take precedence; join by UNITID where present. The annual dataset is historical coverage, not a substitute for current institutional price verification.
