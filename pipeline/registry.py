"""Source registry: which institutions are in scope for a state and where their official sites start.

Seeds come from the pinned IPEDS HD survey file (official website, admissions, financial-aid and
net-price URLs that each institution reports to NCES). Institution keys and data folders follow
docs/PROGRAM_DATA.md: an existing curated folder keeps its key; everyone else is `ipeds-<unitid>`.
The registry is deterministic for a given HD file and repository state, so it is committed and
reviewed like data.
"""
from __future__ import annotations
import csv, io, json, re, zipfile
from pathlib import Path
from urllib.parse import urlsplit

from backend.catalog import ROOT, records

HD_DIR = ROOT / 'sources/ipeds/2023-24'
REGISTRY_DIR = ROOT / 'pipeline/registry'
SEED_FIELDS = {'WEBADDR': 'website', 'ADMINURL': 'admissions', 'FAIDURL': 'financial_aid', 'NPRICURL': 'net_price'}


def hd_rows():
    manifest = json.loads((HD_DIR / 'manifest.json').read_text())
    entry = next(f for f in manifest['files'] if f['filename'] == 'HD2023.zip')
    raw = b''.join((HD_DIR / p).read_bytes() for p in entry['parts'])
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        name = next(n for n in z.namelist() if n.lower().endswith('.csv'))
        return list(csv.DictReader(io.StringIO(z.read(name).decode('utf-8-sig', 'replace'))))


def normalize_url(u: str) -> str | None:
    u = (u or '').strip().split()[0] if (u or '').strip() else ''
    if not u: return None
    if not re.match(r'^https?://', u, re.I): u = 'https://' + u
    u = re.sub(r'^http://', 'https://', u, flags=re.I)
    parts = urlsplit(u)
    if not parts.netloc or '.' not in parts.netloc: return None
    return u


def registrable_domain(host: str) -> str:
    """'www.catalog.utc.edu' -> 'utc.edu'. Good enough for .edu/.org/.com/.gov hosts in IPEDS."""
    labels = host.lower().split(':')[0].strip('.').split('.')
    if len(labels) >= 3 and labels[-2] in {'tn', 'k12', 'co', 'ac'} and len(labels[-1]) == 2:
        return '.'.join(labels[-3:])
    return '.'.join(labels[-2:])


def curated_folders():
    """institution_key -> existing data/institutions/<folder> name."""
    out = {}
    for path, domain, r in records():
        parts = path.relative_to(ROOT).parts
        if parts[:2] == ('data', 'institutions') and r.get('institution_key'):
            out.setdefault(r['institution_key'], parts[2])
    return out


def existing_ipeds_presence(state: str):
    """UNITIDs with a first-time-undergraduate admissions or price record in the national snapshot."""
    have = set()
    for f in ('admissions.csv', 'costs.csv'):
        p = ROOT / 'data/national/ipeds/2023-24' / state / f
        if p.exists():
            with p.open(encoding='utf-8', newline='') as fh:
                have |= {r['unitid'] for r in csv.DictReader(fh)}
    return have


def in_scope(r, presence) -> bool:
    return (r['CYACTIVE'] == '1' and r['DEGGRANT'] == '1' and r['UGOFFER'] == '1'
            and r['CONTROL'] in {'1', '2'} and r['ICLEVEL'] in {'1', '2'} and r['UNITID'] in presence)


def cited_sources():
    """institution_key -> official URLs already cited by curated records (re-verified on every run)."""
    out = {}
    for path, domain, r in records():
        if path.suffix == '.json' and r.get('institution_key'):
            for k in ('source_url', 'policy_url', 'program_url'):
                if str(r.get(k) or '').startswith('https://'): out.setdefault(r['institution_key'], set()).add(r[k])
    return {k: sorted(v) for k, v in out.items()}


def build(state: str):
    state = state.upper()
    presence = existing_ipeds_presence(state)
    folders = curated_folders()
    cited = cited_sources()
    aliases = {}
    for p in (ROOT / 'data/institutions').glob('*/institution.json'):
        r = json.loads(p.read_text()); aliases[str(r.get('unitid'))] = r['institution_key']
    rows = [r for r in hd_rows() if r['STABBR'] == state and in_scope(r, presence)]
    slugs = {}
    institutions = []
    for r in sorted(rows, key=lambda r: r['INSTNM']):
        key = aliases.get(r['UNITID'], 'ipeds-' + r['UNITID'])
        seeds = {}
        for field, label in SEED_FIELDS.items():
            u = normalize_url(r.get(field))
            if u: seeds[label] = u
        site = seeds.get('website')
        domain = registrable_domain(urlsplit(site).netloc) if site else None
        folder = folders.get(key) or (domain.split('.')[0] if domain else 'ipeds-' + r['UNITID'])
        slugs.setdefault(folder, []).append(key)
        institutions.append({
            'institution_key': key, 'unitid': int(r['UNITID']), 'name': r['INSTNM'], 'city': r['CITY'],
            'folder': folder, 'control': {'1': 'public', '2': 'private_nonprofit'}[r['CONTROL']],
            'level': {'1': 'four_year', '2': 'two_year'}[r['ICLEVEL']], 'domain': domain,
            # Net-price calculators are often hosted by vendors, so they never widen the crawl.
            'allowed_domains': sorted({registrable_domain(urlsplit(u).netloc) for l, u in seeds.items() if l != 'net_price'}
                                      | {registrable_domain(urlsplit(u).netloc) for u in cited.get(key, [])}),
            'seeds': seeds, 'existing_sources': cited.get(key, [])})
    for inst in institutions:  # Two campuses sharing a domain get distinct folders.
        if len(slugs[inst['folder']]) > 1 and inst['folder'] not in folders.values():
            inst['folder'] = f"{inst['folder']}-{inst['unitid']}"
    return {'state': state, 'source': 'IPEDS HD2023 (sources/ipeds/2023-24/manifest.json)',
            'scope_rule': 'active, degree-granting, undergraduate, public or private nonprofit, 2- or 4-year, '
                          'with a 2023-24 IPEDS first-time undergraduate admissions or price record',
            'institutions': institutions, 'state_sources': state_sources(state)}


def state_sources(state: str):
    """Hand-maintained statewide official seeds (aid agencies, articulation, residency rules)."""
    p = REGISTRY_DIR / 'states' / f'{state}.json'
    return json.loads(p.read_text())['sources'] if p.exists() else []


def write(state: str) -> Path:
    out = REGISTRY_DIR / f'{state.upper()}.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(build(state), indent=1, ensure_ascii=False) + '\n')
    return out


def load(state: str):
    return json.loads((REGISTRY_DIR / f'{state.upper()}.json').read_text())
