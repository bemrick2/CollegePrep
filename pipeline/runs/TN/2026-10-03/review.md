# Review queue — TN (2026-27)

Pages fetched: 3553; failures: 484. Candidates: 426 (123 without issues, 303 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 10 | 0 | 0 | 6 | 35 | 1 | 7 |
| cost_of_attendance | 6 | 1 | 0 | 1 | 42 | 2 | 7 |
| admissions_tests | 2 | 0 | 0 | 1 | 45 | 4 | 7 |
| common_data_set | 2 | 0 | 0 | 1 | 7 | 42 | 7 |
| merit_scholarships | 3 | 3 | 4 | 1 | 33 | 8 | 7 |
| ap_credit | 1 | 3 | 0 | 3 | 11 | 34 | 7 |
| clep_credit | 1 | 2 | 2 | 1 | 6 | 40 | 7 |
| ib_credit | 1 | 1 | 0 | 1 | 3 | 46 | 7 |
| dual_enrollment | 1 | 0 | 19 | 6 | 14 | 12 | 7 |
| transfer_credit | 0 | 7 | 2 | 0 | 38 | 5 | 7 |
| statewide_articulation | 0 | 0 | 0 | 0 | 17 | 35 | 7 |
| residency | 0 | 0 | 0 | 0 | 24 | 28 | 7 |
| degree_requirements | 1 | 1 | 0 | 0 | 38 | 12 | 7 |
| aid_appeals | 1 | 1 | 0 | 30 | 5 | 15 | 7 |

## Ready for review (123)

### `526bb1e22d847856` American Baptist College — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://abcnash.edu/admissions/requirements/ (sha256 242f3034d05f)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Only the grade of “C” or above may be transferred.”
### `04b84c8da27e8d65` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/ (sha256 6d70bdfa32d9)
- checks: {"thresholds": null}
  - test_requirement: ACT These scholarships are awarded based on a student's application for admission and are funded by private sources. / SAT These scholarships are awarded based on a student's application for admission and are funded by private sources. ⟵ “Private Academic Scholarships | These scholarships are awarded based on a student's application for admission and are funded by private sources.”
### `1eb1908d123e8f97` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - gpa_requirement: 3.5 ⟵ “Presidents Emerging Leaders Program (PELP) | 3.5 | Refer to the PELP Guidelines | 8 | Full-Time”
### `27394f6df05dd80e` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/ (sha256 6d70bdfa32d9)
- checks: {"thresholds": null}
  - test_requirement: ACT Students transferring to APSU may be offered awards, particularly students graduating from a community college with an Associates Degree / SAT Students transferring to APSU may be offered awards, particularly students graduating from a community college with an Associates Degree ⟵ “Transfer Students | Students transferring to APSU may be offered awards, particularly students graduating from a community college with an Associates Degree”
### `38934a28125a2628` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Governor's Out of State (formerly Provost) | 2.75 ♦ | 0 | 8 | Full-Time”
### `3f7b0f0954f53a49` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “Governor's Merit | 3.5 - 3.69 GPA | Admissions application to APSU | $1,500”
### `5c4d7ee9b98b49ab` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Academic Achievement(formerly Achievement) | 2.75 ♦ | 0 | 8 | Full-Time”
### `717fd2e41e88e44f` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/ (sha256 6d70bdfa32d9)
- checks: {"thresholds": null}
  - test_requirement: ACT Qualifying students may have substantial awards to reduce out-of-state charges. / SAT Qualifying students may have substantial awards to reduce out-of-state charges. ⟵ “Out-of-State Students | Qualifying students may have substantial awards to reduce out-of-state charges.”
### `71d87d3186b81ed6` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: Award Amount Varies ⟵ “Howell C. Smith (Limited Awards Available) | High-achieving students | Admissions application to APSU | Award Amount Varies”
### `8a87e9fc1912cece` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “Presidents Emerging Leaders Program (PELP)Apply by 12/31 | 3.6 GPA 23 ACT | More information about PELP | $3,000”
### `b46871af65eed607` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Howell C. Smith | 2.75 ♦ | 0 | 4 | Full-Time”
### `bdc5eb41bc3b8d8b` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “Academic Achievement | 3.7 - 3.84 GPA | Admissions application to APSU | $2,000”
### `ebfc8dc592177d0a` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Governor's Merit(formerly Advancement) | 2.75 ♦ | 0 | 8 | Full-Time”
### `f042c1593b24ffb2` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 3.0 ♦ ⟵ “Kimbrough | 3.0 ♦ | 0 | 8 | Full-Time”
### `facbd450ba1efadf` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Kimbrough (Limited Awards Available) | 3.0 GPA 25 ACT In-State Resident | Admissions application to APSU | $1,000”
### `fe7408b747d742b9` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/ (sha256 6d70bdfa32d9)
- checks: {"thresholds": null}
  - test_requirement: ACT Potential scholarships available to students who are taking a study abroad course. / SAT Potential scholarships available to students who are taking a study abroad course. ⟵ “Study Abroad | Potential scholarships available to students who are taking a study abroad course.”
### `caed1e0cf833bd4f` Austin Peay State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.apsu.edu/govnow/affording-dual-enrollment/bibb-family-scholarship.php (sha256 d25b9a19f949)
- checks: {"fields": ["college_gpa_to_continue"], "tiers": 0}
  - college_gpa_to_continue: 2.7 ⟵ “Students must maintain a cumulative college GPA of 2.75 to be eligible for the award”
  - college_gpa_to_continue: 2.7 ⟵ “Students must maintain a cumulative college GPA of 2.75 to be eligible for the award in future semesters.”
  - college_gpa_to_continue: 2.7 ⟵ “I understand that I must maintain a 2.75 college GPA to receive the scholarship in”
### `m221607a655c95b4` Belmont University — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.belmont.edu/registrar/transfer-students-info/tn-community-colleges.html (sha256 e8e4f31b87f6)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 3}
  - max_transfer_credits: 64 ⟵ “Of the 128 credit hours required: Up to 64 hours of work from a community college can be transferred to Belmont.”
  - min_grade: C ⟵ “For courses to transfer to Belmont, they must be from a regionally accredited college/university, must not be remedial and the student must have earned a grade of “C” or better.”
  - residency_requirement_credits: 32 ⟵ “SENIORS with 94+ completed hours are required to complete the last 32 hours of their degree program at Belmont.”
### `m21be78891cd38ac` Bethel University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.bethelu.edu/admissions/dual-enrollment (sha256 d8438f1c59a0)
- checks: {"fields": ["alt_min_act", "min_hs_gpa", "state_grant_accepted"], "merged_pages": 5, "tiers": 1}
  - state_grant_accepted: True ⟵ “Request that Official Transcripts from other universities attended if you've used the Dual Enrollment Grant at those institutions. Bethel will accept official transcripts via email, mail, Parchment, or Clearinghouse.”
  - eligibility_tier: 3.0 ⟵ “Attain a cumulative GPA of 3.0 (4.0 scale) or 21 on the ACT.”
  - per_credit_hour_charge: 100 ⟵ “Bethel’s Dual Enrollment tuition is fully covered by the Tennessee Dual Enrollment Grant for the first set of five courses (15 credit hours). For the second set of five courses, the Grant only covers $100 per credit hour. For those courses, Bethel matches the Grant with a scholarship making the seco”
  - state_grant_accepted: True ⟵ “Bethel’s Dual Enrollment tuition is fully covered by the Tennessee Dual Enrollment Grant for the first set of five courses (15 credit hours). For the second set of five courses, the Grant only covers $100 per credit hour. For those courses, Bethel matches the Grant with a scholarship making the seco”
  - state_grant_accepted: True ⟵ “Apply for the Tennessee Dual Enrollment Grant”
  - state_grant_accepted: True ⟵ “On the top of your screen, under the Red TN, click apply. Click Dual Enrollment Grant for Fall 2025, Spring 2026, Summer 2026. Read the Eligibility Requirements and Click OK.”
  - eligibility_tier: 3.0 ⟵ “Attain a cumulative GPA of 3.0 (4.0 scale) or 21 on the ACT.”
  - state_grant_accepted: True ⟵ “Did you know state financial aid is available to cover much of the cost of dual enrollment courses? Tennessee's Dual Enrollment Grant provides funding for high school students taking college-level courses at eligible post-secondary institutions.”
  - state_grant_accepted: True ⟵ “Grant Information If you are applying for and planning to use the Dual Enrollment Grant, please click here. It is a separate application from the admission application. If you have any questions, please contact Gara Scruggs in the Dual Enrollment Financial Aid office at scruggsg@bethelu.edu or (731)”
### `38aa93d298554bc6` Bryan College-Dayton — awards 2026-27 [same] (source_unlabeled)
- source: https://www.bryan.edu/scholarship/academic-leadership-scholarships/ (sha256 f453b5ae88c0)
- checks: {"thresholds": {"act_min": 24, "gpa_min": 3.6}}
  - award_amount_text: $4,100 ⟵ “Silver | 3.60 | 24 | 3.25 | $4,100”
  - gpa_requirement: 3.60 ⟵ “Silver | 3.60 | 24 | 3.25 | $4,100”
  - test_requirement: ACT 24 ⟵ “Silver | 3.60 | 24 | 3.25 | $4,100”
### `96731f77e9d75700` Bryan College-Dayton — awards 2026-27 [same] (source_unlabeled)
- source: https://www.bryan.edu/scholarship/academic-leadership-scholarships/ (sha256 f453b5ae88c0)
- checks: {"thresholds": {"act_min": 27, "gpa_min": 3.8}}
  - award_amount_text: $5,600 ⟵ “Platinum | 3.80 | 27 | 3.50 | $5,600”
  - gpa_requirement: 3.80 ⟵ “Platinum | 3.80 | 27 | 3.50 | $5,600”
  - test_requirement: ACT 27 ⟵ “Platinum | 3.80 | 27 | 3.50 | $5,600”
### `b6baffe687e9c7f5` Bryan College-Dayton — awards 2026-27 [same] (source_unlabeled)
- source: https://www.bryan.edu/scholarship/academic-leadership-scholarships/ (sha256 f453b5ae88c0)
- checks: {"thresholds": {"act_min": 21, "gpa_min": 3.4}}
  - award_amount_text: $2,500 ⟵ “Crimson | 3.40 | 21 | 3.00 | $2,500”
  - gpa_requirement: 3.40 ⟵ “Crimson | 3.40 | 21 | 3.00 | $2,500”
  - test_requirement: ACT 21 ⟵ “Crimson | 3.40 | 21 | 3.00 | $2,500”
### `3005de413ce7dff5` Bryan College-Dayton — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.bryan.edu/admissions/tuition-fees/ (sha256 ec9b11f80095)
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition (12-17 hours): 21700 ⟵ “Tuition (12-17 hours) | $10,850 | $21,700”
  - column:Board: 3900 ⟵ “Board | $1,950 | $3,900”
  - column:Room (traditional dorms): 5650 ⟵ “Room (traditional dorms) | $2,825 | $5,650”
  - column:Total traditional (tuition, room & board): 31250 ⟵ “Total traditional (tuition, room & board) | $15,625 | $31,250”
### `94371f77c67e1d64` Carson-Newman University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/types-of-aid/scholarships/ (sha256 4a5604a0718a)
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '<2.5', 'amount_text': '$10,000'}, {'gpa': '2.5', 'amount_text': '$12,000'}, {'gpa': '3.0', 'amount_text': '$14,000'}, {'gpa': '3.5', 'amount_text': '$16,000'}, {'gpa': '3.9', 'amount_text': '$18,000'}] ⟵ “GPA | Merit || <2.5 | $10,000 || 2.5 | $12,000 || 3.0 | $14,000 || 3.5 | $16,000 || 3.9 | $18,000”
  - gpa_requirement: Tiered by GPA: <2.5 → $10,000; 2.5 → $12,000; 3.0 → $14,000; 3.5 → $16,000; 3.9 → $18,000 ⟵ “GPA | Merit || <2.5 | $10,000 || 2.5 | $12,000 || 3.0 | $14,000 || 3.5 | $16,000 || 3.9 | $18,000”
### `93af76cc253f8e9f` Carson-Newman University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.cn.edu/wp-content/uploads/2025/11/2025-26-Dual-Enrollment-Agreement-Form.pdf (sha256 19f76c79a5f9)
- checks: {"fields": ["max_credit_hours_per_term", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - max_credit_hours_per_term: 14 ⟵ “•   Students may take up to a maximum of 14 hours of Dual Enrollment courses in each semester at the current Dual”
  - per_credit_hour_charge: 174 ⟵ “Enrollment tuition rate of $174 per credit hour with a $10 per credit hour technology fee. In addition to the tuition and”
  - per_credit_hour_charge: 10 ⟵ “Enrollment tuition rate of $174 per credit hour with a $10 per credit hour technology fee. In addition to the tuition and”
### `994681945138e02b` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 eac9e4c2acaa)
- checks: {"thresholds": {"act_min": 22, "gpa_min": 3.5, "sat_min": 1100}}
  - gpa_requirement: 3.5+ ⟵ “Lasallian Scholarship | $18,000.00 | 3.5+ |  | 22+ |  | 1100+”
  - test_requirement: ACT 22+ / SAT 1100+ ⟵ “Lasallian Scholarship | $18,000.00 | 3.5+ |  | 22+ |  | 1100+”
### `a007e0c53e793369` Christian Brothers University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 eac9e4c2acaa)
- checks: {"thresholds": null}
  - gpa_requirement: N/A ⟵ “University | $14,000.00 | N/A |  | N/A |  | N/A”
  - test_requirement: ACT N/A / SAT N/A ⟵ “University | $14,000.00 | N/A |  | N/A |  | N/A”
### `a36a329f90444760` Christian Brothers University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 eac9e4c2acaa)
- checks: {"thresholds": null}
  - gpa_requirement: N/A ⟵ “University Scholarship | $12,000 | N/A”
### `ae504e4a523532dd` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 eac9e4c2acaa)
- checks: {"thresholds": {"act_min": 25, "gpa_min": 3.75, "sat_min": 1200}}
  - gpa_requirement: 3.75+ ⟵ “Presidential Scholarship | $20,000.00 | 3.75+ |  | 25+ |  | 1200+”
  - test_requirement: ACT 25+ / SAT 1200+ ⟵ “Presidential Scholarship | $20,000.00 | 3.75+ |  | 25+ |  | 1200+”
### `c18e7b6ea71efcd7` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 eac9e4c2acaa)
- checks: {"thresholds": {"act_min": 18, "gpa_min": 3.0, "sat_min": 960}}
  - gpa_requirement: 3.0+ ⟵ “Deans' Scholarship | $15,000.00 | 3.0+ |  | 18+ |  | 960+”
  - test_requirement: ACT 18+ / SAT 960+ ⟵ “Deans' Scholarship | $15,000.00 | 3.0+ |  | 18+ |  | 960+”
### `c7d674c872c2306e` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 eac9e4c2acaa)
- checks: {"thresholds": {"act_min": 20, "gpa_min": 3.25, "sat_min": 1030}}
  - gpa_requirement: 3.25+ ⟵ “Maurelian Scholarship | $16,000.00 | 3.25+ |  | 20+ |  | 1030+”
  - test_requirement: ACT 20+ / SAT 1030+ ⟵ “Maurelian Scholarship | $16,000.00 | 3.25+ |  | 20+ |  | 1030+”
### `f97b0349295d6cc1` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 eac9e4c2acaa)
- checks: {"thresholds": {"act_min": 30, "sat_min": 1360}}
  - gpa_requirement: N/A ⟵ “30+ Club | $21,000.00 | N/A |  | 30+ |  | 1360+”
  - test_requirement: ACT 30+ / SAT 1360+ ⟵ “30+ Club | $21,000.00 | N/A |  | 30+ |  | 1360+”
### `m6f90f7bb41bec69` Columbia State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.columbiastate.edu/admissions/documents19/Dual_Enrollment_Grant_Students.pdf (sha256 4ba10c79893e)
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa", "state_grant_accepted"], "merged_pages": 4, "tiers": 1}
  - college_gpa_to_continue: 2.0 ⟵ “2. A student must maintain a cumulative 2.0 GPA for all college courses certified under the Dual Enrollment Grant”
  - state_grant_accepted: True ⟵ “(DEG). Students who do not maintain the minimum GPA will no longer be eligible for the DEG and may be”
  - state_grant_accepted: True ⟵ “The only financial aid Dual Enrollment students are eligible for is the Dual Enrollment Grant.”
  - state_grant_accepted: True ⟵ “To learn more about the Dual Enrollment Grant and to apply, go to Dual Enrollment.”
  - eligibility_tier: 3.2 ⟵ “Academically Talent and Gifted students are currently enrolled in a TN high school, have a 3.2 or higher GPA and have an Individualized Educational Program (IEP) in which college courses are recommended.”
  - eligibility_tier: 3.6 ⟵ “not taken the ACT/SAT or doesn’t have a 3.6 cumulative GPA, they can schedule a placement exam (once admitted) with”
  - state_grant_accepted: True ⟵ “Visit www.tn.gov/CollegePays to apply. TSAC has strict Dual Enrollment Grant application”
  - state_grant_accepted: True ⟵ “• To remain eligible for the Dual Enrollment GRANT each semester, students must maintain a 2.0”
  - college_gpa_to_continue: 2.0 ⟵ “• To remain eligible for the Dual Enrollment GRANT each semester, students must maintain a 2.0”
### `96c1a5a25b7256f3` Dyersburg State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.dscc.edu/dual-enrollment/ (sha256 eee651926101)
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "tiers": 1}
  - state_grant_accepted: True ⟵ “Are eligible to receive the Dual Enrollment Grant.”
  - eligibility_tier: 3.0 ⟵ “Submit an official copy of your high school transcript indicating a 3.0 grade point average (on a 4.0 scale) as well as ACT scores.”
  - state_grant_accepted: True ⟵ “Apply for the Tennessee Dual Enrollment Grant”
  - state_grant_accepted: True ⟵ “Apply for the Dual Enrollment Grant each semester by these deadlines:”
### `585a7b789ef7b7d1` East Tennessee State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php (sha256 1c8b6a0cbbba)
- checks: {"thresholds": null}
  - award_amount_text: Provides In-StateTuition Rate ⟵ “More Info | Public Service Corps Scholarship | Provides In-StateTuition Rate | N/A | See Requirements”
  - gpa_requirement: N/A ⟵ “More Info | Public Service Corps Scholarship | Provides In-StateTuition Rate | N/A | See Requirements”
  - test_requirement: ACT See Requirements / SAT See Requirements ⟵ “More Info | Public Service Corps Scholarship | Provides In-StateTuition Rate | N/A | See Requirements”
### `c48e22b72c8c2caa` East Tennessee State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php (sha256 1c8b6a0cbbba)
- checks: {"thresholds": {"gpa_min": 3.2}}
  - award_amount_text: Provides In-StateTuition Rate ⟵ “More Info | STEM Community Outreach Scholarship | Provides In-StateTuition Rate | 3.2 | See Requirements”
  - gpa_requirement: 3.2 ⟵ “More Info | STEM Community Outreach Scholarship | Provides In-StateTuition Rate | 3.2 | See Requirements”
  - test_requirement: ACT See Requirements / SAT See Requirements ⟵ “More Info | STEM Community Outreach Scholarship | Provides In-StateTuition Rate | 3.2 | See Requirements”
### `e51adf3359bfad02` East Tennessee State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php (sha256 1c8b6a0cbbba)
- checks: {"thresholds": null}
  - award_amount_text: Provides In-StateTuition Rate ⟵ “More Info | Creative Arts Scholarship | Provides In-StateTuition Rate | See Requirements | See Requirements”
  - gpa_requirement: See Requirements ⟵ “More Info | Creative Arts Scholarship | Provides In-StateTuition Rate | See Requirements | See Requirements”
  - test_requirement: ACT See Requirements / SAT See Requirements ⟵ “More Info | Creative Arts Scholarship | Provides In-StateTuition Rate | See Requirements | See Requirements”
### `fbf7ce5c78359ff1` East Tennessee State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.etsu.edu/admissions/dual_enrollment/ (sha256 f50a621e2adf)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted"], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “3.0 or higher high school GPA on a 4.0 scale”
  - per_credit_hour_charge: 100 ⟵ “enrollment grant. After the first five free classes, the grant will provide $100/credit”
  - eligibility_tier: 3.0 ⟵ “Dual Enrollment students who present a 3.0 or higher high school GPA, may qualify”
  - state_grant_accepted: True ⟵ “Students admitted as dual enrollment students may be eligible for the Dual Enrollment Grant. In addition, students may qualify for an ETSU Dual Enrollment Scholarship. Consult”
### `6b6f158855599e37` Jackson State Community College — credit_policies 2026-27 · policy_kind=CLEP [changed] (source_unlabeled)
- source: https://jscc.edu/admissions/prior-learning/equivalency-exams/ (sha256 e188ca9a6ea3)
- checks: {"distinct_exams": 33, "equivalencies": 36, "rows_without_score": 0}
- change equivalency clepamericangovernment score 50: `3` → `POLS 1030 American Government`
- change equivalency clepamericanliterature score 50: `6` → `ENGL 2110 Early American Literature & ENGL 2120 Modern American Literature`
- change equivalency clepanalyzinginterpretingliterature score 50: `6` → `Credit for Literature Requirement or specific ENGL course`
- change equivalency clepbiology score 50: `8` → `BIOL 1110 & 1120 General Biology I & II`
- change equivalency clepcalculus score 50: `4` → `MATH 1910 Calculus`
- change equivalency clepchemistry score 50: `8` → `CHEM 1110 & 1120 General Chemistry I & II`
- change equivalency clepcollegealgebra score 50: `3` → `MATH 1130 College Algebra or MATH 1630 Finite Mathematics`
- change equivalency clepcollegecomposition score 50: `6` → `ENGL 1010 & 1020 Composition I & II`
- change equivalency clepcollegecompositionmodular score 50: `3/6` → `ENGL 1010 & 1020 Composition I & II`
- change equivalency clepcollegemathematics score 50: `3` → `MATH 1010 Math for General Studies`
- change equivalency clepenglishliterature score 50: `6` → `ENGL 2210 Early British Literature and ENGL 2220 Modern British Literature`
- change equivalency clepfinancialaccounting score 50: `3` → `ACCT 1010 Principles of Accounting I`
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | POLS 1030 American Government”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 6 | ENGL 2110 Early American Literature & ENGL 2120 Modern American Literature”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | 6 | Credit for Literature Requirement or specific ENGL course”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 8 | BIOL 1110 & 1120 General Biology I & II”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 4 | MATH 1910 Calculus”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 8 | CHEM 1110 & 1120 General Chemistry I & II”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 | MATH 1130 College Algebra or MATH 1630 Finite Mathematics”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition (also Freshmen) | 50 | 6 | ENGL 1010 & 1020 Composition I & II”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 3/6 | ENGL 1010 & 1020 Composition I & II”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | MATH 1010 Math for General Studies”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 6 | ENGL 2210 Early British Literature and ENGL 2220 Modern British Literature”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 | ACCT 1010 Principles of Accounting I”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, level 1 | 50 | 6 | FREN 1010 & 1020 Beginning French I & II”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, level II | 59 | 12 | FREN 1010 & 1020 Beginning French I & II FREN 2010 & 2020 Intermediate French I & II”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, level 1*** | 50 | 6 | GERM 1010 & 1020 Beginning German I & II”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language, level II*** | 60 | 12 | GERM 1010 & 1020 Beginning German I & II GERM 2010 & 2020 Intermediate German I & II”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | 3 | HIST 2010 Early American History”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | 3 | HIST 2020 Modern American History”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | PSYC 2130 Lifespan Psychology”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 6 | HUM 1010 Early Humanities and HUM 1020 Modern Humanities”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | 3 | INFS 1010 Computer Applications”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | 3 | EDUC 2210 Educational Psychology”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | BUSN 2370 Legal Environment of Business”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | PSYC 1030 General Psychology”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | SOCI 1010 Introduction to Sociology”
  - … 11 more rows
### `8310ce0226644cf2` Jackson State Community College — credit_policies 2026-27 · policy_kind=AP [same] (source_unlabeled)
- source: https://jscc.edu/admissions/prior-learning/equivalency-exams/ (sha256 e188ca9a6ea3)
- checks: {"distinct_exams": 38, "equivalencies": 56, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3,4,5]:  ⟵ “African American Studies | 3,4,5 | 3 SCH | HIST 2060 African American History”
  - equivalencies[AP-ART-HISTORY|3,4,5]:  ⟵ “Art History | 3,4,5 | 3 SCH | ARTH 2010 Art History I”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 SCH | BIOL 1110 General Biology I”
  - equivalencies[AP-BIOLOGY|4,5]:  ⟵ “Biology | 4,5 | 8 SCH | BIOL 1110 & 1120 General Biology I & II”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 3 SCH | MATH 1830 Applied Calculus”
  - equivalencies[AP-CALCULUS-AB|4,5]:  ⟵ “Calculus AB | 4,5 | 3 SCH | MATH 1830 Applied Calculus or MATH 1910 Calculus I”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 4 SCH | MATH 1910 Calculus I or MATH 1920 Calculus II”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 SCH | CHEM 1110 General Chemistry I”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 8 SCH | CHEM 1110 General Chemistry I & CHEM 1120 General Chemistry II”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture*** | 3 | 6 SCH | 1010 & 1020 Beginning Language I & 2”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture*** | 4 | 9 SCH | 1010, 1020, & 2010 Intermediate Language I”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language & Culture*** | 5 | 12 SCH | 1010, 1020, 2010, & 2020 Intermediate Language II”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4,5]:  ⟵ “Computer Science A | 4,5 | 4 SCH | CISP 1010 Computer Science I”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3,4,5]:  ⟵ “Computer Science Principles | 3,4,5 | 3 SCH | CITC 1301 Introduction to Programming and Logic Design”
  - equivalencies[AP-MACROECONOMICS|3,4,5]:  ⟵ “Macroeconomics | 3,4,5 | 3 SCH | ECON 2010 Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|3,4,5]:  ⟵ “Microeconomics | 3,4,5 | 3 SCH | ECON 2020 Microeconomics”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language | 3 | 3 SCH | ENGL 1010 Composition I”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4,5]:  ⟵ “English Language | 4,5 | 6 SCH | ENGL 1010 Composition I & ENGL 1020 Composition II”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3,4,5]:  ⟵ “English Literature | 3,4,5 | 6 SCH | ENGL 2210 & 2220 Survey of British Literature I & II”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3,4,5]:  ⟵ “Environmental Science | 3,4,5 | 4 SCH | BIOL 1510 Environmental Science I”
  - equivalencies[AP-EUROPEAN-HISTORY|3,4,5]:  ⟵ “European History*** | 3,4,5 | 6 SCH | HIST 1010 & 1020 Survey of Western Civilization I, II”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | 6 SCH | FREN 1010 & 1020 Beginning French I & II”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language & Culture | 4 | 9 SCH | FREN 1010, 1020, & 2010 Intermediate French I”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture | 5 | 12 SCH | FREN 1010, 1020, 2010 & 2020 Intermediate French II”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture*** | 3 | 6 SCH | 1010 & 1020 Beginning Language I & 2”
  - … 31 more rows
### `m480a8d25c2a85e8` Johnson University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://johnsonu.edu/admissions/dual-enrollment-students-how-to-apply/online/ (sha256 0609b73fc10f)
- checks: {"fields": ["per_credit_hour_charges"], "merged_pages": 2, "tiers": 0}
  - per_credit_hour_charge: 179.55 ⟵ “The cost for a dual enrollment course is $179.55 per credit, or $538.65 for a typical 3-credit course. The Tennessee Dual Enrollment Grant currently pays $538.65 per course for the first five courses and $100 per credit for courses 6-10. Click here to learn more about the grant!”
  - per_credit_hour_charge: 100 ⟵ “The cost for a dual enrollment course is $179.55 per credit, or $538.65 for a typical 3-credit course. The Tennessee Dual Enrollment Grant currently pays $538.65 per course for the first five courses and $100 per credit for courses 6-10. Click here to learn more about the grant!”
  - per_credit_hour_charge: 184 ⟵ “The cost is $184 per credit or $552 for a 3-credit course. The Tennessee Dual Enrollment Grant pays $554.40 per course for the first five courses.”
### `35c687a1705aeb71` Johnson University — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://johnsonu.edu/admissions/transfer-students/ (sha256 6c0c3bd4f7e4)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Here’s how it works: ✔ Credits are reviewed to see how they apply to your intended degree ✔ Courses with a grade of C or better are generally eligible for transfer If you completed an associate degree through Tennessee community colleges under the Tennessee Transfer Pathways, Johnson University may accept ALL 60 credits toward degree requirements.”
### `b86467f1a90f16a4` King University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.king.edu/academics/high-school-dual-enrollment/ (sha256 a8108878e13d)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a 3.0 GPA or higher”
### `e0e181c47f3214e7` Lane College — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.lanecollege.edu/admissions/transfers-and-readmission (sha256 3a08b35db3ba)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C ⟵ “Students who transfer will be awarded credit for all courses which parallel the Lane College curriculum, and for which a grade of “C” or higher was earned.”
  - max_transfer_credits: 68 ⟵ “A maximum of 68 semester hours (102 quarter hours) will be accepted as transfer credit.”
### `e90e275de89497c7` Lee University — admissions_metrics 2025-26 [same] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/2025-2026-CDS-1-1.pdf (sha256 2789690c4071)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 2481 ⟵ “Total applied                                                                          2,481”
  - admits: 1771 ⟵ “Total admitted                                                                         1,771”
  - enrolled: 570 ⟵ “Total enrolled                                                                          570”
  - sat_composite_25..75: [1030, 1120, 1230] ⟵ “SAT Composite                                                        1030                               1120                               1230”
  - sat_reading_25..75: [530, 570, 640] ⟵ “SAT Evidence-Based Reading and Writing                               530                                570                                640”
  - sat_math_25..75: [490, 540, 600] ⟵ “SAT Math                                                             490                                540                                600”
  - act_25..75: [20, 23, 27] ⟵ “ACT Composite                                                         20                                 23                                 27”
### `7dff415b8952981c` Lipscomb University — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://lipscomb.edu/admission/tuition-and-financial-aid/cost-attendance (sha256 4fe1468ec981)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition & Fees: 44486 ⟵ “Tuition & Fees | $44,486 | $44,486 | $44,486”
  - on_campus:Housing: 11044 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - on_campus:Food: 6988 ⟵ “Food | $6,988** | $3,034 | $2,020”
  - on_campus:Books & Supplies: 1800 ⟵ “Books & Supplies | $1,800 | $1,800 | $1,800”
  - on_campus:Personal Expenses: 2530 ⟵ “Personal Expenses | $2,530 | $2,530 | $2,530”
  - on_campus:Transportation: 2314 ⟵ “Transportation | $2,314 | $2,314 | $2,314”
  - on_campus:Loan Fees: 48 ⟵ “Loan Fees | $48 | $48 | $48”
  - on_campus:Total: 69210 ⟵ “Total | $69,210 | $67,452 | $57,698”
  - off_campus_not_with_family:Tuition & Fees: 44486 ⟵ “Tuition & Fees | $44,486 | $44,486 | $44,486”
  - off_campus_not_with_family:Housing: 13240 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - off_campus_not_with_family:Food: 3034 ⟵ “Food | $6,988** | $3,034 | $2,020”
  - off_campus_not_with_family:Books & Supplies: 1800 ⟵ “Books & Supplies | $1,800 | $1,800 | $1,800”
  - off_campus_not_with_family:Personal Expenses: 2530 ⟵ “Personal Expenses | $2,530 | $2,530 | $2,530”
  - off_campus_not_with_family:Transportation: 2314 ⟵ “Transportation | $2,314 | $2,314 | $2,314”
  - off_campus_not_with_family:Loan Fees: 48 ⟵ “Loan Fees | $48 | $48 | $48”
  - off_campus_not_with_family:Total: 67452 ⟵ “Total | $69,210 | $67,452 | $57,698”
  - with_parents_or_family:Tuition & Fees: 44486 ⟵ “Tuition & Fees | $44,486 | $44,486 | $44,486”
  - with_parents_or_family:Housing: 4500 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - with_parents_or_family:Food: 2020 ⟵ “Food | $6,988** | $3,034 | $2,020”
  - with_parents_or_family:Books & Supplies: 1800 ⟵ “Books & Supplies | $1,800 | $1,800 | $1,800”
  - with_parents_or_family:Personal Expenses: 2530 ⟵ “Personal Expenses | $2,530 | $2,530 | $2,530”
  - with_parents_or_family:Transportation: 2314 ⟵ “Transportation | $2,314 | $2,314 | $2,314”
  - with_parents_or_family:Loan Fees: 48 ⟵ “Loan Fees | $48 | $48 | $48”
  - with_parents_or_family:Total: 57698 ⟵ “Total | $69,210 | $67,452 | $57,698”
### `af194fcdca8f55e5` Lipscomb University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://lipscomb.edu/admission/transfer-admission/transferring-credit?_gl=1%2A13kx7ol%2A_up%2AMQ..%2A_ga%2ANTMwNDcyNDQxLjE3ODQ5MDQyNDk.%2A_ga_42WYYDFCEN%2AczE3ODQ5MDQyNDgkbzEkZzEkdDE3ODQ5MDQ3OTEkajYwJGwwJGgxMzM2NDI3Mzc4 (sha256 3c07c517dacd)
- checks: {"distinct_exams": 24, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | Survey of American Literature | 50 | Literary Inquiry”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | Survey of English Literature | 50 | Literary Inquiry”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|55]:  ⟵ “College Composition | EN 1113 Freshman Comp. & Reading I or 3 hours elective credit | 55 | Elective”
  - equivalencies[CLEP-FRENCH-LANGUAGE|48]:  ⟵ “College French (Level I) | FR 1114 | 48 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-FRENCH-LANGUAGE|52]:  ⟵ “College French (Level I) | FR 1114 and 1124 | 52 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-FRENCH-LANGUAGE|56]:  ⟵ “College French (Level II) | FR 1114, 1124 and 2114 | 56 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “College French (Level II) | FR 1114, 1124, 2114, and 2124 | 62 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-GERMAN-LANGUAGE|48]:  ⟵ “College German (Level I) | GE 1114 | 48 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-GERMAN-LANGUAGE|52]:  ⟵ “College German (Level I) | GE 1114 and 1124 | 52 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-GERMAN-LANGUAGE|56]:  ⟵ “College German (Level II) | GE 1114, 1123, and 2114 | 56 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “College German (Level II) | GE 1114, 1124, 2114 and 2124 | 63 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-SPANISH-LANGUAGE|48]:  ⟵ “College Spanish (Level I) | SN 1114 | 48 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-SPANISH-LANGUAGE|54]:  ⟵ “College Spanish (Level I) | SN 1114 and 1124 | 54 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-SPANISH-LANGUAGE|60]:  ⟵ “College Spanish (Level II) | SN 1114, 1124, and 2114 | 60 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-SPANISH-LANGUAGE|66]:  ⟵ “College Spanish (Level II) | SN 1114, 1124, 2114, and 2124 | 66 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | PO 1023 Introduction to American Government | 50 | Great Ideas in Politics”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Develop. | PS 2423 Life Span Development | 50 | Social Inquiry”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psychology | PS 3243 Human Development and Learning | 50 | Social Inquiry”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | EC 2403 Principles of Macroeconomics | 50 | Social Inquiry”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | EC 2413 Principles of Microeconomics | 50 | Social Inquiry”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PS 1113 Introduction to Psychology | 50 | Solical Inquiry”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | SO 1123 Introduction to Sociology | 50 | Social Inquiry”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | HI 1113 Foundations of Western Civilization to 1600 | 50 | Great Ideas in History”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: -1648 to present | HI 1123 Foundations of Western Civilization since 1600 | 50 | Great Ideas in History”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus with Elem. Func. | MA 1314 Calculus I | 50 | Quantitative Reasoning, B.S. Hours”
  - … 9 more rows
### `f6b61f70ba86ad1d` Lipscomb University — credit_policies 2026-27 · policy_kind=AP [same] (source_unlabeled)
- source: https://lipscomb.edu/admission/transfer-admission/transferring-credit (sha256 a7ffd3af7b5c)
- checks: {"distinct_exams": 31, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|No credit]:  ⟵ “American Gov./Pol. | No credit | PO 1023 | Same as 4 | 3 | Great Ideas in Politics”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|No credit]:  ⟵ “Comparative Gov./Pol. | No credit | PO 1013 | Same as 4 | 3 | Great Ideas in Politics”
  - equivalencies[AP-UNITED-STATES-HISTORY|No credit]:  ⟵ “American History | No credit | HI 2213 | Same as 4 | 3 | Great Ideas in History”
  - equivalencies[AP-EUROPEAN-HISTORY|No credit]:  ⟵ “European History | No credit | HI 1113 | Same as 4 | 3 | Great Ideas in History”
  - equivalencies[AP-WORLD-HISTORY-MODERN|No credit]:  ⟵ “World History | No credit | HI 1013 | Same as 4 | 3 | Great Ideas in History”
  - equivalencies[AP-MACROECONOMICS|EC 2403]:  ⟵ “Macroeconomics | EC 2403 | Same as 3 | Same as 3 & 4 | 3 | Social Inquiry”
  - equivalencies[AP-MICROECONOMICS|EC 2413]:  ⟵ “Microeconomics | EC 2413 | Same as 3 | Same as 3 & 4 | 3 | Social Inquiry”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|EN 1113]:  ⟵ “English Lang. and Comp.* | EN 1113 | Same as 3 | Same as 3 & 4 | 3 | Elective”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|EN 1113]:  ⟵ “English Lit. and Comp.* | EN 1113 | Same as 3 | Same as 3 & 4 | 3 | Elective”
  - equivalencies[AP-ART-HISTORY|AR 4813]:  ⟵ “Art History | AR 4813 | Same as 3 | Same as 3 & 4 | 3 | Artistic Inquiry”
  - equivalencies[AP-2-D-ART-DESIGN|AR 1033]:  ⟵ “Studio Art- 2-D Design* | AR 1033 | Same as 3 | Same as 3 & 4 | 3 | Artistic Inquiry”
  - equivalencies[AP-3-D-ART-DESIGN|AR 1033]:  ⟵ “Studio Art- 3-D Design* | AR 1033 | Same as 3 | Same as 3 & 4 | 3 | Artistic Inquiry”
  - equivalencies[AP-DRAWING|AR 1033]:  ⟵ “Studio Art-Drawing* | AR 1033 | Same as 3 | Same as 3 & 4 | 3 | Artistic Inquiry”
  - equivalencies[AP-MUSIC-THEORY|No credit]:  ⟵ “Music Theory | No credit | MU 1111, MU 1133 | MU 1111, MU 1121MU 1133, MU 1143 | 8 | Artistic Inquiry”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|FR 1114]:  ⟵ “French Language | FR 1114 | FR 1114, FR 1124, & FR 2114 | FR 1114, FR 1124, FR 2114, & FR 2124 | 16 | B.A. Foreign Language Hours”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|GE 1114]:  ⟵ “German Language | GE 1114 | GE 1114, GE 1124 & GE 2114 | GE 1114, GE 1124, GE 2114, & GE 2124 | 16 | B.A. Foreign Language Hours”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|SN 1114]:  ⟵ “Spanish Language | SN 1114 | SN 1114, SN 1124 & SN 2114 | SN 1114, SN 1124, SN 2114, & SN 2124 | 16 | B.A. Foreign Language Hours”
  - equivalencies[AP-STATISTICS|MA2183]:  ⟵ “Statistics | MA2183 | Same as 3 | Same as 3 & 4 | 3 | Quantitative reason, B.S. hours”
  - equivalencies[AP-CALCULUS-AB|No Credit]:  ⟵ “Calculus AB* | No Credit | MA 1314 | Same as 4 | 4 | Quantitative reason, B.S. hours”
  - equivalencies[AP-CALCULUS-BC|MA 1314]:  ⟵ “Calculus BC* | MA 1314 | MA 1314 & MA 2314 | Same as 4 | 8 | Quantitative reason, B.S. hours”
  - equivalencies[AP-PRECALCULUS|No Credit]:  ⟵ “Precalculus | No Credit | MA 1123 or MA 1135 | Same as 4 | 5 | Quantitative reason, B.S. hours”
  - equivalencies[AP-COMPUTER-SCIENCE-A|CS 1213]:  ⟵ “Computer Science A | CS 1213 | Same as 3 | Same as 3 & 4 | 6 | B.S. Hours”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|CCT 1133]:  ⟵ “Computer Science Principles | CCT 1133 | Same as 3 | Same as 3 & 4 | 3 | B.S. Hours”
  - equivalencies[AP-BIOLOGY|BY 1003]:  ⟵ “Biology* | BY 1003 | BY 1003 | BY1144 | 3 | Score of 3 or 4: Hours towards science requirement; Score of 5: Science requirement fully met; All scores: B.S. hours”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|BY 1003]:  ⟵ “Environmental Science* | BY 1003 | BY 1003, or BY 1013, or ESS 1013 | Same as 4 | 3 | Hours toward science requirement; B.S. hours”
  - … 6 more rows
### `6c868df4e11f9925` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 a75bff557ffe)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $5,000 per year. Renewable for eight fall/spring semesters of full-time study with 2.75 GPA ⟵ “Art & Design ScholarshipOpen to all artists based on individual talent. | $500 to $5,000 per year. Renewable for eight fall/spring semesters of full-time study with 2.75 GPA”
### `8f6532afaab402a4` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 a75bff557ffe)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $5,000 per year. Renewable for eight fall/spring semesters of full-time study with 2.75 GPA ⟵ “Theatre ScholarshipOpen to all actors and/or theatre technicians. | $500 to $5,000 per year. Renewable for eight fall/spring semesters of full-time study with 2.75 GPA”
### `cabd5a42f51b43dd` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 d7000dce9f61)
- checks: {"thresholds": null}
  - gpa_requirement: Covenant Stone Scholarship3.5+ GPA. ⟵ “Covenant Stone Scholarship3.5+ GPA. | Up to $22,000 per year on-campus. Up to $16,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.5 GPA.”
  - award_amount_text: Up to $22,000 per year on-campus. Up to $16,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.5 GPA. ⟵ “Covenant Stone Scholarship3.5+ GPA. | Up to $22,000 per year on-campus. Up to $16,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.5 GPA.”
### `cb414eb449592ab1` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 d7000dce9f61)
- checks: {"thresholds": null}
  - gpa_requirement: Kin Takahashi Scholarship2.75+ GPA. ⟵ “Kin Takahashi Scholarship2.75+ GPA. | Up to $16,000 per year on-campus. Up to $10,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
  - award_amount_text: Up to $16,000 per year on-campus. Up to $10,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA. ⟵ “Kin Takahashi Scholarship2.75+ GPA. | Up to $16,000 per year on-campus. Up to $10,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
### `ea62da14b832ed83` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 d7000dce9f61)
- checks: {"thresholds": null}
  - gpa_requirement: Orange & Garnet Scholarship3.0+ GPA. ⟵ “Orange & Garnet Scholarship3.0+ GPA. | Up to $18,000 per year on-campus. Up to $12,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
  - award_amount_text: Up to $18,000 per year on-campus. Up to $12,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA. ⟵ “Orange & Garnet Scholarship3.0+ GPA. | Up to $18,000 per year on-campus. Up to $12,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
### `efe8f46637c6a8e7` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 d7000dce9f61)
- checks: {"thresholds": null}
  - gpa_requirement: MC Scots Scholarship3.25+ GPA. ⟵ “MC Scots Scholarship3.25+ GPA. | Up to $20,000 per year on-campus. Up to $14,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
  - award_amount_text: Up to $20,000 per year on-campus. Up to $14,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA. ⟵ “MC Scots Scholarship3.25+ GPA. | Up to $20,000 per year on-campus. Up to $14,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
### `e875a5d6c61b8d94` Maryville College — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.maryvillecollege.edu/admissions/tuition-and-fees/ (sha256 654ce4cb7eca)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition (Full-Time): 41300 ⟵ “Tuition (Full-Time) | $20,650 | $41,300”
  - column:Activity Fee: 512 ⟵ “Activity Fee | $256 | $512”
  - column:Orientation Fee (one time): 325 ⟵ “Orientation Fee (one time) | $325 | $325”
  - column:Service Fee: 472 ⟵ “Service Fee | $236 | $472”
  - column:Room (Basic rate – See all rates): 6880 ⟵ “Room (Basic rate – See all rates) | $3,440 | $6,880”
  - column:Meals (Scots Unlimited – See all plans): 7392 ⟵ “Meals (Scots Unlimited – See all plans) | $3,696 | $7,392”
  - column:TOTAL: 56881 ⟵ “TOTAL | $28,603 | $56,881”
### `1a5bcfce232355be` Mid-South Christian College — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.midsouthchristian.edu/transferability-of-credits (sha256 045a44f5d239)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Courses eligible for transfer must reflect a grade of C- or higher.”
### `401733d856d0ab8b` Middle Tennessee State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.mtsu.edu/dualenrollment/ (sha256 e9b66716b4ec)
- checks: {"fields": ["alt_min_act", "min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a minimum 3.0 high school GPA (if GPA is below 3.0, an ACT composite of 22 is acceptable)”
  - per_credit_hour_charge: 206.85 ⟵ “In many instances, there is no out-of-pocket tuition cost to students. This is made possible by a combination of state funding (the Dual Enrollment Grant) and MTSU funding. The standard in-state tuition rate for dual enrollment classes is $206.85 per credit hour. A 3- credit hour course is $620.55.”
### `mb99ffd462f4d734` Motlow State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.mscc.edu/students/high-school/dual-enrollment/index.html (sha256 a22cc9c445a7)
- checks: {"fields": ["college_gpa_to_continue", "state_grant_accepted"], "merged_pages": 3, "tiers": 1}
  - state_grant_accepted: True ⟵ “The DEG will pay in entirety for tuition for eligible students for courses 1 through”
  - per_credit_hour_charge: 100 ⟵ “5. For classes 6 through 10, eligible students will be awarded $100 per credit hour”
  - state_grant_accepted: True ⟵ “STAYING ELIGIBLE FOR THE DUAL ENROLLMENT GRANT”
  - eligibility_tier: 3.0 ⟵ “to take Dual       you must have an overall GPA of 3.0 or higher and a 3.0”
  - eligibility_tier: 3.0 ⟵ “classes?         an overall GPA of 3.0 or higher and an overall GPA of”
  - eligibility_tier: 2.5 ⟵ “must have an overall GPA of 2.5 or higher.”
  - eligibility_tier: 3.0 ⟵ “overall GPA of 3.0 or higher, in addition to”
  - state_grant_accepted: True ⟵ “you are automatically eligible to receive monies from the Dual Enrollment Grant”
  - state_grant_accepted: True ⟵ “The DEG applies to 10 courses; the breakdown of money distribution can be found in”
  - eligibility_tier: 3.0 ⟵ “3.0 High School GPA (2.5 GPA for CTE courses, such as Mechatronics) and a 3.0 GPA”
  - college_gpa_to_continue: 2.0 ⟵ “Students must maintain a 2.0 College GPA to receive the grant in future semesters”
  - state_grant_accepted: True ⟵ “The deadline to apply for the Dual Enrollment Grant is June 30 for all semesters”
### `08ae014800c04912` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Pete Faison Endowed Scholarship | Computer Information Technology students | Up to $1,000 per academic year”
### `0bf215abfdd69c18` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “ESL Ambassador Scholarship | All majors accepted | Up to $2,000 per academic year”
### `15f0b3efbe7374a6` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,000 per academic year ⟵ “Early Childhood Education Scholarship | Early Childhood Education student | Up to $3,000 per academic year”
### `1a24a1ebfbce9b1c` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “NSCC Foundation Endowed Scholarship | All majors accepted | Up to $1,000 per academic year”
### `1b665673d5d29996` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Roberts – Williams Memorial Scholarship | Computer Information Technology and Business students | Up to $1,000 per academic year”
### `1e442030ca3c5b43` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “Brian Uhl Scholarship | Culinary Arts students | Up to $2,000 per academic year”
### `1f8d4dab7dc6a129` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,372 per academic year ⟵ “The Doochin Family Scholarship | Formerly incarcerated individuals | Up to $5,372 per academic year”
### `2036b5ae177e02f5` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “Moe's Southwest Grill Scholarship | All majors accepted | Up to $2,000 per academic year”
### `2b7269104db3ed9b` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “Fuqua Family Endowed Scholarship | All majors accepted | Up to $2,000 per academic year”
### `431722ec04b38e1d` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Doug Jameson Memorial Scholarship | All majors accepted | Up to $500 per academic year”
### `4bdb4bdc2e25d275` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Ram Lal Seekri Endowed Scholarship | All Majors | Up to $500 per academic year”
### `55db957cb2510b9e` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Mary Elizabeth Williams Endowed Scholarship | All majors accepted | Up to $1,000 per academic year”
### `5cc4e7680de58516` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,250 per academic year ⟵ “Darrell Freeman Memorial Scholarship | Computer Information Technology, Computer Programming, or IT Support Specialist students | Up to $2,250 per academic year”
### `7628061ec5f99954` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “Dr. Wallace Wilson Scholarship | Architectural Engineering Technology, Civil and Construction Engineering Technology, Civil Engineering, and Mechanical Engineering students | Up to $2,000 per academic year”
### `7e2311a8e5137bcc` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Dickson High Noon Rotary Scholarship | All majors accepted | Up to $500 per academic year”
### `842e4d86c4d37252` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Cathy O'Bryant Memorial Endowed Scholarship | Visual Communications Photography students | Up to $1,000 per academic year”
### `854dff8ce0586670` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Jim Formosa Memorial Scholarship | Accounting students | Up to $500 per academic year”
### `867b823cb44dfa31` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $800 per academic year ⟵ “John E. Mayfield Endowed Scholarship | All majors accepted | Up to $800 per academic year”
### `868d7e175f10a792` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,500 per academic year ⟵ “Sanford E. Harper Endowed Scholarship | Business student | Up to $1,500 per academic year”
### `98bf512f2735c2ce` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “NSCC Foundation Culinary Arts Scholarship | Culinary Arts students | Up to $2,000 per academic year”
### `9b3138689bfc31d5` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,250 per academic year ⟵ “Oscar Lasko Endowment Scholarship | Engineering, Computer Science, or Manufacturing students | Up to $1,250 per academic year”
### `9c77d5dc2a3da7f4` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Lance Woodard Memorial Scholarship | All majors accepted | Up to $500 per academic year”
### `9da30260c2b9a9ff` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,500 per academic year ⟵ “Finish Line Scholarship | All majors accepted | Up to $1,500 per academic year”
### `9f73fd9dd160c437` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “NSCC Foundation Scholarship | All majors accepted | Up to $1,000 per academic year”
### `a54d3b5b11354600` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Jacob Roberts Memorial Endowed Scholarship | Computer Information Technology students | Up to $500 per academic year”
### `ae6bc7aa1d336a99` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,150 per academic year ⟵ “Randy Rayburn Culinary Arts Scholarship | Culinary Arts students | Up to $5,150 per academic year”
### `bebb0b4447845691` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,500 per academic year ⟵ “Danny Jackson Endowed Scholarship | All Majors | Up to $2,500 per academic year”
### `c89d501d4cd6c481` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,575 per academic year ⟵ “Jay Luther Memorial Scholarship | Culinary Arts students | Up to $2,575 per academic year”
### `d3ff405f7a0c5682` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Dorothy Gaubert Pyle Endowed Scholarship | Black and White Photography Students | Up to $1,000 per academic year”
### `d7b0ddb591de8b32` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “ISSA Scholarship | Cyber Defense students | Up to $2,000 per academic year”
### `dcbd6e32416bb56c` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Dr. Federick J. Berger Endowed Scholarship | Tennessee Beta Chapter, Tau Alpha Pi Honor Society Students | Up to $500 per academic year”
### `ee0e97f7404ba1c3` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,250 per academic year ⟵ “HCA Foundation Endowed Scholarship | Nursing or Surgical Technology students | Up to $1,250 per academic year”
### `eeededf6a9d2cfe1` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 per academic year ⟵ “21st Century Educational Foundation Scholarship | Humphreys County campus student | Up to $5,000 per academic year”
### `f65ae39bd9cd8352` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,500 per academic year ⟵ “Ted M. Washington Endowed Memorial Scholarship | Computer Information Technology students | Up to $1,500 per academic year”
### `f94e046175c21822` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “NSCC Foundation Ambassador Scholarship | All majors accepted | Up to $1,000 per academic year”
### `facbda2b6402a875` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $6,000 per academic year ⟵ “Funding Our Future | Ages 18-23 not eligible for TN Promise or TN Reconnect, resident of Humphreys, Stewart, Benton, or Perry counties, complete FAFSA, maintain 2.0 GPA, enrolled in at least two courses-one of which must be in-person at Humphreys County campus, enrolled in fall and spring semesters ”
### `fb4ac1be5a1c5b5d` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “NSCC Foundation OTA Scholarship | Occupational Therapy Assistant students | Up to $1,000 per academic year”
### `4b10a92ab2ce6077` Northeast State Community College — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/cost-of-attendance.html (sha256 883da26037d6)
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees*: 8848 ⟵ “Tuition and Fees* | $8,848 | $8,848”
  - with_parents_or_family:Living Expenses (Housing & Food): 7532 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - with_parents_or_family:Books and Supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - with_parents_or_family:Transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - with_parents_or_family:Personal Expenses: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - with_parents_or_family:Total: 23872 ⟵ “Total | $23,872 | $31,711”
  - off_campus_not_with_family:Tuition and Fees*: 8848 ⟵ “Tuition and Fees* | $8,848 | $8,848”
  - off_campus_not_with_family:Living Expenses (Housing & Food): 15371 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - off_campus_not_with_family:Books and Supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - off_campus_not_with_family:Transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - off_campus_not_with_family:Personal Expenses: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - off_campus_not_with_family:Total: 31711 ⟵ “Total | $23,872 | $31,711”
### `768a594551190e83` Northeast State Community College — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/cost-of-attendance.html (sha256 883da26037d6)
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees*: 5280 ⟵ “Tuition and Fees* | $5,280 | $5,280”
  - with_parents_or_family:Living Expenses (Housing & Food): 7532 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - with_parents_or_family:Books and Supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - with_parents_or_family:Transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - with_parents_or_family:Personal Expenses: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - with_parents_or_family:Total: 20304 ⟵ “Total | $20,304 | $28,143”
  - off_campus_not_with_family:Tuition and Fees*: 5280 ⟵ “Tuition and Fees* | $5,280 | $5,280”
  - off_campus_not_with_family:Living Expenses (Housing & Food): 15371 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - off_campus_not_with_family:Books and Supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - off_campus_not_with_family:Transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - off_campus_not_with_family:Personal Expenses: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - off_campus_not_with_family:Total: 28143 ⟵ “Total | $20,304 | $28,143”
### `fa900dc2bcf7b830` Rhodes College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.rhodes.edu/admission-aid/apply-rhodes/college-credit-transfer-policies (sha256 43f7e211ac84)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer courses taken on a Pass/Fail basis must be passed with a grade of C or better.”
### `10f26f0d105ca9b3` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “4,800-5,700 | Bronze | $2,000”
### `2e9a3be83f39702a` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “6,601 - 7,300 | Presidential | $24,000 | $6,000”
### `4f7aa062b0ba1193` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “4,800 - 5,700 | Honors | $8,000 | $2,000”
### `6548ae9c5d9fc74a` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 ⟵ “5,701-6,600 | Silver | $4,000”
### `ab27153023773714` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 ⟵ “5,701 - 6,600 | Dean | $16,000 | $4,000”
### `cae853055f3449e9` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “6,601 & higher | Gold | $6,000”
### `21f3f1ed23928c45` Southern Adventist University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.southern.edu/academics/online-campus/dual-enrollment.html (sha256 6a128f4d3663)
- checks: {"fields": ["max_credit_hours_per_term", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 3}
  - max_credit_hours_per_term: 6 ⟵ “with convenient online scheduling. Students may take up to 6 credit hours per semester”
  - per_credit_hour_charge: 200 ⟵ “through this program at a reduced fee of $200 per credit hour (textbooks and lab fees”
  - per_credit_hour_charge: 200 ⟵ “TUITION: $200 Per credit hour”
  - eligibility_tier: 3.0 ⟵ “High School Senior with GPA of 3.0+”
  - eligibility_tier: 3.5 ⟵ “High School Junior with GPA of 3.5+”
  - eligibility_tier: 3.5 ⟵ “GPA of 3.5+ (Jr & Sr.)”
  - per_credit_hour_charge: 200 ⟵ “Dual enrollment students can take advantage of the reduced tuition rate of $200 per credit hour. This does not include textbook or lab fees. Tennessee students may be eligible for”
### `26804fbd6793034d` Tennessee Technological University — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/cost.php (sha256 88176cba5638)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 17551 ⟵ “Tuition/Fees | $17,551 | $17,551”
  - on_campus:Housing: 7365 ⟵ “Housing | $7,365 | $8,403”
  - on_campus:Food: 7026 ⟵ “Food | $7,026 | $7,026”
  - on_campus:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - on_campus:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - on_campus:Personal Expenses: 2500 ⟵ “Personal Expenses | $2,500 | $2,500”
  - on_campus:TOTAL: 38522 ⟵ “TOTAL | $38,522 | $39,560”
  - with_parents_or_family:Tuition/Fees: 17551 ⟵ “Tuition/Fees | $17,551 | $17,551”
  - with_parents_or_family:Housing: 8403 ⟵ “Housing | $7,365 | $8,403”
  - with_parents_or_family:Food: 7026 ⟵ “Food | $7,026 | $7,026”
  - with_parents_or_family:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - with_parents_or_family:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - with_parents_or_family:Personal Expenses: 2500 ⟵ “Personal Expenses | $2,500 | $2,500”
  - with_parents_or_family:TOTAL: 39560 ⟵ “TOTAL | $38,522 | $39,560”
### `e0f3f4396a8b9c8f` Tennessee Technological University — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/cost.php (sha256 88176cba5638)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 12685 ⟵ “Tuition/Fees | $12,685 | $12,685”
  - on_campus:Housing: 7365 ⟵ “Housing | $7,365 | $8,403”
  - on_campus:Food: 7026 ⟵ “Food | $7,026 | $7,026”
  - on_campus:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - on_campus:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - on_campus:Personal Expenses: 2500 ⟵ “Personal Expenses | $2,500 | $2,500”
  - on_campus:TOTAL: 33656 ⟵ “TOTAL | $33,656 | $34,694”
  - with_parents_or_family:Tuition/Fees: 12685 ⟵ “Tuition/Fees | $12,685 | $12,685”
  - with_parents_or_family:Housing: 8403 ⟵ “Housing | $7,365 | $8,403”
  - with_parents_or_family:Food: 7026 ⟵ “Food | $7,026 | $7,026”
  - with_parents_or_family:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - with_parents_or_family:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - with_parents_or_family:Personal Expenses: 2500 ⟵ “Personal Expenses | $2,500 | $2,500”
  - with_parents_or_family:TOTAL: 34694 ⟵ “TOTAL | $33,656 | $34,694”
### `f22e1a0d94616e57` Tennessee Technological University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.tntech.edu/admissions/dualenrollment/cost.php (sha256 cbf78e500fea)
- checks: {"fields": ["state_grant_accepted"], "tiers": 0}
  - state_grant_accepted: True ⟵ “To be eligible for the TSAC Dual Enrollment Grant, you must:”
### `0c7714dbc070073e` Tennessee Technological University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://undergrad.catalog.tntech.edu/ugrequirements/transfertrack (sha256 5e7f23877f25)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Courses to be transferred under the stipulations of the University Track Module must have been completed with the grade of “C” or better.”
### `m6f95769cc6770bc` Tennessee Wesleyan University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: http://www.tnwesleyan.edu/admissions/undergraduate-admissions/dual-enrollment/ (sha256 27f20d15901f)
- checks: {"fields": ["per_credit_hour_charges", "state_grant_accepted"], "merged_pages": 3, "tiers": 0}
  - per_credit_hour_charge: 100 ⟵ “The Dual Enrollment Grant (DEG) through the state of Tennessee covers the cost of a student’s first five dual enrollment courses at Tennessee Wesleyan University. For courses 6-10, the DEG provides $100 per credit hour, making each three-hour course cost $213 which will be covered in full by TWU, me”
  - state_grant_accepted: True ⟵ “The Dual Enrollment Grant (DEG) through the state of Tennessee covers the cost of a student’s first five dual enrollment courses at Tennessee Wesleyan University. For courses 6-10, the DEG provides $100 per credit hour, making each three-hour course cost $213 which will be covered in full by TWU, me”
  - state_grant_accepted: True ⟵ “Cost fully covered by Dual Enrollment Grant (student must apply for DEG)”
  - state_grant_accepted: True ⟵ “Cost partially covered by Dual Enrollment Grant (student must apply for DEG), partially covered by TWU*.”
  - per_credit_hour_charge: 100 ⟵ “The Dual Enrollment Grant (DEG) through the state of Tennessee covers the cost of a student’s first five dual enrollment courses at Tennessee Wesleyan University. For courses 6-10, the DEG provides $100 per credit hour, making each three-hour course cost $213 which will be covered in full by TWU, me”
  - state_grant_accepted: True ⟵ “The Dual Enrollment Grant (DEG) through the state of Tennessee covers the cost of a student’s first five dual enrollment courses at Tennessee Wesleyan University. For courses 6-10, the DEG provides $100 per credit hour, making each three-hour course cost $213 which will be covered in full by TWU, me”
  - state_grant_accepted: True ⟵ “Cost fully covered by Dual Enrollment Grant (student must apply for DEG)”
  - state_grant_accepted: True ⟵ “Cost partially covered by Dual Enrollment Grant (student must apply for DEG), partially covered by TWU*.”
  - state_grant_accepted: True ⟵ “Commit Dual Enrollment Grant: I want to use my Dual Enrollment Grant to pay my bill and defer any remaining”
  - per_credit_hour_charge: 171 ⟵ “I acknowledge the cost of dual enrollment courses at $171 per credit hour. If the student does not pay for the class in”
  - per_credit_hour_charge: 100 ⟵ “enrollment classes, and $100 per credit hour for classes 6-10, resulting in a cost of $213 per 3-hour course. Finally, I”
### `11607cb26f92c638` The University of Tennessee-Chattanooga — credit_policies 2026-27 · policy_kind=CLEP [changed] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/clep (sha256 6611ab9c865c)
- checks: {"distinct_exams": 33, "equivalencies": 36, "rows_without_score": 0}
- change equivalency clepbiology score 50: `BIOL 1110/1110L & BIOL 1120/1120L` → `BIOL 1110/1110L & BIOL1120/1120L`
- change equivalency clepchemistry score 50: `CHEM 1110/1110L & CHEM 1120/1120L` → `CHEM1110/1110L & CHEM1120/1120L`
- change equivalency clepenglishliterature score 50: `ENGL 2230` → `ENGL2230`
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | PSPS 1010 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science or 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL 2130 | 3 | ”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | ENGL 1330 | 3 | Literature; 23GE Humanities & Fine Arts”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL 1110/1110L & BIOL1120/1120L | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH 1950 | 4 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM1110/1110L & CHEM1120/1120L | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH 1130 | 3 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENGL 1010 & ENGL 1020 | 6 | Rhetoric & Writing I/ Rhetoric & Writing II; 23GE Writing & Communication”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | ENGL 1020 | 3 | Rhetoric & Writing I/ Rhetoric & Writing II; 23GE Writing & Communication (1 course)”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MATH 1010 | 3 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL2230 | 3 | ”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACC 1XXX | 3 | ”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language Level 1 | 50 | FREN 1010 & FREN 1020 | 8 | 23GE Humanities & Fine Arts and 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language Level 2 | 59 | FREN 2110 & FREN 2120 | 6 | 23GE Humanities & Fine Arts and 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language Level 1 | 50 | GER 1010 & GER 1020 | 8 | 23GE Humanities & Fine Arts and 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language Level 2 | 60 | GER 2110 & GER 2120 | 6 | ”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | HIST 2010 | 3 | Historical Understanding; 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | HIST 2020 | 3 | Historical Understanding; 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PSY 2220 | 3 | ”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | ENGL 1150 | 3 | Literature or Thoughts, Values, and Beliefs; 23GE Humanities & Fine Arts”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | MGT 1XXX | 3 | ”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | EDUC 2XXX | 3 | ”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | BUS 1XXX | 3 | ”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSY 1010 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOC 1510 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - … 11 more rows
### `19d86a24f9ced2e2` The University of Tennessee-Chattanooga — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/admissions/dual-enrollment (sha256 61d75dbde145)
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Is your high school grade point average 3.0 or higher?”
  - state_grant_accepted: True ⟵ “3. Apply for Tennessee Dual Enrollment Grant”
  - state_grant_accepted: True ⟵ “Apply for TN DE Grant”
### `1cd65173cf2e4c70` The University of Tennessee-Chattanooga — credit_policies 2026-27 · policy_kind=AP [changed] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/ap-exam (sha256 f352fcedef67)
- checks: {"distinct_exams": 39, "equivalencies": 57, "rows_without_score": 0}
- change equivalency_count: `58` → `57`
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | ART 2140 & ART 2150 | 6 | Historical Understanding; 23GE Humanities & Fine Arts”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ART 2140 | 3 | Historical Understanding or Visual & Performing Arts; 23GE Humanities & Fine Arts”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 1110 & BIOL 1120 | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH 1950 | 4 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MATH 1950 & MATH 1960 | 8 | Mathematics; 23GE Quantitative Reasoning (1 course)”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry** | 5 | CHEM 1110/1110L & CHEM 1120/1120L | 8 | Lab Science; 23GE Natural Science Lecture/Lab (1 course)”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry** | 4 | CHEM 1110/1110L | 4 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language & Culture | 5 | FLNG 1010, FLNG 1020, FLNG 2110 & FLNG 2120 | 12 | ”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture | 4 | FLNG 1010, FLNG 1020 & FLNG 2110 | 9 | ”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | FLNG 1010 & FLNG 1020 | 6 | ”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics | 3 | PSPS Elective | 3 | Behavioral & Social Sciences”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | 4 | CPSC 1100 | 4 | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles | 4 | CPSC 1XXX | 3 | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language & Composition | 4 | ENGL 1010 & ENGL 1020 | 6 | Rhetoric & Writing I/ Rhetoric & Writing II; 23GE Writing & Communication”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition | 3 | ENGL 1010 | 3 | Rhetoric & Writing I; 23GE Writing & Communication”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition | 3 | ENGL 1330 | 3 | Literature; 23GE Humanities & Fine Arts”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ESC 1500 & ESC 1510 | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | HIST 2220 | 3 | Historical Understanding; 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture | 5 | FREN 1010, FREN 1020, FREN 2110 & FREN 2120 | 14 | 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language & Culture | 4 | FREN 1010, FREN 1020 & FREN 2110 | 11 | 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | FREN 1010 & FREN 1020 | 8 | 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language & Culture | 5 | GER 1010, GER 1020, GER 2110 & GER 2120 | 14 | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language & Culture | 4 | GER 1010, GER 1020 & GER 2110 | 11 | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture | 3 | GER 1010 & GER 1020 | 8 | ”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 1040 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - … 32 more rows
### `2dc615c03212b1a5` The University of Tennessee-Chattanooga — credit_policies 2026-27 · policy_kind=IB [same] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/ib-exam (sha256 5295dee7971b)
- checks: {"distinct_exams": 23, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|SL & HL]:  ⟵ “Biology | SL & HL | HL | 5,6, OR 7 | BIOL 1110 & BIOL 1120 | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[IB-BUSINESS-MANAGEMENT|SL & HL]:  ⟵ “Business Management | SL & HL | HL | 5,6, OR 7 | MGT 1XXX (Lower Division) | 3 | ”
  - equivalencies[IB-CHEMISTRY|SL & HL]:  ⟵ “Chemistry | SL & HL | HL | 5,6, OR 7 | CHEM 1110/1110L & CHEM 1120/1120L | 8 | Lab Science; 23GE Natural Science Lecture/Lab (1 course)”
  - equivalencies[IB-LATIN|SL & HL]:  ⟵ “Classical Languages-Latin | SL & HL | HL | 5,6, OR 7 | LAT 1010 & LAT 1020 | 6 | 23GE Humanities & Fine Arts”
  - equivalencies[IB-COMPUTER-SCIENCE|SL & HL]:  ⟵ “Computer Science | SL & HL | HL | 5,6, OR 7 | CPSC 1XXX | 3 | ”
  - equivalencies[IB-ECONOMICS|SL & HL]:  ⟵ “Economics | SL & HL | HL | 5,6, OR 7 | ECON 1010 & ECON 1020 | 6 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|SL Only]:  ⟵ “Environmental Systems & Societies | SL Only | SL | 5,6, OR 7 | ESC 1100 | 3 | Non-Lab Science; 23GE Natural Science Non-Lab”
  - equivalencies[IB-FILM|SL & HL]:  ⟵ “Film | SL & HL | HL | 5,6, OR 7 | THSP 2800 | 3 | Visual & Performing Arts; 23GE Humanities & Fine Arts”
  - equivalencies[IB-GEOGRAPHY|SL & HL]:  ⟵ “Geography | SL & HL | HL | 5,6, OR 7 | GEOG 1040 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - equivalencies[IB-GLOBAL-POLITICS|SL & HL]:  ⟵ “Global Politics | SL & HL | HL | 5,6, OR 7 | PSPS 1020 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science or 23GE Individual & Global Citizenship”
  - equivalencies[IB-HISTORY|SL & HL]:  ⟵ “History of Africa and the Middle East* | SL & HL | HL | 5,6, OR 7 | HIST 1XXX (Lower Division) | 3 | Historical Understanding; 23GE Humanities & Fine Arts”
  - equivalencies[IB-FRENCH|SL & HL]:  ⟵ “Language B-French | SL & HL | HL | 5,6, OR 7 | FREN 1010 & FREN 1020 | 8 | 23GE Humanities & Fine Arts; 23GE Individual & Global Citizenship”
  - equivalencies[IB-GERMAN|SL & HL]:  ⟵ “Language B-German | SL & HL | HL | 5,6, OR 7 | GER 1010 & GER 1020 | 8 | ”
  - equivalencies[IB-SPANISH|SL & HL]:  ⟵ “Language B-Spanish | SL & HL | HL | 5,6, OR 7 | SPAN 1010 & SPAN 1020 | 8 | 23GE Humanities & Fine Arts; 23GE Individual & Global Citizenship”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL & HL]:  ⟵ “Mathematics - Analysis & Approaches | SL & HL | HL | 5,6, OR 7 | MATH 1950 | 4 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL & HL]:  ⟵ “Mathematics - Analysis & Approaches | SL & HL | HL | 4 | MATH 1830 | 3 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL & HL]:  ⟵ “Mathematics - Analysis & Approaches | SL & HL | SL | 5,6, OR 7 | MATH 1010, MATH 1730 | 3, 4 | Mathematics; 23GE Quantitative Reasoning (2 courses)”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|SL & HL]:  ⟵ “Mathematics - Applications & Interpretation | SL & HL | HL | 5,6, OR 7 | MATH 1010, MATH 1730 | 3 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[IB-MUSIC|SL & HL]:  ⟵ “Music | SL & HL | HL | 5,6, OR 7 | MUS 1XXX (Lower Division) | 3 | ”
  - equivalencies[IB-PHILOSOPHY|SL & HL]:  ⟵ “Philosophy | SL & HL | HL | 5,6, OR 7 | PHIL 1010 | 3 | Thoughts, Values & Beliefs; 23GE Humanities & Fine Arts”
  - equivalencies[IB-PHYSICS|SL & HL]:  ⟵ “Physics | SL & HL | HL | 5,6, OR 7 | PHYS 1030/1030L & PHYS 1040/1040L | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[IB-PSYCHOLOGY|SL & HL]:  ⟵ “Psychology | SL & HL | HL | 5,6, OR 7 | PSY 1010 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|SL & HL]:  ⟵ “Social & Cultural Anthropology | SL & HL | HL | 5,6, OR 7 | ANTH 1200 | 3 | Non-Western Culture; 23GE Behavioral & Social Science or 23GE Individual & Global Citizenship”
  - equivalencies[IB-THEATRE|SL & HL]:  ⟵ “Theatre | SL & HL | HL | 5,6, OR 7 | THSP 1110 | 3 | Visual & Performing Arts; 23GE Humanities & Fine Arts”
  - equivalencies[IB-VISUAL-ARTS|SL & HL]:  ⟵ “3"Visual Arts" | SL & HL | HL | 5,6, OR 7 | ART 1XXX (Lower Division) | 3 | ”
### `693934574a10c83b` The University of Tennessee-Knoxville — awards 2026-27 [new] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/orange-white-scholarship/ (sha256 4083f167e10c)
- checks: {"thresholds": null}
  - test_requirement: 3.6+ GPA*,26-27 ACT**,1230-1290 SAT** ⟵ “3.6+ GPA*,26-27 ACT**,1230-1290 SAT** | $1,500 | $6,000 | $26,400”
  - award_amount_text: $1,500 ⟵ “3.6+ GPA*,26-27 ACT**,1230-1290 SAT** | $1,500 | $6,000 | $26,400”
### `7dbbc171f9db65dd` The University of Tennessee-Knoxville — awards 2026-27 [new] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/orange-white-scholarship/ (sha256 4083f167e10c)
- checks: {"thresholds": null}
  - test_requirement: 3.6–3.79 GPA*,28–36 ACT**,1300–1600 SAT** ⟵ “3.6–3.79 GPA*,28–36 ACT**,1300–1600 SAT** | $1,500 | $6,000 | $26,400”
  - award_amount_text: $1,500 ⟵ “3.6–3.79 GPA*,28–36 ACT**,1300–1600 SAT** | $1,500 | $6,000 | $26,400”
### `f18f9466c40d460a` The University of Tennessee-Knoxville — awards 2026-27 [new] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/next-chapter-scholarship-next-chapter-scholar-of-the-year-award/ (sha256 8689988779f9)
- checks: {"thresholds": null}
  - award_amount_text: Tuition & mandatory fees ⟵ “Next Chapter Scholar of the Year | Tuition & mandatory fees | Tuition & mandatory fees up to four years | n/a”
### `51b8e04e8633e256` Trevecca Nazarene University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.trevecca.edu/admissions/dual-enrollment (sha256 b4fa606769d8)
- checks: {"fields": ["per_credit_hour_charges", "state_grant_accepted"], "tiers": 0}
  - per_credit_hour_charge: 197 ⟵ “Trevecca offers a special rate for our dual enrollment courses. Dual enrollment courses are discounted to $620.55 per three-credit course ($197 per credit).”
  - state_grant_accepted: True ⟵ “Qualifying Tennessee students are eligible for the Tennessee Dual Enrollment Grant, which is a part of the Tennessee HOPE Scholarship. Visit collegeforTN.org for more information and to apply for the grant.”
### `e1c8b31d689f9b97` Tusculum University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://site.tusculum.edu/apply-visit/apply/dual-enrollment/payment-models/ (sha256 8490c552aa9d)
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted"], "tiers": 1}
  - state_grant_accepted: True ⟵ “Here are some examples of course tuition payment plans using the Tennessee Dual Enrollment Grant and the Tusculum Access Grant. Eligible students can apply to receive grant funding through the Tennessee Dual Enrollment Grant. Students can receive tuition funding for additional courses as shown from ”
  - eligibility_tier: 2.75 ⟵ “2.75 high school GPA to get in OR successful admission appeal”
  - college_gpa_to_continue: 2.0 ⟵ “Maintain a 2.0 College GPA”
  - per_credit_hour_charge: 197 ⟵ “The models are tuition only based on 3 credit hour courses. For courses that are less or more than 3 credit hours, the tuition will be billed at $197 per credit hour with a Dual Enrollment fee of $9.55 per credit hour.”
  - per_credit_hour_charge: 9.55 ⟵ “The models are tuition only based on 3 credit hour courses. For courses that are less or more than 3 credit hours, the tuition will be billed at $197 per credit hour with a Dual Enrollment fee of $9.55 per credit hour.”
  - state_grant_accepted: True ⟵ “For courses 1-5, an eligible Dual Enrollment Grant student shall have the tuition and general fee paid for and shall only be responsible for books and course fees.”
  - per_credit_hour_charge: 100 ⟵ “For courses 6-10, the student shall receive $100 per credit hour in the Dual Enrollment Grant. If the student has taken all courses with Tusculum, they shall receive the difference of tuition and the general fee in Tusculum Access Grant funding. Tusculum will also pay the tuition and general fee for”
  - state_grant_accepted: True ⟵ “For courses 6-10, the student shall receive $100 per credit hour in the Dual Enrollment Grant. If the student has taken all courses with Tusculum, they shall receive the difference of tuition and the general fee in Tusculum Access Grant funding. Tusculum will also pay the tuition and general fee for”
### `e4ddb730106d6d6a` Walters State Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://ws.edu/admissions/prior-learning/exams/clep/index.aspx (sha256 ef41ef8f7f6f)
- checks: {"distinct_exams": 31, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government || 50 | 3 | POLS 1030”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature || 50 | 6 | ENGL 2110 & 2120”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature || 50 | 6 | Credit for Literature Requirement or Specific ENGL Course”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology || 50 | 8 | BIOL 1110/1011 & 1120/1121”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus || 50 | 4 | MATH 1910”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry || 50 | 8 | CHEM 1110 & 1120”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra || 50 | 3 | MATH 1630”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition (also Freshman) || 50 | 6 | ENGL 1010 & 1020”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular || 50 | 3/6 | ENGL 1010 & 1020”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics || 50 | 3 | MATH 1010 Math for Liberal Arts OR Credit for College-level Mathematics Requirement”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature || 50 | 6 | ENGL 2010 & 2020 OR ENGL 2210 & 2220”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting || 50 | 3 | ACCT 1010”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level I || 50 | 6 | FREN 1010 & 1020”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, Level II || 59 | 12 | FREN 1010, 1020, 2010 & 2020”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level I || 50 | 6 | GERM 1010 & 1020”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language, Level II || 60 | 12 | GERM 1010, 1020, 2010 & 2020”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I || 50 | 3 | HIST 2010”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II || 50 | 3 | HIST 2020”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development || 50 | 3 | PSYC 2130”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities || 50 | 6 | HUM 2010 & 2110”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications || 50 | 3 | INFS 1010”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law || 50 | 3 | BUSN 2510”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology || 50 | 3 | PSYC 1030”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology || 50 | 3 | SOCI 1010”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences || 50 | 8 | BIOL 1010/1011 & 1020/1021”
  - … 9 more rows
### `m8b49882259667ad` Walters State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://ws.edu/admissions/high-school-programs/dual-enrollment/index.aspx (sha256 3cbaabcf813f)
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 2.0 ⟵ “Students must have a minimum high school GPA of 2.0 on a 4.0 scale.”
  - state_grant_accepted: True ⟵ “Apply for the Dual Enrollment Grant”
  - eligibility_tier: 3.0 ⟵ “Students must have a 3.0 or higher high school GPA or an ACT Composite of 21. Note: High Schools may require a higher GPA for participation in the program.”
  - eligibility_tier: 3.0 ⟵ “sub-score of 18 and a Reading sub-score of 19) or a minimum high school GPA of 3.0.”
### `22e5986ec402b793` Welch College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://welch.edu/admissions/apply/high-school-college-dual-enrollment/ (sha256 28dcea8e6ffa)
- checks: {"fields": ["state_grant_accepted"], "tiers": 0}
  - state_grant_accepted: True ⟵ “The Dual Enrollment Grant program is defined as a grant for study at an eligible postsecondary institution that is funded from net proceeds of the state lottery and awarded to students who are attending an eligible high school and who are also enrolled in college courses at eligible postsecondary in”
### `md2e50bdb139193a` Williamson Christian College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://williamsoncc.edu/projects/dual-enrollment/ (sha256 664f47b0ca5c)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - per_credit_hour_charge: 75 ⟵ “$75 per credit hour”
  - eligibility_tier: 3.0 ⟵ “Request an official high school transcript to be mailed directly from the high school to the Office of Admissions; applicants must have a minimum cumulative GPA of 3.0 on a 4.0 scale.”

## Exceptions (303)

### `00943895470c529d` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/mass-communication (sha256 de5b931d101c)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Mass Communication pathway has specific requirements depending on the campus you select.”
### `00a10cabbcc72aa2` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/computer-science (sha256 ba61ca755f72)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Computer Science pathway has specific requirements depending on the campus you select.”
### `00ab4139f07dc15f` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/mid-level-english-education-4-8 (sha256 ee5da79c2605)
- issues: semantic_review_required
- checks: {"exceptions": 1, "requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Mid-Level English Education (4-8) pathway has specific requirements depending on the campus you select.”
  - statements.exceptions: 1 ⟵ “Middle School Teachers, Except Special and Career/Technical Education Middle School Teachers – Occupational Outlook Handbook Tennessee Board of Regents is an AA/EEO employer and does not discriminate on the basis of race, color, national origin, sex, disability, or age in its programs and activities”
### `0105c76679c2d1be` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/secondary-education-%E2%80%93-social-studies (sha256 eec0c17832d0)
- issues: semantic_review_required, conflicting_sources:https://www.tntransferpathway.org/majors/secondary-education-%E2%80%93-english,https://www.tntransferpathway.org/majors/secondary-education-%E2%80%93-math
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Secondary Education – Social Studies pathway has specific requirements depending on the campus you select.”
### `057d73a7b4b48616` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/elementary-education-k-5 (sha256 7c132af09d94)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Elementary Education (K-5) pathway has specific requirements depending on the campus you select.”
### `0c3426b23fb1b41e` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/agriculture-plant-and-soil-science (sha256 43154d4c7c66)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Agriculture- Plant and Soil Science pathway has specific requirements depending on the campus you select.”
### `12c737526e2248df` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/mid-level-social-studies-education-4-8 (sha256 65eb4685597a)
- issues: semantic_review_required
- checks: {"exceptions": 1, "requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Mid-Level Social Studies Education (4-8) pathway has specific requirements depending on the campus you select.”
  - statements.exceptions: 1 ⟵ “Middle School Teachers, Except Special and Career/Technical Education Middle School Teachers – Occupational Outlook Handbook Tennessee Board of Regents is an AA/EEO employer and does not discriminate on the basis of race, color, national origin, sex, disability, or age in its programs and activities”
### `135d9a0d66da6dae` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.collegefortn.org/college-transfer/ (sha256 92b448770fa2)
- issues: semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “With the Tennessee Transfer programs, you can begin your college studies at a community college or similar two-year program and earn an associate degree, plus rest assured your credits will transfer to a bachelor’s degree program at any public university and many private universities in Tennessee.”
  - statements.requirements: 1 ⟵ “Next, you must re-enter your Username and Password and answer the challenge question.”
### `14d20a04983a1f14` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tn.gov/thec/for-institutions/articulation-and-transfer/tennessee-reverse-transfer/resources-for-administrators.html (sha256 c1cd90ac2dfc)
- issues: semantic_review_required
- checks: {"requirements": 5}
  - statements.requirements: 5 ⟵ “Approximately 2,300 students transfer each year from Tennessee’s community colleges to four-year colleges and universities with at least 45 of the 60 credits required for most associate degrees.”
### `16e6db44622724aa` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/mid-level-mathematics-education-4-8 (sha256 b1b47f0f0183)
- issues: semantic_review_required
- checks: {"exceptions": 1, "requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Mid-Level Mathematics Education (4-8) pathway has specific requirements depending on the campus you select.”
  - statements.exceptions: 1 ⟵ “Middle School Teachers, Except Special and Career/Technical Education Middle School Teachers – Occupational Outlook Handbook Tennessee Board of Regents is an AA/EEO employer and does not discriminate on the basis of race, color, national origin, sex, disability, or age in its programs and activities”
### `188db81204a6c76b` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/information-systems (sha256 4b8788e74cba)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Information Systems pathway has specific requirements depending on the campus you select.”
### `1a0abc567ab04105` state-TN — state_policies 2026-27 · policy_kind=transfer_guarantee [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/transfer-admission-guarantee (sha256 bc9f30bae027)
- issues: semantic_review_required
- checks: {"effective": 2, "exceptions": 7, "guarantees": 4, "requirements": 13}
  - statements.guarantees: 4 ⟵ “Transfer Admission Guarantee | TN Transfer Pathway Important information regarding Tennessee Transfer Pathways transfer of community-college programs to four-year colleges or universities in Tennessee.”
  - statements.requirements: 13 ⟵ “The TTPs also constitute an agreement between community colleges and four-year colleges/universities confirming that community college courses meet major preparation requirements.”
  - statements.exceptions: 7 ⟵ “Admission to UT, Knoxville is competitive.”
  - statements.effective: 2 ⟵ “These Transfer Pathways have been effective beginning Fall 2011.”
### `1cbe346cffdff25a` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/accounting (sha256 65e2cef1ec2e)
- issues: semantic_review_required
- checks: {"requirements": 4}
  - statements.requirements: 4 ⟵ “A considerable amount of education, work-related skill, knowledge, and experience is required.”
### `1e19ee775ba2269d` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/english (sha256 79ab795789de)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The English pathway has specific requirements depending on the campus you select.”
### `23135308a49e28cf` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/philosophy (sha256 9226e79c07e7)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Philosophy pathway has specific requirements depending on the campus you select.”
### `2418a53cb66620f1` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/biology (sha256 f08a6cb270fb)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Biology pathway has specific requirements depending on the campus you select.”
### `2652a35aa25c4bd8` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/art-studio (sha256 2625bceec7a5)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Art (Studio) pathway has specific requirements depending on the campus you select.”
### `2f965eb55b936224` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/civil-engineering (sha256 7d44657d5092)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Civil Engineering pathway has specific requirements depending on the campus you select.”
### `2fbe0550bed1f9e4` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/sport-and-leisure-management (sha256 a21bbf9fcd2f)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Sport and Leisure Management pathway has specific requirements depending on the campus you select.”
### `35243ebd2271760f` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/secondary-education-%E2%80%93-math (sha256 c8033276577f)
- issues: semantic_review_required, conflicting_sources:https://www.tntransferpathway.org/majors/secondary-education-%E2%80%93-english,https://www.tntransferpathway.org/majors/secondary-education-%E2%80%93-social-studies
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Secondary Education – Math pathway has specific requirements depending on the campus you select.”
### `3533b36e24666b5b` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/pre-physical-therapy (sha256 1fab83690e6f)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Pre-Physical Therapy pathway has specific requirements depending on the campus you select.”
### `388ab7bd9e097f4a` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/finance (sha256 00a42ed9ab51)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Finance pathway has specific requirements depending on the campus you select.”
### `44860a55b4801c8d` state-TN — state_policies 2017-18 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.tn.gov/content/dam/tn/thec/bureau/research/other-research/all-other/articulation/AT_2024_Final.pdf (sha256 c93221581b84)
- issues: stale_year_label:2017-18, semantic_review_required
- checks: {"effective": 2, "exceptions": 9, "guarantees": 3, "requirements": 23}
  - statements.exceptions: 9 ⟵ “However, many students begin their enrollment at a community college and do not progress to a university.”
  - statements.requirements: 23 ⟵ “The Articulation and Transfer (A&T) Council is necessary to fulfill the requirements in Tennessee Code Annotated § 49-7-202 (r)(1-5), including collaboration on the development and maintenance of Tennessee Transfer Pathways and of common course numbering.”
  - statements.effective: 2 ⟵ “New TTPs approved and effective Fall 2025 are: Fermentation Science, Middle School – English, Middle School – History, Middle School – Science, Middle School – Social Studies, and Urban Studies.”
  - statements.guarantees: 3 ⟵ “For community college students who plan to transfer to a Tennessee public university, or to select non-profit private colleges and universities in Tennessee, the TTP provides a guarantee that courses will transfer.”
### `460df47b8790a442` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/mid-level-science-education-4-8 (sha256 155f1e194bc9)
- issues: semantic_review_required
- checks: {"exceptions": 1, "requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Mid-Level Science Education (4-8) pathway has specific requirements depending on the campus you select.”
  - statements.exceptions: 1 ⟵ “Middle School Teachers, Except Special and Career/Technical Education Middle School Teachers – Occupational Outlook Handbook Tennessee Board of Regents is an AA/EEO employer and does not discriminate on the basis of race, color, national origin, sex, disability, or age in its programs and activities”
### `4670b0217fc03acd` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/agriculture-animal-science (sha256 06bb1b7e64c2)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Agriculture- Animal Science pathway has specific requirements depending on the campus you select.”
### `489bee5b563e9bb0` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/pre-health (sha256 b694e2241357)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Pre-Health pathway has specific requirements depending on the campus you select.”
### `48dd3e7322ea0ef6` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/secondary-education-%E2%80%93-english (sha256 fb3995236c70)
- issues: semantic_review_required, conflicting_sources:https://www.tntransferpathway.org/majors/secondary-education-%E2%80%93-math,https://www.tntransferpathway.org/majors/secondary-education-%E2%80%93-social-studies
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Secondary Education – English pathway has specific requirements depending on the campus you select.”
### `4bcd3cf892fa2cd2` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/special-education (sha256 ef0327f7d1a6)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Special Education pathway has specific requirements depending on the campus you select.”
### `4c5f4beb6f9069f5` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/engineering-technology (sha256 5ce293a53508)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Engineering Technology pathway has specific requirements depending on the campus you select.”
### `4cf03478ca300c77` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/supply-chain-management (sha256 107507b8ce1d)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Supply Chain Management pathway has specific requirements depending on the campus you select.”
### `52ce87d0f55e777f` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/chemistry (sha256 45aca6eb9b14)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Chemistry pathway has specific requirements depending on the campus you select.”
### `6e9580199848ce5b` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/sociology (sha256 836ce14c9658)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Sociology pathway has specific requirements depending on the campus you select.”
### `6fa97d8560aa2829` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/electrical-engineering (sha256 ef23412d06ab)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Electrical Engineering pathway has specific requirements depending on the campus you select.”
### `70a0a4bb479beff9` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/ (sha256 ecf3f8fda8b1)
- issues: semantic_review_required
- checks: {"exceptions": 2, "guarantees": 3}
  - statements.guarantees: 3 ⟵ “With the Tennessee Transfer programs, you can begin your college studies at a community college or similar two-year program and earn an associate degree, plus rest assured your credits will transfer to a bachelor’s degree program at any public university and many private universities in Tennessee.”
  - statements.exceptions: 2 ⟵ “If a community college student transfers to another Tennessee community college, he or she is guaranteed that all courses transfer. *Admission to UT, Knoxville is competitive.”
### `72d36e34078e0944` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/exercise-science (sha256 32c08941afd9)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Exercise Science pathway has specific requirements depending on the campus you select.”
### `750492a08f3a4586` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/marketing (sha256 50af3b206e86)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Marketing pathway has specific requirements depending on the campus you select.”
### `77a749129ad667f6` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/theatre-arts (sha256 8a0509c5abc6)
- issues: semantic_review_required, conflicting_sources:https://www.tntransferpathway.org/majors/theatre-arts-design-tech,https://www.tntransferpathway.org/majors/theatre-arts-performance
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Theatre Arts pathway has specific requirements depending on the campus you select.”
### `789bf5b60063274f` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/music (sha256 0e66be95b227)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Music pathway has specific requirements depending on the campus you select.”
### `7b0b39384d334a65` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/agriculture-agriculture-business (sha256 8f896459ecbb)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Agriculture- Agriculture Business pathway has specific requirements depending on the campus you select.”
### `7da075ff992ec9f9` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/anthropology (sha256 87ac47b410b3)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Anthropology pathway has specific requirements depending on the campus you select.”
### `7f1e4c25864371ec` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/imaging-sciences (sha256 93e33a0cebad)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Imaging Sciences pathway has specific requirements depending on the campus you select.”
### `80c953f92696a592` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/Fermentation (sha256 eeaf32f49739)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Fermentation pathway has specific requirements depending on the campus you select.”
### `80e94e506327bddc` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/physics (sha256 087c5c14b980)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Physics pathway has specific requirements depending on the campus you select.”
### `82553225f578362f` state-TN — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.collegefortn.org/wp-content/uploads/2024/02/TCAT-DE-for-HS-Grad-Requirements-FAQ_Feb-2024.pdf (sha256 d29cbcb3edb9)
- issues: semantic_review_required
- checks: {"exceptions": 2, "requirements": 10}
  - statements.requirements: 10 ⟵ “SBE policy states: In addition to the specific courses listed in this policy, pursuant to the State Board of Education Rule 0520-01- 03.03 (7) LEAs shall accept postsecondary credits as a substitution for an aligned graduation requirement course, including general education and elective focus course”
  - statements.exceptions: 2 ⟵ “However, it is less clear how the Production Machine Tender trimester could appropriately be used as a substitution for a high school graduation requirement based on the certification name and the fact that the necessary clock hours are earned over multiple high school academic years. 3.”
### `89aa5a9ca1fa992e` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/theatre-arts-design-tech (sha256 33758bf3bf7c)
- issues: semantic_review_required, conflicting_sources:https://www.tntransferpathway.org/majors/theatre-arts,https://www.tntransferpathway.org/majors/theatre-arts-performance
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Theatre Arts - Design / Tech pathway has specific requirements depending on the campus you select.”
### `8a8fddf0991fd0e8` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/management (sha256 f1c3d5346418)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Management pathway has specific requirements depending on the campus you select.”
### `8c9150aa4f42378f` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/mechanical-engineering (sha256 6a2a5850d5b6)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Mechanical Engineering pathway has specific requirements depending on the campus you select.”
### `8e2ce192f501af08` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/kinesiology (sha256 b966e2f4a092)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Kinesiology pathway has specific requirements depending on the campus you select.”
### `91205f8aeaeccd7e` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/communication-studies-formerly-speech-communication (sha256 432a8402dc9f)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Communication Studies (formerly Speech Communication) pathway has specific requirements depending on the campus you select.”
### `943e56d9aa476a99` state-TN — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.collegefortn.org/dualenrollment/ (sha256 94f3b0d76697)
- issues: semantic_review_required
- checks: {"requirements": 9}
  - statements.requirements: 9 ⟵ “TN College Application & Exploration Month FAST & Additional Financial Aid Resources TN College Application & Exploration Month FAST & Additional Financial Aid Resources OverviewAward InformationEligibilityApplicationTermination CriteriaRelated Links The Dual Enrollment Grant program is for students”
### `94d681276f529e91` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/economics (sha256 9eb902dc4507)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Economics pathway has specific requirements depending on the campus you select.”
### `94f548f51535bba8` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.collegefortn.org/college-transfer/articulation-agreements/ (sha256 be23d0159aa9)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Next, you must re-enter your Username and Password and answer the challenge question.”
### `99393a3a3652725b` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/religious-studies (sha256 63c80a5de95c)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Religious Studies pathway has specific requirements depending on the campus you select.”
### `996d455cd63eb924` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/steps (sha256 23503096a5ad)
- issues: semantic_review_required
- checks: {"exceptions": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Investigate program-specific selection criteria and requirements such as auditions, portfolios or entrance exams (ask your advisor).”
  - statements.exceptions: 1 ⟵ “Be aware of course sequences and prerequisites which may require you to complete courses certain semesters to stay on track and not delay your transfer/graduation plans. 4.”
### `a41d40f3747b51ec` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/physical-education (sha256 de9c365b8f1e)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Physical Education pathway has specific requirements depending on the campus you select.”
### `b09b1d03093a6868` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/criminal-justice (sha256 1b11ca5dd704)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Criminal Justice pathway has specific requirements depending on the campus you select.”
### `b486d4709ca4fd25` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.collegefortn.org/college-transfer/reverse-transfer/ (sha256 e50dfb8dd80a)
- issues: semantic_review_required
- checks: {"guarantees": 1, "requirements": 4}
  - statements.guarantees: 1 ⟵ “If you earn an associate degree, you guarantee that all of your coursework transfers to a four-year institution in the event that you begin working toward a bachelor’s degree again.”
  - statements.requirements: 4 ⟵ “As you fulfill requirements at your four-year school that qualify you for an associate degree by Reverse Transfer, you are simultaneously making progress toward completing your bachelor’s degree!”
### `b60ed06073ee1e36` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/history (sha256 f18ee5341947)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The History pathway has specific requirements depending on the campus you select.”
### `b66dc9992b94a1c6` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/geosciences (sha256 18a0a001000c)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Geosciences pathway has specific requirements depending on the campus you select.”
### `b7408848efbbd470` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/psychology (sha256 91d87be6c4b4)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Psychology pathway has specific requirements depending on the campus you select.”
### `c0c9379a1a9d44ef` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/foreign-language (sha256 7c65fb6f5687)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Foreign Language pathway has specific requirements depending on the campus you select.”
### `c51af6d0e8d1a50d` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/international-affairs (sha256 84ad70211cf9)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The International Affairs pathway has specific requirements depending on the campus you select.”
### `cd8ae36768c30c2e` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/art (sha256 e5104db9df0d)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Art pathway has specific requirements depending on the campus you select.”
### `d0cba458559b332d` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/theatre-arts-performance (sha256 9c4ef9c11795)
- issues: semantic_review_required, conflicting_sources:https://www.tntransferpathway.org/majors/theatre-arts,https://www.tntransferpathway.org/majors/theatre-arts-design-tech
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Theatre Arts - Performance pathway has specific requirements depending on the campus you select.”
### `d43cc61c650aeb7c` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/pre-occupational-therapy (sha256 ed095fcc4f64)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Pre-Occupational Therapy pathway has specific requirements depending on the campus you select.”
### `d6a691192278f02f` state-TN — state_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.collegefortn.org/wp-content/uploads/2026/07/DEG-2026-2027-Handout.pdf (sha256 8891c799a157)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Amounts will differ depending on the number of credit hours.      To qualify for DEG at a 2- or 4-year college, student must be a high school junior or senior and satisfy dual enrollment (DE) admissions criteria set by the college.      DEG students must earn a minimum cumulative 2.00 GPA, for all”
### `d8181536625cc240` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/social-work (sha256 9ed3031ff390)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Social Work pathway has specific requirements depending on the campus you select.”
### `d9b885e43fa596c5` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tn.gov/thec/for-institutions/articulation-and-transfer/tennessee-reverse-transfer.html (sha256 ab8b8e42a508)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “As of January 2023, THEC is responsible for the centralized administration and coordination of The Tennessee Reverse Transfer Senior Director of Transfer & Veteran Initiatives”
### `da7ed4c691bd727d` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/business-administration (sha256 300ad1e4d753)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Business Administration pathway has specific requirements depending on the campus you select.”
### `dcbd60feabe1a2ef` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/pre-clinical-laboratory-science (sha256 da6b1f335844)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Pre-Clinical Laboratory Science pathway has specific requirements depending on the campus you select.”
### `ddcf7d6eda4419c3` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/mathematics (sha256 f435c8763ecd)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Mathematics pathway has specific requirements depending on the campus you select.”
### `e142e75404ce3b4a` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/political-science (sha256 d5afcd8fdeb3)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The Political Science pathway has specific requirements depending on the campus you select.”
### `e75357d2b16a1595` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tn.gov/thec/for-institutions/articulation-and-transfer/articulation-and-transfer-council-members/reverse-transfer-subcouncil.html (sha256 5ddfac61171e)
- issues: semantic_review_required
- checks: {"effective": 1, "requirements": 1}
  - statements.effective: 1 ⟵ “Reduction in Force (RIF) Tuition Assistance Benefit Outcomes Based Funding Formulas Resources TN Technical Transfer Pathways Subcouncil This subcouncil focuses on the advancement of the effectiveness of the Tennessee Reverse Transfer Program, which allows students who started their postsecondary edu”
  - statements.requirements: 1 ⟵ “As of January 2023, THEC will be responsible for the centralized administration and coordination of Reverse Transfer for the state. | University of Tennessee of Tennessee System”
### `ea9e54d6e26c34de` state-TN — state_policies 2026-27 · policy_kind=dual_admission [new] (source_unlabeled)
- source: https://www.tn.gov/thec/for-institutions/articulation-and-transfer/articulation-and-transfer-council-members/dual-admissions.html (sha256 b0c8d7e675d3)
- issues: semantic_review_required
- checks: {"effective": 1, "guarantees": 1}
  - statements.guarantees: 1 ⟵ “Reduction in Force (RIF) Tuition Assistance Benefit Outcomes Based Funding Formulas Resources TN Technical Transfer Pathways Subcouncil The Dual Admission Sub-council is charged with providing expertise and guidance on dual admissions policies and, processes, and within guaranteed transfer pathways.”
  - statements.effective: 1 ⟵ “The sub-council will review existing practices, identify barriers to student progression, and recommend improvements that enhance the efficiency and effectiveness of dual admissions programs.”
### `ef4e3116356041ae` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/pre-dental-hygiene (sha256 ef7e38c6bf75)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Pre-Dental Hygiene pathway has specific requirements depending on the campus you select.”
### `f0a0802735fbcd8b` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/nutrition-and-food-science (sha256 758c73dab206)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Nutrition and Food Science pathway has specific requirements depending on the campus you select.”
### `f31c328a445ac3a2` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/urban-planning (sha256 066aa2f8a237)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Urban Planning pathway has specific requirements depending on the campus you select.”
### `f878dedc6e3c8cd1` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/family-and-consumer-sciences (sha256 7b10d4cf24e4)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “The Family and Consumer Sciences pathway has specific requirements depending on the campus you select.”
### `fb5595a0279e0d4a` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tntransferpathway.org/majors/early-childhood-education-pre-k-3 (sha256 b5de5627b7ae)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Associate of Science in Teaching (A.S.T..) The Early Childhood Education (Pre K-3) pathway has specific requirements depending on the campus you select.”
### `fb9abfdf3cd8d363` state-TN — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.tn.gov/thec/for-institutions/articulation-and-transfer.html (sha256 a1e9a78c6b0f)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Reduction in Force (RIF) Tuition Assistance Benefit Outcomes Based Funding Formulas Resources Outcomes Based Funding Formulas Resources Application, Deadlines, and Meeting Dates Distance Education Authorization Requirements Archive - Institution Closure Information Host-State Institutions or Non-SAR”
### `181260ca236bbf9c` American Baptist College — appeals 2024-25 [new] (labeled_in_title)
- source: https://abcnash.edu/wp-content/uploads/2024/06/2024-2025-Special-Circumstances-Form.pdf (sha256 a51d02490624)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “2024-2025 Special Circumstance Request This form is used to request a reevalua on of the informa on you provided on the Free Applica on for Federal Student Aid (FAFSA) due to special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Other Unusual Circumstances Personal statement, with suppor ng documenta on from a third-party such as teacher, clergy, counselor, medical or government authority/agency, or court that is aware of the circumstances that exist such as abandonment by parents, abusive family environment that threatens the health and safety of the student, unable to locate parents, risk of being homeless, or unaccompa”
### `105b8c0513ad88e8` Austin Peay State University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.apsu.edu/financialaid/sat_prog.php (sha256 0d9d1196ea37)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appeal Submission Information: SAP appeals and academic reviews may be submitted at any time, but it is best to appeal early to prevent delays in your financial aid if approved.”
  - sentence: sap_appeal ⟵ “Students may view their Inclusive Combined GPA on OneStop > Web Self Service > Student > Student Records > Student GPA. 2025-2026 SAP Policy SAP Policy Guidelines SAP Appeal Form SAP Appeal Form This form should be completed when a student has been notified by the Office of Student Financial Aid that their SAP status requires an appeal.”
  - sentence: sap_appeal ⟵ “Supporting Letter for SAP Appeal This form may be completed by a third party in support of a student's appeal in place of a letter of support.”
### `59f8bb4907d708f5` Austin Peay State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/financialaid/forms/scholarship-forms.php (sha256 f855944bda5d)
- issues: semantic_review_required, conflicting_sources:https://www.apsu.edu/financialaid/forms/appeal-forms.php,https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php,https://www.apsu.edu/scholarships/tn-education-lottery-programs/lottery-appeals.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “Fall 2025, Spring 2026, and Summer 2026 Form Scholarship Appeal Form - This form is used to appeal the loss of an academic scholarship.”
  - sentence: scholarship_retention_appeal ⟵ “Normally, a student is not able to appeal the loss of the scholarship until after one semester/term has elapsed.”
### `75d2cf74dfaad1c9` Austin Peay State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/financialaid/types-of-aid-scholarships/grants/federal-grants.php (sha256 18fac647ff2c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Exceptions to this policy are granted based on professional judgment.”
### `77c4d55900847739` Austin Peay State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.apsu.edu/financialaid/special-circumstance-request.php (sha256 6883da29bcd8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Department of Veterans Affairs VA Education Benefits Applicant Checklists VA Education Benefits Information GI Bill® Comparison Tool VA Veteran Readiness & Employment VA Work Study Principles of Excellence Faculty and Staff Resources Guide for Faculty and Staff Functional Support Request Form Financial Aid for Transfer Students Special Circumstance Request A Special Circumstance Request form is co”
  - sentence: need_based_special_circumstances ⟵ “The three reasons to complete this form are: Loss of Employment/Income Divorce or Separation Death of a Spouse/Parent* If the student has any one of these reasons, they may complete a Special Circumstance Request as long as: Verification is completed, if selected.”
  - sentence: need_based_special_circumstances ⟵ “Christopher hears about the Special Circumstance Request from an email from the Financial Aid Office, and decides to complete the request.”
  - sentence: need_based_special_circumstances ⟵ “Unfortunately, the Special Circumstances Request will not benefit Christopher.”
  - sentence: need_based_special_circumstances ⟵ “Heather hears from her advisor that she can complete a Special Circumstance Request to exclude her ex-spouse’s financial information from the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Toggle Death of a Parent/Spouse Example 1 John’s spouse lost a battle with cancer in 2024, and he heard from a friend that he could complete a Special Circumstance Request with the Financial Aid Office to see if his spouse’s income could be excluded from his eligibility for need-based aid.”
### `7909beda86cbdfcd` Austin Peay State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/tn-education-lottery-programs/lottery-appeals.php (sha256 7e4d78c05f7b)
- issues: semantic_review_required, conflicting_sources:https://www.apsu.edu/financialaid/forms/appeal-forms.php,https://www.apsu.edu/financialaid/forms/scholarship-forms.php,https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If the initial appeal is denied, the student may file a new appeal to the TSAC HOPE Lottery Scholarship Award Appeal Panel at the following address: Tennessee Education Lottery Scholarship 404 James Robertson Parkway Suite 1950, Parkway Towers Nashville, TN 37243-0820 Further Information pertaining to appealing your loss through TSAC may be reviewed here.”
### `e05c40118fd0537d` Austin Peay State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/financialaid/forms/appeal-forms.php (sha256 dde578b5975c)
- issues: semantic_review_required, conflicting_sources:https://www.apsu.edu/financialaid/forms/scholarship-forms.php,https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php,https://www.apsu.edu/scholarships/tn-education-lottery-programs/lottery-appeals.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “Scholarship Appeal Form - This form is used to appeal the loss of an academic scholarship.”
  - sentence: scholarship_retention_appeal ⟵ “Normally, a student is not able to appeal the loss of the scholarship until after one semester/term has elapsed.”
### `e8d281cba616f442` Austin Peay State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- issues: semantic_review_required, conflicting_sources:https://www.apsu.edu/financialaid/forms/appeal-forms.php,https://www.apsu.edu/financialaid/forms/scholarship-forms.php,https://www.apsu.edu/scholarships/tn-education-lottery-programs/lottery-appeals.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Appeals: Normally a student is not able to appeal the loss of one of the above scholarships until after one semester/term.”
### `f6827a9452662960` Austin Peay State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/financialaid/forms/appeal-forms.php (sha256 dde578b5975c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form Satisfactory Academic Progress Appeal Form - This form must be completed when a student has been notified by the Student Financial Aid Office that they are in violation of the Satisfactory Academic Progress Policy Guidelines.”
### `f9448803e04cd87b` Austin Peay State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.apsu.edu/financialaid/special-circumstance-request.php (sha256 6883da29bcd8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Rather, if the student does not maintain a relationship with their other parent, they may qualify for a dependency override.”
### `01e9ec1bb0b2a39e` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- issues: conflicting_sources:https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “Presidential | 4.0 GPA | Admissions application to APSU | $6,000”
### `1bbb283af6253f48` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- issues: conflicting_sources:https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Dean's | 2.75 ♦ | 0 | 8 | Full-Time”
### `1d25a4ae8cd7a6a8` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- issues: conflicting_sources:https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php
- checks: {"thresholds": {"gpa_min": 2.75}}
  - gpa_requirement: 2.75 ⟵ “Governor's Excellence | 2.75 | 0 | 8 | Full-Time”
### `1e0139aafdfb0ca6` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- issues: conflicting_sources:https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Presidential | 2.75 ♦ | 75 per semester | 8 | Full-Time”
### `6a1b89f1b4580076` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- issues: conflicting_sources:https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php
- checks: {"thresholds": null}
  - award_amount_text: $3,500 ⟵ “Dean's | 3.85 - 3.99 GPA | Admissions application to APSU | $3,500”
### `a71a7151515d81d0` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- issues: conflicting_sources:https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Governor's Excellence | 3.0-3.49 GPA | Admissions application to APSU | $1,000”
### `1960dfa074951f21` Baptist Health Sciences University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.baptistu.edu/tuition-financial-aid/scholarships-grants/hope-scholarships/hope-lottery-scholarship-appeal (sha256 153cceb96e08)
- issues: semantic_review_required, conflicting_sources:https://www.baptistu.edu/sites/default/files/Financial%20Aid%20forms/hope_lottery_scholarship_appeal_form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Click the following link to get additional information regarding the HOPE Lottery Scholarship appeals process.”
### `c8d042ff18228301` Baptist Health Sciences University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.baptistu.edu/sites/default/files/Financial%20Aid%20forms/hope_lottery_scholarship_appeal_form.pdf (sha256 f23003b97889)
- issues: semantic_review_required, conflicting_sources:https://www.baptistu.edu/tuition-financial-aid/scholarships-grants/hope-scholarships/hope-lottery-scholarship-appeal
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: scholarship_retention_appeal ⟵ “Student Financial Aid Office 1003 Monroe Avenue Memphis, TN 38104 Office: (901) 575-2247 Fax: (901) 572-2461 Email: financial.aid@baptistU.edu HOPE LOTTERY SCHOLARSHIP APPEAL FORM The HOPE Lottery Scholarship is awarded based on policies set forth by the Tennessee Student Assistance Corporation (TSAC).”
  - sentence: scholarship_retention_appeal ⟵ “Tennessee Lottery Legislation DOES NOT grant the authority to allow appeals (regardless of the circumstances) for the following: GPA requirements for both initial and continuing eligibility; Score requirements for ACT, SAT, and GED tests; Limit on attempted hours or years of enrollment; Income limit for a Need-Based Supplemental Award; Residency status.”
  - sentence: scholarship_retention_appeal ⟵ “If, after reviewing the information above, you feel that you can meet the criteria for an appeal, please complete the attached Baptist College HOPE Lottery Scholarship Appeal Form.”
  - sentence: scholarship_retention_appeal ⟵ “HOPE Lottery Scholarship Appeal Form - Page 1 of 2 Student Financial Aid Office 1003 Monroe Avenue Memphis, TN 38104 Office: (901) 575-2247 Fax: (901) 572-2461 Email: financial.aid@baptistU.edu Complete the information below and return to the Financial Aid Office using the contact information above.”
  - sentence: scholarship_retention_appeal ⟵ “CERTIFICATION I certify that I have reviewed the HOPE Lottery Scholarship appeal guidelines attached.”
  - sentence: scholarship_retention_appeal ⟵ “Student Signature: _____________________________________________________ Date: ______________________ HOPE Lottery Scholarship Appeal Form - Page 2 of 2”
### `bd4835a9e3ca282c` Belmont University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.belmont.edu/sfs/financial-aid/ (sha256 1afbe0465444)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals add VIII.”
  - sentence: sap_appeal ⟵ “Fax To: (615) 460-6141 Attn: SAP Appeals Committee Physically Mail To: SAP APPEALS COMMITTEE Office of Student Financial Services Belmont University 1900 Belmont Boulevard Nashville, TN 37212 IX.”
### `1f1e82d749ed3844` Belmont University — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.belmont.edu/sfs/cost/ (sha256 681bf7a760c7)
- issues: conflicting_sources:https://www.belmont.edu/admissions/first-year/tuition-aid.html,https://www.belmont.edu/admissions/transfer/tuition-aid.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 45200 ⟵ “Tuition and Fees | $45,200”
  - column:Residence Hall and Meal Plan*: 16130 ⟵ “Residence Hall and Meal Plan* | $16,130”
  - column:Total Estimated Cost for 2026-2027**: 61330 ⟵ “Total Estimated Cost for 2026-2027** | $61,330”
### `51a626e97240dd22` Belmont University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.belmont.edu/admissions/transfer/tuition-aid.html (sha256 193916464e1e)
- issues: conflicting_sources:https://www.belmont.edu/admissions/first-year/tuition-aid.html,https://www.belmont.edu/sfs/cost/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
- change total_direct_cost: `61330` → `68370`
  - column:Tuition and Fees: 45200 ⟵ “Tuition and Fees | $45,200”
  - column:Residence Hall and Meal Plan*: 23170 ⟵ “Residence Hall and Meal Plan* | $23,170”
  - column:Total Estimated Cost for 2026-2027**: 68370 ⟵ “Total Estimated Cost for 2026-2027** | $68,370”
### `65204062fce35275` Belmont University — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.belmont.edu/admissions/first-year/tuition-aid.html (sha256 09ad51e3649b)
- issues: conflicting_sources:https://www.belmont.edu/admissions/transfer/tuition-aid.html,https://www.belmont.edu/sfs/cost/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 45200 ⟵ “Tuition and Fees | $45,200”
  - column:Residence Hall and Meal Plan*: 16130 ⟵ “Residence Hall and Meal Plan* | $16,130”
  - column:Total Estimated Cost for 2026-2027**: 61330 ⟵ “Total Estimated Cost for 2026-2027** | $61,330”
### `f5a3775f879d7fe5` Belmont University — costs 2025-26 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.belmont.edu/sfs/cost/ (sha256 681bf7a760c7)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 43750 ⟵ “Tuition and Fees | $43,750”
  - column:Residence Hall and Meal Plan*: 15530 ⟵ “Residence Hall and Meal Plan* | $15,530”
  - column:Total Estimated Cost for 2025-2026**: 59280 ⟵ “Total Estimated Cost for 2025-2026** | $59,280”
### `0bf0dbe588917746` Bryan College-Dayton — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.bryan.edu/admissions/financial-aid/ (sha256 1e23efac6008)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If the process requires our office to make corrections to your FAFSA and those changes necessitate a change in your financial aid award you will receive a revised award letter within two to three weeks that will replace your previous award offer.”
### `fba5b95986309c83` Bryan College-Dayton — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.bryan.edu/admissions/financial-aid/ (sha256 1e23efac6008)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Process A student who feels mitigating circumstances existed that adversely affected the student‘s ability to maintain satisfactory academic progress may submit a written appeal within five business days of receiving notification of the suspension status.”
### `m50eb0be45eec5d4` Bryan College-Dayton — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://www.bryan.edu/admissions/dual-enrollment/ (sha256 412d7d7a6ba9)
- issues: ambiguous_year_labels, conflicting_sources:max_credit_hours_per_term, state_grant_mixed_statements
- checks: {"fields": ["college_gpa_to_continue", "max_credit_hours_per_term"], "merged_pages": 2, "tiers": 5}
  - eligibility_tier: 3.5 ⟵ “All high school sophomores with a minimum grade point average (GPA) of 3.5 are eligible for dual enrollment. Students may take one class at a time. The TN grant does not apply; no discounts are offered.”
  - state_grant_accepted: False ⟵ “All high school sophomores with a minimum grade point average (GPA) of 3.5 are eligible for dual enrollment. Students may take one class at a time. The TN grant does not apply; no discounts are offered.”
  - eligibility_tier: 3.0 ⟵ “All high school juniors and seniors with a minimum grade point average (GPA) of 3.0 are eligible for dual enrollment. Out-of-state scholarships and the TN grant apply.”
  - state_grant_accepted: True ⟵ “All high school juniors and seniors with a minimum grade point average (GPA) of 3.0 are eligible for dual enrollment. Out-of-state scholarships and the TN grant apply.”
  - max_credit_hours_per_term: 13 ⟵ “Dual enrollment students may register for a maximum of 13 credit hours for both fall and spring semesters. For summer sessions, a maximum of 3 credit hours per session is allowed.”
  - eligibility_tier: 3.5 ⟵ “Sophomores: 3.5 GPA (1 class per fall/spring)”
  - eligibility_tier: 3.0 ⟵ “Juniors & Seniors: 3.0 GPA (up to 13 credits per fall/spring)”
  - max_credit_hours_per_term: 13 ⟵ “Juniors & Seniors: 3.0 GPA (up to 13 credits per fall/spring)”
  - eligibility_tier: 2.8 ⟵ “2.8–2.99 GPA may qualify for Conditional Acceptance”
  - college_gpa_to_continue: 2.0 ⟵ “Yes. TN juniors and seniors may apply annually and must maintain a 2.0 college GPA.”
  - max_credit_hours_per_term: 13 ⟵ “Juniors/Seniors: Up to 13 credits per fall/spring”
  - max_credit_hours_per_term: 12 ⟵ “Fall Semester - 15 weeks | Maximum of 12 credits | August 19 - December 11, 2026”
  - max_credit_hours_per_term: 12 ⟵ “Spring Semester - 15 weeks | Maximum of 12 credits | January 5 - April 30, 2027”
### `3722e673f34c337e` Carson-Newman University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cn.edu/wp-content/uploads/2024/06/SAP-Appeal-Form97.pdf (sha256 2c19589aa0af)
- issues: semantic_review_required, conflicting_sources:https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-important-dates/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Carson-Newman University Financial Aid Office • 1645 Russell Avenue • Jefferson City, TN 37760 Financial Aid Office • (800) 678-9061 • (865) 471-3247 • Fax (865) 471-2035 financialaid@cn.edu • www.cn.edu Satisfactory Academic Progress Appeal Form Satisfactory Academic Progress (SAP) Overview Federal regulations require that all students meet minimum qualitative (grades) and minimum quantitative (h”
  - sentence: sap_appeal ⟵ “SAP Appeal Process If extenuating circumstances precluded you from meeting the standards, you may file an appeal.”
### `4252ea3a3d97cc31` Carson-Newman University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-forms/ (sha256 ca72f296f2d5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “Dependency Override Appeal Application – A student may need to request an override to their dependency status due to unusual and unavoidable circumstances.”
  - sentence: dependency_override ⟵ “A Dependency Status Appeal Application is considered on a case-by-case basis depending on the situation and supporting documentation provided.”
  - sentence: dependency_override ⟵ “Dependency Override Appeal Application – A student may need to request an override to their dependency status due to unusual and unavoidable circumstances.”
  - sentence: dependency_override ⟵ “A Dependency Status Appeal Application is considered on a case-by-case basis depending on the situation and supporting documentation provided.”
### `4682cf577334df3f` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Independent-Appeal.pdf (sha256 ca619c461fc9)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Carson-Newman University 2025-2026 Special Circumstance Appeal for Independent Students ______________________________________________________________ ___________________________________ Student’s Last Name Student’s First Name Student’s M.I.”
  - sentence: need_based_special_circumstances ⟵ “Student’s Identification (ID) Number ______________________________________________________________ ___________________________________ Student’s E-Mail Address Student’s Home/Cell Phone Number This Appeal is a request for a review of special circumstances that you feel may change your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Please note: Loss of income for the 2023 IRS Tax Return calendar year will NOT be considered for special circumstances ___ Copy of 2024 IRS Tax Return Transcript or signed copy of 2024 appeal as this process will be based on current year data only.”
### `90cb605425d821b5` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf (sha256 485c9c14b0e0)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Independent-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Carson-Newman University 2025-2026 Special Circumstances Appeal for Dependent Students ______________________________________________________________ ___________________________________ Student’s Last Name Student’s First Name Student’s M.I.”
  - sentence: need_based_special_circumstances ⟵ “Student’s Identification (ID) Number ______________________________________________________________ ___________________________________ Student’s E-Mail Address Student’s Home/Cell Phone Number This Appeal is a request for a review of special circumstances that you feel may change your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Please note: Loss of income for the 2023 IRS Tax Return calendar year will NOT be considered for special circumstances ___ Copy of 2024 IRS Tax Return Transcript or signed copy of 2024 appeal as this process will be based on current year data only.”
### `b06b5e871156aace` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Independent-Appeal.pdf (sha256 ca619c461fc9)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment refers to the school’s authority to make adjustments to the data elements reported on the Free Application for Federal Student Aid (FAFSA) so that the Department of Education can recalculate the Student Aid Index (SAI).”
### `c08310cf5e3eb0f1` Carson-Newman University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cn.edu/college-of-professional-studies/cps-tuition-financial-aid/ (sha256 4134e2bf7b0f)
- issues: semantic_review_required, conflicting_sources:https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-forms/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “To find out what state aid you may qualify for, click here- https://www.cn.edu/admissions-and-aid/financial-aid/types-of-aid/state-aid There are several special circumstances that may arise in the financial aid process that may be confusing or make you feel unsure about how to proceed.”
### `ccde3144671b080f` Carson-Newman University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-important-dates/ (sha256 fc82be26a5fa)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2024/06/SAP-Appeal-Form97.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Complete verification (if required) by May 2, 2025 Accept/reject aid by May 5, 2025 New loan borrowers and TEACH Grant recipients need to complete loan and/or TEACH paperwork by May 5, 2025 Notify Financial Aid about any housing and/or enrollment changes by May 2, 2025 Satisfactory Academic Progress Appeal deadline is May 2, 2025, or ASAP after Spring grades are reported and SAP status is calculat”
### `d6fcec6916eb8e2f` Carson-Newman University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-forms/ (sha256 ca72f296f2d5)
- issues: semantic_review_required, conflicting_sources:https://www.cn.edu/college-of-professional-studies/cps-tuition-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Verification paperwork is attached to the Special Circumstances Appeal form.”
  - sentence: need_based_special_circumstances ⟵ “Keep in mind that in order to submit a Special Circumstance Appeal for the 2026-27 academic year, the 2025 taxes must be complete to attach to the appeal, and the student must have already received his/her original aid offer.”
  - sentence: need_based_special_circumstances ⟵ “Independent Special Circumstance Appeal Form – Please complete this form along with supporting documentation if you have suffered a loss of income.”
  - sentence: need_based_special_circumstances ⟵ “Verification paperwork is attached to the Special Circumstances Appeal form.”
  - sentence: need_based_special_circumstances ⟵ “Fall 2025, Spring 2026 & Summer 2026 Dependent Verification Worksheet Independent Verification Worksheet Dependent Special Circumstance Appeal Form – Please complete this form along with supporting documentation if you have suffered a loss of income.”
  - sentence: need_based_special_circumstances ⟵ “Verification paperwork is attached to the Special Circumstances Appeal form.”
### `fdd1747b66a80035` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf (sha256 485c9c14b0e0)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Independent-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment refers to the school’s authority to make adjustments to the data elements reported on the Free Application for Federal Student Aid (FAFSA) so that the Department of Education can recalculate the Expected Family Contribution (SAI).”
### `ee67a9053540ab21` Carson-Newman University — awards 2025-26 [same] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/types-of-aid/scholarships/ (sha256 4a5604a0718a)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '2.2', 'amount_text': '$8,000'}, {'gpa': '2.75', 'amount_text': '$10,000'}, {'gpa': '3.5', 'amount_text': '$12,000'}, {'gpa': '3.75', 'amount_text': '$14,000'}, {'gpa': '3.9', 'amount_text': '$16,000'}] ⟵ “GPA | Merit || 2.2 | $8,000 || 2.75 | $10,000 || 3.5 | $12,000 || 3.75 | $14,000 || 3.9 | $16,000”
  - gpa_requirement: Tiered by GPA: 2.2 → $8,000; 2.75 → $10,000; 3.5 → $12,000; 3.75 → $14,000; 3.9 → $16,000 ⟵ “GPA | Merit || 2.2 | $8,000 || 2.75 | $10,000 || 3.5 | $12,000 || 3.75 | $14,000 || 3.9 | $16,000”
### `666d72c4faf3dbbb` Carson-Newman University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/tuition-costs/ (sha256 4daabe57bedc)
- issues: components_do_not_reconcile, conflicting_sources:https://www.cn.edu/admissions-and-aid/financial-aid/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": false, "rows": 2}
- change total_direct_cost: `55300` → `55100`
  - column:Tuition & Fees: 42500 ⟵ “Tuition & Fees | $42,500”
  - column:Total Estimated Direct (billable) costs:: 55100 ⟵ “Total Estimated Direct (billable) costs: | $55,100”
### `f06dee3d7094e419` Carson-Newman University — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/ (sha256 ed693223d0c2)
- issues: conflicting_sources:https://www.cn.edu/admissions-and-aid/financial-aid/tuition-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 42500 ⟵ “Tuition | $21,250 | $42,500”
  - column:Residential Student Fee: 200 ⟵ “Residential Student Fee |  | 200”
  - column:Meal Plan*: 6300 ⟵ “Meal Plan* | 3,150 | 6,300”
  - column:Room**: 6300 ⟵ “Room** | 3,150 | 6,300”
  - column:Total: 55300 ⟵ “Total | $27,550 | $55,300”
### `8a7bb3636e59e903` Carson-Newman University — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/dual-enrollment/ (sha256 45c1990482a4)
- issues: stale_year_label:2025-26
- checks: {"fields": ["alt_min_act", "alt_min_sat", "max_credit_hours_per_term", "min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Minimum GPA of 3.0 (on 4.0 scale) OR minimum GPA of 2.0 with 19+ ACT composite score, 1030 SAT (combined Evidence-Based Reading and Writing and Math), or 63 Classical Learning Test (CLT)”
  - max_credit_hours_per_term: 14 ⟵ “Allowed to take a maximum of 14 credit hours per semester”
  - per_credit_hour_charge: 190 ⟵ “Dual Enrollment is $190 per credit hour (an additional $10 per credit hour Technology Fee.) Tennessee resident students may qualify for the Tennessee Dual Enrollment Grant. Most dual enrollment courses are covered by the grant if students qualify, complete all appropriate paperwork, and meet all eli”
  - per_credit_hour_charge: 10 ⟵ “Dual Enrollment is $190 per credit hour (an additional $10 per credit hour Technology Fee.) Tennessee resident students may qualify for the Tennessee Dual Enrollment Grant. Most dual enrollment courses are covered by the grant if students qualify, complete all appropriate paperwork, and meet all eli”
  - per_credit_hour_charge: 100 ⟵ “For 2025-26 school year, the TN Dual Enrollment grant covers full tuition and technology fees toward your first (5) courses. Additional six – ten courses are $100 per credit hour. Students must maintain a minimum 2.0 GPA to keep the grant.”
  - state_grant_accepted: True ⟵ “For 2025-26 school year, the TN Dual Enrollment grant covers full tuition and technology fees toward your first (5) courses. Additional six – ten courses are $100 per credit hour. Students must maintain a minimum 2.0 GPA to keep the grant.”
  - per_credit_hour_charge: 174 ⟵ “$174/credit hour | $10/credit hour – Technology Fee. Tennessee residents are eligible for the TN Dual Enrollment Grant. Visit their website for information and application.”
  - per_credit_hour_charge: 10 ⟵ “$174/credit hour | $10/credit hour – Technology Fee. Tennessee residents are eligible for the TN Dual Enrollment Grant. Visit their website for information and application.”
  - state_grant_accepted: True ⟵ “$174/credit hour | $10/credit hour – Technology Fee. Tennessee residents are eligible for the TN Dual Enrollment Grant. Visit their website for information and application.”
  - max_credit_hours_per_term: 14 ⟵ “At Carson-Newman, students may take up to a maximum of 14 credit hours of Dual Enrollment per semester.”
### `0ecdb84bc6defe87` Christian Brothers University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cbu.edu/admissions-aid/financial-aid/financial-aid-forms/ (sha256 86b1c4e88c09)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Satisfactory Progress for Title IV (PDF) Satisfactory Progress Appeal Form (PDF) Disclaimer: Information contained on this site is subject to change without prior notification.”
### `503e6d5f4cb3b7c8` Christian Brothers University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 eac9e4c2acaa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “DOWNLOAD THE TELS REQUEST FOR CHANGE OF ENROLLMENT STATUS FORM HOPE FAQ’s Appeals Students should submit a letter detailing the reason for dropping below full-time.”
### `611f60e5a8fea3ad` Christian Brothers University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cbu.edu/admissions-aid/financial-aid/financial-aid-resources/ (sha256 5192bec01db7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment The Higher Education Act of 1965, as amended (HEA) provides the authority for the financial aid administrator to exercise discretion in a number of areas when a student has special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “This authority is known as professional judgment (PJ).”
### `486d62c4408a6d70` Dyersburg State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.dscc.edu/wp-content/uploads/2024/11/COA-Adjustment-Request-Form.pdf (sha256 14207191c1a2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Office of Financial Aid 1510 Lake Rd | Dyersburg, TN 38024 financialaid@dscc.edu Fax: 731-286-3354 Phone: 731-286-3350 Cost of Attendance Adjustment Request Student’s Name: Student ID: The Cost of Attendance Adjustment form is for students who have additional expenses during the enrollment period, such as childcare costs, laptops, and supplies.”
  - sentence: budget_increase ⟵ “Cost of Attendance reviews will take place after you complete the FAFSA, and after you receive a financial aid offer notification for the year in which you are requesting a cost of attendance adjustment.”
### `072e7835fa8c7aea` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/hope/appeals.php (sha256 f6e32412720e)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/lottery-appeal-25.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/default.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If you receive notice that you have lost your eligibility for a TELS award, you will need to submit an appeal to the Office of Financial Aid and Scholarships as soon as possible.”
### `38fa467beca7b17f` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php (sha256 4cb91f9b9fb1)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “If your circumstances have not changed since last year, please provide the following to the Office of Financial Aid and Scholarships in person or via email at finaid@etsu.edu. · Signed 2026-27 Dependency Override Appeal form · Signed, dated statement outlining your circumstances and that they have not changed.”
  - sentence: dependency_override ⟵ “Dependency Override For financial aid purposes, a student is considered a dependent of their parents unless the student is: 24 years old married serving on active duty in the US Armed Forces a veteran a parent with dependents an emancipated minor homeless assigned a legal guardian before the age of 18 How to Appeal Contact our Assistant Director of Training and Service to discuss your circumstance”
### `4e0ed53c097b83fe` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf (sha256 e9dd7116362d)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: dependency_override ⟵ “Returning ETSU Students Only: If you were approved last year for a Dependency Override and have submitted your 2026-27 FAFSA application to ETSU, your process is different.”
  - sentence: dependency_override ⟵ “If your circumstances have not changed since last year, please provide the following to the Office of Financial Aid and Scholarships in person or via email at finaid@etsu.edu. • Signed 2026-27 Dependency Override Appeal form • Signed and dated statement outlining your circumstances and that they 2026-27 Dependency have not changed You do not need to submit any additional documentation to our offic”
  - sentence: dependency_override ⟵ “What is a Dependency Override?”
  - sentence: dependency_override ⟵ “What conditions COULD warrant What conditions DO NOT warrant a Dependency Override? a Dependency Override?”
  - sentence: dependency_override ⟵ “Please note the following: • Complete the 2026-27 FAFSA online at www.fafsa.gov prior to completing and submitting the Dependency Override Appeal. • Financial Aid Policy at the East Tennessee State University requires that a student seeking a Dependency Override must complete the Dependency Override Appeal.”
  - sentence: dependency_override ⟵ “Please schedule an appointment online through FASTPASS. • The determination of whether or not to approve a dependency override is made by Student Financial Aid— not the U.S.”
### `4fd258e67f7d9f52` East Tennessee State University — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/ (sha256 eba080aff84c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “General Assembly Merit Scholarship (GAMS) Aspire Award Non-Traditional Lottery Don’t Lose Hope Appeals Process for Hope Getting Help Cost of Attendance Financial Aid TV GoldLink Guide Bucky's Treasure Map Schedule an Appointment Financial Aid Steps School Code 003487 1 | Submit FAFSA 2 | Verification 3 | Check Status 4 | Aid Offers 5 | Confirm Registration 6 | Majors & MinorsCost EstimateRequest I”
### `767c95a2c75e87a4` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf (sha256 e9dd7116362d)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-change-of-circumstance-form.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you have any questions, please contact our Assistant Director of Training and Service by selecting the 'Special Circumstance Appeal' option on our website.”
  - sentence: need_based_special_circumstances ⟵ “Select the 'Special Circumstance Appeal' option.”
### `870cb21945b09ba2` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf (sha256 e9dd7116362d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “A dependency override occurs when a financial aid administrator exercises professional judgment and overrides the Department of Education’s criteria for dependent students.”
### `98c007b93a81e797` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php (sha256 4cb91f9b9fb1)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-change-of-circumstance-form.pdf,https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “There are two different appeal processes available to you and your family: Special Circumstances Appeal Dependency Override For ETSU to grant an appeal, there must be compelling reasons.”
  - sentence: need_based_special_circumstances ⟵ “The first step is to be sure to select the correct forms for the aid year in which you are submitting an appeal. 2026-2027 Forms Special Circumstance Appeal Dependency Override Returning ETSU Students Only: If you were approved last year for a Dependency Override and have submitted your 2026-27 FAFSA application to ETSU, your process is different.”
  - sentence: need_based_special_circumstances ⟵ “If you have any questions, please make an appointment with our Assistant Director of Training and Service by selecting the 'Special Circumstance Appeals' option.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Should I Appeal?”
  - sentence: need_based_special_circumstances ⟵ “What Special Circumstances We DO Consider: Loss or change of employment Loss or change in untaxed income (child support, Social Security, or other benefits) Divorce or separation of parents or student Death of parent(s) or spouse Unusual medical expenses (not covered by insurance) One-time taxable income used for life changing events (e.g.”
### `9ab6f32695eb276a` East Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/max-appeal-edited.pdf (sha256 bf6d4e23f8ed)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/gpa-pace-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php,https://www.etsu.edu/financial-aid-and-scholarships/policies/satisfactorypro.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “TENNESSEE STATE OFFIC OF UNIVERSITY Finan Satisfactory Academic Progress Form – Maximum Time Name ETSU ID Number E ETSU email Phone: IMPORTANT: SAP appeals are reviewed by Committee according to the published Appeals Review Committee Schedule.”
### `9b38d386567da31c` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/policies/satisfactorypro.php (sha256 cf5ae3ccedcc)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/gpa-pace-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/documents/max-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Students who fail to earn 100% of attempted hours due to extenuating circumstances have the opportunity to submit a SAP appeal.”
  - sentence: sap_appeal ⟵ “Students who choose to appeal, will be required to complete the Satisfactory Academic Progress Form – Maximum Time Appeal form (not the GPA and PACE appeal), since they will not be able to complete 100% of their program of study.”
  - sentence: sap_appeal ⟵ “Steps to file an appeal: Complete and submit the correct Satisfactory Academic Progress Appeal Form based on your situation (GPA/PACE or Max Hours).”
### `b1ffd266f97bcdf9` East Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/lottery-appeal-25.pdf (sha256 ffff37221745)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/forms/default.php,https://www.etsu.edu/financial-aid-and-scholarships/scholarships/hope/appeals.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “9 EAST TENNESSEE STATE - UNIVERSITY ETSU Tennessee Education Lottery Scholarship Appeal Form How to submit: Complete the following information and submit your appeal (including your statement and supporting documentation) to the Office of Student Financial Aid and Scholarships, Box 70722, ETSU, Johnson City, TN; Fax: 423-439-5855; Room 105, Burgin Dossett Hall.”
### `c0f6aab38052f5ed` East Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-change-of-circumstance-form.pdf (sha256 69ee1b8c2787)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Appeal Form Name ETSU ID Number E _ Address City/State/Zip: _ _ The Office of Financial Aid and Scholarships recognizes that many families have changes in income or family situations that cannot be reflected in the 2024 tax return.”
  - sentence: need_based_special_circumstances ⟵ “A Special Circumstances Appeal may be filed if you or your family have extenuating circumstances, which you believe warrant a reevaluation of your financial aid.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeals received after 11/15/26 will not be considered until a signedcopy ofa2026 tax return, including all schedules, and 2026 W-2s and/or 1099s have been submitted.”
  - sentence: need_based_special_circumstances ⟵ “Student Signature Date Parent/Spouse Signature Date To submit the completed form, please make an appointment with our Assistant Director of Training and Service by selecting the 'Special Circumstance Appeal' option on our website.”
### `c895ecdfbf356436` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php (sha256 4cb91f9b9fb1)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/gpa-pace-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/documents/max-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/policies/satisfactorypro.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeals Academic Appeal Forms and Links In certain circumstances, students have the option to appeal based on their academic performance.”
### `d7f86fc0f22066a7` East Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/default.php (sha256 7c725e141c81)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/lottery-appeal-25.pdf,https://www.etsu.edu/financial-aid-and-scholarships/scholarships/hope/appeals.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Financial Aid Forms Appeal SAP, Professional Judgment, Lottery, Refund/Withdraw appeal forms Discount ETSU Employee, TBR/UT Employee, State Employee and Certified Public School Teacher forms Withdrawal The withdrawal form can be found under the 'Records Office Services' tab on the page linked above.”
### `f2b218ce6a04850b` East Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/gpa-pace-appeal-edited.pdf (sha256 9b5ac0691990)
- issues: semantic_review_required, conflicting_sources:https://www.etsu.edu/financial-aid-and-scholarships/documents/max-appeal-edited.pdf,https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php,https://www.etsu.edu/financial-aid-and-scholarships/policies/satisfactorypro.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “TENNESSEE STATE OFFIC UNIVERSITY Satisfactory Academic Progress Form – GPA and PACE Name ETSU ID Number E ETSU email Phone: IMPORTANT: SAP appeals are reviewed by Committee according to the published Appeals Review Committee Schedule.”
### `fc3df6516cfb04d3` Freed-Hardeman University — appeals 2026-27 [new] (source_unlabeled)
- source: https://fhu.edu/admissions-aid/financial-aid/grants-scholarships-discounts/hope-scholarship/ (sha256 06f7a7c79e65)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “The student must complete a HOPE Scholarship Appeal Form (for the reasons listed above)and submit it to the Director of Financial Aid.”
  - sentence: scholarship_retention_appeal ⟵ “Appeals should be submitted within 30 days of notification of the loss of the HOPE Scholarship.”
### `ff924c40c55708b6` Freed-Hardeman University — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://fhu.edu/wp-content/uploads/dual-enrollment-handbook-oos.pdf (sha256 3fb920237dc7)
- issues: stale_year_label:2024-25
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 6}
  - eligibility_tier: 3.0 ⟵ “● Have a cumulative GPA of 3.000 with an ACT composite of 21 OR”
  - eligibility_tier: 3.5 ⟵ “● Have a cumulative GPA of 3.500 without an ACT score”
  - max_credit_hours_per_term: 12 ⟵ “Traditional DE students can take up to 12 hours per semester if approved by your”
  - eligibility_tier: 3.0 ⟵ “cumulative 3.0 grade point average on at least 12 hours of FHU dual enrollment”
  - eligibility_tier: 3.0 ⟵ “1. A student must have a cumulative high school GPA of 3.000 or above”
  - eligibility_tier: 3.5 ⟵ “2. A student must have a cumulative high school GPA of 3.500 or higher”
  - eligibility_tier: 3.0 ⟵ “○ A 3.0 or higher GPA on a 4.0 scale in the two high school algebra”
### `mb86ddc470a9e4cf` Freed-Hardeman University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://fhu.edu/wp-content/uploads/dual-enrollment-handbook-tn.pdf (sha256 a15631fc2f1e)
- issues: ambiguous_year_labels, state_grant_mixed_statements
- checks: {"fields": ["college_gpa_to_continue", "per_credit_hour_charges"], "merged_pages": 25, "tiers": 6}
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA of 3.000 or above and ACT composite score of 21 or higher, or SAT equivalent OR”
  - eligibility_tier: 3.5 ⟵ “Cumulative GPA of 3.500 or above”
  - state_grant_accepted: True ⟵ “If you are a resident of Tennessee, you may qualify for the TN Dual Enrollment Grant. DE courses are offered at a deeply discounted tuition rate. Other discounts, which might apply to you as a full-time student, are not applicable for the tuition of a Dual Enrollment course.”
  - eligibility_tier: 3.25 ⟵ “A cumulative high school GPA of 3.25 or higher and ACT composite score of 21 or higher or SAT equivalent; OR cumulative high school GPA or 3.75 or higher.”
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA of 3.000 or above and ACT composite score of 21 or higher, or SAT equivalent OR”
  - eligibility_tier: 3.5 ⟵ “Cumulative GPA of 3.500 or above”
  - state_grant_accepted: True ⟵ “If you are a resident of Tennessee, you may qualify for the TN Dual Enrollment Grant. DE courses are offered at a deeply discounted tuition rate. Other discounts, which might apply to you as a full-time student, are not applicable for the tuition of a Dual Enrollment course.”
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA of 3.000 or above and ACT composite score of 21 or higher, or SAT equivalent OR”
  - eligibility_tier: 3.5 ⟵ “Cumulative GPA of 3.500 or above”
  - state_grant_accepted: True ⟵ “If you are a resident of Tennessee, you may qualify for the TN Dual Enrollment Grant. DE courses are offered at a deeply discounted tuition rate. Other discounts, which might apply to you as a full-time student, are not applicable for the tuition of a Dual Enrollment course.”
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA of 3.000 or above and ACT composite score of 21 or higher, or SAT equivalent OR”
  - eligibility_tier: 3.5 ⟵ “Cumulative GPA of 3.500 or above”
  - state_grant_accepted: True ⟵ “If you are a resident of Tennessee, you may qualify for the TN Dual Enrollment Grant. DE courses are offered at a deeply discounted tuition rate. Other discounts, which might apply to you as a full-time student, are not applicable for the tuition of a Dual Enrollment course.”
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA of 3.000 or above and ACT composite score of 21 or higher, or SAT equivalent OR”
  - eligibility_tier: 3.5 ⟵ “Cumulative GPA of 3.500 or above”
  - state_grant_accepted: True ⟵ “If you are a resident of Tennessee, you may qualify for the TN Dual Enrollment Grant. DE courses are offered at a deeply discounted tuition rate. Other discounts, which might apply to you as a full-time student, are not applicable for the tuition of a Dual Enrollment course.”
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA of 3.000 or above and ACT composite score of 21 or higher, or SAT equivalent OR”
  - eligibility_tier: 3.5 ⟵ “Cumulative GPA of 3.500 or above”
  - state_grant_accepted: True ⟵ “If you are a resident of Tennessee, you may qualify for the TN Dual Enrollment Grant. DE courses are offered at a deeply discounted tuition rate. Other discounts, which might apply to you as a full-time student, are not applicable for the tuition of a Dual Enrollment course.”
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA of 3.000 or above and ACT composite score of 21 or higher, or SAT equivalent OR”
  - eligibility_tier: 3.5 ⟵ “Cumulative GPA of 3.500 or above”
  - state_grant_accepted: True ⟵ “If you are a resident of Tennessee, you may qualify for the TN Dual Enrollment Grant. DE courses are offered at a deeply discounted tuition rate. Other discounts, which might apply to you as a full-time student, are not applicable for the tuition of a Dual Enrollment course.”
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA of 3.000 or above and ACT composite score of 21 or higher, or SAT equivalent OR”
  - eligibility_tier: 3.5 ⟵ “Cumulative GPA of 3.500 or above”
  - state_grant_accepted: True ⟵ “If you are a resident of Tennessee, you may qualify for the TN Dual Enrollment Grant. DE courses are offered at a deeply discounted tuition rate. Other discounts, which might apply to you as a full-time student, are not applicable for the tuition of a Dual Enrollment course.”
  - … 61 more rows
### `0e6e9f72ca7fb463` Jackson State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://jscc.edu/costs-and-aid/satisfactory-academic-progress-sap/ (sha256 6994832800fb)
- issues: semantic_review_required, conflicting_sources:https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/acadplan.pdf,https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/faq-sap-updated-040615.pdf,https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/satisfactory.academic.progress.policy.20260428.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal Process (§ 668.34, (d) (2)): Students can file a Financial Aid appeal to regain eligibility if there were extenuating circumstances that warrant a student to continue receiving Title IV and/or State aid. (§ 668.34, (a) (9) (ii)) To successfully appeal the student must: Complete and submit a Satisfactory Academic Progress Appeal An Academic Plan may also be required.”
  - sentence: sap_appeal ⟵ “Financial Aid Probation Approved status is assigned to a student who fails to meet satisfactory academic progress guidelines, submitted an appeal, the appeal was approved, and the student is projected to meet satisfactory academic progress standards or complete their degree within one semester.”
### `4916fc775f02fceb` Jackson State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/acadplan.pdf (sha256 1d5c1521ded4)
- issues: semantic_review_required, conflicting_sources:https://jscc.edu/costs-and-aid/satisfactory-academic-progress-sap/,https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/faq-sap-updated-040615.pdf,https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/satisfactory.academic.progress.policy.20260428.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Academic Plan Form This plan must be completed, signed by your academic advisor or counselor, and attached to your SAP Appeal Form.”
### `9e2fdb1dc7b30e26` Jackson State Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/financial-aid-forms/ (sha256 90d77634db14)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appeal Process Any loss of eligibility for financial aid because of this policy may be appealed by submitting an online SAP Appeal form to the Student Aid & Awards Committee.”
  - sentence: sap_appeal ⟵ “Appeal Process Students must: Submit the online Satisfactory Academic Progress Appeal form.”
  - sentence: sap_appeal ⟵ “The Financial Aid Office will notify, by letter or email to the student’s JSCC email address, any student that does not meet minimum satisfactory academic progress requirements as well as the results of any appeal.”
### `ad444f0ada74b5f0` Jackson State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/satisfactory.academic.progress.policy.20260428.pdf (sha256 e28d1d94bdb2)
- issues: semantic_review_required, conflicting_sources:https://jscc.edu/costs-and-aid/satisfactory-academic-progress-sap/,https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/acadplan.pdf,https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/faq-sap-updated-040615.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Financial aid probation is a status assigned by Jackson State to students who fail to make satisfactory academic progress and have had their eligibility for aid reinstated for one semester after an appeal.”
  - sentence: sap_appeal ⟵ “Page 6 of 8 Satisfactory Academic Progress (SAP) Policy Appeal Process (§ 668.34, (d) (2)): Students can file a Financial Aid appeal to regain eligibility if there were extenuating circumstances that warrant a student to continue receiving Title IV and/or State aid. (§ 668.34, (a) (9) (ii)) To successfully appeal the student must: 1.”
  - sentence: sap_appeal ⟵ “Complete and submit a Satisfactory Academic Progress Appeal Form.”
  - sentence: sap_appeal ⟵ “Page 7 of 8 Satisfactory Academic Progress (SAP) Policy Financial Aid Probation Approved status is assigned to a student who fails to meet satisfactory academic progress guidelines, submitted an appeal, the appeal was approved, and the student is projected to meet satisfactory academic progress standards or complete their degree within one semester.”
### `c41fa897749cc061` Jackson State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/faq-sap-updated-040615.pdf (sha256 179dd5621176)
- issues: semantic_review_required, conflicting_sources:https://jscc.edu/costs-and-aid/satisfactory-academic-progress-sap/,https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/acadplan.pdf,https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/satisfactory.academic.progress.policy.20260428.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Or, if the reason for your unsatisfactory academic progress was not due to GPA and you had extenuating circumstances, you may choose to appeal.”
### `1a4423c33f866215` Jackson State Community College — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: components_do_not_reconcile
- checks: {"columns": 3, "components_reconcile": false, "rows": 7}
  - with_parents_or_family:TUITION & FEES*: 2535 ⟵ “TUITION & FEES* | $2,535 | $2,535 | $2,535”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3841 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - with_parents_or_family:TOTAL: (FOR FALL AND SPRING): 21318 ⟵ “TOTAL: (FOR FALL AND SPRING) | $21,318 | $29,312 | $18,652”
  - with_parents_or_family:TOTAL (PER SEMESTER): 10659 ⟵ “TOTAL (PER SEMESTER) | $10,659 | $14,656 | $9,326”
  - off_campus_not_with_family:TUITION & FEES*: 2535 ⟵ “TUITION & FEES* | $2,535 | $2,535 | $2,535”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7838 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - off_campus_not_with_family:TOTAL: (FOR FALL AND SPRING): 29312 ⟵ “TOTAL: (FOR FALL AND SPRING) | $21,318 | $29,312 | $18,652”
  - off_campus_not_with_family:TOTAL (PER SEMESTER): 14656 ⟵ “TOTAL (PER SEMESTER) | $10,659 | $14,656 | $9,326”
  - other:TUITION & FEES*: 2535 ⟵ “TUITION & FEES* | $2,535 | $2,535 | $2,535”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2508 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - other:TOTAL: (FOR FALL AND SPRING): 18652 ⟵ “TOTAL: (FOR FALL AND SPRING) | $21,318 | $29,312 | $18,652”
  - other:TOTAL (PER SEMESTER): 9326 ⟵ “TOTAL (PER SEMESTER) | $10,659 | $14,656 | $9,326”
### `22579b5babe33f65` Jackson State Community College — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": false, "rows": 7}
  - with_parents_or_family:TUITION & FEES*: 8862 ⟵ “TUITION & FEES* | $8,862 | $8,862 | $8,862”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3452 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - with_parents_or_family:TOTAL (FOR FALL AND SPRING): 32732 ⟵ “TOTAL (FOR FALL AND SPRING) | $32,732 | $40,364 | $30,189”
  - with_parents_or_family:TOTAL (PER SEMESTER): 16366 ⟵ “TOTAL (PER SEMESTER) | $16,366 | $20,182 | $15,094”
  - off_campus_not_with_family:TUITION & FEES*: 8862 ⟵ “TUITION & FEES* | $8,862 | $8,862 | $8,862”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7268 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - off_campus_not_with_family:TOTAL (FOR FALL AND SPRING): 40364 ⟵ “TOTAL (FOR FALL AND SPRING) | $32,732 | $40,364 | $30,189”
  - off_campus_not_with_family:TOTAL (PER SEMESTER): 20182 ⟵ “TOTAL (PER SEMESTER) | $16,366 | $20,182 | $15,094”
  - other:TUITION & FEES*: 8862 ⟵ “TUITION & FEES* | $8,862 | $8,862 | $8,862”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2180 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - other:TOTAL (FOR FALL AND SPRING): 30189 ⟵ “TOTAL (FOR FALL AND SPRING) | $32,732 | $40,364 | $30,189”
  - other:TOTAL (PER SEMESTER): 15094 ⟵ “TOTAL (PER SEMESTER) | $16,366 | $20,182 | $15,094”
### `3700d28276a0159a` Jackson State Community College — costs 2025-26 · residency=in_state [same] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": false, "rows": 7}
  - with_parents_or_family:TUITION & FEES*: 2447 ⟵ “TUITION & FEES* | $2,447 | $2,447 | $2,447”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3550 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - with_parents_or_family:TOTAL: (FOR FALL AND SPRING): 20324 ⟵ “TOTAL: (FOR FALL AND SPRING) | $20,324 | $28,172 | $17,708”
  - with_parents_or_family:TOTAL (PER SEMESTER): 10162 ⟵ “TOTAL (PER SEMESTER) | $10,162 | $14,086 | $8,854”
  - off_campus_not_with_family:TUITION & FEES*: 2447 ⟵ “TUITION & FEES* | $2,447 | $2,447 | $2,447”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7474 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - off_campus_not_with_family:TOTAL: (FOR FALL AND SPRING): 28172 ⟵ “TOTAL: (FOR FALL AND SPRING) | $20,324 | $28,172 | $17,708”
  - off_campus_not_with_family:TOTAL (PER SEMESTER): 14086 ⟵ “TOTAL (PER SEMESTER) | $10,162 | $14,086 | $8,854”
  - other:TUITION & FEES*: 2447 ⟵ “TUITION & FEES* | $2,447 | $2,447 | $2,447”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2242 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - other:TOTAL: (FOR FALL AND SPRING): 17708 ⟵ “TOTAL: (FOR FALL AND SPRING) | $20,324 | $28,172 | $17,708”
  - other:TOTAL (PER SEMESTER): 8854 ⟵ “TOTAL (PER SEMESTER) | $10,162 | $14,086 | $8,854”
### `bab5795119104dcc` Jackson State Community College — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": false, "rows": 7}
  - with_parents_or_family:TUITION & FEES*: 2370 ⟵ “TUITION & FEES* | $2,370 | $2,370 | $2,370”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3452 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - with_parents_or_family:TOTAL (FOR FALL AND SPRING): 19748 ⟵ “TOTAL (FOR FALL AND SPRING) | $19,748 | $27,380 | $17,205”
  - with_parents_or_family:TOTAL (PER SEMESTER): 9874 ⟵ “TOTAL (PER SEMESTER) | $9,874 | $13,690 | $8,602”
  - off_campus_not_with_family:TUITION & FEES*: 2370 ⟵ “TUITION & FEES* | $2,370 | $2,370 | $2,370”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7268 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - off_campus_not_with_family:TOTAL (FOR FALL AND SPRING): 27380 ⟵ “TOTAL (FOR FALL AND SPRING) | $19,748 | $27,380 | $17,205”
  - off_campus_not_with_family:TOTAL (PER SEMESTER): 13690 ⟵ “TOTAL (PER SEMESTER) | $9,874 | $13,690 | $8,602”
  - other:TUITION & FEES*: 2370 ⟵ “TUITION & FEES* | $2,370 | $2,370 | $2,370”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2180 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - other:TOTAL (FOR FALL AND SPRING): 17205 ⟵ “TOTAL (FOR FALL AND SPRING) | $19,748 | $27,380 | $17,205”
  - other:TOTAL (PER SEMESTER): 8602 ⟵ “TOTAL (PER SEMESTER) | $9,874 | $13,690 | $8,602”
### `bcc3a95e9085b1ee` Jackson State Community College — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: components_do_not_reconcile
- checks: {"columns": 3, "components_reconcile": false, "rows": 7}
  - with_parents_or_family:TUITION & FEES*: 4275 ⟵ “TUITION & FEES* | $4,275 | $4,275 | $4,275”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3841 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - with_parents_or_family:TOTAL: (FOR FALL AND SPRING): 24796 ⟵ “TOTAL: (FOR FALL AND SPRING) | $24,796 | $32,791 | $22,131”
  - with_parents_or_family:TOTAL (PER SEMESTER): 12398 ⟵ “TOTAL (PER SEMESTER) | $12,398 | $16,396 | $11,066”
  - off_campus_not_with_family:TUITION & FEES*: 4275 ⟵ “TUITION & FEES* | $4,275 | $4,275 | $4,275”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7838 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - off_campus_not_with_family:TOTAL: (FOR FALL AND SPRING): 32791 ⟵ “TOTAL: (FOR FALL AND SPRING) | $24,796 | $32,791 | $22,131”
  - off_campus_not_with_family:TOTAL (PER SEMESTER): 16396 ⟵ “TOTAL (PER SEMESTER) | $12,398 | $16,396 | $11,066”
  - other:TUITION & FEES*: 4275 ⟵ “TUITION & FEES* | $4,275 | $4,275 | $4,275”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2508 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - other:TOTAL: (FOR FALL AND SPRING): 22131 ⟵ “TOTAL: (FOR FALL AND SPRING) | $24,796 | $32,791 | $22,131”
  - other:TOTAL (PER SEMESTER): 11066 ⟵ “TOTAL (PER SEMESTER) | $12,398 | $16,396 | $11,066”
### `f8d65a949dbe6b49` Jackson State Community College — costs 2025-26 · residency=out_of_state [same] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": false, "rows": 7}
  - with_parents_or_family:TUITION & FEES*: 4127 ⟵ “TUITION & FEES* | $4,127 | $4,127 | $4,127”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3550 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - with_parents_or_family:TOTAL: (FOR FALL AND SPRING): 23684 ⟵ “TOTAL: (FOR FALL AND SPRING) | $23,684 | $31,532 | $21,068”
  - with_parents_or_family:TOTAL (PER SEMESTER): 11842 ⟵ “TOTAL (PER SEMESTER) | $11,842 | $15,766 | $10,534”
  - off_campus_not_with_family:TUITION & FEES*: 4127 ⟵ “TUITION & FEES* | $4,127 | $4,127 | $4,127”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7474 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - off_campus_not_with_family:TOTAL: (FOR FALL AND SPRING): 31532 ⟵ “TOTAL: (FOR FALL AND SPRING) | $23,684 | $31,532 | $21,068”
  - off_campus_not_with_family:TOTAL (PER SEMESTER): 15766 ⟵ “TOTAL (PER SEMESTER) | $11,842 | $15,766 | $10,534”
  - other:TUITION & FEES*: 4127 ⟵ “TUITION & FEES* | $4,127 | $4,127 | $4,127”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2242 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - other:TOTAL: (FOR FALL AND SPRING): 21068 ⟵ “TOTAL: (FOR FALL AND SPRING) | $23,684 | $31,532 | $21,068”
  - other:TOTAL (PER SEMESTER): 10534 ⟵ “TOTAL (PER SEMESTER) | $11,842 | $15,766 | $10,534”
### `ea983ca313d68c04` Jackson State Community College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://jscc.edu/media/jackson-state/content-assets/documents/costs--aid/Dual-Enrollment-2025-2026-Fee-Schedule.pdf (sha256 1f01f2f11c68)
- issues: stale_year_label:2025-26
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 191 ⟵ “Instate 1 - 12 hours = $191/hr”
  - per_credit_hour_charge: 10 ⟵ “* Technology Fee - $10/hour up to 11 hours; max $116.00 for 12 hours and above.”
  - per_credit_hour_charge: 331 ⟵ “Out-of-State 1 - 12 hours = $331/hr”
  - per_credit_hour_charge: 10 ⟵ “* Technology Fee - $10/hour up to 11 hours; max $116.00 for 12 hours and above.”
### `m12d4e5dc2892641` Jackson State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://jscc.edu/admissions/apply/dual-enrollment/ (sha256 47d14d41dd14)
- issues: conflicting_values:college_gpa_to_continue, state_grant_mixed_statements
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “i. 3.0 High School GPA AND satisfy specific course requirements by one of the following ways:”
  - college_gpa_to_continue: 2.0 ⟵ “Students must maintain a 2.0 College GPA (different from HS GPA) to receive the grant in future semesters”
  - eligibility_tier: 3.0 ⟵ “i. 3.0 High School GPA AND satisfy specific course requirements by one of the following ways:”
  - college_gpa_to_continue: 3.0 ⟵ “Students must maintain a 3.0 College GPA (different from high school GPA) to receive the scholarship in future semesters”
  - college_gpa_to_continue: 2.0 ⟵ “2. A student must maintain a cumulative 2.0 GPA for all college courses certified under the Dual Enrollment Grant (DEG).”
  - state_grant_accepted: True ⟵ “Students who do not maintain the minimum GPA will no longer be eligible for the DEG and may be withdrawn from the”
  - state_grant_accepted: False ⟵ “the student’s DE if the DEG does not cover all tuition expenses or if the student does not qualify for the grant.”
  - state_grant_accepted: True ⟵ “4. Eligible students may receive DEG funding for up to 10 courses.”
  - state_grant_accepted: True ⟵ “university simultaneously and receive the Dual Enrollment Grant at all eligible schools. This process has important”
### `63217249422066fb` John A Gupton College — appeals 2026-27 [new] (source_unlabeled)
- source: https://guptoncollege.edu/financial-aid-2/satisfactory-academic-scholarship/ (sha256 79b39af941b6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “All appeals must include documentation of any unusual circumstance that contributed to the probation.”
### `7b7f97cefa99d352` John A Gupton College — appeals 2026-27 [new] (source_unlabeled)
- source: https://guptoncollege.edu/financial-aid-2/satisfactory-academic-scholarship/ (sha256 79b39af941b6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “All probations may be appealed in writing by completing a Satisfactory Academic Progress Appeal Form (located in the Financial Aid Office).”
### `16d0922fbf512ee5` Johnson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://johnsonu.edu/admissions/financial-aid/financial-aid-faqs/ (sha256 21756cec5c4f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You may have a special circumstance and will need to contact the financial aid director with a detailed explanation of your circumstance.”
### `a6e2bc3e61ca0566` Johnson University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://johnsonu.edu/admissions/tuition/ (sha256 14bc220ac1c5)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "rows": 8}
  - column:Tuition/Fees: 22612 ⟵ “Tuition/Fees | $22,612 | $8,496”
  - column:Housing/Food: 9501 ⟵ “Housing/Food | $9,501 | $4,750”
  - column:Transportation: 3220 ⟵ “Transportation | $3,220 | $1,610”
  - column:Books/Supplies: 1200 ⟵ “Books/Supplies | $1,200 | $600”
  - column:Personal: 1600 ⟵ “Personal | $1,600 | $800”
  - column:Loan Fees: 68 ⟵ “Loan Fees | $68 | $68”
  - column:Annual COA: 38200 ⟵ “Annual COA | $38,200 | $16,324”
  - column:Semester COA: 19100 ⟵ “Semester COA | $19,100 | $8,162”
  - column:Tuition/Fees: 8496 ⟵ “Tuition/Fees | $22,612 | $8,496”
  - column:Housing/Food: 4750 ⟵ “Housing/Food | $9,501 | $4,750”
  - column:Transportation: 1610 ⟵ “Transportation | $3,220 | $1,610”
  - column:Books/Supplies: 600 ⟵ “Books/Supplies | $1,200 | $600”
  - column:Personal: 800 ⟵ “Personal | $1,600 | $800”
  - column:Loan Fees: 68 ⟵ “Loan Fees | $68 | $68”
  - column:Annual COA: 16324 ⟵ “Annual COA | $38,200 | $16,324”
  - column:Semester COA: 8162 ⟵ “Semester COA | $19,100 | $8,162”
### `773e332215cfb1a2` Lane College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.lanecollege.edu/financial-aid-tuition/federal-and-state-aid/dependency-and-verification (sha256 541d1cd40340)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Parental information must be included on the FAFSA unless the student is: an orphan or ward of the court a veteran a graduate of professional student married has legal dependents other than a spouse 24 years old a student with documented special circumstances for independence SPECIAL CIRCUMSTANCES Although the process of determining need for financial aid is generally the same for all students, th”
  - sentence: need_based_special_circumstances ⟵ “If you feel you have special circumstances, contact the Office of Financial Aid. 2025-2026 Dependent Verification Worksheet V1 2025-2026 Independent Verification Worksheet V1 2025-2026 Dependent Verification Worksheet V4/V5 2025-2026 Independent Verification Worksheet V4/V5 News Employment Alumni Financial Services Communications IT Help Desk Institutional Research and Effectiveness Consumer Infor”
### `b42969313a508f7a` Lane College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lanecollege.edu/financial-aid-tuition/financial-aid-sap (sha256 3bb451938f69)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: sap_appeal ⟵ “Appeals Students placed on Financial Aid Suspension may appeal to the SAP Appeal Committee for the following reasons: serious illness or accident related to the student; death, accident, or serious illness in the immediate family (parent/guardian or sibling); and/or other extenuating circumstances directly affecting academic performance.”
  - sentence: sap_appeal ⟵ “Appeal Process Students must submit a completed SAP Appeal Form to the Office of Financial Aid.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Form will be sent to the student.”
  - sentence: sap_appeal ⟵ “Completed SAP Appeals will be reviewed within two weeks of submission.”
  - sentence: sap_appeal ⟵ “Tips for Writing a Successful Appeal You have the right to appeal your Financial Aid Satisfactory Academic Progress Suspension.”
  - sentence: sap_appeal ⟵ “Be honest with yourself and the FA SAP Appeal Committee.”
### `3489ed4267f75802` Lane College — costs 2025-26 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.lanecollege.edu/financial-aid-tuition/college-costs (sha256 ec5554585949)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition (12-16 hours): 10198.0 ⟵ “Tuition (12-16 hours) | $5,099.00 | $5,099.00 | $10,198.00”
  - column:Text Book Fee: 770.0 ⟵ “Text Book Fee | $385.00 | $385.00 | $770.00”
  - column:Matriculation Fee: 1000.0 ⟵ “Matriculation Fee | $500.00 | $ 500.00 | $ 1,000.00”
  - column:Technology Fee: 700.0 ⟵ “Technology Fee | $350.00 | $350.00 | $700.00”
  - column:Student Activity Fee: 250.0 ⟵ “Student Activity Fee | $125.00 | $125.00 | $250.00”
  - column:Housing (9-Month): 5240.0 ⟵ “Housing (9-Month) | $2,620.00 | $2,620.00 | $5,240.00”
  - column:Meal Plan (9-Month): 3140.0 ⟵ “Meal Plan (9-Month) | $1,570.00 | $1,570.00 | $3,140.00”
  - column:Health Service Fee: 150.0 ⟵ “Health Service Fee | $75.00 | $75.00 | $150.00”
  - column:Total: 21448.0 ⟵ “Total | $10,724.00 | $10,724.00 | $21,448.00”
### `8c01be759d686005` Lee University — admissions_metrics 2024-25 [same] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/2024-2025-CDS.pdf (sha256 0e1d4e31cec3)
- issues: stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 2388 ⟵ “Total applied                                                                          2,388”
  - admits: 1684 ⟵ “Total admitted                                                                         1,684”
  - enrolled: 589 ⟵ “Total enrolled                                                                          589”
  - sat_composite_25..75: [1020, 1140, 1210] ⟵ “SAT Composite                                                        1020                               1140                               1210”
  - sat_reading_25..75: [540, 580, 630] ⟵ “SAT Evidence-Based Reading and Writing                               540                                580                                630”
  - sat_math_25..75: [500, 550, 600] ⟵ “SAT Math                                                             500                                550                                600”
  - act_25..75: [20, 23, 27] ⟵ “ACT Composite                                                         20                                 23                                 27”
### `37e45fdacb761600` Lee University — appeals 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/financial-aid/scholarships/ (sha256 d71004083c61)
- issues: stale_year_label:2020-21, semantic_review_required, conflicting_sources:https://www.leeuniversity.edu/financial-aid/scholarships/,https://www.leeuniversity.edu/financial-aid/scholarships/?source=mw-scholarship-cta,https://www.leeuniversity.edu/wp-content/uploads/Scholarships-TELS-SAP-Standards.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Information on enrollment, continued eligibility, and student appeal requirements for the HOPE scholarship can be found here. × Tennessee Minority Teaching Fellows Program This award is for entering freshmen with a 2.5 high school GPA on a 4.0 scale.”
### `4a528c2c71470cb5` Lee University — appeals 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/Scholarships-TELS-SAP-Standards.pdf (sha256 8b44ac676e1d)
- issues: stale_year_label:2020-21, semantic_review_required, conflicting_sources:https://www.leeuniversity.edu/financial-aid/scholarships/,https://www.leeuniversity.edu/financial-aid/scholarships/,https://www.leeuniversity.edu/financial-aid/scholarships/?source=mw-scholarship-cta
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: scholarship_retention_appeal ⟵ “GPA Review & Continuous Enrollment Appeal Process GPA Standard Review Request As per Tennessee Code Annotated Rule 1640-01-19-.28 the Institutional Review Panel (IRP) does not have the authority to decide on an appeal due to a low HOPE GPA.”
  - sentence: scholarship_retention_appeal ⟵ “Continuous Enrollment Appeal Students who are not eligible for TN HOPE due to not meeting the Continuous enrollment standard may submit an appeal to the Financial Aid Office – Institutional Review Panel (IRP).”
  - sentence: scholarship_retention_appeal ⟵ “For more details, visit TSAC’s website at: https://www.tn.gov/content/tn/collegepays/money-for-college/tn-education-lottery-programs/tels-program-and-tn-promis- scholarship-appeals-and -exeptions.html T:\Document Printing\2020-2021 (Updated 10/28/2020)”
### `4b05dd351d422408` Lee University — appeals 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/Scholarships-TELS-SAP-Standards.pdf (sha256 8b44ac676e1d)
- issues: stale_year_label:2020-21, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Tennessee HOPE Scholarship Retention Standards & Appeal Process Students must maintain Satisfactory Academic Progress AND Continuous Enrollment as outlined below to retain eligibility for Tennessee HOPE Scholarship.”
### `4e19e05cef107802` Lee University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.leeuniversity.edu/financial-aid/cost/ (sha256 12a1e2671c68)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Information on enrollment, continued eligibility, and student appeal requirements for the HOPE scholarship can be found here. × Tennessee Minority Teaching Fellows Program This award is for entering freshmen with a 2.5 high school GPA on a 4.0 scale.”
### `5a0f5ce4030f9ea7` Lee University — appeals 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/financial-aid/scholarships/?source=mw-scholarship-cta (sha256 3b0597b2fc6c)
- issues: stale_year_label:2020-21, semantic_review_required, conflicting_sources:https://www.leeuniversity.edu/financial-aid/scholarships/,https://www.leeuniversity.edu/financial-aid/scholarships/,https://www.leeuniversity.edu/wp-content/uploads/Scholarships-TELS-SAP-Standards.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Information on enrollment, continued eligibility, and student appeal requirements for the HOPE scholarship can be found here. × Tennessee Minority Teaching Fellows Program This award is for entering freshmen with a 2.5 high school GPA on a 4.0 scale.”
### `c1397afc7071ef6b` Lee University — appeals 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/financial-aid/scholarships/?source=mw-scholarship-cta (sha256 3b0597b2fc6c)
- issues: stale_year_label:2020-21, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If there are extreme special circumstances then you need to fill out a Special Conditions form and schedule an appointment to meet with the Director of Financial Aid.”
### `c6c29e01015bc9c5` Lee University — appeals 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/financial-aid/scholarships/ (sha256 a6e9eca20b9a)
- issues: stale_year_label:2020-21, semantic_review_required, conflicting_sources:https://www.leeuniversity.edu/financial-aid/scholarships/,https://www.leeuniversity.edu/financial-aid/scholarships/?source=mw-scholarship-cta,https://www.leeuniversity.edu/wp-content/uploads/Scholarships-TELS-SAP-Standards.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Information on enrollment, continued eligibility, and student appeal requirements for the HOPE scholarship can be found here. × Tennessee Minority Teaching Fellows Program This award is for entering freshmen with a 2.5 high school GPA on a 4.0 scale.”
### `defb709da79783b8` Lee University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.leeuniversity.edu/financial-aid/cost/ (sha256 12a1e2671c68)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If there are extreme special circumstances then you need to fill out a Special Conditions form and schedule an appointment to meet with the Director of Financial Aid.”
### `526d008253c66f25` Lincoln Memorial University — appeals 2026-27 [new] (source_unlabeled)
- source: https://undergraduatecatalog.lmunet.edu/financial-aid-satisfactory-academic-progress (sha256 1e1109d06349)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeals Students who are on Financial Aid Suspension may appeal this decision by contacting Student Financial Services.”
### `7255008b9adf3bd5` Lincoln Memorial University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://nursingtampacatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce (sha256 ac4a17206a2e)
- issues: conflicting_sources:https://graduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce,https://undergraduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce
- checks: {"distinct_exams": 27, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|45]:  ⟵ “Art History | 45 | ART 381ART 381, 382”
  - equivalencies[AP-2-D-ART-DESIGN|34-5]:  ⟵ “Studio Art: 2-D Design | 34-5 | ART electiveART 105”
  - equivalencies[AP-3-D-ART-DESIGN|34-5]:  ⟵ “Studio Art: 3-D Design | 34-5 | ART electiveART 110”
  - equivalencies[AP-DRAWING|34-5]:  ⟵ “Studio Art: Drawing | 34-5 | ART ElectiveART 110”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang. & Comp. | 4-5 | ENGL 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Lit. &Comp. | 4-5 | ENGL 102”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “European History | 3-5 | HIST elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4-5]:  ⟵ “Human Geography | 4-5 | GEOG 211”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics | 4-5 | ECON 212”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics | 4-5 | ECON 213”
  - equivalencies[AP-PSYCHOLOGY|4-5]:  ⟵ “Psychology | 4-5 | PYSC 100”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4-5]:  ⟵ “U.S. Gov. & Politics | 4-5 | POLS 100”
  - equivalencies[AP-UNITED-STATES-HISTORY|34-5]:  ⟵ “U.S. History | 34-5 | HIST 131HIST 131, 132”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4-5]:  ⟵ “World History: Modern | 4-5 | HIST 122”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB | 4-5 | MATH 150”
  - equivalencies[AP-CALCULUS-BC|34-5]:  ⟵ “Calculus BC | 34-5 | MATH 150MATH 150, 250”
  - equivalencies[AP-STATISTICS|4-5]:  ⟵ “Statistics | 4-5 | MATH 270”
  - equivalencies[AP-BIOLOGY|34-5]:  ⟵ “Biology* | 34-5 | BIOL 111BIOL 111, 112”
  - equivalencies[AP-CHEMISTRY|34-5]:  ⟵ “Chemistry* | 34-5 | CHEM 111CHEM 111, 112”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science * | 3-5 | ENVS 100”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics I* | 4 | PHYS 211”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics II* | 4 | PHYS 212”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3-5]:  ⟵ “Physics C: Mechanics* | 3-5 | PHYS 211”
  - equivalencies[AP-PRECALCULUS|345]:  ⟵ “Precalculus | 345 | MATH 110MATH 115MATH 120”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|34-5]:  ⟵ “French Lang. & Culture | 34-5 | FREN 111FREN 111, 112”
  - … 2 more rows
### `b2e33199d4031886` Lincoln Memorial University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://graduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce (sha256 94c6ba721b5c)
- issues: conflicting_sources:https://nursingtampacatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce,https://undergraduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce
- checks: {"distinct_exams": 27, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4 5]:  ⟵ “Art History | 4 5 | ART 381 ART 381, 382”
  - equivalencies[AP-MUSIC-THEORY|3 4-5]:  ⟵ “Music Theory | 3 4-5 | MUSC 111 MUSC 111, 112”
  - equivalencies[AP-2-D-ART-DESIGN|3 4-5]:  ⟵ “Studio Art: 2-D Design | 3 4-5 | ART elective ART 105”
  - equivalencies[AP-3-D-ART-DESIGN|3 4-5]:  ⟵ “Studio Art: 3-D Design | 3 4-5 | ART elective ART 110”
  - equivalencies[AP-DRAWING|3 4-5]:  ⟵ “Studio Art: Drawing | 3 4-5 | ART elective ART 110”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang. & Comp. | 4-5 | ENGL 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Lit. & Comp. | 4-5 | ENGL 102”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “European History | 3-5 | HIST elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4-5]:  ⟵ “Human Geography | 4-5 | GEOG 211”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics | 4-5 | ECON 212”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics | 4-5 | ECON 213”
  - equivalencies[AP-PSYCHOLOGY|4-5]:  ⟵ “Psychology | 4-5 | PSYC 100”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4-5]:  ⟵ “U. S. Gov. & Politics | 4-5 | POLS 211”
  - equivalencies[AP-UNITED-STATES-HISTORY|3 4-5]:  ⟵ “U. S. History | 3 4-5 | HIST 131 HIST 131, 132”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3 4-5]:  ⟵ “World History | 3 4-5 | HIST 121 HIST 121, 122”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB | 4-5 | MATH 150”
  - equivalencies[AP-CALCULUS-BC|3 4-5]:  ⟵ “Calculus BC | 3 4-5 | MATH 150 MATH 150, 250”
  - equivalencies[AP-STATISTICS|4-5]:  ⟵ “Statistics | 4-5 | MATH 270”
  - equivalencies[AP-BIOLOGY|3 4-5]:  ⟵ “Biology* | 3 4-5 | BIOL 111 BIOL 111, 112”
  - equivalencies[AP-CHEMISTRY|3 4-5]:  ⟵ “Chemistry* | 3 4-5 | CHEM 111 CHEM 111, 112”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science* | 3-5 | ENVS 100”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics I* | 4 | PHYS 211”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics II | 4 | PHYS 212”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3-5]:  ⟵ “Physics C: Mechanics* | 3-5 | PHYS 211”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 4-5]:  ⟵ “French Lang. & Culture | 3 4-5 | FREN 111 FREN 111, 112”
  - … 2 more rows
### `df2a54aa45737c95` Lincoln Memorial University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://undergraduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce (sha256 c1de449eb2d0)
- issues: conflicting_sources:https://graduatecatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce,https://nursingtampacatalog.lmunet.edu/special-credit-sc-and-credit-by-examination-ce
- checks: {"distinct_exams": 27, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|45]:  ⟵ “Art History | 45 | ART 381ART 381, 382”
  - equivalencies[AP-2-D-ART-DESIGN|34-5]:  ⟵ “Studio Art: 2-D Design | 34-5 | ART electiveART 105”
  - equivalencies[AP-3-D-ART-DESIGN|34-5]:  ⟵ “Studio Art: 3-D Design | 34-5 | ART electiveART 110”
  - equivalencies[AP-DRAWING|34-5]:  ⟵ “Studio Art: Drawing | 34-5 | ART ElectiveART 110”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang. & Comp. | 4-5 | ENGL 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Lit. &Comp. | 4-5 | ENGL 102”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “European History | 3-5 | HIST elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4-5]:  ⟵ “Human Geography | 4-5 | GEOG 211”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics | 4-5 | ECON 212”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics | 4-5 | ECON 213”
  - equivalencies[AP-PSYCHOLOGY|4-5]:  ⟵ “Psychology | 4-5 | PYSC 100”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4-5]:  ⟵ “U.S. Gov. & Politics | 4-5 | POLS 100”
  - equivalencies[AP-UNITED-STATES-HISTORY|34-5]:  ⟵ “U.S. History | 34-5 | HIST 131HIST 131, 132”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4-5]:  ⟵ “World History: Modern | 4-5 | HIST 122”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB | 4-5 | MATH 150”
  - equivalencies[AP-CALCULUS-BC|34-5]:  ⟵ “Calculus BC | 34-5 | MATH 150MATH 150, 250”
  - equivalencies[AP-STATISTICS|4-5]:  ⟵ “Statistics | 4-5 | MATH 270”
  - equivalencies[AP-BIOLOGY|34-5]:  ⟵ “Biology* | 34-5 | BIOL 111BIOL 111, 112”
  - equivalencies[AP-CHEMISTRY|34-5]:  ⟵ “Chemistry* | 34-5 | CHEM 111CHEM 111, 112”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science * | 3-5 | ENVS 100”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics I* | 4 | PHYS 211”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics II* | 4 | PHYS 212”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3-5]:  ⟵ “Physics C: Mechanics* | 3-5 | PHYS 211”
  - equivalencies[AP-PRECALCULUS|345]:  ⟵ “Precalculus | 345 | MATH 110MATH 115MATH 120”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|34-5]:  ⟵ “French Lang. & Culture | 34-5 | FREN 111FREN 111, 112”
  - … 2 more rows
### `254f88e373d0da2e` Lipscomb University — appeals 2026-27 [new] (source_unlabeled)
- source: https://lipscomb.edu/admissions/cost-financial-aid/resources/satisfactory-academic-progress (sha256 3796312e350e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “All probations may be appealed in writing by completing a Satisfactory Academic Progress Appeal Form.”
### `d188edb892dad8fa` Lipscomb University — appeals 2026-27 [new] (source_unlabeled)
- source: https://lipscomb.edu/admissions/cost-financial-aid/resources/satisfactory-academic-progress (sha256 3796312e350e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “All appeals must include documentation of any unusual circumstance that contributed to the probation.”
### `560881171654f5ee` Lipscomb University — costs 2025-26 · residency=not_applicable [same] (labeled_in_source)
- source: https://lipscomb.edu/admission/tuition-and-financial-aid/cost-attendance (sha256 4fe1468ec981)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition & Fees: 42596 ⟵ “Tuition & Fees | $42,596 | $42,596 | $42,596”
  - on_campus:Housing: 11044 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - on_campus:Food: 6700 ⟵ “Food | $6,700** | $3,004 | $2,000”
  - on_campus:Books & Supplies: 1750 ⟵ “Books & Supplies | $1,750 | $1,750 | $1,750”
  - on_campus:Personal Expenses: 2460 ⟵ “Personal Expenses | $2,460 | $2,460 | $2,460”
  - on_campus:Transportation: 2250 ⟵ “Transportation | $2,250 | $2,250 | $2,250”
  - on_campus:Loan Fee (If Accepting): 48 ⟵ “Loan Fee (If Accepting) | 48 | 48 | 48”
  - on_campus:Total: 66848 ⟵ “Total | $66,848 | $65,348 | $55,604”
  - off_campus_not_with_family:Tuition & Fees: 42596 ⟵ “Tuition & Fees | $42,596 | $42,596 | $42,596”
  - off_campus_not_with_family:Housing: 13240 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - off_campus_not_with_family:Food: 3004 ⟵ “Food | $6,700** | $3,004 | $2,000”
  - off_campus_not_with_family:Books & Supplies: 1750 ⟵ “Books & Supplies | $1,750 | $1,750 | $1,750”
  - off_campus_not_with_family:Personal Expenses: 2460 ⟵ “Personal Expenses | $2,460 | $2,460 | $2,460”
  - off_campus_not_with_family:Transportation: 2250 ⟵ “Transportation | $2,250 | $2,250 | $2,250”
  - off_campus_not_with_family:Loan Fee (If Accepting): 48 ⟵ “Loan Fee (If Accepting) | 48 | 48 | 48”
  - off_campus_not_with_family:Total: 65348 ⟵ “Total | $66,848 | $65,348 | $55,604”
  - with_parents_or_family:Tuition & Fees: 42596 ⟵ “Tuition & Fees | $42,596 | $42,596 | $42,596”
  - with_parents_or_family:Housing: 4500 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - with_parents_or_family:Food: 2000 ⟵ “Food | $6,700** | $3,004 | $2,000”
  - with_parents_or_family:Books & Supplies: 1750 ⟵ “Books & Supplies | $1,750 | $1,750 | $1,750”
  - with_parents_or_family:Personal Expenses: 2460 ⟵ “Personal Expenses | $2,460 | $2,460 | $2,460”
  - with_parents_or_family:Transportation: 2250 ⟵ “Transportation | $2,250 | $2,250 | $2,250”
  - with_parents_or_family:Loan Fee (If Accepting): 48 ⟵ “Loan Fee (If Accepting) | 48 | 48 | 48”
  - with_parents_or_family:Total: 55604 ⟵ “Total | $66,848 | $65,348 | $55,604”
### `9d2f53eb5672f1d8` Lipscomb University — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://lipscomb.edu/admissions/non-traditional-admissions/dual-enrollment (sha256 fef48ba21bfc)
- issues: stale_year_label:2025-26, state_grant_mixed_statements
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - state_grant_accepted: True ⟵ “To correctly complete the application, students MUST select Lipscomb University as the “institution granting credit”—not the school they plan to attend once they graduate high school. If applicants fill out and submit the grant application incorrectly, they will NOT receive any grant funding. Studen”
  - eligibility_tier: 2.0 ⟵ “For the 2025-2026 school year, this grant pays $200.55 per credit hour toward classes one through five. It then pays $100 per credit hour for courses 6 through 10. A minimum GPA of 2.0 is necessary to keep the TN Dual Enrollment Grant.”
  - per_credit_hour_charge: 200.55 ⟵ “For the 2025-2026 school year, this grant pays $200.55 per credit hour toward classes one through five. It then pays $100 per credit hour for courses 6 through 10. A minimum GPA of 2.0 is necessary to keep the TN Dual Enrollment Grant.”
  - per_credit_hour_charge: 100 ⟵ “For the 2025-2026 school year, this grant pays $200.55 per credit hour toward classes one through five. It then pays $100 per credit hour for courses 6 through 10. A minimum GPA of 2.0 is necessary to keep the TN Dual Enrollment Grant.”
  - state_grant_accepted: True ⟵ “To be eligible for the dual enrollment grant, students must complete the following steps during the application process:”
  - state_grant_accepted: False ⟵ “Students must also maintain a university 2.75 GPA to continue to be eligible for the dual enrollment grant. Students who are not eligible to receive the grant money are responsible for payment in full of all charges incurred by participation in the dual enrollment program.”
### `m93e8edd11915823` Lipscomb University — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://lipscomb.edu/admission/transfer-admission/transferring-credit (sha256 a7ffd3af7b5c)
- issues: conflicting_values:max_transfer_credits
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “At Lipscomb, we generally accept courses for transfer if they were earned at a regionally accredited college or university with a grade of “C” or higher.”
  - min_grade: C ⟵ “Check Your Credits We generally accept courses for transfer if they were earned at a regionally accredited college or university with a grade of “C” or higher.”
  - min_grade: C ⟵ “Check Your Credits We generally accept courses for transfer if they were earned at a regionally accredited college or university with a grade of “C” or higher.”
### `a0ff5058898528da` Maryville College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/professional-judgment/ (sha256 50f469fde879)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “The outline below indicates circumstances where a PJ may be warranted: Special Circumstances: extenuating circumstances (i.e., job loss) leading to changes in your family’s financial situation that are not reflected accurately or occurred after the submission of your current year FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances: a student’s dependency status is based on a unique situation (e.g., parental abandonment, abuse, or incarceration) where there is no parental involvement.”
### `bb644a01765eedf3` Maryville College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/professional-judgment/ (sha256 50f469fde879)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The Financial Aid Office will accept, and review all submitted Professional Judgment (PJ) requests from students and/or families.”
### `c529b10f0a1b7aa9` Maryville College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/professional-judgment/ (sha256 50f469fde879)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “This is more commonly referred to as a dependency override.”
  - sentence: dependency_override ⟵ “Self-supporting students without a documented extenuating family circumstance do not qualify for a dependency override.”
### `0e65afa59bfc016b` Middle Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mtsu.edu/financial-aid/appeals/ (sha256 a7a69df62029)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals NOTE: Students should also be aware of the difference between a financial aid suspension based on the Financial Aid Satisfactory Academic Progress Policy and an academic suspension which is based solely on grades and GPA (refer to the Academic Standing policies in the Undergraduate & Graduate Catalogs).”
  - sentence: sap_appeal ⟵ “MTSU Financial Aid Satisfactory Academic Progress Appeal Form located on the forms page.”
  - sentence: sap_appeal ⟵ “An academic appeal, if approved, will allow you to enroll in classes for the affected semester; a scholarship or SAP appeal, if approved, will allow you to receive your related aid for the affected semester.”
### `0fe408ad0c0766dc` Middle Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mtsu.edu/financial-aid/appeals/ (sha256 a7a69df62029)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: scholarship_retention_appeal ⟵ “Institutional Scholarship Appeal Form found on our forms page.”
  - sentence: scholarship_retention_appeal ⟵ “Once you have gotten your GPA back up to the required level, then you will need to submit a new Institutional Scholarship Appeal Form, and check the box that indicates you are now meeting the GPA requirement.”
  - sentence: scholarship_retention_appeal ⟵ “If this is applicable, please submit the Institutional Scholarship Appeal Form along with a written statement explaining why unable to enroll full-time in CPoS eligible classes.”
  - sentence: scholarship_retention_appeal ⟵ “Tennessee Education Lottery Scholarship (TELS) Appeal Process The Tennessee Education Lottery Scholarship (TELS) is awarded based on policies set forth by the Tennessee Student Assistance Corporation (TSAC).”
  - sentence: scholarship_retention_appeal ⟵ “TSAC’s TELS policy allows an appeal process for students who fail to meet enrollment requirements due to extenuating medical or personal circumstances.”
  - sentence: scholarship_retention_appeal ⟵ “Appealing the cancellation of the TELS/Lottery Scholarship If you lost TELS eligibility while attending another institution or 1 of the items listed under ‘Who cannot submit an appeal to the MTSU TELS Institutional Review Panel (IRP)’ heading applies to yourself, then you must appeal directly to the Tennessee Student Assistance Corporation (TSAC).”
### `18c356ad0d35a50c` Middle Tennessee State University — credit_policies 2010-11 · policy_kind=IB [new] (labeled_in_source)
- source: https://www.mtsu.edu/how-to-apply/credit-by-examination/ (sha256 83df4bc5b3f6)
- issues: stale_year_label:2010-11
- checks: {"distinct_exams": 15, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5 or higher]:  ⟵ “Biology (higher level) | 5 or higher | BIOL 1110/ BIOL 1111 and BIOL 1120/BIOL 1121 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5 or higher (SL)4 or higher (HL)]:  ⟵ “Business and Management (standard or higher level) | 5 or higher (SL)4 or higher (HL) | BCED 1400 | 3”
  - equivalencies[IB-CHEMISTRY|5 or higher]:  ⟵ “Chemistry (higher level) | 5 or higher | CHEM 1110/1111 and 1120/1121 | 8”
  - equivalencies[IB-CHEMISTRY|5 or higher]:  ⟵ “Chemistry (standard level) | 5 or higher | CHEM 1110/1111 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|6 or higher (SL)5 or higher (HL)]:  ⟵ “Computer Science (standard or higher level) | 6 or higher (SL)5 or higher (HL) | CSCI 1170 | 4”
  - equivalencies[IB-ECONOMICS|5 or higher (SL)5 or higher (HL)]:  ⟵ “Economics (standard or higher level) | 5 or higher (SL)5 or higher (HL) | ECON 2410ECON 2410 and 2420 | 36”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4 or higher]:  ⟵ “Environmental Systems or Societies (standard or higher level) | 4 or higher | ENVS 2810/ENVS 2811 | 4”
  - equivalencies[IB-GEOGRAPHY|5 or higher (SL)4 or higher (HL)]:  ⟵ “Geography (standard or higher level) | 5 or higher (SL)4 or higher (HL) | GEOG 2000 | 3”
  - equivalencies[IB-HISTORY|5 or higher]:  ⟵ “History (higher level) | 5 or higher | HIST 1120 and depending on higher level option (Paper #3)Europe: HIST 1020; Americas: either HIST 2010 or 2020 to be determined at orientation/advising; Africa and the Middle East or Asia and Ocean – 3 hours lower-division history credit | 6”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4 or higher]:  ⟵ “Mathematics: Analysis & Approaches (standard level) | 4 or higher | MATH 1730 | 4”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4 or higher]:  ⟵ “Mathematics: Analysis & Approaches (higher level) | 4 or higher | MATH 1910 | 4”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|4 or higher]:  ⟵ “Mathematics: Applications & Interpretation (standard or higher level) | 4 or higher | MATH 1530 (student may request MATH 1730 instead) | 3 (4)”
  - equivalencies[IB-PHILOSOPHY|5 or higher]:  ⟵ “Philosophy (standard level) | 5 or higher | 3 hours lower-division philosophy credit | 3”
  - equivalencies[IB-PHILOSOPHY|5 or higher]:  ⟵ “Philosophy (higher level) | 5 or higher | PHIL 1030 | 3”
  - equivalencies[IB-PHYSICS|5 or higher]:  ⟵ “Physics (standard or higher level) | 5 or higher | PHYS 2010/PHYS 2011 | 4”
  - equivalencies[IB-PHYSICS|6 or higher]:  ⟵ “Physics (standard or higher level) | 6 or higher | PHYS 2010/PHYS 2011 and PHYS 2020/PHYS 2021 | 8”
  - equivalencies[IB-PSYCHOLOGY|4 or higher]:  ⟵ “Psychology (higher level) | 4 or higher | 3 hours lower-division psychology credit | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4 or higher]:  ⟵ “Social and Cultural Anthropology (standard level) | 4 or higher | ANTH 2010 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4 or higher]:  ⟵ “Social and Cultural Anthropology (higher level) | 4 or higher | ANTH 2010 plus 3 hours ANTH lower division elective | 6”
  - equivalencies[IB-THEATRE|5 or higher]:  ⟵ “Theatre (standard or higher level) | 5 or higher | THEA 1030 | 3”
### `ac11364f1eddc7f6` Middle Tennessee State University — credit_policies 2010-11 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://www.mtsu.edu/how-to-apply/credit-by-examination/ (sha256 83df4bc5b3f6)
- issues: stale_year_label:2010-11
- checks: {"distinct_exams": 19, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50 or greater]:  ⟵ “American Government | 50 or greater | PS 1005 | 3”
  - equivalencies[CLEP-BIOLOGY|50 or greater]:  ⟵ “Biology | 50 or greater | BIOL 1030/1031 | 4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50 or greater]:  ⟵ “Business Law, Introductory | 50 or greater | BLAW 3430 | 3”
  - equivalencies[CLEP-CALCULUS|50 or greater]:  ⟵ “Calculus | 50 or greater | MATH 1910 | 4”
  - equivalencies[CLEP-CHEMISTRY|50 or greater]:  ⟵ “Chemistry | 50 or greater | CHEM 1110/CHEM 1111, CHEM 1120/CHEM 1121 | 8”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50 or greater]:  ⟵ “College Algebra | 50 or greater | MATH 1710 | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50 or greater]:  ⟵ “College Mathematics | 50 or greater | MATH 1010 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50 or greater]:  ⟵ “Financial Accounting | 50 or greater | ACTG 2110 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50 or greater]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 or greater | HIST 2010 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50 or greater]:  ⟵ “History of the United States II: 1865 to Present | 50 or greater | HIST 2020 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50 or greater]:  ⟵ “Macroeconomics, Principles of | 50 or greater | ECON 2410 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50 or greater]:  ⟵ “Management, Principles of | 50 or greater | MGMT 3610 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50 or greater]:  ⟵ “Marketing, Principles of | 50 or greater | MKT 3820 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50 or greater]:  ⟵ “Microeconomics, Principles of | 50 or greater | ECON 2420 | 3”
  - equivalencies[CLEP-PRECALCULUS|50 or greater]:  ⟵ “Precalculus | 50 or greater | MATH 1730 | 4”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50 or greater]:  ⟵ “Psychology, Introductory | 50 or greater | PSY 1410 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50 or greater]:  ⟵ “Sociology, Introductory | 50 or greater | SOC 1010 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50 or greater]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 or greater | HIST 1010 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50 or greater]:  ⟵ “Western Civilization II: 1648 to Present | 50 or greater | HIST 1020 | 3”
### `eebfe8746855d458` Middle Tennessee State University — credit_policies 2010-11 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.mtsu.edu/how-to-apply/credit-by-examination/ (sha256 83df4bc5b3f6)
- issues: stale_year_label:2010-11
- checks: {"distinct_exams": 32, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3 or above]:  ⟵ “African American Studies | 3 or above | HIST 2040, HIST 2050 | 6”
  - equivalencies[AP-ART-HISTORY|3 or above]:  ⟵ “Art History | 3 or above | ART 1030 | 3”
  - equivalencies[AP-BIOLOGY|3 or above]:  ⟵ “Biology | 3 or above | BIOL1030/ BIOL 1031 (Science major may receive credit for BIOL 1110/BIOL 1111, BIOL 1120/BIOL 1121 upon recommendation of chair, Department of Biology.) | 4”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3 or above]:  ⟵ “Business with Personal Finance | 3 or above | FCSE 1400 | 3”
  - equivalencies[AP-CALCULUS-AB|3 or above]:  ⟵ “Calculus AB | 3 or above | MATH 1910 | 4”
  - equivalencies[AP-CALCULUS-BC|3 or above]:  ⟵ “Calculus BC | 3 or above | Math 1920 | 4”
  - equivalencies[AP-CHEMISTRY|3 or 45]:  ⟵ “Chemistry | 3 or 45 | CHEM 1110/ CHEM 1111 OR CHEM 1010/ CHEM 1011CHEM 1110/ CHEM 1111, CHEM 1120/ CHEM 1121 | 4 8”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3 or above]:  ⟵ “Comparative Government and Politics | 3 or above | PS 1010 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3 or above]:  ⟵ “Computer Science A | 3 or above | CSCI 1170 | 4”
  - equivalencies[AP-CYBERSECURITY|3 or above]:  ⟵ “Cybersecurity | 3 or above | CYBM 1300 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 or above]:  ⟵ “English Language and Composition | 3 or above | ENGL 1010 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3 or above]:  ⟵ “English Literature and Composition | 3 or above | ENGL1010 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3 or above]:  ⟵ “Environmental Science | 3 or above | ENVS 2810/ENVS 2811 | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|3 or above]:  ⟵ “European History | 3 or above | HIST 1020 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3 or above]:  ⟵ “Human Geography | 3 or above | GS 2010 | 3”
  - equivalencies[AP-MACROECONOMICS|3 or above]:  ⟵ “Macroeconomics | 3 or above | ECON 2410 | 3”
  - equivalencies[AP-MICROECONOMICS|3 or above]:  ⟵ “Microeconomics | 3 or above | ECON 2420 | 3”
  - equivalencies[AP-MUSIC-THEORY|3 or above]:  ⟵ “Music Theory | 3 or above | MUTH 1000 | 3”
  - equivalencies[AP-PHYSICS-1|4 or above]:  ⟵ “Physics 1 | 4 or above | PHYS 2010/2011* | 4”
  - equivalencies[AP-PHYSICS-2|4 or above]:  ⟵ “Physics 2 | 4 or above | PHYS 2020/2021* | 4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4 or above]:  ⟵ “Physics C: Electricity & Magnetism | 4 or above | PHYS 2120/2121* | 4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4 or above]:  ⟵ “Physics C: Mechanics | 4 or above | PHYS 2110/2111* | 4”
  - equivalencies[AP-PRECALCULUS|3 or above]:  ⟵ “Precalculus | 3 or above | MATH 1730 | 4”
  - equivalencies[AP-PSYCHOLOGY|3 or above]:  ⟵ “Psychology | 3 or above | PSY 1410 | 3”
  - equivalencies[AP-SEMINAR|3 or above]:  ⟵ “Seminar | 3 or above | CLA 2000 | 3”
  - … 7 more rows
### `184a27a6f6104abe` Nashville State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/documents/financial-aid/sap-infographic.pdf (sha256 3a3adf26aca8)
- issues: semantic_review_required, conflicting_sources:https://www.nscc.edu/documents/financial-aid/sap-policy.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Click on Financial Aid on Student Requirements HOW DO I GET A SAP WHAT DO I NEED TO APPEAL PACKET AND INCLUDE IN MY APPEAL?”
  - sentence: sap_appeal ⟵ “You cannot file an *Make sure to explain how circumstances have SAP Appeal until all of your final changed and/or what steps you have taken to grades have been posted. alleviate any obstacles.”
### `be91abfaa97c1a22` Nashville State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/documents/financial-aid/sap-policy.pdf (sha256 b480d6a744ea)
- issues: semantic_review_required, conflicting_sources:https://www.nscc.edu/documents/financial-aid/sap-infographic.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Complete and submit a Satisfactory Academic Progress Appeal Form.”
  - sentence: sap_appeal ⟵ “Financial Aid Probation Approved status is assigned to a student who fails to meet satisfactory academic progress guidelines, submitted an appeal, and the appeal was approved.”
### `9f74514996deb3b4` Nashville State Community College — credit_policies 2023-24 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.nscc.edu/admissions/dual-enrollment.php (sha256 77c883f2d47e)
- issues: stale_year_label:2023-24
- checks: {"fields": ["state_grant_accepted"], "tiers": 2}
  - eligibility_tier: 2.8 ⟵ “If a DE student has an unweighted cumulative HS GPA of 2.8-3.59, and also a B or higher”
  - eligibility_tier: 3.6 ⟵ “GPA of 3.60 or higher will be able to have prerequisites waived for courses that require”
  - state_grant_accepted: True ⟵ “To be eligible to receive a Dual Enrollment scholarship grant you must provide proof”
### `mc1f1d11a55f5b89` Nashville State Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/admissions/how-to-apply/transfer-students.php (sha256 4c5398a6ebac)
- issues: conflicting_sources:min_grade, conflicting_values:residency_requirement_credits
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “South College Transfer Credit Undergraduate – Credit for transfer work may be given if it was taken at an accredited collegiate institution, if it is equivalent to courses offered at South College, and if it carries a grade of C or better.”
  - min_grade: D ⟵ “Step 5: Take Placement Assessment Transfer applicants with college-level English and Math with a grade of “D” or better will be exempt from the placement assessment.”
### `053f5eace98a7a2c` Northeast State Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-forms.html (sha256 8dc08c660399)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal - Satisfactory Academic Progress This form must be completed when the Financial Aid Office has notified a student that he/she is currently or was previously placed on financial aid removal.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Standards Policy Satisfactory Academic Progress (SAP) Appeal Form Request for Degree Works Audit for SAP Read the Satisfactory Academic Progress Standards Policy.”
  - sentence: sap_appeal ⟵ “If the appeal is approved, a student must sign the Satisfactory Academic Progress 'Plan' and must adhere to the agreed upon terms of the 'Plan'.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeals Committee will review and rule on a complete submitted appeal.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeals Committee may request additional documentation for an appeal and the documents must be submitted before the committee can rule on an appeal.”
  - sentence: sap_appeal ⟵ “HOPE One Time Repeat/Regain Appeal HOPE Enrollment Status Appeal TN Promise Enrollment Status Appeal TN Reconnect Enrollment Status Appeal Financial Aid Plan for Satisfactory Academic Progress Financial Aid Plan for Satisfactory Academic Progress Change of Income Appeals It is the policy of the Northeast State Financial Aid Office to consider change of income requests related to unexpected events ”
### `361923da1baec848` Northeast State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.northeaststate.edu/financial-aid-tuition/policies/financial-aid-standards.html (sha256 f3983b2de692)
- issues: semantic_review_required, conflicting_sources:https://www.northeaststate.edu/financial-aid-tuition/maintaining-eligibility.html
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Turn in the degree audit at the same time as the SAP Appeal form.”
  - sentence: sap_appeal ⟵ “Appeals will be considered for the following reasons: Serious injury or illness of the student Death, serious illness, or injury of immediate family member (mother, father, sibling, spouse, child) Family trauma which occurred during the semester in question Change in work schedule or responsibilities Change in household or marital status Other extenuating circumstances (must be documented) Process”
  - sentence: sap_appeal ⟵ “FINANCIAL AID PLAN and DENIAL Plan – Students will be placed on the Financial Aid Plan if their SAP appeal is approved.”
  - sentence: sap_appeal ⟵ “Denial – A student will be placed on Financial Aid Denial if their SAP appeal is denied by the SAP Committee.”
### `3e07ae78c75c6071` Northeast State Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-appeals.html (sha256 fd007050b235)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Students classified as Dependent on the FAFSA who are unable to provide parent information may request a review of their dependency status based on adverse family circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Students who wish to have their dependency status reviewed should contact the Financial Aid Office to discuss an Unusual Circumstance Appeal.”
### `3f721f8002437d09` Northeast State Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-forms.html (sha256 8dc08c660399)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Northeast State Online General Scholarship Application HOPE, TN Promise, & TN Reconnect Appeals This form must be completed prior to the following requests.”
### `5422f79b8b63dfe9` Northeast State Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-appeals.html (sha256 fd007050b235)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress View our Satisfactory Academic Progress page for information on SAP appeals and standards.”
### `722434bad602e3f9` Northeast State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.northeaststate.edu/financial-aid-tuition/renewal-requirements.html (sha256 53a58b826e95)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Learn HOPE information on exceptions, appeals and more.”
### `7f5f70608924741a` Northeast State Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-appeals.html (sha256 fd007050b235)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Appeals are approved or denied based upon the professional judgment of financial aid staff and various appeal committees.”
### `d465ebb6a40ff836` Northeast State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.northeaststate.edu/financial-aid-tuition/maintaining-eligibility.html (sha256 971161c3d178)
- issues: semantic_review_required, conflicting_sources:https://www.northeaststate.edu/financial-aid-tuition/policies/financial-aid-standards.html
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Students who graduate with any credential will be required to provide a SAP appeal with a degree audit as well.”
  - sentence: sap_appeal ⟵ “Turn in the degree audit at the same time as the SAP Appeal form.”
  - sentence: sap_appeal ⟵ “Appeals will be considered for the following reasons: Serious injury or illness of the student Death, serious illness, or injury of an immediate family member (mother, father, sibling, spouse, child) Family trauma which occurred during the semester in question Change in work schedule or responsibilities Change in household or marital status Other extenuating circumstances (must be documented) Proc”
  - sentence: sap_appeal ⟵ “FINANCIAL AID PLAN and DENIAL Plan – Students will be placed on the Financial Aid Plan if their SAP appeal is approved.”
  - sentence: sap_appeal ⟵ “Denial – A student will be placed on Financial Aid Denial if their SAP appeal is denied or if the student failed to meet the requirements of the Financial Aid Plan.”
### `e4e9699330324131` Rhodes College — admissions_metrics 2024-25 [same] (labeled_in_source)
- source: https://www.rhodes.edu/sites/default/files/2026-02/CDS_2024-2025%20_Rhodes_College_.pdf (sha256 1e6d625b330b)
- issues: stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 6365 ⟵ “Total first-time, first-year (degree-seeking) who applied          1103       2872            2390           0     6365”
  - admits: 3205 ⟵ “Total first-time, first-year (degree-seeking) who were admitted     708         2160          337            0     3205”
  - enrolled: 388 ⟵ “Total first-time, first-year (degree-seeking) enrolled              126         216            46            0      388”
  - sat_composite_25..75: [1352, 1420, 1478] ⟵ “SAT Composite                     1352                      1420                       1478”
  - sat_math_25..75: [670, 720, 740] ⟵ “SAT Math                           670                       720                       740”
  - act_25..75: [28, 31, 32] ⟵ “ACT Composite                      28                        31                         32”
### `388bf69f380e9a68` Rhodes College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/rhodes-institutional-aid (sha256 9a95f432930b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Exceptions to this are within the purview of the Financial Aid Office in response to extreme increases in demonstrated financial need documented through the completion of the Special Circumstance Request and other supporting documents that may be required.”
### `9bb9f34e2714a8da` Rhodes College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/faq (sha256 fdedb1e7cc08)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Yes, if your family has experienced a change in financial circumstances (such as loss of employment, separation or divorce, or death of a parent) that is not adequately reflected on your FAFSA application, you may complete our Change of Financial Circumstances Form.”
  - sentence: need_based_special_circumstances ⟵ “In an effort to determine the need of our families and to best distribute any available awards we are asking families to complete the attached Special Circumstance Form.”
  - sentence: need_based_special_circumstances ⟵ “What can I do if I have unusual circumstances that prevent me from reporting parent information on my FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “Students with unusual circumstances (such as parental abandonment, abuse, or incarceration) are encouraged to reach out to the Office of Student Financial Aid to explain their situation and provide supporting documentation.”
### `e5ebe3b59e74f90c` Rhodes College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/faq (sha256 fdedb1e7cc08)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Our committee will review each situation on a case-by-case basis to determine if a dependency override can be granted.”
### `3c91fb0c9e68cf13` Rhodes College — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://catalog.rhodes.edu/book/export/html/72 (sha256 a1e7393fe133)
- issues: conflicting_sources:https://catalog.rhodes.edu/general-information/expenses,https://www.rhodes.edu/admission-aid/cost-affordability/tuition-fees
- checks: {"columns": 1, "rows": 5}
  - column:Tuition (Full Time): 60240.0 ⟵ “Tuition (Full Time) | 30,120.00 | 60,240.00”
  - column:Activity Fee: 320.0 ⟵ “Activity Fee | 160.00 | 320.00”
  - column:Health & Wellness Fee: 500.0 ⟵ “Health & Wellness Fee | 250.00 | 500.00”
  - column:Tuition Refund Plan Coverage (Resident): 435.0 ⟵ “Tuition Refund Plan Coverage (Resident) |  | 435.00”
  - column:Tuition Refund Plan Coverage (Commuter): 348.0 ⟵ “Tuition Refund Plan Coverage (Commuter) |  | 348.00”
### `6802b23c61c9e09f` Rhodes College — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://catalog.rhodes.edu/general-information/expenses (sha256 d9d73e75048d)
- issues: conflicting_sources:https://catalog.rhodes.edu/book/export/html/72,https://www.rhodes.edu/admission-aid/cost-affordability/tuition-fees
- checks: {"columns": 1, "rows": 5}
  - column:Tuition (Full Time): 60240.0 ⟵ “Tuition (Full Time) | 30,120.00 | 60,240.00”
  - column:Activity Fee: 320.0 ⟵ “Activity Fee | 160.00 | 320.00”
  - column:Health & Wellness Fee: 500.0 ⟵ “Health & Wellness Fee | 250.00 | 500.00”
  - column:Tuition Refund Plan Coverage (Resident): 435.0 ⟵ “Tuition Refund Plan Coverage (Resident) |  | 435.00”
  - column:Tuition Refund Plan Coverage (Commuter): 348.0 ⟵ “Tuition Refund Plan Coverage (Commuter) |  | 348.00”
### `a8e4516e86bbe2b5` Rhodes College — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/tuition-fees (sha256 13cfdc4a9137)
- issues: conflicting_sources:https://catalog.rhodes.edu/book/export/html/72,https://catalog.rhodes.edu/general-information/expenses
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 60240 ⟵ “Tuition | $60,240”
  - column:Mandatory Fees: 820 ⟵ “Mandatory Fees | $820”
  - column:Housing & Food (Unlimited, All-Access Meal Plan)*: 15196 ⟵ “Housing & Food (Unlimited, All-Access Meal Plan)* | $15,196”
  - column:Total: 76256 ⟵ “Total | $76,256”
### `028aab420531bda3` Roane State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.roanestate.edu/?8056-Dependency-Status-Appeal (sha256 92597758998f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “Requesting a Dependency Status Appeal To request independent status, you must complete the Dependency Status Appeal form via RaiderNet.”
  - sentence: dependency_override ⟵ “After you have submitted the form, please check 'Your Alerts' to see what documents are needed to complete your Dependency Status Appeal.”
  - sentence: dependency_override ⟵ “Renewing a Dependency Status Appeal To renew a previous Dependency Status Appeal, complete the Dependency Status Appeal form in your RaiderNet account, and submit the documents requested.”
  - sentence: dependency_override ⟵ “Students seeking to renew a Dependency Status Appeal, must provide a letter explaining their current living situation and describing any changes since the previous year.”
### `327fc1deb86abb7a` Roane State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.roanestate.edu/?8056-Dependency-Status-Appeal (sha256 92597758998f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “However, if there are severe family problems, which constitute special circumstances, you may appeal this federal law.”
### `84b3aeea63b3e91d` Roane State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.roanestate.edu/?6662-Satisfactory-Academic-Progress-SAP (sha256 505f45c18834)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If it is determined that it is mathematically impossible for a student to regain good standing (2.0 GPA and passing 67% of all attempted hours that apply to your program of study) upon graduation, the SAP appeal will be denied.”
  - sentence: sap_appeal ⟵ “Appeals If there were circumstances beyond a student's control OUTSIDE the classroom that caused failure to meet SAP, they may appeal.”
  - sentence: sap_appeal ⟵ “Examples of circumstances beyond a student's control are: Loss or change of job Serious illness of self or an immediate family member Death of an immediate family member Military Car problems Family Issues (Divorce, Separation, Childcare, etc) To appeal, the student will complete the SAP Appeal form in RaiderNet, submit documentation that supports the outstanding circumstances that were experience”
  - sentence: sap_appeal ⟵ “Please be advised that if a student has been approved for a Satisfactory Academic Progress Appeal (SAP) and does a total withdrawal, officially or unofficially, the appeal is voided and the student must REAPPEAL.”
### `17cc1a5c67347b1f` Southern Adventist University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Dropping below full-time status or withdrawing after the census date can result in immediate loss of the scholarship, repayment of funds, and loss of future eligibility, unless an appeal for exceptional circumstances is approved.”
### `60f11093dba13702` Southern Adventist University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/tuition.html (sha256 cc56cec75708)
- issues: ambiguous_year_labels, arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 5}
  - on_campus:Undergraduate Tuition (12-16 hours): 28900 ⟵ “Undergraduate Tuition (12-16 hours) | $28,900 | $28,900”
  - on_campus:General Fee: 1500 ⟵ “General Fee | $1,500 | $1,500”
  - on_campus:Residence Hall Rent: 6000 ⟵ “Residence Hall Rent | $6,000 | --”
  - on_campus:Estimated Food Allowance*: 3900 ⟵ “Estimated Food Allowance* | $3,900 | --”
  - on_campus:Total: 40300 ⟵ “Total | $40,300 | $30,400”
  - column:Undergraduate Tuition (12-16 hours): 28900 ⟵ “Undergraduate Tuition (12-16 hours) | $28,900 | $28,900”
  - column:General Fee: 1500 ⟵ “General Fee | $1,500 | $1,500”
  - column:Total: 30400 ⟵ “Total | $40,300 | $30,400”
### `19ee0164d36a2527` Southwest Tennessee Community College — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.southwest.tn.edu/dual-enrollment/docs/dual-enrollment-handbook.pdf (sha256 42b394fe4a24)
- issues: stale_year_label:2024-25
- checks: {"fields": ["per_credit_hour_charges", "state_grant_accepted"], "tiers": 0}
  - state_grant_accepted: True ⟵ “The lottery based dual enrollment grant can be used for all dual enrollment programs if the”
  - state_grant_accepted: True ⟵ “student is eligible. The dual enrollment grant is funded through the state lottery and is available”
  - state_grant_accepted: True ⟵ “•   To be eligible for a Dual Enrollment Grant for any semester beyond the first semester of”
  - per_credit_hour_charge: 100 ⟵ “Courses 6-10                   Up to $100 per credit hour”
  - per_credit_hour_charge: 100 ⟵ “The grant covers the first five classes taken and pays up to $100 per credit hour for”
  - state_grant_accepted: True ⟵ “Have students apply for the Dual Enrollment Grant Online. Ensure that students direct their grant to Southwest”
  - state_grant_accepted: True ⟵ “The lottery based dual enrollment grant can be used for all dual enrollment programs if the”
  - state_grant_accepted: True ⟵ “The dual enrollment grant is funded through the state lottery and is available to apply”
### `20dace0481afe0a3` Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tnstate.edu/admissions/financial-aid/admissions-admissions-satprog/ (sha256 109551586805)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Such circumstances might include the death of a relative, an injury to or illness of the student, or other special circumstances.”
### `2e4e361ec826272d` Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tnstate.edu/admissions/financial-aid/financial-aid-forms/ (sha256 cb2428432e82)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “NOTE: requesting a budget increase DOES NOT mean that there are additional funds available.”
### `d15a96d526f39e19` Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tnstate.edu/admissions/financial-aid/financial-aid-forms/ (sha256 cb2428432e82)
- issues: semantic_review_required, conflicting_sources:https://www.tnstate.edu/admissions/financial-aid/admissions-admissions-satprog/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Learn More Satisfactory Academic Progress Appeal (SAP) If your satisfactory academic progress was not meeting institutional requirements at the last measurement, you must file an appeal in myTSU by the published deadline.”
### `f708e2eaf0d70780` Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tnstate.edu/admissions/financial-aid/admissions-admissions-satprog/ (sha256 109551586805)
- issues: semantic_review_required, conflicting_sources:https://www.tnstate.edu/admissions/financial-aid/financial-aid-forms/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “IMPORTANT INFORMATION RELATING TO COVID-19 and SAP: Circumstances related to an outbreak of COVID-19, including, but not limited to, the illness of a student or family member, compliance with a quarantine period, or a general disruption from such an outbreak may form the basis of a student’s SAP appeal.”
  - sentence: sap_appeal ⟵ “Refer to the TSU website regarding procedures for submitting an SAP Appeal for GPA and Completion Rate standards.”
### `454d9c726264dd61` Tennessee Technological University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/professional-judgement.php (sha256 984c0110a4a7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Circumstances Not Given Consideration The Department of Education has identified conditions that, individually or in combination with one another, DO NOT QUALIFY AS UNUSUAL CIRCUMSTANCES, or do not merit a change in dependency status.”
### `775567f8cb73d667` Tennessee Technological University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/professional-judgement.php (sha256 984c0110a4a7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: professional_judgment ⟵ “Click the links below to access the desired information. 26/27 Professional Judgment Forms 25/26 Professions Judgment Forms Appeal Examples Dependency Overrides Fall 2026, Spring 2027 and Summer 2027 Professional Judgment Form Use the link below to access the Professional Judgment form.”
  - sentence: professional_judgment ⟵ “Forms must be initiated by the student, who when prompted will add other individuals (parent or spouse) if needed. 2026-2027 Professional Judgment Form Fall 2025, Spring 2026 and Summer 2026 Professional Judgment Forms Use the links below to access the appropriate Professional Judgment form for your circumstances.”
  - sentence: professional_judgment ⟵ “The student will be prompted to add other individuals (parent or spouse) if needed. 2025-2026 Professional Judgment Appeal Form 2025-2026 Professional Judgment Appeal Form: Marital Status to Tax Return Filing Status Professional Judgment Appeal Examples Listed below are examples of circumstances for which a professional judgment may be considered at Tennessee Tech University.”
  - sentence: professional_judgment ⟵ “A Professional Judgment Appeal Form requesting a re-evaluation should be completed and submitted for review to determine documentation needed.”
  - sentence: professional_judgment ⟵ “Please note that prior to the Professional Judgment process, the FAFSA application considers prior-prior year tax return information.”
### `e4708a66562cc3c3` Tennessee Technological University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tntech.edu/financialaid/sap.php (sha256 dfa2f7a684f5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 21}
  - sentence: sap_appeal ⟵ “Click the links below to learn more about Satisfactory Academic Progress, Tech's SAP Policy, Financial Aid Termination, and submitting appeals!”
  - sentence: sap_appeal ⟵ “Financial Aid Termination The SAP Appeal Process SAP Policy What is SAP?”
  - sentence: sap_appeal ⟵ “Students who do not meet one of the three above requirements when evaluated at the end of any given spring semester are placed on Financial Aid Termination and must submit a SAP Appeal to potentially regain their aid for the upcoming semester.”
  - sentence: sap_appeal ⟵ “A student placed on Financial Aid Termination cannot utilize their eligible federal or state aid until they either return to 'Good Standing' by meeting the SAP requirements for future semesters or submit a SAP Appeal for review that is then approved.”
  - sentence: sap_appeal ⟵ “Students placed on FA Termination receive an email notification from the Office of Financial Aid titled "TTU Financial Aid Information" that directs them to Eagle Online to view their Financial Aid Termination status - selecting the status redirects students to the Satisfactory Academic Progress webpage to learn more about Financial Aid Termination and submit a SAP Appeal.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Process Students placed on FA Termination who wish to continue using their aid can complete and submit a SAP Appeal for review.”
### `efc201fc84459cd2` Tennessee Technological University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/professional-judgement.php (sha256 984c0110a4a7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency Overrides Students must communicate with the Financial Aid Office for assistance with a Dependency Override request.”
### `0df2023009e0ea68` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Vice President's Residential Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `0eb2d5324a1cf398` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Fifth Semester at Tech ⟵ “Golden Eagle Excellence Scholarship | 8 Semesters | End of Fifth Semester at Tech | 2.50 | 0 | First year”
### `238e627fd18c92ef` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Fifth Semester at Tech ⟵ “Soaring Eagle Scholarship | 8 Semesters | End of Fifth Semester at Tech | 3.00 | 0 | First year”
### `26ab29dbd0629b71` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “University Academic Scholarship - Chess Tournament | 8 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `290fe444356365f0` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Second Semester at Tech & every semester thereafter ⟵ “All-Tennessee Academic Team Scholarship | 6 Semesters | End of Second Semester at Tech & every semester thereafter | 3.00 | 0 | Every year”
### `329c15a5be5000f7` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Fifth Semester at Tech ⟵ “High Flyers Scholarship | 8 Semesters | End of Fifth Semester at Tech | 3.25 | 0 | First year”
### `37055718841ebd7d` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Golden Eagle Excellence Scholarship | 8 Semesters | End of Every Spring Semester | 2.5 | 0 | First year”
### `3ac8908080d6b321` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Soaring Eagle Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 0 | First year”
### `3d2f38a735b54a19` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Admissions Academic Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 0 | First year”
### `5006c02c2a297eef` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Fifth Semester at Tech ⟵ “Tennessee State Scholastic Chess Championship Scholarship | 8 Semesters | End of Fifth Semester at Tech | 3.25 | 0 | Every year”
### `6b18155250f69078` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Second Semester at Tech & every semester thereafter ⟵ “Phi Theta Kappa Scholarship | 6 Semesters | End of Second Semester at Tech & every semester thereafter | 3.00 | 0 | Every year”
### `7f07ccb43c159ce1` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Community College Transfer Scholarship | 6 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `954e35feeb66bd18` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Phi Theta Kappa Scholarship | 6 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `ad0c112dc4e26746` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Third Semester at Tech & every semester thereafter ⟵ “Presidential Scholars Scholarship | 8 Semesters | End of Third Semester at Tech & every semester thereafter | 3.00 | 0 | N/A”
### `bbdcef2c9a95e8d2` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Tech Alumni Legacy Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 0 | First year”
### `c32aacc38b4a1733` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Second Semester at Tech & every semester thereafter ⟵ “Flight to Tech Transfer Scholarship (formerly Tech Transfer Pride) | 6 Semesters | End of Second Semester at Tech & every semester thereafter | 3.00 | 0 | N/A”
### `d54b01c495a0e206` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “University Academic Service Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `d68e45d26882253b` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “All-Tennessee Academic Team Scholarship | 6 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `e8e622b5d81c2225` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Upper Cumberland Valedictorian/Salutatorian Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 0 | First year”
### `f8a3c8fe497e63aa` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Third Semester at Tech & every semester thereafter ⟵ “Golden Opportunity Grant | 8 Semesters | End of Third Semester at Tech & every semester thereafter | 3.00 | 55 | Every year”
### `fcafd64be742593c` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Third Semester at Tech & every semester thereafter ⟵ “Upper Cumberland Valedictorian/Salutatorian Scholarship | 8 Semesters | End of Third Semester at Tech & every semester thereafter | 3.00 | 0 | Every year”
### `74a16798ae79d370` Tennessee Technological University — costs 2025-26 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/cost.php (sha256 88176cba5638)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 16712 ⟵ “Tuition/Fees | $16,712 | $16,712”
  - on_campus:Housing: 7014 ⟵ “Housing | $7,014 | $8,403”
  - on_campus:Food: 6821 ⟵ “Food | $6,821 | $6,821”
  - on_campus:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - on_campus:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - on_campus:Personal Expenses: 2750 ⟵ “Personal Expenses | $2,750 | $2,750”
  - on_campus:TOTAL: 37377 ⟵ “TOTAL | $37,377 | $38,766”
  - with_parents_or_family:Tuition/Fees: 16712 ⟵ “Tuition/Fees | $16,712 | $16,712”
  - with_parents_or_family:Housing: 8403 ⟵ “Housing | $7,014 | $8,403”
  - with_parents_or_family:Food: 6821 ⟵ “Food | $6,821 | $6,821”
  - with_parents_or_family:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - with_parents_or_family:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - with_parents_or_family:Personal Expenses: 2750 ⟵ “Personal Expenses | $2,750 | $2,750”
  - with_parents_or_family:TOTAL: 38766 ⟵ “TOTAL | $37,377 | $38,766”
### `d44ab9350efe52cf` Tennessee Technological University — costs 2025-26 · residency=in_state [same] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/cost.php (sha256 88176cba5638)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 12081 ⟵ “Tuition/Fees | $12,081 | $12,081”
  - on_campus:Housing: 7014 ⟵ “Housing | $7,014 | $8,403”
  - on_campus:Food: 6821 ⟵ “Food | $6,821 | $6,821”
  - on_campus:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - on_campus:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - on_campus:Personal Expenses: 2750 ⟵ “Personal Expenses | $2,750 | $2,750”
  - on_campus:TOTAL: 32746 ⟵ “TOTAL | $32,746 | $34,135”
  - with_parents_or_family:Tuition/Fees: 12081 ⟵ “Tuition/Fees | $12,081 | $12,081”
  - with_parents_or_family:Housing: 8403 ⟵ “Housing | $7,014 | $8,403”
  - with_parents_or_family:Food: 6821 ⟵ “Food | $6,821 | $6,821”
  - with_parents_or_family:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - with_parents_or_family:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - with_parents_or_family:Personal Expenses: 2750 ⟵ “Personal Expenses | $2,750 | $2,750”
  - with_parents_or_family:TOTAL: 34135 ⟵ “TOTAL | $32,746 | $34,135”
### `1e319c5098f4838c` Tennessee Wesleyan University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: http://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/ (sha256 1c46152d271d)
- issues: conflicting_sources:https://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/,https://www.tnwesleyan.edu/wp-content/uploads/2026/06/COA2627.pdf
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 31880 ⟵ “Tuition | $30,650 | $31,880 | $15,940”
  - column:Clinical Fees: 2250 ⟵ “Clinical Fees | $2,150 | $2,250 | $1,125”
  - column:RN-BSN: 400 ⟵ “RN-BSN | $385 | $400 | ”
### `b999031e5d69bd7e` Tennessee Wesleyan University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/ (sha256 57aac58c528b)
- issues: conflicting_sources:http://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/,https://www.tnwesleyan.edu/wp-content/uploads/2026/06/COA2627.pdf
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 31880 ⟵ “Tuition | $30,650 | $31,880 | $15,940”
  - column:Clinical Fees: 2250 ⟵ “Clinical Fees | $2,150 | $2,250 | $1,125”
  - column:RN-BSN: 400 ⟵ “RN-BSN | $385 | $400 | ”
### `c56434ac7eb2311e` Tennessee Wesleyan University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/ (sha256 57aac58c528b)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 30650 ⟵ “Tuition | $30,650 | $31,880 | $15,940”
  - column:Clinical Fees: 2150 ⟵ “Clinical Fees | $2,150 | $2,250 | $1,125”
  - column:RN-BSN: 385 ⟵ “RN-BSN | $385 | $400 | ”
### `d6309aa0f5f3cd20` Tennessee Wesleyan University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tnwesleyan.edu/wp-content/uploads/2026/06/COA2627.pdf (sha256 ae6c8ecb8a93)
- issues: multiple_total_rows, conflicting_sources:http://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/,https://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/
- checks: {"columns": 1, "rows": 6}
  - column:Tuition & Fees: 33280 ⟵ “Tuition & Fees | 33280”
  - column:Books: 1400 ⟵ “Books | 1400”
  - column:Food & Housing: 10528 ⟵ “Food & Housing | 10528”
  - column:Transportation: 2000 ⟵ “Transportation | 2000”
  - column:Misc.: 1500 ⟵ “Misc. | 1500”
  - column:Total: 48708 ⟵ “Total | 48708”
  - column:Tuition & Fees: 34030 ⟵ “Tuition & Fees | 34030”
  - column:Books: 1400 ⟵ “Books | 1400”
  - column:Food & Housing: 10528 ⟵ “Food & Housing | 10528”
  - column:Transportation: 2000 ⟵ “Transportation | 2000”
  - column:Misc.: 1500 ⟵ “Misc. | 1500”
  - column:Total: 49458 ⟵ “Total | 49458”
  - column:Tuition & Fees: 33810 ⟵ “Tuition & Fees | 33810”
  - column:Books: 2100 ⟵ “Books | 2100”
  - column:Food & Housing: 11428 ⟵ “Food & Housing | 11428”
  - column:Transportation: 3000 ⟵ “Transportation | 3000”
  - column:Misc.: 2250 ⟵ “Misc. | 2250”
  - column:Total: 52588 ⟵ “Total | 52588”
  - column:Tuition & Fees: 14520 ⟵ “Tuition & Fees | 14520”
  - column:Books: 1400 ⟵ “Books | 1400”
  - column:Food & Housing: 10528 ⟵ “Food & Housing | 10528”
  - column:Transportation: 2000 ⟵ “Transportation | 2000”
  - column:Misc.: 1500 ⟵ “Misc. | 1500”
  - column:Total: 29948 ⟵ “Total | 29948”
  - column:Tuition & Fees: 39775 ⟵ “Tuition & Fees | 39775”
  - … 5 more rows
### `9a70e2cdc3511292` The University of Tennessee Southern — appeals 2026-27 [new] (source_unlabeled)
- source: http://utsouthern.edu/cost-and-aid/financial-aid/financial-aid-faq/ (sha256 cb422347662f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “If you have any issues locating a requested document (tax document, dependency override document, etc.), please contact the Financial Aid Office at financialaid@utsouthern.edu.”
### `f6b0df480d63f691` The University of Tennessee Southern — appeals 2026-27 [new] (source_unlabeled)
- source: http://utsouthern.edu/cost-and-aid/financial-aid/financial-aid-faq/ (sha256 cb422347662f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “You’ll also find guidance on how to handle special circumstances, like locating requested documents or addressing a denied SAP appeal.”
  - sentence: sap_appeal ⟵ “What happens if my SAP appeal is denied?”
  - sentence: sap_appeal ⟵ “If your SAP appeal is denied, you can set up a payment plan with the Bursar’s Office or consider applying for a private loan to fund your education.”
### `47d81e1f126d9a7b` The University of Tennessee Southern — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://utsouthern.edu/wp-content/uploads/2026/09/2026-2027-Standard-cost-of-attendance-002.docx.pdf (sha256 690886045400)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 1, "rows": 14}
  - column:Tuition: 10228.0 ⟵ “Tuition | $10,228.00”
  - column:Required Fees: 1374.0 ⟵ “Required Fees | $1,374.00”
  - column:Housing: 5877.0 ⟵ “Housing | $5,877.00”
  - column:Meals: 4867.0 ⟵ “Meals | $4,867.00”
  - column:Direct Costs Subtotal: 22346.0 ⟵ “Direct Costs Subtotal | $22,346.00”
  - column:Books & Supplies: 1500.0 ⟵ “Books & Supplies | $1,500.00”
  - column:Loan Fees: 95.0 ⟵ “Loan Fees | $95.00”
  - column:Personal Expenses: 2000.0 ⟵ “Personal Expenses | $2,000.00”
  - column:Transportation: 2500.0 ⟵ “Transportation | $2,500.00”
  - column:Indirect Costs Subtotal: 6095.0 ⟵ “Indirect Costs Subtotal | $6,095.00”
  - column:Grand Total: 28441.0 ⟵ “Grand Total | $28,441.00”
  - column:Tuition: 10228.0 ⟵ “Tuition | $10,228.00”
  - column:Required Fees: 1374.0 ⟵ “Required Fees | $1,374.00”
  - column:Direct Costs Subtotal: 11602.0 ⟵ “Direct Costs Subtotal | $11,602.00”
  - column:Estimated Housing: 9360.0 ⟵ “Estimated Housing | $9,360.00”
  - column:Food/Meals: 4867.0 ⟵ “Food/Meals | $4,867.00”
  - column:Books & Supplies: 1500.0 ⟵ “Books & Supplies | $1,500.00”
  - column:Loan Fees: 95.0 ⟵ “Loan Fees | $95.00”
  - column:Personal Expenses: 2000.0 ⟵ “Personal Expenses | $2,000.00”
  - column:Transportation: 2500.0 ⟵ “Transportation | $2,500.00”
  - column:Indirect Costs Subtot: 20322.0 ⟵ “Indirect Costs Subtot | $20,322.00”
  - column:Grand Total: 31924.0 ⟵ “Grand Total | $31,924.00”
  - column:Tuition: 10228.0 ⟵ “Tuition | $10,228.00”
  - column:Required Fees: 1374.0 ⟵ “Required Fees | $1,374.00”
  - column:Direct Costs Subtotal: 11602.0 ⟵ “Direct Costs Subtotal | $11,602.00”
  - … 19 more rows
### `10e40c98c5c887d6` The University of Tennessee-Chattanooga — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/transfer-scholarship (sha256 a814af58c6d8)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/chancellors-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/mocs-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/provosts-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of this scholarship and Is Not appealable. • You did not maintain the required cumulative GPA; • You did not pass the required number of credit hours (or service/work hours); • You have taken a fall or spring semester off and not attended classes; • You have totally withdrawn from classes for the term, officially or unofficiall”
### `22c396544d6281ac` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/academic-service-scholars-program (sha256 78c50bae1505)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap,https://www.utc.edu/enrollment-management-and-student-affairs/mocs-one-center/choose-correct-appeal-form
- checks: {"negative_sentences": 0, "sentences": 1}
- change process_summary: `Scholarship Appeal for students who lost a UTC scholarship or the Tennessee HOPE scholarship because of GPA, credit completion or enrollment status; online form; decision within 45 days.` → `Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable. • You did not maintain the required cumulative GPA; • You did not pass the required number of credit hours (or service/work hours); • You have taken a fall or spring semester off and not attended classes; • You have totally withdrawn from classes for the term, officially or unofficially.`
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable. • You did not maintain the required cumulative GPA; • You did not pass the required number of credit hours (or service/work hours); • You have taken a fall or spring semester off and not attended classes; • You have totally withdrawn from classes for the term, officia”
### `271e1fdd74334180` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/mocs-one-center/choose-correct-appeal-form (sha256 8365480cd807)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/academic-service-scholars-program
- checks: {"negative_sentences": 0, "sentences": 1}
- change process_summary: `Scholarship Appeal for students who lost a UTC scholarship or the Tennessee HOPE scholarship because of GPA, credit completion or enrollment status; online form; decision within 45 days.` → `A Scholarship Appeal for the loss of your TN HOPE Scholarship can be submitted if you have extenuating circumstances have contributed to the following: You have totally withdrawn from classes for the term.`
  - sentence: scholarship_retention_appeal ⟵ “A Scholarship Appeal for the loss of your TN HOPE Scholarship can be submitted if you have extenuating circumstances have contributed to the following: You have totally withdrawn from classes for the term.”
### `45cea4c46cfb1bbe` The University of Tennessee-Chattanooga — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/mocs-scholarship (sha256 a02171e97356)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/chancellors-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/provosts-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/transfer-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable (i.e.”
### `491b557f852aa994` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap (sha256 a5bec19d078c)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 5}
- change offered: `False` → `True`
- change process_summary: `The appeal-form guide lists no special-circumstances / professional-judgment appeal; financial aid forms pages were not fully reviewed.` → `Appeal statements should include the following: Explain any unusual circumstances that led to your financial aid suspension.`
  - sentence: need_based_special_circumstances ⟵ “Appeal statements should include the following: Explain any unusual circumstances that led to your financial aid suspension.”
  - sentence: need_based_special_circumstances ⟵ “Be specific- indicate dates and time periods involved and how the unusual circumstances affected your academic performance.”
  - sentence: need_based_special_circumstances ⟵ “If UTC offers a service that helps mitigate your unusual circumstance, you may be required to document that you are using this service.”
  - sentence: need_based_special_circumstances ⟵ “Signed Statement, indicating rationale for app Statement must include an explanation of unusual circumstances that led to financial aid suspension.”
  - sentence: need_based_special_circumstances ⟵ “Sufficient documentation to support claim of unusual circumstances.”
### `b918848305774b72` The University of Tennessee-Chattanooga — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/professional-judgment (sha256 9dd86f982faa)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: professional_judgment ⟵ “Quick Links » Calendar Campus News Canvas Change Password Class Schedule Crisis Resources Library Google Workspace MocSync MyMocsNet Microsoft O365 GTranslate Special and Unusual Circumstances Professional Judgment What is a professional judgment?”
  - sentence: professional_judgment ⟵ “Such exceptions, known as professional judgment, are considered on a case-by-case basis with supporting documentation of your unique circumstances.”
  - sentence: professional_judgment ⟵ “Please note you must be currently enrolled in the aid year for which you are requesting the Professional Judgment for it to be considered.”
  - sentence: professional_judgment ⟵ “Professional judgments take 6-8 weeks for a decision once all documentation is submitted.”
  - sentence: professional_judgment ⟵ “Professional Judgment Special and Unusual Circumstances Appeal Instructions Complete your Professional Judgment Professional Judgment FAQs What documents should I submit with my Professional Judgment request?”
  - sentence: professional_judgment ⟵ “How long before I know the outcome of a Professional Judgment?”
### `bbf5746ce49fe84f` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap (sha256 a5bec19d078c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
- change process_summary: `Financial Aid / Satisfactory Academic Progress (SAP) Appeal for students who lost financial aid by not meeting SAP standards; online form; decision within 45 days.` → `Financial Aid Probation - If a student has a Satisfactory Academic Progress (SAP) Appeal approved, they will be placed on a one semester warning period if it will be possible to bring their Course Completion Rate and GPA to maintain SAP standards after the next semester.`
  - sentence: sap_appeal ⟵ “Financial Aid Probation - If a student has a Satisfactory Academic Progress (SAP) Appeal approved, they will be placed on a one semester warning period if it will be possible to bring their Course Completion Rate and GPA to maintain SAP standards after the next semester.”
  - sentence: sap_appeal ⟵ “Academic Plan - If a student has a Satisfactory Academic Progress (SAP) Appeal approved and it is NOT possible for them to maintain the required Course Completion Rate and GPA to maintain SAP after one semester of enrollment, they will be placed in a SAP Academic Plan.”
  - sentence: sap_appeal ⟵ “Notification of Status and right to appeal Students will be notified of changes to SAP status and any appeal decisions via UTC email.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals Process and Financial Aid Appeal Forms Students appealing their Satisfactory Academic Progress status are required to submit an appeals packet for review.”
  - sentence: sap_appeal ⟵ “The following are due in the SAP Appeals packet: Financial Aid Appeal Form.”
  - sentence: sap_appeal ⟵ “Review Process There are three levels of appeal in the SAP Appeals process.”
### `bcfa9290a1d7fd6c` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap (sha256 a5bec19d078c)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/academic-service-scholars-program,https://www.utc.edu/enrollment-management-and-student-affairs/mocs-one-center/choose-correct-appeal-form
- checks: {"negative_sentences": 0, "sentences": 2}
- change process_summary: `Scholarship Appeal for students who lost a UTC scholarship or the Tennessee HOPE scholarship because of GPA, credit completion or enrollment status; online form; decision within 45 days.` → `The Financial Aid SAP Committee does not have authority to approve or deny University or TN HOPE Scholarship appeals.`
  - sentence: scholarship_retention_appeal ⟵ “The Financial Aid SAP Committee does not have authority to approve or deny University or TN HOPE Scholarship appeals.”
  - sentence: scholarship_retention_appeal ⟵ “The Financial Aid SAP Committee does not have authority to approve or deny University or TN HOPE scholarship appeals.”
### `d0cbce2e8fcc24ea` The University of Tennessee-Chattanooga — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/chancellors-scholarship (sha256 c56f17f98ee2)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/mocs-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/provosts-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/transfer-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable (i.e.”
### `e14d61d15a330d23` The University of Tennessee-Chattanooga — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships (sha256 eaf88556f581)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Quick Links » Calendar Campus News Canvas Change Password Class Schedule Crisis Resources Library Google Workspace MocSync MyMocsNet Microsoft O365 GTranslate Financial Aid and Scholarships Dates Forms Accepting Aid Parents Faculty and Staff Professional Judgment Frequently Asked Questions Office of Financial Aid and Scholarships Student Employment FAFSA An affordable degree starts here UTC’s Offi”
### `e8f1a13fa78665c2` The University of Tennessee-Chattanooga — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/provosts-scholarship (sha256 41aa73fe1e12)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/chancellors-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/mocs-scholarship,https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/transfer-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable (i.e.”
### `fabe62c66ff9da7b` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/professional-judgment (sha256 9dd86f982faa)
- issues: semantic_review_required, conflicting_sources:https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap
- checks: {"negative_sentences": 0, "sentences": 5}
- change offered: `False` → `True`
- change process_summary: `The appeal-form guide lists no special-circumstances / professional-judgment appeal; financial aid forms pages were not fully reviewed.` → `What is considered special or unusual circumstance?`
  - sentence: need_based_special_circumstances ⟵ “What is considered special or unusual circumstance?”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are financial changes that have occurred to a student or parent since completing the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances refer to a student’s dependency status, also known as dependency override.”
  - sentence: need_based_special_circumstances ⟵ “None of the following conditions, singly or in combination, qualify as unusual circumstances meriting a dependency override: Parents refuse to contribute to the student's education.”
  - sentence: need_based_special_circumstances ⟵ “Submitting an explanation with supporting documentation does not guarantee a change in financial aid awards.”
### `26063ed084e45178` The University of Tennessee-Chattanooga — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://www.utc.edu/sites/default/files/2026-09/2026-27-estimated-cost-of-attendance.pdf (sha256 4dc086460fb0)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "rows": 9}
  - with_parents_or_family:Enrollment Fees: 11084 ⟵ “Enrollment Fees | 11084 | 11084 | 11084 | 11789”
  - with_parents_or_family:Books: 1400 ⟵ “Books | 1400 | 1400 | 1400 | 1200”
  - with_parents_or_family:Housing: 2600 ⟵ “Housing | 2600 | 8800 | 9204 | 9450”
  - with_parents_or_family:Food: 4552 ⟵ “Food | 4552 | 4552 | 4552 | 4552”
  - with_parents_or_family:Transportation: 2300 ⟵ “Transportation | 2300 | 2300 | 2300 | 3200”
  - with_parents_or_family:Personal Expenses: 1800 ⟵ “Personal Expenses | 1800 | 1800 | 1800 | 2600”
  - with_parents_or_family:IN-STATE TOTAL: 23736 ⟵ “IN-STATE TOTAL | 23736 | 29936 | 30340 | 32791”
  - with_parents_or_family:Out-of-State Tuition: 8306 ⟵ “Out-of-State Tuition | 8306 | 8306 | 8306 | 8306”
  - with_parents_or_family:Out-of-State Total: 32042 ⟵ “Out-of-State Total | 32042 | 38242 | 38646 | 41097”
  - with_parents_or_family:Enrollment Fees: 11084 ⟵ “Enrollment Fees | 11084 | 11084 | 11084 | 11789”
  - with_parents_or_family:Books: 1400 ⟵ “Books | 1400 | 1400 | 1400 | 1200”
  - with_parents_or_family:Housing: 2600 ⟵ “Housing | 2600 | 8800 | 9204 | 9450”
  - with_parents_or_family:Food: 4552 ⟵ “Food | 4552 | 4552 | 4552 | 4552”
  - with_parents_or_family:Transportation: 2300 ⟵ “Transportation | 2300 | 2300 | 2300 | 3200”
  - with_parents_or_family:Personal Expenses: 1800 ⟵ “Personal Expenses | 1800 | 1800 | 1800 | 2600”
  - with_parents_or_family:IN-STATE TOTAL: 23736 ⟵ “IN-STATE TOTAL | 23736 | 29936 | 30340 | 32791”
  - with_parents_or_family:Out-of-State Tuition: 642 ⟵ “Out-of-State Tuition | 642 | 642 | 642 | 872”
  - with_parents_or_family:Out-of-State Total: 24378 ⟵ “Out-of-State Total | 24378 | 30578 | 30982 | 33663”
  - off_campus_not_with_family:Enrollment Fees: 11084 ⟵ “Enrollment Fees | 11084 | 11084 | 11084 | 11789”
  - off_campus_not_with_family:Books: 1400 ⟵ “Books | 1400 | 1400 | 1400 | 1200”
  - off_campus_not_with_family:Housing: 8800 ⟵ “Housing | 2600 | 8800 | 9204 | 9450”
  - off_campus_not_with_family:Food: 4552 ⟵ “Food | 4552 | 4552 | 4552 | 4552”
  - off_campus_not_with_family:Transportation: 2300 ⟵ “Transportation | 2300 | 2300 | 2300 | 3200”
  - off_campus_not_with_family:Personal Expenses: 1800 ⟵ “Personal Expenses | 1800 | 1800 | 1800 | 2600”
  - off_campus_not_with_family:IN-STATE TOTAL: 29936 ⟵ “IN-STATE TOTAL | 23736 | 29936 | 30340 | 32791”
  - … 47 more rows
### `c643c360044a6731` The University of Tennessee-Knoxville — admissions_metrics 2025-26 [same] (labeled_in_source)
- source: https://irsa.utk.edu/wp-content/uploads/sites/5/2026/06/CDS_2025-26_C_.pdf (sha256 432ea71922ec)
- issues: applications_breakdown_does_not_reconcile
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 53841 ⟵ “Total first-time, first-year (degree-seeking) who applied   11,980           41,408          452       0     53,841”
  - admits: 23464 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                    8,725           14,526          213       0     23,464”
  - enrolled: 7143 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                         4,326            2,764           53       0       7,143”
  - sat_composite_25..75: [1280, 1330, 1380] ⟵ “SAT Composite                                1280            1330          1380”
  - sat_reading_25..75: [640, 670, 700] ⟵ “SAT Evidence-Based Reading and   640            670           700”
  - sat_math_25..75: [630, 660, 700] ⟵ “SAT Math                                      630            660           700”
  - act_25..75: [26, 29, 31] ⟵ “ACT Composite                                 26              29            31”
### `3f95fc85ded8e5c4` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (source_unlabeled)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/information/ (sha256 09f48a3ebda4)
- issues: semantic_review_required, conflicts_with_verified_record
- checks: {"negative_sentences": 1, "sentences": 2}
- change process_summary: `The official Scholarship FAQ answers "Will UT match scholarship and financial aid offers from other institutions?" with "UT cannot match scholarship or aid offers from other institutions."` → `Will UT match scholarship and financial aid offers from other institutions?`
  - sentence: competing_offer_review ⟵ “Will UT match scholarship and financial aid offers from other institutions?”
  - sentence: competing_offer_review ⟵ “UT cannot match scholarship or aid offers from other institutions.”
### `498c0550f01d565d` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (source_unlabeled)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/hope-institutional-scholarship-appeals/ (sha256 ba74b75d22de)
- issues: semantic_review_required, conflicting_sources:https://onestop.utk.edu/scholarships-financial-aid/scholarships/chancellors-scholarships/, conflicts_with_verified_record
- checks: {"negative_sentences": 0, "sentences": 6}
- change process_summary: `HOPE & Institutional Scholarship Appeals: students may appeal loss of HOPE or institutional scholarship eligibility caused by extenuating circumstances (health emergency, death of immediate family member, mental health crisis). Dropping courses to protect GPA does not qualify. HOPE GPA review after a later benchmark and the one-time HOPE grade-replacement option are also handled here. Complete appeals (statement plus documentation) go to the Institutional Review Panel. Chancellor's Scholarship GPA-loss appeals can grant probationary eligibility for one semester.` → `In certain circumstances, students may appeal a loss of scholarship eligibility when an extenuating circumstance affected their ability to meet those requirements.`
  - sentence: scholarship_retention_appeal ⟵ “In certain circumstances, students may appeal a loss of scholarship eligibility when an extenuating circumstance affected their ability to meet those requirements.”
  - sentence: scholarship_retention_appeal ⟵ “Eligibility for HOPE & Institutional Scholarship Appeals If an extenuating circumstance affected your ability to meet the scholarship’s requirements, you may be eligible to appeal your loss of scholarship eligibility.”
  - sentence: scholarship_retention_appeal ⟵ “If you have already lost your HOPE Scholarship due to a change in enrollment status, you may appeal to regain your award.”
  - sentence: scholarship_retention_appeal ⟵ “How to Submit a HOPE & Institutional Scholarship Appeal Access the Hope & Institutional Scholarship Appeal Request Form to begin the appeal process.”
  - sentence: scholarship_retention_appeal ⟵ “HOPE Scholarship Appeals: If your appeal is denied by the IRP, you may appeal directly with THEC within 45 days of receiving your denial letter.”
  - sentence: scholarship_retention_appeal ⟵ “For more information, visit TELS, TN Promise and TN Reconnect Appeals and Exceptions – collegefortn.org.”
### `816ec152388d24dc` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (source_unlabeled)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/satisfactory-academic-progress-sap-appeals/ (sha256 e7e96ea19c07)
- issues: semantic_review_required, conflicting_sources:https://onestop.utk.edu/scholarships-financial-aid/financial-aid/keep-your-financial-aid-sap/, conflicts_with_verified_record
- checks: {"negative_sentences": 0, "sentences": 4}
- change process_summary: `Satisfactory Academic Progress appeals to restore federal aid eligibility: personal statement (what happened, what changed, academic plan), third-party documentation and an advisor-signed academic plan; due at least 14 days before the last day of classes for the term.` → `How to Start Your SAP Appeal To. submit a SAP appeal, follow these steps: Step 1: Submit a Case in Vol Connect Portal Log in to the Vol Connect Portal Open a new case, select Financial Aid as the Request Type.`
  - sentence: sap_appeal ⟵ “How to Start Your SAP Appeal To. submit a SAP appeal, follow these steps: Step 1: Submit a Case in Vol Connect Portal Log in to the Vol Connect Portal Open a new case, select Financial Aid as the Request Type.”
  - sentence: sap_appeal ⟵ “What You’ll Need to Submit Once you access the CampusLogic Student Forms Portal, you will see your SAP Appeal requirement.”
  - sentence: sap_appeal ⟵ “Incomplete SAP appeals will not be reviewed.”
  - sentence: sap_appeal ⟵ “Once your materials are submitted, the SAP Appeal Committee will review your case.”
### `8a5b5bb202d59600` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/chancellors-scholarships/ (sha256 2788ed6093e9)
- issues: semantic_review_required, conflicting_sources:https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/hope-institutional-scholarship-appeals/, conflicts_with_verified_record
- checks: {"negative_sentences": 0, "sentences": 1}
- change process_summary: `HOPE & Institutional Scholarship Appeals: students may appeal loss of HOPE or institutional scholarship eligibility caused by extenuating circumstances (health emergency, death of immediate family member, mental health crisis). Dropping courses to protect GPA does not qualify. HOPE GPA review after a later benchmark and the one-time HOPE grade-replacement option are also handled here. Complete appeals (statement plus documentation) go to the Institutional Review Panel. Chancellor's Scholarship GPA-loss appeals can grant probationary eligibility for one semester.` → `All Chancellor’s Scholarships require a cumulative GPA of 3.25 or higher If the student experienced extenuating circumstances that affected their ability to meet the minimum requirements, they can submit a written appeal for the loss of their scholarship.`
  - sentence: scholarship_retention_appeal ⟵ “All Chancellor’s Scholarships require a cumulative GPA of 3.25 or higher If the student experienced extenuating circumstances that affected their ability to meet the minimum requirements, they can submit a written appeal for the loss of their scholarship.”
### `a5606ac2e4558bb4` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (source_unlabeled)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/budget-increase-appeals/ (sha256 bd068cb95ca5)
- issues: semantic_review_required, conflicts_with_verified_record
- checks: {"negative_sentences": 0, "sentences": 1}
- change process_summary: `Budget Increase Appeals for additional education-related expenses (childcare, one-time computer purchase, internship/student teaching, one medical expense per year, extra books/supplies, study abroad). Excludes reimbursed expenses, amounts within the standard allowance, vehicle costs and expenses while not enrolled. Approval does not guarantee additional aid; decisions are final absent new documentation.` → `To submit a Budget Increase Appeal, follow these steps: Step 1: Submit a Case in Vol Connect Log in to the Vol Connect Portal.`
  - sentence: budget_increase ⟵ “To submit a Budget Increase Appeal, follow these steps: Step 1: Submit a Case in Vol Connect Log in to the Vol Connect Portal.”
### `c857a5314602dad2` The University of Tennessee-Knoxville — appeals 2027-28 [new] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/special-circumstances-appeals/ (sha256 d415417f42c8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Students may only complete one Special Circumstance Appeal per academic year (August–July).”
  - sentence: need_based_special_circumstances ⟵ “To submit a Special Circumstances Appeal, follow these steps: Step 1: Submit a Case in Vol Connect Log in to the Vol Connect Portal.”
### `d1976e7da7579e2e` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (source_unlabeled)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/keep-your-financial-aid-sap/ (sha256 cd8b985c9d5f)
- issues: semantic_review_required, conflicting_sources:https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/satisfactory-academic-progress-sap-appeals/, conflicts_with_verified_record
- checks: {"negative_sentences": 0, "sentences": 1}
- change process_summary: `Satisfactory Academic Progress appeals to restore federal aid eligibility: personal statement (what happened, what changed, academic plan), third-party documentation and an advisor-signed academic plan; due at least 14 days before the last day of classes for the term.` → `SAP Grades & Appeals UT monitors your cumulative completion percentage, maximum time allowance, and grade point average at the end of each semester.`
  - sentence: sap_appeal ⟵ “SAP Grades & Appeals UT monitors your cumulative completion percentage, maximum time allowance, and grade point average at the end of each semester.”
### `1566b95fe338d5a9` The University of Tennessee-Knoxville — awards 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/tri-star-scholarships/ (sha256 8623f762a82a)
- issues: conflicts_with_verified_record
- checks: {"thresholds": null}
- change award_type: `institutional_access` → `institutional_other`
- change award_amount_text: `Combined with HOPE, covers tuition and mandatory fees for up to eight semesters.` → `Tuition & mandatory fees`
  - award_amount_text: Tuition & mandatory fees ⟵ “Flagship Scholarship | First-time, First-Year, Current, & Transfer Students | Tuition & mandatory fees | UT Priority Filing Date | January 5”
### `2df2bf266a7e9550` The University of Tennessee-Knoxville — awards 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/tri-star-scholarships/ (sha256 8623f762a82a)
- issues: conflicts_with_verified_record
- checks: {"thresholds": null}
- change award_type: `institutional_need_last_dollar` → `institutional_other`
- change award_amount_text: `Last-dollar award that, combined with other aid, covers tuition, mandatory fees and average on-campus housing and food, for up to eight semesters; college-specific course fees for architecture, business, engineering and nursing are not covered.` → `Tuition, mandatory fees, average on-campus Housing and Food*`
  - award_amount_text: Tuition, mandatory fees, average on-campus Housing and Food* ⟵ “Tennessee Pledge Scholarship | First-time, First-Year, Current, & Transfer Students | Tuition, mandatory fees, average on-campus Housing and Food* | UT Priority Filing Date | January 5”
### `e6ec39e58d30adcd` The University of Tennessee-Knoxville — awards 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/next-chapter-scholarship-next-chapter-scholar-of-the-year-award/ (sha256 8689988779f9)
- issues: conflicts_with_verified_record
- checks: {"thresholds": null}
- change award_type: `institutional_program_based` → `institutional_other`
- change award_amount_text: `$1,500 per year, up to $6,000 over four years.` → `$1,500`
  - award_amount_text: $1,500 ⟵ “Next Chapter Scholarship | $1,500 | $6,000 | $26,400”
### `e92052d73507dc0b` The University of Tennessee-Knoxville — awards 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/tri-star-scholarships/ (sha256 8623f762a82a)
- issues: conflicts_with_verified_record
- checks: {"thresholds": null}
- change award_type: `institutional_need_last_dollar` → `institutional_other`
- change award_amount_text: `Last-dollar award covering tuition and mandatory fees when combined with other federal, state and institutional aid.` → `Tuition & mandatory fees`
  - award_amount_text: Tuition & mandatory fees ⟵ “UT Promise Scholarship | First-Year, Transfer, Current, & Non-Traditional Students receiving HOPE Scholarship | Tuition & mandatory fees | UT Priority Filing Date | January 5”
### `9b435c8d9c1bfec8` The University of Tennessee-Knoxville — costs 2025-26 · residency=in_state [same] (labeled_in_source)
- source: https://admissions.utk.edu/undergraduate-tuition-aid/ (sha256 bd8e2c65df7f)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition & Fees: 13876 ⟵ “Tuition & Fees | $13,876”
  - column:Housing & Food: 14738 ⟵ “Housing & Food | $14,738”
  - column:Books, Course Materials, Supplies and Equipment: 1598 ⟵ “Books, Course Materials, Supplies and Equipment | $1,598”
  - column:Total: 30212 ⟵ “Total | $30,212”
### `a6cc0f2876c95ac3` The University of Tennessee-Knoxville — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://onestop.utk.edu/billing-payments/cost-of-attending-ut-undergraduate-student/ (sha256 30140893482e)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 11560 ⟵ “Tuition | $11,560 | $31,672”
  - column:FeesThis is an estimate of what a student will spend on tuition and fees for the Fall and Spring semesters.: 2464 ⟵ “FeesThis is an estimate of what a student will spend on tuition and fees for the Fall and Spring semesters. | $2,464 | $2,806”
  - column:On-Campus Housing*This is an estimate of what a student will spend on housing and meals for the Fall and Spring semesters if they live in university housing.: 9572 ⟵ “On-Campus Housing*This is an estimate of what a student will spend on housing and meals for the Fall and Spring semesters if they live in university housing. | $9,572 | $9,572”
  - column:Food: 5166 ⟵ “Food | $5,166 | $5,166”
  - column:TransportationThis item is for budgeting purposes only and will not be billed to you.: 3500 ⟵ “TransportationThis item is for budgeting purposes only and will not be billed to you. | $3,500 | $3,500”
  - column:Miscellaneous Personal Expenses (Based on personal spending habits)This item is for budgeting purposes only and will not be billed to you.: 3042 ⟵ “Miscellaneous Personal Expenses (Based on personal spending habits)This item is for budgeting purposes only and will not be billed to you. | $3,042 | $3,042”
  - column:Loan FeesThis is an estimate of what the average student spends in federal loan origination fee.: 92 ⟵ “Loan FeesThis is an estimate of what the average student spends in federal loan origination fee. | $92 | $92”
  - column:Total, with on-campus housing(Direct costs plus estimated indirect costs): 36994 ⟵ “Total, with on-campus housing(Direct costs plus estimated indirect costs) | $36,994 | $57,448”
### `b792d43eaa353beb` The University of Tennessee-Knoxville — costs 2025-26 · residency=out_of_state [same] (labeled_in_source)
- source: https://admissions.utk.edu/undergraduate-tuition-aid/ (sha256 bd8e2c65df7f)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition & Fees: 33336 ⟵ “Tuition & Fees | $33,336”
  - column:Housing & Food: 14738 ⟵ “Housing & Food | $14,738”
  - column:Books, Course Materials, Supplies and Equipment: 1598 ⟵ “Books, Course Materials, Supplies and Equipment | $1,598”
  - column:Total: 49672 ⟵ “Total | $49,672”
### `ba8a402c0b2bf4e3` The University of Tennessee-Knoxville — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://onestop.utk.edu/billing-payments/cost-of-attending-ut-undergraduate-student/ (sha256 30140893482e)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 31672 ⟵ “Tuition | $11,560 | $31,672”
  - column:FeesThis is an estimate of what a student will spend on tuition and fees for the Fall and Spring semesters.: 2806 ⟵ “FeesThis is an estimate of what a student will spend on tuition and fees for the Fall and Spring semesters. | $2,464 | $2,806”
  - column:On-Campus Housing*This is an estimate of what a student will spend on housing and meals for the Fall and Spring semesters if they live in university housing.: 9572 ⟵ “On-Campus Housing*This is an estimate of what a student will spend on housing and meals for the Fall and Spring semesters if they live in university housing. | $9,572 | $9,572”
  - column:Food: 5166 ⟵ “Food | $5,166 | $5,166”
  - column:TransportationThis item is for budgeting purposes only and will not be billed to you.: 3500 ⟵ “TransportationThis item is for budgeting purposes only and will not be billed to you. | $3,500 | $3,500”
  - column:Miscellaneous Personal Expenses (Based on personal spending habits)This item is for budgeting purposes only and will not be billed to you.: 3042 ⟵ “Miscellaneous Personal Expenses (Based on personal spending habits)This item is for budgeting purposes only and will not be billed to you. | $3,042 | $3,042”
  - column:Loan FeesThis is an estimate of what the average student spends in federal loan origination fee.: 92 ⟵ “Loan FeesThis is an estimate of what the average student spends in federal loan origination fee. | $92 | $92”
  - column:Total, with on-campus housing(Direct costs plus estimated indirect costs): 57448 ⟵ “Total, with on-campus housing(Direct costs plus estimated indirect costs) | $36,994 | $57,448”
### `m91994a855b5c4bd` The University of Tennessee-Knoxville — transfer_policies 2026-27 [changed] (source_unlabeled)
- source: https://admissions.utk.edu/rocky-top-transfer-participant-information/ (sha256 0e8a021d72c9)
- issues: conflicting_values:residency_requirement_credits
- checks: {"fields": ["min_grade"], "merged_pages": 3}
- change additional_source_urls: `['https://admissions.utk.edu/admitted-students/transfer/', 'https://irsa.utk.edu/wp-content/uploads/sites/5/2026/06/CDS_2025-26_D.pdf', 'https://catalog.utk.edu/content.php?catoid=56&navoid=12030']` → `['https://admissions.utk.edu/admitted-students-vols-online/', 'https://admissions.utk.edu/admitted-students/transfer/']`
  - min_grade: D- ⟵ “Transfer credit will be granted only for college level non-remedial courses in which a grade of D- or better was earned.”
  - min_grade: D- ⟵ “Transfer credit will be granted only for college level non-remedial courses in which a grade of D- or better was earned.”
  - min_grade: D- ⟵ “Transfer credit will be granted only for college level non-remedial courses in which a grade of D- or better was earned.”
### `0318aa4a471ee1d6` Union University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.uu.edu/admissions/financial-aid/policies-practices/ (sha256 fceb7cb8b778)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Adjustments for Special Circumstances Students who feel their FAFSA information does not accurately reflect their financial situation due to certain special or unusual circumstances, may request to have their FAFSA information reviewed for possible adjustment (known as a Professional Judgement).”
  - sentence: professional_judgment ⟵ “However, there is some flexibility, when appropriate, for financial aid administrators to exercise professional judgment on a case-by-case basis to override the student’s dependency status and/or recalculate the student’s eligibility for financial aid.”
### `d72d8fd06f476689` Union University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.uu.edu/admissions/financial-aid/policies-practices/ (sha256 fceb7cb8b778)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: need_based_special_circumstances ⟵ “Skip To: General Policies Academic Standards/Satisfactory Academic Progress Institutional Scholarship Policy Loan Credit Refund Dates Consumer Information Special Circumstances Policy General Policies Edits made to reflect 2021-22 and 2022-23 Academic Year applicable information.”
  - sentence: need_based_special_circumstances ⟵ “Students/parents must complete a Special Circumstances Form available on the Student Financial Aid website (or by contacting the Office of Student Financial Aid), providing any other requested support documentation, and be available to discuss your situation if needed with a staff member from Student Financial Aid.”
  - sentence: need_based_special_circumstances ⟵ “If selected for verification, a student’s FAFSA information must be verified and corrected before consideration for special circumstances adjustment can be given.”
  - sentence: need_based_special_circumstances ⟵ “Decision regarding Special Circumstance appeals are final.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Policy The rules and the formula to determine financial aid eligibility are standard for all applicants.”
  - sentence: need_based_special_circumstances ⟵ “Submitting an appeal for special circumstances does not guarantee that it will be approved, or additional financial aid will be granted.”
### `f2e840f8189f391f` Union University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.uu.edu/admissions/financial-aid/policies-practices/ (sha256 fceb7cb8b778)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal While students are expected to meet the minimum academic progress requirements to maintain eligibility for financial aid, the university recognizes that extenuating circumstances may occasionally prevent students from making satisfactory progress toward their degree.”
  - sentence: sap_appeal ⟵ “If the student becomes ineligible for financial aid due to not meeting Satisfactory Academic Progress (SAP) requirements before the beginning of the academic year, and if extenuating circumstances have impacted their academic performance, he/she may submit a SAP Appeal for reconsideration of financial aid eligibility.”
  - sentence: sap_appeal ⟵ “The SAP Appeal provides an opportunity for students to explain the circumstances that affected their academic progress and request an evaluation of their financial aid status.”
### `17f9c262cdf2824f` Union University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/biology/ (sha256 6d08223a34ab)
- issues: conflicting_sources:https://www.uu.edu/admissions/financial-aid/cost-of-attendance/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/edge/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/education/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/mcuts/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/nursing/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/soaps/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/social-work/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/theology-missions/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
- change tuition: `41170` → `11214`
- change mandatory_fees: `1520` → `612`
- change books_supplies: `750` → `450`
- change total_cost_of_attendance: `75476` → `52693`
  - column:Tuition: 11214 ⟵ “Tuition | $11,214 | Based on 6 credits each semester over Fall, Spring, and Summer”
  - column:Mandatory Fees: 612 ⟵ “Mandatory Fees | $612 | Based on fees for 18 credits total”
  - column:Housing: 14220 ⟵ “Housing | $14,220 | This is a standard allowance for the cost of off-campus rent or other housing costs over the course of the academic year. Your actual costs may vary.”
  - column:Food/Meals: 6696 ⟵ “Food/Meals | $6,696 | This is an allowance for off-campus food/meals over the course of the academic year. Your actual costs may vary.”
  - column:Books, Course Materials, Supplies, and Equipment: 450 ⟵ “Books, Course Materials, Supplies, and Equipment | $450 | This is an estimate; your costs could differ depending on how you obtain your books and required course materials or supplies.”
  - column:Transportation: 4404 ⟵ “Transportation | $4,404 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Loan Fees: 217 ⟵ “Loan Fees | $217 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFP for more information.”
  - column:Personal Expenses: 14880 ⟵ “Personal Expenses | $14,880 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 52693 ⟵ “Total COA | $52,693 | Total allowable Cost of Attendance for Master of Biology and Master of Conservation Biology students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 11826 ⟵ “Total Direct Costs | $11,826 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 40867 ⟵ “Total Indirect Costs | $40,867 | ”
### `4dd7a0a50ae7f9cc` Union University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/edge/ (sha256 5ff1794d6d99)
- issues: conflicting_sources:https://www.uu.edu/admissions/financial-aid/cost-of-attendance/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/biology/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/education/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/mcuts/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/nursing/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/soaps/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/social-work/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/theology-missions/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
- change tuition: `41170` → `20590`
- change books_supplies: `750` → `600`
- change total_cost_of_attendance: `75476` → `54616`
  - column:Tuition: 20590 ⟵ “Tuition | $20,590 | Block rate at $10,295 per semester.”
  - column:Mandatory Fees: 1520 ⟵ “Mandatory Fees | $1,520 | Block rate at $760 per semester.”
  - column:Housing: 10800 ⟵ “Housing | $10,800 | ”
  - column:Food/Meals: 6636 ⟵ “Food/Meals | $6,636 | This is the 285 meal-plan; your costs could differ depending on your meal-plan selection.”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | This is an estimate; your costs could differ depending on how you obtain your books and required course materials or supplies.”
  - column:Transportation: 3316 ⟵ “Transportation | $3,316 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Personal Expenses: 11154 ⟵ “Personal Expenses | $11,154 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 54616 ⟵ “Total COA | $54,616 | Total allowable Cost of Attendance for EDGE students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 39546 ⟵ “Total Direct Costs | $39,546 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 15070 ⟵ “Total Indirect Costs | $15,070 | ”
### `8bcad21f12b3b471` Union University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/social-work/ (sha256 401bc0e79bce)
- issues: conflicting_sources:https://www.uu.edu/admissions/financial-aid/cost-of-attendance/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/biology/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/edge/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/education/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/mcuts/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/nursing/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/soaps/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/theology-missions/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
- change tuition: `41170` → `10890`
- change mandatory_fees: `1520` → `612`
- change books_supplies: `750` → `450`
- change total_cost_of_attendance: `75476` → `52284`
  - column:Tuition: 10890 ⟵ “Tuition | $10,890 | Based on 6 credits each semester over Fall, Spring, and Summer”
  - column:Mandatory Fees: 612 ⟵ “Mandatory Fees | $612 | Based on fees for 18 credits total”
  - column:Housing: 14220 ⟵ “Housing | $14,220 | This is a standard allowance for the cost of off-campus rent or other housing costs over the course of the academic year. Your actual costs may vary.”
  - column:Food/Meals: 6696 ⟵ “Food/Meals | $6,696 | This is an allowance for off-campus food/meals over the course of the academic year. Your actual costs may vary.”
  - column:Books, Course Materials, Supplies, and Equipment: 450 ⟵ “Books, Course Materials, Supplies, and Equipment | $450 | This is an estimate; your costs could differ depending on how you obtain your books and required course materials or supplies.”
  - column:Transportation: 4404 ⟵ “Transportation | $4,404 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Loan Fees: 132 ⟵ “Loan Fees | $132 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFA for more information.”
  - column:Personal Expenses: 14880 ⟵ “Personal Expenses | $14,880 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 52284 ⟵ “Total COA | $52,284 | Total allowable Cost of Attendance for Adult Bachelor of Social Work students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 11502 ⟵ “Total Direct Costs | $11,502 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 40782 ⟵ “Total Indirect Costs | $40,782 | ”
### `973687be3fe2f62a` Union University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/theology-missions/ (sha256 78dff9f48ffb)
- issues: conflicting_sources:https://www.uu.edu/admissions/financial-aid/cost-of-attendance/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/biology/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/edge/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/education/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/mcuts/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/nursing/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/soaps/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/social-work/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
- change tuition: `41170` → `8100`
- change mandatory_fees: `1520` → `612`
- change books_supplies: `750` → `450`
- change total_cost_of_attendance: `75476` → `49579`
  - column:Tuition: 8100 ⟵ “Tuition | $8,100 | Based on 6 credits each semester over Fall, Spring, and Summer”
  - column:Mandatory Fees: 612 ⟵ “Mandatory Fees | $612 | Based on fees for 18 credits total”
  - column:Housing: 14220 ⟵ “Housing | $14,220 | This is a standard allowance for the cost of off-campus rent or other housing costs over the course of the academic year. Your actual costs may vary.”
  - column:Food/Meals: 6696 ⟵ “Food/Meals | $6,696 | This is an allowance for off-campus food/meals over the course of the academic year. Your actual costs may vary.”
  - column:Books, Course Materials, Supplies, and Equipment: 450 ⟵ “Books, Course Materials, Supplies, and Equipment | $450 | This is an estimate; your costs could differ depending on how you obtain your books and required course materials or supplies.”
  - column:Transportation: 4404 ⟵ “Transportation | $4,404 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Loan Fees: 217 ⟵ “Loan Fees | $217 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFA for more information.”
  - column:Personal Expenses: 14880 ⟵ “Personal Expenses | $14,880 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 49579 ⟵ “Total COA | $49,579 | Total allowable Cost of Attendance for Master of Christian Studies students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 8712 ⟵ “Total Direct Costs | $8,712 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 40867 ⟵ “Total Indirect Costs | $40,867 | ”
### `a353a149e9f8e4c0` Union University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/mcuts/ (sha256 f8fa1c3e741e)
- issues: conflicting_sources:https://www.uu.edu/admissions/financial-aid/cost-of-attendance/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/biology/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/edge/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/education/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/nursing/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/soaps/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/social-work/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/theology-missions/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
- change tuition: `41170` → `7416`
- change mandatory_fees: `1520` → `720`
- change books_supplies: `750` → `450`
- change total_cost_of_attendance: `75476` → `48918`
  - column:Tuition: 7416 ⟵ “Tuition | $7,416 | Based on 6 credits each semester over Fall, Spring, and Summer”
  - column:Mandatory Fees: 720 ⟵ “Mandatory Fees | $720 | Based on fees for Fall, Spring, and Summer”
  - column:Housing: 14220 ⟵ “Housing | $14,220 | This is a standard allowance for the cost of off-campus rent or other housing costs over the course of the academic year. Your actual costs may vary.”
  - column:Food/Meals: 6696 ⟵ “Food/Meals | $6,696 | This is an allowance for off-campus food/meals over the course of the academic year. Your actual costs may vary.”
  - column:Books, Course Materials, Supplies, and Equipment: 450 ⟵ “Books, Course Materials, Supplies, and Equipment | $450 | This is an estimate; your costs could differ depending on how you obtain your books and required course materials or supplies.”
  - column:Transportation: 4404 ⟵ “Transportation | $4,404 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Loan Fees: 132 ⟵ “Loan Fees | $132 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFA for more information.”
  - column:Personal Expenses: 14880 ⟵ “Personal Expenses | $14,880 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 48918 ⟵ “Total COA | $48,918 | Total allowable Cost of Attendance for Memphis Center for Urban and Theological Studies (MCUTS) students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 8136 ⟵ “Total Direct Costs | $8,136 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 40782 ⟵ “Total Indirect Costs | $40,782 | ”
### `b7cc5c2c66d7dcc2` Union University — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/ (sha256 85d194790377)
- issues: conflicting_sources:https://www.uu.edu/admissions/financial-aid/cost-of-attendance/biology/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/edge/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/education/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/mcuts/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/nursing/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/soaps/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/social-work/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/theology-missions/
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition: 41170 ⟵ “Tuition | $41,170 | 12-16 hours per semester as a block rate”
  - column:Mandatory Fees: 1520 ⟵ “Mandatory Fees | $1,520 | This does not include a one-time $185 Orientation fee for first-time Union students.”
  - column:Housing: 10800 ⟵ “Housing | $10,800 | This is the cost for The Quads Apartments; your costs could differ depending on your housing option.”
  - column:Food/Meals: 6636 ⟵ “Food/Meals | $6,636 | This is the 285 meal-plan; your costs could differ depending on your meal-plan selection.”
  - column:Books, Course Materials, Supplies, and Equipment: 750 ⟵ “Books, Course Materials, Supplies, and Equipment | $750 | This is an estimate using the Buster Book Bundle; your costs could differ depending on how you purchase your books”
  - column:Transportation: 3316 ⟵ “Transportation | $3,316 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Loan Fees: 130 ⟵ “Loan Fees | $130 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFP for more information.”
  - column:Personal Expenses: 11154 ⟵ “Personal Expenses | $11,154 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 75476 ⟵ “Total COA | $75,476 | Total allowable Cost of Attendance for on-campus, traditional undergraduate students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 60126 ⟵ “Total Direct Costs | $60,126 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 15350 ⟵ “Total Indirect Costs | $15,350 | ”
### `c51e76a4d770ba7b` Union University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/education/ (sha256 da39776b340c)
- issues: conflicting_sources:https://www.uu.edu/admissions/financial-aid/cost-of-attendance/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/biology/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/edge/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/mcuts/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/nursing/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/soaps/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/social-work/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/theology-missions/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
- change tuition: `41170` → `11484`
- change mandatory_fees: `1520` → `612`
- change books_supplies: `750` → `450`
- change total_cost_of_attendance: `75476` → `52963`
  - column:Tuition: 11484 ⟵ “Tuition | $11,484 | Based on 6 credits each semester over Fall, Spring, and Summer”
  - column:Mandatory Fees: 612 ⟵ “Mandatory Fees | $612 | Based on fees for 18 credits total”
  - column:Housing: 14220 ⟵ “Housing | $14,220 | This is a standard allowance for the cost of off-campus rent or other housing costs over the course of the academic year. Your actual costs may vary.”
  - column:Food/Meals: 6696 ⟵ “Food/Meals | $6,696 | This is an allowance for off-campus food/meals over the course of the academic year. Your actual costs may vary.”
  - column:Books, Course Materials, Supplies, and Equipment: 450 ⟵ “Books, Course Materials, Supplies, and Equipment | $450 | This is an estimate; your costs could differ depending on how you obtain your books and required course materials or supplies.”
  - column:Transportation: 4404 ⟵ “Transportation | $4,404 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Loan Fees: 217 ⟵ “Loan Fees | $217 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFP for more information.”
  - column:Personal Expenses: 14880 ⟵ “Personal Expenses | $14,880 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 52963 ⟵ “Total COA | $52,963 | Total allowable Cost of Attendance for Master of Education or Master of Arts in Education students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 12096 ⟵ “Total Direct Costs | $12,096 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 40867 ⟵ “Total Indirect Costs | $40,867 | ”
### `c5a6bf5ab3a6c502` Union University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/nursing/ (sha256 8e35dd28f81c)
- issues: conflicting_sources:https://www.uu.edu/admissions/financial-aid/cost-of-attendance/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/biology/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/edge/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/education/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/mcuts/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/soaps/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/social-work/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/theology-missions/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": true, "rows": 12}
- change tuition: `41170` → `35808`
- change mandatory_fees: `1520` → `350`
- change books_supplies: `750` → `1200`
- change total_cost_of_attendance: `75476` → `78507`
  - column:Tuition: 35808 ⟵ “Tuition | $35,808* | Based on 48 total credits over Fall, Spring, and Summer”
  - column:Mandatory Fees: 350 ⟵ “Mandatory Fees | $350* | Based on fees for 48 total credits”
  - column:Housing: 14220 ⟵ “Housing | $14,220 | This is a standard allowance for the cost of off-campus rent or other housing costs over the course of the academic year. Your actual costs may vary.”
  - column:Food/Meals: 6696 ⟵ “Food/Meals | $6,696 | This is an allowance for off-campus food/meals over the course of the academic year. Your actual costs may vary.”
  - column:Books, Course Materials, Supplies, and Equipment: 1200 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,200 | This is an estimate; your costs could differ depending on how you obtain your books and required course materials or supplies.”
  - column:Transportation: 4404 ⟵ “Transportation | $4,404 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Loan Fees: 132 ⟵ “Loan Fees | $132 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFP for more information.”
  - column:Additional Out-Of-Pocket Required Expenses: 817 ⟵ “Additional Out-Of-Pocket Required Expenses | $817 | This is an estimate for additional cost requirements of the program such as CPR training, background checks, etc.”
  - column:Personal Expenses: 14880 ⟵ “Personal Expenses | $14,880 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 78507 ⟵ “Total COA | $78,507 | Total allowable Cost of Attendance for BSNA Accelerated Nursing students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 36158 ⟵ “Total Direct Costs | $36,158 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 42349 ⟵ “Total Indirect Costs | $42,349 | ”
### `f4c675c86cb0cb8c` Union University — costs 2026-27 · residency=not_applicable [changed] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/soaps/ (sha256 0a81ea889015)
- issues: conflicting_sources:https://www.uu.edu/admissions/financial-aid/cost-of-attendance/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/biology/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/edge/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/education/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/mcuts/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/nursing/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/social-work/,https://www.uu.edu/admissions/financial-aid/cost-of-attendance/theology-missions/, conflicts_with_verified_record
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
- change tuition: `41170` → `7416`
- change mandatory_fees: `1520` → `612`
- change books_supplies: `750` → `450`
- change total_cost_of_attendance: `75476` → `48810`
  - column:Tuition: 7416 ⟵ “Tuition | $7,416 | Based on 6 credits each semester over Fall, Spring, and Summer”
  - column:Mandatory Fees: 612 ⟵ “Mandatory Fees | $612 | Based on fees for 18 credits total”
  - column:Housing: 14220 ⟵ “Housing | $14,220 | This is a standard allowance for the cost of off-campus rent or other housing costs over the course of the academic year. Your actual costs may vary.”
  - column:Food/Meals: 6696 ⟵ “Food/Meals | $6,696 | This is an allowance for off-campus food/meals over the course of the academic year. Your actual costs may vary.”
  - column:Books, Course Materials, Supplies, and Equipment: 450 ⟵ “Books, Course Materials, Supplies, and Equipment | $450 | This is an estimate; your costs could differ depending on how you obtain your books and required course materials or supplies.”
  - column:Transportation: 4404 ⟵ “Transportation | $4,404 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Loan Fees: 132 ⟵ “Loan Fees | $132 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFA for more information.”
  - column:Personal Expenses: 14880 ⟵ “Personal Expenses | $14,880 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 48810 ⟵ “Total COA | $48,810 | Total allowable Cost of Attendance for Adult Studies (SOAPS) Associate or Bachelor Degree students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 8028 ⟵ “Total Direct Costs | $8,028 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 40782 ⟵ “Total Indirect Costs | $40,782 | ”
### `317dd537ab3ed665` Vanderbilt University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/reconsideration/ (sha256 b7bb05c5c772)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.vanderbilt.edu/financialaid/undergraduate/satisfactory-progress/
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: need_based_special_circumstances ⟵ “What are Special Circumstances? “Special circumstances” refers to financial situations that may lead to a financial aid adjustment.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances could include one or more of the following: PROFILE or FAFSA information reported erroneously or omitted.”
  - sentence: need_based_special_circumstances ⟵ “What will not be considered for special circumstances: Differences between the nationally accepted methodology used for awarding institutional funds and the mandated federal methodology used for awarding limited federal assistance.”
  - sentence: need_based_special_circumstances ⟵ “The reason for the adjustment must be adequately documented and must be related to special circumstances that differentiate the student.”
  - sentence: need_based_special_circumstances ⟵ “More information about Undergraduate Special Circumstances.”
  - sentence: need_based_special_circumstances ⟵ “More information about Graduate Special Circumstances.”
### `34dc73e2303d6c2f` Vanderbilt University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/undergraduate/satisfactory-progress/ (sha256 890634a4ec83)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Procedures Any student whose institutional and/or federal Title IV student aid is Suspended due to unsatisfactory academic progress may submit an appeal for reinstatement of such assistance to the Office of Student Financial Aid and Scholarships.”
### `57f9eba4b13f7d0c` Vanderbilt University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/reconsideration/ (sha256 b7bb05c5c772)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “This type of adjustment is called a Dependency Override.”
  - sentence: dependency_override ⟵ “All requests for determination of independence, including dependency overrides and unaccompanied homeless youth determinations, will be reviewed as soon as practicable once all documentation is received.”
### `6d72bb26da4b81dc` Vanderbilt University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/reconsideration/ (sha256 b7bb05c5c772)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “This type of adjustment is called a Request for Professional Judgment.”
  - sentence: professional_judgment ⟵ “The Financial Aid Office may use professional judgment on a case-by-case basis to adjust a student’s cost of attendance or the data used to calculate the students’ Student Aid Index.”
  - sentence: professional_judgment ⟵ “A school is not permitted to make a professional judgment for a student after that student has ceased to be eligible, including when the student is no longer enrolled.”
### `75f4cefa41e64305` Vanderbilt University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/undergraduate/satisfactory-progress/ (sha256 890634a4ec83)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.vanderbilt.edu/financialaid/reconsideration/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The appeal for reinstatement should include the following elements: An explanation of extenuating circumstances, such as injury, illness, death of a relative, or other special circumstance as to why you failed to meet satisfactory academic progress requirements.”
### `b7dcf2324fab8e49` Vanderbilt University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.vanderbilt.edu/financialaid/wp-content/uploads/sites/92/2025/09/UGRAD-Request-for-Reconsideration.pdf (sha256 e721fc9b72cb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances refer to financial situations that may lead to a financial aid adjustment.”
  - sentence: need_based_special_circumstances ⟵ “Reconsideration of your financial aid eligibility can be given under such special circumstances, and if you have not already notified us of such errors, omissions, or significant changes, please do so at this time.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances refer to conditions that may lead to an adjustment to a student’s dependency status based on a unique situation.”
### `ab5a635a3d48e504` Vanderbilt University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/costs-undergraduate/ (sha256 8ceae287ccc8)
- issues: conflicting_sources:https://admissions.vanderbilt.edu/affordability/
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 69822 ⟵ “Tuition | $69,822”
  - column:Housing: 15170 ⟵ “Housing | $15,170”
  - column:Food: 8520 ⟵ “Food | $8,520”
  - column:Student Support Fee: 3384 ⟵ “Student Support Fee | $3,384”
  - column:Total Direct Cost of Attendance - Mandatory: 96896 ⟵ “Total Direct Cost of Attendance - Mandatory | $96,896”
### `d57591531102aac4` Vanderbilt University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://admissions.vanderbilt.edu/affordability/ (sha256 a80f3d79c819)
- issues: components_do_not_reconcile, conflicting_sources:https://www.vanderbilt.edu/financialaid/costs-undergraduate/
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 69822 ⟵ “Tuition | $69,822”
  - column:Housing: 15170 ⟵ “Housing | $15,170”
  - column:Food: 8520 ⟵ “Food | $8,520”
  - column:Student Support Fee: 3384 ⟵ “Student Support Fee | $3,384”
  - column:Total Direct Cost of Attendance – Mandatory: 96896 ⟵ “Total Direct Cost of Attendance – Mandatory | $96,896”
  - column:Books, Course Materials, Supplies, & Equipment Allowance: 1100 ⟵ “Books, Course Materials, Supplies, & Equipment Allowance | $1,100”
  - column:Personal Expenses Allowance: 1998 ⟵ “Personal Expenses Allowance | $1,998”
  - column:Total Indirect Costs – Discretionary/Elective: 3098 ⟵ “Total Indirect Costs – Discretionary/Elective | $3,098”
### `304d648d165d1e4e` Walters State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ws.edu/cost-aid/types/scholarships/lottery/index.aspx (sha256 7b3ce5136792)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: scholarship_retention_appeal ⟵ “Additional information for Lottery is available at: Tennessee HOPE Scholarship Appeal Process for Tennessee Education Lottery Scholarship (TELS) Complete the relevant appeal form.”
  - sentence: scholarship_retention_appeal ⟵ “Appeals cannot be considered if Lottery eligibility is lost due to GPA. | Reasons that may be considered for Lottery Appeals Change of Enrollment Status: A recipient of the TELS may not withdraw or drop below full-time enrollment after the 14th calendar day (census date) of the semester and maintain their scholarship unless the student requests and the institution approves the change in enrollment”
  - sentence: scholarship_retention_appeal ⟵ “The student will be notified by TSAC of a decision after an appeal is filed and documentation is received The TELS Award Appeals Panel at TSAC is the final administrative appeal. *TELS GPA Your TELS (Lottery) GPA may differ from your overall combined GPA.”
### `5d49636d134c30c1` Walters State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ws.edu/cost-aid/eligibility-verification/maintain/index.aspx (sha256 5ce4c5393838)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeals will be considered for the following reasons: Serious injury or illness of the student Death, serious injury/illness of immediate family member (mother, father, sibling, spouse, child) Family trauma which occurred during the semester in question Other extenuating circumstances (must be documented) Process for filing an appeal: Complete the Satisfactory Academic Progress (SAP) Appeal.”
  - sentence: sap_appeal ⟵ “Forms are available in the Financial Aid Office and off-campus sites or by emailing finaid@ws.edu from Senators Mail account to request the electronic SAP appeal.”
### `de3a758394f7da43` Walters State Community College — credit_policies 2010-11 · policy_kind=AP [new] (labeled_in_source)
- source: https://ws.edu/admissions/prior-learning/exams/ap/index.aspx (sha256 609b40b677ff)
- issues: stale_year_label:2010-11
- checks: {"distinct_exams": 28, "equivalencies": 45, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3, 4, 5]:  ⟵ “Art History || 3, 4, 5 | 3 | ARTH 2010”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology || 3 | 4 | BIOL 1010/1011 OR BIOL 1110/1111”
  - equivalencies[AP-BIOLOGY|4, 5]:  ⟵ “Biology || 4, 5 | 8 | BIOL 1010/1110 & 1020/1021 OR BIOL 1110/1111 & BIOL 1120/1121”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB || 3 | 3 | MATH 1830”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “Calculus AB || 4, 5 | 3 | MATH 1830 OR MATH 1910”
  - equivalencies[AP-CALCULUS-BC|3, 4, 5]:  ⟵ “Calculus BC || 3, 4, 5 | 8 | MATH 1910 & MATH 1920”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry || 3 | 4 | CHEM 1110/1111”
  - equivalencies[AP-CHEMISTRY|4, 5]:  ⟵ “Chemistry || 4, 5 | 8 | CHEM 1110/111 & CHEM 1120/1121”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture || 3 | 6 | Foreign Language Elective Hours”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture || 4 | 9 | Foreign Language Elective Hours”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language & Culture || 5 | 12 | Foreign Language Elective Hours”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, 5]:  ⟵ “Computer Science A || 3, 4, 5 | 3 | INFS 1010”
  - equivalencies[AP-MACROECONOMICS|3, 4, 5]:  ⟵ “Macroeconomics || 3, 4, 5 | 3 | ECON 2010”
  - equivalencies[AP-MICROECONOMICS|3, 4, 5]:  ⟵ “Microeconomics || 3, 4, 5 | 3 | ECON 2020”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3, 4, 5]:  ⟵ “English Language & Composition || 3, 4, 5 | 3 | ENGL 1010”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, 5]:  ⟵ “English Literature || 3, 4, 5 | 3 | ENGL 1020”
  - equivalencies[AP-EUROPEAN-HISTORY|3, 4, 5]:  ⟵ “European History || 3, 4, 5 | 6 | HIST 1110 & 1120”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture || 3 | 6 | FREN 1010 & 1020”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language & Culture || 4 | 9 | FREN 1010, 1020 & 2010”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture || 5 | 12 | FREN 1010, 1020, 2010 & 2020”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture || 3 | 6 | GERM 1010 & 1020”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language & Culture || 4 | 9 | GERM 1010, 1020 & 2010”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language & Culture || 5 | 12 | GERM 1010, 1020, 2010 & 2020”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “Comparative Government & Politics || 3, 4, 5 | 3 | POLS 2100”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “U.S. Government & Politics || 3, 4, 5 | 3 | POLS 1030”
  - … 20 more rows
### `1e5adfc64b3c85bb` Welch College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://welch.edu/wp-content/uploads/2024/02/DE-Grant-Information-rev.-7_2026.docx-Google-Docs-1.pdf (sha256 4d12a0f021c7)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted"], "tiers": 1}
  - state_grant_accepted: True ⟵ “​ he Dual Enrollment Grant program is defined as a grant for study at an eligible postsecondary institution,​”
  - per_credit_hour_charge: 100 ⟵ “​Courses​                          ​$100.00/hr.​      ​$190.00/hr.​          ​$90.00/hr.​         ​Student Responsibility​”
  - per_credit_hour_charge: 190 ⟵ “​Courses​                          ​$100.00/hr.​      ​$190.00/hr.​          ​$90.00/hr.​         ​Student Responsibility​”
  - per_credit_hour_charge: 90 ⟵ “​Courses​                          ​$100.00/hr.​      ​$190.00/hr.​          ​$90.00/hr.​         ​Student Responsibility​”
  - per_credit_hour_charge: 190 ⟵ “​Courses​                             ​$0​        ​$190/credit hr.​       ​$190/credit hr.​      ​Student Responsibility​”
  - per_credit_hour_charge: 190 ⟵ “​Courses​                             ​$0​        ​$190/credit hr.​       ​$190/credit hr.​      ​Student Responsibility​”
  - eligibility_tier: 2.0 ⟵ “​b.​ ​A 2.0 GPA for all postsecondary courses attempted under the Dual Enrollment Grant is required​”
  - state_grant_accepted: True ⟵ ““​ The DEG application has been expanded to allow students to list up to three eligible​”

## Re-verification of existing records (57)

- nothing_to_check: data/institutions/abcnash/transfer_policies/2026-27.json ["transfer_policies", "ipeds-219505", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Academic Achievement"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Dean's"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Governor's Excellence"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Governor's Merit"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Presidential"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Presidents Emerging Leaders Program (PELP)Apply by 12/31"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Kimbrough (Limited Awards Available)"}]
- nothing_to_check: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Howell C. Smith (Limited Awards Available)"}]
- all_values_found_year_not_labeled: data/institutions/belmont/transfer_policies/2026-27.json ["transfer_policies", "ipeds-219709", null, "2026-27", {}]
- values_not_found_verbatim: data/institutions/bryan/awards/2026-27.json ["awards", "ipeds-219790", null, "2026-27", {"award_name": "Platinum"}] missing=['thresholds.gpa_min']
- values_not_found_verbatim: data/institutions/bryan/awards/2026-27.json ["awards", "ipeds-219790", null, "2026-27", {"award_name": "Silver"}] missing=['thresholds.gpa_min']
- values_not_found_verbatim: data/institutions/bryan/awards/2026-27.json ["awards", "ipeds-219790", null, "2026-27", {"award_name": "Crimson"}] missing=['thresholds.gpa_min']
- all_values_found_year_not_labeled: data/institutions/jscc/costs/2026-27.json ["costs", "ipeds-220400", null, "2026-27", {"residency": "out_of_state"}]
- all_values_found_year_not_labeled: data/institutions/jscc/credit_policies/2026-27.json ["credit_policies", "ipeds-220400", null, "2026-27", {"policy_kind": "AP"}]
- nothing_to_check: data/institutions/jscc/credit_policies/2026-27.json ["credit_policies", "ipeds-220400", null, "2026-27", {"policy_kind": "CLEP"}]
- nothing_to_check: data/institutions/johnsonu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-220473", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/lanecollege/transfer_policies/2026-27.json ["transfer_policies", "ipeds-220598", null, "2026-27", {}]
- nothing_to_check: data/institutions/lipscomb/credit_policies/2026-27.json ["credit_policies", "ipeds-219976", null, "2026-27", {"policy_kind": "AP"}]
- nothing_to_check: data/institutions/lipscomb/transfer_policies/2026-27.json ["transfer_policies", "ipeds-219976", null, "2026-27", {}]
- nothing_to_check: data/institutions/midsouthchristian/transfer_policies/2026-27.json ["transfer_policies", "ipeds-481225", null, "2026-27", {}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "sap_appeal"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "scholarship_retention_appeal"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "merit_reconsideration"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "competing_offer_review"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "need_based_special_circumstances"}]
- policy_text_not_verbatim: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Chancellor's Scholarship"}] year=2025-26
- policy_text_not_verbatim: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Provost's Scholarship"}] year=2025-26
- policy_text_not_verbatim: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Mocs Scholarship"}] year=2025-26
- policy_text_not_verbatim: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Academic Service Scholars Program"}]
- values_not_found_verbatim: data/institutions/utc/costs/2026-27.json ["costs", "ipeds-221740", null, "2026-27", {"residency": "in_state"}] missing=['on_campus_food_housing', 'on_campus_other_expenses'] year=2026-27
- values_not_found_verbatim: data/institutions/utc/costs/2026-27.json ["costs", "ipeds-221740", null, "2026-27", {"residency": "out_of_state"}] missing=['on_campus_food_housing', 'on_campus_other_expenses'] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/credit_policies/2026-27.json ["credit_policies", "ipeds-221740", null, "2026-27", {"policy_kind": "AP"}]
- policy_text_not_verbatim: data/institutions/utc/credit_policies/2026-27.json ["credit_policies", "ipeds-221740", null, "2026-27", {"policy_kind": "CLEP"}]
- all_values_found_year_not_labeled: data/institutions/utc/credit_policies/2026-27.json ["credit_policies", "ipeds-221740", null, "2026-27", {"policy_kind": "IB"}]
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "program-total"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "upper-division-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "residency-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "gen-ed-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "major-hours"}] year=2026-27
- nothing_to_check: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "four-year-plan"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "program-total"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "upper-division-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "residency-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "gen-ed-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "major-hours"}] year=2026-27
- nothing_to_check: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "four-year-plan"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "program-total"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "upper-division-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "residency-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "gen-ed-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "major-hours"}] year=2026-27
- nothing_to_check: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "four-year-plan"}] year=2026-27
- values_not_found_verbatim: data/institutions/utc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-221740", null, "2026-27", {}] missing=['residency_requirement_credits']
- nothing_to_check: data/institutions/utk/awards/2026-27.json ["awards", "utk", null, "2026-27", {"award_name": "Manning Scholars"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utk/awards/2026-27.json ["awards", "utk", null, "2026-27", {"award_name": "Out-of-State Volunteer Scholarship"}] year=2026-27
- source_not_fetched: data/institutions/utk/transfer_policies/2026-27.json ["transfer_policies", "utk", null, "2026-27", {}]

## Statewide sources

Pages fetched: 270; pages by category: admissions_tests 7, common_data_set 2, cost_of_attendance 3, degree_requirements 1, dual_enrollment 5, merit_scholarships 23, residency 4, statewide_articulation 143, transfer_credit 150, tuition_fees 7

## Blocked by the site (every request refused; needs the browser fallback)

- Chattanooga State Community College (`ipeds-219824`)
- Cleveland State Community College (`ipeds-219879`)
- Cumberland University (`ipeds-219949`)
- Pellissippi State Community College (`ipeds-221643`)
- The University of Tennessee-Martin (`ipeds-221768`)
- Volunteer State Community College (`ipeds-222053`)
- Milligan University (`ipeds-486901`)

## Leads: official pages found with no extracted record

- American Baptist College: tuition_fees, cost_of_attendance, admissions_tests, degree_requirements
- Austin Peay State University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, residency
- Baptist Health Sciences University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- Belmont University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- Bethel University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements, aid_appeals
- Bryan College-Dayton: cost_of_attendance, admissions_tests, ap_credit, clep_credit, transfer_credit, degree_requirements
- Carson-Newman University: cost_of_attendance, admissions_tests, transfer_credit, residency, degree_requirements
- Christian Brothers University: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, statewide_articulation, residency
- Columbia State Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, transfer_credit, residency, degree_requirements
- Dyersburg State Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, transfer_credit, residency, degree_requirements
- East Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Fisk University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Freed-Hardeman University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit, degree_requirements
- Herzing University-Nashville: tuition_fees, cost_of_attendance, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, degree_requirements
- Jackson State Community College: admissions_tests, common_data_set, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- John A Gupton College: tuition_fees, cost_of_attendance, admissions_tests, degree_requirements
- Johnson University: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- King University: tuition_fees, admissions_tests, residency, degree_requirements
- Lane College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, degree_requirements
- Le Moyne-Owen College: tuition_fees, cost_of_attendance, dual_enrollment, transfer_credit
- Lee University: tuition_fees, cost_of_attendance, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Lincoln Memorial University: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, degree_requirements
- Lipscomb University: admissions_tests, merit_scholarships, statewide_articulation, degree_requirements
- Maryville College: cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Mid-South Christian College: tuition_fees, cost_of_attendance
- Middle Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Motlow State Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Nashville State Community College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Northeast State Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Remington College-Memphis Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Remington College-Nashville Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Rhodes College: cost_of_attendance, merit_scholarships, ap_credit, ib_credit, dual_enrollment, degree_requirements
- Roane State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Southern Adventist University: cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Southwest Tennessee Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Tennessee Technological University: admissions_tests, ap_credit, residency, degree_requirements
- Tennessee Wesleyan University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- The University of Tennessee Southern: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment
- The University of Tennessee-Chattanooga: tuition_fees, admissions_tests, transfer_credit, statewide_articulation, residency
- The University of Tennessee-Knoxville: statewide_articulation, residency
- The University of the South: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Trevecca Nazarene University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Tusculum University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit, degree_requirements
- Union University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- University of Memphis: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Vanderbilt University: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Visible Music College: cost_of_attendance
- Walters State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- Welch College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- William R Moore College of Technology: tuition_fees, admissions_tests, merit_scholarships
- Williamson Christian College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
