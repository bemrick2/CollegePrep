# Review queue — FL (2026-27)

Pages fetched: 5282; failures: 530. Candidates: 933 (433 without issues, 500 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 10 | 32 | 32 | 8 | 11 |
| cost_of_attendance | 0 | 0 | 6 | 23 | 44 | 9 | 11 |
| admissions_tests | 0 | 0 | 0 | 1 | 69 | 12 | 11 |
| common_data_set | 0 | 0 | 0 | 1 | 11 | 70 | 11 |
| merit_scholarships | 0 | 0 | 7 | 4 | 59 | 12 | 11 |
| ap_credit | 0 | 0 | 9 | 1 | 17 | 55 | 11 |
| clep_credit | 0 | 0 | 4 | 5 | 27 | 46 | 11 |
| ib_credit | 0 | 0 | 6 | 3 | 10 | 63 | 11 |
| dual_enrollment | 0 | 0 | 16 | 10 | 35 | 21 | 11 |
| transfer_credit | 0 | 0 | 10 | 2 | 56 | 14 | 11 |
| statewide_articulation | 0 | 0 | 0 | 0 | 31 | 51 | 11 |
| residency | 0 | 0 | 0 | 0 | 58 | 24 | 11 |
| degree_requirements | 0 | 0 | 0 | 0 | 62 | 20 | 11 |
| aid_appeals | 0 | 0 | 0 | 42 | 15 | 25 | 11 |

## Ready for review (433)

### `0fe5021f381c909d` AdventHealth University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.ahu.edu/tuition-and-aid/scholarships (sha256 36d62f89dfc5)
- checks: {"thresholds": null}
  - gpa_requirement: GPA Requirement: 3.01 to 3.4 ⟵ “3.01 to 3.4 | $1000/year”
  - award_amount_text: $1000/year ⟵ “3.01 to 3.4 | $1000/year”
### `5c9fa66b0b407224` AdventHealth University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.ahu.edu/tuition-and-aid/scholarships (sha256 36d62f89dfc5)
- checks: {"thresholds": null}
  - gpa_requirement: GPA Requirement: 3.76 or higher ⟵ “3.76 or higher | $3000/year”
  - award_amount_text: $3000/year ⟵ “3.76 or higher | $3000/year”
### `f6dc13665f41c76e` AdventHealth University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.ahu.edu/tuition-and-aid/scholarships (sha256 36d62f89dfc5)
- checks: {"thresholds": null}
  - gpa_requirement: GPA Requirement: 3.41 to 3.75 ⟵ “3.41 to 3.75 | $2000/year”
  - award_amount_text: $2000/year ⟵ “3.41 to 3.75 | $2000/year”
### `9aebe7a50f77c02d` AdventHealth University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ahu.edu/tuition-and-aid/cost-of-attendance (sha256 bd33dc97ab4b)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition and Fees: 22140 ⟵ “Tuition and Fees | $22,140 | $22,140 | $22,140”
  - off_campus_not_with_family:Books and Supplies: 3600 ⟵ “Books and Supplies | $3,600 | $3,600 | $3,600”
  - off_campus_not_with_family:Housing and Food (Living Expenses): 21228 ⟵ “Housing and Food (Living Expenses) | $21,228 | $13,728 | $13,728”
  - off_campus_not_with_family:Transportation: 5757 ⟵ “Transportation | $5,757 | $5,757 | $5,757”
  - off_campus_not_with_family:Personal: 1758 ⟵ “Personal | $1,758 | $1,758 | $1,758”
  - off_campus_not_with_family:Loan Fees: 96 ⟵ “Loan Fees | $96 | $96 | $96”
  - off_campus_not_with_family:Total Cost of Attendance: 54579 ⟵ “Total Cost of Attendance | $54,579 | $47,079 | $47,079”
  - on_campus:Tuition and Fees: 22140 ⟵ “Tuition and Fees | $22,140 | $22,140 | $22,140”
  - on_campus:Books and Supplies: 3600 ⟵ “Books and Supplies | $3,600 | $3,600 | $3,600”
  - on_campus:Housing and Food (Living Expenses): 13728 ⟵ “Housing and Food (Living Expenses) | $21,228 | $13,728 | $13,728”
  - on_campus:Transportation: 5757 ⟵ “Transportation | $5,757 | $5,757 | $5,757”
  - on_campus:Personal: 1758 ⟵ “Personal | $1,758 | $1,758 | $1,758”
  - on_campus:Loan Fees: 96 ⟵ “Loan Fees | $96 | $96 | $96”
  - on_campus:Total Cost of Attendance: 47079 ⟵ “Total Cost of Attendance | $54,579 | $47,079 | $47,079”
  - with_parents_or_family:Tuition and Fees: 22140 ⟵ “Tuition and Fees | $22,140 | $22,140 | $22,140”
  - with_parents_or_family:Books and Supplies: 3600 ⟵ “Books and Supplies | $3,600 | $3,600 | $3,600”
  - with_parents_or_family:Housing and Food (Living Expenses): 13728 ⟵ “Housing and Food (Living Expenses) | $21,228 | $13,728 | $13,728”
  - with_parents_or_family:Transportation: 5757 ⟵ “Transportation | $5,757 | $5,757 | $5,757”
  - with_parents_or_family:Personal: 1758 ⟵ “Personal | $1,758 | $1,758 | $1,758”
  - with_parents_or_family:Loan Fees: 96 ⟵ “Loan Fees | $96 | $96 | $96”
  - with_parents_or_family:Total Cost of Attendance: 47079 ⟵ “Total Cost of Attendance | $54,579 | $47,079 | $47,079”
### `0af92d40803671b5` Albizu University-Miami — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.albizu.edu/miami/admissions/ (sha256 56578d6de0d6)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Albizu University accepts transfer credits applicable to the student’s study program from a regionally accredited institution for courses in which a letter grade of “C” or higher was earned.”
### `294d33d06cd0b1fd` Ave Maria University — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.avemaria.edu/admissions/tuition-and-cost (sha256 9cf49064f0eb)
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 33200 ⟵ “Tuition | $16,600 | $16,600 | $33,200”
  - column:Fees: 1820 ⟵ “Fees | $910 | $910 | $1,820”
  - column:Tuition & Fees - Subtotal (excludes textbooks and lab fees): 35020 ⟵ “Tuition & Fees - Subtotal (excludes textbooks and lab fees) | $17,510 | $17,510 | $35,020”
### `e9d8d10926b882d6` Barry University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.barry.edu/en/financial-aid/undergraduate/ (sha256 0fd452ce48bd)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 12000 ⟵ “Tuition | $12,000”
  - on_campus:Books: 1848 ⟵ “Books | $1,848”
  - on_campus:Housing/Food: 3268 ⟵ “Housing/Food | $3,268”
  - on_campus:Personal Expenses: 5118 ⟵ “Personal Expenses | $5,118”
  - on_campus:Transportation: 2016 ⟵ “Transportation | $2,016”
  - on_campus:Student Services Fee: 1000 ⟵ “Student Services Fee | $1,000”
  - on_campus:Federal Loan Fees: 116 ⟵ “Federal Loan Fees | $116”
  - on_campus:Total COA: 25366 ⟵ “Total COA | $25,366”
### `007ff994ef91e79b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student seeing ASN and RN-BSN degrees 50% of the way through the degree program Minimum GPA 2.0 ⟵ “MedPro Future Nurse Scholarship | Student seeing ASN and RN-BSN degrees 50% of the way through the degree program Minimum GPA 2.0”
### `017a1efdecffa3f2` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Religion or Music Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 3.5 ⟵ “Tom Webb Memorial Scholarship | Religion or Music Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 3.5”
### `01cb07e95f206d57` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Environmental Science Full/Part-time student AA, AS, or BS degree Florida Resident Minimum GPA 2.50 Available to international students ⟵ “Michelle A. Lawless Environmental Scholarship | Environmental Science Full/Part-time student AA, AS, or BS degree Florida Resident Minimum GPA 2.50 Available to international students”
### `02dd21afcd5e88c3` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA: Health Sciences Demonstrate financial need as determined by the FAFSA application ⟵ “Health Foundation of South Florida Book/Supplies Scholarship | AA: Health Sciences Demonstrate financial need as determined by the FAFSA application”
### `02e39cf9efae2b70` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Hospitality majors Full or part-time Minimum GPA 2.0 International students may qualify ⟵ “James B. Fazio, Sr. Scholarship | Hospitality majors Full or part-time Minimum GPA 2.0 International students may qualify”
### `035e3c712a9738ac` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Honors College Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.5 International students may qualify ⟵ “Honors Institute Endowed Scholarship | Honors College Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.5 International students may qualify”
### `057d48afe5c75f2e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Enrolled in the following programs: Architecture, Civil Engineering, Mechanical Engineering, Electrical Engineering, Building Construction, Landscape Architecture, Interior Design Student must have at least 16 semester hours Broward County resident Applicants must submit a letter of recommendation from a non-family member Applicants must submit an essay indicating why they should be awarded the scholarship ⟵ “Construction Specifications Institute Endowed Scholarship | Enrolled in the following programs: Architecture, Civil Engineering, Mechanical Engineering, Electrical Engineering, Building Construction, Landscape Architecture, Interior Design Student must have at least 16 semester hours Broward County ”
### `0662a0ba3402996d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify (must have a student visa F1 status) Student must be a member of GSA on any campus, or a member of any other human rights organization ⟵ “Todd Stolfa Endowed Scholarship | Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify (must have a student visa F1 status) Student must be a member of GSA on any campus, or a member of any other human rights organization”
### `07fd3cabcca13811` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Demonstrate financial need as determined by the FAFSA application Broward/Miami-Dade County resident ⟵ “Sandra and Max Bleicher Memorial Nursing Scholarship | Nursing Demonstrate financial need as determined by the FAFSA application Broward/Miami-Dade County resident”
### `0856b09268165477` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application 2nd year Theater students ⟵ “Mary Edelstein Memorial Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application 2nd year Theater students”
### `08692f139274b8e3` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major Full or part-time Demonstrate financial need as determined by the FAFSA application Broward County resident ⟵ “Berthola Rasmussen Endowed Scholarship | Any major Full or part-time Demonstrate financial need as determined by the FAFSA application Broward County resident”
### `0a28a6ca4ecc9ec1` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.5 Classified as Head of Household Broward County resident ⟵ “Zonta Club of Greater Deerfield Beach Scholarship | Full or part-time Minimum GPA 2.5 Classified as Head of Household Broward County resident”
### `0ad137376bd4b303` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 ⟵ “Steven R. Berrard Endowed Scholarship | Full or part-time Minimum GPA 2.0”
### `0ad7dba18c0125d3` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.0 ⟵ “Angelo and Diane Gencarelli Scholarship | Any major Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.0”
### `0b640a26f847ef9a` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Charles & Marguerite Cave Endowed Scholarship | Any major Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `0b9f85f2e47bdd7d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA & AS Non-degree students taking vocational courses Full or part-time Minimum GPA 2.0 Broward County resident only ⟵ “Dr. James L. & Sylvia W. Burnstead Endowed Scholarship | AA & AS Non-degree students taking vocational courses Full or part-time Minimum GPA 2.0 Broward County resident only”
### `0c92bd5c58129d4c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Sciences (preference for Environmental Science) Florida Resident Minimum GPA 2.50 Demonstrate financial need as determined by the FAFSA application Must have completed a minimum of one college semester Applicants must complete a one-page essay on why they chose to major in one of the sciences Applicants must present documentation verifying at least 50 hours of environmental services in the community or at Broward College. Available to international students ⟵ “Michelle A. Lawless Environmental Endowed Scholarship | Sciences (preference for Environmental Science) Florida Resident Minimum GPA 2.50 Demonstrate financial need as determined by the FAFSA application Must have completed a minimum of one college semester Applicants must complete a one-page essay ”
### `0ccbb6ddfe6346f0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Criminal Justice Demonstrate financial need as determined by the FAFSA application Broward County HS graduate Minimum 2.75 HS or BC GPA First preference for a student from the Wilton Manors community (e.g., ZIP codes 33305, 33306, 33311, or 33334) ⟵ “Kiwanis Club of Wilton Manors Honors Buster Barton & Ed Miller Scholarship | Criminal Justice Demonstrate financial need as determined by the FAFSA application Broward County HS graduate Minimum 2.75 HS or BC GPA First preference for a student from the Wilton Manors community (e.g., ZIP codes 33305,”
### `100881b354a70cc8` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify (must have a student visa F1 status) Student must have an interest in Hispanic culture ⟵ “Hollywood Beach Latin Festival Endowed Scholarship | Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify (must have a student visa F1 status) Student must have an interest in Hispanic culture”
### `114e9f9f24b5b94d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full-time Central campus theater student Award based on talent and commitment Minimum GPA 2.5 ⟵ “Mildred Bailey Mullikin Endowed Scholarship | Full-time Central campus theater student Award based on talent and commitment Minimum GPA 2.5”
### `123043625aa210ae` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Available to international students ⟵ “Elmer Rasmuson Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Available to international students”
### `12718b133643b593` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Information Technology Merit-based (scholarship based on academic achievement) Full-time Minimum GPA 3.0 US citizen ⟵ “Jeremy David Buford Memorial Scholarship | Information Technology Merit-based (scholarship based on academic achievement) Full-time Minimum GPA 3.0 US citizen”
### `13849524efb59715` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA, AS Minimum GPA 2.5 ⟵ “Dr. Philip Benjamin Academic Improvement Endowment | AA, AS Minimum GPA 2.5”
### `145ff4df41823e31` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Area of study: Paralegal Demonstrate financial need as determined by FAFSA application Part-time Minimum GPA 3.0 ⟵ “The Lois Ketenheim White Endowed Scholarship | Area of study: Paralegal Demonstrate financial need as determined by FAFSA application Part-time Minimum GPA 3.0”
### `14f7df93167966b3` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA & AS Degrees Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Broward County resident US Citizen Priority for foster children ⟵ “Children's Opportunity Group Endowed Scholarship | AA & AS Degrees Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Broward County resident US Citizen Priority for foster children”
### `1608534812560163` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Music Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Student must be a resident of Florida ⟵ “Anderson Estate Endowed Scholarship | Music Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Student must be a resident of Florida”
### `16a961e41452d7d6` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Classified as head of household Not entering college directly from high school ⟵ “Willis Holcombe Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Classified as head of household Not entering college directly from high school”
### `1937e4a090f57264` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: First preference is the Environmental Sciences Program Second preference is the Hospitality Program ⟵ “Alan Mortimer Memorial Endowed Scholarship | First preference is the Environmental Sciences Program Second preference is the Hospitality Program”
### `19e7d839fcf1b644` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must be attending Central Campus Student must be or have previously enrolled in a class in social sciences Open to international students ⟵ “Handleman Family Memorial Endowed Scholarship | Student must be attending Central Campus Student must be or have previously enrolled in a class in social sciences Open to international students”
### `1b1cf6fe9d4fddd1` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: BS Math Education Full or part-time ⟵ “Abraham K. Biggs, Jr. Memorial Endowed Scholarship | BS Math Education Full or part-time”
### `1b70abf34955a24d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing 10 credits or more Student referrals provided by the Nursing Department ⟵ “Adopt-A-Nurse Program | Nursing 10 credits or more Student referrals provided by the Nursing Department”
### `1bd24bed739e9cdc` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Pursuing a degree or certification at North Campus Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 The Leadership Committee of North Campus will select a student to receive the award ⟵ “North Campus President's Fund for Academic Affairs, Student | Pursuing a degree or certification at North Campus Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 The Leadership Committee of North Campus will select a student to receive the award”
### `1c1437f29a52e9a8` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Bachelor of Science in Education Demonstrate financial need as determined by the FAFSA application Service learning must be part of the curriculum Minimum GPA 2.5 ⟵ “Dana, Charley and Margot Fund | Bachelor of Science in Education Demonstrate financial need as determined by the FAFSA application Service learning must be part of the curriculum Minimum GPA 2.5”
### `1d2aa550844cc94b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Student must take: PHI2600, JST1700, EUH2033, SYG2010, JST1500, JST2400, JST2815, REL2300, SYG1931C, SYG2441, or IDH2408 ⟵ “Norma R. Sonnenklar Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Student must take: PHI2600, JST1700, EUH2033, SYG2010, JST1500, JST2400, JST2815, REL2300, SYG1931C, SYG2441, or IDH2408”
### `1f8c30f8bf3fbe39` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA or AS degree Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 3.0 ⟵ “Dr. Halina Adamska Memorial Endowed Scholarship | AA or AS degree Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 3.0”
### `1fb2bd7910aa5bae` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Science or Aviation Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 ⟵ “David Mann Memorial Science Scholarship | Health Science or Aviation Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5”
### `23322b2557c4b52b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Music majors Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Dr. Ruth L. Schmidt Endowed Music Scholarship | Music majors Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `24509a9f01f8638a` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Area of Study: Teaching Merit-based (scholarship based on academic achievement) Full-time Minimum 3.3 GPA Broward County resident Associate and Baccalaureate programs ⟵ “Margaret T. Tait Endowed Teaching Scholarship | Area of Study: Teaching Merit-based (scholarship based on academic achievement) Full-time Minimum 3.3 GPA Broward County resident Associate and Baccalaureate programs”
### `245a19dd36758f1d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Architecture Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify ⟵ “Gresham, Smith & Partners Endowed Scholarship | Architecture Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify”
### `24763a5ec692e5c0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Theatre majors Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 ⟵ “Lambertus Endowed Scholarship | Theatre majors Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0”
### `24f916ff513d701c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Jennifer H. Maurer Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `2520d15147f4facc` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing students in the AS LPN, AS RN, BS, RN to BSN Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5 ⟵ “Sara & Romeyne Klingensmith Memorial Nursing Endowed Scholar | Nursing students in the AS LPN, AS RN, BS, RN to BSN Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5”
### `25dce7b77982ac3d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Greatness in Making (GIM) members; students must upload a letter of eligibility provided by the GIM faculty advisor Full or part-time Minimum GPA 2.5 ⟵ “Dr. Bunny Hedrick Endowed Scholarship | Greatness in Making (GIM) members; students must upload a letter of eligibility provided by the GIM faculty advisor Full or part-time Minimum GPA 2.5”
### `2b0d4dd288e51a4b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing or Health Science Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Florida resident ⟵ “Florida Blue Nursing Scholarship | Nursing or Health Science Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Florida resident”
### `2b1ae75291159e53` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major Employees of Bank of Atlantic are not eligible ⟵ “BankAtlantic Foundation Endowed Scholarship | Any major Employees of Bank of Atlantic are not eligible”
### `2b4dc1762c3db607` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major ⟵ “Blosser Family Endowed Scholarship | Any major”
### `2d4df9be4ffa6c6e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Building Construction Technology, Architecture, Engineering Demonstrate financial need as determined by the FAFSA application Full-time Broward County resident ⟵ “Tom & Julie Carney Endowed Scholarship | Building Construction Technology, Architecture, Engineering Demonstrate financial need as determined by the FAFSA application Full-time Broward County resident”
### `2ee20b47bf90f58b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Registered in the RN to BSN Nursing program Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 US citizen Florida resident ⟵ “Lessie Pryor RN to BSN Endowed Memorial Scholarship | Registered in the RN to BSN Nursing program Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 US citizen Florida resident”
### `30018376c3fbcc0f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Second year Nursing student Preferably attending South Campus Recommended by the Dean of Nursing ⟵ “The Justice Family Endowed Memorial Scholarship Fund | Second year Nursing student Preferably attending South Campus Recommended by the Dean of Nursing”
### `300413f66b8c9cf0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Science or Aviation majors Minimum GPA 2.5 ⟵ “AT&T Endowed Scholarship (BELLSOUTH TELECOMMUNICATIONS) | Health Science or Aviation majors Minimum GPA 2.5”
### `31232f1a9ded62cb` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Education majors Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5 ⟵ “Veazy Holt Memorial Endowed Scholarship | Education majors Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5”
### `356f9d535b478fcb` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA, AS, BS Demonstrate financial need as determined by the FAFSA application Full-time student Student must be a member of DECA ⟵ “Richard Goodwin Memorial Endowed Scholarship | AA, AS, BS Demonstrate financial need as determined by the FAFSA application Full-time student Student must be a member of DECA”
### `36d8dd9ee2da52f2` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Science Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 ⟵ “Broad & Cassel Endowed Health Science Scholarship | Health Science Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0”
### `37d5d2fb458cdef5` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major Minimum GPA 2.0 Handy membership verification required Available to international students ⟵ “HANDY Inc. Scholarship Fund | Any major Minimum GPA 2.0 Handy membership verification required Available to international students”
### `38496d3fdebb5417` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Science pathway Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Kindred Healthcare Sponsorship | Health Science pathway Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `393764d9410a3314` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Science Demonstrate financial need as determined by the FAFSA application Part-time ⟵ “Fred Deal Memorial Endowed Scholarship | Health Science Demonstrate financial need as determined by the FAFSA application Part-time”
### `395369681746d383` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Aviation Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Ursula Davidson Endowed Scholarship | Aviation Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `3a6e791aad3bc00f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must be enrolled in the Ceramics course on Central campus Full or part-time Minimum GPA 2.0 Available to international students ⟵ “Alice Werbel Memorial Endowment | Student must be enrolled in the Ceramics course on Central campus Full or part-time Minimum GPA 2.0 Available to international students”
### `3b88ccf7b6e4c395` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time ⟵ “Judith Bowen Endowed Scholarship | Full or part-time”
### `3ca5a77a34a41843` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Music students Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Carl and Pearlie Crawford Endowed Scholarship | Music students Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `3d6f036d31774258` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Referred by the SFUYSA association Merit-based (scholarship based on academic achievement) ⟵ “SFUYSA Michael W. Weber Memorial Referee Annual Scholarship | Referred by the SFUYSA association Merit-based (scholarship based on academic achievement)”
### `3eb3625665e5bddf` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Behavioral Sciences Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 ⟵ “Dr. Stephen Barker Memorial Endowed Scholarship | Behavioral Sciences Merit-based (scholarship based on academic achievement) Minimum GPA 3.0”
### `3f9f2f7caed3bcc5` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.0 Not entering college directly from high school ⟵ “Debra Levy Neimark Memorial Scholarship | Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.0 Not entering college directly from high school”
### `4157244c60aaa374` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Referred by the SFUYSA association Merit-based (scholarship based on academic achievement) ⟵ “SFUYSA Player Annual Scholarship | Referred by the SFUYSA association Merit-based (scholarship based on academic achievement)”
### `4221d952f34dbcca` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Broward College Memorial Scholarship | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `434b3ae850b8f591` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Pre-Med, Life Sciences, Environmental Sciences Demonstrate financial need as determined by the FAFSA application Merit-based (scholarship based on academic achievement) Full time Minimum GPA 3.0 Broward County resident US Citizen ⟵ “George and Jean Trebbi Endowed Scholarship | Pre-Med, Life Sciences, Environmental Sciences Demonstrate financial need as determined by the FAFSA application Merit-based (scholarship based on academic achievement) Full time Minimum GPA 3.0 Broward County resident US Citizen”
### `434bdc4242df6dd4` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Demonstrate financial need as determined by the FAFSA application Preference given to RN to BSN students ⟵ “Dr. Susan B. Hassmiller Nursing Scholarship | Nursing Demonstrate financial need as determined by the FAFSA application Preference given to RN to BSN students”
### `43a60e2db3ba0e2e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major Minimum GPA 2.0 ⟵ “Edward Seese AITF Endowed Scholarship | Any major Minimum GPA 2.0”
### `445a610c8f807854` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 Available to international students ⟵ “AVMED Endowed Scholarship | Full or part-time Minimum GPA 2.0 Available to international students”
### `44e0c9c573e5823f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Sciences program Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 ⟵ “Dr. Wanda Thomas Health Science Endowed Scholarship | Health Sciences program Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0”
### `45784c04ffc63bb0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Available to international students Minimum 2.5 GPA Student must have an interest in promoting and engaging in Venezuelan culture ⟵ “Fazzano Ficano Scholarship Fund | Available to international students Minimum 2.5 GPA Student must have an interest in promoting and engaging in Venezuelan culture”
### `45cef3d7994b008e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Preference for Business majors Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 Students who have participated in community service in the past two years ⟵ “Berson Levinson Community Service Scholarship | Preference for Business majors Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 Students who have participated in community service in the past two years”
### `47524a34707abd93` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Aviation Maintenance Management Merit-based (scholarship based on academic achievement) Full or part-time Live in the tri-county area Minimum GPA 3.0 ⟵ “SFAMC Aviation Maintenance Scholarship | Aviation Maintenance Management Merit-based (scholarship based on academic achievement) Full or part-time Live in the tri-county area Minimum GPA 3.0”
### `4983428f8afdf7ed` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: First generation in college Full or part-time Minimum GPA 2.0 Recipients must write a thank-you letter to Bank of America and send it to BC Foundation ⟵ “Bank of America Dream Makers Scholarship | First generation in college Full or part-time Minimum GPA 2.0 Recipients must write a thank-you letter to Bank of America and send it to BC Foundation”
### `49e985d146ff8cfd` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.5 ⟵ “Frances Tyler Reina Memorial Endowed Scholarship | Full or part-time Minimum GPA 2.5”
### `49fb2a4c3239a88d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA, AS, AAS: Pre-Med, Business, Health Sciences Merit-based, Need-based - either or both Full or part-time Minimum GPA 2.5 ⟵ “The Jeanette Tilles and Samuel Tilles, M.D. Memorial Endowed | AA, AS, AAS: Pre-Med, Business, Health Sciences Merit-based, Need-based - either or both Full or part-time Minimum GPA 2.5”
### `4a0760364ce77810` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing RN program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Kathryn Krause Scholarship for Nurses Endowment | Nursing RN program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `4b3e44d335869ae9` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AS & AAS Degrees Minimum GPA 2.0 Preference for Automotive students ⟵ “James Craney Automotive Scholarship | AS & AAS Degrees Minimum GPA 2.0 Preference for Automotive students”
### `4d2bd1b6275e2986` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Referred by the Nursing and Allied Health Dept. To assist with supplies ⟵ “Deans' Student Success Fund | Referred by the Nursing and Allied Health Dept. To assist with supplies”
### `4d4a323814a1eda1` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Minimum GPA 2.0 ⟵ “Edward Seese Endowed Scholarship | Minimum GPA 2.0”
### `4fd56dd4cbe87dc9` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Community service Florida resident only ⟵ “Ethics in Business Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Community service Florida resident only”
### `50289140c738599c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must be a dependent of a deceased or disabled law enforcement officer, firefighter, or peace officer Dependents of living law enforcement officers, firefighters, or peace officers Dependents of a Veteran killed in the line of duty Full or part-time Minimum GPA 2.0 ⟵ “Hundred Club Endowed Scholarship | Student must be a dependent of a deceased or disabled law enforcement officer, firefighter, or peace officer Dependents of living law enforcement officers, firefighters, or peace officers Dependents of a Veteran killed in the line of duty Full or part-time Minimum ”
### `50996a7baa11cbda` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Social and Behavioral Science Full or part-time Minimum GPA 2.5 ⟵ “Dr. Nagel & Professor Bryant Memorial Scholarship | Social and Behavioral Science Full or part-time Minimum GPA 2.5”
### `52214c6a7dd7f67a` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Graduates of Broward County High Schools Full-time Minimum 2.0 GPA ⟵ “James F. Minnet Memorial Scholarship | Demonstrate financial need as determined by the FAFSA application Graduates of Broward County High Schools Full-time Minimum 2.0 GPA”
### `5338ef86930561a6` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Professional Pilot Demonstrate financial need as determined by the FAFSA application Full-time or 3/4 time Minimum GPA 3.0 ⟵ “Paul Rose Memorial Endowed Scholarship | Professional Pilot Demonstrate financial need as determined by the FAFSA application Full-time or 3/4 time Minimum GPA 3.0”
### `5384eb8a9ffa4ab5` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 International students may be eligible ⟵ “J. Paul and Beulah Lee Peek Memorial Endowed Scholarship | Full or part-time Minimum GPA 2.0 International students may be eligible”
### `5406e83cfec4b378` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must be the son or daughter of a Broward County Police Officer Full-time ⟵ “Wm. H. Van Keuren Memorial Police Endowed Scholarship | Student must be the son or daughter of a Broward County Police Officer Full-time”
### `57a0c85ae69c79db` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Minimum GPA 2.5 Full or part-time ⟵ “Stiles Corporation Endowed Scholarship | Minimum GPA 2.5 Full or part-time”
### `58e7dbdf3b6bec3e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA or AS Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Heminger Family Endowed Scholarship | AA or AS Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `591ff2dc174832f6` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Part-time Minimum GPA 2.5 Graduates of the Salvation Army rehabilitation program/Transitional Housing program ⟵ “Major Ron Busroe Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Part-time Minimum GPA 2.5 Graduates of the Salvation Army rehabilitation program/Transitional Housing program”
### `596a73ef183da47e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Jeffrey D. & Nancy Hulmes Memorial Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `59c887f429b19079` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Aviation, must demonstrate a pilot's license Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Sherri Poel Memorial Endowed Scholarship | Aviation, must demonstrate a pilot's license Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `5a0e2de210e5d0f1` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must be taking an English class Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “John J. Czyzak Endowed Scholarship | Student must be taking an English class Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `5a5304570a4ffbae` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Child of an incarcerated parent U.S. Citizen Live in the tri-county area ⟵ “Nnamdi Richard Louis Memorial Fund | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Child of an incarcerated parent U.S. Citizen Live in the tri-county area”
### `5ac3ee7a33f81d21` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5 ⟵ “Nursing Scholarship | Nursing Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5”
### `5ae964efe9ed148b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Honor's College student ⟵ “Robert Elmore Honors Part-Time Endowed Scholarship | Honor's College student”
### `5c6159a28b864727` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student pursuing a teaching career Demonstrate financial need as determined by the FAFSA application Full or part-time student Minimum GPA 2.5 ⟵ “Dr. E. Ann McGee Endowed Scholarship in Teaching | Student pursuing a teaching career Demonstrate financial need as determined by the FAFSA application Full or part-time student Minimum GPA 2.5”
### `5c76d0195e8120f2` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Martin J & Sylvia K Yohalem Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `5c8bdc2f637ea946` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Demonstrate financial need as determined by the FAFSA application Full or Part-time Minimum GPA 2.5 ⟵ “Adeline Vanditti Memorial Endowed Scholarship | Nursing Demonstrate financial need as determined by the FAFSA application Full or Part-time Minimum GPA 2.5”
### `5d6d27682094013d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Students pursuing a degree in Music or the Pilot Training Program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Stanley B. and Eileen M. Burns Family Fund at the Community | Students pursuing a degree in Music or the Pilot Training Program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `5e364e6c59d835e0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/bright-futures.html (sha256 5468ffaad049)
- checks: {"thresholds": null}
  - gpa_requirement: 3.00 cumulative GPA ⟵ “Florida Academic Scholars (FAS) | 3.00 cumulative GPA”
### `5e6fc3cb82a2168f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Demonstrate financial need as determined by the FAFSA application ⟵ “Broward Endowed Scholarship | Full or part-time Demonstrate financial need as determined by the FAFSA application”
### `5e9e57b3a368b995` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/bright-futures.html (sha256 5468ffaad049)
- checks: {"thresholds": null}
  - award_amount_text: 12+9=21 ⟵ “n/a | Three-Quarter Time | 12+9=21”
### `5f5c7495d6fa5f01` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Reva Daniels Metzinger Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `6016743fb9c7deb0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.0 Member of Student Government or Honors College Broward County resident International students may qualify (must have a student visa F1 status) ⟵ “Diana Wasserman-Rubin Endowed Scholarship | Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.0 Member of Student Government or Honors College Broward County resident International students may qualify (must have a student visa F1 status)”
### `60d9570f7d19f251` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Broward County resident Full or part-time Demonstrate financial need as determined by the FAFSA application Preference for a student from Guardian Ad Litem or HANDY ⟵ “Bridge Scholarship Endowment | Broward County resident Full or part-time Demonstrate financial need as determined by the FAFSA application Preference for a student from Guardian Ad Litem or HANDY”
### `611bd89e7f2016d8` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA or AS Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 Students who participate in Brain Bowl, are members of Phi Theta Kappa, or are members of the Honors College International students may qualify (must have a student visa F1 status) ⟵ “Home Savings Association Endowed Scholarship | AA or AS Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 Students who participate in Brain Bowl, are members of Phi Theta Kappa, or are members of the Honors College International students may qualify (must have a student visa F1”
### `61744b4b10588fa0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Science pathway Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “HCA Healthcare Corporation of America Scholarship | Health Science pathway Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `62d0f1faf80d7f46` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 3.0 ⟵ “Greater Ft. Lauderdale Heart Group Endowed Scholarship | Full or part-time Minimum GPA 3.0”
### `630b11c47a8e6bff` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/bright-futures.html (sha256 5468ffaad049)
- checks: {"thresholds": null}
  - award_amount_text: 6+12=18 ⟵ “Half-time (6-8) | Full-Time | 6+12=18”
### `6365e9aaccae662a` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Criminal Justice program Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Joseph Fink Memorial Endowed Scholarship | Criminal Justice program Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `64424588a77bd11d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.5 Preference for Physical Therapy ⟵ “Tim Robinson Endowed Scholarship in Physical Therapy | Full or part-time Minimum GPA 2.5 Preference for Physical Therapy”
### `64d420d4e4e18c0e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify (must have a student visa F1 status) ⟵ “North Ridge Medical Center Auxiliary Endowed Scholarship | Nursing Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify (must have a student visa F1 status)”
### `64db8be894ac4258` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AS or AAS degree-seeking Demonstrate financial need as determined by the FAFSA application Minimum 2.0 GPA ⟵ “Janet Sturdy Endowment Scholarship | AS or AAS degree-seeking Demonstrate financial need as determined by the FAFSA application Minimum 2.0 GPA”
### `65ca43b34c8fac31` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must be a dependent of a firefighter or EMT in Broward County ⟵ “Steve J. Parker Endowed Scholarship Fund | Student must be a dependent of a firefighter or EMT in Broward County”
### `66ac48078fdef0df` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must be enrolled in at least one Dance course Full or part-time Minimum GPA 2.5 Students referred by the Dance Department Available to international students ⟵ “Talamo-Mosquera Dance Scholarship | Student must be enrolled in at least one Dance course Full or part-time Minimum GPA 2.5 Students referred by the Dance Department Available to international students”
### `671e8a2e4ccc658a` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/bright-futures.html (sha256 5468ffaad049)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 cumulative GPA ⟵ “Florida Gold Seal Vocational Scholars (GSV/GSC) | 2.75 cumulative GPA”
### `67ca4148192aa809` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Students accepted to the Nursing program with a minimum 3.0 GPA Student will sign a letter of intent to work in Miami-Dade, Broward, or Monroe counties for at least a year ⟵ “Health Foundation of South Florida Scholarship | Demonstrate financial need as determined by the FAFSA application Students accepted to the Nursing program with a minimum 3.0 GPA Student will sign a letter of intent to work in Miami-Dade, Broward, or Monroe counties for at least a year”
### `68e83c1518792a4b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must be a participant/resident in a community/state-sponsored resident or rehabilitative program Full or part-time Minimum GPA 2.5 ⟵ “Rotary Club Ft. Lauderdale South Endowed Scholarship | Student must be a participant/resident in a community/state-sponsored resident or rehabilitative program Full or part-time Minimum GPA 2.5”
### `6a05cf48b21fd184` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.25 Student must be first-generation in their family to attend college Student must be listed as the head of household ⟵ “Marissa D. Kelley Endowed Scholarship | Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.25 Student must be first-generation in their family to attend college Student must be listed as the head of household”
### `6a0c726155b313a6` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Enrolled in a degree-seeking program on South campus Full or part-time Minimum GPA 3.0 Graduate of either South Broward HS, Hollywood Hill HS, or McArthur HS Available to international students ⟵ “G.W. "Bill" McCall Endowed Scholarship | Merit-based (scholarship based on academic achievement) Enrolled in a degree-seeking program on South campus Full or part-time Minimum GPA 3.0 Graduate of either South Broward HS, Hollywood Hill HS, or McArthur HS Available to international students”
### `6bd7621b281c3cba` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 ⟵ “Senator Jim Scott Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0”
### `6c6450a035f7287e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 Full or part-time AA must be taking the ENC course South campus Broward County resident ⟵ “Robine Eniece Gray Memorial Scholarship | Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 Full or part-time AA must be taking the ENC course South campus Broward County resident”
### `6c68ca54ece2d99a` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Teacher Education Program (TEP) Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 ⟵ “TITLE V CO-OP Central Endowment | Teacher Education Program (TEP) Merit-based (scholarship based on academic achievement) Minimum GPA 3.0”
### `6c798845e224bdb6` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Referred by the SFUYSA association Merit-based (scholarship based on academic achievement) ⟵ “SFUYSA Mike Weber Memorial Endowed Scholarship | Referred by the SFUYSA association Merit-based (scholarship based on academic achievement)”
### `6df2aad70d5a1fe2` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Science/Nursing degree Full-time Minimum GPA 2.0 Student must submit a thank-you letter before being awarded the scholarship ⟵ “Elaine P. Krupnick Endowed Scholarship Fund | Health Science/Nursing degree Full-time Minimum GPA 2.0 Student must submit a thank-you letter before being awarded the scholarship”
### `6e5bc2cba1defaf9` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “George & Virginia Young Memorial Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `6f372e2e5c587a30` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: North campus students Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 First Generation Broward County resident ⟵ “Dr. Leonard Bryant, Jr. Student Success Endowed Scholarship | North campus students Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 First Generation Broward County resident”
### `6fc95032f49dbc41` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.0 Preference for a Junior or Senior majoring in Math Education or Science Education ⟵ “Mr. & Mrs. Moore C. Perfect Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.0 Preference for a Junior or Senior majoring in Math Education or Science Education”
### `70e76c918d002301` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Marine Engineering Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Pantropic Power/Caterpillar Marine Excellence Scholarship | Marine Engineering Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `7122504d2825ace0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Broward County resident ⟵ “Esther Barron Memorial Nursing Scholarship | Nursing Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Broward County resident”
### `72af2337089570f4` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.5 Available to international students ⟵ “James B. and Lynn LaBate Endowed Scholarship | Full or part-time Minimum GPA 2.5 Available to international students”
### `743b70c9c6597a60` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 ⟵ “David R. Pacini Memorial Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5”
### `743d1470adc46187` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Education major Full or part-time Minimum GPA 3.2 ⟵ “Andrea Mays Memorial Endowed Scholarship | Education major Full or part-time Minimum GPA 3.2”
### `745587647e12b71f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Teacher Education Program (TEP) Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 ⟵ “TITLE V CO-OP South Endowment | Teacher Education Program (TEP) Merit-based (scholarship based on academic achievement) Minimum GPA 3.0”
### `757d7ec60760aa63` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Educating Black Boys (EBB-FLOW) and Fostering Learning Opportunity | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `764b75fb3d3e49c5` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Referred by the SFUYSA association Merit-based (scholarship based on academic achievement) ⟵ “SFUYSA Player Endowed Scholarship | Referred by the SFUYSA association Merit-based (scholarship based on academic achievement)”
### `76cd5a0fd21d9b1b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major Degree seeking Demonstrate financial need as determined by the FAFSA application ⟵ “Arthur and Bertha Lezar Endowed Scholarship | Any major Degree seeking Demonstrate financial need as determined by the FAFSA application”
### `76fa412981ebc041` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.5 International students may qualify BC Honors student who has earned the Honors Institute Certificate Must have demonstrated leadership/service in Honors, Phi Theta Kappa or other student organization or club at BC Must be a BC candidate for graduation in May who is transferring to a college or university, preferably in Florida ⟵ “Robert F. Bocchino Family Scholarship | Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.5 International students may qualify BC Honors student who has earned the Honors Institute Certificate Must have demonstrated leadership/service in Honors, Phi Theta Kappa ”
### `7701092b42209745` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA Scholarship is restricted to individuals who have participated in Broward UP Enrolled in a Health Science degree program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Health Foundation of South Florida Broward UP Scholarship | AA Scholarship is restricted to individuals who have participated in Broward UP Enrolled in a Health Science degree program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `776055baec3fd9eb` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 Demonstrate financial need as determined by the FAFSA application The award is for students to use to purchase books at the campus Barnes & Noble bookstores Available to international students ⟵ “The Barnes & Noble Book Awards | Full or part-time Minimum GPA 2.0 Demonstrate financial need as determined by the FAFSA application The award is for students to use to purchase books at the campus Barnes & Noble bookstores Available to international students”
### `776a2647c3a53900` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA students seeking a 4-year degree Demonstrate financial need as determined by the FAFSA application Full or part-time Preference is that the student maintain a 3.0 GPA ⟵ “Betty & David Owen Endowed Scholarship | AA students seeking a 4-year degree Demonstrate financial need as determined by the FAFSA application Full or part-time Preference is that the student maintain a 3.0 GPA”
### `7793af66d7cafeb7` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Teacher Education Program (TEP) Minimum GPA 2.5 ⟵ “Barbara Evertz Memorial Endowed Scholarship | Teacher Education Program (TEP) Minimum GPA 2.5”
### `77a579db14fe8027` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 ⟵ “Mentor Program Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0”
### `77bae4003ec44073` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 Preference for students recovering from drug or alcohol abuse, or who come from a family where there has been a presence of drug or alcohol abuse ⟵ “Joyce B. Cross Endowed Scholarship | Full or part-time Minimum GPA 2.0 Preference for students recovering from drug or alcohol abuse, or who come from a family where there has been a presence of drug or alcohol abuse”
### `78618fd54785502c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must have participated in HANDY, Boys & Girls Club, or other at-risk programs Demonstrate financial need as determined by the FAFSA application ⟵ “Mr. and Mrs. Gregory and Chae Haile Scholarship | Student must have participated in HANDY, Boys & Girls Club, or other at-risk programs Demonstrate financial need as determined by the FAFSA application”
### `7ade51c27265e968` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-timeMinimum GPA 2.0 Classified as Head of Household Broward County resident ⟵ “Broward County Women's History Coalition Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-timeMinimum GPA 2.0 Classified as Head of Household Broward County resident”
### `7c1e4dcb72f21919` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit based Minimum 3.25 GPA Full-time or Part-time Degree seeking Member of the Honors Institute and/or PTK Available to international students ⟵ “Cynthia Roberts Memorial Endowed Scholarship | Merit based Minimum 3.25 GPA Full-time or Part-time Degree seeking Member of the Honors Institute and/or PTK Available to international students”
### `7c2b7dd306abc858` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Paramedic/EMT Demonstrate financial need as determined by the FAFSA application Broward County HS graduate Minimum 2.75 HS or BC GPA First preference for a student from the Wilton Manors community (e.g., ZIP codes 33305, 33306, 33311, or 33334) ⟵ “Kiwanis Club of Wilton Manors Honors David Platz & Randy Comer Scholarship | Paramedic/EMT Demonstrate financial need as determined by the FAFSA application Broward County HS graduate Minimum 2.75 HS or BC GPA First preference for a student from the Wilton Manors community (e.g., ZIP codes 33305, 33”
### `7e296389f6319f3f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 Broward County resident ⟵ “Vince Bryant Memorial Endowed Scholarship | Full or part-time Minimum GPA 2.0 Broward County resident”
### `807bdab6f6aba37f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Dental Hygiene or Dental Assistant program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Broward Dental Research Fund | Dental Hygiene or Dental Assistant program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `815eb457961997c3` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Aviation Maintenance Full-time Demonstrate financial need as determined by the FAFSA application ⟵ “Broward College Aviation Maintenance Faculty Scholarship | Aviation Maintenance Full-time Demonstrate financial need as determined by the FAFSA application”
### `816109cc5b4b4163` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Student serving in a human services organization in Broward County ⟵ “Jon Harris Maurer Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Student serving in a human services organization in Broward County”
### `844449622558407d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 ⟵ “Elinor Wilkov Endowed Scholarship | Full or part-time Minimum GPA 2.0”
### `8478f7bc34f077c5` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 ⟵ “Edward Seese Memorial Scholarship Fund | Full or part-time Minimum GPA 2.0”
### `848174ea570da2b9` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Theatre Full or part-time Minimum GPA 2.5 ⟵ “Richard Hinners Memorial Endowed Scholarship | Theatre Full or part-time Minimum GPA 2.5”
### `860e7e56795bc243` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Full or part-time Minimum GPA 2.0 ⟵ “Harriet Steinman Endowed Nursing Scholarship | Nursing Full or part-time Minimum GPA 2.0”
### `86c7037c61a80a48` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Pepsi-Cola Bottling Co. Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `8732270d69ec5727` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: All AA or AS in Aviation, Journalism, or Health Sciences Member of Boys & Girls Club Full or part-time Minimum GPA 2.5 ⟵ “Marti Huizenga Endowed Scholarship | All AA or AS in Aviation, Journalism, or Health Sciences Member of Boys & Girls Club Full or part-time Minimum GPA 2.5”
### `8830c63980bcbb2f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA, AS, AAS or Certificate Programs Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Leo Goodwin Foundation Endowed Scholarship | AA, AS, AAS or Certificate Programs Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `8899cd4d3658353f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Members of GSA Full or part-time Minimum GPA 2.5 ⟵ “BC Pride Scholarship | Members of GSA Full or part-time Minimum GPA 2.5”
### `88f0c8fd64c4f859` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Full-time ⟵ “Gertrude E. Skelly Memorial Nursing Emergency Scholarship | Nursing Full-time”
### `896010532972fd62` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/bright-futures.html (sha256 5468ffaad049)
- checks: {"thresholds": null}
  - award_amount_text: 9+12=21 ⟵ “Three Quarter time (9-11) | Full-Time | 9+12=21”
### `8cb7a3dcccaa7e16` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Degree seeking Enrolled in fall and spring terms Enrolled in a minimum of 3 credits Must complete FAFSA International students are not eligible ⟵ “General Scholarship | Demonstrate financial need as determined by the FAFSA application Degree seeking Enrolled in fall and spring terms Enrolled in a minimum of 3 credits Must complete FAFSA International students are not eligible”
### `8d5727499f364a96` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 3.0 Broward County resident ⟵ “Thomas F. Maurer Endowed Scholarship | Full or part-time Minimum GPA 3.0 Broward County resident”
### `8e7cdf090155cad0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Enrolled in a Health Science program Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum 2.0 GPA ⟵ “Fischley Health Challenge Scholarship | Enrolled in a Health Science program Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum 2.0 GPA”
### `9081ae9f1f69ce50` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Demonstrate financial need as determined by the FAFSA application Broward County HS graduate Minimum 2.75 HS or BC GPA First preference for a student from the Wilton Manors community (e.g., ZIP codes 33305, 33306, 33311, or 33334) ⟵ “Kiwanis Club of Wilton Manors Honors James Dean & Jim Carroll Scholarship | Nursing Demonstrate financial need as determined by the FAFSA application Broward County HS graduate Minimum 2.75 HS or BC GPA First preference for a student from the Wilton Manors community (e.g., ZIP codes 33305, 33306, 33”
### `928d5c749cac0c13` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Business Majors Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Full or part-time ⟵ “Helen Klonarides Business Center Memorial Scholarship | Business Majors Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Full or part-time”
### `93e7986f27cb87bc` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 Student must attend Central Campus International students may qualify (must have a student visa F1 status) ⟵ “Madalyn Taitelbaum Memorial Endowed Scholarship | Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 Student must attend Central Campus International students may qualify (must have a student visa F1 status)”
### `945c34289575fc35` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA and BA Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 This scholarship is to fund students from PACE Center for Girls, Inc., Broward ⟵ “PACE Center for Girls Inc., Broward Scholarship | AA and BA Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 This scholarship is to fund students from PACE Center for Girls, Inc., Broward”
### `9480895b202fceab` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Biological Sciences Full or part-time Minimum GPA 2.5 ⟵ “Bernard Fritze Memorial Endowed Scholarship | Biological Sciences Full or part-time Minimum GPA 2.5”
### `95312ab0ad201bb3` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Awarded to a student who participates in the Brain Bowl, is a member of Phi Theta Kappa, or is a member of the Honors College International students may qualify (must have a student visa F1 status) ⟵ “Gabriel Milanese Memorial Endowed Scholarship | Merit-based (scholarship based on academic achievement) Awarded to a student who participates in the Brain Bowl, is a member of Phi Theta Kappa, or is a member of the Honors College International students may qualify (must have a student visa F1 status”
### `9627ccd10c559e29` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: RN to BSN, RN, & LPN Programs Merit-based (scholarship based on academic achievement) Student must have completed at least one course in any of the BC nursing programs Minimum GPA 3.0 ⟵ “Mary & Ernest Costantino Merit Nursing Scholarship | RN to BSN, RN, & LPN Programs Merit-based (scholarship based on academic achievement) Student must have completed at least one course in any of the BC nursing programs Minimum GPA 3.0”
### `9670d357363fbaa5` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Must have completed at least one semester with a minimum 3.5 GPA ⟵ “Lawrence M. and Elsie S. Davie Mem Endowed Scholarship | Merit-based (scholarship based on academic achievement) Must have completed at least one semester with a minimum 3.5 GPA”
### `981001256a34e337` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Enrolled in the Teacher's Education Program in pursuit of a bachelor's degree in Education Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Rotary Club of Downtown Ft. Lauderdale Scholarship | Enrolled in the Teacher's Education Program in pursuit of a bachelor's degree in Education Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `98a976280b32641e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 Students affiliated with IBEW Local Union 728 ⟵ “John F. Ranken Memorial Endowed Scholarship | Full or part-time Minimum GPA 2.0 Students affiliated with IBEW Local Union 728”
### `98dc02742c61b04e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing student Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5 ⟵ “Romeyne & Sarah Klingensmith Memorial Nursing Scholarship | Nursing student Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5”
### `995ad1d977846ded` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major Full or part-time Minimum GPA 2.5 ⟵ “Cigna HealthCare Endowed Scholarship | Any major Full or part-time Minimum GPA 2.5”
### `9ad30fbce794d440` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/bright-futures.html (sha256 5468ffaad049)
- checks: {"thresholds": null}
  - award_amount_text: 12+12=24 ⟵ “Full-time (12 or more) | Full-Time | 12+12=24”
### `9cb3104c2554361d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Honor's College student Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 Full or part-time ⟵ “The Rosemary Duffy Larson Endowment | Honor's College student Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 Full or part-time”
### `9f43db136b791db6` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 First-generation student ⟵ “Helios Education Foundation First Generation Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 First-generation student”
### `9f7ba7ea62845428` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 Broward County resident Person with special learning disabilities ⟵ “Brooke A. Siegle Endowed Scholarship | Full or part-time Minimum GPA 2.0 Broward County resident Person with special learning disabilities”
### `9fa496009bbc10ef` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: STEM or Education Pathways Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Student must have completed a minimum of one college semester to be eligible ⟵ “Tom and Debbie Nycz Memorial Scholarship | STEM or Education Pathways Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Student must have completed a minimum of one college semester to be eligible”
### `9fddc6a458c36f14` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA, AS, or Supply Chain Management AS/BS Full or part-time Minimum GPA 2.5 Preference for children of members of the Greater South Florida Maritime Trade Council-affiliated unions ⟵ “Raymond T. McKay Memorial Endowed Scholarship | AA, AS, or Supply Chain Management AS/BS Full or part-time Minimum GPA 2.5 Preference for children of members of the Greater South Florida Maritime Trade Council-affiliated unions”
### `a1855b927d6c5d34` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Radiology Technology Full-time Minimum GPA 2.5 ⟵ “Radiology Assoc. Scholarship in Memory of Jeffrey Rippstein | Radiology Technology Full-time Minimum GPA 2.5”
### `a1afaaf2e521976c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Dental Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5 ⟵ “Broward Dental Research Clinic Dental Assisting Scholarship | Dental Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.5”
### `a1e1b3ccdafc3745` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full-time Minimum GPA 3.0 Graduating senior from Miramar High School Available to international students ⟵ “Leah Mattson Memorial Endowed Scholarship | Full-time Minimum GPA 3.0 Graduating senior from Miramar High School Available to international students”
### `a2b5d2348db74095` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Head of Household Broward County resident Full or part-time Minimum GPA of 2.5 ⟵ “Elizabeth Athanasakos Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Head of Household Broward County resident Full or part-time Minimum GPA of 2.5”
### `a2d740256d29bf29` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Minimum GPA 3.2 in any field Member of Broward College's Gay Straight Alliance (GSA) International students may qualify ⟵ “Be Proud Endowed Scholarship | Minimum GPA 3.2 in any field Member of Broward College's Gay Straight Alliance (GSA) International students may qualify”
### `a4aae45b46d462ab` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Environmental Science or Social Behavioral Science Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Burkhardt 79 Endowed Scholarship | Environmental Science or Social Behavioral Science Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `a6b0bc5e844f0ebc` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Area of study: Fine Arts Full or part-time Minimum GPA 2.5 Must be a graduate of Hallandale High School ⟵ “Zeltner Family Endowed Scholarship | Area of study: Fine Arts Full or part-time Minimum GPA 2.5 Must be a graduate of Hallandale High School”
### `a854bd07a70656d7` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: The Dalianis Scholars should be champions of that mission by demonstrating engagement in activities that preserve and promote Greek heritage Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Available to international students ⟵ “The Joan Dalianis Foundation Memorial Scholarship | The Dalianis Scholars should be champions of that mission by demonstrating engagement in activities that preserve and promote Greek heritage Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Available to internationa”
### `aa3026d05d8cc343` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Area of study: Theater Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Wendy Cohen Bailey Hall Endowed Scholarship | Area of study: Theater Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `aa401949b2b3abca` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Honor's College Students studying in the Robert "Bob" Elmore Honors College Minimum GPA 3.5 ⟵ “Farlie Turner & Co. Honors Scholarship | Honor's College Students studying in the Robert "Bob" Elmore Honors College Minimum GPA 3.5”
### `aa8b32413bbf32d1` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Science Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify ⟵ “Benjamin Bryan Klein Memorial Endowed Scholarship | Health Science Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify”
### `aaabde42c2af009c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AS, AS, BS, RN to BSN Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “BC Colleagues Scholarship | AS, AS, BS, RN to BSN Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `ad0fc1e10e9fd07e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Building Construction Technology, Architecture, Engineering Full or part-time Minimum GPA 2.75 ⟵ “Siemens Building Technologies Endowed Scholarship | Building Construction Technology, Architecture, Engineering Full or part-time Minimum GPA 2.75”
### `add0f0261898ed49` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Music majors Demonstrate financial need as determined by the FAFSA application Full or part-time ⟵ “Emil & Natalie Meyersfield Endowed Scholarship | Music majors Demonstrate financial need as determined by the FAFSA application Full or part-time”
### `af4fabbdfb338afc` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA degrees, Nursing and Aviation Full or part-time Minimum GPA 2.5 Broward County resident Preference for Davie or Cooper City Resident ⟵ “Davie-Cooper City Joan Morsillo Endowed Scholarship | AA degrees, Nursing and Aviation Full or part-time Minimum GPA 2.5 Broward County resident Preference for Davie or Cooper City Resident”
### `af613e732b242541` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Classified as Head of Household on FAFSA ⟵ “Kate and Melina Platt Memorial Scholarship | Demonstrate financial need as determined by the FAFSA application Classified as Head of Household on FAFSA”
### `afbc970ad8fb64d3` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Music majors Merit-based (scholarship based on academic achievement) Student must have completed a minimum of 12 semester hours with an overall 3.0 GPA ⟵ “Nathan and Rhea Gilson Memorial Music Endowed Scholarship | Music majors Merit-based (scholarship based on academic achievement) Student must have completed a minimum of 12 semester hours with an overall 3.0 GPA”
### `b0b67fcf08743d61` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.0 ⟵ “Lyle S. Salisbury Endowed Scholarship Fund | Demonstrate financial need as determined by the FAFSA application Full-time Minimum GPA 2.0”
### `b4449e2989b9c6b2` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA, AS Demonstrate financial need as determined by the FAFSA application Broward County resident Minimum GPA 3.0 Preference to graduates of Coconut Creek or St. Thomas Aquinas ⟵ “Stephen McFarlane Memorial Endowed Scholarship | AA, AS Demonstrate financial need as determined by the FAFSA application Broward County resident Minimum GPA 3.0 Preference to graduates of Coconut Creek or St. Thomas Aquinas”
### `b569acb621f11057` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time student Minimum GPA 2.5 ⟵ “Dan Marino Foundation Endowed Scholarship | Full or part-time student Minimum GPA 2.5”
### `b85994ec1c4124f5` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Honor's College student ⟵ “Robert Elmore Honors Full-Time Endowed Scholarships | Honor's College student”
### `b899a24fb066818f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Spirit of Broward College Employees Scholarship | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `bca984ccb6315c20` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 3.0 ⟵ “Elsie Davie Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 3.0”
### `c18949e9960198b1` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Honor's College Merit-based (scholarship based on academic achievement) Minimum GPA 3.5 ⟵ “Porterfield Family Honors Endowed Scholarship | Honor's College Merit-based (scholarship based on academic achievement) Minimum GPA 3.5”
### `c1ef4dae0b2b0846` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Radiology in their 2nd year Degree seeking Full-time (11 credits) Minimum GPA 2.0 ⟵ “Alisa Story Memorial Endowed Scholarship | Radiology in their 2nd year Degree seeking Full-time (11 credits) Minimum GPA 2.0”
### `c26d6e91cbd04150` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Students must be enrolled at least part-time (minimum of 6 credits/term) Minimum GPA 2.0 Student must be at a minimum of 50% completion benchmark Currently participating in Broward College’s PFiC Peer Mentoring & Leadership program Recipients will be required to write a letter of gratitude upon receipt of this scholarship ⟵ “Peer Forward/Greenwald Leadership Scholarship | Students must be enrolled at least part-time (minimum of 6 credits/term) Minimum GPA 2.0 Student must be at a minimum of 50% completion benchmark Currently participating in Broward College’s PFiC Peer Mentoring & Leadership program Recipients will be r”
### `c2de87a2a4d0a14c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Accepted at Broward College in the Business Pathway Area of Study: Hospitality and Tourism Management Full or Part-time AA or AS program Minimum High School GPA OR Broward College GPA 2.5 ⟵ “Motwani Family Academy | Accepted at Broward College in the Business Pathway Area of Study: Hospitality and Tourism Management Full or Part-time AA or AS program Minimum High School GPA OR Broward College GPA 2.5”
### `c330b5e9d9a62535` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Automotive Technology Program Full or Part-time Minimum GPA 2.0 ⟵ “Advance Auto Parts Automotive Technology Program Scholarship | Automotive Technology Program Full or Part-time Minimum GPA 2.0”
### `c3ae2bbdc93ac31b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/bright-futures.html (sha256 5468ffaad049)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 cumulative GPA ⟵ “Florida Medallion Scholars (FMS) | 2.75 cumulative GPA”
### `c50521fd41b279ea` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Business Administration Graduate of Broward County High School Full-time Minimum GPA 2.5 at BC Incoming students must have a 3.0 high school GPA ⟵ “Arden D. Dickey Endowed Scholarship | Business Administration Graduate of Broward County High School Full-time Minimum GPA 2.5 at BC Incoming students must have a 3.0 high school GPA”
### `c5522cafa3273e3d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Preference for 2 students who have been involved in the PACE Center for Girls, Inc., Broward ⟵ “Pettis Family Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Preference for 2 students who have been involved in the PACE Center for Girls, Inc., Broward”
### `c63accca53812b68` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Member of the Professional Enhancement Program (PEP) Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.0 Available to international students ⟵ “Broward College Central Campus Social Behavioral Sciences Department Scholarship | Member of the Professional Enhancement Program (PEP) Merit-based (scholarship based on academic achievement) Full or part-time Minimum GPA 3.0 Available to international students”
### `c66eed9b3c779632` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Students must be currently employed by the Museum of Discovery & Science (MODS) and are responsible for providing a letter of eligibility from MODS each semester, which is required to be uploaded to BC ⟵ “R Squared Charitable Fund MODS Scholarship | Students must be currently employed by the Museum of Discovery & Science (MODS) and are responsible for providing a letter of eligibility from MODS each semester, which is required to be uploaded to BC”
### `ca081bd42b84eb79` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 ⟵ “BC Trustees Endowed Scholarship | Full or part-time Minimum GPA 2.0”
### `ca6cb5b0bba25b8d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Employees of Sun Sentinel Minimum GPA 2.0 Must provide a certification letter from Sun Sentinel stating their eligibility for the award ⟵ “Sun-Sentinel Endowed Scholarship | Employees of Sun Sentinel Minimum GPA 2.0 Must provide a certification letter from Sun Sentinel stating their eligibility for the award”
### `ccaef8781812f14f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA, AS, AAS, BS Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Full or Part-time Available to international students ⟵ “Balfour Beatty LLC Endowed Scholarship | AA, AS, AAS, BS Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Full or Part-time Available to international students”
### `cd7beac21e8c5d48` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA or AS in Criminal Justice, Crime Scene, or Public Safety Minimum GPA 2.0 International students may qualify (must have a student visa F1 status) ⟵ “Lt. Patrick G. McDonald Memorial Scholarship | AA or AS in Criminal Justice, Crime Scene, or Public Safety Minimum GPA 2.0 International students may qualify (must have a student visa F1 status)”
### `cddf262f942c1381` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Criminal Justice Demonstrate financial need as determined by the FAFSA application Graduate of Coral Springs High, Taravella High, or Stoneman Douglas Resident of Coral Springs Full or part-time Minimum GPA 2.5 ⟵ “FOP Lodge #87 Sharyn Rapoport Biondo Endowment | Criminal Justice Demonstrate financial need as determined by the FAFSA application Graduate of Coral Springs High, Taravella High, or Stoneman Douglas Resident of Coral Springs Full or part-time Minimum GPA 2.5”
### `cf67b66d542635f8` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: South campus students Full or part-time Minimum GPA 2.5 ⟵ “Kyra Belan Endowed Scholarship | South campus students Full or part-time Minimum GPA 2.5”
### `cf7318d7d5a5dc2f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major Demonstrate financial need as determined by the FAFSA application Full-time or Part-time Minimum GPA 2.0 Available to International students Recipients must write a Thank you letter ⟵ “Dade County Federal Credit Union Financial Future Scholarship | Any major Demonstrate financial need as determined by the FAFSA application Full-time or Part-time Minimum GPA 2.0 Available to International students Recipients must write a Thank you letter”
### `d0f209c63407f117` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Physical Therapy or Radiation Therapy Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 ⟵ “Sal Bosco Memorial Endowed Scholarship | Physical Therapy or Radiation Therapy Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5”
### `d1bd280ed123d992` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Student must be an employee of an Exec's member or any family member of any employee of an Exec's member Student must obtain a verification letter from the Executives Association of Ft. Lauderdale before applying ⟵ “Executives Association of Ft, Lauderdale Endowed Scholarship | Student must be an employee of an Exec's member or any family member of any employee of an Exec's member Student must obtain a verification letter from the Executives Association of Ft. Lauderdale before applying”
### `d402233d43cc397e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Professional Pilot Technology Program, and are currently enrolled in or completing a flight course Private Pilot Certificate Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Available to international students ⟵ “Emil Buehler Trust Endowed Scholarship | Professional Pilot Technology Program, and are currently enrolled in or completing a flight course Private Pilot Certificate Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Available to international student”
### `d541c2ab185e5fed` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: History major Merit-based (scholarship based on academic achievement) Full-time Minimum GPA 3.0 ⟵ “Catherine Dinnen Memorial History Endowed Scholarship | History major Merit-based (scholarship based on academic achievement) Full-time Minimum GPA 3.0”
### `d597d4ebcd40639e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Students who aspire for a career in public service or serve as a leaders in the community ⟵ “Virginia S. Young Memorial Scholarship | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Students who aspire for a career in public service or serve as a leaders in the community”
### `d62e01aae4f90d90` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Hotel/Restaurant Management Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Walter and Deborah Banks Family Endowed Scholarship | Hotel/Restaurant Management Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `d657d6277b3efbfc` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AS in Nursing (RN) Full or part-time Minimum GPA 2.75 ⟵ “Seymour and Ruth H. Kleinfeld Endowed Nursing Scholarship | AS in Nursing (RN) Full or part-time Minimum GPA 2.75”
### `d8ccb2704f998969` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Fine Arts Full or part-time Minimum GPA 3.0 International students may qualify ⟵ “Hilma Klock Goos Endowed Scholarship | Fine Arts Full or part-time Minimum GPA 3.0 International students may qualify”
### `d9b34d2a98929a2b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full-time Resident of Broward Preference for Construction Technology ⟵ “Jeffrey W. Simon/IAEI Endowed Memorial Scholarship | Full-time Resident of Broward Preference for Construction Technology”
### `d9cf55ab8077c9d8` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Business Administration ⟵ “Gene A. Whiddon Memorial Scholarship | Business Administration”
### `da1f728bda8693ae` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Shepard & Louise Lee Endowed Nursing Scholarship | Nursing Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `daf3c5ddd494b83c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA or AS Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “June Fooshe Endowed Veterinary Scholarship | AA or AS Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `db7001970170fe13` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full-time PTS employee FAFSA required ⟵ “PTS Fund | Demonstrate financial need as determined by the FAFSA application Full-time PTS employee FAFSA required”
### `dbb32b9bc0218303` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 Associate and Baccalaureate programs US Citizen ⟵ “Teresa B. Sjogren Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 Associate and Baccalaureate programs US Citizen”
### `dce1dbe12ec2fa51` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Political Science/Pre-Law Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Jane Ferris Endowed Scholarship | Political Science/Pre-Law Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `dd733cc22e6e92aa` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA or AS in Health Sciences, Journalism, and Aviation Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Florida resident ⟵ “Herman and Nana Klein Endowed Scholarship | AA or AS in Health Sciences, Journalism, and Aviation Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Florida resident”
### `e1fb06457e0dd94c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA or AS: Environmental, Marine, or Aquatic Sciences Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “PADI Endowed Scholarship | AA or AS: Environmental, Marine, or Aquatic Sciences Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `e359a4d346fb8529` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 International students may qualify Awarded to the winner of the annual BC Creative Writing contest ⟵ “Michael Cleary Creative Writing Award | Full or part-time Minimum GPA 2.0 International students may qualify Awarded to the winner of the annual BC Creative Writing contest”
### `e4554c241aa20e48` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Students enrolled in the Handy program ⟵ “Kathryn Krause HANDY Book Award Endowment | Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.0 Students enrolled in the Handy program”
### `e48458c824907e0c` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Automotive Maintenance program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 Full or part-time ⟵ “Lipton Toyota Endowment | Automotive Maintenance program Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 Full or part-time”
### `e4c36998b8ee2568` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Herbert H. Talbot Memorial Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `e6ba687f68e7ad83` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA, AS Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Marie Harrington and Ann Powell Endowed Scholarship | AA, AS Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `e7a03bcc35859872` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5 ⟵ “Campaign 2000 Endowed Scholarship | Full or part-time Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.5”
### `e8248d9ae7842799` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Full or part-time Student must upload a document provided by UFF-BC to certify that the student is eligible ⟵ “United Faculty of Florida Endowed Scholarship | Demonstrate financial need as determined by the FAFSA application Full or part-time Student must upload a document provided by UFF-BC to certify that the student is eligible”
### `e89dd1464b7d989f` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Any major ⟵ “Pepsi-Cola Bottling Co. Endowed Athletic Scholarship | Any major”
### `e8c3b11bb9314c9d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based (scholarship based on academic achievement) Enrolled currently or previously in an ESL class Minimum GPA 3.0 International students may qualify (must have a student visa F1 status) Student must be attending North campus ⟵ “John Nandor Orias Memorial Scholarship | Merit-based (scholarship based on academic achievement) Enrolled currently or previously in an ESL class Minimum GPA 3.0 International students may qualify (must have a student visa F1 status) Student must be attending North campus”
### `e96e7aef027abce4` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Broward County HS graduate Minimum 2.75 HS or BC GPA First preference for a student from the Wilton Manors community (e.g., ZIP codes 33305, 33306, 33311, or 33334) ⟵ “Kiwanis Club of Wilton Manors Sal Bellassai Scholarship | Demonstrate financial need as determined by the FAFSA application Broward County HS graduate Minimum 2.75 HS or BC GPA First preference for a student from the Wilton Manors community (e.g., ZIP codes 33305, 33306, 33311, or 33334)”
### `eacd349ce44696eb` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Music Full or Part-time Minimum GPA 2.5 Students must be enrolled in one of two ensemble classes: MUN1120 or MUN1280C Available to international students ⟵ “Rosemary Duffy Larson Music Scholarship | Music Full or Part-time Minimum GPA 2.5 Students must be enrolled in one of two ensemble classes: MUN1120 or MUN1280C Available to international students”
### `eae6e62d40f4e256` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Sistrunk neighborhood, zip code 33311 ⟵ “Dr. James Sistrunk Scholarship | Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Sistrunk neighborhood, zip code 33311”
### `ed3fd1dcb32040dd` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Music majors Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 ⟵ “Julie Powell Rozman Memorial Scholarship for Music | Music majors Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0”
### `ee68ead90cab420a` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Area of study: Math, Science, Technology, Engineering (STEM) Members of the Minority Male Initiative (MMI) student organization ⟵ “Florida Power & Light MMI Annual Scholarship | Area of study: Math, Science, Technology, Engineering (STEM) Members of the Minority Male Initiative (MMI) student organization”
### `efc0c5eb003ecad9` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Honor's College student Part-time ⟵ “Robert Elmore Honors Institute Endowed Scholarship | Honor's College student Part-time”
### `f14d966521507900` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Dental Assisting Merit-based (scholarship based on academic achievement) Full-time Minimum GPA 3.0 ⟵ “Dr. William Shumpert Memorial Endowed Scholarship | Dental Assisting Merit-based (scholarship based on academic achievement) Full-time Minimum GPA 3.0”
### `f171b3382f6fae9e` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Computer Science or Information Technology ⟵ “CSIT Scholarship | Computer Science or Information Technology”
### `f2e4db7bbb194b28` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.0 ⟵ “Blockbuster Entertainment Endowed Scholarship | Full or part-time Minimum GPA 2.0”
### `f4f2261731208517` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.5 Students participating in the Honors Institute program ⟵ “Ruth H. Brown Endowed Scholarship | Full or part-time Minimum GPA 2.5 Students participating in the Honors Institute program”
### `f5d7282f4b3f2e54` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Science in the Radiology Nursing program ⟵ “Tenet Scholarship Fund | Health Science in the Radiology Nursing program”
### `f5dd79271526fa6d` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Business students Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify (must have a student visa F1 status) ⟵ “Lotspeich Company of Florida Endowed Scholarship | Business students Merit-based (scholarship based on academic achievement) Minimum GPA 3.0 International students may qualify (must have a student visa F1 status)”
### `f73be1baddc78804` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.5 Preference for students attending the North Campus and attending night classes ⟵ “Bunny Wagner Endowed Scholarship | Full or part-time Minimum GPA 2.5 Preference for students attending the North Campus and attending night classes”
### `f909a7639c1918e7` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Students registered with Broward College Accessibility Resources with an ADA-approved documented disability that requires them to use a wheelchair Preference is given to students with Cerebral Palsy ⟵ “John H. Murphy Scholarship | Students registered with Broward College Accessibility Resources with an ADA-approved documented disability that requires them to use a wheelchair Preference is given to students with Cerebral Palsy”
### `f93c94a6d5180e07` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing-RN ⟵ “Geri Malloy Maliner Nursing Scholarship | Nursing-RN”
### `f9419a892067d6b0` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Health Sciences Broward County resident Full or part-time Minimum GPA 2.3 ⟵ “Lucille Forman Memorial Endowed Scholarship | Health Sciences Broward County resident Full or part-time Minimum GPA 2.3”
### `fa89fd9b8edbe797` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Hospitality and Tourism Broward County resident Full or part-time Minimum GPA 2.5 ⟵ “Nicki Englander Grossman Endowed Hospitality and Tourism Mgt | Hospitality and Tourism Broward County resident Full or part-time Minimum GPA 2.5”
### `fa9d28572b5da571` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Honor's College Full or part-time Minimum GPA 3.5 Available to international students ⟵ “Dr. Irmgard Bocchino Honors Endowed Scholarship | Honor's College Full or part-time Minimum GPA 3.5 Available to international students”
### `fc9bab5e8436efce` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Nursing Full or part-time Minimum GPA 2.5 ⟵ “Doctors Hospital Foundation Endowed Scholarship | Nursing Full or part-time Minimum GPA 2.5”
### `fcc016851be70e99` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: AA & AS Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 ⟵ “Lillian Gutterman Memorial Endowed Scholarship | AA & AS Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5”
### `fccc462f83c2d308` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Building Construction Technology Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Broward County resident ⟵ “James B. Pirtle Construction Co. Scholarship | Building Construction Technology Demonstrate financial need as determined by the FAFSA application Full or part-time Minimum GPA 2.5 Broward County resident”
### `fdcea985bd083a69` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Automotive Education Programs Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Available to international students ⟵ “AutoNation Endowed Scholarship | Automotive Education Programs Demonstrate financial need as determined by the FAFSA application Minimum GPA 2.0 Available to international students”
### `ffaaed1c9aa10097` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Business or Economics Full or part-time Minimum GPA 2.5 ⟵ “Wells Fargo Endowed Scholarship | Business or Economics Full or part-time Minimum GPA 2.5”
### `ffedfd66519bcb2b` Broward College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/scholarships/scholarships-list.html (sha256 87d8bf1ad7c1)
- checks: {"thresholds": null}
  - eligibility_summary: Full or part-time Minimum GPA 2.7 Students who are working part-time and not receiving any other financial aid International students may qualify ⟵ “Brian Neuer Memorial Scholarship | Full or part-time Minimum GPA 2.7 Students who are working part-time and not receiving any other financial aid International students may qualify”
### `04279e1563403685` Broward College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/credit-for-prior-learning/international-baccalaureate.html (sha256 70ae9e40503b)
- checks: {"distinct_exams": 35, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|4 5 to 7]:  ⟵ “Biology | BSC1005 & BSC1005L BSC1005 & BSC1005L and BSC2010 & BSC2010L | 4 8 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-BIOLOGY-HL|4 to 7]:  ⟵ “Biology (HL) (Effective for exams taken after 09/23/2020) | BSC1005 & BSC1005L and BSC2010 & BSC2010L | 8 | 4 to 7 | No |  | ”
  - equivalencies[IB-BIOLOGY-SL|4 to 7]:  ⟵ “Biology (SL) (Effective for exams taken after 09/23/2020) | BSC1005 & BSC1005L | 4 | 4 to 7 | No |  | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4 5 to 7]:  ⟵ “Business and Management | GEB1011 GEB1011 and MAN2604 | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-CHEMISTRY|4 5 to 7]:  ⟵ “Chemistry | CHM1020 & CHM1020L CHM1020 & CHM1020L and CHM1045 & CHM1045L | 4 8 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-COMPUTER-SCIENCE|4 5 to 7]:  ⟵ “Computer Science | CGS2100C CGS2100C and COP1000C | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-ECONOMICS|4 5 to 7]:  ⟵ “Economics | ECO1000 ECO2013 and ECO2023 | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4 5 to 7]:  ⟵ “Environmental Systems | ISC1050 ISC1050 and ISC1141 | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|4 to 7]:  ⟵ “Environmental Systems and Societies (SL) (Effective for exams taken after 5/16/2018) | EVR1001 | 3 | 4 to 7 | No |  | ”
  - equivalencies[IB-FILM|4 5 to 7]:  ⟵ “Film Studies | FIL2000 FIL2000 and FIL1420C | 3 6 | 4 5 to 7 | No | Yes (FIL2000) | Yes (FIL2000)”
  - equivalencies[IB-FRENCH|4 5 to 7]:  ⟵ “French: Language B Meets Foreign Language Requirement | FRE1121 FRE1121 and FRE2220 | 4 8 | 4 5 to 7 | No |  | Yes”
  - equivalencies[IB-GEOGRAPHY|4 5 to 7]:  ⟵ “Geography | GEA2000 GEO2200 and GEO2400 | 3 6 | 4 5 to 7 | No | Yes (GEA2000) | Yes (GEA2000)”
  - equivalencies[IB-GERMAN|4 5 to 7]:  ⟵ “German: Language B | GER1121 GER1121 and GER2220 | 4 8 | 4 5 to 7 | No |  | Yes”
  - equivalencies[IB-GLOBAL-POLITICS-HL|4 5 to 7]:  ⟵ “Global Politics (HL) | INR2002 INR2002 and | 3 6 | 4 5 to 7 | No | Yes | Yes”
  - equivalencies[IB-GLOBAL-POLITICS-SL|4 to 7]:  ⟵ “Global Politics (SL) | INR2002 | 3 | 4 to 7 | No | Yes | Yes”
  - equivalencies[IB-HISTORY|4 5 to 7]:  ⟵ “History | WOH2030 WOH2030 and | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-HISTORY-HL|4 5 to 7]:  ⟵ “History (HL): History of Africa and the Middle East (Effective for exams taken after 5/16/2018) | WOH2030 WOH2030 and WOH2031 | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-HISTORY-SL|4 to 7]:  ⟵ “History (SL) (Effective for exams taken after 5/16/2018) | WOH2030 | 3 | 4 to 7 | No |  | ”
  - equivalencies[IB-HISTORY|4 5 to 7]:  ⟵ “Islamic History |  | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-LATIN|4 5 to 7]:  ⟵ “Latin | LAT2130 LAT2130 and | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|4 5 to 7]:  ⟵ “Math Analysis and Approaches (HL) | MAC1105 MAC1105 and MAC2311 or MAC1140 or MAC1147 | 3 6 - 8 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|4 5 to 7]:  ⟵ “Math Analysis and Approaches (SL) | MAC1105 MAC1105 and MAC1140 | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|4 5 to 7]:  ⟵ “Math Applications and Interpretations (HL) | MAC1140 MAC1140 and MAC1114 | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-SL|4 5 to 7]:  ⟵ “Math Applications and Interpretations (SL) | MAC1105 MAC1105 and MGF1106 | 3 6 | 4 5 to 7 | No |  | ”
  - equivalencies[IB-MUSIC|4 5 to 7]:  ⟵ “Music | MUL2010 MUL2010 and MUH2111 | 3 6 | 4 5 to 7 | No |  | Yes”
  - … 11 more rows
### `f948435881d44faf` Broward College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/credit-for-prior-learning/advanced-placement.html (sha256 f6384ee4453a)
- checks: {"distinct_exams": 37, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3 to 5]:  ⟵ “2-D Art and Design | ART1201C | 3 | 3 to 5 | No |  | ”
  - equivalencies[AP-3-D-ART-DESIGN|3 to 5]:  ⟵ “3-D Art and Design | ART1203C | 3 | 3 to 5 | No |  | ”
  - equivalencies[AP-ART-HISTORY|3 4 to 5]:  ⟵ “Art History(exams taken before 5/17/2018) | ARH2000 ARH2050 and ARH2051 | 3 6 | 3 4 to 5 | No |  | ”
  - equivalencies[AP-BIOLOGY|3 4 5]:  ⟵ “Biology | BSC1005 & BSC1005L BSC2010 & BSC2010L BSC2010 & BSC2010L and BSC2011 & BSC2011L | 4 4 8 | 3 4 5 | No |  | ”
  - equivalencies[AP-CALCULUS-AB|3 to 5]:  ⟵ “Calculus AB | MAC2311 | 5 | 3 to 5 | No |  | ”
  - equivalencies[AP-CALCULUS-BC|3 4 to 5]:  ⟵ “Calculus BC(Sub-score is evaluated based on the Calculus AB exam) | MAC2311 MAC2311 and MAC2312 | 5 10 | 3 4 to 5 | No |  | ”
  - equivalencies[AP-CHEMISTRY|3 4 5]:  ⟵ “Chemistry | CHM1020 & CHM1020L CHM1045 & CHM1045L CHM1045 & CHM1045L and CHM1046 & CHM1046L | 4 4 8 | 3 4 5 | No |  | ”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3 4 to 5]:  ⟵ “Chinese Language and Culture Meets Foreign Language Requirement | CHI2220 CHI2220 and CHI2221 | 4 6 | 3 4 to 5 | No |  | Yes”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3 to 5]:  ⟵ “Comparative Government and Politics | CPO2002 | 3 | 3 to 5 | No |  | ”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3 to 5]:  ⟵ “Computer Science A Meets Digital Literacy Requirement | CGS1060C | 3 | 3 to 5 | No |  | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3 to 5]:  ⟵ “Computer Science Principles | COP1000C | 3 | 3 to 5 | No |  | ”
  - equivalencies[AP-DRAWING|3 to 5]:  ⟵ “Drawing | ART1300C | 3 | 3 to 5 | No |  | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 4 to 5]:  ⟵ “English Language and Composition | ENC1101 ENC1101 and ENC1102 | 3 6 | 3 4 to 5 | No |  | ”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3 4 to 5]:  ⟵ “English Literature and Composition | ENC1101 or LIT2000 ENC1101 & ENC1102 or LIT2000 | 3 6 | 3 4 to 5 | No | Yes | Yes (LIT2000)”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3 to 5]:  ⟵ “Environmental Science | EVR1001 | 3 | 3 to 5 | No |  | ”
  - equivalencies[AP-EUROPEAN-HISTORY|3 4 to 5]:  ⟵ “European History | EUH1000 EUH1000 and EUH1001 | 3 6 | 3 4 to 5 | No | Yes | Yes”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 4 to 5]:  ⟵ “French Language and Culture Meets Foreign Language Requirement | FRE2220 FRE2220 and FRE2201 | 4 6 | 3 4 to 5 | No |  | Yes”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 4 to 5]:  ⟵ “French Literature(Discontinued in 2011) | LIT2000 LIT2000 and LIT2190 | 3 6 | 3 4 to 5 | No |  | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3 4 to 5]:  ⟵ “German Language and Culture Meets Foreign Language Requirement | GER2220 GER2220 and GER2201 | 4 6 | 3 4 to 5 | No |  | Yes”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3 to 5]:  ⟵ “Human Geography | GEO2420 | 3 | 3 to 5 | No | Yes | Yes”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3 4 to 5]:  ⟵ “Italian Language and Culture Meets Foreign Language Requirement | ITA2220 ITA2220 and ITA2221 | 4 6 | 3 4 to 5 | No |  | Yes”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3 4 to 5]:  ⟵ “Japanese Language and Culture Meets Foreign Language Requirement | JPN2220 JPN2220 and JPN2221 | 4 6 | 3 4 to 5 | No |  | Yes”
  - equivalencies[AP-LATIN|3 to 5]:  ⟵ “Latin | LNW1700 | 3 | 3 to 5 | No |  | ”
  - equivalencies[AP-LATIN|3 to 5]:  ⟵ “Latin: Latin Literature(Discontinued in 2012) | LN1700 | 3 | 3 to 5 | No |  | ”
  - equivalencies[AP-MACROECONOMICS|3 to 5]:  ⟵ “Macroeconomics | ECO2013 | 3 | 3 to 5 | No | Yes | ”
  - … 16 more rows
### `m67942db19f6a471` Broward College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.broward.edu/academics/dual-enrollment/eligibility-requirements.html (sha256 312c4f092a90)
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - college_gpa_to_continue: 2.0 ⟵ “Maintain a 2.0 Broward College GPA”
  - eligibility_tier: 3.0 ⟵ “Unweighted overall GPA of 3.0 or higher”
  - eligibility_tier: 3.0 ⟵ “Unweighted overall GPA of 3.0 or higher”
  - eligibility_tier: 3.0 ⟵ “Unweighted overall GPA of 3.0 or higher”
  - eligibility_tier: 3.0 ⟵ “Unweighted overall GPA of 3.0 or higher”
  - eligibility_tier: 3.0 ⟵ “Unweighted overall GPA of 3.0 or higher”
  - eligibility_tier: 2.0 ⟵ “Early Admission, a form of dual enrollment, allows eligible high school senior students to enroll in at least 12 credits per term, Fall and Spring, and maintain a college GPA of 2.0 or greater. Early admission students wishing to matriculate to BC will need to submit their final high school transcri”
  - college_gpa_to_continue: 2.0 ⟵ “Early Admission, a form of dual enrollment, allows eligible high school senior students to enroll in at least 12 credits per term, Fall and Spring, and maintain a college GPA of 2.0 or greater. Early admission students wishing to matriculate to BC will need to submit their final high school transcri”
### `07a86fc6587aa102` Chipola College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.chipola.edu/admissions/testing-center/college-level-examination-program-clep/ (sha256 d54115e96ceb)
- checks: {"distinct_exams": 28, "equivalencies": 28, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENC 1101 | 4”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | No direct equivalency** | n/a”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | No direct equivalency** | n/a”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POS 2041 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | AML 2010 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | No direct equivalency | ”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology, General | 50 | BSC 1005 | 3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MAC 2233 | 3”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry, General | 50 | CHM 1030 | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MAC 1105 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus Algebra | 50 | MAC 1140 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENL 2011 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACG 2021 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, College Level | 50 | FRE 1120 | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, College Level | 50 | No direct equivalency | ”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | DEP 2004 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | No direct equivalency | ”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introduction to Business Law | 50 | BUL 2131 | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | No direct equivalency | ”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSY 2012 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SYG 1000 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | EC0 2013 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | MAN 2021 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | MAR 2011 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECO 2023 | 3”
  - … 3 more rows
### `m446572a8aafb622` Chipola College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.chipola.edu/admissions/dual-enrollment/ (sha256 8cbc8eb63fac)
- checks: {"fields": ["college_gpa_to_continue"], "merged_pages": 2, "tiers": 6}
  - eligibility_tier: 3.0 ⟵ “5. Have a minimum, unweighted cumulative high school 3.0 GPA in 5 high school credits.”
  - eligibility_tier: 3.0 ⟵ “Have a minimum, unweighted cumulative high school 3.0 GPA in 5 high school credits.”
  - eligibility_tier: 2.0 ⟵ “Have a minimum, unweighted cumulative high school 2.0 GPA in 5 high school credits.”
  - eligibility_tier: 3.0 ⟵ “Have a minimum, unweighted cumulative high school 3.0 GPA”
  - eligibility_tier: 2.0 ⟵ “Have a minimum, unweighted cumulative high school 2.0 GPA”
  - eligibility_tier: 2.0 ⟵ “Students must maintain a cumulative college GPA of 2.0. Students who fail to meet this requirement will be placed on academic suspension until after high school graduation. Final grades become part of both the students high school transcript and college transcript.”
  - college_gpa_to_continue: 2.0 ⟵ “Students must maintain a cumulative college GPA of 2.0. Students who fail to meet this requirement will be placed on academic suspension until after high school graduation. Final grades become part of both the students high school transcript and college transcript.”
  - max_credit_hours_per_term: 18 ⟵ “enroll and maintain a full-time status. Academic students are limited to no more than 18 hours per semester for fall”
### `12f8a89471ccb74d` College of Central Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.cf.edu/admissions/paying-for-college/cost-of-attendance/ (sha256 e2b6b137478a)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition/Fees: 2712 ⟵ “Tuition/Fees | $2,712 | $10,512”
  - off_campus_not_with_family:Distance Learning Fees: 120 ⟵ “Distance Learning Fees | $120 | $120”
  - off_campus_not_with_family:Books & Supplies*: 1700 ⟵ “Books & Supplies* | $1,700 | $1,700”
  - off_campus_not_with_family:Living Expenses: 11412 ⟵ “Living Expenses | $11,412 | $11,412”
  - off_campus_not_with_family:Transportation: 3132 ⟵ “Transportation | $3,132 | $3,132”
  - off_campus_not_with_family:Personal/Misc: 2277 ⟵ “Personal/Misc | $2,277 | $2,277”
  - off_campus_not_with_family:Total Budget: 21353 ⟵ “Total Budget | $21,353 | $29,153”
### `43e3e87a3c71ebe7` College of Central Florida — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.cf.edu/admissions/paying-for-college/cost-of-attendance/ (sha256 e2b6b137478a)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition/Fees: 10512 ⟵ “Tuition/Fees | $2,712 | $10,512”
  - off_campus_not_with_family:Distance Learning Fees: 120 ⟵ “Distance Learning Fees | $120 | $120”
  - off_campus_not_with_family:Books & Supplies*: 1700 ⟵ “Books & Supplies* | $1,700 | $1,700”
  - off_campus_not_with_family:Living Expenses: 11412 ⟵ “Living Expenses | $11,412 | $11,412”
  - off_campus_not_with_family:Transportation: 3132 ⟵ “Transportation | $3,132 | $3,132”
  - off_campus_not_with_family:Personal/Misc: 2277 ⟵ “Personal/Misc | $2,277 | $2,277”
  - off_campus_not_with_family:Total Budget: 29153 ⟵ “Total Budget | $21,353 | $29,153”
### `570ebba9813b2b2c` Eastern Florida State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.easternflorida.edu/admissions/documents/dual-enrollment-efsc-articulation-agreement-bps-and-efsc-dual-enrollment-2026-27.pdf (sha256 9f53c5bddc0f)
- checks: {"fields": [], "tiers": 10}
  - eligibility_tier: 3.0 ⟵ “1. Present an unweighted high school GPA of at least 3.0.”
  - eligibility_tier: 3.0 ⟵ “2.   Present an unweighted high school GPA of at least 3.0.”
  - eligibility_tier: 3.0 ⟵ “School GPA of 3.0+:”
  - eligibility_tier: 3.0 ⟵ “2. Present an unweighted high school GPA of at least 3.0.”
  - eligibility_tier: 2.5 ⟵ “School GPA of 2.5+”
  - eligibility_tier: 2.5 ⟵ “2. Present an unweighted high school GPA of at least 2.5.”
  - eligibility_tier: 3.0 ⟵ “requirements, maintain the unweighted high school GPA of 3.0, and achieve an overall GPA of 2 .0 in college”
  - eligibility_tier: 2.5 ⟵ “1. An unweighted high school GPA of 2.5-3.5.”
  - eligibility_tier: 3.5 ⟵ “GPA of 3.5 may register for six courses each term with their high school's approval.”
  - eligibility_tier: 3.0 ⟵ “1.     An unweighted h i g h s c h o o l GPA of at least 3.0.”
### `m74875b7753e712f` Eastern Florida State College — credit_policies 2027-28 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.easternflorida.edu/admissions/dual-enrollment/faq.php (sha256 bbff4b5df9f2)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “An unweighted cumulative high school GPA of at least 3.0”
  - eligibility_tier: 3.5 ⟵ “unless they have an unweighted high school GPA of at least 3.5 and the permission”
  - eligibility_tier: 2.0 ⟵ “are expected to complete and achieve an overall GPA of 2.0 in dual enrollment coursework”
  - per_credit_hour_charge: 25 ⟵ “Automatically enrolled in the Titan First Day Ready Program and charged $25 per credit hour to cover the cost of required instructional materials.”
### `bf521b42cbf70b7a` Eckerd College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.eckerd.edu/quicklinks/transfer-credit (sha256 456a76903bf4)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C- ⟵ “Grades of "C-" or better only will be accepted for transfer credit.”
  - max_transfer_credits: 63 ⟵ “Eckerd accepts a maximum of 63 semester hours of transfer credit which may be applied toward meeting degree requirements.”
### `14dafc99a54aca48` Flagler College — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.flagler.edu/admissions-aid/tuition-and-fees (sha256 ad7a2fc9e934)
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition: 38660 ⟵ “Tuition | $38,660 | $38,660 | $38,660”
  - on_campus:Mandatory Activity Fee: 300 ⟵ “Mandatory Activity Fee | $300 | $300 | $300”
  - on_campus:Technology Fee: 300 ⟵ “Technology Fee | $300 | $300 | $300”
  - on_campus:First Day Complete: 660 ⟵ “First Day Complete | $660 | $660 | $660”
  - on_campus:Food and Housing: 18230 ⟵ “Food and Housing | $18,230 | $18,230 | $18,230”
  - on_campus:Total Direct Costs: 58150 ⟵ “Total Direct Costs | $58,150 | $58,150 | $58,150”
  - off_campus_not_with_family:Tuition: 38660 ⟵ “Tuition | $38,660 | $38,660 | $38,660”
  - off_campus_not_with_family:Mandatory Activity Fee: 300 ⟵ “Mandatory Activity Fee | $300 | $300 | $300”
  - off_campus_not_with_family:Technology Fee: 300 ⟵ “Technology Fee | $300 | $300 | $300”
  - off_campus_not_with_family:First Day Complete: 660 ⟵ “First Day Complete | $660 | $660 | $660”
  - off_campus_not_with_family:Food and Housing: 18230 ⟵ “Food and Housing | $18,230 | $18,230 | $18,230”
  - off_campus_not_with_family:Total Direct Costs: 58150 ⟵ “Total Direct Costs | $58,150 | $58,150 | $58,150”
  - with_parents_or_family:Tuition: 38660 ⟵ “Tuition | $38,660 | $38,660 | $38,660”
  - with_parents_or_family:Mandatory Activity Fee: 300 ⟵ “Mandatory Activity Fee | $300 | $300 | $300”
  - with_parents_or_family:Technology Fee: 300 ⟵ “Technology Fee | $300 | $300 | $300”
  - with_parents_or_family:First Day Complete: 660 ⟵ “First Day Complete | $660 | $660 | $660”
  - with_parents_or_family:Food and Housing: 18230 ⟵ “Food and Housing | $18,230 | $18,230 | $18,230”
  - with_parents_or_family:Total Direct Costs: 58150 ⟵ “Total Direct Costs | $58,150 | $58,150 | $58,150”
### `06ba34d89fd85d52` Florida Atlantic University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.fau.edu/admissions/ap/ (sha256 f2ba0d7580b3)
- checks: {"distinct_exams": 32, "equivalencies": 51, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | ARH 2000 | 3 | 3”
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History | ARH 2000, ARH 2051 | 4-5 | 6”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | BSC 1005, BSC 1005L | 3 | 4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | BSC 1010, BSC 1010L | 4 | 4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | BSC 1010, BSC 1010L, BSC 1011, BSC 1011L | 5 | 8”
  - equivalencies[AP-CALCULUS-AB|3-5]:  ⟵ “Calculus AB | MAC 2311 | 3-5 | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | MAC 2311 | 3 | 4”
  - equivalencies[AP-CALCULUS-BC|4-5]:  ⟵ “Calculus BC | MAC 2311, MAC 2312 | 4-5 | 8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | CHM 1020, CHM 1020L | 3 | 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | CHM 2045, CHM 2045L | 4 | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | CHM 2045, CHM 2045L CHM 2046, CHM 2046L | 5 | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | FOL 2220 | 3 | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language and Culture | FOL 2220, FOL 2221 | 4-5 | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3-5]:  ⟵ “Computer Science A | CGS 1075 | 3-5 | 3”
  - equivalencies[AP-MACROECONOMICS|3-5]:  ⟵ “Economics/Macro | ECO 2013 | 3-5 | 3”
  - equivalencies[AP-MICROECONOMICS|3-5]:  ⟵ “Economics/Micro | ECO 2023 | 3-5 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science | ISC 2051 | 3-5 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | WOH 2022 | 3 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4-5]:  ⟵ “European History | WOH 2012, WOH 2022 | 4-5 | 6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | FRE 2220 | 3 | 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4-5]:  ⟵ “French Language and Culture | FRE 2220, FRE 2221 | 4-5 | 8”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture | GER 2220 | 3 | 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4-5]:  ⟵ “German Language and Culture | GER 2220, GER 2221 | 4-5 | 8”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3-5]:  ⟵ “Human Geography | GEA 2000 | 3-5 | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture | ITA 2220 | 3 | 4”
  - … 26 more rows
### `5f31074f05986c7b` Florida College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://floridacollege.edu/academics/dual-enrollment/ (sha256 df099d61ec63)
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa", "per_credit_hour_charges"], "tiers": 3}
  - per_credit_hour_charge: 105 ⟵ “All classes are $105 per credit hour for all students. Take advantage of this affordable pricing for all courses.”
  - per_credit_hour_charge: 90 ⟵ “Members of the Hutchinson Bell will receive a discounted price of only $90 per credit hour.”
  - eligibility_tier: 3.0 ⟵ “Maintain GPA at high school (3.0 GPA) and college level (2.5 GPA)”
  - per_credit_hour_charge: 105 ⟵ “Pricing Rate………$105/credit hour”
  - eligibility_tier: 3.0 ⟵ “Minimum high school GPA of 3.0 (Unweighted)”
  - eligibility_tier: 3.0 ⟵ “To remain dual enrolled, a student must maintain a 3.0 high school GPA and a 2.5 Florida College GPA.*”
  - college_gpa_to_continue: 3.0 ⟵ “To remain dual enrolled, a student must maintain a 3.0 high school GPA and a 2.5 Florida College GPA.*”
### `2d23d1cb4bc0098c` Florida Gateway College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.fgc.edu/tuition-financial-aid/cost-of-attendance.html (sha256 99b5bd8981c9)
- checks: {"columns": 1, "rows": 8}
  - on_campus:Tuition & Fees: 3100.0 ⟵ “Tuition & Fees | $3,100.00 | $11,747.00”
  - on_campus:Housing Double Occupancy: 4000.0 ⟵ “Housing Double Occupancy | $4,000.00 | $4,000.00”
  - on_campus:Housing Single Occupancy: 4800.0 ⟵ “Housing Single Occupancy | $4,800.00 | $4,800.00”
  - on_campus:Food: 2700.0 ⟵ “Food | $2,700.00 | $2,700.00”
  - on_campus:Books, Course Materials, Supplies, And Equipment($1200 Allowance For Rental Or Purchase Of Computer To Be Included On A Case By Case Basis.): 1271.0 ⟵ “Books, Course Materials, Supplies, And Equipment($1200 Allowance For Rental Or Purchase Of Computer To Be Included On A Case By Case Basis.) | $1,271.00 | $1,271.00”
  - on_campus:Transportation: 625.0 ⟵ “Transportation | $625.00 | $1,625.00”
  - on_campus:Double Occupancy: 13756.0 ⟵ “Double Occupancy | $13,756.00 | $23,403.00”
  - on_campus:Single Occupancy: 14556.0 ⟵ “Single Occupancy | $14,556.00 | $24,203.00”
### `782b38ad63f53957` Florida Gateway College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.fgc.edu/tuition-financial-aid/cost-of-attendance.html (sha256 99b5bd8981c9)
- checks: {"columns": 1, "rows": 8}
  - on_campus:Tuition & Fees: 11747.0 ⟵ “Tuition & Fees | $3,100.00 | $11,747.00”
  - on_campus:Housing Double Occupancy: 4000.0 ⟵ “Housing Double Occupancy | $4,000.00 | $4,000.00”
  - on_campus:Housing Single Occupancy: 4800.0 ⟵ “Housing Single Occupancy | $4,800.00 | $4,800.00”
  - on_campus:Food: 2700.0 ⟵ “Food | $2,700.00 | $2,700.00”
  - on_campus:Books, Course Materials, Supplies, And Equipment($1200 Allowance For Rental Or Purchase Of Computer To Be Included On A Case By Case Basis.): 1271.0 ⟵ “Books, Course Materials, Supplies, And Equipment($1200 Allowance For Rental Or Purchase Of Computer To Be Included On A Case By Case Basis.) | $1,271.00 | $1,271.00”
  - on_campus:Transportation: 1625.0 ⟵ “Transportation | $625.00 | $1,625.00”
  - on_campus:Double Occupancy: 23403.0 ⟵ “Double Occupancy | $13,756.00 | $23,403.00”
  - on_campus:Single Occupancy: 24203.0 ⟵ “Single Occupancy | $14,556.00 | $24,203.00”
### `md05b161de13808f` Florida Gateway College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.fgc.edu/admissions-information/dual-enrollment-student/Public_and_Private_High_School_Students.html (sha256 1f6f4eaabfc9)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “A minimum unweighted high school GPA of 3.0 for college credit courses.”
  - eligibility_tier: 3.0 ⟵ “A minimum high school GPA of 3.0”
  - eligibility_tier: 3.0 ⟵ “a high school unweighted GPA of 3.0 to enroll in academic classes and a high school unweighted GPA of 2.0 to”
### `ecbe2a71e443418d` Florida Gulf Coast University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.fgcu.edu/admissionsandaid/undergraduateadmissions/transferadmissions (sha256 8c6ee921298a)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 60 ⟵ “Thirty (30) of the last 60 hours must be earned at FGCU to receive a baccalaureate degree from FGCU.”
### `3edcb4167b0b5d90` Florida International University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://onestop.fiu.edu/finances/estimate-your-costs/index.html (sha256 4ff478de0496)
- checks: {"columns": 1, "components_per_semester": true, "components_reconcile": true, "rows": 9}
  - column:Tuition: 10926 ⟵ “Tuition | $10,926”
  - column:Fees: 199 ⟵ “Fees | $199”
  - column:Direct Loan Origination Fee: 25 ⟵ “Direct Loan Origination Fee | $25”
  - column:Books & Supplies: 675 ⟵ “Books & Supplies | $675”
  - column:Housing: 5025 ⟵ “Housing | $5,025”
  - column:Food: 2595 ⟵ “Food | $2,595”
  - column:Transportation: 1515 ⟵ “Transportation | $1,515”
  - column:Personal: 1784 ⟵ “Personal | $1,784”
  - column:Total Annual: 45488 ⟵ “Total Annual | $45,488”
### `4a4cd827d0a65644` Florida International University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://onestop.fiu.edu/finances/estimate-your-costs/index.html (sha256 4ff478de0496)
- checks: {"columns": 1, "components_per_semester": true, "components_reconcile": true, "rows": 9}
  - column:Tuition: 3084 ⟵ “Tuition | $3,084”
  - column:Fees: 199 ⟵ “Fees | $199”
  - column:Direct Loan Origination Fee: 25 ⟵ “Direct Loan Origination Fee | $25”
  - column:Books & Supplies: 675 ⟵ “Books & Supplies | $675”
  - column:Housing: 5025 ⟵ “Housing | $5,025”
  - column:Food: 2595 ⟵ “Food | $2,595”
  - column:Transportation: 1515 ⟵ “Transportation | $1,515”
  - column:Personal: 1784 ⟵ “Personal | $1,784”
  - column:Total Annual: 29804 ⟵ “Total Annual | $29,804”
### `35e466292f5b62bf` Florida International University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://transfer.fiu.edu/transfer-101/credit-options/credit-by-exam-tables/ (sha256 1ee2a29e663f)
- checks: {"distinct_exams": 28, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-SL|BSC UCC1/L (3,1)]:  ⟵ “Biology Standard Level (SL) | BSC UCC1/L (3,1) | BSC UCC1/ UCC1L (3,1) | Natural Science with Lab*”
  - equivalencies[IB-BIOLOGY-HL|BSC UCC1/L (3,1) & BSC 2010/ 2010L (3,1)]:  ⟵ “Biology Higher Level (HL) | BSC UCC1/L (3,1) & BSC 2010/ 2010L (3,1) | BSC UCC1/ UCC1L (3,1) &BSC 2010/ 2010L (3,1) | Natural Science Groups 1&2 with Lab*”
  - equivalencies[IB-CHEMISTRY|CHM 1020/ 1020L (3,1)]:  ⟵ “Chemistry | CHM 1020/ 1020L (3,1) | CHM 1020/ 1020L (3, 1) &CHM 1045/ 1045L (3, 1) | Natural Science Group 1with Lab”
  - equivalencies[IB-COMPUTER-SCIENCE|CGS 2518 (3)]:  ⟵ “Computer Science | CGS 2518 (3) | CGS 2518 (3) & ELE UCC1 (3) | Mathematics Group 2”
  - equivalencies[IB-ECONOMICS|SOC UCC2 (3)]:  ⟵ “Economics | SOC UCC2 (3) | ECO 2013 (3) & ECO 2023 (3) | Social Science Groups 1&2”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|EVR 1001 (3)]:  ⟵ “Environmental Systems | EVR 1001 (3) | EVR 1001 (3) & ELE UCC1 (3) | Natural Science Group 1(No Lab)”
  - equivalencies[IB-GEOGRAPHY|GEA 2000 (3)]:  ⟵ “Geography | GEA 2000 (3) | GEA 2000 (3) & GEO 2200 (3) | Social Science Group 2”
  - equivalencies[IB-GLOBAL-POLITICS-SL|INR 2001 (3)]:  ⟵ “Global Politics (SL) | INR 2001 (3) | INR2001 (3) | Social Science Group 2”
  - equivalencies[IB-GLOBAL-POLITICS-HL|INR 2001 (3)]:  ⟵ “Global Politics (HL) | INR 2001 (3) | INR2001 & SOC UCC2 (3) | Social Science Group 2”
  - equivalencies[IB-HISTORY-SL|WOH 2001 (3)]:  ⟵ “History (SL) | WOH 2001 (3) | WOH 2001 (3), WIR UCC1 & ELE UCC1 (3) | Humanities Group 2(& 1WIR with score of 5-7)+”
  - equivalencies[IB-HISTORY-HL|WOH 2001 (3)]:  ⟵ “History (HL): History of Africa and the Middle East | WOH 2001 (3) | WOH 2001 (3), WIR UCC1 & ELE UCC1 (3) | Humanities Group 2(& 1WIR with score of 5-7)+”
  - equivalencies[IB-HISTORY-HL|WOH 2001 (3)]:  ⟵ “History (HL): History of the Americas | WOH 2001 (3) | WOH 2001 (3) & AMH 2020 or AMH 2010 (3), WIR UCC1 & CIV UCC1 | Humanities Group 2(& Social Science Group 1, 1WIR , and Civic Literacy course with score of 5-7)**+”
  - equivalencies[IB-HISTORY-HL|WOH 2001 (3)]:  ⟵ “History (HL): History of Asia and Oceania | WOH 2001 (3) | WOH 2001 (3) & WIR UCC1 & ELE UCC1 (3) | Humanities Group 2 (1WIR)+”
  - equivalencies[IB-HISTORY|HUM UCC2 (3)]:  ⟵ “Islamic History | HUM UCC2 (3) | HUM UCC2(3) & ELE UCC1 (3) | Humanities Group 2”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|MAC 1105 (3)]:  ⟵ “Math Analysis & Approaches (SL) | MAC 1105 (3) | MAC1105 (3) & MAC1140 (3) | Mathematics Groups 1&2”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|MAC1105 (3)]:  ⟵ “Math Analysis & Approaches (HL) | MAC1105 (3) | MAC1105 (3) & MAC1147 (4) | Mathematics Groups 1&2”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-SL|MAC1105 (3)]:  ⟵ “Math Applications & Interpretations (SL) | MAC1105 (3) | MAC1105 (3) & MAC1140 (3) | Mathematics Groups 1&2”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|MAC1140 (3)]:  ⟵ “Math Applications & Interpretations (HL) | MAC1140 (3) | MAC1140 (3) & STA2023(3) | Mathematics Groups 1&2”
  - equivalencies[IB-MUSIC|MUL 1010 (3)]:  ⟵ “Music | MUL 1010 (3) | MUL 1010 (3) & ELE UCC1 (3) | Humanities Group 1”
  - equivalencies[IB-PHILOSOPHY|PHI 2010 (3)]:  ⟵ “Philosophy | PHI 2010 (3) | PHI 2010 (3) & WIR UCC1 & ELE UCC1 (3) | Humanities Group 1 (1WIR)”
  - equivalencies[IB-PHYSICS-SL|PHY 1020/1020L (3,1)]:  ⟵ “Physics Standard Level (SL) | PHY 1020/1020L (3,1) | PHY 1020/1020L (3,1) | Natural Science Group 1(with Lab)*”
  - equivalencies[IB-PHYSICS-HL|PHY 1020/1020L (3,1) &PHY2053/2048L (4,1)]:  ⟵ “Physics Higher Level (HL) | PHY 1020/1020L (3,1) &PHY2053/2048L (4,1) | PHY 2053/ 2048L (4,1) &PHY 2054/ 2049L (4,1) | Natural Sciences Groups 1&2 (with Lab)*”
  - equivalencies[IB-PSYCHOLOGY|PSY 2012 (3)]:  ⟵ “Psychology | PSY 2012 (3) | PSY 2012 (3) & ELE UCC1 (3) | Social Science Group 1”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|SOC UCC2 (3)]:  ⟵ “Social and Cultural Anthropology | SOC UCC2 (3) | SOC UCC2 (3) & ELE UCC1 (3) | Social Science Group 2”
  - equivalencies[IB-THEATRE|THE 2000 (3)]:  ⟵ “Theatre Arts | THE 2000 (3) | THE 2000 (3) & ELE UCC1 (3) | Humanities Group 1”
  - … 9 more rows
### `6ca7b0644c64c68b` Florida International University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://transfer.fiu.edu/transfer-101/credit-options/credit-by-exam-tables/ (sha256 1ee2a29e663f)
- checks: {"distinct_exams": 28, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|ARH 2000 (3)]:  ⟵ “Art History | ARH 2000 (3) | ARH 2000 (3) &ARH 2050++ (3) | ARH 2000 (3) &ARH 2050++ (3) | Humanities Group 1 (& Arts with score of 4-5)”
  - equivalencies[AP-BIOLOGY|BSC UCC1/ UCC1L (3,1)]:  ⟵ “Biology | BSC UCC1/ UCC1L (3,1) | BSC 2010/ 2010L (3,1) | BSC 2010/ 2010L (3,1) & BSC 2011/ 2011L (3,1) | Natural Science Group 1(& Natural Science Group 2 with score of 5)”
  - equivalencies[AP-CALCULUS-AB|MAC 2311 (4)]:  ⟵ “Calculus AB | MAC 2311 (4) | MAC 2311 (4) | MAC 2311 (4) | Mathematics Group 1”
  - equivalencies[AP-CALCULUS-BC|MAC 2311 (4)]:  ⟵ “Calculus BC | MAC 2311 (4) | MAC 2311 (4)&MAC 2312 (4) | MAC 2311 (4)&MAC 2312 (4) | Mathematics Group 1(& Mathematics Group 2 with score of 4-5)”
  - equivalencies[AP-CHEMISTRY|CHM 1020/ 1020L (3, 1)]:  ⟵ “Chemistry | CHM 1020/ 1020L (3, 1) | CHM 1045/ 1045L (3,1) | CHM 1045/ 1045L (3,1) & CHM 1046/ 1046L (3,1) | Natural Science Group 1”
  - equivalencies[AP-COMPUTER-SCIENCE-A|ELE UCC1 (3)]:  ⟵ “Computer Science A | ELE UCC1 (3) | COP 2210 (4) | COP 2210 (4) | Mathematics Group 1 with score 4-5”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|NPM UCC1 (3)]:  ⟵ “Computer Science Principles | NPM UCC1 (3) | NPM UCC1 (3) | NPM UCC1 (3) | Mathematics Group 2”
  - equivalencies[AP-MACROECONOMICS|ECO 2013 (3)]:  ⟵ “Economics: Macro | ECO 2013 (3) | ECO 2013 (3) | ECO 2013 (3) | Social Science Group 1”
  - equivalencies[AP-MICROECONOMICS|ECO 2023 (3)]:  ⟵ “Economics: Micro | ECO 2023 (3) | ECO 2023 (3) | ECO 2023 (3) | Social Science Group 2”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|ENC 1101 (3)]:  ⟵ “English Language and Composition | ENC 1101 (3) | ENC 1101 (3)&ENC 1102 (3) | ENC 1101 (3)&ENC 1102 (3) | Communication”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|ENC 1101 (3)1]:  ⟵ “English Literature and Composition | ENC 1101 (3)1 | ENC 1101 (3)&ENC 1102 (3)1 | ENC 1101 (3)&ENC 1102 (3)1 | Communication (or Humanities Group 1)”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|EVR 1001 (3)]:  ⟵ “Environmental Science | EVR 1001 (3) | EVR 1001 (3) | EVR 1001 (3) | Natural Science Group 1 (No lab)”
  - equivalencies[AP-EUROPEAN-HISTORY|EUH 2030 (3) & WIR UCC1]:  ⟵ “European History | EUH 2030 (3) & WIR UCC1 | EUH 2030 (3)&ELE UCC1 (3)&WIR UCC1 | EUH 2030 (3)&ELE UCC1 (3)&WIR UCC1) | Humanities Group 2 (WIR)”
  - equivalencies[AP-HUMAN-GEOGRAPHY|GEO 2000 (3)]:  ⟵ “Human Geography | GEO 2000 (3) | GEO 2000 (3) | GEO 2000 (3) | Social Science Group 2”
  - equivalencies[AP-PHYSICS-1|PHY 2053/ 2048L (4,1)]:  ⟵ “Physics 1 | PHY 2053/ 2048L (4,1) | PHY 2053/ 2048L (4,1) | PHY 2053/ 2048L (4,1) | Natural Sciences Group 1”
  - equivalencies[AP-PHYSICS-2|PHY 2054/ 2049L (4,1)]:  ⟵ “Physics 2 | PHY 2054/ 2049L (4,1) | PHY 2054/ 2049L (4,1) | PHY 2054/ 2049L (4,1) | Natural Science Group 2”
  - equivalencies[AP-PHYSICS-C-MECHANICS|PHY 2053/ 2048L (4,1)]:  ⟵ “Physics C: Mechanics | PHY 2053/ 2048L (4,1) | PHY 2048/ 2048L (4,1) | PHY 2048/ 2048L (4,1) | Natural Science Group 1”
  - equivalencies[AP-PRECALCULUS|MAC 1140 (3)]:  ⟵ “Precalculus | MAC 1140 (3) | MAC1140 &MAC1114 (6) | MAC1140 &MAC1114 (6) | Mathematics Group 2”
  - equivalencies[AP-PSYCHOLOGY|PSY 2012 (3)]:  ⟵ “Psychology | PSY 2012 (3) | PSY 2012 (3) | PSY 2012 (3) | Social Science Group 1”
  - equivalencies[AP-STATISTICS|STA 2023 (3)]:  ⟵ “Statistics | STA 2023 (3) | STA 2023(3) | STA 2023 (3) | Mathematics Group 1”
  - equivalencies[AP-UNITED-STATES-HISTORY|SOC UCC1 (3)]:  ⟵ “United States History | SOC UCC1 (3) | AMH 2020 (3)&AMH 2010 (3)& WIR UCC1 | AMH 2020 (3)&AMH 2010 (3)& WIR UCC1 | Social Science Group 1 with score of 3(& 1WIR and Civics with score of 4-5). Students who achieve a score of 4-5 and receive credit for AMH 2020/AMH 2010 will have met the Civic Literac”
  - equivalencies[AP-WORLD-HISTORY-MODERN|WOH 2001 (3)& WIR UCC1]:  ⟵ “World History: Modern | WOH 2001 (3)& WIR UCC1 | WOH 2001 (3)& WIR UCC1 | WOH 2001 (3)& WIR UCC1 | Humanities Group 2 (1WIR)”
  - equivalencies[AP-LATIN|LAT 2200 (3)]:  ⟵ “Latin | LAT 2200 (3) | LAT 2200 (3) | LAT 2200 (3) | Foreign Language”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|XXX 2200 (3)]:  ⟵ “Modern Language & Culture: Chinese, French, German, Italian, Japanese, Russian, Spanish | XXX 2200 (3) | XXX 2200 (6) | XXX 2200 (6) | Foreign Language”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|XXX 2200 (3)]:  ⟵ “Modern Language: Literature (French, Latin) | XXX 2200 (3) | XXX 2200 (3) & ELEUCC1 (3) | XXX 2200 (3) & ELEUCC1 (3) | Foreign Language”
  - … 7 more rows
### `738b215c22bb9880` Florida Southern College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.flsouthern.edu/admissions/undergraduate/undergraduate-tuition-and-costs (sha256 47186a3bfa0c)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 47670 ⟵ “Tuition and Fees | $47,670”
  - column:Food and Housing: 15130 ⟵ “Food and Housing | $15,130”
  - column:Total: 62800 ⟵ “Total | $62,800”
### `f15dc7267de25d3a` Florida State University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://admissions.fsu.edu/transfer/credit/ap (sha256 3c3f7807085d)
- checks: {"distinct_exams": 30, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|ART 1201C (3)]:  ⟵ “2-D ART & DESIGN | ART 1201C (3) | Same as 3 | Same as 3”
  - equivalencies[AP-3-D-ART-DESIGN|ART 1203 (3)]:  ⟵ “3-D ART & DESIGN | ART 1203 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-ART-HISTORY|ARH 2000 (3)]:  ⟵ “ART HISTORY | ARH 2000 (3) | ARH 2000 (3)ARH 2050 (3) | Same as 4”
  - equivalencies[AP-BIOLOGY|BSC 1005 (3)BSC 1005L (1)]:  ⟵ “BIOLOGY | BSC 1005 (3)BSC 1005L (1) | BSC 2010 (3)BSC 2010L (1) | BSC 2010 (3)BSC 2010L (1)BSC 2011 (3)BSC 2011L (1)”
  - equivalencies[AP-CHEMISTRY|CHM 1020 (3)CHM 1020L (1)]:  ⟵ “CHEMISTRY | CHM 1020 (3)CHM 1020L (1) | CHM 1045 (3)CHM 1045L (1) | CHM 1045 (3)CHM 1045L (1)CHM 1046 (3)CHM 1046L (1)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|CHI 2220 (4)]:  ⟵ “CHINESE LANGUAGE & CULTURE | CHI 2220 (4) | CHI 2220 (4)CHI 2300 (4) | Same as 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|CGS 2060 (3)]:  ⟵ “COMPUTER SCIENCE A | CGS 2060 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|CGS 1000 (3)]:  ⟵ “COMPUTER SCIENCE PRINCIPLES | CGS 1000 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-DRAWING|ART 1300C (3)]:  ⟵ “DRAWING | ART 1300C (3) | Same as 3 | Same as 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|EVR 1001 (3)]:  ⟵ “ENVIRONMENTAL SCIENCE | EVR 1001 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-EUROPEAN-HISTORY|EUH 1009 (3)]:  ⟵ “EUROPEAN HISTORY | EUH 1009 (3) | EUH 2000 (3)EUH 2001 (3) | Same as 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|FRE 2220 (4)]:  ⟵ “FRENCH - LANGUAGE & CULTURE | FRE 2220 (4) | FRE 2220 (4)FRE 3420 (3) | Same as 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|GER 2220 (4)]:  ⟵ “GERMAN - LANGUAGE & CULTURE | GER 2220 (4) | GER 2220 (4)GER 2221 (4) | Same as 4”
  - equivalencies[AP-HUMAN-GEOGRAPHY|GEO 1400 (3)]:  ⟵ “HUMAN GEOGRAPHY | GEO 1400 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|ITA 2220 (4)]:  ⟵ “ITALIAN LANGUAGE & CULTURE | ITA 2220 (4) | ITA 2220 (4)ITA 2240 (3) | Same as 4”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|JPN 2220 (4)]:  ⟵ “JAPANESE LANGUAGE & CULTURE | JPN 2220 (4) | JPN 2220 (4)JPN 2300 (4) | Same as 4”
  - equivalencies[AP-LATIN|LNW 3211 (3)]:  ⟵ “LATIN | LNW 3211 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-MACROECONOMICS|ECO 2013 (3)]:  ⟵ “MACROECONOMICS | ECO 2013 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-MICROECONOMICS|ECO 2023 (3)]:  ⟵ “MICROECONOMICS | ECO 2023 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-MUSIC-THEORY|MUT 1001 (3)]:  ⟵ “MUSIC THEORY (if composite score is 3 or higher) | MUT 1001 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-MUSIC-THEORY|MUT 1111 (3)MUT 1241 (1)]:  ⟵ “MUSIC THEORY (if both aural and non-aural subscores are 3 or higher) | MUT 1111 (3)MUT 1241 (1) | Same as 3 | Same as 3”
  - equivalencies[AP-PHYSICS-1|PHY 2053C (4)]:  ⟵ “PHYSICS 1 | PHY 2053C (4) | Same as 3 | Same as 3”
  - equivalencies[AP-PHYSICS-2|PHY 2054C (4)]:  ⟵ “PHYSICS 2 | PHY 2054C (4) | Same as 3 | Same as 3”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|PHY 2054C (4)]:  ⟵ “PHYSICS C - ELECTRICITY & MAGNETISM | PHY 2054C (4) | PHY 2049C (5) | Same as 4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|PHY 2053C (4)]:  ⟵ “PHYSICS C - MECHANICS | PHY 2053C (4) | PHY 2048C (5) | Same as 4”
  - … 7 more rows
### `bd4d0404fcbab197` Jacksonville University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ju.edu/financialservices/tuition/adult.php (sha256 26e5e017c766)
- checks: {"columns": 1, "rows": 2}
  - column:Tuition (Full Program Cost): 70000 ⟵ “Tuition (Full Program Cost) | $70,000”
  - column:Subscription Fee (One-time fee): 2000 ⟵ “Subscription Fee (One-time fee) | $2,000”
### `aab1ffd14d05b8ac` Jacksonville University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ju.edu/admissions/transfer/transfer-student-faq.php (sha256 3f2908e0924d)
- checks: {"fields": ["max_transfer_credits", "min_grade", "residency_requirement_credits"]}
  - min_grade: C ⟵ “Academic courses completed at institutions which are approved by a regional accrediting agency are acceptable in transfer provided they are comparable to courses offered at JU and were completed with a grade of “C” (2.0) or better.”
  - max_transfer_credits: 60 ⟵ “A maximum of 60 semester hours of transfer credit will be accepted from community college.”
  - residency_requirement_credits: 30 ⟵ “The final 30 semester hours toward a bachelor’s degree must be completed at Jacksonville University.”
### `m9449ff47dda6b4c` Johnson University Florida — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://johnsonu.edu/admissions/dual-enrollment-students-how-to-apply/online/ (sha256 fdc081e5ff6d)
- checks: {"fields": ["per_credit_hour_charges"], "merged_pages": 2, "tiers": 0}
  - per_credit_hour_charge: 179.55 ⟵ “The cost for a dual enrollment course is $179.55 per credit, or $538.65 for a typical 3-credit course. The Tennessee Dual Enrollment Grant currently pays $538.65 per course for the first five courses and $100 per credit for courses 6-10. Click here to learn more about the grant!”
  - per_credit_hour_charge: 100 ⟵ “The cost for a dual enrollment course is $179.55 per credit, or $538.65 for a typical 3-credit course. The Tennessee Dual Enrollment Grant currently pays $538.65 per course for the first five courses and $100 per credit for courses 6-10. Click here to learn more about the grant!”
  - per_credit_hour_charge: 184 ⟵ “The cost is $184 per credit or $552 for a 3-credit course. The Tennessee Dual Enrollment Grant pays $554.40 per course for the first five courses.”
### `5f0f54767871484a` Miami Dade College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.mdc.edu/financialaid/scholarships/american-dream.aspx (sha256 64f1e5e36724)
- checks: {"thresholds": null}
  - test_requirement: ACT ≥ 19 / SAT ≥ 24 ⟵ “Mathematics | ≥ 19 | ≥ 24 | > 480 | ≥114 | > 16 | ≥242 (QAS is used) | ≥261 (QAS is used)”
### `7b8aa296b206ca5d` Miami Dade College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.mdc.edu/financialaid/scholarships/american-dream.aspx (sha256 64f1e5e36724)
- checks: {"thresholds": null}
  - test_requirement: ACT ≥ 17 / SAT ≥ 25 (Writing and Language) ⟵ “Writing | ≥ 17 | ≥ 25 (Writing and Language) | Evidence-Based Reading and Writing > 490 | ≥ 103 | Verbal Reasoning + Grammar/Writing Sections > 38 | ≥245 | ≥253”
### `bab61839f8eb3ce9` Miami Dade College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.mdc.edu/financialaid/scholarships/american-dream.aspx (sha256 64f1e5e36724)
- checks: {"thresholds": null}
  - test_requirement: ACT ≥ 19 / SAT ≥ 24 ⟵ “Reading | ≥ 19 | ≥ 24 | Evidence-Based Reading and Writing > 490 | ≥106 | Verbal Reasoning + Grammar/Writing Sections > 38 | ≥245 | ≥256”
### `a67f7fb0e3d5b2e4` New College of Florida — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ncf.edu/admissions/first-year-students/tuition-fees/ (sha256 36b292077276)
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition & Fees: 32471 ⟵ “Tuition & Fees | $6,724 | $32,471”
  - on_campus:Housing: 9450 ⟵ “Housing | $9,450 | $9,450”
  - on_campus:Food: 5084 ⟵ “Food | $5,084 | $5,084”
  - on_campus:Billable Costs Subtotal:: 47005 ⟵ “Billable Costs Subtotal: | $21,258 | $47,005”
  - on_campus:Books, Supplies & Course Materials: 1200 ⟵ “Books, Supplies & Course Materials | $1,200 | $1,200”
  - on_campus:Personal Expenses: 2170 ⟵ “Personal Expenses | $2,170 | $2,170”
  - on_campus:Transportation: 1100 ⟵ “Transportation | $1,100 | $1,100”
  - on_campus:Additional Food Allowance: 470 ⟵ “Additional Food Allowance | $470 | $470”
  - on_campus:Non-Billable Costs Subtotal: 4940 ⟵ “Non-Billable Costs Subtotal | $4,940 | $4,940”
  - on_campus:Estimated Total Cost of Attendance (COA): 51945 ⟵ “Estimated Total Cost of Attendance (COA) | $26,198 | $51,945”
### `f80f6fac612b3c55` New College of Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ncf.edu/admissions/first-year-students/tuition-fees/ (sha256 36b292077276)
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition & Fees: 6724 ⟵ “Tuition & Fees | $6,724 | $32,471”
  - on_campus:Housing: 9450 ⟵ “Housing | $9,450 | $9,450”
  - on_campus:Food: 5084 ⟵ “Food | $5,084 | $5,084”
  - on_campus:Billable Costs Subtotal:: 21258 ⟵ “Billable Costs Subtotal: | $21,258 | $47,005”
  - on_campus:Books, Supplies & Course Materials: 1200 ⟵ “Books, Supplies & Course Materials | $1,200 | $1,200”
  - on_campus:Personal Expenses: 2170 ⟵ “Personal Expenses | $2,170 | $2,170”
  - on_campus:Transportation: 1100 ⟵ “Transportation | $1,100 | $1,100”
  - on_campus:Additional Food Allowance: 470 ⟵ “Additional Food Allowance | $470 | $470”
  - on_campus:Non-Billable Costs Subtotal: 4940 ⟵ “Non-Billable Costs Subtotal | $4,940 | $4,940”
  - on_campus:Estimated Total Cost of Attendance (COA): 26198 ⟵ “Estimated Total Cost of Attendance (COA) | $26,198 | $51,945”
### `50fbfea3ac2a6126` New College of Florida — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ncf.edu/admissions/transfer-students/transfer-credit/ap-credit-chart/ (sha256 5c7bc491f873)
- checks: {"distinct_exams": 29, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|ART 1201C (3)]:  ⟵ “2-D ART & DESIGN | ART 1201C (3) | Same as 3 | Same as 3”
  - equivalencies[AP-3-D-ART-DESIGN|ART 1203 (3)]:  ⟵ “3-D ART & DESIGN | ART 1203 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-ART-HISTORY|ARH 2000 (3)]:  ⟵ “ART HISTORY | ARH 2000 (3) | ARH 2000 (3)ARH 2050 (3) | Same as 4”
  - equivalencies[AP-BIOLOGY|BSC 1005 (3)BSC 1005L (1)]:  ⟵ “BIOLOGY | BSC 1005 (3)BSC 1005L (1) | BSC 2010 (3)BSC 2010L (1) | BSC 2010 (3)BSC 2010L (1)BSC 2011 (3)BSC 2011L (1)”
  - equivalencies[AP-CHEMISTRY|CHM 1020 (3)CHM 1020L (1)]:  ⟵ “CHEMISTRY | CHM 1020 (3)CHM 1020L (1) | CHM 1045 (3)CHM 1045L (1) | CHM 1045 (3)CHM 1045L (1)CHM 1046 (3)CHM 1046L (1)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|CHI 2220 (4)]:  ⟵ “CHINESE LANGUAGE & CULTURE | CHI 2220 (4) | CHI 2220 (4)CHI 2300 (4) | Same as 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|CGS 2060 (3)]:  ⟵ “COMPUTER SCIENCE A | CGS 2060 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|CGS 1000 (3)]:  ⟵ “COMPUTER SCIENCE PRINCIPLES | CGS 1000 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-DRAWING|ART 1300C (3)]:  ⟵ “DRAWING | ART 1300C (3) | Same as 3 | Same as 3”
  - equivalencies[AP-MACROECONOMICS|ECO 2013 (3)]:  ⟵ “ECONOMICS – MACRO | ECO 2013 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-MICROECONOMICS|ECO 2023 (3)]:  ⟵ “ECONOMICS – MICRO | ECO 2023 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|GEO1330 (3)]:  ⟵ “ENVIRONMENTAL SCIENCE | GEO1330 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-EUROPEAN-HISTORY|EUH 1009 (3)]:  ⟵ “EUROPEAN HISTORY | EUH 1009 (3) | EUH 2000 (3)EUH 2001 (3) | Same as 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|FRE 2220 (4)]:  ⟵ “FRENCH – LANGUAGE & CULTURE | FRE 2220 (4) | FRE 2220 (4)FRE 3420 (3) | Same as 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|FRW 3100 (3)]:  ⟵ “FRENCH – LITERATURE | FRW 3100 (3) | FRW 3100 (3)FRW 3101 (3) | Same as 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|GER 2220 (4)]:  ⟵ “GERMAN – LANGUAGE & CULTURE | GER 2220 (4) | GER 2220 (4)GER 2221 (4) | Same as 4”
  - equivalencies[AP-HUMAN-GEOGRAPHY|GEO 1400 (3)]:  ⟵ “HUMAN GEOGRAPHY | GEO 1400 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|ITA 2220 (4)]:  ⟵ “ITALIAN LANGUAGE & CULTURE | ITA 2220 (4) | ITA 2220 (4)ITA 2240 (3) | Same as 4”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|JPN 2220 (4)]:  ⟵ “JAPANESE LANGUAGE & CULTURE | JPN 2220 (4) | JPN 2220 (4)JPN 2300 (4) | Same as 4”
  - equivalencies[AP-LATIN|LNW 3211 (3)]:  ⟵ “LATIN | LNW 3211 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-MUSIC-THEORY|MUT 1001 (3)]:  ⟵ “MUSIC THEORY (if composite score is 3 or higher) | MUT 1001 (3) | Same as 3 | Same as 3”
  - equivalencies[AP-MUSIC-THEORY|MUT 1111 (3)MUT 1241 (1)]:  ⟵ “MUSIC THEORY (if both aural and non-aural subscores are 3 or higher) | MUT 1111 (3)MUT 1241 (1) | Same as 3 | Same as 3”
  - equivalencies[AP-PHYSICS-1|PHY 2053C (4)]:  ⟵ “PHYSICS 1 | PHY 2053C (4) | Same as 3 | Same as 3”
  - equivalencies[AP-PHYSICS-2|PHY 2054C (4)]:  ⟵ “PHYSICS 2 | PHY 2054C (4) | Same as 3 | Same as 3”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|PHY 2054C (4)]:  ⟵ “PHYSICS C – ELECTRICITY & MAGNETISM | PHY 2054C (4) | PHY 2049C (5) | Same as 4”
  - … 7 more rows
### `52581d0fc646512c` New College of Florida — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.ncf.edu/admissions/transfer-students/transfer-credit/ib-credit-chart/ (sha256 c2f9221ded00)
- checks: {"distinct_exams": 33, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|4 credits]:  ⟵ “Biology | 4 credits | 8 credits”
  - equivalencies[IB-BIOLOGY-SL|4 credits]:  ⟵ “Biology (SL) | 4 credits | 8 credits”
  - equivalencies[IB-BIOLOGY-HL|4 credits]:  ⟵ “Biology (HL) | 4 credits | 8 credits”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4 credits]:  ⟵ “Business and Management | 4 credits | 8 credits”
  - equivalencies[IB-CHEMISTRY|4 credits]:  ⟵ “Chemistry | 4 credits | 8 credits”
  - equivalencies[IB-COMPUTER-SCIENCE|4 credits]:  ⟵ “Computer Science | 4 credits | 8 credits”
  - equivalencies[IB-ECONOMICS|4 credits]:  ⟵ “Economics | 4 credits | 8 credits”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|4 credits]:  ⟵ “Environmental Systems & Societies (SL) | 4 credits | 8 credits”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4 credits]:  ⟵ “Environmental Systems | 4 credits | 8 credits”
  - equivalencies[IB-FILM|4 credits]:  ⟵ “Film Studies | 4 credits | 8 credits”
  - equivalencies[IB-FRENCH|4 credits]:  ⟵ “French: Language B | 4 credits | 8 credits”
  - equivalencies[IB-GEOGRAPHY|4 credits]:  ⟵ “Geography | 4 credits | 8 credits”
  - equivalencies[IB-GERMAN|4 credits]:  ⟵ “German: Language B | 4 credits | 8 credits”
  - equivalencies[IB-GLOBAL-POLITICS-SL|4 credits]:  ⟵ “Global Politics (SL) | 4 credits | 8 credits”
  - equivalencies[IB-GLOBAL-POLITICS-HL|4 credits]:  ⟵ “Global Politics (HL) | 4 credits | 8 credits”
  - equivalencies[IB-HISTORY|4 credits]:  ⟵ “History | 4 credits | 8 credits”
  - equivalencies[IB-HISTORY-SL|4 credits]:  ⟵ “History (SL) | 4 credits | 8 credits”
  - equivalencies[IB-HISTORY-HL|4 credits]:  ⟵ “History (HL): History of Africa and the Middle East | 4 credits | 8 credits”
  - equivalencies[IB-LATIN|4 credits]:  ⟵ “Latin | 4 credits | 8 credits”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|4 credits]:  ⟵ “Math Analysis and Approaches (SL) | 4 credits | 8 credits”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|4 credits]:  ⟵ “Math Applications and Interpretations (HL) | 4 credits | 8 credits”
  - equivalencies[IB-MUSIC|4 credits]:  ⟵ “Music | 4 credits | 8 credits”
  - equivalencies[IB-PHILOSOPHY|4 credits]:  ⟵ “Philosophy | 4 credits | 8 credits”
  - equivalencies[IB-PHYSICS|4 credits]:  ⟵ “Physics | 4 credits | 8 credits”
  - equivalencies[IB-PHYSICS-SL|4 credits]:  ⟵ “Physics (SL) | 4 credits | 8 credits”
  - … 8 more rows
### `e725c539c62cfc6e` New College of Florida — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ncf.edu/admissions/transfer-students/transfer-application-process/ (sha256 79065b81cd6e)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “SAT, ACT, or CLT scores (self-reported on STAR), or possess 30+ transferable semester hours and have completed with a grade of “C” or better both a college level math and English course.”
  - min_grade: C ⟵ “New College accepts transferable coursework related to areas of study offered at New College with a grade of C or better, which is non-developmental.”
### `8345947ed2e2a93b` North Florida College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.nfc.edu:443/admissions/testing/clep-exam-list (sha256 f2a10d35f6be)
- checks: {"distinct_exams": 27, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Intro. to Business Law | 50 | 3 Hours | BUL 2241”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro. to Educational Psychology | 50 | 3 Hours | EDP 2002”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 Hours | ACG 1001”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 50 | 3 Hours | CGS 1077”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 Hours | MAN 2021”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 3 Hours | MAR 2011”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 6 Hours | ENC 1101 & 1102”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French, Level I | 50 | 3 Hours | AA elective credit”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French, Level II | 59 | 6 Hours | AA elective credit”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German, Level I | 50 | 3 Hours | AA elective credit”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German, Level II | 60 | 6 Hours | AA elective credit”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish, Level I | 50 | 4 Hours | SPN 1120”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish, Level II | 63 | 8 Hours | SPN 1120 & 1121”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 Hours | AML 1000”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 Hours | ENL 1000”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 Hours | HUM 2235 or 2250”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 Hours | MGF 1130”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 Hours | MAC 1105”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 3 Hours | MAC 2233”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 3 Hours | MAC 2140”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 3 Hours | BSC 1005 (no lab)”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 3 Hours | CHM 1020 or 1025 (no lab)”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government (this CLEP exam satisfies Civic Literacy course and assessment requirements) | 50 | 3 hours | POS 2041”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | 3 hours | DEP 2004”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics | 50 | 3 hours | ECO 2013”
  - … 12 more rows
### `49b8a2f887565f2e` Nova Southeastern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nova.edu/financial-aid/grants-scholarships/undergraduate.html (sha256 5da41af1eee7)
- checks: {"thresholds": null}
  - award_amount_text: 2.75 ⟵ “Minimum Cumulative GPA (unrounded and unweighted) | 3.0* | 2.75 | 2.75”
### `d20bb5dd17048b4d` Nova Southeastern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nova.edu/financial-aid/grants-scholarships/undergraduate.html (sha256 5da41af1eee7)
- checks: {"thresholds": null}
  - award_amount_text: 9 semester** (earned hours) ⟵ “Minimum Hours Required Per Term, if funded Three-quarter Time (9-11 hours) | 9 semester** (earned hours) | 9 semester** (earned hours) | 9 semester** (earned hours)”
### `fb358e9c7b6fd638` Nova Southeastern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nova.edu/financial-aid/grants-scholarships/undergraduate.html (sha256 5da41af1eee7)
- checks: {"thresholds": null}
  - award_amount_text: 12 semester** (earned hours) ⟵ “Minimum Hours Required Per Term if funded Full Time (12+ hours) | 12 semester** (earned hours) | 12 semester** (earned hours) | 12 semester** (earned hours)”
### `ff0380297b3b97ae` Nova Southeastern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nova.edu/financial-aid/grants-scholarships/undergraduate.html (sha256 5da41af1eee7)
- checks: {"thresholds": null}
  - award_amount_text: 6 semester** (earned hours) ⟵ “Minimum Hours Required Per Term, if funded Half Time (6-8 hours) | 6 semester** (earned hours) | 6 semester** (earned hours) | 6 semester** (earned hours)”
### `377a2b6d730b5319` Nova Southeastern University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://undergrad.nova.edu/admissions/transfer/transfer-advantage.html (sha256 c6dbe81a49ab)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “For TAP applicants, a grade of C or higher must be earned for an equivalent transfer course.”
### `6607801d87d56a6e` Pasco-Hernando State College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://accelerated.phsc.edu/transfer/springfield (sha256 94ea67733010)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Generally, courses taken at regionally accredited institutions that are 100-level or higher in which students earned a grade of C- or better will transfer to Springfield College as well as credits earned on joint service transcripts.”
### `e9f10830d368f469` Pensacola State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://pensacolastate.edu/academics/programs/dual-enrollment/ (sha256 70cdf71d8833)
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa"], "tiers": 3}
  - eligibility_tier: 3.0 ⟵ “Students intending to enroll in college credit courses must have an unweighted high school grade point average of 3.0 or above.”
  - eligibility_tier: 2.0 ⟵ “Students intending to enroll in a career and technical certificate program leading to an industry certification or applied technology diploma must have an unweighted high school grade point average of 2.0 or higher.”
  - college_gpa_to_continue: 2.5 ⟵ “Maintain a college GPA of 2.5 or higher.”
  - eligibility_tier: 3.0 ⟵ “Maintain an unweighted high school GPA of 3.0 or higher to take undergraduate-level courses and 2.0 or higher for vocational courses.”
  - college_gpa_to_continue: 2.5 ⟵ “Maintain a college GPA of 2.5 or higher.”
  - eligibility_tier: 3.0 ⟵ “Maintain an unweighted high school GPA of 3.0 or higher to take undergraduate-level courses and 2.0 or higher for vocational courses.”
### `bfb5ea0860d0d024` Polk State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.polk.edu/admission-aid/dual-enrollment-early-admission/seven-steps-to-admission-for-dual-enrolled-and-early-admission-students/ (sha256 1929f8249e51)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 3}
  - max_credit_hours_per_term: 11 ⟵ “Dual Enrollment — (taking up to 11 credits per term as a part-time student while in grades 6-12)”
  - eligibility_tier: 3.0 ⟵ “Unweighted high school GPA of 3.0”
  - eligibility_tier: 3.2 ⟵ “Unweighted high school GPA of 3.2”
  - eligibility_tier: 3.0 ⟵ “An unweighted high school GPA of 3.0 and an approved alternative method, which includes:”
### `4ec75026eb3ad597` Ringling College of Art and Design — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://catalog.ringling.edu/advanced-placement-ap-equivalency-chart (sha256 aedfc5e07e4c)
- checks: {"distinct_exams": 35, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3**]:  ⟵ “2-D Art and Design | 3** | Open Elective”
  - equivalencies[AP-3-D-ART-DESIGN|3**]:  ⟵ “3-D Art and Design | 3** | Open Elective”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | ARTH 111”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | Scientific Practices”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | Scientific Practices”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | Scientific Practices”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | Scientific Practices”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3*]:  ⟵ “Chinese Language and Culture | 3* | General Education Elective”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | 3 | General Education Elective”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | Open Elective”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | Open Elective”
  - equivalencies[AP-DRAWING|3**]:  ⟵ “Drawing | 3** | Open Elective”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | WRIT 151”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language and Composition | 4 | WRIT 151 & WRIT elective (6 cr)”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | Literature and Media Studies”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | Scientific Practices”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | General Education Elective”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3*]:  ⟵ “French Language and Culture | 3* | General Education Elective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3*]:  ⟵ “German Language and Culture | 3* | General Education Elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | Social and Behavioral Sciences”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3*]:  ⟵ “Italian Language and Culture | 3* | General Education Elective”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3*]:  ⟵ “Japanese Language and Culture | 3* | General Education Elective”
  - equivalencies[AP-LATIN|3*]:  ⟵ “Latin | 3* | General Education Elective”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | General Education Elective”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | General Education Elective”
  - … 11 more rows
### `ab00b5baa180f01f` Ringling College of Art and Design — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://catalog.ringling.edu/international-baccalaureate-ib-equivalency-chart (sha256 be40867ee6bf)
- checks: {"distinct_exams": 18, "equivalencies": 18, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | 4 | Scientific Practices”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business Management]:  ⟵ “Business Management | 4 | General Education Elective”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | 4 | Scientific Practices”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | 4 | Scientific Practices”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | 4 | General Education Elective”
  - equivalencies[IB-FILM|Film]:  ⟵ “Film | 4* | Open Elective”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | 4 | Social and Behavioral Sciences”
  - equivalencies[IB-GLOBAL-POLITICS|Global Politics]:  ⟵ “Global Politics | 4 | Social and Behavioral Sciences”
  - equivalencies[IB-HISTORY|History]:  ⟵ “History | 4 | General Education Elective”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|Mathematics: Analysis and Approaches]:  ⟵ “Mathematics: Analysis and Approaches | 4 | Scientific Practices”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|Mathematics: Applications and Interpretation]:  ⟵ “Mathematics: Applications and Interpretation | 4 | Scientific Practices”
  - equivalencies[IB-MUSIC|Music]:  ⟵ “Music | 4* | Open Elective”
  - equivalencies[IB-PHILOSOPHY|Philosophy]:  ⟵ “Philosophy | 4 | Arts and Humanities”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | 4 | Scientific Practices”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | 4 | Social and Behavioral Sciences”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|Social and Cultural Anthropology]:  ⟵ “Social and Cultural Anthropology | 4 | Social and Behavioral Sciences”
  - equivalencies[IB-THEATRE|Theatre]:  ⟵ “Theatre | 4* | Open Elective”
  - equivalencies[IB-VISUAL-ARTS|Visual Arts]:  ⟵ “Visual Arts | 4* | Open Elective”
### `bcc67c8aa2f6abe2` Ringling College of Art and Design — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.ringling.edu/clep-examinations-equivalency-chart (sha256 fcbf8198dd4b)
- checks: {"distinct_exams": 34, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | General Education Elective”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | Literature and Media Studies”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | Literature and Media Studies”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | Scientific Practices”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | Scientific Practices”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | Scientific Practices”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | Scientific Practices”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | WRIT 151 & WRIT elective (6 cr)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular (must include essay portion) | 50 | WRIT 151 & WRIT elective (6 cr)”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | Scientific Practices”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | Literature and Media Studies”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | General Education Elective”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language: Levels 1 and 2 | 50 | General Education Elective”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language: Levels 1 and 2 | 50 | General Education Elective”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | General Education Elective”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | General Education Elective”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | Social and Behavioral Sciences”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | Arts and Humanities”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | Open Elective”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | Social and Behavioral Sciences”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | Open Elective”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | Social and Behavioral Sciences”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | Social and Behavioral Sciences”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | Scientific Practices”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | Scientific Practices”
  - … 9 more rows
### `m2cfca1971fb04ea` Ringling College of Art and Design — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ringling.edu/admissions/apply/transfers/ (sha256 9fec799fd673)
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “Transfer Credits and Placement Ringling College will consider for transfer any liberal arts or studio art credit that meets our academic requirements and where a grade of C or better was earned from an accredited college or university.”
  - min_grade: C ⟵ “Ringling College of Art and Design will consider for transfer any liberal arts or studio credit that meets academic requirements and in which a grade of “C” or better was earned from a regionally accredited college or university.”
  - min_grade: C ⟵ “Transfer Credits and Placement | Ringling College Skip to main content Course Catalog Fulltext search Main navigation Catalog Home Majors, Minors and Certificates Courses Breadcrumb Home Transfer Credits and Placement Transfer Credits and Placement Download as PDF Ringling College will consider for transfer any liberal arts or studio art credit that meets our academic requirements and where a grad”
### `c606a4778bb50f27` Rollins College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/ap-credits/ (sha256 a10bd119358e)
- checks: {"distinct_exams": 38, "equivalencies": 40, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|MINIMUM SCORE 4]:  ⟵ “2-D Art & Design | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES ART 110: 2D Foundations”
  - equivalencies[AP-3-D-ART-DESIGN|MINIMUM SCORE 4]:  ⟵ “3-D Art & Design | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES ART 120: 3D Foundations”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|MINIMUM SCORE 4]:  ⟵ “African American Studies | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES Elective credit: AAAS 1XX”
  - equivalencies[AP-ART-HISTORY|MINIMUM SCORE 4]:  ⟵ “Art History | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES ARH 1XX (Choice of ARH 110 or ARH 120 in major/minor)”
  - equivalencies[AP-BIOLOGY|MINIMUM SCORE 4]:  ⟵ “Biology | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES Elective credit: BIO 1XX”
  - equivalencies[AP-BIOLOGY|MINIMUM SCORE 5]:  ⟵ “Biology | MINIMUM SCORE 5 | COMP | COMMENTS/NOTES BIO 120: General Biology I or BIO 121: General Biology II with department approval”
  - equivalencies[AP-CALCULUS-AB|MINIMUM SCORE 4]:  ⟵ “Calculus AB | MINIMUM SCORE 4 | COMP MCMP | COMMENTS/NOTES MAT 111: Calculus I”
  - equivalencies[AP-CALCULUS-BC|MINIMUM SCORE 4]:  ⟵ “Calculus BC | MINIMUM SCORE 4 | COMP MCMP | COMMENTS/NOTES MAT 112: Calculus II”
  - equivalencies[AP-CHEMISTRY|MINIMUM SCORE 4]:  ⟵ “Chemistry | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES CHM 120: Chemistry I”
  - equivalencies[AP-CHEMISTRY|MINIMUM SCORE 5]:  ⟵ “Chemistry | MINIMUM SCORE 5 | COMP | COMMENTS/NOTES CHM 120: Chemistry I and CHM 121: Chemistry II”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|MINIMUM SCORE 4]:  ⟵ “Chinese Language & Culture | MINIMUM SCORE 4 | COMP FCMP | COMMENTS/NOTES Elective credit: CHN 2XX”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|MINIMUM SCORE 4]:  ⟵ “Comparative Government & Politics | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES POL 100: Introduction to Comparative Politics”
  - equivalencies[AP-COMPUTER-SCIENCE-A|MINIMUM SCORE 4]:  ⟵ “Computer Science A | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES Elective credit: CMS 1XX”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|MINIMUM SCORE 4]:  ⟵ “Computer Science Principles | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES Elective credit: CMS 1XX”
  - equivalencies[AP-DRAWING|MINIMUM SCORE 4]:  ⟵ “Drawing | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES ART 221: Drawing and Composition”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|MINIMUM SCORE 4]:  ⟵ “English Language & Composition | MINIMUM SCORE 4 | COMP WCMP | COMMENTS/NOTES ENGW 140: Composition: Writing About Selected Topics”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|MINIMUM SCORE 4]:  ⟵ “English Literature & Composition | MINIMUM SCORE 4 | COMP WCMP | COMMENTS/NOTES ENGW 140: Composition: Writing About Selected Topics”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|MINIMUM SCORE 4]:  ⟵ “Environmental Science | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES Elective credit: ENV 1XX”
  - equivalencies[AP-EUROPEAN-HISTORY|MINIMUM SCORE 4]:  ⟵ “European History | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES Elective credit: HIS 1XX”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|MINIMUM SCORE 4]:  ⟵ “French Language & Culture | MINIMUM SCORE 4 | COMP FCMP | COMMENTS/NOTES Elective credit: FRN 2XX”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|MINIMUM SCORE 4]:  ⟵ “German Language & Culture | MINIMUM SCORE 4 | COMP FCMP | COMMENTS/NOTES Elective credit: GMN 2XX”
  - equivalencies[AP-HUMAN-GEOGRAPHY|MINIMUM SCORE 4]:  ⟵ “Human Geography | MINIMUM SCORE 4 | COMP | COMMENTS/NOTES Elective credit: SSC 1XX”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|MINIMUM SCORE 4]:  ⟵ “Italian Language & Culture | MINIMUM SCORE 4 | COMP FCMP | COMMENTS/NOTES Elective credit: ITN 2XX”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|MINIMUM SCORE 4]:  ⟵ “Japanese Language & Culture | MINIMUM SCORE 4 | COMP FCMP | COMMENTS/NOTES Elective credit: JPN 2XX”
  - equivalencies[AP-LATIN|MINIMUM SCORE 4]:  ⟵ “Latin | MINIMUM SCORE 4 | COMP FCMP | COMMENTS/NOTES Elective credit: LAT 2XX”
  - … 15 more rows
### `d43eccdff4b9871d` Saint Johns River State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.sjrstate.edu/dual-early-college-program (sha256 4ca9bf69d223)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Having a minimum 8th grade GPA of 3.0 in core academic coursework, and”
### `00d25b138ff50589` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $15,000 for transfer students ⟵ “University Transfer Award | up to $15,000 for transfer students”
### `06d00f6a5ff23e33` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $16,000 for transfer students ⟵ “Excellence Transfer Award | up to $16,000 for transfer students”
### `0dc1a6993271feb2` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $15,000 for incoming first-year students ⟵ “Campus Award | up to $15,000 for incoming first-year students”
### `1ba5a4552c27fe43` Saint Leo University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants/teach (sha256 fb52d324254d)
- checks: {"thresholds": null}
  - award_amount_text: $ 1,886 ⟵ “1/2 time | $ 1,886”
### `3bdab630b1251081` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $19,000 for transfer students ⟵ “Presidential Transfer Award | up to $19,000 for transfer students”
### `4a8f4778b9a33988` Saint Leo University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants/teach (sha256 fb52d324254d)
- checks: {"thresholds": null}
  - award_amount_text: $ 2,829 ⟵ “3/4 time | $ 2,829”
### `93f3d905f813be3a` Saint Leo University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants/teach (sha256 fb52d324254d)
- checks: {"thresholds": null}
  - award_amount_text: $ 943 ⟵ “Less-than 1/2 time | $ 943”
### `cd4f97df2c882cc3` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $24,000 for incoming first-year students ⟵ “Presidential Award | up to $24,000 for incoming first-year students”
### `d98d30001ad0db78` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $13,000 for transfer students ⟵ “Campus Transfer Award | up to $13,000 for transfer students”
### `e39e83b211bbe1e4` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $20,000 for incoming first-year students ⟵ “Excellence Award | up to $20,000 for incoming first-year students”
### `eb777e49cbf0f773` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $21,000 for incoming first-year students ⟵ “Dean's Award | up to $21,000 for incoming first-year students”
### `fa207df2046ef55c` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $18,000 for transfer students ⟵ “Dean's Transfer Award | up to $18,000 for transfer students”
### `fb5b9ea290812b42` Saint Leo University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- checks: {"thresholds": null}
  - award_amount_text: up to $18,000 for incoming first-year students ⟵ “University Award | up to $18,000 for incoming first-year students”
### `8b5b4d56b3b39f4f` Saint Leo University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.saintleo.edu/academics/academic-affairs/registrar/transfer-policies (sha256 90eeb56e42bb)
- checks: {"fields": ["min_grade"]}
  - min_grade: D ⟵ “Coursework at the 100-200 level, and completed with grades of D or better, will be transferred based on predetermined equivalencies.”
### `mebaf40eb0574d82` Seminole State College of Florida — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.seminolestate.edu/uploads/documents/dual-enrollment/DualEnrollmentApplicationforAdmissionsLIVE-1-A.pdf (sha256 14581c27c428)
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa"], "merged_pages": 4, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “A cumulative, unweighted high school GPA of 3.0 is required for this program.”
  - eligibility_tier: 3.0 ⟵ “Students may enroll in Career Dual Enrollment with a 2.5 cumulative, unweighted high school GPA. However, if the A.S. program requires General Education courses, students must have a 3.0 GPA to take those courses.”
  - max_credit_hours_per_term: 10 ⟵ “Dual enrolled students are eligible to take up to 10 credit hours per semester, including the summer semester.”
  - eligibility_tier: 2.5 ⟵ “Career Dual Enrollment can be taken with a 2.5 or higher, unweighted high school GPA and no test scores necessary. Please review our Resources website for a list of courses that can be taken with a 2.5 GPA.”
  - eligibility_tier: 3.0 ⟵ “A 3.0 high school GPA for Academic Dual Enrollment”
  - eligibility_tier: 2.5 ⟵ “A 2.5 high school GPA for Career Dual Enrollment”
  - eligibility_tier: 2.5 ⟵ “Courses that can be taken with a 2.5GPA and no test scores”
  - college_gpa_to_continue: 2.0 ⟵ “1.    Continued eligibility for Dual Enrollment requires that students maintain a 2.0 or”
  - college_gpa_to_continue: 2.0 ⟵ “1. Continued eligibility for Dual Enrollment requires that students maintain a 2.0 or”
  - eligibility_tier: 2.0 ⟵ “• Students must maintain a cumulative college GPA of 2.0 or higher and an unweighted high school GPA of 3.0 or higher for academic coursework or 2.5 higher”
  - college_gpa_to_continue: 2.0 ⟵ “• Students must maintain a cumulative college GPA of 2.0 or higher and an unweighted high school GPA of 3.0 or higher for academic coursework or 2.5 higher”
### `601072b38f264a41` Seminole State College of Florida — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://www.seminolestate.edu/catalog/student-info/admissions/transfer-students (sha256 c17ac6bd6d68)
- checks: {"fields": ["min_grade"]}
  - min_grade: D ⟵ “Transfer Credit Policy Transfer credits from institutions accredited by one of six regional associations will be accepted, provided a grade of "D" or higher was earned (see College Procedure 3.200).”
### `0190e275276bbcf0` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 28, 2014 ⟵ “Douglas M. Andrews | May 28, 2014 | Dean”
### `0924c62d485ae8c6` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Aug. 1, 2019 ⟵ “Dr. Peter Hamlet | Aug. 1, 2019 | Professor”
### `0a4bc8694f7b4ae5` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 24, 2015 ⟵ “Dr. Dale McDaniel | June 24, 2015 | Professor”
### `154e50087929e1ee` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 28, 2008 ⟵ “Bill Shaffer | June 28, 2008 | Vice President”
### `15c041db927eaa2d` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 13, 2001 ⟵ “Barbara L. Goza | May 13, 2001 | Professor”
### `1b0860c867636e0b` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 5, 2016 ⟵ “Dr. Michael J. McLeod | May 5, 2016 | Dean”
### `1ca5a44fd56531e8` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 18, 2020 ⟵ “Glenn Little | Dec. 18, 2020 | Vice President”
### `1e15ad47f3a9c3a6` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 24, 2006 ⟵ “William R. Boyer Sr. | May 24, 2006 | Professor”
### `1fd16635ddcfa724` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: March 22, 2023 ⟵ “Junior Gray | March 22, 2023 | Director”
### `2059dfefc287658e` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 17, 2021 ⟵ “Erik Christensen | Dec. 17, 2021 | Dean”
### `2bed92dbb26a73c1` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 6, 2013 ⟵ “Susan C. Livingston | May 6, 2013 | Librarian”
### `3b56cf37934ff050` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 7, 2011 ⟵ “Judy H. Zemko | Dec. 7, 2011 | Professor”
### `41e78e8e9add4dd8` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: April 26, 2016 ⟵ “Cathy C. Futral | April 26, 2016 | Professor”
### `489b71742ead5c3c` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Jan. 5, 1998 ⟵ “Carol J. Emery | Jan. 5, 1998 | Professor”
### `5190e2107bb7927c` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Oct. 25, 2017 ⟵ “Lorrie Key | Oct. 25, 2017 | Director”
### `527ba3803b1ca0b2` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 28, 2006 ⟵ “Kay H. Bloom | June 28, 2006 | Professor”
### `534372e92d45697c` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 24, 2006 ⟵ “Edward L. Morgan | May 24, 2006 | Professor”
### `547bcb144253e94e` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 23, 2021 ⟵ “Dr. James Broen | June 23, 2021 | Professor”
### `57a8a16abda91087` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 24, 2015 ⟵ “Dr. Leana Revell | June 24, 2015 | Vice President”
### `586a0682391f41d5` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Jan. 14, 2022 ⟵ “Helen Shoemaker | Jan. 14, 2022 | Professor”
### `58e344e7e3d565d6` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 4, 2024 ⟵ “Elizabeth Broen | Dec. 4, 2024 | Professor”
### `5b56c1af7cffd85d` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Jan. 28, 2022 ⟵ “Dr. Robert Flores | Jan. 28, 2022 | Director”
### `611395da0878ac08` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 17, 2002 ⟵ “Michele Roberts | May 17, 2002 | Dean”
### `64d7a5d7e8b129f9` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Sept. 1, 2021 ⟵ “Adam Martin | Sept. 1, 2021 | Professor”
### `6733b5ec58b25177` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: July 24, 2013 ⟵ “Norm Church | July 24, 2013 | Professor”
### `6b40a972a6bb54a6` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 24, 2015 ⟵ “Donald Appelquist | June 24, 2015 | Dean”
### `72a289f2616b9862` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 26, 2022 ⟵ “Darlene Saccuzzo | June 26, 2022 | Professor”
### `7bd932a8bc3464b8` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 6, 2007 ⟵ “Clay Gooch | June 6, 2007 | Professor”
### `7c4b004df4735617` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 19, 2004 ⟵ “Dr. W. Aubrey Gardner | May 19, 2004 | Vice President”
### `7dd8adec3104f25a` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 18, 2020 ⟵ “Timothy Hansen | June 18, 2020 | Professor”
### `806827a270dfa393` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 7, 2011 ⟵ “Pamela B. Hansen | Dec. 7, 2011 | Professor”
### `82736917f2a594f0` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Aug. 22, 2018 ⟵ “Dr. Deborah Fuschetti | Aug. 22, 2018 | Registrar”
### `8d109d812f04c758` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: April 27, 2016 ⟵ “James Kevin Brown | April 27, 2016 | Dean”
### `902c54cae31013f8` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 25, 2014 ⟵ “Annie L. Alexander-Harvey | June 25, 2014 | Dean”
### `9e1bf494a752fb5d` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: July 14, 2021 ⟵ “Bobby Sconyers | July 14, 2021 | Professor”
### `9f7dcdd4c9502f77` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 4, 2002 ⟵ “Dr. Robert L. Fitzgerald Jr. | Dec. 4, 2002 | Professor”
### `a08c42072e0bb716` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 27, 2018 ⟵ “Lynn MacNeill | June 27, 2018 | Professor”
### `a1424f51863de7d7` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 6, 2007 ⟵ “Jack Parr | June 6, 2007 | Professor”
### `a51fdd34ffc7afb5` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 8, 2004 ⟵ “Dr. Bill Gene Smith | Dec. 8, 2004 | Professor”
### `a58b4d21a1d91154` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 27, 2026 ⟵ “Cindy Garren | May 27, 2026 | Director”
### `a5e908c1b47ac523` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 10, 2008 ⟵ “Dr. Henry Bettich | Dec. 10, 2008 | Professor”
### `a9f4f2193b3e6590` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: April 27, 2016 ⟵ “Ellen L. Thornton | April 27, 2016 | Professor”
### `ad90a42404966821` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: April 26, 2017 ⟵ “Dr. Bill Gregory | April 26, 2017 | Professor”
### `af352e5c10590c89` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: April 23, 2025 ⟵ “Cynthia Kinser | April 23, 2025 | Professor”
### `b35cf63344408a56` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Jan. 18, 2017 ⟵ “Susan D. Hale | Jan. 18, 2017 | Director”
### `b3ee1fa37334c65d` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: March 19, 2008 ⟵ “Dr. Mary Ann Fritz | March 19, 2008 | Professor”
### `b41dd48e3fb8acb3` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 7, 2019 ⟵ “Dr. Kristina Lewis | May 7, 2019 | Professor”
### `b530e734f087bdc1` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Jan. 22, 2014 ⟵ “Joel E. Boydston | Jan. 22, 2014 | Professor”
### `b76046fec495b118` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: April 25, 2009 ⟵ “Francisca “Dee” Oakes | April 25, 2009 | Professor”
### `bacf383c58d3d692` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 4, 2024 ⟵ “Dr. Teresa Crawford | Dec. 4, 2024 | Director”
### `c0909e02f7fff790` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 15, 2016 ⟵ “Mollie Doctrow | June 15, 2016 | Curator”
### `c57acbecf3b9e06d` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: April 22, 2009 ⟵ “Lyn Latham | April 22, 2009 | Professor”
### `c8c4e7e04f796803` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 17, 2014 ⟵ “Daniel West | June 17, 2014 | Professor”
### `c9dd15b5dc3108d0` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Jan. 27, 2016 ⟵ “Richard D. Morey | Jan. 27, 2016 | Professor”
### `cd02419d5122a0e2` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 7, 2002 ⟵ “Dr. Catherine P. Cornelius | May 7, 2002 | President”
### `cf725083ae67f60a` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 27, 2007 ⟵ “Mary Starling | June 27, 2007 | Professor”
### `d77307a06d842e17` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 10, 2022 ⟵ “James J. Moye | May 10, 2022 | Professor”
### `dc8b9e93dd9c0086` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 27, 2009 ⟵ “Rebecca Henry | May 27, 2009 | Professor”
### `ddbd8a9390bc62c9` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 7, 2019 ⟵ “Dr. Christopher McConnell | May 7, 2019 | Professor”
### `de55f8850ba37f77` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Jan. 31, 2001 ⟵ “Larry C. Hooper | Jan. 31, 2001 | Professor”
### `e1ddea5534a59d63` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 30, 2023 ⟵ “Dr. Thomas C. Leitzel | June 30, 2023 | President”
### `e80e9b3d66ba9d1c` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Dec. 7, 2011 ⟵ “Barbara Ann Hergianto | Dec. 7, 2011 | Professor”
### `eb42f070d65187c7` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 26, 2013 ⟵ “Dr. Norman L. Stephens Jr. | June 26, 2013 | President”
### `ede32c4e5d6386f7` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: July 18, 2019 ⟵ “Enrique Ramos | July 18, 2019 | Professor”
### `f1122eb5f21c9749` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Aug. 22, 2012 ⟵ “Laura Robinson-White | Aug. 22, 2012 | Professor”
### `f3b23a1f6233e59e` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: June 17, 2003 ⟵ “Donald Farrens | June 17, 2003 | Professor”
### `f4b5166bdfb81566` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Sept. 28, 2016 ⟵ “Rebecca A. Sroda | Sept. 28, 2016 | Dean”
### `f4fc8bbb997a9f13` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: July 31, 2022 ⟵ “Dr. Theresa James | July 31, 2022 | Professor”
### `f600f0e02bba312b` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: May 19, 2004 ⟵ “Dale L. Craft | May 19, 2004 | Professor”
### `ffd6663a3c1b59a8` South Florida State College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/college/retirees/emeriti (sha256 c990940ee96c)
- checks: {"thresholds": null}
  - award_amount_text: Feb. 21, 2018 ⟵ “Benjamin Carter Jr. | Feb. 21, 2018 | Director”
### `8f6b55b090cdfe71` St Petersburg College — credit_policies 2027-28 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.spcollege.edu:443/future-students/admissions/high-school-programs/early-college (sha256 886745c8b282)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Unweighted cumulative GPA of 3.0 or higher.”
### `d63c88dd80a8d78a` St. Thomas University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.stu.edu/dualenrollment/ (sha256 c73264b43172)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Students qualify for admission to the Dual Enrollment Program when they are identified, by the designated Dual Enrollment High School Liaison, as students with junior or senior standing, and a 3.0 or better unweighted grade point average on a 4.0 scale. Students must maintain the required GPA to rem”
### `m34dd8f6950eaeb8` The College of the Florida Keys — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.cfk.edu/forms/DE_Eligibility_form-updated_3-2026%20(One%20page).pdf (sha256 45483ecc8cec)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “An un-weighted cumulative high school GPA of 3.0 or higher (a cumulative GPA of 2.0 is required for vocational PSAV courses)”
  - eligibility_tier: 3.0 ⟵ “High School Coursework (GPA 3.0+ with grade of B or better)”
### `0817a5912ff48731` The University of Tampa — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ut.edu/about-utampa/university-services/office-of-the-registrar/advanced-placement-credit (sha256 27ad759d459b)
- checks: {"distinct_exams": 35, "equivalencies": 75, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, 5]:  ⟵ “African American Studies | 3, 4, 5 | Humanities Elective | HUM TR | TBH | 4”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | History Survey I 1 | ART 268 | TBH | 4”
  - equivalencies[AP-ART-HISTORY|4, 5]:  ⟵ “Art History | 4, 5 | History Survey I 1 | ART 268 | TBH | 4”
  - equivalencies[AP-ART-HISTORY|4, 5]:  ⟵ “Art History | 4, 5 | History Survey II2 | ART 269 | TBH | 4”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “Studio Art: 2-D Design Portfolio | 3, 4, 5 | Art Elective | ART TR | VPA | 4”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, 5]:  ⟵ “Studio Art: 3-D Design Portfolio | 3, 4, 5 | Art Elective | ART TR | VPA | 4”
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “Studio Art: Drawing Portfolio | 3, 4, 5 | Art Elective | ART TR | VPA | 4”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | Biological Science | BIO 124 | NSD | 4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | General Biology I 1 | BIO 198 and 198L | NSD | 4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | 5 | General Biology I 1 with Lab | BIO 198 and 198L | NSD | 4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | 5 | General Biology II 2 with Lab | BIO 199 and 199L |  | 4”
  - equivalencies[AP-CALCULUS-AB|3, 4, 5]:  ⟵ “Calculus AB | 3, 4, 5 | Calculus I 1 | MAT 260 | UTMAT | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | Calculus I 1 | MAT 260 | UTMAT | 4”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC | 4, 5 | Calculus I 1 | MAT 260 | UTMAT | 4”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC | 4, 5 | Calculus II 2 | MAT 261 | UTMAT | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | Chemistry and Society | CHE 126 | NSD | 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | General Chemistry I 1 with Lab | CHE 152 and 153L | NSD | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | General Chemistry I 1 with Lab | CHE 152 and 153L | NSD | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | General Chemistry II 2 with Lab | CHE 154 and 155L |  | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language | 3 | Intermediate Chinese I 1 | CHI 201 | TBH | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4, 5]:  ⟵ “Chinese Language | 4, 5 | Intermediate Chinese I 1 | CHI 201 | TBH | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4, 5]:  ⟵ “Chinese Language | 4, 5 | Intermediate Chinese II 2 | CHI 202 | TBH | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4]:  ⟵ “Computer Science A | 3, 4 | General Elective | UT TR |  | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|5]:  ⟵ “Computer Science A | 5 | The Science of Computing I | CSC 101 |  | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | General Elective | UT TR |  | 4”
  - … 50 more rows
### `a6b046bb3974ea72` The University of Tampa — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.ut.edu/about-utampa/university-services/office-of-the-registrar/international-baccalaureate (sha256 a503ffb3d4e6)
- checks: {"distinct_exams": 23, "equivalencies": 66, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | Biological Science | BIO 124 | NSD | 3”
  - equivalencies[IB-BIOLOGY|5 to 7]:  ⟵ “Biology | 5 to 7 | Biological Science | BIO 124 | NSD | 3”
  - equivalencies[IB-BIOLOGY|5 to 7]:  ⟵ “Biology | 5 to 7 | General Biology I (1) | BIO 198 & 198L | NSD | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business Management | 4 | Introduction to Business | BUS 101 |  | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5 to 7]:  ⟵ “Business Management | 5 to 7 | Introduction to Business | BUS 101 |  | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5 to 7]:  ⟵ “Business Management | 5 to 7 | Business Elective | BUS TR |  | 4”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | Chemistry and Society | CHE 126 | NSD | 3”
  - equivalencies[IB-CHEMISTRY|5 to 7]:  ⟵ “Chemistry | 5 to 7 | Chemistry and Society | CHE 126 | NSD | 3”
  - equivalencies[IB-CHEMISTRY|5 to 7]:  ⟵ “Chemistry | 5 to 7 | General Chemistry I (1) with Lab | CHE 152 & 153L | NSD | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|4]:  ⟵ “Computer Science | 4 | Computer Science Elective | CSC TR | UTAMPA 200 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|5 to 7]:  ⟵ “Computer Science | 5 to 7 | Computer Science Elective | CSC TR | UTAMPA 200 | 4”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics | 4 | Principles of Microeconomics | ECO 204 | SSD | 4”
  - equivalencies[IB-ECONOMICS|5 to 7]:  ⟵ “Economics | 5 to 7 | Principles of Microeconomics | ECO 204 | SSD | 4”
  - equivalencies[IB-ECONOMICS|5 to 7]:  ⟵ “Economics | 5 to 7 | Principles of Macroeconomics | ECO 205 |  | 4”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4]:  ⟵ “Environmental Systems and Societies | 4 | Environmental Studies | ENS 112 | NSD | 4”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|5 to 7]:  ⟵ “Environmental Systems and Societies | 5 to 7 | Environmental Studies | ENS 112 | NSD | 4”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|5 to 7]:  ⟵ “Environmental Systems and Societies | 5 to 7 | Environmental Studies Elective | ENS TR | NSD | 4”
  - equivalencies[IB-FILM|4]:  ⟵ “Film Studies | 4 | Communication Elective | COM TR | TBH | 4”
  - equivalencies[IB-FILM|5 to 7]:  ⟵ “Film Studies | 5 to 7 | Communication Elective | COM TR | TBH | 4”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French Language A: Language and Literature | 4 | Language Elective | FRE TR | TBH | 4”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French Language B | 4 | Elementary French I (1) | FRE 101 | TBH | 4”
  - equivalencies[IB-FRENCH|5 to 7]:  ⟵ “French Language B | 5 to 7 | Elementary French I (1) | FRE 101 | TBH | 4”
  - equivalencies[IB-FRENCH|5 to 7]:  ⟵ “French Language B | 5 to 7 | Elementary French II (2) | FRE 102 | TBH | 4”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | World Regional Geography | GEO 102 | SSD | 4”
  - equivalencies[IB-GEOGRAPHY|5 to 7]:  ⟵ “Geography | 5 to 7 | Geography Elective | GEO TR | SSD | 4”
  - … 41 more rows
### `m78c7f0f1b6c1c60` University of Central Florida — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ucf.edu/admissions/undergraduate/dual-enrollment-2/ (sha256 01f977401c69)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.8 ⟵ “Must have a 3.8 high school GPA* (see note) as re-calculated by UCF using only academic core courses.”
  - max_credit_hours_per_term: 6 ⟵ “Your admission to UCF’s Dual Enrollment program is valid for the term listed in your admission letter. You are admitted as a non-degree-seeking, part-time student and may enroll in up to 6 credit hours.”
### `ecdb90856b845076` University of North Florida — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.unf.edu/catalog/admissions/undergrad/Dual-Enrollment.html (sha256 0b1c24388772)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “An official and current high school transcript reflecting a minimum 3.0 unweighted GPA”
### `b188142a65856e1f` University of West Florida — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/cost-of-attendance/cost-of-attendance-estimates/ (sha256 923d42c3a3cb)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition 2: 16968 ⟵ “Tuition 2 | 16,968 | 16,968 | 16,968”
  - with_parents_or_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - with_parents_or_family:Food 3: 2848 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - with_parents_or_family:Housing 3: 2182 ⟵ “Housing 3 | 2,182 | 7,358 | 8,730”
  - with_parents_or_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - with_parents_or_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - with_parents_or_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - with_parents_or_family:TOTAL: 29226 ⟵ “TOTAL | $29,226 | $37,182 | $38,554”
  - on_campus:Tuition 2: 16968 ⟵ “Tuition 2 | 16,968 | 16,968 | 16,968”
  - on_campus:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - on_campus:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - on_campus:Housing 3: 7358 ⟵ “Housing 3 | 2,182 | 7,358 | 8,730”
  - on_campus:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - on_campus:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - on_campus:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - on_campus:TOTAL: 37182 ⟵ “TOTAL | $29,226 | $37,182 | $38,554”
  - off_campus_not_with_family:Tuition 2: 16968 ⟵ “Tuition 2 | 16,968 | 16,968 | 16,968”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - off_campus_not_with_family:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - off_campus_not_with_family:Housing 3: 8730 ⟵ “Housing 3 | 2,182 | 7,358 | 8,730”
  - off_campus_not_with_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - off_campus_not_with_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - off_campus_not_with_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - off_campus_not_with_family:TOTAL: 38554 ⟵ “TOTAL | $29,226 | $37,182 | $38,554”
### `267d615d856a5a6a` University of West Florida — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.uwf.edu/undergraduate/transfercredit/ (sha256 404831594d1f)
- checks: {"distinct_exams": 35, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|ART 2201C(min. 3 credits)]:  ⟵ “2-D Art and Design 1 | ART 2201C(min. 3 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-3-D-ART-DESIGN|ART 2203C(min. 3 credits)]:  ⟵ “3-D Art and Design 2 | ART 2203C(min. 3 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-ART-HISTORY|ARH 1000 core(min. 3 credits)]:  ⟵ “Art History | ARH 1000 core(min. 3 credits) | ARH 2050 and ARH 2051(min. 6 credits) | Same as 4”
  - equivalencies[AP-ART-HISTORY|ARH 1000 core(min. 3 credits)]:  ⟵ “Art History (Effective for exams taken after 5/16/2018) | ARH 1000 core(min. 3 credits) | ARH 1000 core and ARH 2050 or ARH 2051(min. 6 credits) | Same as 4”
  - equivalencies[AP-BIOLOGY|BSC 1005 BSC 1005L core(min. 4 credits)]:  ⟵ “Biology | BSC 1005 BSC 1005L core(min. 4 credits) | BSC 2010 BSC 2010L core(min. 4 credits) | BSC 2010 BSC 2010L coreand BSC 2011 BSC 2011L(min. 8 credits)”
  - equivalencies[AP-CALCULUS-AB|MAC 2311 core(min. 4 credits)]:  ⟵ “Calculus AB | MAC 2311 core(min. 4 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-CALCULUS-BC|MAC 2311 core(min. 4 credits)]:  ⟵ “Calculus BC | MAC 2311 core(min. 4 credits) | MAC 2311 core and MAC 2312(min. 8 credits) | Same as 4”
  - equivalencies[AP-CHEMISTRY|CHM 1020 CHM 1020L core(min. 4 credits)]:  ⟵ “Chemistry | CHM 1020 CHM 1020L core(min. 4 credits) | CHM 2045 CHM 2045L core(min. 4 credits) | CHM 2045 CHM 2045L core and CHM 2046 CHM 2046L(min. 8 credits)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|CHI 2200(min. 3 credits)]:  ⟵ “Chinese Language and Culture | CHI 2200(min. 3 credits) | CHI 2200 and CHI 2XX1(min. 6 credits) | Same as 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|CGS 1075^(min. 3 credits)]:  ⟵ “Computer Science A | CGS 1075^(min. 3 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|COP 1000(min. 3 credits)]:  ⟵ “Computer Science Principles | COP 1000(min. 3 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-DRAWING|ART 1300C(min. 3 credits)]:  ⟵ “Drawing 3 | ART 1300C(min. 3 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-MACROECONOMICS|ECO 2013 core(min. 3 credits)]:  ⟵ “Economics: Macro | ECO 2013 core(min. 3 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-MICROECONOMICS|ECO 2023(min. 3 credits)]:  ⟵ “Economics: Micro | ECO 2023(min. 3 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|ENC 1101 core(min. 3 credits)]:  ⟵ “English Language and Composition 4 | ENC 1101 core(min. 3 credits) | ENC 1101 core and ENC 1102(min. 6 credits) | Same as 4”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|ENC 1101 core or LIT 2000(min. 3 credits)]:  ⟵ “English Literature and Composition 4 | ENC 1101 core or LIT 2000(min. 3 credits) | ENC 1101 core and either ENC 1102 or LIT 2000(min. 6 credits) | Same as 4”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|EVR 2001 core(min. 3 credits)]:  ⟵ “Environmental Science | EVR 2001 core(min. 3 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-EUROPEAN-HISTORY|EUH 1009^(min. 3 credits)]:  ⟵ “European History | EUH 1009^(min. 3 credits) | EUH 1000 and EUH 1001(min. 6 credits) | Same as 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|FRE 2200(min. 3 credits)]:  ⟵ “French Language and Culture | FRE 2200(min. 3 credits) | FRE 2200 and FRE 2210(min. 6 credits) | Same as 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|FRW2XX1^(min. 3 credits)]:  ⟵ “French Literature | FRW2XX1^(min. 3 credits) | FRW 2XX1^ and FRW 2XX2^(min. 6 credits) | Same as 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|GER 2240(min. 3 credits)]:  ⟵ “German Language and Culture | GER 2240(min. 3 credits) | GER 2240 and GER 2241(min. 6 credits) | Same as 4”
  - equivalencies[AP-HUMAN-GEOGRAPHY|GEO 1400^(min. 3 credits)]:  ⟵ “Human Geography | GEO 1400^(min. 3 credits) | Same as 3 | Same as 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|XFER 2XX1^(min. 3 credits)]:  ⟵ “Italian Language and Culture | XFER 2XX1^(min. 3 credits) | XFER 2XX1^ and XFER 2XX2^(min. 6 credits) | Same as 4”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|JPN 2200(min. 3 credits)]:  ⟵ “Japanese Language and Culture | JPN 2200(min. 3 credits) | JPN 2200 and JPN 2201(min. 6 credits) | Same as 4”
  - equivalencies[AP-LATIN|LNW 1700^]:  ⟵ “Latin: Latin Literature | LNW 1700^ | Same as 3 | Same as 3”
  - … 14 more rows
### `4dcee5afe3d7da85` University of West Florida — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.uwf.edu/undergraduate/transfercredit/ (sha256 404831594d1f)
- checks: {"distinct_exams": 29, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|POS 2041 core, civics (min. 3 credits)]:  ⟵ “American Government | POS 2041 core, civics (min. 3 credits)”
  - equivalencies[CLEP-AMERICAN-LITERATURE|AML 1000 (min. 3 credits)]:  ⟵ “American Literature | AML 1000 (min. 3 credits)”
  - equivalencies[CLEP-BIOLOGY|BSC 1005 core (min. 3 credits) No lab credit.]:  ⟵ “Biology | BSC 1005 core (min. 3 credits) No lab credit.”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|BUL 2241 (min. 3 credits)]:  ⟵ “Business Law, Introductory | BUL 2241 (min. 3 credits)”
  - equivalencies[CLEP-CALCULUS|MAC 2233 (min. 3 credits)]:  ⟵ “Calculus | MAC 2233 (min. 3 credits)”
  - equivalencies[CLEP-CHEMISTRY|CHM 1020 core (min. 3 credits) No lab credit.]:  ⟵ “Chemistry | CHM 1020 core (min. 3 credits) No lab credit.”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|ENC 1101 core and ENC 1102 (min. 6 credits)]:  ⟵ “College Composition | ENC 1101 core and ENC 1102 (min. 6 credits)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|ENC 1101 core and ENC 1102 (min. 6 credits)]:  ⟵ “College Composition Modular | ENC 1101 core and ENC 1102 (min. 6 credits)”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|EDP 1002 (min. 3 credits)]:  ⟵ “Educational Psychology, Introduction to | EDP 1002 (min. 3 credits)”
  - equivalencies[CLEP-ENGLISH-LITERATURE|ENL 1000 (min. 3 credits)]:  ⟵ “English Literature | ENL 1000 (min. 3 credits)”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|ACG 2001 (min. 3 credits)]:  ⟵ “Financial Accounting | ACG 2001 (min. 3 credits)”
  - equivalencies[CLEP-FRENCH-LANGUAGE|FRE 1120C (min. 3 credits)]:  ⟵ “French Language 2 | FRE 1120C (min. 3 credits)”
  - equivalencies[CLEP-GERMAN-LANGUAGE|GER 1120C (min. 3 credits)]:  ⟵ “German Language 3 | GER 1120C (min. 3 credits)”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|AMH 2010 (min. 3 credits)]:  ⟵ “History of the United States I: Early Colonization to 1877 | AMH 2010 (min. 3 credits)”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|AMH 2020 core (min. 3 credits)]:  ⟵ “History of the United States II: 1865 to Present | AMH 2020 core (min. 3 credits)”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|DEP 2004 (min. 3 credits)]:  ⟵ “Human Growth and Development | DEP 2004 (min. 3 credits)”
  - equivalencies[CLEP-HUMANITIES|HUM 2235 or HUM 2250 (min. 3 credits)]:  ⟵ “Humanities | HUM 2235 or HUM 2250 (min. 3 credits)”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|CGS 1077^ (min. 3 credits)]:  ⟵ “Information Systems | CGS 1077^ (min. 3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|ECO 2013 core (min. 3 credits)]:  ⟵ “Macroeconomics, Principles of | ECO 2013 core (min. 3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|MAN 1021 (min. 3 credits)]:  ⟵ “Management, Principles of | MAN 1021 (min. 3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|MAR 1011 (min. 3 credits)]:  ⟵ “Marketing, Principles of | MAR 1011 (min. 3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|ECO 2023 (min. 3 credits)]:  ⟵ “Microeconomics, Principles of | ECO 2023 (min. 3 credits)”
  - equivalencies[CLEP-PRECALCULUS|MAC 1140 (min. 3 credits)]:  ⟵ “Precalculus | MAC 1140 (min. 3 credits)”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|PSY 2012 core (min. 3 credits)]:  ⟵ “Psychology, Introductory | PSY 2012 core (min. 3 credits)”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|SYG 2000 (min. 3 credits)]:  ⟵ “Sociology, Introductory | SYG 2000 (min. 3 credits)”
  - … 5 more rows
### `dbee3ff9d321c1a1` University of West Florida — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.uwf.edu/undergraduate/transfercredit/ (sha256 404831594d1f)
- checks: {"distinct_exams": 35, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|BSC 1005 BSC 1005L core]:  ⟵ “Biology | BSC 1005 BSC 1005L core | BSC 1005 BSC 1005L core and BSC 2010 BSC 2010L core”
  - equivalencies[IB-BIOLOGY-SL|BSC 1005C core or BSC 1005/BSC 1005L core]:  ⟵ “Biology (SL) 1 | BSC 1005C core or BSC 1005/BSC 1005L core | BSC 1005C core or BSC 1005/BSC 1005L core”
  - equivalencies[IB-BIOLOGY-HL|BSC 1005C core and BSC 2010C core or BSC 1005/BSC 1005L core and BSC 2010/BSC 2010L core]:  ⟵ “Biology (HL) 1 | BSC 1005C core and BSC 2010C core or BSC 1005/BSC 1005L core and BSC 2010/BSC 2010L core | BSC 1005C core and BSC 2010C core or BSC 1005/BSC 1005L core and BSC 2010/BSC 2010L core”
  - equivalencies[IB-BUSINESS-MANAGEMENT|GEB 1011]:  ⟵ “Business and Management | GEB 1011 | GEB 1011 and MAN 1XX1^”
  - equivalencies[IB-CHEMISTRY|CHM 1020 CHM 1020L core]:  ⟵ “Chemistry | CHM 1020 CHM 1020L core | CHM 1020 CHM 1020L core and CHM 2045 CHM 2045L core”
  - equivalencies[IB-COMPUTER-SCIENCE|CGS 1100 (3 credits)]:  ⟵ “Computer Science | CGS 1100 (3 credits) | COP 1000 and CGS 1100^ (6 credits)”
  - equivalencies[IB-ECONOMICS|ECO 1000^]:  ⟵ “Economics | ECO 1000^ | ECO 2013 core and ECO 2023”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|EVR 2001 or EVR 2002^]:  ⟵ “Environmental Systems and Societies (SL) | EVR 2001 or EVR 2002^ | Same as 4”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|ISC X050 (3 credits)]:  ⟵ “Environmental Systems | ISC X050 (3 credits) | ISC X050 and other Interdisciplinary Science or Environmental Science course determined by institution.”
  - equivalencies[IB-FILM|FIL 1000^]:  ⟵ “Film Studies | FIL 1000^ | FIL 1000^ or FIL 1001^ and FIL 1002^ or FIL 1420^”
  - equivalencies[IB-FRENCH|FRE 1121C]:  ⟵ “French: Language B | FRE 1121C | FRE 1121C and FRE 2XX1”
  - equivalencies[IB-GEOGRAPHY|GEA 2000]:  ⟵ “Geography | GEA 2000 | GEO 1200^ and GEO 1400^”
  - equivalencies[IB-GERMAN|One semester of language credit at Elementary Language II level (min. 3 credits)]:  ⟵ “German: Language B | One semester of language credit at Elementary Language II level (min. 3 credits) | Two semesters of Elementary Language and Intermediate Language I level (min. 6 credits)”
  - equivalencies[IB-GLOBAL-POLITICS-SL|INR X002]:  ⟵ “Global Politics (SL) | INR X002 | Same as 4”
  - equivalencies[IB-GLOBAL-POLITICS-HL|INR X002]:  ⟵ “Global Politics (HL) | INR X002 | INR X002 and additional Politics/Government course (min. 6 credits)”
  - equivalencies[IB-HISTORY|WOH 1030^]:  ⟵ “History | WOH 1030^ | WOH 1030^ and HIS 1XX1^”
  - equivalencies[IB-HISTORY-SL|WOH 1030^]:  ⟵ “History (SL) 3 | WOH 1030^ | Same as 4”
  - equivalencies[IB-HISTORY-HL|WOH 1030]:  ⟵ “History (HL): History of Africa and the Middle East 3 | WOH 1030 | WOH 1030 and WOH 1031”
  - equivalencies[IB-HISTORY-HL|WOH 1030^]:  ⟵ “History (HL): History of the Americas 3 | WOH 1030^ | WOH 1030^ and AMH 2010 or AMH 2020 core”
  - equivalencies[IB-HISTORY-HL|WOH 1030^]:  ⟵ “History (HL): History of Asia and Oceania 3 | WOH 1030^ | WOH 1030^ and WOH 1031”
  - equivalencies[IB-HISTORY-HL|WOH 1030^]:  ⟵ “History (HL): History of Europe 3 | WOH 1030^ | WOH 1030^ and WOH 1031^”
  - equivalencies[IB-HISTORY|No direct equivalent (min. 3 credits)]:  ⟵ “Islamic History | No direct equivalent (min. 3 credits) | No direct equivalent (min. 6 credits)”
  - equivalencies[IB-LATIN|LAT 1130^ or LAT 1XX1^]:  ⟵ “Latin | LAT 1130^ or LAT 1XX1^ | LAT 1130^ and LAT 1XX1^ or LNW 1XX1^”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|MAC 1105 core]:  ⟵ “Math Analysis and Approaches (SL) | MAC 1105 core | MAC 1105 core and MAC 1140”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|MAC 1105 core]:  ⟵ “Math Analysis and Approaches (HL) | MAC 1105 core | MAC 1105 core and MAC 2311 core or MAC 1140 or MAC 1147”
  - … 14 more rows
### `48fc504b8a779503` University of West Florida — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.uwf.edu/undergraduate/transfercredit/ (sha256 404831594d1f)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 90 ⟵ “For example, no more than 90 hours of a 120-hour degree program can be applied if earned through transfer credit or any of the acceleration mechanisms recognized.”
### `72e51ff84f0a3467` Valencia College — awards 2026-27 [new] (source_unlabeled)
- source: https://valenciacollege.edu/finaid/programs/ (sha256 d48aa22c67ed)
- checks: {"thresholds": null}
  - eligibility_summary: A merit-based scholarship through the state of Florida. A student is determined to be eligible based on high school GPA and must meet specific state requirements for awarding and renewal each year. ⟵ “Bright Futures | A merit-based scholarship through the state of Florida. A student is determined to be eligible based on high school GPA and must meet specific state requirements for awarding and renewal each year. | A minimum of 6 credit hours (halftime). The amount adjusts based on the number of e”
### `8c1868b534f7a610` Valencia College — awards 2026-27 [new] (source_unlabeled)
- source: https://valenciacollege.edu/finaid/programs/ (sha256 d48aa22c67ed)
- checks: {"thresholds": null}
  - eligibility_summary: Merit-based scholarship for students admitted into the James M. and Dayle L. Seneff Honors College. Students must meet specific scholarship criteria. ⟵ “Valencia Honors Scholarship | Merit-based scholarship for students admitted into the James M. and Dayle L. Seneff Honors College. Students must meet specific scholarship criteria. | Must be registered for at least one honors class.”
### `b04dc966dab3444a` Valencia College — awards 2026-27 [new] (source_unlabeled)
- source: https://valenciacollege.edu/finaid/programs/ (sha256 d48aa22c67ed)
- checks: {"thresholds": null}
  - eligibility_summary: Foundation scholarships may be need or merit-based depending on scholarship criteria. ⟵ “Valencia Foundation Scholarships | Foundation scholarships may be need or merit-based depending on scholarship criteria. | Please review your scholarship award letter for minimum enrollment requirements.”
### `ca0464f4f9f8bc14` Valencia College — awards 2026-27 [new] (source_unlabeled)
- source: https://valenciacollege.edu/finaid/programs/ (sha256 d48aa22c67ed)
- checks: {"thresholds": null}
  - eligibility_summary: A need-based scholarship for students who demonstrate unmet financial need and who qualify for limited or no other source of grant or scholarship funding. ⟵ “Valencia Advantage Scholarship | A need-based scholarship for students who demonstrate unmet financial need and who qualify for limited or no other source of grant or scholarship funding. | A minimum of 6 credit hours (halftime). Award amounts vary depending on demonstrated financial need.”
### `md00cba0b9cd1635` Warner University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://warner.edu/admissions-aid/dual-enrollment/ (sha256 adf07a6a69e2)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “3.00 unweighted grade point average”
  - per_credit_hour_charge: 105.07 ⟵ “$105.07 per credit hour per student and will provide student access to all required instructional materials/textbooks through the”

## Exceptions (500)

### `c858e491269fbc87` AdventHealth University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ahu.edu/programs/doctor-of-nurse-anesthesia-practice/tuition-and-fees (sha256 9c228dfef4fd)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 16800 ⟵ “Tuition | 16,800”
  - column:Matriculation Fee: 300 ⟵ “Matriculation Fee | 300”
  - column:Professional Program Fee: 1000 ⟵ “Professional Program Fee | 1,000”
  - column:Books (approx) *: 1500 ⟵ “Books (approx) * | 1,500”
  - column:AANA Associate Membership (student pays to AANA) *: 200 ⟵ “AANA Associate Membership (student pays to AANA) * | 200”
  - column:Laptop Computer *: 1050 ⟵ “Laptop Computer * | 1,050”
  - column:TOTAL: 20850 ⟵ “TOTAL | $20,850”
### `3b382905593b4815` Albizu University-Miami — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.albizu.edu/wp-content/uploads/dlm_uploads/2026/08/SAP-Appeal-Form-MIA.pdf (sha256 337d94ed9ba9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “See examples of such unusual circumstances and the appropriate supporting documentation below.”
### `463265069670e95c` Albizu University-Miami — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.albizu.edu/wp-content/uploads/dlm_uploads/2026/08/SAP-Appeal-Form-MIA.pdf (sha256 337d94ed9ba9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Form Full Name: Student ID Number: Date: Address: Phone Number: Email: Type of Appeal: ( ) Loss of Financial Aid ( ) Academic Suspension Indicate the Academic Year: Add a checkmark next to the academic term for which you are requesting the appeal. ( ) Fall Term ( ) Spring Term ( ) Summer Term Add a checkmark next to the circumstance(s) that prevented ach”
  - sentence: sap_appeal ⟵ “Ensure the appeal includes the following required documents: ( ) Signed Appeal Form Signed (See page 2) ( )Signed and dated personal statement of explanation ( ) Relevant supporting documents substantiating extenuating circumstances ( )Academic Plan of Action (obtained from the Academic Advisor) Important note: Albizu University will not accept or review a SAP Appeal without the aforementioned req”
  - sentence: sap_appeal ⟵ “Committee Review Allow the SAP Appeals Committee 15 working days to review the student submission.”
  - sentence: sap_appeal ⟵ “SAP Appeal decisions are non-appealable.”
### `4819892528325dc6` Ave Maria University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.avemaria.edu/pdfs/financial-aid/Satisfactory%20Academic%20Progress%20Policy.pdf (sha256 4823df909f1b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Petition for Reinstatement of donor funded scholarships* If the failure to meet the minimum criteria defined by the respective donor agreement is attributable to extenuating circumstances such as the following, the student may appeal the loss of the scholarship eligibility. • Death/illness of an immediate family member • Personal injury/illness • Physical disability • Other extraordinary/extenuati”
### `4ef843e60ee2ba4a` Ave Maria University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.avemaria.edu/admissions/financial-aid-policies (sha256 1f1e2e6044e0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “We can process a Dependency override for any of the following reasons: Dependency Override Review An unsuitable household (e.g., child removed from the household and placed in foster care, tutorship, etc.) Human trafficking Legally granted refugee or asylum status Parental abandonment or estrangement Student or parental incarceration.”
  - sentence: dependency_override ⟵ “The following circumstances do not merit a Dependency Override: Parents refuse to contribute to the student's education.”
### `5b267b16a31ecd73` Ave Maria University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.avemaria.edu/pdfs/financial-aid/Professional%20Judgment%20Review.pdf (sha256 fb114d6752dc)
- issues: semantic_review_required, conflicting_sources:https://www.avemaria.edu/admissions/financial-aid-faq,https://www.avemaria.edu/admissions/financial-aid-policies
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment Review The office of financial aid at Ave Maria University recognizes that the formula used to calculate aid eligibility may not accurately reflect current special circumstances for individual students and/or their families.”
  - sentence: professional_judgment ⟵ “Circumstances NOT considered for Professional Judgement review: • Standard living expenses (utilities, car payments, etc.) • Mortgage payments • Credit card/other personal debts • Filing for bankruptcy • Elective surgeries • All other discretionary expenses • Different university offering more aid • Reduction in 401K/investment values Cost of Attendance (COA) Adjustment- Link to the Change in COA ”
### `6f89ead018c4d7b5` Ave Maria University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.avemaria.edu/admissions/financial-aid-policies (sha256 1f1e2e6044e0)
- issues: semantic_review_required, conflicting_sources:https://www.avemaria.edu/admissions/financial-aid-faq,https://www.avemaria.edu/pdfs/financial-aid/Professional%20Judgment%20Review.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgement Policy See Ave Maria University's Professional Judgement Policy Excessive Awards Eligibility for institutional aid may change based on funds received from other sources.”
### `72a88b24e9b7935a` Ave Maria University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.avemaria.edu/admissions/financial-aid-faq (sha256 4dacaf644f01)
- issues: semantic_review_required, conflicting_sources:https://www.avemaria.edu/admissions/financial-aid-policies,https://www.avemaria.edu/pdfs/financial-aid/Professional%20Judgment%20Review.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If your situation is unusual or financial circumstances have significantly changed from the previous tax year, you may submit a Professional Judgement appeal.”
  - sentence: professional_judgment ⟵ “Professional Judgement Form WHAT IF I HAVE MORE AID THAN I NEED?”
### `a223c707ed9e6308` Ave Maria University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.avemaria.edu/admissions/financial-aid-policies (sha256 1f1e2e6044e0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Dependency Override Appeal Dependency Override Financial Aid professionals have the authority, through Section 480(d) (7) of the Higher Education Act, to change a student's status from Dependent to Independent in cases involving unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Link to the Dependency Override Appeal Form Unusual Circumstances Appeal Dependent student without parental support Most unmarried undergraduates under the age of 24 are considered dependent for federal financial aid purposes and therefore must provide parental information on the FAFSA.”
### `c4e3563aab833ebe` Ave Maria University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.avemaria.edu/admissions/financial-aid-faq (sha256 4dacaf644f01)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “To learn more about the Satisfactory Academic Progress (SAP) policy and see how to appeal the loss of your aid visit our web-site.”
### `1ea2455d97dd6c3d` Barry University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.barry.edu/en/financial-aid/satisfactory-academic-progress/ (sha256 576e32eb0cf4)
- issues: semantic_review_required, conflicting_sources:https://www.barry.edu/en/financial-aid/professional-judgment-and-appeals/,https://www.barry.edu/en/financial-aid/undergraduate/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The probationary period may be extended to more than one semester if approved by professional judgment.”
### `707d4b789ec26b93` Barry University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.barry.edu/en/financial-aid/undergraduate/ (sha256 0fd452ce48bd)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students and/or families may need to indicate special circumstances that may not be evident on the FAFSA, or circumstances may have changed.”
### `74a60f643e4c1375` Barry University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.barry.edu/en/financial-aid/undergraduate/ (sha256 0fd452ce48bd)
- issues: semantic_review_required, conflicting_sources:https://www.barry.edu/en/financial-aid/professional-judgment-and-appeals/,https://www.barry.edu/en/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “OverviewProfessional Judgment and Appeals Occasionally, unique circumstances influence income for students and/or families.”
  - sentence: professional_judgment ⟵ “When these situations arise, we may re-evaluate a student’s aid eligibility based on current circumstances using the Professional Judgment (PJ) process.”
### `e786f64b432a99ce` Barry University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.barry.edu/en/financial-aid/satisfactory-academic-progress/ (sha256 576e32eb0cf4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “A University Satisfactory Academic Progress appeal form must be submitted via the Financial Aid Portal, along with supporting documentation.”
### `fb17c7cf1e365949` Barry University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.barry.edu/en/financial-aid/professional-judgment-and-appeals/ (sha256 b7a1e9f06d06)
- issues: semantic_review_required, conflicting_sources:https://www.barry.edu/en/financial-aid/satisfactory-academic-progress/,https://www.barry.edu/en/financial-aid/undergraduate/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Professional Judgment and Appeals - Undergraduate Financial Aid - Barry University, Miami, FL Skip to main content About Barry Academics Admissions Student Life Alumni Give Apply Now Contact Us iMessage WhatsApp Chat Facebook Messenger Text Us Live Chat Ask a Question Request More Information myBarry Apply Now Create Account Sign in How do I apply?”
  - sentence: professional_judgment ⟵ “When these situations arise, we may re-evaluate a student’s aid eligibility based on current circumstances using the Professional Judgment (PJ) process.”
  - sentence: professional_judgment ⟵ “Select +- Request (upper right-hand corner) Click the + next to the type of Professional Judgment you want to request Type in a brief explanation for the request (e.g. "I am requesting a PJ because my parent lost their job."), and hit submit to create a task (it will appear as a tab at the top of the screen) Follow the instructions to complete the webform and upload supporting documentation If it ”
### `bac42125f1b671b2` Barry University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.barry.edu/en/admissions/undergraduate/ (sha256 a9db8687d978)
- issues: components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": false, "rows": 9}
  - on_campus:Tuition/Fees: 34600 ⟵ “Tuition/Fees | $34,600 | $34,600 | $34,600”
  - on_campus:Books: 1500 ⟵ “Books | $1,500 | $1,500 | $1,500”
  - on_campus:Housing/Food: 14736 ⟵ “Housing/Food | $14,736 | $17,442 | $3,078”
  - on_campus:Personal Expenses: 3742 ⟵ “Personal Expenses | $3,742 | $4,108 | $1,150”
  - on_campus:Transportation: 1400 ⟵ “Transportation | $1,400 | $3,280 | $1,944”
  - on_campus:Student Services Fee: 1000 ⟵ “Student Services Fee | $1,000 | $1,000 | $1,000”
  - on_campus:Federal Loan Fees: 116 ⟵ “Federal Loan Fees | $116 | $116 | $116”
  - on_campus:Direct Costs: 50336 ⟵ “Direct Costs | $50,336 | $35,600 | $35,600”
  - on_campus:Total COA: 57094 ⟵ “Total COA | $57,094 | $62,046 | $43,388”
  - off_campus_not_with_family:Tuition/Fees: 34600 ⟵ “Tuition/Fees | $34,600 | $34,600 | $34,600”
  - off_campus_not_with_family:Books: 1500 ⟵ “Books | $1,500 | $1,500 | $1,500”
  - off_campus_not_with_family:Housing/Food: 17442 ⟵ “Housing/Food | $14,736 | $17,442 | $3,078”
  - off_campus_not_with_family:Personal Expenses: 4108 ⟵ “Personal Expenses | $3,742 | $4,108 | $1,150”
  - off_campus_not_with_family:Transportation: 3280 ⟵ “Transportation | $1,400 | $3,280 | $1,944”
  - off_campus_not_with_family:Student Services Fee: 1000 ⟵ “Student Services Fee | $1,000 | $1,000 | $1,000”
  - off_campus_not_with_family:Federal Loan Fees: 116 ⟵ “Federal Loan Fees | $116 | $116 | $116”
  - off_campus_not_with_family:Direct Costs: 35600 ⟵ “Direct Costs | $50,336 | $35,600 | $35,600”
  - off_campus_not_with_family:Total COA: 62046 ⟵ “Total COA | $57,094 | $62,046 | $43,388”
  - with_parents_or_family:Tuition/Fees: 34600 ⟵ “Tuition/Fees | $34,600 | $34,600 | $34,600”
  - with_parents_or_family:Books: 1500 ⟵ “Books | $1,500 | $1,500 | $1,500”
  - with_parents_or_family:Housing/Food: 3078 ⟵ “Housing/Food | $14,736 | $17,442 | $3,078”
  - with_parents_or_family:Personal Expenses: 1150 ⟵ “Personal Expenses | $3,742 | $4,108 | $1,150”
  - with_parents_or_family:Transportation: 1944 ⟵ “Transportation | $1,400 | $3,280 | $1,944”
  - with_parents_or_family:Student Services Fee: 1000 ⟵ “Student Services Fee | $1,000 | $1,000 | $1,000”
  - with_parents_or_family:Federal Loan Fees: 116 ⟵ “Federal Loan Fees | $116 | $116 | $116”
  - … 2 more rows
### `af7428c9369a5bd2` Beacon College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.beaconcollege.edu/admissions-aid/financial-aid-faqs/ (sha256 5f49565161eb)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If you are a returning student whose grades did not pass Beacon’s satisfactory academic progress standards last semester, your appeal letter must be reviewed and approved before financial aid will be paid into your student account.”
### `1449042da29d9f30` Bethune-Cookman University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cookman.edu/osas/tuition.html (sha256 b9b4a4fe0c22)
- issues: multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 11}
  - column:Tuition (12 - 18 hours) *: 14536.0 ⟵ “Tuition (12 - 18 hours) * | $7,268.00 | $7,268.00 | $14,536.00”
  - column:Room (On-Campus Housing): 7744.0 ⟵ “Room (On-Campus Housing) | $3,872.00 | $3,872.00 | $7,744.00”
  - column:Board: 3646.0 ⟵ “Board | $1,823.00 | $1,823.00 | $3,646.00”
  - column:Book Smart (Opt-Out date listed on Student Account Website): 680.0 ⟵ “Book Smart (Opt-Out date listed on Student Account Website) | $340.00 | $340.00 | $680.00”
  - column:Fees: 998.0 ⟵ “Fees | $499.00 | $499.00 | $998.00”
  - column:Total (On-Campus Housing): 27604.0 ⟵ “Total (On-Campus Housing) | $13,802.00 | $13,802.00 | $27,604.00”
  - column:Books & Supplies: 1450 ⟵ “Books & Supplies | $725.00 | $725.00 | $1,450”
  - column:Personal Expenses: 3300.0 ⟵ “Personal Expenses | $1,650.00 | $1,650.00 | $3,300.00”
  - column:Transportation: 2854.0 ⟵ “Transportation | $1,427.00 | $1,427.00 | $2,854.00”
  - column:Total: 7604.0 ⟵ “Total | $3,802.00 | $3,802.00 | $7,604.00”
  - column:On-Campus - Cost of Attendance (COA) = Direct Costs + Estimated Indirect Costs: 35208.0 ⟵ “On-Campus - Cost of Attendance (COA) = Direct Costs + Estimated Indirect Costs | $17,604.00 | $17,604.00 | $35,208.00”
### `1a43539f8d912603` Broward College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.broward.edu/admissions/financial-aid/maintaining-eligibility.html (sha256 6a0d32feb034)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Status and Appeal If you are in a Failed SAP status, you may request an appeal.”
  - sentence: sap_appeal ⟵ “The student will receive, within 14 business days, an explanation via email of why an appeal was denied, and if approved, what is required during the approved term(s). *Please Note: A SAP Appeal will not be approved for students who have lost financial aid eligibility due to Time to Complete as per federal regulations.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal 2025-2026 Tools for Calculating Satisfactory Academic Progress GPA Calculator Students must maintain a minimum 2.0 cumulative (FINANCIAL AID) GPA in order to remain eligible for financial aid.”
### `1b8d375190f99131` Broward College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.broward.edu/admissions/financial-aid/forms.html (sha256 b4488dd674e6)
- issues: semantic_review_required, conflicting_sources:https://www.broward.edu/admissions/financial-aid/professional-judgment.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Verification Special Circumstances Unusual Enrollment History Additional Forms High School Outreach WHY WAS I SELECTED FOR VERIFICATION AND WHAT DOES THAT MEAN?”
  - sentence: need_based_special_circumstances ⟵ “Some of those special circumstances include job loss, income reduction, asset value reduction, illness, etc.”
### `25311b8605ae585b` Broward College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.broward.edu/admissions/financial-aid/forms.html (sha256 b4488dd674e6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Note: Completion of these forms does not always equal an outcome that changes your aid award amount or your eligibility to receive aid. 2026-2027 2026-2027 Independent Document Override 2026-2027 Special Circumstances for Income Adjustment 2026-2027 Request for Cost of Attendance Increase 2026-2027 Unusual Circumstances for Dependency Override 2026-2027 Satisfactory Academic Progress Appeal The De”
### `5d55a041e4121a24` Broward College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/professional-judgment.html (sha256 e09020905e89)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “All Professional Judgment applications must contain a detailed letter explaining the situation and supporting documentation to be considered.”
### `df427ffe141ce286` Broward College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/financial-aid/professional-judgment.html (sha256 e09020905e89)
- issues: semantic_review_required, conflicting_sources:https://www.broward.edu/admissions/financial-aid/forms.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you experienced a significant change in your household financial situation and want to apply for re-evaluation, please follow the steps below: First, determine which type of appeal you need to file: Types of Appeals | Change to Expected Family Contribution (EFC) | Change to Cost of Attendance (COA) | Loss or reduction of employment/earnings The loss or reduction must be significant and sustaine”
  - sentence: need_based_special_circumstances ⟵ “Determine the documentation needed to submit to support your situation: Request for Income Adjustment Appeals Form Loss or Reduction in Employment/Earnings A detailed letter of explanation that provides a clear timeline regarding your change in income.”
### `65d8ee71d96198f4` Broward College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/tuition-costs/cost-of-attendance.html (sha256 a4194306a9de)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition: 984.0 ⟵ “Tuition | $984.00 | $984.00”
  - with_parents_or_family:Fees: 3492.0 ⟵ “Fees | $3,492.00 | $3,492.00”
  - with_parents_or_family:Food & Housing: 3861.0 ⟵ “Food & Housing | $3,861.00 | $9,750.00”
  - with_parents_or_family:Books, Course Material, Supplies, & Equipment: 1502.0 ⟵ “Books, Course Material, Supplies, & Equipment | $1,502.00 | $1,000.00”
  - with_parents_or_family:Transportation: 2600.0 ⟵ “Transportation | $2,600.00 | $5,000.00”
  - with_parents_or_family:Personal Expenses: 1475.0 ⟵ “Personal Expenses | $1,475.00 | $2,500.00”
  - with_parents_or_family:Total: 13914.0 ⟵ “Total | $13,914.00 | $22,726.00”
  - column:Tuition: 984.0 ⟵ “Tuition | $984.00 | $984.00”
  - column:Fees: 3492.0 ⟵ “Fees | $3,492.00 | $3,492.00”
  - column:Food & Housing: 9750.0 ⟵ “Food & Housing | $3,861.00 | $9,750.00”
  - column:Books, Course Material, Supplies, & Equipment: 1000.0 ⟵ “Books, Course Material, Supplies, & Equipment | $1,502.00 | $1,000.00”
  - column:Transportation: 5000.0 ⟵ “Transportation | $2,600.00 | $5,000.00”
  - column:Personal Expenses: 2500.0 ⟵ “Personal Expenses | $1,475.00 | $2,500.00”
  - column:Total: 22726.0 ⟵ “Total | $13,914.00 | $22,726.00”
### `9082884f2f53c8b2` Broward College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/tuition-costs/cost-of-attendance.html (sha256 a4194306a9de)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition: 984.0 ⟵ “Tuition | $984.00 | $984.00”
  - with_parents_or_family:Fees: 431.0 ⟵ “Fees | $431.00 | $431.00”
  - with_parents_or_family:Food & Housing: 3861.0 ⟵ “Food & Housing | $3,861.00 | $9,750.00”
  - with_parents_or_family:Books, Course Material, Supplies, & Equipment: 1502.0 ⟵ “Books, Course Material, Supplies, & Equipment | $1,502.00 | $1,000.00”
  - with_parents_or_family:Transportation: 2600.0 ⟵ “Transportation | $2,600.00 | $5,000.00”
  - with_parents_or_family:Personal Expenses: 1475.0 ⟵ “Personal Expenses | $1,475.00 | $2,500.00”
  - with_parents_or_family:Total: 10853.0 ⟵ “Total | $10,853.00 | $19,665.00”
  - column:Tuition: 984.0 ⟵ “Tuition | $984.00 | $984.00”
  - column:Fees: 431.0 ⟵ “Fees | $431.00 | $431.00”
  - column:Food & Housing: 9750.0 ⟵ “Food & Housing | $3,861.00 | $9,750.00”
  - column:Books, Course Material, Supplies, & Equipment: 1000.0 ⟵ “Books, Course Material, Supplies, & Equipment | $1,502.00 | $1,000.00”
  - column:Transportation: 5000.0 ⟵ “Transportation | $2,600.00 | $5,000.00”
  - column:Personal Expenses: 2500.0 ⟵ “Personal Expenses | $1,475.00 | $2,500.00”
  - column:Total: 19665.0 ⟵ “Total | $10,853.00 | $19,665.00”
### `bb5e94a287e5a29c` Broward College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/tuition-costs/ (sha256 215931ae09c1)
- issues: ambiguous_year_labels, residency_unknown
- checks: {"columns": 1, "rows": 8}
  - column:Tuition Fee: 82.0 ⟵ “Tuition Fee | $82.00”
  - column:Differential Tuition Fee: 104.0 ⟵ “Differential Tuition Fee | $104.00”
  - column:Distance Learning Fee: 9.0 ⟵ “Distance Learning Fee | $9.00”
  - column:Student Activities Fee: 8.2 ⟵ “Student Activities Fee | $8.20”
  - column:Student Financial Aid Fee: 9.3 ⟵ “Student Financial Aid Fee | $9.30”
  - column:Capital Improvement Fee: 19.6 ⟵ “Capital Improvement Fee | $19.60”
  - column:Library Fee: 2.0 ⟵ “Library Fee | $2.00”
  - column:Technology Fee: 9.3 ⟵ “Technology Fee | $9.30”
### `1424395506e71df8` Broward College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.broward.edu/admissions/credit-for-prior-learning/clep-exams.html (sha256 61d423539a27)
- issues: merged_score_cells
- checks: {"distinct_exams": 32, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government Meets Civic Literacy Requirement | POS2041 | 3 | 50 | Yes | Yes | ”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | AML2010 | 3 | 50 | Yes | Yes | Yes”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|N/A]:  ⟵ “Analyzing and Interpreting Literature | None (Recommend American or English Literature) | N/A | N/A | No |  | ”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | BSC1005 (no lab credit) | *3 | 50 | Yes |  | ”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | MAC2233 (Business Calculus) | 3 | 50 | Yes |  | ”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | CHM1020 (no lab credit) | *3 | 50 | Yes |  | ”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | MAC1105 | 3 | 50 | Yes |  | ”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition (Recommended for BC Purposes) | ENC1101 & ENC1102 | 6 | 50 | Yes |  | ”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|N/A]:  ⟵ “College Composition Modular (Not recommended for BC Purposes) | None | N/A | N/A | No |  | ”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra-Trigonometry (unavailable after 6/30/2006) | MAC1147 | 3 | 50 | No |  | ”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | MGF1130 | 3 | 50 | Yes |  | ”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | LIT2000 | 3 | 50 | Yes | Yes | Yes”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | ACG2001 | 3 | 50 | Yes |  | ”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50 59]:  ⟵ “French Language | FRE1120 FRE1120 & FRE1121 (Meets Foreign Language Requirement) | 4 8 | 50 59 | Yes |  | Yes”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50 60]:  ⟵ “German Language | GER1120 GER1120 & GER1121 (Meets Foreign Language Requirement) | 4 8 | 50 60 | Yes |  | Yes”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States 1: Early colonization's to 1877 | AMH2010 | 3 | 50 | Yes | Yes | ”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States 2: 1865 to Present | AMH2020 | 3 | 50 | Yes | Yes | ”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | DEP2004 | 3 | 50 | Yes | Yes | Yes”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | HUM1235 | 3 | 50 | Yes | Yes | Yes”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems (Formerly Information Systems and Computer Applications) Meets Digital Literacy Requirement | CGS1060C | 3 | 50 | Yes |  | ”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | EDP2002 | 3 | 50 | Yes |  | ”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introduction to Business Law | BUL2241 | 3 | 50 | Yes |  | ”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PSY2012 | 3 | 50 | Yes | Yes | Yes”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | ECO2013 | 3 | 50 | Yes | Yes | ”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | MAN2021 | 3 | 50 | Yes |  | ”
  - … 8 more rows
### `m770987f8b8cd31e` College of Central Florida — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://pr.cf.edu/files/admissions/dual-enrollment/dual-articulation-ocala.pdf (sha256 39d494920e4d)
- issues: ambiguous_year_labels, conflicting_values:max_credit_hours_per_term, multicolumn_layout_review
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa"], "merged_pages": 6, "tiers": 3}
  - eligibility_tier: 2.0 ⟵ “courses. An overall GPA of 2.0 on an un-weighted 4.0 scale is required for students to enroll in”
  - eligibility_tier: 3.0 ⟵ “a 3.0 grade point average in EMT program coursework and satisfy all EMT program entry”
  - eligibility_tier: 3.0 ⟵ “1. Students must have an overall grade point average (GPA) of 3.0 on an unweighted”
  - max_credit_hours_per_term: 18 ⟵ “enroll in at least 12 credits and may take up to 18 credit hours in the fall and spring terms.”
  - eligibility_tier: 3.0 ⟵ “a. An overall grade point average (GPA) of 3.0 on an unweighted 4.0 scale is required”
  - eligibility_tier: 3.0 ⟵ “maintenance of a 3.0 unweighted GPA and the minimum GPA required by CF.”
  - eligibility_tier: 3.0 ⟵ “1. Students must have an overall grade point average (GPA) of 3.0 on an unweighted”
  - college_gpa_to_continue: 3.0 ⟵ “Continued eligibility requires that students maintain a 3.0 unweighted high school”
  - max_credit_hours_per_term: 18 ⟵ “CF Collegiate Academy students must enroll in at least 12 credits and may take up to 18 credit hours in fall and spring semesters. Collegiate Academy students are also eligible for summer classes. Traditional dual enrolled students may take as little as one course.”
  - college_gpa_to_continue: 3.0 ⟵ “The student must maintain a 3.0 GPA to remain eligible for the program.”
  - max_credit_hours_per_term: 18 ⟵ “maximum of 18 credit hours in fall and spring semesters. Students may register for a maximum of”
  - eligibility_tier: 3.0 ⟵ “No. You must maintain at least a 3.0 high school GPA (or 2.0 for Career Academy/Vocational Cohorts) to remain eligible for dual enrollment. Please check with your high school counselor if you fear your GPA might be too low.”
  - max_credit_hours_per_term: 6 ⟵ “ 9th grade: up to 6 credit hours (2 classes) each semester and during summer”
  - max_credit_hours_per_term: 6 ⟵ “ 10th grade: up to 6 credit hours (2 classes) each semester and up to 9 credit”
  - max_credit_hours_per_term: 9 ⟵ “ 11th grade: up to 9 credit hours (3 classes) each semester and up to 12 credit”
  - max_credit_hours_per_term: 16 ⟵ “ 12th grade: up to 16 credit hours each semester”
  - max_credit_hours_per_term: 12 ⟵ “ Up to 12 credit hours during the summer term”
  - eligibility_tier: 3.0 ⟵ “helped me toward a career in               » 3.0 unweighted GPA”
### `b1ce2e5686578932` Daytona State College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.daytonastate.edu:443/financial-aid/ (sha256 14f192875743)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Please contact the Financial Aid Services Office by calling 386-506-3015 or emailing financialaid@daytonastate.edu for the process on submitting a SAP Appeal.”
  - sentence: sap_appeal ⟵ “Fall 2026 SAP Appeal Form Other Forms Change of Major or Program Correction to Graduate Student Status Clock Hour Program Intent to Enroll Students currently enrolled in a clock hour program who will be continuing for the next consecutive semester are required to complete this form, as there are more than 14 days between the semesters.”
### `4fc1bca9baec61e3` Eckerd College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eckerd.edu/admissions/financial-aid/ (sha256 d11ca48ae7e1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances: student’s dependency status is based on a unique situation (e.g. parental abandonment, abuse or incarceration) where there is no parental involvement.”
### `edb38c964b1ebf19` Eckerd College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eckerd.edu/admissions/financial-aid/ (sha256 d11ca48ae7e1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “This is more commonly referred to as a dependency override.”
  - sentence: dependency_override ⟵ “Self supporting students without a documented extenuating family circumstance do not qualify for a dependency override.”
### `f9262fd680b8d023` Eckerd College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eckerd.edu/admissions/financial-aid/ (sha256 d11ca48ae7e1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The beautiful scenery and the financial aid were what drew me in more.” —Tamiya Palmer ’26 Applying for aid FAFSA Verification Renewal Requirements Cost of Attendance (COA) Professional Judgment Applying for Aid At Eckerd College, we believe financial aid should help make a college education more accessible and help you and your family plan with confidence.”
### `4ea0634d3a2ba9f9` Eckerd College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.eckerd.edu/bursar/tuition/ (sha256 f44e56c7a2a6)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - column:Tuition: 27135 ⟵ “Tuition | $27,135 | $27,135 | $54,270”
  - column:Traditional Double Room: 4097 ⟵ “Traditional Double Room | $4,097 | $4,097 | $8,194”
  - column:Meal Plan Tier A-250 (Anytime Plan): 3719 ⟵ “Meal Plan Tier A-250 (Anytime Plan) | $3,719 | $3,719 | $7,438”
  - column:Student Activity Fee: 218 ⟵ “Student Activity Fee | $218 | $218 | $436”
  - column:Technology Fee: 165 ⟵ “Technology Fee | $165 | $165 | $330”
  - column:Total: 35334 ⟵ “Total | $35,334 | $35,334 | $70,668”
  - column:Tuition: 27135 ⟵ “Tuition | $27,135 | $27,135 | $54,270”
  - column:Traditional Double Room: 4097 ⟵ “Traditional Double Room | $4,097 | $4,097 | $8,194”
  - column:Meal Plan Tier A-250 (Anytime Plan): 3719 ⟵ “Meal Plan Tier A-250 (Anytime Plan) | $3,719 | $3,719 | $7,438”
  - column:Student Activity Fee: 218 ⟵ “Student Activity Fee | $218 | $218 | $436”
  - column:Technology Fee: 165 ⟵ “Technology Fee | $165 | $165 | $330”
  - column:Total: 35334 ⟵ “Total | $35,334 | $35,334 | $70,668”
  - column:Tuition: 54270 ⟵ “Tuition | $27,135 | $27,135 | $54,270”
  - column:Traditional Double Room: 8194 ⟵ “Traditional Double Room | $4,097 | $4,097 | $8,194”
  - column:Meal Plan Tier A-250 (Anytime Plan): 7438 ⟵ “Meal Plan Tier A-250 (Anytime Plan) | $3,719 | $3,719 | $7,438”
  - column:Student Activity Fee: 436 ⟵ “Student Activity Fee | $218 | $218 | $436”
  - column:Technology Fee: 330 ⟵ “Technology Fee | $165 | $165 | $330”
  - column:Total: 70668 ⟵ “Total | $35,334 | $35,334 | $70,668”
### `a07f8300d52fff72` Flagler College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.flagler.edu/sites/default/files/t4/media/documents/admissions-amp-aid/financial-aid-process/Flagler_College_Financial_Aid_Verification_Policy.pdf (sha256 5b711cfa9227)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “These cases must be sufficiently documented and may be processed in accordance with regulations as defined in Professional Judgement and Dependency Overrides Statute: HEA Sec. 479A(a)(7) and Sec. 480(d)(7).”
### `bdd0e8a610915fd3` Flagler College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.flagler.edu/admissions-aid/financial-aid-scholarships/financial-aid-process/fafsa (sha256 9d1490d0e0b4)
- issues: semantic_review_required, conflicting_sources:https://www.flagler.edu/sites/default/files/t4/media/documents/admissions-amp-aid/financial-aid-process/Flagler_College_Financial_Aid_Verification_Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “FAFSA guidance This link provides a series of videos with additional information about completing and submitting the FAFSA, special circumstances, troubleshooting, and more!”
### `c8c499e1f987b252` Flagler College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.flagler.edu/sites/default/files/t4/media/documents/admissions-amp-aid/financial-aid-process/Flagler_College_Financial_Aid_Verification_Policy.pdf (sha256 5b711cfa9227)
- issues: semantic_review_required, conflicting_sources:https://www.flagler.edu/admissions-aid/financial-aid-scholarships/financial-aid-process/fafsa
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Under certain circumstances a CPS selected application may be excluded from some or all of the federal verification requirements due to unusual circumstances including: the death of the student, a student who is not an aid recipient, a student who is only eligible to receive unsubsidized student financial assistance.”
### `5b3d65d653bc1bca` Flagler College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.flagler.edu/admissions-aid/tuition-and-fees/cost-details (sha256 cb75dc46a8c4)
- issues: conflicting_sources:https://www.flagler.edu/admissions-aid/tuition-and-fees
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 36120 ⟵ “Tuition | $36,120 | $36,120 | $36,120”
  - on_campus:Fees: 600 ⟵ “Fees | $600 | $600 | $600”
  - on_campus:Food and Housing: 17420 ⟵ “Food and Housing | $17,420 | $14,290 | $5,560”
  - on_campus:Books/Supplies: 960 ⟵ “Books/Supplies | $960 | $960 | $960”
  - on_campus:Personal/Misc.: 2340 ⟵ “Personal/Misc. | $2,340 | $2,340 | $2,340”
  - on_campus:Transportation: 1900 ⟵ “Transportation | $1,900 | $1,900 | $1,900”
  - on_campus:Loan Fees: 162 ⟵ “Loan Fees | $162 | $162 | $162”
  - on_campus:Total Cost of Attendance: 59502 ⟵ “Total Cost of Attendance | $59,502 | $56,372 | $47,642”
  - off_campus_not_with_family:Tuition: 36120 ⟵ “Tuition | $36,120 | $36,120 | $36,120”
  - off_campus_not_with_family:Fees: 600 ⟵ “Fees | $600 | $600 | $600”
  - off_campus_not_with_family:Food and Housing: 14290 ⟵ “Food and Housing | $17,420 | $14,290 | $5,560”
  - off_campus_not_with_family:Books/Supplies: 960 ⟵ “Books/Supplies | $960 | $960 | $960”
  - off_campus_not_with_family:Personal/Misc.: 2340 ⟵ “Personal/Misc. | $2,340 | $2,340 | $2,340”
  - off_campus_not_with_family:Transportation: 1900 ⟵ “Transportation | $1,900 | $1,900 | $1,900”
  - off_campus_not_with_family:Loan Fees: 162 ⟵ “Loan Fees | $162 | $162 | $162”
  - off_campus_not_with_family:Total Cost of Attendance: 56372 ⟵ “Total Cost of Attendance | $59,502 | $56,372 | $47,642”
  - with_parents_or_family:Tuition: 36120 ⟵ “Tuition | $36,120 | $36,120 | $36,120”
  - with_parents_or_family:Fees: 600 ⟵ “Fees | $600 | $600 | $600”
  - with_parents_or_family:Food and Housing: 5560 ⟵ “Food and Housing | $17,420 | $14,290 | $5,560”
  - with_parents_or_family:Books/Supplies: 960 ⟵ “Books/Supplies | $960 | $960 | $960”
  - with_parents_or_family:Personal/Misc.: 2340 ⟵ “Personal/Misc. | $2,340 | $2,340 | $2,340”
  - with_parents_or_family:Transportation: 1900 ⟵ “Transportation | $1,900 | $1,900 | $1,900”
  - with_parents_or_family:Loan Fees: 162 ⟵ “Loan Fees | $162 | $162 | $162”
  - with_parents_or_family:Total Cost of Attendance: 47642 ⟵ “Total Cost of Attendance | $59,502 | $56,372 | $47,642”
### `5e768efab45e55ae` Flagler College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.flagler.edu/admissions-aid/tuition-and-fees (sha256 ad7a2fc9e934)
- issues: conflicting_sources:https://www.flagler.edu/admissions-aid/tuition-and-fees/cost-details
- checks: {"columns": 3, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition: 36120 ⟵ “Tuition | $36,120 | $36,120 | $36,120”
  - on_campus:Fees: 600 ⟵ “Fees | $600 | $600 | $600”
  - on_campus:Food and Housing: 17420 ⟵ “Food and Housing | $17,420 | $14,290 | $5,560”
  - on_campus:Books/Supplies: 960 ⟵ “Books/Supplies | $960 | $960 | $960”
  - on_campus:Personal/Misc.: 2340 ⟵ “Personal/Misc. | $2,340 | $2,340 | $2,340”
  - on_campus:Transportation: 1900 ⟵ “Transportation | $1,900 | $1,900 | $1,900”
  - on_campus:Loan Fees: 162 ⟵ “Loan Fees | $162 | $162 | $162”
  - on_campus:Total Cost of Attendance (All Costs): 59502 ⟵ “Total Cost of Attendance (All Costs) | $59,502 | $56,372 | $47,642”
  - on_campus:Total Direct Costs: 54140 ⟵ “Total Direct Costs | $54,140 | $51,010 | $42,280”
  - on_campus:Total Indirect Costs: 5362 ⟵ “Total Indirect Costs | $5,362 | $5,362 | $5,362”
  - off_campus_not_with_family:Tuition: 36120 ⟵ “Tuition | $36,120 | $36,120 | $36,120”
  - off_campus_not_with_family:Fees: 600 ⟵ “Fees | $600 | $600 | $600”
  - off_campus_not_with_family:Food and Housing: 14290 ⟵ “Food and Housing | $17,420 | $14,290 | $5,560”
  - off_campus_not_with_family:Books/Supplies: 960 ⟵ “Books/Supplies | $960 | $960 | $960”
  - off_campus_not_with_family:Personal/Misc.: 2340 ⟵ “Personal/Misc. | $2,340 | $2,340 | $2,340”
  - off_campus_not_with_family:Transportation: 1900 ⟵ “Transportation | $1,900 | $1,900 | $1,900”
  - off_campus_not_with_family:Loan Fees: 162 ⟵ “Loan Fees | $162 | $162 | $162”
  - off_campus_not_with_family:Total Cost of Attendance (All Costs): 56372 ⟵ “Total Cost of Attendance (All Costs) | $59,502 | $56,372 | $47,642”
  - off_campus_not_with_family:Total Direct Costs: 51010 ⟵ “Total Direct Costs | $54,140 | $51,010 | $42,280”
  - off_campus_not_with_family:Total Indirect Costs: 5362 ⟵ “Total Indirect Costs | $5,362 | $5,362 | $5,362”
  - with_parents_or_family:Tuition: 36120 ⟵ “Tuition | $36,120 | $36,120 | $36,120”
  - with_parents_or_family:Fees: 600 ⟵ “Fees | $600 | $600 | $600”
  - with_parents_or_family:Food and Housing: 5560 ⟵ “Food and Housing | $17,420 | $14,290 | $5,560”
  - with_parents_or_family:Books/Supplies: 960 ⟵ “Books/Supplies | $960 | $960 | $960”
  - with_parents_or_family:Personal/Misc.: 2340 ⟵ “Personal/Misc. | $2,340 | $2,340 | $2,340”
  - … 5 more rows
### `f17636cc156d4c7b` Flagler College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.flagler.edu/admissions-aid/tuition-and-fees/cost-details (sha256 cb75dc46a8c4)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 32840 ⟵ “Tuition | $32,840 | $32,840 | $32,840”
  - on_campus:Fees: 550 ⟵ “Fees | $550 | $550 | $550”
  - on_campus:Food and Housing: 16470 ⟵ “Food and Housing | $16,470 | $14,200 | $5,560”
  - on_campus:Books/Supplies: 1300 ⟵ “Books/Supplies | $1,300 | $1,300 | $1,300”
  - on_campus:Personal/Misc.: 2320 ⟵ “Personal/Misc. | $2,320 | $2,320 | $2,320”
  - on_campus:Transportation: 1880 ⟵ “Transportation | $1,880 | $1,880 | $1,880”
  - on_campus:Loan Fees: 118 ⟵ “Loan Fees | $118 | $118 | $118”
  - on_campus:Total Cost of Attendance: 55478 ⟵ “Total Cost of Attendance | $55,478 | $53,208 | $44,568”
  - off_campus_not_with_family:Tuition: 32840 ⟵ “Tuition | $32,840 | $32,840 | $32,840”
  - off_campus_not_with_family:Fees: 550 ⟵ “Fees | $550 | $550 | $550”
  - off_campus_not_with_family:Food and Housing: 14200 ⟵ “Food and Housing | $16,470 | $14,200 | $5,560”
  - off_campus_not_with_family:Books/Supplies: 1300 ⟵ “Books/Supplies | $1,300 | $1,300 | $1,300”
  - off_campus_not_with_family:Personal/Misc.: 2320 ⟵ “Personal/Misc. | $2,320 | $2,320 | $2,320”
  - off_campus_not_with_family:Transportation: 1880 ⟵ “Transportation | $1,880 | $1,880 | $1,880”
  - off_campus_not_with_family:Loan Fees: 118 ⟵ “Loan Fees | $118 | $118 | $118”
  - off_campus_not_with_family:Total Cost of Attendance: 53208 ⟵ “Total Cost of Attendance | $55,478 | $53,208 | $44,568”
  - with_parents_or_family:Tuition: 32840 ⟵ “Tuition | $32,840 | $32,840 | $32,840”
  - with_parents_or_family:Fees: 550 ⟵ “Fees | $550 | $550 | $550”
  - with_parents_or_family:Food and Housing: 5560 ⟵ “Food and Housing | $16,470 | $14,200 | $5,560”
  - with_parents_or_family:Books/Supplies: 1300 ⟵ “Books/Supplies | $1,300 | $1,300 | $1,300”
  - with_parents_or_family:Personal/Misc.: 2320 ⟵ “Personal/Misc. | $2,320 | $2,320 | $2,320”
  - with_parents_or_family:Transportation: 1880 ⟵ “Transportation | $1,880 | $1,880 | $1,880”
  - with_parents_or_family:Loan Fees: 118 ⟵ “Loan Fees | $118 | $118 | $118”
  - with_parents_or_family:Total Cost of Attendance: 44568 ⟵ “Total Cost of Attendance | $55,478 | $53,208 | $44,568”
### `a11da63154c58f46` Flagler College — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.flagler.edu/admissions-aid/florida-transfer-students-flagler-college (sha256 735efd99b1f6)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “If you received a grade of “C” or better, your credits will generally transfer.”
### `m837e45daa0b0636` Flagler College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.flagler.edu/sites/default/files/t4/media/documents/admissions-amp-aid/Transfer-Transient.pdf (sha256 4c3a425ef638)
- issues: conflicting_sources:residency_requirement_credits
- checks: {"fields": ["min_grade", "residency_requirement_credits"], "merged_pages": 3}
  - min_grade: C ⟵ “If you received a grade of “C” or better, your credits will generally transfer.”
  - min_grade: C ⟵ “Transfer credits will generally be granted for courses in which a grade of “C” or better was earned from regionally accredited institutions.”
  - residency_requirement_credits: 30 ⟵ “Seniors must complete their final 30 semester hours of credit at Flagler College, except for those students participating in a Study Abroad or Study Away Program.”
  - residency_requirement_credits: 45 ⟵ “Applicants who transfer from senior institutions must complete the last 45 semester hours at Flagler, not including departmentally-required internships.”
### `054a85c7b78e2394` Florida Agricultural and Mechanical University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.famu.edu/students/office-of-financial-aid/forms/pdf/2026-2027%20SAP%20Academic%20Form.pdf (sha256 edf477e35ce2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “DIVISION OF STUDENT AFFAIRS OFFICE OF FINANCIAL AID TELEPHONE: (850) 599-3730 FAX: (850) 561-2730 EMAIL: financialaiddocs@famu.edu Satisfactory Academic Progress (SAP) Appeal Form Please complete all steps outlined on this form to appeal your financial aid ineligibility.”
  - sentence: sap_appeal ⟵ “SAP Appeals Committee Only: Academic Plan Approved Academic Plan Denied Date Notes/Comments: Revised August 18, 2026”
### `2b9bc5467f8f3004` Florida Agricultural and Mechanical University — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.famu.edu/students/office-of-financial-aid/forms/pdf/SAP%20Procedures%20Final%20Website%202023-2024.pdf (sha256 2a27fd209b22)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “If students are cited for not maintaining SAP, they may appeal to receive financial aid for the subsequent semester.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee may reevaluate the timeframe limit if there are program changes.”
  - sentence: sap_appeal ⟵ “APPEAL OF FINANCIAL AID SUSPENSION Students who fail to meet the Satisfactory Academic Progress standards may appeal the suspension of their student financial assistance funds to the Satisfactory Academic Progress Appeals Committee.”
  - sentence: sap_appeal ⟵ “Students who cannot meet the above requirements for an appeal must reestablish Satisfactory Academic Progress through Reinstatement before regaining eligibility for assistance.”
  - sentence: sap_appeal ⟵ “SAP APPEAL LIMITS The Satisfactory Academic Progress Appeals Committee may grant or deny any SAP appeal.”
  - sentence: sap_appeal ⟵ “DEADLINES FOR SAP APPEALS Semester Deadline Date Summer Semester June 5 Fall Semester July 1 Rev. 06/21 FAMU IS AN EQUAL OPPORTUNITY/EQUAL ACCESS UNIVERSITY Spring Semester December 17 REESTABLISHING ELIGIBILITY FOR FEDERAL STUDENT AID REINSTATEMENT OF ACADEMIC STANDARDS Any student whose eligibility for financial aid consideration has been terminated due to unsatisfactory academic progress may re”
### `521f40195d3ae78e` Florida Agricultural and Mechanical University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.famu.edu/students/office-of-financial-aid/forms/index.php (sha256 fa2fccecd5ee)
- issues: semantic_review_required, conflicting_sources:https://www.famu.edu/students/office-of-financial-aid/forms/pdf/2026-2027%20Special%20Circumstance%20-%20Accessible.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Home Students Scholarships Commencement New Student Orientation International Education & Development Rattler Pack Digital Rattler Initiative rattlerverse Office of Financial Aid APPLY FOR AID FAFSA Special Circumstances Unusual Circumstances MAINTAIN YOUR AID Important Dates Student Academic Progress Financial Literacy Financial Aid Representatives TYPES OF AID Scholarships Grants Loans COST OF A”
### `52418985c783705b` Florida Agricultural and Mechanical University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.famu.edu/students/office-of-financial-aid/forms/pdf/2026-2027%20Special%20Circumstance%20-%20Accessible.pdf (sha256 72cfd7a47224)
- issues: semantic_review_required, conflicting_sources:https://www.famu.edu/students/office-of-financial-aid/forms/index.php
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Each request for a special circumstance review is evaluated on an individual basis.”
  - sentence: need_based_special_circumstances ⟵ “The number of special circumstance requests by this office may possibly cause a delay in reviewing your application.”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special circumstance review application does not guarantee additional funding. 2.”
  - sentence: need_based_special_circumstances ⟵ “Therefore, only the portion of expenses which exceed 11% will be considered an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “FAMU IS AN EQUAL OPPORTUNITY/EQUAL ACCESS UNIVERSITY CERTIFICATION STATEMENT: Although your Special Circumstances may be approved, it may not warrant additional aid due to availability of funds.”
  - sentence: need_based_special_circumstances ⟵ “If additional changes occur during the 2026-2027 academic year that would alter the information provided on this Special Circumstance Form, we will immediately contact the Financial Aid Office.”
### `438f86ebf748f770` Florida Agricultural and Mechanical University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/cost-of-attendance-undergrad.php (sha256 159a1841599c)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/cost-of-attendance-distance-learner.php
- checks: {"columns": 2, "components_reconcile": true, "rows": 10}
  - column:Tuition: 17885.4 ⟵ “Tuition | $5,697.30 | $5,697.30 | $17,885.40 | $17,585.40”
  - column:Required Fees: 140.0 ⟵ “Required Fees | $140.00 | $140.00 | $140.00 | $140.00”
  - column:Housing: 7680.0 ⟵ “Housing | $7,680.00 | $7,212.00 | $7,680.00 | $7,212.00”
  - column:Food: 3382.0 ⟵ “Food | $3,382.00 | $5,940.00 | $3,382.00 | $5,116.00”
  - column:Books/Supplies: 1138.0 ⟵ “Books/Supplies | $1,138.00 | $1,138.00 | $1,138.00 | $1,138.00”
  - column:Personal: 3914.0 ⟵ “Personal | $3,914.00 | $2,416.00 | $3,914.00 | $2,416.00”
  - column:Loan Fees: 52.0 ⟵ “Loan Fees | $52.00 | $52.00 | $52.00 | $52.00”
  - column:Health Insurance: 1880.0 ⟵ “Health Insurance | $1,880.00 | $1,880.00 | $1,880.00 | $1,880.00”
  - column:Transportation: 2038.0 ⟵ “Transportation | $2,038.00 | $1,446.00 | $2,038.00 | $1,446.00”
  - column:Fall/Spring Total Cost: 38109.4 ⟵ “Fall/Spring Total Cost | $25,921.30 | $25,921.30 | $38,109.40 | $36,985.40”
  - column:Tuition: 17585.4 ⟵ “Tuition | $5,697.30 | $5,697.30 | $17,885.40 | $17,585.40”
  - column:Required Fees: 140.0 ⟵ “Required Fees | $140.00 | $140.00 | $140.00 | $140.00”
  - column:Housing: 7212.0 ⟵ “Housing | $7,680.00 | $7,212.00 | $7,680.00 | $7,212.00”
  - column:Food: 5116.0 ⟵ “Food | $3,382.00 | $5,940.00 | $3,382.00 | $5,116.00”
  - column:Books/Supplies: 1138.0 ⟵ “Books/Supplies | $1,138.00 | $1,138.00 | $1,138.00 | $1,138.00”
  - column:Personal: 2416.0 ⟵ “Personal | $3,914.00 | $2,416.00 | $3,914.00 | $2,416.00”
  - column:Loan Fees: 52.0 ⟵ “Loan Fees | $52.00 | $52.00 | $52.00 | $52.00”
  - column:Health Insurance: 1880.0 ⟵ “Health Insurance | $1,880.00 | $1,880.00 | $1,880.00 | $1,880.00”
  - column:Transportation: 1446.0 ⟵ “Transportation | $2,038.00 | $1,446.00 | $2,038.00 | $1,446.00”
  - column:Fall/Spring Total Cost: 36985.4 ⟵ “Fall/Spring Total Cost | $25,921.30 | $25,921.30 | $38,109.40 | $36,985.40”
### `61e9cc430ad62da4` Florida Agricultural and Mechanical University — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/index.php (sha256 906d24f35794)
- issues: conflicting_sources:https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/cost-of-attendance-undergrad.php
- checks: {"columns": 2, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition: 19291.2 ⟵ “Tuition | $9,645.60 | $9,645.60 | $19,291.20 | $5,144.32”
  - on_campus:Required Fees: 140.0 ⟵ “Required Fees | $70.00 | $70.00 | $140.00 | $33.00”
  - on_campus:Housing: 8844.0 ⟵ “Housing | $4,422.00 | $4,422.00 | $8,844.00 | $2,761.00”
  - on_campus:Food: 5940.0 ⟵ “Food | $2,970.00 | $2,970.00 | $5,940.00 | $1,705.00”
  - on_campus:Books/Supplies: 1138.0 ⟵ “Books/Supplies | $569.00 | $569.00 | $1,138.00 | $379.00”
  - on_campus:Personal: 2416.0 ⟵ “Personal | $1,208.00 | $1,208.00 | $2,416.00 | $805.00”
  - on_campus:Loan Fees: 52.0 ⟵ “Loan Fees | $26.00 | $26.00 | $52.00 | $26.00”
  - on_campus:Health Insurance: 1880.0 ⟵ “Health Insurance | $940.00 | $940.00 | $1,880.00 | $626.00”
  - on_campus:Transportation: 1446.0 ⟵ “Transportation | $723.00 | $723.00 | $1,446.00 | $482.00”
  - on_campus:Total Cost: 41147.2 ⟵ “Total Cost | $20,573.60 | $20,573.60 | $41,147.20 | $11,961.32”
  - on_campus:Tuition: 5144.32 ⟵ “Tuition | $9,645.60 | $9,645.60 | $19,291.20 | $5,144.32”
  - on_campus:Required Fees: 33.0 ⟵ “Required Fees | $70.00 | $70.00 | $140.00 | $33.00”
  - on_campus:Housing: 2761.0 ⟵ “Housing | $4,422.00 | $4,422.00 | $8,844.00 | $2,761.00”
  - on_campus:Food: 1705.0 ⟵ “Food | $2,970.00 | $2,970.00 | $5,940.00 | $1,705.00”
  - on_campus:Books/Supplies: 379.0 ⟵ “Books/Supplies | $569.00 | $569.00 | $1,138.00 | $379.00”
  - on_campus:Personal: 805.0 ⟵ “Personal | $1,208.00 | $1,208.00 | $2,416.00 | $805.00”
  - on_campus:Loan Fees: 26.0 ⟵ “Loan Fees | $26.00 | $26.00 | $52.00 | $26.00”
  - on_campus:Health Insurance: 626.0 ⟵ “Health Insurance | $940.00 | $940.00 | $1,880.00 | $626.00”
  - on_campus:Transportation: 482.0 ⟵ “Transportation | $723.00 | $723.00 | $1,446.00 | $482.00”
  - on_campus:Total Cost: 11961.32 ⟵ “Total Cost | $20,573.60 | $20,573.60 | $41,147.20 | $11,961.32”
### `72df5a4dbd8494ab` Florida Agricultural and Mechanical University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/index.php (sha256 906d24f35794)
- issues: conflicting_sources:https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/cost-of-attendance-undergrad.php
- checks: {"columns": 2, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition: 5697.3 ⟵ “Tuition | $2,848.65 | $2,848.65 | $5,697.30 | $1,519.00”
  - on_campus:Required Fees: 140.0 ⟵ “Required Fees | $70.00 | $70.00 | $140.00 | $33.00”
  - on_campus:Housing: 8844.0 ⟵ “Housing | $4,422.00 | $4,422.00 | $8,844.00 | $2,761.00”
  - on_campus:Food: 5940.0 ⟵ “Food | $2,970.00 | $2,970.00 | $5,940.00 | $1,705.00”
  - on_campus:Books/Supplies: 1138.0 ⟵ “Books/Supplies | $569.00 | $569.00 | $1,138.00 | $379.00”
  - on_campus:Personal: 2416.0 ⟵ “Personal | $1,208.00 | $1,208.00 | $2,416.00 | $805.00”
  - on_campus:Loan Fees: 52.0 ⟵ “Loan Fees | $26.00 | $26.00 | $52.00 | $26.00”
  - on_campus:Health Insurance: 1880.0 ⟵ “Health Insurance | $940.00 | $940.00 | $1,880.00 | $626.00”
  - on_campus:Transportation: 1446.0 ⟵ “Transportation | $723.00 | $723.00 | $1,446.00 | $482.00”
  - on_campus:Total Cost: 27553.3 ⟵ “Total Cost | $13,776.65 | $13,776.65 | $27,553.30 | $8,336.00”
  - on_campus:Tuition: 1519.0 ⟵ “Tuition | $2,848.65 | $2,848.65 | $5,697.30 | $1,519.00”
  - on_campus:Required Fees: 33.0 ⟵ “Required Fees | $70.00 | $70.00 | $140.00 | $33.00”
  - on_campus:Housing: 2761.0 ⟵ “Housing | $4,422.00 | $4,422.00 | $8,844.00 | $2,761.00”
  - on_campus:Food: 1705.0 ⟵ “Food | $2,970.00 | $2,970.00 | $5,940.00 | $1,705.00”
  - on_campus:Books/Supplies: 379.0 ⟵ “Books/Supplies | $569.00 | $569.00 | $1,138.00 | $379.00”
  - on_campus:Personal: 805.0 ⟵ “Personal | $1,208.00 | $1,208.00 | $2,416.00 | $805.00”
  - on_campus:Loan Fees: 26.0 ⟵ “Loan Fees | $26.00 | $26.00 | $52.00 | $26.00”
  - on_campus:Health Insurance: 626.0 ⟵ “Health Insurance | $940.00 | $940.00 | $1,880.00 | $626.00”
  - on_campus:Transportation: 482.0 ⟵ “Transportation | $723.00 | $723.00 | $1,446.00 | $482.00”
  - on_campus:Total Cost: 8336.0 ⟵ “Total Cost | $13,776.65 | $13,776.65 | $27,553.30 | $8,336.00”
### `a6cbc12f725fbb9e` Florida Agricultural and Mechanical University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/cost-of-attendance-distance-learner.php (sha256 eaeee7cf7e61)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/cost-of-attendance-undergrad.php
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - column:*Tuition & Fees: 6588.0 ⟵ “*Tuition & Fees | $6,588.00 | $6,588.00 | $13,176.00 | $4,392.00”
  - column:Housing: 4216.0 ⟵ “Housing | $4,216.00 | $4,216.00 | $ 8,432.00 | $2,527.00”
  - column:Food: 1293.0 ⟵ “Food | $1,293.00 | $1,293.00 | $ 2,586.00 | $1,180.00”
  - column:Books/Supplies: 569.0 ⟵ “Books/Supplies | $569.00 | $569.00 | $ 1,138.00 | $369.00”
  - column:Loan Fees: 149.0 ⟵ “Loan Fees | $149.00 | $149.00 | $ 298.00 | $66.00”
  - column:Total: 12815.0 ⟵ “Total | $12,815.00 | $12,815.00 | $25,630.00 | $8,534.00”
  - column:*Tuition & Fees: 6588.0 ⟵ “*Tuition & Fees | $6,588.00 | $6,588.00 | $13,176.00 | $4,392.00”
  - column:Housing: 4216.0 ⟵ “Housing | $4,216.00 | $4,216.00 | $ 8,432.00 | $2,527.00”
  - column:Food: 1293.0 ⟵ “Food | $1,293.00 | $1,293.00 | $ 2,586.00 | $1,180.00”
  - column:Books/Supplies: 569.0 ⟵ “Books/Supplies | $569.00 | $569.00 | $ 1,138.00 | $369.00”
  - column:Loan Fees: 149.0 ⟵ “Loan Fees | $149.00 | $149.00 | $ 298.00 | $66.00”
  - column:Total: 12815.0 ⟵ “Total | $12,815.00 | $12,815.00 | $25,630.00 | $8,534.00”
  - column:*Tuition & Fees: 13176.0 ⟵ “*Tuition & Fees | $6,588.00 | $6,588.00 | $13,176.00 | $4,392.00”
  - column:Housing: 8432.0 ⟵ “Housing | $4,216.00 | $4,216.00 | $ 8,432.00 | $2,527.00”
  - column:Food: 2586.0 ⟵ “Food | $1,293.00 | $1,293.00 | $ 2,586.00 | $1,180.00”
  - column:Books/Supplies: 1138.0 ⟵ “Books/Supplies | $569.00 | $569.00 | $ 1,138.00 | $369.00”
  - column:Loan Fees: 298.0 ⟵ “Loan Fees | $149.00 | $149.00 | $ 298.00 | $66.00”
  - column:Total: 25630.0 ⟵ “Total | $12,815.00 | $12,815.00 | $25,630.00 | $8,534.00”
  - column:*Tuition & Fees: 4392.0 ⟵ “*Tuition & Fees | $6,588.00 | $6,588.00 | $13,176.00 | $4,392.00”
  - column:Housing: 2527.0 ⟵ “Housing | $4,216.00 | $4,216.00 | $ 8,432.00 | $2,527.00”
  - column:Food: 1180.0 ⟵ “Food | $1,293.00 | $1,293.00 | $ 2,586.00 | $1,180.00”
  - column:Books/Supplies: 369.0 ⟵ “Books/Supplies | $569.00 | $569.00 | $ 1,138.00 | $369.00”
  - column:Loan Fees: 66.0 ⟵ “Loan Fees | $149.00 | $149.00 | $ 298.00 | $66.00”
  - column:Total: 8534.0 ⟵ “Total | $12,815.00 | $12,815.00 | $25,630.00 | $8,534.00”
### `bd4961927117af77` Florida Agricultural and Mechanical University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/cost-of-attendance-undergrad.php (sha256 159a1841599c)
- issues: conflicting_sources:https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/index.php
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Tuition: 5697.3 ⟵ “Tuition | $5,697.30 | $5,697.30 | $17,885.40 | $17,585.40”
  - column:Required Fees: 140.0 ⟵ “Required Fees | $140.00 | $140.00 | $140.00 | $140.00”
  - column:Housing: 7680.0 ⟵ “Housing | $7,680.00 | $7,212.00 | $7,680.00 | $7,212.00”
  - column:Food: 3382.0 ⟵ “Food | $3,382.00 | $5,940.00 | $3,382.00 | $5,116.00”
  - column:Books/Supplies: 1138.0 ⟵ “Books/Supplies | $1,138.00 | $1,138.00 | $1,138.00 | $1,138.00”
  - column:Personal: 3914.0 ⟵ “Personal | $3,914.00 | $2,416.00 | $3,914.00 | $2,416.00”
  - column:Loan Fees: 52.0 ⟵ “Loan Fees | $52.00 | $52.00 | $52.00 | $52.00”
  - column:Health Insurance: 1880.0 ⟵ “Health Insurance | $1,880.00 | $1,880.00 | $1,880.00 | $1,880.00”
  - column:Transportation: 2038.0 ⟵ “Transportation | $2,038.00 | $1,446.00 | $2,038.00 | $1,446.00”
  - column:Fall/Spring Total Cost: 25921.3 ⟵ “Fall/Spring Total Cost | $25,921.30 | $25,921.30 | $38,109.40 | $36,985.40”
### `fa89dff7b23b9eed` Florida Agricultural and Mechanical University — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/cost-of-attendance-undergrad.php (sha256 159a1841599c)
- issues: conflicting_sources:https://www.famu.edu/students/office-of-financial-aid/cost-of-attendance/index.php
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Tuition: 5697.3 ⟵ “Tuition | $5,697.30 | $5,697.30 | $17,885.40 | $17,585.40”
  - column:Required Fees: 140.0 ⟵ “Required Fees | $140.00 | $140.00 | $140.00 | $140.00”
  - column:Housing: 7212.0 ⟵ “Housing | $7,680.00 | $7,212.00 | $7,680.00 | $7,212.00”
  - column:Food: 5940.0 ⟵ “Food | $3,382.00 | $5,940.00 | $3,382.00 | $5,116.00”
  - column:Books/Supplies: 1138.0 ⟵ “Books/Supplies | $1,138.00 | $1,138.00 | $1,138.00 | $1,138.00”
  - column:Personal: 2416.0 ⟵ “Personal | $3,914.00 | $2,416.00 | $3,914.00 | $2,416.00”
  - column:Loan Fees: 52.0 ⟵ “Loan Fees | $52.00 | $52.00 | $52.00 | $52.00”
  - column:Health Insurance: 1880.0 ⟵ “Health Insurance | $1,880.00 | $1,880.00 | $1,880.00 | $1,880.00”
  - column:Transportation: 1446.0 ⟵ “Transportation | $2,038.00 | $1,446.00 | $2,038.00 | $1,446.00”
  - column:Fall/Spring Total Cost: 25921.3 ⟵ “Fall/Spring Total Cost | $25,921.30 | $25,921.30 | $38,109.40 | $36,985.40”
### `6cd999731d47d083` Florida Atlantic University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fau.edu/finaid/resources/policies/ (sha256 b295a682d44e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 19}
  - sentence: sap_appeal ⟵ “If eligibility is terminated, the student may apply for reinstatement on a probationary basis through the Satisfactory Academic Progress Appeal process (see below).”
  - sentence: sap_appeal ⟵ “If eligibility is terminated, the student may apply for reinstatement on a probationary basis through the Satisfactory Academic Progress Appeal process (see below).”
  - sentence: sap_appeal ⟵ “Exceptions made for programs requiring more than 120 credits to complete and cases where the Revised Maximum Timeframe has been extended as a result of the Satisfactory Academic Progress Appeal process.”
  - sentence: sap_appeal ⟵ “Exceptions will be made for specific programs based on published second bachelor program length and cases where the Revised Maximum Timeframe has been extended as a result of the Satisfactory Academic Progress Appeal process.”
  - sentence: sap_appeal ⟵ “Students in violation of the maximum timeframe criteria may petition to have their maximum timeframe extended through the Satisfactory Academic Progress Appeal process (see below).”
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL PROCESS A student whose aid eligibility has been terminated may apply for reinstatement on a probationary basis by submitting a Satisfactory Academic Progress Appeal form to the Office of Student Financial Aid.”
### `ef7fdee2da001375` Florida Atlantic University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fau.edu/finaid/resources/policies/ (sha256 b295a682d44e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you are returning from academic suspension or dismissal, documentation of special circumstances or documented satisfactory academic progress (no failing grades or withdrawals) after being suspended or dismissed is required.”
  - sentence: need_based_special_circumstances ⟵ “If GPA is below 1.0 (Undergraduate) or 2.0 (Graduate) and/or Pace is below 50%, documentation of special circumstances or documented satisfactory academic progress is required (no failing grades or withdrawals).”
### `1d1ad9f0af84aa7e` Florida Atlantic University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fau.edu/finaid/other/cost-of-attendance/20252026/ (sha256 fd957ffe94ac)
- issues: components_do_not_reconcile, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": false, "rows": 9}
  - on_campus:Tuition & Fees: 5976 ⟵ “Tuition & Fees | $5,976*”
  - on_campus:Books, course materials, supplies and equipment: 1288 ⟵ “Books, course materials, supplies and equipment | $1,288”
  - on_campus:Living Expenses - Housing: 11324 ⟵ “Living Expenses - Housing | $11,324*”
  - on_campus:LIVING EXPENSES - FOOD: 5090 ⟵ “LIVING EXPENSES - FOOD | $5,090*”
  - on_campus:TRANSPORTATION: 2390 ⟵ “TRANSPORTATION | $2,390”
  - on_campus:Miscellaneous Personal Expenses: 5020 ⟵ “Miscellaneous Personal Expenses | $5,020”
  - on_campus:Estimated Direct Costs: Payable to FAU and reflected on student's bill (* Items): 22390 ⟵ “Estimated Direct Costs: Payable to FAU and reflected on student's bill (* Items) | $22,390”
  - on_campus:Estimated Indirect Costs:: 8698 ⟵ “Estimated Indirect Costs: | $8,698”
  - on_campus:TOTAL: 31088 ⟵ “TOTAL | $31,088”
### `5c99ff53c1da66b7` Florida Atlantic University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fau.edu/finaid/other/cost-of-attendance/ (sha256 0c42198f5ec1)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 9}
  - on_campus:Tuition & Fees: 5984 ⟵ “Tuition & Fees | $5,984*”
  - on_campus:Books, course materials, supplies and equipment: 1368 ⟵ “Books, course materials, supplies and equipment | $1,368”
  - on_campus:Living Expenses - Housing: 10524 ⟵ “Living Expenses - Housing | $10,524*”
  - on_campus:LIVING EXPENSES - FOOD: 5308 ⟵ “LIVING EXPENSES - FOOD | $5,308*”
  - on_campus:TRANSPORTATION: 3090 ⟵ “TRANSPORTATION | $3,090”
  - on_campus:Miscellaneous Personal Expenses: 4756 ⟵ “Miscellaneous Personal Expenses | $4,756”
  - on_campus:Estimated Direct Costs: Payable to FAU and reflected on student's bill (* Items): 21816 ⟵ “Estimated Direct Costs: Payable to FAU and reflected on student's bill (* Items) | $21,816”
  - on_campus:Estimated Indirect Costs:: 9214 ⟵ “Estimated Indirect Costs: | $9,214”
  - on_campus:TOTAL: 31030 ⟵ “TOTAL | $31,030”
### `d3998014d43b3d51` Florida College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://floridacollege.edu/admissions/financial-aid/costs-and-fees/ (sha256 d06e202c7dba)
- issues: cost_period_semester
- checks: {"columns": 1, "rows": 5}
  - column:Tuition (12-16 hours): 10670.0 ⟵ “Tuition (12-16 hours) | $10,670.00”
  - column:Room (average): 3450.0 ⟵ “Room (average) | $3,450.00”
  - column:Meal Plan (required, subject to sales tax): 2475.0 ⟵ “Meal Plan (required, subject to sales tax) | $2,475.00”
  - column:Activity, Technology, and Security Fees: 675.0 ⟵ “Activity, Technology, and Security Fees | $675.00”
  - column:Resident Student Total: 17270.0 ⟵ “Resident Student Total | $17,270.00”
### `1eef89bf0d833bb5` Florida Gateway College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fgc.edu/tuition-financial-aid/documents/06-11-25%20Revised%20SAP%20Appeal%20Packet.pdf (sha256 09d8c9cf3216)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Instructions for Satisfactory Academic Progress Appeal Federal Regulations require institutions to establish a Satisfactory Academic Progress (SAP) policy to monitor a student’s academic progress toward the completion of their program.”
  - sentence: sap_appeal ⟵ “How to Complete a Satisfactory Academic Progress Appeal (SAP): Step 1: Contact your academic advisor or program advisor to create an Academic Plan Worksheet.”
  - sentence: sap_appeal ⟵ “Please do not submit this page with your appeal form. revised 02/2024 Satisfactory Academic Progress (SAP) Appeal Please select the area(s) of SAP you are not meeting: GPA Below 2.0 67% 150% Student’s Name: Last First MI Student ID: Phone: ( ) Area Code Please refer to the instruction page for detailed information on how to complete this form.”
  - sentence: sap_appeal ⟵ “Please note: SAP Appeal due dates: January 20th, March 20th, June 20th, September 20th, and November 20th.”
  - sentence: sap_appeal ⟵ “If my SAP Appeal is approved, I understand if I do not follow the conditions of the SAP Appeal and be meeting SAP by the projected date above, this will result in the loss of my Financial Aid eligibility.”
  - sentence: sap_appeal ⟵ “I understand that receiving an "D", "F", "W" ,"I GRADE" or changing a program plan, does not follow the conditions of the SAP Appeal, which will result in the loss of my Financial Aid eligibility.”
### `1cab8ddf595e078f` Florida Gulf Coast University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/formsandresources/change_in_circumstances (sha256 87088345cf5b)
- issues: semantic_review_required, conflicting_sources:https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/eligibility/termsandconditions/satisfactoryacademicprogress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Requesting a Change in Circumstances Appeal To process a request for review, the student must: Have the current academic year's FAFSA on file Be accepted for Admission and/or a continuing degree seeking student Complete the Verification process (if selected) Be meeting Satisfactory Academic Progress Standards The Change in Circumstances Appeal will be submitted electronically and requires formal d”
### `234bbce498725161` Florida Gulf Coast University — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/formsandresources/faqs (sha256 6f49ebaebb9d)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Toggle More Info If you have no contact with your parents and don't know where they live, or you've left home due to an abusive situation, select “Yes” to the “Do unusual circumstances prevent the student from contacting their parents or would contacting their parents pose a risk to the student?” question on the FAFSA form.”
  - sentence: need_based_special_circumstances ⟵ “Scholarship checks should be made payable to "Florida Gulf Coast University" and sent to: Florida Gulf Coast University Office of Financial Aid & Scholarships 10501 FGCU Blvd S Fort Myers, FL 33965 Back to top Special Circumstances/Unique Situations My financial situation has changed since filing the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Change in Circumstances What should I do if I have a special circumstance?”
### `7e8ced7da6e6132c` Florida Gulf Coast University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/formsandresources/change_in_circumstances (sha256 87088345cf5b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Possible Outcomes: No change Reduced SAI but no change in financial aid offer Reduced SAI and adjustments made to federal loans Reduced SAI and adjustments made to gift/grant aid Please note that submitting an appeal does not guarantee that you will be eligible to receive additional financial aid.”
  - sentence: need_based_special_circumstances ⟵ “Please contact us to discuss the special circumstances process or any other financial aid questions you may have.”
### `9392304115ccefc0` Florida Gulf Coast University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/eligibility/termsandconditions/satisfactoryacademicprogress (sha256 ab17fbc26c36)
- issues: semantic_review_required, conflicting_sources:https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/formsandresources/change_in_circumstances
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “To access a Fall, Spring, or Summer Satisfactory Academic Progress Appeal form, follow the steps below: Login to Gulfline Click the top left four square Click Gulfline Click Financial Aid Click Financial Aid Online Forms Note: Financial Aid for the current academic term will be awarded at the time of reinstatement providing funds are still available.”
  - sentence: sap_appeal ⟵ “Students will remain on suspension until meeting SAP or may appeal again after completing one semester on their own, as long as they have achieved SAP standards during that semester.”
### `c6e4747c1364fb65` Florida Gulf Coast University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/formsandresources/change_in_circumstances (sha256 87088345cf5b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “FGCU makes every effort to work with students and families to discuss and evaluate changes in a family’s financial circumstances through the Professional Judgement process.”
### `e3175ce417a6ad4b` Florida Gulf Coast University — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/formsandresources/faqs (sha256 6f49ebaebb9d)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Back to top What is the SAP appeal process?”
  - sentence: sap_appeal ⟵ “Log in to your Gulfline Student Portal Select the Financial Aid Tab Select Online Forms Complete and submit the Satisfactory Academic Progress Appeal form Back to top My appeal was approved; what is financial aid probation?”
  - sentence: sap_appeal ⟵ “Students will remain on suspension until meeting SAP or may appeal again after completing one semester on their own, if they have achieved SAP standards during that semester.”
### `318eec812e89ec52` Florida Gulf Coast University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.fgcu.edu/admissionsandaid/undergraduateadmissions/scholarshipsandwaivers (sha256 c5d4b18be92f)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $3,000 per year up to three years ⟵ “Accelerated Collegiate Experience (ACE) Graduates | $3,000 per year up to three years | Successful completion of the ACE Honors program with an FGCU GPA of 3.0; Must be recommended by ACE Program Director.”
  - eligibility_summary: Successful completion of the ACE Honors program with an FGCU GPA of 3.0; Must be recommended by ACE Program Director. ⟵ “Accelerated Collegiate Experience (ACE) Graduates | $3,000 per year up to three years | Successful completion of the ACE Honors program with an FGCU GPA of 3.0; Must be recommended by ACE Program Director.”
### `496f2f20e514346c` Florida Gulf Coast University — awards 2022-23 [new] (labeled_in_source)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/typesofaid/brightfutures (sha256 2e8b20055548)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - award_amount_text: 2.75 ⟵ “3.0* | 2.75 | Minimum Cumulative GPA(unrounded & unweighted)”
  - eligibility_summary: Minimum Cumulative GPA(unrounded & unweighted) ⟵ “3.0* | 2.75 | Minimum Cumulative GPA(unrounded & unweighted)”
### `74149f108e450edb` Florida Gulf Coast University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.fgcu.edu/admissionsandaid/undergraduateadmissions/scholarshipsandwaivers (sha256 c5d4b18be92f)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $3,000 per year up to three years ⟵ “Eagle Collegiate School | $3,000 per year up to three years | Florida Southwestern Collegiate School or State College of Florida Collegiate School graduate with an AA degree and 3.0 GPA.”
  - eligibility_summary: Florida Southwestern Collegiate School or State College of Florida Collegiate School graduate with an AA degree and 3.0 GPA. ⟵ “Eagle Collegiate School | $3,000 per year up to three years | Florida Southwestern Collegiate School or State College of Florida Collegiate School graduate with an AA degree and 3.0 GPA.”
### `7a47af1e47c2b298` Florida Gulf Coast University — awards 2022-23 [new] (labeled_in_source)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/typesofaid/brightfutures (sha256 2e8b20055548)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - award_amount_text: 12 semester(earned hours) ⟵ “12 semester(earned hours) | 12 semester(earned hours) | Minimum Hours Required Per Term if funded Full Time (12+ hours)”
  - eligibility_summary: Minimum Hours Required Per Term if funded Full Time (12+ hours) ⟵ “12 semester(earned hours) | 12 semester(earned hours) | Minimum Hours Required Per Term if funded Full Time (12+ hours)”
### `8db43eff6e1e552a` Florida Gulf Coast University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.fgcu.edu/admissionsandaid/undergraduateadmissions/scholarshipsandwaivers (sha256 c5d4b18be92f)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1,000 per year, up to 2 years; Fall and Spring semesters only ⟵ “Eagle Transfer(Details below) | $1,000 per year, up to 2 years; Fall and Spring semesters only | 3.0 GPA or higher; AA or AS Degree from a Florida college Competitive award based on selection criteria and financial need”
  - eligibility_summary: 3.0 GPA or higher; AA or AS Degree from a Florida college Competitive award based on selection criteria and financial need ⟵ “Eagle Transfer(Details below) | $1,000 per year, up to 2 years; Fall and Spring semesters only | 3.0 GPA or higher; AA or AS Degree from a Florida college Competitive award based on selection criteria and financial need”
### `bd1323f49100e25c` Florida Gulf Coast University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.fgcu.edu/admissionsandaid/undergraduateadmissions/scholarshipsandwaivers (sha256 c5d4b18be92f)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $3,000 per year, up to 2 years; Fall and Spring semesters only ⟵ “Eagle Transfer Gold | $3,000 per year, up to 2 years; Fall and Spring semesters only | 3.5 GPA or higher; AA Degree from a Florida college Must submit an FGCU application by posted deadline for automatic consideration”
  - eligibility_summary: 3.5 GPA or higher; AA Degree from a Florida college Must submit an FGCU application by posted deadline for automatic consideration ⟵ “Eagle Transfer Gold | $3,000 per year, up to 2 years; Fall and Spring semesters only | 3.5 GPA or higher; AA Degree from a Florida college Must submit an FGCU application by posted deadline for automatic consideration”
### `d47fae8cc678e09b` Florida Gulf Coast University — awards 2022-23 [new] (labeled_in_source)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/typesofaid/brightfutures (sha256 2e8b20055548)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - award_amount_text: 9 semester(earned hours) ⟵ “9 semester(earned hours) | 9 semester(earned hours) | Minimum Hours Required Per Termif funded Three-quarter Time (9-11 hours)”
  - eligibility_summary: Minimum Hours Required Per Termif funded Three-quarter Time (9-11 hours) ⟵ “9 semester(earned hours) | 9 semester(earned hours) | Minimum Hours Required Per Termif funded Three-quarter Time (9-11 hours)”
### `dd222fcbd9df3d75` Florida Gulf Coast University — awards 2022-23 [new] (labeled_in_source)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/typesofaid/brightfutures (sha256 2e8b20055548)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - award_amount_text: 6 semester(earned hours) ⟵ “6 semester(earned hours) | 6 semester(earned hours) | Minimum Hours Required Per Term, if funded Half Time (6-8 hours)”
  - eligibility_summary: Minimum Hours Required Per Term, if funded Half Time (6-8 hours) ⟵ “6 semester(earned hours) | 6 semester(earned hours) | Minimum Hours Required Per Term, if funded Half Time (6-8 hours)”
### `facfe9273f2aad08` Florida Gulf Coast University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.fgcu.edu/admissionsandaid/undergraduateadmissions/scholarshipsandwaivers (sha256 c5d4b18be92f)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $5,000 per year up to three years ⟵ “Accelerated Collegiate Experience (ACE) Honors Graduates | $5,000 per year up to three years | Successful completion of the ACE Honors program with an FGCU GPA of 3.0; Students may also be considered if they have a 1320 rSAT or 28 ACT or 88 CLT at time of initial enrollment; Must be recommended by A”
  - eligibility_summary: Successful completion of the ACE Honors program with an FGCU GPA of 3.0; Students may also be considered if they have a 1320 rSAT or 28 ACT or 88 CLT at time of initial enrollment; Must be recommended by ACE Program Director. ⟵ “Accelerated Collegiate Experience (ACE) Honors Graduates | $5,000 per year up to three years | Successful completion of the ACE Honors program with an FGCU GPA of 3.0; Students may also be considered if they have a 1320 rSAT or 28 ACT or 88 CLT at time of initial enrollment; Must be recommended by A”
### `128f187e02c41136` Florida Gulf Coast University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/cost/costofattendance (sha256 667ad3572955)
- issues: ambiguous_year_labels
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 6118 ⟵ “Tuition and Fees | $ 6,118 | $ 6,118 | $ 6,118”
  - with_parents_or_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $ 1,200 | $ 1,200 | $ 1,200”
  - with_parents_or_family:Food and Housing: 5075 ⟵ “Food and Housing | $ 5,075 | $ 12,320 | $ 14,219”
  - with_parents_or_family:Transportation: 2750 ⟵ “Transportation | $ 2,750 | $ 2,750 | $ 2,750”
  - with_parents_or_family:Personal Expenses: 2750 ⟵ “Personal Expenses | $ 2,750 | $ 2,750 | $ 2,750”
  - with_parents_or_family:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - with_parents_or_family:Estimated Total Cost: 17951 ⟵ “Estimated Total Cost | $ 17,951 | $ 25,196 | $ 27,095”
  - on_campus:Tuition and Fees: 6118 ⟵ “Tuition and Fees | $ 6,118 | $ 6,118 | $ 6,118”
  - on_campus:Books and Supplies: 1200 ⟵ “Books and Supplies | $ 1,200 | $ 1,200 | $ 1,200”
  - on_campus:Food and Housing: 12320 ⟵ “Food and Housing | $ 5,075 | $ 12,320 | $ 14,219”
  - on_campus:Transportation: 2750 ⟵ “Transportation | $ 2,750 | $ 2,750 | $ 2,750”
  - on_campus:Personal Expenses: 2750 ⟵ “Personal Expenses | $ 2,750 | $ 2,750 | $ 2,750”
  - on_campus:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - on_campus:Estimated Total Cost: 25196 ⟵ “Estimated Total Cost | $ 17,951 | $ 25,196 | $ 27,095”
  - off_campus_not_with_family:Tuition and Fees: 6118 ⟵ “Tuition and Fees | $ 6,118 | $ 6,118 | $ 6,118”
  - off_campus_not_with_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $ 1,200 | $ 1,200 | $ 1,200”
  - off_campus_not_with_family:Food and Housing: 14219 ⟵ “Food and Housing | $ 5,075 | $ 12,320 | $ 14,219”
  - off_campus_not_with_family:Transportation: 2750 ⟵ “Transportation | $ 2,750 | $ 2,750 | $ 2,750”
  - off_campus_not_with_family:Personal Expenses: 2750 ⟵ “Personal Expenses | $ 2,750 | $ 2,750 | $ 2,750”
  - off_campus_not_with_family:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - off_campus_not_with_family:Estimated Total Cost: 27095 ⟵ “Estimated Total Cost | $ 17,951 | $ 25,196 | $ 27,095”
### `3cb9242d002028c2` Florida Gulf Coast University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.fgcu.edu/admissionsandaid/financialaid/undergraduate/cost/costofattendance (sha256 667ad3572955)
- issues: ambiguous_year_labels, residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 28019 ⟵ “Tuition and Fees | $ 28,019 | $ 28,019 | $ 28,019”
  - with_parents_or_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $ 1,200 | $ 1,200 | $ 1,200”
  - with_parents_or_family:Food and Housing: 5075 ⟵ “Food and Housing | $ 5,075 | $ 12,320 | $ 14,219”
  - with_parents_or_family:Transportation: 2750 ⟵ “Transportation | $ 2,750 | $ 2,750 | $ 2,750”
  - with_parents_or_family:Personal Expenses: 2750 ⟵ “Personal Expenses | $ 2,750 | $ 2,750 | $ 2,750”
  - with_parents_or_family:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - with_parents_or_family:Estimated Total Cost: 39852 ⟵ “Estimated Total Cost | $ 39,852 | $ 47,097 | $ 48,996”
  - on_campus:Tuition and Fees: 28019 ⟵ “Tuition and Fees | $ 28,019 | $ 28,019 | $ 28,019”
  - on_campus:Books and Supplies: 1200 ⟵ “Books and Supplies | $ 1,200 | $ 1,200 | $ 1,200”
  - on_campus:Food and Housing: 12320 ⟵ “Food and Housing | $ 5,075 | $ 12,320 | $ 14,219”
  - on_campus:Transportation: 2750 ⟵ “Transportation | $ 2,750 | $ 2,750 | $ 2,750”
  - on_campus:Personal Expenses: 2750 ⟵ “Personal Expenses | $ 2,750 | $ 2,750 | $ 2,750”
  - on_campus:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - on_campus:Estimated Total Cost: 47097 ⟵ “Estimated Total Cost | $ 39,852 | $ 47,097 | $ 48,996”
  - off_campus_not_with_family:Tuition and Fees: 28019 ⟵ “Tuition and Fees | $ 28,019 | $ 28,019 | $ 28,019”
  - off_campus_not_with_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $ 1,200 | $ 1,200 | $ 1,200”
  - off_campus_not_with_family:Food and Housing: 14219 ⟵ “Food and Housing | $ 5,075 | $ 12,320 | $ 14,219”
  - off_campus_not_with_family:Transportation: 2750 ⟵ “Transportation | $ 2,750 | $ 2,750 | $ 2,750”
  - off_campus_not_with_family:Personal Expenses: 2750 ⟵ “Personal Expenses | $ 2,750 | $ 2,750 | $ 2,750”
  - off_campus_not_with_family:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - off_campus_not_with_family:Estimated Total Cost: 48996 ⟵ “Estimated Total Cost | $ 39,852 | $ 47,097 | $ 48,996”
### `00d27920212c47d6` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT reichardr@fit.edu ⟵ “ | Reichard, Ronnal | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences , College of Engineering and Science: Department of Aerospace, Physics and Space Sciences |  | reichardr@fit.edu | composite materials, composite structures, composite des”
### `028bdca8b64affcd` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT barker@fit.edu ⟵ “ | Barker, Ballard | Emeritus Faculty | College of Aeronautics |  | barker@fit.edu | ”
### `06fabbba2948d204` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT dwilt@fit.edu ⟵ “ | Wilt, Donna | Emeritus Faculty | College of Aeronautics |  | dwilt@fit.edu | ”
### `083b86d86e963af5` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT chelmste@fit.edu ⟵ “ | Helmstetter, Charles | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | chelmste@fit.edu | ”
### `13b91173a6ebac17` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT babich@fit.edu ⟵ “ | Babich, Michael | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering | Chemistry | babich@fit.edu | ”
### `1408f5721c612f38` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT wallen@fit.edu ⟵ “ | Allen, William | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | wallen@fit.edu | ”
### `17bc6897d15936fa` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT relmore@fit.edu ⟵ “ | Elmore, Richard | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology |  | relmore@fit.edu | ”
### `1b75067e23e7aa6f` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jrokach@fit.edu ⟵ “ | Rokach, Joshua | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering |  | jrokach@fit.edu | ”
### `1d62d041fa5a7c3d` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gmicklow@fit.edu ⟵ “ | Micklow, Gerald | Emeritus Faculty | College of Engineering and Science: Department of Mechanical and Civil Engineering | Mechanical Engineering | gmicklow@fit.edu | ”
### `2539fdde0a9ab9a4` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT eugene@fit.edu ⟵ “ | Dshalalow, Jewgeni | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering |  | eugene@fit.edu | stochastic processes, abstract analysis, random measures, biomathematics, queueing, reliability, stochastic games, stochastic finance, cancer researc”
### `28fc2a481a741ce3` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT kzieg@fit.edu ⟵ “ | Zieg, Kermit | Emeritus Faculty | Nathan M. Bisk College of Business |  | kzieg@fit.edu | ”
### `31d5d4e2f57cdb09` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT ggoldberg@fit.edu ⟵ “ | Goldberg, Gerald F | Emeritus Faculty | Nathan M. Bisk College of Business |  | ggoldberg@fit.edu | ”
### `335bffa0e00d89a7` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT leachb@fit.edu ⟵ “ | Leach, Billy | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | leachb@fit.edu | ”
### `3c78d0f2d5cf0d95` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT ryan@fit.edu ⟵ “ | Stansifer, Ryan | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | ryan@fit.edu | programming languages, formal methods and software development, compilers and static analy”
### `3cdac64b9bedb71c` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mshahsavari@fit.edu ⟵ “ | Shahsavari, Mehdi | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | mshahsavari@fit.edu | ”
### `3d1434e1359bd0e0` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT sullivan@fit.edu ⟵ “ | Sullivan, Robert | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | sullivan@fit.edu | ”
### `46ad3719221ad42f` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT hheck@fit.edu ⟵ “ | Heck, Howell | Emeritus Faculty | College of Engineering and Science: Department of Mechanical and Civil Engineering | Civil Engineering | hheck@fit.edu | ”
### `4b1fbe51dba1f261` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT catanese@fit.edu ⟵ “ | Catanese, Anthony | Emeritus Faculty | Florida Institute of Technology |  | catanese@fit.edu | ”
### `4cd069363ebaaf46` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT whitlow@fit.edu ⟵ “ | Whitlow, Jonathan | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering | Chemical Engineering | whitlow@fit.edu | chemical engineering, process design, renewable energy, process control, process modeling, process simulation”
### `4da3f3f812f27d9f` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT fmh@fit.edu ⟵ “ | Ham, Fredric | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | fmh@fit.edu | ”
### `51158971bd936f99` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT djackson@fit.edu ⟵ “ | Jackson, Dennis | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering | Mathematics | djackson@fit.edu | ”
### `52bd190c51abfc78` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rmarshall1995@my.fit.edu ⟵ “ | Marshall, Ronald L. | Emeritus Faculty | Nathan M. Bisk College of Business |  | rmarshall1995@my.fit.edu | ”
### `52ea2eeb2186b211` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT engblom@fit.edu ⟵ “ | Engblom, John | Emeritus Faculty | College of Engineering and Science | Mechanical Engineering | engblom@fit.edu | ”
### `5bd249e5dace6711` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT adilpare@fit.edu ⟵ “ | Dil Pare, Armand | Emeritus Faculty | College of Engineering and Science: Department of Mechanical and Civil Engineering | Mechanical Engineering | adilpare@fit.edu | ”
### `5e2a70a9b7c03a3c` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT twaite@fit.edu ⟵ “ | Waite, Thomas | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences |  | twaite@fit.edu | ”
### `5ffa0cdf70370469` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT lindeman@fit.edu ⟵ “ | Lindeman, Kenyon | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences |  | lindeman@fit.edu | Coastal management, Coastal fishes and habitats, Spatial planning, Marine protected areas, Systems science, Governance. Institutional sustainabilit”
### `662bd9e948391f6b` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT nchlosta@fit.edu ⟵ “ | Chlosta, Norman | Emeritus Faculty | Nathan M. Bisk College of Business |  | nchlosta@fit.edu | ”
### `68206e2011f40405` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mglicksman@fit.edu ⟵ “ | Glicksman, Martin | Emeritus Faculty | Florida Institute of Technology , College of Engineering and Science: Department of Mechanical and Civil Engineering | Mechanical Engineering | mglicksman@fit.edu | ”
### `68b6ace96f1b3d7d` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT avamosi@fit.edu ⟵ “ | Vamosi, Alexander | Emeritus Faculty | Nathan M. Bisk College of Business |  | avamosi@fit.edu | ”
### `6bbcd4de5ade11e7` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rweigel@fit.edu ⟵ “ | Weigel, Russell | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | rweigel@fit.edu | ”
### `6d2084918df34ff3` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mshaikh@fit.edu ⟵ “ | Shaikh, Muzaffar | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering | Systems Engineering | mshaikh@fit.edu | ”
### `6ecbcbb6cfaec5c2` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gallo@fit.edu ⟵ “ | Gallo, Michael | Emeritus Faculty | College of Aeronautics |  | gallo@fit.edu | ”
### `6fd94a74f9deea5d` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rturner@fit.edu ⟵ “ | Turner, Richard L. | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences | Marine Science | rturner@fit.edu | ”
### `736e1c3e85c1b980` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rotaylor@fit.edu ⟵ “ | Taylor, Robert A. | Emeritus Faculty | College of Psych. and Liberal Arts |  | rotaylor@fit.edu | ”
### `746e290eeea4e783` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT dcarroll@fit.edu ⟵ “ | Carroll, David | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | dcarroll@fit.edu | ”
### `76d7430b15b11366` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT bakerj@fit.edu ⟵ “ | Baker, Juanita | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology | Psychology - Clinical | bakerj@fit.edu | ”
### `7a9f6dd0e634513b` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jolson@fit.edu ⟵ “ | Olson, Joel | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering | Chemistry | jolson@fit.edu | ”
### `7ca6b7b4393ba762` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mcfarlan@fit.edu ⟵ “ | McFarland, Thomas | Emeritus Faculty | Evans Library |  | mcfarlan@fit.edu | ”
### `7f584a8956ba21f1` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT eperez@fit.edu ⟵ “ | Perez, Enrique | Emeritus Faculty | Nathan M. Bisk College of Business |  | eperez@fit.edu | ”
### `80d7f611c034be3e` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT grimwade@fit.edu ⟵ “ | Grimwade, Julia | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | grimwade@fit.edu | ”
### `835ece434b549450` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT clang@fit.edu ⟵ “ | Lang, Celine | Emeritus Faculty | Evans Library , College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | clang@fit.edu | ”
### `894f8089ee8103f3` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT webbe@fit.edu ⟵ “ | Webbe, Frank M. | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology | Psychology - Clinical | webbe@fit.edu | ”
### `89c0b33ec994d8f1` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT strother@fit.edu ⟵ “ | Strother, Judith | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | strother@fit.edu | ”
### `8d2c886907295199` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT apandit@fit.edu ⟵ “ | Pandit, Ashok | Emeritus Faculty | College of Engineering and Science: Department of Mechanical and Civil Engineering |  | apandit@fit.edu | groundwater, hydrologic modeling, numerical models, stormwater management”
### `8e94c5e8857ac3f2` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT sepri@fit.edu ⟵ “ | Sepri, Paavo | Emeritus Faculty | College of Engineering and Science: Department of Aerospace, Physics and Space Sciences |  | sepri@fit.edu | ”
### `8fd5f75cb7bd8f9d` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT lperdiga@fit.edu ⟵ “ | Perdigao, Lisa K. | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | lperdiga@fit.edu | ”
### `973b6c875a686ed4` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mdenius@fit.edu ⟵ “ | Denius, Marcia | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | mdenius@fit.edu | ”
### `992f655e0ea00a2e` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT shenker@fit.edu ⟵ “ | Shenker, Jonathan | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences | Marine Science | shenker@fit.edu | ”
### `a37f7195fb07e7c4` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gmarin@fit.edu ⟵ “ | Marin, Gerald A | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | gmarin@fit.edu | ”
### `a45fd1e7bf5b424f` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mkenkel@fit.edu ⟵ “ | Kenkel, Mary Beth | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology |  | mkenkel@fit.edu | ”
### `b3d814e960b44c0c` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT kgallagher@fit.edu ⟵ “ | Gallagher, Keith | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | kgallagher@fit.edu | ”
### `b4bb2008b5136538` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mgrace@fit.edu ⟵ “ | Grace, Michael | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | mgrace@fit.edu | ”
### `b8a41ef9f25c87a3` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT clarkj@fit.edu ⟵ “ | Clark, John F. | Emeritus Faculty | Nathan M. Bisk College of Business |  | clarkj@fit.edu | ”
### `b97700295945a394` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT msohn@fit.edu ⟵ “ | Sohn, Mary | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering |  | msohn@fit.edu | ”
### `bb04e978bb6707b6` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT lkhan@fit.edu ⟵ “ | Khan, Linda | Emeritus Faculty | Evans Library |  | lkhan@fit.edu | ”
### `bd22e01b609f8782` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT fronk@fit.edu ⟵ “ | Fronk, Robert | Emeritus Faculty | College of Engineering and Science , College of Engineering and Science: Department of Mathematics and Systems Engineering | Education | fronk@fit.edu | ”
### `bddec01fc97ea6e4` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT zborowski@fit.edu ⟵ “ | Zborowski, Andrew | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences | Ocean Engineering | zborowski@fit.edu | ”
### `bf33b0708828ea9b` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT wds@fit.edu ⟵ “ | Shoaff, William David | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | wds@fit.edu | ”
### `c09e99b2e82676ae` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT lweaver@fit.edu ⟵ “ | Weaver, Lynn Edward | Emeritus Faculty | Florida Institute of Technology , College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | lweaver@fit.edu | ”
### `c0d1b982e4091da6` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT vedkins@fit.edu ⟵ “ | Edkins, Vanessa | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology |  | vedkins@fit.edu | ”
### `c0e4bb7e61cb2bea` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT belanger@fit.edu ⟵ “ | Belanger, Thomas | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences | Marine Science | belanger@fit.edu | ”
### `c67979e8df6e1e9c` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT bonhomme@fit.edu ⟵ “ | Bonhomme, Mary | Emeritus Faculty | Florida Institute of Technology |  | bonhomme@fit.edu | ”
### `ccb4e90c44661154` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rbonhomm@fit.edu ⟵ “ | Bonhomme, Raymond | Emeritus Faculty | Florida Institute of Technology |  | rbonhomm@fit.edu | ”
### `d06e2ffba76c7f03` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT ahollingsworth@fit.edu ⟵ “ | Hollingsworth, Tim | Emeritus Faculty | Nathan M. Bisk College of Business |  | ahollingsworth@fit.edu | ”
### `da6d1e2f5c47875b` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gabrenya@fit.edu ⟵ “ | Gabrenya, William | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology |  | gabrenya@fit.edu | ”
### `db4995ee30f19660` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jwiggenhorn@fit.edu ⟵ “ | Wiggenhorn, Joan | Emeritus Faculty | Nathan M. Bisk College of Business |  | jwiggenhorn@fit.edu | ”
### `dbba1e566f51687d` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jsparks@fit.edu ⟵ “ | Sparks, Jean | Emeritus Faculty | Evans Library |  | jsparks@fit.edu | ”
### `de98a746c4a755dc` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT dsblenis@gmail.com ⟵ “ | Blenis, Debra | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering | Education | dsblenis@gmail.com | ”
### `e3c4eb5b549a8beb` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jflavelle1950@gmail.com ⟵ “ | Lavelle, John F | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | jflavelle1950@gmail.com | ”
### `e7fcaf8ac5741e96` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT aleonard@fit.edu ⟵ “ | Leonard, Alan | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | aleonard@fit.edu | ”
### `e8c36d7ae030b5a6` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jwindsor@fit.edu ⟵ “ | Windsor, John | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences |  | jwindsor@fit.edu | ”
### `ebe602095d9165d7` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mshaw@fit.edu ⟵ “ | Shaw, Michael | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering |  | mshaw@fit.edu | computer algebra systems, generalized variation of parameters, initial time difference, Kronecker products, matrix Lyapunov functions, nonlinear, sensitivi”
### `efd0b77c61fa516d` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jtrefry@fit.edu ⟵ “ | Trefry, John | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences |  | jtrefry@fit.edu | ”
### `f2350f81c909ecff` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT vkepuska@fit.edu ⟵ “ | Kepuska, Veton | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | vkepuska@fit.edu | ”
### `f5c31e5bc839d2de` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jennings@fit.edu ⟵ “ | Jennings, Paul | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering | Chemical Engineering | jennings@fit.edu | ”
### `f7550b30557e3464` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gary@fit,edu ⟵ “ | Hamme, Gary L. | Emeritus Faculty | Enrollment Management |  | gary@fit,edu | ”
### `f7ea3b8fcf8d2f2c` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT stilley@fit.edu ⟵ “ | Tilley, Scott | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering |  | stilley@fit.edu | ”
### `feb1e5170fcec7c6` Florida Institute of Technology — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT wscott@fit.edu ⟵ “ | Scott, Winston | Emeritus Faculty | Florida Institute of Technology |  | wscott@fit.edu | ”
### `mb1d0bca8bf6bc5d` Florida Institute of Technology — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.fit.edu/admission/applying/dual-enrollment/ (sha256 afada31794df)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 3, "tiers": 1}
  - per_credit_hour_charge: 100 ⟵ “Take Florida Tech classes for $100 per credit hour—a significant discount over normal tuition”
  - eligibility_tier: 3.0 ⟵ “Guaranteed admission to a Florida Tech degree program if you complete at least 6 semester credit hours and obtain a cumulative GPA of 3.00 or higher. (GPA calculated from Florida Tech courses taken)”
  - per_credit_hour_charge: 100 ⟵ “Dual enrollment tuition is only $100 per credit hour—a rate that is greatly reduced from normal tuition rates!”
  - eligibility_tier: 3.0 ⟵ “Guaranteed admission to a Florida Tech degree program if you complete at least 6 semester credit hours and achieve a cumulative GPA of 3.0 or higher in your courses at Florida Tech”
  - eligibility_tier: 3.0 ⟵ “Retention of a cumulative 3.0 unweighted GPA throughout all four years of the program.”
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA: 3.00 (un-weighted) on a 4.00 scale.”
### `00ef32bdeaef619e` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT aleonard@fit.edu ⟵ “ | Leonard, Alan | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | aleonard@fit.edu | ”
### `02242af79807f183` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT catanese@fit.edu ⟵ “ | Catanese, Anthony | Emeritus Faculty | Florida Institute of Technology |  | catanese@fit.edu | ”
### `031682a28b64ff6e` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT lweaver@fit.edu ⟵ “ | Weaver, Lynn Edward | Emeritus Faculty | Florida Institute of Technology , College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | lweaver@fit.edu | ”
### `051e03404c967b62` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mshaikh@fit.edu ⟵ “ | Shaikh, Muzaffar | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering | Systems Engineering | mshaikh@fit.edu | ”
### `057ba2f212656ef1` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT reichardr@fit.edu ⟵ “ | Reichard, Ronnal | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences , College of Engineering and Science: Department of Aerospace, Physics and Space Sciences |  | reichardr@fit.edu | composite materials, composite structures, composite des”
### `05b2ed0dca539c07` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT bonhomme@fit.edu ⟵ “ | Bonhomme, Mary | Emeritus Faculty | Florida Institute of Technology |  | bonhomme@fit.edu | ”
### `0c547d1a381d1532` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT webbe@fit.edu ⟵ “ | Webbe, Frank M. | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology | Psychology - Clinical | webbe@fit.edu | ”
### `1b208eead34886c1` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gary@fit,edu ⟵ “ | Hamme, Gary L. | Emeritus Faculty | Enrollment Management |  | gary@fit,edu | ”
### `1d32ab0ca50b2feb` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT msohn@fit.edu ⟵ “ | Sohn, Mary | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering |  | msohn@fit.edu | ”
### `25f2ec65ffcf35fc` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT sullivan@fit.edu ⟵ “ | Sullivan, Robert | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | sullivan@fit.edu | ”
### `30e0b83a46f8646b` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT fronk@fit.edu ⟵ “ | Fronk, Robert | Emeritus Faculty | College of Engineering and Science , College of Engineering and Science: Department of Mathematics and Systems Engineering | Education | fronk@fit.edu | ”
### `31c977a028c345b6` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT ggoldberg@fit.edu ⟵ “ | Goldberg, Gerald F | Emeritus Faculty | Nathan M. Bisk College of Business |  | ggoldberg@fit.edu | ”
### `32ae0316315915e5` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gabrenya@fit.edu ⟵ “ | Gabrenya, William | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology |  | gabrenya@fit.edu | ”
### `381f44b1a43cdad4` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mcfarlan@fit.edu ⟵ “ | McFarland, Thomas | Emeritus Faculty | Evans Library |  | mcfarlan@fit.edu | ”
### `3a94034f3ce9ba02` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT whitlow@fit.edu ⟵ “ | Whitlow, Jonathan | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering | Chemical Engineering | whitlow@fit.edu | chemical engineering, process design, renewable energy, process control, process modeling, process simulation”
### `476e18306ba48709` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT adilpare@fit.edu ⟵ “ | Dil Pare, Armand | Emeritus Faculty | College of Engineering and Science: Department of Mechanical and Civil Engineering | Mechanical Engineering | adilpare@fit.edu | ”
### `4ce8d6275a8400e0` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT zborowski@fit.edu ⟵ “ | Zborowski, Andrew | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences | Ocean Engineering | zborowski@fit.edu | ”
### `4f3f520922876680` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT grimwade@fit.edu ⟵ “ | Grimwade, Julia | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | grimwade@fit.edu | ”
### `569b76c68e44046a` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT djackson@fit.edu ⟵ “ | Jackson, Dennis | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering | Mathematics | djackson@fit.edu | ”
### `56ad22fd694e8046` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT babich@fit.edu ⟵ “ | Babich, Michael | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering | Chemistry | babich@fit.edu | ”
### `579e2ba59cbf1529` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mdenius@fit.edu ⟵ “ | Denius, Marcia | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | mdenius@fit.edu | ”
### `5a5982d7a45b7012` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT dcarroll@fit.edu ⟵ “ | Carroll, David | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | dcarroll@fit.edu | ”
### `5d8aeadf5daede16` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT bakerj@fit.edu ⟵ “ | Baker, Juanita | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology | Psychology - Clinical | bakerj@fit.edu | ”
### `5de01e55b8deaf9e` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jwiggenhorn@fit.edu ⟵ “ | Wiggenhorn, Joan | Emeritus Faculty | Nathan M. Bisk College of Business |  | jwiggenhorn@fit.edu | ”
### `60e1be6078bda56d` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mglicksman@fit.edu ⟵ “ | Glicksman, Martin | Emeritus Faculty | Florida Institute of Technology , College of Engineering and Science: Department of Mechanical and Civil Engineering | Mechanical Engineering | mglicksman@fit.edu | ”
### `60f0d779cc1e2e88` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT shenker@fit.edu ⟵ “ | Shenker, Jonathan | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences | Marine Science | shenker@fit.edu | ”
### `6323a809257e5df1` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jtrefry@fit.edu ⟵ “ | Trefry, John | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences |  | jtrefry@fit.edu | ”
### `6aed8148b7f9444d` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT belanger@fit.edu ⟵ “ | Belanger, Thomas | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences | Marine Science | belanger@fit.edu | ”
### `6f16777e7eed3c4e` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gmarin@fit.edu ⟵ “ | Marin, Gerald A | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | gmarin@fit.edu | ”
### `7af9aef28f2f2be4` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT clang@fit.edu ⟵ “ | Lang, Celine | Emeritus Faculty | Evans Library , College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | clang@fit.edu | ”
### `7e36e0b4a27355e7` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gallo@fit.edu ⟵ “ | Gallo, Michael | Emeritus Faculty | College of Aeronautics |  | gallo@fit.edu | ”
### `8a2faeeef9834c31` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT dsblenis@gmail.com ⟵ “ | Blenis, Debra | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering | Education | dsblenis@gmail.com | ”
### `8e3c0396157e0abf` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rmarshall1995@my.fit.edu ⟵ “ | Marshall, Ronald L. | Emeritus Faculty | Nathan M. Bisk College of Business |  | rmarshall1995@my.fit.edu | ”
### `99e482409b537c68` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT wds@fit.edu ⟵ “ | Shoaff, William David | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | wds@fit.edu | ”
### `a0f8cacd72a3eeea` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT wscott@fit.edu ⟵ “ | Scott, Winston | Emeritus Faculty | Florida Institute of Technology |  | wscott@fit.edu | ”
### `a29379cfc69db413` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT eperez@fit.edu ⟵ “ | Perez, Enrique | Emeritus Faculty | Nathan M. Bisk College of Business |  | eperez@fit.edu | ”
### `a2b6d6ca8bb1677a` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT dwilt@fit.edu ⟵ “ | Wilt, Donna | Emeritus Faculty | College of Aeronautics |  | dwilt@fit.edu | ”
### `a5b29a5a51760ee9` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT avamosi@fit.edu ⟵ “ | Vamosi, Alexander | Emeritus Faculty | Nathan M. Bisk College of Business |  | avamosi@fit.edu | ”
### `a957764c4d1c5847` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT gmicklow@fit.edu ⟵ “ | Micklow, Gerald | Emeritus Faculty | College of Engineering and Science: Department of Mechanical and Civil Engineering | Mechanical Engineering | gmicklow@fit.edu | ”
### `adb18fcdacc54147` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT lindeman@fit.edu ⟵ “ | Lindeman, Kenyon | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences |  | lindeman@fit.edu | Coastal management, Coastal fishes and habitats, Spatial planning, Marine protected areas, Systems science, Governance. Institutional sustainabilit”
### `af292965f512f150` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jrokach@fit.edu ⟵ “ | Rokach, Joshua | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering |  | jrokach@fit.edu | ”
### `afaef890ce1572f8` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jennings@fit.edu ⟵ “ | Jennings, Paul | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering | Chemical Engineering | jennings@fit.edu | ”
### `b33b0943a8d388bc` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT stilley@fit.edu ⟵ “ | Tilley, Scott | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering |  | stilley@fit.edu | ”
### `b378936ea0aa0492` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT twaite@fit.edu ⟵ “ | Waite, Thomas | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences |  | twaite@fit.edu | ”
### `b44825235532c5fd` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mkenkel@fit.edu ⟵ “ | Kenkel, Mary Beth | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology |  | mkenkel@fit.edu | ”
### `b5dd0eb6f7925a2c` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT relmore@fit.edu ⟵ “ | Elmore, Richard | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology |  | relmore@fit.edu | ”
### `b83ffa3166eaac00` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mshahsavari@fit.edu ⟵ “ | Shahsavari, Mehdi | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | mshahsavari@fit.edu | ”
### `be9ae0acc9cc3971` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT leachb@fit.edu ⟵ “ | Leach, Billy | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | leachb@fit.edu | ”
### `bf834e187bb7852a` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT barker@fit.edu ⟵ “ | Barker, Ballard | Emeritus Faculty | College of Aeronautics |  | barker@fit.edu | ”
### `c19411cb6caadf14` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rotaylor@fit.edu ⟵ “ | Taylor, Robert A. | Emeritus Faculty | College of Psych. and Liberal Arts |  | rotaylor@fit.edu | ”
### `c29dbc59bf4766e9` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jsparks@fit.edu ⟵ “ | Sparks, Jean | Emeritus Faculty | Evans Library |  | jsparks@fit.edu | ”
### `c5f0f7a0839777be` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rturner@fit.edu ⟵ “ | Turner, Richard L. | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences | Marine Science | rturner@fit.edu | ”
### `c8623ec52a4bc0d2` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jflavelle1950@gmail.com ⟵ “ | Lavelle, John F | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | jflavelle1950@gmail.com | ”
### `c953698357143b49` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT ahollingsworth@fit.edu ⟵ “ | Hollingsworth, Tim | Emeritus Faculty | Nathan M. Bisk College of Business |  | ahollingsworth@fit.edu | ”
### `c97c23d7b140976a` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jolson@fit.edu ⟵ “ | Olson, Joel | Emeritus Faculty | College of Engineering and Science: Chemistry and Chemical Engineering | Chemistry | jolson@fit.edu | ”
### `cd2621f8c2521b49` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT vkepuska@fit.edu ⟵ “ | Kepuska, Veton | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | vkepuska@fit.edu | ”
### `d057254e7d7fcb38` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT ryan@fit.edu ⟵ “ | Stansifer, Ryan | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | ryan@fit.edu | programming languages, formal methods and software development, compilers and static analy”
### `d4674ce508766efd` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mgrace@fit.edu ⟵ “ | Grace, Michael | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | mgrace@fit.edu | ”
### `d60678cf15bd3e3e` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT clarkj@fit.edu ⟵ “ | Clark, John F. | Emeritus Faculty | Nathan M. Bisk College of Business |  | clarkj@fit.edu | ”
### `d71d633239059572` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rweigel@fit.edu ⟵ “ | Weigel, Russell | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | rweigel@fit.edu | ”
### `dde8211afd8d5dd5` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT nchlosta@fit.edu ⟵ “ | Chlosta, Norman | Emeritus Faculty | Nathan M. Bisk College of Business |  | nchlosta@fit.edu | ”
### `dedea8f1f860c64a` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT lperdiga@fit.edu ⟵ “ | Perdigao, Lisa K. | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | lperdiga@fit.edu | ”
### `e75d7118006d1d04` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT jwindsor@fit.edu ⟵ “ | Windsor, John | Emeritus Faculty | College of Engineering and Science: Department of Ocean Engineering and Marine Sciences |  | jwindsor@fit.edu | ”
### `ebb8a33f65a008d5` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT rbonhomm@fit.edu ⟵ “ | Bonhomme, Raymond | Emeritus Faculty | Florida Institute of Technology |  | rbonhomm@fit.edu | ”
### `ec08e6e75293543a` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT eugene@fit.edu ⟵ “ | Dshalalow, Jewgeni | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering |  | eugene@fit.edu | stochastic processes, abstract analysis, random measures, biomathematics, queueing, reliability, stochastic games, stochastic finance, cancer researc”
### `ece0d56c7d90cf08` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT chelmste@fit.edu ⟵ “ | Helmstetter, Charles | Emeritus Faculty | College of Engineering and Science: Biomedical Engineering and Science |  | chelmste@fit.edu | ”
### `eef4bf1ce9734191` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT fmh@fit.edu ⟵ “ | Ham, Fredric | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Electrical and Computer Engineering | fmh@fit.edu | ”
### `f038275f1a1e53c4` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT engblom@fit.edu ⟵ “ | Engblom, John | Emeritus Faculty | College of Engineering and Science | Mechanical Engineering | engblom@fit.edu | ”
### `f0f55158cb1bb978` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT apandit@fit.edu ⟵ “ | Pandit, Ashok | Emeritus Faculty | College of Engineering and Science: Department of Mechanical and Civil Engineering |  | apandit@fit.edu | groundwater, hydrologic modeling, numerical models, stormwater management”
### `f1628ad9bf160836` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT kgallagher@fit.edu ⟵ “ | Gallagher, Keith | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | kgallagher@fit.edu | ”
### `f17a6f224f51fdca` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT mshaw@fit.edu ⟵ “ | Shaw, Michael | Emeritus Faculty | College of Engineering and Science: Department of Mathematics and Systems Engineering |  | mshaw@fit.edu | computer algebra systems, generalized variation of parameters, initial time difference, Kronecker products, matrix Lyapunov functions, nonlinear, sensitivi”
### `f62aaf4e2c440f1e` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT hheck@fit.edu ⟵ “ | Heck, Howell | Emeritus Faculty | College of Engineering and Science: Department of Mechanical and Civil Engineering | Civil Engineering | hheck@fit.edu | ”
### `f62ab5d3d71daf8e` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT lkhan@fit.edu ⟵ “ | Khan, Linda | Emeritus Faculty | Evans Library |  | lkhan@fit.edu | ”
### `f92e279e260cb89b` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT wallen@fit.edu ⟵ “ | Allen, William | Emeritus Faculty | College of Engineering and Science: Department of Electrical Engineering and Computer Science | Computer Science, Software Engineering and Cybersecurity | wallen@fit.edu | ”
### `fa65c128f09755e5` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT strother@fit.edu ⟵ “ | Strother, Judith | Emeritus Faculty | College of Psych. and Liberal Arts: School of Arts and Communication |  | strother@fit.edu | ”
### `fb962cd45b746b52` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT kzieg@fit.edu ⟵ “ | Zieg, Kermit | Emeritus Faculty | Nathan M. Bisk College of Business |  | kzieg@fit.edu | ”
### `fc19a62b4ccabaf3` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT sepri@fit.edu ⟵ “ | Sepri, Paavo | Emeritus Faculty | College of Engineering and Science: Department of Aerospace, Physics and Space Sciences |  | sepri@fit.edu | ”
### `fcfd05459cdec19d` Florida Institute of Technology-Online — awards 2026-27 [new] (source_unlabeled)
- source: https://www.fit.edu/faculty-profiles/emeritus/ (sha256 04ab9aab8873)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT vedkins@fit.edu ⟵ “ | Edkins, Vanessa | Emeritus Faculty | College of Psych. and Liberal Arts: School of Psychology |  | vedkins@fit.edu | ”
### `m50fcacc7b64da15` Florida Institute of Technology-Online — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.fit.edu/admission/applying/dual-enrollment/ (sha256 afada31794df)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 3, "tiers": 1}
  - per_credit_hour_charge: 100 ⟵ “Take Florida Tech classes for $100 per credit hour—a significant discount over normal tuition”
  - eligibility_tier: 3.0 ⟵ “Guaranteed admission to a Florida Tech degree program if you complete at least 6 semester credit hours and obtain a cumulative GPA of 3.00 or higher. (GPA calculated from Florida Tech courses taken)”
  - per_credit_hour_charge: 100 ⟵ “Dual enrollment tuition is only $100 per credit hour—a rate that is greatly reduced from normal tuition rates!”
  - eligibility_tier: 3.0 ⟵ “Guaranteed admission to a Florida Tech degree program if you complete at least 6 semester credit hours and achieve a cumulative GPA of 3.0 or higher in your courses at Florida Tech”
  - eligibility_tier: 3.0 ⟵ “Retention of a cumulative 3.0 unweighted GPA throughout all four years of the program.”
  - eligibility_tier: 3.0 ⟵ “Cumulative GPA: 3.00 (un-weighted) on a 4.00 scale.”
### `bf46a79a9cf030ec` Florida International University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://transfer.fiu.edu/transfer-101/credit-options/credit-by-exam-tables/ (sha256 1ee2a29e663f)
- issues: rows_without_score
- checks: {"distinct_exams": 16, "equivalencies": 31, "rows_without_score": 2}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | POS 2041 (3)1 | 50 | Social Science Group 1 (& Civic Literacy course and exam requirement)”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology, General | BSC UCC1 (3) | 50 | Natural Sciences (No lab)”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | MAC 2233 (3) | 50 | Mathematics Group 2”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry, General | CHM UCC1 (3) | 50 | Natural Sciences (No lab)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition* | ENC 1101 (3) & ENC 1102 (3) | 50 | Communication”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | DEP 2000 (3) | 50 | Social Science Group 2”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | HUM UCC2 (3) | 50 | Humanities Group 2”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Principles of | ECO 2013 (3) | 50 | Social Science Group 1”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Principles of | ECO 2023 (3) | 50 | Social Science Group 2”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-Calculus | MAC 1140 (3) | 50 | Mathematics Group 2”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory | PSY 2012 (3) | 50 | Social Science Group 1”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introductory | SYG 2000 (3) | 50 | Elective”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Sociology, Introductory | Additional CLEP Exams”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language | FRE 1130 (5) | 50 | Foreign Language”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language | FRE 1130 (5) & FRE 1131 (5) | 59 | Foreign Language”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language | GER 1130 (5) | 50 | Foreign Language”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language | GER 1130 (5) & GER 1131 (5) | 60 | Foreign Language”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language | SPN 1130 (3) | 50 | Foreign Language”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language | SPN 1130 (3) & SPN 1131 (3) | 63 | Foreign Language”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing | SPN 1130 (3) | 50 | Foreign Language”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|65]:  ⟵ “Spanish with Writing | SPN 1130 (3) & SPN 1131 (3) | 65 | Foreign Language”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|ELE UCC1 (3)]:  ⟵ “Spanish with Writing | Analyzing and Interpreting Literature 2 | ELE UCC1 (3) | 50”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|AML 2010 (3)]:  ⟵ “Spanish with Writing | American Literature | AML 2010 (3) | 50”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|ELE UCC1 (3)]:  ⟵ “Spanish with Writing | Business Law, Introduction to | ELE UCC1 (3) | 50”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|ELE UCC1 (3)]:  ⟵ “Spanish with Writing | Educational Psychology, Introduction to | ELE UCC1 (3) | 50”
  - … 6 more rows
### `89e26d65ceadee6e` Florida Polytechnic University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://floridapoly.edu/wp-content/uploads/2025/09/cds_2024-2025.pdf (sha256 4c812bfc1ea4)
- issues: stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 3624 ⟵ “Total first-time, first-year (degree-seeking) who applied          2935         590            99           0      3624”
  - admits: 1435 ⟵ “Total first-time, first-year (degree-seeking) who were admitted    1003         373            59           0      1435”
  - enrolled: 477 ⟵ “Total first-time, first-year (degree-seeking) enrolled              435         31             11           0       477”
  - sat_composite_25..75: [1170, 1250, 1340] ⟵ “SAT Composite                     1170                      1250                       1340”
  - sat_math_25..75: [580, 620, 670] ⟵ “SAT Math                           580                       620                       670”
  - act_25..75: [21, 24, 26] ⟵ “ACT Composite                      21                        24                         26”
### `ecf16a9ec012af22` Florida Polytechnic University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://floridapoly.edu/admissions/financial-aid-resources/ (sha256 3df4401fd09e)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please refer to the FPU 5.00742 Satisfactory Academic Progress Policy for additional information on SAP, including Warning, Appeal and Probation.”
### `08772c13fbca0fe1` Florida SouthWestern State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fsw.edu/financialaid/pj (sha256 c6e4cf5d3221)
- issues: semantic_review_required, conflicting_sources:https://www.fsw.edu/financialaid,https://www.fsw.edu/financialaid/scholarships
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Cashier Services Satisfactory Academic Progress (SAP) Professional Judgment Grants & Loans Net Price Calculator Attendance Verification Work Study Program Scholarship Information Verification Information Over Awards Calculate your GPA Privacy Information and Your Rights (FERPA) Professional Judgment The Higher Education Act of 1965 (HEA), as amended, combined with the FAFSA Simplification Act prov”
  - sentence: professional_judgment ⟵ “The authority is known as Professional Judgment (PJ) and may be exercised on a case-by-case basis to different categories as described below: Special Circumstances refer to the financial situations (loss of a job, etc.) that justify an aid administrator adjusting data elements in the Cost of Attendance (COA) or in the Student Aid Index (SAI) calculation.”
### `9cf5e5aa01650cf2` Florida SouthWestern State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fsw.edu/financialaid/pj (sha256 c6e4cf5d3221)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “The reasons may be: you are unaccompanied and homeless, or at risk of homelessness unsure if a dependency override is warranted you may have to provide parental data you may be permitted to borrow only unsubsidized loans because you can document that your parents have refused support and will not provide their information on the FAFSA If you feel that any of the mentioned circumstances apply to yo”
### `a8194099cf7c463d` Florida SouthWestern State College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.fsw.edu/financialaid/scholarships (sha256 d629e770a2af)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.fsw.edu/financialaid,https://www.fsw.edu/financialaid/pj
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Cashier Services Satisfactory Academic Progress (SAP) Professional Judgment Grants & Loans Net Price Calculator Attendance Verification Work Study Program Scholarship Information Verification Information Over Awards Calculate your GPA Privacy Information and Your Rights (FERPA) Scholarship Information Apply Now Federal and State Scholarships/Grants Institutional Scholarships Contact Information Th”
### `b499362db299d81e` Florida SouthWestern State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fsw.edu/financialaid/pj (sha256 c6e4cf5d3221)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abuse or abandonment, incarceration), more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Providing relevant documentation, preferably from an unrelated third party, is critical to the special or unusual circumstance appeal’s success.”
  - sentence: need_based_special_circumstances ⟵ “Unable to Provide Parent Data Students who are unable to provide parent data and have a FAFSA that was rejected due to an unusual or special circumstance should also reach out to our office immediately.”
### `b7197dab971521ba` Florida SouthWestern State College — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.fsw.edu/financialaid (sha256 31bc7e169cce)
- issues: semantic_review_required, conflicting_sources:https://www.fsw.edu/financialaid/pj,https://www.fsw.edu/financialaid/scholarships
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Cashier Services Satisfactory Academic Progress (SAP) Professional Judgment Grants & Loans Net Price Calculator Attendance Verification Work Study Program Scholarship Information Verification Information Over Awards Calculate your GPA Privacy Information and Your Rights (FERPA) Financial Aid TODAY'S TOP TIPS Breaking news!”
### `fe787635356c2603` Florida SouthWestern State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fsw.edu/financialaid/sap (sha256 88192d411049)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “The student will NOT receive financial aid for the next semester without an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “How can I submit a SAP Appeal?”
### `00a99b1043d4eb2a` Florida Southern College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.flsouthern.edu/getmedia/1699df9f-12a7-40a9-b644-305a30175852/fsc-terms-and-conditions-sap-26-27.pdf (sha256 d94a5a22c209)
- issues: semantic_review_required, conflicting_sources:https://www.flsouthern.edu/admissions/undergraduate/undergraduate-financial-aid/undergraduate-scholarships/george-w-jenkins-application
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Items that would be acceptable reasons for appeal would be the death of a relative of the student, an injury or illness of the student, or other documentable special circumstance.”
### `096e3c39f68e0718` Florida Southern College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.flsouthern.edu/getmedia/1699df9f-12a7-40a9-b644-305a30175852/fsc-terms-and-conditions-sap-26-27.pdf (sha256 d94a5a22c209)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Renewal requires the successful completion of at least 24 credit hours during the academic year, 12 if aid is received for only one semester. • Details of state requirements may be found at https://www.floridastudentfinancialaidsg.org/SAPHome/SAPHome?url=home under specific aid programs. • Students that do not meet the renewal GPA and/or required credit hours for the Bright Futures scholarship due”
### `28bd333e674ff85b` Florida Southern College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.flsouthern.edu/getmedia/c5edc2b6-9f20-403f-b496-b527a217d606/fsc-terms-and-conditions-sap-25-26.pdf (sha256 dc22c12c7093)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Items that would be acceptable reasons for appeal would be the death of a relative of the student, an injury or illness of the student, or other documentable special circumstances.”
### `297206e945dd30ad` Florida Southern College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.flsouthern.edu/getmedia/1699df9f-12a7-40a9-b644-305a30175852/fsc-terms-and-conditions-sap-26-27.pdf (sha256 d94a5a22c209)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) APPEAL PROCESS • With mitigating circumstances, a written appeal for continued eligibility may be made to the Director of Financial Aid, and an ad hoc committee will adjudicate the appeal.”
  - sentence: sap_appeal ⟵ “Financial aid probation is a status assigned to a student who fails to make satisfactory academic progress and who has appealed and has had eligibility for aid reinstated.”
### `82046fe230e29ad3` Florida Southern College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.flsouthern.edu/getmedia/c5edc2b6-9f20-403f-b496-b527a217d606/fsc-terms-and-conditions-sap-25-26.pdf (sha256 dc22c12c7093)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP APPEAL PROCESS • With mitigating circumstances, a written appeal for continued eligibility may be made to the Director of Financial Aid, and an ad hoc committee will adjudicate the appeal.”
  - sentence: sap_appeal ⟵ “Financial aid probation is a status assigned to a student who fails to make satisfactory academic progress and who has appealed and has had eligibility for aid reinstated.”
### `88dabbae591f7ec1` Florida Southern College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.flsouthern.edu/getmedia/c5edc2b6-9f20-403f-b496-b527a217d606/fsc-terms-and-conditions-sap-25-26.pdf (sha256 dc22c12c7093)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Renewal generally requires the successful completion of at least 24 credit hours during the academic year, (12 if aid is received for only one semester). • Details of state requirements may be found at https://www.floridastudentfinancialaidsg.org/SAPHome/SAPHome?url=home under specific aid programs. • Students that do not meet the renewal GPA and/or required credit hours for the Bright Futures sch”
### `abf61709bd4c3d83` Florida Southern College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.flsouthern.edu/admissions/undergraduate/undergraduate-financial-aid/undergraduate-scholarships/george-w-jenkins-application (sha256 f0b86da1cce3)
- issues: semantic_review_required, conflicting_sources:https://www.flsouthern.edu/getmedia/1699df9f-12a7-40a9-b644-305a30175852/fsc-terms-and-conditions-sap-26-27.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Submit a Jenkins Scholarship Essay with significant emphasis on what special circumstances you have faced, specifically detailing your long history of facing and overcoming significant adversity.”
  - sentence: need_based_special_circumstances ⟵ “What special circumstances have you faced, specifically your history of facing and overcoming significant adversity?”
### `5af9ddfae8a94148` Florida State College at Jacksonville — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fscj.edu/financial-aid/satisfactory-academic-progress/sap-appeal---appeal-process (sha256 836ae47c0aed)
- issues: semantic_review_required, conflicting_sources:https://www.fscj.edu/financial-aid/satisfactory-academic-progress,https://www.fscj.edu/financial-aid/satisfactory-academic-progress/life-cycle-of-the-sap-appeal-process
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Speak with a Student Success Navigator to discuss your “Not Meets” Status This will include checking your GPA and credit attempts Extenuating circumstance(s) Adding the SAP appeal to your Task List Make sure to open the Satisfactory Academic Progress Task link and follow the instructions.”
  - sentence: sap_appeal ⟵ “Fill out the SAP Appeal Form Write your statement explaining (in detail) your extenuating circumstance(s).”
  - sentence: sap_appeal ⟵ “Incomplete SAP appeals will be denied.”
  - sentence: sap_appeal ⟵ “It is advised that you are registered in at least one class in case your SAP Appeal is approved.”
  - sentence: sap_appeal ⟵ “Email your complete SAP Appeal Packet to financialaid@fscj.edu.”
  - sentence: sap_appeal ⟵ “Periodically check your SAP status to see if a SAP Appeal decision has been made.”
### `a12294a462f3c868` Florida State College at Jacksonville — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.fscj.edu/financial-aid/satisfactory-academic-progress/sap-frequently-asked-questions (sha256 1f151e257de7)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.fscj.edu/financial-aid/satisfactory-academic-progress/sap-statuses
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Yes, if you have a strong reason for not “Meeting SAP”, like an accident, medical situation, death in your immediate family, or another major challenge that was out of your control, you have the option to submit a SAP Appeal.”
  - sentence: sap_appeal ⟵ “Can I submit a SAP Appeal more than once?”
  - sentence: sap_appeal ⟵ “If your SAP Appeal submitted for a Fall 2023 car accident is approved, you can submit a new SAP Appeal if you are in another car accident for a more recent semester.”
  - sentence: sap_appeal ⟵ “If your SAP Appeal submitted for a Fall 2023 car accident is denied, you cannot submit a new SAP Appeal for the same Fall 2023 car accident.”
  - sentence: sap_appeal ⟵ “How long does it take to hear back about my SAP Appeal decision?”
  - sentence: sap_appeal ⟵ “SAP appeal decisions can take up to 30 business days.”
### `bb2c9b7eefdd3368` Florida State College at Jacksonville — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fscj.edu/financial-aid/satisfactory-academic-progress/life-cycle-of-the-sap-appeal-process (sha256 b88f488873cc)
- issues: semantic_review_required, conflicting_sources:https://www.fscj.edu/financial-aid/satisfactory-academic-progress,https://www.fscj.edu/financial-aid/satisfactory-academic-progress/sap-appeal---appeal-process
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “You (the student) will reach out to a Student Success Navigator to discuss why you are in the current SAP status The discussion can be about # of credits to pass to bring SAP status back to Meets and/or offer the SAP appeal option.”
  - sentence: sap_appeal ⟵ “It is advised that you are registered in at least one class in case your SAP Appeal is approved.”
  - sentence: sap_appeal ⟵ “The Student Success Navigator will: Add the SAP Appeal task to your account You (the student) will: Log in to your MyFSCJ Student portal and click on Tasks Click on the Satisfactory Academic Progress Task item, read and follow the included instructions After your statement is written and documentation is gathered, schedule an appointment with your Assigned Advisor or any Academic and Career Adviso”
  - sentence: sap_appeal ⟵ “The ACA will: Create an Academic Degree Plan and discuss which class you are paying for to submit your appeal Review and sign your SAP Appeal Packet Provide instructions on how to submit your SAP Appeal for a decision.”
  - sentence: sap_appeal ⟵ “You (the student) will email your SAP Appeal packet to financialaid@fscj.edu.”
  - sentence: sap_appeal ⟵ “The first day to submit a SAP Appeal is the first day of the semester The last day to submit a SAP Appeal is 30 days after the C session starts Decisions can take up to 30 calendar days, and you will be notified by email in your MyFSCJ student account.”
### `c26d3163ae56f098` Florida State College at Jacksonville — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fscj.edu/financial-aid/satisfactory-academic-progress (sha256 3947b0dcde3a)
- issues: semantic_review_required, conflicting_sources:https://www.fscj.edu/financial-aid/satisfactory-academic-progress/life-cycle-of-the-sap-appeal-process,https://www.fscj.edu/financial-aid/satisfactory-academic-progress/sap-appeal---appeal-process
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Receive an approval decision for a SAP appeal.”
  - sentence: sap_appeal ⟵ “Who can help you understand SAP and the Appeal Process better?”
### `d810a200394e2aff` Florida State College at Jacksonville — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.fscj.edu/financial-aid/satisfactory-academic-progress/sap-statuses (sha256 e622de910d86)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.fscj.edu/financial-aid/satisfactory-academic-progress/sap-frequently-asked-questions
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Submit a SAP Appeal Florida State College at Jacksonville empowers students to achieve their goals by providing exceptional learning experiences that promote intellectual growth, civic engagement, and workforce connections.”
### `2e96a07b739009fa` Florida State College at Jacksonville — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.fscj.edu/academics/college-readiness-programs/dual-enrollment (sha256 09e91dbe2434)
- issues: conflicting_values:max_credit_hours_per_term
- checks: {"fields": [], "tiers": 0}
  - max_credit_hours_per_term: 11 ⟵ “Traditional Dual Enrollment provides eligible accelerated high school students the opportunity to simultaneously earn both college credit and a high school diploma. Students may take a maximum of 11 credits in the fall and spring terms, and up to 6 credits for the summer term (for a total of two cou”
  - max_credit_hours_per_term: 6 ⟵ “Traditional Dual Enrollment provides eligible accelerated high school students the opportunity to simultaneously earn both college credit and a high school diploma. Students may take a maximum of 11 credits in the fall and spring terms, and up to 6 credits for the summer term (for a total of two cou”
### `0bae6386f5fc42e5` Florida State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://tuition.fsu.edu/cost-attendance/cost-estimates-fall-2026-spring-2027 (sha256 47e6c956d1e8)
- issues: components_do_not_reconcile, cost_period_semester, conflicting_sources:https://tuition.fsu.edu/cost-attendance/cost-estimates-summer-2026
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - on_campus:Tuition: 4693 ⟵ “Tuition | $4,693 | $4,693 | $4,693 | $21,320 | $21,320 | $21,320”
  - on_campus:Fees: 10 ⟵ “Fees | $10 | $10 | $10 | $10 | $10 | $10”
  - on_campus:Course Materials, Supplies, and Equipment: 1380 ⟵ “Course Materials, Supplies, and Equipment | $1,380 | $1,380 | $1,380 | $1,380 | $1,380 | $1,380”
  - on_campus:Transportation: 2320 ⟵ “Transportation | $2,320 | $2,320 | $1,160 | $3,590 | $3,590 | $1,795”
  - on_campus:Personal: 2504 ⟵ “Personal | $2,504 | $2,504 | $2,504 | $2,504 | $2,504 | $2,504”
  - on_campus:TOTAL: 25487 ⟵ “TOTAL | $25,487 | $25,067 | $19,697 | $43,384 | $42,964 | $36,959”
### `2b5e54d0054530e6` Florida State University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://tuition.fsu.edu/cost-estimates-fall-2025-spring-2026 (sha256 a16e0d7b1f4d)
- issues: components_do_not_reconcile, cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - on_campus:Tuition: 4693 ⟵ “Tuition | $4,693 | $4,693 | $4,693 | $19,152 | $19,152 | $19,152”
  - on_campus:Fees: 10 ⟵ “Fees | $10 | $10 | $10 | $10 | $10 | $10”
  - on_campus:Course Materials, Supplies, and Equipment: 1200 ⟵ “Course Materials, Supplies, and Equipment | $1,200 | $1,200 | $1,200 | $1,200 | $1,200 | $1,200”
  - on_campus:Transportation: 2460 ⟵ “Transportation | $2,460 | $2,460 | $1,230 | $3,652 | $3,652 | $1,826”
  - on_campus:Personal: 2432 ⟵ “Personal | $2,432 | $2,432 | $2,432 | $2,432 | $2,432 | $2,432”
  - on_campus:TOTAL: 24375 ⟵ “TOTAL | $24,375 | $24,375 | $19,155 | $40,026 | $40,026 | $34,210”
### `33660b798c17cacd` Florida State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://tuition.fsu.edu/cost-attendance/cost-estimates-fall-2026-spring-2027 (sha256 47e6c956d1e8)
- issues: components_do_not_reconcile, cost_period_semester, conflicting_sources:https://tuition.fsu.edu/cost-attendance/cost-estimates-summer-2026
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - on_campus:Tuition: 4693 ⟵ “Tuition | $4,693 | $4,693 | $4,693 | $21,320 | $21,320 | $21,320”
  - on_campus:Fees: 10 ⟵ “Fees | $10 | $10 | $10 | $10 | $10 | $10”
  - on_campus:Course Materials, Supplies, and Equipment: 1380 ⟵ “Course Materials, Supplies, and Equipment | $1,380 | $1,380 | $1,380 | $1,380 | $1,380 | $1,380”
  - on_campus:Transportation: 2320 ⟵ “Transportation | $2,320 | $2,320 | $1,160 | $3,590 | $3,590 | $1,795”
  - on_campus:Personal: 2504 ⟵ “Personal | $2,504 | $2,504 | $2,504 | $2,504 | $2,504 | $2,504”
  - on_campus:TOTAL: 25067 ⟵ “TOTAL | $25,487 | $25,067 | $19,697 | $43,384 | $42,964 | $36,959”
### `40f1ffed2a2ab4ff` Florida State University — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://tuition.fsu.edu/cost-attendance/cost-estimates-summer-2026 (sha256 b3c4dd3ea069)
- issues: ambiguous_year_labels, arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://tuition.fsu.edu/cost-attendance/cost-estimates-fall-2026-spring-2027
- checks: {"columns": 2, "components_reconcile": false, "rows": 6}
  - column:Tuition: 1800 ⟵ “Tuition | $1,800 | $2,400”
  - column:Fees: 113 ⟵ “Fees | $113 | $113”
  - column:Books, Course Materials, Supplies, and Equipment: 250 ⟵ “Books, Course Materials, Supplies, and Equipment | $250 | $250”
  - column:Transportation: 591 ⟵ “Transportation | $591 | $591”
  - column:Personal: 1165 ⟵ “Personal | $1,165 | $1,250”
  - column:TOTAL: 7038 ⟵ “TOTAL | $7,038 | $8,253”
  - column:Tuition: 2400 ⟵ “Tuition | $1,800 | $2,400”
  - column:Fees: 113 ⟵ “Fees | $113 | $113”
  - column:Books, Course Materials, Supplies, and Equipment: 250 ⟵ “Books, Course Materials, Supplies, and Equipment | $250 | $250”
  - column:Transportation: 591 ⟵ “Transportation | $591 | $591”
  - column:Personal: 1250 ⟵ “Personal | $1,165 | $1,250”
  - column:TOTAL: 8253 ⟵ “TOTAL | $7,038 | $8,253”
### `4e4b9b2cced38b8c` Florida State University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://tuition.fsu.edu/cost-estimates-fall-2025-spring-2026 (sha256 a16e0d7b1f4d)
- issues: arrangement_unlabeled, components_do_not_reconcile, cost_period_semester, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": false, "rows": 7}
  - column:Tuition: 5604 ⟵ “Tuition | $5,604 | $5,604 | $5,604 | $20,063 | $20,063 | $20,063”
  - column:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50 | $50 | $50”
  - column:Books: 800 ⟵ “Books | $800 | $800 | $800 | $800 | $800 | $800”
  - column:Course Materials, Supplies, and Equipment: 400 ⟵ “Course Materials, Supplies, and Equipment | $400 | $400 | $400 | $400 | $400 | $400”
  - column:Transportation: 1230 ⟵ “Transportation | $2,460 | $2,460 | $1,230 | $3,652 | $3,652 | $1,826”
  - column:Personal: 2432 ⟵ “Personal | $2,432 | $2,432 | $2,432 | $2,432 | $2,432 | $2,432”
  - column:TOTAL: 20326 ⟵ “TOTAL | $25,766 | $25,766 | $20,326 | $41,417 | $41,417 | $35,381”
  - column:Tuition: 20063 ⟵ “Tuition | $5,604 | $5,604 | $5,604 | $20,063 | $20,063 | $20,063”
  - column:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50 | $50 | $50”
  - column:Books: 800 ⟵ “Books | $800 | $800 | $800 | $800 | $800 | $800”
  - column:Course Materials, Supplies, and Equipment: 400 ⟵ “Course Materials, Supplies, and Equipment | $400 | $400 | $400 | $400 | $400 | $400”
  - column:Transportation: 3652 ⟵ “Transportation | $2,460 | $2,460 | $1,230 | $3,652 | $3,652 | $1,826”
  - column:Personal: 2432 ⟵ “Personal | $2,432 | $2,432 | $2,432 | $2,432 | $2,432 | $2,432”
  - column:TOTAL: 41417 ⟵ “TOTAL | $25,766 | $25,766 | $20,326 | $41,417 | $41,417 | $35,381”
  - column:Tuition: 20063 ⟵ “Tuition | $5,604 | $5,604 | $5,604 | $20,063 | $20,063 | $20,063”
  - column:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50 | $50 | $50”
  - column:Books: 800 ⟵ “Books | $800 | $800 | $800 | $800 | $800 | $800”
  - column:Course Materials, Supplies, and Equipment: 400 ⟵ “Course Materials, Supplies, and Equipment | $400 | $400 | $400 | $400 | $400 | $400”
  - column:Transportation: 3652 ⟵ “Transportation | $2,460 | $2,460 | $1,230 | $3,652 | $3,652 | $1,826”
  - column:Personal: 2432 ⟵ “Personal | $2,432 | $2,432 | $2,432 | $2,432 | $2,432 | $2,432”
  - column:TOTAL: 41417 ⟵ “TOTAL | $25,766 | $25,766 | $20,326 | $41,417 | $41,417 | $35,381”
  - column:Tuition: 20063 ⟵ “Tuition | $5,604 | $5,604 | $5,604 | $20,063 | $20,063 | $20,063”
  - column:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50 | $50 | $50”
  - column:Books: 800 ⟵ “Books | $800 | $800 | $800 | $800 | $800 | $800”
  - column:Course Materials, Supplies, and Equipment: 400 ⟵ “Course Materials, Supplies, and Equipment | $400 | $400 | $400 | $400 | $400 | $400”
  - … 3 more rows
### `99ef2884c38d6ce8` Florida State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://tuition.fsu.edu/cost-attendance/cost-estimates-fall-2026-spring-2027 (sha256 47e6c956d1e8)
- issues: arrangement_unlabeled, components_do_not_reconcile, cost_period_semester, residency_unknown, conflicting_sources:https://tuition.fsu.edu/cost-attendance/cost-estimates-summer-2026
- checks: {"columns": 4, "components_reconcile": false, "rows": 6}
  - column:Tuition: 5604 ⟵ “Tuition | $5,604 | $5,604 | $5,604 | $22,232 | $22,232 | $22,232”
  - column:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50 | $50 | $50”
  - column:Books ,Course Materials, Supplies, and Equipment: 1380 ⟵ “Books ,Course Materials, Supplies, and Equipment | $1,380 | $1,380 | $1,380 | $1,380 | $1,380 | $1,380”
  - column:Transportation: 1160 ⟵ “Transportation | $2,320 | $2,320 | $1,160 | $3,590 | $3,590 | $1,795”
  - column:Personal: 2504 ⟵ “Personal | $2,504 | $2,504 | $2,504 | $2,504 | $2,504 | $2,432”
  - column:TOTAL: 20648 ⟵ “TOTAL | $26,438 | $26,018 | $20,648 | $44,336 | $43,916 | $37,911”
  - column:Tuition: 22232 ⟵ “Tuition | $5,604 | $5,604 | $5,604 | $22,232 | $22,232 | $22,232”
  - column:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50 | $50 | $50”
  - column:Books ,Course Materials, Supplies, and Equipment: 1380 ⟵ “Books ,Course Materials, Supplies, and Equipment | $1,380 | $1,380 | $1,380 | $1,380 | $1,380 | $1,380”
  - column:Transportation: 3590 ⟵ “Transportation | $2,320 | $2,320 | $1,160 | $3,590 | $3,590 | $1,795”
  - column:Personal: 2504 ⟵ “Personal | $2,504 | $2,504 | $2,504 | $2,504 | $2,504 | $2,432”
  - column:TOTAL: 44336 ⟵ “TOTAL | $26,438 | $26,018 | $20,648 | $44,336 | $43,916 | $37,911”
  - column:Tuition: 22232 ⟵ “Tuition | $5,604 | $5,604 | $5,604 | $22,232 | $22,232 | $22,232”
  - column:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50 | $50 | $50”
  - column:Books ,Course Materials, Supplies, and Equipment: 1380 ⟵ “Books ,Course Materials, Supplies, and Equipment | $1,380 | $1,380 | $1,380 | $1,380 | $1,380 | $1,380”
  - column:Transportation: 3590 ⟵ “Transportation | $2,320 | $2,320 | $1,160 | $3,590 | $3,590 | $1,795”
  - column:Personal: 2504 ⟵ “Personal | $2,504 | $2,504 | $2,504 | $2,504 | $2,504 | $2,432”
  - column:TOTAL: 43916 ⟵ “TOTAL | $26,438 | $26,018 | $20,648 | $44,336 | $43,916 | $37,911”
  - column:Tuition: 22232 ⟵ “Tuition | $5,604 | $5,604 | $5,604 | $22,232 | $22,232 | $22,232”
  - column:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50 | $50 | $50”
  - column:Books ,Course Materials, Supplies, and Equipment: 1380 ⟵ “Books ,Course Materials, Supplies, and Equipment | $1,380 | $1,380 | $1,380 | $1,380 | $1,380 | $1,380”
  - column:Transportation: 1795 ⟵ “Transportation | $2,320 | $2,320 | $1,160 | $3,590 | $3,590 | $1,795”
  - column:Personal: 2432 ⟵ “Personal | $2,504 | $2,504 | $2,504 | $2,504 | $2,504 | $2,432”
  - column:TOTAL: 37911 ⟵ “TOTAL | $26,438 | $26,018 | $20,648 | $44,336 | $43,916 | $37,911”
### `9d331474f33d1c94` Florida State University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://tuition.fsu.edu/cost-attendance/cost-estimates-summer-2026 (sha256 b3c4dd3ea069)
- issues: ambiguous_year_labels, arrangement_unlabeled, components_do_not_reconcile, residency_unknown, conflicting_sources:https://tuition.fsu.edu/cost-attendance/cost-estimates-fall-2026-spring-2027
- checks: {"columns": 6, "components_reconcile": false, "rows": 6}
  - column:Tuition: 1509 ⟵ “Tuition | $1,293 | $1,293 | $1,509 | $1,293 | $4,630 | $4,630 | $5,402 | $4,630”
  - column:Fees: 25 ⟵ “Fees | $25 | $25 | $25 | $25 | $25 | $25 | $25 | $25”
  - column:Books ,Course Materials, Supplies, and Equipment: 300 ⟵ “Books ,Course Materials, Supplies, and Equipment | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Transportation: 360 ⟵ “Transportation | $360 | $360 | $360 | $180 | $540 | $540 | $540 | $270”
  - column:Personal: 2138 ⟵ “Personal | $1,170 | $1,170 | $2,138 | $1,170 | $1,170 | $1,170 | $2,138 | $1,170”
  - column:TOTAL: 7837 ⟵ “TOTAL | $6,653 | $6,653 | $7,837 | $4,721 | $10,170 | $10,170 | $11,910 | $8,148”
  - column:Tuition: 1293 ⟵ “Tuition | $1,293 | $1,293 | $1,509 | $1,293 | $4,630 | $4,630 | $5,402 | $4,630”
  - column:Fees: 25 ⟵ “Fees | $25 | $25 | $25 | $25 | $25 | $25 | $25 | $25”
  - column:Books ,Course Materials, Supplies, and Equipment: 300 ⟵ “Books ,Course Materials, Supplies, and Equipment | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Transportation: 180 ⟵ “Transportation | $360 | $360 | $360 | $180 | $540 | $540 | $540 | $270”
  - column:Personal: 1170 ⟵ “Personal | $1,170 | $1,170 | $2,138 | $1,170 | $1,170 | $1,170 | $2,138 | $1,170”
  - column:TOTAL: 4721 ⟵ “TOTAL | $6,653 | $6,653 | $7,837 | $4,721 | $10,170 | $10,170 | $11,910 | $8,148”
  - column:Tuition: 4630 ⟵ “Tuition | $1,293 | $1,293 | $1,509 | $1,293 | $4,630 | $4,630 | $5,402 | $4,630”
  - column:Fees: 25 ⟵ “Fees | $25 | $25 | $25 | $25 | $25 | $25 | $25 | $25”
  - column:Books ,Course Materials, Supplies, and Equipment: 300 ⟵ “Books ,Course Materials, Supplies, and Equipment | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Transportation: 540 ⟵ “Transportation | $360 | $360 | $360 | $180 | $540 | $540 | $540 | $270”
  - column:Personal: 1170 ⟵ “Personal | $1,170 | $1,170 | $2,138 | $1,170 | $1,170 | $1,170 | $2,138 | $1,170”
  - column:TOTAL: 10170 ⟵ “TOTAL | $6,653 | $6,653 | $7,837 | $4,721 | $10,170 | $10,170 | $11,910 | $8,148”
  - column:Tuition: 4630 ⟵ “Tuition | $1,293 | $1,293 | $1,509 | $1,293 | $4,630 | $4,630 | $5,402 | $4,630”
  - column:Fees: 25 ⟵ “Fees | $25 | $25 | $25 | $25 | $25 | $25 | $25 | $25”
  - column:Books ,Course Materials, Supplies, and Equipment: 300 ⟵ “Books ,Course Materials, Supplies, and Equipment | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Transportation: 540 ⟵ “Transportation | $360 | $360 | $360 | $180 | $540 | $540 | $540 | $270”
  - column:Personal: 1170 ⟵ “Personal | $1,170 | $1,170 | $2,138 | $1,170 | $1,170 | $1,170 | $2,138 | $1,170”
  - column:TOTAL: 10170 ⟵ “TOTAL | $6,653 | $6,653 | $7,837 | $4,721 | $10,170 | $10,170 | $11,910 | $8,148”
  - column:Tuition: 5402 ⟵ “Tuition | $1,293 | $1,293 | $1,509 | $1,293 | $4,630 | $4,630 | $5,402 | $4,630”
  - … 11 more rows
### `a65f6e1ed9498169` Florida State University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://tuition.fsu.edu/cost-estimates-fall-2025-spring-2026 (sha256 a16e0d7b1f4d)
- issues: components_do_not_reconcile, cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - on_campus:Tuition: 4693 ⟵ “Tuition | $4,693 | $4,693 | $4,693 | $19,152 | $19,152 | $19,152”
  - on_campus:Fees: 10 ⟵ “Fees | $10 | $10 | $10 | $10 | $10 | $10”
  - on_campus:Course Materials, Supplies, and Equipment: 1200 ⟵ “Course Materials, Supplies, and Equipment | $1,200 | $1,200 | $1,200 | $1,200 | $1,200 | $1,200”
  - on_campus:Transportation: 2460 ⟵ “Transportation | $2,460 | $2,460 | $1,230 | $3,652 | $3,652 | $1,826”
  - on_campus:Personal: 2432 ⟵ “Personal | $2,432 | $2,432 | $2,432 | $2,432 | $2,432 | $2,432”
  - on_campus:TOTAL: 24375 ⟵ “TOTAL | $24,375 | $24,375 | $19,155 | $40,026 | $40,026 | $34,210”
### `f618c45fddede16b` Florida State University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://tuition.fsu.edu/cost-attendance/cost-estimates-summer-2026 (sha256 b3c4dd3ea069)
- issues: ambiguous_year_labels, components_do_not_reconcile, conflicting_sources:https://tuition.fsu.edu/cost-attendance/cost-estimates-fall-2026-spring-2027
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - column:Tuition: 1293 ⟵ “Tuition | $1,293 | $1,293 | $1,509 | $1,293 | $4,630 | $4,630 | $5,402 | $4,630”
  - column:Fees: 25 ⟵ “Fees | $25 | $25 | $25 | $25 | $25 | $25 | $25 | $25”
  - column:Books ,Course Materials, Supplies, and Equipment: 300 ⟵ “Books ,Course Materials, Supplies, and Equipment | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Transportation: 360 ⟵ “Transportation | $360 | $360 | $360 | $180 | $540 | $540 | $540 | $270”
  - column:Personal: 1170 ⟵ “Personal | $1,170 | $1,170 | $2,138 | $1,170 | $1,170 | $1,170 | $2,138 | $1,170”
  - column:TOTAL: 6653 ⟵ “TOTAL | $6,653 | $6,653 | $7,837 | $4,721 | $10,170 | $10,170 | $11,910 | $8,148”
### `6df5c8af21abc63b` Florida State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admissions.fsu.edu/transfer/credit/ib (sha256 bb2b8d019af2)
- issues: rows_without_score
- checks: {"distinct_exams": 35, "equivalencies": 36, "rows_without_score": 36}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “BIOLOGY | BSC 1005 (3)BSC 1005L (1) | BSC 1005 (3), BSC 1005L (1)BSC 2010 (3), BSC 2010L (1) | Same as 5”
  - equivalencies[IB-BIOLOGY-SL|None]:  ⟵ “BIOLOGY (SL) | BSC 1005 (3)BSC 1005L (1) | Same as 4 | Same as 4”
  - equivalencies[IB-BIOLOGY-HL|None]:  ⟵ “BIOLOGY (HL) | BSC 1005 (3), BSC 1005L (1)BSC 2010 (3), BSC 2010L (1) | Same as 4 | Same as 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “BUSINESS AND MANAGEMENT | GEB 1011 (3) | GEB 1011 (3), GEB 1012 (3) | Same as 5”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “CHEMISTRY | CHM 1020 (3)CHM 1020L (1) | CHM 1020 (3), CHM 1020L (1)CHM 1045 (3), CHM 1045L (1) | Same as 5”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “COMPUTER SCIENCE | CGS 2100 (3) | CGS 2100 (3), CGS 2060 (3) | Same as 5”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “ECONOMICS | ECO 2000 (3) | ECO 2013 (3), ECO 2023 (3) | Same as 5”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|None]:  ⟵ “ENVIRONMENTAL SYSTEMS | GEO 1330 (3) | GEO 1330 (3), ISC 1050 (3) | Same as 5”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|None]:  ⟵ “ENVIRONMENTAL SYSTEMS & SOCIETIES (SL) | EVR 1001 (3) | Same as 4 | Same as 4”
  - equivalencies[IB-FILM|None]:  ⟵ “FILM STUDIES | FIL 2001 (3) | FIL 2001 (3), FIL 2002 (3) | Same as 5”
  - equivalencies[IB-FRENCH|None]:  ⟵ “FRENCH: LANGUAGE B | FRE 1121 (4) | FRE 1121 (4), FRE 2220 (4) | Same as 5”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “GEOGRAPHY | GEA 1000 (3) | GEO 1400 (3), GEO 2200 (3) | Same as 5”
  - equivalencies[IB-GERMAN|None]:  ⟵ “GERMAN: LANGUAGE B | GER 1121 (4) | GER 1121 (4), GER 2220 (4) | Same as 5”
  - equivalencies[IB-GLOBAL-POLITICS-SL|None]:  ⟵ “GLOBAL POLITICS (SL) | INR 2002 (3) | Same as 4 | Same as 4”
  - equivalencies[IB-GLOBAL-POLITICS-HL|None]:  ⟵ “GLOBAL POLITICS (HL) | INR 2002 (3) | INR 2002 (3), INR**** (3) | Same as 5”
  - equivalencies[IB-HISTORY|None]:  ⟵ “HISTORY | WOH 2030 (3) | WOH 2030 (3), WOH 2023 (3) | Same as 5”
  - equivalencies[IB-HISTORY-SL|None]:  ⟵ “HISTORY (SL) | WOH 2030 (3) | Same as 4 | Same as 4”
  - equivalencies[IB-HISTORY-HL|None]:  ⟵ “HISTORY (HL): HISTORY OF AFRICA & THE MIDDLE EAST | WOH 2030 (3) | WOH 2030 (3), FSU **** (3) | Same as 5”
  - equivalencies[IB-HISTORY|None]:  ⟵ “ISLAMIC HISTORY | ASH 1044 (3) | ASH 1044 (3), REL 3363 (3) | Same as 5”
  - equivalencies[IB-LATIN|None]:  ⟵ “LATIN | LAT 1121 (4) | LAT 1121 (4), LAT 2220 (4) | Same as 5”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|None]:  ⟵ “MATH ANALYSIS & APPROACHES (SL) | MAC 1105 (3) | MAC 1105 (3)MAC 1140 (3) | Same as 5”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|None]:  ⟵ “MATH ANALYSIS & APPROACHES (HL) | MAC 1105 (3) | MAC 1105 (3)MAC 2311 (4) | Same as 5”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-SL|None]:  ⟵ “MATH APPLICATIONS & INTERPRETATIONS (SL) | MAC 1105 (3) | MAC 1105 (3)MAC 1140 (3) | Same as 5”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|None]:  ⟵ “MATH APPLICATIONS & INTERPRETATIONS (HL) | MAC 1140 (3) | MAC 1140 (3)STA 2023 (3) | Same as 5”
  - equivalencies[IB-MUSIC|None]:  ⟵ “MUSIC | MUL 2010 (3) | MUL 2010 (3), MUT 1001 (3) | Same as 5”
  - … 11 more rows
### `c84c187d2e98d764` Florida State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://admissions.fsu.edu/transfer/credit/clep (sha256 de718152a8d0)
- issues: rows_without_score
- checks: {"distinct_exams": 28, "equivalencies": 28, "rows_without_score": 2}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | POS 1041 (3) | 50”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | AML 1000 (3) | 50”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|None]:  ⟵ “Analyzing & Interpreting Literature | No credit | ”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology, General | BSC 1005 (3) | 50”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business Law, Introduction to | BUL 2241 (3) | 50”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | MAC 2233 (3) | 50”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry, General | CHM 1020 (3) | 50”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition (includes essay)* | ENC 1101 (3), ENC 1102 (3) | 50”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|None]:  ⟵ “College Composition Modular (no essay) | No credit | ”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Educational Psychology, Introduction to | EDP 1002 (3) | 50”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | ENL 1000 (3) | 50”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | ACG 1001 (3) | 50”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | HUM 2235 (3) | 50”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | DEP 2004 (3) | 50”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | CGS 2060 (3) | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Principles of | ECO 2013 (3) | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Principles of | MAN 2021 (3) | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of | MAR 2011 (3) | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Principles of | ECO 2023 (3) | 50”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “PreCalculus | MAC 1140 (3) | 50”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory | PSY 2012 (3) | 50”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introductory | SYG 1000 (3) | 50”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I, to 1648 | EUH 2000 (3) | 50”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II, from 1648 | EUH 2001 (3) | 50”
  - equivalencies[CLEP-FRENCH-LANGUAGE|[50]FRE 1120 (4)]:  ⟵ “French | [50]FRE 1120 (4) | [59]FRE 1120 (4)FRE 1121 (4) | [66]FRE 1120 (4)FRE 1121 (4)FRE 2992 (4)”
  - … 3 more rows
### `5fe825a952d3e764` Gulf Coast State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gulfcoast.edu/tuition-aid/financial-aid/grants-and-scholarships/index.html (sha256 9a1c3e509c28)
- issues: semantic_review_required, conflicting_sources:https://www.gulfcoast.edu/tuition-aid/financial-aid/grants-and-scholarships/guarantee/index.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students who fail to meet renewal criteria due to illness, death in the family, or other special circumstances may submit an appeal request online.”
### `71e733e412ff4193` Gulf Coast State College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.gulfcoast.edu/tuition-aid/financial-aid/understanding-your-award.html (sha256 b9646ba66c28)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Adjustments to budgets may be considered on a case-by-case basis with appropriate documentation via Professional Judgment.”
  - sentence: professional_judgment ⟵ “Adjustments to budgets may be considered on a case-by-case basis with appropriate documentation via Professional Judgment.”
### `8a5e78a6398990f8` Gulf Coast State College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.gulfcoast.edu/tuition-aid/financial-aid/understanding-your-award.html (sha256 b9646ba66c28)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.gulfcoast.edu/tuition-aid/financial-aid/satisfactory-academic-progress.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Please note: A course that you are repeating, which has not been previously completed with a passing grade, may count towards enrollment with regard to the awarding of Title IV funds as long as you are achieving Satisfactory Academic Progress or are on an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “A course that you are repeating for the first time, after having previously completed with a passing grade once, may count towards enrollment with regard to the awarding of Title IV funds as long as you are achieving Satisfactory Academic Progress or are on an approved SAP appeal.”
### `bfd8baa2a11d0120` Gulf Coast State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gulfcoast.edu/tuition-aid/financial-aid/grants-and-scholarships/guarantee/index.html (sha256 a831d387141a)
- issues: semantic_review_required, conflicting_sources:https://www.gulfcoast.edu/tuition-aid/financial-aid/grants-and-scholarships/index.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students who fail to meet renewal criteria due to illness, death in the family, or other special circumstances may submit an appeal request.”
### `c8c1b46b2605f10f` Gulf Coast State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gulfcoast.edu/tuition-aid/financial-aid/satisfactory-academic-progress.html (sha256 032ae31b73c4)
- issues: semantic_review_required, conflicting_sources:https://www.gulfcoast.edu/tuition-aid/financial-aid/understanding-your-award.html
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: sap_appeal ⟵ “GCSC | Satisfactory Academic Progress Guidelines and Appeals Skip to Content Skip to Navigation menusearch mygcsc Home Tuition and Aid Financial Aid Satisfactory Academic Progress Satisfactory Academic Progress Imm 7.083: Satisfactory Academic Progress (SAP) PLEASE READ BEFORE COMPLETING APPEAL FORM The Higher Education Act of 1965 is a federal law that requires Gulf Coast State College (GCSC) to ”
  - sentence: sap_appeal ⟵ “FA Appeal Approved When a student in "Needs to be Reviewed" or "Financial Aid Suspension" status submits a SAP appeal and that SAP appeal is approved.”
  - sentence: sap_appeal ⟵ “Meeting Academic Plan When a student in "FA Appeal Approved" or "Meeting Academic Plan" status achieves the progress outlined in their approved SAP appeal and academic plan.”
  - sentence: sap_appeal ⟵ “FA Appeal Denied When a student submits a SAP appeal and that SAP appeal is denied.”
  - sentence: sap_appeal ⟵ “Sap Appeals A student in ‘Financial Aid Suspension’ status may submit a SAP appeal to the financial aid office.”
  - sentence: sap_appeal ⟵ “SAP appeals must be approved before the last day of class in the semester/ payment period a student is attempting to reestablish federal aid eligibility for.”
### `51ef18d502d1a85f` Gulf Coast State College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.gulfcoast.edu/tuition-aid/financial-aid/understanding-your-award.html (sha256 b9646ba66c28)
- issues: ambiguous_year_labels, components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 7065 ⟵ “Tuition | 7,065*”
  - column:Books, Materials, Supplies, & Equipment: 1200 ⟵ “Books, Materials, Supplies, & Equipment | 1,200*”
  - column:Housing Expenses: 9540 ⟵ “Housing Expenses | 9,540”
  - column:Food Expenses: 3942 ⟵ “Food Expenses | 3,942”
  - column:Transportation Expenses: 2808 ⟵ “Transportation Expenses | 2,808”
  - column:Miscellaneous Expenses: 2160 ⟵ “Miscellaneous Expenses | 2,160”
  - column:Federal Loan Fees: 54 ⟵ “Federal Loan Fees | 54**”
  - column:Total: 28339 ⟵ “Total | 28,339”
### `8ec17847710b1845` Gulf Coast State College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.gulfcoast.edu/tuition-aid/financial-aid/understanding-your-award.html (sha256 b9646ba66c28)
- issues: ambiguous_year_labels, components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 1750 ⟵ “Tuition | 1,750*”
  - column:Books, Materials, Supplies, & Equipment: 1200 ⟵ “Books, Materials, Supplies, & Equipment | 1,200*”
  - column:Housing Expenses: 9540 ⟵ “Housing Expenses | 9,540”
  - column:Food Expenses: 3942 ⟵ “Food Expenses | 3,942”
  - column:Transportation Expenses: 2808 ⟵ “Transportation Expenses | 2,808”
  - column:Miscellaneous Expenses: 2160 ⟵ “Miscellaneous Expenses | 2,160”
  - column:Federal Loan Fees: 54 ⟵ “Federal Loan Fees | 54**”
  - column:Total: 22074 ⟵ “Total | 22,074”
### `38340e4a1ecbcdd1` Herzing University-Orlando — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 78955fb15674)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
### `a8f22ed6e48e5db4` Herzing University-Orlando — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 78955fb15674)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “A student not meeting satisfactory academic progress will be required to appeal in order to change programs and may be limited on the number of allowable program changes.”
  - sentence: sap_appeal ⟵ “If mitigating or extenuating circumstances exist, a student may appeal a dismissal from the University using the SAP Appeal process above.”
### `962daad82d4331ea` Herzing University-Tampa — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 78955fb15674)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
### `e546359796186b56` Herzing University-Tampa — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 78955fb15674)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “A student not meeting satisfactory academic progress will be required to appeal in order to change programs and may be limited on the number of allowable program changes.”
  - sentence: sap_appeal ⟵ “If mitigating or extenuating circumstances exist, a student may appeal a dismissal from the University using the SAP Appeal process above.”
### `d0a6068e31dd4d1a` Indian River State College — appeals 2026-27 [new] (labeled_in_source)
- source: https://irsc.edu/admissions/financial-aid/faqs/ (sha256 28f785aaec50)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Armed Forces Are an orphan, ward of the court, or were in foster care after age 13 Are an emancipated minor or in a legal guardianship Are experiencing homelessness or are at risk of homelessness If you cannot provide parent information due to unusual circumstances (such as a severed or unsafe relationship), contact the Financial Aid Office for guidance on possible options.”
  - sentence: need_based_special_circumstances ⟵ “Answer: If unusual circumstances prevent you from providing parent information, contact the Financial Aid Office for assistance: Phone: (772) 462-7450 Email: financialaid-info@irsc.edu Walk-in: Main Campus, Building W Student Services Our staff will discuss your situation and determine if you qualify for a dependency override or other exceptions.”
### `151b20b841766337` Indian River State College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://irsc.edu/admissions/tuition-fees/estimated-costs/ (sha256 5aa84cd69cfe)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - column:Tuition and fees: 10212 ⟵ “Tuition and fees | $10,212 | $10,212 | $13,936 | $13,936”
  - column:Books and supplies: 1350 ⟵ “Books and supplies | $1,350 | $1,350 | $1,350 | $1,350”
  - column:Room and board: 4460 ⟵ “Room and board | $4,460 | $8,670 | $4,460 | $8,670”
  - column:Transportation: 3850 ⟵ “Transportation | $3,850 | $3,850 | $3,850 | $3,850”
  - column:Miscellaneous: 1420 ⟵ “Miscellaneous | $1,420 | $1,420 | $1,420 | $1,420”
  - column:Total cost: 21292 ⟵ “Total cost | $21,292 | $25,502 | $25,016 | $29,226”
  - column:Tuition and fees: 10212 ⟵ “Tuition and fees | $10,212 | $10,212 | $13,936 | $13,936”
  - column:Books and supplies: 1350 ⟵ “Books and supplies | $1,350 | $1,350 | $1,350 | $1,350”
  - column:Room and board: 8670 ⟵ “Room and board | $4,460 | $8,670 | $4,460 | $8,670”
  - column:Transportation: 3850 ⟵ “Transportation | $3,850 | $3,850 | $3,850 | $3,850”
  - column:Miscellaneous: 1420 ⟵ “Miscellaneous | $1,420 | $1,420 | $1,420 | $1,420”
  - column:Total cost: 25502 ⟵ “Total cost | $21,292 | $25,502 | $25,016 | $29,226”
  - column:Tuition and fees: 13936 ⟵ “Tuition and fees | $10,212 | $10,212 | $13,936 | $13,936”
  - column:Books and supplies: 1350 ⟵ “Books and supplies | $1,350 | $1,350 | $1,350 | $1,350”
  - column:Room and board: 4460 ⟵ “Room and board | $4,460 | $8,670 | $4,460 | $8,670”
  - column:Transportation: 3850 ⟵ “Transportation | $3,850 | $3,850 | $3,850 | $3,850”
  - column:Miscellaneous: 1420 ⟵ “Miscellaneous | $1,420 | $1,420 | $1,420 | $1,420”
  - column:Total cost: 25016 ⟵ “Total cost | $21,292 | $25,502 | $25,016 | $29,226”
  - column:Tuition and fees: 13936 ⟵ “Tuition and fees | $10,212 | $10,212 | $13,936 | $13,936”
  - column:Books and supplies: 1350 ⟵ “Books and supplies | $1,350 | $1,350 | $1,350 | $1,350”
  - column:Room and board: 8670 ⟵ “Room and board | $4,460 | $8,670 | $4,460 | $8,670”
  - column:Transportation: 3850 ⟵ “Transportation | $3,850 | $3,850 | $3,850 | $3,850”
  - column:Miscellaneous: 1420 ⟵ “Miscellaneous | $1,420 | $1,420 | $1,420 | $1,420”
  - column:Total cost: 29226 ⟵ “Total cost | $21,292 | $25,502 | $25,016 | $29,226”
### `cc7cfb91dc208a09` Indian River State College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://irsc.edu/admissions/tuition-fees/estimated-costs/ (sha256 5aa84cd69cfe)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition and fees: 2760 ⟵ “Tuition and fees | $2,760 | $2,760”
  - column:Books and supplies: 1350 ⟵ “Books and supplies | $1,350 | $1,350”
  - column:Room and board: 4460 ⟵ “Room and board | $4,460 | $8,670”
  - column:Transportation: 3850 ⟵ “Transportation | $3,850 | $3,850”
  - column:Miscellaneous: 1420 ⟵ “Miscellaneous | $1,420 | $1,420”
  - column:Total cost: 13840 ⟵ “Total cost | $13,840 | $18,050”
  - column:Tuition and fees: 2760 ⟵ “Tuition and fees | $2,760 | $2,760”
  - column:Books and supplies: 1350 ⟵ “Books and supplies | $1,350 | $1,350”
  - column:Room and board: 8670 ⟵ “Room and board | $4,460 | $8,670”
  - column:Transportation: 3850 ⟵ “Transportation | $3,850 | $3,850”
  - column:Miscellaneous: 1420 ⟵ “Miscellaneous | $1,420 | $1,420”
  - column:Total cost: 18050 ⟵ “Total cost | $13,840 | $18,050”
### `md6579e87b98d595` Indian River State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://irsc.edu/wp-content/uploads/2025/10/DE-Agreement-Okeechobee-25-27-Final-003.pdf (sha256 610cb72d08ee)
- issues: ambiguous_year_labels
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 8, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Any student who has an unweighted high school GPA of 3.0 and achieves a grade of “B” or better in any of the full credit (1 credit) courses  listed below shall have demonstrated readiness for college-level work.”
  - eligibility_tier: 3.0 ⟵ “Any student who has an unweighted high school GPA of 3.0 and achieves a grade of “B” or better in two half credit (0.5 credit) courses with the same name and listed below shall have demonstrated readiness for college-level work.  Any grades that are not “B” or better will not demonstrate readiness f”
  - eligibility_tier: 3.0 ⟵ “4. Students must have a minimum of a 3.0 unweighted GPA.”
  - per_credit_hour_charge: 71.98 ⟵ “1009.23) is $71.98 per credit hour or $2.33 per vocational clock hour. Online dual”
  - eligibility_tier: 3.0 ⟵ “4. Students must have a minimum of a 3.0 unweighted GPA.”
  - per_credit_hour_charge: 71.98 ⟵ “1009.23) is $71.98 per credit hour or $2.33 per vocational clock hour. Online dual”
  - eligibility_tier: 3.0 ⟵ “4. Students must have a minimum of a 3.0 unweighted GPA.”
  - per_credit_hour_charge: 71.98 ⟵ “1009.23) is $71.98 per credit hour or $2.33 per vocational clock hour. Online dual”
  - eligibility_tier: 3.0 ⟵ “4. Students must have a minimum of a 3.0 unweighted GPA.”
  - per_credit_hour_charge: 71.98 ⟵ “1009.23) is $71.98 per credit hour or $2.33 per vocational clock hour. Online dual”
  - eligibility_tier: 3.0 ⟵ “4. Students must have a minimum of a 3.0 unweighted GPA.”
  - per_credit_hour_charge: 71.98 ⟵ “1009.23) is $71.98 per credit hour or $2.33 per vocational clock hour. Online dual”
  - college_gpa_to_continue: 2.0 ⟵ “student must maintain a college 2.0 cumulative GPA for continuous dual enrollment participation. I am aware that a second attempt requires”
  - eligibility_tier: 3.0 ⟵ “Student has a minimum high school unweighted GPA of 3.0 to enroll in any college credit course or 2.0 for vocational clock”
### `dea81660c128887f` Jacksonville University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ju.edu/financialservices/tuition/adult-archive-2025-2026.php (sha256 44b67181a1a5)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Tuition (Full Program Cost): 70000 ⟵ “Tuition (Full Program Cost) | $70,000”
  - column:Subscription Fee (One-time fee): 2000 ⟵ “Subscription Fee (One-time fee) | $2,000”
### `056b680367c9750d` Johnson University Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://johnsonu.edu/admissions/financial-aid/financial-aid-faqs/ (sha256 8b604a91e43f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You may have a special circumstance and will need to contact the financial aid director with a detailed explanation of your circumstance.”
### `77b0f93426297a3f` Johnson University Florida — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://johnsonu.edu/admissions/tuition/ (sha256 569078a7e6ce)
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
### `749076cd5ca0387c` Lake-Sumter State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lssc.edu/financial-aid/policies/satisfactory-academic-progress/ (sha256 6145998d3704)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appealing a Suspension Students may submit an SAP appeal for consideration of reinstatement of Federal Financial Aid eligibility.”
### `46659ca93128eeac` Lake-Sumter State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lssc.edu/financial-aid/cost-of-attendance/ (sha256 a4251c414bfb)
- issues: residency_unknown
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition*: 3292 ⟵ “Tuition* | $3,292 | $13,276 | $3,292 | $13,276”
  - off_campus_not_with_family:Books: 1800 ⟵ “Books | $1,800 | $1,800 | $1,800 | $1,800”
  - off_campus_not_with_family:Housing/Food: 12672 ⟵ “Housing/Food | $12,672 | $12,672 | $4,032 | $4,032”
  - off_campus_not_with_family:Personal/Misc.: 2375 ⟵ “Personal/Misc. | $2,375 | $2,375 | $2,375 | $2,375”
  - off_campus_not_with_family:Transportation: 2610 ⟵ “Transportation | $2,610 | $2,610 | $2,610 | $2,610”
  - off_campus_not_with_family:Total: 22749 ⟵ “Total | $22,749 | $32,733 | $14,019 | $24,093”
  - off_campus_not_with_family:Tuition*: 13276 ⟵ “Tuition* | $3,292 | $13,276 | $3,292 | $13,276”
  - off_campus_not_with_family:Books: 1800 ⟵ “Books | $1,800 | $1,800 | $1,800 | $1,800”
  - off_campus_not_with_family:Housing/Food: 12672 ⟵ “Housing/Food | $12,672 | $12,672 | $4,032 | $4,032”
  - off_campus_not_with_family:Personal/Misc.: 2375 ⟵ “Personal/Misc. | $2,375 | $2,375 | $2,375 | $2,375”
  - off_campus_not_with_family:Transportation: 2610 ⟵ “Transportation | $2,610 | $2,610 | $2,610 | $2,610”
  - off_campus_not_with_family:Total: 32733 ⟵ “Total | $22,749 | $32,733 | $14,019 | $24,093”
  - with_parents_or_family:Tuition*: 3292 ⟵ “Tuition* | $3,292 | $13,276 | $3,292 | $13,276”
  - with_parents_or_family:Books: 1800 ⟵ “Books | $1,800 | $1,800 | $1,800 | $1,800”
  - with_parents_or_family:Housing/Food: 4032 ⟵ “Housing/Food | $12,672 | $12,672 | $4,032 | $4,032”
  - with_parents_or_family:Personal/Misc.: 2375 ⟵ “Personal/Misc. | $2,375 | $2,375 | $2,375 | $2,375”
  - with_parents_or_family:Transportation: 2610 ⟵ “Transportation | $2,610 | $2,610 | $2,610 | $2,610”
  - with_parents_or_family:Total: 14019 ⟵ “Total | $22,749 | $32,733 | $14,019 | $24,093”
  - with_parents_or_family:Tuition*: 13276 ⟵ “Tuition* | $3,292 | $13,276 | $3,292 | $13,276”
  - with_parents_or_family:Books: 1800 ⟵ “Books | $1,800 | $1,800 | $1,800 | $1,800”
  - with_parents_or_family:Housing/Food: 4032 ⟵ “Housing/Food | $12,672 | $12,672 | $4,032 | $4,032”
  - with_parents_or_family:Personal/Misc.: 2375 ⟵ “Personal/Misc. | $2,375 | $2,375 | $2,375 | $2,375”
  - with_parents_or_family:Transportation: 2610 ⟵ “Transportation | $2,610 | $2,610 | $2,610 | $2,610”
  - with_parents_or_family:Total: 24093 ⟵ “Total | $22,749 | $32,733 | $14,019 | $24,093”
### `48d0f520f828c195` Lake-Sumter State College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lssc.edu/financial-aid/cost-of-attendance/ (sha256 f4ea22d41571)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition*: 3292 ⟵ “Tuition* | $3,292 | $13,276 | $3,292 | $13,276”
  - off_campus_not_with_family:Books: 1800 ⟵ “Books | $1,800 | $1,800 | $1,800 | $1,800”
  - off_campus_not_with_family:Housing/Food: 12672 ⟵ “Housing/Food | $12,672 | $12,672 | $4,032 | $4,032”
  - off_campus_not_with_family:Personal/Misc.: 2375 ⟵ “Personal/Misc. | $2,375 | $2,375 | $2,375 | $2,375”
  - off_campus_not_with_family:Transportation: 2520 ⟵ “Transportation | $2,520 | $2,520 | $2,520 | $2,520”
  - off_campus_not_with_family:Total: 22659 ⟵ “Total | $22,659 | $32,643 | $14,019 | $24,003”
  - off_campus_not_with_family:Tuition*: 13276 ⟵ “Tuition* | $3,292 | $13,276 | $3,292 | $13,276”
  - off_campus_not_with_family:Books: 1800 ⟵ “Books | $1,800 | $1,800 | $1,800 | $1,800”
  - off_campus_not_with_family:Housing/Food: 12672 ⟵ “Housing/Food | $12,672 | $12,672 | $4,032 | $4,032”
  - off_campus_not_with_family:Personal/Misc.: 2375 ⟵ “Personal/Misc. | $2,375 | $2,375 | $2,375 | $2,375”
  - off_campus_not_with_family:Transportation: 2520 ⟵ “Transportation | $2,520 | $2,520 | $2,520 | $2,520”
  - off_campus_not_with_family:Total: 32643 ⟵ “Total | $22,659 | $32,643 | $14,019 | $24,003”
  - with_parents_or_family:Tuition*: 3292 ⟵ “Tuition* | $3,292 | $13,276 | $3,292 | $13,276”
  - with_parents_or_family:Books: 1800 ⟵ “Books | $1,800 | $1,800 | $1,800 | $1,800”
  - with_parents_or_family:Housing/Food: 4032 ⟵ “Housing/Food | $12,672 | $12,672 | $4,032 | $4,032”
  - with_parents_or_family:Personal/Misc.: 2375 ⟵ “Personal/Misc. | $2,375 | $2,375 | $2,375 | $2,375”
  - with_parents_or_family:Transportation: 2520 ⟵ “Transportation | $2,520 | $2,520 | $2,520 | $2,520”
  - with_parents_or_family:Total: 14019 ⟵ “Total | $22,659 | $32,643 | $14,019 | $24,003”
  - with_parents_or_family:Tuition*: 13276 ⟵ “Tuition* | $3,292 | $13,276 | $3,292 | $13,276”
  - with_parents_or_family:Books: 1800 ⟵ “Books | $1,800 | $1,800 | $1,800 | $1,800”
  - with_parents_or_family:Housing/Food: 4032 ⟵ “Housing/Food | $12,672 | $12,672 | $4,032 | $4,032”
  - with_parents_or_family:Personal/Misc.: 2375 ⟵ “Personal/Misc. | $2,375 | $2,375 | $2,375 | $2,375”
  - with_parents_or_family:Transportation: 2520 ⟵ “Transportation | $2,520 | $2,520 | $2,520 | $2,520”
  - with_parents_or_family:Total: 24003 ⟵ “Total | $22,659 | $32,643 | $14,019 | $24,003”
### `89ac6ee4526dbe78` Miami Dade College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mdc.edu/financialaid/how-aid-works/sap-policy.aspx (sha256 0c2a75520a09)
- issues: semantic_review_required, conflicting_sources:https://www.mdc.edu/financialaid/how-aid-works/sap-appeal.aspx,https://www.mdc.edu/financialaid/how-aid-works/transfer-students.aspx
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “You may regain aid via a SAP appeal approval.”
  - sentence: sap_appeal ⟵ “How can I submit a SAP Appeal?”
  - sentence: sap_appeal ⟵ “Can a SAP appeal approval be applied to previous terms?”
  - sentence: sap_appeal ⟵ “My SAP appeal was approved, what's next?”
  - sentence: sap_appeal ⟵ “Additional Information Cost of Attendance and Awards Get an estimate of attendance costs at MDC Get an estimate of your financial aid award Satisfactory Academic Progress Standards of Academic Progress Policy Standards of Academic Progress Appeal Guide Consumer Information Access consumer-related resources SingleStop Single Stop offers students a wide array of services including benefits screening”
### `99b552db77c4f51e` Miami Dade College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mdc.edu/financialaid/how-aid-works/transfer-students.aspx (sha256 53fafc9f29c2)
- issues: semantic_review_required, conflicting_sources:https://www.mdc.edu/financialaid/how-aid-works/sap-appeal.aspx,https://www.mdc.edu/financialaid/how-aid-works/sap-policy.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Additional Information Cost of Attendance and Awards Get an estimate of attendance costs at MDC Get an estimate of your financial aid award Satisfactory Academic Progress Standards of Academic Progress Policy Standards of Academic Progress Appeal Guide Consumer Information Access consumer-related resources SingleStop Single Stop offers students a wide array of services including benefits screening”
### `c7cc16bc587beb68` Miami Dade College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mdc.edu/financialaid/how-aid-works/sap-appeal.aspx (sha256 63d073901800)
- issues: semantic_review_required, conflicting_sources:https://www.mdc.edu/financialaid/how-aid-works/sap-policy.aspx,https://www.mdc.edu/financialaid/how-aid-works/transfer-students.aspx
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Important Information Submitting a SAP appeal does not guarantee approval.”
  - sentence: sap_appeal ⟵ “Additional Information Cost of Attendance and Awards Get an estimate of attendance costs at MDC Get an estimate of your financial aid award Satisfactory Academic Progress Standards of Academic Progress Policy Standards of Academic Progress Appeal Guide Consumer Information Access consumer-related resources SingleStop Single Stop offers students a wide array of services including benefits screening”
### `03d0051a754074b1` Miami Dade College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://online.mdc.edu/tuition/tuition-and-costs/ (sha256 9b5b2d3604be)
- issues: implausible_amount, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 7}
  - on_campus:Tuition: 82.78 ⟵ “Tuition | $82.78”
  - on_campus:Student Services: 8.28 ⟵ “Student Services | $8.28”
  - on_campus:Financial Aid: 4.14 ⟵ “Financial Aid | $4.14”
  - on_campus:Capital Improvement: 15.88 ⟵ “Capital Improvement | $15.88”
  - on_campus:Technology: 4.14 ⟵ “Technology | $4.14”
  - on_campus:Distance Learning Fee: 15.0 ⟵ “Distance Learning Fee | $15.00”
  - on_campus:Cost per Term (12 credits): 1598.64 ⟵ “Cost per Term (12 credits) | $1,598.64”
### `7faa4a43af9b8d9b` Miami Dade College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://online.mdc.edu/tuition/tuition-and-costs/ (sha256 9b5b2d3604be)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 6}
  - on_campus:Tuition: 331.11 ⟵ “Tuition | $331.11”
  - on_campus:Student Services: 8.28 ⟵ “Student Services | $8.28”
  - on_campus:Financial Aid: 16.56 ⟵ “Financial Aid | $16.56”
  - on_campus:Capital Improvement: 27.0 ⟵ “Capital Improvement | $27.00”
  - on_campus:Technology: 16.56 ⟵ “Technology | $16.56”
  - on_campus:Cost per Term (12 credits): 4794.12 ⟵ “Cost per Term (12 credits) | $4,794.12”
### `16ebfc1b4b1406ec` New College of Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ncf.edu/admissions/tuition-fee-info/ (sha256 10ca033e68ac)
- issues: semantic_review_required, conflicting_sources:https://www.ncf.edu/admissions/financial-aid/resources/,https://www.ncf.edu/wp-content/uploads/2025/10/Undergrad-SAP-Policy-updated-10.25.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Learn more about grandparent waiver and apply Tuition Waivers or Exemptions There are special circumstances where students may qualify for a tuition exemption or waiver.”
### `521d4e5790d01e0e` New College of Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ncf.edu/admissions/financial-aid/resources/ (sha256 84d175bd11f0)
- issues: semantic_review_required, conflicting_sources:https://www.ncf.edu/admissions/tuition-fee-info/,https://www.ncf.edu/wp-content/uploads/2025/10/Undergrad-SAP-Policy-updated-10.25.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances that may be considered include: change in employment status, income or assets; change in housing status (e.g. homelessness); medical, dental, or nursing home expenses not covered by insurance; child or dependent care expenses; death of a parent; and divorce or separation of a parent.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances that may be considered include: human trafficking; legally granted refugee or asylum status; parental abandonment or estrangement; or student or parental incarceration.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances do NOT include parents refusing to contribute to the student’s education; parents who will not provide information for the FAFSA or verification; parents who do not claim the student as a dependent for income tax purposes; or students who demonstrate total self-sufficiency.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance AND an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Documentation of the special or unusual circumstances are required.”
### `a166f511567cc7bf` New College of Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ncf.edu/admissions/financial-aid/resources/ (sha256 84d175bd11f0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “Service Members, and Their Families How To Keep Your Aid (For Students) How To Help Your Student Keep Financial Aid (for Parents and Family) Policies Satisfactory Academic Progress Policy for Financial Aid Purposes Satisfactory Academic Progress for Graduate Students Forms Academic Performance Petition Form Financial Aid Verification and Forms Professional Judgements Due to Special or Unusual Circ”
  - sentence: professional_judgment ⟵ “Professional judgement determinations are made on a case by case basis by financial aid staff and are only valid for the current academic year.”
  - sentence: professional_judgment ⟵ “The Department of Education distinguishes between 2 different categories of professional judgements: Professional Judgements due to Special Circumstances: Special Circumstances refer to the financial situations that justify an aid administrator adjusting data elements in the Cost of Attendance or in the SAI calculation.”
  - sentence: professional_judgment ⟵ “All students requesting a professional judgement due to special circumstances, as defined above, must first complete verification.”
  - sentence: professional_judgment ⟵ “Professional Judgements due to Unusual Circumstances: Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation, more commonly referred to as a dependency override.”
  - sentence: professional_judgment ⟵ “To request a professional judgement, please contact the financial aid office at [email protected].”
### `a3ddf4e88c30976c` New College of Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ncf.edu/wp-content/uploads/2025/10/Undergrad-SAP-Policy-updated-10.25.pdf (sha256 f5986a54ff30)
- issues: semantic_review_required, conflicting_sources:https://www.ncf.edu/admissions/financial-aid/resources/,https://www.ncf.edu/admissions/tuition-fee-info/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “The Office of Financial Aid will notify the student of any change in financial aid status through the student’s Self Service Student tile once SAP has been reviewed after the end of the term.”
  - sentence: need_based_special_circumstances ⟵ “The appeal must be written by the student, and include the following: ● Why the student failed to meet the SAP requirements (information on the death of a relative, injury or illness of the student, or other special circumstances and information). ● How and when the student reached out for help. ● What has changed in the student’s situation that will allow the student to meet the SAP requirements.”
### `10620bcd6a7bf17b` North Florida College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nfc.edu:443/admissions/registration (sha256 69943ba5595d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCES Students with the following circumstances must register with assistance from an advisor.”
### `4fd694b9cbb73f5b` North Florida College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.nfc.edu:443/admissions/paying-for-college/ (sha256 8223366a6a20)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "rows": 4}
  - column:Tuition and Fees (30 Credits): 3084 ⟵ “Tuition and Fees (30 Credits) | $3,084 | $12,018”
  - column:Books and Supplies: 1400 ⟵ “Books and Supplies | $1,400 | $1,400”
  - column:Personal Expenses: 1100 ⟵ “Personal Expenses | $1,100 | $1,100”
  - column:Transportation: 1800 ⟵ “Transportation | $1,800 | $1,800”
### `c1875e9089cde400` North Florida College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.nfc.edu:443/admissions/paying-for-college/ (sha256 8223366a6a20)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "rows": 4}
  - column:Tuition and Fees (30 Credits): 12018 ⟵ “Tuition and Fees (30 Credits) | $3,084 | $12,018”
  - column:Books and Supplies: 1400 ⟵ “Books and Supplies | $1,400 | $1,400”
  - column:Personal Expenses: 1100 ⟵ “Personal Expenses | $1,100 | $1,100”
  - column:Transportation: 1800 ⟵ “Transportation | $1,800 | $1,800”
### `f3b17a1ad66a55df` Northwest Florida State College — transfer_policies 2021-22 [new] (labeled_in_source)
- source: https://catalog.nwfsc.edu/degree-information/aa (sha256 cb98c860afb1)
- issues: stale_year_label:2021-22
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Meet the College-Level Communications and Computation Skills minimum grade and writing requirements: Attain a grade of “C” or higher in ENC 1101, ENC 1102, and two courses designated as writing-focused courses, whether credits in such courses are earned at NWFSC or transferred for credit from other institutions.”
  - min_grade: C ⟵ “Attain a grade of “C” or higher in each College-Level Communications and Computation Skills Mathematics course (any course from the Mathematics category that is used to meet A.A. general education requirements), whether credits in such courses are earned at NWFSC or transferred for credit from other institutions.”
### `34bea31d0ca16c15` Nova Southeastern University — appeals 2026-27 [new] (labeled_in_title)
- source: https://nova.edu/financial-aid/apply-for-aid/2627terms.html (sha256 4b68b711ce45)
- issues: semantic_review_required, conflicting_sources:https://www.nova.edu/financial-aid/index.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Holds Special Circumstances Withdrawing from the University Refund and Repayment Policy Financial aid recipients who withdraw from NSU for any reason must notify the Office of Financial Aid.”
### `4321b7aff6bc88ae` Nova Southeastern University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.nova.edu/financial-aid/index.html (sha256 817a8a57f3a1)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://nova.edu/financial-aid/apply-for-aid/2627terms.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Aid Learn About Federal Aid State Aid View Florida Aid Programs Scholarships Search Scholarships Grants See Grant Options Loans Compare Loan Options Veterans Benefits Access Veteran Benefits Employer Tuition Assistance See If You’re Eligible Student Employment and Assistantships Discover Assistantships Tools and Resources Forms and Documents Find verification forms, appeals, special circum”
### `8c0b6fc98ff606dc` Nova Southeastern University — appeals 2026-27 [new] (labeled_in_title)
- source: https://nova.edu/financial-aid/apply-for-aid/2627terms.html (sha256 4b68b711ce45)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Verification Significant Change in Income/Expenses (Professional Judgment) The Office of Financial Aid may use Professional Judgment (PJ) to consider special and/or unusual circumstances to make adjustments to (1) certain components of the Student Aid Index (SAI), (2) the Cost of Attendance (COA) budget, and/or (3) a student's dependency status, as determined by federal financial aid guidelines.”
  - sentence: professional_judgment ⟵ “For more information on Professional Judgment (PJ), including instructions on how to submit a request, students should click the link below.”
  - sentence: professional_judgment ⟵ “Professional Judgment Request Form Repeating Courses You can only receive Title IV financial aid once for a course you already passed.”
### `93445354079636f8` Nova Southeastern University — appeals 2026-27 [new] (source_unlabeled)
- source: https://nova.edu/financial-aid/eligibility/satisfactory-academic-progress.html (sha256 fa5964d076ef)
- issues: semantic_review_required, conflicting_sources:https://nova.edu/financial-aid/eligibility/sap-academic-plan.html,https://nova.edu/financial-aid/eligibility/sap-faq.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP Appeal A student with extenuating circumstances may appeal the denial of student financial assistance by submitting a SAP Appeal Form within 60 days from the date the failure notice was sent.”
  - sentence: sap_appeal ⟵ “Learn More About SAP Appeals and Academic Plans Have a Question?”
### `9ea6a8522d57a43e` Nova Southeastern University — appeals 2026-27 [new] (source_unlabeled)
- source: https://nova.edu/financial-aid/eligibility/sap-faq.html (sha256 9d2ab89b613f)
- issues: semantic_review_required, conflicting_sources:https://nova.edu/financial-aid/eligibility/sap-academic-plan.html,https://nova.edu/financial-aid/eligibility/satisfactory-academic-progress.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If you have experienced extenuating circumstances beyond your control, you may appeal the denial of student financial aid by submitting a completed SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “For more information on the SAP Appeal process, visit the SAP Appeal and Academic Plan.”
### `aa9f7a458eb773c3` Nova Southeastern University — appeals 2026-27 [new] (source_unlabeled)
- source: https://nova.edu/financial-aid/eligibility/sap-academic-plan.html (sha256 945118170b7b)
- issues: semantic_review_required, conflicting_sources:https://nova.edu/financial-aid/eligibility/sap-faq.html,https://nova.edu/financial-aid/eligibility/satisfactory-academic-progress.html
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: sap_appeal ⟵ “SAP Appeals and Academic Plans | NSU Financial Aid Office | Nova Southeastern University Office of Financial Aid QUICK LINKS Canvas SharkLink Abraham S.”
  - sentence: sap_appeal ⟵ “Wayne Huizenga College of Business and Entrepreneurship Halmos College of Arts and Sciences Ron and Kathy Assaf College of Nursing Shepard Broad College of Law Undergraduate Admissions University School Give Request Info Apply Now Back to NSU Home Financial Aid Eligibility SAP Appeals and Academic Plans SAP Appeals and Academic Plans If you have failed to make Satisfactory Academic Progress (SAP) ”
  - sentence: sap_appeal ⟵ “The appeal must be made in writing, addressed to the Satisfactory Academic Progress Committee in care of the Office of Student Financial Assistance, and include the following documentation: Completed Satisfactory Academic Progress (SAP) Appeal Form describing why you have failed SAP and what has changed that will allow you to successfully meet SAP in the future A physician's note if your appeal is”
  - sentence: sap_appeal ⟵ “If you are able to meet SAP within one semester or your SAP failure was based on the quantitative measure (annual credits) alone, an academic plan is not needed and you may submit your SAP Appeal Form without the academic plan portion.”
  - sentence: sap_appeal ⟵ “Resources for Academic Advisers DocuSign Process Upon accessing the SAP Appeal Form, you will be prompted to enter your name and email address.”
  - sentence: sap_appeal ⟵ “You must finish the process for your SAP Appeal Form and Academic Plan to be submitted to the Office of Student Financial Assistance.”
### `1a7b460de1a5250b` Palm Beach State College — costs 2023-24 · residency=in_state [same] (labeled_in_source)
- source: https://www.palmbeachstate.edu/collegeaffordability/ (sha256 2a24019e5b31)
- issues: arrangement_unlabeled, stale_year_label:2023-24
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition / Fees: 4638 ⟵ “Tuition / Fees | $4,638 | $4,638”
  - column:Books, Course Materials, Supplies, Equipment: 2700 ⟵ “Books, Course Materials, Supplies, Equipment | $2,700 | $2,700”
  - column:Transportation: 5400 ⟵ “Transportation | $5,400 | $5,400”
  - column:Miscellaneous Personal Expenses: 1755 ⟵ “Miscellaneous Personal Expenses | $1,755 | $1,755”
  - column:Living Expenses: 9450 ⟵ “Living Expenses | $9,450 | $12,825”
  - column:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | $56 | $56”
  - column:Total: 23999 ⟵ “Total | $23,999 | $27,374”
  - column:Tuition / Fees: 4638 ⟵ “Tuition / Fees | $4,638 | $4,638”
  - column:Books, Course Materials, Supplies, Equipment: 2700 ⟵ “Books, Course Materials, Supplies, Equipment | $2,700 | $2,700”
  - column:Transportation: 5400 ⟵ “Transportation | $5,400 | $5,400”
  - column:Miscellaneous Personal Expenses: 1755 ⟵ “Miscellaneous Personal Expenses | $1,755 | $1,755”
  - column:Living Expenses: 12825 ⟵ “Living Expenses | $9,450 | $12,825”
  - column:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | $56 | $56”
  - column:Total: 27374 ⟵ “Total | $23,999 | $27,374”
### `2d89a9981481d862` Pasco-Hernando State College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://financial-aid.phsc.edu/important-information/cost-attendance (sha256 0866b06f3bc6)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 11230 ⟵ “Tuition and Fees | $2,945 | $11,230”
  - column:Transportation: 2124 ⟵ “Transportation | $2,124 | $2,124”
  - column:Housing and Meals: 18729 ⟵ “Housing and Meals | $18,792 | $18,729”
  - column:Books: 1540 ⟵ “Books | $1,540 | $1,540”
  - column:Miscellaneous: 2394 ⟵ “Miscellaneous | $2,394 | $2,394”
  - column:Total: 36017 ⟵ “Total | $27,732 | $36,017”
### `a6b8a8b3dd857027` Pasco-Hernando State College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://financial-aid.phsc.edu/important-information/cost-attendance (sha256 0866b06f3bc6)
- issues: components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - column:Tuition and Fees: 2945 ⟵ “Tuition and Fees | $2,945 | $11,230”
  - column:Transportation: 2124 ⟵ “Transportation | $2,124 | $2,124”
  - column:Housing and Meals: 18792 ⟵ “Housing and Meals | $18,792 | $18,729”
  - column:Books: 1540 ⟵ “Books | $1,540 | $1,540”
  - column:Miscellaneous: 2394 ⟵ “Miscellaneous | $2,394 | $2,394”
  - column:Total: 27732 ⟵ “Total | $27,732 | $36,017”
### `44a00156e6c650dc` Pasco-Hernando State College — credit_policies 2021-22 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://accelerated.phsc.edu/sites/default/files/documents/2026-2027-private-school-de-articulation-agreement.pdf (sha256 02a648814cad)
- issues: stale_year_label:2021-22
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa"], "tiers": 2}
  - max_credit_hours_per_term: 16 ⟵ “Based on test scores and course placement, students may be eligible for a maximum of 16 credit hours in fall and”
  - eligibility_tier: 2.0 ⟵ “academic standing, which is defined as a 2.0 cumulative grade point average (GPA) for all hours attempted at”
  - eligibility_tier: 2.0 ⟵ “participating in the dual enrollment program with PHSC. Any requests for exceptions to the 2.0 GPA requirement”
### `m882625c2d18afe2` Pasco-Hernando State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://accelerated.phsc.edu/transfer/famu (sha256 394b6416f327)
- issues: ambiguous_year_labels
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 8, "tiers": 2}
  - max_credit_hours_per_term: 8 ⟵ “Students must be enrolled full time – in a minimum of 12 credits (maximum of 16) in fall and spring semesters. A maximum of 8 credit hours may be taken in the summer between 11th and 12th grades.”
  - eligibility_tier: 2.0 ⟵ “the 2.0 GPA requirement for each semester will require a written letter from the student and”
  - eligibility_tier: 2.0 ⟵ “3.0 unweighted high school GPA for college credit courses or 2.0 unweighted GPA for technical credit courses.”
  - max_credit_hours_per_term: 8 ⟵ “hours in fall and spring semesters. Students may take up to 8 credit hours through”
  - college_gpa_to_continue: 2.0 ⟵ “will be included. Those students who do not maintain a 2.0 cumulative college GPA in all”
  - eligibility_tier: 3.0 ⟵ “The FAMU Ignite ID card is available to new IGNITE students with a collegiate grade point average of 3.0 or higher (4.0 scale).  The card grants FREE access to most FAMU athletic and on-campus events.  In order to receive the FAMU Ignite ID card, interested students must meet the following requireme”
  - eligibility_tier: 3.0 ⟵ “Students must have at least a 3.0 GPA”
  - eligibility_tier: 2.5 ⟵ “Students with a 2.50 - 2.74 GPA are eligible for $1,000/year for 2 years (4 semesters).”
  - eligibility_tier: 2.75 ⟵ “Students with a 2.75 - 2.99 GPA are eligible for $2,000/year for 2 years (4 semesters).”
  - eligibility_tier: 3.0 ⟵ “Students with a 3.00 - 3.49 GPA are eligible for $3,000/year for 2 years (4 semesters).”
  - eligibility_tier: 3.5 ⟵ “Students with a 3.50 or higher GPA are eligible for $4,000/year for 2 years (4 semesters).”
  - eligibility_tier: 2.5 ⟵ “2.5 or higher GPA”
### `40968a7cc0e07824` Pensacola State College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://financialaid.pensacolastate.edu/alabama-residents-tuition-rates/ (sha256 b1707c6d5d06)
- issues: arrangement_unlabeled, conflicting_sources:https://financialaid.pensacolastate.edu/in-state-resident-rates/,https://financialaid.pensacolastate.edu/non-florida-residents-tuition-rates/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 2980 ⟵ “Tuition and Fees | $2,980 | $2,980”
  - column:Books and Supplies: 1800 ⟵ “Books and Supplies | $1,800 | $1,800”
  - column:Living Expenses: 10226 ⟵ “Living Expenses | $10,226 | $17,556”
  - column:Transportation: 2246 ⟵ “Transportation | $2,246 | $2,246”
  - column:Miscellaneous: 1500 ⟵ “Miscellaneous | $1,500 | $1,500”
  - column:Total: 18752 ⟵ “Total | $18,752 | $26,082”
  - column:Tuition and Fees: 2980 ⟵ “Tuition and Fees | $2,980 | $2,980”
  - column:Books and Supplies: 1800 ⟵ “Books and Supplies | $1,800 | $1,800”
  - column:Living Expenses: 17556 ⟵ “Living Expenses | $10,226 | $17,556”
  - column:Transportation: 2246 ⟵ “Transportation | $2,246 | $2,246”
  - column:Miscellaneous: 1500 ⟵ “Miscellaneous | $1,500 | $1,500”
  - column:Total: 26082 ⟵ “Total | $18,752 | $26,082”
### `5809fd3622778f84` Pensacola State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://pensacolastate.edu/docs/finAid/2026/FinancialAid_NineMonthCoABudget_20260512_v2_Active_ADA_Student.pdf (sha256 60fb944e4f65)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, conflicting_sources:https://pensacolastate.edu/docs/finAid/2026/FinancialAid_CoAClockHours_20260512_v2_Active_ADA_Student.pdf
- checks: {"columns": 2, "rows": 36}
  - column:Tuition and fees: 2720 ⟵ “Tuition and fees | *$ 2,720 | *$ 3,144”
  - column:Books and supplies: 1800 ⟵ “Books and supplies | 1,800 | 1,800”
  - column:Living expenses: 17556 ⟵ “Living expenses | 17,556 | 17,556”
  - column:Transportation: 2246 ⟵ “Transportation | 2,246 | 2,246”
  - column:Miscellaneous: 1500 ⟵ “Miscellaneous | 1,500 | 1,500”
  - column:Total: 25822 ⟵ “Total | $ 25,822 | $26,246”
  - column:Tuition and fees (2): 2572 ⟵ “Tuition and fees | *$ 2,572”
  - column:Books and supplies (2): 1800 ⟵ “Books and supplies | 1,800”
  - column:Living expenses (2): 17556 ⟵ “Living expenses | 17,556”
  - column:Transportation (2): 2246 ⟵ “Transportation | 2,246”
  - column:Miscellaneous (2): 1500 ⟵ “Miscellaneous | 1,500”
  - column:Total (2): 25674 ⟵ “Total | $25,674”
  - column:Tuition and fees (3): 2980 ⟵ “Tuition and fees | *$ 2,980 | *$ 3,404”
  - column:Books and supplies (3): 1800 ⟵ “Books and supplies | 1,800”
  - column:Living expenses (3): 17556 ⟵ “Living expenses | 17,556 | 17,556”
  - column:Transportation (3): 2246 ⟵ “Transportation | 2,246 | 2,246”
  - column:Miscellaneous (3): 1500 ⟵ “Miscellaneous | 1,500 | 1,500”
  - column:Total (3): 26082 ⟵ “Total | $ 26,082 | $ 26,506”
  - column:Tuition and fees (4): 2872 ⟵ “Tuition and fees | *$ 2,872”
  - column:Books and supplies (4): 1800 ⟵ “Books and supplies | 1,800”
  - column:Living expenses (4): 17556 ⟵ “Living expenses | 17,556”
  - column:Transportation (4): 2246 ⟵ “Transportation | 2,246”
  - column:Miscellaneous (4): 1500 ⟵ “Miscellaneous | 1,500”
  - column:Total (4): 25974 ⟵ “Total | $25,974”
  - column:Tuition and fees (5): 10914 ⟵ “Tuition and fees | *$ 10,914 | *$ 12,650”
  - … 28 more rows
### `61fce57f15653dfa` Pensacola State College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://financialaid.pensacolastate.edu/in-state-resident-rates/ (sha256 94aafeb6f23e)
- issues: arrangement_unlabeled, conflicting_sources:https://financialaid.pensacolastate.edu/alabama-residents-tuition-rates/,https://financialaid.pensacolastate.edu/non-florida-residents-tuition-rates/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 2720 ⟵ “Tuition and Fees | $2,720 | $2,720”
  - column:Books and Supplies: 1800 ⟵ “Books and Supplies | $1,800 | $1,800”
  - column:Living Expenses: 10226 ⟵ “Living Expenses | $10,226 | $17,556”
  - column:Transportation: 2246 ⟵ “Transportation | $2,246 | $2,246”
  - column:Miscellaneous: 1500 ⟵ “Miscellaneous | $1,500 | $1,500”
  - column:Total: 18492 ⟵ “Total | $18,492 | $25,822”
  - column:Tuition and Fees: 2720 ⟵ “Tuition and Fees | $2,720 | $2,720”
  - column:Books and Supplies: 1800 ⟵ “Books and Supplies | $1,800 | $1,800”
  - column:Living Expenses: 17556 ⟵ “Living Expenses | $10,226 | $17,556”
  - column:Transportation: 2246 ⟵ “Transportation | $2,246 | $2,246”
  - column:Miscellaneous: 1500 ⟵ “Miscellaneous | $1,500 | $1,500”
  - column:Total: 25822 ⟵ “Total | $18,492 | $25,822”
### `7e03f6437db71e1e` Pensacola State College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://pensacolastate.edu/docs/finAid/2026/FinancialAid_CoAClockHours_20260213_Active_ADA_Student.pdf (sha256 f73c7c43af95)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2025-26, conflicting_sources:https://pensacolastate.edu/docs/finAid/2026/FinancialAid_NineMonthCoABudget_Active_ADA_Student.pdf
- checks: {"columns": 5, "rows": 13}
  - column:TOTAL: 18344 ⟵ “TOTAL | $18,344 | 25,674 | 15,408 | $22,738”
  - column:1. Tuition and fees***: 10289 ⟵ “1. Tuition and fees*** | $10,289 | $10,289 | $ 5,144 | $ 5,144”
  - column:2. Books and supplies: 1800 ⟵ “2. Books and supplies | 1,800 | 1,800 | 900 | 900”
  - column:3. Living expenses: 10226 ⟵ “3. Living expenses | 10,226 | 17,556 | 10,226 | 17,556”
  - column:4. Transportation: 2246 ⟵ “4. Transportation | 2,246 | 2,246 | 2,246 | 2,246”
  - column:5. Miscellaneous: 1500 ⟵ “5. Miscellaneous | 1,500 | 1,500 | 750 | 750”
  - column:TOTAL (2): 26061 ⟵ “TOTAL | $26,061 | $33,391 | $19,266 | $26,596”
  - column:1. Tuition and fees*** (2): 2872 ⟵ “1. Tuition and fees*** | $ 2,872 | $2,872 | $ 1,436 | $ 1,436”
  - column:2. Books and supplies (2): 1800 ⟵ “2. Books and supplies | 1,800 | 1,800 | 900 | 900”
  - column:3. Living expenses (2): 10226 ⟵ “3. Living expenses | 10,226 | 17,556 | 10,226 | 17,556”
  - column:4. Transportation (2): 2246 ⟵ “4. Transportation | 2,246 | 2,246 | 2,246 | 2,246”
  - column:5. Miscellaneous (2): 1500 ⟵ “5. Miscellaneous | 1,500 | 1,500 | 750 | 750”
  - column:TOTAL (3): 18644 ⟵ “TOTAL | $18,644 | $25,974 | $15,558 | $22,888”
  - column:1.: 2572 ⟵ “1. | Tuition and fees*** | $ 2,572 | $ 2,572 | $ 1,286 | $ 1,286”
  - column:2.: 1800 ⟵ “2. | Books and supplies | 1,800 | 1,800 | 900 | 900”
  - column:3.: 10226 ⟵ “3. | Living expenses | 10,226 | 17,556 | 10,226 | 17,556”
  - column:4.: 2246 ⟵ “4. | Transportation | 2,246 | 2,246 | 2,246 | 2,246”
  - column:5.: 1500 ⟵ “5. | Miscellaneous | 1,500 | 1,500 | 750 | 750”
  - column:TOTAL: 25674 ⟵ “TOTAL | $18,344 | 25,674 | 15,408 | $22,738”
  - column:1. Tuition and fees***: 10289 ⟵ “1. Tuition and fees*** | $10,289 | $10,289 | $ 5,144 | $ 5,144”
  - column:2. Books and supplies: 1800 ⟵ “2. Books and supplies | 1,800 | 1,800 | 900 | 900”
  - column:3. Living expenses: 17556 ⟵ “3. Living expenses | 10,226 | 17,556 | 10,226 | 17,556”
  - column:4. Transportation: 2246 ⟵ “4. Transportation | 2,246 | 2,246 | 2,246 | 2,246”
  - column:5. Miscellaneous: 1500 ⟵ “5. Miscellaneous | 1,500 | 1,500 | 750 | 750”
  - column:TOTAL (2): 33391 ⟵ “TOTAL | $26,061 | $33,391 | $19,266 | $26,596”
  - … 47 more rows
### `ad8d1e56cc80bf5f` Pensacola State College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://financialaid.pensacolastate.edu/non-florida-residents-tuition-rates/ (sha256 32255f0e687e)
- issues: arrangement_unlabeled, conflicting_sources:https://financialaid.pensacolastate.edu/alabama-residents-tuition-rates/,https://financialaid.pensacolastate.edu/in-state-resident-rates/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 10914 ⟵ “Tuition and Fees | $10,914 | $10,914”
  - column:Books and Supplies: 1800 ⟵ “Books and Supplies | $1,800 | $1,800”
  - column:Living Expenses: 10226 ⟵ “Living Expenses | $10,226 | $17,556”
  - column:Transportation: 2246 ⟵ “Transportation | $2,246 | $2,246”
  - column:Miscellaneous: 1500 ⟵ “Miscellaneous | $1,500 | $1,500”
  - column:Total: 26686 ⟵ “Total | $26,686 | $34,016”
  - column:Tuition and Fees: 10914 ⟵ “Tuition and Fees | $10,914 | $10,914”
  - column:Books and Supplies: 1800 ⟵ “Books and Supplies | $1,800 | $1,800”
  - column:Living Expenses: 17556 ⟵ “Living Expenses | $10,226 | $17,556”
  - column:Transportation: 2246 ⟵ “Transportation | $2,246 | $2,246”
  - column:Miscellaneous: 1500 ⟵ “Miscellaneous | $1,500 | $1,500”
  - column:Total: 34016 ⟵ “Total | $26,686 | $34,016”
### `d7d36db37b599a3d` Pensacola State College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://pensacolastate.edu/docs/finAid/2026/FinancialAid_NineMonthCoABudget_Active_ADA_Student.pdf (sha256 64ad9748e259)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2025-26, conflicting_sources:https://pensacolastate.edu/docs/finAid/2026/FinancialAid_CoAClockHours_20260213_Active_ADA_Student.pdf
- checks: {"columns": 2, "rows": 36}
  - column:Tuition and fees: 2720 ⟵ “Tuition and fees | *$ 2,720 | *$ 3,144”
  - column:Books and supplies: 1800 ⟵ “Books and supplies | 1,800 | 1,800”
  - column:Living expenses: 17556 ⟵ “Living expenses | 17,556 | 17,556”
  - column:Transportation: 2246 ⟵ “Transportation | 2,246 | 2,246”
  - column:Miscellaneous: 1500 ⟵ “Miscellaneous | 1,500 | 1,500”
  - column:Total: 25822 ⟵ “Total | $ 25,822 | $26,246”
  - column:Tuition and fees (2): 2572 ⟵ “Tuition and fees | *$ 2,572”
  - column:Books and supplies (2): 1800 ⟵ “Books and supplies | 1,800”
  - column:Living expenses (2): 17556 ⟵ “Living expenses | 17,556”
  - column:Transportation (2): 2246 ⟵ “Transportation | 2,246”
  - column:Miscellaneous (2): 1500 ⟵ “Miscellaneous | 1,500”
  - column:Total (2): 25674 ⟵ “Total | $25,674”
  - column:Tuition and fees (3): 2980 ⟵ “Tuition and fees | *$ 2,980 | *$ 3,404”
  - column:Books and supplies (3): 1800 ⟵ “Books and supplies | 1,800”
  - column:Living expenses (3): 17556 ⟵ “Living expenses | 17,556 | 17,556”
  - column:Transportation (3): 2246 ⟵ “Transportation | 2,246 | 2,246”
  - column:Miscellaneous (3): 1500 ⟵ “Miscellaneous | 1,500 | 1,500”
  - column:Total (3): 26082 ⟵ “Total | $ 26,082 | $ 26,506”
  - column:Tuition and fees (4): 2872 ⟵ “Tuition and fees | *$ 2,872”
  - column:Books and supplies (4): 1800 ⟵ “Books and supplies | 1,800”
  - column:Living expenses (4): 17556 ⟵ “Living expenses | 17,556”
  - column:Transportation (4): 2246 ⟵ “Transportation | 2,246”
  - column:Miscellaneous (4): 1500 ⟵ “Miscellaneous | 1,500”
  - column:Total (4): 25974 ⟵ “Total | $25,974”
  - column:Tuition and fees (5): 10914 ⟵ “Tuition and fees | *$ 10,914 | *$ 12,650”
  - … 28 more rows
### `f09b02053db88365` Pensacola State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://pensacolastate.edu/docs/finAid/2026/FinancialAid_CoAClockHours_20260512_v2_Active_ADA_Student.pdf (sha256 064fdc868b5a)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, conflicting_sources:https://pensacolastate.edu/docs/finAid/2026/FinancialAid_NineMonthCoABudget_20260512_v2_Active_ADA_Student.pdf
- checks: {"columns": 5, "rows": 13}
  - column:TOTAL: 18344 ⟵ “TOTAL | $18,344 | 25,674 | 15,408 | $22,738”
  - column:1. Tuition and fees***: 10289 ⟵ “1. Tuition and fees*** | $10,289 | $10,289 | $ 5,144 | $ 5,144”
  - column:2. Books and supplies: 1800 ⟵ “2. Books and supplies | 1,800 | 1,800 | 900 | 900”
  - column:3. Living expenses: 10226 ⟵ “3. Living expenses | 10,226 | 17,556 | 10,226 | 17,556”
  - column:4. Transportation: 2246 ⟵ “4. Transportation | 2,246 | 2,246 | 2,246 | 2,246”
  - column:5. Miscellaneous: 1500 ⟵ “5. Miscellaneous | 1,500 | 1,500 | 750 | 750”
  - column:TOTAL (2): 26061 ⟵ “TOTAL | $26,061 | $33,391 | $19,266 | $26,596”
  - column:1. Tuition and fees*** (2): 2872 ⟵ “1. Tuition and fees*** | $ 2,872 | $2,872 | $ 1,436 | $ 1,436”
  - column:2. Books and supplies (2): 1800 ⟵ “2. Books and supplies | 1,800 | 1,800 | 900 | 900”
  - column:3. Living expenses (2): 10226 ⟵ “3. Living expenses | 10,226 | 17,556 | 10,226 | 17,556”
  - column:4. Transportation (2): 2246 ⟵ “4. Transportation | 2,246 | 2,246 | 2,246 | 2,246”
  - column:5. Miscellaneous (2): 1500 ⟵ “5. Miscellaneous | 1,500 | 1,500 | 750 | 750”
  - column:TOTAL (3): 18644 ⟵ “TOTAL | $18,644 | $25,974 | $15,558 | $22,888”
  - column:1.: 2572 ⟵ “1. | Tuition and fees*** | $ 2,572 | $ 2,572 | $ 1,286 | $ 1,286”
  - column:2.: 1800 ⟵ “2. | Books and supplies | 1,800 | 1,800 | 900 | 900”
  - column:3.: 10226 ⟵ “3. | Living expenses | 10,226 | 17,556 | 10,226 | 17,556”
  - column:4.: 2246 ⟵ “4. | Transportation | 2,246 | 2,246 | 2,246 | 2,246”
  - column:5.: 1500 ⟵ “5. | Miscellaneous | 1,500 | 1,500 | 750 | 750”
  - column:TOTAL: 25674 ⟵ “TOTAL | $18,344 | 25,674 | 15,408 | $22,738”
  - column:1. Tuition and fees***: 10289 ⟵ “1. Tuition and fees*** | $10,289 | $10,289 | $ 5,144 | $ 5,144”
  - column:2. Books and supplies: 1800 ⟵ “2. Books and supplies | 1,800 | 1,800 | 900 | 900”
  - column:3. Living expenses: 17556 ⟵ “3. Living expenses | 10,226 | 17,556 | 10,226 | 17,556”
  - column:4. Transportation: 2246 ⟵ “4. Transportation | 2,246 | 2,246 | 2,246 | 2,246”
  - column:5. Miscellaneous: 1500 ⟵ “5. Miscellaneous | 1,500 | 1,500 | 750 | 750”
  - column:TOTAL (2): 33391 ⟵ “TOTAL | $26,061 | $33,391 | $19,266 | $26,596”
  - … 47 more rows
### `54de23a0a18e51c7` Polk State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.polk.edu/admission-aid/financial-aid/policies/satisfactory-academic-progress/ (sha256 4fbbd5949f51)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Students will not have eligibility for any further financial aid until they meet Satisfactory Academic Progress standards or have an approved appeal on file with the Office of Student Financial Services.”
  - sentence: sap_appeal ⟵ “Types of SAP Appeals GPA and/or Completion Ratio Appeal This appeal applies to students whose SAP evaluation indicates they did not meet the minimum cumulative grade point average (GPA) and/or completion ratio (PACE) requirements.”
  - sentence: sap_appeal ⟵ “Appeal Submission Deadlines SAP Appeals are accepted each term according to the schedule below: | TERM | DEADLINE | Fall (202720) | TBD | Spring (202640) | January 6, 2026 | Summer (202660) | May 13, 2026 SAP Appeal Packet Requirements Your SAP Appeal Packet must be submitted through Etrieve and include all of the following items: SAP Appeal Form (available in Etrieve) Personal Statement explainin”
  - sentence: sap_appeal ⟵ “Review Process and Notification The SAP Appeal Committee reviews complete packets in the order they are received.”
  - sentence: sap_appeal ⟵ “Reinstatement of Financial Aid Eligibility A student who has lost financial aid eligibility may be reinstated after the student has taken classes to meet the minimum requirements of an overall GPA of 2.0 and a cumulative completion rate of 67% of all credit hours being evaluated or if approved on an SAP appeal.”
### `96710c40934ae081` Polk State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.polk.edu/admission-aid/financial-aid/pay-for-college-2/ (sha256 15d61f843aee)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “You may be asked to provide detailed documentation to receive special consideration for a professional judgment about your circumstances.”
### `ac5c431eee145c2b` Polk State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.polk.edu/wp-content/uploads/Polk-State-College-Tuition-and-Fees-Chart-2026-2027-ADA-rev-6.12.26.pdf (sha256 ff25bce29e51)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.polk.edu/wp-content/uploads/COA_2026-2027_Lower_Division_Breakdown_Accessible.pdf,https://www.polk.edu/wp-content/uploads/COA_2026-2027_Upper_Division_Breakdown_Accessible.pdf
- checks: {"columns": 4, "rows": 17}
  - column:Tuition: 82.78 ⟵ “Tuition | 82.78 | 82.78 | N/A | N/A”
  - column:Technology: 4.14 ⟵ “Technology | 4.14 | 16.56 | N/A | N/A”
  - column:Financial Aid: 4.14 ⟵ “Financial Aid | 4.14 | 16.56 | N/A | N/A”
  - column:Student Activity: 8.28 ⟵ “Student Activity | 8.28 | 8.28 | N/A | N/A”
  - column:Capital Improvement: 11.88 ⟵ “Capital Improvement | 11.88 | 35.55 | N/A | N/A”
  - column:Student Services: 1.0 ⟵ “Student Services | 1.00 | 1.00 | N/A | N/A”
  - column:Tuition (2): 91.79 ⟵ “Tuition | 91.79 | 91.79 | N/A | N/A”
  - column:Technology (2): 4.59 ⟵ “Technology | 4.59 | 19.06 | N/A | N/A”
  - column:Financial Aid (2): 4.59 ⟵ “Financial Aid | 4.59 | 19.06 | N/A | N/A”
  - column:Student Activity (2): 9.18 ⟵ “Student Activity | 9.18 | 9.18 | N/A | N/A”
  - column:Capital Improvement (2): 12.74 ⟵ “Capital Improvement | 12.74 | 40.30 | N/A | N/A”
  - column:Student Services (2): 1.0 ⟵ “Student Services | 1.00 | 1.00”
  - column:Tuition (3): 73.4 ⟵ “Tuition | 73.40 | 73.40 | 2.4467 | 2.4467”
  - column:Out-of-State: 220.19 ⟵ “Out-of-State | 220.19 | 7.3397”
  - column:Technology (3): 3.67 ⟵ “Technology | 3.67 | 14.68 | 0.1223 | 0.4893”
  - column:Capital Improvement (3): 3.67 ⟵ “Capital Improvement | 3.67 | 14.68 | 0.1223 | 0.4893”
  - column:Student Services (3): 1.0 ⟵ “Student Services | 1.00 | 1.00 | 0.0333 | 0.0333”
  - column:Tuition: 82.78 ⟵ “Tuition | 82.78 | 82.78 | N/A | N/A”
  - column:Out-of-State: 248.33 ⟵ “Out-of-State | - | 248.33 | N/A | N/A”
  - column:Technology: 16.56 ⟵ “Technology | 4.14 | 16.56 | N/A | N/A”
  - column:Financial Aid: 16.56 ⟵ “Financial Aid | 4.14 | 16.56 | N/A | N/A”
  - column:Student Activity: 8.28 ⟵ “Student Activity | 8.28 | 8.28 | N/A | N/A”
  - column:Capital Improvement: 35.55 ⟵ “Capital Improvement | 11.88 | 35.55 | N/A | N/A”
  - column:Student Services: 1.0 ⟵ “Student Services | 1.00 | 1.00 | N/A | N/A”
  - column:Tuition (2): 91.79 ⟵ “Tuition | 91.79 | 91.79 | N/A | N/A”
  - … 19 more rows
### `d8d77d6e48c0a60d` Polk State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.polk.edu/wp-content/uploads/COA_2026-2027_Upper_Division_Breakdown_Accessible.pdf (sha256 582501f34ca7)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.polk.edu/wp-content/uploads/COA_2026-2027_Lower_Division_Breakdown_Accessible.pdf,https://www.polk.edu/wp-content/uploads/Polk-State-College-Tuition-and-Fees-Chart-2026-2027-ADA-rev-6.12.26.pdf
- checks: {"columns": 4, "components_reconcile": true, "rows": 10}
  - column:Tuition & Mandatory Fees: 2973.36 ⟵ “Tuition & Mandatory Fees | $2,973.36 | $2,973.36 | $11,272.80 | $11,272.80”
  - column:Books, Supplies, Course Materials & Equipment: 1349.0 ⟵ “Books, Supplies, Course Materials & Equipment | $1,349.00 | $1,349.00 | $1,349.00 | $1,349.00”
  - column:Food Allowance: 3060 ⟵ “Food Allowance | $3,060 | $3,060 | $3,060 | $3,060”
  - column:Housing: 4725 ⟵ “Housing | $4,725 | $11,412 | $4,725 | $11,412”
  - column:Miscellaneous Personal Expenses: 2120 ⟵ “Miscellaneous Personal Expenses | $2,120 | $2,120 | $2,120 | $2,120”
  - column:Transportation: 2712 ⟵ “Transportation | $2,712 | $2,712 | $2,712 | $2,712”
  - column:Program Fees: 0 ⟵ “Program Fees | $0 | $0 | $0 | $0”
  - column:Direct Loan Fees: 0 ⟵ “Direct Loan Fees | $0 | $0 | $0 | $0”
  - column:Aviation Fees: 0 ⟵ “Aviation Fees | $0 | $0 | $0 | $0”
  - column:Estimated Total (Full-Time / Full Year): 16939.36 ⟵ “Estimated Total (Full-Time / Full Year) | $16,939.36 | $23,626.36 | $25,238.80 | $31,925.80”
  - column:Tuition & Mandatory Fees: 2973.36 ⟵ “Tuition & Mandatory Fees | $2,973.36 | $2,973.36 | $11,272.80 | $11,272.80”
  - column:Books, Supplies, Course Materials & Equipment: 1349.0 ⟵ “Books, Supplies, Course Materials & Equipment | $1,349.00 | $1,349.00 | $1,349.00 | $1,349.00”
  - column:Food Allowance: 3060 ⟵ “Food Allowance | $3,060 | $3,060 | $3,060 | $3,060”
  - column:Housing: 11412 ⟵ “Housing | $4,725 | $11,412 | $4,725 | $11,412”
  - column:Miscellaneous Personal Expenses: 2120 ⟵ “Miscellaneous Personal Expenses | $2,120 | $2,120 | $2,120 | $2,120”
  - column:Transportation: 2712 ⟵ “Transportation | $2,712 | $2,712 | $2,712 | $2,712”
  - column:Program Fees: 0 ⟵ “Program Fees | $0 | $0 | $0 | $0”
  - column:Direct Loan Fees: 0 ⟵ “Direct Loan Fees | $0 | $0 | $0 | $0”
  - column:Aviation Fees: 0 ⟵ “Aviation Fees | $0 | $0 | $0 | $0”
  - column:Estimated Total (Full-Time / Full Year): 23626.36 ⟵ “Estimated Total (Full-Time / Full Year) | $16,939.36 | $23,626.36 | $25,238.80 | $31,925.80”
  - column:Tuition & Mandatory Fees: 11272.8 ⟵ “Tuition & Mandatory Fees | $2,973.36 | $2,973.36 | $11,272.80 | $11,272.80”
  - column:Books, Supplies, Course Materials & Equipment: 1349.0 ⟵ “Books, Supplies, Course Materials & Equipment | $1,349.00 | $1,349.00 | $1,349.00 | $1,349.00”
  - column:Food Allowance: 3060 ⟵ “Food Allowance | $3,060 | $3,060 | $3,060 | $3,060”
  - column:Housing: 4725 ⟵ “Housing | $4,725 | $11,412 | $4,725 | $11,412”
  - column:Miscellaneous Personal Expenses: 2120 ⟵ “Miscellaneous Personal Expenses | $2,120 | $2,120 | $2,120 | $2,120”
  - … 15 more rows
### `ddcc8346adfc67c4` Polk State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.polk.edu/wp-content/uploads/COA_2026-2027_Lower_Division_Breakdown_Accessible.pdf (sha256 e3a29e81a9cb)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.polk.edu/wp-content/uploads/COA_2026-2027_Upper_Division_Breakdown_Accessible.pdf,https://www.polk.edu/wp-content/uploads/Polk-State-College-Tuition-and-Fees-Chart-2026-2027-ADA-rev-6.12.26.pdf
- checks: {"columns": 4, "components_reconcile": true, "rows": 10}
  - column:Tuition & Mandatory Fees: 2693.28 ⟵ “Tuition & Mandatory Fees | $2,693.28 | $2,693.28 | $9,817.44 | $9,817.44”
  - column:Books, Supplies, Course Materials & Equipment: 1349.0 ⟵ “Books, Supplies, Course Materials & Equipment | $1,349.00 | $1,349.00 | $1,349.00 | $1,349.00”
  - column:Food Allowance: 3060 ⟵ “Food Allowance | $3,060 | $3,060 | $3,060 | $3,060”
  - column:Housing: 4725 ⟵ “Housing | $4,725 | $11,412 | $4,725 | $11,412”
  - column:Miscellaneous Personal Expenses: 2120 ⟵ “Miscellaneous Personal Expenses | $2,120 | $2,120 | $2,120 | $2,120”
  - column:Transportation: 2712 ⟵ “Transportation | $2,712 | $2,712 | $2,712 | $2,712”
  - column:Program Fees: 0 ⟵ “Program Fees | $0 | $0 | $0 | $0”
  - column:Direct Loan Fees: 0 ⟵ “Direct Loan Fees | $0 | $0 | $0 | $0”
  - column:Aviation Fees: 0 ⟵ “Aviation Fees | $0 | $0 | $0 | $0”
  - column:Estimated Total (Full-Time / Full Year): 16659.28 ⟵ “Estimated Total (Full-Time / Full Year) | $16,659.28 | $23,346.28 | $23,783.44 | $30,470.44”
  - column:Tuition & Mandatory Fees: 2693.28 ⟵ “Tuition & Mandatory Fees | $2,693.28 | $2,693.28 | $9,817.44 | $9,817.44”
  - column:Books, Supplies, Course Materials & Equipment: 1349.0 ⟵ “Books, Supplies, Course Materials & Equipment | $1,349.00 | $1,349.00 | $1,349.00 | $1,349.00”
  - column:Food Allowance: 3060 ⟵ “Food Allowance | $3,060 | $3,060 | $3,060 | $3,060”
  - column:Housing: 11412 ⟵ “Housing | $4,725 | $11,412 | $4,725 | $11,412”
  - column:Miscellaneous Personal Expenses: 2120 ⟵ “Miscellaneous Personal Expenses | $2,120 | $2,120 | $2,120 | $2,120”
  - column:Transportation: 2712 ⟵ “Transportation | $2,712 | $2,712 | $2,712 | $2,712”
  - column:Program Fees: 0 ⟵ “Program Fees | $0 | $0 | $0 | $0”
  - column:Direct Loan Fees: 0 ⟵ “Direct Loan Fees | $0 | $0 | $0 | $0”
  - column:Aviation Fees: 0 ⟵ “Aviation Fees | $0 | $0 | $0 | $0”
  - column:Estimated Total (Full-Time / Full Year): 23346.28 ⟵ “Estimated Total (Full-Time / Full Year) | $16,659.28 | $23,346.28 | $23,783.44 | $30,470.44”
  - column:Tuition & Mandatory Fees: 9817.44 ⟵ “Tuition & Mandatory Fees | $2,693.28 | $2,693.28 | $9,817.44 | $9,817.44”
  - column:Books, Supplies, Course Materials & Equipment: 1349.0 ⟵ “Books, Supplies, Course Materials & Equipment | $1,349.00 | $1,349.00 | $1,349.00 | $1,349.00”
  - column:Food Allowance: 3060 ⟵ “Food Allowance | $3,060 | $3,060 | $3,060 | $3,060”
  - column:Housing: 4725 ⟵ “Housing | $4,725 | $11,412 | $4,725 | $11,412”
  - column:Miscellaneous Personal Expenses: 2120 ⟵ “Miscellaneous Personal Expenses | $2,120 | $2,120 | $2,120 | $2,120”
  - … 15 more rows
### `684dbbe8dd4686e4` Ringling College of Art and Design — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ringling.edu/admissions/financial-aid-and-tuition/financial-aid-opportunities/ (sha256 cbc17575bb9f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Please note that approved special circumstances do not guarantee that any additional aid will be awarded.”
### `72eba5e34d352f4b` Ringling College of Art and Design — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ringling.edu/admissions/financial-aid-and-tuition/financial-aid-opportunities/ (sha256 cbc17575bb9f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Increase in Student’s Cost of Attendance Incurred While Attending the College: Child or dependent care expenses Changes in Family Dynamics that Justify Applying as an Independent Student (Dependency Override): Abandonment by parents An Abusive family environment that threatens the student’s health of safety In accordance to 24-25 HEA 479A, extenuating family circumstances will be reviewed such as;”
### `d9f750049ac9b6ed` Ringling College of Art and Design — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ringling.edu/admissions/financial-aid-and-tuition/financial-aid-opportunities/ (sha256 cbc17575bb9f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Ringling College of Art and Design Verification Gateway Links and Deadlines Inceptia Federal Verification Gateway Special Circumstance/Professional Judgment The U.S.”
  - sentence: professional_judgment ⟵ “Professional judgment is to be exercised in situations which a significant impact on the family’s ability to contribute as reflected on the FAFSA has occurred.”
  - sentence: professional_judgment ⟵ “Ringling College of Art and Design has partnered with Inceptia to gather the required documents for the Office of Financial Aid to make our Professional Judgement.”
### `234ac5c34021f765` Ringling College of Art and Design — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ringling.edu/admissions/financial-aid-and-tuition/tuition/ (sha256 980ef4df08c6)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 11}
  - column:Tuition: 55760 ⟵ “Tuition | $55,760”
  - column:Fees (Matriculation, Student Activity, Health Services, Technology): 5710 ⟵ “Fees (Matriculation, Student Activity, Health Services, Technology) | $5,710”
  - column:Room and Board: 18510 ⟵ “Room and Board | $18,510”
  - column:TOTAL: 79980 ⟵ “TOTAL | $79,980”
  - column:First Year Materials Kit – BOAD: 100 ⟵ “First Year Materials Kit – BOAD | $100”
  - column:First Year Materials Kit – Entertainment Design: 320 ⟵ “First Year Materials Kit – Entertainment Design | $320”
  - column:First Year Materials Kit – 2D Character Animation, 3D Character Animation, Game Art, Illustration: 320 ⟵ “First Year Materials Kit – 2D Character Animation, 3D Character Animation, Game Art, Illustration | $320”
  - column:First Year Materials Kit – Fine Arts: 285 ⟵ “First Year Materials Kit – Fine Arts | $285”
  - column:First Year Materials Kit – Creative Technologies, Graphic Design: 145 ⟵ “First Year Materials Kit – Creative Technologies, Graphic Design | $145”
  - column:First Year Materials Kit – Motion Design: 375 ⟵ “First Year Materials Kit – Motion Design | $375”
  - column:First Year Materials Kit – Virtual Reality: 365 ⟵ “First Year Materials Kit – Virtual Reality | $365”
### `03ac557a23bff5d8` Rollins College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rollins.edu/scholarships-aid/faqs/rights-responsibilities/ (sha256 633b0e601e76)
- issues: semantic_review_required, conflicting_sources:https://crummer.rollins.edu/admission-and-aid/financial-aid-and-scholarships/,https://www.rollins.edu/scholarships-aid/fafsa/,https://www.rollins.edu/scholarships-aid/fafsa/special-circumstances/,https://www.rollins.edu/scholarships-aid/faqs/,https://www.rollins.edu/scholarships-aid/faqs/special-circumstances/,https://www.rollins.edu/scholarships-aid/loans/plus-loans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Notifying the Office of Financial Aid if a change in your family financial situation occurs, or if you receive assistance from an outside source.”
### `08b6f17536f826d6` Rollins College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rollins.edu/scholarships-aid/faqs/special-circumstances/ (sha256 216214498fe3)
- issues: semantic_review_required, conflicting_sources:https://crummer.rollins.edu/admission-and-aid/financial-aid-and-scholarships/,https://www.rollins.edu/scholarships-aid/fafsa/,https://www.rollins.edu/scholarships-aid/fafsa/special-circumstances/,https://www.rollins.edu/scholarships-aid/faqs/,https://www.rollins.edu/scholarships-aid/faqs/rights-responsibilities/,https://www.rollins.edu/scholarships-aid/loans/plus-loans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If your family has experienced an unusual change in financial circumstances not considered on the Free Application for Federal Student Aid (FAFSA), you may wish to request consideration.”
### `26dab66a7b7f7bbe` Rollins College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.rollins.edu/scholarships-aid/fafsa/ (sha256 a0bc404b9abc)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://crummer.rollins.edu/admission-and-aid/financial-aid-and-scholarships/,https://www.rollins.edu/scholarships-aid/fafsa/special-circumstances/,https://www.rollins.edu/scholarships-aid/faqs/,https://www.rollins.edu/scholarships-aid/faqs/rights-responsibilities/,https://www.rollins.edu/scholarships-aid/faqs/special-circumstances/,https://www.rollins.edu/scholarships-aid/loans/plus-loans/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The need analysis process does not always consider every family situation.”
  - sentence: need_based_special_circumstances ⟵ “If your family has experienced a change in financial circumstances not considered on the FAFSA, you may request a review of special circumstances.”
### `35a1196e4a93c1ea` Rollins College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rollins.edu/scholarships-aid/faqs/ (sha256 3e976cffe4ab)
- issues: semantic_review_required, conflicting_sources:https://crummer.rollins.edu/admission-and-aid/financial-aid-and-scholarships/,https://www.rollins.edu/scholarships-aid/fafsa/,https://www.rollins.edu/scholarships-aid/fafsa/special-circumstances/,https://www.rollins.edu/scholarships-aid/faqs/rights-responsibilities/,https://www.rollins.edu/scholarships-aid/faqs/special-circumstances/,https://www.rollins.edu/scholarships-aid/loans/plus-loans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “How Financial Aid Works Rights & Responsibilities Special Circumstances As a member of the Rollins community, it is important that you have the necessary information to be an informed consumer of the College’s services.”
### `40bcda7d43f7b938` Rollins College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rollins.edu/scholarships-aid/fafsa/special-circumstances/ (sha256 d48e1b1bdf97)
- issues: semantic_review_required, conflicting_sources:https://crummer.rollins.edu/admission-and-aid/financial-aid-and-scholarships/,https://www.rollins.edu/scholarships-aid/fafsa/,https://www.rollins.edu/scholarships-aid/faqs/,https://www.rollins.edu/scholarships-aid/faqs/rights-responsibilities/,https://www.rollins.edu/scholarships-aid/faqs/special-circumstances/,https://www.rollins.edu/scholarships-aid/loans/plus-loans/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “If your family has experienced an unusual change in financial circumstances not considered on the Free Application for Federal Student Aid (FAFSA), you may request a review of special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Request Process To request a review for special circumstances, please contact our office.”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances may include, but are not limited to, significant change in income or medical or dental expenses not covered by insurance.”
  - sentence: need_based_special_circumstances ⟵ “Change in Income You or your parent has become unemployed or disabled.”
### `566250bc0484cdab` Rollins College — appeals 2026-27 [new] (source_unlabeled)
- source: https://crummer.rollins.edu/admission-and-aid/financial-aid-and-scholarships/ (sha256 31ab1c25fcc9)
- issues: semantic_review_required, conflicting_sources:https://www.rollins.edu/scholarships-aid/fafsa/,https://www.rollins.edu/scholarships-aid/fafsa/special-circumstances/,https://www.rollins.edu/scholarships-aid/faqs/,https://www.rollins.edu/scholarships-aid/faqs/rights-responsibilities/,https://www.rollins.edu/scholarships-aid/faqs/special-circumstances/,https://www.rollins.edu/scholarships-aid/loans/plus-loans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Notifying the Office of Financial Aid if a change in your family financial situation occurs, or if you receive assistance from an outside source.”
### `75a4470ad6689a19` Rollins College — appeals 2026-27 [new] (source_unlabeled)
- source: https://crummer.rollins.edu/admission-and-aid/financial-aid-and-scholarships/ (sha256 31ab1c25fcc9)
- issues: semantic_review_required, conflicting_sources:https://www.rollins.edu/scholarships-aid/faqs/rights-responsibilities/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeal Review Students can appeal financial aid suspension once under mitigating circumstances.”
### `9f2ae0cd9da78165` Rollins College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rollins.edu/scholarships-aid/faqs/rights-responsibilities/ (sha256 633b0e601e76)
- issues: semantic_review_required, conflicting_sources:https://crummer.rollins.edu/admission-and-aid/financial-aid-and-scholarships/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Download Satisfactory Academic Progress Appeal Instructions (PDF).”
  - sentence: sap_appeal ⟵ “SAP Appeal Reviews The committee will review your appeal within 10-15 business days after receipt of your completed appeal form and the required documentation.”
### `fbf09e269abd486f` Rollins College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.rollins.edu/scholarships-aid/loans/plus-loans/ (sha256 6058725a6d78)
- issues: semantic_review_required, conflicting_sources:https://crummer.rollins.edu/admission-and-aid/financial-aid-and-scholarships/,https://www.rollins.edu/scholarships-aid/fafsa/,https://www.rollins.edu/scholarships-aid/fafsa/special-circumstances/,https://www.rollins.edu/scholarships-aid/faqs/,https://www.rollins.edu/scholarships-aid/faqs/rights-responsibilities/,https://www.rollins.edu/scholarships-aid/faqs/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Dependency exceptions are made for veterans, wards of the court, and other special circumstances.”
### `0f87d479066d3522` Rollins College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/dual-enrollment-credits/ (sha256 d4fedd8c3d1d)
- issues: rows_without_score, conflicting_sources:https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/aice-credits/,https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/cape-credit-list/
- checks: {"distinct_exams": 7, "equivalencies": 7, "rows_without_score": 7}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “General Biology I (w/lab) | BSC 1010C | Science Requirement | BIO 121 - Meets Science rFLA”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “General Chemistry (w/lab) | CHM 1025C | Science Requirement | Science w/labCHM 1XX - Meets Science rFLA”
  - equivalencies[IB-PHILOSOPHY|None]:  ⟵ “Introduction to Philosophy | PHI 2010 | Humanities Requirement | PHI 103 - Meets Humanities rFLA”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Introduction to Psychology | PSY 2012Social SciencePSY 101 - Meets Soc Sci rFLA | Social Science Requirement | PSY 101 - Meets Soc Sci rFLA”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music Appreciation | MUL 1010Expressive ArtMUS 1XX - Meets Art rFLAPublic | Expressive Art Requirement | MUS 1XX - Meets Art rFLAPublic”
  - equivalencies[IB-SPANISH|None]:  ⟵ “Intermediate Spanish | SPN 2200 | FCMP | SPN 201 - Meets Foreign Lang CompU”
  - equivalencies[IB-HISTORY|None]:  ⟵ “U.S. History to 1877 | AMH 2010 | Social Science Requirement | HIS 1XX - Meets Soc Sci rFLA”
### `3ccbfd873909b3cd` Rollins College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/cape-credit-list/ (sha256 fdefb6d9106f)
- issues: conflicting_sources:https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/aice-credits/,https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/dual-enrollment-credits/
- checks: {"distinct_exams": 10, "equivalencies": 10, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|SCORE 1 or 2]:  ⟵ “Biology | UNIT Unit 1 & 2 | SCORE 1 or 2 | NOTES BIO 1XX”
  - equivalencies[IB-BUSINESS-MANAGEMENT|SCORE 1 or 2]:  ⟵ “Business | UNIT Unit 1 & 2 | SCORE 1 or 2 | NOTES BUS 1XX”
  - equivalencies[IB-CHEMISTRY|SCORE 1 or 2]:  ⟵ “Chemistry | UNIT Unit 1 & 2 | SCORE 1 or 2 | NOTES CHM 1XX”
  - equivalencies[IB-COMPUTER-SCIENCE|SCORE 1 or 2]:  ⟵ “Computer Science | UNIT Unit 1 | SCORE 1 or 2 | NOTES CMS 1XX”
  - equivalencies[IB-ECONOMICS|SCORE 1 or 2]:  ⟵ “Economics | UNIT Unit 1 & 2 | SCORE 1 or 2 | NOTES ECO 1XX”
  - equivalencies[IB-FRENCH|SCORE 1 or 2]:  ⟵ “French | UNIT Unit 1 | SCORE 1 or 2 | NOTES FRN 101”
  - equivalencies[IB-GEOGRAPHY|SCORE 1 or 2]:  ⟵ “Geography | UNIT Unit 1 | SCORE 1 or 2 | NOTES SSC 1XX”
  - equivalencies[IB-HISTORY|SCORE 1 or 2]:  ⟵ “History | UNIT Unit 1 | SCORE 1 or 2 | NOTES HIS 1XX”
  - equivalencies[IB-PHYSICS|SCORE 1 or 2]:  ⟵ “Physics | UNIT Unit 1 | SCORE 1 or 2 | NOTES PHY 1XX”
  - equivalencies[IB-SPANISH|SCORE 1 or 2]:  ⟵ “Spanish | UNIT Unit 1 | SCORE 1 or 2 | NOTES SPN 101”
### `b01e36efc2691ede` Rollins College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/aice-credits/ (sha256 8ed45f2938e3)
- issues: conflicting_sources:https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/cape-credit-list/,https://www.rollins.edu/apply/ap-ib-dual-enrollment-cape-credits/dual-enrollment-credits/
- checks: {"distinct_exams": 3, "equivalencies": 6, "rows_without_score": 0}
  - equivalencies[IB-CHEMISTRY|Level AS-Level]:  ⟵ “Chemistry | Level AS-Level | Minimum Grade (UK Scale) C | Credits 4 | Comp | Notes Elective Credit: CHM 1XX”
  - equivalencies[IB-CHEMISTRY|Level A-Level]:  ⟵ “Chemistry | Level A-Level | Minimum Grade (UK Scale) C | Credits 8 | Comp | Notes Elective Credit: CHM 1XX”
  - equivalencies[IB-COMPUTER-SCIENCE|Level AS-Level]:  ⟵ “Computer Science | Level AS-Level | Minimum Grade (UK Scale) C | Credits 4 | Comp | Notes Elective Credit: CMS 1XX”
  - equivalencies[IB-COMPUTER-SCIENCE|Level A-Level]:  ⟵ “Computer Science | Level A-Level | Minimum Grade (UK Scale) C | Credits 8 | Comp | Notes Elective Credit: CMS 1XX”
  - equivalencies[IB-PHYSICS|Level AS-Level]:  ⟵ “Physics | Level AS-Level | Minimum Grade (UK Scale) C | Credits 4 | Comp | Notes Elective Credit: PHY 1XX”
  - equivalencies[IB-PHYSICS|Level A-Level]:  ⟵ “Physics | Level A-Level | Minimum Grade (UK Scale) C | Credits 8 | Comp | Notes Elective Credit: PHY 1XX”
### `312344b85192b482` Saint Leo University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process/appeals (sha256 4b91b4498cef)
- issues: semantic_review_required, conflicting_sources:https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process,https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process/eligibility
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Utilizing the Special Circumstances form (available in Financial Aid Forms), allows students and/or families to indicate special circumstances that may not be evident on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If current year income will be lower due to special circumstances the Student Financial Services office may be able to use current year projected income to assess financial need.”
  - sentence: need_based_special_circumstances ⟵ “A processed FAFSA and completed verification, if selected, must be on file before special circumstances can be considered.”
### `5b74bdf1c86376c5` Saint Leo University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process/eligibility (sha256 edefe6d9efec)
- issues: semantic_review_required, conflicting_sources:https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process,https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process/appeals
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “This may include a signed and dated statement explaining the special circumstance that caused the student to not earn credits, as well as supporting documentation to verify the special circumstance(s) described.”
### `5bdcd645777dc51d` Saint Leo University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process (sha256 a46bc67bea1f)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process/appeals,https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process/eligibility
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Utilizing the Special Circumstances form (available in Financial Aid Forms), allows students and/or families to indicate special circumstances that may not be evident on the FAFSA®.”
### `c21cf020dd376d13` Saint Leo University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process/sap-policy (sha256 57efbdc2ef5d)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeals If a student has experienced special circumstances (e.g. illness, job related issues, family illness) during the most recent evaluation period that s/he did not meet standards of academic progress, an appeal to request reinstatement of financial aid eligibility can be submitted.”
### `e303cf309c78a5be` Saint Leo University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/financial-aid-process/sap-policy (sha256 57efbdc2ef5d)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If you have completed a Free Application for Federal Student Aid (FAFSA), you should submit your SAP appeal through Financial Aid Forms.”
  - sentence: sap_appeal ⟵ “You can then review the SAP Appeal Instructions document by clicking the Request button.”
  - sentence: sap_appeal ⟵ “Your SAP appeal review will move forward once all items are submitted and satisfied.”
### `08f6af716c2a0bbc` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $15,000 for incoming first-year students ⟵ “University Award | up to $15,000 for incoming first-year students”
### `56d31c69bc3de407` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $12,000 for incoming first-year students ⟵ “Campus Award | up to $12,000 for incoming first-year students”
### `6653df4c510223d7` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $16,000 for transfer students ⟵ “Presidential Transfer Award | up to $16,000 for transfer students”
### `7e33ae8270ca23f2` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $12,000 for transfer students ⟵ “University Transfer Award | up to $12,000 for transfer students”
### `8b28c3c2c71f4df0` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $10,000 for transfer students ⟵ “Campus Transfer Award | up to $10,000 for transfer students”
### `9048704cef1a8962` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $18,000 for incoming first-year students ⟵ “Dean's Award | up to $18,000 for incoming first-year students”
### `b428693b68b113be` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $19,000 for incoming first-year students ⟵ “Presidential Award | up to $19,000 for incoming first-year students”
### `b7cc998682917e9e` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $15,000 for transfer students ⟵ “Dean's Transfer Award | up to $15,000 for transfer students”
### `d9b706ac0a49c4cd` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $13,000 for transfer students ⟵ “Excellence Transfer Award | up to $13,000 for transfer students”
### `f71b44947e4b21cb` Saint Leo University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.saintleo.edu/tuition-financial-aid/aid/grants-scholarships (sha256 a0c1aed44870)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: up to $17,000 for incoming first-year students ⟵ “Excellence Award | up to $17,000 for incoming first-year students”
### `9e80effbab518360` Saint Leo University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.saintleo.edu/sites/default/files/2026-07/2026-2027-Tuition-and-Fees-Campus-Undergraduate-2026-06-30.pdf (sha256 c4760b2f24ea)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 102}
  - on_campus:Tuition**: 17500 ⟵ “Tuition** | $17,500 | $35,000”
  - on_campus:Average Housing (See Residence Hall Room Rates): 4653 ⟵ “Average Housing (See Residence Hall Room Rates) | $4,653 | $9,306”
  - on_campus:Meal Plan (19 meal plan): 3760 ⟵ “Meal Plan (19 meal plan) | $3,760 | $7,520”
  - on_campus:Fees (Orientation***, Student Activity, & Student Services): 940 ⟵ “Fees (Orientation***, Student Activity, & Student Services) | $940 | $1,880”
  - on_campus:Books, Course Materials, Supplies, and Equipment: 555 ⟵ “Books, Course Materials, Supplies, and Equipment | $555 | $1,110”
  - on_campus:Miscellaneous Personal Expenses: 1386 ⟵ “Miscellaneous Personal Expenses | $1,386 | $2,772”
  - on_campus:Transportation: 1494 ⟵ “Transportation | $1,494 | $2,988”
  - on_campus:Federal Loan Fees: 46 ⟵ “Federal Loan Fees | $46 | $92”
  - on_campus:Total Cost of Attendance (Direct & Indirect): 30334 ⟵ “Total Cost of Attendance (Direct & Indirect) | $30,334 | $60,668”
  - on_campus:19 Meal Plan: 3760 ⟵ “19 Meal Plan | $3,760 | $7,520”
  - on_campus:10 Meal Plan: 2420 ⟵ “10 Meal Plan | $2,420 | $4,840”
  - on_campus:5 Meal Plan: 1300 ⟵ “5 Meal Plan | $1,300 | $2,600”
  - on_campus:Commuter Meal Plan (Block of 25 meals): 250 ⟵ “Commuter Meal Plan (Block of 25 meals) | $250 | $500”
  - on_campus:Student Health Insurance*: 1937 ⟵ “Student Health Insurance* | $1,937”
  - on_campus:Student Services Fee: 1100 ⟵ “Student Services Fee | $1,100”
  - on_campus:Student Activity Fee: 280 ⟵ “Student Activity Fee | $280”
  - on_campus:Orientation Fee (New Students Only) $250 for Spring Start: 500 ⟵ “Orientation Fee (New Students Only) $250 for Spring Start | $500”
  - on_campus:Alumni Double: 3995 ⟵ “Alumni Double | $3,995 | $7,990”
  - on_campus:Alumni Double Single: 5990 ⟵ “Alumni Double Single | $5,990 | $11,980”
  - on_campus:Benoit/Henderson Room: 3660 ⟵ “Benoit/Henderson Room | $3,660 | $7,320”
  - on_campus:Benoit/Henderson Double Single: 5490 ⟵ “Benoit/Henderson Double Single | $5,490 | $10,980”
  - on_campus:Benoit/Henderson Physical Single: 4385 ⟵ “Benoit/Henderson Physical Single | $4,385 | $8,770”
  - on_campus:Benoit/Henderson Triple: 3660 ⟵ “Benoit/Henderson Triple | $3,660 | $7,320”
  - on_campus:Henderson Quad Room: 3660 ⟵ “Henderson Quad Room | $3,660 | $7,320”
  - on_campus:Marmion/Snyder Room: 3660 ⟵ “Marmion/Snyder Room | $3,660 | $7,320”
  - … 162 more rows
### `515b8f5c61a8ddb9` Santa Fe College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfcollege.edu/fa/get/special-situations.html (sha256 5d68ddf3670f)
- issues: semantic_review_required, conflicting_sources:https://www.sfcollege.edu/fa/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “If you are required to provide parental information on your (FAFSA) but have an unusual circumstance that prevents you from contacting your parents or contacting your parents poses a risk to you, then you can request the Financial Aid change your dependency status.”
  - sentence: need_based_special_circumstances ⟵ “If you answered "yes" to the unusual circumstances question on the FAFSA, the Financial Aid portal should already have a place to document your unusual circumstances and validate the provisional independent status you were granted.”
  - sentence: need_based_special_circumstances ⟵ “You may be experiencing unusual circumstances if you: Left home due to an abusive or threatening environment; Are abandoned by or estranged from your parents, and have not been adopted; Have refugee or asylee status and are separated from your parents, or your parents are displaced in a foreign country; Are a victim of human trafficking; Your parents are incarcerated, and contact with the parents ”
### `5bdfe57d2947c00a` Santa Fe College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfcollege.edu/fa/keep/sap.html (sha256 594789e8a6d8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 13}
  - sentence: sap_appeal ⟵ “SAP Appeal Can I appeal to have my aid reinstated?What are the appeal dates and deadlines?My appeal was approved, now what?My appeal was denied, now what?”
  - sentence: sap_appeal ⟵ “Suspension Suspended students will not have eligibility for federal aid until they have met all requirements for Satisfactory Academic Progress or have an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “The financial aid SAP appeal process is different from the Registrar's petition process.”
  - sentence: sap_appeal ⟵ “Appeal Availability and Due Dates | Date | Appeal Available Dates | Appeal Due Dates | Fall | Last Day to Drop with Refund for Summer B*** | October 1st | Spring | Last Day to Drop with Refund for Fall B | March 1st | Summer | Last Day to Drop with Refund for Spring B | July 1st Appeal Guidelines SAP Appeals are reviewed in accordance with institutional policy and applicable federal regulations.”
  - sentence: sap_appeal ⟵ “Students are limited to 3 lifetime SAP appeals at Santa Fe College.”
  - sentence: sap_appeal ⟵ “Extenuating circumstances for SAP appeals that may be considered include: Personal illness or accident; Serious illness or death within the immediate family; or Other circumstances beyond the control of the student.”
### `84214d6e6004123a` Santa Fe College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfcollege.edu/fa/get/special-situations.html (sha256 5d68ddf3670f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Add the document called "Professional Judgement".”
### `bcd17dbfd63d5d23` Santa Fe College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sfcollege.edu/fa/ (sha256 64ff82726e3f)
- issues: semantic_review_required, conflicting_sources:https://www.sfcollege.edu/fa/get/special-situations.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “You may have special circumstances that require you to provide additional documents or information.”
  - sentence: need_based_special_circumstances ⟵ “Learn more about Special Circumstances here.”
### `558ad8c5381d684a` Santa Fe College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.sfcollege.edu/finance/student/tuition-dates-schedules.html (sha256 69bf83d494a6)
- issues: implausible_amount
- checks: {"columns": 1, "rows": 8}
  - on_campus:Tuition: 77.98 ⟵ “Tuition | 77.98 | 77.98”
  - on_campus:Capital Improvement: 8.66 ⟵ “Capital Improvement | 8.66 | 31.67”
  - on_campus:Financial Aid: 3.83 ⟵ “Financial Aid | 3.83 | 15.33”
  - on_campus:Student Activities*: 7.8 ⟵ “Student Activities* | 7.80 | 7.80”
  - on_campus:Technology**: 3.5 ⟵ “Technology** | 3.50 | 14.00”
  - on_campus:Subtotal: 101.77 ⟵ “Subtotal | $101.77 | $377.90”
  - on_campus:Access Fee**: 2.0 ⟵ “Access Fee** | 2.00 | 2.00”
  - on_campus:Transportation Fee**: 3.0 ⟵ “Transportation Fee** | 3.00 | 3.00”
### `75865d654bff4bf5` Santa Fe College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.sfcollege.edu/finance/student/tuition-dates-schedules.html (sha256 69bf83d494a6)
- issues: implausible_amount
- checks: {"columns": 1, "rows": 9}
  - on_campus:Tuition: 77.98 ⟵ “Tuition | 77.98 | 77.98”
  - on_campus:Non-Resident Tuition: 231.12 ⟵ “Non-Resident Tuition |  | 231.12”
  - on_campus:Capital Improvement: 31.67 ⟵ “Capital Improvement | 8.66 | 31.67”
  - on_campus:Financial Aid: 15.33 ⟵ “Financial Aid | 3.83 | 15.33”
  - on_campus:Student Activities*: 7.8 ⟵ “Student Activities* | 7.80 | 7.80”
  - on_campus:Technology**: 14.0 ⟵ “Technology** | 3.50 | 14.00”
  - on_campus:Subtotal: 377.9 ⟵ “Subtotal | $101.77 | $377.90”
  - on_campus:Access Fee**: 2.0 ⟵ “Access Fee** | 2.00 | 2.00”
  - on_campus:Transportation Fee**: 3.0 ⟵ “Transportation Fee** | 3.00 | 3.00”
### `c1ccaee730702370` Seminole State College of Florida — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.seminolestate.edu/catalog/student-info/financial-aid/satisfactory-academic-progress-sap (sha256 aa3b4af4fd06)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Students may re-establish Title IV eligibility by meeting the minimum SAP standards or by having an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “The student may submit a SAP appeal.”
  - sentence: sap_appeal ⟵ “This is only applicable to the program in which the SAP appeal is approved.”
### `4e511fa74ab6bcb0` Seminole State College of Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.seminolestate.edu/financial-aid/coa (sha256 533434cd6dd3)
- issues: components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - with_parents_or_family:Tuition*: 1915 ⟵ “Tuition* | $1,915 | $1,915”
  - with_parents_or_family:Fees**: 583 ⟵ “Fees** | $583 | $583”
  - with_parents_or_family:Food & Housing: 12696 ⟵ “Food & Housing | $12,696 | $25,391”
  - with_parents_or_family:Transportation: 2106 ⟵ “Transportation | $2,106 | $2,106”
  - with_parents_or_family:Books & Supplies: 1450 ⟵ “Books & Supplies | $1,450 | $1,450”
  - with_parents_or_family:Personal Expenses: 1600 ⟵ “Personal Expenses | $1,600 | $1,600”
  - with_parents_or_family:Loan Fees: 60 ⟵ “Loan Fees | $60 | $60”
  - with_parents_or_family:Total Budget: 20409 ⟵ “Total Budget | $20,409 | $33,105”
  - off_campus_not_with_family:Tuition*: 1915 ⟵ “Tuition* | $1,915 | $1,915”
  - off_campus_not_with_family:Fees**: 583 ⟵ “Fees** | $583 | $583”
  - off_campus_not_with_family:Food & Housing: 25391 ⟵ “Food & Housing | $12,696 | $25,391”
  - off_campus_not_with_family:Transportation: 2106 ⟵ “Transportation | $2,106 | $2,106”
  - off_campus_not_with_family:Books & Supplies: 1450 ⟵ “Books & Supplies | $1,450 | $1,450”
  - off_campus_not_with_family:Personal Expenses: 1600 ⟵ “Personal Expenses | $1,600 | $1,600”
  - off_campus_not_with_family:Loan Fees: 60 ⟵ “Loan Fees | $60 | $60”
  - off_campus_not_with_family:Total Budget: 33105 ⟵ “Total Budget | $20,409 | $33,105”
### `f08129344d5e510f` Seminole State College of Florida — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.seminolestate.edu/catalog/programs/aa-gen (sha256 cff164bbb84f)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 4, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 3131 ⟵ “Tuition and Fees | $3,131 | $6,440 | $5,654 | $5,954”
  - column:Books and Supplies: 1000 ⟵ “Books and Supplies | $1,000 | $810 | $1,380 | $1,200”
  - column:Total: 4131 ⟵ “Total | $4,131 | $21,440 | $21,194 | $22,074”
  - column:Tuition and Fees: 6440 ⟵ “Tuition and Fees | $3,131 | $6,440 | $5,654 | $5,954”
  - column:Room and Board: 14190 ⟵ “Room and Board | -0- | $14,190 | $14,160 | $14,920”
  - column:Books and Supplies: 810 ⟵ “Books and Supplies | $1,000 | $810 | $1,380 | $1,200”
  - column:Total: 21440 ⟵ “Total | $4,131 | $21,440 | $21,194 | $22,074”
  - column:Tuition and Fees: 5654 ⟵ “Tuition and Fees | $3,131 | $6,440 | $5,654 | $5,954”
  - column:Room and Board: 14160 ⟵ “Room and Board | -0- | $14,190 | $14,160 | $14,920”
  - column:Books and Supplies: 1380 ⟵ “Books and Supplies | $1,000 | $810 | $1,380 | $1,200”
  - column:Total: 21194 ⟵ “Total | $4,131 | $21,440 | $21,194 | $22,074”
  - column:Tuition and Fees: 5954 ⟵ “Tuition and Fees | $3,131 | $6,440 | $5,654 | $5,954”
  - column:Room and Board: 14920 ⟵ “Room and Board | -0- | $14,190 | $14,160 | $14,920”
  - column:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,000 | $810 | $1,380 | $1,200”
  - column:Total: 22074 ⟵ “Total | $4,131 | $21,440 | $21,194 | $22,074”
### `0c236d1898b75256` South Florida State College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.southflorida.edu/wp-content/uploads/2025/11/General-Scholarship_Application.pdf (sha256 fe5d18d0ca98)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Please mention any unusual circumstances affecting your ability to pay for school 3.”
### `24709e943affdb3e` South Florida State College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/wp-content/uploads/2026/06/2026-2027-SAP-Appeal-Form.pdf (sha256 effa81cd99ce)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Form 2026-2027 Important: You must have a current FAFSA on file.”
### `cf1c1b4f6254e5be` South Florida State College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.southflorida.edu/wp-content/uploads/2026/04/General-Scholarship_Application.pdf (sha256 5602d01aec5b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Please mention any unusual circumstances affecting your ability to pay for school 3.”
### `436070cd781e520c` South Florida State College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.southflorida.edu/current-students/financial-aid-scholarships/financial-need-calculation (sha256 2eb77503858a)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 2, "rows": 12}
  - column:Tuition and Fees: 9722 ⟵ “Tuition and Fees | $2,593 | $2,593 | $9,722 | $9,722”
  - column:Books/Supplies: 1275 ⟵ “Books/Supplies | $1,275 | $1,275 | $1,275 | $1,275”
  - column:Room and Board: 2081 ⟵ “Room and Board | $2,081 | $6,161 | $2,081 | $6,161”
  - column:Transportation Expense: 2514 ⟵ “Transportation Expense | $2,514 | $2,514 | $2,514 | $2,514”
  - column:Miscellaneous/Personal: 1158 ⟵ “Miscellaneous/Personal | $1,158 | $1,897 | $1,158 | $1,897”
  - column:TOTAL ESTIMATED COST: 16750 ⟵ “TOTAL ESTIMATED COST | $9,621 | $14,440 | $16,750 | $21,569”
  - column:Tuition and Fees (2): 11087 ⟵ “Tuition and Fees | $2,958 | $2,958 | $11,087 | $11,087”
  - column:Books/Supplies (2): 1275 ⟵ “Books/Supplies | $1,275 | $1,275 | $1,275 | $1,275”
  - column:Room and Board (2): 2081 ⟵ “Room and Board | $2,081 | $6,161 | $2,081 | $6,161”
  - column:Transportation Expense (2): 2514 ⟵ “Transportation Expense | $2,514 | $2,514 | $2,514 | $2,514”
  - column:Miscellaneous/Personal (2): 1158 ⟵ “Miscellaneous/Personal | $1,158 | $1,897 | $1,158 | $1,897”
  - column:TOTAL ESTIMATED COST (2): 18115 ⟵ “TOTAL ESTIMATED COST | $9,986 | $14,805 | $18,115 | $22,934”
  - column:Tuition and Fees: 9722 ⟵ “Tuition and Fees | $2,593 | $2,593 | $9,722 | $9,722”
  - column:Books/Supplies: 1275 ⟵ “Books/Supplies | $1,275 | $1,275 | $1,275 | $1,275”
  - column:Room and Board: 6161 ⟵ “Room and Board | $2,081 | $6,161 | $2,081 | $6,161”
  - column:Transportation Expense: 2514 ⟵ “Transportation Expense | $2,514 | $2,514 | $2,514 | $2,514”
  - column:Miscellaneous/Personal: 1897 ⟵ “Miscellaneous/Personal | $1,158 | $1,897 | $1,158 | $1,897”
  - column:TOTAL ESTIMATED COST: 21569 ⟵ “TOTAL ESTIMATED COST | $9,621 | $14,440 | $16,750 | $21,569”
  - column:Tuition and Fees (2): 11087 ⟵ “Tuition and Fees | $2,958 | $2,958 | $11,087 | $11,087”
  - column:Books/Supplies (2): 1275 ⟵ “Books/Supplies | $1,275 | $1,275 | $1,275 | $1,275”
  - column:Room and Board (2): 6161 ⟵ “Room and Board | $2,081 | $6,161 | $2,081 | $6,161”
  - column:Transportation Expense (2): 2514 ⟵ “Transportation Expense | $2,514 | $2,514 | $2,514 | $2,514”
  - column:Miscellaneous/Personal (2): 1897 ⟵ “Miscellaneous/Personal | $1,158 | $1,897 | $1,158 | $1,897”
  - column:TOTAL ESTIMATED COST (2): 22934 ⟵ “TOTAL ESTIMATED COST | $9,986 | $14,805 | $18,115 | $22,934”
### `45e5645afe67567f` South Florida State College — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.southflorida.edu/current-students/financial-aid-scholarships/financial-need-calculation (sha256 2eb77503858a)
- issues: multiple_total_rows, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 12}
  - column:Tuition and Fees: 2593 ⟵ “Tuition and Fees | $2,593 | $2,593 | $9,722 | $9,722”
  - column:Books/Supplies: 1275 ⟵ “Books/Supplies | $1,275 | $1,275 | $1,275 | $1,275”
  - column:Room and Board: 6161 ⟵ “Room and Board | $2,081 | $6,161 | $2,081 | $6,161”
  - column:Transportation Expense: 2514 ⟵ “Transportation Expense | $2,514 | $2,514 | $2,514 | $2,514”
  - column:Miscellaneous/Personal: 1897 ⟵ “Miscellaneous/Personal | $1,158 | $1,897 | $1,158 | $1,897”
  - column:TOTAL ESTIMATED COST: 14440 ⟵ “TOTAL ESTIMATED COST | $9,621 | $14,440 | $16,750 | $21,569”
  - column:Tuition and Fees (2): 2958 ⟵ “Tuition and Fees | $2,958 | $2,958 | $11,087 | $11,087”
  - column:Books/Supplies (2): 1275 ⟵ “Books/Supplies | $1,275 | $1,275 | $1,275 | $1,275”
  - column:Room and Board (2): 6161 ⟵ “Room and Board | $2,081 | $6,161 | $2,081 | $6,161”
  - column:Transportation Expense (2): 2514 ⟵ “Transportation Expense | $2,514 | $2,514 | $2,514 | $2,514”
  - column:Miscellaneous/Personal (2): 1897 ⟵ “Miscellaneous/Personal | $1,158 | $1,897 | $1,158 | $1,897”
  - column:TOTAL ESTIMATED COST (2): 14805 ⟵ “TOTAL ESTIMATED COST | $9,986 | $14,805 | $18,115 | $22,934”
### `d1303cf31fbaae78` South Florida State College — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.southflorida.edu/current-students/financial-aid-scholarships/financial-need-calculation (sha256 2eb77503858a)
- issues: multiple_total_rows, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 12}
  - column:Tuition and Fees: 2593 ⟵ “Tuition and Fees | $2,593 | $2,593 | $9,722 | $9,722”
  - column:Books/Supplies: 1275 ⟵ “Books/Supplies | $1,275 | $1,275 | $1,275 | $1,275”
  - column:Room and Board: 2081 ⟵ “Room and Board | $2,081 | $6,161 | $2,081 | $6,161”
  - column:Transportation Expense: 2514 ⟵ “Transportation Expense | $2,514 | $2,514 | $2,514 | $2,514”
  - column:Miscellaneous/Personal: 1158 ⟵ “Miscellaneous/Personal | $1,158 | $1,897 | $1,158 | $1,897”
  - column:TOTAL ESTIMATED COST: 9621 ⟵ “TOTAL ESTIMATED COST | $9,621 | $14,440 | $16,750 | $21,569”
  - column:Tuition and Fees (2): 2958 ⟵ “Tuition and Fees | $2,958 | $2,958 | $11,087 | $11,087”
  - column:Books/Supplies (2): 1275 ⟵ “Books/Supplies | $1,275 | $1,275 | $1,275 | $1,275”
  - column:Room and Board (2): 2081 ⟵ “Room and Board | $2,081 | $6,161 | $2,081 | $6,161”
  - column:Transportation Expense (2): 2514 ⟵ “Transportation Expense | $2,514 | $2,514 | $2,514 | $2,514”
  - column:Miscellaneous/Personal (2): 1158 ⟵ “Miscellaneous/Personal | $1,158 | $1,897 | $1,158 | $1,897”
  - column:TOTAL ESTIMATED COST (2): 9986 ⟵ “TOTAL ESTIMATED COST | $9,986 | $14,805 | $18,115 | $22,934”
### `146e51d417995b97` St Petersburg College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.spcollege.edu/financial-aid (sha256 5f0914ffc3e5)
- issues: semantic_review_required, conflicting_sources:https://www.spcollege.edu:443/financial-aid/apply-for-financial-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment Are you juggling your finances? - We might be able to help.”
  - sentence: professional_judgment ⟵ “See about a Professional Judgment.”
### `74531923a40abd31` St Petersburg College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.spcollege.edu:443/financial-aid/apply-for-financial-aid/professional-judgment (sha256 05f62e53c20c)
- issues: semantic_review_required, conflicting_sources:https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-appeal,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-gpa,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/view-your-sap-status
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please note the following before starting the process: You must be eligible for federal aid either by meeting Satisfactory Academic Progress or have an approved SAP Appeal Verification must be complete if you have been selected If your request is approved, SPC does not guarantee that there will be a change in your federal financial aid eligibility.”
### `7887c41febd4f990` St Petersburg College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.spcollege.edu:443/financial-aid/apply-for-financial-aid/professional-judgment (sha256 05f62e53c20c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances (formerly Change in Circumstances) You can ask for a review if your financial circumstances have changed and your situation is different from the norm.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances (formerly Dependency Override) You can ask for a review of your dependency status.”
### `7f0f0d77a5103c10` St Petersburg College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/view-your-sap-status (sha256 46cb59cb03f4)
- issues: semantic_review_required, conflicting_sources:https://www.spcollege.edu:443/financial-aid/apply-for-financial-aid/professional-judgment,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-appeal,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-gpa
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “SAP appeals If you have submitted an appeal, you can check the status in your To Do List.”
  - sentence: sap_appeal ⟵ “If the SAP Appeal Checklist Item has disappeared from your To Do List, the decision has been made and you will be notified by SPC student email.”
  - sentence: sap_appeal ⟵ “Probation (Academic Plan) You are placed on Financial Aid Probation after submitting a written SAP appeal and the appeal has been approved.”
  - sentence: sap_appeal ⟵ “Apply to SPC Apply for Aid Check Your Aid Ask Financial Aid Satisfactory Academic Progress (SAP) View Your SAP Status SAP Appeal SAP GPA SAP Completion Ratio SAP Maximum Time Frame Student Success Plan Request Information Apply to SPC Connect Connect Alumni Network Careers at SPC Contact SPC Events Foundation Newsroom Resources Resources Academic Calendar Accessibility Services Safety and Security”
### `ad7d3afd69016020` St Petersburg College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-gpa (sha256 4d84f508b482)
- issues: semantic_review_required, conflicting_sources:https://www.spcollege.edu:443/financial-aid/apply-for-financial-aid/professional-judgment,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-appeal,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/view-your-sap-status
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Apply to SPC Apply for Aid Check Your Aid Ask Financial Aid Satisfactory Academic Progress (SAP) View Your SAP Status SAP Appeal SAP GPA SAP Completion Ratio SAP Maximum Time Frame Student Success Plan Request Information Apply to SPC Connect Connect Alumni Network Careers at SPC Contact SPC Events Foundation Newsroom Resources Resources Academic Calendar Accessibility Services Safety and Security”
### `b5bb5c321ddf1937` St Petersburg College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress (sha256 c1000dcf4c45)
- issues: semantic_review_required, conflicting_sources:https://www.spcollege.edu:443/financial-aid/apply-for-financial-aid/professional-judgment,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-appeal,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-gpa,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/view-your-sap-status
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Apply to SPC Apply for Aid Check Your Aid Ask Financial Aid Satisfactory Academic Progress (SAP) View Your SAP Status SAP Appeal SAP GPA SAP Completion Ratio SAP Maximum Time Frame Student Success Plan Request Information Apply to SPC Connect Connect Alumni Network Careers at SPC Contact SPC Events Foundation Newsroom Resources Resources Academic Calendar Accessibility Services Safety and Security”
### `d6d6dc8425a7c875` St Petersburg College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.spcollege.edu:443/financial-aid/types-of-financial-aid/scholarships/institutional-scholarships/spc-promise-scholarship (sha256 a9355321d6e4)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If you have experienced extenuating circumstances beyond your control that prevented you from satisfying the requirements to maintain Satisfactory Academic Progress (SAP), you may appeal that status.”
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS (SAP) APPEAL If you are ineligible due to not meeting SAP and have experienced extenuating circumstances beyond your control that prevented you from satisfying the requirements to maintain (SAP), you may appeal that status.”
  - sentence: sap_appeal ⟵ “No, students on SAP suspension are required to submit an SAP appeal and get on an academic plan before being considered eligible for the SPC Promise Program.”
### `d9a856f507d3efcd` St Petersburg College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-appeal (sha256 5b0c6b8cf837)
- issues: semantic_review_required, conflicting_sources:https://www.spcollege.edu:443/financial-aid/apply-for-financial-aid/professional-judgment,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/sap-gpa,https://www.spcollege.edu:443/financial-aid/keeping-your-financial-aid/satisfactory-academic-progress/view-your-sap-status
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal || St.”
  - sentence: sap_appeal ⟵ “If you have experienced extenuating circumstances beyond your control that prevented you from satisfying the requirements to maintain Satisfactory Academic Progress (SAP), you may appeal that status.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal - Complete this form if you are on Financial Aid Suspension for Financial Aid GPA, Completion Ratio, Maximum Time Frame or a failed Student Success Plan (formerly called Financial Aid Academic Plan), and are submitting an appeal to a previously denied SAP appeal.”
  - sentence: sap_appeal ⟵ “SAP Appeal Additional Documentation - Use this form to submit any additional documentation.”
  - sentence: sap_appeal ⟵ “Student Success Plan If your SAP Appeal is approved, you must meet with an Academic Advisor to assist you with developing a Student Success Plan that will get you back on track to maintaining academic progress and completing your current academic program of study.”
  - sentence: sap_appeal ⟵ “Once the plan has been finalized, you must "accept" the plan in MySPC before the SAP Appeal process can be completed and your financial aid can be reinstated.”
### `f38ad14cf6f59c23` St Petersburg College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.spcollege.edu:443/financial-aid/apply-for-financial-aid/professional-judgment (sha256 05f62e53c20c)
- issues: semantic_review_required, conflicting_sources:https://www.spcollege.edu/financial-aid
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “What is Professional Judgment?”
  - sentence: professional_judgment ⟵ “There are two types of Professional Judgments: Special Circumstances (formerly Change in Circumstances) Unusual Circumstances (formerly Dependency Override) Decisions regarding adjustment(s) are final and cannot be appealed to the Department of Education.”
  - sentence: professional_judgment ⟵ “SPC is not limited to these examples, nor are we required to use Professional Judgment in these circumstances. tuition expenses at an elementary or secondary school medical or dental expenses paid, but not covered by insurance unusually high child care costs recent unemployment (student, spouse, and/or parent of dependent student) Supporting documentation by a third party, if possible, must relate”
### `mca50e6b657a378b` St Petersburg College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.spcollege.edu:443/Documents/community/community-resources/high-school-programs/dual-enrollment/High-School-Options-Chart.pdf (sha256 46adf572c037)
- issues: multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - college_gpa_to_continue: 2.0 ⟵ “To remain in the Dual Enrollment program, you must maintain a college GPA of 2.0 (C average).”
  - eligibility_tier: 3.0 ⟵ “Academics                     High school GPA of 3.0+ (academic)     High school GPA of 3.0+                High school GPA of 3.0+ (academic)”
### `daec9b83fa0a0564` St. John Vianney College Seminary — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sjvcs.edu/about-us/admissions-and-tuition (sha256 3f455f0a722c)
- issues: arrangement_unlabeled, stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 5}
  - column:Tuition and Fees:: 25500 ⟵ “Tuition and Fees: | $25,500 | $25,500”
  - column:Room and Board:: 14500 ⟵ “Room and Board: | $14,500 | $14,500”
  - column:Books:: 800 ⟵ “Books: | $800 | $800”
  - column:New Student Experience:: 2000 ⟵ “New Student Experience: | $2,000 | N/A”
  - column:Total:: 42800 ⟵ “Total: | $42,800 | $40,800”
  - column:Tuition and Fees:: 25500 ⟵ “Tuition and Fees: | $25,500 | $25,500”
  - column:Room and Board:: 14500 ⟵ “Room and Board: | $14,500 | $14,500”
  - column:Books:: 800 ⟵ “Books: | $800 | $800”
  - column:Total:: 40800 ⟵ “Total: | $42,800 | $40,800”
### `234f427922935f9f` St. Thomas University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stu.edu/cost-of-attendance/ (sha256 d0acc538014d)
- issues: components_do_not_reconcile, conflicting_sources:https://www.stu.edu/tuition-and-fees/
- checks: {"columns": 3, "components_reconcile": false, "rows": 8}
  - on_campus:Tuition & Fees: 34544 ⟵ “Tuition & Fees | $34,544 | $34,544 | $34,544”
  - on_campus:Books & Supplies: 1584 ⟵ “Books & Supplies | $1,584 | $1,584 | $1,584”
  - on_campus:Housing Allowance: 7830 ⟵ “Housing Allowance | $7,830 | $12,424 | $2000”
  - on_campus:Food Allowance: 5850 ⟵ “Food Allowance | $5,850 | $5,380 | $1,280”
  - on_campus:Estimated Loan Fees: 70 ⟵ “Estimated Loan Fees | $70 | $70 | $70”
  - on_campus:Transportation: 1815 ⟵ “Transportation | $1,815 | $3,630 | $3,630”
  - on_campus:Personal: 3201 ⟵ “Personal | $3,201 | $3,201 | $3,201”
  - on_campus:TOTAL COA: 54904 ⟵ “TOTAL COA | $54,904 | $60,843 | $46,319”
  - off_campus_not_with_family:Tuition & Fees: 34544 ⟵ “Tuition & Fees | $34,544 | $34,544 | $34,544”
  - off_campus_not_with_family:Books & Supplies: 1584 ⟵ “Books & Supplies | $1,584 | $1,584 | $1,584”
  - off_campus_not_with_family:Housing Allowance: 12424 ⟵ “Housing Allowance | $7,830 | $12,424 | $2000”
  - off_campus_not_with_family:Food Allowance: 5380 ⟵ “Food Allowance | $5,850 | $5,380 | $1,280”
  - off_campus_not_with_family:Estimated Loan Fees: 70 ⟵ “Estimated Loan Fees | $70 | $70 | $70”
  - off_campus_not_with_family:Transportation: 3630 ⟵ “Transportation | $1,815 | $3,630 | $3,630”
  - off_campus_not_with_family:Personal: 3201 ⟵ “Personal | $3,201 | $3,201 | $3,201”
  - off_campus_not_with_family:TOTAL COA: 60843 ⟵ “TOTAL COA | $54,904 | $60,843 | $46,319”
  - with_parents_or_family:Tuition & Fees: 34544 ⟵ “Tuition & Fees | $34,544 | $34,544 | $34,544”
  - with_parents_or_family:Books & Supplies: 1584 ⟵ “Books & Supplies | $1,584 | $1,584 | $1,584”
  - with_parents_or_family:Housing Allowance: 2000 ⟵ “Housing Allowance | $7,830 | $12,424 | $2000”
  - with_parents_or_family:Food Allowance: 1280 ⟵ “Food Allowance | $5,850 | $5,380 | $1,280”
  - with_parents_or_family:Estimated Loan Fees: 70 ⟵ “Estimated Loan Fees | $70 | $70 | $70”
  - with_parents_or_family:Transportation: 3630 ⟵ “Transportation | $1,815 | $3,630 | $3,630”
  - with_parents_or_family:Personal: 3201 ⟵ “Personal | $3,201 | $3,201 | $3,201”
  - with_parents_or_family:TOTAL COA: 46319 ⟵ “TOTAL COA | $54,904 | $60,843 | $46,319”
### `be620b2a80cf8c0c` St. Thomas University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stu.edu/tuition-and-fees/ (sha256 d05b9b7c33fc)
- issues: implausible_amount, conflicting_sources:https://www.stu.edu/cost-of-attendance/
- checks: {"columns": 1, "rows": 8}
  - column:Late Registration Fee (after 1st week): 150 ⟵ “Late Registration Fee (after 1st week) | $150 | Flat Rate”
  - column:Diploma replacement: 150 ⟵ “Diploma replacement | $150 | Per Diploma”
  - column:ID Replacement: 10 ⟵ “ID Replacement | $10 | Per ID Card”
  - column:Portfolio Assessment fee (9 credit max.): 836 ⟵ “Portfolio Assessment fee (9 credit max.) | $836 | Flat Rate”
  - column:Returned check fee & Credit Card chargeback fee: 50 ⟵ “Returned check fee & Credit Card chargeback fee | $50 | Flat Rate”
  - column:Late / Non-Payment Fee: 150 ⟵ “Late / Non-Payment Fee | $150 | Flat Rate”
  - column:Add/Drop Courses (after the first week of term/semester): 10 ⟵ “Add/Drop Courses (after the first week of term/semester) | $10 | Flat Rate”
  - column:Tuition payment plan: 80 ⟵ “Tuition payment plan | $80 | Per Term”
### `656a0e8bf890045b` State College of Florida-Manatee-Sarasota — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.scf.edu/admissions/tuition/cost-of-attendance/ (sha256 0e1f8e8c9ca5)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2024-25
- checks: {"columns": 4, "rows": 9}
  - column:Tuition & fees(Lower Division): 9276 ⟵ “Tuition & fees(Lower Division) | $9,276 | $6,957 | $4,638 | $2,319”
  - column:Tuition & fees(Upper Division): 10610 ⟵ “Tuition & fees(Upper Division) | $10,610 | $7,958 | $5,305 | $2,652”
  - column:Books: 1200 ⟵ “Books | $1,200 | $900 | $600 | –”
  - column:Living Expenses(Housing & food): 21375 ⟵ “Living Expenses(Housing & food) | $21,375 | $21,375 | $21,375 | –”
  - column:Transportation: 2144 ⟵ “Transportation | $2,144 | $1,608 | $1,072 | $536”
  - column:Miscellaneous: 1920 ⟵ “Miscellaneous | $1,920 | $1,920 | $1,920 | –”
  - column:Loan fee: 36 ⟵ “Loan fee | $36 | $36 | $36 | –”
  - column:Total(Lower division): 35951 ⟵ “Total(Lower division) | $35,951 | $32,796 | $29,641 | $2,855”
  - column:Total (Upper Division): 37285 ⟵ “Total (Upper Division) | $37,285 | $33,797 | $30,308 | $3,188”
  - column:Tuition & fees(Lower Division): 6957 ⟵ “Tuition & fees(Lower Division) | $9,276 | $6,957 | $4,638 | $2,319”
  - column:Tuition & fees(Upper Division): 7958 ⟵ “Tuition & fees(Upper Division) | $10,610 | $7,958 | $5,305 | $2,652”
  - column:Books: 900 ⟵ “Books | $1,200 | $900 | $600 | –”
  - column:Living Expenses(Housing & food): 21375 ⟵ “Living Expenses(Housing & food) | $21,375 | $21,375 | $21,375 | –”
  - column:Transportation: 1608 ⟵ “Transportation | $2,144 | $1,608 | $1,072 | $536”
  - column:Miscellaneous: 1920 ⟵ “Miscellaneous | $1,920 | $1,920 | $1,920 | –”
  - column:Loan fee: 36 ⟵ “Loan fee | $36 | $36 | $36 | –”
  - column:Total(Lower division): 32796 ⟵ “Total(Lower division) | $35,951 | $32,796 | $29,641 | $2,855”
  - column:Total (Upper Division): 33797 ⟵ “Total (Upper Division) | $37,285 | $33,797 | $30,308 | $3,188”
  - column:Tuition & fees(Lower Division): 4638 ⟵ “Tuition & fees(Lower Division) | $9,276 | $6,957 | $4,638 | $2,319”
  - column:Tuition & fees(Upper Division): 5305 ⟵ “Tuition & fees(Upper Division) | $10,610 | $7,958 | $5,305 | $2,652”
  - column:Books: 600 ⟵ “Books | $1,200 | $900 | $600 | –”
  - column:Living Expenses(Housing & food): 21375 ⟵ “Living Expenses(Housing & food) | $21,375 | $21,375 | $21,375 | –”
  - column:Transportation: 1072 ⟵ “Transportation | $2,144 | $1,608 | $1,072 | $536”
  - column:Miscellaneous: 1920 ⟵ “Miscellaneous | $1,920 | $1,920 | $1,920 | –”
  - column:Loan fee: 36 ⟵ “Loan fee | $36 | $36 | $36 | –”
  - … 7 more rows
### `6df0aeb65ce09b04` State College of Florida-Manatee-Sarasota — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.scf.edu/admissions/tuition/cost-of-attendance/ (sha256 0e1f8e8c9ca5)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2024-25
- checks: {"columns": 4, "rows": 9}
  - column:Tuition & fees*(Lower Division): 2460 ⟵ “Tuition & fees*(Lower Division) | $2,460 | $1,845 | $1,230 | $615”
  - column:Tuition & fees*(Upper Division): 9276 ⟵ “Tuition & fees*(Upper Division) | $9,276 | $6,958 | $4,638 | $2,320”
  - column:Books & Course Materials: 1200 ⟵ “Books & Course Materials | $1,200 | $900 | $600 | –”
  - column:Living Expenses(Housing & food): 21375 ⟵ “Living Expenses(Housing & food) | $21,375 | $21,375 | $21,375 | –”
  - column:Transportation: 2144 ⟵ “Transportation | $2,144 | $1,608 | $1,072 | $536”
  - column:Miscellaneous: 1920 ⟵ “Miscellaneous | $1,920 | $1,920 | $1,920 | –”
  - column:Loan fee: 36 ⟵ “Loan fee | $36 | $36 | $36 | –”
  - column:Total(Lower division): 29135 ⟵ “Total(Lower division) | $29,135 | $27,684 | $26,233 | $1,151”
  - column:Total (Upper Division): 35951 ⟵ “Total (Upper Division) | $35,951 | $32,797 | $29,641 | $2,856”
  - column:Tuition & fees*(Lower Division): 1845 ⟵ “Tuition & fees*(Lower Division) | $2,460 | $1,845 | $1,230 | $615”
  - column:Tuition & fees*(Upper Division): 6958 ⟵ “Tuition & fees*(Upper Division) | $9,276 | $6,958 | $4,638 | $2,320”
  - column:Books & Course Materials: 900 ⟵ “Books & Course Materials | $1,200 | $900 | $600 | –”
  - column:Living Expenses(Housing & food): 21375 ⟵ “Living Expenses(Housing & food) | $21,375 | $21,375 | $21,375 | –”
  - column:Transportation: 1608 ⟵ “Transportation | $2,144 | $1,608 | $1,072 | $536”
  - column:Miscellaneous: 1920 ⟵ “Miscellaneous | $1,920 | $1,920 | $1,920 | –”
  - column:Loan fee: 36 ⟵ “Loan fee | $36 | $36 | $36 | –”
  - column:Total(Lower division): 27684 ⟵ “Total(Lower division) | $29,135 | $27,684 | $26,233 | $1,151”
  - column:Total (Upper Division): 32797 ⟵ “Total (Upper Division) | $35,951 | $32,797 | $29,641 | $2,856”
  - column:Tuition & fees*(Lower Division): 1230 ⟵ “Tuition & fees*(Lower Division) | $2,460 | $1,845 | $1,230 | $615”
  - column:Tuition & fees*(Upper Division): 4638 ⟵ “Tuition & fees*(Upper Division) | $9,276 | $6,958 | $4,638 | $2,320”
  - column:Books & Course Materials: 600 ⟵ “Books & Course Materials | $1,200 | $900 | $600 | –”
  - column:Living Expenses(Housing & food): 21375 ⟵ “Living Expenses(Housing & food) | $21,375 | $21,375 | $21,375 | –”
  - column:Transportation: 1072 ⟵ “Transportation | $2,144 | $1,608 | $1,072 | $536”
  - column:Miscellaneous: 1920 ⟵ “Miscellaneous | $1,920 | $1,920 | $1,920 | –”
  - column:Loan fee: 36 ⟵ “Loan fee | $36 | $36 | $36 | –”
  - … 7 more rows
### `d68e51cec762dd22` State College of Florida-Manatee-Sarasota — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.scf.edu/admissions/veterans/ (sha256 fdecea225403)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 6}
  - column:Non-Resident Tuition and Fees: 4500.0 ⟵ “Non-Resident Tuition and Fees | $4500.00”
  - column:Post 9/11 GI Bill® Covers (instate cost): 1500.0 ⟵ “Post 9/11 GI Bill® Covers (instate cost) | $1500.00”
  - column:Amount Not Covered: 3000.0 ⟵ “Amount Not Covered | $3000.00”
  - column:SCF Contribution: 1500.0 ⟵ “SCF Contribution | $1500.00”
  - column:Yellow Ribbon Contribution: 1500.0 ⟵ “Yellow Ribbon Contribution | $1500.00”
  - column:Student Cost: 0 ⟵ “Student Cost | $0*”
### `m3b09ec1d0868fe4` State College of Florida-Manatee-Sarasota — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.scf.edu/wp-content/uploads/2026/08/2627_EarlyCollegeSummary.pdf (sha256 7edce7c3c586)
- issues: conflicting_values:max_credit_hours_per_term, multicolumn_layout_review
- checks: {"fields": [], "merged_pages": 2, "tiers": 2}
  - max_credit_hours_per_term: 11 ⟵ “Dual Enrollment enables qualified public, private, and home education students to enroll in selected college credit courses offered by SCF. Credits earned count toward both a college degree and a high school diploma. Students may enroll in up to 11 credit hours per semester in Fall and Spring and up”
  - max_credit_hours_per_term: 6 ⟵ “Dual Enrollment enables qualified public, private, and home education students to enroll in selected college credit courses offered by SCF. Credits earned count toward both a college degree and a high school diploma. Students may enroll in up to 11 credit hours per semester in Fall and Spring and up”
  - eligibility_tier: 3.3 ⟵ “Accelerated Dual Enrollment (ADE): Public Schools only; 12-15         3.3 high school GPA”
  - eligibility_tier: 2.0 ⟵ “    Students must maintain a 3.0 high school unweighted GPA and an SCF term GPA of 2.0.”
### `626a667942d1dd50` Tallahassee Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tsc.fl.edu/admissions/financial-aid/special-conditions-professional-judgment/ (sha256 f7ed0a71fbea)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “Special Conditions-Professional Judgment - Tallahassee State College Resources Email and Calendar Canvas MyTSC Workday EagleQ Zoom Employee Help Desk Academic Dates & Deadlines Student Central FAQs Faculty/Staff Intranet TSC Alerts Newsroom 25Live Policies & Procedures Apporto Need Help?”
  - sentence: professional_judgment ⟵ “Federal regulations permit Student Financial Services to administer professional judgment, on a case-by-case basis (with supporting documentation), of the situation that is beyond the student’s control.”
  - sentence: professional_judgment ⟵ “Supporting documentation includes, but is not limited to: A signed statement from the student A signed statement from the parent Court documents Death notice Unemployment verification Letters of support from counselors, ministers, lawyers, doctors Other legal documents TSC has an electronic form for professional judgments.”
  - sentence: professional_judgment ⟵ “The "Request for Professional Judgment" forms are located in Workday.”
  - sentence: professional_judgment ⟵ “Upon receipt of the "Request for Professional Judgment" form and supporting documentation, Student Financial Services will review your situation and, where appropriate, make changes to your or your family’s financial information, family size, or number in college.”
  - sentence: professional_judgment ⟵ “Professional Judgment Decision The request will be reviewed by Student Financial Services, and a response will be provided to you.”
### `b38a7163ee8cd2ae` Tallahassee Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tsc.fl.edu/admissions/financial-aid/special-conditions-professional-judgment/ (sha256 f7ed0a71fbea)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Students from regions beyond the normal service region for TSC may receive a budget increase by verbal request if the increase is appropriate or if it is noticed in the financial aid file by Student Financial Services.”
### `7fb308688a23ae4c` Tallahassee Community College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.tsc.fl.edu/admissions/financial-aid/ (sha256 4113477b4380)
- issues: implausible_amount, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - on_campus:Tuition Costs (including non-resident fee): 76.8 ⟵ “Tuition Costs (including non-resident fee) | $76.80 | $307.20”
  - on_campus:Student Activities Fee: 5.35 ⟵ “Student Activities Fee | $5.35 | $5.35”
  - on_campus:Financial Aid Fee: 3.84 ⟵ “Financial Aid Fee | $3.84 | $15.36”
  - on_campus:Capital Improvement Fee: 11.0 ⟵ “Capital Improvement Fee | $11.00 | $44.00”
  - on_campus:Technology Fee: 3.84 ⟵ “Technology Fee | $3.84 | $15.36”
### `893be221bf3c8267` Tallahassee Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.tsc.fl.edu/admissions/financial-aid/ (sha256 4113477b4380)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - on_campus:Tuition Costs (including non-resident fee): 307.2 ⟵ “Tuition Costs (including non-resident fee) | $76.80 | $307.20”
  - on_campus:Student Activities Fee: 5.35 ⟵ “Student Activities Fee | $5.35 | $5.35”
  - on_campus:Financial Aid Fee: 15.36 ⟵ “Financial Aid Fee | $3.84 | $15.36”
  - on_campus:Capital Improvement Fee: 44.0 ⟵ “Capital Improvement Fee | $11.00 | $44.00”
  - on_campus:Technology Fee: 15.36 ⟵ “Technology Fee | $3.84 | $15.36”
### `8426e7ef8e96aebd` Tallahassee Community College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_title)
- source: https://www.tsc.fl.edu/media/divisions/admissions-and-recruiting/dual-enrollment/View-Additional-Test-Score-Requirements.pdf (sha256 e5cb7cabca61)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “(Performance in public high school coursework includes an unweighted GPA of 3.0 or better plus”
### `925420aad518cc9b` Tallahassee Community College — credit_policies 2024-25 · policy_kind=IB [new] (labeled_in_source)
- source: https://www.tsc.fl.edu/academics/credit-for-prior-learning/ (sha256 727649249dcf)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 34, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|BSC1005 & BSC1005L]:  ⟵ “Biology | BSC1005 & BSC1005L | BSC1005 & BSC1005L and BSC2010 & BSC2010L”
  - equivalencies[IB-BIOLOGY-SL|BSC1005 & BSC1005L]:  ⟵ “Biology (SL)- Effective for exams taken after 9/23/20 | BSC1005 & BSC1005L | BSC1005 & BSC1005L”
  - equivalencies[IB-BIOLOGY-HL|BSC1005 & BSC1005L and BSC2010 & BSC2010L]:  ⟵ “Biology (HL)- Effective for exams taken after 9/23/20 | BSC1005 & BSC1005L and BSC2010 & BSC2010L | BSC1005 & BSC1005L and BSC2010 & BSC2010L”
  - equivalencies[IB-BUSINESS-MANAGEMENT|GEB1011]:  ⟵ “Business and Management | GEB1011 | GEB1011 and Management course determined by institution.”
  - equivalencies[IB-CHEMISTRY|CHM1020 & CHM1030L]:  ⟵ “Chemistry | CHM1020 & CHM1030L | CHM1020, CHM1030L, CHM1045, CHM1045L”
  - equivalencies[IB-COMPUTER-SCIENCE|CGS2100]:  ⟵ “Computer Science | CGS2100 | CGS2100 & COP2220”
  - equivalencies[IB-ECONOMICS|SSI9000]:  ⟵ “Economics | SSI9000 | ECO2013 & ECO2023”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|ISC9000]:  ⟵ “Environmental Systems | ISC9000 | EVR1001 & ISC9000”
  - equivalencies[IB-FILM|FIL2000]:  ⟵ “Film Studies | FIL2000 | FIL2000 and Film elective”
  - equivalencies[IB-FRENCH|FRE1121]:  ⟵ “French: Language B | FRE1121 | FRE1121 & FL9000B”
  - equivalencies[IB-GEOGRAPHY|GEA2000]:  ⟵ “Geography | GEA2000 | GEA2000 & GEO1400”
  - equivalencies[IB-GERMAN|GER1121]:  ⟵ “German | GER1121 | GER1121 & GRE1121B”
  - equivalencies[IB-GLOBAL-POLITICS-SL|INR2002]:  ⟵ “Global Politics (SL) | INR2002 | INR2002”
  - equivalencies[IB-GLOBAL-POLITICS-HL|INR 2002]:  ⟵ “Global Politics (HL) | INR 2002 | INR2002 & CPO2001”
  - equivalencies[IB-HISTORY|WOH2022]:  ⟵ “History | WOH2022 | WOH2022”
  - equivalencies[IB-HISTORY-SL|WOH2022]:  ⟵ “History (SL) | WOH2022 | WOH2022”
  - equivalencies[IB-HISTORY-HL|WOH2022]:  ⟵ “History (HL): History of Africa and the Middle East | WOH2022 | WOH2021 & WOH2022”
  - equivalencies[IB-HISTORY-HL|WOH2022]:  ⟵ “History (HL): History of Americas | WOH2022 | WOH2022 and AMH2010 or AMH2020”
  - equivalencies[IB-HISTORY|No equivalent]:  ⟵ “Islamic History | No equivalent | No equivalent”
  - equivalencies[IB-LATIN|LAT1121]:  ⟵ “Latin | LAT1121 | LAT1121 & FL9000B”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|MAT1033]:  ⟵ “Mathematics: Analysis and Approaches SL | MAT1033 | MAT1033 & MGF1130”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|MAC1105]:  ⟵ “Mathematics: Analysis and Approaches HL | MAC1105 | MAC1105 & MAC2233 or MAC1105 & MAC1140”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-SL|MAC1105]:  ⟵ “Mathematics: Applications and Interpretation SL | MAC1105 | MAC1140 & MAC2233 or MAC1140 & MAC1114”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|MAC1114]:  ⟵ “Mathematics: Applications and Interpretation HL | MAC1114 | MAC1140 & MAC2311 or MAC2233 & MAC1114”
  - equivalencies[IB-MUSIC|MUL2010]:  ⟵ “Music | MUL2010 | MUL2010”
  - … 11 more rows
### `a7cff9b9af5c2b00` Tallahassee Community College — credit_policies 2024-25 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.tsc.fl.edu/academics/credit-for-prior-learning/ (sha256 727649249dcf)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.tsc.fl.edu/media/divisions/admissions-and-recruiting/forms/TSC-Credit-by-Exam-Fall-2026.pdf
- checks: {"distinct_exams": 35, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|ART2101C (3 credits)]:  ⟵ “2-D Art and Design | ART2101C (3 credits) | ART2101C (3 credits) | ART2101C (3 credits)”
  - equivalencies[AP-3-D-ART-DESIGN|ART2103C (3 credits)]:  ⟵ “3-D Art and Design | ART2103C (3 credits) | ART2103C (3 credits) | ART2103C (3 credits)”
  - equivalencies[AP-ART-HISTORY|ARH2000 (3 credits)]:  ⟵ “Art History (exams taken before 5/16/18) | ARH2000 (3 credits) | ARH2050 & ARH2051 (6 credits) | ARH2050 & ARH2051 (6 credits)”
  - equivalencies[AP-ART-HISTORY|ARH2000 (3 credits)]:  ⟵ “Art History (exams taken after 5/16/18) | ARH2000 (3 credits) | ARH2000 & ARH2050 or ARH 2000 & ARH2051 (6 credits) | ARH2000 & ARH2050 or ARH 2000 & ARH2051 (6 credits)”
  - equivalencies[AP-BIOLOGY|BSC1005 & BSC1005L (4 credits)]:  ⟵ “Biology | BSC1005 & BSC1005L (4 credits) | BSC2010 & BSC2010L (4 credits) | BSC2010, BSC2010L, BSC2011, & BSC2011L (8 credits)”
  - equivalencies[AP-CALCULUS-AB|MAC2311 (5 credits)]:  ⟵ “Calculus AB | MAC2311 (5 credits) | MAC2311 (5 credits) | MAC2311 (5 credits)”
  - equivalencies[AP-CALCULUS-BC|MAC2311 (5 credits)]:  ⟵ “Calculus BC | MAC2311 (5 credits) | MAC2311 & MAC2312 (10 credits) | MAC2311 & MAC2312 (10 credits)”
  - equivalencies[AP-CHEMISTRY|CHM1020 & CHM1030L (4 credits)]:  ⟵ “Chemistry | CHM1020 & CHM1030L (4 credits) | CHM1045 & CHM1045L (4 credits) | CHM 1045, CHM1045L, CHM1046, & CHM1046L (8 credits)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|FL90001 (3 credits)]:  ⟵ “Chinese Language and Culture | FL90001 (3 credits) | FL90001 & FL90002 (6 credits) | FL90001 & FL90002 (6 credits)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|COP2800 (3 credits)]:  ⟵ “Computer Science A | COP2800 (3 credits) | COP2800 (3 credits) | COP2800 (3 credits)”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|COP1000 (3 credits)]:  ⟵ “Computer Science Principles | COP1000 (3 credits) | COP1000 (3 credits) | COP1000 (3 credits)”
  - equivalencies[AP-DRAWING|ART1300C (3 credits)]:  ⟵ “Drawing | ART1300C (3 credits) | ART1300C (3 credits) | ART1300C (3 credits)”
  - equivalencies[AP-MACROECONOMICS|ECO2013 (3 credits)]:  ⟵ “Economics: Macro | ECO2013 (3 credits) | ECO2013 (3 credits) | ECO2013 (3 credits)”
  - equivalencies[AP-MICROECONOMICS|ECO2023 (3 credits)]:  ⟵ “Economics Micro | ECO2023 (3 credits) | ECO2023 (3 credits) | ECO2023 (3 credits)”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|ENC1101 (3 credits)]:  ⟵ “English Language and Composition* | ENC1101 (3 credits) | ENC1101 & ENC1102 (6 credits) | ENC1101 & ENC1102 (6 credits)”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|ENC1101 or LIT2000 (3 credits). If the student already has credit for ENC1101, then the student will receive the LIT2000.]:  ⟵ “English Literature and Composition* | ENC1101 or LIT2000 (3 credits). If the student already has credit for ENC1101, then the student will receive the LIT2000. | ENC1101 & ENC1102 or ENC1102 & LIT2000 (6 credits) | ENC1101 & ENC1102 or ENC1102 & LIT2000 (6 credits)”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|EVR1001 (3 credits)]:  ⟵ “Environmental Science | EVR1001 (3 credits) | EVR1001 (3 credits) | EVR1001 (3 credits)”
  - equivalencies[AP-EUROPEAN-HISTORY|EUH9000B]:  ⟵ “European History | EUH9000B | EUH1000 & EUH1001 (6 credits) | EUH1000 & EUH1001 (6 credits)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|FRE1120 (4 credits)]:  ⟵ “French Language & Culture | FRE1120 (4 credits) | FRE1120 & FRE1121 (8 credits) | FRE1120 & FRE1121 (8 credits)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|LIT2000 (3 credits)]:  ⟵ “French Literature | LIT2000 (3 credits) | LIT2000 & LIT2100 (6 credits) | LIT2000 & LIT2100 (6 credits)”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|FL90001 (3 credits)]:  ⟵ “German Language & Culture | FL90001 (3 credits) | FL90001 & FL90002 (6 credits) | FL90001 & FL90002 (6 credits)”
  - equivalencies[AP-HUMAN-GEOGRAPHY|GEO1400 (3 credits)]:  ⟵ “Human Geography | GEO1400 (3 credits) | GEO1400 (3 credits) | GEO1400 (3 credits)”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|FL90001 (3 credits)]:  ⟵ “Italian Language and Culture | FL90001 (3 credits) | FL90001 & FL90002 (6 credits) | FL90001 & FL90002 (6 credits)”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|FL90001 (3 credits)]:  ⟵ “Japanese Language and Culture | FL90001 (3 credits) | FL90001 & FL90002 (6 credits) | FL90001 & FL90002 (6 credits)”
  - equivalencies[AP-LATIN|FL90001 (3 credits)]:  ⟵ “Latin | FL90001 (3 credits) | FL90001 & FL90002 (6 credits) | FL90001 & FL90002 (6 credits)”
  - … 12 more rows
### `b988085f1d5b5d18` Tallahassee Community College — credit_policies 2024-25 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.tsc.fl.edu/media/divisions/admissions-and-recruiting/forms/TSC-Credit-by-Exam-Fall-2026.pdf (sha256 6c088de91961)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.tsc.fl.edu/academics/credit-for-prior-learning/
- checks: {"distinct_exams": 3, "equivalencies": 3, "rows_without_score": 0}
  - equivalencies[AP-PSYCHOLOGY|46]:  ⟵ “Lifespan Developmental Psychology             DEP2004                   46                   400”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|46]:  ⟵ “Personal Finance                              FIN1100                   46                   400”
  - equivalencies[AP-STATISTICS|48]:  ⟵ “Principles of Statistics                      STA2023                   48                   400”
### `da9f1fcf1849fbff` Tallahassee Community College — credit_policies 2024-25 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://www.tsc.fl.edu/academics/credit-for-prior-learning/ (sha256 727649249dcf)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 27, "equivalencies": 28, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|POS1041 (3 credits]:  ⟵ “American Government | POS1041 (3 credits”
  - equivalencies[CLEP-AMERICAN-LITERATURE|AML2301 (3 credits)]:  ⟵ “American Literature | AML2301 (3 credits)”
  - equivalencies[CLEP-BIOLOGY|BSC1005 (3 credits) no lab credit]:  ⟵ “Biology, General | BSC1005 (3 credits) no lab credit”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|BUL2241 (3 credits)]:  ⟵ “Business Law, Introduction to | BUL2241 (3 credits)”
  - equivalencies[CLEP-CALCULUS|MAC2233 (3 credits)]:  ⟵ “Calculus | MAC2233 (3 credits)”
  - equivalencies[CLEP-CHEMISTRY|CHM1020 (3 credits) No lab credit]:  ⟵ “Chemistry, General | CHM1020 (3 credits) No lab credit”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|ENC1101 & ENC1102 (6 credits)]:  ⟵ “College Composition | ENC1101 & ENC1102 (6 credits)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|ENC1101 & ENC1102 (6 credits); No guaranteed credit for College Composition Modular without essay portion. Recommend College Composition exam.]:  ⟵ “College Composition Modular | ENC1101 & ENC1102 (6 credits); No guaranteed credit for College Composition Modular without essay portion. Recommend College Composition exam.”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|Elective (3 credits)]:  ⟵ “Educational Psychology, Introduction to | Elective (3 credits)”
  - equivalencies[CLEP-ENGLISH-LITERATURE|ENL2000 (3 credits)]:  ⟵ “English Literature | ENL2000 (3 credits)”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|ACG 2001 (3 credits)]:  ⟵ “Financial Accounting | ACG 2001 (3 credits)”
  - equivalencies[CLEP-FRENCH-LANGUAGE|On Level I exam- FRE1120 (4 credits) On Level II exam- score of 59 earns a minimum of two semesters of Elementary Language I and II- FRE1120 & FRE1121 (8 credits). No literature credit. College Board recommended score change from 62 to 59, 12/2007.]:  ⟵ “French Language | On Level I exam- FRE1120 (4 credits) On Level II exam- score of 59 earns a minimum of two semesters of Elementary Language I and II- FRE1120 & FRE1121 (8 credits). No literature credit. College Board recommended score change from 62 to 59, 12/2007.”
  - equivalencies[CLEP-GERMAN-LANGUAGE|On Level I exam- GRE1120 (4 credits) On Level II exam- score of 60 earns a minimum of two semesters of Elementary Language I and II- GRE1120 & GRE1121 (8 credits). No literature credit. College Board recommended score change from 63 to 60, 08/2008.]:  ⟵ “German Language | On Level I exam- GRE1120 (4 credits) On Level II exam- score of 60 earns a minimum of two semesters of Elementary Language I and II- GRE1120 & GRE1121 (8 credits). No literature credit. College Board recommended score change from 63 to 60, 08/2008.”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|AMH2010 (3 credits)]:  ⟵ “History of the United States I: Early Colonization to 1877 | AMH2010 (3 credits)”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|DEP2004 (3 credits)]:  ⟵ “Human Growth and Development | DEP2004 (3 credits)”
  - equivalencies[CLEP-HUMANITIES|HUM2020 (3 credits)]:  ⟵ “Humanities | HUM2020 (3 credits)”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|CGS1000 (3 credits)]:  ⟵ “Information Systems and Computer Applications | CGS1000 (3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|ECO2013 (3 credits)]:  ⟵ “Macroeconomics, Principles of | ECO2013 (3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|MAN2021 (3 credits)]:  ⟵ “Management, Principles of | MAN2021 (3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|MAR2011 (3 credits)]:  ⟵ “Marketing, Principles of | MAR2011 (3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|ECO2023 (3 credits)]:  ⟵ “Microeconomics, Principles of | ECO2023 (3 credits)”
  - equivalencies[CLEP-PRECALCULUS|MAC1140 (3 credits)]:  ⟵ “Pre-calculus | MAC1140 (3 credits)”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|PSY2012 (3 credits)]:  ⟵ “Psychology, Introductory | PSY2012 (3 credits)”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|SYG1000 (3 credits) - SYG 1000 removed from general education core effective 2024-2025.]:  ⟵ “Sociology, Introductory | SYG1000 (3 credits) - SYG 1000 removed from general education core effective 2024-2025.”
  - equivalencies[CLEP-SPANISH-LANGUAGE|On Level I exam- SPN1120 (4 credits) On Level II exam- score of 63 earns SPN1120 & SPN1121 (8 credits). No literature credit.]:  ⟵ “Spanish Language | On Level I exam- SPN1120 (4 credits) On Level II exam- score of 63 earns SPN1120 & SPN1121 (8 credits). No literature credit.”
  - … 3 more rows
### `mca8987d5ec4f4a9` Tallahassee Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.tsc.fl.edu/media/divisions/admissions-and-recruiting/dual-enrollment/Dual-Enrollment-Brochure.pdf (sha256 97ee8a6193ef)
- issues: conflicting_values:max_credit_hours_per_term, multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - max_credit_hours_per_term: 11 ⟵ “Traditional dual enrolled students can take a maximum of 11 credit hours each semester. Early admission students can take a minimum of 12 credit hours and a maximum of 15 credit hours each semester. Special permission is required each semester for the early admission program.”
  - max_credit_hours_per_term: 15 ⟵ “Traditional dual enrolled students can take a maximum of 11 credit hours each semester. Early admission students can take a minimum of 12 credit hours and a maximum of 15 credit hours each semester. Special permission is required each semester for the early admission program.”
  - eligibility_tier: 3.0 ⟵ “organizations and academic teams      • Unweighted 3.0 high school GPA”
### `43da5cccadd83ec1` The College of the Florida Keys — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.cfk.edu/paying-for-college/tuition-estimated-costs/tuition-fees/ (sha256 8fc609526dbe)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - on_campus:Tuition: 331.11 ⟵ “Tuition | 82.78 | 331.11”
  - on_campus:Technology Fee: 16.56 ⟵ “Technology Fee | 4.14 | 16.56”
  - on_campus:Financial Aid Fee: 16.56 ⟵ “Financial Aid Fee | 4.14 | 16.56”
  - on_campus:Student Activity Fee: 8.28 ⟵ “Student Activity Fee | 8.28 | 8.28”
  - on_campus:Capital Improvement Fee: 66.22 ⟵ “Capital Improvement Fee | 9.88 | 66.22”
### `5d9b237ff99e4424` The College of the Florida Keys — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cfk.edu/paying-for-college/financial-aid/ (sha256 59a408a772bc)
- issues: residency_unknown, conflicting_sources:https://www.cfk.edu/paying-for-college/tuition-estimated-costs/cost-of-attendance/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition & fees: 2621 ⟵ “Tuition & fees | $2,621 | $2,621 | $2,621”
  - with_parents_or_family:Books & supplies: 1787 ⟵ “Books & supplies | $1,787 | $1,787 | $1,787”
  - with_parents_or_family:Room & board: 5522 ⟵ “Room & board | $5,522 | $28,798 | $15,172”
  - with_parents_or_family:Transportation: 3726 ⟵ “Transportation | $3,726 | $3,726 | $900”
  - with_parents_or_family:Personal expenses: 1868 ⟵ “Personal expenses | $1,868 | $1,868 | $1,868”
  - with_parents_or_family:Estimated total cost: 15524 ⟵ “Estimated total cost | $15,524 | $38,800 | $22,348”
  - on_campus:Tuition & fees: 2621 ⟵ “Tuition & fees | $2,621 | $2,621 | $2,621”
  - on_campus:Books & supplies: 1787 ⟵ “Books & supplies | $1,787 | $1,787 | $1,787”
  - on_campus:Room & board: 15172 ⟵ “Room & board | $5,522 | $28,798 | $15,172”
  - on_campus:Transportation: 900 ⟵ “Transportation | $3,726 | $3,726 | $900”
  - on_campus:Personal expenses: 1868 ⟵ “Personal expenses | $1,868 | $1,868 | $1,868”
  - on_campus:Estimated total cost: 22348 ⟵ “Estimated total cost | $15,524 | $38,800 | $22,348”
### `9b2d0a3e47a7cbec` The College of the Florida Keys — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.cfk.edu/paying-for-college/tuition-estimated-costs/tuition-fees/ (sha256 8fc609526dbe)
- issues: implausible_amount, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - on_campus:Tuition: 82.78 ⟵ “Tuition | 82.78 | 331.11”
  - on_campus:Technology Fee: 4.14 ⟵ “Technology Fee | 4.14 | 16.56”
  - on_campus:Financial Aid Fee: 4.14 ⟵ “Financial Aid Fee | 4.14 | 16.56”
  - on_campus:Student Activity Fee: 8.28 ⟵ “Student Activity Fee | 8.28 | 8.28”
  - on_campus:Capital Improvement Fee: 9.88 ⟵ “Capital Improvement Fee | 9.88 | 66.22”
### `9fa3aa5680886fed` The College of the Florida Keys — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.cfk.edu/paying-for-college/tuition-estimated-costs/cost-of-attendance/ (sha256 1e5896e34740)
- issues: conflicting_sources:https://www.cfk.edu/paying-for-college/financial-aid/
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition & fees: 2621 ⟵ “Tuition & fees | $2,621 | $2,621 | $2,621”
  - off_campus_not_with_family:Books & supplies: 1745 ⟵ “Books & supplies | $1,745 | $1,745 | $1,745”
  - off_campus_not_with_family:Room & board: 28798 ⟵ “Room & board | $5,393 | $28,798 | $14,623”
  - off_campus_not_with_family:Transportation: 3639 ⟵ “Transportation | $3,639 | $3,639 | $900”
  - off_campus_not_with_family:Personal expenses: 1824 ⟵ “Personal expenses | $1,824 | $1,824 | $1,824”
  - off_campus_not_with_family:Estimated total cost: 38627 ⟵ “Estimated total cost | $15,222 | $38,627 | $21,713”
### `b069f9a3c8a77f70` The College of the Florida Keys — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.cfk.edu/paying-for-college/tuition-estimated-costs/cost-of-attendance/ (sha256 1e5896e34740)
- issues: residency_unknown, conflicting_sources:https://www.cfk.edu/paying-for-college/financial-aid/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition & fees: 2621 ⟵ “Tuition & fees | $2,621 | $2,621 | $2,621”
  - with_parents_or_family:Books & supplies: 1745 ⟵ “Books & supplies | $1,745 | $1,745 | $1,745”
  - with_parents_or_family:Room & board: 5393 ⟵ “Room & board | $5,393 | $28,798 | $14,623”
  - with_parents_or_family:Transportation: 3639 ⟵ “Transportation | $3,639 | $3,639 | $900”
  - with_parents_or_family:Personal expenses: 1824 ⟵ “Personal expenses | $1,824 | $1,824 | $1,824”
  - with_parents_or_family:Estimated total cost: 15222 ⟵ “Estimated total cost | $15,222 | $38,627 | $21,713”
  - on_campus:Tuition & fees: 2621 ⟵ “Tuition & fees | $2,621 | $2,621 | $2,621”
  - on_campus:Books & supplies: 1745 ⟵ “Books & supplies | $1,745 | $1,745 | $1,745”
  - on_campus:Room & board: 14623 ⟵ “Room & board | $5,393 | $28,798 | $14,623”
  - on_campus:Transportation: 900 ⟵ “Transportation | $3,639 | $3,639 | $900”
  - on_campus:Personal expenses: 1824 ⟵ “Personal expenses | $1,824 | $1,824 | $1,824”
  - on_campus:Estimated total cost: 21713 ⟵ “Estimated total cost | $15,222 | $38,627 | $21,713”
### `ea5ee66f444bdaf1` The College of the Florida Keys — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.cfk.edu/paying-for-college/financial-aid/ (sha256 59a408a772bc)
- issues: conflicting_sources:https://www.cfk.edu/paying-for-college/tuition-estimated-costs/cost-of-attendance/
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition & fees: 2621 ⟵ “Tuition & fees | $2,621 | $2,621 | $2,621”
  - off_campus_not_with_family:Books & supplies: 1787 ⟵ “Books & supplies | $1,787 | $1,787 | $1,787”
  - off_campus_not_with_family:Room & board: 28798 ⟵ “Room & board | $5,522 | $28,798 | $15,172”
  - off_campus_not_with_family:Transportation: 3726 ⟵ “Transportation | $3,726 | $3,726 | $900”
  - off_campus_not_with_family:Personal expenses: 1868 ⟵ “Personal expenses | $1,868 | $1,868 | $1,868”
  - off_campus_not_with_family:Estimated total cost: 38800 ⟵ “Estimated total cost | $15,524 | $38,800 | $22,348”
### `1b1c471a0f4472c5` The University of Tampa — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ut.edu/admissions/financial-aid/special-circumstances-and-professional-judgment- (sha256 21d14b6c7afe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “If you have been selected for Federal Verification, a Professional Judgment cannot be processed for changes until verification is complete.”
  - sentence: professional_judgment ⟵ “The submission of a Professional Judgement request does not guarantee a change to your financial aid award.”
  - sentence: professional_judgment ⟵ “Therefore, students who already have a 0 Expected Family Contribution (EFC) do not qualify for a Professional Judgment review; they already receive the maximum amount of aid possible.”
  - sentence: professional_judgment ⟵ “The Professional Judgment is not a guarantee of additional funding.”
### `5600ba4c6a06796b` The University of Tampa — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ut.edu/admissions/financial-aid/special-circumstances-and-professional-judgment- (sha256 21d14b6c7afe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “The student must provide documentation to demonstrate the reason for the adjustment and it must relate to the special circumstances that differentiate the student.”
  - sentence: need_based_special_circumstances ⟵ “In the subject include “Change in Family Circumstances” and provide a detailed explanation of your special circumstances.”
### `5c26fe03bddbe4e3` The University of Tampa — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ut.edu/admissions/financial-aid/special-circumstances-and-professional-judgment- (sha256 21d14b6c7afe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Possible Documentation Required: Signed taxes (years to be determined by the counselor) W2s and /or 1099 forms Unemployment benefits Court or Legal Documents Death certificates Additional Documentation may be requested Changes to the Cost of Attendance (Budget Adjustment) The Cost of Attendance (COA) consists of standard school expenses (tuition, fees and books) and an estimate of a student's stan”
  - sentence: budget_increase ⟵ “In the subject include “Cost of Attendance adjustment request” and provide a detailed explanation of your actual expenses related to the Costs of Attendance.”
### `719949636d9aff04` The University of Tampa — appeals 2017-18 [new] (labeled_in_source)
- source: https://www.ut.edu/admissions/financial-aid/financial-aid-glossary (sha256 e1be8ea1978a)
- issues: stale_year_label:2017-18, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Budget Adjustment | Back to top.”
### `789cd6334ffb41db` The University of Tampa — appeals 2016-17 [new] (labeled_in_source)
- source: https://www.ut.edu/admissions/financial-aid/award-notification (sha256 3b2057fe5a46)
- issues: stale_year_label:2016-17, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals UTampa’s official Satisfactory Academic Progress (SAP) policy is maintained in the current University Catalog.”
  - sentence: sap_appeal ⟵ “Students who received a notification that they have failed to meet the minimum standards of Satisfactory Academic Progress and have extenuating circumstances (such as an accident or illness) that prevented them from being able to meet the minimum standards of Satisfactory Academic Progress may submit an appeal.”
  - sentence: sap_appeal ⟵ “Students who wish to submit an appeal for failure to meet Satisfactory Academic Progress should speak to their financial aid counselor.”
### `b0cfc20f9b4b0e62` The University of Tampa — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ut.edu/admissions/financial-aid/special-circumstances-and-professional-judgment- (sha256 21d14b6c7afe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: dependency_override ⟵ “Possible Documentation Required: Signed copy of lease Utility bills with breakdown of charges Medical documentation Receipts (grocery, computer, medical bills etc.) Additional Documentation may be requested Dependency Override Students Students who are over the age of 24, have dependents of their own, are an orphan or ward of the court or are veterans or active-duty military service members are co”
  - sentence: dependency_override ⟵ “The goal of a dependency override is to make the student independent for financial aid purposes, and remove parental information from the EFC calculation on the FAFSA.”
  - sentence: dependency_override ⟵ “Dependency overrides are rare, and documentation is essential.”
  - sentence: dependency_override ⟵ “Dependency override status change to student marital status is usually not permitted.”
  - sentence: dependency_override ⟵ “Examples of reasons to request a dependency override: Cases of parental abuse, neglect, abandonment or incarceration (with appropriate written third-party documentation) Parents cannot be located Death of the custodial parent and no other biological or adoptive parent can be reached by ordinary means Student is a political refugee Student has been a ward of the court at any time after the age of 1”
  - sentence: dependency_override ⟵ “In the subject include “Dependency Override request” and provide a detailed explanation of your circumstances related to the dependency override.”
### `d88837d2f02df167` The University of Tampa — appeals 2016-17 [new] (labeled_in_source)
- source: https://www.ut.edu/admissions/financial-aid/award-notification (sha256 3b2057fe5a46)
- issues: stale_year_label:2016-17, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Appeals Special Circumstances If your family’s financial circumstances change after you apply for aid, contact your Financial Aid counselor.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances can potentially include: Loss of income Reduced income Unusually high medical expenses Separation or divorce Loss of benefit (child support, etc.) Federally declared natural disaster The U.S.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Unusual circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (like human trafficking, refugee or asylee status, parental abandonment, or incarceration).”
  - sentence: need_based_special_circumstances ⟵ “Students should not attempt to make the changes necessary to support unusual circumstances to their FAFSA; a financial aid professional must make these changes.”
### `fb3ecd38960f89b5` The University of Tampa — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ut.edu/admissions/financial-aid/financial-aid-renewal (sha256 bd572f1c3ea1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “An SAP Appeal Questionnaire will be made available to you on Workday.”
### `8f63998968763f5e` The University of Tampa — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ut.edu/admissions/tuition-and-costs (sha256 aa3d9c6fbc10)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 10}
  - column:Tuition: 12624 ⟵ “Tuition | $12,624 | $6,312”
  - column:Fees: 100 ⟵ “Fees | $100 | $100”
  - column:Living Expenses (Housing and Food): 20000 ⟵ “Living Expenses (Housing and Food) | $20,000 | $20,000”
  - column:Personal Expenses: 5500 ⟵ “Personal Expenses | $5,500 | $5,500”
  - column:Transportation: 3000 ⟵ “Transportation | $3,000 | $3,000”
  - column:Books (8 credits/semester): 800 ⟵ “Books (8 credits/semester) | $800 | $400”
  - column:Loan Fees: 160 ⟵ “Loan Fees | $160 | $160”
  - column:Total Estimated Cost of Attendance: 42184 ⟵ “Total Estimated Cost of Attendance | $42,184 | $35,472”
  - column:Total Direct Costs: 12724 ⟵ “Total Direct Costs | $12,724 | $6,412”
  - column:Total Indirect Costs: 29460 ⟵ “Total Indirect Costs | $29,460 | $29,060”
  - column:Tuition: 6312 ⟵ “Tuition | $12,624 | $6,312”
  - column:Fees: 100 ⟵ “Fees | $100 | $100”
  - column:Living Expenses (Housing and Food): 20000 ⟵ “Living Expenses (Housing and Food) | $20,000 | $20,000”
  - column:Personal Expenses: 5500 ⟵ “Personal Expenses | $5,500 | $5,500”
  - column:Transportation: 3000 ⟵ “Transportation | $3,000 | $3,000”
  - column:Books (8 credits/semester): 400 ⟵ “Books (8 credits/semester) | $800 | $400”
  - column:Loan Fees: 160 ⟵ “Loan Fees | $160 | $160”
  - column:Total Estimated Cost of Attendance: 35472 ⟵ “Total Estimated Cost of Attendance | $42,184 | $35,472”
  - column:Total Direct Costs: 6412 ⟵ “Total Direct Costs | $12,724 | $6,412”
  - column:Total Indirect Costs: 29060 ⟵ “Total Indirect Costs | $29,460 | $29,060”
### `35ea51ad503412d2` The University of Tampa — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ut.edu/about-utampa/university-services/office-of-the-registrar/clep-credit (sha256 bbc54bb0860a)
- issues: rows_without_score
- checks: {"distinct_exams": 26, "equivalencies": 28, "rows_without_score": 28}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|None]:  ⟵ “Financial Accounting | Business | BUS TR |  |  | 4”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|None]:  ⟵ “Information Systems | Business | BUS TR |  |  | 4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “Introductory Business Law | Business | BUS TR |  |  | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|None]:  ⟵ “Principles of Macroeconomics | Economics | ECO TR | SS |  | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “Principles of Microeconomics | Economics | ECO TR | SS |  | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|None]:  ⟵ “Principles of Management | Business | BUS TR |  |  | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|None]:  ⟵ “Principles of Marketing | Business | BUS TR |  |  | 4”
  - equivalencies[CLEP-AMERICAN-LITERATURE|None]:  ⟵ “American Literature | Literature Elective | LIT TR | HFA, AA | TBH | 4”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|None]:  ⟵ “Analyzing and Interpreting Literature | Literature Elective | LIT TR | HFA, AA | TBH | 4”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | Writing and Inquiry | AWR 101 |  |  | 4”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|None]:  ⟵ “College Composition Modular | Writing and Inquiry | AWR 101 |  |  | 4”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “English Literature | Literature Elective | LIT TR | HFA, AA | TBH | 4”
  - equivalencies[CLEP-HUMANITIES|None]:  ⟵ “Humanities | Humanities Elective | HUM TR | HFA | TBH | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|None]:  ⟵ “American Government | American Government | PSC 101 | SS | SSD | 4”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|None]:  ⟵ “Introduction to Educational Psychology | Social Science Elective | SSC TR | SS | SSD | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|None]:  ⟵ “Human Growth and Development | Psychology Elective | PSY TR | SS | SSD | 4”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “Introductory Psychology | General Psychology | PSY 101 | SS | SSD | 4”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|None]:  ⟵ “Social Sciences and History | Sociology Elective | SOC TR | SS | SSD | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|None]:  ⟵ “Social Sciences and History | History Elective | HIS TR | SS | SSD | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Introduction to Sociology | Intro to Sociology (NW-IG) | SOC 100 | SS, NW (or) SS, IG | SSD | 4”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “Biology | General Biology I (1) | BIO 198/ 198L | NS-BIO | NSD | 4”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | Calculus I (1) | MAT 260 | MATH | UTMAT | 4”
  - equivalencies[CLEP-CHEMISTRY|None]:  ⟵ “Chemistry | General Chemistry I (1) | CHE 152/153L | NS-CHEM/PHY | NSD | 4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “College Algebra | College Algebra | MAT 160 | MATH | UTMAT | 4”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|None]:  ⟵ “College Mathematics | Math for Liberal Arts | MAT 155 | MATH | UTMAT | 4”
  - … 3 more rows
### `1e5b45ea8c067be1` Trinity College of Florida — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.trinitycollege.edu/dual-enrollment/ (sha256 769f7c579fb6)
- issues: conflicting_values:max_credit_hours_per_term
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 175 ⟵ “Trinity College of Florida will offer Dual Enrollment Courses at the cost of $175.00 per credit hour. (Additional costs for books and other materials may be required.)”
  - per_credit_hour_charge: 175 ⟵ “The courses are $525.00 for a 3 credit hour course, $175 per credit hour. Additional costs are the purchase of required books for the class.”
  - max_credit_hours_per_term: 9 ⟵ “Freshman and sophomores can take up to 9 credit hours per semester.  Juniors and seniors and take up to 12 credit hours per semester.”
  - max_credit_hours_per_term: 12 ⟵ “Freshman and sophomores can take up to 9 credit hours per semester.  Juniors and seniors and take up to 12 credit hours per semester.”
### `16325bed924a9e04` University of Central Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://undergrad.ucf.edu/appeals/ (sha256 db2f57a86bc7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Assignment, exam and project grades are determined based on the instructor’s professional judgment.”
### `9b6f9f75bab8c96e` University of Central Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ucf.edu/financial-aid/types/scholarships/provost/ (sha256 77f3e24db4b0)
- issues: semantic_review_required, conflicting_sources:https://www.ucf.edu/financial-aid/resources/scholarship-appeal/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You must submit a Scholarship Appeal Form and letter stating the reason(s) that you need the time away from UCF.”
### `ca8faf7f9496ad56` University of Central Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ucf.edu/financial-aid/resources/scholarship-appeal/ (sha256 abf6c0e4f5a7)
- issues: semantic_review_required, conflicting_sources:https://www.ucf.edu/financial-aid/types/scholarships/provost/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You must complete and sign the Scholarship Appeal Form.”
### `1808461447f52dfa` University of Central Florida — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ucf.edu/about-ucf/facts/ (sha256 6261b0034ab6)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Total: 43918 ⟵ “Total | $43,918”
  - column:Nonresident tuition and fees: 24076 ⟵ “Nonresident tuition and fees | $24,076”
  - column:Books: 1200 ⟵ “Books | $1,200”
  - column:Room and Board: 13412 ⟵ “Room and Board | $13,412”
  - column:Transportation: 2126 ⟵ “Transportation | $2,126”
  - column:Personal Expense: 3104 ⟵ “Personal Expense | $3,104”
### `319294a39ac6dcc3` University of Central Florida — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ucf.edu/admissions/undergraduate/tuition-aid/ (sha256 8655662be049)
- issues: conflicting_sources:https://www.ucf.edu/financial-aid/cost/,https://www.ucf.edu/online/costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 22482 ⟵ “Tuition and Fees | $22,482”
  - column:Books: 1200 ⟵ “Books | $1,200”
  - column:Housing: 8750 ⟵ “Housing | $8,750”
  - column:Food: 6170 ⟵ “Food | $6,170”
  - column:Transportation: 2126 ⟵ “Transportation | $2,126”
  - column:Personal Expenses: 3104 ⟵ “Personal Expenses | $3,104”
  - column:Total: 43832 ⟵ “Total | $43,832”
### `4b40a0c1bbdc9ffb` University of Central Florida — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.ucf.edu/online/costs/ (sha256 edf2d9c668bc)
- issues: conflicting_sources:https://www.ucf.edu/admissions/undergraduate/tuition-aid/,https://www.ucf.edu/financial-aid/cost/
- checks: {"columns": 1, "rows": 12}
  - on_campus:Tuition: 105.07 ⟵ “Tuition | 105.07 | 105.07”
  - on_campus:Non-Resident Fee: 646.48 ⟵ “Non-Resident Fee | 0.00 | 646.48”
  - on_campus:Capital Improvement Fee: 6.76 ⟵ “Capital Improvement Fee | 6.76 | 6.76”
  - on_campus:Financial Aid Fee: 5.16 ⟵ “Financial Aid Fee | 5.16 | 5.16”
  - on_campus:Non-Resident Financial Aid Fee: 32.31 ⟵ “Non-Resident Financial Aid Fee | 0.00 | 32.31”
  - on_campus:Tuition Differential: 44.2 ⟵ “Tuition Differential | 44.20 | 44.20”
  - on_campus:Distance Learning Fee: 18.0 ⟵ “Distance Learning Fee | 18.00 | 18.00”
  - on_campus:Activity & Service Fee: 0.0 ⟵ “Activity & Service Fee | 0.00 | 0.00”
  - on_campus:Transportation Access Fee: 0.0 ⟵ “Transportation Access Fee | 0.00 | 0.00”
  - on_campus:Health Fee: 0.0 ⟵ “Health Fee | 0.00 | 0.00”
  - on_campus:Athletic Fee: 0.0 ⟵ “Athletic Fee | 0.00 | 0.00”
  - on_campus:Technology Fee: 0.0 ⟵ “Technology Fee | 0.00 | 0.00”
### `70b9f997bbf3a186` University of Central Florida — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ucf.edu/financial-aid/cost/ (sha256 509c1c3f72cb)
- issues: arrangement_unlabeled, conflicting_sources:https://www.ucf.edu/admissions/undergraduate/tuition-aid/,https://www.ucf.edu/online/costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees: 24960 ⟵ “Tuition & Fees | $24,960 | $24,960 | $24,960”
  - on_campus:Books: 1200 ⟵ “Books | $1,200 | $1,200 | $1,200”
  - on_campus:Housing: 8750 ⟵ “Housing | $8,750 | $9,918 | $3,860”
  - on_campus:Food: 6170 ⟵ “Food | $6,170 | $3,970 | $3,192”
  - on_campus:Transportation: 1094 ⟵ “Transportation | $1,094 | $2,126 | $2,126”
  - on_campus:Personal Expenses: 3104 ⟵ “Personal Expenses | $3,104 | $3,104 | $3,104”
  - on_campus:Total Costs: 45278 ⟵ “Total Costs | $45,278 | $45,278 | $38,442”
  - off_campus_not_with_family:Tuition & Fees: 24960 ⟵ “Tuition & Fees | $24,960 | $24,960 | $24,960”
  - off_campus_not_with_family:Books: 1200 ⟵ “Books | $1,200 | $1,200 | $1,200”
  - off_campus_not_with_family:Housing: 9918 ⟵ “Housing | $8,750 | $9,918 | $3,860”
  - off_campus_not_with_family:Food: 3970 ⟵ “Food | $6,170 | $3,970 | $3,192”
  - off_campus_not_with_family:Transportation: 2126 ⟵ “Transportation | $1,094 | $2,126 | $2,126”
  - off_campus_not_with_family:Personal Expenses: 3104 ⟵ “Personal Expenses | $3,104 | $3,104 | $3,104”
  - off_campus_not_with_family:Total Costs: 45278 ⟵ “Total Costs | $45,278 | $45,278 | $38,442”
  - column:Tuition & Fees: 24960 ⟵ “Tuition & Fees | $24,960 | $24,960 | $24,960”
  - column:Books: 1200 ⟵ “Books | $1,200 | $1,200 | $1,200”
  - column:Housing: 3860 ⟵ “Housing | $8,750 | $9,918 | $3,860”
  - column:Food: 3192 ⟵ “Food | $6,170 | $3,970 | $3,192”
  - column:Transportation: 2126 ⟵ “Transportation | $1,094 | $2,126 | $2,126”
  - column:Personal Expenses: 3104 ⟵ “Personal Expenses | $3,104 | $3,104 | $3,104”
  - column:Total Costs: 38442 ⟵ “Total Costs | $45,278 | $45,278 | $38,442”
### `85cba6f603a838ff` University of Central Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ucf.edu/financial-aid/cost/ (sha256 509c1c3f72cb)
- issues: conflicting_sources:https://www.ucf.edu/admissions/undergraduate/tuition-aid/,https://www.ucf.edu/online/costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition & Fees: 5954 ⟵ “Tuition & Fees | $5,954”
  - on_campus:Housing: 8750 ⟵ “Housing | $8,750”
  - on_campus:Food: 6170 ⟵ “Food | $6,170”
  - on_campus:Total: 20874 ⟵ “Total | $20,874”
### `b0c19377554ea351` University of Central Florida — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.ucf.edu/online/costs/ (sha256 edf2d9c668bc)
- issues: conflicting_sources:https://www.ucf.edu/admissions/undergraduate/tuition-aid/,https://www.ucf.edu/financial-aid/cost/
- checks: {"columns": 1, "rows": 12}
  - on_campus:Tuition: 105.07 ⟵ “Tuition | 105.07 | 105.07”
  - on_campus:Non-Resident Fee: 0.0 ⟵ “Non-Resident Fee | 0.00 | 646.48”
  - on_campus:Capital Improvement Fee: 6.76 ⟵ “Capital Improvement Fee | 6.76 | 6.76”
  - on_campus:Financial Aid Fee: 5.16 ⟵ “Financial Aid Fee | 5.16 | 5.16”
  - on_campus:Non-Resident Financial Aid Fee: 0.0 ⟵ “Non-Resident Financial Aid Fee | 0.00 | 32.31”
  - on_campus:Tuition Differential: 44.2 ⟵ “Tuition Differential | 44.20 | 44.20”
  - on_campus:Distance Learning Fee: 18.0 ⟵ “Distance Learning Fee | 18.00 | 18.00”
  - on_campus:Activity & Service Fee: 0.0 ⟵ “Activity & Service Fee | 0.00 | 0.00”
  - on_campus:Transportation Access Fee: 0.0 ⟵ “Transportation Access Fee | 0.00 | 0.00”
  - on_campus:Health Fee: 0.0 ⟵ “Health Fee | 0.00 | 0.00”
  - on_campus:Athletic Fee: 0.0 ⟵ “Athletic Fee | 0.00 | 0.00”
  - on_campus:Technology Fee: 0.0 ⟵ “Technology Fee | 0.00 | 0.00”
### `c71de55c4280ec65` University of Central Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ucf.edu/admissions/undergraduate/tuition-aid/ (sha256 8655662be049)
- issues: conflicting_sources:https://www.ucf.edu/financial-aid/cost/,https://www.ucf.edu/online/costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 5954 ⟵ “Tuition and Fees | $5,954”
  - column:Books: 1200 ⟵ “Books | $1,200”
  - column:Housing: 8750 ⟵ “Housing | $8,750”
  - column:Food: 6170 ⟵ “Food | $6,170”
  - column:Transportation: 1094 ⟵ “Transportation | $1,094”
  - column:Personal Expenses: 3104 ⟵ “Personal Expenses | $3,104”
  - column:Total: 26272 ⟵ “Total | $26,272”
### `f874d194c725ca3e` University of Central Florida — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.ucf.edu/about-ucf/facts/ (sha256 6261b0034ab6)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Total: 26210 ⟵ “Total | $26,210”
  - column:Tuition and fees: 6368 ⟵ “Tuition and fees | $6,368”
  - column:Books: 1200 ⟵ “Books | $1,200”
  - column:Room and Board: 13412 ⟵ “Room and Board | $13,412”
  - column:Transportation: 2126 ⟵ “Transportation | $2,126”
  - column:Personal Expense: 3104 ⟵ “Personal Expense | $3,104”
### `2eaa5a709a6a0c44` University of Florida — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/process/additional-information/satisfactory-academic-progress-policy/ (sha256 21558c264780)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Bright Futures will not be disbursed or will be repaid for courses listed in a Satisfactory Academic Progress Appeal as not required for a student’s degree.”
  - sentence: sap_appeal ⟵ “Other Categories Students enrolled in curricula not specifically addressed in this policy must petition the SAP Appeals Committee to continue to receive financial aid. » top Facebook Icon Twitter Icon Instagram Icon Youtube Icon Contact Us Student Financial Aid and Scholarships S-107 Criser Hall P.O.”
### `459648c01f0f9d0e` University of Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.admissions.ufl.edu/cost-and-aid/scholarships (sha256 cc30060ca590)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 1, "sentences": 1}
  - sentence: competing_offer_review ⟵ “No, UF cannot match offers made by other colleges or universities and there is no scholarship appeal process.”
### `aea7d275f48f0163` University of Florida — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/contact-sfa/message/ (sha256 839535924e7c)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “SFA recognizes that each student’s financial situation is unique and makes every effort to develop policies and procedures that treat each student fairly and equitably while taking into account unusual circumstances.”
### `1231e7b7cad6b235` University of Florida — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 8906f7143e89)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - off_campus_not_with_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - off_campus_not_with_family:Living Expenses: 12615 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 24180 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
  - with_parents_or_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - with_parents_or_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - with_parents_or_family:Living Expenses: 4560 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16125 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
  - on_campus:*Tuition / Fees: 2550 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - on_campus:Books, Course Materials, Supplies, Equipment: 546 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - on_campus:Transportation: 550 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - on_campus:Living Expenses: 3990 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - on_campus:Miscellaneous Personal Expenses: 667 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8313 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
### `27c793d119035000` University of Florida — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/innovation-academy-cost/ (sha256 53c01f0b488b)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $6,380 | $30,900”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235”
  - off_campus_not_with_family:Transportation: 1380 ⟵ “Transportation | 1,380 | 1,380 | 1,380”
  - off_campus_not_with_family:Living Expenses: 10298 ⟵ “Living Expenses | 10,298 | 3,670 | 10,298”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1784 ⟵ “Miscellaneous Personal Expenses | 1,784 | 1,784 | 1,784”
  - off_campus_not_with_family:Federal Student Loan Fees: 38 ⟵ “Federal Student Loan Fees | 38 | 38 | 38”
  - off_campus_not_with_family:Total Budget: 21115 ⟵ “Total Budget | $21,115 | $14,487 | $45,635”
  - with_parents_or_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $6,380 | $30,900”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235”
  - with_parents_or_family:Transportation: 1380 ⟵ “Transportation | 1,380 | 1,380 | 1,380”
  - with_parents_or_family:Living Expenses: 3670 ⟵ “Living Expenses | 10,298 | 3,670 | 10,298”
  - with_parents_or_family:Miscellaneous Personal Expenses: 1784 ⟵ “Miscellaneous Personal Expenses | 1,784 | 1,784 | 1,784”
  - with_parents_or_family:Federal Student Loan Fees: 38 ⟵ “Federal Student Loan Fees | 38 | 38 | 38”
  - with_parents_or_family:Total Budget: 14487 ⟵ “Total Budget | $21,115 | $14,487 | $45,635”
### `2cf6c3683779686b` University of Florida — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 419c871ab809)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - off_campus_not_with_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - off_campus_not_with_family:Living Expenses: 12615 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 24180 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
  - with_parents_or_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - with_parents_or_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - with_parents_or_family:Living Expenses: 4560 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16125 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
  - on_campus:*Tuition / Fees: 2550 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - on_campus:Books, Course Materials, Supplies, Equipment: 546 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - on_campus:Transportation: 550 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - on_campus:Living Expenses: 3990 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - on_campus:Miscellaneous Personal Expenses: 667 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8313 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
### `5f80399a86f4d2a2` University of Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 419c871ab809)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 25830 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - with_parents_or_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - with_parents_or_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - with_parents_or_family:Living Expenses: 4600 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16240 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - on_campus:*Tuition / Fees: 2580 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - on_campus:Books, Course Materials, Supplies, Equipment: 466 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - on_campus:Transportation: 570 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - on_campus:Living Expenses: 4550 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - on_campus:Miscellaneous Personal Expenses: 662 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8838 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `716d2385d4fcda77` University of Florida — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 8906f7143e89)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 34620 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 54010 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `8637f71bca10677e` University of Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/innovation-academy-cost/ (sha256 53c01f0b488b)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $6,440 | $34,620”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1146 ⟵ “Books, Course Materials, Supplies, Equipment | 1,146 | 1,146 | 1,146”
  - off_campus_not_with_family:Transportation: 1420 ⟵ “Transportation | 1,420 | 1,420 | 1,420”
  - off_campus_not_with_family:Living Expenses: 11645 ⟵ “Living Expenses | 11,645 | 3,920 | 11,645”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1774 ⟵ “Miscellaneous Personal Expenses | 1,774 | 1,774 | 1,774”
  - off_campus_not_with_family:Federal Student Loan Fees: 48 ⟵ “Federal Student Loan Fees | 48 | 48 | 48”
  - off_campus_not_with_family:Total Budget: 22473 ⟵ “Total Budget | $22,473 | $14,748 | $50,653”
  - with_parents_or_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $6,440 | $34,620”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1146 ⟵ “Books, Course Materials, Supplies, Equipment | 1,146 | 1,146 | 1,146”
  - with_parents_or_family:Transportation: 1420 ⟵ “Transportation | 1,420 | 1,420 | 1,420”
  - with_parents_or_family:Living Expenses: 3920 ⟵ “Living Expenses | 11,645 | 3,920 | 11,645”
  - with_parents_or_family:Miscellaneous Personal Expenses: 1774 ⟵ “Miscellaneous Personal Expenses | 1,774 | 1,774 | 1,774”
  - with_parents_or_family:Federal Student Loan Fees: 48 ⟵ “Federal Student Loan Fees | 48 | 48 | 48”
  - with_parents_or_family:Total Budget: 14748 ⟵ “Total Budget | $22,473 | $14,748 | $50,653”
### `8cd80520a9a3dba0` University of Florida — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/ (sha256 56d6cc18e8b3)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 34620 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 54010 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `9162983f57084d6c` University of Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/ (sha256 56d6cc18e8b3)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 25830 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - with_parents_or_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - with_parents_or_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - with_parents_or_family:Living Expenses: 4600 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16240 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - on_campus:*Tuition / Fees: 2580 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - on_campus:Books, Course Materials, Supplies, Equipment: 466 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - on_campus:Transportation: 570 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - on_campus:Living Expenses: 4550 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - on_campus:Miscellaneous Personal Expenses: 662 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8838 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `bb1a879cb56a3da2` University of Florida — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 419c871ab809)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 30900 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - off_campus_not_with_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - off_campus_not_with_family:Living Expenses: 12615 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 48700 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
### `ce789ba0838c7046` University of Florida — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/innovation-academy-cost/ (sha256 53c01f0b488b)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 34620 ⟵ “*Tuition / Fees | $6,440 | $6,440 | $34,620”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1146 ⟵ “Books, Course Materials, Supplies, Equipment | 1,146 | 1,146 | 1,146”
  - off_campus_not_with_family:Transportation: 1420 ⟵ “Transportation | 1,420 | 1,420 | 1,420”
  - off_campus_not_with_family:Living Expenses: 11645 ⟵ “Living Expenses | 11,645 | 3,920 | 11,645”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1774 ⟵ “Miscellaneous Personal Expenses | 1,774 | 1,774 | 1,774”
  - off_campus_not_with_family:Federal Student Loan Fees: 48 ⟵ “Federal Student Loan Fees | 48 | 48 | 48”
  - off_campus_not_with_family:Total Budget: 50653 ⟵ “Total Budget | $22,473 | $14,748 | $50,653”
### `e446281024d5e771` University of Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 8906f7143e89)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 25830 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - with_parents_or_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - with_parents_or_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - with_parents_or_family:Living Expenses: 4600 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16240 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - on_campus:*Tuition / Fees: 2580 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - on_campus:Books, Course Materials, Supplies, Equipment: 466 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - on_campus:Transportation: 570 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - on_campus:Living Expenses: 4550 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - on_campus:Miscellaneous Personal Expenses: 662 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8838 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `ee1eebffc4dcabc0` University of Florida — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/innovation-academy-cost/ (sha256 53c01f0b488b)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 30900 ⟵ “*Tuition / Fees | $6,380 | $6,380 | $30,900”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235”
  - off_campus_not_with_family:Transportation: 1380 ⟵ “Transportation | 1,380 | 1,380 | 1,380”
  - off_campus_not_with_family:Living Expenses: 10298 ⟵ “Living Expenses | 10,298 | 3,670 | 10,298”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1784 ⟵ “Miscellaneous Personal Expenses | 1,784 | 1,784 | 1,784”
  - off_campus_not_with_family:Federal Student Loan Fees: 38 ⟵ “Federal Student Loan Fees | 38 | 38 | 38”
  - off_campus_not_with_family:Total Budget: 45635 ⟵ “Total Budget | $21,115 | $14,487 | $45,635”
### `f4b2e3954dc306ac` University of Florida — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 8906f7143e89)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 30900 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - off_campus_not_with_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - off_campus_not_with_family:Living Expenses: 12615 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 48700 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
### `f69dda1029686c94` University of Florida — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 419c871ab809)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 34620 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 54010 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `329b7c115df8fd59` University of Florida-Online — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/contact-sfa/message/ (sha256 2ff0e1debfc7)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “SFA recognizes that each student’s financial situation is unique and makes every effort to develop policies and procedures that treat each student fairly and equitably while taking into account unusual circumstances.”
### `f5486ae3f219de69` University of Florida-Online — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/process/additional-information/satisfactory-academic-progress-policy/ (sha256 e5a43bbf0541)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Bright Futures will not be disbursed or will be repaid for courses listed in a Satisfactory Academic Progress Appeal as not required for a student’s degree.”
  - sentence: sap_appeal ⟵ “Other Categories Students enrolled in curricula not specifically addressed in this policy must petition the SAP Appeals Committee to continue to receive financial aid. » top Facebook Icon Twitter Icon Instagram Icon Youtube Icon Contact Us Student Financial Aid and Scholarships S-107 Criser Hall P.O.”
### `ffcd77811a2b1879` University of Florida-Online — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.ufl.edu/cost-and-aid/scholarships (sha256 cc30060ca590)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 1, "sentences": 1}
  - sentence: competing_offer_review ⟵ “No, UF cannot match offers made by other colleges or universities and there is no scholarship appeal process.”
### `01fb57d5d11bbdc9` University of Florida-Online — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 1cbdf98f235a)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 34620 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 54010 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `131e3d1b4b94b88b` University of Florida-Online — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 28325f68543b)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 34620 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 54010 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `18ed69e2a5ad5a19` University of Florida-Online — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/innovation-academy-cost/ (sha256 de715fc4ebf1)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $6,440 | $34,620”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1146 ⟵ “Books, Course Materials, Supplies, Equipment | 1,146 | 1,146 | 1,146”
  - off_campus_not_with_family:Transportation: 1420 ⟵ “Transportation | 1,420 | 1,420 | 1,420”
  - off_campus_not_with_family:Living Expenses: 11645 ⟵ “Living Expenses | 11,645 | 3,920 | 11,645”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1774 ⟵ “Miscellaneous Personal Expenses | 1,774 | 1,774 | 1,774”
  - off_campus_not_with_family:Federal Student Loan Fees: 48 ⟵ “Federal Student Loan Fees | 48 | 48 | 48”
  - off_campus_not_with_family:Total Budget: 22473 ⟵ “Total Budget | $22,473 | $14,748 | $50,653”
  - with_parents_or_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $6,440 | $34,620”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1146 ⟵ “Books, Course Materials, Supplies, Equipment | 1,146 | 1,146 | 1,146”
  - with_parents_or_family:Transportation: 1420 ⟵ “Transportation | 1,420 | 1,420 | 1,420”
  - with_parents_or_family:Living Expenses: 3920 ⟵ “Living Expenses | 11,645 | 3,920 | 11,645”
  - with_parents_or_family:Miscellaneous Personal Expenses: 1774 ⟵ “Miscellaneous Personal Expenses | 1,774 | 1,774 | 1,774”
  - with_parents_or_family:Federal Student Loan Fees: 48 ⟵ “Federal Student Loan Fees | 48 | 48 | 48”
  - with_parents_or_family:Total Budget: 14748 ⟵ “Total Budget | $22,473 | $14,748 | $50,653”
### `200319259af71da7` University of Florida-Online — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 1cbdf98f235a)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - off_campus_not_with_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - off_campus_not_with_family:Living Expenses: 12615 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 24180 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
  - with_parents_or_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - with_parents_or_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - with_parents_or_family:Living Expenses: 4560 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16125 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
  - on_campus:*Tuition / Fees: 2550 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - on_campus:Books, Course Materials, Supplies, Equipment: 546 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - on_campus:Transportation: 550 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - on_campus:Living Expenses: 3990 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - on_campus:Miscellaneous Personal Expenses: 667 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8313 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
### `2278aa256f89ceb5` University of Florida-Online — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/ (sha256 517f8c4d3e76)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 25830 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - with_parents_or_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - with_parents_or_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - with_parents_or_family:Living Expenses: 4600 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16240 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - on_campus:*Tuition / Fees: 2580 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - on_campus:Books, Course Materials, Supplies, Equipment: 466 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - on_campus:Transportation: 570 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - on_campus:Living Expenses: 4550 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - on_campus:Miscellaneous Personal Expenses: 662 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8838 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `23eb8463a75e52ac` University of Florida-Online — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 28325f68543b)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 30900 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - off_campus_not_with_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - off_campus_not_with_family:Living Expenses: 12615 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 48700 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
### `281a1be7a917a27a` University of Florida-Online — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/ (sha256 364b71d00c98)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 34620 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 54010 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `5a53cfc4a6d8effc` University of Florida-Online — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/innovation-academy-cost/ (sha256 de715fc4ebf1)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 34620 ⟵ “*Tuition / Fees | $6,440 | $6,440 | $34,620”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1146 ⟵ “Books, Course Materials, Supplies, Equipment | 1,146 | 1,146 | 1,146”
  - off_campus_not_with_family:Transportation: 1420 ⟵ “Transportation | 1,420 | 1,420 | 1,420”
  - off_campus_not_with_family:Living Expenses: 11645 ⟵ “Living Expenses | 11,645 | 3,920 | 11,645”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1774 ⟵ “Miscellaneous Personal Expenses | 1,774 | 1,774 | 1,774”
  - off_campus_not_with_family:Federal Student Loan Fees: 48 ⟵ “Federal Student Loan Fees | 48 | 48 | 48”
  - off_campus_not_with_family:Total Budget: 50653 ⟵ “Total Budget | $22,473 | $14,748 | $50,653”
### `70f2a0c78127c243` University of Florida-Online — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 1cbdf98f235a)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 25830 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - with_parents_or_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - with_parents_or_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - with_parents_or_family:Living Expenses: 4600 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16240 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - on_campus:*Tuition / Fees: 2580 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - on_campus:Books, Course Materials, Supplies, Equipment: 466 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - on_campus:Transportation: 570 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - on_campus:Living Expenses: 4550 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - on_campus:Miscellaneous Personal Expenses: 662 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8838 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `8d270602240fbf6a` University of Florida-Online — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/ (sha256 364b71d00c98)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 25830 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - with_parents_or_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - with_parents_or_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - with_parents_or_family:Living Expenses: 4600 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16240 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - on_campus:*Tuition / Fees: 2580 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - on_campus:Books, Course Materials, Supplies, Equipment: 466 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - on_campus:Transportation: 570 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - on_campus:Living Expenses: 4550 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - on_campus:Miscellaneous Personal Expenses: 662 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8838 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `8f7a0606d8746f1e` University of Florida-Online — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 1cbdf98f235a)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 30900 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - off_campus_not_with_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - off_campus_not_with_family:Living Expenses: 12615 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 48700 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
### `8fd01b29dd4bd997` University of Florida-Online — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/innovation-academy-cost/ (sha256 de715fc4ebf1)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $6,380 | $30,900”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235”
  - off_campus_not_with_family:Transportation: 1380 ⟵ “Transportation | 1,380 | 1,380 | 1,380”
  - off_campus_not_with_family:Living Expenses: 10298 ⟵ “Living Expenses | 10,298 | 3,670 | 10,298”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1784 ⟵ “Miscellaneous Personal Expenses | 1,784 | 1,784 | 1,784”
  - off_campus_not_with_family:Federal Student Loan Fees: 38 ⟵ “Federal Student Loan Fees | 38 | 38 | 38”
  - off_campus_not_with_family:Total Budget: 21115 ⟵ “Total Budget | $21,115 | $14,487 | $45,635”
  - with_parents_or_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $6,380 | $30,900”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235”
  - with_parents_or_family:Transportation: 1380 ⟵ “Transportation | 1,380 | 1,380 | 1,380”
  - with_parents_or_family:Living Expenses: 3670 ⟵ “Living Expenses | 10,298 | 3,670 | 10,298”
  - with_parents_or_family:Miscellaneous Personal Expenses: 1784 ⟵ “Miscellaneous Personal Expenses | 1,784 | 1,784 | 1,784”
  - with_parents_or_family:Federal Student Loan Fees: 38 ⟵ “Federal Student Loan Fees | 38 | 38 | 38”
  - with_parents_or_family:Total Budget: 14487 ⟵ “Total Budget | $21,115 | $14,487 | $45,635”
### `9392dc619e607d1d` University of Florida-Online — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 28325f68543b)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - off_campus_not_with_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - off_campus_not_with_family:Living Expenses: 12615 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 24180 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
  - with_parents_or_family:*Tuition / Fees: 6380 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - with_parents_or_family:Transportation: 1660 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - with_parents_or_family:Living Expenses: 4560 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2234 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16125 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
  - on_campus:*Tuition / Fees: 2550 ⟵ “*Tuition / Fees | $6,380 | $30,900 | $6,380 | $2,550”
  - on_campus:Books, Course Materials, Supplies, Equipment: 546 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235 | 546”
  - on_campus:Transportation: 550 ⟵ “Transportation | 1,660 | 1,660 | 1,660 | 550”
  - on_campus:Living Expenses: 3990 ⟵ “Living Expenses | 12,615 | 12,615 | 4,560 | 3,990”
  - on_campus:Miscellaneous Personal Expenses: 667 ⟵ “Miscellaneous Personal Expenses | 2,234 | 2,234 | 2,234 | 667”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8313 ⟵ “Total Budget | $24,180 | $48,700 | $16,125 | $8,313”
### `9b98593aa4b73175` University of Florida-Online — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/undergraduate-costs/ (sha256 28325f68543b)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 25830 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - with_parents_or_family:*Tuition / Fees: 6440 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - with_parents_or_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - with_parents_or_family:Living Expenses: 4600 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - with_parents_or_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - with_parents_or_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - with_parents_or_family:Total Budget: 16240 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
  - on_campus:*Tuition / Fees: 2580 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - on_campus:Books, Course Materials, Supplies, Equipment: 466 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - on_campus:Transportation: 570 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - on_campus:Living Expenses: 4550 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - on_campus:Miscellaneous Personal Expenses: 662 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - on_campus:Federal Student Loan Fees: 10 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - on_campus:Total Budget: 8838 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `a785b73dab1be5de` University of Florida-Online — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/innovation-academy-cost/ (sha256 de715fc4ebf1)
- issues: stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 30900 ⟵ “*Tuition / Fees | $6,380 | $6,380 | $30,900”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1235 ⟵ “Books, Course Materials, Supplies, Equipment | 1,235 | 1,235 | 1,235”
  - off_campus_not_with_family:Transportation: 1380 ⟵ “Transportation | 1,380 | 1,380 | 1,380”
  - off_campus_not_with_family:Living Expenses: 10298 ⟵ “Living Expenses | 10,298 | 3,670 | 10,298”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1784 ⟵ “Miscellaneous Personal Expenses | 1,784 | 1,784 | 1,784”
  - off_campus_not_with_family:Federal Student Loan Fees: 38 ⟵ “Federal Student Loan Fees | 38 | 38 | 38”
  - off_campus_not_with_family:Total Budget: 45635 ⟵ “Total Budget | $21,115 | $14,487 | $45,635”
### `d2eac15b07f19a81` University of Florida-Online — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sfa.ufl.edu/cost/ (sha256 517f8c4d3e76)
- issues: shared_site_attribution_review, conflicting_sources:https://www.sfa.ufl.edu/cost/,https://www.sfa.ufl.edu/cost/innovation-academy-cost/,https://www.sfa.ufl.edu/cost/undergraduate-costs/,https://www.sfa.ufl.edu/cost/undergraduate-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:*Tuition / Fees: 34620 ⟵ “*Tuition / Fees | $6,440 | $34,620 | $6,440 | $2,580”
  - off_campus_not_with_family:Books, Course Materials, Supplies, Equipment: 1220 ⟵ “Books, Course Materials, Supplies, Equipment | 1,220 | 1,220 | 1,220 | 466”
  - off_campus_not_with_family:Transportation: 1700 ⟵ “Transportation | 1,700 | 1,700 | 1,700 | 570”
  - off_campus_not_with_family:Living Expenses: 14190 ⟵ “Living Expenses | 14,190 | 14,190 | 4,600 | 4,550”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2224 ⟵ “Miscellaneous Personal Expenses | 2,224 | 2,224 | 2,224 | 662”
  - off_campus_not_with_family:Federal Student Loan Fees: 56 ⟵ “Federal Student Loan Fees | 56 | 56 | 56 | 10”
  - off_campus_not_with_family:Total Budget: 54010 ⟵ “Total Budget | $25,830 | $54,010 | $16,240 | $8,838”
### `0909e47dcbb3b359` University of North Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unf.edu/financialaid/files/certified.rf.Consortium-or-Study-Abroad-Satisfactory-Academic-Progress-Appeal.pdf (sha256 c84f7af4b2b2)
- issues: semantic_review_required, conflicting_sources:https://www.unf.edu/financialaid/files/certified.rf.2023---2024-Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/satisfactory-academic-progress.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Consortium or Study Abroad ~ Satisfactory Academic ProgressAppeal UNIVE.RSITY o/ UNF NORTH FLORIDA.”
  - sentence: sap_appeal ⟵ “I understand that after review of the consortium/study abroad transfer hours for the term and institution(s) listed above, I may be required to submit an entire Satisfactory Academic Progress Appeal packet if it has been determined that I did not meet the SAP standards outlined above and in UNF’s official SAP policy.”
### `0a7a93c7839f54a7` University of North Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unf.edu/financialaid/files/certified.rf.2023---2024-Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf (sha256 8aa0387a362d)
- issues: semantic_review_required, conflicting_sources:https://www.unf.edu/financialaid/files/certified.rf.Consortium-or-Study-Abroad-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/satisfactory-academic-progress.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Graduation Contract ~ Satisfactory Academic ProgressAppeal UNIVERSITY of UNF NORTH FLORIDA.”
### `4b449e1b8a6df584` University of North Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unf.edu/financialaid/files/certified.rf.Satisfactory-Academic-Progress-Appeal.pdf (sha256 25362b94793b)
- issues: semantic_review_required, conflicting_sources:https://www.unf.edu/financialaid/files/certified.rf.2023---2024-Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Consortium-or-Study-Abroad-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/satisfactory-academic-progress.html
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal The Higher Education Act of 1965 requires institutions of higher education to establish and apply standards of Satisfactory Academic Progress (SAP) that all students must meet to qualify and remain eligible for assistance from Title IV (Federal) student financial aid programs.”
  - sentence: sap_appeal ⟵ “How To Complete the Satisfactory Academic Progress Appeal: Step 1: Complete all pages of this form.”
  - sentence: sap_appeal ⟵ “Step 8: Review the SAP Appeal deadline at https://www.unf.edu/financialaid/important-dates.html Student Statement of Understanding: Please review and initial next to the statement below.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Section I: Student Information Student Name Student ID#: N Email address Phone SAP Level: □ Warning □ Suspension (Financial aid cannot disburse in Suspension) SAP Type: (refer to your SAP email and check all that apply) □ Pass Rate Rule □ GPA Rule □ Both Pass Rate and GPA □ Max Hours/150% Rule Please indicate the term you were placed in this SAP status: □ Fall”
  - sentence: sap_appeal ⟵ “I understand that withdrawing from any course(s) during the SAP appeal process may result in the denial of my appeal.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Section V: Academic Information Student’s current major(s): Minor (if applicable): Is a minor required for the student’s degree program?”
### `66125b60ead44cf5` University of North Florida — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.unf.edu/scholarships/programs.html (sha256 151cc428325d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: competing_offer_review ⟵ “Scholarship Universe is a platform that automatically matches students to potential awards based on your major, GPA, and other information UNF already knows.”
### `68a54da0acdebb62` University of North Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unf.edu/financialaid/satisfactory-academic-progress.html (sha256 00c6972156d0)
- issues: semantic_review_required, conflicting_sources:https://www.unf.edu/financialaid/files/certified.rf.2023---2024-Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Consortium-or-Study-Abroad-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Satisfactory-Academic-Progress-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “Official UNF SAP Policy SAP Policy Information SAP Status Appeals Additional Information SAP Policy Information Required Pass Rate (Pace): Students are required to earn a minimum of 67% of the cumulative credit hours they attempt.”
  - sentence: sap_appeal ⟵ “A student on Financial Aid Suspension (for reasons other than violating the maximum time frame) may re-establish their Satisfactory Academic Progress status to Good Standing without appeal by following the Re-establishing Eligibility without an Appeal by taking coursework at UNF and achieving all Satisfactory Academic Progress requirements.”
  - sentence: sap_appeal ⟵ “Appeals Satisfactory Academic Progress (SAP) Appeals: If a student is ineligible for Federal Financial Aid based on the Satisfactory Academic Progress requirements, the student may appeal this decision by completing the Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “Save, sign, and submit the Satisfactory Academic Progress Appeal signed by the student.”
  - sentence: sap_appeal ⟵ “For students who have exceeded or will exceed the maximum time frame requirement, a Graduation Contract signed by both the student and the academic/program advisor must be submitted with the Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “Please submit the completed appeal and supporting documentation following instructions on the Satisfactory Academic Progress Appeal Form.”
### `6d9ec0670ff84771` University of North Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unf.edu/financialaid/files/certified.rf.Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf (sha256 10633c2d8d8f)
- issues: semantic_review_required, conflicting_sources:https://www.unf.edu/financialaid/files/certified.rf.2023---2024-Graduation-Contract-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Consortium-or-Study-Abroad-Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/files/certified.rf.Satisfactory-Academic-Progress-Appeal.pdf,https://www.unf.edu/financialaid/satisfactory-academic-progress.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Graduation Contract ~ Satisfactory Academic ProgressAppeal UNIVERSITY of UNF NORTH FLORIDA.”
### `2a2666e11f0e1103` University of North Florida — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.unf.edu/scholarships/programs.html (sha256 151cc428325d)
- issues: ambiguous_year_labels
- checks: {"thresholds": {"act_min": 21, "gpa_min": 4.5, "sat_min": 1060}}
  - award_amount_text: $2,000 ⟵ “Provost's Award | $2,000 | 4.5 | 1060 | 21 | 67”
  - gpa_requirement: 4.5 ⟵ “Provost's Award | $2,000 | 4.5 | 1060 | 21 | 67”
  - test_requirement: ACT 21 / SAT 1060 ⟵ “Provost's Award | $2,000 | 4.5 | 1060 | 21 | 67”
### `5ae84e06332a203b` University of North Florida — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.unf.edu/scholarships/programs.html (sha256 151cc428325d)
- issues: ambiguous_year_labels
- checks: {"thresholds": {"act_min": 21, "gpa_min": 4.2, "sat_min": 1060}}
  - award_amount_text: $1,000 ⟵ “Dean's Award | $1,000 | 4.2 | 1060 | 21 | 67”
  - gpa_requirement: 4.2 ⟵ “Dean's Award | $1,000 | 4.2 | 1060 | 21 | 67”
  - test_requirement: ACT 21 / SAT 1060 ⟵ “Dean's Award | $1,000 | 4.2 | 1060 | 21 | 67”
### `621c3337fa6f6ec2` University of North Florida — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.unf.edu/scholarships/programs.html (sha256 151cc428325d)
- issues: ambiguous_year_labels
- checks: {"thresholds": {"act_min": 29, "gpa_min": 4.1, "sat_min": 1330}}
  - award_amount_text: $5,000 ⟵ “President's Platinum | $5,000 | 4.1 | 1330 | 29 | 95”
  - gpa_requirement: 4.1 ⟵ “President's Platinum | $5,000 | 4.1 | 1330 | 29 | 95”
  - test_requirement: ACT 29 / SAT 1330 ⟵ “President's Platinum | $5,000 | 4.1 | 1330 | 29 | 95”
### `89c8d4264802a560` University of North Florida — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.unf.edu/scholarships/programs.html (sha256 151cc428325d)
- issues: ambiguous_year_labels
- checks: {"thresholds": {"act_min": 27, "gpa_min": 3.9, "sat_min": 1260}}
  - award_amount_text: $4,000 ⟵ “President's Gold | $4,000 | 3.9 | 1260 | 27 | 89”
  - gpa_requirement: 3.9 ⟵ “President's Gold | $4,000 | 3.9 | 1260 | 27 | 89”
  - test_requirement: ACT 27 / SAT 1260 ⟵ “President's Gold | $4,000 | 3.9 | 1260 | 27 | 89”
### `9dd63c679a282345` University of North Florida — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.unf.edu/scholarships/programs.html (sha256 151cc428325d)
- issues: ambiguous_year_labels
- checks: {"thresholds": {"act_min": 25, "gpa_min": 3.7, "sat_min": 1200}}
  - award_amount_text: $3,000 ⟵ “President's Silver | $3,000 | 3.7 | 1200 | 25 | 83”
  - gpa_requirement: 3.7 ⟵ “President's Silver | $3,000 | 3.7 | 1200 | 25 | 83”
  - test_requirement: ACT 25 / SAT 1200 ⟵ “President's Silver | $3,000 | 3.7 | 1200 | 25 | 83”
### `0a50ab598e60a314` University of North Florida — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.unf.edu/scholarships/programs.html (sha256 151cc428325d)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees: 20790 ⟵ “Tuition & Fees | $6,390 | $20,790”
  - on_campus:Books & Supplies: 1200 ⟵ “Books & Supplies | $1,200 | $1,200”
  - on_campus:Housing: 6988 ⟵ “Housing | $6,988 | $6,988”
  - on_campus:Food: 4822 ⟵ “Food | $4,822 | $4,822”
  - on_campus:Transportation: 3029 ⟵ “Transportation | $3,029 | $3,029”
  - on_campus:Miscellaneous: 2368 ⟵ “Miscellaneous | $2,368 | $2,368”
  - on_campus:Total: 39197 ⟵ “Total | $24,797 | $39,197”
### `2d76f2a7833bdebe` University of North Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.unf.edu/catalog/financial/academics/Cost-of-Attendance.html (sha256 d0b018f24828)
- issues: arrangement_unlabeled, conflicting_sources:https://www.unf.edu/scholarships/programs.html
- checks: {"columns": 6, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition & Fees: 6390 ⟵ “Tuition & Fees | $6,390 | $6,390 | $6,390 | $20,790 | $20,790 | $20,790”
  - on_campus:Books & Supplies: 1200 ⟵ “Books & Supplies | $1,200 | $1,200 | 1,200 | $1,200 | 1,200 | $1,200”
  - on_campus:Housing: 6988 ⟵ “Housing | $6,988 | $9,580 | $1,874 | $6,988 | $9,580 | $1,874”
  - on_campus:Food: 4822 ⟵ “Food | $4,822 | $2,370 | $4,822 | $4,822 | $2,370 | $4,822”
  - on_campus:Transportation: 3029 ⟵ “Transportation | $3,029 | $2,889 | $2,889 | $3,029 | $2,889 | $2,889”
  - on_campus:Miscellaneous: 2368 ⟵ “Miscellaneous | $2,368 | $2,368 | $2,368 | $2,368 | $2,368 | $2,368”
  - on_campus:Direct Loan Fees: 44 ⟵ “Direct Loan Fees | $44 | $44 | $44 | $44 | $44 | $44”
  - on_campus:Total: 24841 ⟵ “Total | $24,841 | $24,841 | $19,587 | $39,241 | $39,241 | $33,987”
  - off_campus_not_with_family:Tuition & Fees: 6390 ⟵ “Tuition & Fees | $6,390 | $6,390 | $6,390 | $20,790 | $20,790 | $20,790”
  - off_campus_not_with_family:Books & Supplies: 1200 ⟵ “Books & Supplies | $1,200 | $1,200 | 1,200 | $1,200 | 1,200 | $1,200”
  - off_campus_not_with_family:Housing: 9580 ⟵ “Housing | $6,988 | $9,580 | $1,874 | $6,988 | $9,580 | $1,874”
  - off_campus_not_with_family:Food: 2370 ⟵ “Food | $4,822 | $2,370 | $4,822 | $4,822 | $2,370 | $4,822”
  - off_campus_not_with_family:Transportation: 2889 ⟵ “Transportation | $3,029 | $2,889 | $2,889 | $3,029 | $2,889 | $2,889”
  - off_campus_not_with_family:Miscellaneous: 2368 ⟵ “Miscellaneous | $2,368 | $2,368 | $2,368 | $2,368 | $2,368 | $2,368”
  - off_campus_not_with_family:Direct Loan Fees: 44 ⟵ “Direct Loan Fees | $44 | $44 | $44 | $44 | $44 | $44”
  - off_campus_not_with_family:Total: 24841 ⟵ “Total | $24,841 | $24,841 | $19,587 | $39,241 | $39,241 | $33,987”
  - column:Tuition & Fees: 6390 ⟵ “Tuition & Fees | $6,390 | $6,390 | $6,390 | $20,790 | $20,790 | $20,790”
  - column:Books & Supplies: 1200 ⟵ “Books & Supplies | $1,200 | $1,200 | 1,200 | $1,200 | 1,200 | $1,200”
  - column:Housing: 1874 ⟵ “Housing | $6,988 | $9,580 | $1,874 | $6,988 | $9,580 | $1,874”
  - column:Food: 4822 ⟵ “Food | $4,822 | $2,370 | $4,822 | $4,822 | $2,370 | $4,822”
  - column:Transportation: 2889 ⟵ “Transportation | $3,029 | $2,889 | $2,889 | $3,029 | $2,889 | $2,889”
  - column:Miscellaneous: 2368 ⟵ “Miscellaneous | $2,368 | $2,368 | $2,368 | $2,368 | $2,368 | $2,368”
  - column:Direct Loan Fees: 44 ⟵ “Direct Loan Fees | $44 | $44 | $44 | $44 | $44 | $44”
  - column:Total: 19587 ⟵ “Total | $24,841 | $24,841 | $19,587 | $39,241 | $39,241 | $33,987”
  - on_campus:Tuition & Fees: 20790 ⟵ “Tuition & Fees | $6,390 | $6,390 | $6,390 | $20,790 | $20,790 | $20,790”
  - … 23 more rows
### `e67938c7cb5bfa5b` University of North Florida — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.unf.edu/scholarships/programs.html (sha256 151cc428325d)
- issues: ambiguous_year_labels, conflicting_sources:https://www.unf.edu/catalog/financial/academics/Cost-of-Attendance.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees: 6390 ⟵ “Tuition & Fees | $6,390 | $20,790”
  - on_campus:Books & Supplies: 1200 ⟵ “Books & Supplies | $1,200 | $1,200”
  - on_campus:Housing: 6988 ⟵ “Housing | $6,988 | $6,988”
  - on_campus:Food: 4822 ⟵ “Food | $4,822 | $4,822”
  - on_campus:Transportation: 3029 ⟵ “Transportation | $3,029 | $3,029”
  - on_campus:Miscellaneous: 2368 ⟵ “Miscellaneous | $2,368 | $2,368”
  - on_campus:Total: 24797 ⟵ “Total | $24,797 | $39,197”
### `16fbc46edc6882eb` University of South Florida — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.usf.edu/admissions/transfer/admission-information/major-requirements.aspx (sha256 81269bf01756)
- issues: conflicting_values:min_grade
- checks: {"fields": []}
### `1f8790a84cbcc3fb` University of West Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://confluence.uwf.edu/pages/diffpagesbyversion.action?pageId=42664455&selectedPageVersions=43&selectedPageVersions=44 (sha256 7c6c56032fc7)
- issues: semantic_review_required, conflicting_sources:https://confluence.uwf.edu/spaces/public/pages/42664455/Submitting+a+Satisfactory+Academic+Progress+Appeal+Form+for+students,https://confluence.uwf.edu/spaces/public/pages/42664455/Submitting+a+Satisfactory+Academic+Progress+Appeal+Form+for+students
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Page Comparison - Submitting a Satisfactory Academic Progress Appeal Form, for students (v.43 vs v.44) - UWF Public Knowledge Base - UWF Confluence Log in Linked Applications Loading...”
  - sentence: sap_appeal ⟵ “The Academic Improvement Plan template is provided within the SAP Appeal webform.”
### `6aa8eb2b87f29474` University of West Florida — appeals 2025-26 [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/applying-for-aid/special-circumstances-and-judgment-appeals/ (sha256 5b8e9e297372)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://uwf.edu/offices/financial-aid/satisfactory-academic-progress/sap-policy-details/
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “To account for special circumstances, Sec. 479A(a) of the Higher Education Act allows institutions to make data value adjustments on a case-by-case basis.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal (EFC/SAI Appeal): Review and possible adjustment of data values that are used to calculate the Expected Family Contribution (EFC) and Student Aid Index (SAI) number.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance Appeal (Dependency Appeal): Unusual family circumstances that allow an applicant to apply as an independent student, i.e., parental data would not be required.”
  - sentence: need_based_special_circumstances ⟵ “Students submitting an Unusual Circumstance Appeal are encouraged to ensure they have their asset information listed on their FAFSA (even if the values are all '$0').”
  - sentence: need_based_special_circumstances ⟵ “Students who are approved for an Unusual Circumstance appeal who have not provided asset information on the FAFSA will be asked to provide it on StudentForms.”
  - sentence: need_based_special_circumstances ⟵ “Per federal regulations, none of the conditions listed below, singly or in combination, qualify as unusual circumstances meriting a dependency override: Parents refuse to contribute to the student's education.”
### `6d55340a8c12e82c` University of West Florida — appeals 2025-26 [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/applying-for-aid/special-circumstances-and-judgment-appeals/ (sha256 5b8e9e297372)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment Appeals At UWF, we recognize that special circumstances may exist that are not sufficiently addressed by the standardized federal student aid formulas on the FAFSA or estimated cost of attendance.”
  - sentence: professional_judgment ⟵ “Cost of Attendance (COA) Professional Judgment: Review and possible increase to a student's COA due to out-of-pocket expenses.”
### `877e5ed403af2af5` University of West Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://confluence.uwf.edu/spaces/public/pages/42664455/Submitting+a+Satisfactory+Academic+Progress+Appeal+Form+for+students (sha256 13f2eb79eeb1)
- issues: semantic_review_required, conflicting_sources:https://confluence.uwf.edu/pages/diffpagesbyversion.action?pageId=42664455&selectedPageVersions=43&selectedPageVersions=44,https://confluence.uwf.edu/spaces/public/pages/42664455/Submitting+a+Satisfactory+Academic+Progress+Appeal+Form+for+students
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Submitting a Satisfactory Academic Progress Appeal Form, for students - UWF Public Knowledge Base - UWF Confluence Log in Linked Applications Loading...”
  - sentence: sap_appeal ⟵ “Students declared ineligible for financial aid on the basis of unsatisfactory academic progress may appeal the decision by completing the Satisfactory Academic Appeal Form.”
  - sentence: sap_appeal ⟵ “Not all students are eligible to appeal their SAP status, so please go to Satisfactory Academic Progress to learn more.”
  - sentence: sap_appeal ⟵ “Step 3 Click the + radio button to add the SAP Appeal request for the applicable aid year.”
  - sentence: sap_appeal ⟵ “Click on the SAP Appeal box to resume the submission.”
  - sentence: sap_appeal ⟵ “The Academic Improvement Plan template is provided within the SAP Appeal webform.”
### `ab04d52df0abc1df` University of West Florida — appeals 2025-26 [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/satisfactory-academic-progress/sap-policy-details/ (sha256 64260917031f)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: sap_appeal ⟵ “Approved Pending Review: After receiving an appeal approval, the Satisfactory Academic Progress GPA and CR conditions are being reviewed to determine eligibility for the following semester.”
  - sentence: sap_appeal ⟵ “Appeal Conditions Not Met: You did not meet the conditions of your approved SAP appeal and are not otherwise meeting SAP.”
  - sentence: sap_appeal ⟵ “Appeal Denied: The SAP committee denied your SAP appeal.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Process (Excluding MTL) If you become ineligible for financial aid and are able to appeal your status, you may choose to submit a SAP appeal for committee review.”
  - sentence: sap_appeal ⟵ “Please note that, during peak times, we cannot guarantee that a SAP appeal will be approved by the time fees are due for the semester.”
  - sentence: sap_appeal ⟵ “If the committee approves your SAP appeal to restore financial aid eligibility, there will be additional details forward and compliance standards to follow (i.e., SAP Appeal Agreement Letter).”
### `ccbc041a0a65331c` University of West Florida — appeals 2025-26 [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/satisfactory-academic-progress/sap-policy-details/ (sha256 64260917031f)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://uwf.edu/offices/financial-aid/applying-for-aid/special-circumstances-and-judgment-appeals/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Limited exceptions may occur depending on unusual circumstances for instances such as, but not limited to, length of time between last date of attendance or University error.”
### `cce86ae93c171014` University of West Florida — appeals 2026-27 [new] (source_unlabeled)
- source: https://confluence.uwf.edu/spaces/public/pages/42664455/Submitting+a+Satisfactory+Academic+Progress+Appeal+Form+for+students (sha256 9e6f8114ddf0)
- issues: semantic_review_required, conflicting_sources:https://confluence.uwf.edu/pages/diffpagesbyversion.action?pageId=42664455&selectedPageVersions=43&selectedPageVersions=44,https://confluence.uwf.edu/spaces/public/pages/42664455/Submitting+a+Satisfactory+Academic+Progress+Appeal+Form+for+students
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Submitting a Satisfactory Academic Progress Appeal Form, for students - UWF Public Knowledge Base - UWF Confluence Log in Linked Applications Loading...”
  - sentence: sap_appeal ⟵ “Students declared ineligible for financial aid on the basis of unsatisfactory academic progress may appeal the decision by completing the Satisfactory Academic Appeal Form.”
  - sentence: sap_appeal ⟵ “Not all students are eligible to appeal their SAP status, so please go to Satisfactory Academic Progress to learn more.”
  - sentence: sap_appeal ⟵ “Step 3 Click the + radio button to add the SAP Appeal request for the applicable aid year.”
  - sentence: sap_appeal ⟵ “Click on the SAP Appeal box to resume the submission.”
  - sentence: sap_appeal ⟵ “The Academic Improvement Plan template is provided within the SAP Appeal webform.”
### `143c42f57c447c7a` University of West Florida — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/cost-of-attendance/cost-of-attendance-estimates/ (sha256 923d42c3a3cb)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://uwf.edu/admissions/transfer/tuition-and-costs/,https://uwf.edu/admissions/undergraduate/cost-and-financial-aid/costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition 2: 7638 ⟵ “Tuition 2 | 7,638 | 7,638 | 7,638”
  - with_parents_or_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - with_parents_or_family:Food 3: 2848 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - with_parents_or_family:Housing 3: 2182 ⟵ “Housing 3 | 2,182 | 7,358 | 8,730”
  - with_parents_or_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - with_parents_or_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - with_parents_or_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - with_parents_or_family:TOTAL: 19896 ⟵ “TOTAL | $19,896 | $27,852 | $29,224”
  - on_campus:Tuition 2: 7638 ⟵ “Tuition 2 | 7,638 | 7,638 | 7,638”
  - on_campus:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - on_campus:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - on_campus:Housing 3: 7358 ⟵ “Housing 3 | 2,182 | 7,358 | 8,730”
  - on_campus:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - on_campus:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - on_campus:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - on_campus:TOTAL: 27852 ⟵ “TOTAL | $19,896 | $27,852 | $29,224”
  - off_campus_not_with_family:Tuition 2: 7638 ⟵ “Tuition 2 | 7,638 | 7,638 | 7,638”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - off_campus_not_with_family:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - off_campus_not_with_family:Housing 3: 8730 ⟵ “Housing 3 | 2,182 | 7,358 | 8,730”
  - off_campus_not_with_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - off_campus_not_with_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - off_campus_not_with_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - off_campus_not_with_family:TOTAL: 29224 ⟵ “TOTAL | $19,896 | $27,852 | $29,224”
### `434001591dc819d8` University of West Florida — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/cost-of-attendance/2025-2026-cost-of-attendance-estimates/ (sha256 a8831658ac48)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition 2: 5088 ⟵ “Tuition 2 | 5,088 | 5,088 | 5,088”
  - with_parents_or_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - with_parents_or_family:Food 3: 2848 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - with_parents_or_family:Housing 3: 2182 ⟵ “Housing 3 | 2,182 | 7,074 | 8,730”
  - with_parents_or_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - with_parents_or_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - with_parents_or_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - with_parents_or_family:TOTAL: 17346 ⟵ “TOTAL | $17,346 | $25,018 | $26,674”
  - on_campus:Tuition 2: 5088 ⟵ “Tuition 2 | 5,088 | 5,088 | 5,088”
  - on_campus:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - on_campus:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - on_campus:Housing 3: 7074 ⟵ “Housing 3 | 2,182 | 7,074 | 8,730”
  - on_campus:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - on_campus:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - on_campus:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - on_campus:TOTAL: 25018 ⟵ “TOTAL | $17,346 | $25,018 | $26,674”
  - off_campus_not_with_family:Tuition 2: 5088 ⟵ “Tuition 2 | 5,088 | 5,088 | 5,088”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - off_campus_not_with_family:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - off_campus_not_with_family:Housing 3: 8730 ⟵ “Housing 3 | 2,182 | 7,074 | 8,730”
  - off_campus_not_with_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - off_campus_not_with_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - off_campus_not_with_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - off_campus_not_with_family:TOTAL: 26674 ⟵ “TOTAL | $17,346 | $25,018 | $26,674”
### `57a87737c1607a91` University of West Florida — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://uwf.edu/admissions/undergraduate/cost-and-financial-aid/costs/ (sha256 348d5b1feef8)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://uwf.edu/admissions/transfer/tuition-and-costs/,https://uwf.edu/offices/financial-aid/cost-of-attendance/cost-of-attendance-estimates/
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition *: 9570 ⟵ “Tuition * | $6,420 | $9,570 | $21,240”
  - on_campus:Housing **: 6622 ⟵ “Housing ** | $6,622 | $6,622 | $6,622”
  - on_campus:Meals ***: 5136 ⟵ “Meals *** | $5,136 | $5,136 | $5,136”
  - on_campus:Total Est. Cost: 21328 ⟵ “Total Est. Cost | $18,178 | $21,328 | $32,998”
### `5ffd2126385a3f84` University of West Florida — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/cost-of-attendance/2025-2026-cost-of-attendance-estimates/ (sha256 a8831658ac48)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition 2: 15384 ⟵ “Tuition 2 | 15,384 | 15,384 | 15,384”
  - with_parents_or_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - with_parents_or_family:Food 3: 2848 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - with_parents_or_family:Housing 3: 2182 ⟵ “Housing 3 | 2,182 | 7,074 | 8,730”
  - with_parents_or_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - with_parents_or_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - with_parents_or_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - with_parents_or_family:TOTAL: 27642 ⟵ “TOTAL | $27,642 | $35,314 | $36,970”
  - on_campus:Tuition 2: 15384 ⟵ “Tuition 2 | 15,384 | 15,384 | 15,384”
  - on_campus:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - on_campus:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - on_campus:Housing 3: 7074 ⟵ “Housing 3 | 2,182 | 7,074 | 8,730”
  - on_campus:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - on_campus:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - on_campus:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - on_campus:TOTAL: 35314 ⟵ “TOTAL | $27,642 | $35,314 | $36,970”
  - off_campus_not_with_family:Tuition 2: 15384 ⟵ “Tuition 2 | 15,384 | 15,384 | 15,384”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - off_campus_not_with_family:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - off_campus_not_with_family:Housing 3: 8730 ⟵ “Housing 3 | 2,182 | 7,074 | 8,730”
  - off_campus_not_with_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - off_campus_not_with_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - off_campus_not_with_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - off_campus_not_with_family:TOTAL: 36970 ⟵ “TOTAL | $27,642 | $35,314 | $36,970”
### `81bb1e94d477f33b` University of West Florida — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://uwf.edu/admissions/transfer/tuition-and-costs/ (sha256 93db26d27084)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://uwf.edu/admissions/undergraduate/cost-and-financial-aid/costs/,https://uwf.edu/offices/financial-aid/cost-of-attendance/cost-of-attendance-estimates/
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition *: 9570 ⟵ “Tuition * | $6,420 | $9,570 | $21,240”
  - on_campus:Housing **: 6622 ⟵ “Housing ** | $6,622 | $6,622 | $6,622”
  - on_campus:Meals ***: 5136 ⟵ “Meals *** | $5,136 | $5,136 | $5,136”
  - on_campus:Total Est. Cost: 21328 ⟵ “Total Est. Cost | $18,178 | $21,328 | $32,998”
### `961b5ef4cbc799b7` University of West Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://uwf.edu/admissions/undergraduate/cost-and-financial-aid/costs/ (sha256 348d5b1feef8)
- issues: conflicting_sources:https://uwf.edu/admissions/transfer/tuition-and-costs/,https://uwf.edu/offices/financial-aid/cost-of-attendance/cost-of-attendance-estimates/
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition *: 6420 ⟵ “Tuition * | $6,420 | $9,570 | $21,240”
  - on_campus:Housing **: 6622 ⟵ “Housing ** | $6,622 | $6,622 | $6,622”
  - on_campus:Meals ***: 5136 ⟵ “Meals *** | $5,136 | $5,136 | $5,136”
  - on_campus:Total Est. Cost: 18178 ⟵ “Total Est. Cost | $18,178 | $21,328 | $32,998”
  - on_campus:Tuition *: 21240 ⟵ “Tuition * | $6,420 | $9,570 | $21,240”
  - on_campus:Housing **: 6622 ⟵ “Housing ** | $6,622 | $6,622 | $6,622”
  - on_campus:Meals ***: 5136 ⟵ “Meals *** | $5,136 | $5,136 | $5,136”
  - on_campus:Total Est. Cost: 32998 ⟵ “Total Est. Cost | $18,178 | $21,328 | $32,998”
### `a0420410deab0b56` University of West Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://uwf.edu/admissions/transfer/tuition-and-costs/ (sha256 93db26d27084)
- issues: conflicting_sources:https://uwf.edu/admissions/undergraduate/cost-and-financial-aid/costs/,https://uwf.edu/offices/financial-aid/cost-of-attendance/cost-of-attendance-estimates/
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition *: 6420 ⟵ “Tuition * | $6,420 | $9,570 | $21,240”
  - on_campus:Housing **: 6622 ⟵ “Housing ** | $6,622 | $6,622 | $6,622”
  - on_campus:Meals ***: 5136 ⟵ “Meals *** | $5,136 | $5,136 | $5,136”
  - on_campus:Total Est. Cost: 18178 ⟵ “Total Est. Cost | $18,178 | $21,328 | $32,998”
  - on_campus:Tuition *: 21240 ⟵ “Tuition * | $6,420 | $9,570 | $21,240”
  - on_campus:Housing **: 6622 ⟵ “Housing ** | $6,622 | $6,622 | $6,622”
  - on_campus:Meals ***: 5136 ⟵ “Meals *** | $5,136 | $5,136 | $5,136”
  - on_campus:Total Est. Cost: 32998 ⟵ “Total Est. Cost | $18,178 | $21,328 | $32,998”
### `cc546de337d3e074` University of West Florida — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/cost-of-attendance/2025-2026-cost-of-attendance-estimates/ (sha256 a8831658ac48)
- issues: components_do_not_reconcile, residency_names_another_state, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": false, "rows": 8}
  - with_parents_or_family:Tuition 2: 7608 ⟵ “Tuition 2 | 7,608 | 7,608 | 7,608”
  - with_parents_or_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - with_parents_or_family:Food 3: 2848 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - with_parents_or_family:Housing 3: 2182 ⟵ “Housing 3 | 2,182 | 7,047 | 8,730”
  - with_parents_or_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - with_parents_or_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - with_parents_or_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - with_parents_or_family:TOTAL: 19866 ⟵ “TOTAL | $19,866 | $27,538 | $29,194”
  - on_campus:Tuition 2: 7608 ⟵ “Tuition 2 | 7,608 | 7,608 | 7,608”
  - on_campus:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - on_campus:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - on_campus:Housing 3: 7047 ⟵ “Housing 3 | 2,182 | 7,047 | 8,730”
  - on_campus:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - on_campus:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - on_campus:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - on_campus:TOTAL: 27538 ⟵ “TOTAL | $19,866 | $27,538 | $29,194”
  - off_campus_not_with_family:Tuition 2: 7608 ⟵ “Tuition 2 | 7,608 | 7,608 | 7,608”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - off_campus_not_with_family:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - off_campus_not_with_family:Housing 3: 8730 ⟵ “Housing 3 | 2,182 | 7,047 | 8,730”
  - off_campus_not_with_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - off_campus_not_with_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - off_campus_not_with_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - off_campus_not_with_family:TOTAL: 29194 ⟵ “TOTAL | $19,866 | $27,538 | $29,194”
### `e92b76e32697023d` University of West Florida — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://uwf.edu/offices/financial-aid/cost-of-attendance/cost-of-attendance-estimates/ (sha256 923d42c3a3cb)
- issues: conflicting_sources:https://uwf.edu/admissions/transfer/tuition-and-costs/,https://uwf.edu/admissions/undergraduate/cost-and-financial-aid/costs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition 2: 5118 ⟵ “Tuition 2 | 5,118 | 5,118 | 5,118”
  - with_parents_or_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - with_parents_or_family:Food 3: 2848 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - with_parents_or_family:Housing 3: 2182 ⟵ “Housing 3 | 2,182 | 7,358 | 8,730”
  - with_parents_or_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - with_parents_or_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - with_parents_or_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - with_parents_or_family:TOTAL: 17376 ⟵ “TOTAL | $17,376 | $25,332 | $26,704”
  - on_campus:Tuition 2: 5118 ⟵ “Tuition 2 | 5,118 | 5,118 | 5,118”
  - on_campus:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - on_campus:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - on_campus:Housing 3: 7358 ⟵ “Housing 3 | 2,182 | 7,358 | 8,730”
  - on_campus:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - on_campus:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - on_campus:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - on_campus:TOTAL: 25332 ⟵ “TOTAL | $17,376 | $25,332 | $26,704”
  - off_campus_not_with_family:Tuition 2: 5118 ⟵ “Tuition 2 | 5,118 | 5,118 | 5,118”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1600 ⟵ “Books, course materials, supplies and equipment | 1,600 | 1,600 | 1,600”
  - off_campus_not_with_family:Food 3: 5628 ⟵ “Food 3 | 2,848 | 5,628 | 5,628”
  - off_campus_not_with_family:Housing 3: 8730 ⟵ “Housing 3 | 2,182 | 7,358 | 8,730”
  - off_campus_not_with_family:Transportation: 2386 ⟵ “Transportation | 2,386 | 2,386 | 2,386”
  - off_campus_not_with_family:Miscellaneous Personal: 3150 ⟵ “Miscellaneous Personal | 3,150 | 3,150 | 3,150”
  - off_campus_not_with_family:Loan Fees 4: 92 ⟵ “Loan Fees 4 | 92 | 92 | 92”
  - off_campus_not_with_family:TOTAL: 26704 ⟵ “TOTAL | $17,376 | $25,332 | $26,704”
### `72c288486c0aa6f4` Valencia College — appeals 2026-27 [new] (source_unlabeled)
- source: https://valenciacollege.edu/finaid/getting-started/index.php (sha256 9c590c6ff00c)
- issues: semantic_review_required, conflicting_sources:https://valenciacollege.edu/finaid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Getting StartedPrograms AvailableFinancial LiteracyDefault Prevention Getting Started Getting StartedObtaining FormsChecking Financial AidDates & EligibilityEligible Vocational Training CertificatesPost-Application CompletionSpecial CircumstancesDependency Override Request Using Financial AidCredit Hours NeededAttending & Withdrawing From Classes ACCESSIBILITY | CONSUMER INFO | POLICY MANUAL | PRI”
### `82c7cf4f98253c15` Valencia College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://valenciacollege.edu/finaid/getting-started/special-circumstances.php (sha256 2f713d6c71ea)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “When these situations occur, it is possible to re-evaluate a student’s aid eligibility based on their current circumstances through the Professional Judgment (PJ) process.”
  - sentence: professional_judgment ⟵ “All Professional Judgment applications are required to have a detailed letter of explanation and supporting documentation.”
  - sentence: professional_judgment ⟵ “If you have been selected for Federal Verification, a Professional Judgment cannot be processed for changes until verification is complete.”
  - sentence: professional_judgment ⟵ “There must be a significant change to the household finances to be considered for a Professional Judgment.”
  - sentence: professional_judgment ⟵ “Non-applicable Circumstances Standard living expenses (utilities, car payments, etc) Mortgage payments Credit card/other personal debts Filing for bankruptcy Vacation expenses All other discretionary expenses To request a Professional Judgment review, please review the list of documentation required below.”
  - sentence: professional_judgment ⟵ “Learn More Documentation Required for Professional Judgment In each case, you must complete our Professional Judgment Request Form and provide the documentation listed on the form before we can review your request. 2025 - 2026 Professional Judgment Request Form 2026 - 2027 Professional Judgment Request Form Please use the Financial Aid Office's Secure Document Upload Form to submit your complete p”
### `890f4080d883839d` Valencia College — appeals 2026-27 [new] (source_unlabeled)
- source: https://valenciacollege.edu/finaid/ (sha256 c471f5be90b3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Getting StartedPrograms AvailableFinancial LiteracyDefault Prevention Important Dates and Deadlines for Fall 2026 | Date | Description | July 17, 2026 | Financial Aid Priority Deadline for Upcoming Term | August 14, 2026 | Fee Payment Deadline: (by 5pm ET) | August 7, 2026 | Financial Aid SAP Appeal Priority Deadline | August 24, 2026 | Classes Begin | August 31, 2026 | Drop/Refund Deadline (11:59”
### `ef01b0aff804ca03` Valencia College — appeals 2026-27 [new] (source_unlabeled)
- source: https://valenciacollege.edu/finaid/ (sha256 c471f5be90b3)
- issues: semantic_review_required, conflicting_sources:https://valenciacollege.edu/finaid/getting-started/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have questions about applying for aid (FAFSA), submitting documents, loans, dependency overrides, change in income, FAFSA corrections, SAP, or other financial aid questions, you can sign in, and you will be connected virtually to the first available financial aid specialist.”
### `5b5d93ae608410d0` Valencia College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://valenciacollege.edu/finaid/attendance-cost.php (sha256 ee84f155cc72)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 4, "rows": 9}
  - column:Tuition & Fees (Lower Division): 2664 ⟵ “Tuition & Fees (Lower Division) | $2,664 | $1,998 | $1,332 | $666”
  - column:Tuition & Fees (Upper Division): 2880 ⟵ “Tuition & Fees (Upper Division) | $2,880 | $2,160 | $1,440 | $720”
  - column:Books & Supplies: 2130 ⟵ “Books & Supplies | $2,130 | $1,578 | $1,052 | $526”
  - column:Food & Housing: 15221 ⟵ “Food & Housing | $15,221 | $15,221 | $15,221 | ”
  - column:Transportation: 3220 ⟵ “Transportation | $3,220 | $2,415 | $1,610 | $805”
  - column:Miscellaneous: 7581 ⟵ “Miscellaneous | $7,581 | $5,686 | $3,791 | ”
  - column:Loan: 66 ⟵ “Loan | $66 | $66 | $66 | ”
  - column:Total 9 month Budget for Lower Division: 30855 ⟵ “Total 9 month Budget for Lower Division | $30,855 | $26,964 | $23,072 | $1,997”
  - column:Total 9 month Budget for Upper Division: 31071 ⟵ “Total 9 month Budget for Upper Division | $31,071 | $27,126 | $23,180 | $2,051”
  - column:Tuition & Fees (Lower Division): 1998 ⟵ “Tuition & Fees (Lower Division) | $2,664 | $1,998 | $1,332 | $666”
  - column:Tuition & Fees (Upper Division): 2160 ⟵ “Tuition & Fees (Upper Division) | $2,880 | $2,160 | $1,440 | $720”
  - column:Books & Supplies: 1578 ⟵ “Books & Supplies | $2,130 | $1,578 | $1,052 | $526”
  - column:Food & Housing: 15221 ⟵ “Food & Housing | $15,221 | $15,221 | $15,221 | ”
  - column:Transportation: 2415 ⟵ “Transportation | $3,220 | $2,415 | $1,610 | $805”
  - column:Miscellaneous: 5686 ⟵ “Miscellaneous | $7,581 | $5,686 | $3,791 | ”
  - column:Loan: 66 ⟵ “Loan | $66 | $66 | $66 | ”
  - column:Total 9 month Budget for Lower Division: 26964 ⟵ “Total 9 month Budget for Lower Division | $30,855 | $26,964 | $23,072 | $1,997”
  - column:Total 9 month Budget for Upper Division: 27126 ⟵ “Total 9 month Budget for Upper Division | $31,071 | $27,126 | $23,180 | $2,051”
  - column:Tuition & Fees (Lower Division): 1332 ⟵ “Tuition & Fees (Lower Division) | $2,664 | $1,998 | $1,332 | $666”
  - column:Tuition & Fees (Upper Division): 1440 ⟵ “Tuition & Fees (Upper Division) | $2,880 | $2,160 | $1,440 | $720”
  - column:Books & Supplies: 1052 ⟵ “Books & Supplies | $2,130 | $1,578 | $1,052 | $526”
  - column:Food & Housing: 15221 ⟵ “Food & Housing | $15,221 | $15,221 | $15,221 | ”
  - column:Transportation: 1610 ⟵ “Transportation | $3,220 | $2,415 | $1,610 | $805”
  - column:Miscellaneous: 3791 ⟵ “Miscellaneous | $7,581 | $5,686 | $3,791 | ”
  - column:Loan: 66 ⟵ “Loan | $66 | $66 | $66 | ”
  - … 8 more rows
### `bc86b7bb318ed6c6` Valencia College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://valenciacollege.edu/finaid/attendance-cost.php (sha256 ee84f155cc72)
- issues: multiple_total_rows
- checks: {"columns": 4, "rows": 9}
  - with_parents_or_family:Tuition & Fees (Lower Division): 2664 ⟵ “Tuition & Fees (Lower Division) | $2,664 | $1,998 | $1,332 | $666”
  - with_parents_or_family:Tuition & Fees (Upper Division): 2880 ⟵ “Tuition & Fees (Upper Division) | $2,880 | $2,160 | $1,440 | $720”
  - with_parents_or_family:Books & Supplies: 2103 ⟵ “Books & Supplies | $2,103 | $1,578 | $1,052 | $526”
  - with_parents_or_family:Food & Housing: 10197 ⟵ “Food & Housing | $10,197 | $10,197 | $10,197 | ”
  - with_parents_or_family:Transportation: 3220 ⟵ “Transportation | $3,220 | $2,415 | $1,610 | $805”
  - with_parents_or_family:Miscellaneous: 7581 ⟵ “Miscellaneous | $7,581 | $5,686 | $3,791 | ”
  - with_parents_or_family:Loan: 66 ⟵ “Loan | $66 | $66 | $66 | ”
  - with_parents_or_family:Total 9 month Budget for Lower Division: 25831 ⟵ “Total 9 month Budget for Lower Division | $25,831 | $21,940 | $18,048 | $1,997”
  - with_parents_or_family:Total 9 month Budget for Upper Division: 26047 ⟵ “Total 9 month Budget for Upper Division | $26,047 | $22,102 | $18,156 | $2,051”
  - with_parents_or_family:Tuition & Fees (Lower Division): 1998 ⟵ “Tuition & Fees (Lower Division) | $2,664 | $1,998 | $1,332 | $666”
  - with_parents_or_family:Tuition & Fees (Upper Division): 2160 ⟵ “Tuition & Fees (Upper Division) | $2,880 | $2,160 | $1,440 | $720”
  - with_parents_or_family:Books & Supplies: 1578 ⟵ “Books & Supplies | $2,103 | $1,578 | $1,052 | $526”
  - with_parents_or_family:Food & Housing: 10197 ⟵ “Food & Housing | $10,197 | $10,197 | $10,197 | ”
  - with_parents_or_family:Transportation: 2415 ⟵ “Transportation | $3,220 | $2,415 | $1,610 | $805”
  - with_parents_or_family:Miscellaneous: 5686 ⟵ “Miscellaneous | $7,581 | $5,686 | $3,791 | ”
  - with_parents_or_family:Loan: 66 ⟵ “Loan | $66 | $66 | $66 | ”
  - with_parents_or_family:Total 9 month Budget for Lower Division: 21940 ⟵ “Total 9 month Budget for Lower Division | $25,831 | $21,940 | $18,048 | $1,997”
  - with_parents_or_family:Total 9 month Budget for Upper Division: 22102 ⟵ “Total 9 month Budget for Upper Division | $26,047 | $22,102 | $18,156 | $2,051”
  - with_parents_or_family:Tuition & Fees (Lower Division): 1332 ⟵ “Tuition & Fees (Lower Division) | $2,664 | $1,998 | $1,332 | $666”
  - with_parents_or_family:Tuition & Fees (Upper Division): 1440 ⟵ “Tuition & Fees (Upper Division) | $2,880 | $2,160 | $1,440 | $720”
  - with_parents_or_family:Books & Supplies: 1052 ⟵ “Books & Supplies | $2,103 | $1,578 | $1,052 | $526”
  - with_parents_or_family:Food & Housing: 10197 ⟵ “Food & Housing | $10,197 | $10,197 | $10,197 | ”
  - with_parents_or_family:Transportation: 1610 ⟵ “Transportation | $3,220 | $2,415 | $1,610 | $805”
  - with_parents_or_family:Miscellaneous: 3791 ⟵ “Miscellaneous | $7,581 | $5,686 | $3,791 | ”
  - with_parents_or_family:Loan: 66 ⟵ “Loan | $66 | $66 | $66 | ”
  - … 8 more rows
### `c5e4c80502b9ef20` Valencia College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://valenciacollege.edu/about/documents/valencia-college-facts.pdf (sha256 45b2be41ed80)
- issues: arrangement_unlabeled, implausible_amount, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 5, "rows": 20}
  - column:Degree Seeking:: 52343 ⟵ “Degree Seeking: | 52,343”
  - column:Dual Enrollment:: 6501 ⟵ “Dual Enrollment: | 6,501”
  - column:Continuing Education:: 7758 ⟵ “Continuing Education: | 7,758 | (Fall 2024)”
  - column:Personal Interest:: 2495 ⟵ “Personal Interest: | 2,495 | County of Residence : | 17%”
  - column:Transient:: 3288 ⟵ “Transient: | 3,288 | Orange County: | 54%”
  - column:Other **:: 2961 ⟵ “Other **: | 2,961 | Osceola County: | 21%”
  - column:Associate in Arts (A.A.):: 1 ⟵ “Associate in Arts (A.A.): | 1 | Associate in Arts (A.A.):: | 74%, 6,480”
  - column:Tuition:: 103.06 ⟵ “Tuition: | $103.06 | $112.19”
  - column:Bachelor’s Degrees (B.A.S. and B.S.):: 7 ⟵ “Bachelor’s Degrees (B.A.S. and B.S.): | 7 | Bachelor’s Degrees (B.A.S. and B.S.): 9% | 827”
  - column:Total Degrees Awarded:: 8826 ⟵ “Total Degrees Awarded: | 8,826”
  - column:State: 390.96 ⟵ “State | $390.96 | $427.59 | Certificate Programs”
  - column:Bright Futures Recipients:: 1062 ⟵ “Bright Futures Recipients: | 1,062 | * Source: 2023-2024 Florida Education and Training Placement”
  - column:Full-Time Staff:: 1272 ⟵ “Full-Time Staff: | 1,272”
  - column:Part-Time Staff:: 769 ⟵ “Part-Time Staff: | 769 | 3437 W.D. Judge Drive,”
  - column:Full-Time Faculty:: 622 ⟵ “Full-Time Faculty: | 622”
  - column:Part-Time Faculty:: 2051 ⟵ “Part-Time Faculty: | 2,051 | 1800 S. Kirkman Road,”
  - column:Total:: 4714 ⟵ “Total: | 4,714 | (Established: 2016),”
  - column:Actual Revenues:: 280429851 ⟵ “Actual Revenues: | $280,429,851 | Downtown Campus, (Established: 2019),”
  - column:Valencia College Students:: 2193 ⟵ “Valencia College Students: | 2,193 | 701 N. Econlockhatchee Trail,”
  - column:Total Amount Awarded:: 1820113 ⟵ “Total Amount Awarded: | $1,820,113 | 95 acres, | Explore Valencia location”
  - column:Tuition:: 112.19 ⟵ “Tuition: | $103.06 | $112.19”
  - column:State: 427.59 ⟵ “State | $390.96 | $427.59 | Certificate Programs”
  - column:Tuition: (2): 7815 ⟵ “Tuition: | Total Certificates Awarded: | 7,815”
  - column:Bachelor’s Degrees (B.A.S. and B.S.):: 827 ⟵ “Bachelor’s Degrees (B.A.S. and B.S.): | 7 | Bachelor’s Degrees (B.A.S. and B.S.): 9% | 827”
  - column:In-State: 39 ⟵ “In-State | Associate | Bachelor’s | Associate in Science (A.S.): | 39 | Associate in Science (A.S.):: | 17%, | 1,519”
  - … 1 more rows
### `mb37f76756b35022` Valencia College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://valenciacollege.edu/admissions/dual-enrollment/parents.php (sha256 8c59483e3df5)
- issues: multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 8, "tiers": 1}
  - max_credit_hours_per_term: 13 ⟵ “Dual Enrollment students may register for up to 13 credits for fall and spring semesters”
  - eligibility_tier: 2.0 ⟵ “a minimum term and cumulative GPA of 2.0.”
  - eligibility_tier: 2.0 ⟵ “a minimum term and cumulative GPA of 2.0.”
  - eligibility_tier: 2.0 ⟵ “a minimum term and cumulative GPA of 2.0.”
  - eligibility_tier: 2.0 ⟵ “a minimum term and cumulative GPA of 2.0.”
  - eligibility_tier: 2.0 ⟵ “a minimum term and cumulative GPA of 2.0.”
  - eligibility_tier: 2.0 ⟵ “must achieve a minimum term and cumulative overall GPA of 2.0 to return to good”
  - eligibility_tier: 3.0 ⟵ “All dual enrollment students must maintain a high school 3.0 cumulative GPA,             for a wide range of subjects. The CLEP is offered at Valencia College.”
  - eligibility_tier: 3.0 ⟵ “Enrolled, must have a minimum unweighted high school GPA of 3.0 or higher. To learn more”
  - max_credit_hours_per_term: 13 ⟵ “| You can register for up to 13 credits (~4 courses) each Fall and Spring term and 7”
### `ce2622c0a5d5eba7` Webber International University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.webber.edu/transfer-students/ (sha256 cb78aaf141c9)
- issues: conflicting_values:max_transfer_credits
- checks: {"fields": []}

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 3; pages by category: 

## Blocked by the site (every request refused; needs the browser fallback)

- Lynn University (`ipeds-132657`)
- Edward Waters University (`ipeds-133526`)
- Florida Memorial University (`ipeds-133979`)
- Keiser University-Ft Lauderdale (`ipeds-135081`)
- University of Miami (`ipeds-135726`)
- Palm Beach Atlantic University (`ipeds-136330`)
- Stetson University (`ipeds-137546`)
- Southeastern University (`ipeds-137564`)
- Hodges University (`ipeds-367884`)
- Everglades University (`ipeds-385619`)
- Polytechnic University of Puerto Rico-Miami (`ipeds-456481`)

## Leads: official pages found with no extracted record

- AdventHealth University: admissions_tests, clep_credit, dual_enrollment, transfer_credit, degree_requirements
- Albizu University-Miami: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, degree_requirements
- Ana G. Mendez University: cost_of_attendance, admissions_tests, ap_credit, clep_credit, transfer_credit, degree_requirements
- Ave Maria University: cost_of_attendance, admissions_tests, merit_scholarships, degree_requirements
- Baptist University of Florida: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements, aid_appeals
- Barry University: admissions_tests, common_data_set, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Beacon College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Bethune-Cookman University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Broward College: admissions_tests, transfer_credit, statewide_articulation, residency, degree_requirements
- Chipola College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- College of Central Florida: admissions_tests, common_data_set, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Daytona State College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency
- Eastern Florida State College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, aid_appeals
- Eckerd College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, residency, degree_requirements
- Embry-Riddle Aeronautical University-Daytona Beach: tuition_fees, cost_of_attendance
- Embry-Riddle Aeronautical University-Worldwide: tuition_fees, cost_of_attendance, transfer_credit
- Faith Theological Seminary and Christian College: degree_requirements
- Flagler College: admissions_tests, common_data_set, merit_scholarships, ap_credit, ib_credit, dual_enrollment, degree_requirements
- Florida Agricultural and Mechanical University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Florida Atlantic University: admissions_tests, merit_scholarships, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Florida College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Florida Gateway College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Florida Gulf Coast University: admissions_tests, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Florida Institute of Technology: tuition_fees, cost_of_attendance, admissions_tests, ib_credit, transfer_credit, residency, degree_requirements
- Florida Institute of Technology-Online: tuition_fees, cost_of_attendance, admissions_tests, ib_credit, transfer_credit, residency, degree_requirements
- Florida International University: tuition_fees, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Florida Polytechnic University: tuition_fees, cost_of_attendance, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Florida SouthWestern State College: tuition_fees, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Florida Southern College: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Florida State College at Jacksonville: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Florida State University: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Gulf Coast State College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Herzing University-Orlando: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Herzing University-Tampa: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Hillsborough Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency
- Hobe Sound Bible College: tuition_fees, cost_of_attendance, merit_scholarships, degree_requirements
- Indian River State College: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency
- Jacksonville University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements, aid_appeals
- Johnson University Florida: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Jones Technical Institute: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, degree_requirements, aid_appeals
- Lake-Sumter State College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Miami Dade College: cost_of_attendance, admissions_tests, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- New College of Florida: admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency
- North Florida College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Northwest Florida State College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, clep_credit, dual_enrollment, statewide_articulation, residency, degree_requirements, aid_appeals
- Nova Southeastern University: tuition_fees, cost_of_attendance, admissions_tests, residency, degree_requirements
- Palm Beach State College: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, residency
- Pasco-Hernando State College: admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements, aid_appeals
- Pensacola State College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Polk State College: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- Polytechnic University of Puerto Rico-Orlando: admissions_tests, transfer_credit
- Ringling College of Art and Design: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements
- Rollins College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Saint Johns River State College: tuition_fees, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Saint Leo University: tuition_fees, admissions_tests, ap_credit, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- Santa Fe College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Seminole State College of Florida: admissions_tests, merit_scholarships, clep_credit, statewide_articulation, residency, degree_requirements
- South Florida Bible College and Theological Seminary: tuition_fees, cost_of_attendance, merit_scholarships, transfer_credit, degree_requirements
- South Florida State College: tuition_fees, cost_of_attendance, admissions_tests, clep_credit, dual_enrollment, transfer_credit, degree_requirements
- St Petersburg College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- St. John Vianney College Seminary: degree_requirements
- St. Thomas University: admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency, degree_requirements, aid_appeals
- State College of Florida-Manatee-Sarasota: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Tallahassee Community College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- The College of the Florida Keys: admissions_tests, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- The University of Tampa: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Trinity College of Florida: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements, aid_appeals
- University of Central Florida: admissions_tests, merit_scholarships, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Florida: admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- University of Florida-Online: admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- University of Fort Lauderdale: cost_of_attendance, admissions_tests, transfer_credit, residency
- University of North Florida: admissions_tests, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- University of South Florida: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- University of West Florida: admissions_tests, merit_scholarships, residency, degree_requirements
- Valencia College: cost_of_attendance, admissions_tests, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Warner University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, aid_appeals
- Webber International University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation
- Yeshivah Gedolah Rabbinical College: tuition_fees, merit_scholarships
