#!/usr/bin/env python3
"""First-time degree/certificate-seeking undergraduates, fall 2023, from the pinned IPEDS EF2023A file
(EFALEVEL 4, EFTOTLT) -> sources/ipeds/2023-24/derived/ef2023a_first_time.csv (unitid, first_time, instcat), with the
HD2023 institutional category so the fallback can be limited to primarily baccalaureate institutions (INSTCAT 2).

The deep-dive coverage share weights each school by its IPEDS ADM2023 'enrolled' count; open-admission schools report
no ADM survey (UVU), so programs/status.py falls back to this count. `--check` fails when the derived file is stale.
"""
import csv, io, json, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / 'sources/ipeds/2023-24'
OUT = D / 'derived/ef2023a_first_time.csv'


def rows():
    m = json.loads((D / 'manifest.json').read_text())
    e = next(f for f in m['files'] if f['filename'] == 'EF2023A.zip')
    raw = b''.join((D / p).read_bytes() for p in e['parts'])
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        name = next(n for n in z.namelist() if n.lower().endswith('.csv') and '_rv' not in n.lower())
        return list(csv.DictReader(io.StringIO(z.read(name).decode('utf-8-sig', 'replace'))))


def build():
    sys.path.insert(0, str(ROOT))
    from pipeline.registry import hd_rows
    cat = {r['UNITID']: r.get('INSTCAT', '') for r in hd_rows()}
    out = io.StringIO(); w = csv.writer(out, lineterminator='\n'); w.writerow(['unitid', 'first_time', 'instcat'])
    for r in sorted((r for r in rows() if r['EFALEVEL'].strip() == '4'), key=lambda r: int(r['UNITID'])):
        w.writerow([r['UNITID'], int(r['EFTOTLT'] or 0), cat.get(r['UNITID'], '')])
    return out.getvalue()


if __name__ == '__main__':
    text = build()
    if '--check' in sys.argv:
        ok = OUT.exists() and OUT.read_text() == text
        print('EF2023A first-time counts current' if ok else f'{OUT} is stale: run python scripts/ipeds_first_time.py'); sys.exit(0 if ok else 1)
    OUT.parent.mkdir(exist_ok=True); OUT.write_text(text); print(f'{OUT.relative_to(ROOT)}: {text.count(chr(10)) - 1} institutions')
