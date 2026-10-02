import json
from datetime import date, timedelta
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
QUALIFYING = {'merit_reconsideration','competing_offer_review','financial_aid_appeal'}

def records(root=ROOT):
    for path in sorted((root/'data').rglob('*')):
        if path.suffix not in {'.json','.jsonl'}: continue
        payloads = [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x] if path.suffix=='.jsonl' else [json.loads(path.read_text(encoding='utf-8'))]
        for payload in payloads:
            children=payload if isinstance(payload,list) else payload.get('records',[payload])
            parent={k:v for k,v in payload.items() if k in {'institution_key','academic_year','state','domain'}} if isinstance(payload,dict) else {}
            for child in children:
                r={**parent,**child}
                domain=r.pop('domain',None) or ('institutions' if path.name=='institution.json' else 'state_aid' if 'state_aid' in path.parts else path.parent.name)
                yield path,domain,r

def eligible_appeal(r,academic_year,today=None):
    today=today or date.today()
    try: verified=date.fromisoformat(r.get('last_verified_at','')[:10])
    except (TypeError,ValueError): return False
    return bool(r.get('academic_year')==academic_year and r.get('verification_status')=='verified'
        and r.get('offered') is True and r.get('appeal_kind') in QUALIFYING
        and r.get('qualifies_for_paid_addon') is True and r.get('qualifying_path_evidence')
        and r.get('source_url','').startswith('https://') and today-timedelta(days=365)<=verified<=today)
