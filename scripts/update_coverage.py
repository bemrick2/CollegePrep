import argparse,json,sys
from collections import Counter,defaultdict
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from backend.catalog import ROOT,records
def build():
    counts=Counter(); years=defaultdict(Counter); states=set(); identities=set(); policy_ids=set(); equivalents=0
    for _,domain,r in records():
        year=r.get('academic_year','identity'); counts[domain+'_records']+=1; years[year][domain+'_records']+=1
        if r.get('verification_status')=='verified':
            counts['verified_'+domain+'_records']+=1; years[year]['verified_'+domain+'_records']+=1
            if domain=='institutions': identities.add(r['institution_key'])
            elif r.get('institution_key'): policy_ids.add(r['institution_key'])
            if domain=='state_aid': states.add(r['state'])
            equivalents+=len(r.get('equivalencies',[]))
    report = {'generated_at':date.today().isoformat(),'status':'in_progress',
      'persistence_scope':'GitHub reference files; not a claim of live database deployment',
      'totals':{**dict(sorted(counts.items())),'states_and_dc_target':51,'states_complete':0,'states_partial':len(states),
        'institutions_verified':len(identities & policy_ids),'verified_institution_identities':len(identities),
        'complete_institutions':0,'verified_credit_equivalencies':equivalents},
      'by_academic_year':{k:dict(sorted(v.items())) for k,v in sorted(years.items())},
      'notes':['Verified historical observations are not current-year coverage.',
        'Completion requires a reviewed full domain inventory; none is persisted yet.',
        'Nested equivalencies inherit parent provenance; null credit amounts remain unknown.']}
    snapshot=ROOT/'docs/coverage/live-supabase.json'
    if snapshot.exists(): report['live_database_snapshot']=json.loads(snapshot.read_text(encoding='utf-8'))
    return report
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--check',action='store_true'); args=p.parse_args(); target=ROOT/'docs/coverage/coverage.json'; result=build()
    if args.check:
        actual=json.loads(target.read_text()); actual.pop('generated_at',None); result.pop('generated_at',None)
        if actual!=result: sys.exit('Coverage is out of date; run scripts/update_coverage.py')
        print('Coverage matches persisted records')
    else: target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
