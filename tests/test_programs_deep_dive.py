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

    def test_graduate_names_never_classified(self):
        self.assertIsNone(X.credential_of('Graduate Certificate, Associate Teacher Licensure'))
        self.assertIsNone(X.credential_of('Master of Science, Computer Science'))
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
