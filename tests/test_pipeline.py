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
from pipeline.extractors import cds, costs, credit  # noqa: E402

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


if __name__ == '__main__':
    unittest.main()
