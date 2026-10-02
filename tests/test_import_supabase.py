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
if __name__=='__main__': unittest.main()
