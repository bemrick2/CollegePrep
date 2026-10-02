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
        ('degree_requirements',{'academic_year':'2025-26','program_key':'biology-bs','requirement_key':'major','requirement_kind':'major','minimum_credits':40}),
        ('degree_requirements',{'academic_year':'2026-27','program_key':'biology-bs','requirement_key':'major','requirement_kind':'major','rule_details':{'description':"Advisor's approval required",'courses':['BIO 101']}})]
    rows=[]
    for domain,fields in specifications:
        payload={**common,**fields}
        rows.append({'domain':domain,'natural_key':natural_key(domain,payload),'source_file':'tests/synthetic.json','payload':payload})
    return rows

def body(rows):
    return bulk_batch(rows).removeprefix('begin;').removesuffix('commit;').replace('on commit drop;', 'on commit drop;')+'\ndrop table import_rows;\n'

def integration_sql():
    rows=fixture_rows()
    sql='begin;\n'+body(rows)+body(rows)
    sql+='''do $test$ begin
 if (select count(*) from public.academic_programs p join public.institutions i on i.id=p.institution_id where i.institution_key='test-program-import')<>2 then raise exception 'Annual programs lost or duplicated'; end if;
 if exists(select 1 from public.academic_programs p join public.institutions i on i.id=p.institution_id where i.institution_key='test-program-import' and (p.active is not null or (p.academic_year='2026-27' and p.total_credits is not null))) then raise exception 'Unknown values guessed'; end if;
 if (select count(*) from public.degree_requirements d join public.academic_programs p on p.id=d.program_id join public.institutions i on i.id=p.institution_id where i.institution_key='test-program-import' and d.academic_year=p.academic_year)<>2 then raise exception 'Requirements attached to wrong catalog'; end if;
 if exists(select 1 from ingestion.reference_revisions where natural_key like '%test-program-import%') then raise exception 'Idempotent import created revisions'; end if;
end $test$;
'''
    for case in ['missing_parent','weaker_evidence']:
        changed=copy.deepcopy(rows[-1])
        if case=='missing_parent': changed['payload']['academic_year']='2099-00'
        else: changed['payload']['verification_status']='partially_verified'
        changed['natural_key']=natural_key(changed['domain'],changed['payload'])
        expected='Missing program dependency for requested academic year' if case=='missing_parent' else 'Refusing weaker or older evidence'
        sql+="do $negative$ begin\n begin\n"+body([changed])+"raise exception 'Expected rejection did not occur';\n exception when raise_exception then\n if sqlerrm<>"+"'"+expected+"' then raise; end if;\n end;\nend $negative$;\n"
    return sql+'rollback;\n'

if __name__=='__main__': print(integration_sql())
