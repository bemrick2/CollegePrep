import json,tempfile,threading,unittest,urllib.request,urllib.error
from pathlib import Path
from contextlib import closing
from backend.api import server
from backend.store import connect,load
class HTTPTests(unittest.TestCase):
    def test_live_readonly_http(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'data').mkdir()
            r={'institution_key':'test','display_name':'Test','domain':'institutions','state_code':'TN','verification_status':'verified','source_url':'https://example.edu','last_verified_at':'2026-10-01'}
            (root/'data/institution.json').write_text(json.dumps(r)); path=root/'reference.sqlite'
            with closing(connect(path)) as db: load(db,root)
            http=server(path,0); thread=threading.Thread(target=http.serve_forever,daemon=True); thread.start()
            base=f'http://127.0.0.1:{http.server_port}'
            try:
                with urllib.request.urlopen(base+'/health') as res: self.assertEqual(json.load(res)['records'],1)
                with urllib.request.urlopen(base+'/v1/institutions/test?academic_year=2026-27') as res: self.assertFalse(json.load(res)['can_offer_paid_addon'])
                with self.assertRaises(urllib.error.HTTPError) as error: urllib.request.urlopen(base+'/v1/institutions/test')
                self.assertEqual(error.exception.code,400)
                req=urllib.request.Request(base+'/v1/institutions',data=b'{}',method='POST')
                with self.assertRaises(urllib.error.HTTPError) as error: urllib.request.urlopen(req)
                self.assertEqual(error.exception.code,501)
            finally: http.shutdown(); http.server_close(); thread.join()
if __name__=='__main__': unittest.main()
