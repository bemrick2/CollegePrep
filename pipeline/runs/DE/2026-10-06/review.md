# Review queue — DE (2026-27)

Pages fetched: 322; failures: 27. Candidates: 37 (30 without issues, 7 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 0 | 1 | 3 | 0 | 2 |
| cost_of_attendance | 0 | 0 | 0 | 1 | 3 | 0 | 2 |
| admissions_tests | 0 | 0 | 0 | 0 | 4 | 0 | 2 |
| common_data_set | 0 | 0 | 0 | 0 | 2 | 2 | 2 |
| merit_scholarships | 0 | 0 | 1 | 0 | 3 | 0 | 2 |
| ap_credit | 0 | 0 | 0 | 0 | 3 | 1 | 2 |
| clep_credit | 0 | 0 | 0 | 0 | 1 | 3 | 2 |
| ib_credit | 0 | 0 | 0 | 0 | 1 | 3 | 2 |
| dual_enrollment | 0 | 0 | 2 | 0 | 1 | 1 | 2 |
| transfer_credit | 0 | 0 | 0 | 0 | 4 | 0 | 2 |
| statewide_articulation | 0 | 0 | 0 | 0 | 2 | 2 | 2 |
| residency | 0 | 0 | 0 | 0 | 2 | 2 | 2 |
| degree_requirements | 0 | 0 | 0 | 0 | 3 | 1 | 2 |
| aid_appeals | 0 | 0 | 0 | 1 | 0 | 3 | 2 |

## Ready for review (30)

### `c27fd6abc7b64612` Delaware State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.desu.edu/admissions/other-admissions-types/dual-enrollment-program (sha256 1101de208086)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.75 ⟵ “High school scholars must maintain a minimum GPA of 2.75 to be eligible for acceptance.”
### `e78164d04dd195f1` University of Delaware — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.pcs.udel.edu/high-school-dual-enrollment/ (sha256 faeac5cb5432)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.6 ⟵ “a high school grade point average of 3.6 or above”
### `068ae17679177f66` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $5,000 ⟵ “College of Nursing & Health Sciences Dean's Merit Scholarship | Fall | $5,000 | One year | Nursing & Health Sciences nursing, health | 4.0 | All graduate level | Part time, Full time | All | ”
  - gpa_requirement: 4.0 ⟵ “College of Nursing & Health Sciences Dean's Merit Scholarship | Fall | $5,000 | One year | Nursing & Health Sciences nursing, health | 4.0 | All graduate level | Part time, Full time | All | ”
### `190070a12219133d` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 3.25}}
  - award_amount_text: Half tuition ⟵ “STAR Scholarship | All Terms Fall, Spring | Half tuition | Varies | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.25 | Undergraduate | Full time | Transfer | Must have conferred associate degree through the SEED p”
  - gpa_requirement: 3.25 ⟵ “STAR Scholarship | All Terms Fall, Spring | Half tuition | Varies | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.25 | Undergraduate | Full time | Transfer | Must have conferred associate degree through the SEED p”
  - eligibility_summary: Must have conferred associate degree through the SEED program. Learn more about the STAR Scholarship. ⟵ “STAR Scholarship | All Terms Fall, Spring | Half tuition | Varies | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.25 | Undergraduate | Full time | Transfer | Must have conferred associate degree through the SEED p”
### `2899297fbac26203` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $5,000 ⟵ “College of Sciences & Engineering Dean's Merit Scholarship | Fall | $5,000 | One year | Sciences & Engineering sciences, engineering | 4.0 | All graduate level | Part time, Full time | All | ”
  - gpa_requirement: 4.0 ⟵ “College of Sciences & Engineering Dean's Merit Scholarship | Fall | $5,000 | One year | Sciences & Engineering sciences, engineering | 4.0 | All graduate level | Part time, Full time | All | ”
### `2d548792a844e8b3` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $5,000 ⟵ “College of Business & Technology Dean's Merit Scholarship | Fall | $5,000 | One year | Business & Technology business, technology | 4.0 | All graduate level | Part time, Full time | All | ”
  - gpa_requirement: 4.0 ⟵ “College of Business & Technology Dean's Merit Scholarship | Fall | $5,000 | One year | Business & Technology business, technology | 4.0 | All graduate level | Part time, Full time | All | ”
### `346586a7f75db8fa` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “Career-Based Scholarship | Fall | $5,000 | One year | Business & Technology, Nursing & Health Sciences business, technology, nursing, health | Varies | Undergraduate | Full-time | All | The Career-Based Scholarship is for students enrolled in a degree program in the State of Delaware that leads to a”
  - eligibility_summary: The Career-Based Scholarship is for students enrolled in a degree program in the State of Delaware that leads to a high-need career field such as finance, human resources, nursing, management, and software development. See application instructions on the Delaware Department of Education website using the link above. ⟵ “Career-Based Scholarship | Fall | $5,000 | One year | Business & Technology, Nursing & Health Sciences business, technology, nursing, health | Varies | Undergraduate | Full-time | All | The Career-Based Scholarship is for students enrolled in a degree program in the State of Delaware that leads to a”
### `351d1b3592e56745` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $5,000 ⟵ “Quinn Family Memorial Scholarship | Fall | $5,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All graduate level | Part time, Full time | All | ”
  - gpa_requirement: 2.5 ⟵ “Quinn Family Memorial Scholarship | Fall | $5,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All graduate level | Part time, Full time | All | ”
### `36ef549f9defa638` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: Full tuition (no fees) ⟵ “Neighborhood Scholarship | Fall | Full tuition (no fees) | Four years | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | Undergraduate | Full time | All | Must be a graduating senior at William Penn High School. ”
  - gpa_requirement: 2.5 ⟵ “Neighborhood Scholarship | Fall | Full tuition (no fees) | Four years | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | Undergraduate | Full time | All | Must be a graduating senior at William Penn High School. ”
  - eligibility_summary: Must be a graduating senior at William Penn High School. Apply for the Neighborhood Scholarship. ⟵ “Neighborhood Scholarship | Fall | Full tuition (no fees) | Four years | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | Undergraduate | Full time | All | Must be a graduating senior at William Penn High School. ”
### `5142eb55a34485d1` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “School of Law Dean's Merit Scholarship | Fall | $5,000 | One year | business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science, school of lawSchool of Law | N/A | School of Law | Part time, Full time | All | ”
### `53144427115ad2ea` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 3.3}}
  - award_amount_text: $1,000 ⟵ “Phi Theta Kappa (PTK) Recognition Scholarship | Fall | $1,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.3 | Undergraduate | Part time, Full time | Transfer | Must be a member of the PTK Honor Soci”
  - gpa_requirement: 3.3 ⟵ “Phi Theta Kappa (PTK) Recognition Scholarship | Fall | $1,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.3 | Undergraduate | Part time, Full time | Transfer | Must be a member of the PTK Honor Soci”
  - eligibility_summary: Must be a member of the PTK Honor Society. ⟵ “Phi Theta Kappa (PTK) Recognition Scholarship | Fall | $1,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.3 | Undergraduate | Part time, Full time | Transfer | Must be a member of the PTK Honor Soci”
### `68c2cf9a0765de2d` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: Varies, up to $7,196 total ⟵ “Aspiring Teachers Scholarship | All Terms Fall, Spring | Varies, up to $7,196 total | Varies | Education & Liberal Arts college of education, liberal arts | 2.5 | Undergraduate | Part time, Full time | All | Must have earned diploma from a Delaware high school, must enroll at WilmU within 12 months ”
  - gpa_requirement: 2.5 ⟵ “Aspiring Teachers Scholarship | All Terms Fall, Spring | Varies, up to $7,196 total | Varies | Education & Liberal Arts college of education, liberal arts | 2.5 | Undergraduate | Part time, Full time | All | Must have earned diploma from a Delaware high school, must enroll at WilmU within 12 months ”
  - eligibility_summary: Must have earned diploma from a Delaware high school, must enroll at WilmU within 12 months of high school graduation, must pursue a teacher preparation program that leads to state licensure, must maintain at least a 2.5 GPA while enrolled at WilmU. Learn more about the Aspiring Teachers Scholarship. ⟵ “Aspiring Teachers Scholarship | All Terms Fall, Spring | Varies, up to $7,196 total | Varies | Education & Liberal Arts college of education, liberal arts | 2.5 | Undergraduate | Part time, Full time | All | Must have earned diploma from a Delaware high school, must enroll at WilmU within 12 months ”
### `6b0e2dc7976f888f` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: Covers tuition for every fifth course, up to $4,500 total ⟵ “Community College Partner Renewable Transfer Scholarship | All Terms Fall, Spring | Covers tuition for every fifth course, up to $4,500 total | Varies | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | Undergradu”
  - gpa_requirement: 2.5 ⟵ “Community College Partner Renewable Transfer Scholarship | All Terms Fall, Spring | Covers tuition for every fifth course, up to $4,500 total | Varies | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | Undergradu”
  - eligibility_summary: Must have conferred associate degree from an eligible partner school, must complete 15 credits within 1 year of enrolling at WilmU. Learn more about the Partner Renewable Transfer Scholarship. ⟵ “Community College Partner Renewable Transfer Scholarship | All Terms Fall, Spring | Covers tuition for every fifth course, up to $4,500 total | Varies | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | Undergradu”
### `6fb62104ed16ebdc` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": null}
  - eligibility_summary: Wilmington University has partnered with Scholarship America to bring quality degree programs to students. These undergrad and graduate programs assist in developing a highly qualified workforce. Learn more about Scholarship America. ⟵ “Scholarship America Scholarship | All Terms Fall, Spring | Varies | Varies | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | Varies | All graduate level | Part time, Full time | All | Wilmington University has partner”
### `827ca3a4abf66788` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $2,000 ⟵ “Linda Thomas Scholarship | Fall | $2,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All graduate level | Part time, Full time | All | ”
  - gpa_requirement: 2.5 ⟵ “Linda Thomas Scholarship | Fall | $2,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All graduate level | Part time, Full time | All | ”
### `935f9cb87b3eb3d4` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Scholarship Incentive Program | Fall | $1,000 | One Year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | Varies | Undergraduate | Full-time | All | The Scholarship Incentive Program (ScIP) is a $1,000 need-based awa”
  - eligibility_summary: The Scholarship Incentive Program (ScIP) is a $1,000 need-based award for qualifying students intending to pursue a bachelor’s degree full-time in Delaware. See application instructions on the Delaware Department of Education website using the link above. ⟵ “Scholarship Incentive Program | Fall | $1,000 | One Year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | Varies | Undergraduate | Full-time | All | The Scholarship Incentive Program (ScIP) is a $1,000 need-based awa”
### `9cf4c587825a2c37` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $5,000 for part time, $10,000 for full time ⟵ “Sandra L. and Thomas S. Shaw Scholarship | Fall | $5,000 for part time, $10,000 for full time | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All graduate level | Part time, Full time | All | Must b”
  - gpa_requirement: 2.5 ⟵ “Sandra L. and Thomas S. Shaw Scholarship | Fall | $5,000 for part time, $10,000 for full time | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All graduate level | Part time, Full time | All | Must b”
  - eligibility_summary: Must be an honorably discharged veteran or active military, or immediate family member of a veteran who graduated from Wilmington University. ⟵ “Sandra L. and Thomas S. Shaw Scholarship | Fall | $5,000 for part time, $10,000 for full time | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All graduate level | Part time, Full time | All | Must b”
### `a8dfbcfccc0e158c` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $2,000 ⟵ “Mig Reardon Memorial Nursing Scholarship | Fall | $2,000 | One year | Nursing & Health Sciences nursing, health | 2.5 | Undergraduate | Part time, Full time | All | Must be a Registered Nurse pursuing a BSN degree”
  - gpa_requirement: 2.5 ⟵ “Mig Reardon Memorial Nursing Scholarship | Fall | $2,000 | One year | Nursing & Health Sciences nursing, health | 2.5 | Undergraduate | Part time, Full time | All | Must be a Registered Nurse pursuing a BSN degree”
  - eligibility_summary: Must be a Registered Nurse pursuing a BSN degree ⟵ “Mig Reardon Memorial Nursing Scholarship | Fall | $2,000 | One year | Nursing & Health Sciences nursing, health | 2.5 | Undergraduate | Part time, Full time | All | Must be a Registered Nurse pursuing a BSN degree”
### `b0c844f52e3642b9` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - award_amount_text: $5,000 ⟵ “Dr. Jack P. Varsalona Scholarship | Fall | $5,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.0 | Undergraduate, Graduate graduate level | Full time | All | Must demonstrate exemplary leadership or ”
  - gpa_requirement: 3.0 ⟵ “Dr. Jack P. Varsalona Scholarship | Fall | $5,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.0 | Undergraduate, Graduate graduate level | Full time | All | Must demonstrate exemplary leadership or ”
  - eligibility_summary: Must demonstrate exemplary leadership or impact through community involvement. ⟵ “Dr. Jack P. Varsalona Scholarship | Fall | $5,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.0 | Undergraduate, Graduate graduate level | Full time | All | Must demonstrate exemplary leadership or ”
### `ba30f61a97b4a6ef` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": null}
  - award_amount_text: Varies based on remaining courses, up to $5,850 total ⟵ “STEP Path™ Scholarship | All Terms | Varies based on remaining courses, up to $5,850 total | Varies | Business & Technology, Social & Behavioral Sciences business, technology, social, behavioral | Varies | Undergraduate | Part time, Full time | Transfer, Camden County College | Must have conferred a”
  - eligibility_summary: Must have conferred associate degree from Camden County College, must enroll in a STEP Path-eligible online bachelor’s degree program at WilmU within 24 months of associate degree conferral, must continue part- or full-time towards bachelor’s degree. Learn more about the STEP Path™ Scholarship. ⟵ “STEP Path™ Scholarship | All Terms | Varies based on remaining courses, up to $5,850 total | Varies | Business & Technology, Social & Behavioral Sciences business, technology, social, behavioral | Varies | Undergraduate | Part time, Full time | Transfer, Camden County College | Must have conferred a”
### `bf8eb5a48939daad` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “AmeriCorps Matching Scholarship | Fall (Once per academic year) | $1,000 | Up to six years | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 GPA for Undergraduate, 3.0 GPA for Graduate | Undergraduate, Graduate gr”
  - gpa_requirement: 2.5 GPA for Undergraduate, 3.0 GPA for Graduate ⟵ “AmeriCorps Matching Scholarship | Fall (Once per academic year) | $1,000 | Up to six years | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 GPA for Undergraduate, 3.0 GPA for Graduate | Undergraduate, Graduate gr”
  - eligibility_summary: Participants who have completed service for AmeriCorps can enroll at Wilmington University and receive $1,000 toward tuition each academic year until graduation, for a maximum of six years. Learn more and apply for the AmeriCorps Matching Scholarship. ⟵ “AmeriCorps Matching Scholarship | Fall (Once per academic year) | $1,000 | Up to six years | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 GPA for Undergraduate, 3.0 GPA for Graduate | Undergraduate, Graduate gr”
### `c3469f425ce28359` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - award_amount_text: $500 for Health Sciences student(s), $2,000 for Nursing student(s) ⟵ “Future of Nursing Excellence Scholarship | Fall | $500 for Health Sciences student(s), $2,000 for Nursing student(s) | One year | Nursing & Health Sciences nursing, health | 3.0 | All graduate level | Part time, Full time | All | Must demonstrate a passion for serving and caring for others in a heal”
  - gpa_requirement: 3.0 ⟵ “Future of Nursing Excellence Scholarship | Fall | $500 for Health Sciences student(s), $2,000 for Nursing student(s) | One year | Nursing & Health Sciences nursing, health | 3.0 | All graduate level | Part time, Full time | All | Must demonstrate a passion for serving and caring for others in a heal”
  - eligibility_summary: Must demonstrate a passion for serving and caring for others in a health professional role. ⟵ “Future of Nursing Excellence Scholarship | Fall | $500 for Health Sciences student(s), $2,000 for Nursing student(s) | One year | Nursing & Health Sciences nursing, health | 3.0 | All graduate level | Part time, Full time | All | Must demonstrate a passion for serving and caring for others in a heal”
### `c3e3678f2b0c4a0d` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $1,200 ⟵ “Dr. Stephanie Battis Memorial Scholarship | Fall | $1,200 | One year | Business & Technology business, technology | 2.5 | Undergraduate | Part time, Full time | All | Must be enrolled in Human Resources Management degree program”
  - gpa_requirement: 2.5 ⟵ “Dr. Stephanie Battis Memorial Scholarship | Fall | $1,200 | One year | Business & Technology business, technology | 2.5 | Undergraduate | Part time, Full time | All | Must be enrolled in Human Resources Management degree program”
  - eligibility_summary: Must be enrolled in Human Resources Management degree program ⟵ “Dr. Stephanie Battis Memorial Scholarship | Fall | $1,200 | One year | Business & Technology business, technology | 2.5 | Undergraduate | Part time, Full time | All | Must be enrolled in Human Resources Management degree program”
### `c51732ac9d561223` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - award_amount_text: $1,000 ⟵ “William and Mary Bescherer Memorial Scholarship | Fall | $1,000 | One year | Nursing & Health Sciences nursing, health | 3.0 | Undergraduate | Part time, Full time | All | Must be enrolled in Health Sciences degree program”
  - gpa_requirement: 3.0 ⟵ “William and Mary Bescherer Memorial Scholarship | Fall | $1,000 | One year | Nursing & Health Sciences nursing, health | 3.0 | Undergraduate | Part time, Full time | All | Must be enrolled in Health Sciences degree program”
  - eligibility_summary: Must be enrolled in Health Sciences degree program ⟵ “William and Mary Bescherer Memorial Scholarship | Fall | $1,000 | One year | Nursing & Health Sciences nursing, health | 3.0 | Undergraduate | Part time, Full time | All | Must be enrolled in Health Sciences degree program”
### `c7ad6c79190d4959` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $5,000 ⟵ “College of Education & Liberal Arts Dean's Merit Scholarship | Fall | $5,000 | One year | Education & Liberal Arts college of education, liberal arts | 4.0 | All graduate level | Part time, Full time | All | ”
  - gpa_requirement: 4.0 ⟵ “College of Education & Liberal Arts Dean's Merit Scholarship | Fall | $5,000 | One year | Education & Liberal Arts college of education, liberal arts | 4.0 | All graduate level | Part time, Full time | All | ”
### `dac313cf10fb01ab` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - award_amount_text: $1,250 for part time, $2,500 for full time ⟵ “Bettye J. and Ralph E. Bailey Scholarship | Fall | $1,250 for part time, $2,500 for full time | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.0 | Undergraduate | Part time, Full time | All | ”
  - gpa_requirement: 3.0 ⟵ “Bettye J. and Ralph E. Bailey Scholarship | Fall | $1,250 for part time, $2,500 for full time | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 3.0 | Undergraduate | Part time, Full time | All | ”
### `e379395f35a8601d` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: Up to $5,000 ⟵ “Wilmington University Scholarship | Fall, Spring | Up to $5,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science, school of law | 2.5 | All graduate level | Part time, Full time | All | ”
  - gpa_requirement: 2.5 ⟵ “Wilmington University Scholarship | Fall, Spring | Up to $5,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science, school of law | 2.5 | All graduate level | Part time, Full time | All | ”
### `e70de337c8723425` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - award_amount_text: $4,000 ⟵ “Wilmington Manor Lions Club Scholarship | Fall | $4,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All | Part time, Full time | All | Must be an active member of the local community.”
  - gpa_requirement: 2.5 ⟵ “Wilmington Manor Lions Club Scholarship | Fall | $4,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All | Part time, Full time | All | Must be an active member of the local community.”
  - eligibility_summary: Must be an active member of the local community. ⟵ “Wilmington Manor Lions Club Scholarship | Fall | $4,000 | One year | All business, technology, college of education, liberal arts, nursing, health, sciences, engineering, social, behavioral science | 2.5 | All | Part time, Full time | All | Must be an active member of the local community.”
### `f59f3fad3281dc12` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “Educator Support Scholarship | Fall | $5,000 | One year | Education & Liberal Arts college of education, liberal arts | Varies | All | Full-time | All | The Educator Support Scholarship is for students enrolled in a degree program in the State of Delaware that leads to a career in education (in a cl”
  - eligibility_summary: The Educator Support Scholarship is for students enrolled in a degree program in the State of Delaware that leads to a career in education (in a classroom or as a specialist). See application instructions on the Delaware Department of Education website using the link above. ⟵ “Educator Support Scholarship | Fall | $5,000 | One year | Education & Liberal Arts college of education, liberal arts | Varies | All | Full-time | All | The Educator Support Scholarship is for students enrolled in a degree program in the State of Delaware that leads to a career in education (in a cl”
### `fbcccc7eac6098c6` Wilmington University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wilmu.edu/scholarships/available-scholarships.aspx (sha256 d6db09a45a09)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $5,000 ⟵ “College of Social & Behavioral Sciences Dean's Merit Scholarship | Fall | $5,000 | One year | Social & Behavioral Sciences social, behavioral | 4.0 | All graduate level | Part time, Full time | All | ”
  - gpa_requirement: 4.0 ⟵ “College of Social & Behavioral Sciences Dean's Merit Scholarship | Fall | $5,000 | One year | Social & Behavioral Sciences social, behavioral | 4.0 | All graduate level | Part time, Full time | All | ”

## Exceptions (7)

### `8844daaa3a26f21b` Delaware State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.desu.edu/admissions/financial-aid/eligibility/satisfactory-academic-progress-sap (sha256 83b3e1053351)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Students who fail to meet SAP standards are not eligible for federal, state, or institutional aid until eligibility is regained. 2026–2027 SAP Appeal Deadline: July 31, 2026 When SAP Is Reviewed SAP is reviewed once a year, at the end of the spring semester.”
  - sentence: sap_appeal ⟵ “Students who fail SAP must appeal to be considered for continued eligibility.”
  - sentence: sap_appeal ⟵ “Students with an approved SAP appeal for the Fall semester, will have their academic progress reviewed at the end of the semester.”
  - sentence: sap_appeal ⟵ “Follow these steps: Go to https://desu.verifymyfafsa.com/account/registerstudent Sign in using your DSU Single Sign on Credentials Click “Sign-In” Enter/confirm your student information Click “Register Account” button How to submit an appeal: Log on to desu.verifymyfafsa.com: Click “Fill Out” under SAP Appeal Confirm that the following information is correction (e.g.”
  - sentence: sap_appeal ⟵ “Appeal “Approval” Probation status is assigned to students failing to make satisfactory academic progress who successfully appeal.”
### `99bac7b89d794a95` Delaware State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.desu.edu/admissions/financial-aid/applying-aid/special-circumstances (sha256 ca93900d5c34)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If you meet any of the conditions listed above, you may submit a SAI Appeal or Professional Judgment Adjustment Form by logging in to desu.studentforms.com.”
### `b989adc1f1825a7e` Delaware State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.desu.edu/admissions/financial-aid/applying-aid/special-circumstances (sha256 ca93900d5c34)
- issues: semantic_review_required, conflicting_sources:https://www.desu.edu/admissions/financial-aid/applying-aid
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “To ensure fairness and compliance with the federal financial aid regulations, special circumstances can be considered on a case-by-case basis and there are limits as to what can be considered.”
  - sentence: need_based_special_circumstances ⟵ “The situations below, while not all inclusive, indicate what types of circumstances we cannot consider. high consumer debt, including credit cards home mortgage expenses car payments private school expenses (including tuition) changes in seasonal employment parent in college Special circumstance information and required forms may vary annually.”
  - sentence: need_based_special_circumstances ⟵ “Applying for Aid Verification Helpful Hints Special Circumstances Step-by-Step Process Summer Start your journey here.”
### `edec1294c19bf80f` Delaware State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.desu.edu/admissions/financial-aid/applying-aid (sha256 9aae3248fed5)
- issues: semantic_review_required, conflicting_sources:https://www.desu.edu/admissions/financial-aid/applying-aid/special-circumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Tuition & Fees Scholarships Forms & Publications Current Students Applying for Aid Verification Helpful Hints Special Circumstances Step-by-Step Process Summer Cost Eligibility FAFSA Application Forms Receiving Funds Resources Types and Sources Start your journey here.”
### `66abd64c6e3f25bf` Delaware State University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.desu.edu/admissions/financial-aid/cost-attendance (sha256 fde93cb75598)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 12}
  - on_campus:Tuition: 19584.0 ⟵ “Tuition | $ 19,584.00 | $ 19,584.00”
  - on_campus:Fees: 1620.0 ⟵ “Fees | $ 1,620.00 | $ 1,620.00”
  - on_campus:Housing: 10768.0 ⟵ “Housing | $ 10,768.00 | $ 13,460.00”
  - on_campus:Food: 3546.0 ⟵ “Food | $ 3,546.00 | $ 4,380.00”
  - on_campus:Books: 648.0 ⟵ “Books | $ 648.00 | $ 648.00”
  - on_campus:Supplies: 500.0 ⟵ “Supplies | $ 500.00 | $ 500.00”
  - on_campus:Transportation: 2522.0 ⟵ “Transportation | $ 2,522.00 | $ 2,522.00”
  - on_campus:Labs: 706.0 ⟵ “Labs | $ 706.00 | $ 706.00”
  - on_campus:Insurance: 1064.0 ⟵ “Insurance | $ 1,064.00 | $ 1,064.00”
  - on_campus:Loan Fees: 856.0 ⟵ “Loan Fees | $ 856.00 | $ 856.00”
  - on_campus:Personal Expenses: 2448.0 ⟵ “Personal Expenses | $ 2,448.00 | $ 2,448.00”
  - on_campus:Total: 44262.0 ⟵ “Total | $ 44,262.00 | $ 47,788.00”
  - off_campus_not_with_family:Tuition: 19584.0 ⟵ “Tuition | $ 19,584.00 | $ 19,584.00”
  - off_campus_not_with_family:Fees: 1620.0 ⟵ “Fees | $ 1,620.00 | $ 1,620.00”
  - off_campus_not_with_family:Housing: 13460.0 ⟵ “Housing | $ 10,768.00 | $ 13,460.00”
  - off_campus_not_with_family:Food: 4380.0 ⟵ “Food | $ 3,546.00 | $ 4,380.00”
  - off_campus_not_with_family:Books: 648.0 ⟵ “Books | $ 648.00 | $ 648.00”
  - off_campus_not_with_family:Supplies: 500.0 ⟵ “Supplies | $ 500.00 | $ 500.00”
  - off_campus_not_with_family:Transportation: 2522.0 ⟵ “Transportation | $ 2,522.00 | $ 2,522.00”
  - off_campus_not_with_family:Labs: 706.0 ⟵ “Labs | $ 706.00 | $ 706.00”
  - off_campus_not_with_family:Insurance: 1064.0 ⟵ “Insurance | $ 1,064.00 | $ 1,064.00”
  - off_campus_not_with_family:Loan Fees: 856.0 ⟵ “Loan Fees | $ 856.00 | $ 856.00”
  - off_campus_not_with_family:Personal Expenses: 2448.0 ⟵ “Personal Expenses | $ 2,448.00 | $ 2,448.00”
  - off_campus_not_with_family:Total: 47788.0 ⟵ “Total | $ 44,262.00 | $ 47,788.00”
### `dbca9c8d6ebd6f43` Delaware State University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.desu.edu/admissions/financial-aid/cost-attendance (sha256 fde93cb75598)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 12}
  - on_campus:Tuition: 9594.0 ⟵ “Tuition | $ 9,594.00 | $ 9,594.00”
  - on_campus:Fees: 1620.0 ⟵ “Fees | $ 1,620.00 | $ 1,620.00”
  - on_campus:Housing: 10768.0 ⟵ “Housing | $ 10,768.00 | $ 13,460.00”
  - on_campus:Food: 3546.0 ⟵ “Food | $ 3,546.00 | $ 4,380.00”
  - on_campus:Books: 648.0 ⟵ “Books | $ 648.00 | $ 648.00”
  - on_campus:Supplies: 500.0 ⟵ “Supplies | $ 500.00 | $ 500.00”
  - on_campus:Transportation: 2522.0 ⟵ “Transportation | $ 2,522.00 | $ 2,522.00”
  - on_campus:Labs: 706.0 ⟵ “Labs | $ 706.00 | $ 706.00”
  - on_campus:Insurance: 1064.0 ⟵ “Insurance | $ 1,064.00 | $ 1,064.00”
  - on_campus:Loan Fees: 856.0 ⟵ “Loan Fees | $ 856.00 | $ 856.00”
  - on_campus:Personal Expenses: 2448.0 ⟵ “Personal Expenses | $ 2,448.00 | $ 2,448.00”
  - on_campus:Total: 34272.0 ⟵ “Total | $ 34,272.00 | $ 37,798.00”
  - off_campus_not_with_family:Tuition: 9594.0 ⟵ “Tuition | $ 9,594.00 | $ 9,594.00”
  - off_campus_not_with_family:Fees: 1620.0 ⟵ “Fees | $ 1,620.00 | $ 1,620.00”
  - off_campus_not_with_family:Housing: 13460.0 ⟵ “Housing | $ 10,768.00 | $ 13,460.00”
  - off_campus_not_with_family:Food: 4380.0 ⟵ “Food | $ 3,546.00 | $ 4,380.00”
  - off_campus_not_with_family:Books: 648.0 ⟵ “Books | $ 648.00 | $ 648.00”
  - off_campus_not_with_family:Supplies: 500.0 ⟵ “Supplies | $ 500.00 | $ 500.00”
  - off_campus_not_with_family:Transportation: 2522.0 ⟵ “Transportation | $ 2,522.00 | $ 2,522.00”
  - off_campus_not_with_family:Labs: 706.0 ⟵ “Labs | $ 706.00 | $ 706.00”
  - off_campus_not_with_family:Insurance: 1064.0 ⟵ “Insurance | $ 1,064.00 | $ 1,064.00”
  - off_campus_not_with_family:Loan Fees: 856.0 ⟵ “Loan Fees | $ 856.00 | $ 856.00”
  - off_campus_not_with_family:Personal Expenses: 2448.0 ⟵ “Personal Expenses | $ 2,448.00 | $ 2,448.00”
  - off_campus_not_with_family:Total: 37798.0 ⟵ “Total | $ 34,272.00 | $ 37,798.00”
### `d4302c3b6cebbc4b` University of Delaware — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.udel.edu/about/facts-figures/financial-profile/ (sha256 5285d217fb64)
- issues: arrangement_unlabeled, multiple_total_rows
- checks: {"columns": 10, "rows": 24}
  - column:Net Undergraduate Tuition & Fees: 349 ⟵ “Net Undergraduate Tuition & Fees | 349 | 364 | 369 | 374 | 337 | 335 | 343 | 363 | 378 | 407”
  - column:Net Graduate Tuition & Fees: 31 ⟵ “Net Graduate Tuition & Fees | 31 | 36 | 34 | 30 | 30 | 28 | 31 | 35 | 36 | 34”
  - column:Other Tuition & Fees: 44 ⟵ “Other Tuition & Fees | 44 | 46 | 56 | 55 | 50 | 62 | 65 | 68 | 72 | 78”
  - column:State Appropriation: 121 ⟵ “State Appropriation | 121 | 119 | 122 | 125 | 125 | 128 | 134 | 140 | 145 | 147”
  - column:Facilities and Administrative Cost Recoveries: 36 ⟵ “Facilities and Administrative Cost Recoveries | 36 | 37 | 40 | 41 | 44 | 54 | 59 | 67 | 66 | 68”
  - column:Endowment Payout and Proceeds of Investment of Previous Surpluses: 69 ⟵ “Endowment Payout and Proceeds of Investment of Previous Surpluses | 69 | 71 | 75 | 72 | 69 | 72 | 88 | 98 | 103 | 98”
  - column:Auxiliary Revenue: 119 ⟵ “Auxiliary Revenue | 119 | 127 | 130 | 90 | 50 | 121 | 136 | 142 | 149 | 154”
  - column:Gifts for Operating: 31 ⟵ “Gifts for Operating | 31 | 29 | 28 | 24 | 29 | 33 | 28 | 37 | 29 | 38”
  - column:Contracts & Grants: 142 ⟵ “Contracts & Grants | 142 | 145 | 165 | 171 | 181 | 232 | 224 | 246 | 232 | 250”
  - column:Other & Entrepreneurial Revenue: 47 ⟵ “Other & Entrepreneurial Revenue | 47 | 51 | 51 | 46 | 35 | 51 | 61 | 60 | 62 | 69”
  - column:Total Operating Revenue: 989 ⟵ “Total Operating Revenue | 989 | 1,025 | 1,070 | 1,033 | 996 | 1,132 | 1,169 | 1,256 | 1,272 | 1,343”
  - column:Faculty Salaries: 151 ⟵ “Faculty Salaries | 151 | 159 | 169 | 177 | 178 | 175 | 180 | 187 | 191 | 199”
  - column:Salaried Staff Salaries: 151 ⟵ “Salaried Staff Salaries | 151 | 162 | 173 | 185 | 184 | 190 | 212 | 235 | 246 | 244”
  - column:Hourly Staff Salaries: 77 ⟵ “Hourly Staff Salaries | 77 | 79 | 80 | 80 | 65 | 72 | 77 | 79 | 78 | 87”
  - column:Adjunct Faculty & Other Contract Workers: 23 ⟵ “Adjunct Faculty & Other Contract Workers | 23 | 24 | 24 | 26 | 21 | 25 | 26 | 28 | 32 | 28”
  - column:Graduate Student Salaries: 42 ⟵ “Graduate Student Salaries | 42 | 45 | 50 | 51 | 52 | 52 | 59 | 62 | 62 | 63”
  - column:Benefits: 167 ⟵ “Benefits | 167 | 175 | 184 | 192 | 190 | 191 | 205 | 224 | 260 | 253”
  - column:Travel: 27 ⟵ “Travel | 27 | 29 | 31 | 25 | 3 | 17 | 30 | 31 | 30 | 32”
  - column:Supplies, Materials and Other: 130 ⟵ “Supplies, Materials and Other | 130 | 145 | 176 | 149 | 121 | 190 | 202 | 228 | 194 | 235”
  - column:Plant Maintenance & Operations: 81 ⟵ “Plant Maintenance & Operations | 81 | 86 | 89 | 82 | 72 | 83 | 85 | 96 | 97 | 99”
  - column:Research Subcontracts: 24 ⟵ “Research Subcontracts | 24 | 25 | 26 | 35 | 38 | 41 | 46 | 48 | 42 | 51”
  - column:Debt Service: 38 ⟵ “Debt Service | 38 | 39 | 41 | 48 | 48 | 42 | 41 | 41 | 39 | 52”
  - column:Total Operating Expenses: 911 ⟵ “Total Operating Expenses | 911 | 968 | 1,043 | 1,050 | 972 | 1,078 | 1,163 | 1,259 | 1,271 | 1,343”
  - column:Operating surplus**/(deficit): 78 ⟵ “Operating surplus**/(deficit) | 78 | 57 | 27 | (17) | 24 | 54 | 6 | (3) | 1 | 0”
  - column:Net Undergraduate Tuition & Fees: 364 ⟵ “Net Undergraduate Tuition & Fees | 349 | 364 | 369 | 374 | 337 | 335 | 343 | 363 | 378 | 407”
  - … 220 more rows

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 1; pages by category: 

## Blocked by the site (every request refused; needs the browser fallback)

- Delaware Technical Community College-Terry (`ipeds-130907`)
- Delaware College of Art and Design (`ipeds-432524`)

## Leads: official pages found with no extracted record

- Delaware State University: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Goldey-Beacom College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- University of Delaware: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Wilmington University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, dual_enrollment, transfer_credit, degree_requirements
