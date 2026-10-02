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
from pipeline.extractors import appeals, catalog, cds, costs, credit, dual, merit, statepolicy, transfer  # noqa: E402

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


    def _de(self, body, url='https://www.example.edu/admissions/dual-enrollment/', title='Dual Enrollment'):
        return dual.extract(INST, {**ENTRY, 'url': url}, T.parse_html('<title>%s</title>%s' % (title, body)), '2026-27')

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
