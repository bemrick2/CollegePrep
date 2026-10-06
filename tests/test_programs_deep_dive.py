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
        bare = {**tgt, '_listed': {url: {**listed, 'printed': 'Cinema Studies'}}}
        self.assertEqual(X.program_page_candidates(bare, {'institution_key': 'k'}, e, page, '2026-27'), [])
        minor = {**tgt, '_listed': {url: {**listed, 'credential_level': None}}}
        self.assertEqual(X.program_page_candidates(minor, {'institution_key': 'k'}, e, page, '2026-27'), [])

    def test_archive_pdf_link_is_not_a_year_label(self):
        from pipeline import text as T
        p = T.Page('Catalog 2026-2027\nPDF of the entire 2025-2026 Catalog\nDownload PDF of the entire 2024-2025 Bulletin', 't', [], [], [])
        self.assertEqual({y for y, _ in X.printed_catalog_years(p)}, {'2026-2027'})


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
                         [('all_required', ['complex_course_row']), ('choose_courses', ['complex_course_row', 'options_not_read', 'options_print_credits']),
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
