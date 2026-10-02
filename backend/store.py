"""Transactional, idempotent local reference adapter; no live Supabase credentials."""
import argparse,hashlib,json,sqlite3
from contextlib import closing
from datetime import datetime,timezone
from pathlib import Path
from backend.catalog import ROOT,records,eligible_appeal

DDL='''
create table if not exists reference_records (
 natural_key text primary key, domain text not null, institution_key text,
 state_code text, academic_year text, payload text not null, digest text not null
);
create index if not exists reference_school_year on reference_records(institution_key,academic_year,domain);
create index if not exists reference_state on reference_records(state_code,domain);
create table if not exists record_revisions (
 id integer primary key, natural_key text not null, previous_payload text not null,
 replaced_at text not null, incoming_digest text not null
);
create table if not exists import_runs (
 id integer primary key, imported_at text not null, inserted integer not null,
 unchanged integer not null, revised integer not null
);
'''
def natural_key(domain,r):
    if domain in {'academic_programs','degree_requirements','transfer_policies'}:
        # Names and optional record labels may change without changing identity.
        discriminator={k:r.get(k) for k in (['program_key','requirement_key'] if domain=='degree_requirements' else ['program_key'] if domain=='academic_programs' else [])}
        return json.dumps([domain,r.get('institution_key'),None,r.get('academic_year'),discriminator],sort_keys=True)
    discriminator={k:r.get(k) for k in ['record_key','program_name','award_name','policy_kind','appeal_kind','residency','program_key','requirement_key','applicant_population'] if r.get(k) is not None}
    return json.dumps([domain,r.get('institution_key'),r.get('state'),r.get('academic_year'),discriminator],sort_keys=True)

def connect(path):
    db=sqlite3.connect(path); db.row_factory=sqlite3.Row; db.executescript(DDL); return db

def load(db,root=ROOT,accept_revisions=False,accept_corrections=False):
    counts={'inserted':0,'unchanged':0,'revised':0}; now=datetime.now(timezone.utc).isoformat()
    with db:
        for _,domain,r in records(root):
            from scripts.validate_data import validate_record
            problems=validate_record(root/'data',r,0,domain=domain)
            if domain!='institutions' and not r.get('academic_year'): problems.append('missing academic_year')
            if problems: raise ValueError('; '.join(problems))
            key=natural_key(domain,r); payload=json.dumps(r,sort_keys=True,ensure_ascii=False)
            digest=hashlib.sha256(payload.encode()).hexdigest()
            old=db.execute('select payload,digest from reference_records where natural_key=?',(key,)).fetchone()
            if old and old['digest']==digest: counts['unchanged']+=1; continue
            if old:
                prev=json.loads(old['payload'])
                correction=accept_corrections and isinstance(r.get('verification_correction_reason'),str) and r['verification_correction_reason'].strip()
                if prev.get('last_verified_at') and r.get('last_verified_at') and prev['last_verified_at'][:10]>r['last_verified_at'][:10]:
                    raise ValueError('Refusing older evidence: '+key)
                if prev.get('verification_status')=='verified' and r.get('verification_status')!='verified' and not correction:
                    raise ValueError('Refusing weaker evidence over verified record: '+key)
                if not accept_revisions: raise ValueError('Changed existing record needs --accept-revisions: '+key)
                db.execute('insert into record_revisions(natural_key,previous_payload,replaced_at,incoming_digest) values (?,?,?,?)',(key,old['payload'],now,digest))
                counts['revised']+=1
            else: counts['inserted']+=1
            db.execute('insert into reference_records values (?,?,?,?,?,?,?) on conflict(natural_key) do update set payload=excluded.payload,digest=excluded.digest,state_code=excluded.state_code',
                (key,domain,r.get('institution_key'),r.get('state_code') or r.get('state'),r.get('academic_year'),payload,digest))
        db.execute('insert into import_runs(imported_at,inserted,unchanged,revised) values (?,?,?,?)',(now,counts['inserted'],counts['unchanged'],counts['revised']))
    return counts

def school(db,key,year):
    identities=db.execute("select payload from reference_records where domain='institutions' and institution_key=?",(key,)).fetchall()
    if not identities: return None
    rs=db.execute("select domain,payload from reference_records where institution_key=? and academic_year=? and domain<>'institutions' order by domain,natural_key",(key,year)).fetchall()
    domains={}
    for row in rs: domains.setdefault(row['domain'],[]).append(json.loads(row['payload']))
    return {'institution':json.loads(identities[0]['payload']),'academic_year':year,'domains':domains,
        'can_offer_paid_addon':any(eligible_appeal(r,year) for r in domains.get('appeals',[])),
        'missing_domains':[d for d in ['costs','admissions_metrics','awards','credit_policies','transfer_policies','degree_requirements','appeals'] if d not in domains]}

COMPARISON_DOMAINS=['costs','admissions_metrics','awards','credit_policies','transfer_policies','academic_programs','degree_requirements','appeals']

def compare(db,keys,year):
    if not isinstance(year,str) or not year.strip() or len(year)>40:
        raise ValueError('academic_year is required (maximum 40 characters)')
    if not 1<=len(keys)<=20 or any(not isinstance(k,str) or not k.strip() or len(k)>200 for k in keys) or len(set(keys))!=len(keys):
        raise ValueError('Provide 1 to 20 distinct nonempty institution keys')
    results=[]
    for key in keys:
        profile=school(db,key,year)
        identity=profile['institution'] if profile and profile['institution'].get('verification_status')=='verified' else None
        domains={d:[r for r in profile['domains'].get(d,[]) if r.get('verification_status')=='verified'] if identity else [] for d in COMPARISON_DOMAINS}
        results.append({'institution_key':key,'found':identity is not None,'institution':identity,
            'academic_year':year,'domains':domains,'missing_domains':[d for d,rs in domains.items() if not rs],
            'can_offer_paid_addon':any(eligible_appeal(r,year) for r in domains['appeals'])})
    return {'academic_year':year,'institutions':results}

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--database',type=Path,required=True); p.add_argument('--accept-revisions',action='store_true'); p.add_argument('--accept-corrections',action='store_true'); a=p.parse_args()
    a.database.parent.mkdir(parents=True,exist_ok=True)
    with closing(connect(a.database)) as db: print(json.dumps(load(db,accept_revisions=a.accept_revisions,accept_corrections=a.accept_corrections)))
