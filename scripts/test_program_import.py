"""Emit rollback-only PostgreSQL integration tests; synthetic data never enters data/."""
import copy
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from backend.store import natural_key
from scripts.import_supabase import bulk_batch

def fixture_rows():
    common={'institution_key':'test-program-import','verification_status':'verified',
            'source_url':'https://example.edu/catalog-test','last_verified_at':'2026-10-02'}
    specifications=[('institutions',{'display_name':'Integration fixture','state_code':'TN'}),
        ('academic_programs',{'academic_year':'2025-26','program_key':'biology-bs','program_name':'Biology','total_credits':120}),
        ('academic_programs',{'academic_year':'2026-27','program_key':'biology-bs','program_name':'Biological Sciences'}),
        ('transfer_policies',{'academic_year':'2026-27','min_grade':'C','max_transfer_credits':60}),
        ('credit_policies',{'academic_year':'2026-27','policy_kind':'AP','policy_url':common['source_url'],'equivalencies':[{'exam_or_course_code':'TEST-OLD','minimum_score':None,'institution_course_equivalent':None,'credits_awarded':3}]}),
        ('admissions_metrics',{'academic_year':'2026-27','entering_fall_year':2026,'applicant_population':'first_time_first_year','sat_composite_25':1230,'sat_composite_75':1380,'sat_reading_25':620,'sat_math_25':630,'average_high_school_gpa':4.25,'notes':'Reported composite, not a sum; GPA uses institutional weights.'}),
        ('costs',{'academic_year':'2026-27','residency':'in_state','currency':'USD','components':{'on_campus_housing':9500,'food':5000,'transportation':3500,'miscellaneous_personal':3000},'notes':'Additional program fees may apply.'}),
        ('degree_requirements',{'academic_year':'2025-26','program_key':'biology-bs','requirement_key':'major','requirement_kind':'major','minimum_credits':40,'rule_details':{'schema':'requirement_group/v1','catalog_year':'2025-2026','group_type':'credit_total','category':'major_core'}}),
        ('degree_requirements',{'academic_year':'2026-27','program_key':'biology-bs','requirement_key':'major','requirement_kind':'major','rule_details':{'schema':'requirement_group/v1','catalog_year':'2026-2027','group_type':'all_required','category':'major_core','description':"Advisor's approval required",'courses':[{'code':'BIO 101'}]}})]
    rows=[]
    for domain,fields in specifications:
        payload={**common,**fields}
        rows.append({'domain':domain,'natural_key':natural_key(domain,payload),'source_file':'tests/synthetic.json','payload':payload})
    return rows

def body(rows,accept_corrections=False):
    return bulk_batch(rows,accept_corrections).removeprefix('begin;').removesuffix('commit;')+'\ndrop table import_rows;\n'

def integration_sql():
    rows=fixture_rows()
    sql='begin;\n'+body(rows)+body(rows)
    sql+='''do $test$ begin
 if (select count(*) from public.academic_programs p join public.institutions i on i.id=p.institution_id where i.institution_key='test-program-import')<>2 then raise exception 'Annual programs lost or duplicated'; end if;
 if exists(select 1 from public.academic_programs p join public.institutions i on i.id=p.institution_id where i.institution_key='test-program-import' and (p.active is not null or (p.academic_year='2026-27' and p.total_credits is not null))) then raise exception 'Unknown values guessed'; end if;
 if (select count(*) from public.degree_requirements d join public.academic_programs p on p.id=d.program_id join public.institutions i on i.id=p.institution_id where i.institution_key='test-program-import' and d.academic_year=p.academic_year)<>2 then raise exception 'Requirements attached to wrong catalog'; end if;
 if exists(select 1 from ingestion.reference_revisions where natural_key like '%test-program-import%') then raise exception 'Idempotent import created revisions'; end if;
 if (select count(*) from public.credit_equivalencies e join public.credit_policies p on p.id=e.credit_policy_id join public.institutions i on i.id=p.institution_id where i.institution_key='test-program-import')<>1 then raise exception 'Null equivalency keys duplicated'; end if;
 if not exists(select 1 from public.admissions_metrics a join public.institutions i on i.id=a.institution_id where i.institution_key='test-program-import' and a.sat_25=1230 and a.average_gpa=4.25 and a.notes is not null) then raise exception 'Reported composite or context lost'; end if;
 if not exists(select 1 from public.institution_costs c join public.institutions i on i.id=c.institution_id where i.institution_key='test-program-import' and c.room=9500 and c.board=5000 and c.total_cost_of_attendance is null and c.notes is not null) then raise exception 'Published components lost or missing total guessed'; end if;
end $test$;
'''
    for case in ['missing_parent','weaker_evidence']:
        changed=copy.deepcopy(rows[-1])
        if case=='missing_parent': changed['payload']['academic_year']='2099-00'; changed['payload']['rule_details']['catalog_year']='2099-2100'
        else: changed['payload']['verification_status']='partially_verified'
        changed['natural_key']=natural_key(changed['domain'],changed['payload'])
        expected='Missing program dependency for requested academic year' if case=='missing_parent' else 'Refusing weaker or older evidence'
        sql+="do $negative$ begin\n begin\n"+body([changed])+"raise exception 'Expected rejection did not occur';\n exception when raise_exception then\n if sqlerrm<>"+"'"+expected+"' then raise; end if;\n end;\nend $negative$;\n"
    correction=copy.deepcopy(rows[-1]); correction['payload']['verification_status']='partially_verified'
    correction['payload']['verification_correction_reason']='Fixture: year label is not established by official source'
    # A per-key approval list (supabase/corrections.json) admits only the listed record.
    sql+="do $negative$ begin\n begin\n"+body([correction],accept_corrections=frozenset({'["other"]'}))+"raise exception 'Expected rejection did not occur';\n exception when raise_exception then\n if sqlerrm<>'Refusing weaker or older evidence' then raise; end if;\n end;\nend $negative$;\n"
    sql+=body([correction],accept_corrections=frozenset({correction['natural_key']}))
    revised=copy.deepcopy(next(r for r in rows if r['domain']=='credit_policies'))
    revised['payload']['equivalencies'][0]['exam_or_course_code']='TEST-NEW'
    sql+=body([revised])+body([revised])
    sql+='''do $test$ begin
 if (select count(*) from ingestion.reference_revisions where natural_key like '%test-program-import%')<>2 then raise exception 'Correction or policy history lost'; end if;
 if (select count(*) from public.credit_equivalencies e join public.credit_policies p on p.id=e.credit_policy_id join public.institutions i on i.id=p.institution_id where i.institution_key='test-program-import')<>2 then raise exception 'Superseded equivalency lost or repeat import duplicated'; end if;
 if (select count(*) from public.credit_equivalencies e join public.credit_policies p on p.id=e.credit_policy_id join public.institutions i on i.id=p.institution_id where i.institution_key='test-program-import' and e.is_current)<>1 then raise exception 'Retired equivalency still current'; end if;
end $test$;
'''
    return sql+'rollback;\n'

if __name__=='__main__': print(integration_sql())
