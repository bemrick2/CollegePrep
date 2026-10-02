import hashlib,json,sys,zipfile,io
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for manifest in (root/'sources').rglob('manifest.json'):
    for r in json.loads(manifest.read_text())['files']:
        b=b''.join((manifest.parent/p).read_bytes() for p in r['parts']) if 'parts' in r else (manifest.parent/r['filename']).read_bytes()
        if len(b)!=r['bytes'] or hashlib.sha256(b).hexdigest()!=r['sha256']: sys.exit('Source hash mismatch: '+r['filename'])
        if zipfile.ZipFile(io.BytesIO(b)).testzip(): sys.exit('Invalid archive: '+r['filename'])
print('Pinned source archives match recorded hashes')
