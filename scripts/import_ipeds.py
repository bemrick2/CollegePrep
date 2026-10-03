"""Normalize pinned official NCES survey ZIPs. No current-year inference."""
import argparse,csv,hashlib,io,json,sys,zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from backend.catalog import ROOT
URL='https://nces.ed.gov/ipeds/datacenter/data/'
YEAR='2023-24'
STATES=set('AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY'.split())
def rows(path):
    with zipfile.ZipFile(path) as z:
        name=next(n for n in z.namelist() if n.lower().endswith('.csv'))
        return list(csv.DictReader(io.StringIO(z.read(name).decode('utf-8-sig'))))
def number(r,k):
    # Only reported values are verified; NCES imputed values stay unknown.
    if r.get('X'+k,'R').strip()!='R': return None
    try:
        v=int(r[k].strip())
        return v if v>=0 else None
    except (KeyError,ValueError): return None
def write(name,rs,states):
    groups={}
    for r in rs: groups.setdefault(states[str(r['unitid'])],[]).append(r)
    for state,group in groups.items():
        p=ROOT/'data/national/ipeds'/YEAR/state/name; p.parent.mkdir(parents=True,exist_ok=True)
        with p.open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(group[0])); w.writeheader(); w.writerows(group)
def import_data(directory,verified_at):
    hd=rows(directory/'HD2023.zip'); adm=rows(directory/'ADM2023.zip'); costs=rows(directory/'IC2023_AY.zip')
    ids={r['UNITID']:r for r in hd if r['STABBR'] in STATES and r['CYACTIVE']=='1'}
    aliases={}
    for p in (ROOT/'data/institutions').glob('*/institution.json'):
        r=json.loads(p.read_text()); aliases[str(r.get('unitid'))]=r['institution_key']
    def key(uid): return aliases.get(uid,'ipeds-'+uid)
    def provenance(domain,uid,survey):
        return {'domain':domain,'institution_key':key(uid),'unitid':int(uid),'academic_year':YEAR,
          'source_url':URL+survey+'.zip','verification_status':'verified','last_verified_at':verified_at}
    identities=[]
    for uid,r in ids.items():
        # Existing curated identities take priority; historical national snapshot remains in raw ZIP.
        if key(uid) in aliases.values(): continue
        identities.append({**provenance('institutions',uid,'HD2023'),'display_name':r['INSTNM'],
            'state_code':r['STABBR'],'city':r['CITY'],'website_url':r['WEBADDR'].strip(),
            'control':{'1':'public','2':'private_nonprofit','3':'private_for_profit'}.get(r['CONTROL']),
            # HD ICLEVEL: highest level of offering (CR-9: a 2-year college is never projected over four years).
            'level':{'1':'four_year','2':'two_year','3':'less_than_two_year'}.get(r['ICLEVEL'].strip()),
            'active_as_of_academic_year':True})
    admissions=[]
    for r in adm:
        uid=r['UNITID']
        if uid not in ids: continue
        admissions.append({**provenance('admissions_metrics',uid,'ADM2023'),
            'entering_fall_year':2023,'applicant_population':'first_time_degree_certificate_seeking_undergraduate',
            'applications':number(r,'APPLCN'),'admits':number(r,'ADMSSN'),'enrolled':number(r,'ENRLT'),
            'sat_reading_25':number(r,'SATVR25'),'sat_reading_75':number(r,'SATVR75'),
            'sat_math_25':number(r,'SATMT25'),'sat_math_75':number(r,'SATMT75'),
            'act_25':number(r,'ACTCM25'),'act_75':number(r,'ACTCM75')})
    prices=[]
    for r in costs:
        uid=r['UNITID']
        if uid not in ids: continue
        for n,residency in [('1','district'),('2','in_state'),('3','out_of_state')]:
            tuition=number(r,'CHG'+n+'AT3'); fees=number(r,'CHG'+n+'AF3')
            if tuition is None and fees is None: continue
            prices.append({**provenance('costs',uid,'IC2023_AY'),'residency':residency,
                'student_population':'full_time_first_time_undergraduate','tuition':tuition,'mandatory_fees':fees,
                'books_supplies':number(r,'CHG4AY3'),'on_campus_food_housing':number(r,'CHG5AY3'),
                'on_campus_other_expenses':number(r,'CHG6AY3'),
                'total_cost_of_attendance':None,'currency':'USD'})
    states={uid:r['STABBR'] for uid,r in ids.items()}
    for name,rs in [('institutions.csv',identities),('admissions.csv',admissions),('costs.csv',prices)]: write(name,rs,states)
    source_dir=ROOT/'sources/ipeds/2023-24'; source_dir.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for n in ['HD2023','ADM2023','IC2023_AY']:
        for suffix in ['', '_Dict']:
            name=n+suffix+'.zip'; b=(directory/name).read_bytes()
            entry={'filename':name,'source_url':URL+name,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'retrieved_at':verified_at}
            if len(b)>400000:
                parts=[]
                for i,offset in enumerate(range(0,len(b),131072)):
                    part=name+f'.part{i:03}'; (source_dir/part).write_bytes(b[offset:offset+131072]); parts.append(part)
                entry['parts']=parts
            else: (source_dir/name).write_bytes(b)
            manifest.append(entry)
    (source_dir/'manifest.json').write_text(json.dumps({'academic_year':YEAR,'files':manifest},indent=2)+'\n')
    print(f'Persisted {len(identities)} identities, {len(admissions)} admissions, {len(prices)} costs')
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--archive-dir',type=Path,required=True); p.add_argument('--verified-at',required=True); a=p.parse_args(); import_data(a.archive_dir,a.verified_at)
