#!/usr/bin/env python3
"""Review provenance of every verified Deep Dive record (academic_programs, degree_requirements, program_catalogs).

A promoted record names its evidence in `notes` ('Evidence: sources/programs/<ST>/<run>/evidence.json#<candidate_id>');
evidence.json keeps, per promoted candidate, the review decision (`decision.reason`), the field evidence and the source
document. Catalog counts keep their decision under 'catalog:<institution_key>:<year>' with the list page's sha256.
This report lists records without an evidence reference, references to a missing archive or candidate, and references
whose entry has neither a review decision nor a recorded correction (issue #129 entries). It does not change anything.

  python scripts/review_provenance.py
"""
import json,glob,re,collections,os
ev_cache={}
def ev(path):
    if path not in ev_cache:
        ev_cache[path]=json.load(open(path)) if os.path.exists(path) else None
    return ev_cache[path]
stats=collections.Counter(); bad=collections.defaultdict(list)
catalog_decisions=collections.defaultdict(list)  # (institution_key, sha256) -> archives holding a reviewed count decision
for p in glob.glob('sources/*/*/*/evidence.json'):
    for k,v in json.load(open(p)).items():
        if k.startswith('catalog:') and (v.get('decision') or {}).get('reason'):
            catalog_decisions[(k.split(':')[1], ((v['decision'].get('source_evidence') or {}).get('sha256') or ''))].append(p)
retained=set()
for p in glob.glob('sources/*/*/*/retention.json'):
    retained|={d.get('sha256') for d in json.load(open(p)).get('documents',[])}
for dom in ('academic_programs','degree_requirements','program_catalogs'):
    for f in glob.glob(f'data/institutions/*/{dom}/2026-27.json'):
        wrapper=json.load(open(f))
        for r in wrapper['records']:
            if r.get('verification_status')!='verified': continue
            if dom=='program_catalogs':
                ik=r.get('institution_key') or wrapper['institution_key']
                m=re.search(r'List document sha256 ([0-9a-f]{16})', r.get('notes',''))
                pre=(r.get('source_evidence') or {}).get('sha256') or (m.group(1) if m else '')
                full=[k[1] for k in catalog_decisions if k[0]==ik and pre and k[1].startswith(pre[:16])]
                sha=full[0] if full else ''
                if not full: stats[(dom,'no_count_decision')]+=1; bad[(dom,'no_count_decision')].append((f,pre[:16]))
                elif sha not in retained: stats[(dom,'list_not_retained')]+=1; bad[(dom,'list_not_retained')].append((f,sha[:16]))
                else: stats[(dom,'ok')]+=1
                continue
            n=r.get('notes','') + ' ' + (r.get('completeness_basis') or '') + ' ' + json.dumps(r.get('evidence') or '')
            refs=re.findall(r'(sources/[\w/.-]+/evidence\.json)#([0-9a-f]{16})', n)
            if not refs:
                stats[(dom,'no_evidence_ref')]+=1; bad[(dom,'no_evidence_ref')].append((f.split('/')[2], r.get('program_key'), r.get('requirement_key'), (r.get('notes') or '')[:120])); continue
            ok=True; decided=False
            for p,cid in refs:
                e=ev(p)
                if e is None: ok=False; stats[(dom,'evidence_file_missing')]+=1; bad[(dom,'evidence_file_missing')].append((f,p)); break
                item=e.get(cid)
                if not item: ok=False; stats[(dom,'candidate_missing')]+=1; bad[(dom,'candidate_missing')].append((f,p,cid)); break
                if (item.get('decision') or {}).get('reason'): decided=True
                elif not item.get('issue'): ok=False; stats[(dom,'ref_without_decision_or_correction')]+=1; bad[(dom,'ref_without_decision_or_correction')].append((f,p,cid)); break
            if ok and not decided: stats[(dom,'only_correction_refs')]+=1; bad[(dom,'only_correction_refs')].append((f.split('/')[2], r.get('program_key'), r.get('requirement_key'), refs, (r.get('notes') or '')[:300]))
            elif ok: stats[(dom,'ok')]+=1
print(json.dumps({f'{a}|{b}':v for (a,b),v in sorted(stats.items())},indent=1))
for k,v in bad.items():
    print(k, len(v)); [print('   ',x) for x in v[:6]]
json.dump({f'{a}|{b}':v for (a,b),v in bad.items()},open('/dev/null','w'),indent=1)
