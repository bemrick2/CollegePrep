#!/usr/bin/env python3
"""Copy the NCES dictionary text the national baseline cites into baseline/reference/ipeds_labels.json.

The dictionaries are .xlsx files inside the pinned *_Dict.zip archives (sources/ipeds/<year>/). Reading them needs
openpyxl, so this runs by hand when a pinned file changes; scripts/build_baseline.py then uses the committed JSON with the
standard library only. Every title and definition is copied as NCES prints it, never paraphrased.

  pip install openpyxl && python3 scripts/refresh_baseline_labels.py
"""
from __future__ import annotations
import io, json, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
from build_baseline import FIELDS, pinned_bytes  # noqa: E402

YEAR = '2023-24'


def workbook(name):
    import openpyxl
    with zipfile.ZipFile(io.BytesIO(pinned_bytes(YEAR, name + '_Dict.zip'))) as z:
        x = next(n for n in z.namelist() if n.lower().endswith('.xlsx'))
        return openpyxl.load_workbook(io.BytesIO(z.read(x)), read_only=True)


def sheet_rows(wb, prefix):
    for ws in wb.worksheets:
        t = ws.title.lower()
        if t.startswith(prefix) and not t.endswith('rv'):
            rows = list(ws.iter_rows(values_only=True))
            if rows: yield [str(c or '').strip().lower() for c in rows[0]], rows[1:]


def variables(wb):
    out = {}
    for hdr, rows in sheet_rows(wb, 'varlist'):
        vi, ti = hdr.index('varname'), hdr.index('vartitle')
        for r in rows:
            if r[vi]: out.setdefault(r[vi], {})['title'] = str(r[ti] or '').strip()
    for hdr, rows in sheet_rows(wb, 'description'):
        vi = hdr.index('varname')
        di = next(i for i, h in enumerate(hdr) if h.startswith('longdescription') or h == 'description')
        for r in rows:
            if r[vi] in out: out[r[vi]]['definition'] = re.sub(r'\s+', ' ', str(r[di] or '')).strip()
    return out


def codes(wb, var):
    out = {}
    for hdr, rows in sheet_rows(wb, 'frequencies'):
        vi, ci, li = hdr.index('varname'), hdr.index('codevalue'), hdr.index('valuelabel')
        for r in rows:
            if r[vi] == var: out[str(r[ci]).strip()] = str(r[li] or '').strip()
    return out


def main():
    used = {}
    for f in FIELDS:
        for src in f['sources']:
            used.setdefault(src['file'], set()).update(src['variables'])
    out = {'note': 'Copied from the NCES dictionaries in the pinned *_Dict.zip files; regenerate with '
                   'scripts/refresh_baseline_labels.py. Titles and definitions are as NCES prints them.',
           'academic_year': YEAR, 'variables': {}, 'codes': {}}
    for file, vs in sorted(used.items()):
        wb = workbook(file)
        allv = variables(wb)
        out['variables'][file] = {v: allv[v] for v in sorted(vs) if v in allv}
        missing = sorted(set(vs) - set(allv))
        if missing: raise SystemExit(f'{file}: no dictionary entry for {missing}')
    for file, var in [('ADM2023', 'ADMCON7'), ('IC2023', 'OPENADMP'), ('HD2023', 'HLOFFER'), ('C2023_A', 'AWLEVEL')]:
        out['codes'][f'{file}.{var}'] = codes(workbook(file), var)
    cip = codes(workbook('C2023_A'), 'CIPCODE')
    out['codes']['C2023_A.CIPCODE.family'] = {k: v for k, v in sorted(cip.items()) if re.fullmatch(r'\d\d', k) and k != '99'}
    p = ROOT / 'baseline/reference/ipeds_labels.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n')
    print(f'wrote {p.relative_to(ROOT)}: {sum(len(v) for v in out["variables"].values())} variables, '
          f'{len(out["codes"]["C2023_A.CIPCODE.family"])} CIP families')


if __name__ == '__main__':
    main()
