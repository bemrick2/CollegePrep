"""Program & Degree Deep Dive (programs/): crawl scope, platform rules, list extraction, evidence.

Synthetic pages only; no network. Fixture pages are not coverage."""
import hashlib, json, tempfile, unittest
from pathlib import Path

from programs import crawl as C, extract as X

ACALOG_HOME = b"""<html><head><title>2026-2027 Undergraduate Catalog - Example University</title></head><body>
<h1>2026-2027 Undergraduate Catalog</h1>
<a href="content.php?catoid=56&navoid=100">Programs A-Z</a>
<a href="content.php?catoid=40&navoid=9">Archived catalog</a>
<a href="https://other.example.org/x">Elsewhere</a></body></html>"""
ACALOG_LIST = b"""<html><head><title>Programs A-Z - 2026-2027 Undergraduate Catalog</title></head><body>
<h1>Programs A-Z</h1><p>2026-2027 Undergraduate Catalog</p>
<a href="preview_program.php?catoid=56&poid=1&returnto=100">Computer Science, BS</a>
<a href="preview_program.php?catoid=56&poid=2&returnto=100">Nursing, BSN</a>
<a href="preview_program.php?catoid=56&poid=3&returnto=100">Computer Science, MS</a>
<a href="preview_program.php?catoid=56&poid=4">Psychology Minor</a>
<a href="preview_program.php?catoid=40&poid=1">Computer Science, BS (2020)</a>
</body></html>"""
PROGRAM = b"""<html><head><title>Program: Computer Science, BS - 2026-2027 Undergraduate Catalog</title></head><body>
<h1>Computer Science, BS</h1><p>2026-2027 Undergraduate Catalog</p>
<p>Admission to the major is competitive and space-limited. Students must earn a minimum cumulative GPA of 3.0 in the prerequisite courses.</p>
<h2>Major Requirements</h2><p>COSC 102 - Introduction to Computer Science Credit Hours: 4</p>
<p>Total Hours: 120</p></body></html>"""
POLICY = b"""<html><head><title>Undeclared students</title></head><body>
<p>First-year students may enter as undeclared. Students must declare a major by the time they complete 45 credit hours.</p>
<p>The weather is nice.</p></body></html>"""


class FakeFetcher:
    def __init__(self, pages): self.pages = pages; self.calls = []
    def fetch(self, url):
        self.calls.append(url)
        body = self.pages.get(url)
        if body is None: return {'status': 404, 'error': 'http_404'}, None
        return {'status': 200, 'final_url': url, 'content_type': 'text/html', 'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body)}, body


TARGET = {'institution_key': 'ipeds-1', 'folder': 'ex', 'name': 'Example University', 'domains': ['example.edu'], 'hosts': [],
          'catalog': {'platform': 'acalog', 'catoid': 56, 'home': 'https://catalog.example.edu/index.php?catoid=56', 'program_lists': []},
          'policy': ['https://www.example.edu/undeclared']}
PAGES = {'https://catalog.example.edu/index.php?catoid=56': ACALOG_HOME,
         'https://catalog.example.edu/content.php?catoid=56&navoid=100': ACALOG_LIST,
         'https://catalog.example.edu/preview_program.php?catoid=56&poid=1': PROGRAM,
         'https://www.example.edu/undeclared': POLICY}


class DeepDiveTests(unittest.TestCase):
    def run_once(self, d):
        f = FakeFetcher(PAGES)
        run = C.Run(Path(d))
        C.crawl_target(TARGET, run, f, log=lambda *_: None)
        return f, run

    def test_scope_and_current_catalog_only(self):
        with tempfile.TemporaryDirectory() as d:
            f, run = self.run_once(d)
            self.assertFalse(any('other.example.org' in u for u in f.calls), 'off-domain link fetched')
            self.assertFalse(any('catoid=40' in u for u in f.calls), 'archived catalog followed')
            self.assertFalse(any('returnto' in u for u in f.calls), 'Acalog returnto not canonicalised')
            roles = {e['url']: e['role'] for e in run.entries()}
            self.assertEqual(roles['https://catalog.example.edu/preview_program.php?catoid=56&poid=1'], 'program_page')

    def test_resume_fetches_nothing_twice(self):
        with tempfile.TemporaryDirectory() as d:
            self.run_once(d)
            f2 = FakeFetcher(PAGES); C.crawl_target(TARGET, C.Run(Path(d)), f2, log=lambda *_: None)
            self.assertEqual(f2.calls, [])

    def test_program_list_credentials_and_evidence(self):
        with tempfile.TemporaryDirectory() as d:
            self.run_once(d)
            X.extract_run({'state': 'ZZ', 'institutions': [TARGET]}, d)
            lists = json.loads((Path(d) / 'program_lists.json').read_text())['ipeds-1']
            names = {p['name']: p['credential_level'] for p in lists['programs']}
            self.assertEqual(names['Computer Science, BS'], 'bachelor')
            self.assertEqual(names['Nursing, BSN'], 'bachelor')
            self.assertIsNone(names['Computer Science, MS'])      # graduate never counted as bachelor
            self.assertIsNone(names['Psychology Minor'])
            self.assertNotIn('Computer Science, BS (2020)', names)  # other catoid is not the current catalog
            self.assertIn('2026-2027', lists['printed_years'])
            ev = [json.loads(l) for l in (Path(d) / 'evidence.jsonl').read_text().splitlines()]
            cats = {(e['category'], e['sentence']) for e in ev}
            self.assertIn(('apply_to_major', 'Admission to the major is competitive and space-limited.'), cats)
            self.assertTrue(any(c == 'gpa_requirement' for c, _ in cats))
            self.assertIn(('declare_by', 'Students must declare a major by the time they complete 45 credit hours.'), cats)
            self.assertFalse(any('weather' in s for _, s in cats))
            for e in ev: self.assertTrue(e['sha256'] and e['url'].startswith('https://'))  # provenance on every sentence

    def test_page_reached_by_two_urls_gives_each_candidate_once(self):  # TX 2026-10-07-flag3: list link and sitemap link
        with tempfile.TemporaryDirectory() as d:
            self.run_once(d)
            m = Path(d) / 'manifest.jsonl'
            es = [json.loads(l) for l in m.read_text().splitlines()]
            prog = next(e for e in es if e.get('role') == 'program_page')
            m.write_text(m.read_text() + json.dumps({**prog, 'url': prog['url'].replace('https://', 'http://')}) + '\n')
            X.extract_run({'state': 'ZZ', 'institutions': [TARGET]}, d)
            ids = [json.loads(l)['candidate_id'] for l in (Path(d) / 'candidates.jsonl').read_text().splitlines()]
            self.assertTrue(ids)
            self.assertEqual(len(ids), len(set(ids)))

    def test_platform_rules(self):
        cl = {'catalog': {'platform': 'courseleaf', 'home': 'https://catalog.x.edu/', 'path_prefix': '/college-departments/', 'min_depth': 1}}
        r = C.program_rule(cl)
        self.assertTrue(r('https://catalog.x.edu/college-departments/engineering/computer-science-bs/'))
        self.assertFalse(r('https://catalog.x.edu/college-departments/engineering/'))
        self.assertFalse(r('https://catalog.x.edu/college-departments/engineering/courses/'))
        self.assertFalse(r('https://evil.x.org/college-departments/a/b/'))
        sm = {'catalog': {'platform': 'smartcatalog', 'home': 'https://u.smartcatalogiq.com/en/2026-2027/catalog/', 'path_prefix': '/en/2026-2027/catalog/'}}
        self.assertFalse(C.program_rule(sm)('https://u.smartcatalogiq.com/en/2025-2026/catalog/a/b'))
        self.assertTrue(C.in_scope({'domains': ['x.edu'], 'hosts': ['u.smartcatalogiq.com']}, 'https://u.smartcatalogiq.com/en/'))
        self.assertFalse(C.in_scope({'domains': ['x.edu'], 'hosts': ['u.smartcatalogiq.com']}, 'https://v.smartcatalogiq.com/en/'))

    def test_targets_are_official_and_wellformed(self):
        root = Path(__file__).resolve().parent.parent
        for st in ('TN', 'OR'):
            doc = json.loads((root / 'programs/targets' / f'{st}.json').read_text())
            keys = set()
            for t in doc['institutions']:
                self.assertNotIn(t['institution_key'], keys); keys.add(t['institution_key'])
                urls = [t.get('catalog', {}).get('home')] + t.get('catalog', {}).get('program_lists', []) + \
                       t.get('policy', []) + t.get('degree_maps', []) + t.get('discover', [])
                for u in filter(None, urls):
                    self.assertTrue(u.startswith('https://'), u)
                    self.assertTrue(C.in_scope(t, u), f'{t["folder"]}: seed outside official hosts: {u}')


if __name__ == '__main__':
    unittest.main()


class ProgramFieldRuleTests(unittest.TestCase):
    """backend/program_fields.py: CR-14 facts need verbatim evidence; completeness needs every listed program."""
    from backend import program_fields as F

    def test_admission_type_needs_quote_and_official_source(self):
        F = self.F
        ok = {'admission_type': 'direct', 'admission_details': {'quote': 'Admitted directly.', 'source_url': 'https://x.edu/a'}}
        self.assertEqual(F.field_errors('academic_programs', ok), [])
        self.assertTrue(F.field_errors('academic_programs', {'admission_type': 'direct'}))
        self.assertTrue(F.field_errors('academic_programs', {'admission_type': 'competitive', 'admission_details': ok['admission_details']}))
        self.assertTrue(F.field_errors('academic_programs', {'admission_type': 'direct', 'admission_details': {'quote': ' ', 'source_url': 'https://x.edu'}}))
        self.assertTrue(F.field_errors('academic_programs', {'admission_type': 'direct', 'admission_details': {'quote': 'q', 'source_url': 'http://x.edu'}}))
        self.assertTrue(F.field_errors('academic_programs', {'admission_details': ok['admission_details']}))

    def test_cip_needs_format_and_source(self):
        F = self.F
        self.assertEqual(F.field_errors('academic_programs', {'cip_code': '14.1901', 'cip_source_url': 'https://thec.example/x'}), [])
        self.assertTrue(F.field_errors('academic_programs', {'cip_code': '14.1901'}))
        self.assertTrue(F.field_errors('academic_programs', {'cip_code': '1419', 'cip_source_url': 'https://x'}))

    def test_internal_transfer_and_undeclared(self):
        F = self.F
        self.assertTrue(F.field_errors('academic_programs', {'internal_transfer': {'restricted': 'yes', 'quote': 'q', 'source_url': 'https://x'}}))
        self.assertEqual(F.field_errors('academic_programs', {'internal_transfer': {'restricted': True, 'quote': 'q', 'source_url': 'https://x', 'gpa_min': 2.5}}), [])
        base = {'institution_key': 'k', 'academic_year': '2026-27', 'catalog_url': 'https://x', 'source_url': 'https://x'}
        self.assertTrue(F.field_errors('program_catalogs', {**base, 'undeclared_policy': {'allowed': True, 'source_url': 'https://x'}}))

    def test_completeness_requires_every_listed_program_verified(self):
        F = self.F
        cat = {'institution_key': 'k', 'academic_year': '2026-27', 'catalog_url': 'https://x', 'source_url': 'https://x',
               'programs_complete': True, 'listed_bachelor_programs': 2, 'completeness_basis': 'A-Z list', 'listed_program_keys': ['a', 'b']}
        self.assertEqual(F.field_errors('program_catalogs', cat), [])
        self.assertTrue(F.field_errors('program_catalogs', {**cat, 'listed_program_keys': ['a']}))
        self.assertTrue(F.field_errors('program_catalogs', {**cat, 'completeness_basis': ''}))
        prog = lambda k, s='verified': ('p', 'academic_programs', {'institution_key': 'k', 'academic_year': '2026-27', 'program_key': k, 'verification_status': s})
        self.assertEqual(F.cross_errors([prog('a'), prog('b'), ('c', 'program_catalogs', cat)]), [])
        self.assertTrue(F.cross_errors([prog('a'), prog('b', 'partially_verified'), ('c', 'program_catalogs', cat)]))
        self.assertTrue(F.cross_errors([prog('a'), ('c', 'program_catalogs', cat)]))

    def test_award_program_links(self):
        F = self.F
        aw = {'institution_key': 'k', 'academic_year': '2026-27', 'award_name': 'Eng', 'program_keys': ['me-bs'], 'major_requirement': 'Engineering majors'}
        self.assertEqual(F.field_errors('awards', aw), [])
        self.assertTrue(F.field_errors('awards', {**aw, 'major_requirement': None}))
        self.assertTrue(F.field_errors('awards', {**aw, 'cip_codes': ['engineering']}))
        self.assertTrue(F.cross_errors([('a', 'awards', aw)]))


class DeepDiveEdgeTests(unittest.TestCase):
    def test_off_domain_seed_never_fetched(self):
        t = {**TARGET, 'policy': ['https://www.example.edu/undeclared', 'https://www.collegeranker.example.com/example-u']}
        with tempfile.TemporaryDirectory() as d:
            f = FakeFetcher(PAGES); C.crawl_target(t, C.Run(Path(d)), f, log=lambda *_: None)
            self.assertFalse(any('collegeranker' in u for u in f.calls))

    def test_single_pdf_catalog_is_fetched_as_catalog_pdf(self):
        # Alaska Bible College: the whole 2026-2027 catalog is one 37 MB PDF; it must use the large-file fetch, not the page fetch
        from unittest import mock
        pdf = 'https://www.example.edu/catalog-2026-2027.pdf'
        t = {**TARGET, 'catalog': {'platform': 'pdf', 'home': pdf, 'catalog_pdfs': [pdf]}, 'policy': []}
        calls = []
        def large(fetcher, url):
            calls.append(url); return {'status': 404, 'error': 'http_404'}, None
        with tempfile.TemporaryDirectory() as d, mock.patch('programs.feeds.fetch_large', large):
            f = FakeFetcher(PAGES); C.crawl_target(t, C.Run(Path(d)), f, log=lambda *_: None)
        self.assertEqual(calls, [pdf])
        self.assertNotIn(pdf, f.calls)

    def test_graduate_names_never_classified(self):
        self.assertIsNone(X.credential_of('Graduate Certificate, Associate Teacher Licensure'))
        self.assertIsNone(X.credential_of('Master of Science, Computer Science'))
        self.assertIsNone(X.credential_of('Business Administration, D.B.A.'))
        self.assertIsNone(X.credential_of('Accounting, M.B.A.'))
        self.assertEqual(X.credential_of('Liberal Arts, B.L.A.'), 'bachelor')
        self.assertEqual(X.credential_of('Associate of Science (A.S.) in Nursing'), 'associate')

    def test_overlong_text_is_not_a_sentence(self):
        page = type('P', (), {'lines': ['Students are admitted directly to the major ' + 'x' * 700]})()
        self.assertEqual(list(X.sentences(page)), [])


class ThecAdapterTests(unittest.TestCase):
    """programs/thec.py: same requests the public search page makes; responses stored with hashes; names matched exactly
    after normalisation (never fuzzily)."""
    def test_inventory_requests_and_storage(self):
        import io, json as J
        from programs import thec
        from pipeline.crawl import HostGate
        calls = []
        class Resp(io.BytesIO):
            status = 200
            def __enter__(self): return self
            def __exit__(self, *a): pass
        class Opener:
            def open(self, req, timeout=None):
                calls.append((req.get_method(), req.full_url, req.data))
                if 'GetInstitutionList' in req.full_url:
                    return Resp(J.dumps([{'institutionName': 'University of Tennessee, Knoxville', 'institutionId': '7'}]).encode())
                body = J.loads(req.data)
                assert str(body['InstitutionId']) == '7' and body['IsActiveChecked'] is True
                return Resp(J.dumps(J.dumps({'ProgramList': [{'MajorName': 'Mechanical Engineering', 'Award': 'BS', 'MajorCipCode': '14.1901'}]})).encode())
        class F:
            gate = HostGate(0); opener = Opener()
            def allowed(self, url): return True
        with tempfile.TemporaryDirectory() as d:
            run = C.Run(Path(d))
            thec.crawl(run, F(), {'utk': 'The University of Tennessee-Knoxville', 'x': 'Nowhere College'}, log=lambda *_: None)
            es = run.entries()
            inv = [e for e in es if e.get('role') == 'state_inventory']
            self.assertEqual(len(inv), 1); self.assertTrue(inv[0]['sha256'])
            self.assertIn('14.1901', run.load_page(inv[0]['page_file'])[0].text)
            self.assertTrue(any('not in THEC list' in (e.get('error') or '') for e in es))
            n = len(calls); thec.crawl(run, F(), {'utk': 'The University of Tennessee-Knoxville'}, log=lambda *_: None)
            self.assertEqual(len(calls), n)  # resumable: nothing requested twice


class SmartCatalogTests(unittest.TestCase):
    def page(self, title, crumb, tables=()):
        from pipeline import text as T
        return T.Page(f'{title}\n{crumb}\nRequirements', f'Union University - {title}', list(tables), [], [title])

    def test_policy_page_with_bachelor_in_title_is_not_a_program(self):  # Union 2026-27: admission policy page
        from programs import smartcatalog as S
        p = self.page("Admission of Students Who Already Have a Bachelor's Degree", '2026-27 Undergraduate Catalogue > Admissions > Admission of Students')
        e = {'url': 'https://uu.smartcatalogiq.com/x', 'sha256': 'a', 'fetched_at': '2026-10-05T00:00:00'}
        self.assertEqual(S.extract({'institution_key': 'k'}, e, p, '2026-27'), [])

    def test_breadcrumb_year_forms(self):
        from programs import smartcatalog as S
        for crumb, y in [('2026-2027 Bulletin > College > Computer Science B.S.', '2026-2027'),
                         ('Academic Catalog 2026-2027 > Programs > Psychology, Bachelor of Arts', '2026-2027'),
                         ('2026-27 Undergraduate Catalogue > College > Art', '2026-2027'), ('Home > Programs > Art', None)]:
            self.assertEqual(S.program_year(self.page('X, B.S.', crumb))[0], y)

    def test_required_only_when_heading_says_so(self):
        from programs import smartcatalog as S
        rows = [['CS 161', 'Intro', '4'], ['CS 162', 'Data', '4']]
        p = self.page('Computer Science B.S.', '2026-2027 Bulletin > CS > Computer Science B.S.',
                      [{'heading': 'Required Courses', 'rows': rows}, {'heading': 'Biology:', 'rows': rows}])
        e = {'url': 'https://pdx.smartcatalogiq.com/x', 'sha256': 'b', 'fetched_at': '2026-10-05T00:00:00'}
        groups = {c['record']['requirement_key']: c for c in S.extract({'institution_key': 'k'}, e, p, '2026-27') if c['domain'] == 'degree_requirements'}
        self.assertEqual(groups['required-courses']['record']['rule_details']['group_type'], 'all_required')
        self.assertEqual(groups['biology']['record']['rule_details']['group_type'], 'elective_pool')
        self.assertIn('group_type_unclear_heading', groups['biology']['issues'])


class ReviewFindingsTests(unittest.TestCase):
    """Regressions from the independent review of the first promotions (2026-10-05)."""
    def test_option_pages_are_not_programs(self):
        mk = lambda n: {'domain': 'academic_programs', 'record': {'program_name': n}}
        self.assertTrue(X.is_option_page(mk('Studio Art BFA Option')))
        self.assertFalse(X.is_option_page(mk('Art Undergraduate Major (BA, BFA, BS, HBA, HBFA, HBS)')))
        self.assertFalse(X.is_option_page(mk('Mechanical Engineering B.S.')))

    def test_smartcatalog_major_total_is_not_degree_total(self):
        from pipeline import text as T
        from programs import smartcatalog as S
        p = T.Page('Anthropology B.A./B.S.\n2026-2027 Bulletin > CLAS > Anthropology B.A./B.S.\nTotal Credit Hours: 53-54', 'PSU - Anthropology B.A./B.S.',
                   [{'heading': 'Required Courses', 'rows': [['Anth 101', 'Intro', '4']]}], [], ['Anthropology B.A./B.S.'])
        out = S.extract({'institution_key': 'k'}, {'url': 'https://x.smartcatalogiq.com/a', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}, p, '2026-27')
        self.assertNotIn('total_credits', out[0]['record'])
        self.assertFalse(any(c['record'].get('requirement_kind') == 'total_credits' for c in out))

    def test_joined_quotes_mark_the_gap(self):
        from programs.promote import _quote
        ev = {'a': {'sentence': 'One.', 'url': 'https://x', 'sha256': 'h', 'fetched_at': '2026'}, 'b': {'sentence': 'Two.', 'url': 'https://x', 'sha256': 'h', 'fetched_at': '2026'}}
        self.assertEqual(_quote(['a', 'b'], ev)[0], 'One. … Two.')


class ThecCipTests(unittest.TestCase):
    def test_federal_cip_only_when_layout_confirmed(self):
        self.assertEqual(X.federal_cip({'MajorCipCode': '09.14.1901.00', 'MajorTaxCode': '14'}), '14.1901')
        self.assertIsNone(X.federal_cip({'MajorCipCode': '09.14.1901.00', 'MajorTaxCode': '09'}))  # layout not confirmed
        self.assertIsNone(X.federal_cip({'MajorCipCode': '14.1901', 'MajorTaxCode': '09'}))

    def test_inventory_rows_bachelor_only_and_unlabeled_year(self):
        rows = [{'MajorName': 'MECHANICAL ENGINEERING', 'Award': 'BSME', 'MajorCipCode': '09.14.1901.00', 'MajorTaxCode': '14', 'CurrentProgramStatus': 'Active', 'CreditOrClockHours': '128'},
                {'MajorName': 'MECHANICAL ENGINEERING', 'Award': 'MS', 'MajorCipCode': '09.14.1901.00', 'MajorTaxCode': '14', 'CurrentProgramStatus': 'Active'},
                {'MajorName': 'NURSING', 'Award': 'C4', 'CurrentProgramStatus': 'Active'}]
        out = X.thec_candidates({'institution_key': 'utk'}, {'url': 'https://thec.example/x', 'sha256': 'z', 'fetched_at': '2026-10-05T00:00:00'}, rows, '2026-27')
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]['record']['cip_code'], '14.1901')
        self.assertEqual(out[0]['year_basis'], 'source_unlabeled')  # promotes as partially_verified, never verified


class InventoryMatchTests(unittest.TestCase):
    def test_exact_major_and_award_only(self):
        from programs import match as Mt
        rows = [{'MajorName': 'MECHANICAL ENGINEERING', 'Award': 'BSME'}, {'MajorName': 'COMPUTER SCIENCE', 'Award': 'BS'},
                {'MajorName': 'PSYCHOLOGY', 'Award': 'BA'}, {'MajorName': 'PSYCHOLOGY', 'Award': 'BA'}]
        recs = [{'program_key': 'me', 'program_name': 'Mechanical Engineering, B.S.M.E.'},
                {'program_key': 'cyber', 'program_name': 'Computer Science: Cyber Security, B.S.'},
                {'program_key': 'psy', 'program_name': 'Psychology, B.A.'},          # two identical rows: ambiguous
                {'program_key': 'me-env', 'program_name': 'Mechanical Engineering, B.S.'},  # award differs
                {'program_key': 'cs-ai', 'program_name': 'Computer Sciences, B.S.'}]        # name differs
        self.assertEqual(sorted(Mt.match(recs, rows)), ['cyber', 'me'])


class InventoryDuplicateTests(unittest.TestCase):
    def test_inventory_and_catalog_record_for_one_program_is_an_error(self):
        from backend import program_fields as F
        base = {'institution_key': 'k', 'academic_year': '2026-27', 'verification_status': 'verified'}
        thec = ('p', 'academic_programs', {**base, 'program_key': 'mechanical-engineering-bsme', 'program_name': 'MECHANICAL ENGINEERING, BSME',
                                            'program_url': 'https://thec.ppr.tn.gov/AcademicProgramInventorySearch'})
        cat = ('p', 'academic_programs', {**base, 'program_key': 'me', 'program_name': 'Mechanical Engineering, B.S.M.E.', 'program_url': 'https://catalog.x.edu/me'})
        other = ('p', 'academic_programs', {**base, 'program_key': 'cs', 'program_name': 'Computer Science, B.S.', 'program_url': 'https://catalog.x.edu/cs'})
        self.assertTrue(F.cross_errors([thec, cat]))
        self.assertEqual(F.cross_errors([thec, other]), [])


class PageQuoteTests(unittest.TestCase):
    def test_lines_must_be_printed_on_the_stored_page(self):
        from programs.promote import page_quote
        with tempfile.TemporaryDirectory() as d:
            f = FakeFetcher(PAGES); run = C.Run(Path(d)); C.crawl_target(TARGET, run, f, log=lambda *_: None)
            q, src = page_quote({'url': 'https://www.example.edu/undeclared', 'lines': ['First-year students may enter as undeclared. Students must declare a major by the time they complete 45 credit hours.']}, run)
            self.assertTrue(src['sha256'])
            with self.assertRaises(ValueError):
                page_quote({'url': 'https://www.example.edu/undeclared', 'lines': ['Students are admitted directly.']}, run)


class StaticProgramTests(unittest.TestCase):
    def test_static_catalog_page_identity(self):
        from pipeline import text as T
        e = {'url': 'https://www.georgefox.edu/catalog/undergrad/curriculum/major_minor/csci_major.html', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        p = T.Page('Bachelors (BS) in Computer Science\n2026-2027 Academic Catalog\nMajor Requirements', 'Bachelors (BS) in Computer Science', [], [], ['Bachelors (BS) in Computer Science'])
        out = X.static_program_identity({'institution_key': 'k'}, e, p, '2026-27')
        self.assertEqual(out[0]['record']['program_name'], 'Bachelors (BS) in Computer Science')
        self.assertEqual(out[0]['academic_year'], '2026-27')
        minor = T.Page('Computer Science Minor\n2026-2027 Academic Catalog', 'Computer Science Minor', [], [], ['Computer Science Minor'])
        self.assertEqual(X.static_program_identity({'institution_key': 'k'}, e, minor, '2026-27'), [])
        two_years = T.Page('Bachelors (BS) in X\n2026-2027 Academic Catalog\nsee the 2025-2026 Academic Catalog', 'Bachelors (BS) in X', [], [], ['Bachelors (BS) in X'])
        self.assertEqual(X.static_program_identity({'institution_key': 'k'}, e, two_years, '2026-27'), [])  # ambiguous year: skipped


    def test_acalog_page_without_read_groups_gives_the_program_record(self):  # Pitt Greensburg 2026-27
        from pipeline import text as T
        e = {'url': 'https://catalog.upg.pitt.edu/preview_program.php?catoid=238&poid=77211', 'role': 'program_page', 'sha256': 's', 'fetched_at': '2026-10-07T00:00:00'}
        target = {'institution_key': 'k', 'catalog': {'platform': 'acalog', 'catoid': 238}}
        p = T.Page('Search\n2026-2027 Greensburg Campus Catalog\nCommunication, BA\nCore Courses 2 courses (6 credits)',
                   'Program: Communication, BA - University of Pittsburgh Greensburg - Acalog ACMS\u2122', [], [], ['Search', 'Communication, BA'])
        out = [c for c in X._program_page_candidates(target, target, e, p, '2026-27') if c['domain'] == 'academic_programs']
        self.assertEqual([(c['extractor'], c['record']['program_name'], c['record']['catalog_year']) for c in out],
                         [('static_program/v1', 'Communication, BA', '2026-2027')])
        minor = T.Page('2026-2027 Greensburg Campus Catalog\nCommunication Minor', 'Program: Communication Minor - University of Pittsburgh Greensburg - Acalog ACMS', [], [], [])
        self.assertEqual([c for c in X._program_page_candidates(target, target, e, minor, '2026-27') if c['domain'] == 'academic_programs'], [])


class AwardInParenthesesTests(unittest.TestCase):
    def test_parenthesised_award_matches_inventory_row(self):
        from programs import match as Mt
        from backend import program_fields as F
        self.assertEqual(Mt.split_catalog_name('Accounting (B.B.A.)'), ('accounting', 'BBA'))
        base = {'institution_key': 'k', 'academic_year': '2026-27'}
        thec = ('p', 'academic_programs', {**base, 'program_key': 'a', 'program_name': 'ACCOUNTING, BBA', 'program_url': 'https://thec.ppr.tn.gov/AcademicProgramInventorySearch'})
        cat = ('p', 'academic_programs', {**base, 'program_key': 'b', 'program_name': 'Accounting (B.B.A.)', 'program_url': 'https://x.edu/c.pdf'})
        self.assertTrue(F.cross_errors([thec, cat]))


class CatalogPdfProgramsTests(unittest.TestCase):
    def test_department_program_blocks(self):
        from pipeline import text as T
        txt = '\n'.join(['Oregon Institute of Technology', '2026-2027 Catalog', 'Intro', 'Programs',
                         'Mechanical Engineering Technology/', 'Manufacturing Engineering Technology, BS', 'Mechanical Engineering, BS',
                         'Emergency Medical Technology Paramedic, AAS', 'Civil Engineering, BS/MS', 'Manufacturing Engineering Technology, MS', 'Courses',
                         'Programs', 'ACCT - Accounting Minor', 'BBA_ACCT - Accounting (B.B.A.)', 'BS_PHIL', 'BSRT_SRT - BSRT_Radiologic Technology', 'Courses'])
        e = {'url': 'https://coursedog-pdfs-public-prod.s3.us-east-2.amazonaws.com/x/catalog/a.pdf', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        names = [c['record']['program_name'] for c in X.catalog_pdf_programs({'institution_key': 'k'}, e, T.Page(txt, '', [], [], []), '2026-27')]
        self.assertEqual(names, ['Mechanical Engineering Technology/ Manufacturing Engineering Technology, BS', 'Mechanical Engineering, BS',
                                 'Accounting (B.B.A.)', 'BSRT_Radiologic Technology'])


class CourseleafPlanTests(unittest.TestCase):
    def setUp(self):  # these synthetic pages print no caption lines; footnote reading is tested in PlanFootnoteTests
        from programs import courseleaf as CL
        self._fn = CL.grid_footnotes
        CL.grid_footnotes = lambda page: [[] for _ in CL.grids(page)]

    def tearDown(self):
        from programs import courseleaf as CL
        CL.grid_footnotes = self._fn

    def grid(self, heading, caption='Degree Map'):
        return {'caption': caption, 'heading': heading, 'rows': [['First Year'], ['Fall'], ['CS 210', 'Computer Science I', '4'],
                                                                 ['', 'Credits', '4'], ['', 'Total Credits', '180']]}

    def test_degree_maps_labelled_by_bachelor_headings(self):  # UO 2026-27 prints one 'Degree Map' per award
        from pipeline import text as T
        from programs import courseleaf as CL
        e = {'url': 'https://catalog.uoregon.edu/cas/cs/', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        two = [self.grid('Bachelor of Science in Computer Science'), self.grid('Bachelor of Arts in Computer Science')]
        p = T.Page('Computer Science BA/BS', 'Computer Science BA/BS', two, [], [])
        out = [c for c in CL.extract({'institution_key': 'k'}, e, p, '2026-2027', '2026-2027 Catalog', True) if c['domain'] == 'degree_requirements']
        self.assertEqual([c['record']['requirement_key'] for c in out], ['bachelor-of-science-in-computer-science', 'bachelor-of-arts-in-computer-science'])
        self.assertTrue(all(not c['issues'] for c in out))
        same = [self.grid('Degree Map'), self.grid('Degree Map')]  # unlabelled: ambiguous, held for review
        out = [c for c in CL.extract({'institution_key': 'k'}, e, T.Page('Computer Science BA/BS', 'Computer Science BA/BS', same, [], []), '2026-2027', '', True)
               if c['domain'] == 'degree_requirements']
        self.assertTrue(all(c['issues'] == ['multiple_plan_grids'] for c in out))
        g2 = {'caption': 'Degree Map', 'heading': 'Degree Map', 'rows': [['Second Year'], ['Fall'], ['CS 313', 'Data Structures', '4'],
                                                                        ['', 'Credits', '4'], ['', 'Total Credits', '4']]}
        out = [c for c in CL.extract({'institution_key': 'k'}, e, T.Page('Computer Science BA/BS', 'Computer Science BA/BS', [self.grid('Degree Map'), g2], [], []),
                                     '2026-2027', '', True) if c['domain'] == 'degree_requirements']  # one plan printed in two grids (Texas A&M)
        self.assertEqual([(c['record']['requirement_key'], c['issues']) for c in out], [('sample-plan', [])])
        rd = out[0]['record']['rule_details']
        self.assertEqual([(t['term_index'], t['label']) for t in rd['terms']], [(1, 'First Year'), (2, 'Fall'), (3, 'Second Year'), (4, 'Fall')])
        self.assertEqual(rd['rule_text'], 'Total Credits 180 (as printed, grid 1 of 2); Total Credits 4 (as printed, grid 2 of 2)')
        txt = ('Computer Science BA/BS\nPlan of Study Grid\n| First Year\nHonors students take CS 211 in place of CS 210.\nPlan of Study Grid\n'
               '| Second Year')
        out = [c for c in CL.extract({'institution_key': 'k'}, e, T.Page(txt, 'Computer Science BA/BS', [self.grid('Degree Map'), g2], [], []),
                                     '2026-2027', '', True) if c['domain'] == 'degree_requirements']
        self.assertEqual([c['issues'] for c in out], [['grid_change_noted']])
        # headings alike for their first 80 characters (LMU 2026-27 math-placement plans) still give distinct keys and ids
        h = 'Model 4-Year Plan\u2013Bachelor of Business Administration\u2013Finance Major Curriculum\u2013Math placement MATH '
        alike = [self.grid(h + '101'), self.grid(h + '110')]
        out = [c for c in CL.extract({'institution_key': 'k'}, e, T.Page('Finance BBA', 'Finance BBA', alike, [], []), '2026-2027', '', True)
               if c['domain'] == 'degree_requirements']
        self.assertEqual(len({c['record']['requirement_key'] for c in out}), 2)
        self.assertEqual(len({c['candidate_id'] for c in out}), 2)

    def test_plan_of_a_program_read_from_the_page_whose_title_names_no_award(self):  # Texas A&M 'Agribusiness - BS'
        from pipeline import text as T
        from programs import courseleaf as CL
        e = {'url': 'https://catalog.tamu.edu/undergraduate/x/agribusiness-bs/', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}
        p = T.Page('Agribusiness - BS', 'Agribusiness - BS < Texas A&M Catalogs', [self.grid('Plan of Study Grid', 'Plan of Study Grid')], [], [])
        self.assertEqual(len(CL.extract({'institution_key': 'k'}, e, p, '2026-2027', '', True)), 1)  # the page's program record exists
        self.assertEqual(CL.extract({'institution_key': 'k'}, e, p, '2026-2027', '', False), [])  # no record and no award in the title

    def test_year_rows_subtotals_and_totals(self):  # JSU / UNI / Texas A&M / UWM 2026-27 Plan of Study Grids
        from programs import courseleaf as CL
        t = {'rows': [['Freshman'], ['Fall', 'Hour'], ['ART 111', 'Survey of Art I 1', '3'], ['Minor/Electives', '7'], ['', 'Hours', '10'],
                      ['Spring'], ['ENGL 102', 'Composition II', '3'], ['', 'Hours', '3'],
                      ['Sophomore'], ['Fall', 'Semester Credit Hours'], ['Semester 1', 'Credits'], ['HIST 201', 'US History', '3'], ['', 'Semester Credit Hours', '3'],
                      ['', 'Total Hours**', '16']]}
        terms, total = CL.parse_grid(t)
        self.assertEqual([(x['label'], x.get('credit_hours'), len(x['items'])) for x in terms],
                         [('Freshman', None, 0), ('Fall', '10', 2), ('Spring', '3', 1), ('Sophomore', None, 0), ('Fall', None, 0), ('Semester 1', '3', 1)])
        self.assertEqual((total, t['_total_label']), ('16', 'Total Hours**'))
        self.assertNotIn('Hours | 10', [i for x in terms for i in x['items']])  # the subtotal is not an item
        u = {'rows': [['Year One'], ['Semester One', 'Credits'], ['ENG 101', 'Composition', '3'], ['', 'Credits', '3'], ['Second Semester', 'Credit Hours'],
                      ['MAT 121', 'Math', '3'], ['', 'Total Credit Hours Required:', '6']]}
        terms, total = CL.parse_grid(u)
        self.assertEqual([(x['label'], x.get('credit_hours')) for x in terms], [('Year One', None), ('Semester One', '3'), ('Second Semester', None)])
        self.assertEqual(total, '6')
        w = {'caption': 'Plan of Study Grid', 'rows': [['First Semester', 'Credits'], ['ENG 101', 'Composition', '3'], ['Third Semeseter'], ['MAT 121', 'Math', '3']]}
        from pipeline import text as T
        [c] = CL.extract({'institution_key': 'k'}, {'url': 'u', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}, T.Page('Art, BA', 'Art, BA', [w], [], []), '2026-2027', '', True)
        self.assertEqual(c['issues'], ['unread_label_row'])  # a misspelled term row is held, not folded silently
        from pipeline import text as T
        e = {'url': 'https://catalog.jsu.edu/x/art-ba/', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}
        [c] = CL.extract({'institution_key': 'k'}, e, T.Page('Art, BA', 'Art, BA', [dict(t, caption='Plan of Study Grid')], [], []), '2026-2027', '', True)
        self.assertEqual((c['extractor'], c['record']['rule_details']['rule_text']), ('courseleaf_plan/v3', 'Total Hours** 16 (as printed)'))

    def test_v3_item_fields(self):  # #229 / #230: code, title and credits as separate fields
        from programs import courseleaf as CL
        P = CL.plan_item
        self.assertEqual(P(['MGMT 4010', 'Total Rewards', '3'], False), {'code': 'MGMT 4010', 'title': 'Total Rewards', 'credits': 3})
        self.assertEqual(P(['BIO SCI 102', 'How Life Works', ''], False), {'code': 'BIO SCI 102', 'title': 'How Life Works'})
        self.assertEqual(P(['MIAD CD 305', '3'], False), {'code': 'MIAD CD 305', 'credits': 3})
        self.assertEqual(P(['General Education: Natural Sciences - S', '3'], False), {'text': 'General Education: Natural Sciences - S', 'credits': 3})
        self.assertEqual(P(['Elective', '', '1.5'], False), {'text': 'Elective', 'credits': '1.5'})
        self.assertEqual(P(['!', 'ASL 19201', 'ELEMENTARY ASL I', '4'], False), {'code': 'ASL 19201', 'title': 'ELEMENTARY ASL I', 'credits': 4, 'marker': '!'})
        self.assertEqual(P(['', 'Kent Core Requirement', '3'], False), {'text': 'Kent Core Requirement', 'credits': 3})
        self.assertEqual(P(['SPAD 281or SPAD 284', 'Principles of Sport Administrationor Sport Leadership and Ethics', '3'], False),
                         {'any_of': [{'code': 'SPAD 281', 'title': 'Principles of Sport Administration'}, {'code': 'SPAD 284', 'title': 'Sport Leadership and Ethics'}], 'credits': 3})
        # rows whose cells do not say which field is which stay as printed
        for cells in (['THEA 3335', 'UIL Debate', '(3)'], ['or EGR 104', 'Engineering'], ['XXXX 1201', 'Lesson', '1'], ['Western Watershed', 'Course', ''],
                      ['PSYC 301or SOC 301', 'Statistics for Behavior Analysisor Intro Stats', '3'], ['MATH 1314', 'A', 'B', '3'], ['or General Elective', '']):
            self.assertIsNone(P(cells, False), cells)

    def test_v3_totals_term_credits_and_unplaced_credit_rows(self):  # Louisville, Kent State, NJIT, LMU 2026-27
        from programs import courseleaf as CL
        t = {'rows': [['1st Semester', 'Credits'], ['CS 101', 'Programming', '3'], ['', 'Term Credits', '3'], ['', 'Minimum Total Hours', '120']]}
        terms, total = CL.parse_grid(t)
        self.assertEqual((terms[0]['credit_hours'], len(terms[0]['items']), total, t['_total_label']), ('3', 1, '120', 'Minimum Total Hours'))
        k = {'rows': [['', 'Semester One', 'Credits'], ['', 'UC 10001', 'FLASHES 101', '1'], ['', '', 'Credit Hours', '1'], ['', '', 'Minimum Total Credit Hours:', '121']]}
        terms, total = CL.parse_grid(k)
        self.assertEqual((terms[0]['items'], terms[0]['credit_hours'], total), ([{'code': 'UC 10001', 'title': 'FLASHES 101', 'credits': 1}], '1', '121'))
        u = {'rows': [['Fall', 'Semester Hours'], ['ENGR 100', 'Intro', '3'], ['', 'Semester Hours', '3'], ['', 'Minimum Semester Hours', '30-32'],
                      ['Spring', 'Semester Hours'], ['ENGR 200', 'Design', '3'], ['', 'Semester Hours', '3'], ['', 'Minimum Semester Hours', '30-32']]}
        terms, total = CL.parse_grid(u)
        self.assertTrue(u.get('_unread_label'))  # a per-year credit row is not placed by guess
        self.assertIsNone(total)  # the last year's row is not the plan total
        v = {'rows': [['Fall', 'Semester Hours'], ['ENGR 100', 'Intro', '3'], ['', 'Semester Hours', '3'], ['', 'Minimum Semester Hours', '107-128']]}
        terms, total = CL.parse_grid(v)  # LMU: printed once, as the grid's last row: the plan total
        self.assertEqual((total, v['_total_label'], v.get('_unread_label'), terms[0]['items']), ('107-128', 'Minimum Semester Hours', None, [{'code': 'ENGR 100', 'title': 'Intro', 'credits': 3}]))

    def test_subsessions_and_spanning_subtotals(self):  # SLU, Marshall, YSU 2026-27 (#229 downgrades)
        from programs import courseleaf as CL
        t = {'rows': [['Year One'], ['Spring', 'Credits'], ['Spring 1', ''], ['CORE Requirement', '3'], ['Spring 2', ''], ['CORE Requirement', '3'], ['', 'Credits', '6'],
                      ['Summer'], ['General Elective', '3'], ['', 'Credits', '3']]}
        terms, _ = CL.parse_grid(t)
        self.assertEqual([(x['label'], x.get('credit_hours'), len(x['items'])) for x in terms],
                         [('Year One', None, 0), ('Spring', '6', 0), ('Spring 1', None, 1), ('Spring 2', None, 1), ('Summer', '3', 1)])
        self.assertFalse(t.get('_subtotal_spans'))
        m = {'rows': [['Second Semester', 'Credit Hours'], ['MI 301', 'A', '17'], ['Summer', ''], ['Statistics', '3'], ['', 'Credit Hours', '20']]}
        terms, _ = CL.parse_grid(m)
        self.assertTrue(m.get('_subtotal_spans'))
        self.assertEqual([x.get('credit_hours') for x in terms], [None, None])  # never placed on one of the two terms
        own = {'rows': [['Spring', 'Credits'], ['Full Spring Term', '3'], ['Spring 2', ''], ['CORE Requirement', '3'], ['', 'Credits', '6']]}
        CL.parse_grid(own); self.assertTrue(own.get('_subtotal_spans'))  # the parent has its own rows: not a parent of sessions
        each = {'rows': [['Fall', 'Credits'], ['Fall 1', ''], ['A 101', 'A', '3'], ['', 'Credits', '3'], ['Fall 2', ''], ['B 101', 'B', '6'], ['', 'Credits', '6']]}
        CL.parse_grid(each); self.assertTrue(each.get('_subtotal_spans'))  # sessions with their own subtotals are not placed by guess
        from pipeline import text as T
        [c] = CL.extract({'institution_key': 'k'}, {'url': 'u', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'},
                         T.Page('Medical Imaging, B.S.', 'Medical Imaging, B.S.', [dict(m, caption='Plan of Study Grid')], [], []), '2026-2027', '', True)
        self.assertIn('subtotal_spans_terms', c['issues'])
        after = {'rows': [['Fall', 'Semester Hours'], ['ENGR 100', 'Intro', '3'], ['', 'Semester Hours', '3'], ['', 'Minimum Semester Hours', '107-128'], ['* See advisor']]}
        self.assertIsNone(CL.parse_grid(after)[1])  # not the grid's last row: not read as the total
        lab = {'rows': [['Fall', 'Semester Hours'], ['ENGR 100', 'Intro', '3'], ['', 'Semester Hours', '3'], ['', 'minimum semester hours', 'TBD']]}
        self.assertIsNone(CL.parse_grid(lab)[1])
        y = {'rows': [['Year 1'], ['Fall', 'S.H.'], ['BUS 1500', 'Foundations of Business', '3'], ['', 'Semester Hours', '3']]}
        self.assertEqual([(x['label'], x.get('credit_hours'), len(x['items'])) for x in CL.parse_grid(y)[0]], [('Year 1', None, 0), ('Fall', '3', 1)])

    def test_track_plans_labelled_by_printed_heading(self):  # several grids under distinct headings
        from programs import courseleaf as CL
        from pipeline import text as T
        g = lambda h: {'caption': 'Plan of Study Grid', 'heading': h, 'rows': [['Fall', 'Credits'], ['GEOG 101', 'Intro', '3']]}
        e = {'url': 'u', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}
        out = CL.extract({'institution_key': 'k'}, e, T.Page('Geography, BA', 'Geography, BA', [g('Physical Geography'), g('Human Geography')], [], []), '2026-2027', '', True)
        self.assertEqual([(c['record']['requirement_key'], c['record']['rule_details']['source_section'], c['issues']) for c in out],
                         [('physical-geography', 'Physical Geography', ['plan_heading_label']), ('human-geography', 'Human Geography', ['plan_heading_label'])])
        same = CL.extract({'institution_key': 'k'}, e, T.Page('Geography, BA', 'Geography, BA', [g('Plan'), g('Plan')], [], []), '2026-2027', '', True)
        self.assertEqual([c['issues'] for c in same], [['multiple_plan_grids'], ['multiple_plan_grids']])

    def test_single_plan_labelled_by_printed_track(self):  # CU Boulder 2026-27 Geography BS, Classics BA
        from programs import courseleaf as CL
        from pipeline import text as T
        g = {'caption': 'Plan of Study Grid', 'heading': 'Recommended Four-Year Plan of Study', 'rows': [['Fall', 'Credits'], ['GEOG 1001', 'Intro', '3']]}
        e = {'url': 'u', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}
        def plan(text):
            [c] = CL.extract({'institution_key': 'k'}, e, T.Page(text, 'Geography - Bachelor of Science (BS)', [g], [], []), '2026-2027', '', True)
            return c['record']['rule_details']['source_section'], c['issues']
        self.assertEqual(plan('Recommended Four-Year Plan of Study\nDepending on which track students follow.\nPhysical Geography Concentration Plan\nPlan of Study Grid\n| x'),
                         ('Physical Geography Concentration Plan', ['plan_heading_label']))
        self.assertEqual(plan('Recommended Four-Year Plan of Study\nStudents fulfill Gen Ed. The below plan is for the Greek and/or Latin Language and Literature track of the major. For other plans, see the department.\nPlan of Study Grid'),
                         ('The below plan is for the Greek and/or Latin Language and Literature track of the major.', ['plan_heading_label']))
        for text in ('Recommended Four-Year Plan of Study\n| Concentration Track | 3\nPlan of Study Grid', 'Recommended Four-Year Plan of Study\nChoose a Concentration:\nPlan of Study Grid',
                     'Recommended Four-Year Plan of Study\n' + 'Concentration ' * 12 + '\nPlan of Study Grid'):
            self.assertEqual(plan(text)[1], [], text)  # a table row, a lead-in ending ':' and a long line are not labels
        g2 = dict(g, heading='Physical Geography Concentration Plan')
        [c] = CL.extract({'institution_key': 'k'}, e, T.Page('Physical Geography Concentration Plan\nPlan of Study Grid', 'Geography - Bachelor of Science (BS)', [g2], [], []), '2026-2027', '', True)
        self.assertEqual(c['issues'], [])  # the line is the grid's own heading, not a label above it
        for text in ('Recommended Four-Year Plan of Study\nPlan of Study Grid', 'Recommended Four-Year Plan of Study\n(120 credits minimum)\nPlan of Study Grid',
                     'Recommended Four-Year Plan of Study\nStudents choose a concentration.\nPlan of Study Grid'):
            self.assertEqual(plan(text), ('Sample Plan: Plan of Study Grid', []), text)

    def test_printed_term_labels_and_multiword_subjects(self):  # #229 re-extraction
        from programs import courseleaf as CL, verify as V
        for lab in ('Term 1', '1st Year', 'Year II', 'Semester III', 'Summer Session I', 'Fall I', 'J-term', 'Junior and Senior Years',
                    'Any Quarter', 'Variable', 'Autumn or Winter'):
            self.assertTrue(CL.TERM.match(lab), lab)
        for lab in ('Transfer Credits', 'Preadmission Courses', 'Term 1 and 2', 'Year 1 Term 1', 'Summer Review'):
            self.assertFalse(CL.TERM.match(lab), lab)
        self.assertTrue(V.code_in('CM\xa0CORE\xa01001 Digital Toolbox', 'CM CORE 1001'))
        self.assertTrue(V.code_in('B\xa0A\xa0324H Honors', 'B A 324H'))
        self.assertFalse(V.code_in('B A 3240 Honors', 'B A 324'))

    def test_verify_alternatives_printed_together(self):  # page text prints each alternative on its own line
        from programs import verify as V
        page = '| DSMR\xa0464\n\nor DSMR\xa0496\n| Merchandising Analytics\n\nor Senior Problem in the Fashion Industry\n| 3'
        ok = [{'code': 'DSMR 464', 'title': 'Merchandising Analytics'}, {'code': 'DSMR 496', 'title': 'Senior Problem in the Fashion Industry'}]
        self.assertTrue(V.alternatives_printed(page, ok))
        wrong = [{'code': 'DSMR 464', 'title': 'Merchandising Analytics or Seni'}, {'code': 'DSMR 496', 'title': 'Problem in the Fashion Industry'}]
        self.assertFalse(V.alternatives_printed(page, wrong))
        self.assertFalse(V.alternatives_printed(page, [{'code': 'DSMR 496'}, {'code': 'DSMR 464'}]))  # order as printed
        self.assertTrue(V.marker_printed('| !\xa0| ASL\xa019201 | ELEMENTARY ASL I | 4', '!', 'ASL 19201'))
        self.assertFalse(V.marker_printed('Courses marked (!) are critical.\n| | ASL 19201 | ELEMENTARY ASL I | 4', '!', 'ASL 19201'))

    def test_verify_checks_v3_alternatives_and_markers(self):  # Louisville 'SPAD 281or SPAD 284', Kent State '!'
        from programs import courseleaf as CL
        from programs.verify import check_candidate
        from pipeline import text as T
        g = {'caption': 'Plan of Study Grid', 'rows': [['Fall', 'Hours'], ['SPAD 281or SPAD 284', 'Principles of Sport Administrationor Sport Leadership', '3'],
                                                       ['!', 'ASL 19201', 'Elementary ASL I', '4'], ['', 'Hours', '7']]}
        page = ('Sport Administration, BS\nCatalog 2026-2027\n| Fall | Hours\n| SPAD\xa0281\n\nor SPAD\xa0284\n| Principles of Sport Administration\n\n'
                'or Sport Leadership\n| 3\n| ! | ASL\xa019201 | Elementary ASL I | 4\n| | Hours | 7')
        [c] = CL.extract({'institution_key': 'k'}, {'url': 'u', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'},
                         T.Page(page, 'Sport Administration, BS', [g], [], []), '2026-2027', '', True)
        self.assertEqual(check_candidate(c, page), [])
        bad = json.loads(json.dumps(c)); items = bad['record']['rule_details']['terms'][0]['items']
        items[0]['any_of'][1]['code'] = 'SPAD 285'; items[1]['marker'] = '#'
        self.assertEqual(sorted(check_candidate(bad, page)), ['alternatives SPAD 281 / SPAD 285 not printed as stored', 'item marker not printed'])

    def test_shared_plan_keys_and_per_area_counts(self):  # #249 review: SHSU concentrations, UNL ACE rows
        from programs import extract as X2
        mk = lambda url, rk='roadmap': {'domain': 'degree_requirements', 'institution_key': 'k', 'source': {'url': url}, 'issues': [],
                                        'record': {'program_key': 'bs-engineering-technology', 'requirement_key': rk, 'requirement_kind': 'program_plan'}}
        cands = [dict(mk('u/a'), candidate_id='1'), dict(mk('u/b'), candidate_id='2'), dict(mk('u/c', 'roadmap-2'), candidate_id='3')]
        out = X2.distinct_candidates(cands)
        self.assertEqual([c['issues'] for c in out], [['plan_key_shared_by_pages'], ['plan_key_shared_by_pages'], []])

    def test_review_followups_v3(self):  # second independent review of #241
        from programs import courseleaf as CL, verify as V
        from pipeline import text as T
        self.assertIsNone(CL.plan_item(['X 101or X 102', 'Intro (or Honors Intro)', '3'], False))  # a '(or' in the title cell
        self.assertFalse(V.marker_printed('| Important! | ASL\xa019201 | Elementary ASL I | 4', '!', 'ASL 19201'))
        page = '| MATH\xa0101\n\nor MATH\xa01025\n| Calculus\n\nor Honors Calculus\n| 4'
        self.assertFalse(V.alternatives_printed(page, [{'code': 'MATH 101', 'title': 'Calculus'}, {'code': 'MATH 102', 'title': 'Honors Calculus'}]))
        self.assertFalse(V.alternatives_printed(page, [{'code': 'MATH 101'}, {'code': 'MATH 102'}]))
        self.assertTrue(V.alternatives_printed(page, [{'code': 'MATH 101', 'title': 'Calculus'}, {'code': 'MATH 1025', 'title': 'Honors Calculus'}]))
        other = page + '\n| ENGL\xa0101\n\nor ENGL\xa0102\n| Writing\n\nor Honors Writing\n| 3'
        self.assertFalse(V.alternatives_printed(other, [{'code': 'ENGL 101', 'title': 'Calculus'}, {'code': 'ENGL 102', 'title': 'Honors Calculus'}]))
        self.assertTrue(CL.TERM.match('Spring III'))
        q = {'rows': [['Fall', 'Credits'], ['OT 101', 'Intro', '3'], ['DOCTORAL YEAR 2', ''], ['OT 801', 'Practice', '3']]}
        CL.parse_grid(q); self.assertTrue(q.get('_unread_label'))
        r = {'rows': [['Fall', 'Credits'], ['OT 101', 'Intro', '3'], ['Apply to the major in Year 2!', '']]}
        CL.parse_grid(r); self.assertFalse(r.get('_unread_label'))
        g = lambda h: {'caption': 'Plan of Study Grid', 'heading': h, 'rows': [['Fall', 'Credits'], ['GEOG 101', 'Intro', '3']]}
        e = {'url': 'u', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}
        out = CL.extract({'institution_key': 'k'}, e, T.Page('Geography, BA', 'Geography, BA', [g('School of Engineering'), g('Physical Geography')], [], []), '2026-2027', '', True)
        self.assertEqual([c['issues'] for c in out], [['multiple_plan_grids'], ['multiple_plan_grids']])

    def test_review_findings_v3(self):  # independent review of #241
        from programs import courseleaf as CL
        from pipeline import text as T
        P = CL.plan_item
        for cells in (['DSMR 464or DSMR 496', 'Merchandising Analytics or Senior Problem in the Fashion Industry', '3'],
                      ['BME 451or BMME 697', 'BME Senior Design: Product Developmentor', '3'],
                      ['MATH 122or MATH 144', 'Calculus for Business Administration and Social Sciences 4or', '4'], ['1', '3']):
            self.assertIsNone(P(cells, False), cells)
        t = {'rows': [['1st Semester', 'Credits'], ['DH 101', 'Intro', '8'], ['', 'Semester Total', '8'], ['4th Semester', 'Credits'], ['DH 401', 'Clinic', '2'], ['', 'Term Total', '2']]}
        terms, _ = CL.parse_grid(t)  # TMCC 2026-27
        self.assertEqual([(x['label'], x.get('credit_hours'), len(x['items'])) for x in terms], [('1st Semester', '8', 1), ('4th Semester', '2', 1)])
        g = lambda h: {'caption': 'Plan of Study Grid', 'heading': h, 'rows': [['Fall', 'Credits'], ['GEOG 101', 'Intro', '3']]}
        e = {'url': 'u', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}
        for heads in (['Semester Sequence', 'Physical Geography'], ['', 'Physical Geography'], ['2026-2027 Edition', 'Plan Requirements']):
            out = CL.extract({'institution_key': 'k'}, e, T.Page('Geography, BA', 'Geography, BA', [g(h) for h in heads], [], []), '2026-2027', '', True)
            self.assertEqual([c['issues'] for c in out], [['multiple_plan_grids'], ['multiple_plan_grids']], heads)

    def test_printed_choice_block_is_one_item(self):  # EKU, LMU, Temple 2026-27: 'Select one of the following: | 3' and blank-credit options
        from programs import courseleaf as CL
        rows = [['Fall', 'Hours'], ['ENG 101', 'Comp', '3'], ['Select one of the following:', '3'], ['ANTH 376', 'Quant', ''], ['BIOL 350', 'Biostat', ''],
                ['MATH 101', 'Algebra', '3'], ['Choose two courses from the following:', '6'], ['ART 101', 'A', ''], ['ART 102', 'B', ''], ['ART 103', 'C', ''],
                ['', 'Hours', '15']]
        items = CL.parse_grid({'rows': rows})[0][0]['items']
        self.assertEqual(items[1], {'choose': 1, 'text': 'Select one of the following:', 'credits': 3,
                                    'options': [{'code': 'ANTH 376', 'title': 'Quant'}, {'code': 'BIOL 350', 'title': 'Biostat'}]})
        self.assertEqual(items[2], {'code': 'MATH 101', 'title': 'Algebra', 'credits': 3})  # a row with credits ends the block
        self.assertEqual((items[3]['choose'], len(items[3]['options'])), (2, 3))
        # a printed label before the instruction and footnote marks after it are kept in the text (JSU, Texas A&M, Temple)
        for hdr in ('Jax MIX Experience: select one of the following: 1', 'Select one of the following: 2,3'):
            items = CL.parse_grid({'rows': [['Fall', 'Hours'], [hdr, '3'], ['PSY 201', 'A', ''], ['SY 221', 'B', ''], ['', 'Hours', '3']]})[0][0]['items']
            self.assertEqual((items[0]['choose'], items[0]['text']), (1, hdr))
        for hdr in ('Select one of the following courses 12', 'Note: select one of the following and more', 'select one of the following: 123',
                    'students who have not completed MATH 142 or an equivalent course in their first year at another school: select one of the following:'):
            self.assertIsNone(CL.CHOICE_HEADER.match(hdr), hdr)
        # not grouped: a header without credits, options with their own credits, one option, a count not below the options
        for hdr, opts in ((['Select one of the following:', ''], [['ANTH 376', 'Q', ''], ['BIOL 350', 'B', '']]),
                          (['Select one of the following:', '3'], [['ANTH 376', 'Q', '3'], ['BIOL 350', 'B', '3']]),
                          (['Select one of the following:', '3'], [['ANTH 376', 'Q', '']]),
                          (['Select two of the following:', '6'], [['ANTH 376', 'Q', ''], ['BIOL 350', 'B', '']]),
                          (['Select one elective:', '3'], [['ANTH 376', 'Q', ''], ['BIOL 350', 'B', '']])):
            items = CL.parse_grid({'rows': [['Fall', 'Hours'], hdr, *opts, ['', 'Hours', '3']]})[0][0]['items']
            self.assertFalse(any(isinstance(i, dict) and 'choose' in i for i in items), hdr)
            self.assertEqual(len(items), 1 + len(opts))
        # options printed as cross-listed or paired codes are options too; a text row among them leaves the block flat,
        # never cut short (#plan-choices review: Texas A&M 'ANSC 326/FSTC 326', NCSU 'GEP Humanities')
        rows = [['Fall', 'Hours'], ['Select one of the following:', '3'], ['ANSC 101', 'A', ''], ['ANSC 326/FSTC 326', 'B', ''],
                ['GEOL 101& GEOL 102', 'C', ''], ['MATH 101', 'Algebra', '3'], ['', 'Hours', '6']]
        items = CL.parse_grid({'rows': rows})[0][0]['items']
        self.assertEqual(len(items[0]['options']), 3)
        rows = [['Fall', 'Hours'], ['Select one of the following:', '3'], ['ANSC 101', 'A', ''], ['ANSC 102', 'B', ''], ['GEP Humanities', ''],
                ['MATH 101', 'Algebra', '3'], ['', 'Hours', '6']]
        items = CL.parse_grid({'rows': rows})[0][0]['items']
        self.assertEqual((len(items), any(isinstance(i, dict) and 'choose' in i for i in items)), (5, False))
        rows = [['Fall', 'Hours'], ['Select one of the following:', '3'], ['ANSC 101', 'A', ''], ['ANSC 102', 'B', ''], ['Elective', 'Any', '3'],
                ['', 'Hours', '6']]
        items = CL.parse_grid({'rows': rows})[0][0]['items']  # a printed row with credits, kept as a string, ends the block
        self.assertEqual((len(items[0]['options']), items[1]), (2, 'Elective | Any | 3'))

    def test_verify_reads_choice_options(self):
        from programs import verify as V
        c = {'candidate_id': 'x', 'domain': 'degree_requirements', 'extractor': 'courseleaf_plan/v3', 'evidence': [], 'source': {'url': 'u'},
             'record': {'program_key': 'p', 'requirement_key': 'sample-plan', 'rule_details': {'terms': [{'label': 'Fall', 'items': [
                 {'choose': 1, 'text': 'Select one of the following:', 'credits': 3, 'options': [{'code': 'ANTH 376', 'title': 'Quant'}, {'code': 'BIOL 350', 'title': 'Biostat'}]}]}]}}}
        text = 'Fall\nSelect one of the following: 3\nANTH 376 Quant\nBIOL 350 Biostat\nUndergraduate Catalog 2026-2027'
        self.assertEqual(V.check_candidate(c, text), [])
        self.assertIn('course BIOL 350 not in source', V.check_candidate(c, text.replace('BIOL 350', 'BIOL 351')))

    def test_plan_printed_as_continued_grids(self):  # Texas A&M Biology BA, JSU, Temple 2026-27: one plan in two grids
        from programs import courseleaf as CL
        g1 = {'heading': 'Biology - BA', 'rows': [['First Year'], ['Fall', 'Semester Credit Hours'], ['BIOL 111', 'Intro', '4'], ['', 'Semester Credit Hours', '4'],
                                                  ['Second Year'], ['Fall', 'Semester Credit Hours'], ['BIOL 213', 'Genetics', '4'], ['', 'Semester Credit Hours', '4'],
                                                  ['', 'Total Semester Credit Hours', '8']]}
        g2 = {'heading': 'Biology - BA', 'rows': [['Third Year'], ['Fall', 'Semester Credit Hours'], ['BIOL 351', 'Micro', '4'], ['', 'Semester Credit Hours', '4'],
                                                  ['', 'Total Semester Credit Hours', '4']]}
        p = [CL.parse_grid(dict(g1)), CL.parse_grid(dict(g2))]
        self.assertTrue(CL.continued_grids(p, ['Biology - BA', 'Biology - BA']))
        self.assertFalse(CL.continued_grids(p, ['Biology - BA', 'Zoology - BS']))
        self.assertFalse(CL.continued_grids(p[::-1], ['Biology - BA', 'Biology - BA']))  # years must run from the first, in order
        self.assertFalse(CL.continued_grids([p[0], p[0]], ['Biology - BA', 'Biology - BA']))  # a repeated year is another plan
        self.assertFalse(CL.continued_grids([p[0], p[0]], ['', '']))
        p3 = CL.parse_grid(dict(g2, rows=[['Fourth Year']] + g2['rows'][1:]))  # 'Third Year' | 'Fourth Year': no first year printed
        self.assertFalse(CL.continued_grids([p[1], p3], ['Biology - BA', 'Biology - BA']))
        # a note between the grids that changes the plan holds it (Texas A&M Business, Temple)
        note = 'Plan of Study Grid\n| First Year\nFinance: Students intending to major in Finance must add FINC 210 to freshman year.\nPlan of Study Grid\n| Third Year'
        self.assertTrue(CL.grid_change_noted(type('P', (), {'text': note})()))
        plain = 'Plan of Study Grid\n| First Year\nUpper-Level Program (Year 3 & 4)\nPlan of Study Grid\n| Third Year'
        self.assertFalse(CL.grid_change_noted(type('P', (), {'text': plain})()))
        self.assertTrue(CL.grid_change_noted(type('P', (), {'text': plain.replace('Upper-Level', 'Option to take ARCH 2123 instead of ARCH 2121. Upper-Level')})()))

    def test_decimal_course_credits_kept_as_printed(self):  # West Chester B.M. 2026-27: '1.5', '0.5'
        from programs import courseleaf as CL
        t = {'rows': [['Semester One', 'Credits'], ['MUS 101', 'Theory I', '1.5'], ['MUE 100', 'Ensemble', '0.5'], ['MUS 102', 'Lab', '1-1.5'],
                      ['ENG 101', 'Composition', '3'], ['', 'Credits', '6.5']]}
        terms, _ = CL.parse_grid(t)
        self.assertEqual([i.get('credits') for i in terms[0]['items']], ['1.5', '0.5', '1-1.5', 3])
        self.assertEqual(terms[0]['credit_hours'], '6.5')
        # a credit cell that is not a plain number keeps the row as printed (#229 recovery review: EKU, UIC, Montana)
        t = {'rows': [['Semester One', 'Credits'], ['CED 200', 'Clinical II', '.5'], ['HIST 419', 'Civics', '3 or 4'], ['THTR 103', 'House', '1 (0)'],
                      ['ENG 101', 'Composition', '3']]}
        terms, _ = CL.parse_grid(t)
        self.assertEqual(terms[0]['items'][:3], ['CED 200 | Clinical II | .5', 'HIST 419 | Civics | 3 or 4', 'THTR 103 | House | 1 (0)'])
        self.assertEqual(terms[0]['items'][3], {'code': 'ENG 101', 'title': 'Composition', 'credits': 3})

    def test_course_titled_total_and_unknown_term_header(self):  # #238 review: UNO HRM, EKU EHS; UMT 'Autumn | Hours'
        from programs import courseleaf as CL
        t = {'rows': [['Fall', 'Hours'], ['MGMT 4010', 'Total Rewards', '3'], ['EHS 340', 'Total Worker Health Principles', '3'], ['', 'Hours', '6']]}
        terms, total = CL.parse_grid(t)
        self.assertEqual((terms[0]['items'], terms[0]['credit_hours'], total),
                         ([{'code': 'MGMT 4010', 'title': 'Total Rewards', 'credits': 3}, {'code': 'EHS 340', 'title': 'Total Worker Health Principles', 'credits': 3}], '6', None))
        self.assertEqual(CL.parse_grid({'rows': [['Fall', 'Hours'], ['MGMT 4010', 'Total Rewards', '3'], ['Total Hours', '3']]})[1], '3')
        for head in (['Summer Review', 'Credit Hours'], ['1st Semester/Term', 'Credits']):
            u = {'rows': [['Fall', 'Hours'], ['ENG 101', 'Composition', '3'], head, ['MAT 121', 'Math', '3']]}
            CL.parse_grid(u)
            self.assertTrue(u.get('_unread_label'), head)
        a = {'rows': [['First Year'], ['Autumn', 'Hours'], ['ENG 101', 'Composition', '3'], ['', 'Hours', '3']]}
        self.assertEqual([(x['label'], x.get('credit_hours')) for x in CL.parse_grid(a)[0]], [('First Year', None), ('Autumn', '3')])
        self.assertFalse(a.get('_unread_label'))
        for rule in ('Select 6 SH from the following', 'Select 6 hrs of the following', 'Select 6 cr of the following'):
            self.assertIsNone(CL.COUNT.match(rule), rule)

    def test_hour_choices_and_placeholder_codes(self):  # SHSU 2026-27 Course Lists (#228 review)
        from programs import courseleaf as CL
        for rule in ('Select 5 hours of the following', 'Select six hours of the following:', 'Select 6 SCH from the following',
                     'Select 18 hours of Minor courses', 'Select 12 units from the following:'):
            self.assertIsNone(CL.COUNT.match(rule), rule)
            self.assertIsNotNone(CL.CREDITS.match(rule), rule)
        for rule in ('Select two BIOL courses', 'Select one of the following:', 'Choose 2 courses from the following', 'Select one Fine Arts course'):
            self.assertIsNotNone(CL.COUNT.match(rule), rule)
        self.assertEqual([bool(CL.CODE_CELL.match(c)) for c in ('XXXX 1201', 'XXXX1201', 'MUEN XXXX', 'BIOL 101', 'XBIO 1201')],
                         [False, False, False, True, True])

    def test_term_header_row_with_milestones_column(self):  # UO 2026-27: 'Fall | Milestones | Credits'
        from programs import courseleaf as CL
        t = {'rows': [['First Year'], ['Fall', 'Milestones', 'Credits'], ['JPN 101', 'First-Year Japanese', '', '4'], ['', 'Credits', '', '16'],
                      ['Winter'], ['WR 122Z', 'Composition II', '', '4']]}
        self.assertEqual([(x['label'], len(x['items'])) for x in CL.parse_grid(t)[0]], [('First Year', 0), ('Fall', 1), ('Winter', 1)])
        self.assertEqual(CL.parse_grid(t)[0][1]['credit_hours'], '16')


class StatedMajorTests(unittest.TestCase):
    def test_award_stated_in_a_sentence(self):  # Linfield 2026-27 'Accounting Major'
        from pipeline import text as T
        e = {'url': 'https://catalog.linfield.edu/programs-az/business/accounting-major/index.html', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        txt = ('Accounting Major\nCatalog 2026-2027\nDegree Requirements\nThis major is available as a bachelor of arts or bachelor of science degree, '
               'as defined in the section on degree requirements for all majors in this catalog.\nPDF of the entire 2025-2026 Catalog')
        tgt = {'catalog': {'platform': 'courseleaf'}}
        out = X.program_page_candidates(tgt, {'institution_key': 'k'}, e, T.Page(txt, 'Accounting Major < Linfield University', [], [], []), '2026-27')
        self.assertEqual([(c['record']['program_name'], c['record']['credential_level'], c['record']['catalog_year']) for c in out],
                         [('Accounting Major', 'bachelor', '2026-2027')])
        none = txt.replace('This major is available as a bachelor of arts or bachelor of science degree', 'This major is great')
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, T.Page(none, 'Accounting Major < Linfield University', [], [], []), '2026-27'), [])
        minor = T.Page(txt, 'Accounting Minor for Students not Earning a Business Major < Linfield University', [], [], [])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, minor, '2026-27'), [])

    def test_department_page_named_by_its_list_line(self):  # UO 2026-27 'Cinema Studies' department page
        from pipeline import text as T
        from programs import verify as V
        url = 'https://catalog.uoregon.edu/arts-sciences/humanities/cinema-studies/'
        e = {'url': url, 'sha256': 'page', 'fetched_at': '2026-10-05T00:00:00'}
        listed = {'name': 'Cinema Studies', 'printed': 'Cinema Studies: BA, BS', 'url': url, 'credential_level': 'bachelor',
                  'listed_on': 'https://catalog.uoregon.edu/ug-programs/', 'listed_on_sha256': 'list'}
        txt = 'Cinema Studies\nCinema Studies Major Requirements\nBachelor of Arts in Cinema Studies\n2026-2027 Catalog'
        heads = ['Cinema Studies', 'Cinema Studies Major Requirements', 'Bachelor of Arts in Cinema Studies']
        tgt = {'catalog': {'platform': 'courseleaf'}, '_listed': {url: listed}}
        page = T.Page(txt, 'Cinema Studies | University of Oregon Academic Catalog', [], [], heads)
        out = X.program_page_candidates(tgt, {'institution_key': 'k'}, e, page, '2026-27')
        self.assertEqual([(c['record']['program_name'], c['record']['credential_level'], c['extractor']) for c in out],
                         [('Cinema Studies: BA, BS', 'bachelor', 'department_major/v1')])
        lists = {'list': 'Undergraduate Majors\nCinema Studies: BA, BS\n2026-2027 Catalog'}
        self.assertEqual(V.check_candidate(out[0], txt, lists.get), [])
        self.assertEqual(V.check_candidate(out[0], txt, {'list': 'Cinema Studies'}.get), ['program_name not verbatim on its list page'])
        self.assertEqual(V.check_candidate(out[0], txt.replace('Cinema Studies Major Requirements', ''), lists.get), ['program page heading not printed'])
        # several majors on one department page: no single '<Name> Major Requirements' heading, no record
        multi = T.Page(txt, 't', [], [], ['Cinema Studies', "Majors - Bachelor's Degree"])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, multi, '2026-27'), [])
        # the list must print the award; a bare anchor is not credential evidence
        # (the page's own degree heading is still read, by department_section/v1)
        bare = {**tgt, '_listed': {url: {**listed, 'printed': 'Cinema Studies'}}}
        got = X.program_page_candidates(bare, {'institution_key': 'k'}, e, page, '2026-27')
        self.assertEqual([(c['extractor'], c['record']['program_name']) for c in got], [('department_section/v1', 'Bachelor of Arts in Cinema Studies')])
        minor = {**tgt, '_listed': {url: {**listed, 'credential_level': None}}}
        self.assertEqual([c['extractor'] for c in X.program_page_candidates(minor, {'institution_key': 'k'}, e, page, '2026-27')], ['department_section/v1'])

    def test_archive_pdf_link_is_not_a_year_label(self):
        from pipeline import text as T
        p = T.Page('Catalog 2026-2027\nPDF of the entire 2025-2026 Catalog\nDownload PDF of the entire 2024-2025 Bulletin', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(p)}, {'2026-2027'})
        # Oklahoma State 2026-27: the edition header and the print link to last year's full PDF catalog
        osu = T.Page('2026-2027 Edition\nFull 2025-2026 Catalog\nZoology, BS', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(osu)}, {'2026-2027'})
        utsa = T.Page('2026-28 Undergraduate Catalog\n2024-2026 Undergraduate Catalog PDF\nDepartment of Computer Science', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(utsa)}, {'2026-2028'})
        # undotted awards are case-sensitive and never a course code: 'Plan B Set of Courses', 'Bes Program', 'BHS 1150' are not awards
        for n in ('Plan B Set of Courses', 'Bes Program', 'BHS 1150', 'BPS 4395 Senior Seminar'):
            self.assertIsNone(X.credential_of(n), n)
        # undotted awards in program names (OSU 'Marketing, BSBA', 'Chemical Engineering, BSCH'; Missouri 'BSAcc in Accountancy')
        for n in ('Marketing, BSBA', 'Chemical Engineering, BSCH', 'Civil Engineering, BSCV', 'Health Care Administration, BPS', 'BSAcc in Accountancy', 'BHS in Health Science'):
            self.assertEqual(X.credential_of(n), 'bachelor', n)
        # undotted awards on program lists (OSU, Missouri, UTEP); a graduate award, a minor or an all-caps name is not one
        for lab in ('Marketing, BSBA', 'Chemical Engineering, BSCH', 'University Studies, BUS', 'BJ*', 'BSAcc', 'Computer Engineering, BSBachelorsUndergraduateEngineering'):
            self.assertEqual(X.list_award(lab, lab), 'bachelor', lab)
        for lab in ('Accounting, MS', 'Accounting (ACCT), Minor', 'BIOLOGY', 'Business, Graduate Certificate', 'Bioinformatics BIOL'):
            self.assertIsNone(X.list_award(lab, lab), lab)
        # VCU 2026-27: another link's text is not this link's printed line; UO's 'Accounting: BA, BS' still is
        vcu = T.Page('Nursing, B.S.\nNursing, B.S., R.N.-B.S. completion program', 't', [], [('u1', 'Nursing, B.S.'), ('u2', 'Nursing, B.S., R.N.-B.S. completion program')], [])
        self.assertIsNone(X.printed_line(vcu, 'Nursing, B.S.'))
        self.assertEqual(X.printed_line(T.Page('Accounting: BA, BS', 't', [], [('u', 'Accounting')], []), 'Accounting'), 'Accounting: BA, BS')
        # the skip never runs on to an unrelated later line (SF State 'Accounting (ACCT)' department link)
        sf = T.Page('Accounting (ACCT)\nAccounting: Bachelor\'s Concentration, Minor', 't', [], [('u1', 'Accounting'), ('u2', 'Accounting (ACCT)')], [])
        self.assertIsNone(X.printed_line(sf, 'Accounting'))
        # the header rule needs a catalog name and a short institution line: a body line after 'Note 12' is not a label
        self.assertEqual(X.printed_catalog_years(T.Page('Policy\nUndergraduate Catalog\nAdopted in fall of the year 12\n2025-2026', 't', [], [], [])), set())
        self.assertEqual(X.printed_catalog_years(T.Page('Policy\nStudent Handbook\nBYU\n2025-2026', 't', [], [], [])), set())
        # BYU and Utah 2026-27 site headers: catalog name, institution short name, year (Utah: 'Home (AY 2026-2027)')
        byu = T.Page('Skip to Main Content\nUndergraduate Catalog\nBYU\n2026-2027\nMyMAP\nAccounting (BS)', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(byu)}, {'2026-2027'})
        utah = T.Page('Skip to Main Content\nThe University of Utah\nGeneral Catalog\nUniversity of Utah\nHome (AY 2026-2027)\nArchitectural Studies', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(utah)}, {'2026-2027'})
        # a year in the body after a short line is not a header label
        body = T.Page('\n'.join(['x'] * 20 + ['Undergraduate Catalog', 'Note', '2025-2026']), 't', [], [], [])
        self.assertEqual(X.printed_catalog_years(body), set())
        # BYU 2026-27 program page: '<code> Program | BYU Catalog', the title heading before 'Download as PDF'
        e2 = {'url': 'https://catalog.byu.edu/programs/34636', 'sha256': 'ab' * 32, 'fetched_at': '2026-10-08T00:00:00+00:00', 'kind': 'html'}
        kp = lambda name, title='554924 Program | BYU Catalog': X.kuali_page_identity({'institution_key': 'k'}, e2, T.Page(
            'Undergraduate Catalog\nBYU\n2026-2027\n' + name + '\nDownload as PDF', title, [], [], ['BYU', name, 'Download as PDF', 'Minimum Credit Hours']), '2026-27')
        [c] = kp('Applied English Linguistics (BA)')
        self.assertEqual((c['record']['program_name'], c['record']['catalog_year'], c['extractor']), ('Applied English Linguistics (BA)', '2026-2027', 'kuali_page/v1'))
        self.assertEqual(kp('Applied English Linguistics (MA)'), [])  # not a bachelor's award
        self.assertEqual(kp('Applied English Linguistics (BA)', title='Applied English Linguistics | BYU'), [])  # another template
        self.assertEqual(kp('General Education and Bachelor Degree Requirements'), [])  # Utah: a policy page
        self.assertEqual(kp('Spanish Studies (Secondary Major) (BA)'), [])  # not earned on its own
        self.assertEqual(kp('Art Education K-12 (BA) *')[0]['record']['program_name'], 'Art Education K-12 (BA)')  # list footnote marker
        two = X.kuali_page_identity({'institution_key': 'k'}, e2, T.Page('Undergraduate Catalog\nBYU\n2026-2027\n2025-2026 Catalog\nArt (BA)', '1 Program | BYU Catalog', [], [],
                                                                          ['BYU', 'Art (BA)', 'Download as PDF']), '2026-27')
        self.assertEqual(two, [])  # two year labels: none
        self.assertEqual(X.kuali_page_identity({'institution_key': 'k'}, e2, T.Page('Undergraduate Catalog\nBYU\n2026-2027', '1 Program | BYU Catalog', [], [],
                                                                              ['Download as PDF', 'Art (BA)']), '2026-27'), [])  # no title heading before it
        # Colorado State 2026-27: the Programs A-Z degree column links 'Major in Anthropology' as 'B.A.'
        lst = lambda printed: {'credential_level': 'bachelor', 'printed': printed, 'listed_on': 'https://c.edu/programsaz/', 'listed_on_sha256': 'cd' * 32}
        e3 = {'url': 'https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/anthropology-geography/anthropology-major/', 'sha256': 'ab' * 32, 'fetched_at': '2026-10-08T00:00:00+00:00', 'kind': 'html'}
        csu = lambda head, printed='B.A.', text='2026-2027 Catalog': X.award_link_major_identity({'institution_key': 'k'}, e3, T.Page(text + '\n' + head, 't', [], [], [head]), '2026-27', lst(printed))
        [c] = csu('Major in Anthropology')
        self.assertEqual((c['record']['program_name'], c['extractor'], [x['value'] for x in c['evidence'] if x['field'] == 'award']), ('Major in Anthropology', 'award_link_major/v1', ['B.A.']))
        self.assertEqual(csu('Major in Political Science, Public Policy and Service Concentration'), [])  # an option page
        self.assertEqual(csu('Major in Anthropology', printed='B.A. Concentration'), [])  # a concentration row
        self.assertEqual(csu('Anthropology'), [])  # not a 'Major in' page
        self.assertEqual(csu('Major in Anthropology', text='2026-2027 Catalog\n2025-2026 Catalog'), [])  # two labels
        self.assertEqual(csu('Major in Anthropology', printed='M.A.'), [])  # not a bachelor's award
        # UT Dallas 2026-27: pages print only the edition name; the edition home page's label is quoted from that page
        ed = {'year': '2026-2027', 'line': '2026-2027 Undergraduate Catalog', 'url': 'https://catalog.utdallas.edu/2026/undergraduate/home/', 'sha256': 'ef' * 32}
        tgt4 = {'institution_key': 'k', 'catalog': {'platform': 'courseleaf'}, '_edition_year': ed}
        e4 = {'url': 'https://catalog.utdallas.edu/2026/undergraduate/programs/aht/animation-and-games', 'sha256': 'ab' * 32, 'fetched_at': '2026-10-08T00:00:00+00:00', 'kind': 'html'}
        utd = lambda title, heads, t=tgt4: X.program_page_candidates(t, {'institution_key': 'k'}, e4, T.Page('Program text', title, [], [], heads), '2026-27')
        [c] = utd('Animation & Games (BA) - UT Dallas 2026 Undergraduate Catalog - UTD', ['School of Arts', 'Animation and Games (BA)'])
        self.assertEqual((c['record']['program_name'], c['record']['catalog_year'], c['extractor']), ('Animation and Games (BA)', '2026-2027', 'edition_program/v1'))
        self.assertEqual([x['source_url'] for x in c['evidence'] if x['field'] == 'catalog_year'], [ed['url']])
        self.assertEqual(utd('Animation & Games (BA) - UT Dallas 2025 Undergraduate Catalog - UTD', ['School of Arts', 'Animation and Games (BA)']), [])  # another edition
        self.assertEqual(utd('Animation & Games (BA) - UT Dallas 2026 Undergraduate Catalog - UTD', ['School of Arts', 'Animation and Games (BA)'],
                             {k: v for k, v in tgt4.items() if k != '_edition_year'}), [])  # not configured
        self.assertEqual(utd('Animation & Games Minor - UT Dallas 2026 Undergraduate Catalog', ['School of Arts', 'Animation and Games Minor']), [])
        self.assertEqual(utd('Animation & Games (BA) - UT Dallas 2026 Undergraduate Catalog', ['School of Arts', 'Animation and Games (BA) Concentration in Games']), [])  # an option
        other = {**tgt4, '_edition_year': {**ed, 'url': 'https://catalog.utdallas.edu/2026/graduate/home/'}}
        self.assertEqual(utd('Animation & Games (BA) - UT Dallas 2026 Undergraduate Catalog - UTD', ['School of Arts', 'Animation and Games (BA)'], other), [])  # another edition directory
        # a page that prints its own year label never takes the home page's
        own = X.program_page_candidates(tgt4, {'institution_key': 'k'}, e4, T.Page('2025-2026 Edition\n2024-2025 Edition', 'Animation & Games (BA) - UT Dallas 2026 Undergraduate Catalog', [], [], ['School', 'Animation and Games (BA)']), '2026-27')
        self.assertEqual(own, [])  # labels of its own (here two): never the home page's
        # edition_home_year: the home page's single printed label, else None
        class Run:
            def __init__(self, text): self.text = text
            def load_page(self, f): return T.Page(self.text, 't', [], [], []), {}
        he = [{'role': 'catalog_home', 'page_file': 'x', 'url': ed['url'], 'sha256': 'ef' * 32}]
        self.assertEqual(X.edition_home_year(Run('2026-2027 Undergraduate Catalog'), he)['year'], '2026-2027')
        self.assertIsNone(X.edition_home_year(Run('2026-2027 Undergraduate Catalog\n2025-2026 Undergraduate Catalog'), he))
        # Biola 2026-27: a PDF link that is the page's only label names the current catalog
        biola = T.Page('2026-2027 Catalog PDF\nBiology, B.S.', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(biola)}, {'2026-2027'})
        self.assertEqual({y for y, _ in X.printed_catalog_years(T.Page('Full 2026-2027 Catalog\nZoology, BS', 't', [], [], []))}, {'2026-2027'})
        self.assertEqual({y for y, _ in X.printed_catalog_years(T.Page('Full 2026-2027 Catalog of courses and programs\n2025-2026 Catalog PDF', 't', [], [], []))}, {'2026-2027'})
        # only the whole line is a print link: a sentence naming the full catalog still carries its label
        self.assertEqual({y for y, _ in X.printed_catalog_years(T.Page('Full 2026-2027 Catalog of courses and programs', 't', [], [], []))}, {'2026-2027'})

    def test_stetson_edition_header_and_coming_soon_pdf_slot(self):
        from pipeline import text as T
        # Stetson 2026-27: '2026-2027 Edition' heads the page; the print menu offers a not-yet-posted PDF of last year's catalog
        p = T.Page('2026-2027 Edition\nBachelor of Science in Biology\nDownload Page (PDF)\n2025-2026 Academic Catalog\nComing Soon!!!', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(p)}, {'2026-2027'})
        q = T.Page('2025-2026 Academic Catalog\nBachelor of Science in Biology', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(q)}, {'2025-2026'})  # a label in use still counts


    def test_campus_catalog_year_label(self):
        from pipeline import text as T
        # Pitt Johnstown 2026-27: the Acalog header names the campus between the year and 'Catalog'
        p = T.Page('2026-2027 Johnstown Campus Catalog\nAccounting, BS', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(p)}, {'2026-2027'})
        q = T.Page('2026-2027 Campus Life and Catalog of Events\nAccounting, BS', 't', [], [], [])
        self.assertEqual(X.printed_catalog_years(q), set())

    def test_print_menu_catalog_pdf_is_not_the_page_label(self):  # UNO 2026-27 print options: '2025-2026 Catalog' / 'A PDF of ...'
        from pipeline import text as T
        p = T.Page('2026-2027 Edition\nEnglish, Bachelor of Arts\nDownload Page (PDF)\n2025-2026 Catalog\nA PDF of the 2025-2026 catalog.\nCancel', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(p)}, {'2026-2027'})
        q = T.Page('2025-2026 Catalog\nEnglish, Bachelor of Arts', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(q)}, {'2025-2026'})

    def test_header_name_and_year_on_two_lines(self):  # UW-Madison 2026-27 site header: 'Guide' / '2026-2027'
        from pipeline import text as T
        p = T.Page('Archive\nGuide\n2026-2027\nSearch this site\nAnthropology, BA\n© 2026-2027 Board of Regents', 't', [], [], [])
        self.assertEqual(X.printed_catalog_years(p), {('2026-2027', 'Guide 2026-2027')})
        for text in ('Archive\n2026-2027\nAnthropology, BA', 'Course Guide Notes\n2026-2027\nX', 'Guide\n2026-2029\nX', '© 2026-2027 Board of Regents'):
            self.assertEqual(X.printed_catalog_years(T.Page(text, 't', [], [], [])), set(), text)

class MajorTableTests(unittest.TestCase):
    def test_marked_majors_with_catalog_award_statement(self):  # Lewis & Clark 2026-27
        from pipeline import text as T
        table = {'caption': 'Majors and Minors', 'rows': [['Major', 'Minor', 'Discipline'], ['', '', 'Anthropology, see Sociology and Anthropology'],
                                                          ['X', '', 'Art (Studio)'], ['', 'X', 'Chinese'], ['X', 'X', 'Chemistry'], ['X', '', 'Student-Designed Major']]}
        pages = {'t': T.Page('2026-27 Edition\nMajors and Minors', 'Majors', [table], [], []),
                 'a': T.Page('Undergraduate work at Lewis & Clark leads to the bachelor of arts degree.', 'Requirements', [], [], [])}
        class R:
            def load_page(self, f): return pages[f], None
        tu, au = 'https://docs.lclark.edu/undergraduate/policiesprocedures/majorsminors/', 'https://docs.lclark.edu/undergraduate/graduationrequirements/requirements/'
        es = [{'url': tu, 'page_file': 't', 'sha256': 's1', 'fetched_at': '2026-10-05T00:00:00'}, {'url': au, 'page_file': 'a', 'sha256': 's2', 'fetched_at': '2026-10-05T00:00:00'}]
        tgt = {'catalog': {'major_table': tu, 'award_statement': {'url': au, 'quote': 'Undergraduate work at Lewis & Clark leads to the bachelor of arts degree'}}}
        out = X.major_table_candidates(tgt, {'institution_key': 'k'}, R(), es, '2026-27')
        self.assertEqual([(c['record']['program_name'], c['record']['catalog_year']) for c in out], [('Art (Studio)', '2026-2027'), ('Chemistry', '2026-2027')])
        tgt['catalog']['award_statement']['quote'] = 'Undergraduate work leads to the bachelor of science degree'  # not printed: nothing
        self.assertEqual(X.major_table_candidates(tgt, {'institution_key': 'k'}, R(), es, '2026-27'), [])


class ListedLocationTests(unittest.TestCase):
    def test_campus_tagged_rows_only(self):  # OSU catalog Programs page, OSU-Cascades tag
        from pipeline import text as T
        lu = 'https://catalog.oregonstate.edu/programs/'
        listed = {'programs': [
            {'printed': 'Biology Undergraduate Major (BS, HBS)MajorCollege of ScienceUndergraduateCorvallisOSU-CascadesBS, HBS', 'credential_level': 'bachelor', 'url': 'https://catalog.oregonstate.edu/x/biology-bs-hbs/', 'listed_on': lu},
            {'printed': 'Chemistry Undergraduate Major (BS, HBS)MajorCollege of ScienceUndergraduateCorvallisBS, HBS', 'credential_level': 'bachelor', 'url': 'https://catalog.oregonstate.edu/x/chem/', 'listed_on': lu},
            {'printed': 'Visual Studies BFA OptionOptionCollege of Liberal ArtsUndergraduateOSU-Cascades', 'credential_level': 'bachelor', 'url': 'https://catalog.oregonstate.edu/x/vs/', 'listed_on': lu}]}
        class R:
            def load_page(self, f): return T.Page('Programs\n2026-2027 Catalog', 'Programs', [], [], []), None
        es = [{'url': lu, 'page_file': 'p', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}]
        out = X.listed_location_candidates({'catalog': {'list_filter': 'OSU-Cascades'}}, {'institution_key': 'k'}, R(), es, listed, '2026-27')
        self.assertEqual([(c['record']['program_name'], c['record']['program_url'][-16:]) for c in out], [('Biology Undergraduate Major (BS, HBS)', '/biology-bs-hbs/')])


class PrintedListTests(unittest.TestCase):
    def test_degree_lines_under_heading(self):  # UP Bulletin 2026-2027 "Undergraduate Programs"
        from pipeline import text as T
        lu = 'https://up.smartcatalogiq.com/en/2026-2027/bulletin/university-academic-programs-of-study/undergraduate-programs'
        txt = '\n'.join(['Bulletin 2026-2027 > University Academic Programs of Study > Undergraduate Programs', 'Undergraduate Programs', 'Minor Programs',
                         'Undergraduate Programs', 'Biology, B.S., B.A.', 'Economics, B.A.', 'Mathematics, Applied, B.S.', '*Pre-law study', 'Economics, B.B.A.',
                         'B.B.A./M.B.A. Program for Accounting Majors', 'Post Baccalaureate Professional Computer Science Degree, Prof-B.C.S.', 'Up one level', 'Art, B.A.'])
        links = [('https://up.example/econ-ba', 'Economics'), ('https://up.example/econ-bba', 'Economics'), ('https://up.example/bio', 'Biology')]
        page = T.Page(txt, 'University of Portland - Undergraduate Programs', [], links, [])
        class R:
            def load_page(self, f): return page, None
        es = [{'url': lu, 'page_file': 'p', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}]
        tgt = {'catalog': {'printed_list': {'url': lu, 'heading': 'Undergraduate Programs', 'stop': 'Up one level'}}}
        out = X.printed_list_candidates(tgt, {'institution_key': 'k'}, R(), es, '2026-27')
        self.assertEqual([(c['record']['program_name'], c['record']['program_url'][-8:], c['record']['catalog_year']) for c in out],
                         [('Biology, B.S., B.A.', 'mple/bio', '2026-2027'), ('Economics, B.A.', 'graduate-programs'[-8:], '2026-2027'),
                          ('Mathematics, Applied, B.S.', 'programs', '2026-2027'), ('Economics, B.B.A.', 'programs', '2026-2027')])


class CoursedogPageTests(unittest.TestCase):
    def test_rendered_program_page_with_catalog_year_statement(self):  # Willamette 2026-27
        from pipeline import text as T
        home = T.Page('Information in this catalog applies to the 2026–2027 academic year and is accurate to the best of our knowledge.', 'Catalog', [], [], [])
        prog = T.Page('Home/\nPrograms/\nBiology (BA)\nBiology (BA)\nDownload as PDF\nDegree\nBachelor of Arts (BA)\nCopyright © 2026-2027 Willamette University', 'BA.BIOL Program', [], [], [])
        class R:
            def load_page(self, f): return {'h': home, 'p': prog}[f], None
        es = [{'url': 'https://catalog.willamette.edu/', 'role': 'catalog_home', 'page_file': 'h', 'sha256': 's'}]
        cy = X.coursedog_year(R(), es)
        self.assertEqual(cy['year'], '2026-2027')
        e = {'url': 'https://catalog.willamette.edu/programs/BA.BIOL', 'sha256': 't', 'fetched_at': '2026-10-05T00:00:00'}
        out = X.coursedog_page_identity({'institution_key': 'k'}, e, prog, '2026-27', cy)
        self.assertEqual([(c['record']['program_name'], c['record']['catalog_year']) for c in out], [('Biology (BA)', '2026-2027')])
        self.assertEqual(X.coursedog_page_identity({'institution_key': 'k'}, e, prog, '2026-27', None), [])  # no year statement, no record
        law = T.Page(prog.text.replace('Biology (BA)', 'Law (JD)').replace('Bachelor of Arts (BA)', 'Juris Doctor'), 'Law', [], [], [])
        self.assertEqual(X.coursedog_page_identity({'institution_key': 'k'}, e, law, '2026-27', cy), [])

    def test_api_rows_use_the_printed_long_name(self):  # FAU 2026-27: no catalogDisplayName, short internal name
        from pipeline import text as T
        rows = {'data': [{'name': 'BA in Lang, Ling and Comparative Lit (LLCP)', 'longName': 'Bachelor of Arts in Languages, Linguistics and Comparative Literature',
                          'level': 'UG', 'status': 'Active', 'programGroupId': 'g1'},
                         {'catalogDisplayName': 'Biology (BS)', 'name': 'BS Bio', 'longName': 'Bachelor of Science in Biology', 'level': 'UG', 'programGroupId': 'g2'}]}
        page = T.Page(json.dumps(rows), 'api', [], [], [])
        e = {'url': 'https://app.coursedog.com/api/v1/x/programs', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}
        out = X.coursedog_candidates({'catalog': {'home': 'https://catalog.fau.edu'}}, {'institution_key': 'k'}, e, page, (None, None, None), '2026-27')
        self.assertEqual([(c['record']['program_key'], c['record']['program_name']) for c in out],
                         [('ba-in-lang-ling-and-comparative-lit-llcp', 'Bachelor of Arts in Languages, Linguistics and Comparative Literature'),
                          ('biology-bs', 'Biology (BS)')])

    def test_milestones_column_kept_apart(self):  # UO 2026-27 Accounting / Business Administration / Music
        from programs import courseleaf as CL
        long = 'SPAN 3xx Hispanic Cultures through Literature or SPAN 3xx ' + 'Creative Writing in Spanish ' * 12
        t = {'rows': [['Fall', 'Milestones', 'Credits'], ['ACTG 450', 'Advanced Financial Accounting', 'Attend Meet the Firms', '4'],
                      ['Upper-division business elective courses', 'Register for commencement', '8'], ['', '', '2'], [long, '', '4'], ['', 'Credits', '', '18']]}
        items = CL.parse_grid(t)[0][0]['items']
        self.assertEqual(items[0], {'code': 'ACTG 450', 'title': 'Advanced Financial Accounting', 'credits': 4, 'milestone': 'Attend Meet the Firms'})
        self.assertEqual(items[1], {'text': 'Upper-division business elective courses', 'credits': 8, 'milestone': 'Register for commencement'})
        self.assertEqual(items[2], {'text': '', 'credits': 2})
        self.assertEqual(items[3], {'text': long.strip(), 'credits': 4})  # never cut (a text row with a blank milestone cell)


class DottedProgramCodeTests(unittest.TestCase):
    def test_dotted_codes_and_parenthesised_awards(self):  # Carson-Newman 2026-2027 Coursedog catalog PDF
        from pipeline import text as T
        txt = '\n'.join(['Carson-Newman University', '2026-2027 Catalog', 'Programs', 'BIOL.BS - Biology (BS)', 'BIOL.GENRL.BA - Biology-General (BA)',
                         'BIOL.RSRCH.BA - Biology-Research Emphasis (BA)', 'ACCT.MINOR - Accounting Minor', 'CHEM.TCHSC.BA - BA in Chemistry - Teacher Licensure',
                         'MGED.SCI.BA - Middle Grades Educ-Teacher Licen. 6-8: Science Emph', 'CPS.BH.CERT - Certificate in Behavioral Health (Cert)', 'NURS.BSN - Nursing (BSN)', 'Courses'])
        e = {'url': 'https://coursedog-pdfs-public-prod.s3.us-east-2.amazonaws.com/cn/catalog/a.pdf', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        names = [c['record']['program_name'] for c in X.catalog_pdf_programs({'institution_key': 'k'}, e, T.Page(txt, '', [], [], []), '2026-27')]
        self.assertEqual(names, ['Biology (BS)', 'Biology-General (BA)', 'BA in Chemistry - Teacher Licensure', 'Nursing (BSN)'])


class CoursedogFeedTests(unittest.TestCase):
    def test_home_year_and_state_layout_cip(self):  # Tennessee Tech 2026-27
        from pipeline import text as T
        home = T.Page('Home\n\n2026-2027\nUndergraduate Catalog\n\nTennessee Tech University', 'Catalog', [], [], [])
        class R:
            def load_page(self, f): return home, None
        y = X.coursedog_home_year(R(), [{'role': 'catalog_home', 'page_file': 'h', 'url': 'https://undergrad.catalog.tntech.edu/'}])
        self.assertEqual(y[:2], ('2026-2027', '2026-2027 Undergraduate Catalog'))
        self.assertEqual(X.coursedog_cip('520301'), '52.0301')
        self.assertEqual(X.coursedog_cip('52.0201 - Management'), '52.0201')
        self.assertIsNone(X.coursedog_cip('3252030100'))  # state inventory layout: not a federal CIP as printed

class CourseListGroupTests(unittest.TestCase):
    def groups(self, rows, heading='X Major Requirements'):
        from programs import courseleaf as CL
        return CL.course_list_groups({'caption': 'Course List', 'heading': heading, 'rows': [['Code', 'Title', 'Credits']] + rows})

    def test_required_run_then_select_with_blank_credit_options(self):  # OSU Accountancy 2026-27
        g = self.groups([['ACTG 427', 'ASSURANCE AND ATTESTATION SERVICES', '4'], ['MATH 241', 'Calculus I', '4'], ['or MATH 251Z', 'Differential Calculus'],
                         ['Major Courses', ''], ['Select two courses from the following:', '8'], ['ACTG 417', 'ADVANCED ACCOUNTING', ''], ['ACTG 420', 'IT AUDITING', ''],
                         ['ACTG 490', 'CAPSTONE', '4'], ['Select a minimum of 9 credits from the following:', '9'], ['AG 311', 'X', ''], ['FW 340', 'Y', '']])
        self.assertEqual([(s, x['group_type'], len(x['courses']), x.get('choose_count'), x.get('choose_credits'), sorted(x['issues'])) for s, x in g],
                         [('X Major Requirements', 'all_required', 2, None, None, []), ('Major Courses', 'choose_courses', 2, 2, None, []),
                          ('Major Courses', 'all_required', 1, None, None, []), ('Major Courses', 'choose_credits', 2, None, 9, [])])
        self.assertEqual(g[0][1]['courses'][1], {'any_of': [{'code': 'MATH 241', 'title': 'Calculus I', 'credits': 4}, {'code': 'MATH 251Z', 'title': 'Differential Calculus'}]})

    def test_row_led_by_a_zero_width_space_is_held(self):  # UW-Madison prints U+200B inside joined code cells
        g = self.groups([['BIOL 101', 'A', '3'], ['\u200bAGROECOL 370 & GENETICS 528', 'B', '3']])
        self.assertIn('complex_course_row', g[0][1]['issues'])

    def test_unrepresentable_rows_are_held(self):
        g = self.groups([['PH 211& PH 212', 'PHYSICS', '8'], ['Select one of the following math pairs:', '4-7'], ['MTH 251Z& MTH 252Z', 'CALCULUS', '8'],
                         ['Select an additional 7 credits from courses that count toward either major.', '7'], ['Capstone', ''], ['ANTH 209', 'Business Anthropology', '4'],
                         ['Select from the list below:', ''], ['BA 252', 'Global Perspectives', ''],
                         ['Select 4 credits from the following:', '4'], ['BA 361', 'Communication', '4'],  # an option or a required course? held
                         ['Select 2 credits from the following courses:', '2'], ['Internships', '']])  # the list is not read: held
        self.assertEqual([(x['group_type'], sorted(x['issues'])) for _, x in g],
                         [('all_required', ['complex_course_row', 'joined_courses_row']),
                          ('choose_courses', ['complex_course_row', 'joined_courses_row', 'options_not_read', 'options_print_credits']),
                          ('elective_pool', []), ('all_required', []), ('choose_unclear', ['choose_number_not_printed']), ('choose_credits', ['options_print_credits']),
                          ('choose_credits', ['options_not_read'])])
        self.assertEqual(g[2][1]['course_rules'], ['Select an additional 7 credits from courses that count toward either major. 7'])
        g = self.groups([['H 301', 'X', '3']], heading='Recommended Public Health Elective Coursework')
        self.assertEqual(sorted(g[0][1]['issues']), ['heading_not_all_required'])


class CourseListHtmlTests(unittest.TestCase):
    def test_row_classes_and_leading_indent(self):
        from programs.courselist_html import course_lists
        html = ('<h2>Major Requirements</h2><p>Students must select one focus area.</p><table class="sc_courselist"><caption>Course List</caption><tbody>'
                '<tr class="even areaheader"><td colspan="2"><span class="courselistcomment areaheader">Core</span></td><td></td></tr>'
                '<tr class="odd"><td><a>ENGR 110</a><span class="blockindent">&amp; <a>ENGR 115</a></span></td><td>X</td><td>3</td></tr>'
                '<tr class="even orclass"><td><div style="margin-left:20px;" class="blockindent">or <a>ENGR 310</a></div></td><td>Y</td><td></td></tr>'
                '<tr class="even"><td><div style="margin-left:20px;" class="blockindent"><a>ACTG 417</a></div></td><td>ADV</td><td></td></tr></tbody></table>')
        t = course_lists(html)[0]
        self.assertEqual((t['heading'], t['context'], t['caption']), ('Major Requirements', 'Students must select one focus area.', 'Course List'))
        self.assertEqual([(r['classes'], r['cells'][0]['text'], r['cells'][0]['indent']) for r in t['rows']],
                         [(['even', 'areaheader'], 'Core', False), (['odd'], 'ENGR 110& ENGR 115', False), (['even', 'orclass'], 'or ENGR 310', True), (['even'], 'ACTG 417', True)])


class CourseListLayoutGroupTests(unittest.TestCase):
    TR = '<tr class="{c}"><td{span}>{a}</td>{rest}</tr>'

    def test_per_area_counts_and_rule_hours(self):  # #249 review: UNL 2026-27
        from programs import courseleaf as CL
        g = CL.html_groups(self.table([('rule', 'Select one course each from ACE outcomes 5, 7, and 9', '', '9'), ('opt', 'ANTH 110', 'A'), ('opt', 'HIST 100', 'B')]))
        self.assertIn('count_per_area', g[0][1]['issues'])
        g = CL.html_groups(self.table([('rule', 'Select 48 hours of Electives/Minor', '', '45'), ('opt', 'ANTH 110', 'A')]))
        self.assertIn('rule_credits_differ_from_hours', g[0][1]['issues'])
        g = CL.html_groups(self.table([('rule', 'Select 6 hours of the following', '', '6'), ('opt', 'ANTH 110', 'A'), ('opt', 'HIST 100', 'B')]))
        self.assertFalse({'count_per_area', 'rule_credits_differ_from_hours'} & g[0][1]['issues'])

    def table(self, rows, heading='Major Requirements', context=''):
        from programs.courselist_html import course_lists
        def row(kind, text, title='', cr=''):
            if kind == 'head': return f'<tr class="even areaheader"><td colspan="2"><span class="courselistcomment areaheader">{text}</span></td><td>{cr}</td></tr>'
            if kind == 'sub': return f'<tr class="odd areasubheader"><td colspan="2"><span class="courselistcomment areasubheader">{text}</span></td><td>{cr}</td></tr>'
            if kind == 'rule': return f'<tr class="odd"><td colspan="2"><span class="courselistcomment">{text}</span></td><td>{cr}</td></tr>'
            if kind == 'irule': return f'<tr class="odd"><td colspan="2"><div style="margin-left:20px;"><span class="courselistcomment">{text}</span></div></td><td>{cr}</td></tr>'
            if kind == 'opt': return f'<tr class="even"><td><div style="margin-left:20px;" class="blockindent"><a>{text}</a></div></td><td>{title}</td><td>{cr}</td></tr>'
            if kind == 'or': return f'<tr class="even orclass"><td><div style="margin-left:20px;">or <a>{text}</a></div></td><td>{title}</td><td></td></tr>'
            return f'<tr class="odd"><td><a>{text}</a></td><td>{title}</td><td>{cr}</td></tr>'
        html = f'<h2>{heading}</h2><p>{context}</p><table class="sc_courselist"><caption>Course List</caption><tbody>' + ''.join(row(*r) for r in rows) + '</tbody></table>'
        return course_lists(html)[0]

    def test_required_choice_and_alternatives(self):
        from programs import courseleaf as CL
        t = self.table([('head', 'Core'), ('c', 'CS 161', 'Intro I', '4'), ('c', 'MTH 251Z', 'Calculus', '4'), ('or', 'MTH 251H', 'Calculus Honors'),
                        ('rule', 'Select two courses from the following:', '', '8'), ('opt', 'CS 450', 'Graphics'), ('opt', 'CS 475', 'Parallel'), ('opt', 'CS 480', 'Translators'),
                        ('rule', 'One of the following:'), ('opt', 'CS 330', 'X'), ('opt', 'CS 420', 'Y'), ('c', 'CS 499', 'Capstone', '4')])
        g = CL.html_groups(t)
        self.assertEqual([(s, x['type'], len(x['courses']), x.get('choose_count'), sorted(x['issues'])) for s, x in g],
                         [('Core', 'all_required', 2, None, []), ('Core', 'choose_courses', 3, 2, []), ('Core', 'choose_courses', 2, 1, []), ('Core', 'all_required', 1, None, [])])
        self.assertEqual(g[0][1]['courses'][1]['any_of'][1]['code'], 'MTH 251H')

    def test_verify_reads_printed_code_shapes(self):
        from programs.verify import code_in
        self.assertTrue(code_in('| IT222 | Cloud |', 'IT222'))
        self.assertTrue(code_in('| ENG/FILM 366 | Narrative Film |', 'ENG/FILM 366'))
        self.assertTrue(code_in('| DANC 1100R | Ballet |', 'DANC 1100R'))
        self.assertFalse(code_in('| IT227 | Cloud |', 'IT222'))
        self.assertFalse(code_in('| FILM 366 |', 'ENG/FILM 366'))
        self.assertTrue(code_in('| 100/200 Level | Mathematics |', '100/200 Level'))  # a code cell that is not SUBJ NUM
        self.assertFalse(code_in('| 300/400 Level |', '100/200 Level'))

    def test_printed_code_shapes_issue_95(self):
        """Issue #95 recovery: codes as the catalogs print them are courses, not 'complex' rows that cut a list apart."""
        from programs import courseleaf as CL
        # Purdue Global prints no space; UVU and TAMUSA print four digits and a suffix letter
        g = CL.html_groups(self.table([('c', 'IT222', 'Cloud', '5'), ('rule', 'Select one of the following:', '', '5'), ('opt', 'IN250', 'Python'), ('opt', 'IN251', 'C#'),
                                       ('c', 'DANC 1100R', 'Ballet', '1'), ('c', 'ENGL 1302', 'Composition II', '3')]))
        self.assertEqual([(x['type'], [c['code'] for c in x['courses']], sorted(x['issues'])) for _, x in g],
                         [('all_required', ['IT222'], []), ('choose_courses', ['IN250', 'IN251'], []), ('all_required', ['DANC 1100R', 'ENGL 1302'], [])])
        # WKU cross-listed courses stay inside the list, kept as printed
        g = CL.html_groups(self.table([('rule', 'Select two of the following:', '', '6'), ('opt', 'FILM 367', 'Genres'), ('opt', 'ENG/FILM 366', 'Narrative Film'),
                                       ('opt', 'ENG/FILM 466', 'Film Theory'), ('opt', 'BCOM 481', 'Problems')]))
        self.assertEqual([(x['type'], x.get('choose_count'), [c['code'] for c in x['courses']], sorted(x['issues'])) for _, x in g],
                         [('choose_courses', 2, ['FILM 367', 'ENG/FILM 366', 'ENG/FILM 466', 'BCOM 481'], [])])
        # a lecture/lab pair and joined courses are held with a reason naming the shape
        g = CL.html_groups(self.table([('rule', 'Select 4 hours from the following:', '', '4'), ('opt', 'BIOL 1306/1106', 'Biology'), ('opt', 'CHEM 1311/1111', 'Chemistry')]))
        self.assertTrue({'complex_course_row', 'lecture_lab_pair_code'} <= g[0][1]['issues'])
        g = CL.html_groups(self.table([('c', 'HIST 2700& HIST 2710', 'US History', '6')]))
        self.assertTrue({'complex_course_row', 'joined_courses_row'} <= g[0][1]['issues'])
        # 'Students must take an additional N credit hours from the following list' is a printed choice of credits
        g = CL.html_groups(self.table([('rule', 'Students must take an additional 15 credit hours from the following list of classes:', '', '15'),
                                       ('opt', 'FILM 367', 'A'), ('opt', 'FILM 399', 'B'), ('opt', 'FILM 469', 'C'), ('opt', 'ENG 309', 'D'), ('opt', 'ENG 365', 'E'), ('opt', 'PS 303', 'F')]))
        self.assertEqual([(x['type'], x.get('choose_credits'), len(x['courses']), sorted(x['issues'])) for _, x in g], [('choose_credits', 15, 6, [])])
        # 'Complete the following:' prints an all-required list (UVU), indented or not
        g = CL.html_groups(self.table([('rule', 'Complete the following:'), ('c', 'DANC 2110', 'Orientation', '3'), ('c', 'DANC 1610R', 'Conditioning', '1'),
                                       ('rule', 'Complete the following courses:'), ('opt', 'DANC 2700R', 'Social Dance II'), ('opt', 'DANC 2710R', 'Ballroom II')]))
        self.assertEqual([(x['type'], [c['code'] for c in x['courses']], sorted(x['issues'])) for _, x in g],
                         [('all_required', ['DANC 2110', 'DANC 1610R'], []), ('all_required', ['DANC 2700R', 'DANC 2710R'], [])])
        # a credit number printed as a word (WKU Theatre)
        g = CL.html_groups(self.table([('rule', 'Take a total of at least two credit hours from the following:', '', '2'), ('opt', 'PERF 321', 'A'), ('opt', 'PERF 420', 'B'), ('opt', 'PERF 340', 'C')]))
        self.assertEqual([(x['type'], x.get('choose_credits'), sorted(x['issues'])) for _, x in g], [('choose_credits', 2, [])])
        # an alternative printed in the new shapes joins the previous course
        g = CL.html_groups(self.table([('c', 'MAT 1030', 'QR', '3'), ('or', 'MAT 1035', 'QR with Algebra')]))
        self.assertEqual(g[0][1]['courses'][0]['any_of'][1]['code'], 'MAT 1035')

    def test_reference_track_and_unclear_tables_are_held(self):
        from programs import courseleaf as CL
        g = CL.html_groups(self.table([('c', 'EC 401', 'Research', '1-16')], heading='Courses Offered Pass/No Pass Only'))
        self.assertIn('reference_or_track_heading', g[0][1]['issues'])
        g = CL.html_groups(self.table([('c', 'ED 150', 'X', '3')], heading='ESOL', context='Students must select one or more focus areas or substitute with a minor.'))
        self.assertIn('context_says_choose_among_tables', g[0][1]['issues'])
        g = CL.html_groups(self.table([('rule', 'Select six NMC courses (can include up to three of the following):', '', '24'), ('opt', 'ART 101', 'A'), ('opt', 'ART 102', 'B')]))
        self.assertTrue({'count_not_below_options', 'rule_mixes_other_courses'} <= g[0][1]['issues'])
        g = CL.html_groups(self.table([('rule', 'Select 6-8 credits from the following:', '', '6-8'), ('opt', 'PSY 401', 'A'), ('irule', 'Any other PSY course')]))
        self.assertTrue({'credit_range', 'text_option'} <= g[0][1]['issues'])
        g = CL.html_groups(self.table([('c', 'GD 101', 'Design', '4')], heading='Bachelor of Fine Arts'), program_awards=3)
        self.assertIn('award_specific_table', g[0][1]['issues'])


class AwardHeadingTests(unittest.TestCase):
    def test_programs_under_award_headings(self):  # Eastern Oregon 2026-27 college pages
        from pipeline import text as T
        txt = '\n'.join(['2026-2027 Academic Catalog', 'Select a Catalog', '2026-2027 Academic Catalog', '2025-2026 Academic Catalog [NOT CURRENT CATALOGS]',
                         'Art', 'Programs', 'Bachelor of Arts/Bachelor of Science', '•', 'Art Major', '•', 'Anthropology/Sociology w/Anthropology Concentration',
                         'Bachelor of Applied Science', '•', 'Business Major [BAS]', 'Minor', '•', 'Art Minor', 'Four Year Plan(s)', '•', 'Art Typical Four Year Curriculum'])
        links = [('https://catalog.eou.edu/preview_program.php?catoid=8&poid=1846', 'Art Major'), ('https://catalog.eou.edu/preview_program.php?catoid=8&poid=1990', 'Business Major [BAS]'),
                 ('https://catalog.eou.edu/preview_program.php?catoid=8&poid=1850', 'Art Minor')]
        e = {'url': 'https://catalog.eou.edu/content.php?catoid=8&navoid=466', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        out = X.award_heading_candidates({'institution_key': 'k'}, e, T.Page(txt, 'College', [], links, []), '2026-27')
        self.assertEqual([(c['record']['program_name'], c['record']['catalog_year'], c['record']['program_url'][-4:]) for c in out],
                         [('Art Major', '2026-2027', '1846'), ('Business Major [BAS]', '2026-2027', '1990')])


class AcalogPlanTests(unittest.TestCase):
    def test_four_year_curriculum_and_college_page_link(self):  # Eastern Oregon 2026-27
        from pipeline import text as T
        college = T.Page('\n'.join(['2026-2027 Academic Catalog', 'Art', 'Go to information for Art.', 'Programs', 'Bachelor of Arts/Bachelor of Science', '•', 'Art Major',
                                    'Minor', '•', 'Art Minor', 'Four Year Plan(s)', '•', 'Art Typical Four Year Curriculum', 'Theatre', 'Go to information for Theatre.']),
                         'College', [], [('https://catalog.eou.edu/preview_program.php?catoid=8&poid=1847', 'Art Typical Four Year Curriculum')], [])
        links = X.college_plan_links(college)
        self.assertEqual(links, {'https://catalog.eou.edu/preview_program.php?catoid=8&poid=1847': 'Art Major'})
        txt = '\n'.join(['2026-2027 Academic Catalog', '2025-2026 Academic Catalog [NOT CURRENT CATALOGS]', 'Art Typical Four Year Curriculum', 'TYPICAL FIRST YEAR CURRICULUM',
                         'Fall', 'ART 101 Foundations of Visual Literacy*AEH (4)', 'General Education and non-art Elective Courses (12)', 'Winter', 'ART 121 Design II*APC (4)',
                         'Spring', 'SOC 204Z Introduction to Sociology*SSC (4) OR SOC 206Z Social Problems*SSC (4)', 'TYPICAL SECOND YEAR CURRICULUM', 'Fall', 'ART 230 Drawing II (4)',
                         'Note: courses may be taken in either order.', 'Back to Top'])
        e = {'url': 'https://catalog.eou.edu/preview_program.php?catoid=8&poid=1847', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        c = X.acalog_plan({'institution_key': 'k'}, e, T.Page(txt, 'Program: Art Typical Four Year Curriculum', [], [], []), 'Art Major', '2026-27')[0]
        rd = c['record']['rule_details']
        self.assertEqual((c['record']['program_key'], rd['catalog_year'], len(rd['terms'])), ('art-major', '2026-2027', 4))
        self.assertEqual(rd['terms'][0]['label'], 'TYPICAL FIRST YEAR CURRICULUM — Fall')
        self.assertEqual(rd['terms'][0]['items'][0], {'code': 'ART 101', 'title': 'Foundations of Visual Literacy*AEH', 'credits': 4})
        self.assertIsInstance(rd['terms'][2]['items'][0], str)  # an 'X OR Y' line stays printed text
        self.assertEqual(rd['course_rules'], ['Note: courses may be taken in either order.'])


class CourseListLayoutReviewTests(unittest.TestCase):
    table = CourseListLayoutGroupTests.table

    def test_second_review_rules(self):
        from programs import courseleaf as CL
        # an unindented course list right after a rule row whose options were not indented
        g = CL.html_groups(self.table([('rule', 'One of the following:'), ('c', 'CS 330', 'X', '4'), ('c', 'CS 420', 'Y', '4')]))
        self.assertIn('follows_rule_without_options', g[-1][1]['issues'])
        # options continue after an unindented text row
        g = CL.html_groups(self.table([('rule', 'Select two courses from the following:', '', '8'), ('opt', 'ENSC 101', 'A'), ('opt', 'ENSC 102', 'B'),
                                       ('rule', 'Alternative Approved Courses:'), ('opt', 'GEO 101', 'C')]))
        self.assertTrue(any('choice_continues_after_text' in x['issues'] or 'choose_number_not_printed' in x['issues'] for _, x in g))
        # a sub-heading inside an open choice holds the choice and what follows until the next heading
        rows = [('rule', 'Select one group:', '', '8'), ('opt', 'MB 302', 'A'), ('opt', 'MB 303', 'B'), ('c', 'MB 999', 'Z', '1')]
        t = self.table(rows); t['rows'].insert(2, {'classes': ['odd', 'areasubheader'], 'cells': [{'text': 'Group 2', 'indent': False, 'spans': ['courselistcomment', 'areasubheader'], 'colspan': 2}]})
        g = CL.html_groups(t)
        self.assertIn('subheading_inside_choice', g[0][1]['issues'])
        # open-ended rules
        g = CL.html_groups(self.table([('rule', 'Select one course from the following or another experience with advisor approval:', '', '3'), ('opt', 'X 101', 'A'), ('opt', 'X 102', 'B')]))
        self.assertIn('rule_mixes_other_courses', g[0][1]['issues'])

    def test_table_level_holds(self):
        from programs import courseleaf as CL
        main = self.table([('c', 'CLAS 101', 'A', '4')], heading='Classics Major Requirements')
        greek = self.table([('c', 'GRK 301', 'B', '4')], heading='Classics (Greek) Major Requirements')
        latin = self.table([('c', 'LAT 301', 'C', '4')], heading='Classics (Latin) Major Requirements')
        ref = self.table([('c', 'ENVS 411', 'D', '4')], heading='Upper-Division Natural Science Courses')
        e = {'url': 'https://catalog.uoregon.edu/x/', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        out = CL.html_candidates({'institution_key': 'k'}, e, {'url': 'https://catalog.uoregon.edu/x/#courselist'}, [main, greek, latin, ref], '2026-2027', 'classics-ba', 1)
        self.assertEqual([sorted(c['issues']) for c in out], [[], ['parallel_tables'], ['parallel_tables'], ['secondary_table']])
        tracks = self.table([('c', 'J 101', 'E', '4')], heading='Major Requirements', context='Students choose one track from the following.')
        out = CL.html_candidates({'institution_key': 'k'}, e, {'url': 'u'}, [tracks], '2026-2027', 'media', 1)
        self.assertIn('context_says_choose_among_tables', out[0]['issues'])
        # UWM 2026-27: the general education paragraph is not a choice among the tables after it
        ger = self.table([('c', 'ENGL 102', 'Writing', '3')], heading='General Education Requirements (GER)',
                         context='They provide a broad body of knowledge as a context for specialization.')
        major = self.table([('c', 'ARTH 101', 'Ancient Art', '3')], heading='Major Requirements')
        out = CL.html_candidates({'institution_key': 'k'}, e, {'url': 'u'}, [major, ger, self.table([('c', 'ART 101', 'Drawing', '3')], heading='Major Requirements')], '2026-2027', 'art', 1)
        self.assertEqual([sorted(c['issues']) for c in out], [[], ['secondary_table'], []])
        for code, ok in (('AGROECOL 101', True), ('F&W ECOL 248', True), ('I&C SCI 31', False), ('CURRINS 301', True), ('BUS ADM 201', True),
                         ('OR BIL 412', False), ('MINOR IN 300', False), ('GRADES 101', False), ('HOURS AT 300', False), ('AND CHEM 101', False)):
            self.assertEqual(bool(CL.CODE_CELL.match(code)), ok, code)
        # a long-subject row that is not one code is held, never dropped (UWM 'CURRINS/EXCEDUC 612', UNI 'ENGLISH 3772/5772')
        g = CL.html_groups(self.table([('c', 'CURRINS 301', 'Teaching', '3'), ('c', 'CURRINS/EXCEDUC 612', 'Cross-listed', '3')], heading='Major Requirements'))
        self.assertEqual([c['code'] for c in g[0][1]['courses']], ['CURRINS 301', 'CURRINS/EXCEDUC 612'])  # one cross-listed course, as printed
        for row in ('ENGLISH 3772/5772', 'PHYSICS 111A- 111B', 'AGROECOL\u200b/ENTOM 101'):
            g = CL.html_groups(self.table([('c', 'CURRINS 301', 'Teaching', '3'), ('c', row, 'Joined', '3')], heading='Major Requirements'))
            self.assertIn('complex_course_row', g[0][1]['issues'], row)
        for text in ('Complete one course from:', 'Choose one course from the following:', 'Select One:', 'A student needs to take one of the following courses'):
            self.assertTrue(CL.CONTEXT_PICK.search(text), text)
        for text in ('A baccalaureate degree requires a minimum of 120 total hours to graduate.', 'Students must complete 40 courses in total.',
                     'Students must earn a minimum of C- in each course.', 'Majors must take three courses: CAS 140, CAS 141, CAS 142.', 'Majors must take 120 credits.'):
            self.assertFalse(CL.CONTEXT_PICK.search(text), text)
        for code in ('AT 310', 'OR 541', 'F&W ECOL 448'):
            self.assertTrue(CL.CODE_CELL.match(code), code)
        g = CL.html_groups(self.table([('c', 'F&W ECOL 448', 'Ecology', '3'), ('c', 'AT 310', 'Athletic Training', '3')], heading='Major Requirements'))
        self.assertEqual(([c['code'] for c in g[0][1]['courses']], g[0][1]['issues']), (['F&W ECOL 448', 'AT 310'], set()))
        g = CL.html_groups(self.table([('c', 'BIOL 101', 'A', '3'), ('c', 'PLANTSCI/\u200bPL PATH 261 & PL PATH/\u200bPLANTSCI 262', 'Joined', '3')], heading='Major Requirements'))
        self.assertTrue(g[0][1]['issues'])  # a long joined row is held, never dropped
        for row in ('E&ES215 & E&ES216', 'COMPLITTHT 3120'):  # Wesleyan, WUSTL: held, never dropped
            g = CL.html_groups(self.table([('c', 'BIOL 101', 'A', '3'), ('c', row, 'Joined', '3')], heading='Major Requirements'))
            self.assertTrue(g[0][1]['issues'], row)
        g = CL.html_groups(self.table([('c', 'INTER-AG 155', 'Seminar', '1'), ('c', 'AN SCI 135', 'Seminar', '1')], heading='Major Requirements'))
        self.assertTrue(g[0][1]['issues'])  # UW-Madison: a hyphenated subject is not read yet, so the group is held, never shortened
        ctx = self.table([('c', 'ARTS 101', 'Drawing', '3'), ('c', 'ARTS 102', 'Painting', '3')], heading='Major Requirements', context='Complete one course from:')
        self.assertIn('context_says_choose', CL.html_candidates({'institution_key': 'k'}, e, {'url': 'u'}, [ctx], '2026-2027', 'x', 1)[0]['issues'])
        self.assertEqual(CL.substitution_codes('STAT 1772 will substitute for SOC SCI 2020.\nCourses in lieu of PHYSICS 125A'), {'STAT 1772', 'SOC SCI 2020', 'PHYSICS 125A'})
        uwm = self.table([('c', 'ARTHIST 101', 'Ancient Art', '3'), ('c', 'BUS ADM 201', 'Business', '3')], heading='Major Requirements')
        self.assertEqual([c['code'] for c in CL.html_groups(uwm)[0][1]['courses']], ['ARTHIST 101', 'BUS ADM 201'])
        from programs import verify as V
        self.assertTrue(V.code_in('ARTHIST\xa0101 Ancient Art', 'ARTHIST 101'))
        spec = self.table([('c', 'X 101', 'A', '3')], heading='Major Requirements', context='Students must choose one specialization.')
        self.assertIn('context_says_choose_among_tables', CL.html_candidates({'institution_key': 'k'}, e, {'url': 'u'}, [spec], '2026-2027', 'x', 1)[0]['issues'])

    def test_credits_overview_is_not_the_first_table(self):  # TAMUSA 2026-27 (issue #95 recovery)
        from programs import courseleaf as CL
        e = {'url': 'https://catalog.tamusa.edu/x/', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}
        over = self.table([('rule', 'Core Curriculum', '', '42'), ('rule', 'Major (Required) Courses', '', '53'), ('rule', 'Electives', '', '25'),
                           ('rule', 'Total Credits', '', '120')], heading='General Requirements')
        main = self.table([('c', 'CSCI 1436', 'Programming Fundamentals I', '4'), ('rule', "Select one of COB's Approved Ethics Electives", '', '3'),
                           ('opt', 'BUAD 4301', 'Ethics I'), ('opt', 'BUAD 4302', 'Ethics II')], heading='Department probation and withdrawal')
        later = self.table([('c', 'CSCI 4391', 'Senior Project', '3')], heading='Additional Courses')
        out = CL.html_candidates({'institution_key': 'k'}, e, {'url': 'u'}, [over, main, later], '2026-2027', 'cs', 1)
        self.assertEqual([(c['record']['rule_details']['group_type'], sorted(c['issues'])) for c in out],
                         [('all_required', []), ('choose_courses', []), ('all_required', ['secondary_table'])])
        self.assertEqual(out[1]['record']['rule_details']['choose_count'], 1)  # "Select one of <named> Electives" over its listed options
        self.assertNotIn('withdrawal', out[0]['record']['rule_details']['source_section'])  # the policy heading above the table is not its section
        # a first table that lists courses keeps its place; so does a term of a plan printed with uncoded course names
        out = CL.html_candidates({'institution_key': 'k'}, e, {'url': 'u'}, [later, main], '2026-2027', 'cs', 1)
        self.assertIn('secondary_table', out[1]['issues'])
        term = self.table([('rule', 'Foundations of Professional Nursing Practice', '', '3'), ('rule', 'Health Assessment', '', '3'),
                           ('rule', 'Pharmacology', '', '3'), ('rule', 'Total Credits', '', '9')], heading='First Year Summer')
        out = CL.html_candidates({'institution_key': 'k'}, e, {'url': 'u'}, [term, later], '2026-2027', 'nrs', 1)
        self.assertIn('secondary_table', out[-1]['issues'])
        # "Select 14 hours of Architectural Science Electives" is hours, never a count of courses
        g = CL.html_groups(self.table([('rule', 'Select 14 hours of Architectural Science Electives', '', '14'), ('opt', 'ARCH 300', 'A'), ('opt', 'ARCH 301', 'B')]))
        self.assertEqual((g[0][1]['type'], g[0][1].get('choose_credits')), ('choose_credits', 14))

    def test_heading_that_prints_a_choice(self):  # TAMUSA BS Public Health 2026-27 (independent re-verification, issue #95)
        from programs import courseleaf as CL
        t = self.table([('head', 'Major Courses'), ('c', 'HLTH 2301', 'Foundations', '3'),
                        ('head', 'Prescribed Electives (Choose 9 hours)'), ('sub', 'Cross-Cutting Issues'), ('c', 'HLTH 3370', 'Directed Study', '3'),
                        ('sub', 'Emergency Management'), ('c', 'HLTH 3355', 'Society and Disaster', '3'),
                        ('head', 'Capstone'), ('c', 'HLTH 4670', 'Internship', '6')])
        self.assertEqual([(s, sorted(g['issues'])) for s, g in CL.html_groups(t)],
                         [('Major Courses', []), ('Cross-Cutting Issues', ['heading_prints_choice']),
                          ('Emergency Management', ['heading_prints_choice']), ('Capstone', [])])
        # the section itself prints the choice (CUW 'Non-Western Global History (choose 2 courses)'); a dash form too
        for h in ('Non-Western Global History (choose 2 courses)', 'Major Electives - Select 12 credits'):
            g = CL.html_groups(self.table([('head', h), ('c', 'HIST 3301', 'Asia', '3'), ('c', 'HIST 3302', 'Africa', '3')]))
            self.assertIn('heading_prints_choice', g[0][1]['issues'])
        # an ordinary heading with a number in it, or one that says to complete all, is not a choice
        for h in ('Required Courses (36 hours)', 'Major Core (Complete all courses)'):
            g = CL.html_groups(self.table([('head', h), ('c', 'HIST 3301', 'Asia', '3')]))
            self.assertNotIn('heading_prints_choice', g[0][1]['issues'])

    def test_third_review_rules(self):
        from programs import courseleaf as CL
        e = {'url': 'https://catalog.uoregon.edu/x/', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        t = self.table([('c', 'STAT 243Z', 'Elementary Statistics I 1', '4'), ('c', 'PSY 201Z', 'Mind', '4')])
        out = CL.html_candidates({'institution_key': 'k'}, e, {'url': 'u'}, [t], '2026-2027', 'psy', 1, 'STAT 243Z is recommended. MATH 241 may be substituted.')
        self.assertIn('substitution_noted_on_page', out[0]['issues'])
        t = self.table([('c', 'MUS 126', 'Music Theory Fundamentals 1', '3')])
        out = CL.html_candidates({'institution_key': 'k'}, e, {'url': 'u'}, [t], '2026-2027', 'mus', 1, 'Placement test may waive the course requirement.')
        self.assertIn('substitution_noted_on_page', out[0]['issues'])
        g = CL.html_groups(self.table([('c', 'DATA 488', 'Capstone (or)', '4'), ('opt', 'MATH 280', 'Internship')]))
        self.assertTrue({'indented_rows_after_required_course', 'substitute_in_title'} <= g[0][1]['issues'])


GRID_HTML = """<h2>Roadmaps</h2><p>Courses marked with (*) are recommended.</p>
<table class="sc_plangrid"><thead>
<tr class="plangridyear firstrow"><th id="year0" colspan="4">First Year</th></tr>
<tr class="plangridterm"><th id="year0_Term0_codecol">Fall</th><th id="year0_Term0_hourscol">Credits</th><th id="year0_Term1_codecol">Spring</th><th id="year0_Term1_hourscol">Credits</th></tr>
</thead><tbody>
<tr class="even"><td header="year0 year0_Term0_codecol" class="codecol"><a>MATH F251X</a><sup>6</sup></td><td header="year0 year0_Term0_hourscol">4</td>
 <td header="year0 year0_Term1_codecol" class="codecol"><a>WRTG F211X</a>, <a> F212X</a>, or <a> F214X</a><sup>1</sup></td><td header="year0 year0_Term1_hourscol">3</td></tr>
<tr class="odd"><td header="year0 year0_Term0_codecol" class="codecol"><a>WRTG F111X</a><sup>1</sup></td><td header="year0 year0_Term0_hourscol">3</td>
 <td header="year0 year0_Term1_codecol" class="codecol">Complete one of the following:<sup>20</sup></td><td header="year0 year0_Term1_hourscol">1-3</td></tr>
<tr class="even"><td header="year0 year0_Term0_codecol" class="codecol">General Elective</td><td header="year0 year0_Term0_hourscol">3</td>
 <td header="year0 year0_Term1_codecol" class="codecol"><div style="margin-left: 20px;"><a>AIS F101</a> (*)</div></td><td header="year0 year0_Term1_hourscol"></td></tr>
<tr class="odd"><td header="year0 year0_Term0_codecol" class="codecol"><a>CS F301</a><sup>20,25</sup></td><td header="year0 year0_Term0_hourscol">3</td>
 <td header="year0 year0_Term1_codecol" class="codecol"><div style="margin-left: 20px;"><a>CIOS F150</a></div></td><td header="year0 year0_Term1_hourscol"></td></tr>
<tr class="even"><td header="year0 year0_Term0_codecol" class="codecol">Complete one of the following:<sup>6</sup></td><td header="year0 year0_Term0_hourscol">3-4</td><td colspan="2"> </td></tr>
<tr class="odd"><td header="year0 year0_Term0_codecol" class="codecol"><div style="margin-left: 20px;"><a>MATH F122X</a> (*)</div></td><td header="year0 year0_Term0_hourscol"></td><td colspan="2"> </td></tr>
<tr class="plangridsum"><td> </td><td header="year0 year0_Term0_hourscol">13-14</td><td> </td><td header="year0 year0_Term1_hourscol">4-6</td></tr>
<tr class="plangridtotal lastrow"><td header="year0" colspan="4">Total Credits 120</td></tr>
</tbody></table>
<h4>Footnote Definitions</h4><table class="sc_sctable tbl_roadmapfootnotes"><tbody>
<tr><td class="column0">1--Communication</td><td class="column1">20--Program Requirement</td></tr>
<tr><td class="column0">6--Mathematics</td><td class="column1">25--Upper Division</td></tr></tbody></table>"""


class InventoryLevelTests(unittest.TestCase):  # UMD 2026-27 majors with no printed award; MHEC Academic Program Inventory
    INV = {'entry': {'url': 'https://mhec.example.gov/inventory', 'sha256': 'f' * 64}, 'institution': 'Univ. of Maryland, College Park', 'publisher': 'MHEC',
           'rows': [['Univ. of Maryland, College Park', 'ACCOUNTING', "Bachelor's Degree"], ['Univ. of Maryland, College Park', 'ACCOUNTING', "Master's Degree"],
                    ['Univ. of Maryland, College Park', 'AGRICULTURAL & RESOURCE ECONOMICS', "Bachelor's Degree"],
                    ['Univ. of Maryland, College Park', 'ARTIFICIAL INTELLIGENCE: COMPUTATIONAL S', "Bachelor's Degree"],
                    ['Univ. of Maryland, College Park', 'BIOLOGY', "Bachelor's Degree"], ['Univ. of Maryland, College Park', 'BIOLOGY', "Bachelor's Degree"],
                    ['Univ. of Maryland, College Park', 'PUBLIC POLICY', "Master's Degree"]]}

    def cands(self, head, year='2026-2027 Catalog'):
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/m/', 'role': 'program_page', 'sha256': 'a' * 64, 'fetched_at': '2026-10-07T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        page = T.Page(year + '\n' + head, head + ' | X', [], [], [head])
        return X.inventory_level_candidates({'institution_key': 'k'}, e, page, '2026-27', self.INV)

    def test_bachelor_level_from_the_inventory_award_unknown(self):
        c = self.cands('Accounting Major')
        self.assertEqual(len(c), 1); c = c[0]
        self.assertEqual((c['record']['program_name'], c['record']['credential_level'], c['issues']), ('Accounting Major', 'bachelor', ['award_not_printed']))
        self.assertEqual([ev['snippet'] for ev in c['evidence'] if ev['field'] == 'credential_level'], ["Univ. of Maryland, College Park | ACCOUNTING | Bachelor's Degree"])
        self.assertEqual(len(self.cands('Agricultural and Resource Economics Major')), 1)  # '&' as printed in the inventory
        self.assertEqual(len(self.cands('Artificial Intelligence: Computational Science Major')), 1)  # inventory name cut at 40
        self.assertEqual(self.cands('Biology Major'), [])  # two bachelor's rows of that name: not one program
        self.assertEqual(self.cands('Public Policy Major'), [])  # master's only
        self.assertEqual(self.cands('Accounting Major at Shady Grove'), [])
        self.assertEqual(self.cands('Accounting Minor'), [])
        self.assertEqual(self.cands('Accounting Major', year='2026-2027 Catalog\n2025-2026 Catalog'), [])
        self.assertEqual(self.cands('Art Major'), [])  # not in the inventory

    def test_award_printed_in_the_page_text(self):  # UMD pages that name the award in a sentence (review of 2026-10-07)
        P = X.printed_awards
        self.assertEqual(set(P('Theatre', 'Theatre Major\nOur program offers a liberal arts education. The B.A. in Theatre seeks to introduce students to the history of theatre.')), {'B.A.'})
        self.assertEqual(set(P('Hearing and Speech Sciences', 'The department studies human communication and its disorders. The department curriculum leads to the Bachelor of Arts degree. An undergraduate major is broad.')), {'B.A.'})
        self.assertEqual(set(P('Architecture', 'For the Bachelor of Science degree option, students must complete three additional studios.\nFor the Bachelor of Arts degree option, students must complete 30 additional credits.')), {'B.A.', 'B.S.'})
        self.assertEqual(P('Theatre', 'Chemistry Major (B.A., B.S.)'), {})  # a navigation line
        self.assertEqual(P('Theatre', 'Theatre Major (B.A., B.S.)'), {})  # a short navigation line, even with the name
        self.assertEqual(P('Technology and Information Design', 'Technology and Information Design students learn design. The college also offers the Bachelor of Science in Information Science at College Park.'), {})
        self.assertEqual(P('Theatre', 'Many students enjoy their time here every year. Bachelor of Science students may join any club on campus as well.'), {})
        self.assertEqual(P('Technology and Information Design', 'Restriction: Students are not permitted to double-major with the Bachelor of Science in Information Science.'), {})
        self.assertEqual(P('Information Systems', 'In addition to the major requirements listed above, please consult the Summary of Bachelor of Science Degree Requirements (All Curricula) for more.'), {})
        self.assertEqual(P('Animal Sciences', 'Our department offers research opportunities. Students learn about animals and their care in many settings.'), {})
        self.assertEqual(set(P('American Studies', 'American Studies examines culture and identity in the United States. The B. A. degree prepares students for graduate work or careers in law.')), {'B.A.'})
        self.assertEqual(set(P('German Studies', 'The 36-credit BA in German Studies is centered on the study of the German language and culture.')), {'B.A.'})
        self.assertEqual(P('German Studies', 'German Studies majors may finish a BA in four years and graduate early from the program here.'), {})  # 'BA in' not followed by the name
        self.assertEqual(set(P('Persian Studies', 'It acquaints them with Persianate cultures and practices. The B.A. in Persian Studies prepares students for a range of careers.')), {'B.A.'})

    def test_verify_requires_the_row_in_the_inventory(self):
        from programs.verify import check_candidate
        c = self.cands('Accounting Major')[0]
        text = "2026-2027 Catalog\nAccounting Major"
        inv_text = "| Univ. of Maryland, College Park | ACCOUNTING | Bachelor's Degree"
        self.assertEqual(check_candidate(c, text, lambda sha: inv_text if sha == 'f' * 64 else ''), [])
        self.assertEqual(check_candidate(c, text, lambda sha: ''), ['credential level row not in its inventory document'])
        import copy
        a = copy.deepcopy(c); a['evidence'].append({'field': 'award', 'value': 'B.S.', 'snippet': 'The Bachelor of Science in Accounting prepares students.'})
        self.assertEqual(check_candidate(a, text, lambda sha: inv_text), ['award sentence not verbatim'])
        self.assertEqual(check_candidate(a, text + '\nThe Bachelor of Science in Accounting prepares students.', lambda sha: inv_text), [])
    def test_award_from_an_official_award_document(self):  # UMD 2026-27 school pages (owner 2026-10-08)
        from pipeline import text as T
        from programs.verify import check_candidate
        e = {'url': 'https://catalog.x.edu/m/', 'role': 'program_page', 'sha256': 'a' * 64, 'fetched_at': '2026-10-07T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        page = T.Page('2026-2027 Catalog\nAccounting Major', 'Accounting Major | X', [], [], ['Accounting Major'])
        docs = [{'majors': ['Accounting Major'], 'read': 'named', 'entry': {'url': 'https://school.x.edu/u', 'sha256': 'd' * 64},
                 'lines': ['Bachelor of Science in Accounting']}]
        c = X.inventory_level_candidates({'institution_key': 'k'}, e, page, '2026-27', self.INV, docs)[0]
        self.assertEqual(c['issues'], [])
        self.assertEqual([(ev['value'], ev['sha256']) for ev in c['evidence'] if ev['field'] == 'award'], [('B.S.', 'd' * 64)])
        inv_text = "| Univ. of Maryland, College Park | ACCOUNTING | Bachelor's Degree"
        other = lambda sha: {'f' * 64: inv_text, 'd' * 64: 'Programs\nBachelor of Science in Accounting'}.get(sha, '')
        self.assertEqual(check_candidate(c, '2026-2027 Catalog\nAccounting Major', other), [])
        self.assertEqual(check_candidate(c, '2026-2027 Catalog\nAccounting Major', lambda sha: inv_text if sha == 'f' * 64 else ''), ['award sentence not verbatim'])
        two = [{**docs[0], 'lines': ['Bachelor of Science in Accounting', 'Bachelor of Arts in Accounting']}]
        self.assertEqual(X.inventory_level_candidates({'institution_key': 'k'}, e, page, '2026-27', self.INV, two)[0]['issues'], ['award_not_printed'])


class CatalogPeriodTests(unittest.TestCase):  # Cal Poly '2026-2028 Catalog' (#153; owner decision 2026-10-07)
    def test_two_year_label_is_kept_as_printed(self):
        from pipeline import text as T
        from programs.years import academic_year_of
        page = T.Page('2026-2028 Catalog\n2026-2028 Edition\nAgricultural Business (BS)', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(page)}, {'2026-2028'})
        self.assertEqual({y for y, _ in X.printed_catalog_years(T.Page('2026-28 Catalog', 't', [], [], []))}, {'2026-2028'})
        self.assertEqual(X.printed_catalog_years(T.Page('2026-2029 Catalog', 't', [], [], [])), set())  # three years: not read
        # UT Austin: a two-year catalog with a yearly edition printed on the page: the edition is the label
        ut = T.Page('2026-27 Edition\nUndergraduate, 2026-2028\n2026-2028 Undergraduate Catalog', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(ut)}, {'2026-2027'})
        self.assertEqual(academic_year_of('2026-2027'), '2026-27')
        self.assertEqual(academic_year_of('2026-2028', '2026-27'), '2026-27')
        self.assertEqual(academic_year_of('2026-2028', '2027-28'), '2027-28')  # the same catalog, read in its second year
        self.assertEqual(academic_year_of('2026-2028', '2029-30'), '2026-27')  # a period that has ended: its first year

    def test_static_record_keeps_the_period(self):
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/p/', 'role': 'program_page', 'sha256': 'a' * 64, 'fetched_at': '2026-10-07T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        page = T.Page('2026-2028 Edition\nAgricultural Business (BS)', 'Agricultural Business (BS) < X', [], [], ['2026-2028 Edition', 'Agricultural Business (BS)'])
        c = X.static_program_identity({'institution_key': 'k'}, e, page, '2026-27')[0]
        self.assertEqual((c['academic_year'], c['record']['catalog_year']), ('2026-27', '2026-2028'))
        self.assertEqual([ev['snippet'] for ev in c['evidence'] if ev['field'] == 'catalog_year'], ['2026-2028 Edition'])

    def test_validation_accepts_a_year_inside_the_period(self):
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
        from validate_data import requirement_group_errors as V
        rec = lambda cy, ay: {'academic_year': ay, 'requirement_kind': 'program_plan', 'rule_details': {'schema': 'requirement_group/v1', 'catalog_year': cy,
              'group_type': 'sequence', 'category': 'recommended_sequence', 'terms': [{'term_index': 1, 'items': []}]}}
        self.assertEqual(V(rec('2026-2028', '2026-27')), [])
        self.assertEqual(V(rec('2026-2028', '2027-28')), [])
        self.assertTrue(V(rec('2026-2028', '2028-29')))
        self.assertTrue(V(rec('2026-2029', '2026-27')))
        self.assertTrue(V(rec('2026-2027', '2027-28')))
        self.assertEqual(V(rec('2026-27', '2026-27')), [])


class RoadmapGridTests(unittest.TestCase):  # UAF 2026-27 roadmaps (#151 reader request)
    def grid(self, html=GRID_HTML):
        from programs.courselist_html import plan_grids
        from programs import courseleaf as CL
        entry = {'url': 'https://catalog.x.edu/bachelors/cs-bs/', 'role': 'program_page', 'sha256': 'a' * 64,
                 'fetched_at': '2026-10-07T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        doc = plan_grids(html)
        return doc, CL.plangrid_candidates({'institution_key': 'k'}, entry, {'url': entry['url'] + '#plangrid', 'sha256': 'b' * 64}, doc, '2026-2027', 'cs-bs')

    def test_terms_columns_options_and_footnotes(self):
        doc, out = self.grid()
        self.assertEqual(len(out), 1); c = out[0]
        self.assertEqual(c['extractor'], 'courseleaf_plangrid/v1'); self.assertEqual(c['issues'], [])
        rd = c['record']['rule_details']
        self.assertEqual(rd['rule_text'], 'Total Credits 120 (as printed)')
        self.assertEqual(rd['footnotes'], {'1': 'Communication', '6': 'Mathematics', '20': 'Program Requirement', '25': 'Upper Division'})
        fall, spring = rd['terms']
        self.assertEqual((fall['label'], fall['credit_hours'], spring['label'], spring['credit_hours']), ('First Year Fall', '13-14', 'First Year Spring', '4-6'))
        self.assertEqual(fall['items'], [
            {'code': 'MATH F251X', 'credits': 4, 'footnotes': ['6']}, {'code': 'WRTG F111X', 'credits': 3, 'footnotes': ['1']},
            {'text': 'General Elective', 'credits': 3}, {'code': 'CS F301', 'credits': 3, 'footnotes': ['20', '25']},
            {'text': 'Complete one of the following:', 'credits': '3-4', 'footnotes': ['6'], 'options': [{'code': 'MATH F122X', 'recommended': True}]}])
        # the options printed in the Spring column belong to Spring's rule, though Fall rows sit beside them
        self.assertEqual(spring['items'], [
            {'text': 'WRTG F211X, F212X, or F214X', 'credits': 3, 'footnotes': ['1']},
            {'text': 'Complete one of the following:', 'credits': '1-3', 'footnotes': ['20'],
             'options': [{'code': 'AIS F101', 'recommended': True}, {'code': 'CIOS F150'}]}])
        # the Course List reader is unchanged by the grid capture: no column attributes recorded there
        from programs.courselist_html import course_lists
        self.assertEqual(course_lists(GRID_HTML.replace('sc_plangrid', 'sc_courselist'))[0]['rows'][2]['cells'][0].get('header'), None)

    def test_unreadable_layouts_hold_the_plan(self):
        cases = {
            'indented_row_without_rule': GRID_HTML.replace('Complete one of the following:<sup>20</sup>', 'Business Elective<sup>20</sup>'),
            'footnote_inside_cell': GRID_HTML.replace('<a>MATH F251X</a><sup>6</sup>', '<a>MATH F251X</a><sup>6</sup> or placement'),
            'footnote_not_defined': GRID_HTML.replace('<sup>6</sup></td>', '<sup>4 or 5</sup></td>', 1),
            'grid_cell_without_column': GRID_HTML.replace('<td colspan="2"> </td></tr>\n<tr class="odd">', '<td colspan="2">MATH F151X</td></tr>\n<tr class="odd">', 1),
            'rule_without_options': GRID_HTML.replace('<div style="margin-left: 20px;"><a>MATH F122X</a> (*)</div>', 'MATH F122X'),
            # a row printed without indentation closes the rule above it: a later indented row has no rule
            'indented_row_without_rule ': GRID_HTML.replace('<tr class="plangridsum">', '<tr><td header="year0 year0_Term0_codecol">General Elective</td><td header="year0 year0_Term0_hourscol">3</td></tr>'
                                                            '<tr><td header="year0 year0_Term0_codecol"><div style="margin-left: 20px;">MATH F151X</div></td></tr><tr class="plangridsum">'),
        }
        for issue, html in cases.items():
            _, out = self.grid(html)
            self.assertIn(issue.strip(), out[0]['issues'], issue)

    def test_concentration_grids_and_a_one_term_year(self):  # UAF Aerospace Engineering, Early Childhood and Family Studies
        two = GRID_HTML.replace('<h2>Roadmaps</h2>', '<h3>Robotics Concentration</h3>') + GRID_HTML.replace('<h2>Roadmaps</h2>', '<h3>Without Concentration</h3>')
        _, out = self.grid(two)
        self.assertEqual([(c['record']['requirement_key'], c['record']['rule_details']['source_section'], c['issues']) for c in out],
                         [('roadmap-robotics-concentration', 'Robotics Concentration', []), ('roadmap-without-concentration', 'Without Concentration', [])])
        _, out = self.grid(GRID_HTML + GRID_HTML)  # two grids under one 'Roadmaps' heading: which plan is which is not printed
        self.assertTrue(all('multiple_plan_grids' in c['issues'] for c in out))
        # a fifth year printing only Fall: its sum row keeps an empty cell for a second term that has no header
        one = GRID_HTML.replace('<tr class="plangridtotal', '<tr class="plangridsum"><td> </td><td header="year0 year9_Term1_hourscol"></td></tr><tr class="plangridtotal')
        self.assertEqual(self.grid(one)[1][0]['issues'], [])
        bad = GRID_HTML.replace('<tr class="plangridtotal', '<tr class="even"><td header="year0 year9_Term1_codecol">MATH F200X</td></tr><tr class="plangridtotal')
        self.assertIn('grid_cell_without_term', self.grid(bad)[1][0]['issues'])

    def test_verify_checks_items_against_grid_cells(self):
        import json as J
        from programs.verify import check_candidate
        doc, out = self.grid()
        other = lambda sha: J.dumps(doc) if sha == 'b' * 64 else ''
        self.assertEqual(check_candidate(out[0], 'page text', other), [])
        bad = J.loads(J.dumps(out[0]))
        bad['record']['rule_details']['terms'][0]['items'][0]['footnotes'] = ['16']
        bad['record']['rule_details']['terms'][1]['items'][1]['options'][1]['code'] = 'CIOS F160'
        self.assertEqual(len(check_candidate(bad, 'page text', other)), 2)
        self.assertIn('roadmap grid document not in run', check_candidate(out[0], 'page text', lambda sha: ''))


class PositionalPlanGridTests(unittest.TestCase):  # SHSU 2026-27 '#plangrid' documents: no column headers on the cells
    @staticmethod
    def cell(text, cls=None, span=1, sups=None, indent=False):
        c = {'text': text, 'classes': [cls] if cls else [], 'colspan': span, 'indent': indent, 'spans': []}
        if cls in ('codecol', 'hourscol'): c['header'] = 'undefined' + cls
        if sups: c['sups'] = [sups]; c['sup_tail'] = sups
        return c

    def grid(self, sum_fall='7', total='Total Hours: 10'):
        C = self.cell
        row = lambda cls, *cells: {'classes': cls, 'cells': list(cells)}
        return {'heading': 'Bachelor of Science, Major in Biology', 'rows': [
            row(['plangridyear', 'firstrow'], C('First Year', span=4)),
            row(['plangridterm'], C('Fall'), C('Hours', 'hourscol'), C('Spring'), C('Hours', 'hourscol')),
            row(['even'], C('BIOL 24031', 'codecol', sups='1'), C('4', 'hourscol'), C('ENGL 1302', 'codecol'), C('3', 'hourscol')),
            row(['odd'], C('', span=2), C('Component Area II', 'codecol'), C('0', 'hourscol')),
            row(['even'], C('MATH 1314', 'codecol'), C('3', 'hourscol'), C('', span=2)),
            row(['plangridsum'], C(''), C(sum_fall, 'hourscol'), C(''), C('3', 'hourscol')),
            row(['plangridtotal', 'lastrow'], C(total, span=4))]}

    def test_columns_by_position_footnotes_and_sums(self):
        from programs import courseleaf as CL
        terms, total, issues = CL.parse_plangrid(self.grid(), {'1': 'Satisfies Core Curriculum requirement for Component Area III.'})
        self.assertEqual([(t['label'], t.get('credit_hours'), t['items']) for t in terms],
                         [('First Year Fall', '7', [{'code': 'BIOL 2403', 'credits': 4, 'footnotes': ['1']}, {'code': 'MATH 1314', 'credits': 3}]),
                          ('First Year Spring', '3', [{'code': 'ENGL 1302', 'credits': 3}, {'text': 'Component Area II', 'credits': 0}])])
        self.assertEqual((total, issues), ('10', set()))

    def test_printed_sums_hold_the_plan(self):
        from programs import courseleaf as CL
        self.assertIn('term_hours_differ', CL.parse_plangrid(self.grid(sum_fall='8', total='Total Hours: 11'), {'1': 'x'})[2])
        self.assertIn('total_hours_differ', CL.parse_plangrid(self.grid(total='Total Hours: 12'), {'1': 'x'})[2])
        self.assertIn('footnote_not_defined', CL.parse_plangrid(self.grid(), {})[2])
        g = self.grid(); g['rows'][2]['cells'][1]['classes'] = []  # an hours cell without its column class
        self.assertIn('grid_cell_without_column', CL.parse_plangrid(g, {'1': 'x'})[2])

    def test_footnotes_printed_after_the_total(self):
        from programs import courseleaf as CL
        text = '| Total Hours: 120\n\n1\n\nSatisfies Core Curriculum requirement.\n\n2\n\nSee listing below.\n\nCourse List\n\n3\n'
        self.assertEqual(CL.page_footnotes(text), {'1': 'Satisfies Core Curriculum requirement.', '2': 'See listing below.'})
        self.assertEqual(CL.page_footnotes('no total here\n1\nx'), {})

    def test_pr249_review_holds(self):  # independent review of #249
        from programs import courseleaf as CL
        # an item with no hours in a summed term; the total is checked even when one term is summed
        g = self.grid(); g['rows'][4]['cells'][1]['text'] = ''
        self.assertIn('term_item_without_hours', CL.parse_plangrid(g, {'1': 'x'})[2])
        self.assertEqual(CL._sum_issues([{'credit_hours': '3', 'items': [{'credits': 3}]}], '4'), {'total_hours_differ'})
        # two-digit footnotes; a number printed twice or a definition that may continue is not read
        g = self.grid(); g['rows'][2]['cells'][0].update(text='BIOL 240312', sups=['12'], sup_tail='12')
        terms, _, issues = CL.parse_plangrid(g, {'12': 'Twelve.'})
        self.assertEqual((terms[0]['items'][0], issues), ({'code': 'BIOL 2403', 'credits': 4, 'footnotes': ['12']}, set()))
        text = '| Total Hours: 120\n1\nOne.\n9\nNine.\n9\nNine again.\nCourse List'
        self.assertEqual(CL.page_footnotes(text), {'1': 'One.', '9': None})
        self.assertEqual(CL.page_footnotes('| Total Hours: 120\n1\nOne\ncontinued here'), {'1': None})
        self.assertEqual(CL.page_footnotes('| Total Hours: 120\n1\nOne.\n7\nSeven.\nNotes\nStudents must ...'), {'1': 'One.', '7': 'Seven.'})  # SHSU
        self.assertIn('footnote_definition_unclear', CL.parse_plangrid(self.grid(), {'1': None})[2])
        # the printed total keeps its label; the layout document's own footnote list comes first
        e = {'url': 'u', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'}
        [c] = CL.plangrid_candidates({'institution_key': 'k'}, e, {'url': 'u#plangrid'}, {'grids': [self.grid()]}, '2026-2027', 'bio', '| Total Hours: 10\n1\nOne.\nCourse List')
        self.assertEqual((c['record']['rule_details']['rule_text'], c['record']['rule_details']['footnotes'], c['issues']), ('Total Hours 10 (as printed)', {'1': 'One.'}, []))
        doc = {'grids': [self.grid()], 'footnotes': [{'rows': [{'cells': [{'text': '1 -- From the document.'}]}]}]}
        [c] = CL.plangrid_candidates({'institution_key': 'k'}, e, {'url': 'u#plangrid'}, doc, '2026-2027', 'bio', '| Total Hours: 10\n1\nOne.\nCourse List')
        self.assertEqual(c['record']['rule_details']['footnotes'], {'1': 'From the document.'})
        # a route's grid (Missouri dual degree) is held; Missouri codes with underscores are codes
        g = self.grid(); g['heading'] = 'Semester Plan - Dual Degree Electrical Engineering and Computer Engineering'
        [c] = CL.plangrid_candidates({'institution_key': 'k'}, e, {'url': 'u#plangrid'}, {'grids': [g]}, '2026-2027', 'bsee', '| Total Hours: 10\n1\nOne.\nCourse List')
        self.assertIn('plan_heading_label', c['issues'])
        self.assertTrue(CL.GRID_CODE.match('AG_S_TCH 1020') and CL.GRID_CODE.match('ENGLSH 1000'))
        g = self.grid(); g['heading'] = 'Physical Geography Concentration'
        [c] = CL.plangrid_candidates({'institution_key': 'k'}, e, {'url': 'u#plangrid'}, {'grids': [g]}, '2026-2027', 'geog', '| Total Hours: 10\n1\nOne.\nCourse List')
        self.assertIn('plan_heading_label', c['issues'])  # an unlabelled grid for one concentration
        two = {'grids': [dict(self.grid(), heading='Semester Plan - Electrical Engineering'), dict(self.grid(), heading='Semester Plan - Dual Degree Electrical and Computer Engineering')]}
        out = CL.plangrid_candidates({'institution_key': 'k'}, e, {'url': 'u#plangrid'}, two, '2026-2027', 'bsee', '| Total Hours: 10\n1\nOne.\nCourse List')
        self.assertEqual([c['issues'] for c in out], [[], ['plan_heading_label']])  # labelled: the dual degree plan is still held

    def test_header_cells_keep_the_header_reading(self):  # UAF grids name their column in each cell's header
        from programs import courseleaf as CL
        g = self.grid()
        for r in g['rows']:
            for c in r['cells']: c['header'] = 'nothing'
        g['rows'][2]['cells'][0]['header'] = 'year0_Term1_codecol'
        self.assertEqual(CL.parse_plangrid(g, {'1': 'x'})[0], [])  # header mode: no term row ids, so no terms; never positional


class FootnoteMarkerTests(unittest.TestCase):  # issue #129: TAMUSA 'Strategic Management 3', UF 'Principles of Journalism 1'
    def test_trailing_superscripts_are_markers_not_title(self):
        from programs.courselist_html import course_lists
        from programs import courseleaf as CL
        html = ('<h2>Major Requirements</h2><table class="sc_courselist"><caption>Course List</caption><tbody>'
                '<tr><td><a>MGMT 4370</a></td><td>Strategic Management <sup>3</sup></td><td>3</td></tr>'
                '<tr><td><a>BUAD 4070</a></td><td>Business Capstone Lab<sup>2</sup>,<sup>5</sup></td><td>0</td></tr>'
                '<tr><td><a>CSCI 1436</a></td><td>Programming Fundamentals 1</td><td>3</td></tr>'
                '<tr><td><a>ARTH 3301</a></td><td>20<sup>th</sup> Century Art</td><td>3</td></tr>'
                '<tr class="orclass"><td><div style="margin-left:20px;">or <a>MGMT 4371</a></div></td><td>Strategy Seminar<sup>1</sup></td><td></td></tr>'
                '</tbody></table>')
        t = course_lists(html)[0]
        cells = [r['cells'][1] for r in t['rows']]
        self.assertEqual([c['text'] for c in cells], ['Strategic Management 3', 'Business Capstone Lab2,5', 'Programming Fundamentals 1',
                                                      '20th Century Art', 'Strategy Seminar1'])  # the text stays as printed
        self.assertEqual([c.get('sup_tail') for c in cells], ['3', '2,5', None, None, '1'])
        g = CL.html_groups(t)
        items = [x for _, grp in g for c in grp['courses'] for x in (c.get('any_of') or [c])]
        self.assertEqual([x['title'] for x in items], ['Strategic Management', 'Business Capstone Lab', 'Programming Fundamentals 1',
                                                       '20th Century Art', 'Strategy Seminar'])
        self.assertTrue(t.get('sups_recorded'))
        self.assertNotIn('title_number_unchecked', set().union(*(grp['issues'] for _, grp in g)))
        # a layout stored before superscripts were recorded keeps its text, and a title ending in a number is held until re-fetched
        old = {'rows': [{'classes': [], 'cells': [{'text': 'MGMT 4370'}, {'text': 'Strategic Management 3'}, {'text': '3'}]}]}
        self.assertEqual(CL.html_groups(old)[0][1]['courses'][0]['title'], 'Strategic Management 3')
        self.assertIn('title_number_unchecked', CL.html_groups(old)[0][1]['issues'])
        plain = {'rows': [{'classes': [], 'cells': [{'text': 'MGMT 4370'}, {'text': 'Strategic Management'}, {'text': '3'}]}]}
        self.assertNotIn('title_number_unchecked', CL.html_groups(plain)[0][1]['issues'])
        self.assertEqual(CL.strip_marks('3', '3'), '3')  # a title that is only a marker is not emptied

    def test_refetch_target_fetches_only_its_pages(self):
        page = b'<html><head><title>P</title></head><body><a href="https://catalog.example.edu/preview_program.php?catoid=56&poid=1">Computer Science, BS</a></body></html>'
        t = {**TARGET, 'refetch': ['https://catalog.example.edu/prog/']}
        with tempfile.TemporaryDirectory() as d:
            f = FakeFetcher({'https://catalog.example.edu/prog/': page, **PAGES}); run = C.Run(Path(d))
            C.crawl_target(t, run, f, log=lambda *_: None)
            self.assertEqual(f.calls, ['https://catalog.example.edu/prog/'])
            self.assertEqual([(e['role'], e['via']) for e in run.entries()], [('program_page', 'refetch')])


class OutlineTests(unittest.TestCase):
    def test_list_depth_and_blocks(self):
        from programs.courselist_html import outline
        html = ('<nav><ul><li>Home</li></ul></nav><h2>Major Requirements</h2><p>Select one of the following:</p>'
                '<ul><li><a class="sc-courselink">PSY 200</a> General Psychology <ul><li>or PSY 201</li></ul></li><li>STAT 243Z</li></ul>')
        b = outline(html)
        self.assertEqual([(x['tag'], x['depth'], x['text']) for x in b],
                         [('h2', 0, 'Major Requirements'), ('p', 0, 'Select one of the following:'), ('li', 1, 'PSY 200 General Psychology'), ('li', 2, 'or PSY 201'), ('li', 1, 'STAT 243Z')])


class PdfLayoutTests(unittest.TestCase):
    def test_bbox_parse(self):
        from programs.pdf_layout import parse_bbox
        x = ('<page width="612.0" height="792.0"><flow><block><line xMin="36.0" yMin="100.0" xMax="200.0" yMax="110.0">'
             '<word xMin="36.0" yMin="100.0" xMax="60.0" yMax="110.0">ANTH</word><word xMin="62.0" yMin="100.0" xMax="90.0" yMax="110.0">1200:</word>'
             '</line></block></flow></page>')
        self.assertEqual(parse_bbox(x), [{'width': 612.0, 'height': 792.0, 'lines': [{'y': 100.0, 'y1': 110.0, 'words': [[36.0, 60.0, 'ANTH'], [62.0, 90.0, '1200:']]}]}])


class ClearPathLayoutTests(unittest.TestCase):
    def page(self):
        def line(y, *ws): return {'y': y - 5, 'y1': y + 5, 'words': [[x, x + 10, t] for x, t in ws]}
        L = [line(84, (38, 'First'), (59, 'Year'), (80, '–'), (87, '7-9'), (113, 'Hours')),
             line(99, (38, 'Fall'), (55, 'Semester:')), line(99, (279, 'Hrs')), line(99, (307, 'Spring'), (336, 'Semester:')), line(99, (548, 'Hrs')),
             line(114, (38, 'ANTH'), (64, '1200:'), (89, 'Cultural'), (124, '(Behavioral')), line(128, (38, 'Science)')), line(121, (279, '3')),
             line(121, (307, 'ANTH'), (333, '1400:'), (358, 'Archaeology'), (548, '3')),
             line(143, (38, 'Elective')), line(143, (279, '1-3')), line(143, (307, 'Writing'), (340, 'and'), (358, 'Communication')), line(143, (548, '3-4')),
             line(160, (279, '4-6')), line(160, (548, '6-7')), line(170, (38, 'Completed:'))]
        return [{'width': 612, 'height': 792, 'lines': L}]

    def test_columns_wrapped_titles_and_totals(self):
        from programs import clearpath as CP
        years = CP.parse_layout(self.page())
        label, fall, ft, spring, st, probs = years[0]
        self.assertEqual((label, ft, st, probs), ('First Year – 7-9 Hours', '4-6', '6-7', set()))
        self.assertEqual(fall, [['ANTH 1200: Cultural (Behavioral Science)', '3'], ['Elective', '1-3']])
        self.assertEqual(spring, [['ANTH 1400: Archaeology', '3'], ['Writing and Communication', '3-4']])
        self.assertTrue(CP.term_ok(fall, ft) and CP.term_ok(spring, st))
        self.assertFalse(CP.term_ok([['Elective', '3']], '4-6'))

    def test_three_line_title_stays_in_one_item(self):  # UTC Biology B.S. Third Year Spring (review 2026-10-05)
        from programs import clearpath as CP
        # lines at 100/113/126 belong to the item whose hours print on the middle line (113); the next item's single line is at 143
        self.assertEqual(CP.blocks([100, 113, 126, 143], [113, 143]), [(0, 3), (3, 4)])
        self.assertEqual(CP.blocks([114, 128, 143], [121, 143]), [(0, 2), (2, 3)])
        self.assertIsNone(CP.blocks([100], [100, 120]))


class BulletMajorTests(unittest.TestCase):
    def test_two_column_bullets_with_bachelor_awards(self):  # King 2026-2027 Academic Catalog
        from pipeline import text as T
        txt = '\n'.join(['King', '2026-2027 Academic Catalog', 'MAJORS (DEGREES AWARDED)                o Special Education Track',
                         '• Accounting (BS)                                          K-8)', '• Biology (BA, BS)                       • Nursing (BSN)',
                         'o General Biology Track (BA, BS)        • Nursing Practice (BSN-DNP)', '• Business (PMBA, TMBA)                  • Exercise Science',
                         'MINORS', '• Theatre (BA)'])
        e = {'url': 'https://media.king.edu/2026/08/academic-catalog.pdf', 'sha256': 's', 'fetched_at': '2026-10-05T00:00:00'}
        out = X.bullet_major_candidates({'catalog': {'bullet_majors': {'heading': 'MAJORS (DEGREES AWARDED)', 'end': 'MINORS'}}}, {'institution_key': 'k'}, e, T.Page(txt, '', [], [], []), '2026-27')
        self.assertEqual([c['record']['program_name'] for c in out], ['Accounting (BS)', 'Biology (BA, BS)', 'Nursing (BSN)'])


class TypePathTests(unittest.TestCase):
    def test_award_paths_and_home_edition(self):  # Lincoln Memorial 2026-2027
        from pipeline import text as T
        lu, hu = 'https://undergraduatecatalog.lmunet.edu/degrees', 'https://undergraduatecatalog.lmunet.edu/'
        links = [('https://undergraduatecatalog.lmunet.edu/education/bachelor-of-science/bs-in-education', 'BS in Education'),
                 ('https://undergraduatecatalog.lmunet.edu/education/bachelor-of-science/bs-in-education', 'Bachelor of Science'),
                 ('https://undergraduatecatalog.lmunet.edu/history/bachelor-of-arts/ba-history-general', 'BA in History - General Track'),
                 ('https://undergraduatecatalog.lmunet.edu/nursing/associate-of-science-in-nursing/asn', 'Associate of Science in Nursing (ASN) (CIP code 51.3801)'),
                 ('https://undergraduatecatalog.lmunet.edu/nursing/bachelor-of-science/bsn', 'Bachelor of Science in Nursing (BSN) (CIP code 51.3801)')]
        pages = {'l': T.Page('Degrees', 'Degrees', [], links, []), 'h': T.Page('Undergraduate Catalog 2026-2027\nVol. XCVII', 'Catalog', [], [], [])}
        class R:
            def load_page(self, f): return pages[f], None
        es = [{'url': lu, 'page_file': 'l', 'sha256': 'a', 'fetched_at': '2026-10-05T00:00:00'}, {'url': hu, 'page_file': 'h', 'sha256': 'b', 'fetched_at': '2026-10-05T00:00:00'}]
        out = X.type_path_candidates({'type_path_list': {'url': lu, 'home': hu}}, {'institution_key': 'k'}, R(), es, '2026-27')
        self.assertEqual([(c['record']['program_name'], c['record'].get('cip_code'), c['record']['catalog_year']) for c in out],
                         [('BS in Education', None, '2026-2027'), ('Bachelor of Science in Nursing (BSN)', '51.3801', '2026-2027')])


class DegreeOfferedTests(unittest.TestCase):  # UNL 2026-2027 major pages: the award only in the summary table (#153)
    def page(self, value='Bachelor of Arts or Bachelor of Science', title='Anthropology < University of Nebraska\u2013Lincoln', rows=None):
        from pipeline import text as T
        rows = rows if rows is not None else [['College:', 'Arts & Sciences'], ['Degree Offered:', value], ['Hours Required:', '120']]
        txt = '\n'.join(['Undergraduate Catalog 2026-2027', 'Arts & Sciences', 'Anthropology'] + [' | '.join(r) for r in rows])
        return T.Page(txt, title, [{'rows': rows}], [], ['Arts & Sciences Anthropology', 'Description'])

    def run_(self, page):
        e = {'url': 'https://catalog.unl.edu/undergraduate/arts-sciences/anthropology/', 'sha256': 's', 'fetched_at': '2026-10-08T00:00:00'}
        return X.degree_offered_identity({'institution_key': 'ipeds-181464'}, e, page, '2026-27')

    def test_major_page_with_printed_awards(self):
        out = self.run_(self.page())
        self.assertEqual([(c['record']['program_name'], c['record']['program_key'], c['record']['catalog_year']) for c in out],
                         [('Anthropology', 'anthropology-bachelor-of-arts-or-bachelor-of-science', '2026-2027')])
        self.assertEqual(out[0]['evidence'][1]['snippet'], 'Degree Offered: Bachelor of Arts or Bachelor of Science')
        self.assertEqual([c['record']['program_key'] for c in self.run_(self.page('Bachelor of Science in Agricultural and Environmental Sciences Education'))],
                         ['anthropology-bachelor-of-science-in-agricultural-and-environmental-sciences-educ'])  # slug cap: 80

    def test_rows_without_a_bachelors_award_give_nothing(self):
        for v in ('Bachelor of Arts, Bachelor of Fine Arts', 'Bachelor of Arts in Hospitality, Restaurant & Tourism Management'):  # UNL Art; HRTM
            self.assertEqual(len(self.run_(self.page(v))), 1, v)
        for v in ('Minor only', 'Non-degree seeking', 'Bachelor of Arts; see adviser', 'Master of Arts', '', 'Bachelor of Arts, Master of Arts',
                  'Bachelor of Science and Master of Science', 'Bachelor of Science & Master of Science', 'Bachelor of Science Master of Science',
                  'Bachelor of Science in Business and Master of Professional Accountancy', 'Bachelor of Science Doctor of Pharmacy',
                  'Bachelor of Arts, Minor', 'Bachelor of Science, Juris Doctor', 'Bachelor of Science, MS', 'Bachelor of Science, Masters',
                  'Bachelor of Science in Food Science & Technology, Master of Science in Food Science & Technology, Ph.D.'):
            self.assertEqual(self.run_(self.page(v)), [], v)
        two = [['Degree Offered:', 'Bachelor of Arts'], ['Degree Offered:', 'Bachelor of Science']]
        self.assertEqual(self.run_(self.page(rows=two)), [])
        self.assertEqual(self.run_(self.page(rows=[['Hours Required:', '120']])), [])

    def test_option_minor_and_unnamed_pages_give_nothing(self):
        from pipeline import text as T
        for n in ('Anthropology Minor', 'Pre-Law', 'Anthropology Option', 'Teaching Certificate'):  # the heading prints the same name
            pg = self.page(title=n + ' < University of Nebraska\u2013Lincoln')
            self.assertEqual(self.run_(T.Page(pg.text, pg.title, pg.tables, [], ['Arts & Sciences ' + n])), [], n)
        self.assertEqual(self.run_(self.page(title='History < University of Nebraska\u2013Lincoln')), [])  # heading names another major

    def test_verify_requires_the_printed_row(self):
        from programs import verify as V
        pg = self.page(); out = self.run_(pg)
        self.assertNotIn('degree offered row not printed', V.check_candidate(out[0], pg.text))
        self.assertIn('degree offered row not printed', V.check_candidate(out[0], pg.text.replace('Bachelor of Science', 'Bachelor of Fine Arts')))
        # a longer printed row is not this row ('... Bachelor of Science and Master of Science')
        self.assertIn('degree offered row not printed', V.check_candidate(out[0], pg.text.replace('Bachelor of Science', 'Bachelor of Science and Master of Science')))

    def test_trusted_after_review(self):
        from programs import autoreview as A
        self.assertIn('degree_offered/v1', A.TRUSTED_PROGRAMS)
        self.assertIn('kuali_award_line/v1', A.TRUSTED_PROGRAMS)


class KualiAwardLineTests(unittest.TestCase):  # Utah 2026-27 '<code> Program' pages: the award after the department (#153)
    def page(self, name='Applied Mathematics', line='MathematicsBachelor of Science', title='AMTHBS Program | University of Utah Catalog', extra=()):
        from pipeline import text as T
        txt = '\n'.join(['General Catalog', 'University of Utah', 'Home (AY 2026-2027)', 'Class Schedule', 'University of Utah', '2026-2027', 'Programs', name, name, 'Download as PDF', line, 'Program Description', *extra])
        return T.Page(txt, title, [], [], ['General Catalog', 'University of Utah', name, 'Download as PDF', 'Program Description'])

    def run_(self, page):
        e = {'url': 'https://catalog.utah.edu/programs/AMTHBS', 'sha256': 's', 'fetched_at': '2026-10-08T00:00:00'}
        return X.kuali_award_line_identity({'institution_key': 'ipeds-230764'}, e, page, '2026-27')

    def test_award_after_department(self):
        out = self.run_(self.page())
        self.assertEqual([(c['record']['program_name'], c['record']['program_key'], c['record']['catalog_year']) for c in out],
                         [('Applied Mathematics', 'applied-mathematics-bachelor-of-science', '2026-2027')])
        self.assertEqual(out[0]['evidence'][1]['snippet'], 'MathematicsBachelor of Science')
        two = self.run_(self.page('Accounting', 'AccountingBachelor of Arts/Bachelor of Science'))
        self.assertEqual([c['record']['program_key'] for c in two], ['accounting-bachelor-of-arts-bachelor-of-science'])
        self.assertEqual(len(self.run_(self.page('Ballet', 'DanceBachelor of Fine Arts'))), 1)

    def test_non_bachelor_lines_give_nothing(self):
        for line in ('MathematicsMaster of Science', 'Art & Art HistoryMinor', 'OtherOther', 'Bachelor of Science', 'MathematicsBachelor of Science; see adviser',
                     'MathematicsBachelor of Science and Master of Science',
                     'MathematicsBachelor of Science/Master of Science'):
            self.assertEqual(self.run_(self.page(line=line)), [], line)

    def test_names_and_layouts_that_give_nothing(self):
        self.assertEqual(self.run_(self.page('Electrical Engineering Minor', 'Electrical and Computer EngineeringBachelor of Science')), [])
        self.assertEqual(self.run_(self.page('General Education and Bachelor Degree Requirements', 'OtherBachelor of Science')), [])
        self.assertEqual(self.run_(self.page('Bioinformatics BS', 'MathematicsBachelor of Science')), [])  # the name carries its award: kuali_page/v1
        self.assertEqual(self.run_(self.page(title='Applied Mathematics | University of Utah Catalog')), [])
        self.assertEqual(self.run_(self.page(extra=('Download as PDF',))), [])
        self.assertEqual(self.run_(self.page(extra=('General Catalog 2025-2026',))), [])

    def test_verify_requires_the_printed_line(self):
        from programs import verify as V
        pg = self.page(); out = self.run_(pg)
        self.assertNotIn('award line not printed', V.check_candidate(out[0], pg.text))
        self.assertIn('award line not printed', V.check_candidate(out[0], pg.text.replace('MathematicsBachelor of Science', 'Mathematics Bachelor of Science Program')))
        moved = pg.text.replace('Download as PDF\nMathematicsBachelor of Science', 'Download as PDF\nProgram Information\nMathematicsBachelor of Science')
        self.assertIn('award line not printed', V.check_candidate(out[0], moved))


class PlanTextTests(unittest.TestCase):  # UNL 2026-2027 '4-Year Plans': printed rows, no plan table
    LINES = ['Pass/No Pass', 'Anthropology (B.A.)', '12 creditsYear 1: Fall', 'Course: Introduction to Cultural Anthropology', '3 credits',
             'Complete ANTH\u00a0212', '<', 'ACE 1: Writing', '3 credits', 'CAS 120 Total Credits (Elective or Other Degree Requirement)', '6 credits',
             'In consultation with your advisor, select elective courses.', '>', '4 creditsYear 1: Spring', 'Course: PrEP II', '1 credits', 'Complete BSAD 222',
             'Milestone: You must declare a required minor by this term.', 'ANTH 485 or ANTH 488', '3 credits', 'Career Information', 'Internships']

    def page(self, lines=None, heads=('Anthropology (B.A.)', 'Career Information')):
        from pipeline import text as T
        return T.Page('\n'.join(lines or self.LINES), 'Anthropology < University of Nebraska\u2013Lincoln', [], [], list(heads))

    def test_terms_rows_notes_and_milestones(self):
        from programs import courseleaf as CL
        [(title, terms, issues)] = CL.plantext_plans(self.page())
        self.assertEqual((title, issues), ('Anthropology (B.A.)', set()))
        self.assertEqual([(t['label'], t['credit_hours']) for t in terms], [('Year 1: Fall', '12'), ('Year 1: Spring', '4')])
        self.assertEqual(terms[0]['items'], [{'code': 'ANTH 212', 'title': 'Introduction to Cultural Anthropology', 'credits': 3},
                                             {'text': 'ACE 1: Writing', 'credits': 3},
                                             {'text': 'CAS 120 Total Credits (Elective or Other Degree Requirement)', 'credits': 6,
                                              'note': 'In consultation with your advisor, select elective courses.'}])
        self.assertEqual(terms[1]['items'], [{'code': 'BSAD 222', 'title': 'PrEP II', 'credits': 1},
                                             {'text': 'Milestone: You must declare a required minor by this term.'},
                                             {'text': 'ANTH 485 or ANTH 488', 'credits': 3}])

    def test_several_plans_keep_their_titles(self):
        from programs import courseleaf as CL
        two = self.LINES[:20] + ['Anthropology (B.S.)', '3 creditsYear 1: Fall', 'ACE 4: Science', '3 credits', 'Career Information']
        out = CL.plantext_candidates({'institution_key': 'ipeds-181464'}, {'url': 'https://catalog.unl.edu/a/', 'sha256': 's', 'fetched_at': '2026-10-08T00:00:00'},
                                     self.page(two, ('Anthropology (B.A.)', 'Anthropology (B.S.)')), '2026-2027', 'anthropology')
        self.assertEqual([(c['record']['requirement_key'], c['record']['rule_details']['source_section'], c['issues']) for c in out],
                         [('plan-anthropology-b-a', 'Anthropology (B.A.)', []), ('plan-anthropology-b-s', 'Anthropology (B.S.)', [])])
        untitled = CL.plantext_plans(self.page(two, ('Anthropology (B.A.)',)))
        self.assertEqual([sorted(i) for _, _, i in untitled], [[], ['no_plan_title']])
        self.assertEqual([t for t, _, _ in CL.plantext_plans(self.page(self.LINES, ()))], [None])  # one untitled plan is the major's
        self.assertEqual(CL.plantext_plans(self.page(self.LINES, ()))[0][2], set())

    def test_credits_and_codes(self):
        from programs import courseleaf as CL
        lines = list(self.LINES); lines[2] = '15 creditsYear 1: Fall'
        self.assertIn('term_credits_differ', CL.plantext_plans(self.page(lines))[0][2])
        lines = self.LINES[:1] + ['PLEASE NOTE', 'This document represents a sample 4-year plan for degree completion with this major.'] + self.LINES[1:]
        self.assertEqual(CL.plantext_plans(self.page(lines))[0][0], 'Anthropology (B.A.)')  # UNL prints the preamble above the title
        lines = list(self.LINES); lines[11] = 'Students usually take these courses in the fall.'
        self.assertEqual(CL.plantext_plans(self.page(lines))[0][1][0]['items'][2]['note'], 'Students usually take these courses in the fall.')
        lines = list(self.LINES); lines[16] = 'CompleteBSAD 222'  # UNL Finance prints it so
        self.assertEqual(CL.plantext_plans(self.page(lines))[0][1][1]['items'][0]['code'], 'BSAD 222')
        lines = list(self.LINES); lines[5] = 'Complete any elective course.'
        [(_, terms, issues)] = CL.plantext_plans(self.page(lines))
        self.assertEqual((terms[0]['items'][0], 'course_without_code' in issues),
                         ({'text': 'Course: Introduction to Cultural Anthropology', 'credits': 3, 'note': 'Complete any elective course.'}, True))

    def test_verify_term_headers_and_notes(self):
        from programs import courseleaf as CL, verify as V
        pg = self.page()
        [c] = CL.plantext_candidates({'institution_key': 'k'}, {'url': 'u', 'sha256': 's', 'fetched_at': '2026-10-08T00:00:00'}, pg, '2026-2027', 'anthropology')
        text = pg.text + '\nUndergraduate Catalog 2026-2027'
        self.assertEqual(V.check_candidate(c, text), [])
        self.assertIn('term header not printed: Year 1: Fall', V.check_candidate(c, text.replace('12 creditsYear 1: Fall', '12 credits Year 1: Fall')))
        self.assertIn('note of an item not verbatim', V.check_candidate(c, text.replace('select elective courses.', 'select courses.')))

    def test_page_without_a_program_reads_no_plan_grid(self):  # regression 2026-10-21: CA/NY/PA pages gained plan programs
        from unittest import mock
        from pipeline import text as T
        pg = T.Page('Undergraduate Catalog 2026-2027\nAbout the Department', 'About the Department < Example University', [], [], ['About the Department'])
        with mock.patch('programs.courseleaf.extract', return_value=[{'domain': 'academic_programs', 'record': {}}]) as ext:
            out = X._program_page_candidates({'catalog': {'platform': 'courseleaf'}}, {'institution_key': 'k'},
                                             {'url': 'https://catalog.example.edu/x/', 'sha256': 's', 'fetched_at': '2026-10-08T00:00:00'}, pg, '2026-27')
        self.assertEqual((out, ext.called), ([], False))

    def test_degree_offered_page_reads_its_plans(self):
        lines = ['Undergraduate Catalog 2026-2027', 'Arts & Sciences', 'Anthropology', 'Degree Offered: | Bachelor of Arts or Bachelor of Science'] + self.LINES
        from pipeline import text as T
        pg = T.Page('\n'.join(lines), 'Anthropology < University of Nebraska\u2013Lincoln', [{'rows': [['Degree Offered:', 'Bachelor of Arts or Bachelor of Science']]}], [],
                    ['Arts & Sciences Anthropology', 'Anthropology (B.A.)'])
        out = X._program_page_candidates({'catalog': {'platform': 'courseleaf'}}, {'institution_key': 'ipeds-181464'},
                                         {'url': 'https://catalog.unl.edu/undergraduate/arts-sciences/anthropology/', 'sha256': 's', 'fetched_at': '2026-10-08T00:00:00'}, pg, '2026-27')
        self.assertEqual([(c['extractor'], c['record']['program_key']) for c in out],
                         [('degree_offered/v1', 'anthropology-bachelor-of-arts-or-bachelor-of-science'),
                          ('courseleaf_plantext/v1', 'anthropology-bachelor-of-arts-or-bachelor-of-science')])
        # the page's Course Lists are read with their layout, keyed to its one program record
        url = 'https://catalog.unl.edu/undergraduate/arts-sciences/anthropology/'
        tgt = {'catalog': {'platform': 'courseleaf'}, '_courselists': {url: ({'url': url + '#courselist'}, ['tables'])}}
        from unittest import mock
        with mock.patch('programs.courseleaf.html_candidates', return_value=['group']) as hc:
            out = X._program_page_candidates(tgt, {'institution_key': 'ipeds-181464'}, {'url': url, 'sha256': 's', 'fetched_at': '2026-10-08T00:00:00'}, pg, '2026-27')
        self.assertEqual((out[-1], hc.call_args[0][3:6]), ('group', (['tables'], '2026-2027', 'anthropology-bachelor-of-arts-or-bachelor-of-science')))
        two = [dict(o, record=dict(o['record'], program_key=k)) for o in out[:1] for k in ('a-ba', 'a-bs')]
        with mock.patch('programs.extract.degree_offered_identity', return_value=two), mock.patch('programs.courseleaf.html_candidates', return_value=['group']) as hc:
            X._program_page_candidates(tgt, {'institution_key': 'ipeds-181464'}, {'url': url, 'sha256': 's', 'fetched_at': '2026-10-08T00:00:00'}, pg, '2026-27')
        self.assertFalse(hc.called)  # two program records: the Course Lists are not attributed by guess


class NamedHeaderYearTests(unittest.TestCase):  # SHSU 2026-27: 'Undergraduate Catalog' / '2026-2027'; print menu '2025-2026 Catalog'
    def test_named_catalog_header_beats_the_print_menu(self):
        from pipeline import text as T
        lines = ['Department of Kinesiology', 'Undergraduate Catalog', '2026-2027', 'Search Catalog', 'Download Page (PDF)',
                 '2025-2026 Catalog', 'A PDF of the 2025-2026 Catalog.', 'Cancel']
        self.assertEqual({y for y, _ in X.printed_catalog_years(T.Page('\n'.join(lines)))}, {'2026-2027'})
        self.assertEqual({y for y, _ in X.printed_catalog_years(T.Page('\n'.join(lines).replace('Undergraduate Catalog', 'Search')))}, {'2025-2026'})
        archive = ['Department of Kinesiology', 'Archived Catalogs', 'Undergraduate Catalog', '2025-2026', 'Undergraduate Catalog', '2024-2025']
        self.assertEqual(X.printed_catalog_years(T.Page('\n'.join(archive))), set())  # an archive menu is not a header


class CompletionStatus(unittest.TestCase):
    """programs/status.py: the state completion rule (docs/PROGRAM_DEPTH_COMPLETION.md)."""

    def setUp(self):
        from programs import status as S
        self.S = S; self.old = S.ROOT
        self.tmp = tempfile.TemporaryDirectory(); root = Path(self.tmp.name); S.ROOT = root
        insts = [{'institution_key': k, 'name': k.upper(), 'folder': k, 'level': lvl}
                 for k, lvl in (('big', 'four_year'), ('mid', 'four_year'), ('small', 'four_year'), ('cc', 'two_year'))]
        (root / 'pipeline/registry').mkdir(parents=True)
        (root / 'pipeline/registry/ZZ.json').write_text(json.dumps({'state': 'ZZ', 'institutions': insts}))
        ip = root / 'data/national/ipeds/2023-24/ZZ'; ip.mkdir(parents=True)
        (ip / 'admissions.csv').write_text('institution_key,enrolled\nbig,800\nmid,150\nsmall,50\ncc,5000\n')
        (root / 'programs/queue').mkdir(parents=True)
        self.root = root

    def tearDown(self):
        self.S.ROOT = self.old; self.tmp.cleanup()

    def put(self, folder, domain, recs, year='2026-27'):
        d = self.root / 'data/institutions' / folder / domain; d.mkdir(parents=True, exist_ok=True)
        (d / f'{year}.json').write_text(json.dumps({'institution_key': folder, 'academic_year': year, 'records': recs}))

    def queue(self, entries):
        (self.root / 'programs/queue/ZZ.json').write_text(json.dumps({'state': 'ZZ', 'entries': entries}))

    def covered_school(self, key, n=10, listed=10, plans=True, admission=True):
        progs = [{'program_key': f'p{i}', 'program_name': 'Computer Science' if i == 0 else f'History {i}', 'credential_level': 'bachelor',
                  'verification_status': 'verified', **({'admission_type': 'direct'} if admission and i == 0 else {})} for i in range(n)]
        self.put(key, 'academic_programs', progs)
        self.put(key, 'program_catalogs', [{'verification_status': 'verified', 'listed_bachelor_programs': listed}])
        reqs = [{'program_key': 'p0', 'requirement_kind': 'major', 'verification_status': 'verified'}]
        if plans: reqs += [{'program_key': f'p{i}', 'requirement_kind': 'program_plan', 'verification_status': 'verified'} for i in range(n)]
        self.put(key, 'degree_requirements', reqs)

    def test_untouched_state_is_not_started_and_unaccounted(self):
        s = self.S.state_status('ZZ')
        self.assertEqual(s['status'], 'not_started')
        self.assertEqual(s['four_year_institutions'], 3)  # two-year colleges are out of deep-dive scope
        self.assertEqual(len(s['unaccounted_institutions']), 3)

    def test_complete_needs_coverage_and_every_gap_queued(self):
        self.covered_school('big')
        self.queue([{'institution_key': 'mid', 'gap': 'institution', 'reason': 'bot_challenge', 'detail': 'challenge page', 'next_action': 'request access'},
                    {'institution_key': 'small', 'gap': 'institution', 'reason': 'not_yet_researched', 'next_action': 'run'}])
        s = self.S.state_status('ZZ')
        self.assertEqual(s['entering_student_share_covered'], 0.8)  # two-year enrolment is not in the denominator
        self.assertEqual(s['status'], 'in_progress')  # 'small' is only queued as not yet researched
        self.queue([{'institution_key': 'mid', 'gap': 'institution', 'reason': 'bot_challenge', 'detail': 'challenge page', 'next_action': 'request access'},
                    {'institution_key': 'small', 'gap': 'institution', 'reason': 'robots_disallowed', 'detail': 'robots.txt', 'next_action': 'ask'}])
        self.assertEqual(self.S.state_status('ZZ')['status'], 'complete')

    def test_queued_large_school_does_not_count_toward_coverage(self):
        self.covered_school('mid'); self.covered_school('small')
        self.queue([{'institution_key': 'big', 'gap': 'institution', 'reason': 'bot_challenge', 'detail': 'x', 'next_action': 'y'}])
        s = self.S.state_status('ZZ')
        self.assertEqual(s['status'], 'in_progress')
        self.assertEqual(s['unaccounted_institutions'], [])

    def test_unqueued_school_blocks_completion(self):
        self.covered_school('big'); self.covered_school('mid')
        s = self.S.state_status('ZZ')
        self.assertEqual(s['status'], 'in_progress'); self.assertEqual(s['unaccounted_institutions'], ['SMALL'])

    def test_catalog_threshold_is_ninety_percent_of_the_official_list(self):
        self.covered_school('big', n=9, listed=10)
        self.assertEqual(self.S.state_status('ZZ')['institutions'][0]['dimensions']['catalog'], 'met')
        self.covered_school('big', n=8, listed=10)
        r = self.S.state_status('ZZ')['institutions'][0]
        self.assertEqual(r['dimensions']['catalog'], 'open'); self.assertEqual(r['status'], 'partial_unqueued')

    def test_only_verified_programs_on_the_list_count(self):
        self.covered_school('big', n=10, listed=10)
        self.put('big', 'program_catalogs', [{'verification_status': 'verified', 'listed_bachelor_programs': 10, 'verified_listed_programs': 8}])
        r = self.S.state_status('ZZ')['institutions'][0]
        self.assertEqual((r['catalog_share'], r['dimensions']['catalog']), (0.8, 'open'))

    def test_a_mechanical_count_is_provisional(self):
        self.covered_school('big', n=10, listed=10)
        self.put('big', 'program_catalogs', [{'verification_status': 'verified', 'listed_bachelor_programs': 10,
                                              'notes': 'Reviewed 2026-10-06: Standing review: official current-catalog program list pages.'}])
        self.assertEqual(self.S.state_status('ZZ')['institutions'][0]['dimensions']['catalog'], 'open')

    def test_partially_verified_records_never_count_toward_the_catalog(self):
        self.put('big', 'academic_programs', [{'program_key': f'p{i}', 'program_name': f'X {i}', 'credential_level': 'bachelor',
                                               'verification_status': 'partially_verified'} for i in range(10)])
        self.put('big', 'program_catalogs', [{'verification_status': 'partially_verified', 'listed_bachelor_programs': 10}])
        r = self.S.state_status('ZZ')['institutions'][0]
        self.assertEqual(r['dimensions']['catalog'], 'open'); self.assertEqual(r['partially_verified_programs'], 10)

    def test_catalog_record_is_required_for_coverage(self):
        self.covered_school('big'); (self.root / 'data/institutions/big/program_catalogs/2026-27.json').unlink()
        self.assertEqual(self.S.state_status('ZZ')['institutions'][0]['dimensions']['catalog'], 'open')

    def test_degree_maps_and_admission_rules_open_until_met_or_queued(self):
        self.covered_school('big', plans=False, admission=False)
        r = self.S.state_status('ZZ')['institutions'][0]
        self.assertEqual((r['dimensions']['degree_maps'], r['dimensions']['admission_rules'], r['status']), ('open', 'open', 'covered_open_items'))
        self.assertEqual(r['high_value_without_admission_rule'], ['computer_science'])
        self.queue([{'institution_key': 'big', 'gap': 'degree_maps', 'reason': 'not_published', 'detail': 'no plans', 'next_action': 'recheck'},
                    {'institution_key': 'big', 'gap': 'admission_rules', 'reason': 'no_official_statement', 'detail': 'read', 'next_action': 'recheck'}])
        self.assertEqual(self.S.state_status('ZZ')['institutions'][0]['status'], 'covered')

    def test_half_of_programs_need_a_plan(self):
        self.covered_school('big', plans=False)
        self.put('big', 'degree_requirements', [{'program_key': 'p0', 'requirement_kind': 'major', 'verification_status': 'verified'}]
                 + [{'program_key': f'p{i}', 'requirement_kind': 'program_plan', 'verification_status': 'verified'} for i in range(4)])
        self.assertEqual(self.S.state_status('ZZ')['institutions'][0]['dimensions']['degree_maps'], 'open')

    def test_requirement_groups_count_only_verified_bachelors_programs(self):
        self.covered_school('big')
        self.put('big', 'academic_programs', [{'program_key': 'p0', 'program_name': 'Computer Science', 'credential_level': 'bachelor', 'verification_status': 'verified'},
                                              {'program_key': 'aas', 'program_name': 'Nursing AAS', 'credential_level': 'associate', 'verification_status': 'verified'},
                                              {'program_key': 'ba-mpa', 'program_name': 'X, BA/MPA', 'credential_level': 'bachelor', 'verification_status': 'unverified'}])
        self.put('big', 'degree_requirements', [{'program_key': k, 'requirement_kind': 'major', 'verification_status': 'verified'} for k in ('aas', 'ba-mpa')])
        r = self.S.state_status('ZZ')['institutions'][0]
        self.assertEqual((r['requirement_groups'], r['dimensions']['requirement_groups']), (0, 'open'))
        self.put('big', 'degree_requirements', [{'program_key': k, 'requirement_kind': 'major', 'verification_status': 'verified'} for k in ('aas', 'p0')])
        self.assertEqual(self.S.state_status('ZZ')['institutions'][0]['requirement_groups'], 1)

    def test_malformed_queue_entries_are_errors(self):
        self.queue([{'institution_key': 'nope', 'gap': 'catalog', 'reason': 'bot_challenge', 'detail': 'x', 'next_action': 'y'},
                    {'institution_key': 'big', 'gap': 'vibes', 'reason': 'bot_challenge', 'detail': 'x', 'next_action': 'y'},
                    {'institution_key': 'big', 'gap': 'catalog', 'reason': 'busy', 'detail': 'x', 'next_action': 'y'},
                    {'institution_key': 'big', 'gap': 'catalog', 'reason': 'bot_challenge', 'detail': 'x', 'next_action': ' '},
                    {'institution_key': 'big', 'gap': 'catalog', 'reason': 'bot_challenge', 'next_action': 'y'}])
        self.assertEqual(len(self.S.state_status('ZZ')['queue_errors']), 5)

    def test_latest_catalog_year_is_measured(self):
        self.covered_school('big')
        self.put('big', 'academic_programs', [], year='2025-26')
        self.assertEqual(self.S.state_status('ZZ')['institutions'][0]['academic_years'], ['2026-27'])

    def test_check_mode_detects_stale_status(self):
        self.covered_school('big')
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(self.S.main(['ZZ'], check=True), 1)  # never generated
            self.assertEqual(self.S.main(['ZZ']), 0)
            self.assertEqual(self.S.main(['ZZ'], check=True), 0)
            self.covered_school('mid')
            self.assertEqual(self.S.main(['ZZ'], check=True), 1)

    def test_states_with_work_finds_promoted_folders(self):
        self.assertEqual(self.S.states_with_work(), [])
        self.covered_school('mid')
        self.assertEqual(self.S.states_with_work(), ['ZZ'])


class RobotsRefusalTests(unittest.TestCase):
    """An unreachable robots.txt (no such host) is recorded as robots_unreachable, not as a robots refusal."""

    def fetcher(self, status, body=b''):
        from pipeline.crawl import Fetcher
        f = Fetcher(delay=0, timeout=1)
        f._raw = lambda url: (status, url, {}, body)
        return f

    def test_unreachable_host_is_not_a_refusal(self):
        f = self.fetcher(None)
        self.assertFalse(f.allowed('https://catalog.nosuch.edu/x'))
        self.assertEqual(f.refusal('https://catalog.nosuch.edu/x'), 'robots_unreachable')
        self.assertEqual(f.fetch('https://catalog.nosuch.edu/x')[0]['error'], 'robots_unreachable')

    def test_disallow_rule_is_a_refusal(self):
        f = self.fetcher(200, b'User-agent: *\nDisallow: /\n')
        self.assertFalse(f.allowed('https://catalog.example.edu/x'))
        self.assertEqual(f.fetch('https://catalog.example.edu/x')[0]['error'], 'disallowed_by_robots')

    def test_missing_robots_allows(self):
        self.assertTrue(self.fetcher(404).allowed('https://catalog.example.edu/x'))


class QueueSuggestTests(unittest.TestCase):
    """programs/queue_suggest.py drafts queue entries only from what the runs show."""

    def setUp(self):
        from programs import status as S
        self.S = S; self.old = S.ROOT
        self.tmp = tempfile.TemporaryDirectory(); root = Path(self.tmp.name); S.ROOT = root; self.root = root
        insts = [{'institution_key': k, 'name': k, 'folder': k, 'level': 'four_year'} for k in ('blocked', 'gone', 'quiet', 'open', 'nopages', 'weak')]
        (root / 'pipeline/registry').mkdir(parents=True)
        (root / 'pipeline/registry/ZZ.json').write_text(json.dumps({'state': 'ZZ', 'institutions': insts}))
        (root / 'data/national/ipeds/2023-24/ZZ').mkdir(parents=True)
        (root / 'data/national/ipeds/2023-24/ZZ/admissions.csv').write_text('institution_key,enrolled\nblocked,1\n')
        run = root / 'programs/runs/ZZ/r1'; (run / 'pages').mkdir(parents=True)
        rows = [{'institution_key': 'blocked', 'url': f'https://catalog.blocked.edu/p{i}', 'role': 'catalog_nav', 'error': 'blocked_bot_challenge'} for i in range(3)]
        rows += [{'institution_key': 'gone', 'url': 'https://catalog.gone.edu/', 'role': 'discover', 'error': 'disallowed_by_robots'}]
        rows += [{'institution_key': 'weak', 'url': 'https://www.weak.edu/', 'role': 'discover', 'error': 'blocked_bot_challenge'}]
        import gzip as gz
        (run / 'pages/a.json.gz').write_bytes(gz.compress(json.dumps({'text': 'Computer Science BS\\nMajor requirements'}).encode()))
        rows += [{'institution_key': 'open', 'url': 'https://catalog.open.edu/cs', 'role': 'program_page', 'page_file': 'a.json.gz'}]
        (run / 'manifest.jsonl').write_text('\n'.join(json.dumps(r) for r in rows) + '\n')
        (run / 'evidence.jsonl').write_text(''); (run / 'candidates.jsonl').write_text('')
        d = root / 'data/institutions/open/academic_programs'; d.mkdir(parents=True)
        (d / '2026-27.json').write_text(json.dumps({'institution_key': 'open', 'academic_year': '2026-27', 'records': [
            {'program_key': 'cs', 'program_name': 'Computer Science BS', 'credential_level': 'bachelor', 'verification_status': 'verified'}]}))
        d = root / 'data/institutions/nopages/academic_programs'; d.mkdir(parents=True)
        (d / '2026-27.json').write_text(json.dumps({'institution_key': 'nopages', 'academic_year': '2026-27', 'records': [
            {'program_key': 'h', 'program_name': 'History BA', 'credential_level': 'bachelor', 'verification_status': 'verified'}]}))

    def tearDown(self):
        self.S.ROOT = self.old; self.tmp.cleanup()

    def test_proposals_follow_run_evidence(self):
        from programs import queue_suggest as Q
        got = {(e['institution_key'], e['gap']): e['reason'] for e in Q.suggest('ZZ')}
        self.assertEqual(got[('blocked', 'institution')], 'bot_challenge')
        self.assertEqual(got[('gone', 'institution')], 'not_yet_researched')  # a refused/unreachable host proves nothing
        self.assertEqual(got[('quiet', 'institution')], 'not_yet_researched')
        self.assertEqual(got[('weak', 'institution')], 'not_yet_researched')  # one challenged request proves nothing
        self.assertEqual(got[('open', 'degree_maps')], 'not_published')       # its program page was read: no plan marker
        self.assertEqual(got[('open', 'admission_rules')], 'no_official_statement')
        self.assertEqual(got[('open', 'catalog')], 'not_yet_researched')
        self.assertEqual(got[('open', 'requirement_groups')], 'not_yet_researched')
        self.assertEqual(got[('nopages', 'degree_maps')], 'not_yet_researched')  # no page read: absence is not shown

    def test_committed_queue_entries_are_not_proposed_again(self):
        from programs import queue_suggest as Q
        (self.root / 'programs/queue').mkdir(parents=True)
        (self.root / 'programs/queue/ZZ.json').write_text(json.dumps({'state': 'ZZ', 'entries': [
            {'institution_key': 'blocked', 'gap': 'institution', 'reason': 'bot_challenge', 'detail': 'x', 'next_action': 'y'}]}))
        self.assertNotIn('blocked', {e['institution_key'] for e in Q.suggest('ZZ')})
        self.assertNotIn('ZZ.proposed', self.S.states_with_work())


class BranchCampusListTests(unittest.TestCase):
    def test_only_rows_tagged_with_the_campus_are_followed(self):
        t = {'catalog': {'platform': 'courseleaf', 'home': 'https://catalog.example.edu/', 'path_prefix': '/college-departments/',
                         'min_depth': 1, 'program_lists': ['https://catalog.example.edu/programs/'], 'list_filter': 'Branch'}}
        links = [('https://catalog.example.edu/college-departments/a/x-bs/', 'X Undergraduate Major (BS)MajorCorvallisBranch'),
                 ('https://catalog.example.edu/college-departments/a/y-bs/', 'Y Undergraduate Major (BS)MajorCorvallis')]
        pushed = []
        C.expand(t, 'program_list', 'u', links, lambda h, r, v, d: pushed.append(h), C.program_rule(t), C.nav_rule(t), 0)
        self.assertEqual(pushed, ['https://catalog.example.edu/college-departments/a/x-bs/'])


class CrawlDelayTests(unittest.TestCase):
    def test_reviewed_config_hosts_join_the_target_hosts(self):
        # Texas State's catalog is on mycatalog.txstate.edu, another official domain than the registry's txst.edu
        import shutil, subprocess, sys, tempfile
        root = Path(__file__).resolve().parent.parent
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            for rel in ('programs/build_targets.py', 'pipeline/registry/TX.json', 'pipeline/registry/TN.json', 'pipeline/registry/OR.json',
                        'data/national/ipeds/2023-24/TX/admissions.csv', 'data/national/ipeds/2023-24/TN/admissions.csv',
                        'data/national/ipeds/2023-24/OR/admissions.csv'):
                if (root / rel).exists(): (d / rel).parent.mkdir(parents=True, exist_ok=True); shutil.copy(root / rel, d / rel)
            (d / 'programs/targets/configs').mkdir(parents=True)
            cfg = {'txst': {'catalog': {'home': 'https://mycatalog.txstate.edu/', 'platform': 'courseleaf', 'path_prefix': '/undergraduate/',
                                        'min_depth': 1, 'program_lists': []}, 'hosts': ['mycatalog.txstate.edu'], 'reviewed': True}}
            (d / 'programs/targets/configs/TX.json').write_text(json.dumps(cfg))
            subprocess.run([sys.executable, str(d / 'programs/build_targets.py'), 'TX'], check=True, capture_output=True)
            t = [x for x in json.loads((d / 'programs/targets/TX.json').read_text())['institutions'] if x['folder'] == 'txst'][0]
            self.assertIn('mycatalog.txstate.edu', t['hosts'])
            self.assertNotIn('extra_hosts', t)
            self.assertEqual(t['mode'], 'catalog')

    def test_target_crawl_delay_slows_its_catalog_host(self):
        from pipeline.crawl import Fetcher, Run
        f = Fetcher(delay=0, timeout=1); f._raw = lambda url: (None, url, {}, b'')
        with tempfile.TemporaryDirectory() as d:
            t = {'institution_key': 'k', 'folder': 'k', 'domains': ['example.edu'], 'crawl_delay': 12,
                 'catalog': {'platform': 'acalog', 'home': 'https://catalog.example.edu/index.php?catoid=1', 'catoid': 1}}
            C.crawl_target(t, Run(Path(d)), f, log=lambda *_: None)
        self.assertEqual(f.gate.host_delay.get('catalog.example.edu'), 12)


class DetectTests(unittest.TestCase):
    """programs/detect.py: catalog platform from official links on stored discovery pages."""

    def test_catalog_host_spellings(self):
        from programs.detect import catalog_host
        for h in ('catalog.x.edu', 'catalogs.rutgers.edu', 'bulletin.brown.edu', 'catalogue.uvm.edu', 'e-catalogue.jhu.edu', 'academiccatalog.umd.edu'):
            self.assertTrue(catalog_host(h), h)
        for h in ('www.uvm.edu', 'mycatalogue.x.edu', 'catalogsearch-tool.x.com'):
            self.assertFalse(catalog_host(h), h)
        cfg, why = self.det([('https://catalogue.uvm.edu/undergraduate/majors/', 'Majors')], url='https://catalogue.uvm.edu/undergraduate/')
        self.assertEqual((cfg['platform'], cfg['program_lists']), ('courseleaf', ['https://catalogue.uvm.edu/undergraduate/majors/']))

    def test_shared_catalog_kept_only_for_the_institution_that_owns_its_host(self):
        from programs import detect as D
        cat = lambda home: {'catalog': {'platform': 'acalog', 'home': home, 'catoid': 4}}
        insts = {f: {'seeds': {'website': w}} for f, w in [('manoa', 'https://manoa.hawaii.edu/'), ('hilo', 'https://hilo.hawaii.edu/'),
                 ('maui', 'https://maui.hawaii.edu/'), ('unh', 'https://www.unh.edu/'), ('manchester', 'https://manchester.unh.edu/'),
                 ('h1', 'https://www.herzing.edu/'), ('h2', 'https://www.herzing.edu/'), ('solo', 'https://www.solo.edu/')]}
        m = 'https://catalog.manoa.hawaii.edu/index.php?catoid=4'
        cfgs = {'manoa': cat(m), 'hilo': cat(m), 'maui': cat(m), 'unh': cat('https://catalog.unh.edu/'), 'manchester': cat('https://catalog.unh.edu/'),
                'h1': cat('https://catalog.herzing.edu/'), 'h2': cat('https://catalog.herzing.edu/'), 'solo': cat('https://catalog.other.edu/')}
        drop = D.shared_catalogs(cfgs, insts)
        self.assertEqual(sorted(drop), ['h1', 'h2', 'hilo', 'manchester', 'maui'])
        self.assertIn('belongs to manoa', drop['hilo'])
        cfgs['h1']['reviewed'] = True
        self.assertNotIn('h1', D.shared_catalogs(cfgs, insts))

    def test_shared_catalog_attributed_across_states(self):
        import tempfile, pathlib
        from programs import detect as D
        cat = {'catalog': {'platform': 'courseleaf', 'home': 'https://catalog.northeastern.edu/'}}
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            (root / 'programs/targets/configs').mkdir(parents=True); (root / 'pipeline/registry').mkdir(parents=True)
            (root / 'programs/targets/configs/MA.json').write_text(json.dumps({'northeastern': cat}))
            (root / 'pipeline/registry/MA.json').write_text(json.dumps({'institutions': [
                {'folder': 'northeastern', 'seeds': {'website': 'https://www.northeastern.edu/'}}]}))
            mills = [{'folder': 'mills', 'seeds': {'website': 'https://www.mills.edu/'}},
                     {'folder': 'own', 'seeds': {'website': 'https://www.own.edu/'}}]
            out = {'mills': cat, 'own': {'catalog': {'platform': 'acalog', 'home': 'https://catalog.own.edu/'}}}
            drop = D.shared_across_states('CA', out, mills, root=root)
            self.assertEqual(list(drop), ['mills'])
            self.assertIn('MA:northeastern', drop['mills'])
            # the owning state is never dropped when it is the one being detected
            self.assertEqual(D.shared_across_states('MA', {'northeastern': cat}, [{'folder': 'northeastern', 'seeds': {'website': 'https://www.northeastern.edu/'}}], root=root), {})

    def det(self, links, title='', text='', url='https://www.x.edu/'):
        from programs import detect as D
        return D.detect_institution([({'url': url}, {'title': title, 'text': text, 'links': links})])

    def test_acalog_current_catalog_is_the_year_labelled_one(self):
        cfg, why = self.det([('https://catalog.x.edu/index.php?catoid=70', '2024-2025 Undergraduate Catalog [ARCHIVED CATALOG]'),
                             ('https://catalog.x.edu/content.php?catoid=70&navoid=3', 'Archived 2024-2025'),
                             ('https://catalog.x.edu/content.php?catoid=70&navoid=4', 'Archived'), ('https://catalog.x.edu/content.php?catoid=70&navoid=5', 'Archived'),
                             ('https://catalog.x.edu/index.php?catoid=40', '2024-2025 Undergraduate Catalog [ARCHIVED CATALOG]'),
                             ('https://catalog.x.edu/index.php?catoid=56', '2026-2027 Undergraduate Catalog'),
                             ('https://catalog.x.edu/content.php?catoid=56&navoid=900', 'Programs A-Z'),
                             ('https://catalog.x.edu/content.php?catoid=56&navoid=901', 'Graduate Programs'),
                             ('https://catalog.x.edu/content.php?catoid=40&navoid=12', 'Programs')])
        self.assertEqual((cfg['platform'], cfg['catoid'], cfg['program_lists']), ('acalog', 56, ['https://catalog.x.edu/content.php?catoid=56&navoid=900']))

    def test_undated_acalog_left_behind_loses_to_the_new_platform(self):
        cfg, _ = self.det([('https://catalog.x.edu/index.php?catoid=27', 'Catalog')] +
                          [(f'https://undergrad.catalog.x.edu/programs/P{i}', f'Prog {i}') for i in range(4)])
        self.assertEqual(cfg['platform'], 'coursedog')

    def test_smartcatalog_newest_year_path(self):
        cfg, _ = self.det([('https://x.smartcatalogiq.com/en/2025-2026/catalog/a', 'a'), ('https://x.smartcatalogiq.com/en/2026-2027/catalog/b', 'b')])
        self.assertEqual(cfg['home'], 'https://x.smartcatalogiq.com/en/2026-2027/catalog/')

    def test_catalog_pdf_needs_a_year_and_is_not_graduate(self):
        cfg, _ = self.det([('https://www.x.edu/files/2026-2027-Graduate-Catalog.pdf', 'Graduate Catalog'),
                           ('https://www.x.edu/files/2026-27-Catalog.pdf', 'Academic Catalog'), ('https://www.x.edu/files/catalog.pdf', 'Catalog')])
        self.assertEqual(cfg['catalog_pdfs'], ['https://www.x.edu/files/2026-27-Catalog.pdf'])

    def test_undated_pdf_is_not_a_catalog(self):
        self.assertIsNone(self.det([('https://www.x.edu/files/catalog.pdf', 'Catalog')])[0])

    def test_nothing_recognised(self):
        self.assertIsNone(self.det([('https://www.x.edu/about', 'About')])[0])


class DiscoverCapsTests(unittest.TestCase):
    def test_discovery_does_not_follow_degree_maps_or_policy_links(self):
        from pipeline.crawl import Fetcher, Run
        f = Fetcher(delay=0, timeout=1)
        body = (b'<html><head><title>X University</title></head><body><a href="https://www.x.edu/catalog/">Academic Catalog</a>'
                b'<a href="https://www.x.edu/maps/four-year-plans.pdf">Four-Year Plans</a><a href="https://www.x.edu/advising/maps">Degree Maps</a></body></html>')
        f._raw = lambda url: (200, url, {'Content-Type': 'text/html'}, body if not url.endswith('robots.txt') else b'')
        with tempfile.TemporaryDirectory() as d:
            t = {'institution_key': 'k', 'folder': 'k', 'domains': ['x.edu'], 'mode': 'discover', 'discover': ['https://www.x.edu/']}
            run = C.crawl_target(t, Run(Path(d)), f, log=lambda *_: None) or Run(Path(d))
            roles = {e['url']: e['role'] for e in Run(Path(d)).entries()}
        self.assertEqual(roles.get('https://www.x.edu/catalog/'), 'discover')
        self.assertNotIn('https://www.x.edu/maps/four-year-plans.pdf', roles)
        self.assertNotIn('https://www.x.edu/advising/maps', roles)


class AutoReviewTests(unittest.TestCase):
    """programs/autoreview.py: the standing review rules for production states."""

    def run_dir(self, cands, verify=None, lists=None):
        d = Path(tempfile.mkdtemp())
        (d / 'candidates.jsonl').write_text('\n'.join(json.dumps(c) for c in cands) + '\n')
        (d / 'verify.json').write_text(json.dumps(verify or {}))
        (d / 'program_lists.json').write_text(json.dumps(lists or {}))
        (d / 'manifest.jsonl').write_text('')
        return d

    def prog(self, cid, name, ext='catalog_program/v1', issues=(), level='bachelor', year='2026-27', key=None):
        return {'candidate_id': cid, 'domain': 'academic_programs', 'extractor': ext, 'issues': list(issues), 'institution_key': 'k',
                'academic_year': year, 'record': {'program_key': key or cid, 'program_name': name, 'credential_level': level, 'catalog_year': '2026-2027'}}

    def req(self, cid, pk, kind='major', ext='courselist_html/v1', issues=()):
        return {'candidate_id': cid, 'domain': 'degree_requirements', 'extractor': ext, 'issues': list(issues), 'institution_key': 'k',
                'academic_year': '2026-27', 'record': {'program_key': pk, 'requirement_kind': kind}}

    def test_standing_rules(self):
        from programs import autoreview as A
        from datetime import date
        cands = [self.prog('ok', 'Biology (BA)'), self.prog('iss', 'Chemistry (BS)', issues=['stale_year_label:2025-26']),
                 self.prog('untr', 'Physics (BS)', ext='thec_inventory/v1'), self.prog('opt', 'Business, Marketing Option, BS'),
                 self.prog('comb', 'Accelerated Bachelor\'s + JD'), self.prog('ms', 'History (MA)', level='master'),
                 self.prog('old', 'Art (BA)', year='2025-26'), self.prog('bad', 'Music (BA)'), self.prog('dup', 'Biology (BA)', key='ok'),
                 self.req('g1', 'ok'), self.req('g2', 'ok', issues=['indented_rows_without_rule']), self.req('g3', 'ok', ext='smartcatalog_program/v1'),
                 self.req('g4', 'iss'), self.req('p1', 'ok', kind='program_plan', ext='courseleaf_plan/v1'),
                 self.prog('v1', 'Architecture (Foundation Unit) – BArch'), self.prog('v2', 'Architecture (Summer Design) – BArch'),
                 self.prog('ba', 'Biology (BA)'), self.prog('bs', 'Biology (BS)'),
                 self.prog('mba', 'Business Administration, M.B.A.'), self.prog('fin', 'Finance, B.S.B.A.'), self.prog('fin2', 'Finance, B.S.B.A. (Online Cohort)')]
        d = self.run_dir(cands, verify={'bad': ['program_name not verbatim']})
        old = A.catalog_records; A.catalog_records = lambda *a: []  # catalog records need a targets file; tested separately
        try: approve, cats, held = A.review('ZZ', d, today=date(2026, 10, 6))
        finally: A.catalog_records = old
        self.assertEqual({a['candidate_id'] for a in approve}, {'ok', 'g1', 'ba', 'bs', 'fin'})  # courseleaf_plan/v1 is no longer trusted (#229)
        self.assertEqual(held['issues'], 1); self.assertEqual(held['option_name'], 1); self.assertEqual(held['combined_program'], 1)
        self.assertEqual(held['entry_path_variant'], 3)
        self.assertEqual(held['not_verbatim'], 1); self.assertEqual(held['duplicate'], 1); self.assertEqual(held['req_program_not_approved'], 1)

    def test_kuali_page_records_are_trusted(self):  # BYU 2026-27: 120 records reviewed by hand before the reader was trusted
        from programs import autoreview as A
        from datetime import date
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try: approve, _, held = A.review('ZZ', self.run_dir([self.prog('b', 'Applied English Linguistics (BA)', ext='kuali_page/v1')]), today=date(2026, 10, 6))
        finally: A.catalog_records = old
        self.assertEqual([a['candidate_id'] for a in approve], ['b'])
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try: approve, _, held = A.review('ZZ', self.run_dir([self.prog('m', 'Major in Anthropology', ext='award_link_major/v1')]), today=date(2026, 10, 6))
        finally: A.catalog_records = old
        self.assertEqual([a['candidate_id'] for a in approve], ['m'])  # Colorado State 2026-10-08: 20 of 60 sampled, 20 right
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try: approve, _, held = A.review('ZZ', self.run_dir([self.prog('u', 'Animation and Games (BA)', ext='edition_program/v1')]), today=date(2026, 10, 6))
        finally: A.catalog_records = old
        self.assertEqual([a['candidate_id'] for a in approve], ['u'])  # UT Dallas 2026-10-08

    def test_options_of_a_listed_degree_are_held(self):  # Oklahoma State 2026-27: 'Zoology: Pre-Medical Sciences, BS' beside 'Zoology, BS'
        from programs import autoreview as A
        from datetime import date
        def at(c, url): c['record']['program_url'] = url; return c
        cands = [at(self.prog('z', 'Zoology, BS', key='zoology-bs'), 'https://a/zoo'),
                 at(self.prog('zp', 'Zoology: Pre-Medical Sciences, BS', key='zoology-pre-medical-sciences-bs'), 'https://a/zoo-premed'),
                 at(self.prog('n', 'Natural Resource Ecology: Fisheries, BSAG', key='nre-fish-bsag'), 'https://a/nre-fish')]
        lists = {'k': {'programs': [{'listed_as': 'bachelor', 'printed': p, 'url': u} for p, u in
                                    (('Zoology, BS', 'https://a/zoo'), ('Zoology: Pre-Medical Sciences, BS', 'https://a/zoo-premed'),
                                     ('Natural Resource Ecology: Fisheries, BSAG', 'https://a/nre-fish'))]}}
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try: approve, _, held = A.review('ZZ', self.run_dir(cands, lists=lists), today=date(2026, 10, 6))
        finally: A.catalog_records = old
        self.assertEqual(sorted(a['candidate_id'] for a in approve), ['n', 'z'])  # no 'Natural Resource Ecology, BSAG' line: kept
        self.assertEqual(held['listed_option'], 1)

    def test_listed_variant_lines_are_the_degree(self):  # UT Arlington 2026-27: 'Data Science BS (Biology)', no 'Data Science BS' line
        from programs import autoreview as A
        from datetime import date
        def at(c, url): c['record']['program_url'] = url; return c
        mk = lambda: [at(self.prog('d1', 'Data Science BS (Biology)', key='ds-bio'), 'https://a/ds-bio'),
                      at(self.prog('d2', 'Data Science BS (Computer Science)', key='ds-cs'), 'https://a/ds-cs')]
        lists = {'k': {'programs': [{'listed_as': 'bachelor', 'printed': 'Data Science BS (Biology)', 'url': 'https://a/ds-bio'},
                                    {'listed_as': 'bachelor', 'printed': 'Data Science BS (Computer Science)', 'url': 'https://a/ds-cs'}]}}
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try:
            approve, _, held = A.review('ZZ', self.run_dir(mk(), lists=lists), today=date(2026, 10, 6))
            self.assertEqual([a['candidate_id'] for a in approve], ['d1', 'd2'])  # each listed line is a listed program
            # with the base line printed, the variants stay held
            lists['k']['programs'].append({'listed_as': 'bachelor', 'printed': 'Data Science BS', 'url': 'https://a/ds'})
            approve, _, held = A.review('ZZ', self.run_dir(mk(), lists=lists), today=date(2026, 10, 6))
            self.assertEqual(approve, []); self.assertEqual(held['entry_path_variant'], 2)
            # TAMUK 2026-27 prints the variant as the page heading too ('Kinesiology, B.S. (Sport Business)'): that heading is
            # not a page of the base degree, so the listed variants stay the degree's records
            km = lambda: [at(self.prog('k1', 'Kinesiology, B.S. (Sport Business)', key='kin-sb'), 'https://a/kin-sb'),
                          at(self.prog('k2', 'Kinesiology, B.S. (Sport and Leisure Studies)', key='kin-sls'), 'https://a/kin-sls')]
            kl = {'k': {'programs': [{'listed_as': 'bachelor', 'printed': 'Kinesiology, B.S. (Sport Business)', 'url': 'https://a/kin-sb'},
                                     {'listed_as': 'bachelor', 'printed': 'Kinesiology, B.S. (Sport and Leisure Studies)', 'url': 'https://a/kin-sls'}]}}
            approve, _, held = A.review('ZZ', self.run_dir(km(), lists=kl), today=date(2026, 10, 6))
            self.assertEqual([a['candidate_id'] for a in approve], ['k1', 'k2'])
            # a page of the base degree of its own ('Kinesiology, B.S.') keeps the variants as options
            approve, _, held = A.review('ZZ', self.run_dir(km() + [at(self.prog('k0', 'Kinesiology, B.S.', key='kin'), 'https://a/kin')], lists=kl), today=date(2026, 10, 6))
            self.assertEqual([a['candidate_id'] for a in approve], ['k0'])
        finally: A.catalog_records = old

    def test_listed_campus_variants_are_the_degree(self):  # Cal Poly 2026-2028: 'Mechanical Engineering (BS) (Solano Campus)'
        from programs import autoreview as A
        from datetime import date
        def at(c, url): c['record']['program_url'] = url; return c
        mk = lambda: [at(self.prog('m1', 'Mechanical Engineering (BS) (San Luis Obispo Campus)', key='me-slo'), 'https://a/me-slo'),
                      at(self.prog('m2', 'Mechanical Engineering (BS) (Solano Campus)', key='me-sol'), 'https://a/me-sol')]
        lists = {'k': {'programs': [{'listed_as': 'bachelor', 'printed': 'Mechanical Engineering (BS) (San Luis Obispo Campus)', 'url': 'https://a/me-slo'},
                                    {'listed_as': 'bachelor', 'printed': 'Mechanical Engineering (BS) (Solano Campus)', 'url': 'https://a/me-sol'}]}}
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try:
            approve, _, held = A.review('ZZ', self.run_dir(mk(), lists=lists), today=date(2026, 10, 7))
            self.assertEqual([a['candidate_id'] for a in approve], ['m1', 'm2'])
            lists['k']['programs'].append({'listed_as': 'bachelor', 'printed': 'Mechanical Engineering (BS)', 'url': 'https://a/me'})
            approve, _, held = A.review('ZZ', self.run_dir(mk(), lists=lists), today=date(2026, 10, 7))
            self.assertEqual(approve, []); self.assertEqual(held['entry_path_variant'], 2)
        finally: A.catalog_records = old

    def test_one_program_on_several_pages_comes_from_the_base_page(self):
        from programs import autoreview as A
        from datetime import date
        U = 'https://catalog.x.edu/undergraduate/sci/'
        def at(c, url, field='program_url'): c['record'][field] = url; return c
        cands = [at(self.prog('u0', 'Agricultural Education', key='aec'), 'https://catalog.x.edu/UGRD/UGAGL/AEC_BS/'),
                 at(self.prog('u1', 'Agricultural Education', key='aec'), 'https://catalog.x.edu/UGRD/UGAGL/AEC_BS_UFO/'),
                 at(self.prog('b1', 'Biology, BS', key='bio'), U + 'biology/biology-bs-pre-professional/'),
                 at(self.prog('b0', 'Biology, BS', key='bio'), U + 'biology/biology-bs/'),
                 at(self.req('rb1', 'bio'), U + 'biology/biology-bs-pre-professional/', 'source_url'),
                 at(self.req('rb0', 'bio'), U + 'biology/biology-bs/#courselist', 'source_url'),
                 # tracks with no plain page: no record (Liberty's online tracks)
                 at(self.prog('t1', 'Bible, BS', key='bible'), U + 'bible-major-bs/bible-bs-apologetics-online'),
                 at(self.prog('t2', 'Bible, BS', key='bible'), U + 'bible-major-bs/bible-bs-exposition-online'),
                 # department page and its award page; a cross-listed copy; a Coursedog default pathway: one page each
                 at(self.prog('a1', 'Asian Studies (BA)', key='asia'), U + 'asian-studies'),
                 at(self.prog('a2', 'Asian Studies (BA)', key='asia'), U + 'asian-studies-ba'),
                 at(self.prog('x1', 'Dance, BA', key='dance'), 'https://catalog.x.edu/arts/dance-ba/'),
                 at(self.prog('x2', 'Dance, BA', key='dance'), 'https://catalog.x.edu/ugrad/arts/dance-ba/'),
                 at(self.prog('w1', 'Art (BA)', key='art'), 'https://catalog.x.edu/programs/BA.ART'),
                 at(self.prog('w2', 'Art (BA)', key='art'), 'https://catalog.x.edu/programs/BA.ART/general-aoYks')]
        d = self.run_dir(cands)
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try: approve, cats, held = A.review('ZZ', d, today=date(2026, 10, 6))
        finally: A.catalog_records = old
        self.assertEqual({a['candidate_id'] for a in approve}, {'u0', 'b0', 'rb0', 'a1', 'x1', 'w1'})  # UF Online copy 'AEC_BS_UFO' held
        self.assertEqual(held['variant_page'], 4); self.assertEqual(held['req_variant_page'], 1); self.assertEqual(held['duplicate'], 3)


class DegreeTypeTests(unittest.TestCase):
    def test_one_stated_degree_type(self):  # NDSU 2026-27 'Accounting Major' / 'Degree Type: B.S.'
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/curriculum/undergraduate/accounting-major/', 'role': 'program_page', 'sha256': 'a' * 64,
             'fetched_at': '2026-10-06T00:00:00+00:00', 'kind': 'html'}
        body = 'University Catalog 2026-2027\n2026-2027 Edition\nAccounting Major\nDegree Type: B.S.\nMinimum credits required: 120'
        tgt = {'catalog': {'platform': 'courseleaf'}}
        out = X.program_page_candidates(tgt, {'institution_key': 'k'}, e, T.Page(body, 'Accounting Major < X University', [], [], ['Accounting Major']), '2026-27')
        self.assertEqual([(c['extractor'], c['record']['program_name'], c['evidence'][1]['snippet']) for c in out],
                         [('stated_major/v1', 'Accounting Major', 'Degree Type: B.S.')])
        two = body + '\nDegree Type: B.A.'
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, T.Page(two, 'Accounting Major < X', [], [], ['Accounting Major']), '2026-27'), [])
        pb = T.Page(body.replace('Accounting Major', 'Nursing Post Baccalaureate Major'), 'Nursing Post Baccalaureate Major < X', [], [], [])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, pb, '2026-27'), [])
        inline = T.Page(body.replace('Degree Type: B.S.', 'The Degree Type: B.S. is not offered'), 'Accounting Major < X', [], [], [])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, inline, '2026-27'), [])  # a whole line only


class HeadingProgramTests(unittest.TestCase):
    def test_award_heading_without_course_list_tables(self):  # UNI 2026-27: 'Physics B.S.' under '2026-27 University Catalog'
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/chas/physicsbs/', 'role': 'program_page', 'sha256': 'a' * 64, 'fetched_at': '2026-10-06T00:00:00+00:00', 'kind': 'html'}
        tgt = {'catalog': {'platform': 'courseleaf'}}
        page = T.Page('2026-27 University Catalog\nPhysics B.S.\nFour-Year Plan', 'Physics B.S. | X University Catalog', [], [], ['Physics B.S.', 'Four-Year Plan'])
        self.assertEqual({y for y, _ in X.printed_catalog_years(page)}, {'2026-2027'})
        out = X.program_page_candidates(tgt, {'institution_key': 'k'}, e, page, '2026-27')
        self.assertEqual([(c['extractor'], c['record']['program_name']) for c in out], [('static_program/v1', 'Physics B.S.')])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, T.Page(page.text, 't', [], [], ['Physics Minor']), '2026-27'), [])
        emph = T.Page('2026-27 University Catalog\nArt: Art History B.A.\nArt: History Emphasis, B.A.', 't', [], [], ['Art: Art History B.A.'])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, emph, '2026-27'), [])
        dual = T.Page('2026-27 University Catalog\nMiddle Level Education Dual Major - Teaching B.A.', 't', [], [], ['Middle Level Education Dual Major - Teaching B.A.'])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, dual, '2026-27'), [])


class DegreeLineTests(unittest.TestCase):
    def test_uf_degree_line(self):  # UF 2026-27
        from pipeline import text as T
        tgt = {'catalog': {'platform': 'courseleaf'}}
        def run(url, heads, body):
            e = {'url': url, 'role': 'program_page', 'sha256': 'a' * 64, 'fetched_at': '2026-10-06T00:00:00+00:00', 'kind': 'html'}
            page = T.Page(heads[0] + '\n' + body + '\nAll pages in 2026-2027 Academic Catalog.', heads[0] + ' | University of X Catalog', [], [], heads)
            return [(c['extractor'], c['record']['program_name'], c['record']['program_key']) for c in X.program_page_candidates(tgt, {'institution_key': 'k'}, e, page, '2026-27')]
        U = 'https://catalog.x.edu/UGRD/colleges-schools/UGACT/'
        self.assertEqual(run(U + 'ACT_BSAC/', ['Accounting', 'Curriculum'], 'Degree: Bachelor of Science in Accounting'),
                         [('degree_line/v1', 'Accounting', 'accounting-bachelor-of-science-in-accounting')])
        self.assertEqual(run(U + 'BLY_BS/BLY_BS01/', ['Applied Biology'], 'Degree: Bachelor of Science'), [])  # a specialization page
        self.assertEqual(run(U + 'ACT_BSAC/', ['Accounting'], 'Degree: Bachelor of Science\nDegree: Bachelor of Arts'), [])  # two awards
        self.assertEqual(run(U + 'ACT_MIN/', ['Accounting Minor'], 'Degree: Bachelor of Science'), [])
        self.assertEqual(run(U + 'ACT_BSAC/', ['Accounting'], 'The Degree: Bachelor of Science is common'), [])  # a whole line only


class DegreePageTests(unittest.TestCase):  # JHU 2026-27 (Research request in #151)
    def test_the_degree_page_is_the_programs_page(self):
        from programs.autoreview import degree_page
        j = 'https://e-catalogue.jhu.edu/'
        self.assertEqual(degree_page({j + 'as/archaeology-ugrad-major/', j + 'as/archaeology-ugrad-major/archaeology-bachelor-arts/'}),
                         j + 'as/archaeology-ugrad-major/archaeology-bachelor-arts/')
        self.assertEqual(degree_page({j + 'eng/engineering-professionals/civil-engineering/', j + 'eng/ft/civil-engineering/civil-engineering-bachelor-science/'}),
                         j + 'eng/ft/civil-engineering/civil-engineering-bachelor-science/')
        self.assertIsNone(degree_page({j + 'p/guitar-bachelor-music/', j + 'p/piano-bachelor-music/'}))  # two degree pages: none chosen
        self.assertIsNone(degree_page({j + 'a/history/', j + 'b/history/'}))
        self.assertEqual(degree_page({j + 'x/biology/', j + 'x/biology/biology-bs/'}), j + 'x/biology/biology-bs/')
        from programs.autoreview import variant_pages_of
        self.assertEqual(variant_pages_of([{j + 'as/archaeology-ugrad-major', j + 'as/archaeology-ugrad-major/archaeology-bachelor-arts'}, {j + 'z/only'}]), {j + 'as/archaeology-ugrad-major'})
        self.assertEqual(variant_pages_of([{j + 'b/biology-bs', j + 'b/biology-bs-pre-professional'}]), {j + 'b/biology-bs-pre-professional'})
        self.assertEqual(variant_pages_of([{j + 'c/asian-studies', j + 'c/asian-studies-ba'}]), set())  # one base page: both are that page
        self.assertEqual(variant_pages_of([{j + 'u/ABC', j + 'u/ABC_HON'}]), {j + 'u/ABC_HON'})  # underscore extensions of a base page
        # Georgia Tech 2026-27: thread pages put the qualifier before the base name ('media-people-computer-science-bs')
        gt = {j + 'p/computer-science-bs', j + 'p/media-people-computer-science-bs', j + 'p/computer-science-theory-bs'}
        self.assertEqual(variant_pages_of([gt]), gt - {j + 'p/computer-science-bs'})
        self.assertEqual(variant_pages_of([{j + 'p/biology-bs', j + 'p/marine-science-bs'}]), {j + 'p/biology-bs', j + 'p/marine-science-bs'})  # no base page


class SamplePlanPageTests(unittest.TestCase):  # KU 2026-27 sample-plan sub-pages; PVAMU award abbreviations (review of 2026-10-07)
    def test_sample_plan_sub_page_gives_no_program_record(self):
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/las/anthropology/ba-bgs/ba-anthropology/', 'role': 'program_page', 'sha256': 'a' * 64,
             'fetched_at': '2026-10-06T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        tgt = {'catalog': {'platform': 'courseleaf'}}
        body = '2026-2027 Academic Catalog\nBA in Anthropology\n'
        page = T.Page(body + 'The Department of Anthropology offers a BA.', 'BA in Anthropology', [], [], ['BA in Anthropology'])
        self.assertTrue([c for c in X.program_page_candidates(tgt, {'institution_key': 'k'}, e, page, '2026-27') if c['domain'] == 'academic_programs'])
        plan = T.Page(body + 'Below is a sample 4-year plan for students pursuing the BA in Anthropology.', 'BA in Anthropology', [], [], ['BA in Anthropology'])
        self.assertEqual([c for c in X.program_page_candidates(tgt, {'institution_key': 'k'}, e, plan, '2026-27') if c['domain'] == 'academic_programs'], [])
        # KU Chemistry: 'Below is a sample 4-year plan for the American Chemical Society Certified BS degree'; Child Life: a
        # suspension notice between the heading and the sentence
        for t in ('Below is a sample 4-year plan for the American Chemical Society Certified BA degree in Anthropology.',
                  'The recommended 4-year plan is listed below by semester to semester enrollment.',  # KU Civil Engineering
                  'Admission to this program has been suspended for the 2026-2027 academic year.\nBelow is a sample 4-year plan for students pursuing the BA.'):
            p = T.Page(body + t, 'BA in Anthropology', [], [], ['2026-27 Academic Catalog', 'BA in Anthropology'])  # KU's year heading first
            self.assertEqual([c for c in X.program_page_candidates(tgt, {'institution_key': 'k'}, e, p, '2026-27') if c['domain'] == 'academic_programs'], [], t)
        # the degree page itself: the sentence follows the requirements (KU Theatre Design's 'Major Junior/Senior Hours')
        deg = T.Page(body + 'Requirements\nMajor Junior/Senior Hours\nStudents must earn 30 hours.\nBelow is a sample 4-year plan for students pursuing the BA.'
                     '\nGrades of C- or Better\nA D does not meet the requirement.\nThe recommended 4-year plan is listed below by semester.',
                     'BA in Anthropology', [], [], ['BA in Anthropology', 'Requirements', 'Major Junior/Senior Hours'])
        self.assertTrue([c for c in X.program_page_candidates(tgt, {'institution_key': 'k'}, e, deg, '2026-27') if c['domain'] == 'academic_programs'])
        # CourseLeaf tab labels printed right under the heading ('Requirements', 'Recommended Four-Year Plan of Study') are not the plan sentence
        tabs = T.Page(body + 'Recommended Four-Year Plan of Study\nRequirements\nStudents complete 30 hours.', 'BA in Anthropology', [], [], ['BA in Anthropology'])
        self.assertTrue([c for c in X.program_page_candidates(tgt, {'institution_key': 'k'}, e, tabs, '2026-27') if c['domain'] == 'academic_programs'])

    def test_pvamu_awards(self):
        for n in ('Criminal Justice, BSCJ', 'Agriculture, BSAG', 'Chemical Engineering, BSCHE', 'Human Nutrition and Food, BSDIET'):
            self.assertEqual(X.credential_of(n), 'bachelor', n)
        self.assertIsNone(X.credential_of('Bsagent Studies'))
        self.assertEqual(X.credential_of('Biology Education 6-12 Major (B.Ed.)'), 'bachelor')
        self.assertIsNone(X.credential_of('Bedford Studies'))


class DepartmentSectionTests(unittest.TestCase):
    def test_degree_sections_on_a_department_page(self):  # MSState 2026-27, Arkansas 2026-27
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/undergraduate/arts/departmentofbiology/', 'role': 'program_page', 'sha256': 'a' * 64,
             'fetched_at': '2026-10-06T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        heads = ['Department of Biological Sciences', 'BS in Biological Sciences (BIO)', 'General Education Requirements', 'BS in Microbiology (MIC)',
                 'B.S. in Biology Sample Schedule', 'B.S. in Biology Suggested Sequence',
                 'BS in Clinical Laboratory Sciences (CLSC)1', 'Requirements for B.A. in Biology', 'B.S. in Biology Eight-Semester Degree Plan',
                 'Requirements for B.S.E. in Childhood Education with STEM Concentration', 'B.S. with non-A.C.S. certification',
                 'B.S. in Industrial Engineering and B.B.A. in Business Administration', 'BS in Applied Sociology (online degree)', 'Biology Minor']
        page = T.Page('2026-2027 Undergraduate Catalog\n' + '\n'.join(heads), 'Department of Biological Sciences < X University', [], [], heads)
        tgt = {'catalog': {'platform': 'courseleaf'}}
        out = X.program_page_candidates(tgt, {'institution_key': 'k'}, e, page, '2026-27')
        got = {c['record']['program_key']: c['record']['program_name'] for c in out}
        self.assertEqual(got, {'biological-sciences-bs': 'BS in Biological Sciences (BIO)', 'microbiology-bs': 'BS in Microbiology (MIC)',
                               'clinical-laboratory-sciences-bs': 'BS in Clinical Laboratory Sciences (CLSC)', 'biology-ba': 'B.A. in Biology'})
        self.assertTrue(all(c['extractor'] == 'department_section/v1' and c['record']['program_url'] == e['url'] for c in out))
        two = T.Page('2026-2027 Undergraduate Catalog\n2025-2026 Undergraduate Catalog\n' + '\n'.join(heads), 't', [], [], heads)
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, two, '2026-27'), [])  # no single current label
        # uark 2026-27: a link to the previous year's PDF is not a second label of this page
        ua = T.Page('2026-27 Edition\nA PDF of the entire 2025-26 Undergraduate catalog.\nRequirements for B.S. in Exercise Science', 't', [], [], ['Requirements for B.S. in Exercise Science'])
        self.assertEqual([c['record']['program_key'] for c in X.department_section_candidates({'institution_key': 'k'}, e, ua, '2026-27')], ['exercise-science-bs'])
        # the review of 2026-10-07: KU sample-plan sub-pages, PVAMU / Tulane section names, Wichita / WUSTL degree pages of their own
        dep = lambda heads, text='', links=(): X.department_section_candidates(
            {'institution_key': 'k'}, e, T.Page('2026-2027 Undergraduate Catalog\n' + text + '\n' + '\n'.join(heads), 't', [], list(links), heads), '2026-27')
        plan = lambda text: X.department_section_candidates({'institution_key': 'k'}, e, T.Page(
            '2026-2027 Undergraduate Catalog\nBA in Anthropology\n' + text, 't', [], [], ['BA in Anthropology']), '2026-27')
        self.assertEqual(plan('Below is a sample 4-year plan for students pursuing the BA in Anthropology.'), [])
        # KU's degree pages print the same sentence below the requirements, under another heading: still the degree
        self.assertTrue(plan('Requirements\nMajor Hours\nStudents must earn 30 hours.\nBelow is a sample 4-year plan for students pursuing the BA in Anthropology.'))
        self.assertEqual(dep(['Bachelor of Science in Juvenile Justice Degree Sequence', 'BS in Health Policy and Management Requirements',
                              'BS in Agribusiness Major Field']), [])
        self.assertEqual(dep(['BS in Computer Engineering'], links=[('https://catalog.x.edu/ece/computer-engineering-bs/', 'Computer Engineering BS')]), [])
        self.assertEqual(len(dep(['BS in Computer Engineering'], links=[(e['url'] + '#bs', 'Computer Engineering BS')])), 1)  # its own anchor
        self.assertEqual(len(dep(['BBA in Economics'], links=[('https://catalog.x.edu/econ-bs/', 'Economics BS')])), 1)  # another award
        self.assertEqual(len(dep(['BS in Nursing'], links=[('https://catalog.x.edu/absn/', 'Accelerated Bachelor of Science in Nursing')])), 1)
        self.assertEqual(len(dep(['BS in Nursing'], links=[('https://catalog.x.edu/bsn/', 'Bachelor of Science in Nursing')])), 0)
        # UF Geography 2026-27: the About box lists specializations; their 'Bachelor of Arts in ...' headings are not degrees
        heads = ['Bachelor of Arts in Geography', 'Bachelor of Arts in Environmental Geosciences', 'Bachelor of Science in Geography']
        uf = T.Page('2026-2027 Undergraduate Catalog\nBA | Specializations: Environmental Geosciences | General Geography\n' + '\n'.join(heads), 't', [], [], heads)
        got = sorted(c['record']['program_name'] for c in X.department_section_candidates({'institution_key': 'k'}, e, uf, '2026-27'))
        self.assertEqual(got, ['Bachelor of Arts in Geography', 'Bachelor of Science in Geography'])
        # UTSA 2026-28: 'Bachelor of Science Degree in X' headings; a department page printing two degrees gives two records
        utsa = dep(['Bachelor of Science Degree in Computer Science', 'Concentration in Cybersecurity', 'Bachelor of Science Degree in Software Engineering'])
        self.assertEqual(sorted(c['record']['program_key'] for c in utsa), ['computer-science-bs', 'software-engineering-bs'])

    def test_programs_sharing_a_page_are_not_duplicates(self):
        from programs import autoreview as A
        from datetime import date
        P = AutoReviewTests.prog
        def at(c, ext, url): c['extractor'] = ext; c['record']['program_url'] = url; return c
        U = 'https://catalog.x.edu/undergraduate/arts/departmentofbiology/'
        cands = [at(P(None, 'a', 'BS in Biology', key='biology-bs'), 'department_section/v1', U),
                 at(P(None, 'b', 'BS in Microbiology', key='microbiology-bs'), 'department_section/v1', U),
                 at(P(None, 'c', 'Chemistry, BS', key='chem'), 'catalog_program/v1', 'https://catalog.x.edu/chem/'),
                 at(P(None, 'd', 'Chemistry, BA', key='chem-ba'), 'catalog_program/v1', 'https://catalog.x.edu/chem/')]
        d = AutoReviewTests.run_dir(None, cands)
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try: approve, cats, held = A.review('ZZ', d, today=date(2026, 10, 6))
        finally: A.catalog_records = old
        self.assertEqual({a['candidate_id'] for a in approve}, {'a', 'b', 'c'})  # one page, two programs; other extractors keep the URL rule
        self.assertEqual(held['duplicate'], 1)


class SitemapTests(unittest.TestCase):
    def test_courseleaf_sitemap_yields_bachelor_program_pages(self):
        from pipeline.crawl import Fetcher, Run
        sm = b'''<?xml version="1.0"?><urlset>
<url><loc>https://catalog.x.edu/undergraduate/sciences/biology/biology-bs/</loc></url>
<url><loc>https://catalog.x.edu/undergraduate/sciences/biology/biology-minor/</loc></url>
<url><loc>https://catalog.x.edu/graduate/sciences/biology/biology-ms/</loc></url>
<url><loc>https://catalog.x.edu/undergraduate/arts/history/history-major/</loc></url>
<url><loc>https://catalog.x.edu/departments-programs-degrees/anthropology/anthropology-ab/</loc></url>
<url><loc>https://catalog.x.edu/undergraduate/sciences/computer-lab/</loc></url>
<url><loc>https://catalog.x.edu/undergraduate/arts/history/</loc></url>
<url><loc>https://catalog.x.edu/undergraduate/business/bba-certificate/</loc></url>
<url><loc>https://catalog.x.edu/graduate/business/accounting-bs/</loc></url>
<url><loc>https://catalog.x.edu/UGRD/colleges-schools/UGAGL/AEC_BS/</loc></url>
<url><loc>https://catalog.x.edu/undergraduatecatalog/coursesofinstruction/badm/</loc></url>
<url><loc>https://catalog.x.edu/undergraduate/courses/busi/</loc></url>
<url><loc>https://catalog.x.edu/undergraduate/business/busi/</loc></url>
<url><loc>https://elsewhere.org/a-bs/</loc></url></urlset>'''
        f = Fetcher(delay=0, timeout=1)
        def raw(url):
            if url.endswith('robots.txt'): return (404, url, {}, b'')
            if url.endswith('sitemap.xml'): return (200, url, {'Content-Type': 'application/xml'}, sm)
            return (200, url, {'Content-Type': 'text/html'}, b'<html><head><title>t</title></head><body>x</body></html>')
        f._raw = raw
        with tempfile.TemporaryDirectory() as d:
            t = {'institution_key': 'k', 'folder': 'k', 'domains': ['x.edu'], 'mode': 'catalog',
                 'catalog': {'platform': 'courseleaf', 'home': 'https://catalog.x.edu/', 'path_prefix': '/', 'min_depth': 1, 'program_lists': []}}
            C.crawl_target(t, Run(Path(d)), f, log=lambda *_: None)
            pages = sorted(e['url'] for e in Run(Path(d)).entries() if e['role'] == 'program_page')
        # UF's underscore slugs are read; a one-word segment ('badm', 'busi': course subjects) is never an award
        # UC Davis prints the A.B. ('anthropology-ab'); 'computer-lab' is not an award
        self.assertEqual(pages, ['https://catalog.x.edu/UGRD/colleges-schools/UGAGL/AEC_BS/',
                                 'https://catalog.x.edu/departments-programs-degrees/anthropology/anthropology-ab/',
                                 'https://catalog.x.edu/undergraduate/arts/history/history-major/',
                                 'https://catalog.x.edu/undergraduate/sciences/biology/biology-bs/'])

    def crawl(self, cat, pages):
        from pipeline.crawl import Fetcher, Run
        f = Fetcher(delay=0, timeout=1)
        def raw(url):
            if url.endswith('robots.txt'): return (404, url, {}, b'')
            body = pages.get(url)
            if body is None: return (404, url, {}, b'')
            ct = 'application/xml' if url.endswith('.xml') else 'text/html'
            return (200, url, {'Content-Type': ct}, body)
        f._raw = raw
        with tempfile.TemporaryDirectory() as d:
            t = {'institution_key': 'k', 'folder': 'k', 'domains': ['x.edu'], 'mode': 'catalog', 'catalog': cat}
            C.crawl_target(t, Run(Path(d)), f, log=lambda *_: None)
            return sorted(e['url'] for e in Run(Path(d)).entries() if e['role'] == 'program_page')

    def test_sitemap_program_pattern_for_department_pages(self):  # uark: programs on department pages, no award in the URL
        sm = b'''<urlset><url><loc>https://catalog.x.edu/ugcat/colleges/arts/historyhist/</loc></url>
<url><loc>https://catalog.x.edu/ugcat/colleges/arts/</loc></url><url><loc>https://catalog.x.edu/gradcat/colleges/arts/historyhist/</loc></url></urlset>'''
        cat = {'platform': 'courseleaf', 'home': 'https://catalog.x.edu/', 'path_prefix': '/', 'min_depth': 1, 'program_lists': [],
               'sitemap_program': r'/ugcat/colleges/[^/]+/[^/]+/$'}
        self.assertEqual(self.crawl(cat, {'https://catalog.x.edu/sitemap.xml': sm}), ['https://catalog.x.edu/ugcat/colleges/arts/historyhist/'])
        # course-description sections are never program pages (uark 'coursesofinstruction')
        rule = C.program_rule({'catalog': cat})
        self.assertTrue(rule('https://catalog.x.edu/ugcat/colleges/arts/historyhist/'))
        self.assertFalse(rule('https://catalog.x.edu/ugcat/coursesofinstruction/hist/'))
        self.assertFalse(rule('https://catalog.x.edu/ugcat/courses-of-instruction/hist/'))

    def test_nav_prefix_walks_sections_without_a_sitemap(self):  # MSState: no sitemap; college and department pages link programs
        page = lambda *links: ('<html><head><title>t</title></head><body>' + ''.join(f'<a href="{h}">{a}</a>' for h, a in links) + '</body></html>').encode()
        U = 'https://catalog.x.edu/undergraduate/'
        pages = {'https://catalog.x.edu/': page((U, 'Undergraduate'), ('https://catalog.x.edu/graduate/', 'Graduate')),
                 U: page((U + 'arts/', 'College of Arts')),
                 U + 'arts/': page((U + 'arts/history/', 'History')),
                 U + 'arts/history/': page((U + 'arts/history/history-ba/', 'History, BA'), (U + 'arts/history/history-minor/', 'History Minor')),
                 'https://catalog.x.edu/graduate/': page(('https://catalog.x.edu/graduate/arts/history/history-ma/', 'History, MA'))}
        cat = {'platform': 'courseleaf', 'home': 'https://catalog.x.edu/', 'path_prefix': '/undergraduate/', 'min_depth': 2, 'program_lists': [],
               'nav_prefix': '/undergraduate/'}
        got = self.crawl(cat, pages)
        self.assertIn(U + 'arts/history/history-ba/', got)
        self.assertFalse([u for u in got if '/graduate/' in u])
        self.assertEqual(self.crawl({**cat, 'nav_prefix': None}, pages), [])  # without it nothing past the home page


class ListedProgramTests(unittest.TestCase):
    def test_award_from_the_list_name_from_the_page(self):  # Auburn 2026-27
        from pipeline import text as T
        from programs import verify as V
        url = 'https://bulletin.auburn.edu/undergraduate/agriculture/agbusiness_major/'
        e = {'url': url, 'sha256': 'page', 'fetched_at': '2026-10-06T00:00:00'}
        listed = {'name': 'Agricultural Business & Economics – BS', 'printed': 'Agricultural Business & Economics – BS', 'url': url,
                  'credential_level': 'bachelor', 'listed_on': 'https://bulletin.auburn.edu/undergraduate/majors/', 'listed_on_sha256': 'list'}
        txt = 'Auburn Bulletin 2026-2027\nAgricultural Business & Economics (AGEC)\nCurriculum'
        page = T.Page(txt, 'Agricultural Business & Economics (AGEC) | Auburn University Bulletin', [], [], ['Agricultural Business & Economics (AGEC)'])
        tgt = {'catalog': {'platform': 'courseleaf'}, '_listed': {url: listed}}
        out = X.program_page_candidates(tgt, {'institution_key': 'k'}, e, page, '2026-27')
        self.assertEqual([(c['record']['program_name'], c['extractor'], c['record']['catalog_year']) for c in out],
                         [('Agricultural Business & Economics – BS', 'listed_program/v1', '2026-2027')])
        self.assertEqual(V.check_candidate(out[0], txt, {'list': 'Majors\nAgricultural Business & Economics – BS'}.get), [])
        other = T.Page(txt.replace('Agricultural Business & Economics (AGEC)', 'Animal Sciences'), 't', [], [], ['Animal Sciences'])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, other, '2026-27'), [])  # page is another program
        undated = T.Page('Agricultural Business & Economics (AGEC)', 't', [], [], ['Agricultural Business & Economics (AGEC)'])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, undated, '2026-27'), [])
        longer = T.Page(txt.replace('Agricultural Business & Economics (AGEC)', 'Agricultural Business & Economics Education'), 't', [], [],
                        ['Agricultural Business & Economics Education'])
        self.assertEqual(X.program_page_candidates(tgt, {'institution_key': 'k'}, e, longer, '2026-27'), [])  # another program's page
        bare = {**tgt, '_listed': {url: {**listed, 'printed': 'Agricultural Business & Economics'}}}
        self.assertEqual(X.program_page_candidates(bare, {'institution_key': 'k'}, e, page, '2026-27'), [])

    def test_strip_award(self):
        for n, base in (('Accounting, BS', 'Accounting'), ('Biology (B.S.)', 'Biology'), ('Art, BA, BFA', 'Art'),
                        ('Art, Media, and Design', 'Art, Media, and Design'), ('Economics: BA, BS', 'Economics')):
            self.assertEqual(X.strip_award(n), base)


class CatalogFieldTests(unittest.TestCase):
    def test_verified_listed_programs_bounds(self):
        from backend.program_fields import field_errors
        base = {'institution_key': 'k', 'academic_year': '2026-27', 'catalog_url': 'https://c.x.edu/', 'source_url': 'https://c.x.edu/l',
                'listed_bachelor_programs': 10}
        self.assertEqual(field_errors('program_catalogs', {**base, 'verified_listed_programs': 10}), [])
        self.assertTrue(field_errors('program_catalogs', {**base, 'verified_listed_programs': 11}))
        self.assertTrue(field_errors('program_catalogs', {**base, 'verified_listed_programs': True}))


class CatalogOverwriteTests(unittest.TestCase):
    def test_standing_review_count_never_replaces_a_reviewed_count(self):
        from programs import promote as P
        import pipeline.promote as PP
        with tempfile.TemporaryDirectory() as d:
            old, oldp = P.ROOT, PP.ROOT; P.ROOT = PP.ROOT = Path(d)
            try:
                f = Path(d) / 'data/institutions/x/program_catalogs'; f.mkdir(parents=True)
                (f / '2026-27.json').write_text(json.dumps({'institution_key': 'k', 'academic_year': '2026-27', 'records': [
                    {'listed_bachelor_programs': 37, 'notes': 'Reviewed 2026-10-06: Catalog-count review 2026-10-06: official current list page.'}]}))
                cat = {'institution_key': 'k', 'catalog_url': 'https://c/', 'source_evidence': {'url': 'https://c/l', 'sha256': 's', 'fetched_at': '2026-10-06T00:00:00'},
                       'listed_bachelor_programs': 72, 'reason': 'Standing review: official current-catalog program list pages.'}
                self.assertEqual(P.apply_catalog(cat, {'k': 'x'}, {}, {}), 0)
                self.assertEqual(json.loads((f / '2026-27.json').read_text())['records'][0]['listed_bachelor_programs'], 37)
            finally:
                P.ROOT, PP.ROOT = old, oldp


class CollegeQualifiedListTests(unittest.TestCase):
    def test_list_line_with_a_college_names_the_program(self):  # Iowa State 2026-27 'Biology, B.S. (College of Liberal Arts and Sciences)'
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/las/biology/', 'role': 'program_page', 'sha256': 'a' * 64, 'fetched_at': '2026-10-07T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        page = T.Page('Iowa State University Courses and Programs (2026-2027 Catalog)\nBiology', 'Biology | X Catalog', [], [], ['Biology', 'Curriculum in Biology'])
        listed = {'credential_level': 'bachelor', 'printed': 'Biology, B.S. (College of Liberal Arts and Sciences)', 'listed_on': 'https://catalog.x.edu/list/', 'listed_on_sha256': 'b' * 64}
        c = X.listed_program_identity({'institution_key': 'k'}, e, page, '2026-27', listed)
        self.assertEqual([x['record']['program_name'] for x in c], ['Biology, B.S. (College of Liberal Arts and Sciences)'])
        self.assertEqual(X.listed_program_identity({'institution_key': 'k'}, e, page, '2026-27', {**listed, 'printed': 'Biology (College of Liberal Arts and Sciences)'}), [])

    def test_department_page_heading_prints_the_listed_program(self):  # Iowa State 'Physics and Astronomy' / 'Physics, B.S'
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/las/physics/', 'role': 'program_page', 'sha256': 'a' * 64, 'fetched_at': '2026-10-07T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        listed = {'credential_level': 'bachelor', 'printed': 'Physics, B.S.', 'listed_on': 'https://catalog.x.edu/list/', 'listed_on_sha256': 'b' * 64}
        mk = lambda heads: T.Page('X Courses and Programs (2026-2027 Catalog)\n' + '\n'.join(heads), 'Physics and Astronomy | X Catalog', [], [], heads)
        c = X.listed_program_identity({'institution_key': 'k'}, e, mk(['Physics and Astronomy', 'The Physics Major', 'Physics, B.S']), '2026-27', listed)
        self.assertEqual([x['record']['program_name'] for x in c], ['Physics, B.S.'])
        self.assertEqual(X.listed_program_identity({'institution_key': 'k'}, e, mk(['Physics and Astronomy', 'Physics, B.A.']), '2026-27', listed), [])
        # a page whose own heading names a bachelor's award is left to the program-page readers
        self.assertEqual(X.listed_program_identity({'institution_key': 'k'}, e, mk(['Astronomy, B.S.', 'Physics, B.S']), '2026-27', listed), [])

    def test_several_majors_heading(self):
        for h in ['Majors', 'Undergraduate Majors', "Majors - Bachelor's Degree", 'The department offers the following majors:']:
            self.assertTrue(X.MAJORS_HEADING.search(h), h)
        for h in ['A. Courses required of all Genetics majors', 'Departmental Requirements for Sociology Majors', 'Majors plan a program of study in one of two tracks:']:
            self.assertFalse(X.MAJORS_HEADING.search(h), h)


class AwardDocumentTests(unittest.TestCase):
    def docs(self):
        L = lambda *ls: list(ls)
        return [{'majors': ['Public Policy Major', 'Global and Foreign Policy Major'], 'read': 'named', 'entry': {'url': 'https://spp/u'},
                 'lines': L('Bachelor of Arts in Public Policy', 'Bachelor of Arts in Global and Foreign Policy', 'Bachelor of Science in Public Policy Analytics')},
                {'majors': ['Animal Sciences Major'], 'read': 'single_award', 'entry': {'url': 'https://agnr/ansc'},
                 'lines': L('The ANSC department has degrees available in Bachelor of Science (B.S.), Master of Science (M.S.).')},
                {'majors': ['Plant Sciences Major'], 'read': 'single_award', 'entry': {'url': 'https://agnr/psla'},
                 'lines': L('Offers Bachelor of Science and Bachelor of Arts degrees.')}]

    def test_award_only_where_an_official_page_prints_it(self):  # UMD 2026-27 school and department pages
        from programs.extract import document_award
        self.assertEqual(document_award('Public Policy Major', self.docs())[:2], ('B.A.', 'Bachelor of Arts in Public Policy'))
        self.assertEqual(document_award('Global and Foreign Policy Major', self.docs())[0], 'B.A.')
        self.assertEqual(document_award('Animal Sciences Major', self.docs())[0], 'B.S.')
        self.assertIsNone(document_award('Plant Sciences Major', self.docs()))  # two bachelor's awards: none recorded
        self.assertIsNone(document_award('History Major', self.docs()))         # no document names the major

    def test_graduate_name_rule_keeps_bachelor_of_musical_arts(self):  # Missouri Western 2026-27
        from programs.autoreview import GRADUATE
        self.assertFalse(GRADUATE.search('Musical Arts (Bachelor of Musical Arts, B.M.A.)'))
        self.assertTrue(GRADUATE.search('History (M.A.)'))
class KeptRecordTests(unittest.TestCase):
    def test_corrected_or_already_promoted_records_are_not_replaced(self):  # JHU 2026-10-07, #129 footnote fixes
        from programs import promote as P
        import pipeline.promote as PP
        with tempfile.TemporaryDirectory() as d:
            old, oldp = P.ROOT, PP.ROOT; P.ROOT = PP.ROOT = Path(d)
            try:
                f = Path(d) / 'data/institutions/x/academic_programs'; f.mkdir(parents=True)
                (f / '2026-27.json').write_text(json.dumps({'institution_key': 'k', 'academic_year': '2026-27', 'records': [
                    {'program_key': 'policy', 'verification_status': 'unverified', 'verification_correction_reason': 'not a program'},
                    {'program_key': 'listed', 'verification_status': 'verified'}, {'program_key': 'fixed', 'verification_status': 'verified'}]}))
                (Path(d) / 'supabase').mkdir()
                (Path(d) / 'supabase/corrections.json').write_text(json.dumps({'corrections': [
                    {'natural_key': json.dumps(['academic_programs', 'k', None, '2026-27', {'program_key': 'listed'}])}]}))
                c = lambda cid, key: {'candidate_id': cid, 'domain': 'academic_programs', 'institution_key': 'k', 'academic_year': '2026-27'}
                self.assertIn('correction', P.kept_record(c('a', 'policy'), {'program_key': 'policy'}, {'k': 'x'}, set()))
                self.assertIn('correction', P.kept_record(c('b', 'listed'), {'program_key': 'listed'}, {'k': 'x'}, set()))
                self.assertIn('already promoted', P.kept_record(c('f', 'fixed'), {'program_key': 'fixed'}, {'k': 'x'}, {'f'}))
                self.assertIsNone(P.kept_record(c('g', 'fixed'), {'program_key': 'fixed'}, {'k': 'x'}, {'f'}))  # a new review may update it
                self.assertIsNone(P.kept_record(c('f', 'fixed'), {'program_key': 'fixed'}, {'k': 'x'}, {'f'}, {'replaces_promoted': 'award from school page'}))
                self.assertIn('correction', P.kept_record(c('a', 'policy'), {'program_key': 'policy'}, {'k': 'x'}, set(), {'replaces_promoted': 'x'}))
                self.assertIsNone(P.kept_record(c('a', 'policy'), {'program_key': 'policy'}, {'k': 'x'}, set(), {'replaces_correction': 'reader fixed'}))
                self.assertIsNone(P.kept_record(c('b', 'listed'), {'program_key': 'listed'}, {'k': 'x'}, set(), {'replaces_correction': 'reader fixed'}))
                self.assertIn('correction', P.kept_record(c('b', 'listed'), {'program_key': 'listed'}, {'k': 'x'}, set(), {'replaces_correction': ''}))
                self.assertIsNone(P.kept_record(c('n', 'new'), {'program_key': 'new'}, {'k': 'x'}, set()))
            finally:
                P.ROOT, PP.ROOT = old, oldp


class PromoteKeepsCorrectionsTests(unittest.TestCase):
    def test_promote_leaves_a_corrected_record_and_reports_it(self):
        from programs import promote as P
        import pipeline.promote as PP
        with tempfile.TemporaryDirectory() as d:
            D = Path(d); old, oldp = P.ROOT, PP.ROOT; P.ROOT = PP.ROOT = D
            try:
                (D / 'programs/targets').mkdir(parents=True)
                (D / 'programs/targets/ZZ.json').write_text(json.dumps({'institutions': [{'institution_key': 'k', 'folder': 'x'}]}))
                run = D / 'programs/runs/ZZ/r'; run.mkdir(parents=True)
                c = {'candidate_id': 'c1', 'domain': 'academic_programs', 'institution_key': 'k', 'academic_year': '2026-27', 'year_basis': 'labeled_in_source',
                     'issues': [], 'extractor': 'static_program/v1', 'evidence': [], 'source': {'url': 'https://u/p'},
                     'record': {'program_key': 'policy', 'program_name': 'Requirements for a Bachelor\'s Degree', 'credential_level': 'bachelor'}}
                (run / 'candidates.jsonl').write_text(json.dumps(c) + '\n'); (run / 'evidence.jsonl').write_text(''); (run / 'manifest.jsonl').write_text('')
                f = D / 'data/institutions/x/academic_programs'; f.mkdir(parents=True)
                on_file = {'institution_key': 'k', 'academic_year': '2026-27', 'records': [
                    {'program_key': 'policy', 'program_name': 'Requirements for a Bachelor\'s Degree', 'verification_status': 'unverified',
                     'verification_correction_reason': 'not a program'}]}
                (f / '2026-27.json').write_text(json.dumps(on_file))
                dec = D / 'dec.json'; dec.write_text(json.dumps({'run': 'programs/runs/ZZ/r', 'approve': [{'candidate_id': 'c1', 'reason': 'x'}]}))
                logs = []
                P.promote(dec, log=logs.append)
                self.assertEqual(json.loads((f / '2026-27.json').read_text()), on_file)
                self.assertTrue(any('kept as on file' in l for l in logs))
                # a reviewed replacement of a record this candidate produced keeps the earlier decision in the archive
                ev = D / 'sources/programs/ZZ/r'; ev.mkdir(parents=True, exist_ok=True)
                (ev / 'evidence.json').write_text(json.dumps({'c2': {'decision': {'candidate_id': 'c2', 'reason': 'first review'}}}))
                c2 = {**c, 'candidate_id': 'c2', 'record': {'program_key': 'bio', 'program_name': 'Biology Major', 'credential_level': 'bachelor', 'program_url': 'https://u/bio'}}
                (run / 'candidates.jsonl').write_text(json.dumps(c2) + '\n')
                dec.write_text(json.dumps({'run': 'programs/runs/ZZ/r', 'approve': [{'candidate_id': 'c2', 'reason': 'award found', 'replaces_promoted': 'award from school page'}]}))
                P.promote(dec, log=logs.append)
                arch = json.loads((ev / 'evidence.json').read_text())
                self.assertEqual(arch['c2']['decision']['reason'], 'award found')
                self.assertEqual([v['decision']['reason'] for k, v in arch.items() if k.startswith('c2~superseded-')], ['first review'])
                # #229 recovery: a reviewed re-extraction replaces a corrected record only with 'replaces_correction'
                c3 = {**c, 'record': {**c['record'], 'institution_key': 'k', 'academic_year': '2026-27', 'last_verified_at': '2026-10-22'}}
                (run / 'candidates.jsonl').write_text(json.dumps(c3) + '\n')
                arch['c1'] = {'decision': {'candidate_id': 'c1', 'reason': 'earlier'}}; (ev / 'evidence.json').write_text(json.dumps(arch))
                dec.write_text(json.dumps({'run': 'programs/runs/ZZ/r', 'approve': [{'candidate_id': 'c1', 'reason': 'rechecked', 'replaces_correction': 'reader now reads the total'}]}))
                P.promote(dec, log=logs.append)
                recs = json.loads((f / '2026-27.json').read_text())['records']; self.assertEqual(len(recs), 2); rec = recs[0]
                self.assertEqual(rec['verification_status'], 'verified')
                self.assertNotIn('verification_correction_reason', rec)
                self.assertIn('Re-verified after the correction on file (kept in supabase/corrections.json): reader now reads the total', rec['notes'])
                arch = json.loads((ev / 'evidence.json').read_text())
                self.assertEqual([v['decision']['reason'] for k, v in arch.items() if k.startswith('c1~superseded-')], ['earlier'])
                # #250 (UWM): rows that match the source but leave part of the printed section uncaptured are partially verified
                c4 = {**c, 'candidate_id': 'c4', 'record': {'program_key': 'chem', 'program_name': 'Chemistry Major', 'credential_level': 'bachelor', 'program_url': 'https://u/chem'}}
                (run / 'candidates.jsonl').write_text(json.dumps(c4) + '\n')
                dec.write_text(json.dumps({'run': 'programs/runs/ZZ/r', 'approve': [{'candidate_id': 'c4', 'reason': 'rows match', 'partial_coverage': 'section also prints CHEM 400'}]}))
                P.promote(dec, log=logs.append)
                rec = next(r for r in json.loads((f / '2026-27.json').read_text())['records'] if r['program_key'] == 'chem')
                self.assertEqual((rec['verification_status'], rec['section_coverage'], rec['captured_rows_match_source'], rec['coverage_note']),
                                 ('partially_verified', 'incomplete', True, 'section also prints CHEM 400'))
                self.assertIn('Partially verified: the captured rows match the source; the section is incomplete: section also prints CHEM 400', rec['notes'])
            finally:
                P.ROOT, PP.ROOT = old, oldp


class PlanFootnoteTests(unittest.TestCase):
    def page(self, text, n=1):
        from pipeline import text as T
        g = {'caption': 'Plan of Study Grid', 'heading': 'Biology - BA', 'rows': [['First Year'], ['Fall', 'Hours'], ['BIOL 111', 'Intro 1', '4'], ['', 'Total Hours', '4']]}
        return T.Page(text, 'Biology - BA', [dict(g) for _ in range(n)], [], [])

    def test_footnotes_after_each_grid(self):  # Texas A&M 2026-27
        from programs import courseleaf as CL
        txt = ('Biology - BA\nPlan of Study Grid\n| First Year\n| Fall | Hours\n| BIOL 111\nwrapped title 1 | 4\n| | Total Hours | 4\n'
               '1\nMATH 147 accepted in lieu of MATH 142.\n2\nSelect from ANTH 200-499.\nTotal Program Hours 120')
        self.assertEqual(CL.grid_footnotes(self.page(txt)), [[{'marker': '1', 'text': 'MATH 147 accepted in lieu of MATH 142.'}, {'marker': '2', 'text': 'Select from ANTH 200-499.'}]])
        self.assertEqual([x['marker'] for x in CL.grid_footnotes(self.page(txt.replace('\n2\n', '\n3\n')))[0]], ['1', '3'])  # a skipped number (Saint Louis)
        self.assertEqual([x['marker'] for x in CL.grid_footnotes(self.page(txt.replace('\n2\n', '\n1\n')))[0]], ['1'])  # numbers must increase
        multi = txt.replace('MATH 147 accepted in lieu of MATH 142.', 'Select one of the following:\nMATH 147\nMATH 151')
        self.assertEqual(CL.grid_footnotes(self.page(multi))[0][0]['text'], 'Select one of the following: / MATH 147 / MATH 151')  # a note of several lines
        last = txt.replace('Select from ANTH 200-499.', 'Choose one group as follows:\nGroup A: ANTH 301\nGroup B: ANTH 302')
        self.assertEqual(CL.grid_footnotes(self.page(last))[0][1]['text'], 'Choose one group as follows: / Group A: ANTH 301 / Group B: ANTH 302')
        sym = txt.replace('1\nMATH 147 accepted in lieu of MATH 142.\n2\n', '+\nMATH 147 accepted in lieu of MATH 142.\n^\n')
        self.assertEqual([x['marker'] for x in CL.grid_footnotes(self.page(sym))[0]], ['+', '^'])  # Oregon State, Tulane
        row = txt.replace('Select from ANTH 200-499.\nTotal Program Hours 120', 'Select one of the following:\n| ANTH 301 | 3')
        self.assertEqual(CL.grid_footnotes(self.page(row))[0][-1]['text'], 'Select one of the following:')  # a table row is never a note's text
        inline = txt.replace('Total Program Hours 120', '**This document serves as a guide.\nTotal Program Hours 120')
        self.assertEqual(CL.grid_footnotes(self.page(inline))[0][-1], {'marker': '**', 'text': 'This document serves as a guide.'})  # Slippery Rock
        two = txt.replace('Total Program Hours 120', 'Plan of Study Grid\n| Third Year\n| | Total Hours | 4\n3\nTwo courses must be writing intensive.')
        self.assertEqual([[x['marker'] for x in g] for g in CL.grid_footnotes(self.page(two, 2))], [['1', '2'], ['3']])  # numbering continues
        self.assertIsNone(CL.grid_footnotes(self.page(txt, 2)))  # captions in the text do not match the grids: never paired
        self.assertIsNone(CL.grid_footnotes(self.page(txt.replace('| | Total Hours | 4', 'Total Hours 4'))))  # the grid's end not found
        e = {'url': 'https://catalog.x.edu/bio/', 'sha256': 's', 'fetched_at': '2026-10-22T00:00:00'}
        out = [c for c in CL.extract({'institution_key': 'k'}, e, self.page(txt), '2026-2027', '', True) if c['domain'] == 'degree_requirements']
        self.assertEqual((out[0]['record']['rule_details']['footnotes'][0]['marker'], out[0]['issues']), ('1', []))
        out = [c for c in CL.extract({'institution_key': 'k'}, e, self.page('Biology - BA'), '2026-2027', '', True) if c['domain'] == 'degree_requirements']
        self.assertEqual(out[0]['issues'], ['footnotes_not_read'])
        g2 = {'caption': 'Plan of Study Grid', 'heading': 'Biology - BA', 'rows': [['Second Year'], ['Fall', 'Hours'], ['BIOL 213', 'Genetics', '4'], ['', 'Total Hours', '4']]}
        p2 = self.page('Biology - BA'); p2.tables.append(g2)  # one plan in two continued grids; footnotes cannot be paired: held
        out = [c for c in CL.extract({'institution_key': 'k'}, e, p2, '2026-2027', '', True) if c['domain'] == 'degree_requirements']
        self.assertEqual([c['issues'] for c in out], [['footnotes_not_read']])
        from programs import verify as V
        c = [c for c in CL.extract({'institution_key': 'k'}, e, self.page(txt), '2026-2027', '', True) if c['domain'] == 'degree_requirements'][0]
        self.assertNotIn('footnote 1 not verbatim', V.check_candidate(c, txt + '\nUndergraduate Catalog 2026-2027'))
        self.assertIn('footnote 1 not verbatim', V.check_candidate(c, txt.replace('in lieu of', 'instead of') + '\nUndergraduate Catalog 2026-2027'))


class PlanNoteTests(unittest.TestCase):
    """Owner decision 2026-10-23: footnotes and unmarked notes that modify a plan are kept, with where they are printed."""
    G = 'Biology - BA\nPlan of Study Grid\n| First Year\n| Fall | Hours\n| BIOL 111 | Intro 1 | 4\n| | Total Hours | 4\n'

    def page(self, tail, n=1, text=None):
        from pipeline import text as T
        g = {'caption': 'Plan of Study Grid', 'heading': 'Biology - BA', 'rows': [['First Year'], ['Fall', 'Hours'], ['BIOL 111', 'Intro 1', '4'], ['', 'Total Hours', '4']]}
        return T.Page(text or self.G + tail, 'Biology - BA', [dict(g) for _ in range(n)], [], ['Program Learning Outcomes'])

    def test_marker_forms(self):
        from programs import courseleaf as CL
        fn = lambda tail: [(x['marker'], x['text']) for x in CL.grid_footnotes(self.page(tail))[0]]
        self.assertEqual(fn('1 Requires English Composition Placement\n2This course may not be required.\n'),
                         [('1', 'Requires English Composition Placement'), ('2', 'This course may not be required.')])  # Nebraska Omaha
        self.assertEqual(fn('1.\nTake it in the first semester.\n2.\nSee an advisor.\n'), [('1', 'Take it in the first semester.'), ('2', 'See an advisor.')])  # Sacramento
        self.assertEqual(fn('****\nCapstone note.\nii\nSecond note.\n'), [('****', 'Capstone note.'), ('ii', 'Second note.')])  # ODU, NJIT
        self.assertEqual(fn('5\n*Approved electives are listed on the department site.\n'), [('5', '*Approved electives are listed on the department site.')])  # NC State
        self.assertEqual(fn('3 credits of electives.\n'), [])  # a number that is not the next marker is not one
        self.assertEqual(fn('1\nSelect one of the following:\nMATH 147\nMATH 151\nMATH 171\nProgram Learning Outcomes\n')[0][1],
                         'Select one of the following: / MATH 147 / MATH 151 / MATH 171')  # a list after ':' runs on

    def test_shared_legend(self):  # Oregon State prints one legend after the last of several grids
        from programs import courseleaf as CL
        from pipeline import text as T
        g = {'caption': 'Plan of Study Grid', 'heading': 'Biology - BA', 'rows': [['First Year'], ['Fall', 'Hours'], ['BIOL 111', 'Intro', '4'], ['', 'Total Hours', '4']]}
        cite = dict(g, rows=[['First Year'], ['Fall', 'Hours'], ['WR 121Z^', 'Writing', '4'], ['', 'Total Hours', '4']])
        two = self.G + 'Plan of Study Grid\n| First Year\n| Fall | Hours\n| BIOL 111 | Intro | 4\n| | Total Hours | 4\n^\nBaccalaureate core course.\n'
        out = CL.grid_footnotes(T.Page(two, 't', [cite, dict(g)], [], []))
        self.assertEqual(out, [[{'marker': '^', 'text': 'Baccalaureate core course.', 'shared': True}], [{'marker': '^', 'text': 'Baccalaureate core course.'}]])
        out = CL.grid_footnotes(T.Page(two, 't', [dict(g), dict(g)], [], []))  # a grid that cites none of the legend gets none (Oregon BA/BS)
        self.assertEqual(out[0], [])

    def test_unmarked_notes(self):
        from programs import courseleaf as CL
        pn = lambda tail, n=1: CL.plan_notes(self.page(tail, n=n))
        got = pn('1\nMust make a C.\nGraduation requirements include 3 hours of International and Cultural Diversity courses.\nFind Us\n1 LMU Drive\n')
        self.assertEqual(got, [[{'text': 'Graduation requirements include 3 hours of International and Cultural Diversity courses.', 'location': 'printed after the plan grid and its footnotes'}]])
        self.assertEqual(pn('Note:\nCOMM 100 does not count toward the major.\n')[0][0]['text'], 'Note: / COMM 100 does not count toward the major.')  # UIC, LMU
        self.assertEqual(pn('Associate Chair\nStudents must complete 35 credits in the major.\n'), ['unclear'])  # where the notes end is not printed
        self.assertEqual(pn('(800) 543-5317\nAll prerequisites must be met before you enroll.\n'), [[]])  # page text ends the notes
        self.assertEqual(pn(''), [[]])

    def test_review_layouts(self):  # the six failure classes of the 2026-10-23 review, on the layouts that showed them
        from programs import courseleaf as CL
        from pipeline import text as T
        fn = lambda tail: [(x['marker'], x['text']) for x in CL.grid_footnotes(self.page(tail))[0]]
        pn = lambda tail: CL.plan_notes(self.page(tail))[0]
        # 1. page text never becomes a note: an address, social links, page metadata (LMU, NMC, Slippery Rock)
        self.assertEqual(fn('*\nSee advisor.\nFind Us\n1 LMU Drive\nLos Angeles, CA 90045\nX\nYouTube\n'), [('*', 'See advisor.')])
        self.assertEqual(fn('*\nSee advisor.\nMajor Code: 2 15\nRevision date: 05.03.2022\n'), [('*', 'See advisor.')])
        p = self.page('Pace University\nAll nursing courses require a grade of C+.\n'); p.title = 'Nursing BS < Pace University'
        self.assertEqual(CL.plan_notes(p)[0], [])  # the institution's name, as the page title prints it, ends the notes
        self.assertEqual(pn('Pace University\nAll nursing courses require a grade of C+.\n'), [])  # an institution's name is page text
        self.assertEqual(pn('Go Getters Go To Pace.\nAll nursing courses require a grade of C+.\n'), 'unclear')  # unknown text: held, not dropped
        self.assertEqual(fn('1\nStudents must apply for admission to the program; see accreditation details.\n'), [('1', 'Students must apply for admission to the program; see accreditation details.')])
        # 2./3. a note ending in ':' keeps the whole list printed under it (Kingsville, South Carolina, Temple)
        self.assertEqual(fn('1\nList of Approved Electives:\nAGRI 3300 Farm Management\nAGRI 4310 Agricultural Policy and Law\nProgram Learning Outcomes\n'),
                         [('1', 'List of Approved Electives: / AGRI 3300 Farm Management / AGRI 4310 Agricultural Policy and Law')])
        self.assertEqual(pn('Advanced Science Courses for BS students consist of:\nCHEM 3301\nPHYS 2021\n')[0]['text'],
                         'Advanced Science Courses for BS students consist of: / CHEM 3301 / PHYS 2021')
        self.assertEqual(pn('One course: CHEM 122, CHEM 123\nand PHYS 141 fulfills four of the nine hours.\n')[0]['text'],
                         'One course: CHEM 122, CHEM 123 / and PHYS 141 fulfills four of the nine hours.')  # one sentence over two lines (UIC)
        # 4. notes JSU prints as table rows are read; a mark a row cites with no note after the grid holds the plan
        self.assertEqual(fn('| 1 | Select from: EC 222, EC 231\n| 2 | See advisor for approval.\n'), [('1', 'Select from: EC 222, EC 231'), ('2', 'See advisor for approval.')])
        e = {'url': 'https://catalog.x.edu/bio/', 'sha256': 's', 'fetched_at': '2026-10-23T00:00:00'}
        g = {'caption': 'Plan of Study Grid', 'heading': 'Biology - BA', 'rows': [['First Year'], ['Fall', 'Hours'], ['BIOL 111', 'Intro 1', '4'], ['', 'Total Hours**', '4']]}
        txt = self.G.replace('| | Total Hours | 4', '| | Total Hours** | 4')
        c = [c for c in CL.extract({'institution_key': 'k'}, e, T.Page(txt + 'Course List\n', 't', [g], [], []), '2026-2027', '', True) if c['domain'] == 'degree_requirements'][0]
        self.assertIn('footnote_missing', c['issues'])  # Slippery Rock: '**This document ...' printed after the elective Course Lists
        self.assertEqual(CL.cited_symbols({'rows': [['+*WR 121Z', 'Writing', '4'], ['PHYS 120*', 'Physics', '4'], ['Calculus 2', '', '4']]}), {'+', '*'})
        # 5. a note's end: a requirement-like line after something that is not a note holds the plan; a note after a
        # footnote that does not end a sentence says so in its location
        self.assertEqual(pn('Associate Chair\nStudents must complete 35 credits in the major.\n'), 'unclear')
        got = CL.plan_notes(self.page('1\nC- or better\nNo course may satisfy more than one requirement.\n'))[0]
        self.assertEqual(got[0]['location'], 'printed directly after footnote 1, which it may continue')
        self.assertEqual(fn('1\nC- or better\nNo course may satisfy more than one requirement.\n'), [('1', 'C- or better')])
        # round 2 of the review: a note that starts like page text is still a note; a list of sentences under ':' is kept whole;
        # any line before the page text that is not read holds the plan; a mark printed after unmarked notes holds it
        self.assertEqual(fn('1\nTotal hours of free electives vary to allow 120 credit hrs.\n2\n2000-3999 electives can be selected from ACCT 2101.\n'),
                         [('1', 'Total hours of free electives vary to allow 120 credit hrs.'), ('2', '2000-3999 electives can be selected from ACCT 2101.')])
        self.assertEqual(fn('6\nCommunication Major Electives (15 hours):\nSix hours at 300-level and above.\nThree hours at 500-level.\nProgram Learning Outcomes\n'),
                         [('6', 'Communication Major Electives (15 hours): / Six hours at 300-level and above. / Three hours at 500-level.')])
        self.assertEqual(pn('All students must earn a C in major courses.\nConcentration in Vascular Sonography: CVTC 496\n'), 'unclear')
        self.assertEqual(pn('All students must earn a C in major courses.\n**Transfer credit is evaluated by the registrar.\n'), 'unclear')
        got = CL.plan_notes(self.page('1\nC- or better\nNotes:\nThis is a sample schedule only.\n'))[0]
        self.assertEqual((got[0]['text'], got[0]['location']), ('Notes: / This is a sample schedule only.', 'printed after the plan grid and its footnotes'))

    def test_boundaries_mutation_cases(self):
        from programs import courseleaf as CL
        fn = lambda tail: [(x['marker'], x['text']) for x in CL.grid_footnotes(self.page(tail))[0]]
        pn = lambda tail: CL.plan_notes(self.page(tail))[0]
        self.assertEqual([x['text'] for x in pn('Students must complete the core first.\n.\nAll majors must complete a capstone.\n')],
                         ['Students must complete the core first.', 'All majors must complete a capstone.'])  # a lone '.' (NC State)
        self.assertEqual(pn('Biology is the study of living things and you will explore many courses.\n'), [])  # description, not a note
        p = self.page('Pace Catalog\nAll nursing courses require a grade of C+.\n'); p.title = 'Nursing BS | Pace Catalog'
        self.assertEqual(CL.plan_notes(p)[0], [])  # the site name from the page title ends the notes
        self.assertEqual(pn('Approved electives for the major include:\nIntroduction to Ecology\nField Methods\n')[0]['text'],
                         'Approved electives for the major include: / Introduction to Ecology / Field Methods')
        self.assertEqual(fn('1\nTake it early.\n2\nSee advisor.\nUnrelated sentence here.\n1\nOther note.\n'), [('1', 'Take it early.'), ('2', 'See advisor.')])  # the last note is not extended by guess
        self.assertEqual(fn('1\nNote applies.\nChoose a track:\nData Analytics\nMarketing\n'), [('1', 'Note applies. / Choose a track: / Data Analytics / Marketing')])
        self.assertEqual(fn('1\nCourses must be\ncompleted in order.\n'), [('1', 'Courses must be / completed in order.')])
        self.assertEqual(fn('*\nSee advisor.\n1 LMU Drive\n'), [('*', 'See advisor.')])
        self.assertEqual(fn('3 Credits of electives.\n'), [])

    def test_extract_keeps_notes_and_holds_unclear_ones(self):
        from programs import courseleaf as CL, verify as V
        e = {'url': 'https://catalog.x.edu/bio/', 'sha256': 's', 'fetched_at': '2026-10-23T00:00:00'}
        tail = 'FINA courses do not count toward the major.\n'
        c = [c for c in CL.extract({'institution_key': 'k'}, e, self.page(tail), '2026-2027', '', True) if c['domain'] == 'degree_requirements'][0]
        self.assertEqual((c['record']['rule_details']['plan_notes'], c['issues']),
                         ([{'text': 'FINA courses do not count toward the major.', 'location': 'printed after the plan grid', 'scope': 'this plan'}], []))
        text = self.G + tail + 'Undergraduate Catalog 2026-2027'
        self.assertEqual(V.check_candidate(c, text), [])
        self.assertIn('plan note not verbatim', V.check_candidate(c, text.replace('do not count', 'never count')))
        c = [c for c in CL.extract({'institution_key': 'k'}, e, self.page('Associate Chair\nStudents must complete 35 credits in the major.\n'), '2026-2027', '', True)
             if c['domain'] == 'degree_requirements'][0]
        self.assertEqual((c['issues'], 'plan_notes' in c['record']['rule_details']), (['plan_note_unclear'], False))
        two = self.G + 'Plan of Study Grid\n| First Year\n| Fall | Hours\n| BIOL 111 | Intro 1 | 4\n| | Total Hours | 4\n' + tail
        g = {'caption': 'Plan of Study Grid', 'rows': [['First Year'], ['Fall', 'Hours'], ['BIOL 111', 'Intro 1', '4'], ['', 'Total Hours', '4']]}
        from pipeline import text as T
        p = T.Page(two, 'Biology - BA', [dict(g, heading='Biology - BA'), dict(g, heading='Biology - BS')], [], [])
        out = [c for c in CL.extract({'institution_key': 'k'}, e, p, '2026-2027', '', True) if c['domain'] == 'degree_requirements']
        self.assertEqual([c['issues'] for c in out], [['plan_heading_label'], ['plan_heading_label', 'plan_note_scope_unclear']])


class ProgramKeymapTests(unittest.TestCase):
    def test_programs_sharing_a_page_keep_their_own_keys(self):
        from programs import promote as P
        U = 'https://catalog.x.edu/dept/'
        on_file = {'records': [{'program_key': 'biology-bs', 'program_url': U}, {'program_key': 'old-key', 'program_url': 'https://catalog.x.edu/chem/'}]}
        cand = lambda cid, key, url, ext: {'candidate_id': cid, 'domain': 'academic_programs', 'institution_key': 'k', 'academic_year': '2026-27',
                                           'extractor': ext, 'record': {'program_key': key, 'program_url': url, 'program_name': key}}
        cands = {c['candidate_id']: c for c in [cand('a', 'biology-bs', U, 'department_section/v1'), cand('b', 'microbiology-bs', U, 'department_section/v1'),
                                                 cand('m', 'microbiology-bs', U, 'catalog_program/v1'), cand('c', 'chemistry-bs', 'https://catalog.x.edu/chem/', 'catalog_program/v1')]}
        old = P._records; P._records = lambda *a: on_file
        try:
            km = P.program_keymap([{'candidate_id': i} for i in ('a', 'b', 'c')], cands, {'k': 'x'})
            self.assertEqual(km, {('k', '2026-27', 'chemistry-bs'): 'old-key'})  # a renamed program keeps its key; siblings never merge
            km = P.program_keymap([{'candidate_id': 'm'}], cands, {'k': 'x'})
            self.assertEqual(km, {('k', '2026-27', 'microbiology-bs'): 'biology-bs'})  # the one-program-per-page rule elsewhere is unchanged
        finally:
            P._records = old

    def test_degrees_split_from_a_two_award_page_keep_their_own_keys(self):  # UT Dallas 'Biology (BA, BS)'
        from programs import promote as P
        U = 'https://catalog.x.edu/bio'
        on_file = {'records': [{'program_key': 'biology-ba-bs', 'program_url': U, 'program_name': 'Biology (BA, BS)'}]}
        cand = lambda cid, key, ext: {'candidate_id': cid, 'domain': 'academic_programs', 'institution_key': 'k', 'academic_year': '2026-27',
                                      'extractor': ext, 'record': {'program_key': key, 'program_url': U, 'program_name': key}}
        cands = {c['candidate_id']: c for c in [cand('a', 'biology-ba', 'edition_program/v1'), cand('b', 'biology-bs', 'edition_program/v1'),
                                                 cand('c', 'biology-bs', 'catalog_program/v1')]}
        old = P._records; P._records = lambda *a: on_file
        try:
            self.assertEqual(P.program_keymap([{'candidate_id': 'a'}, {'candidate_id': 'b'}], cands, {'k': 'x'}), {})
            self.assertEqual(P.program_keymap([{'candidate_id': 'c'}], cands, {'k': 'x'}), {('k', '2026-27', 'biology-bs'): 'biology-ba-bs'})
        finally:
            P._records = old


class FolderOwnershipTests(unittest.TestCase):
    def test_a_folder_two_registries_claim_receives_no_records(self):
        from programs import promote as P
        with tempfile.TemporaryDirectory() as d:
            old = P.ROOT; P.ROOT = Path(d)
            try:
                (Path(d) / 'pipeline/registry').mkdir(parents=True)
                (Path(d) / 'pipeline/registry/AA.json').write_text(json.dumps({'institutions': [{'institution_key': 'a', 'folder': 'tiu'}]}))
                (Path(d) / 'pipeline/registry/BB.json').write_text(json.dumps({'institutions': [{'institution_key': 'b', 'folder': 'tiu'}]}))
                with self.assertRaises(ValueError): P.check_folder_ownership({'a': 'tiu'})
                f = Path(d) / 'data/institutions/tiu/costs'; f.mkdir(parents=True)
                (f / '2026-27.json').write_text(json.dumps({'institution_key': 'a', 'records': []}))
                P.check_folder_ownership({'a': 'tiu'})  # its own records are already there
                with self.assertRaises(ValueError): P.check_folder_ownership({'b': 'tiu'})
            finally:
                P.ROOT = old


class ListedEmphasisTests(unittest.TestCase):
    """UVU 2026-27 lists each emphasis as its own bachelor's program and has no line for the base degree."""
    def test_listed_emphasis_is_a_program_only_without_a_base_degree(self):
        import re
        from programs.extract import listed_emphasis_pages
        norm = lambda u: re.sub(r'/?$', '', u)
        lists = {'x': {'programs': [
            {'listed_as': 'bachelor', 'printed': 'Political Science - American Government Emphasis, B.A.College of Humanities', 'url': 'https://a/ps-ag'},
            {'listed_as': 'bachelor', 'printed': 'Biology - Ecology Emphasis, B.S.College of Science', 'url': 'https://a/bio-eco'},
            {'listed_as': 'bachelor', 'printed': 'Biology, B.S.College of Science', 'url': 'https://a/bio'},
            {'listed_as': 'bachelor', 'printed': 'Forensic Science - Forensic Investigation Emphasis, B.SCollege of Health', 'url': 'https://a/fs'},
            {'listed_as': 'bachelor', 'printed': 'Chemistry - Bio Emphasis, B.S.College', 'url': 'https://a/chem-bio'},
            {'listed_as': 'bachelor', 'printed': 'Chemistry, B.A.College', 'url': 'https://a/chem-ba'},
            {'listed_as': None, 'printed': 'Art - Paint Emphasis, Minor', 'url': 'https://a/art-minor'}]}}
        self.assertEqual(sorted(u for _, u in listed_emphasis_pages(lists, norm)), ['https://a/chem-bio', 'https://a/fs', 'https://a/ps-ag'])

    def test_degree_index_segment_is_not_a_certificate_path(self):
        from programs.extract import not_bachelor_path
        self.assertFalse(not_bachelor_path('https://catalog.uas.alaska.edu/certificate-degree-programs/bachelors-degrees/biology-ba/'))
        self.assertTrue(not_bachelor_path('https://catalog.uas.alaska.edu/certificate-degree-programs/certificates/fisheries-technology/'))
        self.assertTrue(not_bachelor_path('https://catalog.uoregon.edu/min-anthropology/'))
        self.assertTrue(not_bachelor_path('https://catalog.wvu.edu/undergraduate/minors/accounting/'))

    def test_program_heading_skips_catalog_year_heading(self):
        from programs.extract import program_heading, static_program_identity
        from pipeline import text as T
        page = T.Page('Catalog 2026-2027\nComputer Science B.A.', 'Computer Science B.A. | University of Alaska Fairbanks Catalog', [], [],
                      ['Catalog 2026-2027', 'Computer Science B.A.', 'Admission Requirements'])
        self.assertEqual(program_heading(page), 'Computer Science B.A.')
        # a page title that names no heading (the title rule does not apply): the year heading is still skipped
        untitled = T.Page(page.text, 'UAF Catalog', [], [], ['Catalog 2026-2027', 'Computer Science B.A.', 'Admission Requirements'])
        self.assertEqual(program_heading(untitled), 'Computer Science B.A.')
        kent = T.Page('', 'Accounting - B.B.A. < Kent State University', [], [], ['University Catalog 2026-2027', 'Accounting - B.B.A.', 'About This Program'])
        self.assertEqual(program_heading(kent), 'Accounting - B.B.A.')
        # the ' < ' title form names the heading even when a non-year heading comes first
        self.assertEqual(program_heading(T.Page('', 'Accounting - B.B.A. < Kent State University', [], [], ['Quick Links', 'Accounting - B.B.A.'])), 'Accounting - B.B.A.')
        self.assertEqual(program_heading(T.Page('', 'X', [], [], ['University Catalog 2026-2027', 'Quick Links'])), 'Quick Links')
        got = static_program_identity({'institution_key': 'k'}, {'url': 'https://catalog.uaf.edu/bachelors/computer-science-ba/'}, page, '2026-27')
        self.assertEqual([c['record']['program_name'] for c in got], ['Computer Science B.A.'])
        index = T.Page('Catalog 2026-2027', "Bachelor's Degrees | UAS", [], [], ['Catalog 2026-2027', "Bachelor's Degrees"])
        self.assertEqual(static_program_identity({'institution_key': 'k'}, {'url': 'https://catalog.uas.alaska.edu/x/'}, index, '2026-27'), [])

    def test_shared_catalog_sections_are_excluded(self):
        from programs.crawl import program_rule, excluded
        t = {'catalog': {'platform': 'courseleaf', 'home': 'https://catalog.unh.edu/', 'path_prefix': '/', 'min_depth': 1,
                         'exclude_paths': ['/undergraduate/professional-studies/']}}
        rule = program_rule(t)
        self.assertTrue(rule('https://catalog.unh.edu/undergraduate/liberal-arts/programs-study/anthropology/anthropology-major-ba/'))
        self.assertFalse(rule('https://catalog.unh.edu/undergraduate/professional-studies/manchester/programs-study/biotechnology/biotechnology-bs/'))
        self.assertTrue(excluded(t, 'https://catalog.unh.edu/undergraduate/professional-studies/online/x/'))
        self.assertFalse(excluded({'catalog': {}}, 'https://catalog.unh.edu/undergraduate/professional-studies/online/x/'))

    def test_unh_option_lines(self):
        import re
        from programs.extract import listed_emphasis_pages
        norm = lambda u: re.sub(r'/?$', '', u)
        lists = {'x': {'programs': [
            {'listed_as': 'bachelor', 'printed': 'Arts Major: Studio Art Option (B.A.)', 'url': 'https://a/arts-studio'},
            {'listed_as': 'bachelor', 'printed': 'Animal Science Major: Equine Studies Option (B.S.)', 'url': 'https://a/ans-eq'},
            {'listed_as': 'bachelor', 'printed': 'Animal Science Major (B.S.)', 'url': 'https://a/ans'},
            {'listed_as': 'bachelor', 'printed': 'Human Development and Family Studies Major: Early Childhood Education Option (Teacher Licensure) (B.S.)', 'url': 'https://a/hdfs-ece'},
            {'listed_as': 'bachelor', 'printed': 'Chemistry Major: Biochemistry Option (B.S.)', 'url': 'https://a/chem-bio'},
            {'listed_as': 'bachelor', 'printed': 'Chemistry Major (B.A.)', 'url': 'https://a/chem-ba'},
            {'listed_as': 'bachelor', 'printed': 'Fisheries and Ocean Sciences with a Concentration in Fisheries Science, B.S.', 'url': 'https://a/fish'},
            {'listed_as': 'bachelor', 'printed': 'Biology with a Concentration in Ecology, B.S.', 'url': 'https://a/bio-eco'},
            {'listed_as': 'bachelor', 'printed': 'Biology, B.S.', 'url': 'https://a/bio'}]}}
        self.assertEqual(sorted(u for _, u in listed_emphasis_pages(lists, norm)), ['https://a/arts-studio', 'https://a/chem-bio', 'https://a/fish', 'https://a/hdfs-ece'])

    def test_ncsu_and_bryant_concentration_lines(self):  # NC State, Bryant 2026-27 (Research request in #151)
        import re, tempfile, json as J
        from pathlib import Path
        from programs.extract import listed_emphasis_pages, collect_lists
        norm = lambda u: re.sub(r'/?$', '', u)
        L = lambda *rows: {'x': {'programs': [{'listed_as': 'bachelor', 'printed': p, 'url': f'https://a/{u}'} for p, u in rows]}}
        lists = L(('Animal Science (BS): Industry Concentration', 'ans-ind'), ('English (BA): Film Studies Concentration', 'eng-film'),
                  ('English (BA)', 'eng'), ('Computer Science (BS): Game Development Concentration', 'cs-game'),
                  ('Bachelor of Science in Business Administration: Accounting Concentration', 'bsba-acct'),
                  ('Bachelor of Arts in Communication: Media Concentration', 'comm-media'), ('Bachelor of Arts in Communication', 'comm'))
        self.assertEqual(sorted(u for _, u in listed_emphasis_pages(lists, norm)), ['https://a/ans-ind', 'https://a/bsba-acct', 'https://a/cs-game'])
        # the base line may print its award with dots ('English (B.A.)') and the concentration line without
        self.assertEqual(listed_emphasis_pages(L(('English (BA): Film Studies Concentration', 'f'), ('English (B.A.)', 'e')), norm), set())
        # a degree with a program page of its own in the run keeps its concentrations as options
        self.assertEqual(sorted(u for _, u in listed_emphasis_pages(lists, norm, {'x': {('computerscience', 'bs')}})), ['https://a/ans-ind', 'https://a/bsba-acct'])
        # VCU 2026-27: the award spelled out, then the concentration; a degree whose own line is listed keeps them as options
        vcu = L(('Chemistry, Bachelor of Science (B.S.) with a concentration in biochemistry', 'chem-bio'),
                ('Chemistry, Bachelor of Science (B.S.) with a concentration in chemical science', 'chem-sci'),
                ('Biology, Bachelor of Science (B.S.) with a concentration in ecology', 'bio-eco'), ('Biology, Bachelor of Science (B.S.)', 'bio'),
                ('Biology, Bachelor of Arts (B.A.) with a concentration in teaching', 'bio-ba'))
        self.assertEqual(sorted(u for _, u in listed_emphasis_pages(vcu, norm)), ['https://a/bio-ba', 'https://a/chem-bio', 'https://a/chem-sci'])
        # the complement: options of a listed degree (VCU biology ecology; OSU 'Zoology: Pre-Medical Sciences, BS' beside 'Zoology, BS'),
        # never a page a degree line also links
        from programs.extract import listed_option_pages
        osu = L(('Zoology, BS', 'zoo'), ('Zoology: Pre-Medical Sciences, BS', 'zoo-premed'), ('Marketing: Sports Marketing, BSBA', 'mkt-sport'),
                ('Geography, BA', 'geog'), ('Geography: Pre-Ministry, BA', 'geog'))
        self.assertEqual(sorted(u for _, u in listed_option_pages(vcu, norm)), ['https://a/bio-eco'])
        self.assertEqual(sorted(u for _, u in listed_option_pages(osu, norm)), ['https://a/zoo-premed'])
        # a list page stored by another run of the same catalog (NC State's discovery run) is read as stored; absent runs are skipped
        page = (b'<html><head><title>Undergraduate</title></head><body><p>University Catalog 2026-2027</p>'
                b'<a href="https://catalog.example.edu/ans/ans-bs-industry-concentration/">Animal Science (BS): Industry Concentration</a></body></html>')
        with tempfile.TemporaryDirectory() as d:
            other = Path(d) / 'disc'; f = FakeFetcher({'https://catalog.example.edu/undergraduate/': page}); run = C.Run(other)
            C.crawl_target({**TARGET, 'refetch': ['https://catalog.example.edu/undergraduate/']}, run, f, log=lambda *_: None)
            entries = [{**e, 'role': 'discover'} for e in run.entries()]
            (other / 'manifest.jsonl').write_text(''.join(J.dumps(e) + '\n' for e in entries))
            t = {**TARGET, 'catalog': {'platform': 'courseleaf', 'home': 'https://catalog.example.edu/', 'path_prefix': '/', 'min_depth': 1,
                                       'list_documents': [{'run': str(other), 'url': 'https://catalog.example.edu/undergraduate/'}]}}
            got = collect_lists(t, C.Run(Path(d) / 'cat'), [])
            self.assertEqual([p['printed'] for p in got['programs']], ['Animal Science (BS): Industry Concentration'])
            t['catalog']['list_documents'][0]['run'] = str(Path(d) / 'missing')
            self.assertEqual(collect_lists(t, C.Run(Path(d) / 'cat'), [])['programs'], [])

    def test_one_page_listed_under_two_awards(self):  # UT Dallas 2026: the BA and BS of one field link one page (#227 review)
        import tempfile
        from programs.extract import collect_lists, list_line, _degree_key
        u = 'https://catalog.example.edu/'
        page = ('<html><head><title>Undergraduate</title></head><body><p>University Catalog 2026-2027</p>'
                f'<a href="{u}nsm/biology/">Bachelor of Arts in Biology (120 semester credit hours)1</a>'
                f'<a href="{u}nsm/biology/">Bachelor of Science in Biology (120 semester credit hours)1, 4</a>'
                f'<a href="{u}nsm/biology/">Biology (BS)</a>'
                f'<a href="{u}nsm/chemistry/">Bachelor of Arts in Chemistry</a>'
                f'<a href="{u}nsm/chemistry/">Bachelor of Science in Physics</a>'
                f'<a href="{u}ah/literature/">Bachelor of Arts in Literature</a>'
                f'<a href="{u}ah/literature/">Literature (BA)</a>'
                f'<a href="{u}ah/literature/">BA in Literature - Pre-Law Concentration</a></body></html>').encode()
        with tempfile.TemporaryDirectory() as d:
            run = C.Run(Path(d) / 'cat'); f = FakeFetcher({u + 'undergraduate/': page})
            C.crawl_target({**TARGET, 'refetch': [u + 'undergraduate/']}, run, f, log=lambda *_: None)
            entries = [{**e, 'role': 'program_list'} for e in run.entries()]
            t = {**TARGET, 'catalog': {'platform': 'courseleaf', 'home': u, 'path_prefix': '/', 'min_depth': 1}}
            got = sorted(p['printed'] for p in collect_lists(t, run, entries)['programs'])
        # the BS of the same field on the same page is kept; the same award again ('Biology (BS)'), another field or an option
        # linking that page is not a second entry
        self.assertEqual(got, ['Bachelor of Arts in Biology (120 semester credit hours)1', 'Bachelor of Arts in Chemistry',
                               'Bachelor of Arts in Literature', 'Bachelor of Science in Biology (120 semester credit hours)1, 4'])
        self.assertEqual(list_line('Bachelor of Science in Data Science (120 semester credit hours)1, 4'), 'Bachelor of Science in Data Science')
        self.assertEqual(_degree_key(list_line('Bachelor of Arts in Literature (120 semester credit hours)1')), _degree_key('Literature (BA)'))

    def test_parenthetical_variant_lines(self):  # UT Arlington, Texas A&M-Kingsville 2026-27 (#148 follow-up)
        import re
        from programs.extract import listed_emphasis_pages, _degree_key
        norm = lambda u: re.sub(r'/?$', '', u)
        L = lambda *rows: {'x': {'programs': [{'listed_as': 'bachelor', 'printed': p, 'url': f'https://a/{u}'} for p, u in rows]}}
        lists = L(('Data Science BS (Biology)', 'ds-bio'), ('Data Science BS (Computer Science)', 'ds-cs'),
                  ('Kinesiology, B.S. (Sport Business)', 'kin-sb'), ('Geology BA (GIS)', 'geo-gis'),
                  ('Chemistry BA (UTeach)', 'chem-ut'), ('Chemistry BA', 'chem'),
                  ('Music, B.M. (Performance)', 'mus-perf'), ('Bachelor of Music in Music', 'mus'))
        self.assertEqual(sorted(u for _, u in listed_emphasis_pages(lists, norm)),
                         ['https://a/ds-bio', 'https://a/ds-cs', 'https://a/geo-gis', 'https://a/kin-sb'])
        # a degree with a program page of its own keeps its variants held
        self.assertEqual(sorted(u for _, u in listed_emphasis_pages(lists, norm, {'x': {('geology', 'ba')}})),
                         ['https://a/ds-bio', 'https://a/ds-cs', 'https://a/kin-sb'])
        self.assertEqual(_degree_key('Chemistry BA'), ('chemistry', 'ba'))
        self.assertEqual(_degree_key('Bachelor of Music in Music'), ('music', 'bm'))
        self.assertEqual(_degree_key('Bachelor of Fine Arts in Theatre'), _degree_key('Theatre (BFA)'))
        self.assertIsNone(_degree_key('Chemistry Ba'))  # the award is printed in capitals
        self.assertEqual(listed_emphasis_pages(L(('Chemistry (Pre-Med)', 'c')), norm), set())  # no award printed: no degree line
        self.assertEqual(listed_emphasis_pages(L(('Marine Bio (Ecology)', 'm')), norm), set())  # 'Bio' is a word, not an award

    def test_reader_requests_153(self):  # CA/NY/PA 2026-27 (shared reader requests #153)
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/p/', 'role': 'program_page', 'sha256': 'a' * 64, 'fetched_at': '2026-10-07T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        def static(name, title=None, heads=None):
            page = T.Page('2026-2027 Catalog\n' + name, title or name + ' < X', [], [], heads or ['2026-2027 Catalog', name])
            return [c['record']['program_name'] for c in X.static_program_identity({'institution_key': 'k'}, e, page, '2026-27')]
        for bad in ('Bachelor of Arts in Economics Roadmap – Quantitative Reasoning Category 1/2', 'ADN to BSN Roadmap CSM',
                    'Department of Nursing (BSN Pre-licensure)', 'Requirements for a Bachelor’s Degree', 'Bachelor’s Degree Requirements Archive',
                    'Modern Language Language for BA Degree (Undergraduate)', 'BS in Information Systems Program Educational Objectives',
                    'B.A. in Theatre Minimum Grade Requirement'):
            self.assertEqual(static(bad), [], bad)
        self.assertEqual(static('Archival Studies, B.A.'), ['Archival Studies, B.A.'])
        self.assertTrue(X.GENERIC_DEGREES.match('Bachelor’s Degrees'))  # UC Davis prints a curly apostrophe
        self.assertEqual(static('Economics, B.A.'), ['Economics, B.A.'])
        # department sections: a section that names a policy of the degree is not a degree
        dep = lambda h: X.department_section_candidates({'institution_key': 'k'}, e, T.Page('2026-2027 Undergraduate Catalog\n' + h, 't', [], [], [h]), '2026-27')
        self.assertEqual(dep('B.S. in Public Health Minimum Grade Requirement for MAT 12'), [])
        self.assertEqual([c['record']['program_name'] for c in dep('B.S. in Public Health')], ['B.S. in Public Health'])
        # UNL: 'Requirements for the Bachelor of Science in ...' names the degree after the prefix
        self.assertEqual(len(dep('Requirements for the Bachelor of Science in Criminology and Criminal Justice (120 Hours)')), 1)
        # UC Davis: the heading runs the college on after the name the title prints
        heads = ['2026-2027 General Catalog', 'Business, Bachelor of Science Graduate School of Management', 'The Major Program']
        page = T.Page('2026-2027 General Catalog\n' + heads[1], 'General Catalog - Business, Bachelor of Science', [], [], heads)
        self.assertEqual(X.program_heading(page), 'Business, Bachelor of Science')
        page = T.Page('', 'General Catalog - Business, Bachelor of Science', [], [], ['2026-2027 General Catalog', 'Business, Bachelor of Science with Honors'])
        self.assertEqual(X.program_heading(page), 'Business, Bachelor of Science with Honors')  # not a college: the heading stands
        # Coursedog cards: the description printed right after the name
        f = X.coursedog_card_name
        self.assertEqual(f('Accounting - BSThe B.S. in Accounting will prepare students for careers'), 'Accounting - BS')
        self.assertEqual(f('Bachelor of Arts - PsychologyThe mission of the Undergraduate Psychology Department at Cal'), 'Bachelor of Arts - Psychology')
        self.assertEqual(f('Accounting (BS)The program prepares you for a career in'), 'Accounting (BS)')
        self.assertEqual(f('MacArthur Studies BA'), 'MacArthur Studies BA')
        self.assertEqual(f('Bachelor of Science - McKinney Leadership Studies'), 'Bachelor of Science - McKinney Leadership Studies')

    def test_texas_am_dash_award_track_lines(self):  # Texas A&M 2026-27 Program Search list
        import re
        from programs.extract import listed_emphasis_pages
        norm = lambda u: re.sub(r'/?$', '', u)
        L = lambda *rows: {'x': {'programs': [{'listed_as': 'bachelor', 'printed': p, 'url': f'https://a/{u}'} for p, u in rows]}}
        lists = L(('Civil Engineering -\u200b BS, Coastal Engineering Track', 'cv1'), ('Civil Engineering -\u200b BS, Structural Engineering Track', 'cv2'),
                  ('Finance -\u200b BBA', 'fin'), ('Finance -\u200b BBA, Real Estate Track', 'fin-re'),
                  ('Civil Engineering -\u200b MS', 'cv-ms'), ('History - BA, Pre-Law', 'hist-pl'))
        self.assertEqual(sorted(u for _, u in listed_emphasis_pages(lists, norm)), ['https://a/cv1', 'https://a/cv2'])

    def test_static_reader_passes_track_pages_to_the_listed_rule(self):  # Texas A&M track pages
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/undergraduate/eng/civil/bs-coastal-engineering-track/', 'role': 'program_page', 'sha256': 'a' * 64,
             'fetched_at': '2026-10-06T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        name = 'Civil Engineering - BS, Coastal Engineering Track'
        page = T.Page('2026-2027 Edition\n' + name, name + ' < X Catalogs', [], [], ['X Catalogs', '2026-2027 Edition', name])
        got = X.static_program_identity({'institution_key': 'k'}, e, page, '2026-27')
        self.assertEqual([c['record']['program_name'] for c in got], [name])
        # unless the list prints it as the degree's only entry, the extraction loop drops it as an option page
        self.assertTrue(X.drops_option_page(got, 'k', e['url'], set()))
        self.assertFalse(X.drops_option_page(got, 'k', e['url'], {('k', X.norm_emph(e['url']))}))

    def test_degree_page_plan_headings_keep_the_degree(self):  # Colorado, Maryland, Missouri, Tennessee, KU engineering 2026-27
        from pipeline import text as T
        e = {'url': 'https://catalog.x.edu/as/anthropology/anthropology-bachelor-arts-ba/', 'role': 'program_page', 'sha256': 'a' * 64,
             'fetched_at': '2026-10-06T00:00:00+00:00', 'status': 200, 'kind': 'html'}
        tgt = {'catalog': {'platform': 'courseleaf'}}
        for plan in ('Recommended Four-Year Plan of Study', 'The recommended 4-year plan is listed below by semester.', 'Sample Four-Year Plan'):
            page = T.Page('2026-2027 Academic Catalog\nBA in Anthropology\nRequirements\nStudents complete 30 hours in the major.\nMajor GPA of 2.0.\n' + plan,
                          'BA in Anthropology', [], [], ['BA in Anthropology'])
            self.assertTrue([c for c in X.program_page_candidates(tgt, {'institution_key': 'k'}, e, page, '2026-27') if c['domain'] == 'academic_programs'], plan)

    def test_award_glued_to_next_column_is_classified(self):
        from programs.extract import list_award
        glued = 'Architecture, B.ArchSmith College of Engineering and TechnologyUndergraduateBachelor'
        self.assertEqual(list_award(glued, glued), 'bachelor')
        self.assertIsNone(list_award('Accounting, MinorWoodbury School of BusinessUndergraduateMinor', 'Accounting, Minor'))

    def test_listed_emphasis_page_is_kept(self):
        from programs.extract import drops_option_page
        found = [{'domain': 'academic_programs', 'record': {'program_name': 'Political Science - American Government Emphasis, B.A.'}}]
        self.assertFalse(drops_option_page(found, 'k', 'https://a/ps-ag/', {('k', 'https://a/ps-ag')}))
        self.assertTrue(drops_option_page(found, 'k', 'https://a/ps-ag/', set()))

    def test_autoreview_approves_a_listed_emphasis_only_without_a_base_degree(self):
        from programs import autoreview as A
        from datetime import date
        T = AutoReviewTests()
        def at(c, url): c['record']['program_url'] = url; return c
        cands = [at(T.prog('e1', 'Political Science - American Government Emphasis, B.A.'), 'https://a/ps-ag'),
                 at(T.prog('e2', 'Biology - Ecology Emphasis, B.S.'), 'https://a/bio-eco'), at(T.prog('b', 'Biology, B.S.'), 'https://a/bio')]
        lists = {'k': {'programs': [{'listed_as': 'bachelor', 'printed': 'Political Science - American Government Emphasis, B.A.', 'url': 'https://a/ps-ag'},
                                    {'listed_as': 'bachelor', 'printed': 'Biology - Ecology Emphasis, B.S.', 'url': 'https://a/bio-eco'},
                                    {'listed_as': 'bachelor', 'printed': 'Biology, B.S.', 'url': 'https://a/bio'}]}}
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try: approve, _, held = A.review('ZZ', T.run_dir(cands, lists=lists), today=date(2026, 10, 7))
        finally: A.catalog_records = old
        self.assertEqual({a['candidate_id'] for a in approve}, {'e1', 'b'})
        self.assertEqual(held['option_name'], 1)

    def test_department_page_yields_to_the_program_page_beneath_it(self):  # Cal Poly 2026-2028
        from programs import autoreview as A
        from datetime import date
        T = AutoReviewTests()
        def at(c, url, field='program_url'): c['record'][field] = url; return c
        D = 'https://catalog.calpoly.edu/engineering/aerospace'
        mk = lambda child: [at(T.prog('dept', 'Aerospace Engineering (BS)', key='ae'), D + '/'),
                            at(T.prog('own', 'Aerospace Engineering (BS)', key='ae'), D + '/' + child + '/'),
                            at(T.req('r-dept', 'ae'), D + '/', 'source_url'), at(T.req('r-own', 'ae'), D + '/' + child + '/', 'source_url')]
        old = A.catalog_records; A.catalog_records = lambda *a: []
        try:
            approve, _, held = A.review('ZZ', T.run_dir(mk('aerospace-engineering-bs')), today=date(2026, 10, 7))
            self.assertEqual({a['candidate_id'] for a in approve}, {'own', 'r-own'})
            self.assertEqual(held['department_page'], 1); self.assertEqual(held['req_department_page'], 1)
            # a page beneath that is not named for the program (Willamette '.../BS.BIOL/general-aoYks') changes nothing
            approve, _, held = A.review('ZZ', T.run_dir(mk('general-aoYks')), today=date(2026, 10, 7))
            self.assertEqual(held['department_page'], 0)
        finally: A.catalog_records = old

    def test_general_requirements_pages_are_not_programs(self):  # Cal Poly 2026-2028, Idaho 2026-27 policy pages
        from programs.extract import NOT_PROGRAM_NAME
        for n in ["General Requirements – Bachelor's Degree", 'General Requirements for all B.A., B.S., and B.Mus. Degrees',
                  "Requirements for a Bachelor's Degree"]:
            self.assertTrue(NOT_PROGRAM_NAME.search(n), n)
        for n in ['General Studies (BA)', 'Requirements Engineering (BS)']:
            self.assertFalse(NOT_PROGRAM_NAME.search(n), n)

    def test_matriculation_sentences_are_evidence(self):
        from programs.extract import EVIDENCE
        rx = dict(EVIDENCE)['apply_to_major']
        for s in ['To be considered matriculated in the Accounting degree, a student must complete the following courses with at least a C- grade:',
                  'To be admitted to the BSME program, a student must complete the foundation courses in Mathematics.',
                  'All prerequisite courses must be completed prior to application.',
                  'Each application for acceptance into the program is for a specific semester only.']:
            self.assertTrue(rx.search(s), s)
class NationalStatusTests(unittest.TestCase):
    def test_registered_researched_covered_kept_apart(self):
        from programs import status
        n = status.national([{'state': 'TN', 'covered_institutions': 1, 'institutions': [
            {'status': 'covered', 'queue': []}, {'status': 'exception', 'queue': ['institution:bot_challenge']},
            {'status': 'exception', 'queue': ['institution:not_yet_researched']}, {'status': 'not_started', 'queue': []}]}])
        tn = next(r for r in n['states'] if r['state'] == 'TN')
        self.assertEqual((tn['researched'], tn['covered'], tn['tracked']), (2, 1, True))
        self.assertEqual(len(n['states']), 51)  # every registry jurisdiction, tracked or not
        self.assertTrue(all(r['researched'] == r['covered'] == 0 for r in n['states'] if not r['tracked']))
        self.assertEqual(n['registered'], sum(r['registered'] for r in n['states']))


class EnteringWeightTests(unittest.TestCase):
    def test_open_admission_school_weighed_by_fall_first_time_count(self):
        from programs import status
        w = status.entering('UT')
        self.assertGreater(w.get('ipeds-230737', 0), 0)  # UVU files no ADM survey; EF2023A first-time count is used
        self.assertEqual(w.get('ipeds-230728'), 4388)    # an ADM 'enrolled' count is kept as reported


class CandidateIdentityTests(unittest.TestCase):
    """One candidate per id (TX 2026-10-07-flag3, LMU and UNK 2026-27)."""

    def cand(self, cid, url, rd, issues=()):
        return {'candidate_id': cid, 'domain': 'degree_requirements', 'issues': list(issues), 'extractor': 'x',
                'source': {'url': url, 'fetched_at': url}, 'record': {'program_key': 'p', 'source_url': url, 'rule_details': rd}}

    def test_page_read_twice_gives_one_candidate(self):
        from programs.extract import distinct_candidates
        out = distinct_candidates([self.cand('a', 'https://x/p/', [1]), self.cand('a', 'http://x//p/', [1]), self.cand('b', 'https://x/q/', [2])])
        self.assertEqual([(c['candidate_id'], c['source']['url']) for c in out], [('a', 'https://x/p/'), ('b', 'https://x/q/')])
        self.assertEqual([c['issues'] for c in out], [[], []])

    def test_same_id_different_content_is_held(self):
        from programs.extract import distinct_candidates
        out = distinct_candidates([self.cand('a', 'https://x/p/', [1]), self.cand('a', 'https://x/p/', [2])])
        self.assertEqual(len(out), 2)
        self.assertTrue(all('candidate_id_collision' in c['issues'] for c in out))

    def test_plan_headings_alike_for_80_characters_get_distinct_keys(self):  # LMU 2026-27 math-placement plans
        from programs.courseleaf import labelled_keys
        from pipeline.extractors.catalog import slug
        h = 'Model 4-Year Plan–Bachelor of Business Administration–Finance Major Curriculum–Math placement MATH '
        keys = labelled_keys([h + '101', h + '110', h + '112'], slug)
        self.assertEqual(len(set(keys)), 3)
        self.assertEqual(keys[2], slug(h + '112'))  # the last keeps the key stored before this rule
        self.assertEqual(labelled_keys(['Robotics Concentration', 'Without Concentration'], slug), ['robotics-concentration', 'without-concentration'])


class CatalogCountTests(unittest.TestCase):
    """programs/catalog_counts.py: catalog completeness from a reviewed decision (rule used since #175)."""

    def run_dir(self, d, listing, records, approved=None):
        d = Path(d); lo = 'https://catalog.x.edu/programs/'
        (d / 'program_lists.json').write_text(json.dumps({'k': {'programs': [
            {'printed': p, 'url': u, 'listed_as': la, 'listed_on': lo} for p, u, la in listing]}}))
        (d / 'manifest.jsonl').write_text(json.dumps({'url': lo, 'sha256': 'a' * 64, 'fetched_at': '2026-10-08T00:00:00+00:00'}) + '\n')
        lines = []
        for i, (name, url) in enumerate(records):
            lines.append(json.dumps({'candidate_id': f'c{i}', 'institution_key': 'k', 'domain': 'academic_programs',
                                     'record': {'program_name': name, 'program_key': f'p{i}'}, 'source': {'requested_url': url}}))
        (d / 'candidates.jsonl').write_text('\n'.join(lines) + '\n')
        (d / 'dec.json').write_text(json.dumps({'approve': [{'candidate_id': f'c{i}'} for i in range(len(records)) if approved is None or i in approved]}))
        return d

    def test_every_entry_is_accounted_for(self):
        import tempfile
        from programs.catalog_counts import entries
        u = 'https://catalog.x.edu/'
        listing = [('Anthropology, BAAnthropology, BA', u + 'anth-ba/', 'bachelor'),           # card prints the name twice
                   ('Individual Major, BSE', u + 'im-bse/', 'bachelor'),                       # not the 'E' of 'BSE' after 'BS'
                   ('Individual Major, BS', u + 'im-bs/', 'bachelor'),
                   ('Individual Major, BS', u + 'im-bs-2/', 'bachelor'),                       # same name, second link: counted once
                   ('Accounting - BSThe B.S. in Accounting prepares students for careers.', u + 'acct/', 'bachelor'),  # run-on description
                   ('Communication, B.A./M.A. (4+1 year)', u + 'comm-bama/', 'bachelor'),        # combined: excluded by name
                   ('Business, BSFinance Option', u + 'bus-fin/', 'bachelor'),                 # a short run-on is not a description
                   ('History, B.A.', u + 'history-ba/', 'bachelor'),                           # credited through its own page (http vs https)
                   ('Biology: Concentration in Ecology, B.S.', u + 'biology-bs/', 'bachelor'),  # not credited through Biology's page
                   ('Environmental Studies Major', u + 'envst/', 'major')]                     # prints no award: named, not counted
        records = [('Anthropology, BA', u + 'anth-ba/'), ('Individual Major, BS', u + 'im-bs/'), ('Accounting - BS', 'https://api.x.com/feed'),
                   ('Business, BS', 'https://api.x.com/feed2'),
                   ('Bachelor of Arts (B.A.) Major in History', 'http://catalog.x.edu/history-ba/'), ('Biology', u + 'biology-bs/')]
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, listing, records)
            e = entries(d, d / 'dec.json', ['k'], reviewed='2026-10-08')[0]
        self.assertEqual((e['listed_bachelor_programs'], e['verified_listed_programs'], e['programs_complete']), (7, 4, False))
        b = e['completeness_basis']
        self.assertIn("not counted, 1 combined or accelerated bachelor's/master's entries: Communication, B.A./M.A. (4+1 year)", b)
        self.assertIn('print no award and are not counted: Environmental Studies Major', b)
        self.assertTrue(b.endswith("Not recorded (names separated by ' | '): Biology: Concentration in Ecology, B.S. | Business, BSFinance Option | Individual Major, BSE."))

    def test_options_of_a_listed_degree_are_one_program(self):
        import tempfile
        from programs.catalog_counts import entries
        u = 'https://catalog.x.edu/'
        listing = [('Chemistry, Bachelor of Science (B.S.)', u + 'chem/', 'bachelor'),
                   ('Chemistry, Bachelor of Science (B.S.) with a concentration in biochemistry', u + 'chem-bio/', 'bachelor'),
                   ('Physics, Bachelor of Science (B.S.) with a concentration in astronomy', u + 'phys-astro/', 'bachelor')]  # no Physics line
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, listing, [('Chemistry, Bachelor of Science (B.S.)', u + 'chem/')])
            e = entries(d, d / 'dec.json', ['k'])[0]
        self.assertEqual((e['listed_bachelor_programs'], e['verified_listed_programs']), (2, 1))
        self.assertIn("not counted, 1 concentrations or options of a degree whose own line is listed: "
                      "Chemistry, Bachelor of Science (B.S.) with a concentration in biochemistry", e['completeness_basis'])
        self.assertTrue(e['completeness_basis'].endswith("Not recorded (names separated by ' | '): "
                                                         "Physics, Bachelor of Science (B.S.) with a concentration in astronomy."))

    def test_award_only_entries_and_category_labels(self):
        import tempfile
        from programs.catalog_counts import entries
        u = 'https://catalog.x.edu/'
        # Missouri: 'BA' / 'BS*' under department headings, each its own program; UTEP: card labels run on to the name
        listing = [('BA', u + 'anth/ba-anthropology/', 'bachelor'), ('BA', u + 'art/ba-art/', 'bachelor'), ('BS*', u + 'ds/bs-data-science/', 'bachelor'),
                   ('BBA in AccountingBusiness, Management, & MarketingBachelorsUndergraduateBusiness Administration', u + 'acct-bba/', 'bachelor'),
                   ('BA in Chicano StudiesBachelorsHumanities, Languages, and Literatures', u + 'chicano-ba/', 'bachelor'),
                   ("Bachelor's Degree Programs", u + 'programs/', 'bachelor'),  # Georgia Tech: the list's own heading link
                   ('Bachelor of Music', u + 'music/bachelor-of-music-general/', 'bachelor'),  # UTEP: the record prints the same name
                   ('Marketing, BSBA', u + 'mkt-bsba/', None),  # OSU: an undotted award the list reader left unclassified
                   ('BIOLOGY', u + 'biology/', 'bachelor'),  # an all-caps name is a name, not an award
                   ('Bio', u + 'bio/', 'bachelor'),  # nor is a short capitalised word
                   ('Physics, Bachelor of Science (B.S.)', u + 'phys/', None),  # VCU: a spelled-out award the reader left unclassified
                   ('Accounting, BSBA/MBA (4 year)', u + 'acct-mba/', None),  # La Salle: combined, excluded by name
                   ('BSBA Graduation Requirements', u + 'bsba-grad/', None),  # YSU: a policy page
                   ('Spanish Studies (Secondary Major) (BA)', u + 'span-sec/', 'bachelor'),  # BYU: not earned alone
                   ('Biology, BA to Secondary Education, MA Accelerated Program', u + 'bio-acc/', 'bachelor'),  # Roosevelt: combined
                   ('Digital Marketing, BA to Marketing Communications, MSIMC', u + 'dm-msimc/', 'bachelor'),  # Roosevelt: combined
                   ('Biology BS, Pharmacy PharmD Dual Degree Acceptance Program', u + 'bio-pharmd/', 'bachelor'),  # Roosevelt: combined
                   ('Biology, BS/BA to Biology, MS Accelerated Program', u + 'bio-ms-acc/', 'bachelor'),  # Roosevelt: combined
                   ('Mathematics Path to Media Accelerated BA', u + 'math-path/', 'bachelor'),  # not combined: no master's award
                   ('Business Administration Dept. Major, B.S./Business Administration, M.B.A.', u + 'bsmba/', 'bachelor'),  # Georgian: combined
                   ('Minor in Nutrition (Traditional BSN)', u + 'min/', 'bachelor'),  # APU: a minor
                   ('Physics B.A. (College of Arts and Sciences)', u + 'physics/physicsba/', 'bachelor'),  # UVM: the college is not a qualifier
                   # Colorado State: concentration rows count with their major (identified by the major's page); dual degrees by page
                   ('B.A.', u + 'pols/political-science-major/', 'bachelor'),
                   ('B.A. Concentration', u + 'pols/political-science-major-public-policy-concentration/', 'bachelor'),
                   ('B.S. Concentration', u + 'cs/computer-science-major-ai-concentration/', 'bachelor'),
                   ('B.S. Concentration', u + 'cs/computer-science-major-software-concentration/', 'bachelor'),
                   ('Dual Degree B.S.', u + 'bme/bme-me-dual/', 'bachelor'), ('Dual Degree B.S.', u + 'bme/bme-cpe-dual/', 'bachelor')]
        records = [('BA in Anthropology', u + 'anth/ba-anthropology/'), ('BA in Art', u + 'art/ba-art/'),
                   ('BBA in Accounting', 'https://api.x.com/feed'), ('BA in Chicano Studies', u + 'chicano-ba/'),
                   ('Bachelor of Music', u + 'music/bachelor-of-music-general/'), ('Marketing, BSBA', u + 'mkt-bsba/'), ('Biology, BS', u + 'biology/'), ('Biology, BA', u + 'bio/'),
                   ('Physics B.A.', u + 'physics/physicsba/'), ('Major in Political Science', u + 'pols/political-science-major/')]
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, listing, records)
            e = entries(d, d / 'dec.json', ['k'])[0]
        self.assertEqual((e['listed_bachelor_programs'], e['verified_listed_programs']), (16, 10))
        b = e['completeness_basis']
        self.assertIn('7 print only an award under a department heading and are identified by their own page', b)
        self.assertTrue(b.startswith("28 linked entries"))
        self.assertIn("3 concentration rows print only an award and are counted with their major, identified by the major's page (1 majors are listed only through concentrations)", b)
        self.assertIn("not counted, 6 combined", b); self.assertIn("Mathematics Path to Media Accelerated BA", b.split("Not recorded")[-1]); self.assertNotIn("Digital Marketing", b.split("Not recorded")[-1])
        self.assertIn("Accounting, BSBA/MBA (4 year)", b); self.assertIn("BSBA Graduation Requirements", b)
        self.assertIn("2 run the card's category labels on to the name", b)
        self.assertIn("not counted, 4 department, roadmap, general or commissioning links that are not a single bachelor's program: BSBA Graduation Requirements | Bachelor's Degree Programs | Minor in Nutrition (Traditional BSN) | Spanish Studies (Secondary Major) (BA)", b)
        miss = b.split("Not recorded (names separated by ' | '): ")[1].rstrip('.').split(' | ')
        self.assertEqual(len(miss), 6)  # BS*, the CS major (only concentrations), two dual degrees, Physics, Mathematics Path
        self.assertTrue(any(m.startswith('B.S. Concentration (https://catalog.x.edu/cs/') for m in miss))
        self.assertEqual(sum(m.startswith('Dual Degree B.S.') for m in miss), 2)
        # a concentration row whose link names no major refuses the count (Colorado State's nested concentration pages)
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, [('B.S.', u + 'cs/computer-science-major/', 'bachelor'), ('B.S. Concentration', u + 'cs/computer-science-major/ai-concentration/', 'bachelor')],
                             [('Major in Computer Science', u + 'cs/computer-science-major/')])
            with self.assertRaises(ValueError): entries(d, d / 'dec.json', ['k'])

    def test_filter_labels_after_the_award(self):
        import tempfile
        from programs.catalog_counts import entries
        u = 'https://catalog.x.edu/'
        # ODU 2026-27: each row runs the award on to its filter labels ('Undergraduate', 'Bachelor's', subject, college)
        listing = [("Art with a Major in Art History, BAArtsUndergraduateBachelor'sHumanitiesCollege of Arts and Letters", u + 'art-history-ba/', 'bachelor'),
                   ("Chemistry with a Major in Chemical Forensic Science (BS)UndergraduateBachelor'sNatural SciencesCollege of Sciences", u + 'chem-fs/', 'bachelor'),
                   ("Cybersecurity with a Major in Artificial Intelligence for CybersecurityUndergraduateBachelor'sSchool of Cybersecurity", u + 'cyber-ai/', 'bachelor'),
                   ("Physics with a Major in Physics and Master of Business Administration, BS-MBAUndergraduateBachelor'sCollege of Sciences", u + 'phys-mba/', 'bachelor'),
                   ("Naval Science, NROTCUndergraduateBachelor'sEngineering & TechnologyBatten College", u + 'nrotc/', 'bachelor'),
                   ("Biology, BSUndergraduateBachelor'sNatural SciencesCollege of Sciences", u + 'biology-bs/', 'bachelor'),
                   ("Medical Technology, BS-MT", u + 'mt/', 'bachelor')]  # a hyphenated single award, not combined
        records = [('Art with a Major in Art History (BA)', u + 'art-history-ba/'), ('Chemistry with a Major in Chemical Forensic Science (BS)', 'https://api.x.com/f'),
                   ('Biology (BS)', u + 'biology-bs/')]
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, listing, records)
            e = entries(d, d / 'dec.json', ['k'])[0]
        b = e['completeness_basis']
        self.assertEqual((e['listed_bachelor_programs'], e['verified_listed_programs']), (5, 3), b)
        self.assertIn("6 run the award on to the row's filter labels", b)
        self.assertIn("combined or accelerated bachelor's/master's entries: Physics with a Major in Physics and Master of Business Administration, BS-MBA", b)
        self.assertIn("commissioning links that are not a single bachelor's program: Naval Science, NROTC", b)
        self.assertTrue(b.endswith("Not recorded (names separated by ' | '): Cybersecurity with a Major in Artificial Intelligence for Cybersecurity | Medical Technology, BS-MT."), b)

    def test_on_file_recount_credits_records_on_file_once_per_page(self):
        import tempfile
        from programs.catalog_counts import on_file_approvals
        u = 'https://catalog.x.edu/'
        with tempfile.TemporaryDirectory() as d:
            d = Path(d); run = d / 'run'; run.mkdir()
            cands = [('c1', 'Accounting (BSBA)', u + 'acct-bsba/', 'accounting-bsba'),       # one record on this page, another name
                     ('c2', 'Bachelor of Science in Accounting', u + 'acct-bsba/', 'x2'),      # second candidate on the same page
                     ('c3', 'Biology (BS)', u + 'bio-bs/', 'biology-bs'),                      # same program key
                     ('c4', 'Chemistry (BS)', u + 'chem-bs/', 'chemistry-bs'),                 # no record on file
                     ('c5', 'Art (BA)', u + 'art/', 'art-ba')]                                  # page with two records, other name
            (run / 'candidates.jsonl').write_text('\n'.join(json.dumps({'candidate_id': i, 'institution_key': 'k', 'domain': 'academic_programs',
                'record': {'program_name': n, 'program_url': url, 'program_key': pk}, 'source': {'requested_url': url}}) for i, n, url, pk in cands) + '\n')
            f = d / 'data/institutions/x/academic_programs'; f.mkdir(parents=True)
            rec = lambda pk, n, url, st='verified': {'program_key': pk, 'program_name': n, 'program_url': url, 'source_url': url, 'credential_level': 'bachelor', 'verification_status': st}
            (f / '2026-27.json').write_text(json.dumps({'records': [rec('bsba-acct', 'BSBA in Accounting', u + 'acct-bsba/'), rec('biology-bs', 'Biology, BS', u + 'bio-bs/'),
                rec('art-studio', 'Art Studio (BA)', u + 'art/'), rec('art-history', 'Art History (BA)', u + 'art/'), rec('chemistry-x', 'Chemistry (BS)', u + 'chem-bs/', 'unverified')]}))
            got = [a['candidate_id'] for a in on_file_approvals(run, 'x', 'k', root=d)]
        self.assertEqual(got, ['c1', 'c3'])

    def test_on_file_recount_credits_each_keyed_record_on_a_two_degree_page(self):  # UT Dallas 'Biology (BA, BS)'
        import tempfile
        from programs.catalog_counts import on_file_approvals
        u = 'https://catalog.x.edu/bio'
        with tempfile.TemporaryDirectory() as d:
            d = Path(d); run = d / 'run'; run.mkdir()
            cands = [('c1', 'Bachelor of Arts in Biology', 'biology-ba'), ('c2', 'Bachelor of Science in Biology', 'biology-bs'),
                     ('c3', 'Bachelor of Science in Biology', 'biology-bs')]  # a second reading of the same record
            (run / 'candidates.jsonl').write_text('\n'.join(json.dumps({'candidate_id': i, 'institution_key': 'k', 'domain': 'academic_programs',
                'record': {'program_name': n, 'program_url': u, 'program_key': pk}, 'source': {'requested_url': u}}) for i, n, pk in cands) + '\n')
            f = d / 'data/institutions/x/academic_programs'; f.mkdir(parents=True)
            rec = lambda pk, n: {'program_key': pk, 'program_name': n, 'program_url': u, 'source_url': u, 'credential_level': 'bachelor', 'verification_status': 'verified'}
            (f / '2026-27.json').write_text(json.dumps({'records': [rec('biology-ba', 'Bachelor of Arts in Biology'), rec('biology-bs', 'Bachelor of Science in Biology')]}))
            got = [a['candidate_id'] for a in on_file_approvals(run, 'x', 'k', root=d)]
        self.assertEqual(got, ['c1', 'c2'])

    def test_edition_page_titled_for_two_awards(self):  # UT Dallas 2026
        from programs.extract import edition_degrees
        from pipeline import text as T
        page = lambda *h: T.Page('', 'Biology (BA, BS) - UT Dallas 2026 Undergraduate Catalog', [], [], list(h))
        both = page('School', 'Biology (BA, BS)', 'Bachelor of Arts in Biology', 'Faculty', 'Bachelor of Science in Biology')
        self.assertEqual([(n, k) for n, k, _ in edition_degrees('Biology (BA, BS)', both)],
                         [('Bachelor of Arts in Biology', 'biology-ba'), ('Bachelor of Science in Biology', 'biology-bs')])
        one = page('School', 'Biology (BA, BS)', 'Bachelor of Arts in Biology')  # the BS heading isn't printed: not split
        self.assertEqual([n for n, _, _ in edition_degrees('Biology (BA, BS)', one)], ['Biology (BA, BS)'])
        self.assertEqual([n for n, _, _ in edition_degrees('Animation and Games (BA)', page('Animation and Games (BA)'))], ['Animation and Games (BA)'])
        self.assertEqual([n for n, _, _ in edition_degrees('Arts (BA, BX)', page('Bachelor of Arts in Arts'))], ['Arts (BA, BX)'])  # unknown award

    def test_programs_az_table_count(self):  # Colorado State 2026-27 Programs A-Z table
        import tempfile, gzip
        from programs.catalog_counts import table_entries
        u = 'https://catalog.x.edu/'; lo = u + 'programsaz/'
        rows = [['Business Administration', 'Business', 'BU', 'Undergraduate', 'Main', 'B.S.'],
                ['Accounting, Business Administration, Accounting Concentration', 'Accounting', 'BU', 'Undergraduate', 'Main', 'B.S. Concentration'],
                ['Finance, Business Administration, Finance Concentration', 'Finance', 'BU', 'Undergraduate', 'Main', 'B.S. Concentration'],
                ['Finance Concentration, Corporate Finance Option', 'Finance', 'BU', 'Undergraduate', 'Main', 'B.S. Concentration Option'],
                ['Computer Science, Artificial Intelligence Concentration', 'CS', 'NS', 'Undergraduate', 'Main', 'B.S. Concentration'],
                ['Computer Science, Software Concentration', 'CS', 'NS', 'Undergraduate', 'Main', 'B.S. Concentration'],
                ['Dance', 'Dance', 'LA', 'Undergraduate', 'Main', 'B.A. and B.F.A.'],
                ['Nutrition Science, Nursing Concentration', 'Nutrition', 'HS', 'Undergraduate', 'Main', 'B.S. Concentration'],
                ['Human Development, Nursing Concentration', 'HD', 'HS', 'Undergraduate', 'Main', 'B.S. Concentration'],
                ['Human Development Studies, Aging Concentration', 'HD', 'HS', 'Undergraduate', 'Main', 'B.S. Concentration'],
                ['Accountancy', 'Accounting', 'BU', 'Graduate', 'Main', 'M.Acc.'],
                ['Business Minor', 'Business', 'BU', 'Undergraduate', 'Main', 'Minor']]
        links = [(u + 'business-administration-major/', 'B.S.'), (u + 'business-administration-major-accounting-concentration/', 'B.S. Concentration'),
                 (u + 'business-administration-major-finance-concentration/', 'B.S. Concentration'), (u + 'finance-option/', 'B.S. Concentration Option'),
                 (u + 'computer-science-major-ai-concentration/', 'B.S. Concentration'), (u + 'computer-science-major-software-concentration/', 'B.S. Concentration'),
                 (u + 'dance/', 'B.A. and B.F.A.'),
                 (u + 'human-development-major-nursing-concentration/', 'B.S. Concentration'),  # Nutrition's row links HD's page
                 (u + 'human-development-major-nursing-concentration/', 'B.S. Concentration'),
                 (u + 'human-development-major-aging-concentration/', 'B.S. Concentration'),  # another major's link resolving to the same page
                 (u + 'accountancy/', 'M.Acc.'), (u + 'business-minor/', 'Minor')]
        records = [{'program_key': 'ba', 'program_name': 'Major in Business Administration', 'credential_level': 'bachelor', 'verification_status': 'verified',
                    'program_url': u + 'business-administration-major/', 'source_url': u + 'business-administration-major/'},
                   {'program_key': 'dba', 'program_name': 'Major in Dance, B.A.', 'credential_level': 'bachelor', 'verification_status': 'verified',
                    'program_url': u + 'dance/dance-ba/', 'source_url': u + 'dance/dance-ba/'},
                   {'program_key': 'hd', 'program_name': 'Major in Human Development', 'credential_level': 'bachelor', 'verification_status': 'verified',
                    'program_url': u + 'human-development-major/', 'source_url': u + 'human-development-major/'},
                   {'program_key': 'x', 'program_name': 'Major in Geology', 'credential_level': 'bachelor', 'verification_status': 'unverified',
                    'program_url': u + 'geology-major/', 'source_url': u + 'geology-major/'}]
        with tempfile.TemporaryDirectory() as d:
            d = Path(d); (d / 'pages').mkdir()
            (d / 'pages/p.json.gz').write_bytes(gzip.compress(json.dumps({'tables': [{'rows': rows}], 'links': links}).encode()))
            (d / 'manifest.jsonl').write_text(json.dumps({'url': lo, 'page_file': 'p.json.gz', 'sha256': 'a' * 64, 'fetched_at': '2026-10-21T00:00:00+00:00'}) + '\n')
            (d / 'candidates.jsonl').write_text(''); (d / 'dec.json').write_text(json.dumps({'approve': []}))
            spec = {'url': lo, 'program': 0, 'level': 3, 'degree': 5, 'level_value': 'Undergraduate'}
            e = table_entries(d, d / 'dec.json', 'k', spec, records=records)
        b = e['completeness_basis']
        # Business Administration BS, Computer Science BS, Dance BA, Dance BFA, Nutrition Science BS, Human Development BS,
        # Human Development Studies BS (its page is HD's, and one record verifies one program)
        self.assertEqual((e['listed_bachelor_programs'], e['verified_listed_programs']), (7, 3), b)
        self.assertTrue(b.endswith("Not recorded (names separated by ' | '): Computer Science, B.S. | Dance, B.F.A. | Human Development Studies, B.S. | Nutrition Science, B.S."), b)

    def test_one_degree_printed_two_ways_and_double_majors(self):  # UT Dallas 2026 program list
        import tempfile
        from programs.catalog_counts import entries, whole_degree
        u = 'https://catalog.x.edu/'
        listing = [('Bachelor of Science in Human Resource Management (120 semester credit hours)', u + 'bad/hrm', 'bachelor'),
                   ('Human Resource Management (BS)', u + 'jsom/human-resource-management', 'bachelor'),
                   ('Bachelor of Arts in Literature (120 semester credit hours)1', u + 'ah/literature', 'bachelor'),
                   ('BA in Literature - Pre-Law Concentration', u + 'ah/literature-pre-law', 'bachelor'),
                   ('BA in Education - 7-12 Social Studies with a concentration in History', u + 'ed/ss-history', 'bachelor'),
                   ('Bachelor of Arts in Education (120 semester credit hours)', u + 'ed/education', 'bachelor'),
                   ('BS in Economics and Finance (Double Major) (129 semester credit hours)', u + 'jsom/econ-fin', 'bachelor'),
                   ('Education (BA) with EC-6 Core Subjects', u + 'ed/ec6', 'bachelor'),
                   ('BA in Mathematics', u + 'ns/math', 'bachelor'), ('BA in Mathematics - Actuarial Concentration', u + 'ns/math-act', 'bachelor')]
        records = [('Human Resource Management (BS)', u + 'jsom/human-resource-management'), ('Literature (BA)', u + 'ah/literature'),
                   ('Education (BA) with EC-6 Core Subjects', u + 'ed/ec6')]
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, listing, records)
            e = entries(d, d / 'dec.json', ['k'])[0]
        b = e['completeness_basis']
        # HRM (two forms, one program), Literature (its concentration is an option), Education BA (its concentration is an
        # option; the EC-6 record names another program and does not verify it), Education (BA) with EC-6; the double major
        # is not counted
        self.assertEqual((e['listed_bachelor_programs'], e['verified_listed_programs']), (5, 3), b)
        self.assertIn("4 print the degree's credit hours after the name", b)
        self.assertIn("not a single bachelor's program: BS in Economics and Finance (Double Major)", b)
        self.assertTrue(b.endswith("Not recorded (names separated by ' | '): BA in Mathematics | Bachelor of Arts in Education."), b)
        self.assertEqual(whole_degree('Bachelor of Science in Human Resource Management'), whole_degree('Human Resource Management (BS)'))
        self.assertIsNone(whole_degree('Education (BA) with EC-6 Core Subjects'))

    def test_tracks_combined_tracks_and_delivery_variants(self):  # YSU 2026-27 program list
        import tempfile
        from programs.catalog_counts import entries, track_of_listed
        u = 'https://catalog.x.edu/'
        listing = [('Bachelor of Arts in Multimedia Communication', u + 'mmc', 'bachelor'),
                   ('Bachelor of Arts in Multimedia Communication, Public Relations Track', u + 'mmc-pr', 'bachelor'),
                   ("Bachelor of Arts in Multimedia Communication, Bachelor's to Master's Track", u + 'mmc-ma', 'bachelor'),
                   ('Bachelor of Science in Computer Science', u + 'cs', 'bachelor'),
                   ('Bachelor of Science in Computer Science Cybersecurity Track', u + 'cs-cyber', 'bachelor'),
                   ('Bachelor of Science in Respiratory Care', u + 'rc', 'bachelor'),
                   ('Bachelor of Science in Respiratory Care with Advanced Placement Option to Master of Respiratory Care', u + 'rc-m', 'bachelor'),
                   ('Bachelor of Science in Applied Science in Exercise Science', u + 'ex', 'bachelor'),
                   ('Bachelor of Science in Applied Science Exercise Science - MAT Track', u + 'ex/mat-track', 'bachelor'),
                   ('Bachelor of Arts in Biochemistry', u + 'biochem', 'bachelor'),
                   ('Bachelor of Science in Biochemistry - Research Track', u + 'biochem/research-track', 'bachelor'),  # another award: counted
                   ('Bachelor of Science in Geographic Information Science', u + 'gis', 'bachelor'),
                   ('Bachelor of Science in Geographic Information Science (online)', u + 'gis-online', 'bachelor'),
                   ('Bachelor of Fine Arts in Graphic Design (Online)', u + 'gd-online', 'bachelor'),
                   ('Bachelor of Science in Chemistry Track', u + 'chem-track', 'bachelor')]  # no 'Chemistry' degree listed: counted
        records = [('Bachelor of Arts in Multimedia Communication', u + 'mmc'), ('Bachelor of Science in Computer Science', u + 'cs'),
                   ('Bachelor of Science in Respiratory Care', u + 'rc'), ('Bachelor of Science in Applied Science in Exercise Science', u + 'ex'),
                   ('Bachelor of Science in Geographic Information Science', u + 'gis'), ('Bachelor of Fine Arts in Graphic Design', u + 'gd-online'),
                   ('Bachelor of Arts in Biochemistry', u + 'biochem')]
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, listing, records)
            e = entries(d, d / 'dec.json', ['k'])[0]
        b = e['completeness_basis']
        # the online degree has its own entry and page: a program of its own (not merged into the campus degree)
        self.assertEqual((e['listed_bachelor_programs'], e['verified_listed_programs']), (10, 7), b)
        self.assertTrue(b.endswith("Not recorded (names separated by ' | '): Bachelor of Science in Biochemistry - Research Track | "
                                   "Bachelor of Science in Chemistry Track | Bachelor of Science in Geographic Information Science (online)."), b)
        degrees = {('multimediacommunication', 'ba')}
        self.assertTrue(track_of_listed('Bachelor of Arts in Multimedia Communication Sports Track', degrees))
        self.assertFalse(track_of_listed('Bachelor of Science in Multimedia Communication Sports Track', degrees))  # another award
        self.assertFalse(track_of_listed('Bachelor of Arts in Multimedia Communication', degrees))  # the degree itself

    def test_jhu_combined_policy_and_double_degree_entries(self):  # JHU 2026-27 program list
        import tempfile
        from programs.catalog_counts import entries, whole_degree
        u = 'https://catalog.x.edu/'
        listing = [('Biology, Bachelor of Arts/Master of Science', u + 'bio-ba-ms', 'bachelor'),
                   ("Bachelor's/Master's Degrees", u + 'ba-ma', 'bachelor'),
                   ("Requirements for a Bachelor's Degree", u + 'reqs', 'bachelor'),
                   ("Peabody-Homewood Double Degree ProgramPeabody InstituteBachelor's", u + 'double', 'bachelor'),
                   ('Bachelor of Fine Arts in Dance (BFA)', u + 'dance', 'bachelor'),
                   ('Bachelor of Music in Performance - Piano', u + 'piano', 'bachelor'),
                   ('Biology, Bachelor of Arts', u + 'bio', 'bachelor'),
                   ('Physics, Bachelor of Science', u + 'phys', 'bachelor')]
        records = [('Bachelor of Fine Arts in Dance', u + 'dance-other-page'), ('Bachelor of Music in Performance - Piano', u + 'piano'),
                   ('Biology, Bachelor of Arts', u + 'bio')]
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, listing, records)
            e = entries(d, d / 'dec.json', ['k'])[0]
        b = e['completeness_basis']
        # combined (2), policy page, double degree: not programs; Dance credited by its whole-degree identity
        self.assertEqual((e['listed_bachelor_programs'], e['verified_listed_programs']), (4, 3), b)
        self.assertIn("Biology, Bachelor of Arts/Master of Science", b)
        self.assertTrue(b.endswith("Not recorded (names separated by ' | '): Physics, Bachelor of Science."), b)
        self.assertEqual(whole_degree('Bachelor of Fine Arts in Dance (BFA)'), whole_degree('Bachelor of Fine Arts in Dance'))
        self.assertIsNone(whole_degree('Bachelor of Science in Dance (BA)'))  # two awards: not one degree

    def test_only_reviewed_approvals_count(self):
        import tempfile
        from programs.catalog_counts import entries
        u = 'https://catalog.x.edu/'
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, [('Art, BA', u + 'art-ba/', 'bachelor'), ('Music, BM', u + 'music-bm/', 'bachelor')],
                             [('Art, BA', u + 'art-ba/'), ('Music, BM', u + 'music-bm/')], approved={0})
            e = entries(d, d / 'dec.json', ['k'])[0]
        self.assertEqual((e['listed_bachelor_programs'], e['verified_listed_programs']), (2, 1))
        self.assertNotIn('listed_program_keys', e)
        # a record whose year is not printed in its source (Coursedog API, FAU) never verifies a listed program
        with tempfile.TemporaryDirectory() as d:
            d = self.run_dir(d, [('Art, BA', u + 'art-ba/', 'bachelor')], [('Art, BA', u + 'art-ba/')])
            lines = [json.loads(l) for l in (d / 'candidates.jsonl').read_text().splitlines()]
            lines[0]['year_basis'] = 'source_unlabeled'
            (d / 'candidates.jsonl').write_text(''.join(json.dumps(l) + '\n' for l in lines))
            self.assertEqual(entries(d, d / 'dec.json', ['k'])[0]['verified_listed_programs'], 0)


class ResearchPriorityTests(unittest.TestCase):
    def test_every_uncovered_institution_is_ranked_once(self):
        import sys
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
        import research_priority as RP
        doc = RP.rank()
        st = json.loads((Path(__file__).resolve().parents[1] / 'docs/coverage/programs/STATUS.json').read_text())
        uncovered = {i['institution_key'] for s in st['states'] for i in s['institutions'] if i['status'] != 'covered'}
        keys = [r['institution_key'] for r in doc['institutions']]
        self.assertEqual(len(keys), len(set(keys))); self.assertEqual(set(keys), uncovered)
        tiers = [RP.TIERS.index(r['tier']) for r in doc['institutions']]
        self.assertEqual(tiers, sorted(tiers))  # tiers in order, largest first within a tier
        self.assertEqual(sum(doc['tiers'].values()), len(keys))


class DiagnoseRobotsTests(unittest.TestCase):
    def test_disallowed_url_is_recorded_not_requested(self):  # VCU bulletin azindex is disallowed by robots.txt (2026-10-08)
        from programs.diagnose import diagnose
        class R:
            def allowed(self, u): return 'azindex' not in u
            def refusal(self, u): return 'disallowed_by_robots'
        asked = []
        class Resp:
            status = 200; headers = {}
            def read(self, n): return b'ok'
            def __enter__(self): return self
            def __exit__(self, *a): return False
        def opener(req, timeout=30): asked.append(req.full_url); return Resp()
        out = diagnose(['https://b.x.edu/azindex/', 'https://b.x.edu/undergraduate/'], R(), opener)
        self.assertEqual(asked, ['https://b.x.edu/undergraduate/'])
        self.assertIn('https://b.x.edu/azindex/ None\ndisallowed_by_robots', out)

