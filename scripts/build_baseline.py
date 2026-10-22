#!/usr/bin/env python3
"""National school-level baseline from pinned IPEDS files, and its completeness report.

Every in-scope school (each four-year school in pipeline/registry/<ST>.json; docs/coverage/baseline/UNIVERSE.md) gets one
row per collection year in baseline/schools/<year>/<ST>.csv. For each essential field the row holds the values exactly as
NCES published them and a status:

  verified_current      reported by the school to NCES, and the latest release of that survey (the next year's file is
                        recorded as not yet served in sources/ipeds/<next>/manifest.json)
  available_older       reported, but older than current: a newer release exists, or it is a price or an average for a
                        past year (2023-24 prices are not 2026-27 prices; net price averages are a past year's aid)
  not_published_or_na   NCES or the school says it does not apply (open admission, test blind, no first-time cohort)
  not_researched        no reported value in the bulk files (no survey record, value left blank, or NCES imputed it);
                        the school's own publications have not been checked yet
  blocked               a source we need is inaccessible (recorded by research, never by this script)

Missing or suppressed values are never written as zero; an imputed NCES value is never shown as a reported one.
Historical averages (net price), published prices (tuition, housing, cost of attendance) and personalised estimates are
kept apart: this file holds only the first two, labelled with their year (baseline/FIELDS.json).

  python3 scripts/build_baseline.py           write baseline/ and docs/coverage/baseline/
  python3 scripts/build_baseline.py --check   fail if a committed IPEDS-derived file (baseline/, UNIVERSE) is stale
"""
from __future__ import annotations
import collections, csv, io, json, re, sys, time, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
YEAR = '2023-24'
NEXT = {'2023-24': '2024-25'}
PLANNING_YEAR = '2026-27'  # the year families are choosing for; a price for an earlier year is older than current
STATES = set('AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK '
             'OR PA RI SC SD TN TX UT VT VA WA WV WI WY'.split())
CONTROL = {'1': 'public', '2': 'private_nonprofit', '3': 'private_for_profit'}
REPORTED = {'R'}            # flag values that are a reported measurement
REPORTED_OR_ZERO = {'R', 'Z'}  # counts: Z is NCES's "implied zero", a reported structural zero
STATUSES = ('verified_current', 'available_older', 'not_published_or_na', 'not_researched', 'blocked')

# The essential school-level fields. `sources` name the pinned file and the variables used; NCES's own title and definition
# for each variable are copied into baseline/FIELDS.json from baseline/reference/ipeds_labels.json.
FIELDS = [
    {'key': 'identity', 'label': 'Name, location, website, type and control', 'kind': 'directory',
     'period': 'IPEDS 2023-24 institutional directory',
     'sources': [{'file': 'HD2023', 'variables': ['INSTNM', 'CITY', 'STABBR', 'WEBADDR', 'CONTROL', 'ICLEVEL', 'HLOFFER']}],
     'columns': ['name', 'city', 'state', 'website_url', 'control', 'level', 'highest_offering', 'closed_per_hd2024']},
    {'key': 'undergraduate_enrollment', 'label': 'Undergraduate enrollment (fall headcount)', 'kind': 'statistic',
     'period': 'Fall 2023', 'next_file': 'DRVEF2024',
     'sources': [{'file': 'DRVEF2023', 'variables': ['EFUG', 'EFUGFT', 'EFUGPT']},
                 {'file': 'EF2023A', 'variables': ['EFTOTLT'], 'role': 'imputation flag of the all-undergraduate line (EFALEVEL 2)'}],
     'columns': ['undergraduate_enrollment', 'undergraduate_full_time', 'undergraduate_part_time']},
    {'key': 'admission_rate', 'label': 'Admission rate, first-time undergraduates', 'kind': 'statistic',
     'period': 'Fall 2023 applicants', 'next_file': 'ADM2024',
     'sources': [{'file': 'DRVADM2023', 'variables': ['DVADM01']},
                 {'file': 'ADM2023', 'variables': ['APPLCN', 'ADMSSN'], 'role': 'imputation flags of the counts'},
                 {'file': 'IC2023', 'variables': ['OPENADMP'], 'role': 'open admission: no selection, so no rate'}],
     'columns': ['admission_rate_percent', 'applications', 'admits', 'open_admission']},
    {'key': 'test_scores', 'label': 'ACT/SAT middle 50% of enrolled first-year students, with the test policy', 'kind': 'statistic',
     'period': 'Fall 2023 enrolled first-time students who submitted scores', 'next_file': 'ADM2024',
     'sources': [{'file': 'ADM2023', 'variables': ['SATVR25', 'SATVR75', 'SATMT25', 'SATMT75', 'ACTCM25', 'ACTCM75', 'SATPCT',
                                                    'ACTPCT', 'ADMCON7']}],
     'columns': ['test_policy', 'sat_ebrw_25', 'sat_ebrw_75', 'sat_math_25', 'sat_math_75', 'act_composite_25',
                 'act_composite_75', 'percent_submitting_sat', 'percent_submitting_act'],
     'context': 'Percentiles describe enrolled students who submitted scores; at test-optional schools they are not the '
                'whole class. SAT section percentiles are never added into a composite.'},
    {'key': 'tuition_fees', 'label': 'Published in-state and out-of-state tuition and required fees', 'kind': 'published_price',
     'period': '2023-24 academic year (full-time first-time undergraduates)',
     'sources': [{'file': 'IC2023_AY', 'variables': ['CHG2AT3', 'CHG2AF3', 'CHG3AT3', 'CHG3AF3']}],
     'columns': ['in_state_tuition', 'in_state_fees', 'out_of_state_tuition', 'out_of_state_fees']},
    {'key': 'housing_food', 'label': 'On-campus food and housing', 'kind': 'published_price',
     'period': '2023-24 academic year',
     'sources': [{'file': 'IC2023_AY', 'variables': ['CHG5AY3']}],
     'columns': ['on_campus_food_housing']},
    {'key': 'cost_of_attendance', 'label': 'Total cost of attendance, living on campus (NCES total price)', 'kind': 'published_price',
     'period': '2023-24 academic year',
     'sources': [{'file': 'DRVIC2023', 'variables': ['CINSON', 'COTSON']},
                 {'file': 'IC2023_AY', 'variables': ['CHG2AT3', 'CHG2AF3', 'CHG3AT3', 'CHG3AF3', 'CHG4AY3', 'CHG5AY3', 'CHG6AY3'],
                  'role': 'imputation flags of the components'}],
     'columns': ['coa_in_state_on_campus', 'coa_out_of_state_on_campus'],
     'context': 'NCES sums tuition and fees, books and supplies, on-campus food and housing and other expenses. Shown only '
                'when every component was reported, not imputed.'},
    {'key': 'net_price', 'label': 'Average net price, overall and by family income', 'kind': 'historical_average',
     'period': '2022-23 aid year (full-time first-time undergraduates awarded aid)',
     'sources': [{'file': 'SFA2223', 'variables': ['NPIST2', 'NPIS412', 'NPIS422', 'NPIS432', 'NPIS442', 'NPIS452',
                                                   'NPGRN2', 'NPT412', 'NPT422', 'NPT432', 'NPT442', 'NPT452']}],
     'columns': ['net_price_average', 'net_price_income_0_30000', 'net_price_income_30001_48000',
                 'net_price_income_48001_75000', 'net_price_income_75001_110000', 'net_price_income_over_110000',
                 'net_price_basis'],
     'context': 'An average over students who received aid in a past year: not a price, not an offer, not a personal '
                'estimate. Publics report in-state students (NPIS*), privates all students (NPGRN2, NPT*).'},
    {'key': 'retention_rate', 'label': 'First-year retention rate (full-time)', 'kind': 'statistic',
     'period': 'Fall 2022 entering cohort, re-enrolled fall 2023', 'next_file': 'EF2024D',
     'sources': [{'file': 'EF2023D', 'variables': ['RET_PCF']}],
     'columns': ['retention_rate_full_time']},
    {'key': 'graduation_rate', 'label': "Bachelor's graduation rate (4- and 6-year) and overall rate", 'kind': 'statistic',
     'period': '2017 entering cohort, reported 2023-24', 'next_file': 'DRVGR2024',
     'sources': [{'file': 'DRVGR2023', 'variables': ['BAGR100', 'BAGR150', 'GRRTTOT']},
                 {'file': 'GR2023', 'variables': ['GRTOTLT'], 'role': 'imputation flags of the cohort counts'}],
     'columns': ['bachelors_grad_rate_4yr', 'bachelors_grad_rate_6yr', 'grad_rate_overall_150pct']},
    {'key': 'fields_and_levels', 'label': 'Broad fields of study and degree levels awarded', 'kind': 'statistic',
     'period': 'Awards conferred July 2022 - June 2023', 'next_file': 'C2024_A',
     'sources': [{'file': 'C2023_A', 'variables': ['CIPCODE', 'AWLEVEL', 'MAJORNUM', 'CTOTALT']}],
     'columns': ['fields_with_bachelors', 'degree_levels_awarded'],
     'context': 'Field families are CIP 2020 two-digit codes with at least one award (first majors). Per-field counts are in '
                'baseline/fields_of_study/<year>/<ST>.csv.'},
]
AWARD_LEVELS = {'3': 'associate', '5': 'bachelor', '7': 'master', '17': 'doctor_research', '18': 'doctor_professional',
                '19': 'doctor_other'}


def manifest(year):
    p = ROOT / 'sources/ipeds' / year / 'manifest.json'
    return json.loads(p.read_text()) if p.exists() else {'files': [], 'unavailable': []}


def pinned_bytes(year, filename):
    d = ROOT / 'sources/ipeds' / year
    f = next(x for x in manifest(year)['files'] if x['filename'] == filename)
    return b''.join((d / p).read_bytes() for p in f['parts']) if f.get('parts') else (d / filename).read_bytes()


def table(file, year=YEAR):
    with zipfile.ZipFile(io.BytesIO(pinned_bytes(year, file + '.zip'))) as z:
        names = [n for n in z.namelist() if n.lower().endswith('.csv')]
        name = next((n for n in names if '_rv' not in n.lower()), names[0])  # the revised file when NCES ships both
        name = next((n for n in names if '_rv' in n.lower()), name)
        text = z.read(name).decode('utf-8-sig', 'replace')
    return [{k.strip().lstrip('﻿'): (v or '').strip() for k, v in r.items()} for r in csv.DictReader(io.StringIO(text))]


def by_unitid(rows):
    return {r['UNITID']: r for r in rows}


def num(r, var, ok=REPORTED, flagged=True, cast=int, signed=False):
    """A reported value or None. Blank, negative codes (-1 not reported, -2 not applicable) and imputed values are None.
    `signed`: the variable can be truly negative (a net price where aid exceeds the price); a negative is kept only when the
    school-reported flag says so."""
    if r is None: return None
    v = r.get(var, '')
    if v in ('', '.'): return None
    if flagged and ('X' + var) in r and r['X' + var] not in ok: return None
    try:
        x = cast(v)
    except ValueError:
        try: x = cast(float(v))
        except ValueError: return None
    if x < 0 and not (signed and flagged and r.get('X' + var) in ok): return None
    return x


def flag(r, var):
    return (r or {}).get('X' + var)


def latest(field):
    """A statistic is current when NCES has not yet served the next year's file (recorded by the pin workflow)."""
    nf = field.get('next_file')
    if not nf: return False
    m = manifest(NEXT[YEAR])
    if any(f['filename'] == nf + '.zip' for f in m['files']): return False
    # Only an HTTP 404 means "not released"; a server or network error proves nothing.
    u = next((u for u in m.get('unavailable', []) if u['filename'] == nf + '.zip' and str(u.get('http_status')) == '404'), None)
    return u['checked_at'] if u else False


def registry():
    out = []
    for p in sorted((ROOT / 'pipeline/registry').glob('*.json')):
        if len(p.stem) != 2 or p.stem not in STATES: continue
        for i in json.loads(p.read_text())['institutions']:
            if i.get('level') == 'four_year': out.append({**i, 'state': p.stem})
    return out


_CACHE = {}


def load_cache():
    if 't' not in _CACHE: _CACHE['t'] = load()
    return _CACHE['t']


def load():
    t = {f: by_unitid(table(f)) for f in ['HD2023', 'DRVEF2023', 'DRVADM2023', 'ADM2023', 'IC2023', 'IC2023_AY', 'DRVIC2023',
                                           'SFA2223', 'EF2023D', 'DRVGR2023']}
    t['EF2023A_UG'] = {r['UNITID']: r for r in table('EF2023A') if r.get('EFALEVEL') == '2'}
    gr = collections.defaultdict(set)
    for r in table('GR2023'):
        for k, v in r.items():
            if k.startswith('X') and v: gr[r['UNITID']].add(v)
    t['GR_FLAGS'] = gr
    comp = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.Counter()))
    t['C_ROWS'] = set()
    for r in table('C2023_A'):
        t['C_ROWS'].add(r['UNITID'])
        code = r['CIPCODE']
        if code == '99' or r.get('MAJORNUM') != '1': continue
        n = num(r, 'CTOTALT', REPORTED_OR_ZERO)
        if not n: continue
        comp[r['UNITID']][code[:2]][r['AWLEVEL']] += n
    t['C'] = comp
    t['FLAGS'] = by_unitid(table('FLAGS2023')) if any(f['filename'] == 'FLAGS2023.zip' for f in manifest(YEAR)['files']) else {}
    hd24 = manifest(NEXT[YEAR])
    t['HD2024'] = by_unitid(table('HD2024', NEXT[YEAR])) if any(f['filename'] == 'HD2024.zip' for f in hd24['files']) else {}
    return t


def cip_families():
    """Two-digit CIP 2020 family titles as NCES prints them (sources/ipeds/reference/CIPCode2020.csv)."""
    try: raw = pinned_bytes('reference', 'CIPCode2020.csv').decode('utf-8-sig')
    except (StopIteration, FileNotFoundError): return {}
    out = {}
    for r in csv.DictReader(io.StringIO(raw)):
        code = (r.get('CIPCode') or '').strip().lstrip('=').strip('"')
        if re.fullmatch(r'\d\d', code): out[code] = (r.get('CIPTitle') or '').strip()
    return out


def labels():
    p = ROOT / 'baseline/reference/ipeds_labels.json'
    return json.loads(p.read_text()) if p.exists() else {'variables': {}, 'codes': {}}


def survey_gap(t, uid, survey):
    """Why a survey has no value for a school, from FLAGS2023: reported with a parent campus, or no response."""
    f = t['FLAGS'].get(uid) or {}
    if f.get('PRCH_' + survey) == '2':
        return 'not_published_or_na', f"reported with its parent campus (IPEDS unitid {f.get('IDX_' + survey)}); NCES publishes no separate figure"
    if f.get('STAT_' + survey) == '-2':
        return 'not_published_or_na', f'the IPEDS {survey} survey does not apply to this school (FLAGS2023 STAT_{survey} -2)'
    if f.get('STAT_' + survey) == '5':
        return 'not_researched', f'did not respond to the IPEDS {survey} survey (not imputed)'
    return None


def evaluate(uid, t, L):
    """(values, statuses, reasons) for one school."""
    v, st, why = {}, {}, {}
    hd = t['HD2023'].get(uid)

    def put(key, status, reason=''):
        st[key], why[key] = status, reason

    # Identity. Current when the 2024-25 directory (provisional) still lists it active under the same name.
    if hd:
        v.update(name=hd['INSTNM'], city=hd['CITY'], state=hd['STABBR'], website_url=hd['WEBADDR'],
                 control=CONTROL.get(hd['CONTROL']), level={'1': 'four_year', '2': 'two_year', '3': 'less_than_two_year'}.get(hd['ICLEVEL']),
                 highest_offering=L['codes'].get('HD2023.HLOFFER', {}).get(hd['HLOFFER'], hd['HLOFFER']))
        h24 = t['HD2024'].get(uid)
        if h24 is None:
            v['closed_per_hd2024'] = 'absent_from_hd2024'
            put('identity', 'available_older', 'not in the 2024-25 IPEDS directory (HD2024): check for closure or merger')
        elif h24.get('CYACTIVE') != '1':
            closed = h24.get('CLOSEDAT') if h24.get('CLOSEDAT') not in (None, '', '-2') else None
            v['closed_per_hd2024'] = closed or 'inactive'
            put('identity', 'available_older', f"HD2024 lists it inactive (CYACTIVE {h24.get('CYACTIVE')}" + (f', closed {closed})' if closed else ')'))
        else:
            web = lambda x: re.sub(r'^(https?://)?(www\.)?', '', (x or '').strip().lower()).rstrip('/')
            diff = [label for label, var, norm in [('name', 'INSTNM', str), ('city', 'CITY', str), ('website', 'WEBADDR', web),
                                                   ('level', 'ICLEVEL', str), ('control', 'CONTROL', str), ('highest offering', 'HLOFFER', str)]
                    if norm(h24.get(var)) != norm(hd.get(var))]
            if diff:
                put('identity', 'available_older', 'HD2024 (provisional) differs: ' + '; '.join(
                    f"{label} {h24.get(var)!r}" for label, var in [('name', 'INSTNM'), ('city', 'CITY'), ('website', 'WEBADDR'),
                    ('level', 'ICLEVEL'), ('control', 'CONTROL'), ('highest offering', 'HLOFFER')] if label in diff))
            else:
                put('identity', 'verified_current', 'HD2023, and HD2024 (provisional) lists the same name, city, website, level, '
                                                    'control and highest offering')
    else:
        put('identity', 'not_researched', 'no HD2023 record')

    cur = {f['key']: latest(f) for f in FIELDS}
    stat = lambda k: 'verified_current' if cur[k] else 'available_older'
    cur_note = lambda k: f'latest NCES release: the next year\'s file was not served (HTTP 404) on {cur[k]}' if cur[k] else ''

    # Undergraduate enrollment: DRVEF totals, unless NCES imputed the all-undergraduate line.
    d = t['DRVEF2023'].get(uid); a = t['EF2023A_UG'].get(uid)
    ug = num(d, 'EFUG', flagged=False)
    if ug is not None and a is not None and flag(a, 'EFTOTLT') not in REPORTED_OR_ZERO:
        put('undergraduate_enrollment', 'not_researched', f"not a school-reported value (NCES flag {flag(a, 'EFTOTLT')})"); ug = None
    elif ug is not None:
        v.update(undergraduate_enrollment=ug, undergraduate_full_time=num(d, 'EFUGFT', flagged=False),
                 undergraduate_part_time=num(d, 'EFUGPT', flagged=False))
        put('undergraduate_enrollment', stat('undergraduate_enrollment'), cur_note('undergraduate_enrollment'))
    else:
        put('undergraduate_enrollment', *(survey_gap(t, uid, 'EF') or ('not_researched', 'no fall 2023 enrollment record')))

    # Admission rate.
    ic = t['IC2023'].get(uid); adm = t['ADM2023'].get(uid); dadm = t['DRVADM2023'].get(uid)
    openadm = (ic or {}).get('OPENADMP') == '1'
    v['open_admission'] = True if openadm else (False if (ic or {}).get('OPENADMP') == '2' else None)
    apps, admits = num(adm, 'APPLCN'), num(adm, 'ADMSSN')
    rate = num(dadm, 'DVADM01', flagged=False)
    if openadm:
        put('admission_rate', 'not_published_or_na', 'open admission (IC2023 OPENADMP): every applicant is admitted, no selection rate')
    elif rate is not None and apps is not None and admits is not None:
        v.update(admission_rate_percent=rate, applications=apps, admits=admits)
        put('admission_rate', stat('admission_rate'), cur_note('admission_rate'))
    elif adm is not None and apps == 0:
        put('admission_rate', 'not_published_or_na', 'no first-time applications reported (APPLCN 0), so no rate')
    elif adm is not None and (flag(adm, 'APPLCN') not in REPORTED or flag(adm, 'ADMSSN') not in REPORTED):
        put('admission_rate', 'not_researched', f"not a school-reported value (NCES flags {flag(adm, 'APPLCN')}/{flag(adm, 'ADMSSN')})")
    else:
        put('admission_rate', *(survey_gap(t, uid, 'ADM') or ('not_researched', 'no fall 2023 admissions record')))

    # Test scores, with the policy as context.
    pol = (adm or {}).get('ADMCON7')
    v['test_policy'] = L['codes'].get('ADM2023.ADMCON7', {}).get(pol) if pol else None
    scores = {c: num(adm, var) for c, var in [('sat_ebrw_25', 'SATVR25'), ('sat_ebrw_75', 'SATVR75'), ('sat_math_25', 'SATMT25'),
                                               ('sat_math_75', 'SATMT75'), ('act_composite_25', 'ACTCM25'), ('act_composite_75', 'ACTCM75')]}
    vars_ = ['SATVR25', 'SATVR75', 'SATMT25', 'SATMT75', 'ACTCM25', 'ACTCM75']
    withheld = sorted({flag(adm, x) for x in vars_ if (adm or {}).get(x) not in (None, '', '.') and flag(adm, x) not in REPORTED and flag(adm, x)})
    if any(x is not None for x in scores.values()):
        v.update(scores, percent_submitting_sat=num(adm, 'SATPCT'), percent_submitting_act=num(adm, 'ACTPCT'))
        put('test_scores', stat('test_scores'), '; '.join(x for x in [cur_note('test_scores'),
            f'some percentiles withheld: not school-reported (NCES flag {"/".join(withheld)})' if withheld else ''] if x))
    elif openadm:
        put('test_scores', 'not_published_or_na', 'open admission')
    elif pol == '3':
        put('test_scores', 'not_published_or_na', 'test blind: scores not considered (ADM2023 ADMCON7)')
    elif withheld:
        put('test_scores', 'not_researched', f'percentiles not school-reported (NCES flag {"/".join(withheld)})')
    else:
        put('test_scores', *(survey_gap(t, uid, 'ADM') or ('not_researched', 'no scores reported to IPEDS'
                                                           + (f' (policy: {v["test_policy"]})' if v['test_policy'] else ''))))

    # Prices (published, 2023-24: older than the planning year by definition).
    ay = t['IC2023_AY'].get(uid)
    tf = {c: num(ay, var) for c, var in [('in_state_tuition', 'CHG2AT3'), ('in_state_fees', 'CHG2AF3'),
                                          ('out_of_state_tuition', 'CHG3AT3'), ('out_of_state_fees', 'CHG3AF3')]}
    if tf['in_state_tuition'] is not None or tf['out_of_state_tuition'] is not None:
        v.update(tf); put('tuition_fees', 'available_older', f'published for 2023-24; current year is {PLANNING_YEAR}')
    elif ay is not None and flag(ay, 'CHG2AT3') == 'A' and flag(ay, 'CHG3AT3') == 'A':
        put('tuition_fees', 'not_published_or_na', 'NCES: not applicable (flag A), e.g. no tuition charged')
    else:
        put('tuition_fees', 'not_researched', 'no 2023-24 academic-year price record' if ay is None else
            f"not a school-reported value (NCES flags {flag(ay, 'CHG2AT3')}/{flag(ay, 'CHG3AT3')})")
    hf = num(ay, 'CHG5AY3')
    if hf is not None:
        v['on_campus_food_housing'] = hf; put('housing_food', 'available_older', f'published for 2023-24; current year is {PLANNING_YEAR}')
    elif ay is not None and flag(ay, 'CHG5AY3') == 'A':
        put('housing_food', 'not_published_or_na', 'no on-campus housing (NCES: not applicable)')
    else:
        put('housing_food', 'not_researched', 'not reported or imputed' if ay is not None else 'no 2023-24 academic-year price record')
    dic = t['DRVIC2023'].get(uid)
    # Tuition and housing must be reported; books and other expenses may be NCES "not applicable" (A): NCES then sums the rest.
    comp_ok = lambda tu, fe: ay is not None and all(flag(ay, x) in REPORTED_OR_ZERO for x in (tu, fe, 'CHG5AY3')) \
        and all(flag(ay, x) in REPORTED_OR_ZERO | {'A'} for x in ('CHG4AY3', 'CHG6AY3'))
    ok_in, ok_out = comp_ok('CHG2AT3', 'CHG2AF3'), comp_ok('CHG3AT3', 'CHG3AF3')
    cin = num(dic, 'CINSON', flagged=False) if ok_in else None
    cout = num(dic, 'COTSON', flagged=False) if ok_out else None
    if cin is not None or cout is not None:
        v.update(coa_in_state_on_campus=cin, coa_out_of_state_on_campus=cout)
        put('cost_of_attendance', 'available_older', f'NCES total price for 2023-24; current year is {PLANNING_YEAR}')
    elif ay is not None and flag(ay, 'CHG5AY3') == 'A':
        put('cost_of_attendance', 'not_published_or_na', 'no on-campus housing, so no on-campus total')
    else:
        put('cost_of_attendance', 'not_researched', 'a component was imputed or not reported' if dic else 'no NCES total price')

    # Net price (a past year's average for aided students).
    sfa = t['SFA2223'].get(uid)
    public = (hd or {}).get('CONTROL') == '1'
    pre = ('NPIST2', 'NPIS4') if public else ('NPGRN2', 'NPT4')
    avg = num(sfa, pre[0], signed=True)
    if avg is not None:
        v.update(net_price_average=avg, net_price_basis=(
            ('in-state ' if public else '') + 'full-time first-time students awarded grant or scholarship aid (average); '
            'income bands: ' + ('in-state ' if public else '') + 'students awarded Title IV aid (grants or loans)'))
        for i, c in enumerate(['net_price_income_0_30000', 'net_price_income_30001_48000', 'net_price_income_48001_75000',
                               'net_price_income_75001_110000', 'net_price_income_over_110000'], 1):
            v[c] = num(sfa, f'{pre[1]}{i}2', signed=True)
        put('net_price', 'available_older', 'average for the 2022-23 aid year; not a price or an offer')
    elif sfa is not None and flag(sfa, pre[0]) == 'A':
        put('net_price', 'not_published_or_na', 'NCES: not applicable (no full-time first-time aided students)')
    else:
        put('net_price', *(survey_gap(t, uid, 'SFA') or ('not_researched', 'no 2022-23 aid record' if sfa is None
                                                          else (f'NCES analyst-corrected value (flag C), withheld pending review' if flag(sfa, pre[0]) == 'C'
                                                                else f'not a school-reported value (NCES flag {flag(sfa, pre[0])})'))))

    # Retention.
    ef = t['EF2023D'].get(uid)
    ret = num(ef, 'RET_PCF')
    if ret is not None:
        v['retention_rate_full_time'] = ret; put('retention_rate', stat('retention_rate'), cur_note('retention_rate'))
    elif ef is not None and flag(ef, 'RET_PCF') == 'A':
        put('retention_rate', 'not_published_or_na', 'NCES: not applicable (no full-time first-time cohort)')
    else:
        put('retention_rate', *(survey_gap(t, uid, 'EF') or ('not_researched', 'no retention record' if ef is None
                                                             else f'not a school-reported value (NCES flag {flag(ef, "RET_PCF")})')))

    # Graduation rates: derived by NCES from GR2023; withheld if any cohort count was imputed.
    g = t['DRVGR2023'].get(uid); gflags = t['GR_FLAGS'].get(uid, set())
    imputed = gflags - {'R', 'Z', 'A'}
    rates = {'bachelors_grad_rate_4yr': num(g, 'BAGR100', flagged=False), 'bachelors_grad_rate_6yr': num(g, 'BAGR150', flagged=False),
             'grad_rate_overall_150pct': num(g, 'GRRTTOT', flagged=False)}
    if imputed and any(x is not None for x in rates.values()):
        put('graduation_rate', 'not_researched', f'NCES imputed part of the cohort (flags {"/".join(sorted(imputed))})')
    elif any(x is not None for x in rates.values()):
        v.update(rates); put('graduation_rate', stat('graduation_rate'), cur_note('graduation_rate'))
    elif gflags and gflags <= {'A', 'Z'}:
        put('graduation_rate', 'not_published_or_na', 'no first-time full-time cohort to report (NCES: not applicable)')
    else:
        put('graduation_rate', *(survey_gap(t, uid, 'GR') or ('not_researched', 'no graduation-rate record')))

    # Fields and levels.
    c = t['C'].get(uid)
    if c:
        fam = sorted(k for k, lv in c.items() if lv.get('5'))
        levels = sorted({AWARD_LEVELS[l] for lv in c.values() for l in lv if l in AWARD_LEVELS},
                        key=list(AWARD_LEVELS.values()).index)
        v.update(fields_with_bachelors=len(fam), degree_levels_awarded=';'.join(levels))
        put('fields_and_levels', stat('fields_and_levels'), 'C2023_A (final); a newer provisional C2024_A is pinned' if not cur['fields_and_levels'] else '')
    elif uid in t['C_ROWS']:
        v.update(fields_with_bachelors=0, degree_levels_awarded='')
        put('fields_and_levels', stat('fields_and_levels'), 'reported no awards in 2022-23 (CTOTALT 0)')
    else:
        put('fields_and_levels', *(survey_gap(t, uid, 'C') or ('not_researched', 'no 2022-23 completions record')))
    return v, st, why


def build():
    t0 = time.time()
    L = labels()
    t = load_cache()
    reg = registry()
    rows, fos = [], []
    cip = cip_families()
    for i in reg:
        uid = str(i['unitid'])
        v, st, why = evaluate(uid, t, L)
        row = {'institution_key': i['institution_key'], 'unitid': i['unitid'], 'registry_state': i['state'],
               'registry_name': i['name']}
        for f in FIELDS:
            for c in f['columns']: row[c] = v.get(c)
            row[f['key'] + '__status'] = st[f['key']]
            row[f['key'] + '__reason'] = why[f['key']]
        if v.get('closed_per_hd2024'):  # closed, inactive or missing in HD2024: history, never current; reviewed, not complete
            for f in FIELDS:
                if row[f['key'] + '__status'] == 'verified_current':
                    row[f['key'] + '__status'] = 'available_older'
                    row[f['key'] + '__reason'] = f"school {v['closed_per_hd2024'].replace('_', ' ')} per HD2024; " + row[f['key'] + '__reason']
        row['baseline_complete'] = not v.get('closed_per_hd2024') and all(
            row[f['key'] + '__status'] in ('verified_current', 'available_older', 'not_published_or_na') for f in FIELDS)
        rows.append(row)
        for fam, lv in sorted((t['C'].get(uid) or {}).items()):
            fos.append({'institution_key': i['institution_key'], 'unitid': i['unitid'], 'state': i['state'], 'cip_family': fam,
                        'cip_family_title': cip.get(fam), 'associate': lv.get('3') or None, 'bachelor': lv.get('5') or None,
                        'master': lv.get('7') or None,
                        'doctor': (lv.get('17', 0) + lv.get('18', 0) + lv.get('19', 0)) or None})
    return rows, fos, round(time.time() - t0, 1)


def csv_text(rows, cols):
    b = io.StringIO()
    w = csv.DictWriter(b, fieldnames=cols, lineterminator='\n'); w.writeheader()
    for r in rows: w.writerow({k: ('' if r.get(k) is None else r.get(k)) for k in cols})
    return b.getvalue()


def field_doc(L):
    out = []
    for f in FIELDS:
        srcs = []
        for s in f['sources']:
            src = {'file': s['file'] + '.zip', 'source_url': f"https://nces.ed.gov/ipeds/datacenter/data/{s['file']}.zip",
                   'collection_year': YEAR, 'variables': {}}
            if s.get('role'): src['role'] = s['role']
            for var in s['variables']:
                src['variables'][var] = L['variables'].get(s['file'], {}).get(var, {})
            srcs.append(src)
        out.append({k: f[k] for k in ('key', 'label', 'kind', 'period', 'columns') if k in f} |
                   ({'context': f['context']} if f.get('context') else {}) | {'sources': srcs,
                   'current_rule': ('a statistic is verified_current while NCES has not served ' + f['next_file'] + '.zip'
                                    if f.get('next_file') else
                                    f'a price or average for a year before {PLANNING_YEAR} is available_older' if f['kind'] != 'directory'
                                    else 'current while the provisional 2024-25 directory (HD2024) lists it active under the same name')})
    return {'note': 'Field dictionary for baseline/schools. kind: directory, statistic (a measurement NCES reports), '
                    'published_price (a price the school published for that year), historical_average (an average over a past '
                    'year\'s students; never a price, offer or personal estimate). Status codes: ' + ', '.join(STATUSES) + '.',
            'collection_year': YEAR, 'planning_year': PLANNING_YEAR,
            'status_sources': {'HD2024.zip': 'provisional 2024-25 directory: identity check and closures (sources/ipeds/2024-25)',
                               'FLAGS2023.zip': 'survey response status and parent/child reporting (STAT_*, PRCH_*, IDX_*)',
                               'sources/ipeds/2024-25/manifest.json': 'files NCES did not serve (HTTP 404 with check date): '
                                                                     'decides verified_current for statistics'},
            'fields': out}


# ---- policy layer and degree detail: separate measures, read from what research has recorded ----
MERIT_TYPES = {'institutional_merit'}
POLICY_STATUSES = ('verified', 'partially_verified', 'no_published_score_formula', 'candidate_in_run', 'candidates_rejected', 'source_found', 'searched_not_found', 'source_inaccessible',
                   'not_researched')


def policy_status(reg):
    """Per school: merit scholarships, exam credit (AP/IB/CLEP), aid appeals, from data/institutions/<folder>/."""
    from backend.catalog import records
    by_key = collections.defaultdict(lambda: collections.defaultdict(list))
    folder_key = {}
    for p in (ROOT / 'data/institutions').glob('*/institution.json'):
        try: folder_key[p.parent.name] = json.loads(p.read_text())['institution_key']
        except (KeyError, ValueError): pass
    for path, domain, r in records():
        k = r.get('institution_key')
        if not k: continue
        if domain == 'awards' and r.get('award_type') in MERIT_TYPES: by_key[k]['merit'].append(r)
        elif domain == 'credit_policies' and r.get('policy_kind') in ('AP', 'IB', 'CLEP'): by_key[k]['exam_credit'].append(r)
        elif domain == 'appeals': by_key[k]['aid_appeals'].append(r)
    att_p = ROOT / 'baseline/policy/pipeline_attempts.json'
    att = json.loads(att_p.read_text()) if att_p.exists() else {}
    attempts, cands = att.get('schools', {}), att.get('candidates', {})
    topic = {'merit': 'merit_scholarships', 'aid_appeals': 'aid_appeals'}
    mr_p = ROOT / 'baseline/policy/merit_research.json'
    research = json.loads(mr_p.read_text())['schools'] if mr_p.exists() else {}
    out = {}
    for i in reg:
        k = i['institution_key']; s = {}
        for layer in ('merit', 'exam_credit', 'aid_appeals'):
            rs = by_key[k].get(layer, [])
            a = (attempts.get(k) or {})
            tl = ['ap_credit', 'ib_credit', 'clep_credit'] if layer == 'exam_credit' else [topic[layer]]
            seen = [a.get(t, {}).get('status') for t in tl]
            if any(r.get('verification_status') == 'verified' for r in rs): s[layer] = 'verified'
            elif rs: s[layer] = 'partially_verified'
            elif layer == 'merit' and any(f['field'] == 'score_formula' and f['value'] == 'no_published_score_formula'
                                          for f in (research.get(k) or {}).get('findings', [])):
                s[layer] = 'no_published_score_formula'  # the school states there are no fixed criteria (quoted)
            elif sum((cands.get(k) or {}).get(t, {}).get('undecided', 0) for t in tl) :
                s[layer] = 'candidate_in_run'      # extracted in a run, never decided by a reviewer
            elif sum((cands.get(k) or {}).get(t, {}).get('rejected', 0) for t in tl):
                s[layer] = 'candidates_rejected'   # reviewed and rejected (e.g. not a freshman award, wrong table); still to research
            elif any(x in ('source_found', 'candidate_ready', 'candidate_exception', 'verified_current', 'partially_verified_current')
                     for x in seen):
                s[layer] = 'source_found'  # official page found; nothing structured for this topic is pending
            elif 'not_found' in seen: s[layer] = 'searched_not_found'  # crawl found no page; NOT "no policy"
            elif 'fetch_failed' in seen: s[layer] = 'source_inaccessible'
            else: s[layer] = 'not_researched'
            s[layer + '_run'] = next((a[t]['run'] for t in (['ap_credit', 'ib_credit', 'clep_credit'] if layer == 'exam_credit'
                                                             else [topic[layer]]) if t in a), None)
        merit = by_key[k].get('merit', [])
        th = lambda r: r.get('thresholds') if isinstance(r.get('thresholds'), dict) else {}
        # A criterion counts only with a number: structured thresholds, or an ACT/SAT name followed by a score, or a GPA figure.
        score_txt = re.compile(r'\b(?:ACT|SAT)\b[^.;]{0,25}?\b(?:[1-3]\d|[4-9]\d0|1[0-6]\d0)\b')
        gpa_txt = re.compile(r'\b[0-4]\.\d{1,2}\b')
        s['merit_score_linked'] = any(th(r).get('act_min') is not None or th(r).get('sat_min') is not None
                                      or score_txt.search(str(r.get('test_requirement') or '')) for r in merit)
        s['merit_gpa_linked'] = any(th(r).get('gpa_min') is not None or gpa_txt.search(str(r.get('gpa_requirement') or ''))
                                    for r in merit)
        out[k] = s
    return out


def current_prices(reg):
    """Schools with a verified school-published tuition record for the planning year or later (research records, not IPEDS)."""
    from backend.catalog import records
    keys = {i['institution_key'] for i in reg}
    by = collections.defaultdict(set)
    for path, domain, r in records():
        if domain != 'costs' or 'data/national' in str(path) or r.get('institution_key') not in keys: continue
        if r.get('verification_status') == 'verified' and r.get('tuition') is not None and str(r.get('academic_year') or '') >= PLANNING_YEAR:
            by['verified'].add(r['institution_key'])
        elif r.get('tuition') is not None and str(r.get('academic_year') or '') >= PLANNING_YEAR:
            by['partially_verified'].add(r['institution_key'])
    by['partially_verified'] -= by['verified']
    return by


def degree_detail():
    p = ROOT / 'docs/coverage/programs/STATUS.json'
    if not p.exists(): return {}
    d = json.loads(p.read_text())
    n = d.get('national') or {}
    covered, researched = n.get('covered'), n.get('researched')  # Deep Dive's own definitions (STATUS.json national)
    keys = {i.get('institution_key') for s in d.get('states') or [] for i in s.get('institutions', [])
            if str(i.get('status', '')).startswith('covered')}
    return {'covered': covered, 'researched': researched, 'covered_keys': keys}


def report(rows, secs, reg):
    n = len(rows)
    w = lambda r: r.get('undergraduate_enrollment') or 0
    W = sum(w(r) for r in rows)
    per = {}
    for f in FIELDS:
        c = collections.Counter(r[f['key'] + '__status'] for r in rows)
        known = sum(w(r) for r in rows if r[f['key'] + '__status'] in ('verified_current', 'available_older', 'not_published_or_na'))
        per[f['key']] = {'label': f['label'], 'period': f['period'], 'kind': f['kind'],
                         **{s: c.get(s, 0) for s in STATUSES},
                         'resolved_share': round((n - c.get('not_researched', 0) - c.get('blocked', 0)) / n, 4) if n else 0,
                         'enrollment_weighted_resolved_share': round(known / W, 4) if W else 0,
                         'top_reasons_not_researched': collections.Counter(r[f['key'] + '__reason'] for r in rows
                                                                           if r[f['key'] + '__status'] == 'not_researched').most_common(4)}
    complete = [r for r in rows if r['baseline_complete']]
    pol = policy_status(reg)
    pl = {layer: dict(collections.Counter(s[layer] for s in pol.values())) for layer in ('merit', 'exam_credit', 'aid_appeals')}
    _CACHE['policy'] = pol
    pl['merit_score_linked_schools'] = sum(1 for s in pol.values() if s['merit_score_linked'])
    pl['merit_gpa_linked_schools'] = sum(1 for s in pol.values() if s['merit_gpa_linked'])
    mr_p = ROOT / 'baseline/policy/merit_research.json'
    pl['merit_research_findings_schools'] = len(json.loads(mr_p.read_text())['schools']) if mr_p.exists() else 0
    ew = lambda keys: round(sum(w(r) for r in rows if r['institution_key'] in keys) / W, 4) if W else 0
    pl['merit_on_file_enrollment_weighted'] = ew({k for k, s in pol.items() if s['merit'] in ('verified', 'partially_verified')})
    pl['merit_score_linked_enrollment_weighted'] = ew({k for k, s in pol.items() if s['merit_score_linked']})
    dd = degree_detail()
    cp = current_prices(reg)
    cpk = cp['verified']
    by_state = collections.defaultdict(lambda: collections.Counter())
    for r in rows:
        by_state[r['registry_state']]['schools'] += 1
        by_state[r['registry_state']]['complete'] += r['baseline_complete']
    return {
        'source': f'scripts/build_baseline.py over pinned IPEDS {YEAR} files (sources/ipeds/{YEAR}/manifest.json) and the registry',
        'in_scope_schools': n,
        'in_scope_rule': 'Every four-year school in pipeline/registry/<ST>.json (docs/coverage/baseline/UNIVERSE.md)',
        'baseline_complete': len(complete),
        'baseline_complete_rule': 'every essential field is verified_current, available_older or not_published_or_na, and the '
                                  'school is listed active in the provisional 2024-25 directory',
        'baseline_complete_and_all_current': sum(1 for r in rows if all(r[f['key'] + '__status'] in ('verified_current', 'not_published_or_na') for f in FIELDS)),
        'closed_or_inactive_per_hd2024': sum(1 for r in rows if r.get('closed_per_hd2024')),
        'undergraduate_enrollment_total': W,
        'schools_without_enrollment_weight': sum(1 for r in rows if not w(r)),
        'enrollment_weighted_complete_share': round(sum(w(r) for r in complete) / W, 4) if W else 0,
        'fields': per,
        'current_published_tuition': {
            'note': f'Separate from IPEDS: a school-published tuition record for {PLANNING_YEAR} or later in data/institutions, '
                    'verified against the official page (pipeline research). IPEDS tuition stays available_older.',
            'verified_schools': len(cpk), 'partially_verified_schools': len(cp['partially_verified']),
            'enrollment_weighted_verified': round(sum(w(r) for r in rows if r['institution_key'] in cpk) / W, 4) if W else 0},
        'policy_layer': {'note': 'Separate measure. From research records in data/institutions/<folder>/ (awards of type '
                                 'institutional_merit, AP/IB/CLEP credit policies, appeals). not_researched means no record yet, '
                                 'never that the school has no policy.', **pl},
        'degree_detail': {'note': 'Separate measure, owned by Deep Dive (docs/coverage/programs/STATUS.json); never a condition '
                                  'of baseline coverage.', 'covered_schools': dd.get('covered'), 'researched_schools': dd.get('researched')},
        'build_seconds': secs,
        'by_state': {s: dict(c) for s, c in sorted(by_state.items())},
    }


def markdown(rep):
    L = [f"# National school baseline: completeness ({YEAR} IPEDS collection)", '',
         f"Generated by `python3 scripts/build_baseline.py`. Rows: `baseline/schools/{YEAR}/<ST>.csv`; field definitions: "
         "`baseline/FIELDS.json`; universe: `docs/coverage/baseline/UNIVERSE.md`.", '',
         f"- **In-scope schools: {rep['in_scope_schools']:,}** ({rep['in_scope_rule']}).",
         f"- **Complete baseline: {rep['baseline_complete']:,}** ({rep['baseline_complete_rule']}); "
         f"{rep['baseline_complete_and_all_current']:,} with every field current or not applicable.",
         f"- **Closed, inactive or missing in the provisional 2024-25 directory: {rep['closed_or_inactive_per_hd2024']}** (still listed and "
         "flagged in `UNIVERSE.md`; never counted complete or current).",
         f"- **Enrollment-weighted:** {rep['enrollment_weighted_complete_share']:.1%} of {rep['undergraduate_enrollment_total']:,} "
         f"undergraduates (fall 2023) attend a school with a complete baseline; {rep['schools_without_enrollment_weight']} schools "
         "have no reported enrollment and weigh zero.",
         "- A complete baseline is historical official data for comparison. IPEDS prices are 2023-24 and net prices are "
         f"2022-23 averages, so they are `available_older`, never current {PLANNING_YEAR} prices or personal estimates.", '',
         '## Per field', '',
         '| Field | Period | Current | Older | N/A or not published | Not researched | Blocked | Resolved | Enrollment-weighted |',
         '|---|---|---|---|---|---|---|---|---|']
    for k, f in rep['fields'].items():
        L.append(f"| {f['label']} | {f['period']} | {f['verified_current']:,} | {f['available_older']:,} | {f['not_published_or_na']:,} | "
                 f"{f['not_researched']:,} | {f['blocked']:,} | {f['resolved_share']:.1%} | {f['enrollment_weighted_resolved_share']:.1%} |")
    c = rep['current_published_tuition']
    L += ['', f"**Current published tuition ({PLANNING_YEAR} or later, school's own page):** {c['verified_schools']:,} schools verified, "
          f"{c['partially_verified_schools']:,} partially verified; {c['enrollment_weighted_verified']:.1%} of undergraduates. {c['note']}"]
    L += ['', 'Most common reasons a field is not researched:', '']
    for k, f in rep['fields'].items():
        if f['top_reasons_not_researched']:
            L.append(f"- **{f['label']}:** " + '; '.join(f'{why} ({n})' for why, n in f['top_reasons_not_researched']))
    p = rep['policy_layer']
    L += ['', '## Policy layer (separate measure)', '', p['note'], '',
          'Statuses: verified / partially verified (records in the repository); candidate never reviewed (extracted in a run, no decision yet); '
          'candidates rejected (a reviewer rejected what a run extracted); source found (official page found, nothing structured yet); searched, not found (the crawl found no page: '
          'never "no policy"); source inaccessible (fetch failed or blocked); not researched.', '',
          '| Policy | Verified | Partially verified | No published score formula (stated) | Candidate never reviewed | Candidates rejected in review | Source found | Searched, not found | Inaccessible | Not researched |',
          '|---|---|---|---|---|---|---|---|---|---|']
    for layer, label in [('merit', 'Freshman merit scholarships'), ('exam_credit', 'AP/IB/CLEP credit'), ('aid_appeals', 'Aid appeals')]:
        c = p[layer]
        L.append(f"| {label} | " + ' | '.join(f"{c.get(x, 0):,}" for x in POLICY_STATUSES) + ' |')
    L += ['', f"- Schools with a merit record that states an ACT/SAT criterion: {p['merit_score_linked_schools']:,}; a GPA criterion: "
          f"{p['merit_gpa_linked_schools']:,}.",
          f"- Schools with reviewed statements on how merit is awarded (no fixed criteria, superscoring, test-optional rules; "
          f"`baseline/policy/merit_research.json`): {p['merit_research_findings_schools']}.",
          f"- Merit records on file (verified or partially verified), enrollment-weighted: {p['merit_on_file_enrollment_weighted']:.1%}; "
          f"with an ACT/SAT criterion: {p['merit_score_linked_enrollment_weighted']:.1%}.", '',
          '## Degree detail (separate measure, Deep Dive)', '', rep['degree_detail']['note'], '',
          f"- Covered schools: {rep['degree_detail']['covered_schools']}; researched: {rep['degree_detail']['researched_schools']}.", '',
          '## By state', '', '| State | Schools | Complete baseline |', '|---|---|---|']
    for s, c in rep['by_state'].items():
        L.append(f"| {s} | {c['schools']} | {c.get('complete', 0)} |")
    return '\n'.join(L) + '\n'


def universe(t, reg):
    """In-scope universe: the registry's four-year schools, reconciled against IPEDS HD2023 and the provisional HD2024."""
    rec = json.loads((ROOT / 'docs/coverage/registry_reconciliation.json').read_text())
    by_uid = collections.Counter(str(i['unitid']) for i in reg)
    by_key = collections.Counter(i['institution_key'] for i in reg)
    hd, h24, fl = t['HD2023'], t['HD2024'], t['FLAGS']
    changes = []
    for i in reg:
        u = str(i['unitid']); a = hd.get(u); b = h24.get(u)
        if b is None: kind = 'absent_from_hd2024'
        elif b.get('CYACTIVE') != '1': kind = 'inactive_in_hd2024'
        elif a and b.get('INSTNM') != a.get('INSTNM'): kind = 'renamed_in_hd2024'
        else: continue
        changes.append({'institution_key': i['institution_key'], 'unitid': i['unitid'], 'state': i['state'], 'name_2023': (a or {}).get('INSTNM'),
                        'change': kind, 'name_2024': (b or {}).get('INSTNM'), 'cyactive_2024': (b or {}).get('CYACTIVE'),
                        'closed_2024': (b or {}).get('CLOSEDAT') if (b or {}).get('CLOSEDAT') not in (None, '', '-2') else None, 'merged_into_unitid': ((b or {}).get('NEWID') or None)
                        if (b or {}).get('NEWID') not in (None, '', '-2') else None})
    reg_uids = set(by_uid)
    new = []
    for u, b in h24.items():
        if u in reg_uids or b.get('STABBR') not in STATES: continue
        if (b.get('CYACTIVE') == '1' and b.get('DEGGRANT') == '1' and b.get('UGOFFER') == '1' and b.get('CONTROL') in {'1', '2'}
                and b.get('ICLEVEL') == '1' and b.get('INSTCAT') in {'2', '3'}):
            new.append({'unitid': int(u), 'name': b.get('INSTNM'), 'state': b.get('STABBR'), 'control': CONTROL.get(b.get('CONTROL')),
                        'in_hd2023': u in hd})
    from urllib.parse import urlsplit
    def dom(u):
        u = (u or '').strip().lower()
        host = urlsplit(u if '://' in u else 'https://' + u).netloc.split(':')[0]
        parts = host.removeprefix('www.').split('.')
        return '.'.join(parts[-2:]) if parts and parts[0] else ''
    by_dom = collections.defaultdict(list)
    for i in reg:
        d = dom((hd.get(str(i['unitid'])) or {}).get('WEBADDR'))
        if d: by_dom[d].append(i)
    shared = [{'website_domain': d, 'schools': [{'institution_key': i['institution_key'], 'unitid': i['unitid'], 'name': i['name']}
                                                 for i in sorted(v, key=lambda x: x['unitid'])]}
              for d, v in sorted(by_dom.items()) if len(v) > 1]
    children = []
    for i in reg:
        f = fl.get(str(i['unitid'])) or {}
        surveys = [s for s in ('EF', 'SFA', 'C', 'GR', 'ADM') if f.get('PRCH_' + s) == '2']
        if surveys:
            children.append({'institution_key': i['institution_key'], 'unitid': i['unitid'], 'state': i['state'],
                             'name': i['name'], 'reported_with_parent': {s: f.get('IDX_' + s) for s in surveys}})
    return {
        'in_scope_rule': 'pipeline/registry.py in_scope, four-year: active (CYACTIVE 1), degree-granting, offers undergraduate '
                         'instruction, public or private nonprofit, ICLEVEL 1, and either a 2023-24 first-time admissions/price record '
                         'or an undergraduate-degree institutional category (INSTCAT 2 or 3). Stable identifier: institution_key '
                         '(a curated folder key, otherwise ipeds-<UNITID>), with the IPEDS UNITID alongside.',
        'in_scope_schools': len(reg),
        'ipeds_four_year_universe': rec['national_four_year_universe'],
        'excluded_from_universe_by_reason': rec['excluded_by_reason'],
        'in_scope_outside_title_iv_universe': rec['registered_outside_universe'],
        'duplicate_unitids': sorted(u for u, n in by_uid.items() if n > 1),
        'duplicate_institution_keys': sorted(k for k, n in by_key.items() if n > 1),
        'changes_in_hd2024': changes,
        'hd2024_candidates_not_in_scope_list': sorted(new, key=lambda x: (x['state'], x['name'])),
        'campuses_reported_with_parent': children,
        'schools_sharing_a_website_domain': shared,
        'shared_domain_note': 'Separate IPEDS units (own UNITID and IPEDS reporting) that publish under one website domain: '
                              'branch campuses, online or adult divisions, systems. Each stays its own row; research of '
                              'school-specific policy must check which unit a page covers.',
        'note': 'HD2024 is NCES\'s provisional 2024-25 directory. A school absent, inactive or renamed there is flagged for review, '
                'never removed or renamed automatically; a candidate is added to the registry only by a reviewed change.',
    }


def universe_md(u):
    L = ['# In-scope school universe', '', 'Generated by `python3 scripts/build_baseline.py` (data: `universe.json`).', '',
         f"- **In scope: {u['in_scope_schools']:,} schools.** {u['in_scope_rule']}",
         f"- IPEDS degree-granting four-year universe (Title IV, 50 states and D.C.): {u['ipeds_four_year_universe']:,}. Not in scope: "
         + ', '.join(f'{k.replace("_", " ")} {n}' for k, n in u['excluded_from_universe_by_reason'].items())
         + f" (docs/coverage/registry_reconciliation.md). In scope but outside the Title IV universe: {len(u['in_scope_outside_title_iv_universe'])} "
         "(UNITIDs in `universe.json`).",
         f"- Duplicate UNITIDs: {len(u['duplicate_unitids'])}; duplicate institution keys: {len(u['duplicate_institution_keys'])}.",
         f"- Campuses whose IPEDS data are reported with a parent campus: {len(u['campuses_reported_with_parent'])} (their figures for "
         'those surveys are `not_published_or_na`, with the parent named).',
         f"- Website domains shared by more than one in-scope school: {len(u['schools_sharing_a_website_domain'])} "
         f"({sum(len(g['schools']) for g in u['schools_sharing_a_website_domain'])} schools). {u['shared_domain_note']}",
         f"- {u['note']}", '',
         f"## Changes in the provisional 2024-25 directory ({len(u['changes_in_hd2024'])})", '',
         '| School | State | Change | 2024-25 name | Closed | Merged into |', '|---|---|---|---|---|---|']
    for c in u['changes_in_hd2024']:
        L.append(f"| {c['name_2023']} (`{c['institution_key']}`) | {c['state']} | {c['change'].replace('_', ' ')} | {c['name_2024'] or ''} | "
                 f"{c['closed_2024'] or ''} | {c['merged_into_unitid'] or ''} |")
    L += ['', f"## New in the 2024-25 directory and meeting the four-year scope rule ({len(u['hd2024_candidates_not_in_scope_list'])})", '',
          'Candidates for a reviewed registry addition (the admissions/price arm of the rule needs 2024-25 files NCES has not served yet).', '',
          '| School | State | Control | In HD2023 |', '|---|---|---|---|']
    for c in u['hd2024_candidates_not_in_scope_list']:
        L.append(f"| {c['name']} ({c['unitid']}) | {c['state']} | {c['control']} | {'yes' if c['in_hd2023'] else 'no'} |")
    L += ['', f"## Schools sharing a website domain ({len(u['schools_sharing_a_website_domain'])} domains)", '',
          '| Domain | Schools |', '|---|---|']
    for g in u['schools_sharing_a_website_domain']:
        L.append(f"| {g['website_domain']} | " + '; '.join(f"{x['name']} ({x['unitid']})" for x in g['schools']) + ' |')
    return '\n'.join(L) + '\n'


def outputs():
    rows, fos, secs = build()
    L = labels()
    reg = registry()
    rep = report(rows, secs, reg)
    files = {}
    cols = ['institution_key', 'unitid', 'registry_state', 'registry_name'] + \
           [c for f in FIELDS for c in f['columns'] + [f['key'] + '__status', f['key'] + '__reason']] + ['baseline_complete']
    for s in sorted({r['registry_state'] for r in rows}):
        files[f'baseline/schools/{YEAR}/{s}.csv'] = csv_text([r for r in rows if r['registry_state'] == s], cols)
    fcols = ['institution_key', 'unitid', 'state', 'cip_family', 'cip_family_title', 'associate', 'bachelor', 'master', 'doctor']
    for s in sorted({r['state'] for r in fos}):
        files[f'baseline/fields_of_study/{YEAR}/{s}.csv'] = csv_text([r for r in fos if r['state'] == s], fcols)
    files['baseline/FIELDS.json'] = json.dumps(field_doc(L), indent=1, ensure_ascii=False) + '\n'
    stable = {k: v for k, v in rep.items() if k != 'build_seconds'}
    files['docs/coverage/baseline/completeness.json'] = json.dumps(stable, indent=1, ensure_ascii=False) + '\n'
    files['docs/coverage/baseline/COMPLETENESS.md'] = markdown(rep)
    pol = _CACHE['policy']
    q = sorted(rows, key=lambda r: (-(r.get('undergraduate_enrollment') or 0), r['institution_key']))
    qrows = [{'rank': n, 'institution_key': r['institution_key'], 'unitid': r['unitid'], 'state': r['registry_state'],
              'name': r['registry_name'], 'undergraduate_enrollment': r.get('undergraduate_enrollment'),
              'merit_status': pol[r['institution_key']]['merit'], 'merit_run': pol[r['institution_key']]['merit_run'],
              'score_linked_on_file': pol[r['institution_key']]['merit_score_linked'],
              'exam_credit_status': pol[r['institution_key']]['exam_credit'], 'aid_appeals_status': pol[r['institution_key']]['aid_appeals']}
             for n, r in enumerate(q, 1)]
    files['docs/coverage/baseline/policy_queue.csv'] = csv_text(qrows, list(qrows[0]))
    u = universe(load_cache(), reg)
    files['docs/coverage/baseline/universe.json'] = json.dumps(u, indent=1, ensure_ascii=False) + '\n'
    files['docs/coverage/baseline/UNIVERSE.md'] = universe_md(u)
    return files, secs


def main():
    check = '--check' in sys.argv
    files, secs = outputs()
    stale = [p for p, text in files.items() if not (ROOT / p).exists() or (ROOT / p).read_text() != text]
    if check:
        # completeness.* also counts research records (policy layer) and Deep Dive's STATUS.json, which other PRs change;
        # they are regenerated at checkpoints, so only the IPEDS-derived files are enforced here.
        stale = [p for p in stale if not p.startswith('docs/coverage/baseline/completeness') and not p.endswith('COMPLETENESS.md')
                 and not p.endswith('policy_queue.csv')]
        if stale: print('stale baseline files (run python3 scripts/build_baseline.py):', *stale[:10], sep='\n  '); return 1
        print(f'Baseline current ({len(files)} files)'); return 0
    for p, text in files.items():
        (ROOT / p).parent.mkdir(parents=True, exist_ok=True); (ROOT / p).write_text(text)
    rep = json.loads(files['docs/coverage/baseline/completeness.json'])
    print(f"{rep['in_scope_schools']} in scope, {rep['baseline_complete']} complete baseline, "
          f"{rep['enrollment_weighted_complete_share']:.1%} enrollment-weighted; built in {secs}s; {len(stale)} files changed")
    return 0


if __name__ == '__main__':
    sys.path.insert(0, str(ROOT))
    sys.exit(main())
