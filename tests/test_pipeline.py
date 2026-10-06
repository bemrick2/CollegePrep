"""Research pipeline: parsing, extraction, crawl politeness/resume, review and promotion rules."""
import functools, json, shutil, sys, tempfile, threading, unittest
from datetime import date
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pipeline import exams, registry, review, text as T, topics  # noqa: E402
from pipeline import promote as P  # noqa: E402
from pipeline.crawl import Fetcher, Run, crawl  # noqa: E402
from pipeline.extractors import appeals, catalog, cds, common, costs, credit, dual, merit, statepolicy, transfer  # noqa: E402

FIX = ROOT / 'tests/fixtures/pipeline'
INST = {'institution_key': 'ipeds-999999', 'control': 'public', 'folder': 'example'}
ENTRY = {'url': 'https://example.edu/x', 'sha256': 'ab' * 32, 'fetched_at': '2026-10-02T12:00:00+00:00', 'kind': 'html'}


def page(name):
    return T.parse_html((FIX / name).read_bytes(), 'https://example.edu/finaid/')


class TextTests(unittest.TestCase):
    def test_year_labels_need_consecutive_years(self):
        self.assertEqual(T.year_labels('2026-2027 and 2026–27, not 2024-2026 or $2026-27'), {'2026-27': 2})
        self.assertEqual(T.dominant_year('nothing here', 'Fees 2025-26'), ('2025-26', 'labeled_in_title'))
        self.assertEqual(T.dominant_year('2025-26 rates; 2026-27 rates', '')[1], 'ambiguous_year_labels')
        self.assertEqual(T.dominant_year('no label', ''), (None, 'source_unlabeled'))
        self.assertEqual(T.current_academic_year(date(2026, 10, 2)), '2026-27')
        self.assertEqual(T.current_academic_year(date(2027, 3, 1)), '2026-27')

    def test_money_and_numbers_are_not_guessed(self):
        self.assertEqual(T.money_values('$11,084 and $12.50 and $3'), [11084, 12.5, 3])
        self.assertEqual(T.plain_number('$1,400'), 1400)
        self.assertIsNone(T.plain_number('1,400 per year'))

    def test_html_tables_links_and_skipped_scripts(self):
        p = T.parse_html(b'<title>t</title><script>var x=1</script><h2>H</h2><table><tr><td>a</td><td>b</td></tr></table><a href="/y#z">Y</a>', 'https://e.edu/a/')
        self.assertNotIn('var x', p.text)
        self.assertEqual(p.tables[0]['rows'], [['a', 'b']])
        self.assertEqual(p.tables[0]['heading'], 'H')
        q = T.parse_html(b'<h2>2026-2027 Cost of Attendance</h2><h3>Undergraduate (In-State)</h3><table><tr><td>a</td></tr></table>')
        self.assertEqual((q.tables[0]['heading'], q.tables[0]['year_heading']), ('Undergraduate (In-State)', '2026-2027 Cost of Attendance'))
        self.assertEqual(p.links, [('https://e.edu/y', 'Y')])


class ExamAndTopicTests(unittest.TestCase):
    def test_specific_exam_patterns_win(self):
        self.assertEqual(exams.match('AP', 'Calculus BC')[0], 'AP-CALCULUS-BC')
        self.assertEqual(exams.match('AP', 'AP Physics C: Electricity and Magnetism')[0], 'AP-PHYSICS-C-ELECTRICITY-MAGNETISM')
        self.assertEqual(exams.match('AP', 'English Literature and Composition')[0], 'AP-ENGLISH-LITERATURE-COMPOSITION')
        self.assertEqual(exams.match('CLEP', 'History of the United States II')[0], 'CLEP-HISTORY-OF-THE-UNITED-STATES-II')
        self.assertEqual(exams.match('IB', 'Biology HL')[1], 'IB Biology (HL)')
        self.assertIsNone(exams.match('AP', 'Scores of 2 receive no credit'))
        self.assertIsNone(exams.match('AP', 'Calculus'))  # AB or BC is never assumed

    def test_link_scores(self):
        self.assertGreater(topics.link_score('https://u.edu/ir/common-data-set-2025-2026.pdf', 'CDS'), 40)
        self.assertEqual(topics.link_score('https://u.edu/news/scholarship-winner'), -1)
        self.assertEqual(topics.link_score('https://u.edu/about'), 0)
        today = date(2026, 10, 2)
        self.assertEqual(topics.link_score('https://u.edu/ir/CDS-2017-2018.pdf', 'Common Data Set', today), -1)
        self.assertEqual(topics.link_score('https://u.edu/catalog06-07.pdf', 'Catalog', today), -1)
        self.assertGreater(topics.link_score('https://u.edu/2026-27-cost-of-attendance.pdf', 'Cost', today),
                           topics.link_score('https://u.edu/cost-of-attendance', 'Cost', today))


class ExtractorTests(unittest.TestCase):
    def test_ap_table(self):
        [c] = credit.extract(INST, ENTRY, page('ap.html'), '2026-27')
        r = c['record']
        self.assertEqual((c['domain'], r['policy_kind'], c['academic_year'], c['year_basis']), ('credit_policies', 'AP', '2026-27', 'labeled_in_title'))
        self.assertEqual(r['verification_status'], 'unverified')
        eq = {(e['exam_or_course_code'], e['minimum_score']): e for e in r['equivalencies']}
        self.assertEqual(eq[('AP-CALCULUS-AB', '4 or 5')]['institution_course_equivalent'], 'MATH 1910, MATH 1920')  # rowspan
        self.assertEqual(eq[('AP-CALCULUS-AB', '4 or 5')]['credits_awarded'], 8)
        self.assertEqual(eq[('AP-UNITED-STATES-HISTORY', '3')]['institution_course_equivalent'], 'HIST 2010')
        self.assertEqual(len(r['equivalencies']), 7)
        self.assertEqual(c['issues'], [])
        self.assertTrue(all(e['snippet'] for e in c['evidence']))

    def test_one_table_per_exam_layout(self):
        # Real layout: the exam name sits in a button/label above each small score-tier table.
        html = '<title>Advanced Placement (AP)</title>' + ''.join(
            f'<button>{name}</button><table><tr><th>AP Score</th><th>Credit Hours</th><th>Course Equivalent*</th></tr>{rows}</table>'
            for name, rows in [('Art History', '<tr><td>3, 4, 5</td><td>3</td><td>ARTH 2010</td></tr>'),
                               ('Biology', '<tr><td>3</td><td>4</td><td>BIOL 1010</td></tr><tr><td>4, 5</td><td>8</td><td>BIOL 1110 &amp; 1120</td></tr>'),
                               ('Calculus AB', '<tr><td>3</td><td>3</td><td>MATH 1830</td></tr>')])
        [c] = credit.extract(INST, ENTRY, T.parse_html(html), '2026-27')
        got = [(e['exam_or_course_code'], e['minimum_score'], e['credits_awarded'], e['institution_course_equivalent']) for e in c['record']['equivalencies']]
        self.assertEqual(got, [('AP-ART-HISTORY', '3, 4, 5', 3, 'ARTH 2010'), ('AP-BIOLOGY', '3', 4, 'BIOL 1010'),
                               ('AP-BIOLOGY', '4, 5', 8, 'BIOL 1110 & 1120'), ('AP-CALCULUS-AB', '3', 3, 'MATH 1830')])

    def test_pdf_credit_chart_lines(self):
        text = """Advanced Placement (AP) Credit Chart 2026-2027
AP Exam                         Score     Course Equivalent            Hours
Biology                         4         BIOL 1110, BIOL 1120         8
Calculus BC                     3         MATH 1910                    4
English Language & Composition  3         ENGL 1010                    3
Scores of 1 or 2 receive no credit."""
        [c] = credit.extract(INST, {**ENTRY, 'kind': 'pdf'}, T.Page(text, 'Advanced Placement (AP) Credit Chart 2026-2027'), '2026-27')
        got = [(e['exam_or_course_code'], e['minimum_score'], e['institution_course_equivalent'], e['credits_awarded']) for e in c['record']['equivalencies']]
        self.assertEqual(got, [('AP-BIOLOGY', '4', 'BIOL 1110, BIOL 1120', 8), ('AP-CALCULUS-BC', '3', 'MATH 1910', 4),
                               ('AP-ENGLISH-LANGUAGE-COMPOSITION', '3', 'ENGL 1010', 3)])
        self.assertEqual((c['academic_year'], c['year_basis']), ('2026-27', 'labeled_in_title'))

    def test_stale_shared_heading_never_names_tables(self):
        p = T.Page('', 'Advanced Placement (AP)', [
            {'heading': 'Art History', 'caption': '', 'rows': [['AP Score', 'Credit Hours', 'Course Equivalent'], ['3', '3', 'ARTH 2010']]},
            {'heading': 'Art History', 'caption': '', 'rows': [['AP Score', 'Credit Hours', 'Course Equivalent'], ['3', '4', 'BIOL 1010']]}])
        self.assertEqual(credit.extract(INST, ENTRY, p, '2026-27'), [])

    def test_cost_table_copies_totals_and_checks_reconciliation(self):
        cands = {c['record']['residency']: c for c in costs.extract(INST, ENTRY, page('coa.html'), '2026-27')}
        ins = cands['in_state']['record']
        self.assertEqual((ins['tuition'], ins['mandatory_fees'], ins['total_cost_of_attendance']), (9800, 1284, 28540))
        self.assertIsNone(ins['on_campus_food_housing'])  # separate housing and food rows are never summed
        self.assertTrue(cands['in_state']['checks']['components_reconcile'])
        self.assertEqual(cands['out_of_state']['record']['tuition'], 27400)
        self.assertEqual(cands['out_of_state']['academic_year'], '2026-27')
        self.assertNotIn('student_population', ins)  # only set when the table or page title says undergraduate

    def test_missing_total_stays_null_and_unreconciled_is_flagged(self):
        html = (FIX / 'coa.html').read_text().replace('<tr><td>Total</td><td>$28,540</td><td>$46,140</td></tr>', '')
        c = {x['record']['residency']: x for x in costs.extract(INST, ENTRY, T.parse_html(html), '2026-27')}['in_state']
        self.assertIsNone(c['record']['total_cost_of_attendance'])
        bad = (FIX / 'coa.html').read_text().replace('$28,540', '$29,000')
        c = {x['record']['residency']: x for x in costs.extract(INST, ENTRY, T.parse_html(bad), '2026-27')}['in_state']
        self.assertIn('components_do_not_reconcile', c['issues'])

    def test_unlabeled_public_page_without_residency_goes_to_exceptions(self):
        html = ('<title>Tuition</title><table><tr><th>Item</th><th>Amount</th></tr><tr><td>Tuition</td><td>$5,000</td></tr>'
                '<tr><td>Fees</td><td>$500</td></tr><tr><td>Total</td><td>$5,500</td></tr></table>')
        [c] = costs.extract(INST, ENTRY, T.parse_html(html), '2026-27')
        self.assertIn('residency_unknown', c['issues'])
        self.assertEqual(c['year_basis'], 'source_unlabeled')
        self.assertEqual(c['record']['academic_year_basis'], 'aid_year_in_force_at_review_source_unlabeled')
        [p] = costs.extract({**INST, 'control': 'private_nonprofit'}, ENTRY, T.parse_html(html), '2026-27')
        self.assertEqual(p['record']['residency'], 'not_applicable')
        self.assertNotIn('residency_unknown', p['issues'])

    def test_direct_cost_total_is_not_cost_of_attendance(self):
        direct = ('<title>Tuition 2026-2027</title><table><tr><th>2026-2027 Costs</th><th>Per Year</th></tr>'
                  '<tr><td>Tuition</td><td>$42,500</td></tr><tr><td>Clinical Fees</td><td>$200</td></tr>'
                  '<tr><td>Room</td><td>$6,300</td></tr><tr><td>Total</td><td>$49,000</td></tr></table>')
        [c] = costs.extract({**INST, 'control': 'private_nonprofit'}, ENTRY, T.parse_html(direct), '2026-27')
        self.assertIsNone(c['record']['total_cost_of_attendance'])
        self.assertEqual(c['record']['total_direct_cost'], 49000)
        self.assertIsNone(c['record']['mandatory_fees'])  # 'Clinical Fees' is not a mandatory fee
        union = ('<title>Cost of Attendance 2026-2027</title><table><tr><th>Item</th><th>Amount</th></tr>'
                 '<tr><td>Tuition</td><td>$41,170</td></tr><tr><td>Mandatory Fees</td><td>$1,520</td></tr>'
                 '<tr><td>Total Direct Costs</td><td>$42,690</td></tr><tr><td>Transportation</td><td>$3,316</td></tr>'
                 '<tr><td>Total Indirect Costs</td><td>$3,316</td></tr><tr><td>Total COA</td><td>$46,006</td></tr></table>')
        [c] = costs.extract({**INST, 'control': 'private_nonprofit'}, ENTRY, T.parse_html(union), '2026-27')
        self.assertEqual(c['record']['total_cost_of_attendance'], 46006)
        self.assertEqual(c['record']['mandatory_fees'], 1520)
        self.assertNotIn('multiple_total_rows', c['issues'])

    def test_common_data_set_totals_only(self):
        text = (FIX / 'cds.txt').read_text()
        [c] = cds.extract(INST, {**ENTRY, 'kind': 'pdf'}, T.Page(text, 'CDS'), '2026-27')
        r = c['record']
        self.assertEqual((c['academic_year'], r['entering_fall_year']), ('2025-26', 2025))
        self.assertEqual((r['applications'], r['admits'], r['enrolled']), (53841, 23464, 7143))
        self.assertEqual((r['sat_composite_25'], r['sat_composite_50'], r['sat_composite_75']), (1280, 1330, 1380))
        self.assertEqual((r['sat_math_25'], r['sat_math_75'], r['act_25'], r['act_75']), (630, 700, 26, 31))
        self.assertEqual(c['issues'], [])
        zeros = text.replace('21,707', '0').replace('32,134', '0').replace('53,841', '0')  # Covenant (GA r1): 0 applied, students enrolled
        [z] = cds.extract(INST, {**ENTRY, 'kind': 'pdf'}, T.Page(zeros, 'CDS'), '2026-27')
        self.assertIn('zero_counts_with_enrollment', z['issues'])
        no_total = '\n'.join(l for l in text.splitlines() if 'who applied' not in l or 'men' in l)
        [c] = cds.extract(INST, {**ENTRY, 'kind': 'pdf'}, T.Page(no_total, 'CDS'), '2026-27')
        self.assertNotIn('applications', c['record'])  # never summed from the by-sex rows
        self.assertIn('c1_totals_incomplete', c['issues'])
        implausible = text.replace('ACT Composite                          26', 'ACT Composite                          46')
        [c] = cds.extract(INST, {**ENTRY, 'kind': 'pdf'}, T.Page(implausible, 'CDS'), '2026-27')
        self.assertIn('act_implausible', c['issues'])
        self.assertNotIn('act_25', c['record'])


    def test_common_data_set_residency_table_template(self):
        text = """Common Data Set 2025-2026
C1   First-time, first-year students
     Total first-time, first-year males who applied                                21,707
     Total first-time, first-year (degree-seeking) who applied                     In-State      Out-of-State International Unknown   Total

                                                                                       11,980           41,408          452       0     53,841
     Total first-time, first-year (degree-seeking) who were admitted                    8,725           14,526          213       0     23,464
     Total first-time, first-year (degree-seeking)
     who enrolled                                                                       4,326            2,764           53       0       7,143
     SAT Evidence-Based Reading and

     Writing                                      640            670           700
"""
        [c] = cds.extract(INST, {**ENTRY, 'kind': 'pdf'}, T.Page(text, 'CDS'), '2026-27')
        r = c['record']
        self.assertEqual((r['applications'], r['admits'], r['enrolled']), (53841, 23464, 7143))
        self.assertEqual((r['sat_reading_25'], r['sat_reading_50'], r['sat_reading_75']), (640, 670, 700))
        self.assertIn('applications_breakdown_does_not_reconcile', c['issues'])  # 11,980+41,408+452+0 = 53,840
        self.assertNotIn('admits_breakdown_does_not_reconcile', c['issues'])


    def test_merit_list_and_grid(self):
        html = """<title>Freshman Merit Scholarships 2026-2027</title><h2>Academic Scholarships</h2><table>
<tr><th>Scholarship</th><th>Minimum GPA</th><th>ACT</th><th>SAT</th><th>Annual Amount</th></tr>
<tr><td>Presidential</td><td>3.75</td><td>30</td><td>1390</td><td>$12,000</td></tr>
<tr><td>Dean's</td><td>3.5+</td><td>27-29</td><td>1280</td><td>$8,000 - $10,000</td></tr>
<tr><td>Need-blind Grant</td><td>3.0 or ACT 21</td><td></td><td></td><td>Up to $4,000</td></tr></table>"""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(html), '2026-27')}
        self.assertEqual(got['Presidential']['thresholds'], {'gpa_min': 3.75, 'act_min': 30, 'sat_min': 1390})
        self.assertEqual(got["Dean's"]['thresholds'], {'gpa_min': 3.5, 'sat_min': 1280})  # '27-29' is a range: text only
        self.assertEqual((got["Dean's"]['award_min'], got["Dean's"]['award_max']), (8000, 10000))
        self.assertNotIn('thresholds', got['Need-blind Grant'])  # mixed wording is never parsed
        self.assertEqual(got['Need-blind Grant']['gpa_requirement'], '3.0 or ACT 21')
        grid = """<title>Merit Scholarship Grid</title><h2>Merit Scholarship Grid 2026-27</h2><table>
<tr><th>GPA</th><th>ACT 21-23 / SAT 1060-1150</th><th>ACT 24-27 / SAT 1160-1290</th></tr>
<tr><td>3.0-3.49</td><td>$2,000</td><td>$4,000</td></tr><tr><td>3.5-4.0</td><td>$4,000</td><td>$6,000</td></tr></table>"""
        [c] = merit.extract(INST, ENTRY, T.parse_html(grid), '2026-27')
        self.assertEqual(len(c['record']['award_tiers']), 4)
        self.assertEqual(c['record']['award_tiers'][3], {'gpa': '3.5-4.0', 'test': 'ACT 24-27 / SAT 1160-1290', 'amount_text': '$6,000'})
        self.assertEqual((c['record']['award_min'], c['record']['award_max']), (2000, 6000))


    def test_appeals_are_queued_and_never_qualify(self):
        html = """<title>Scholarship FAQ</title><h2>Financial Aid Appeals</h2><p>If your family has experienced special
circumstances such as job loss, you may submit a special circumstances appeal to the Office of Financial Aid.
UT cannot match scholarship or aid offers from other institutions. Students who are not meeting Satisfactory
Academic Progress may file a SAP appeal each term.</p>"""
        got = {c['record']['appeal_kind']: c for c in appeals.extract(INST, ENTRY, T.parse_html(html), '2026-27')}
        self.assertEqual(set(got), {'need_based_special_circumstances', 'competing_offer_review', 'sap_appeal'})
        self.assertFalse(got['competing_offer_review']['record']['offered'])  # negative statement recorded as such
        self.assertTrue(got['need_based_special_circumstances']['record']['offered'])
        for c in got.values():
            self.assertFalse(c['record']['qualifies_for_paid_addon'])
            self.assertIn('semantic_review_required', c['issues'])
            self.assertTrue(c['evidence'][0]['snippet'])


    def test_transfer_rules_from_sentences(self):
        html = """<title>Transfer Credit Policy</title><p>Courses completed with a grade of C or better transfer to the
university. A maximum of 64 semester hours may be transferred from community colleges. Students must complete the
last 30 hours in residence at the university.</p>"""
        [c] = transfer.extract(INST, ENTRY, T.parse_html(html), '2026-27')
        r = c['record']
        self.assertEqual((r['min_grade'], r['max_transfer_credits'], r['residency_requirement_credits']), ('C', 64, 30))
        self.assertEqual(c['issues'], [])
        conflict = html + '<p>Transfer courses with a grade of D or better are accepted for elective credit.</p>'
        [c] = transfer.extract(INST, ENTRY, T.parse_html(conflict), '2026-27')
        self.assertNotIn('min_grade', c['record'])
        self.assertIn('conflicting_values:min_grade', c['issues'])


    def test_tn_r5_review_regressions(self):
        """Defects found reviewing Tennessee run 2026-10-02-r5."""
        # MTSU / Walters State: course numbers are not academic-year labels.
        self.assertEqual(T.year_labels('Physics 1 | 4 or above | PHYS 2010/2011* | 4; BIOL 2010-2011'), {})
        self.assertEqual(T.year_labels('Catalog 2026-2027; FY 2026-27'), {'2026-27': 2})
        # APSU Bibb scholarship: a two-decimal college GPA is kept whole.
        [c] = self._de('<p>Students must maintain a cumulative college GPA of 2.75 to be eligible for the award in future semesters.</p>')
        self.assertEqual(c['record']['dual_enrollment']['college_gpa_to_continue'], 2.75)
        # Welch / Nashville State / Columbia State: course-GPA, waiver and placement lines are not HS eligibility.
        got = self._de('<p>A 2.0 GPA for all postsecondary courses attempted under the Dual Enrollment Grant is required.</p>'
                       '<p>Students with a GPA of 3.60 or higher will be able to have prerequisites waived.</p>'
                       '<p>If a student has not taken the ACT or does not have a 3.6 cumulative GPA, they can schedule a placement exam.</p>'
                       '<p>Juniors and seniors need a minimum GPA of 3.0.</p>')
        self.assertEqual([t['min_hs_gpa'] for t in got[0]['record']['dual_enrollment']['eligibility_tiers']], [3.0])
        # Grant payments per credit hour are not prices.
        [c] = self._de('<p>For courses 6-10, the Dual Enrollment Grant provides $100 per credit hour. Tuition is $197 per credit hour.</p>')
        self.assertEqual([(x['amount'], x['kind']) for x in c['record']['dual_enrollment']['per_credit_hour_charges']], [(100, 'state_grant'), (197, 'tuition')])
        # Rhodes / TN Tech: pass/fail-only and module-scoped grade rules are not the general minimum grade.
        html = ('<title>College Credit Transfer Policies</title><p>Transfer courses taken on a Pass/Fail basis must be passed with a grade '
                'of C or better. Courses to be transferred under the University Track Module must have been completed with the grade of "C" or better.</p>')
        self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html(html), '2026-27'), [])
        # Maryville / ETSU / APSU / Nashville State: merged cells, placeholders, retention tables and "up to" amounts.
        html = """<title>Scholarships &amp; Awards for First-Year Students</title><h2>Academic Scholarship Information</h2><table>
<tr><th>Scholarship</th><th>Amount</th><th>GPA</th></tr>
<tr><td>Covenant Stone Scholarship3.5+ GPA.</td><td>Up to $22,000 per year on-campus. Up to $16,000 per year off-campus.</td><td></td></tr>
<tr><td>Theatre ScholarshipOpen to all actors and/or theatre technicians.</td><td>$500 to $5,000 per year</td><td></td></tr>
<tr><td>Creative Arts Scholarship</td><td>Provides In-State Tuition Rate</td><td>See Requirements</td></tr></table>"""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(html), '2026-27')}
        self.assertEqual(got['Covenant Stone Scholarship']['gpa_requirement'], '3.5+ GPA.')
        self.assertEqual(got['Covenant Stone Scholarship']['award_max'], 22000)
        self.assertNotIn('award_min', got['Covenant Stone Scholarship'])  # "up to" prints only a maximum
        self.assertEqual((got['Theatre Scholarship']['award_min'], got['Theatre Scholarship']['award_max']), (500, 5000))
        self.assertNotIn('gpa_requirement', got['Creative Arts Scholarship'])  # "See Requirements" is not a requirement
        retention = html.replace('First-Year Students', 'Academic Scholarship Retention Information')
        self.assertEqual(merit.extract(INST, ENTRY, T.parse_html(retention), '2026-27'), [])
        # Tier rows take the scholarship name from the page title, not the "Award Amounts" table heading.
        tiers = """<title>Orange White Scholarship - One Stop Student Services</title><h3>Award Amounts</h3><table>
<tr><th>Criteria</th><th>Annual Award</th><th>Four-year</th></tr>
<tr><td>3.6+ GPA*,26-27 ACT**</td><td>$1,500</td><td>$6,000</td></tr><tr><td>3.6-3.79 GPA*,28-36 ACT**</td><td>$1,500</td><td>$6,000</td></tr></table>"""
        names = sorted(c['record']['award_name'] for c in merit.extract(INST, ENTRY, T.parse_html(tiers), '2026-27'))
        self.assertTrue(all(n.startswith('Orange White Scholarship: ') for n in names), names)
        # JSCC / MTSU IB: hours read as the course column, and merged hour cells, are exceptions.
        rows = [['CLEP Exam', 'Score', 'Course', 'Credit'], ['American Government', '50', '3', 'POLS 1030'],
                ['Biology', '50', '8', 'BIOL 1110'], ['Calculus', '50', '4', 'MATH 1910']]
        page_ = T.Page('', 'CLEP Credit', [{'rows': rows, 'heading': 'CLEP', 'caption': '', 'lead': ''}], [], [])
        [c] = credit.extract(INST, ENTRY, page_, '2026-27')
        # GA r1: a numeric "Course" column is recognised as hours and the course codes are found by their cells.
        self.assertEqual([(e['institution_course_equivalent'], e['credits_awarded']) for e in c['record']['equivalencies']][:2],
                         [('POLS 1030', 3), ('BIOL 1110', 8)])

    def test_fall_spring_total_columns(self):
        """SC r1 (Presbyterian, Benedict): "Fall | Spring | Total" - the total column is the academic year."""
        html = ('<title>Tuition and Fees 2026-27</title><h3>Residential Students</h3><table><tr><th>Direct Costs</th><th>Fall</th><th>Spring</th><th>Total</th></tr>'
                '<tr><td>Tuition</td><td>22,180</td><td>22,180</td><td>44,360</td></tr><tr><td>Fees</td><td>1,600</td><td>1,600</td><td>3,200</td></tr>'
                '<tr><td>Housing</td><td>3,572</td><td>3,572</td><td>7,144</td></tr><tr><td>Total</td><td>27,352</td><td>27,352</td><td>54,704</td></tr></table>')
        [c] = costs.extract({**INST, 'control': 'private_nonprofit'}, ENTRY, T.parse_html(html), '2026-27')
        self.assertEqual((c['record']['tuition'], c['record']['mandatory_fees'], c['record']['cost_period']), (44360, 3200, 'academic_year'))
        html = ('<title>Tuition and Fees 2026-2027</title><h3>Boarding</h3><table><caption>BOARDING (ON-CAMPUS)</caption>'
                '<tr><td>TUITION</td><td>$8,172</td><td>$8,171</td><td>$16,343</td></tr><tr><td>GENERAL FEES</td><td>$1,061</td><td>$1,061</td><td>$2,122</td></tr>'
                '<tr><td>TECHNOLOGY FEE</td><td>$300</td><td>$300</td><td>$600</td></tr><tr><td>FOOD &amp; HOUSING</td><td>$3,726</td><td>$3,726</td><td>$7,452</td></tr></table>')
        [c] = costs.extract({**INST, 'control': 'private_nonprofit'}, ENTRY, T.parse_html(html), '2026-27')
        self.assertEqual(c['record']['tuition'], 16343)  # headerless: the column that sums the other two is the year

    def test_cost_tables_per_arrangement_and_enrollment(self):
        """AL r1: Enterprise State prints one table per living arrangement (named in the row-label header) and a
        less-than-half-time table; Alabama State prints two 'Subtotal' rows."""
        def tbl(first, rows):
            return {'heading': 'In State', 'caption': '', 'lead': '', 'rows': [[first, '4 Month', '9 Month', '12 Month']] + rows}
        rows = lambda housing: [['Tuition & Fees', '$2940.00', '$5880.00', '$8820.00'], ['Housing & Food', housing[0], housing[1], housing[2]],
                                ['Books, Supplies, & Equipment', '$1500.00', '$3000.00', '$4500.00'], ['Total', '$9000.00', '$24269.00', '$30000.00']]
        p = T.Page('Cost of Attendance 2026-2027', 'Cost of Attendance 2026-2027',
                   [tbl('With Parent', rows(('$3847.00', '$7694.00', '$10259.00'))), tbl('Off Campus', rows(('$7695.00', '$15389.00', '$20518.00'))),
                    tbl('Less Than Half-Time Enrollment', rows(('$1.00', '$2.00', '$3.00')))], [], [])
        [c] = costs.extract({**INST, 'state': 'AL'}, ENTRY, p, '2026-27')
        part = T.Page('Cost of Attendance 2026-2027', 'Cost of Attendance 2026-2027', [p.tables[2]], [], [])
        self.assertEqual(costs.extract({**INST, 'state': 'AL'}, ENTRY, part, '2026-27'), [])  # less-than-half-time budget
        r = c['record']
        self.assertEqual((r['residency'], r['living_arrangement'], r['components']['Housing & Food']), ('in_state', 'off_campus_not_with_family', 15389))
        dup = T.Page('Cost of Attendance 2026-2027', 'Cost of Attendance 2026-2027', [{'heading': 'Cost of Attendance', 'caption': '', 'lead': '', 'rows': [
            ['', 'In-State', 'Out-of-State'], ['Tuition/Fees', '$11,068', '$19,936'], ['Room/Board', '$6,050', '$6,050'], ['Subtotal', '$17,118', '$25,986'],
            ['Books', '$1,320', '$1,320'], ['Transportation', '$3,000', '$3,000'], ['Subtotal', '$4,320', '$4,320'], ['Estimated Total', '$21,438', '$30,306']]}], [], [])
        got = {c['record']['residency']: c['record']['components'] for c in costs.extract({**INST, 'state': 'AL'}, ENTRY, dup, '2026-27')}
        self.assertEqual((got['in_state']['Subtotal'], got['in_state']['Subtotal (2)']), (17118, 4320))

    def test_id_r1_rules(self):
        """ID r1: New Saint Andrews "Reward" column and "$5,000 or more"; BYU-Idaho's transposed table; CSI's
        financial-aid and continuation GPA lines are not dual-enrollment eligibility."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Merit Scholarships</h2><table><tr><th>Scholarship</th><th>Eligibility</th><th>Reward</th><th>Renewal</th></tr>'
            '<tr><td>Presidential</td><td>Outstanding record</td><td>$5,000 or more</td><td>3.5 GPA</td></tr>'
            '<tr><td>Legacy</td><td>Parent is an alumnus</td><td>$500</td><td>Auto</td></tr></table>'), '2026-27')}
        self.assertEqual((got['Presidential']['award_min'], got['Presidential'].get('award_max')), (5000, None))
        self.assertEqual(got['Legacy']['award_max'], 500)
        transposed = merit.extract(INST, ENTRY, T.parse_html(
            '<title>Academic Scholarships</title><h2>New Freshman</h2><table><tr><th>2026-2027 Award Amounts</th><th>Full Tuition $2,544/semester</th><th>Half Tuition $1,272/semester</th></tr>'
            '<tr><td>Qualifications</td><td>See matrix</td><td>See matrix</td></tr><tr><td>Duration</td><td>4 years</td><td>4 years</td></tr></table>'), '2026-27')
        self.assertEqual(transposed, [])
        page = T.parse_html('<title>Dual Credit Handbook</title><h1>Dual Credit</h1><ul><li>Have a minimum GPA of 2.5 to enroll in dual credit.</li>'
                            '<li>To be eligible for Federal Financial Aid and to graduate, a student must have a 2.0 or higher cumulative GPA.</li>'
                            '<li>Students who fall below a 2.0 cumulative GPA will be placed on probation.</li></ul>')
        [c] = dual.extract(INST, ENTRY, page, '2026-27')
        self.assertEqual([t['min_hs_gpa'] for t in c['record']['dual_enrollment']['eligibility_tiers']], [2.5])

    def test_wi_r1_rules(self):
        """WI r1: Marquette's refund 'Example', UW-Platteville's loans page, Concordia's 'On Campus/Off Campus (Not with
        Family)' budget and Blackhawk's high-school grade clause."""
        table = ('<table><tr><th>Scholarship</th><th>Amount</th></tr><tr><td>Dean Award</td><td>$1,932</td></tr>'
                 '<tr><td>Honor Award</td><td>$791</td></tr><tr><td>Merit Award</td><td>$277</td></tr></table>')
        self.assertTrue(merit.extract(INST, ENTRY, T.parse_html('<title>Award Information</title><h3>Scholarships</h3>' + table), '2026-27'))
        self.assertEqual(merit.extract(INST, ENTRY, T.parse_html('<title>Award Information</title><h3>Example:</h3>' + table), '2026-27'), [])
        loans = ('<h2>Dependent Students</h2><table><tr><th>Year</th><th>Amount</th></tr><tr><td>Freshman</td><td>$5,500</td></tr>'
                 '<tr><td>Sophomore</td><td>$6,500</td></tr><tr><td>Junior/Senior</td><td>$7,500</td></tr></table>')
        self.assertTrue(merit.extract(INST, ENTRY, T.parse_html('<title>Financial Aid &amp; Scholarships</title>' + loans), '2026-27'))
        self.assertEqual(merit.extract(INST, ENTRY, T.parse_html('<title>Financial Aid &amp; Scholarships - Loans</title>' + loans), '2026-27'), [])
        rows = [['', 'On Campus/Off Campus (Not with Family)', 'Living At Home'], ['Tuition', '$37,080', '$37,080'],
                ['Books & Supplies', '$1,250', '$1,250'], ['Total', '$38,330', '$38,330']]
        p = T.Page('', 'Cost of Attendance', [{'heading': 'Cost of Attendance 2026-27', 'caption': '', 'lead': '', 'rows': rows}], [], [])
        [c] = costs.extract(INST, ENTRY, p, '2026-27')
        self.assertNotIn('with_parents_or_family', [a['arrangement'] for a in c['record']['living_arrangements']][:1])
        self.assertIsNone(costs.column_meaning('On Campus/Off Campus')['arrangement'])
        self.assertEqual(costs.column_meaning('Off Campus (Not with Family)')['arrangement'], 'off_campus_not_with_family')
        self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html(
            '<title>Transfer</title><p>Transfer credit is evaluated for high school courses for which advanced standing was granted and a grade '
            'of "B" or better was earned.</p>'), '2026-27'), [])

    def test_oh_r1_rules(self):
        """OH r1: OWU's academic-progress GPA rows, Walsh's OT tuition-and-fees page, CWRU/Dayton no-credit rows, a quoted
        national average beside a dual-credit price, a DeVry transfer-pledge MOU and Kenyon's applicant-grade sentence."""
        table = ('<h2>Scholarships</h2><table><tr><th>Scholarship</th><th>GPA</th><th>Amount</th></tr>'
                 '<tr><td>1st Semester Freshman</td><td>1.50</td><td></td></tr><tr><td>1st and 2nd Semester Juniors</td><td>2.00</td><td></td></tr>'
                 '<tr><td>All Seniors</td><td>2.00</td><td></td></tr><tr><td>Dean Award</td><td>3.5</td><td>$1,932</td></tr><tr><td>Honor Award</td><td>3.0</td><td>$791</td></tr></table>')
        names = [c['record']['award_name'] for c in merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title>' + table), '2026-27')]
        self.assertEqual(sorted(names), ['Dean Award', 'Honor Award'])
        self.assertEqual(merit.extract(INST, {**ENTRY, 'url': 'https://www.example.edu/ot-tuition-and-fees.html'}, T.parse_html('<title>Awards</title>' + table), '2026-27'), [])
        ap = [['AP Exam', 'Score', 'Credits', 'Course'], ['AP Research', '---', '---', 'CWRU does not award credit for AP Research.'],
              ['AP Seminar', 'N/A', '0', 'Non-Transferable Credit'], ['Art History', '4', '4', 'ART 101'], ['Biology', '4', '4', 'BIOL 1000'], ['Chemistry', '4', '4', 'CHEM 1000']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'AP', [{'rows': ap, 'heading': 'Advanced Placement Credit', 'caption': '', 'lead': ''}], [], []), '2026-27')
        codes = [e['exam_or_course_code'] for e in c['record']['equivalencies']]
        self.assertNotIn('AP-RESEARCH', codes)
        self.assertNotIn('AP-SEMINAR', codes)
        [c] = self._de('<h1>Dual Credit</h1><ul><li>Dual credit tuition is $147.50 per credit hour</li>'
                       '<li>The average college course costs $594 per credit hour.</li></ul>')
        self.assertEqual([x['amount'] for x in c['record']['dual_enrollment']['per_credit_hour_charges']], [147.5])
        page = '<title>Transfer</title><p>Only courses with a grade of C or better will be accepted for transfer to the university.</p>'
        for u in ['https://www.example.edu/media/devry-university-mou.pdf', 'https://www.example.edu/files/transfer-pledge.pdf']:
            self.assertEqual(transfer.extract(INST, {**ENTRY, 'url': u}, T.parse_html(page), '2026-27'), [], u)
        self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html('<title>Transfer Applicants</title><p>In most cases, successful transfer '
                                                                    'applicants present grades of B or better in their current courses.</p>'), '2026-27'), [])

    def test_il_r1_rules(self):
        """IL r1: UIC deadline rows and Quincy's 'In This Section', Knox IB credit and AcademicWorks pages, Augustana's
        'Not accepted' rows, continuation and exception GPA lines, Olivet's GI Bill example, accelerated BS/MS programs."""
        table = ('<h2>Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th></tr>'
                 '<tr><td>Transfer applicants: April 1</td><td>$7,500</td></tr><tr><td>Fall 2026 (Priority)</td><td>$5,000</td></tr>'
                 '<tr><td>In This Section</td><td>$4,000</td></tr><tr><td>Dean Award</td><td>$1,932</td></tr><tr><td>Honor Award</td><td>$791</td></tr></table>')
        names = [c['record']['award_name'] for c in merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title>' + table), '2026-27')]
        self.assertEqual(sorted(names), ['Dean Award', 'Honor Award'])
        for url in ['https://www.example.edu/international-baccalaureate', 'https://clc.academicworks.com/opportunities']:
            self.assertEqual(merit.extract(INST, {**ENTRY, 'url': url}, T.parse_html('<title>Awards</title>' + table), '2026-27'), [], url)
        self.assertTrue(merit.extract(INST, {**ENTRY, 'url': 'https://www.example.edu/international-baccalaureate-scholarship'}, T.parse_html('<title>Awards</title>' + table), '2026-27'))
        ap = [['AP Exam', 'Score', 'Credits', 'Course'], ['African American Studies', 'NA', '', 'Not accepted'], ['Art History', '4', '4', 'ART 101'],
              ['Biology', '4', '4', 'BIOL 1000'], ['Chemistry', '4', '4', 'CHEM 1000']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'AP', [{'rows': ap, 'heading': 'Advanced Placement Credit', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertNotIn('AP-AFRICAN-AMERICAN-STUDIES', [e['exam_or_course_code'] for e in c['record']['equivalencies']])
        [c] = self._de('<h1>Dual Credit</h1><ul><li>Must have 3 completed semesters of coursework and a 2.75 GPA</li>'
                       '<li>NOTE: Students with below a 2.25 GPA may request a review</li><li>Students are dropped at any time his/her cumulative GPA falls below a 2.0 GPA.</li></ul>')
        self.assertEqual([t['min_hs_gpa'] for t in c['record']['dual_enrollment']['eligibility_tiers']], [2.75])
        rows = [['', 'Amount'], ['University Tuition & Fees', '$41,120'], ['Less: Post-9/11 GI Bill', '$28,937'], ['Housing', '$8,000'], ['Amount Student Owes', '$0']]
        p = T.Page('', 'Military Aid', [{'heading': 'Example 2026-27', 'caption': '', 'lead': '', 'rows': rows}], [], [])
        self.assertEqual(costs.extract(INST, ENTRY, p, '2026-27'), [])
        url = {**ENTRY, 'url': 'https://catalog.example.edu/undergraduate/science/biology/biology-bs/'}
        raw = (FIX / 'courseleaf_program.html').read_bytes()
        self.assertTrue(catalog.extract(INST, url, T.parse_html(raw, 'https://x'), '2026-27'))
        acc = T.parse_html(raw.replace(b'Biology, Bachelor of Science', b'Biology, Bachelor of Science/MS Accelerated Program'), 'https://x')
        self.assertEqual(catalog.extract(INST, url, acc, '2026-27'), [])

    def test_mi_r1_rules(self):
        """MI r1: Madonna's eligibility text under a GPA/ACT/SAT header, GRCC's program budgets, Macomb's no-credit score
        bands, partner articulation agreements, and transfer/continuation GPA lines on dual-enrollment pages."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Scholarships</h2><table><tr><th>Scholarships</th><th>Amount/Year</th><th>Eligibility Requirements GPA / ACT / ~SAT</th></tr>'
            '<tr><td>Alumni Legacy</td><td>$2,000</td><td>Parent/Grandparent is an alumna/alumnus</td></tr>'
            '<tr><td>Honors Award</td><td>$5,000</td><td>3.5 / 24 / 1160</td></tr><tr><td>Dean Award</td><td>$3,000</td><td>3.0 / 21 / 1060</td></tr></table>'), '2026-27')}
        self.assertNotIn('test_requirement', got['Alumni Legacy'])
        self.assertEqual(got['Alumni Legacy']['eligibility_summary'], 'Parent/Grandparent is an alumna/alumnus')
        self.assertIn('test_requirement', got['Honors Award'])
        rows = [['', 'In-District', 'Out-of-District'], ['Tuition', '$17,920', '$27,120'], ['Fees', '$460', '$460'], ['Books and Supplies', '$626', '$626']]
        for heading, n in [('Nursing Programs (Fall and Winter) 2026-27', 0), ('Cost of Attendance (Fall and Winter) 2026-27', 1)]:
            p = T.Page('', 'Cost of Attendance', [{'heading': heading, 'caption': '', 'lead': '', 'rows': rows}], [], [])
            self.assertEqual(bool(costs.extract(INST, ENTRY, p, '2026-27')), bool(n), heading)
        ap = [['AP Exam', 'Score', 'Credits', 'Course'], ['Art History', '1, 2', 'None', 'None'], ['Art History', '3, 4, 5', '6', 'ARTT 1010'],
              ['Biology', '3', '4', 'BIOL 1000'], ['Chemistry', '3', '4', 'CHEM 1000']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'AP', [{'rows': ap, 'heading': 'Advanced Placement Credit', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertEqual([e['minimum_score'] for e in c['record']['equivalencies'] if e['exam_or_course_code'] == 'AP-ART-HISTORY'], ['3, 4, 5'])
        page = '<title>Transfer Guide</title><p>Only courses with a grade of C or better will be accepted for transfer to the university.</p>'
        self.assertEqual(transfer.extract(INST, {**ENTRY, 'url': 'https://www.example.edu/transfer-agreements/emu-guide.pdf'}, T.parse_html(page), '2026-27'), [])
        self.assertEqual(transfer.extract(INST, {**ENTRY, 'url': 'https://www.example.edu/files/Renewal_Articulation_2025.pdf'}, T.parse_html(page), '2026-27'), [])
        self.assertEqual(transfer.extract(INST, {**ENTRY, 'url': 'https://www.example.edu/files/TT-FVTC-Culinary-2026.pdf'}, T.parse_html(page), '2026-27'), [])
        self.assertTrue(transfer.extract(INST, {**ENTRY, 'url': 'https://www.example.edu/transfer/transfer-credit-agreements/'}, T.parse_html(page), '2026-27'))
        [c] = transfer.extract(INST, {**ENTRY, 'url': 'https://www.example.edu/admissions/transfer/'}, T.parse_html(page), '2026-27')
        self.assertEqual(c['record']['min_grade'], 'C')
        [c] = self._de('<h1>Dual Enrollment</h1><ul><li>Have a minimum GPA of 2.5 to enroll.</li><li>Students need a 2.0 GPA or higher for credits to transfer.</li>'
                       '<li>1 to 14 credits attempted: required GPA of 1.5 or higher</li></ul>')
        self.assertEqual([t['min_hs_gpa'] for t in c['record']['dual_enrollment']['eligibility_tiers']], [2.5])

    def test_mn_r1_rules(self):
        """MN r1: one-rate and Midwest-exchange residency labels, SMSU's one-semester total, Minnesota State's
        program-scoped C rules, Minnesota West's petition/course GPA lines, deadline rows and exam-credit pages."""
        self.assertEqual(costs.residency('mn resident & non resident', 'MN'), 'not_applicable')
        self.assertEqual(costs.residency('smsu does not charge out-of-state tuition', 'MN'), 'not_applicable')
        self.assertEqual(costs.residency('no out-state tuition rates', 'MN'), 'not_applicable')
        self.assertEqual(costs.residency('midwest nonresident', 'MN'), 'named_other_state')
        self.assertEqual(costs.residency('residents of other states', 'MN'), 'out_of_state')
        self.assertEqual(costs.residency('nonresident', 'MN'), 'out_of_state')
        rows = [['Tuition and Fees (at 12-18 credits)', '$5,758'], ['Housing and Food Estimate', '$5,925'],
                ['Total Estimated Charges for One Semester', '$11,683']]
        lead = 'The following figures represent estimated costs for two semesters during the 2026-2027 academic year.'
        p = T.Page('', 'Budget', [{'heading': 'Cost of Attendance', 'caption': '', 'lead': lead, 'rows': rows}], [], [])
        self.assertTrue(all('cost_period_semester' in c['issues'] for c in costs.extract(INST, ENTRY, p, '2026-27')))
        rows[-1] = ['Total Estimated Charges', '$11,683']
        p = T.Page('', 'Budget', [{'heading': 'Cost of Attendance', 'caption': '', 'lead': lead, 'rows': rows}], [], [])
        got = costs.extract(INST, ENTRY, p, '2026-27')
        self.assertTrue(got and all('cost_period_semester' not in c['issues'] for c in got))
        for s in ['While D grades transfer, some specialized/ occupational/technical programs require courses to have a grade of C or higher to fulfill requirements.',
                  'Health programs require a grade of C or better in all courses, therefore grades of C- or below do not count.',
                  'Students planning to transfer and who have made the proper selection of course work, and maintained grades of "C" or better, may expect to transfer without loss of credit.']:
            self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html('<title>Transfer</title><p>%s</p>' % s), '2026-27'), [], s)
        [c] = transfer.extract(INST, ENTRY, T.parse_html('<title>Transfer</title><p>Only courses in which students earn a grade of C- or better may be transferred.</p>'), '2026-27')
        self.assertEqual(c['record']['min_grade'], 'C-')
        [c] = self._de('<h1>PSEO</h1><ul><li>HS GPA of 2.0 or higher</li><li>If the 2.0 GPA isn\'t met, a petition form may be completed with an advisor</li>'
                       '<li>Course requirements for reading-based courses (2.6 GPA)</li></ul>')
        self.assertEqual([t['min_hs_gpa'] for t in c['record']['dual_enrollment']['eligibility_tiers']], [2.0])
        table = ('<h2>Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th></tr><tr><td>October 1</td><td>$1,000</td></tr>'
                 '<tr><td>Dean Award</td><td>$1,932</td></tr><tr><td>Honor Award</td><td>$791</td></tr></table>')
        names = [c['record']['award_name'] for c in merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title>' + table), '2026-27')]
        self.assertIn('Dean Award', names)
        self.assertNotIn('October 1', names)
        for title in ['AP and IB Course Awards', 'CLEP Credit', 'College-Level Examination Program']:
            self.assertEqual(merit.extract(INST, ENTRY, T.parse_html('<title>%s</title>' % title + table), '2026-27'), [], title)

    def test_tx_r1_rules(self):
        """TX r1: annual/four-year pairs, fall/spring splits, Yes/No and e-mail cells, AP credit tables; 'not living at
        home', 'At-Home' and a per-semester lead; residency 'N semester credit hours of the last M' and scoped caps."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Freshman Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th><th>GPA</th></tr>'
            '<tr><td>Presidential</td><td>$4,000/$16,000</td><td>3.95</td></tr><tr><td>College Success Scholarship</td><td>$500 Fall &amp; $500 Spring</td><td>Yes</td></tr>'
            '<tr><td>Cambria Changing Lives</td><td>$250</td><td>No</td></tr><tr><td>Graduate College scholarships</td><td>$1,000</td><td>gc@txstate.edu</td></tr></table>'), '2026-27')}
        self.assertEqual((got['Presidential']['award_min'], got['Presidential']['award_max']), (4000, 4000))
        self.assertNotIn('award_max', got['College Success Scholarship'])
        self.assertNotIn('gpa_requirement', got['Cambria Changing Lives'])
        self.assertNotIn('gpa_requirement', got['Graduate College scholarships'])
        self.assertEqual(merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Awards</h2><table><tr><th>Scholarship</th><th>Criteria</th></tr>'
            '<tr><td>AP Credit Award Physics 1</td><td>Score of 3</td></tr><tr><td>AP Credit Award Physics 2</td><td>Score of 3</td></tr></table>'), '2026-27'), [])
        stacked = [['Category', 'Out-of-State student not living at home', 'Out-of-State student living at home with parents'],
                   ['Full Time', 'Full Time'], ['Tuition and fees', '$6,540', '$6,540'], ['Housing and food', '$18,240', '$8,800'], ['Total', '$24,780', '$15,340']]
        p = T.Page('', 'Cost of Attendance', [{'heading': '2026-2027 Cost of Attendance', 'caption': '', 'lead': '', 'rows': stacked}], [], [])
        [c] = costs.extract(INST, ENTRY, p, '2026-27')
        self.assertEqual(sorted(a['arrangement'] for a in c['record']['living_arrangements']), ['off_campus_not_with_family', 'with_parents_or_family'])
        athome = [['Fall/Spring', 'On-Campus', 'Off-Campus', 'At-Home'], ['Tuition & Fees', '$8,032', '$8,032', '$8,032'],
                  ['Housing', '$8,446', '$10,380', '$3,700'], ['Total', '$16,478', '$18,412', '$11,732']]
        p = T.Page('', 'Cost of Attendance', [{'heading': 'Cost of Attendance for 2026-2027', 'caption': '', 'lead': '', 'rows': athome}], [], [])
        [c] = costs.extract(INST, ENTRY, p, '2026-27')
        self.assertIn('with_parents_or_family', [a['arrangement'] for a in c['record']['living_arrangements']])
        lead = [['Credit Hours', '12-18'], ['Tuition', '$15,370'], ['Technology Fee', '$270'], ['Total', '$15,640']]
        p = T.Page('', 'Tuition and Fees', [{'heading': 'Tuition and Fees', 'caption': '', 'lead': 'Fall and Spring Semesters Block Rate 2026-27 (per semester)', 'rows': lead}], [], [])
        self.assertTrue(all('cost_period_semester' in c['issues'] for c in costs.extract(INST, ENTRY, p, '2026-27')))
        load = [['Expense', 'Resident Living Off Campus'], ['Tuition and Fees', '$4,935'], ['Books and Supplies', '$528'], ['Total', '$5,463']]
        p = T.Page('', 'Tuition', [{'heading': 'Estimated Costs for 2026-27', 'caption': '', 'lead': 'These budgets reflect full-time enrollment, 15 credits per term.', 'rows': load}], [], [])
        self.assertTrue(all('cost_period_semester' not in c['issues'] for c in costs.extract(INST, ENTRY, p, '2026-27')))
        [c] = transfer.extract(INST, ENTRY, T.parse_html('<title>Transfer</title><p>Additionally, at least 24 semester credit hours of the last 30 hours '
                                                          'completed that are required for the degree must be taken at the university.</p>'), '2026-27')
        self.assertEqual(c['record']['residency_requirement_credits'], 24)
        [c] = transfer.extract(INST, ENTRY, T.parse_html('<title>Transfer</title><p>Graduation includes earning 32 of the last 40 hours at the '
                                                          'college with a minimum 2.0 GPA.</p>'), '2026-27')
        self.assertEqual(c['record']['residency_requirement_credits'], 32)  # NC (Lees-McRae): the GPA is a separate condition
        for s in ['Students need a GPA of at least 3.0 for the last 60 hours of baccalaureate studies at the university.',
                  'A minimum of 30 semester credit hours must be earned at the university before the final semester to qualify for this recognition.',
                  'A maximum of 12 hours of transferable Honors credits may transfer to the university.',
                  'Texas public senior colleges are required to accept up to 66 hours of transfer credit from a community college.',
                  'A maximum of 72 semester hours may be transferred from institutions that do not have engineering programs accredited by ABET.',
                  'Students seeking to transfer from an unaccredited college may transfer courses with a grade of C or better.']:
            self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html('<title>Transfer</title><p>' + s + '</p>'), '2026-27'), [], s)

    def test_wa_r1_rules(self):
        """WA r1: Seattle Colleges' two-row header ("WA Resident" over "Living without Parent | Living with Parent"); a
        two-row header that cannot be aligned is blocked; Columbia Basin's "One Quarter" table is one term; the direct
        transfer agreement's "each course completed from this list" is not the general transfer minimum."""
        INST_WA = {**INST, 'state': 'WA'}
        rows = [['Estimated Cost', 'WA Resident', 'Non-Resident'],
                ['Living without Parent', 'Living with Parent', 'Living without Parent', 'Living with Parent'],
                ['Tuition and Fees', '$4,935', '$4,935', '$5,520', '$5,520'], ['Food and Housing', '$19,473', '$10,072', '$19,473', '$10,072'],
                ['Total', '$24,408', '$15,007', '$24,993', '$15,592']]
        p = T.Page('', 'Cost of Attendance', [{'heading': 'Annual Cost of Attendance 2026-27', 'caption': '', 'lead': '', 'rows': rows}], [], [])
        got = {c['record']['residency']: c for c in costs.extract(INST_WA, ENTRY, p, '2026-27')}
        self.assertEqual(set(got), {'in_state', 'out_of_state'})
        self.assertEqual(sorted(a['arrangement'] for a in got['in_state']['record']['living_arrangements']),
                         ['off_campus_not_with_family', 'with_parents_or_family'])
        self.assertEqual(got['out_of_state']['record']['tuition_and_mandatory_fees'] if 'tuition_and_mandatory_fees' in got['out_of_state']['record']
                         else got['out_of_state']['record']['tuition'], 5520)
        uneven = [['Residency', 'Arizona Resident', 'Non-Resident'], ['Housing', 'With Parent', 'On-Campus', 'Off-Campus', 'On-Campus', 'Off-Campus'],
                  ['Tuition & Fees', '$13,900', '$13,900', '$13,900', '$44,400', '$44,400'], ['Housing & Food', '$3,140', '$17,770', '$13,100', '$17,770', '$13,100'],
                  ['Books', '$600', '$600', '$600', '$600', '$600']]
        p = T.Page('', 'Cost of Attendance', [{'heading': '2026-2027 Cost of Attendance', 'caption': '', 'lead': '', 'rows': uneven}], [], [])
        self.assertTrue(all('stacked_header_unparsed' in c['issues'] for c in costs.extract(INST, ENTRY, p, '2026-27')))
        quarter = [['One Quarter', 'Resident Dependent Living with Parent(s)', 'Resident Living Away from Parent(s)'],
                   ['Tuition & Fees', '$2,079', '$2,079'], ['Books & Supplies', '$176', '$176'], ['Total', '$2,255', '$2,255']]
        p = T.Page('', 'Cost of Attendance', [{'heading': '2026-27 Cost of Attendance', 'caption': '', 'lead': '', 'rows': quarter}], [], [])
        cands = costs.extract(INST, ENTRY, p, '2026-27')
        self.assertTrue(cands and all('cost_period_semester' in c['issues'] for c in cands))
        self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html(
            '<title>Transfer</title><p>For transfer purposes, a student must have a minimum grade of C or better in each course completed from this list.</p>'),
            '2026-27'), [])
        self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html(
            '<title>Transfer</title><p>The course must be completed with a grade of C or better, even though it does not transfer as college credit.</p>'),
            '2026-27'), [])

    def test_az_r1_rules(self):
        """AZ r1: Prescott's Ph.D. scholarship tiers are graduate awards; Northland Pioneer's 'Social Media' heading is not where
        awards are listed; ERAU's international budget is labelled only in the table's lead text."""
        tiers = ('<title>Scholarships</title><h2>Ph.D. Changemaker Scholarship</h2><table><tr><th>Enrollment</th><th>Amount</th></tr>'
                 '<tr><td>Full-time (12 or more credits)</td><td>$4,000 / term</td></tr><tr><td>Half time (6 – 8 credits)</td><td>$2,000 / term</td></tr>'
                 '<tr><td>Three-quarter time (9 – 11 credits)</td><td>$3,000 / term</td></tr></table>')
        self.assertEqual(merit.extract(INST, ENTRY, T.parse_html(tiers), '2026-27'), [])
        self.assertTrue(merit.extract(INST, ENTRY, T.parse_html(tiers.replace('Ph.D. Changemaker', 'Changemaker')), '2026-27'))
        nav = ('<title>Scholarships</title><h2>Social Media</h2><table><tr><th>Scholarship</th><th>Amount</th><th>Deadline</th></tr>'
               '<tr><td>Visual Arts Scholarship</td><td>$4,000</td><td>September 18</td></tr><tr><td>President\'s Scholars</td><td>$2,200</td><td>March</td></tr></table>')
        got = merit.extract(INST, ENTRY, T.parse_html(nav), '2026-27')
        self.assertTrue(got and all('eligibility_summary' not in c['record'] for c in got))
        p = T.Page('', 'Tuition and Costs', [{'heading': 'Academic Year 2026-27', 'caption': '', 'lead': 'International Student Cost of Attendance - Undergraduate',
                                              'rows': [['Budget Component', 'Standard On-Campus Costs'], ['Tuition and Fees', '$47,844'],
                                                       ['Housing and Food', '$15,816'], ['Total', '$63,660']]}], [], [])
        self.assertEqual(costs.extract(INST, ENTRY, p, '2026-27'), [])

    def test_nm_r1_rules(self):
        """NM r1: Luna's staff contact table and NMSU's private-scholarship page are not awards; ENMU-Roswell's English-course
        grade is not the general transfer minimum; WNMU's overload petition is not dual-enrollment eligibility."""
        staff = ('<title>Scholarships</title><h2>Contacts</h2><table><tr><th>Name</th><th>Title</th><th>Phone</th><th>ACT</th></tr>'
                 '<tr><td>Rachael Lucero</td><td>Registrar</td><td>505-587-3829</td><td>Click Here</td></tr>'
                 '<tr><td>Ida Valdez</td><td>Associate Registrar</td><td>505-587-3823</td><td>Click Here</td></tr>'
                 '<tr><td>Alicia Chacon</td><td>Associate Registrar</td><td>505-454-2546</td><td>Click Here</td></tr></table>')
        self.assertEqual(merit.extract(INST, ENTRY, T.parse_html(staff), '2026-27'), [])
        awards = ('<h2>Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th><th>Deadline</th></tr>'
                  '<tr><td>Chemistry Scholarship</td><td>$1,000</td><td>October 31</td></tr>'
                  '<tr><td>Youth Mentor Scholarship</td><td>$1,000</td><td>November 2</td></tr></table>')
        self.assertTrue(merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title>' + awards), '2026-27'))
        self.assertEqual(merit.extract(INST, ENTRY, T.parse_html('<title>Private Scholarships</title>' + awards), '2026-27'), [])
        self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html(
            '<title>Transfer</title><p>A college-level English course with a grade of C or better is required for transfer.</p>'), '2026-27'), [])
        # FL (New College): "non-developmental" coursework is the general rule, not a developmental-course rule.
        [c] = transfer.extract(INST, ENTRY, T.parse_html(
            '<title>Transfer</title><p>The college accepts transferable coursework with a grade of C or better, which is non-developmental.</p>'), '2026-27')
        self.assertEqual(c['record']['min_grade'], 'C')
        [c] = self._de('<p>Have a cumulative high school GPA of 2.5 to enroll in dual credit.</p>'
                       '<p>Dual Credit students wanting to take more than 18 hours must file a petition to overload with a 3.0 GPA.</p>')
        self.assertEqual([t['min_hs_gpa'] for t in c['record']['dual_enrollment']['eligibility_tiers']], [2.5])
        # "overload" on its own (no "petition", which MN r1 also excludes) is still not eligibility.
        [c] = self._de('<p>Have a cumulative high school GPA of 2.5 to enroll in dual credit.</p>'
                       '<p>Dual Credit students may take a course overload with a 3.0 GPA.</p>')
        self.assertEqual([t['min_hs_gpa'] for t in c['record']['dual_enrollment']['eligibility_tiers']], [2.5])

    def test_co_r1_rules(self):
        """CO r1: Otero's fall/spring split is not a minimum; CCD's ENG 1021 grade and Regis's program-dependent cap are
        not general transfer rules; Western's charge for skipping a step is not the dual-enrollment price."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Institutional Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th><th>Requirements</th></tr>'
            '<tr><td>SEBREA Scholarship</td><td>$1000 ($500 for Fall semester and $500 for Spring semester)</td><td>Rural business</td></tr>'
            '<tr><td>Pinnacol Scholarship</td><td>$2,500</td><td>CTE pathway</td></tr></table>'), '2026-27')}
        self.assertEqual((got['SEBREA Scholarship']['award_min'], got['SEBREA Scholarship']['award_max']), (1000, 1000))
        self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html(
            '<title>Transfer</title><p>ENG 1021 must be completed with a grade of B or better for transfer.</p>'), '2026-27'), [])
        [c] = transfer.extract(INST, ENTRY, T.parse_html(
            '<title>Transfer Guides</title><p>Depending on the program, up to 87 credit hours may be eligible for transfer!</p>'
            '<p>A transfer is accepted only for courses in which a grade of C- or better is earned.</p>'), '2026-27')
        self.assertEqual((c['record'].get('min_grade'), c['record'].get('max_transfer_credits')), ('C-', None))
        self.assertEqual(self._de('<p>Important: If you don’t do this step, you’ll be charged $116 per credit.</p>'), [])

    def test_ut_r1_rules(self):
        """UT r1: SUU "$12,000 ($6,000/semester*)" is one annual amount; Utah Tech's "Per Semester (full-time)" row-label
        header makes a semester table; Weber's scholarship-retention GPA is not the program's; SUU "N/A" notes are blank."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Utah Resident</h2><table><tr><th>Scholarship</th><th>Award</th><th>GPA</th></tr>'
            '<tr><td>Centurium Scholarship</td><td>$12,000 ($6,000/semester*)</td><td>2.50-3.69</td></tr>'
            '<tr><td>Deans Scholarship</td><td>$2,000</td><td>3.60-3.79</td></tr></table>'), '2026-27')}
        self.assertEqual((got['Centurium Scholarship']['award_min'], got['Centurium Scholarship']['award_max']), (12000, 12000))
        html = ('<title>Tuition &amp; Costs</title><h2>2026-27 Academic Year</h2><table><tr><th>Per Semester (full-time)</th><th>Utah Resident</th><th>Non-Resident</th></tr>'
                '<tr><td>Tuition</td><td>$2,784.12</td><td>$8,900.04</td></tr><tr><td>Student Fees</td><td>$456.75</td><td>$456.75</td></tr>'
                '<tr><td>Total</td><td>$3,240.87</td><td>$9,356.79</td></tr></table>')
        cands = costs.extract(INST, ENTRY, T.parse_html(html), '2026-27')
        self.assertTrue(cands and all('cost_period_semester' in c['issues'] for c in cands))
        [c] = self._de('<p>Have a cumulative high school GPA of 3.00 or higher to enroll in dual enrollment.</p>'
                       '<p>Students must maintain a 2.5 college GPA to retain scholarship eligibility.</p>')
        self.assertNotIn('college_gpa_to_continue', c['record']['dual_enrollment'])
        p = T.Page('', 'Advanced Placement Credit', [{'heading': 'AP Credit', 'caption': '', 'lead': '', 'rows': [
            ['AP Exam', 'Score', 'Course', 'Credits', 'Gen Ed'], ['Biology', '3-5', 'BIOL 1010', '3', 'N/A'],
            ['Art History', '3-5', 'ARTH 2710', '3', 'Humanities'], ['Chemistry', '3-5', 'CHEM 1110', '4', 'n/a']]}], [], [])
        [c] = credit.extract(INST, ENTRY, p, '2026-27')
        notes = {e['exam_or_course_name']: e['notes'] for e in c['record']['equivalencies']}
        self.assertEqual((notes['AP Biology'], notes['AP Art History'], notes['AP Chemistry']), (None, 'Humanities', None))

    def test_wy_r1_rules(self):
        """WY r1: Northwest's credit-load rows are named after the award and "/semester" amounts give no annual range."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Welcome to Wyoming Scholarship</title><h2>Welcome to Wyoming Scholarship</h2><table><tr><th>Enrollment</th><th>Amount</th></tr>'
            '<tr><td>15.0 credits or more</td><td>$2,300/semester</td></tr><tr><td>Full Time (12.0-14.5 credits)</td><td>$2,000/semester</td></tr>'
            '<tr><td>Half Time (6.0-8.5 credits)</td><td>$1,000/semester</td></tr></table>'), '2026-27')}
        self.assertEqual(sorted(got), ['Welcome to Wyoming Scholarship: 15.0 credits or more', 'Welcome to Wyoming Scholarship: Full Time (12.0-14.5 credits)',
                                       'Welcome to Wyoming Scholarship: Half Time (6.0-8.5 credits)'])
        self.assertTrue(all('award_max' not in r and 'gpa_requirement' not in r for r in got.values()))

    def test_mt_r1_rules(self):
        """MT r1: Carroll's undocumented-student page and Yellow Ribbon row; UM "renewable for four years" is annual;
        MSU-Northern's college-preparatory curriculum table is not credit by exam."""
        table = ('<h2>Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th><th>Criteria</th></tr>'
                 '<tr><td>Bishop Carroll Scholarship</td><td>$9,000</td><td>Admitted</td></tr>'
                 '<tr><td>Yellow Ribbon Program for Veterans</td><td>$26,800</td><td>Post 9/11 GI Bill</td></tr>'
                 '<tr><td>Admissions Scholarship</td><td>$4,000 renewable for four years ($16,000 four-year value)</td><td>4.0 GPA</td></tr>'
                 '<tr><td>Trustee Scholarship</td><td>$5,000</td><td>3.5 GPA</td></tr></table>')
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title>' + table), '2026-27')}
        self.assertNotIn('Yellow Ribbon Program for Veterans', got)
        self.assertEqual(got['Admissions Scholarship']['award_max'], 4000)
        self.assertEqual(merit.extract(INST, {**ENTRY, 'url': 'https://x.edu/admission-aid/scholarships-grants/undocumented-student-information'},
                                       T.parse_html('<title>Scholarships</title>' + table), '2026-27'), [])
        rows = [['Course', 'Advanced Placement', 'Exam', 'Score'], ['Mathematics', 'AP courses prepare students', 'Calculus AB', '3+'],
                ['English', 'AP courses prepare students', 'English Language', '3+'], ['Science', 'AP courses prepare students', 'Biology', '3+']]
        p = T.Page('', 'Freshman Admission', [{'rows': rows, 'heading': 'College Preparatory Curriculum', 'caption': '', 'lead': ''}], [], [])
        self.assertEqual(credit.extract(INST, ENTRY, p, '2026-27'), [])

    def test_nd_r1_rules(self):
        """ND r1: Lake Region en-dash cells and semester-basis amounts; Minot tiers with four-year totals; VCSU "for two
        year"; Jamestown amounts under a blank header."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Scholarships</h2><table><tr><th>Scholarship</th><th>ACT</th><th>GPA</th><th>Amount</th></tr>'
            '<tr><td>Presidential Scholarship</td><td>28 &amp; higher</td><td>–</td><td>$4,500</td></tr>'
            '<tr><td>Part-time Scholarship</td><td></td><td>2.5</td><td>$100–$300 awarded on a semester basis</td></tr>'
            '<tr><td>Clock Tower</td><td></td><td>3.05-3.64</td><td>$1,500 per year for two year ($3,000)</td></tr>'
            '<tr><td>Leader Scholarship</td><td>25–27</td><td>3.8–4.0</td><td>$1,500</td></tr></table>'), '2026-27')}
        self.assertNotIn('gpa_requirement', got['Presidential Scholarship'])
        self.assertNotIn('award_max', got['Part-time Scholarship'])
        self.assertNotIn('award_max', got['Clock Tower'])
        self.assertEqual(got['Leader Scholarship']['award_max'], 1500)
        [c] = merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Academic Excellence Scholarship</h2><table><tr><th>High School GPA</th><th>Scholarship Award</th></tr>'
            '<tr><td>3.9+</td><td>$10,000 $2,500/year for a maximum of 4 years</td></tr><tr><td>3.7-3.89</td><td>$7,500 $1,875/year for a maximum of 4 years</td></tr>'
            '<tr><td>3.5-3.69</td><td>$5,000 $1,250/year for a maximum of 4 years</td></tr></table>'), '2026-27')
        self.assertNotIn('award_max', c['record'])
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Institutional Aid</h2><table><tr><th>Scholarship</th><th>GPA</th><th></th></tr>'
            '<tr><td>Knight Scholarship</td><td>Below 2.5</td><td>$6000</td></tr><tr><td>Trustee Scholarship</td><td>2.5-3.0</td><td>$7000</td></tr></table>'), '2026-27')}
        self.assertEqual(got['Knight Scholarship']['award_max'], 6000)

    def test_ne_r1_rules(self):
        """NE r1: community colleges' transfer-out advice (Northeast, Central, Mid-Plains) and an entrance requirement
        (Southeast); UNO's separate SL/HL column; Concordia's teacher scholarship and late fee are not course prices."""
        base = '<title>Transfer Credit</title><p>Courses completed with a grade of D or better transfer to the university.</p>'
        for scoped in ('The generally accepted requirements for transfer to another college include: Grades of "C" or higher in a transferable course.',
                       'The degree requires 60 credit hours, and most schools require a course grade of C or higher to transfer.',
                       'Applicants meet college entrance requirements through three or more hours of transfer credit with a grade of C or better.'):
            [c] = transfer.extract(INST, ENTRY, T.parse_html(base + f'<p>{scoped}</p>'), '2026-27')
            self.assertEqual(c['record'].get('min_grade'), 'D', scoped)
        [c] = transfer.extract(INST, ENTRY, T.parse_html(base + '<p>Most four-year colleges will accept up to 60 semester credit hours earned at a community college as transfer credit.</p>'), '2026-27')
        self.assertNotIn('max_transfer_credits', c['record'])
        ib = [['IB Exam', 'Level', 'Score', 'Course'], ['Biology', 'SL', '5-7', 'BIOL 1020'], ['Biology', 'HL', '5-7', 'BIOL 1020 & BIOL 1030'],
              ['Chemistry', 'HL', '5-7', 'CHEM 1180']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'IB', [{'rows': ib, 'heading': 'International Baccalaureate', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertEqual(sorted(e['minimum_score'] for e in c['record']['equivalencies']), ['HL 5-7', 'HL 5-7', 'SL 5-7'])
        page = T.parse_html('<title>Dual Credit</title><h1>Dual Credit</h1><ul><li>Juniors and seniors with a 3.0 GPA are eligible for dual credit.</li>'
                            '<li>Dual credit tuition is $150 per credit hour.</li>'
                            '<li>Concordia provides scholarships up to $300/credit for teachers to earn the graduate hours to offer dual credit.</li>'
                            '<li>Registration after the deadline will be assessed a $10/credit late fee.</li></ul>')
        [c] = dual.extract(INST, ENTRY, page, '2026-27')
        self.assertEqual([x['amount'] for x in c['record']['dual_enrollment']['per_credit_hour_charges']], [150])

    def test_ia_r1_rules(self):
        """IA r1: Hawkeye eligibility headings; Graceland sample aid package; Wartburg academic-progress table; conditional
        transfer grades (William Penn, Dubuque, Emmaus) and a cap for the major (Iowa)."""
        got = merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h3>Students Involved in Student Life</h3><table><tr><th>Scholarship</th><th>Amount</th><th>Application Deadline</th></tr>'
            '<tr><td>Billy Owens</td><td>$250</td><td>October 1</td></tr><tr><td>Goodwin Honor</td><td>$500</td><td>February 1</td></tr></table>'), '2026-27')
        self.assertTrue(got and all(c['record']['eligibility_summary'] == 'Listed under: Students Involved in Student Life' for c in got))
        package = merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Sample Award</h2><table><tr><th>Scholarship</th><th>Amount</th></tr>'
            '<tr><td>Graceland Scholarships</td><td>$11,000</td></tr><tr><td>Outside Scholarship(s)</td><td>$2,400</td></tr>'
            '<tr><td>Federal/State Grants</td><td>$8,395</td></tr><tr><td>Merit Award</td><td>$1,000</td></tr></table>'), '2026-27')
        self.assertEqual(package, [])
        sap = merit.extract(INST, ENTRY, T.parse_html(
            '<title>Financial Aid | Learn About Your Award</title><h2>Financial Aid Policies</h2><table><tr><th>Course Credits Completed</th><th>Required GPA</th><th>Pace (earned/attempted)</th></tr>'
            '<tr><td>Course Credits Completed: 0.25-6.75</td><td>Required GPA: 1.60</td><td>Pace (earned/attempted): 67%</td></tr>'
            '<tr><td>Course Credits Completed: 7.00-15.75</td><td>Required GPA: 1.80</td><td>Pace (earned/attempted): 67%</td></tr>'
            '<tr><td>Course Credits Completed: 26.00+</td><td>Required GPA: 2.00</td><td>Pace (earned/attempted): 67%</td></tr></table>'), '2026-27')
        self.assertEqual(sap, [])
        base = '<title>Transfer Credit</title><p>Courses completed with a grade of D or better transfer to the university.</p>'
        for scoped in ('For those students with an overall transfer grade point average of less than 2.0, only courses with a grade of "C-" or above will transfer.',
                       'A grade of C or better when the minimum acceptable grade is stated to be a C is required for transfer.',
                       'Students must earn a grade of C or better for the transfer of courses completed within the last fifteen years.'):
            [c] = transfer.extract(INST, ENTRY, T.parse_html(base + f'<p>{scoped}</p>'), '2026-27')
            self.assertEqual(c['record'].get('min_grade'), 'D', scoped)
        [c] = transfer.extract(INST, ENTRY, T.parse_html(base + '<p>A maximum of 15 semester hours of approved transfer credit may be counted toward the major.</p>'), '2026-27')
        self.assertNotIn('max_transfer_credits', c['record'])

    def test_ks_r1_rules(self):
        """KS r1: Hesston sample aid package; Barclay cost rows; Dodge City per-semester parentheticals; K-State Salina
        "Total Value"; Pitt State per-semester columns that mention the academic year, out-of-state table headings and an
        international budget."""
        table = ('<h2>Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th><th>Criteria</th></tr>'
                 '<tr><td>Presidential Gold</td><td>$2,000 per year ($1,000 per semester)</td><td>3.5 GPA</td></tr>'
                 '<tr><td>Vanier Scholarship</td><td>Total Value: $40,000 Freshman Year Award: $10,000</td><td>Incoming freshman</td></tr>'
                 '<tr><td>Annual Total</td><td>$9,120</td><td></td></tr>'
                 '<tr><td>Purple Merit</td><td>$1,000</td><td>2.5 GPA</td></tr></table>')
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title>' + table), '2026-27')}
        self.assertEqual((got['Presidential Gold']['award_min'], got['Presidential Gold']['award_max']), (2000, 2000))
        self.assertNotIn('award_max', got['Vanier Scholarship'])
        self.assertNotIn('Annual Total', got)
        self.assertEqual(merit.extract(INST, {**ENTRY, 'url': 'https://x.edu/admissions/scholarships-and-aid/sample-aid-packages/'},
                                       T.parse_html('<title>Scholarships</title>' + table), '2026-27'), [])
        tbl = lambda heading, amt: {'heading': heading, 'caption': '', 'lead': '', 'rows': [
            ['Tuition & costs per semester (academic year 2026-2027 )', ''], ['Tuition (flat rate, incl. campus fees)', amt], ['Books', '$500']]}
        p = T.Page('Tuition and Costs 2026-2027', 'Tuition and Costs 2026-2027',
                   [tbl('Undergraduate In-State Tuition & Costs', '$4,442'), tbl('Undergraduate Out-of-State Tuition & Costs', '$10,114'),
                    tbl('International Undergraduate Tuition & Costs', '$20,228')], [], [])
        got = {c['record']['residency']: c for c in costs.extract({**INST, 'state': 'KS'}, ENTRY, p, '2026-27')}
        self.assertEqual(sorted(got), ['in_state', 'out_of_state'])
        self.assertEqual(got['in_state']['record']['tuition'], 4442)
        self.assertTrue(all('cost_period_semester' in c['issues'] for c in got.values()))

    def test_mo_r1_rules(self):
        """MO r1: Logan per-trimester totals and per-credit amounts; Columbia College "$1,000-2,000"; ROTC; Southwest
        Baptist's two versions of one table; STLCC accreditation years; Truman A-Level, Westminster dual-credit-only
        rules; Cottey "SL/HL" rows."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th><th>Criteria</th></tr>'
            '<tr><td>President Scholarship</td><td>Up to $18,000 — $1,800 per trimester for 10 trimesters</td><td>3.75 GPA</td></tr>'
            '<tr><td>Tower Scholarship</td><td>$400 per credit hour</td><td>Transfer student</td></tr>'
            '<tr><td>Talent Award</td><td>$1,000-2,000</td><td>Audition</td></tr>'
            '<tr><td>Army ROTC Scholarship</td><td>Full tuition</td><td>Visit goarmy.com</td></tr>'
            '<tr><td>Sibling Award</td><td>$500</td><td>Sibling enrolled</td></tr></table>'), '2026-27')}
        self.assertNotIn('award_max', got['President Scholarship'])
        self.assertNotIn('award_max', got['Tower Scholarship'])
        self.assertEqual((got['Talent Award']['award_min'], got['Talent Award']['award_max']), (1000, 2000))
        self.assertNotIn('Army ROTC Scholarship', got)
        table = lambda amt: ('<h2>Freshman Academic Scholarships</h2><table><tr><th>Award</th><th>Annual Total</th></tr>'
                             f'<tr><td>Presidential Scholar</td><td>${amt},500</td></tr><tr><td>Dean Scholar</td><td>$9,000</td></tr></table>')
        cands = merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title>' + table(16) + table(18)), '2026-27')
        self.assertTrue(cands and all('duplicate_table_versions' in c['issues'] for c in cands))
        once = merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title>' + table(16)), '2026-27')
        self.assertTrue(once and all('duplicate_table_versions' not in c['issues'] for c in once))
        self.assertEqual(T.year_labels("STLCC's program is accredited through the 2028–2029 school year."), {})
        self.assertEqual(T.year_labels('Dual credit for the 2026-2027 school year.'), {'2026-27': 1})
        base = '<title>Transfer Credit</title><p>Courses completed with a grade of D or better transfer to the university.</p>'
        for scoped in ('Students must achieve a grade of C or higher to receive transfer credit for qualified A-Levels.',
                       'Dual credit courses will be considered for transfer as long as the student has received a grade of "C" or better.'):
            [c] = transfer.extract(INST, ENTRY, T.parse_html(base + f'<p>{scoped}</p>'), '2026-27')
            self.assertEqual(c['record'].get('min_grade'), 'D', scoped)
        ib = [['IB Exam', 'Score', 'Course', 'Hours'], ['Biology (SL/HL)', '4', 'BIO 101', '4'], ['Chemistry (HL)', '5', 'CHE 160', '4'],
              ['Geography, Standard Level', '4', 'ENV 125', '3']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'IB', [{'rows': ib, 'heading': 'International Baccalaureate', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertEqual(sorted(e['minimum_score'] for e in c['record']['equivalencies']), ['4', 'HL 5', 'SL 4'])

    def test_ok_r1_rules(self):
        """OK r1: multi-year package values (OU, USAO, SWOSU); repeated header rows (Oklahoma Christian); admission GPA
        standards and gen-ed rules in transfer text (Cameron, NSU, USAO); a CLEP row scored 3 (OKBU); bare department
        codes as courses (Cameron IB)."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Freshman Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th><th>Criteria</th></tr>'
            '<tr><td>GPA</td><td>ACT</td><td>SAT</td></tr>'
            '<tr><td>Award of Excellence</td><td>$16,000 ($4,000 x 4 years)</td><td>31 ACT and 3.5 GPA</td></tr>'
            '<tr><td>Welcome Scholarship</td><td>$44,760 total estimated value 8 fall/spring terms, $5,595 estimate/term</td><td>Non-resident</td></tr>'
            '<tr><td>Green Scholarship</td><td>$10,000 total estimated value 4 years x ($1,500 tuition + $1,000 housing)</td><td>3.5 GPA</td></tr>'
            '<tr><td>Nominee Scholarship</td><td>$3200 cash per year, full tuition, and residence hall scholarship</td><td>30 ACT</td></tr>'
            '<tr><td>Tier Scholarship</td><td>$6350 ($3175 tuition waiver per semester) for up to 8 semesters.</td><td>3.5 GPA</td></tr>'
            '<tr><td>Dougherty Scholarship</td><td>$4,000/year</td><td>28 ACT</td></tr></table>'), '2026-27')}
        self.assertNotIn('GPA', got)
        for name in ('Award of Excellence', 'Welcome Scholarship', 'Green Scholarship', 'Nominee Scholarship'):
            self.assertNotIn('award_max', got[name], name)
        self.assertEqual(got['Tier Scholarship']['award_max'], 6350)  # "for up to 8 semesters" is a duration, not a total
        self.assertEqual(got['Dougherty Scholarship']['award_max'], 4000)
        base = '<title>Transfer Credit</title><p>Courses completed with a grade of D or better transfer to the university.</p>'
        for scoped in ('Transfer students must be in good standing and have an average grade of C or better at the sending institution.',
                       'General education credit earned with a grade of C or better by the transferring student will apply toward the degree.'):
            [c] = transfer.extract(INST, ENTRY, T.parse_html(base + f'<p>{scoped}</p>'), '2026-27')
            self.assertEqual(c['record'].get('min_grade'), 'D', scoped)
        clep = [['CLEP Exam', 'Score', 'Course', 'Hours'], ['History of the United States I', '3', 'HIST 1013', '3'],
                ['American Government', '50', 'POLS 1113', '3'], ['College Algebra', '50', 'MATH 1513', '3'], ['Biology', '50', 'BIOL 1114', '4']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'CLEP', [{'rows': clep, 'heading': 'CLEP Credit', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertIn('score_scale_mismatch', c['issues'])
        ib = [['IB Exam', 'Score', 'Course', 'Hours'], ['Film (HL)', '4 or higher', 'ENGL', '3'], ['Spanish (HL)', '5 or higher', 'SPAN', '3'],
              ['Biology (HL)', '5 or higher', 'BIOL', '4']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'IB', [{'rows': ib, 'heading': 'International Baccalaureate', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertIn('course_number_missing', c['issues'])

    def test_ar_r1_rules(self):
        """AR r1: ATU and/or column; UA-PTC placement score rows; UCA merged-cell rows; UAPB four-year totals;
        UACCB/UACCM course-specific grade rules."""
        cands = merit.extract(INST, ENTRY, T.parse_html(
            '<title>Freshman Academic Scholarships</title><h2>Academic Scholarships</h2><table><tr><th>Level</th><th>ACT</th><th>SAT</th><th></th><th>GPA</th><th>Amount</th></tr>'
            '<tr><td>Level-2</td><td>19-20</td><td>990-1050</td><td>or</td><td>3.25-3.49</td><td>$2,000</td></tr>'
            '<tr><td>Level-4</td><td>24-27</td><td>1160-1290</td><td>&amp;</td><td>3.75+</td><td>$8,000</td></tr>'
            '<tr><td>Level-1</td><td>N/A</td><td>N/A</td><td></td><td>2.75-3.24</td><td>$1,000</td></tr></table>'), '2026-27')
        got = {c['record']['award_name']: c['issues'] for c in cands}
        self.assertIn('threshold_logic_column', got['Level-2'])
        self.assertIn('threshold_logic_column', got['Level-4'])
        self.assertNotIn('threshold_logic_column', got['Level-1'])
        sections = merit.extract(INST, ENTRY, T.parse_html(
            '<title>Concurrent Scholarship</title><h2>Scholarship Score Requirements</h2><table><tr><th>Subject</th><th>ACT</th><th>SAT</th></tr>'
            '<tr><td>Reading</td><td>19+</td><td>470+</td></tr><tr><td>English</td><td>19+</td><td>470+</td></tr><tr><td>Math</td><td>19+</td><td>460+</td></tr></table>'), '2026-27')
        self.assertEqual(sections, [])
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Freshman Scholarships</h2><table><tr><th></th><th>Scholarship</th><th>Requirements</th><th>Annual Total Award</th></tr>'
            '<tr><td>Institutional</td><td>Achievement</td><td>Minimum 4.00 GPA</td><td>$6,500</td></tr>'
            '<tr><td>Honors</td><td>Presidential</td><td>Minimum 3.90 GPA</td><td>$8,000</td></tr>'
            '<tr><td>University</td><td>Minimum 3.75 GPA</td><td>$4,500</td></tr></table>'), '2026-27')}
        self.assertEqual(sorted(got), ['Achievement', 'Presidential'])
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Academic Scholarships</h2><table><tr><th>Scholarship</th><th>Criteria</th><th>Amount</th></tr>'
            '<tr><td>Chancellor Scholarship</td><td>Minimum 3.75 GPA</td><td>$66,000 for four years ($8,250 per semester)</td></tr>'
            '<tr><td>Golden Lion Scholarship</td><td>Minimum 2.75 GPA</td><td>$4,000</td></tr></table>'), '2026-27')}
        self.assertNotIn('award_max', got['Chancellor Scholarship'])
        self.assertEqual(got['Golden Lion Scholarship']['award_max'], 4000)
        base = '<title>Transfer Credit</title><p>Courses completed with a grade of D or better transfer to the university.</p>'
        for scoped in ('This course is required and must be completed with a grade of C or higher through another institution and transferred.',
                       'Grades of D are not acceptable in some majors and cannot be used as prerequisites for courses that require a grade of C or higher in transfer.'):
            [c] = transfer.extract(INST, ENTRY, T.parse_html(base + f'<p>{scoped}</p>'), '2026-27')
            self.assertEqual(c['record'].get('min_grade'), 'D', scoped)
        [c] = transfer.extract(INST, ENTRY, T.parse_html('<title>Transfer</title><p>A minimum grade of C or better will be accepted for transfer credit '
                                                        "(D's are accepted in some majors and for some lower division courses).</p>"), '2026-27')
        self.assertEqual(c['record'].get('min_grade'), 'C')  # Clayton State: the general rule stands

    def test_la_r1_rules(self):
        """LA r1: UL Lafayette 'Offer' column and one-time awards; LSUS tuition-plus amounts; scoped transfer rules
        (Delgado, LSU, River Parishes, LSUA, NOBTS); Louisiana Tech merged tiers; AP scores under a CLEP heading;
        Xavier IB levels; Xavier summer fee schedule."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Freshman Scholarships</title><h2>Supplemental Scholarships</h2><table><tr><th>Scholarship</th><th>Eligibility Requirements</th><th>Offer</th></tr>'
            '<tr><td>Valedictorian Scholarship</td><td>High School Valedictorian</td><td>$2,000 for freshman yearContact the office</td></tr>'
            '<tr><td>Louisiana Scholarship</td><td>3.5 GPA</td><td>Tuition &amp; Fees + $1,200 Campus Housing Credit</td></tr>'
            '<tr><td>Purple Scholarship</td><td>2.5 GPA</td><td>$2,000</td></tr></table>'), '2026-27')}
        v = got['Valedictorian Scholarship']
        self.assertEqual((v['award_max'], v['renewable']), (2000, False))
        self.assertNotIn('award_max', got['Louisiana Scholarship'])
        self.assertEqual((got['Purple Scholarship']['award_max'], got['Purple Scholarship'].get('renewable')), (2000, None))
        base = '<title>Transfer Credit</title><p>Courses completed with a grade of C or better transfer to the university.</p>'
        for scoped in ('Transfer equivalencies in developmental courses are used for placement if a grade of "C" or better is earned.',
                       'Transfer applicants to the College of Science need a grade of C or better in all math and science courses.',
                       'To qualify for block transfer guarantees, you must earn a grade of "D" or better in each course.'):
            [c] = transfer.extract(INST, ENTRY, T.parse_html(base.replace('C or better', 'D or better') + f'<p>{scoped}</p>'), '2026-27')
            self.assertEqual(c['record'].get('min_grade'), 'D', scoped)
        # Ringling's heading "Transfer Credits and Placement" and UNCP's "not guaranteed the same benefits" keep the general rule.
        for general in ('Transfer Credits and Placement Ringling College will consider for transfer any credit where a grade of C or better was earned.',
                        'Students are not guaranteed the same benefits; however, they shall receive transfer credit for courses completed with a grade of "C" or better.'):
            [c] = transfer.extract(INST, ENTRY, T.parse_html(f'<title>Transfer Credit</title><p>{general}</p>'), '2026-27')
            self.assertEqual(c['record'].get('min_grade'), 'C', general)
        for capped in ('A maximum of 15 hours of lower-level transfer credit evaluated as upper-level credit may be used toward the degree.',
                       'Up to 18 semester hours from institutions not accredited by CHEA may be transferred.'):
            [c] = transfer.extract(INST, ENTRY, T.parse_html(base + f'<p>{capped}</p>'), '2026-27')
            self.assertNotIn('max_transfer_credits', c['record'], capped)
        rows = [['AP Exam', 'Score', 'Course', 'Hours'], ['Biology', '3 or 4 5', 'Bio Science 101 Bio Science 101, 102', '3 6'],
                ['Chemistry', '4, 5', 'CHEM 1070', '3'], ['Calculus AB', '4 or 5', 'MATH 240', '3']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'Advanced Placement', [{'rows': rows, 'heading': 'Advanced Placement', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertIn('merged_score_cells', c['issues'])
        ok = [rows[0], rows[2], rows[3], ['Psychology', '3', 'PSYC 101', '3']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'Advanced Placement', [{'rows': ok, 'heading': 'Advanced Placement', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertEqual(c['issues'], [])
        clep = [['CLEP Exam', 'Score', 'Course', 'Hours'], ['Biology', '3', 'BIOL 1100', '4'], ['Chemistry', '3', 'CHEM 1100', '4'], ['College Algebra', '3', 'MATH 1100', '3']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'CLEP', [{'rows': clep, 'heading': 'CLEP Credit', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertIn('score_scale_mismatch', c['issues'])
        ib = [['IB Exam', 'Score', 'Course', 'Hours'], ['Biology, Standard Level', '6', 'BIOL 1030', '6'], ['Biology, Higher Level', '6', 'BIOL 1230', '8'],
              ['Chemistry, Higher Level', '5', 'CHEM 1010', '4']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'IB', [{'rows': ib, 'heading': 'International Baccalaureate', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertEqual(sorted(e['minimum_score'] for e in c['record']['equivalencies']), ['HL 5', 'HL 6', 'SL 6'])
        fees = T.Page('', 'Tuition and Fees', [{'heading': 'Tuition', 'caption': '', 'lead': '', 'rows': [
            ['', 'In-State', 'Out-of-State'], ['Tuition', '$4,000', '$9,000'], ['Fees', '$500', '$500'], ['Total', '$4,500', '$9,500']]}], [], [])
        self.assertTrue(costs.extract({**INST, 'state': 'LA'}, ENTRY, fees, '2026-27'))
        self.assertEqual(costs.extract({**INST, 'state': 'LA'}, {**ENTRY, 'url': 'https://x.edu/forms-2026-2027/summer-2026-tuition-fees.pdf'}, fees, '2026-27'), [])

    def test_ms_r1_merit_and_costs(self):
        """MS r1: Tougaloo phone numbers and non-score criteria in the ACT column; USM GPA-band headers over ACT rows;
        Ole Miss 'No Test Score' grid column; Sumners amounts by enrollment level; Alcorn 'On/Off Campus' budgets."""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Academic Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th><th>GPA</th><th>ACT/SAT</th></tr>'
            '<tr><td>Presidential Academic Scholarship</td><td>$9,000</td><td>3.5+</td><td>ACT: 27+ / SAT: 1220+</td></tr>'
            '<tr><td>Eagle Academic Scholarship</td><td>$5,000</td><td>3.25+</td><td>Valedictorian or Salutatorian</td></tr>'
            '<tr><td>Servant Leader Scholarship</td><td>$4,000</td><td>3.0+</td><td>21</td></tr>'
            '<tr><td>Awarded at discretion of Athletic Department</td><td></td><td></td><td>601-977-7700</td></tr></table>'), '2026-27')}
        self.assertEqual(got['Presidential Academic Scholarship']['test_requirement'], 'ACT: 27+ / SAT: 1220+')
        self.assertEqual(got['Eagle Academic Scholarship']['test_requirement'], 'Valedictorian or Salutatorian')
        self.assertEqual(got['Servant Leader Scholarship']['test_requirement'], 'ACT 21')
        self.assertNotIn('Awarded at discretion of Athletic Department', got)
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Freshmen</title><h2>Academic Excellence Scholarships</h2><table><tr><th>3.0 - 3.24 GPA</th><th>Annual Merit Scholarship</th></tr>'
            '<tr><td>23 - 25 ACT Score</td><td>$1,500 annually</td></tr><tr><td>26 - 29 ACT Score</td><td>$2,500 annually</td></tr></table>'), '2026-27')}
        r = got['Academic Excellence Scholarships: 3.0 - 3.24 GPA 23 - 25 ACT Score']
        self.assertEqual((r['gpa_requirement'], r['test_requirement']), ('3.0 - 3.24 GPA', '23 - 25 ACT Score'))
        [c] = merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Academic Merit Scholarships</h2><table><tr><th>High School GPA</th><th>No Test Score</th><th>24-25 ACT</th><th>26-27 ACT</th></tr>'
            '<tr><td>3.0-3.49</td><td>$3,000</td><td>$4,000</td><td>$5,000</td></tr><tr><td>3.5-3.74</td><td>$5,000</td><td>$7,000</td><td>$8,000</td></tr></table>'), '2026-27')
        self.assertEqual((c['record']['award_min'], len(c['record']['award_tiers'])), (3000, 6))
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Sumners Scholarship</title><h2>Sumners Scholarship</h2><table><tr><th>Enrollment</th><th>Amount</th></tr>'
            '<tr><td>Full Time</td><td>$5,000 per semester</td></tr><tr><td>Half-Time</td><td>$2,500 per semester</td></tr></table>'), '2026-27')}
        self.assertEqual(sorted(got), ['Sumners Scholarship: Full Time', 'Sumners Scholarship: Half-Time'])
        self.assertNotIn('gpa_requirement', got['Sumners Scholarship: Full Time'])
        p = T.Page('Cost of Attendance', 'Cost of Attendance (COA) Budget', [{'heading': 'Cost of Attendance (COA) Budget', 'caption': '', 'lead': '', 'rows': [
            ['2026-2027 Undergraduate Cost of Attendance'], ['', 'Undergraduate in State On/Off Campus Fall/Spring', 'Undergraduate out of State On/Off Campus Fall/Spring'],
            ['Tuition', '$8,105.00', '$9,105.00'], ['Fees', '$730.00', '$730.00'], ['Housing', '$7,581.00', '$7,581.00'], ['Food', '$4,693.00', '$4,693.00'],
            ['Total Cost of Attendance', '$21,109.00', '$22,109.00']]}], [], [])
        got = {c['record']['residency']: c['record'] for c in costs.extract({**INST, 'state': 'MS'}, ENTRY, p, '2026-27')}
        self.assertEqual((got['in_state']['tuition'], got['in_state'].get('living_arrangement')), (8105, None))

    def test_merit_columns_al_r1(self):
        """AL r1: annual vs four-year columns (AUM), a single 'Test Score' column (UAB), a requirements column
        (Huntingdon) and an entering-class heading (UA '2027 In-State Freshman ...')."""
        aum = """<title>Scholarships</title><h2>Freshman Scholarships at a Glance</h2><table>
<tr><th>Name</th><th>Min. Superscore</th><th>Min. High School GPA</th><th>Total over 4 years</th><th>Total for academic year</th></tr>
<tr><td>Outstanding Scholars Award</td><td>ACT 30 / SAT 1400</td><td>3.0</td><td>$40,000</td><td>$10,000</td></tr>
<tr><td>Principal Scholarship</td><td>ACT 29 / SAT 1350</td><td>3.0</td><td>$36,000</td><td>$9,000</td></tr></table>"""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(aum), '2026-27')}
        r = got['Outstanding Scholars Award']
        self.assertEqual((r['award_max'], r['test_requirement'], r['gpa_requirement']), (10000, 'ACT 30 / SAT 1400', '3.0'))
        hunt = """<title>2026-2027 Undergraduate Scholarships</title><h2>Merit Scholarships</h2><table>
<tr><th>Scholarship</th><th>Award Amount</th><th>Minimum Requirements</th></tr>
<tr><td>Presidential Scholars</td><td>$20,000</td><td>3.0 GPA and 23 ACT or 3.75 GPA with no test scores.</td></tr>
<tr><td>James W. Wilson Jr. Scholarship</td><td>$16,500</td><td>3.75 GPA and 25 ACT</td></tr></table>"""
        got = {c['record']['award_name']: c for c in merit.extract(INST, ENTRY, T.parse_html(hunt), '2026-27')}
        self.assertEqual(got['Presidential Scholars']['record']['eligibility_summary'], '3.0 GPA and 23 ACT or 3.75 GPA with no test scores.')
        ua = """<title>In-State Freshman Scholarships</title><h2>2027 In-State Freshman Automatic Merit Scholarships</h2><table>
<tr><th>Scholarship</th><th>ACT</th><th>SAT</th><th>GPA</th><th>Yearly Value</th></tr>
<tr><td>UA Recognition</td><td>25</td><td>1200-1220</td><td>3.00-3.49</td><td>$4,000</td></tr>
<tr><td>Crimson Achievement</td><td>26</td><td>1230-1250</td><td>3.00-3.49</td><td>$5,000</td></tr></table>"""
        c = merit.extract(INST, ENTRY, T.parse_html(ua), '2026-27')[0]
        self.assertEqual(c['record']['residency_requirement'], 'In-state')
        self.assertEqual((c['academic_year'], c['year_basis']), ('2027-28', 'labeled_entering_class'))
        self.assertEqual(P.status_for(c, accepted_issues=False), 'partially_verified')  # never verified from a class label
        intl = {**ENTRY, 'url': 'https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/international'}
        self.assertEqual(merit.extract(INST, intl, T.parse_html(aum), '2026-27'), [])

    def test_al_r1_renewal_headerless_semesters_and_transfer_scope(self):
        miles = """<title>Scholarships</title><h2>Freshman Scholarships</h2><table>
<tr><th>Scholarship Name</th><th>Required GPA</th><th>Required ACT</th><th>Award Details</th><th>Renewal Requirements</th></tr>
<tr><td>Presidential Scholarship</td><td>3.7</td><td>24</td><td>Covers Tuition, Room/Board and Books</td><td>15 hours per semester, 3.3 cumulative GPA</td></tr>
<tr><td>Dean's Scholarship</td><td>3.2</td><td>20</td><td>Covers Tuition</td><td>3.0 cumulative GPA</td></tr></table>"""
        r = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(miles), '2026-27')}['Presidential Scholarship']
        self.assertEqual((r['award_amount_text'], r['renewal_requirements']), ('Covers Tuition, Room/Board and Books', '15 hours per semester, 3.3 cumulative GPA'))
        self.assertNotIn('eligibility_summary', r)  # the renewal column is not an entry requirement
        uwa = """<title>Scholarships</title><h2>Academic Scholarships</h2><table>
<tr><td>Tiger Achievement Award</td><td>21-22 ACT / 1060-1120 SAT or 3.00-3.24 GPA</td><td>$2,000.00 per year</td></tr>
<tr><td>Counselor's Award</td><td>23-24 ACT / 1130-1190 SAT or 3.25-3.74 GPA</td><td>$3,000.00 per year</td></tr>
<tr><td>Dean's Award</td><td>27-28 ACT / 1260-1320 SAT</td><td>$5,000.00 per year</td></tr></table>"""
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(uwa), '2026-27')}
        self.assertEqual(got['Tiger Achievement Award']['eligibility_summary'], '21-22 ACT / 1060-1120 SAT or 3.00-3.24 GPA')
        self.assertNotIn('gpa_requirement', got['Tiger Achievement Award'])
        self.assertEqual(got["Counselor's Award"]['award_max'], 3000)
        stillman = T.parse_html('<title>Policy on Awarding Course Credit</title><h2>Contacts</h2>' + uwa.split('</h2>', 1)[1])
        self.assertEqual(merit.extract(INST, {**ENTRY, 'url': 'https://catalog.x.edu/policy-on-awarding-course-credit'}, stillman, '2026-27'), [])
        self.assertEqual(costs.column_meaning('2 Semesters')['period'], 'year')
        self.assertEqual(costs.column_meaning('3 Semesters')['period'], 'partial_year')
        html = ('<title>Transfer Credit</title><p>UAB will award up to 24 hours of transferable military credit for veterans. A student with '
                'an associate degree may be eligible for admission to AUM with up to a maximum of 64 semester hours transferring. '
                'The student will retain this status until the student has attempted at least 12 credit hours at the College.</p>')
        self.assertEqual(transfer.extract(INST, ENTRY, T.parse_html(html), '2026-27'), [])
        sch = '<title>Transfer Scholarships</title><p>Minimum requirements: 3.0 GPA and at least 12 credit hours earned at the college in residence.</p>'
        self.assertEqual(transfer.extract(INST, {**ENTRY, 'url': 'https://www.x.edu/scholarships'}, T.parse_html(sch), '2026-27'), [])

    def test_two_column_program_map(self):
        """UTC 'Clear Path for Advising' layout: wrapped cells, hours on their own line, a left-column
        hours token running into the right column, and the hour summary block."""
        from pipeline.extractors import programmap
        text = (FIX / 'program_map_clear_path.txt').read_text()
        page_ = T.Page(text, text.splitlines()[0][:200], [], [], [])
        entry = {**ENTRY, 'kind': 'pdf', 'url': 'https://www.utc.edu/x/cecs-cs-data-science-ai-bs-2026-v1-accessible.pdf'}
        out = programmap.extract(INST, entry, page_, '2026-27')
        prog = next(c['record'] for c in out if c['domain'] == 'academic_programs')
        self.assertEqual((prog['program_name'], prog['catalog_year'], prog['total_credits']),
                         ('Computer Science: Data Science and Artificial Intelligence, B.S.', '2026-2027', 122))
        rows = {c['record']['requirement_key']: c['record'] for c in out if c['domain'] == 'degree_requirements'}
        terms = rows['four-year-plan']['rule_details']['terms']
        self.assertEqual([t['credit_hours'] for t in terms], ['14-15', '17-18', '16-18', '14', '15', '16', '15-16', '15'])
        codes = lambda t: [i['code'] if isinstance(i, dict) else i for i in t['items']]
        self.assertEqual(codes(terms[1])[:3], ['CPSC 1110', 'ENGL 1020', 'MATH 1960'])  # ENGL 1020 is a spring course
        self.assertEqual(terms[3]['items'][0], {'code': 'CPEN 3700', 'title': 'Digital Logic and Introduction to Computer Hardware', 'credits': 4})
        self.assertIn('MATH 2030: Discrete Math for Computer Science or MATH 3000: Introduction to Logic and Proof (3)', terms[3]['items'])
        self.assertEqual({k: r.get('minimum_credits') for k, r in rows.items() if k != 'four-year-plan'},
                         {'program-total': 122, 'upper-division-hours': 39, 'residency-hours': 30, 'four-year-institution-hours': 45,
                          'gen-ed-hours': 21, 'major-hours': 101})
        sys.path.insert(0, str(ROOT / 'scripts'))
        from validate_data import validate_record
        for c in out:
            self.assertEqual(validate_record(ROOT / 'data', c['record'], 0, domain=c['domain']), [], c['record'].get('requirement_key'))
        unlabeled = text.replace('2026-2027', '')
        self.assertEqual(programmap.extract(INST, entry, T.Page(unlabeled, '', [], [], []), '2026-27'), [])  # no printed year, no record

    def _de(self, body, url='https://www.example.edu/admissions/dual-enrollment/', title='Dual Enrollment'):
        return dual.extract(INST, {**ENTRY, 'url': url}, T.parse_html('<title>%s</title>%s' % (title, body)), '2026-27')

    def test_tn_r6_review_regressions(self):
        """Defects found reviewing Tennessee run 2026-10-03."""
        # UTC: "completed your sophomore year" means rising juniors and seniors, not sophomores.
        [c] = self._de('<p>Have you completed your sophomore year of high school?</p><p>Is your high school grade point average 3.0 or higher?</p>')
        self.assertEqual(c['record']['dual_enrollment']['eligibility_tiers'][0]['grades'], ['11', '12'])
        # APSU: a named dual enrollment scholarship's GPA rules are the award's.
        self.assertEqual(self._de('<p>Students must maintain a cumulative college GPA of 2.75 to be eligible.</p>',
                                  title='Bibb Family Dual Enrollment Scholarship'), [])
        # Trenholm State (AL): a plural "Dual Enrollment Scholarships" eligibility page is the program; ordinal lists name every grade.
        [c] = self._de('<p>The student must be in the 10th, 11th, or 12th grade and have a 2.5 GPA or higher.</p>',
                       title='Student Eligibility for Dual Enrollment Scholarships')
        self.assertEqual(c['record']['dual_enrollment']['eligibility_tiers'][0]['grades'], ['10', '11', '12'])
        # Motlow: side-by-side columns interleave words; the tiers go to review.
        [c] = dual.extract(INST, ENTRY, T.Page('to take Dual       you must have an overall GPA of 3.0 or higher and a 3.0',
                                               'Dual Enrollment', [], [], []), '2026-27')
        self.assertIn('multicolumn_layout_review', c['issues'])
        # Carson-Newman: a document's file name can carry its only year label.
        entry = {**ENTRY, 'url': 'https://www.example.edu/wp-content/uploads/2025/11/2025-26-Dual-Enrollment-Agreement-Form.pdf', 'kind': 'pdf'}
        [c] = dual.extract(INST, entry, T.Page('Students may take up to a maximum of 14 hours of Dual Enrollment courses in each semester.',
                                               'Dual Enrollment Agreement Form', [], [], []), '2026-27')
        self.assertEqual((c['academic_year'], c['year_basis']), ('2025-26', 'labeled_in_url'))
        self.assertIn('stale_year_label:2025-26', c['issues'])
        # Lipscomb: analytics parameters are not part of the source URL.
        from pipeline.crawl import requote
        self.assertEqual(requote('https://lipscomb.edu/a/transferring-credit?_gl=1*13kx7ol*_up*MQ..&utm_source=x'),
                         'https://lipscomb.edu/a/transferring-credit')
        self.assertEqual(requote('https://x.edu/p.php?catoid=3&navoid=9'), 'https://x.edu/p.php?catoid=3&navoid=9')
        self.assertEqual(T.canonical_url('https://x.edu/p?_gl=1&id=2'), 'https://x.edu/p?id=2')
        self.assertEqual(T.canonical_url('https://www.erskine.edu/admissions-aid/#story'), 'https://www.erskine.edu/admissions-aid/')

    def test_ga_r1_review_regressions(self):
        """Defects found reviewing Georgia run 2026-10-03."""
        tiers = lambda html: [(t['min_hs_gpa'], t['grades']) for c in self._de(html) for t in c['record']['dual_enrollment'].get('eligibility_tiers', [])]
        # Dalton State / Georgia Southern / Columbus Tech / Savannah Tech / GMC: not high-school admission minimums.
        self.assertEqual(tiers('<p>SAP is defined as a minimum cumulative course completion rate of 67% and a minimum GPA of 2.0.</p>'
                               '<p>A student is in Good Academic Standing with an institutional grade point average (GPA) of 2.0 or higher.</p>'
                               '<p>If a student does not have a 2.00 high school GPA, they will need a qualifying test score.</p>'
                               '<p>Rhett Dozier earned an Associate of Science degree with a 4.0 GPA.</p>'
                               '<p>Juniors or Seniors with a 2.0 or higher GPA</p>'), [(2.0, ['11', '12'])])
        # Southern Regional / Athens Tech / West Georgia Tech: completed grades vs grades named.
        self.assertEqual(tiers('<p>HOPE GPA: 2.6 or higher (after 10th grade completion)</p>'), [(2.6, ['11', '12'])])
        self.assertEqual(tiers('<p>10th grade students must submit an overall GPA of 2.0 or higher after the completion of the 9th grade.</p>'), [(2.0, ['10'])])
        self.assertEqual(tiers('<p>11th and 12th graders with a 2.00 high school GPA can enroll in academic core classes.</p>'), [(2.0, ['11', '12'])])
        self.assertEqual(dual._grades('Students must have a minimum class rank of junior.'), ['11', '12'])
        # FL r1: "Career Dual Enrollment" tiers are scoped, so the academic 3.0 stays the general minimum.
        [c] = self._de('<p>A 3.0 high school GPA for Academic Dual Enrollment.</p><p>Career Dual Enrollment can be taken with a 2.5 or higher unweighted GPA.</p>')
        self.assertEqual(c['record']['dual_enrollment'].get('min_hs_gpa'), 3.0)
        # VA r1 (ODU) / NC r1 (CPCC): "Art History" and "History of Art" are not IB History.
        self.assertIsNone(exams.match('IB', 'Art History'))
        self.assertIsNone(exams.match('IB', 'History of Art'))
        self.assertEqual(exams.match('IB', 'History (HL)'), ('IB-HISTORY-HL', 'IB History (HL)'))
        # Gordon State CLEP: section-heading rows are skipped; merged score tiers go to review.
        rows = [['CLEP Exam', 'Minimum Score', 'Course Equivalent', 'Credit'], ['Humanities', 'Foreign Languages', '', ''],
                ['American Literature', '50', 'ENGL 2131, 2132', '6'], ['French Language', '50 62', 'FREN 1101, 1102 FREN 1101, 1102, 2001, 2002', '6 12'],
                ['Biology', '50', 'BIOL 1107', '4']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'CLEP', [{'rows': rows, 'heading': 'College Level Examination Program (CLEP)', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertNotIn('CLEP-HUMANITIES', [e['exam_or_course_code'] for e in c['record']['equivalencies']])
        self.assertIn('merged_score_cells', c['issues'])
        # Georgia College: SAT/ACT section scores are not composite minimums.
        [c] = self._de('<p>Have a minimum 580 Evidence-based Reading/Writing and 560 Math on the SAT OR 23 English &amp; 22 Math on the ACT, AND a High School academic GPA of 3.0 or higher.</p>')
        self.assertNotIn('alt_min_sat', c['record']['dual_enrollment'])
        self.assertNotIn('alt_min_act', c['record']['dual_enrollment'])
        # UGA / Coastal Georgia: "45 of the last 60" is 45 hours in residence; Atlanta Metro / KSU: course-specific or advisory grades.
        html = ('<title>Transfer FAQs</title><p>To earn a UGA baccalaureate degree, at least 45 of the last 60 semester credit hours must be completed in residence at UGA.</p>'
                '<p>A grade of C or higher must have been earned in Composition courses in order to receive transfer credit for ENGL 1101.</p>'
                '<p>Transfer applicants are encouraged to have completed MATH 1101 with grades of "C" or better.</p>')
        [c] = transfer.extract(INST, ENTRY, T.parse_html(html), '2026-27')
        self.assertEqual(c['record'].get('residency_requirement_credits'), 45)
        [c] = transfer.extract(INST, ENTRY, T.parse_html('<title>Transfer Admissions</title><p>Thirty (30) of the last 60 hours must be earned at FGCU to receive a baccalaureate degree.</p>'), '2026-27')
        self.assertEqual(c['record'].get('residency_requirement_credits'), 30)
        # FSU-style AP chart: the "score" column holds course codes; a table with no course column is incomplete.
        rows = [['AP Exam', 'Score 3', 'Score 4'], ['Art History', 'ARH 2000 (3)', 'ARH 2000 & ARH 2050'], ['Biology', 'BSC 2010 (3)', 'BSC 2010 & 2011'],
                ['Chemistry', 'CHM 1045 (3)', 'CHM 1045 & 1046']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'AP', [{'rows': rows, 'heading': 'Advanced Placement', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertIn('score_column_not_scores', c['issues'])
        rows = [['IB Exam', 'Minimum Score', 'Credits'], ['Biology', '4', '8'], ['Chemistry', '5', '4'], ['Economics', '5', '3']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'IB', [{'rows': rows, 'heading': 'International Baccalaureate', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertIn('course_column_missing', c['issues'])
        self.assertNotIn('min_grade', c['record'])
        # NC r1: Chowan's "($44,000 over 4 years)" is not the annual maximum; Greensboro's achievements list and divinity aid are skipped.
        got = {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(
            '<title>Scholarships</title><h2>Academic Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th></tr>'
            '<tr><td>Presidential Scholarship</td><td>$11,000 ($44,000 over 4 years)</td></tr><tr><td>Alumni Scholarship</td><td>$9,000 ($36,000 over 4 years)</td></tr></table>'), '2026-27')}
        self.assertEqual((got['Presidential Scholarship'].get('award_min'), got['Presidential Scholarship']['award_max']), (11000, 11000))
        self.assertTrue(common.professional_source({'url': 'https://divinity.wfu.edu/admissions/financial-aid/'}, T.Page('', 'Aid', [], [], [])))
        # Agnes Scott / Georgia Southern / WGTC: other organizations' award lists; Thomas University: "+Scholarships" heading.
        table = ('<h2>National Scholarships</h2><table><tr><th>Scholarship</th><th>Amount</th><th>Eligibility</th></tr><tr><td>Coca-Cola Scholars</td><td>$20,000</td><td>Seniors</td></tr>'
                 '<tr><td>Ron Brown Scholar Program</td><td>$10,000</td><td>Seniors</td></tr></table>')
        for url in ('https://www.example.edu/aid/outside-scholarships.html', 'https://www.example.edu/military-scholarships', 'https://www.example.edu/foundation/foundation-scholarship/', 'https://www.example.edu/aid/scholarships/donor-scholarships/index.html', 'https://www.example.edu/academics/student-academic-achievements/', 'https://home.example.edu/student-affairs/testing/intl_credits/',
                    'https://www.example.edu/college/retirees/emeriti', 'https://www.example.edu/aid/scholarships/bright-futures.html', 'https://www.example.edu/aid/grants/teach'):
            self.assertEqual(merit.extract(INST, {**ENTRY, 'url': url}, T.parse_html('<title>Scholarships</title>' + table), '2026-27'), [])
        self.assertEqual(len(merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title>' + table), '2026-27')), 2)  # the same table elsewhere is kept
        [c] = merit.extract(INST, ENTRY, T.parse_html('<title>On Campus Students</title><h3>+Scholarships</h3><table><tr><th>Unweighted GPA</th><th>Scholarship</th></tr>'
                                                     '<tr><td>3.9+</td><td>$7,000</td></tr><tr><td>3.7 – 3.89</td><td>$5,000</td></tr><tr><td>3.5 - 3.69</td><td>$3,000</td></tr></table>'), '2026-27')
        self.assertEqual((c['record']['award_name'], c['record']['award_min'], c['record']['award_max']), ('Scholarships', 3000, 7000))
        [c] = merit.extract(INST, ENTRY, T.parse_html('<title>Scholarships</title><h3>Merit-Based Aid</h3><table><tr><th>Calculated Admissions GPA</th><th>Annual Award Amount (One – Time)</th></tr>'
                                                     '<tr><td>4.00 +</td><td>$1000</td></tr><tr><td>3.80 – 3.99</td><td>$750</td></tr><tr><td>3.50 – 3.79</td><td>$500</td></tr>'
                                                     '<tr><td>Below 3.50</td><td>Not eligible for automatic merit aid</td></tr></table>'), '2026-27')
        self.assertEqual((c['record']['renewable'], c['record']['award_max']), (False, 1000))
        # GSW: the exam header says "Course" too; Georgia Tech: courses under a "Credit" header.
        rows = [['Advanced Placement Course', 'Minimum Score for Awarding Credit', 'GSW Course Credit', 'Semester Credit Hours'],
                ['Art History', '3', 'ARTC 1100', '3'], ['Biology', '3', 'BIOL 1103, 1103L', '4'], ['Chemistry', '3', 'CHEM 1211K', '4']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'Advanced Credit Courses', [{'rows': rows, 'heading': 'Advanced Placement', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertEqual([(e['institution_course_equivalent'], e['credits_awarded']) for e in c['record']['equivalencies']][:2], [('ARTC 1100', 3), ('BIOL 1103, 1103L', 4)])
        rows = [['Subject', 'Exam Scores', 'Credit'], ['Biology HL', '4-5', 'BIOS 1107 and BIOS 1107L'],
                ['Chemistry HL', '5-7', 'CHEM 1310'], ['Economics HL', '5-7', 'ECON 2100']]
        [c] = credit.extract(INST, ENTRY, T.Page('', 'International Baccalaureate Exams', [{'rows': rows, 'heading': 'International Baccalaureate Exams', 'caption': '', 'lead': ''}], [], []), '2026-27')
        self.assertEqual(c['record']['equivalencies'][1]['institution_course_equivalent'], 'CHEM 1310')

    def test_tn_r6_merit_tables(self):
        """TN 2026-10-03 merit tables: key/value facts, sentence rows, transfer tiers, criteria and points columns."""
        def awards(html, title='Scholarships'):
            return {c['record']['award_name']: c['record'] for c in merit.extract(INST, ENTRY, T.parse_html(f'<title>{title}</title>{html}'), '2026-27')}
        # UTK: "Requirement | Details" rows are facts about one award, not awards.
        self.assertEqual(awards('<h2>Next Chapter Scholar of the Year Scholarship</h2><table><tr><th>Requirement</th><th>Details</th></tr>'
                                '<tr><td>FAFSA Required</td><td>No</td></tr><tr><td>Residency</td><td>In-state only</td></tr>'
                                '<tr><td>Award Basis</td><td>Program-based</td></tr></table>'), {})
        # APSU: a first row of sentences is not a header.
        self.assertEqual(awards('<h2>Academic Scholarship Opportunities</h2><table><tr><td>Freshmen</td><td>Qualifying freshmen have a large number of opportunities; contact our office for details.</td></tr>'
                                '<tr><td>Transfer Students</td><td>Students transferring to APSU may be offered awards, particularly with an ACT.</td></tr>'
                                '<tr><td>Study Abroad</td><td>Potential scholarships available to students who are taking a study abroad course.</td></tr></table>'), {})
        # CBU: college-GPA tiers are transfer awards.
        self.assertEqual(awards('<h2>Scholarships</h2><table><tr><th>Scholarship</th><th>Award</th><th>College GPA</th></tr>'
                                '<tr><td>Presidential Scholarship</td><td>$18,000</td><td>3.6+</td></tr><tr><td>Lasallian Scholarship</td><td>$16,000</td><td>3.4+</td></tr>'
                                '<tr><td>University Scholarship</td><td>$12,000</td><td>N/A</td></tr></table>'), {})
        # UTK Orange & White: the criteria column is the threshold; the award is named by the page.
        got = awards('<h2>Award Amounts</h2><table><tr><th>Scholarship Criteria</th><th>Annual Award</th><th>Four-Year Award Amount</th></tr>'
                     '<tr><td>3.6-3.79 GPA*,28-36 ACT**,1300-1600 SAT**</td><td>$1,500</td><td>$6,000</td></tr><tr><td>OR</td><td></td><td></td></tr>'
                     '<tr><td>3.6+ GPA*,26-27 ACT**,1230-1290 SAT**</td><td>$1,500</td><td>$6,000</td></tr></table>',
                     title='Orange White Scholarship - One Stop Student Services')
        self.assertEqual(sorted(got), ['Orange White Scholarship: 3.6+ GPA*,26-27 ACT**,1230-1290 SAT**',
                                       'Orange White Scholarship: 3.6-3.79 GPA*,28-36 ACT**,1300-1600 SAT**'])
        # UTK In-State Volunteer: the score column labels the rows; the page names the award.
        got = awards('<h2>Award Amounts</h2><table><tr><th>ACT / SAT</th><th>Annual Award</th><th>Four-Year Award</th></tr>'
                     '<tr><td>34-36 / 1490-1600</td><td>$9,000</td><td>$36,000</td></tr><tr><td>30-33 / 1360-1480</td><td>$5,000</td><td>$20,000</td></tr></table>',
                     title='In-State Volunteer Scholarship - One Stop Student Services')
        r = got['In-State Volunteer Scholarship: ACT / SAT 30-33 / 1360-1480']
        self.assertEqual((r['award_max'], r['test_requirement']), (5000, 'ACT / SAT: 30-33 / 1360-1480'))
        got = awards('<h2>Award Amounts</h2><table><tr><th>*UT Core Weighted GPA</th><th>**ACT/SAT Score</th><th>Annual Award</th></tr>'
                     '<tr><td>4.0+</td><td>34-36/1490-1600</td><td>$18,000</td></tr><tr><td>4.0+</td><td>30-33/1360-1480</td><td>$9,000</td></tr></table>',
                     title='Out-of-State Volunteer Scholarship - One Stop Student Services')
        r = got['Out-of-State Volunteer Scholarship: UT Core Weighted GPA 4.0+, ACT/SAT Score 30-33/1360-1480']
        self.assertEqual((r['award_max'], r['gpa_requirement'], r['test_requirement']),
                         (9000, 'UT Core Weighted GPA: 4.0+', 'ACT/SAT Score: 30-33/1360-1480'))
        # Southern Adventist: a points column is the eligibility rule and keeps its name.
        got = awards('<h2>Renewable Scholarships for Freshmen</h2><table><tr><th>Points</th><th>Scholarship</th><th>4 Year Total</th><th>Awarded Per Year</th></tr>'
                     '<tr><td>4,800 - 5,700</td><td>Honors</td><td>$8,000</td><td>$2,000</td></tr><tr><td>5,701 - 6,600</td><td>Dean</td><td>$16,000</td><td>$4,000</td></tr></table>')
        self.assertEqual((got['Dean']['award_max'], got['Dean']['eligibility_summary']), (4000, 'Points: 5,701 - 6,600'))

    def test_dual_enrollment_eligibility_and_charges(self):
        # Layout from a real Tennessee page: eligibility list, then an FAQ with per-credit prices.
        [c] = self._de("""<h3>Eligibility & Requirements</h3><ul><li>High School Junior or Seniors</li>
<li>Minimum GPA of 3.0 (on 4.0 scale) OR minimum GPA of 2.0 with 19+ ACT composite score</li>
<li>Allowed to take a maximum of 14 credit hours per semester</li></ul>
<p>$174/credit hour | $10/credit hour - Technology Fee. Tennessee residents are eligible for the TN Dual Enrollment Grant.</p>""")
        de = c['record']['dual_enrollment']
        self.assertEqual(c['record']['policy_kind'], 'dual_enrollment')
        self.assertEqual(de['max_credit_hours_per_term'], 14)
        self.assertTrue(de['state_grant_accepted'])
        self.assertEqual([(x['amount'], x['kind']) for x in de['per_credit_hour_charges']], [(174, 'other'), (10, 'fee')])
        self.assertNotIn('tuition_per_credit_hour', de)  # '$174/credit hour' never says tuition
        self.assertEqual(de['eligibility_tiers'][0]['min_hs_gpa'], 3.0)
        self.assertEqual(de['eligibility_tiers'][0]['grades'], ['11', '12'])  # from the heading line just above

    def test_dual_enrollment_grade_tiers_and_mixed_grant(self):
        [c] = self._de("""<p>All high school sophomores with a minimum grade point average (GPA) of 3.5 are eligible for dual
enrollment. The TN grant does not apply; no discounts are offered.</p><p>All high school juniors and seniors with a
minimum grade point average (GPA) of 3.0 are eligible for dual enrollment. Out-of-state scholarships and the TN grant apply.</p>""")
        de = c['record']['dual_enrollment']
        self.assertEqual([(t['grades'], t['min_hs_gpa']) for t in de['eligibility_tiers']], [(['10'], 3.5), (['11', '12'], 3.0)])
        self.assertNotIn('min_hs_gpa', de)  # tiers disagree, so no single minimum
        self.assertNotIn('state_grant_accepted', de)
        self.assertIn('state_grant_mixed_statements', c['issues'])

    def test_dual_enrollment_needs_a_dual_enrollment_page(self):
        self.assertEqual(self._de('<p>Minimum GPA of 3.0 for dual enrollment.</p>', url='https://www.example.edu/admissions/', title='Admissions'), [])

    def test_pages_merge_field_by_field(self):
        a = self._de('<p>Juniors and seniors need a minimum GPA of 3.0.</p>', url='https://e.edu/dual-enrollment/a')[0]
        b = self._de('<p>Dual enrollment students may take a maximum of 12 credit hours per semester.</p>', url='https://e.edu/dual-enrollment/b')[0]
        b['source']['sha256'] = 'cd' * 32; b['candidate_id'] = 'other'
        [m] = review.dedupe([a, b])
        self.assertEqual((m['record']['dual_enrollment']['min_hs_gpa'], m['record']['dual_enrollment']['max_credit_hours_per_term']), (3.0, 12))
        self.assertEqual(m['record']['additional_source_urls'], ['https://e.edu/dual-enrollment/b'])
        self.assertEqual(m['issues'], [])
        c = self._de('<p>Dual enrollment students may take a maximum of 15 credit hours per semester.</p>', url='https://e.edu/dual-enrollment/c')[0]
        c['candidate_id'] = 'third'
        [m] = review.dedupe([a, b, c])
        self.assertNotIn('max_credit_hours_per_term', m['record']['dual_enrollment'])  # 12 vs 15: dropped and queued
        self.assertIn('conflicting_sources:max_credit_hours_per_term', m['issues'])

    def test_https_page_is_the_merge_primary(self):
        """TN r6, Tennessee Wesleyan: an http twin with more fields must not become the cited source."""
        a = self._de('<p>Juniors and seniors need a minimum GPA of 3.0. Students may take a maximum of 12 credit hours per semester.</p>',
                     url='http://e.edu/dual-enrollment/')[0]
        b = self._de('<p>Juniors and seniors need a minimum GPA of 3.0.</p>', url='https://e.edu/dual-enrollment/')[0]
        b['source']['sha256'] = 'cd' * 32; b['candidate_id'] = 'other'
        [m] = review.dedupe([a, b])
        self.assertEqual(m['record']['source_url'], 'https://e.edu/dual-enrollment/')
        self.assertEqual(m['record']['dual_enrollment']['max_credit_hours_per_term'], 12)

    def test_residency_from_table_captions_and_reciprocity(self):
        """Regression (KY, Ashland CTC): stacked In-State / Out-of-State COA tables; a neighbouring-state reciprocity table."""
        inst = {**INST, 'state': 'KY'}
        got = {c['record']['residency']: c for c in costs.extract(inst, ENTRY, page('coa_captions_ky.html'), '2026-27')}
        self.assertEqual(got['in_state']['record']['tuition'], 4752)
        self.assertEqual(got['out_of_state']['record']['tuition'], 6480)
        self.assertNotIn('residency_unknown', got['in_state']['issues'])
        recip = [c for c in got.values() if c['record'].get('tuition') == 5000]
        self.assertEqual(len(recip), 1)
        self.assertIn('residency_names_another_state', recip[0]['issues'])

    def test_state_names_mean_in_state_only_for_the_home_state(self):
        self.assertEqual(costs.residency('Kentucky Residents', 'KY'), 'in_state')
        self.assertEqual(costs.residency('Non-Tennessee Residents', 'TN'), 'out_of_state')
        self.assertEqual(costs.residency('Ohio and Indiana residents', 'KY'), 'named_other_state')
        self.assertEqual(costs.residency('West Virginia residents', 'VA'), 'named_other_state')
        self.assertEqual(costs.residency('Tennessee residents', None), 'named_other_state')  # unknown home state is never assumed

    def test_table_kind_comes_from_the_nearest_label(self):
        """Regression (KY, Big Sandy CTC): an IB table under a CLEP section heading was read as CLEP."""
        got = {c['record']['policy_kind']: c for c in credit.extract(INST, ENTRY, page('cpl_stacked_ky.html'), '2026-27')}
        self.assertEqual(sorted(got), ['AP', 'CLEP', 'IB'])
        self.assertEqual(len(got['IB']['record']['equivalencies']), 3)
        self.assertEqual(got['AP']['record']['equivalencies'][0]['institution_course_equivalent'], 'ART 105 or ART 106')

    def test_exam_column_is_not_the_code_column(self):
        """Regression (KY, EKU): 'Test Code' precedes 'AP Exam'; the code column was taken as the exam column."""
        (c,) = credit.extract(INST, ENTRY, page('ap_test_code_ky.html'), '2026-27')
        eqs = c['record']['equivalencies']
        self.assertEqual(len(eqs), 4)
        self.assertEqual([e['minimum_score'] for e in eqs if e['exam_or_course_code'] == 'AP-BIOLOGY'], ['3', '5'])
        self.assertEqual(eqs[0]['notes'], 'APAH')  # the printed code is kept, not dropped
        self.assertEqual(eqs[0]['credits_awarded'], 3)

    def test_courseleaf_program_groups(self):
        """Courseleaf (KY: WKU, EKU, Bellarmine): Course List tables; subtotals are not the degree total."""
        out = catalog.extract(INST, {**ENTRY, 'url': 'https://catalog.example.edu/undergraduate/science/biology/biology-bs/'},
                              page('courseleaf_program.html'), '2026-27')
        prog = next(c for c in out if c['domain'] == 'academic_programs')['record']
        self.assertEqual((prog['program_name'], prog['total_credits'], prog['credential_level']), ('Biology, Bachelor of Science', 120, 'bachelor'))
        groups = {c['record']['requirement_key']: c for c in out if c['domain'] == 'degree_requirements'}
        core = groups['program-requirements-52-hours-required-core']
        self.assertNotIn('minimum_credits', core['record'])  # the parent "(52 hours)" is not this sub-area's minimum
        self.assertIn('course_alternatives_in_rule_text', core['issues'])
        self.assertEqual(groups['program-requirements-52-hours-electives']['record']['rule_details']['choose_credits'], 12)
        self.assertEqual(groups['program-total']['record']['minimum_credits'], 120)
        self.assertNotIn('course_alternatives_in_rule_text', groups['colonnade-general-education-requirements']['issues'])
        # Regression (KY, WKU English BA): pairing rows were area headers. "Choose one pairing" has no schema shape,
        # so the group is skipped and the program goes to the exception queue rather than misstated.
        self.assertNotIn('literature-survey', groups)
        prog_c = next(c for c in out if c['domain'] == 'academic_programs')
        ranged = T.parse_html((FIX / 'courseleaf_program.html').read_bytes().replace(b'Total Hours 120</td>', b'Total Hours 112-124</td>'), 'https://x')
        rp = next(c for c in catalog.extract(INST, ENTRY, ranged, '2026-27') if c['domain'] == 'academic_programs')
        self.assertNotIn('total_credits', rp['record'])  # Regression (WKU Theatre BA): a range is not a total
        self.assertIn('requirement_groups_skipped', prog_c['issues'])
        # NC r1 (NC State): a course list under an "Electives" heading with no "select N" line is a pool to choose from.
        pool = T.parse_html((FIX / 'courseleaf_program.html').read_bytes().replace(b'<tr><td>Select 12 hours from the following:</td><td>12</td></tr>', b''), 'https://x')
        g = {c['record']['requirement_key']: c['record'] for c in catalog.extract(INST, ENTRY, pool, '2026-27') if c['domain'] == 'degree_requirements'}
        self.assertEqual(g['program-requirements-52-hours-electives']['rule_details']['group_type'], 'elective_pool')
        self.assertEqual(g['program-requirements-52-hours-required-core']['rule_details']['group_type'], 'all_required')
        # VSU: a "| University Catalog" title suffix is not part of the program name.
        piped = T.parse_html((FIX / 'courseleaf_program.html').read_bytes().replace(b'(0123) &lt; Example University', b'(0123) | Example University Catalog'), 'https://x')
        self.assertEqual(next(c for c in catalog.extract(INST, ENTRY, piped, '2026-27') if c['domain'] == 'academic_programs')['record']['program_name'],
                         'Biology, Bachelor of Science')
        # NC State: footnote markers ("Cells 1" with a "1" footnote line) are not part of course titles.
        noted = T.parse_html((FIX / 'courseleaf_program.html').read_bytes().replace(b'Biological Concepts: Cells</td>', b'Biological Concepts: Cells 1</td>')
                             .replace(b'</body>', b'<p>1</p><p>A grade of C- or higher is required.</p></body>'), 'https://x')
        g = {c['record']['requirement_key']: c['record'] for c in catalog.extract(INST, ENTRY, noted, '2026-27') if c['domain'] == 'degree_requirements'}
        self.assertEqual(g['program-requirements-52-hours-required-core']['rule_details']['courses'][0]['title'], 'Biological Concepts: Cells')

    def test_dual_credit_vocabulary_and_faq_questions(self):
        """Regression (KY): 'Dual Credit' pages were skipped (TN says 'dual enrollment'); a FAQ question's price was taken as a charge."""
        html = (b'<html><head><title>Dual Credit | Example CTC</title></head><body><h1>Dual Credit</h1>'
                b'<p>Students must have a 2.0 high school GPA to enroll in dual credit courses.</p>'
                b'<p>For the 2026-2027 academic year, dual credit tuition is capped at $99 per credit hour.</p>'
                b'<p>For students taking online classes, are we waiving the $20 per credit hour online course fee</p>'
                b'<p>The Kentucky Dual Credit Scholarship can be used for up to two courses.</p></body></html>')
        (c,) = dual.extract(INST, {**ENTRY, 'url': 'https://example.edu/dual-credit/'}, T.parse_html(html, 'https://example.edu/dual-credit/'), '2026-27')
        de = c['record']['dual_enrollment']
        self.assertEqual([x['amount'] for x in de['per_credit_hour_charges']], [99])
        self.assertEqual(de['tuition_per_credit_hour'], 99)
        self.assertIs(de['state_grant_accepted'], True)

    def test_resident_as_housing_is_not_in_state(self):
        """Regression (KY: Union, Campbellsville, Lindsey Wilson): 'Residential Student', 'Resident Budget' meant in-state."""
        self.assertIsNone(costs.residency('traditional residential student 2026-2027', 'KY', private=True))
        self.assertIsNone(costs.residency('resident budget', 'KY'))
        self.assertIsNone(costs.residency('resident', 'KY', private=True))
        self.assertIsNone(costs.residency('resident | commuter', 'KY'))
        self.assertEqual(costs.residency('resident students', 'KY'), 'in_state')  # public tuition tables (Ashland)
        self.assertEqual(costs.residency('nonresident', 'KY', private=True), 'out_of_state')

    def test_dual_gpa_ranges_and_course_scoped_tiers(self):
        """Regression (KY: Thomas More '2.5 to 2.79 GPA' -> 2.79; KCTCS technical-course 2.0 GPA shown as the general minimum)."""
        html = (b'<html><head><title>Dual Credit</title></head><body><p>Students admitted with an unweighted 2.5 to 2.79 GPA may only take one course.</p>'
                b'<p>3.3 Addendum for Enrollment into Technical Education Dual Credit Courses: students without the minimum unweighted high school 2.0 GPA required for technical course work</p></body></html>')
        (c,) = dual.extract(INST, {**ENTRY, 'url': 'https://x.edu/dual-credit/'}, T.parse_html(html, 'https://x'), '2026-27')
        de = c['record']['dual_enrollment']
        self.assertEqual([(t['min_hs_gpa'], t.get('course_scope')) for t in de['eligibility_tiers']], [(2.5, None), (2.0, 'technical')])
        self.assertEqual(de['min_hs_gpa'], 2.5)  # the technical-course tier is not the page's general minimum

    def test_ib_course_header_is_not_the_equivalent_column(self):
        """Regression (KY, Big Sandy): 'IB Course | Score | Credit Awarded | Credit Statement' lost every course and credit."""
        got = {c['record']['policy_kind']: c for c in credit.extract(INST, ENTRY, page('cpl_stacked_ky.html'), '2026-27')}
        ib = got['IB']['record']['equivalencies'][0]
        self.assertEqual((ib['institution_course_equivalent'], ib['credits_awarded']), ('BIO 152', 3))
        self.assertEqual(got['AP']['record']['equivalencies'][0]['credits_awarded'], 6)  # "6 credit hours"

    def test_dual_grant_negations_and_glossaries(self):
        """Regression (KY: EKU 'may not use the KHEAA ... Scholarship' read as accepted; Owensboro glossary GPA as a tier)."""
        html = (b'<html><head><title>Dual Credit</title></head><body><p>KHEAA Dual Credit Scholarships may be used towards covering tuition.</p>'
                b'<p>Homeschool students may not use the KHEAA Work Ready Dual Credit Scholarship to pay for their courses.</p>'
                b'<p>The student must have an unweighted GPA of 2.5 or higher.</p></body></html>')
        (c,) = dual.extract(INST, {**ENTRY, 'url': 'https://x.edu/dual-credit/'}, T.parse_html(html, 'https://x'), '2026-27')
        self.assertNotIn('state_grant_accepted', c['record']['dual_enrollment'])
        self.assertIn('state_grant_mixed_statements', c['issues'])
        g = b'<html><head><title>Glossary | Dual Credit</title></head><body><p>Grade point average: GPA of 2.0 (a C average) on a 4.0 scale.</p></body></html>'
        self.assertEqual(dual.extract(INST, {**ENTRY, 'url': 'https://x.edu/dual-credit/glossary.aspx'}, T.parse_html(g, 'https://x'), '2026-27'), [])

    def test_or_regressions_address_cost_rows_and_non_programs(self):
        """Regression (OR): Lewis & Clark title address -> in_state; Clackamas COA rows as awards; UO/SOCC non-programs."""
        self.assertIsNone(costs.residency('oregon', 'OR', private=True))
        self.assertEqual(costs.residency('oregon residents', 'OR'), 'in_state')
        self.assertTrue(merit.NOT_AWARD_NAME.search('Books/Supplies'))
        self.assertTrue(merit.NOT_AWARD_NAME.search('Personal expenses (entertainment, clothes, etc.)'))
        self.assertFalse(merit.NOT_AWARD_NAME.search('Presidential Scholarship'))
        for title in ("Bachelor's Degree Requirements | University of Oregon Academic Catalog", 'Oregon Transfer Module (OTM) < SOCC'):
            html = ('<html><head><title>%s</title></head><body><p>2026-2027 Catalog</p><h2>Courses</h2><table><caption>Course List</caption>'
                    '<tr><th>Code</th><th>Title</th><th>Hours</th></tr><tr><td>WR 121</td><td>Composition</td><td>4</td></tr></table></body></html>' % title)
            self.assertEqual(catalog.extract(INST, ENTRY, T.parse_html(html.encode(), 'https://x'), '2026-27'), [])

    def test_quarter_term_columns_and_arrangement_vocabulary(self):
        """Regression (OR: OSU '3 Terms | 1 Term', community colleges '1-4 Terms', Blue Mountain 'w/parent')."""
        cm = costs.column_meaning
        self.assertEqual([cm(h)['period'] for h in ('3 Terms', '1 Term', '2 terms', '4 Terms', '9 Months', '3 Months')],
                         ['year', 'semester', 'partial_year', 'partial_year', 'year', 'partial_year'])
        self.assertEqual(cm('Dependent (living w/parent)')['arrangement'], 'with_parents_or_family')
        self.assertEqual(cm('Not living w/parents (dependent and independent)')['arrangement'], 'off_campus_not_with_family')
        self.assertEqual(cm('Living in Student Housing')['arrangement'], 'on_campus')
        self.assertEqual(cm('Living in Own House/Apartment')['arrangement'], 'off_campus_not_with_family')
        self.assertIsNone(cm('Dependent Student')['arrangement'])  # dependency status is not a living arrangement
        html = ('<html><head><title>Cost of Attendance</title></head><body><h2>2026-2027 Estimated Resident Undergraduate</h2><table>'
                '<tr><th></th><th>3 Terms</th><th>1 Term</th></tr><tr><td>Tuition and Fees</td><td>$13,000</td><td>$4,333</td></tr>'
                '<tr><td>Living Expenses (Food and Housing)</td><td>$15,000</td><td>$5,000</td></tr>'
                '<tr><td>Books, Course Materials, Supplies, and Equipment</td><td>$1,200</td><td>$400</td></tr>'
                '<tr><td>Estimated TOTAL</td><td>$29,200</td><td>$9,733</td></tr></table></body></html>')
        (c,) = costs.extract({**INST, 'state': 'OR'}, ENTRY, T.parse_html(html.encode(), 'https://x'), '2026-27')
        self.assertEqual((c['record']['residency'], c['record']['total_cost_of_attendance']), ('in_state', 29200))
        self.assertNotIn('arrangement_unlabeled', c['issues'])

    def test_international_pages_and_billable_subtotals(self):
        """Regression (OR: PCC/Chemeketa international budgets conflicting with domestic COA; OSU billable subtotals)."""
        from pipeline.extractors import common
        P = type('P', (), {'title': ''})()
        self.assertTrue(common.international_source({'url': 'https://www.pcc.edu/international-students/tuition/'}, P))
        self.assertTrue(common.international_source({'url': 'https://www.centre.edu/admission-aid/international-applicants'}, P))
        self.assertFalse(common.international_source({'url': 'https://x.edu/programs/international-business-ba/'}, P))
        html = ('<html><head><title>Cost of Attendance</title></head><body><h2>2026-2027 Estimated Resident Undergraduate</h2><table>'
                '<tr><th></th><th>3 Terms</th></tr><tr><td>Tuition and Fees</td><td>$13,000</td></tr><tr><td>Estimated Billable Cost Total</td><td>$13,000</td></tr>'
                '<tr><td>Living Expenses (Food and Housing)</td><td>$15,000</td></tr><tr><td>Books, Course Materials, Supplies, and Equipment</td><td>$1,200</td></tr>'
                '<tr><td>Estimated Non-Billable Cost Total</td><td>$16,200</td></tr><tr><td>Estimated TOTAL</td><td>$29,200</td></tr></table></body></html>')
        (c,) = costs.extract({**INST, 'state': 'OR'}, ENTRY, T.parse_html(html.encode(), 'https://x'), '2026-27')
        self.assertEqual(c['record']['total_cost_of_attendance'], 29200)
        self.assertNotIn('components_do_not_reconcile', c['issues'])

    def test_two_documents_with_the_same_record_key_are_both_compared(self):
        a = credit.extract(INST, ENTRY, page('ap.html'), '2026-27')[0]
        other = {**ENTRY, 'url': 'https://example.edu/y', 'sha256': 'ef' * 32}
        html = (FIX / 'ap.html').read_text().replace('ART 2140 &amp; ART 2150', 'ART 1000')
        b = credit.extract(INST, other, T.parse_html(html), '2026-27')[0]
        self.assertNotEqual(a['candidate_id'], b['candidate_id'])
        out = review.dedupe([a, b])
        self.assertEqual(len(out), 2)
        self.assertTrue(all(any(i.startswith('conflicting_sources') for i in c['issues']) for c in out))


    def test_catalog_program_groups_validate(self):
        sys.path.insert(0, str(ROOT / 'scripts'))
        from validate_data import validate_record
        e = {**ENTRY, 'url': 'https://catalog.example.edu/preview_program.php?catoid=50&poid=1234'}
        out = catalog.extract(INST, e, page('acalog_program.html'), '2026-27')
        prog = [c for c in out if c['domain'] == 'academic_programs'][0]['record']
        self.assertEqual((prog['program_name'], prog['credential_level'], prog['total_credits'], prog['catalog_year']),
                         ('Computer Science, B.S.', 'bachelor', 120, '2026-2027'))
        groups = {c['record']['requirement_key']: c['record'] for c in out if c['domain'] == 'degree_requirements'}
        ge = groups['general-education-requirements-41-credits']['rule_details']
        self.assertEqual((ge['group_type'], ge['category'], [x['code'] for x in ge['courses']]), ('all_required', 'general_education', ['ENGL 1010', 'ENGL 1020']))
        core = groups['major-core-36-credits']
        self.assertEqual([(x['code'], x.get('credits')) for x in core['rule_details']['courses']], [('CSCI 1250', 4), ('CSCI 1260', 4)])
        self.assertEqual(core['minimum_credits'], 36)
        math = groups['mathematics-requirement']['rule_details']
        self.assertEqual((math['group_type'], math['choose_count']), ('choose_courses', 1))
        el = groups['major-electives']['rule_details']
        self.assertEqual((el['group_type'], el['choose_credits']), ('choose_credits', 9))
        self.assertEqual(groups['program-total']['minimum_credits'], 120)
        for c in out:  # every emitted record satisfies the repository's own data contract
            self.assertEqual(validate_record(ROOT / 'data', {**c['record'], 'verification_status': 'partially_verified'}, 0, domain=c['domain']), [])

    def test_catalog_skips_unlabeled_and_graduate_pages(self):
        e = {**ENTRY, 'url': 'https://catalog.example.edu/preview_program.php?catoid=50&poid=1'}
        html = (FIX / 'acalog_program.html').read_text()
        self.assertEqual(catalog.extract(INST, e, T.parse_html(html.replace('2026-2027 Undergraduate Catalog', 'Catalog')), '2026-27'), [])
        self.assertEqual(catalog.extract(INST, e, T.parse_html(html.replace('Computer Science, B.S.', 'Computer Science, M.S.')), '2026-27'), [])
        old = catalog.extract(INST, e, T.parse_html(html.replace('2026-2027 Undergraduate Catalog', '2023-2024 Undergraduate Catalog [ARCHIVED CATALOG]')), '2026-27')
        self.assertTrue(all('stale_year_label:2023-24' in c['issues'] for c in old))


    def test_state_transfer_guarantee_statements(self):
        html = """<title>Transfer Admission Guarantee | TN Transfer Pathway</title><p>A student who completes all the courses listed on a
particular Transfer Pathway will earn an A.A. or A.S. degree at the community college. If a community college student transfers to another
Tennessee community college, he or she is guaranteed that all courses transfer. Admission to UT, Knoxville is competitive and the Pathways
do not guarantee admission there. These Transfer Pathways have been effective beginning Fall 2011 and are reviewed annually.</p>"""
        state = {'institution_key': 'state-TN', 'state': 'TN', 'control': 'state'}
        [c] = statepolicy.extract(state, {**ENTRY, 'url': 'https://www.tntransferpathway.org/transfer-admission-guarantee'}, T.parse_html(html), '2026-27')
        r = c['record']
        self.assertEqual((r['state'], r['policy_kind'], r['policy_key']), ('TN', 'transfer_guarantee', 'transfer-admission-guarantee'))
        self.assertNotIn('institution_key', r)
        self.assertTrue(any('guaranteed that all courses transfer' in x for x in r['statements']['guarantees']))
        self.assertTrue(any('competitive' in x for x in r['statements']['exceptions']))
        self.assertTrue(any('Fall 2011' in x for x in r['statements']['effective']))
        self.assertIn('semantic_review_required', c['issues'])
        sys.path.insert(0, str(ROOT / 'scripts'))
        from validate_data import validate_record
        from backend.catalog import import_contract_errors
        rec = {**r, 'verification_status': 'partially_verified'}
        self.assertEqual(validate_record(ROOT / 'data', rec, 0, domain='state_policies'), [])
        self.assertEqual(import_contract_errors('state_policies', rec), [])
        self.assertEqual(statepolicy.extract({'institution_key': 'ipeds-1', 'control': 'public'}, ENTRY, T.parse_html(html), '2026-27'), [])

    def test_state_regulation_titled_by_number_and_dual_credit_policy(self):
        """Regression (KY): 13 KAR 2:045 is titled by number; the CPE Dual Credit Policy had no state policy kind."""
        sinst = {'institution_key': 'state-KY', 'state': 'KY', 'control': 'state'}
        reg = (b'<html><head><title>Title 013 Chapter 2 Regulation 045</title></head><body><h1>13 KAR 2:045. Determination of residency status for admission and tuition assessment purposes.</h1>'
               b'<p>A person who enters the state primarily for the purpose of education shall be presumed to be nonresident.</p>'
               b'<p>A student must establish domicile in Kentucky for twelve months before the start of the term.</p></body></html>')
        (c,) = statepolicy.extract(sinst, {**ENTRY, 'url': 'https://apps.legislature.ky.gov/law/kar/titles/013/002/045/'}, T.parse_html(reg, 'https://x'), '2026-27')
        self.assertEqual(c['record']['policy_kind'], 'tuition_residency')
        dc = (b'<html><head><title>Dual Credit Policy for Kentucky</title></head><body><h1>Dual Credit Policy for Kentucky</h1>'
              b'<p>Students must meet the course prerequisites and placement requirements of the postsecondary institution.</p></body></html>')
        (d,) = statepolicy.extract(sinst, {**ENTRY, 'url': 'https://cpe.ky.gov/policies/academicaffairs/dualcreditpolicy.pdf'}, T.parse_html(dc, 'https://x'), '2026-27')
        self.assertEqual(d['record']['policy_kind'], 'dual_enrollment')
        self.assertIn('dual_enrollment', __import__('backend.catalog', fromlist=['x']).CONTROLLED_VALUES['state_policies']['policy_kind'])
        rep = dc.replace(b'Dual Credit Policy for Kentucky</title>', b'Dual Credit and Student Success Report</title>')
        self.assertEqual(statepolicy.extract(sinst, {**ENTRY, 'url': 'https://cpe.ky.gov/data/reports/dualcreditreport.pdf'}, T.parse_html(rep, 'https://x'), '2026-27'), [])

    def test_state_policy_extractor_ignores_institution_pages(self):
        """Regression (KY): registry institutions gained `state`; university transfer agreements became statewide policies."""
        html = (b'<html><head><title>Transfer Pathway Guide</title></head><body><p>All courses transfer and will be accepted toward the degree.</p>'
                b'<p>Students must complete the associate degree with a 2.0 GPA.</p></body></html>')
        inst = {**INST, 'state': 'KY'}
        self.assertEqual(statepolicy.extract(inst, ENTRY, T.parse_html(html, 'https://x'), '2026-27'), [])
        self.assertEqual(len(statepolicy.extract({'institution_key': 'state-KY', 'state': 'KY', 'control': 'state'}, ENTRY, T.parse_html(html, 'https://x'), '2026-27')), 1)

    def test_state_policy_keys_from_generic_titles(self):
        sinst = {'institution_key': 'state-KY', 'state': 'KY', 'control': 'state'}
        html = (b'<html><head><title>KHEAA</title></head><body><h1>Dual Credit Scholarship</h1>'
                b'<p>Students must be Kentucky residents enrolled in an eligible high school to receive dual credit awards.</p></body></html>')
        (c,) = statepolicy.extract(sinst, {**ENTRY, 'url': 'https://www.kheaa.com/web/scholarships-grants.faces'}, T.parse_html(html, 'https://x'), '2026-27')
        self.assertEqual(c['record']['policy_key'], 'scholarships-grants')
        self.assertRegex(c['record']['policy_key'], r'^[a-z0-9][a-z0-9-]*$')

    def test_state_crawl_skips_member_college_hosts(self):
        """Regression (KY): the state crawl followed kctcs.edu into ashland.kctcs.edu (an institution's own site)."""
        st = {'institution_key': 'state-KY', 'allowed_domains': ['kctcs.edu'], 'excluded_hosts': ['ashland.kctcs.edu']}
        self.assertTrue(registry.in_host_scope(st, 'kctcs.edu'))
        self.assertFalse(registry.in_host_scope(st, 'ashland.kctcs.edu'))
        self.assertFalse(registry.in_host_scope(st, 'catalog.ashland.kctcs.edu'))

    def test_state_handbook_chapters_keep_distinct_keys(self):
        """Regression (NV): every NSHE handbook chapter is titled 'Title 4 - Codification ...'; all became key 'title-4'."""
        sinst = {'institution_key': 'state-NV', 'state': 'NV', 'control': 'state'}
        html = (b'<html><head><title>Title 4 - Codification of Board Policy Statements</title></head><body><p>Chapter 15</p>'
                b'<p>REGULATIONS FOR DETERMINING RESIDENCY AND TUITION CHARGES</p>'
                b'<p>A student must provide documentation to support residency classification at the request of an institution.</p></body></html>')
        url = 'https://nshe.nevada.edu/Handbook/title4//T4-CH15%20Regulations%20for%20Determining%20Residency.pdf'
        (c,) = statepolicy.extract(sinst, {**ENTRY, 'url': url}, T.parse_html(html, 'https://x'), '2026-27')
        self.assertEqual(c['record']['policy_kind'], 'tuition_residency')
        self.assertEqual(c['record']['policy_key'], 't4-ch15-regulations-for-determining-residency')

    def test_requirement_rows_need_their_program(self):
        """VA r1 (VSU): requirement rows approved while their program went to review made the import fail."""
        tmp = Path(tempfile.mkdtemp())
        run = tmp / 'run'; run.mkdir()
        mk = lambda cid, domain, rec: {'candidate_id': cid, 'domain': domain, 'institution_key': 'ipeds-1', 'academic_year': '2026-27',
                                       'year_basis': 'labeled_in_source', 'issues': [], 'record': rec, 'source': {}, 'extractor': 'x', 'evidence': []}
        row = mk('r1', 'degree_requirements', {'program_key': 'agri-ed-bs', 'requirement_key': 'core', 'requirement_kind': 'major'})
        (run / 'candidates.json').write_text(json.dumps([row]))
        (run / 'verify.json').write_text('[]')
        (tmp / 'dec.json').write_text(json.dumps({'run': 'run', 'approve': [{'candidate_id': 'r1', 'reason': 'x'}]}))
        with mock.patch.object(P, 'ROOT', tmp):
            with self.assertRaises(ValueError):
                P.promote({'state': 'ZZ', 'institutions': [{'institution_key': 'ipeds-1', 'folder': 'x'}]}, tmp / 'dec.json', log=lambda *_: None)

    def test_state_policy_promotion_path(self):
        tmp = Path(tempfile.mkdtemp())
        with mock.patch.object(P, 'ROOT', tmp):
            path = P._file_for(None, 'state_policies', '2026-27', 'TN')
            P._upsert(path, None, '2026-27', {'state': 'TN', 'academic_year': '2026-27', 'policy_kind': 'transfer_guarantee',
                      'policy_key': 'x', 'title': 'X', 'verification_status': 'partially_verified', 'last_verified_at': '2026-10-02',
                      'source_url': 'https://e.gov'}, 'state_policies')
        d = json.loads((tmp / 'data/state_policies/TN/2026-27.json').read_text())
        self.assertEqual((d['state'], d['academic_year'], len(d['records'])), ('TN', '2026-27', 1))
        self.assertNotIn('state', d['records'][0])


class _Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


class CrawlTests(unittest.TestCase):
    def setUp(self):
        handler = functools.partial(_Quiet, directory=str(FIX / 'site'))
        self.server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.base = f'http://127.0.0.1:{self.server.server_port}'
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        self.server.shutdown(); self.server.server_close(); shutil.rmtree(self.tmp)

    def reg(self):
        inst = {**INST, 'name': 'Example', 'allowed_domains': [registry.registrable_domain('127.0.0.1')],
                'seeds': {'website': self.base + '/', 'net_price': 'https://vendor.example.com/npc'}, 'existing_sources': []}
        return {'state': 'ZZ', 'institutions': [inst], 'state_sources': []}

    def test_polite_fenced_resumable_crawl(self):
        run = crawl(self.reg(), self.tmp / 'run', budget=10, workers=1, delay=0, fetcher=Fetcher(delay=0, timeout=5), log=lambda *_: None)
        entries = run.entries()
        urls = {e['url']: e for e in entries}
        self.assertIn(self.base + '/finaid/ap-credit.html', urls)
        self.assertIn(self.base + '/finaid/cost-of-attendance.html', urls)
        self.assertEqual(urls[self.base + '/private/scholarships.html']['error'], 'disallowed_by_robots')
        self.assertFalse(any('elsewhere.example.org' in u or 'vendor.example.com' in u or '/news/' in u for u in urls))
        ap = urls[self.base + '/finaid/ap-credit.html']
        self.assertIn('ap_credit', ap['topics'])
        self.assertEqual(ap['year_labels'], {'2026-27': 2})
        self.assertTrue((run.dir / 'pages' / ap['page_file']).exists())
        before = len(entries)
        crawl(self.reg(), self.tmp / 'run', budget=10, workers=1, delay=0, fetcher=Fetcher(delay=0, timeout=5), log=lambda *_: None)
        self.assertEqual(len(Run(self.tmp / 'run').entries()), before)  # finished run is a no-op on resume

    def test_a_failing_fetch_does_not_stop_the_run(self):
        class Boom(Fetcher):
            def fetch(self, url):
                if url.endswith('ap-credit.html'): raise RuntimeError('boom')
                return super().fetch(url)
        run = crawl(self.reg(), self.tmp / 'run', budget=10, workers=1, delay=0, fetcher=Boom(delay=0, timeout=5), log=lambda *_: None)
        urls = {e['url']: e for e in run.entries()}
        self.assertTrue(urls[self.base + '/finaid/ap-credit.html']['error'].startswith('fetch_exception:RuntimeError'))
        self.assertIn(self.base + '/finaid/cost-of-attendance.html', urls)

    def test_crawl_delay_backoff_and_single_retry(self):
        class Challenging(_Quiet):
            hits = {}
            def do_GET(self):
                if self.path == '/robots.txt':
                    body = b'User-agent: *\nCrawl-delay: 2\nDisallow: /private/\n'
                    self.send_response(200); self.send_header('Content-Type', 'text/plain'); self.end_headers(); self.wfile.write(body); return
                if self.path.startswith('/finaid/ap-credit'):
                    Challenging.hits[self.path] = Challenging.hits.get(self.path, 0) + 1
                    self.send_response(202); self.end_headers(); return
                return super().do_GET()
        handler = functools.partial(Challenging, directory=str(FIX / 'site'))
        server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        base = f'http://127.0.0.1:{server.server_port}'
        try:
            reg = self.reg(); reg['institutions'][0]['seeds'] = {'website': base + '/'}
            f = Fetcher(delay=0, timeout=5)
            with mock.patch('pipeline.crawl.time.sleep'):  # keep the test fast; delays are asserted, not waited
                run = crawl(reg, self.tmp / 'r', budget=10, workers=1, delay=0, fetcher=f, log=lambda *_: None)
            host = f'127.0.0.1:{server.server_port}'
            self.assertGreaterEqual(f.gate.delay_for(host), 5.0)  # crawl-delay 2, then backoff after the 202
            self.assertEqual(Challenging.hits['/finaid/ap-credit.html'], 2)  # first try + exactly one retry
            tries = [e for e in run.entries() if e['url'].endswith('/finaid/ap-credit.html')]
            self.assertEqual([e.get('will_retry', False) for e in tries], [True, False])
        finally:
            server.shutdown(); server.server_close()

    def test_program_links(self):
        self.assertEqual(topics.link_score('https://catalog.x.edu/preview_program.php?catoid=5&poid=9', 'Accounting, MBA'), -1)
        self.assertEqual(topics.link_score('https://catalog.x.edu/preview_program.php?catoid=5&poid=9', 'Accounting, B.S.'), 30)
        self.assertTrue(topics.is_program_page('https://catalog.x.edu/preview_program.php?catoid=5&poid=9'))

    def test_clean_catalog_program_links_and_index(self):
        self.assertTrue(topics.is_program_page('https://undergrad.catalog.tntech.edu/programs/computer-science-bs'))
        self.assertFalse(topics.is_program_page('https://grad.catalog.tntech.edu/programs/mba'))
        self.assertFalse(topics.is_program_page('https://undergrad.catalog.tntech.edu/programs'))
        self.assertEqual(topics.link_score('https://undergrad.catalog.tntech.edu/programs?page=2', 'Next'), 25)
        self.assertEqual(topics.link_score('https://catalog.rhodes.edu/programs-study', 'Programs of Study'), 25)
        self.assertIn('degree_requirements', topics.link_topics('https://www.tntech.edu/engineering/pdf/degree-map/2026-27/BS_CS_Degree_Map_2026-27.pdf'))
        self.assertIn('degree_requirements', topics.link_topics('https://www.utc.edu/x.pdf', 'Clear Path for Advising'))

    def test_repeated_challenges_stop_a_host(self):
        from pipeline.crawl import HostGate
        g = HostGate(0.0)
        for _ in range(HostGate.CHALLENGE_STOP - 1): g.backoff('catalog.example.edu')
        self.assertFalse(g.stopped('catalog.example.edu'))
        g.answered('catalog.example.edu')  # an answered request resets the streak
        for _ in range(HostGate.CHALLENGE_STOP): g.backoff('catalog.example.edu')
        self.assertTrue(g.stopped('catalog.example.edu'))
        self.assertFalse(g.stopped('www.example.edu'))

    def test_strong_document_links_go_one_level_deeper(self):
        """Regression (TN r5, Rhodes): the 2026-27 AP/IB equivalency PDF was linked only from a depth-3 catalog page."""
        import hashlib
        from pipeline.crawl import crawl_institution
        b = 'https://www.example.edu'
        site = {b + '/': '<a href="/a/ap-credit.html">AP credit</a>',
                b + '/a/ap-credit.html': '<a href="/b/ap-credit.html">AP credit</a>',
                b + '/b/ap-credit.html': '<a href="/c/ap-credit.html">AP credit</a>',
                b + '/c/ap-credit.html': ('<a href="/files/2026-27_AP_IB_Equivalencies.pdf">AP and IB equivalencies 2026-27</a>'
                                          '<a href="/d/ap-credit.html">AP credit</a><a href="/files/ap-note.pdf">AP</a>'
                                          '<a href="/hum/240">Humanities 240</a>')}

        class Fake:
            def fetch(self, url):
                html = site.get(url, '%PDF-1.4 nothing')
                body = f'<html><head><title>AP credit</title></head><body>{html}</body></html>'.encode()
                return {'status': 200, 'final_url': url, 'content_type': 'text/html' if url in site else 'application/pdf',
                        'sha256': hashlib.sha256(body + url.encode()).hexdigest()}, body
        inst = {'institution_key': 'ipeds-1', 'domain': 'example.edu', 'allowed_domains': ['example.edu'],
                'seeds': {'website': b + '/'}, 'existing_sources': []}
        run = Run(self.tmp / 'deep')
        crawl_institution(inst, run, Fake(), budget=20, max_depth=3, log=lambda *_: None)
        urls = {e['url']: e['depth'] for e in run.entries()}
        self.assertEqual(urls.get(b + '/files/2026-27_AP_IB_Equivalencies.pdf'), 4)
        self.assertNotIn(b + '/d/ap-credit.html', urls)   # ordinary pages keep the depth limit
        self.assertNotIn(b + '/files/ap-note.pdf', urls)  # and so do weak documents
        site[b + '/'] += '<a href="http://www.example.edu/a/ap-credit.html">AP credit (again)</a>'
        run2 = Run(self.tmp / 'deep2')
        crawl_institution(inst, run2, Fake(), budget=20, max_depth=3, log=lambda *_: None)
        self.assertFalse(any(e['url'].startswith('http://') for e in run2.entries()))  # http twins of an https site are one page
        self.assertEqual(topics.link_score('https://catalog.rhodes.edu/hum/240', 'HUM 240 Credit'), -1)
        self.assertEqual(topics.link_score('https://catalog.example.edu/preview_course_nopop.php?catoid=3&coid=9', 'ENGL 1010'), -1)

    def test_courseleaf_program_links(self):
        self.assertTrue(topics.is_program_page('https://catalog.wku.edu/undergraduate/ogden/biology/biology-bs/'))
        self.assertFalse(topics.is_program_page('https://catalog.wku.edu/undergraduate/ogden/biology/biology-bs/biology-bs.pdf'))
        self.assertFalse(topics.is_program_page('https://catalogs.eku.edu/undergraduate/general-academic-information/academic-standards/'))
        self.assertEqual(topics.link_score('https://catalog.wku.edu/undergraduate/ogden/biology/biology-bs/', 'Biology, Bachelor of Science'), 30)
        self.assertEqual(topics.link_score('https://catalog.wku.edu/graduate/health-human-services/nursing/dnp/', 'Nursing Practice, DNP'), -1)

    def test_links_with_spaces_and_unicode_are_requoted(self):
        """Regression (NV: NSHE handbook chapters; OR: Klamath articulation PDFs) -> InvalidURL before fetching."""
        from pipeline.crawl import requote
        self.assertEqual(requote('https://nshe.nevada.edu/Handbook/T4-CH15 Residency.pdf'), 'https://nshe.nevada.edu/Handbook/T4-CH15%20Residency.pdf')
        self.assertEqual(requote('https://x.edu/a%20b/?q=1&r=a b'), 'https://x.edu/a%20b/?q=1&r=a%20b')  # no double encoding
        self.assertEqual(requote('https://x.edu/admisi\u00f3n/'), 'https://x.edu/admisi%C3%B3n/')
        self.assertEqual(requote('https://x.edu/p/#frag'), 'https://x.edu/p/')

    def test_budget_and_resume_continue_where_stopped(self):
        crawl(self.reg(), self.tmp / 'run', budget=2, workers=1, delay=0, fetcher=Fetcher(delay=0, timeout=5), log=lambda *_: None)
        self.assertEqual(len(Run(self.tmp / 'run').entries()), 2)
        crawl(self.reg(), self.tmp / 'run', budget=10, workers=1, delay=0, fetcher=Fetcher(delay=0, timeout=5), log=lambda *_: None)
        urls = [e['url'] for e in Run(self.tmp / 'run').entries()]
        self.assertEqual(len(urls), len(set(urls)))
        self.assertIn(self.base + '/finaid/cost-of-attendance.html', urls)


class ReviewAndPromoteTests(unittest.TestCase):
    def cand(self, **kw):
        [c] = credit.extract(INST, ENTRY, page('ap.html'), '2026-27')
        c.update(kw); return c

    def test_conflicting_sources_are_both_queued(self):
        a = self.cand()
        b = json.loads(json.dumps(a)); b['candidate_id'] = 'other'; b['source']['url'] = 'https://example.edu/y'
        b['record']['equivalencies'][0]['institution_course_equivalent'] = 'ART 1000'
        out = review.dedupe([a, b])
        self.assertEqual(len(out), 2)
        self.assertTrue(all(any(i.startswith('conflicting_sources') for i in c['issues']) for c in out))

    def test_change_against_verified_record_is_an_exception(self):
        c = self.cand()
        old = {**c['record'], 'verification_status': 'verified',
               'equivalencies': [{**c['record']['equivalencies'][0], 'institution_course_equivalent': 'ART 1000'}]}
        [d] = review.diff([c], {INST['institution_key']: [(Path('x.json'), 'credit_policies', old)]})
        self.assertEqual(d['diff']['status'], 'changed')
        self.assertIn('conflicts_with_verified_record', d['issues'])

    def test_status_rule(self):
        self.assertEqual(P.status_for({'year_basis': 'labeled_in_title', 'issues': []}, False), 'verified')
        self.assertEqual(P.status_for({'year_basis': 'source_unlabeled', 'issues': []}, False), 'partially_verified')
        self.assertIsNone(P.status_for({'year_basis': 'labeled_in_source', 'issues': ['x']}, False))
        self.assertEqual(P.status_for({'year_basis': 'labeled_in_source', 'issues': ['x']}, True), 'partially_verified')

    def test_upsert_refuses_weaker_replacement_of_verified(self):
        tmp = Path(tempfile.mkdtemp()) / 'f.json'
        rec = {'institution_key': 'k', 'academic_year': '2026-27', 'policy_kind': 'AP', 'verification_status': 'verified',
               'last_verified_at': '2026-10-02', 'source_url': 'https://e.edu'}
        P._upsert(tmp, 'k', '2026-27', rec, 'credit_policies')
        with self.assertRaises(ValueError):
            P._upsert(tmp, 'k', '2026-27', {**rec, 'verification_status': 'partially_verified'}, 'credit_policies')
        P._upsert(tmp, 'k', '2026-27', {**rec, 'last_verified_at': '2026-10-03'}, 'credit_policies')
        self.assertEqual(len(json.loads(tmp.read_text())['records']), 1)

    def test_verbatim_value_search(self):
        norm = T.normalize_for_search('Tuition $11,084 per year; ENGL 1010 – Composition')
        self.assertTrue(review.found_in(norm, 11084))
        self.assertFalse(review.found_in(norm, 1108))
        self.assertTrue(review.found_in(norm, 'ENGL 1010'))


class RegistryTests(unittest.TestCase):
    def test_program_depth_records_do_not_queue_national_reverification(self):
        """Issue #90: program-depth records (re-verified by programs/) stay out of existing_sources; other domains stay in."""
        fake = [(Path('a.json'), 'academic_programs', {'institution_key': 'k', 'program_url': 'https://x.edu/prog'}),
                (Path('b.json'), 'degree_requirements', {'institution_key': 'k', 'source_url': 'https://x.edu/req'}),
                (Path('c.json'), 'program_catalogs', {'institution_key': 'k', 'source_url': 'https://x.edu/cat'}),
                (Path('d.json'), 'costs', {'institution_key': 'k', 'source_url': 'https://x.edu/cost'}),
                (Path('e.json'), 'transfer_policies', {'institution_key': 'k', 'policy_url': 'https://x.edu/transfer'}),
                (Path('f.json'), 'awards', {'institution_key': 'k', 'source_url': 'https://x.edu/req'})]
        with mock.patch.object(registry, 'records', lambda: iter(fake)):
            self.assertEqual(registry.cited_sources(), {'k': ['https://x.edu/cost', 'https://x.edu/req', 'https://x.edu/transfer']})

    def test_tennessee_registry_is_current(self):
        built = registry.build('TN')
        self.assertEqual(built, registry.load('TN'), 'run: python -m pipeline registry --state TN')
        keys = {i['institution_key'] for i in built['institutions']}
        self.assertIn('utk', keys); self.assertIn('ipeds-221740', keys)
        self.assertNotIn('ipeds-492263', keys)  # UT System Office is not an institution students attend
        self.assertTrue(all(i['seeds'].get('website', '').startswith('https://') for i in built['institutions']))

    def test_every_committed_registry_is_current(self):
        for path in sorted((ROOT / 'pipeline/registry').glob('*.json')):
            self.assertEqual(registry.build(path.stem), registry.load(path.stem), f'run: python -m pipeline registry --state {path.stem}')

    def test_data_folders_are_unique_across_states(self):
        """NM r1: a folder holding data belongs to one institution in every state (ERAU Prescott/Daytona, UNM branches, admissions.* hosts)."""
        owner, curated = {}, registry.curated_folders()
        for path in sorted((ROOT / 'pipeline/registry').glob('*.json')):
            for inst in registry.load(path.stem)['institutions']:
                key, folder = inst['institution_key'], inst['folder']
                if folder in curated.values():  # a folder that already holds data belongs to exactly one institution
                    self.assertEqual(owner.setdefault(folder, key), key, f'{folder} is shared by {owner[folder]} and {key}')
                if folder in registry.GENERIC_LABELS:
                    self.assertEqual(curated.get(key), folder, f'{key} would be filed under the generic folder {folder}')
        self.assertFalse([f for f, keys in __import__('collections').Counter(curated.values()).items() if keys > 1])
        self.assertEqual((registry.folder_label('ashland.kctcs.edu'), registry.folder_label('admissions.unl.edu')), ('ashland', None))

    def test_seed_overrides_need_reason_and_evidence(self):
        built = registry.load('NV')
        nsu = next(i for i in built['institutions'] if i['unitid'] == 441900)
        self.assertEqual(nsu['allowed_domains'], ['nevadastate.edu'])
        self.assertTrue(nsu['seed_override']['ipeds_seeds']['website'].startswith('https://nsc.edu'))  # original kept
        with mock.patch.object(registry.json, 'loads', return_value={'seed_overrides': {'1': {'seeds': {'website': 'https://a.edu'}}}}):
            with self.assertRaises(ValueError): registry.seed_overrides('NV')

    def test_registrable_domain_is_not_state_specific(self):
        self.assertEqual(registry.registrable_domain('www.state.tn.us'), 'state.tn.us')
        self.assertEqual(registry.registrable_domain('www.state.ky.us'), 'state.ky.us')
        self.assertEqual(registry.registrable_domain('henderson.kctcs.edu'), 'kctcs.edu')

    def test_system_colleges_on_a_shared_domain_stay_on_their_own_hosts(self):
        """Regression (KY): 16 KCTCS colleges are subdomains of kctcs.edu; domain scoping let one college crawl another."""
        def inst(key, host):
            return {'institution_key': key, 'allowed_domains': ['kctcs.edu'], 'seeds': {'website': f'https://{host}/'}, 'existing_sources': []}
        a, b, c = inst('a', 'henderson.kctcs.edu'), inst('b', 'jefferson.kctcs.edu'), inst('c', 'kctcs.edu')
        c['seeds']['admissions'] = 'https://kctcs.edu/admissions'
        a['seeds']['admissions'] = 'https://www.kctcs.edu/apply'
        registry.scope_shared_domains([a, b, c])
        self.assertTrue(registry.in_host_scope(a, 'henderson.kctcs.edu'))
        self.assertTrue(registry.in_host_scope(a, 'catalog.henderson.kctcs.edu'))
        self.assertFalse(registry.in_host_scope(a, 'jefferson.kctcs.edu'))
        self.assertTrue(registry.in_host_scope(a, 'kctcs.edu'))  # its own seed is there ...
        self.assertTrue(registry.is_shared_host(a, 'www.kctcs.edu'))  # ... but that host belongs to the system
        self.assertFalse(registry.is_shared_host(a, 'henderson.kctcs.edu'))
        c2 = {'institution_key': 'x', 'allowed_domains': ['solo.edu'], 'seeds': {}, 'existing_sources': []}
        registry.scope_shared_domains([c2])
        self.assertTrue(registry.in_host_scope(c2, 'catalog.solo.edu'))

    def test_shared_host_pages_need_attribution_review(self):
        from pipeline.extractors import common
        c = common.make('credit_policies', 'ipeds-1', '2026-27', 'labeled_in_title', {}, [], {**ENTRY, 'shared_host': True}, 'x', {})
        self.assertIn('shared_site_attribution_review', c['issues'])
        self.assertNotIn('shared_site_attribution_review', P.INFORMATIONAL)
        self.assertEqual(common.make('credit_policies', 'ipeds-1', '2026-27', 'labeled_in_title', {}, [], ENTRY, 'x', {})['issues'], [])

    def test_state_pages_only_feed_state_level_extractors(self):
        """Regression: institution extractors ran on statewide pages and keyed records to 'state-TN'."""
        self.assertEqual(review.STATE_EXTRACTORS, [statepolicy.extract])
        calls = []
        with mock.patch.object(review, 'EXTRACTORS', [lambda *a: calls.append('inst') or []]), \
             mock.patch.object(review, 'STATE_EXTRACTORS', [lambda *a: calls.append('state') or []]):
            run = mock.Mock(); run.entries.return_value = [{'institution_key': 'state-TN', 'page_file': 'p', 'url': 'u'}]
            run.load_page.return_value = (None, [])
            review.extract_run({'state': 'TN', 'institutions': []}, run, '2026-27')
        self.assertEqual(calls, ['state'])


if __name__ == '__main__':
    unittest.main()
