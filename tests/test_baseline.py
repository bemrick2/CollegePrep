"""National baseline (scripts/build_baseline.py): statuses, no zero for missing, imputed values withheld, the complete rule."""
import csv, glob, json, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_baseline as b  # noqa: E402

ROWS = [r for p in sorted(glob.glob(str(ROOT / 'baseline/schools/2023-24/*.csv'))) for r in csv.DictReader(Path(p).read_text(encoding='utf-8').splitlines())]


class Evaluate(unittest.TestCase):
    """Rules on synthetic IPEDS rows, independent of the pinned files."""

    def tables(self, **over):
        t = {k: {} for k in ['HD2023', 'DRVEF2023', 'DRVADM2023', 'ADM2023', 'IC2023', 'IC2023_AY', 'DRVIC2023', 'SFA2223',
                             'EF2023D', 'DRVGR2023', 'EF2023A_UG', 'HD2024', 'FLAGS']}
        t['GR_FLAGS'] = {}; t['C'] = {}
        t['HD2023']['1'] = {'INSTNM': 'X U', 'CITY': 'C', 'STABBR': 'TN', 'WEBADDR': 'x.edu', 'CONTROL': '1', 'ICLEVEL': '1', 'HLOFFER': '9'}
        t['HD2024']['1'] = {'INSTNM': 'X U', 'CYACTIVE': '1'}
        for k, v in over.items(): t[k]['1'] = v
        return t

    L = {'codes': {}, 'variables': {}}

    def test_missing_is_never_zero_and_imputed_is_withheld(self):
        t = self.tables(ADM2023={'APPLCN': '100', 'XAPPLCN': 'R', 'ADMSSN': '50', 'XADMSSN': 'P'}, DRVADM2023={'DVADM01': '50'},
                        IC2023={'OPENADMP': '2'}, EF2023D={'RET_PCF': '', 'XRET_PCF': 'A'})
        v, st, why = b.evaluate('1', t, self.L)
        self.assertNotIn('admission_rate_percent', v)
        self.assertEqual(st['admission_rate'], 'not_researched')
        self.assertIn('NCES flags R/P', why['admission_rate'])
        self.assertEqual(st['retention_rate'], 'not_published_or_na')
        self.assertIsNone(v.get('retention_rate_full_time'))
        self.assertEqual(st['net_price'], 'not_researched')  # no record: not zero, not N/A

    def test_open_admission_is_not_applicable(self):
        v, st, _ = b.evaluate('1', self.tables(IC2023={'OPENADMP': '1'}), self.L)
        self.assertEqual((st['admission_rate'], st['test_scores']), ('not_published_or_na', 'not_published_or_na'))
        self.assertIs(v['open_admission'], True)

    def test_test_blind_scores_not_applicable_but_test_optional_unreported_is_not_researched(self):
        _, st, _ = b.evaluate('1', self.tables(ADM2023={'ADMCON7': '3'}, IC2023={'OPENADMP': '2'}), self.L)
        self.assertEqual(st['test_scores'], 'not_published_or_na')
        _, st, _ = b.evaluate('1', self.tables(ADM2023={'ADMCON7': '5'}, IC2023={'OPENADMP': '2'}), self.L)
        self.assertEqual(st['test_scores'], 'not_researched')

    def test_prices_are_older_than_the_planning_year(self):
        ay = {'CHG2AT3': '9000', 'XCHG2AT3': 'R', 'CHG2AF3': '1000', 'XCHG2AF3': 'R', 'CHG4AY3': '1200', 'XCHG4AY3': 'R',
              'CHG5AY3': '11000', 'XCHG5AY3': 'R', 'CHG6AY3': '3000', 'XCHG6AY3': 'R'}
        v, st, _ = b.evaluate('1', self.tables(IC2023_AY=ay, DRVIC2023={'CINSON': '25200'}), self.L)
        self.assertEqual((st['tuition_fees'], st['cost_of_attendance']), ('available_older', 'available_older'))
        self.assertEqual(v['coa_in_state_on_campus'], 25200)
        # One imputed component withholds the NCES total.
        v, st, _ = b.evaluate('1', self.tables(IC2023_AY={**ay, 'XCHG4AY3': 'P'}, DRVIC2023={'CINSON': '25200'}), self.L)
        self.assertIsNone(v.get('coa_in_state_on_campus')); self.assertEqual(st['cost_of_attendance'], 'not_researched')

    def test_imputed_graduation_cohort_withholds_rates(self):
        t = self.tables(DRVGR2023={'BAGR150': '60'}); t['GR_FLAGS']['1'] = {'R', 'P'}
        v, st, _ = b.evaluate('1', t, self.L)
        self.assertNotIn('bachelors_grad_rate_6yr', v); self.assertEqual(st['graduation_rate'], 'not_researched')

    def test_child_campus_is_named_with_its_parent(self):
        t = self.tables(FLAGS={'PRCH_SFA': '2', 'IDX_SFA': '999'})
        _, st, why = b.evaluate('1', t, self.L)
        self.assertEqual(st['net_price'], 'not_published_or_na'); self.assertIn('999', why['net_price'])

    def test_closed_school_is_flagged(self):
        v, st, _ = b.evaluate('1', self.tables(HD2024={'INSTNM': 'X U', 'CYACTIVE': '3', 'CLOSEDAT': '05/01/2024'}), self.L)
        self.assertEqual(v['closed_per_hd2024'], '05/01/2024'); self.assertEqual(st['identity'], 'available_older')


class Committed(unittest.TestCase):
    """The committed baseline files."""

    def test_one_row_per_in_scope_school(self):
        self.assertEqual(len(ROWS), len(b.registry()))
        self.assertEqual(len({r['institution_key'] for r in ROWS}), len(ROWS))

    def test_statuses_are_known_and_values_only_where_resolved(self):
        for r in ROWS:
            for f in b.FIELDS:
                s = r[f['key'] + '__status']
                self.assertIn(s, b.STATUSES)
                if s in ('not_researched', 'not_published_or_na') and f['key'] not in ('identity', 'admission_rate', 'test_scores'):
                    self.assertTrue(all(r[c] == '' for c in f['columns'] if c not in ('net_price_basis',)), (r['institution_key'], f['key']))

    def test_complete_rule(self):
        for r in ROWS:
            ok = all(r[f['key'] + '__status'] in ('verified_current', 'available_older', 'not_published_or_na') for f in b.FIELDS)
            self.assertEqual(r['baseline_complete'], str(ok))

    def test_sat_sections_never_summed(self):
        self.assertFalse(any('sat_composite' in c for f in b.FIELDS for c in f['columns']))

    def test_matches_the_existing_ipeds_import_where_both_exist(self):
        """Same pinned file, two readers: the baseline and data/national/ipeds must agree on admissions and tuition."""
        adm = {r['unitid']: r for p in glob.glob(str(ROOT / 'data/national/ipeds/2023-24/*/admissions.csv'))
               for r in csv.DictReader(Path(p).read_text(encoding='utf-8').splitlines())}
        cost = {(r['unitid'], r['residency']): r for p in glob.glob(str(ROOT / 'data/national/ipeds/2023-24/*/costs.csv'))
                for r in csv.DictReader(Path(p).read_text(encoding='utf-8').splitlines())}
        n = 0
        for r in ROWS:
            a = adm.get(r['unitid'])
            if a and r['test_scores__status'] in ('verified_current', 'available_older'):
                self.assertEqual((r['act_composite_25'], r['sat_math_75']), (a['act_25'], a['sat_math_75']), r['institution_key']); n += 1
            c = cost.get((r['unitid'], 'in_state'))
            if c and r['tuition_fees__status'] == 'available_older':
                self.assertEqual(r['in_state_tuition'], c['tuition'] or '', r['institution_key']); n += 1
        self.assertGreater(n, 1000)


if __name__ == '__main__':
    unittest.main()
