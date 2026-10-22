#!/usr/bin/env python3
"""Pin IPEDS survey files into sources/ipeds/<year>/ (131,072-byte parts + manifest.json entry with sha256).

  python scripts/pin_ipeds.py 2023-24 EF2023A.zip [EF2023A_Dict.zip ...]   (files already downloaded to the cwd)
  python scripts/pin_ipeds.py --unavailable 2024-25 FILE STATUS [URL]     (records a file NCES did not serve)
  python scripts/pin_ipeds.py --url https://nces.ed.gov/ipeds/cipcode/Files/CIPCode2020.csv reference CIPCode2020.csv
Run by .github/workflows/ipeds-source.yml, where nces.ed.gov is reachable; never overwrites a pinned file with other bytes.
A collection year's directory and manifest are created on first use. A file NCES did not serve is listed under
`unavailable` with the HTTP status and date, so "not released yet" is recorded rather than guessed.
"""
import hashlib, json, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART = 131072


def load(year):
    d = ROOT / 'sources/ipeds' / year
    d.mkdir(parents=True, exist_ok=True)
    mf = d / 'manifest.json'
    return d, (json.loads(mf.read_text()) if mf.exists() else {'academic_year': year, 'files': []})


def unavailable(year, name, status, url=None):
    d, m = load(year)
    if any(f['filename'] == name for f in m['files']): return
    u = [x for x in m.get('unavailable', []) if x['filename'] != name]
    u.append({'filename': name, 'source_url': url or f'https://nces.ed.gov/ipeds/datacenter/data/{name}', 'http_status': status,
              'checked_at': date.today().isoformat()})
    m['unavailable'] = sorted(u, key=lambda x: x['filename'])
    (d / 'manifest.json').write_text(json.dumps(m, indent=2) + '\n')
    print(f'{name}: not served (HTTP {status}), recorded as unavailable')


def main(year, names, url=None):
    d, m = load(year)
    for name in names:
        raw = Path(name).read_bytes(); sha = hashlib.sha256(raw).hexdigest()
        old = next((f for f in m['files'] if f['filename'] == name), None)
        if old and old['sha256'] != sha: raise SystemExit(f'{name}: pinned {old["sha256"]} differs from download {sha}')
        if old: print(f'{name}: already pinned'); continue
        parts = []
        for i in range(0, len(raw), PART):
            p = f'{name}.part{i // PART:03d}'; (d / p).write_bytes(raw[i:i + PART]); parts.append(p)
        m['files'].append({'filename': name, 'source_url': url or f'https://nces.ed.gov/ipeds/datacenter/data/{name}', 'sha256': sha,
                           'bytes': len(raw), 'retrieved_at': date.today().isoformat(), 'parts': parts})
        print(f'{name}: {len(raw)} bytes, sha256 {sha}, {len(parts)} parts')
        m['unavailable'] = [x for x in m.get('unavailable', []) if x['filename'] != name] or None
        if m['unavailable'] is None: m.pop('unavailable')
    (d / 'manifest.json').write_text(json.dumps(m, indent=2) + '\n')


if __name__ == '__main__':
    if sys.argv[1] == '--unavailable': unavailable(sys.argv[2], sys.argv[3], sys.argv[4], *sys.argv[5:6])
    elif sys.argv[1] == '--url': main(sys.argv[3], [sys.argv[4]], sys.argv[2])  # --url URL YEAR FILENAME
    else: main(sys.argv[1], sys.argv[2:])
