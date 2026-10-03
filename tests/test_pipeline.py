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
        for url in ('https://www.example.edu/aid/outside-scholarships.html', 'https://www.example.edu/military-scholarships', 'https://www.example.edu/foundation/foundation-scholarship/', 'https://www.example.edu/aid/scholarships/donor-scholarships/index.html', 'https://www.example.edu/academics/student-academic-achievements/', 'https://home.example.edu/student-affairs/testing/intl_credits/'):
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
