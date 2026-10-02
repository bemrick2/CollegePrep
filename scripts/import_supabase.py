"""Emit transactional SQL batches from validated repository data; contains no secrets.

Run generated SQL through an authorized admin connection or Supabase connector.
Unmapped fields remain in the private lossless ledger, never discarded.
"""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from backend.catalog import ROOT,records,IMPORT_DOMAINS,import_contract_errors
from backend.store import natural_key
from scripts.validate_data import validate_record
SUPPORTED_DOMAINS=IMPORT_DOMAINS

def literal(v):
    if v is None: return 'null'
    if isinstance(v,bool): return 'true' if v else 'false'
    if isinstance(v,(int,float)): return str(v)
    return "'"+str(v).replace("'","''")+"'"

def bulk_batch(rows,accept_corrections=False):
    for row in rows:
        if row['domain'] not in SUPPORTED_DOMAINS:
            raise ValueError('Domain needs an explicit normalized mapping: '+row['domain'])
        problems=validate_record(ROOT/'data',row['payload'],0,domain=row['domain'])+import_contract_errors(row['domain'],row['payload'])
        if problems: raise ValueError('; '.join(problems))
    data=literal(json.dumps(rows,ensure_ascii=False))+'::jsonb'
    sql=f'''begin;
create temporary table import_rows(domain text,natural_key text,source_file text,payload jsonb) on commit drop;
insert into import_rows select * from jsonb_to_recordset({data}) as x(domain text,natural_key text,source_file text,payload jsonb);
do $guard$ begin
 perform pg_advisory_xact_lock(hashtextextended(natural_key,0)) from import_rows order by natural_key;
 if exists(select 1 from import_rows r join ingestion.reference_records old using(natural_key)
 where old.payload->>'verification_status'='verified' and (
 (r.payload->>'verification_status'<>'verified' and not (
 '''+literal(accept_corrections)+''' and nullif(btrim(r.payload->>'verification_correction_reason'),'') is not null)) or
 (old.payload->>'last_verified_at')::timestamptz>(r.payload->>'last_verified_at')::timestamptz))
 then raise exception 'Refusing weaker or older evidence'; end if;
end $guard$;
insert into ingestion.reference_revisions(natural_key,previous_payload)
 select old.natural_key,old.payload from import_rows r join ingestion.reference_records old using(natural_key) where old.payload<>r.payload;
insert into ingestion.reference_records(natural_key,domain,academic_year,source_file,payload)
 select natural_key,domain,payload->>'academic_year',source_file,payload from import_rows
 on conflict(natural_key) do update set payload=excluded.payload,source_file=excluded.source_file,imported_at=now()
 where reference_records.payload<>excluded.payload;
insert into public.sources(canonical_url,authority)
 select distinct payload->>'source_url',case
 when payload->>'source_url' like 'https://nces.ed.gov/%' or payload->>'source_url' like 'https://fsapartners.ed.gov/%' then 'federal'::public.source_authority
 when domain in ('state_aid','state_policies') then 'state'::public.source_authority else 'institution'::public.source_authority end
 from import_rows on conflict(canonical_url) do nothing;
'''
    def field(k,t='text'): return f"(r.payload->>{literal(k)})::{t}"
    def insert(domain,table,fields,conflict,extra=None,joins=''):
        vals={k:field(k,t) for k,t in fields.items()}; vals.update(extra or {})
        vals.update(source_id='s.id',verification_status=field('verification_status','public.verification_status'),last_verified_at=field('last_verified_at','timestamptz'))
        updates=','.join(f'{k}=excluded.{k}' for k in vals if k not in conflict)
        return f"insert into public.{table}({','.join(vals)}) select {','.join(vals.values())} from import_rows r join public.sources s on s.canonical_url=r.payload->>'source_url' {joins} where r.domain={literal(domain)} on conflict({','.join(conflict)}) do update set {updates};\n"
    text=lambda *ks:{k:'text' for k in ks}
    numbers=lambda *ks:{k:'numeric' for k in ks}
    ints=lambda *ks:{k:'integer' for k in ks}
    instjoin="join public.institutions i on i.institution_key=r.payload->>'institution_key'"
    sql+=insert('institutions','institutions',{**text('institution_key','display_name','state_code','city','website_url','admissions_url','financial_aid_url','control'),**ints('unitid')},['institution_key'],{'ipeds_name':"coalesce(r.payload->>'ipeds_name',r.payload->>'display_name')",'active':'null::boolean','identity_academic_year':field('academic_year'),'active_as_of_academic_year':field('active_as_of_academic_year','boolean')})
    sql+='''do $guard$ begin
 if exists(select 1 from import_rows r where r.domain<>'institutions' and r.payload->>'institution_key' is not null and not exists(select 1 from public.institutions i where i.institution_key=r.payload->>'institution_key')) then raise exception 'Missing institution dependency'; end if;
end $guard$;
'''
    sql+=insert('costs','institution_costs',{**text('academic_year','residency','currency','student_population','notes'),**numbers('tuition','mandatory_fees','books_supplies','on_campus_food_housing','on_campus_other_expenses','total_cost_of_attendance')},['institution_id','academic_year','residency'],{'institution_id':'i.id',**{column:f"coalesce(r.payload->>{literal(column)},r.payload->'components'->>{literal(component)})::numeric" for column,component in [('room','on_campus_housing'),('board','food'),('transportation','transportation'),('personal_misc','miscellaneous_personal')]}},instjoin)
    sql+=insert('admissions_metrics','admissions_metrics',{**text('academic_year','applicant_population','test_policy','notes'),**ints('entering_fall_year','applications','admits','enrolled','sat_reading_25','sat_reading_75','sat_math_25','sat_math_75'),**numbers('act_25','act_75','admit_rate')},['institution_id','entering_fall_year','applicant_population'],{'institution_id':'i.id','sat_25':"coalesce(r.payload->>'sat_25',r.payload->>'sat_composite_25')::integer",'sat_75':"coalesce(r.payload->>'sat_75',r.payload->>'sat_composite_75')::integer",'average_gpa':"coalesce(r.payload->>'average_gpa',r.payload->>'average_high_school_gpa')::numeric"},instjoin)
    sql+=insert('state_aid','state_aid_programs',{**text('academic_year','program_name','program_type','eligibility_summary','residency_requirement','gpa_requirement','test_requirement','income_requirement','award_amount_text','renewal_requirements','application_method','notes'),**numbers('award_min','award_max'),'renewable':'boolean','priority_deadline':'date','final_deadline':'date'},['state_code','program_name','academic_year'],{'state_code':field('state'),'official_url':field('source_url')})
    sql+=insert('awards','institutional_awards',{**text('academic_year','award_name','award_type','eligibility_summary','gpa_requirement','test_requirement','residency_requirement','major_requirement','award_amount_text','renewal_requirements','notes'),**numbers('award_min','award_max'),'automatic_consideration':'boolean','separate_application':'boolean','renewable':'boolean','full_tuition':'boolean','full_ride':'boolean','deadline':'date'},['institution_id','award_name','academic_year'],{'institution_id':'i.id'},instjoin)
    sql+=insert('appeals','appeal_policies',{**text('academic_year','appeal_kind','process_summary','required_documents','deadline_text','contact_method','notes','qualifying_path_evidence'),'offered':'boolean'},['institution_id','academic_year','appeal_kind'],{'institution_id':'i.id','policy_url':"coalesce(r.payload->>'policy_url',r.payload->>'source_url')",'qualifies_for_paid_addon':"coalesce((r.payload->>'qualifies_for_paid_addon')::boolean,false)"},instjoin)
    sql+=insert('credit_policies','credit_policies',{**text('academic_year','policy_kind','policy_url','notes'),**numbers('general_limit_credits','residency_credit_requirement')},['institution_id','policy_kind','academic_year'],{'institution_id':'i.id'},instjoin)
    sql+=insert('state_policies','state_policies',text('academic_year','policy_kind','policy_key','title','summary','notes'),['state_code','policy_kind','policy_key','academic_year'],{'state_code':"r.payload->>'state'",'official_url':"coalesce(r.payload->>'policy_url',r.payload->>'source_url')",'policy_details':'r.payload'})
    sql+=insert('federal_aid','federal_aid_programs',text('academic_year'),['program_key','academic_year'],{'program_key':"'pell_grant'",'policy_details':'r.payload'})
    sql+=insert('transfer_policies','transfer_policies',{**text('academic_year','min_grade','articulation_url','summary','notes'),**numbers('max_transfer_credits','max_transfer_percent','residency_requirement_credits')},['institution_id','academic_year'],{'institution_id':'i.id','policy_url':"coalesce(r.payload->>'policy_url',r.payload->>'source_url')",'policy_details':'r.payload'},instjoin)
    sql+=insert('academic_programs','academic_programs',{**text('academic_year','program_key','program_name','cip_code','credential_level','delivery_mode','catalog_year','program_url'),**numbers('total_credits'),'active':'boolean'},['institution_id','program_key','academic_year'],{'institution_id':'i.id'},instjoin)
    sql+='''do $guard$ begin
 if exists(select 1 from import_rows r where r.domain='degree_requirements' and not exists(
 select 1 from public.academic_programs p join public.institutions i on i.id=p.institution_id
 where i.institution_key=r.payload->>'institution_key' and p.program_key=r.payload->>'program_key'
 and p.academic_year=r.payload->>'academic_year')) then raise exception 'Missing program dependency for requested academic year'; end if;
end $guard$;
'''
    programjoin=instjoin+" join public.academic_programs p on p.institution_id=i.id and p.program_key=r.payload->>'program_key' and p.academic_year=r.payload->>'academic_year'"
    sql+=insert('degree_requirements','degree_requirements',{**text('academic_year','requirement_key','requirement_kind'),**numbers('minimum_credits','minimum_gpa')},['program_id','academic_year','requirement_key'],{'program_id':'p.id','rule_details':"coalesce(r.payload->'rule_details','{}'::jsonb)"},programjoin)
    eqfields=['exam_or_course_code','exam_or_course_name','minimum_score','institution_course_equivalent','credits_awarded','applies_to_gen_ed','applies_to_major','notes']
    # Retain superseded rows as history; only the reviewed snapshot stays current.
    sql+=f"update public.credit_equivalencies e set is_current=false from public.credit_policies p,public.institutions i,import_rows r where e.credit_policy_id=p.id and p.institution_id=i.id and i.institution_key=r.payload->>'institution_key' and p.academic_year=r.payload->>'academic_year' and p.policy_kind=r.payload->>'policy_kind' and r.domain='credit_policies';\n"
    values=["(eq->>'"+k+"')"+('::numeric' if k=='credits_awarded' else '::boolean' if k.startswith('applies_to') else '') for k in eqfields]
    conflict=['credit_policy_id','exam_or_course_code','minimum_score','institution_course_equivalent']
    updates=','.join(k+'=excluded.'+k for k in eqfields if k not in conflict)
    sql+=f"insert into public.credit_equivalencies(credit_policy_id,{','.join(eqfields)},is_current) select p.id,{','.join(values)},true from import_rows r {instjoin} join public.credit_policies p on p.institution_id=i.id and p.academic_year=r.payload->>'academic_year' and p.policy_kind=r.payload->>'policy_kind' cross join lateral jsonb_array_elements(r.payload->'equivalencies') eq where r.domain='credit_policies' on conflict({','.join(conflict)}) do update set {updates},is_current=true;\ncommit;"
    return sql

def batches(size=400,accept_corrections=False):
    collected=[]
    ordered=sorted(records(),key=lambda x: {'institutions':0,'academic_programs':1,'degree_requirements':3}.get(x[1],2))
    for path,domain,r in ordered:
        if domain not in SUPPORTED_DOMAINS: raise ValueError('Domain needs an explicit normalized mapping: '+domain)
        contract=import_contract_errors(domain,r)
        if contract: raise ValueError(path.relative_to(ROOT).as_posix()+': '+'; '.join(contract))
        if domain=='federal_aid' and 'pell_grant' not in r: raise ValueError('Federal program needs an explicit mapping')
        errors=validate_record(path,r,0,domain=domain)
        if domain!='institutions' and not r.get('academic_year'): errors.append('missing academic_year')
        if errors: raise ValueError('; '.join(errors))
        collected.append({'domain':domain,'natural_key':natural_key(domain,r),'source_file':path.relative_to(ROOT).as_posix(),'payload':r})
        if len(collected)==size:
            yield bulk_batch(collected,accept_corrections); collected=[]
    if collected: yield bulk_batch(collected,accept_corrections)

TABLES={'institutions':'public.institutions where institution_key is not null','costs':'public.institution_costs',
    'admissions_metrics':'public.admissions_metrics','state_aid':'public.state_aid_programs','awards':'public.institutional_awards',
    'appeals':'public.appeal_policies','credit_policies':'public.credit_policies','federal_aid':'public.federal_aid_programs',
    'academic_programs':'public.academic_programs where program_key is not null',
    'transfer_policies':'public.transfer_policies','degree_requirements':'public.degree_requirements',
    'state_policies':'public.state_policies'}

def reconcile_sql(fresh=True):
    """SQL assertions that every repository record landed in the ledger and its normalized table."""
    counts={}; equivalencies=0
    for _,domain,r in records():
        counts[domain]=counts.get(domain,0)+1
        if domain=='credit_policies': equivalencies+=len(r.get('equivalencies') or [])
    missing=set(counts)-set(TABLES)
    if missing: raise ValueError('No reconciliation table for domains: '+', '.join(sorted(missing)))
    checks=[]
    for domain,n in sorted(counts.items()):
        checks.append(f"if (select count(*) from ingestion.reference_records where domain={literal(domain)})<>{n} then raise exception 'ledger count mismatch for {domain}'; end if;")
        checks.append(f"if (select count(*) from {TABLES[domain]})<>{n} then raise exception 'normalized count mismatch for {domain}'; end if;")
    checks.append(f"if (select count(*) from public.credit_equivalencies where is_current)<>{equivalencies} then raise exception 'credit equivalency count mismatch'; end if;")
    if fresh: checks.append("if (select count(*) from ingestion.reference_revisions)<>0 then raise exception 'repeat import created revisions'; end if;")
    return 'do $reconcile$ begin\n '+'\n '.join(checks)+'\nend $reconcile$;\n'

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True); p.add_argument('--batch-size',type=int,default=400)
    p.add_argument('--reconcile-sql',type=Path,help='also write count assertions for a fresh database after import')
    p.add_argument('--accept-corrections',action='store_true',help='allow reviewed status corrections only with a persisted verification_correction_reason')
    p.add_argument('--existing-database',action='store_true',help='allow existing revision history during reconciliation'); a=p.parse_args()
    if not 1<=a.batch_size<=400: p.error('batch-size must be 1-400')
    a.output.mkdir(parents=True,exist_ok=True); count=0
    for count,sql in enumerate(batches(a.batch_size,a.accept_corrections),1): (a.output/f'{count:04}.sql').write_text(sql,encoding='utf-8')
    if a.reconcile_sql: a.reconcile_sql.write_text(reconcile_sql(fresh=not a.existing_database),encoding='utf-8')
    print(json.dumps({'batches':count,'output':str(a.output)}))
