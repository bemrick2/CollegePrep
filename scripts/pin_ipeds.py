#!/usr/bin/env python3
"""Pin IPEDS survey files into sources/ipeds/<year>/ (131,072-byte parts + manifest.json entry with sha256).

  python scripts/pin_ipeds.py 2023-24 EF2023A.zip [EF2023A_Dict.zip ...]   (files already downloaded to the cwd)
Run by .github/workflows/ipeds-source.yml, where nces.ed.gov is reachable; never overwrites a pinned file with other bytes.
"""
import hashlib, json, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART = 131072


def main(year, names):
    d = ROOT / 'sources/ipeds' / year
    m = json.loads((d / 'manifest.json').read_text())
    for name in names:
        raw = Path(name).read_bytes(); sha = hashlib.sha256(raw).hexdigest()
        old = next((f for f in m['files'] if f['filename'] == name), None)
        if old and old['sha256'] != sha: raise SystemExit(f'{name}: pinned {old["sha256"]} differs from download {sha}')
        if old: print(f'{name}: already pinned'); continue
        parts = []
        for i in range(0, len(raw), PART):
            p = f'{name}.part{i // PART:03d}'; (d / p).write_bytes(raw[i:i + PART]); parts.append(p)
        m['files'].append({'filename': name, 'source_url': f'https://nces.ed.gov/ipeds/datacenter/data/{name}', 'sha256': sha,
                           'bytes': len(raw), 'retrieved_at': date.today().isoformat(), 'parts': parts})
        print(f'{name}: {len(raw)} bytes, sha256 {sha}, {len(parts)} parts')
    (d / 'manifest.json').write_text(json.dumps(m, indent=2) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
