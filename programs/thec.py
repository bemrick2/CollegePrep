"""Tennessee Higher Education Commission Academic Program Inventory (official state source).

The public search page (https://thec.ppr.tn.gov/AcademicProgramInventorySearch) loads its data from its own JSON
endpoints; this adapter makes the same requests the page makes, politely (robots.txt and per-host delay from
pipeline.crawl.Fetcher), and stores every response in the run like any fetched document:

  GET  /MasterData/GetInstitutionList?ignoreGroupedAllValues=true
  POST /Home/GetProgramList  {"InstitutionId": id, "IsActiveChecked": true, ...}

Each program row carries InstitutionName, MajorName, Award, MajorCipCode (6-digit federal CIP), CreditOrClockHours,
EffectiveStartDate, CurrentProgramStatus. Nothing is derived: rows are stored and later extracted as printed.
"""
from __future__ import annotations
import hashlib, json, urllib.request
from urllib.parse import urlsplit

from pipeline import text as T
from pipeline.crawl import USER_AGENT, HostGate, now

BASE = 'https://thec.ppr.tn.gov/AcademicProgramInventorySearch'
INSTITUTIONS = BASE + '/MasterData/GetInstitutionList?ignoreGroupedAllValues=true'
PROGRAMS = BASE + '/Home/GetProgramList'


def norm_name(n):
    """'The University of Tennessee-Knoxville' and 'University of Tennessee, Knoxville' compare equal."""
    import re
    n = re.sub(r'[^a-z0-9 ]', ' ', n.lower().replace('&', ' and '))
    return ' '.join(w for w in n.split() if w not in {'the', 'at'})


def _request(fetcher, url, payload=None):
    if not fetcher.allowed(url):
        return {'status': None, 'error': 'disallowed_by_robots'}, None
    host = urlsplit(url).netloc.lower()
    entry = fetcher.gate.wait(host)
    try:
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(url, data=data, method='POST' if data else 'GET',
                                     headers={'User-Agent': USER_AGENT, 'Accept': 'application/json',
                                              **({'Content-Type': 'application/json'} if data else {})})
        with fetcher.opener.open(req, timeout=60) as r:
            body = r.read(); status = r.status
    except Exception as exc:
        return {'status': getattr(exc, 'code', None), 'error': f'{type(exc).__name__}: {exc}'[:300]}, None
    finally:
        HostGate.done(entry)
    return {'status': status, 'final_url': url, 'content_type': 'application/json', 'bytes': len(body),
            'sha256': hashlib.sha256(body).hexdigest()}, body


def _store(run, key, url, role, meta, body, request_payload=None, log=print):
    entry = {'institution_key': key, 'url': url, 'role': role, 'via': 'thec_api', 'depth': 0, 'fetched_at': now(), **meta}
    if request_payload is not None: entry['request'] = request_payload
    if body is not None:
        try:
            parsed = json.loads(body)
            if isinstance(parsed, str): parsed = json.loads(parsed)  # GetProgramList returns a JSON-encoded string
        except ValueError:
            entry['error'] = 'unparsed_json'; run.record(entry); return None
        text = json.dumps(parsed, indent=0, ensure_ascii=False)
        page = T.Page(text, 'THEC Academic Program Inventory', [], [], [])
        entry['kind'] = 'json'; entry['title'] = 'THEC Academic Program Inventory'
        entry['page_file'] = run.save_page(meta['sha256'], 'json', page, [])
        run.record(entry); return parsed
    run.record(entry); return None


def crawl(run, fetcher, institution_names, log=print):
    """institution_names: {institution_key: THEC InstitutionName}. Fetches the institution list, then each
    institution's active program inventory. Resumable: requests already in the manifest are skipped."""
    done = {(e['url'], json.dumps(e.get('request'), sort_keys=True)) for e in run.entries() if e.get('via') == 'thec_api' and e.get('page_file')}
    insts = None
    if (INSTITUTIONS, 'null') not in done:
        meta, body = _request(fetcher, INSTITUTIONS)
        insts = _store(run, 'state-TN', INSTITUTIONS, 'state_source', meta, body, log=log)
    else:
        e = next(e for e in run.entries() if e['url'] == INSTITUTIONS and e.get('page_file'))
        insts = json.loads(run.load_page(e['page_file'])[0].text)
    if not insts:
        log('THEC: institution list unavailable'); return
    rows = insts if isinstance(insts, list) else insts.get('InstitutionList') or insts.get('data') or []
    by_name = {}
    for r in rows:
        name = r.get('InstitutionName') or r.get('Text') or r.get('text') or r.get('Name')
        ident = r.get('InstitutionId') or r.get('Value') or r.get('value') or r.get('Id')
        if name and ident is not None: by_name[norm_name(name)] = ident
    for key, name in institution_names.items():
        ident = by_name.get(norm_name(name))
        if ident is None:
            run.record({'institution_key': key, 'url': PROGRAMS, 'role': 'state_source', 'via': 'thec_api', 'fetched_at': now(),
                        'error': f'institution not in THEC list: {name}'}); continue
        payload = {'InstitutionId': ident, 'MajorName': '', 'ConcentrationName': '', 'FederalCipCode': '', 'Award': '',
                   'IsApprovedNotActiveChecked': False, 'IsActiveChecked': True, 'IsPhaseoutChecked': False}
        if (PROGRAMS, json.dumps(payload, sort_keys=True)) in done: continue
        meta, body = _request(fetcher, PROGRAMS, payload)
        _store(run, key, PROGRAMS, 'state_inventory', meta, body, payload, log=log)
    log(f'THEC: {len(institution_names)} institutions requested')
