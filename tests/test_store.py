import json,tempfile,unittest
from pathlib import Path
from backend.store import connect,load,school
from backend.api import query
class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name); (self.root/'data').mkdir(); self.db=connect(':memory:')
        self.identity={'institution_key':'test','display_name':'Test University','state_code':'TN','domain':'institutions','source_url':'https://example.edu','verification_status':'verified','last_verified_at':'2026-10-01'}
        self.price={**self.identity,'domain':'costs','academic_year':'2025-26','residency':'in_state','tuition':1000}
        self.write([self.identity,self.price])
    def tearDown(self): self.db.close(); self.tmp.cleanup()
    def write(self,rs): (self.root/'data/fixture.json').write_text(json.dumps(rs))
    def test_idempotence_and_year_isolation(self):
        self.assertEqual(load(self.db,self.root)['inserted'],2)
        self.assertEqual(load(self.db,self.root)['unchanged'],2)
        self.assertEqual(school(self.db,'test','2026-27')['domains'],{})
        self.assertEqual(school(self.db,'test','2025-26')['domains']['costs'][0]['tuition'],1000)
    def test_revision_history_and_atomic_downgrade_rejection(self):
        load(self.db,self.root); self.price['tuition']=2000; self.write([self.identity,self.price])
        with self.assertRaises(ValueError): load(self.db,self.root)
        self.assertEqual(school(self.db,'test','2025-26')['domains']['costs'][0]['tuition'],1000)
        load(self.db,self.root,accept_revisions=True)
        self.assertEqual(self.db.execute('select count(*) from record_revisions').fetchone()[0],1)
        self.price['verification_status']='unverified'; self.write([self.identity,self.price])
        with self.assertRaises(ValueError): load(self.db,self.root,accept_revisions=True)
    def test_api_input_and_missing_data(self):
        load(self.db,self.root)
        with self.assertRaises(ValueError): query(self.db,'/v1/institutions/test',{})
        with self.assertRaises(ValueError): query(self.db,'/v1/institutions',{'limit':['1000']})
        self.assertEqual(query(self.db,'/v1/institutions/missing',{'academic_year':['2026-27']})[0],404)
        result=query(self.db,'/v1/institutions/test',{'academic_year':['2026-27']})[1]
        self.assertFalse(result['can_offer_paid_addon']); self.assertIn('costs',result['missing_domains'])
    def test_invalid_provenance_rolls_back(self):
        self.price['last_verified_at']='invalid'; self.write([self.identity,self.price])
        with self.assertRaises(ValueError): load(self.db,self.root)
        self.assertEqual(self.db.execute('select count(*) from reference_records').fetchone()[0],0)
    def test_reviewed_correction_requires_opt_in_and_reason(self):
        load(self.db,self.root)
        self.price['verification_status']='partially_verified'
        self.price['verification_correction_reason']='Official source does not establish this academic year'
        self.write([self.identity,self.price])
        with self.assertRaises(ValueError): load(self.db,self.root,accept_revisions=True)
        load(self.db,self.root,accept_revisions=True,accept_corrections=True)
        self.assertEqual(self.db.execute('select count(*) from record_revisions').fetchone()[0],1)
        self.assertEqual(school(self.db,'test','2025-26')['domains']['costs'][0]['verification_status'],'partially_verified')
if __name__=='__main__': unittest.main()
