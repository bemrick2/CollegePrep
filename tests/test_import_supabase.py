import unittest
from scripts.import_supabase import bulk_batch,literal
from backend.store import natural_key
class ImportTests(unittest.TestCase):
    def test_sql_quoting_and_unknown_values(self):
        self.assertEqual(literal("O'Brien"),"'O''Brien'")
        self.assertEqual(literal(None),'null')
        r={'institution_key':'test','display_name':"O'Brien College",'verification_status':'verified','source_url':'https://example.edu','last_verified_at':'2026-10-02'}
        sql=bulk_batch([{'domain':'institutions','natural_key':natural_key('institutions',r),'source_file':'fixture.json','payload':r}])
        self.assertIn("O''Brien",sql)
        self.assertIn('null::boolean',sql)
        self.assertIn('ingestion.reference_revisions',sql)
        self.assertNotIn('security definer',sql.lower())
        self.assertTrue(sql.startswith('begin;'))
        self.assertTrue(sql.endswith('commit;'))

    def test_cost_period_and_printed_totals_are_imported_and_reconciled(self):
        # #296: a per-semester record must not reach institution_costs as if it were a year's price.
        r={'institution_key':'test','academic_year':'2026-27','residency':'in_state','tuition':8379,'total_direct_cost':8662,
           'cost_period':'semester','verification_status':'partially_verified','source_url':'https://example.edu','last_verified_at':'2026-10-06'}
        sql=bulk_batch([{'domain':'costs','natural_key':natural_key('costs',r),'source_file':'fixture.json','payload':r}])
        line=next(l for l in sql.splitlines() if l.startswith('insert into public.institution_costs('))
        cols=line[len('insert into public.institution_costs('):line.index(')')].split(',')
        for c in ('cost_period','tuition_and_mandatory_fees','total_direct_cost'): self.assertIn(c,cols)
        self.assertIn("cost_period=excluded.cost_period",line)
        from scripts.import_supabase import reconcile_sql
        rec=reconcile_sql()
        self.assertIn("cost_period='semester'",rec)
        self.assertIn('cost period or printed totals differ from the record',rec)
        self.assertIn('combined tuition and fees count mismatch',rec)
if __name__=='__main__': unittest.main()
