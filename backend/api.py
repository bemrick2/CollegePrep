"""Read-only development API. Explicit years; parameterized queries; bounded responses."""
import argparse,json,sqlite3
from contextlib import closing
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from urllib.parse import parse_qs,urlparse
from pathlib import Path
from backend.catalog import ROOT
from backend.store import school

def query(db,path,params):
    def one(k,default=''): return params.get(k,[default])[0]
    if path=='/health': return 200,{'status':'ok','records':db.execute('select count(*) from reference_records').fetchone()[0]}
    if path=='/v1/coverage': return 200,json.loads((ROOT/'docs/coverage/coverage.json').read_text())
    if path=='/v1/institutions':
        limit=int(one('limit','25')); offset=int(one('offset','0'))
        if not 1<=limit<=100 or offset<0: raise ValueError('limit must be 1–100; offset must be nonnegative')
        rows=db.execute("select payload from reference_records where domain='institutions' and (?='' or state_code=?) and (?='' or lower(json_extract(payload,'$.display_name')) like ?) order by institution_key limit ? offset ?",(one('state'),one('state'),one('q'),'%'+one('q').lower()+'%',limit,offset)).fetchall()
        return 200,{'records':[json.loads(r[0]) for r in rows],'limit':limit,'offset':offset}
    if path.startswith('/v1/institutions/'):
        year=one('academic_year')
        if not year: raise ValueError('academic_year is required; there is no silent latest-year fallback')
        key=path[len('/v1/institutions/'):]; result=school(db,key,year)
        return (200,result) if result else (404,{'error':'Unknown institution'})
    return 404,{'error':'Unknown route'}

def server(database,port):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed=urlparse(self.path)
            try:
                # URI read-only mode prevents accidental writes through the HTTP process.
                with closing(sqlite3.connect(Path(database).resolve().as_uri()+'?mode=ro',uri=True)) as db:
                    db.row_factory=sqlite3.Row
                    status,payload=query(db,parsed.path,parse_qs(parsed.query))
            except ValueError as e: status,payload=400,{'error':str(e)}
            except sqlite3.Error: status,payload=503,{'error':'Reference database unavailable'}
            body=json.dumps(payload,ensure_ascii=False).encode()
            self.send_response(status); self.send_header('Content-Type','application/json; charset=utf-8'); self.send_header('Content-Length',str(len(body))); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(body)
    return ThreadingHTTPServer(('127.0.0.1',port),Handler)

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--database',required=True); p.add_argument('--port',type=int,default=8080); a=p.parse_args()
    server(a.database,a.port).serve_forever()
