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
        # headings alike for their first 80 characters (LMU 2026-27 math-placement plans) still give distinct keys and ids
        h = 'Model 4-Year Plan\u2013Bachelor of Business Administration\u2013Finance Major Curriculum\u2013Math placement MATH '
        alike = [self.grid(h + '101'), self.grid(h + '110')]
        out = [c for c in CL.extract({'institution_key': 'k'}, e, T.Page('Finance BBA', 'Finance BBA', alike, [], []), '2026-2027', '', True)
               if c['domain'] == 'degree_requirements']
        self.assertEqual(len({c['record']['requirement_key'] for c in out}), 2)
        self.assertEqual(len({c['candidate_id'] for c in out}), 2)

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
        self.assertEqual(items[3], long.strip() + ' | 4')  # never cut


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
        self.assertEqual({a['candidate_id'] for a in approve}, {'ok', 'g1', 'p1', 'ba', 'bs', 'fin'})
        self.assertEqual(held['issues'], 1); self.assertEqual(held['option_name'], 1); self.assertEqual(held['combined_program'], 1)
        self.assertEqual(held['entry_path_variant'], 3)
        self.assertEqual(held['not_verbatim'], 1); self.assertEqual(held['duplicate'], 1); self.assertEqual(held['req_program_not_approved'], 1)

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
            finally:
                P.ROOT, PP.ROOT = old, oldp


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
