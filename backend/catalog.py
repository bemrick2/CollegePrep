import json, csv
from datetime import date, timedelta
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
QUALIFYING = {'merit_reconsideration','competing_offer_review','financial_aid_appeal'}

# Import contract shared by scripts/validate_data.py and scripts/import_supabase.py.
# Every persisted domain must have a normalized Supabase mapping, and controlled values
# must match the database check constraints (see the latest supabase/migrations file).
IMPORT_DOMAINS = frozenset({'institutions','costs','admissions_metrics','state_aid','awards','appeals',
    'credit_policies','federal_aid','academic_programs','transfer_policies','degree_requirements','state_policies'})
CONTROLLED_VALUES = {
    'costs': {'residency': frozenset({'in_state','out_of_state','district','international','not_applicable'})},
    'credit_policies': {'policy_kind': frozenset({'AP','CLEP','IB','dual_enrollment','A_level','DSST','other',
        'cambridge_international','statewide_dual_credit','industry_certification'})},
    'appeals': {'appeal_kind': frozenset({'need_based_special_circumstances','professional_judgment',
        'merit_reconsideration','competing_offer_review','financial_aid_appeal','other',
        'scholarship_retention_appeal','budget_increase','dependency_override','sap_appeal'})},
    'degree_requirements': {'requirement_kind': frozenset({'total_credits','general_education','major','minor',
        'residency','gpa','other','program_plan'})},
    'state_policies': {'policy_kind': frozenset({'tuition_residency','statewide_articulation','transfer_pathway','dual_enrollment',
        'transfer_guarantee','dual_admission','other'})},
}
# Fields the normalized tables require (not null) beyond provenance.
REQUIRED_IMPORT_FIELDS = {
    'costs': ('academic_year','residency'),
    'admissions_metrics': ('entering_fall_year','applicant_population'),
    'state_aid': ('state','program_name','program_type','eligibility_summary','source_url'),
    'awards': ('institution_key','award_name','award_type','source_url'),
    'appeals': ('institution_key','appeal_kind','offered'),
    'credit_policies': ('institution_key','policy_kind','policy_url','source_url'),
    'transfer_policies': ('institution_key','academic_year','source_url'),  # policy_url falls back to source_url
    'academic_programs': ('institution_key','academic_year','program_key','program_name','source_url'),
    'degree_requirements': ('institution_key','academic_year','program_key','requirement_key','requirement_kind','source_url'),
    'state_policies': ('state','academic_year','policy_kind','policy_key','title','source_url'),
}

def import_contract_errors(domain,r):
    """Return reasons a record would be rejected by the normalized Supabase import."""
    errors=[]
    if domain not in IMPORT_DOMAINS:
        return ['domain %r has no normalized Supabase mapping; add one in scripts/import_supabase.py and a migration'%domain]
    for field in REQUIRED_IMPORT_FIELDS.get(domain,()):
        if r.get(field) in (None,''): errors.append('%s record missing %s required by the database'%(domain,field))
    for field,allowed in CONTROLLED_VALUES.get(domain,{}).items():
        if r.get(field) not in allowed: errors.append('%s.%s=%r is not allowed by the database check constraint'%(domain,field,r.get(field)))
    return errors

def records(root=ROOT):
    for path in sorted((root/'data').rglob('*')):
        if path.suffix == '.csv':
            with path.open(encoding='utf-8',newline='') as f:
                for r in csv.DictReader(f):
                    for k,v in list(r.items()):
                        if v == '': r[k]=None
                        elif k in {'unitid','applications','admits','enrolled','entering_fall_year','sat_reading_25','sat_reading_75','sat_math_25','sat_math_75','act_25','act_75','tuition','mandatory_fees','books_supplies','on_campus_food_housing','on_campus_other_expenses'}: r[k]=int(v)
                        elif v in {'True','False'}: r[k]=(v=='True')
                    yield path,r.pop('domain'),r
            continue
        if path.suffix not in {'.json','.jsonl'}: continue
        payloads = [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x] if path.suffix=='.jsonl' else [json.loads(path.read_text(encoding='utf-8'))]
        for payload in payloads:
            children=payload if isinstance(payload,list) else payload.get('records',[payload])
            parent={k:v for k,v in payload.items() if k in {'institution_key','academic_year','state','domain'}} if isinstance(payload,dict) else {}
            for child in children:
                r={**parent,**child}
                domain=r.pop('domain',None) or ('institutions' if path.name=='institution.json' else 'state_aid' if 'state_aid' in path.parts
                    else 'state_policies' if 'state_policies' in path.parts else path.parent.name)
                yield path,domain,r

def eligible_appeal(r,academic_year,today=None):
    today=today or date.today()
    try: verified=date.fromisoformat(r.get('last_verified_at','')[:10])
    except (TypeError,ValueError): return False
    return bool(r.get('academic_year')==academic_year and r.get('verification_status')=='verified'
        and r.get('offered') is True and r.get('appeal_kind') in QUALIFYING
        and r.get('qualifies_for_paid_addon') is True and r.get('qualifying_path_evidence')
        and r.get('source_url','').startswith('https://') and today-timedelta(days=365)<=verified<=today)
