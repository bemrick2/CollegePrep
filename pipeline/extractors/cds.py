"""Common Data Set (sections C1 and C9) -> admissions_metrics candidates.

The CDS is a standard survey, so its wording is stable across institutions. Applicant counts are
taken only from explicit total lines (never summed from the men/women/gender rows). Test-score
percentiles must sit in their scale's range and be non-decreasing, or they are dropped and flagged.
"""
from __future__ import annotations
import re

from . import common

EXTRACTOR = 'common_data_set/v1'
CDS_YEAR = re.compile(r'common\s+data\s+set\s+(20\d{2})\s*[-–/]\s*(20)?(\d{2})', re.I)
_FTFY = r'total\s+first-time,?\s+first-year\s+(\((freshman|degree-seeking)\)\s+)?(students\s+)?'
TOTALS = {
    'applications': re.compile(r'(?:^|\s)(' + _FTFY + r'who\s+applied|total\s+applied)\b', re.I),
    'admits': re.compile(r'(?:^|\s)(' + _FTFY + r'who\s+were\s+admitted|total\s+admitted)\b', re.I),
    'enrolled': re.compile(r'(?:^|\s)(' + _FTFY + r'(who\s+)?enrolled|total\s+enrolled)\b', re.I),
}
SCORES = {  # field prefix: (label pattern, low, high)
    'sat_composite': (r'^\s*sat\s+composite\b', 400, 1600),
    'sat_reading': (r'^\s*sat\s+evidence-based\s+reading', 200, 800),
    'sat_math': (r'^\s*sat\s+math\b', 200, 800),
    'act': (r'^\s*act\s+composite\b', 1, 36),
}
GENDER = re.compile(r'\b(men|women|males?|females?|gender|sex)\b', re.I)


def _numbers_after(line, pattern):
    m = re.search(pattern, line, re.I)
    if not m: return []
    tail = line[m.end():]
    return [int(x.replace(',', '')) for x in re.findall(r'(?<![\d.])(\d{1,3}(?:,\d{3})+|\d+)(?![\d.%])', tail)]


def joined_lines(text):
    """Layout lines with wrapped labels re-joined: a label line with no numbers is merged into the
    next line when that line continues the label ('who enrolled', 'Writing')."""
    raw = [l.rstrip() for l in text.splitlines() if l.strip()]
    out, i = [], 0
    label = re.compile(r'(total\s+first-time|sat\s+evidence)', re.I)
    while i < len(raw):
        line = raw[i]
        nxt = raw[i + 1] if i + 1 < len(raw) else ''
        if label.search(line) and not re.search(r'\d{2}', line.split('first-year')[-1]):
            if re.match(r'\s*(who\s|writing\b|and\s+writing\b)', nxt, re.I):
                out.append(line + ' ' + nxt.strip()); i += 2; continue
            # Column headers printed on the label line, numbers on the next line.
            if re.fullmatch(r'[\s\d,]+', nxt) and len(re.findall(r'\d[\d,]*', nxt)) >= 1:
                m = re.match(r'^.*?(who\s+applied|who\s+were\s+admitted|enrolled|writing)\b', line, re.I)
                out.append((m.group(0) if m else line) + '   ' + nxt.strip())
                i += 2; continue
        out.append(line); i += 1
    return out


def total_from(nums):
    """(value, parts, reconciles). One printed number, or a residency breakdown whose last column is
    the printed Total (CDS template). A total that differs from its printed parts is still the
    printed value, but the candidate goes to the exception queue."""
    if len(nums) == 1: return nums[0], None, True
    if len(nums) >= 3: return nums[-1], nums[:-1], nums[-1] == sum(nums[:-1])
    return None, None, False


def extract(inst, entry, page, today_year):
    head = page.text[:4000]
    m = CDS_YEAR.search(page.title + '\n' + head)
    if not m or not re.search(r'first-time,?\s+first-year', page.text, re.I):
        return []
    first = int(m.group(1)); second = int((m.group(2) or str(first)[:2]) + m.group(3))
    if second != first + 1: return []
    year = f'{first}-{str(second)[-2:]}'
    record, evidence, issues = {'entering_fall_year': first, 'applicant_population': 'first_time_first_year_degree_seeking'}, [], []
    lines = joined_lines(page.text)
    for line in lines:
        if GENDER.search(line) or re.search(r'part-time|full-time', line, re.I): continue
        for field, rx in TOTALS.items():
            if field in record: continue
            if rx.search(line):
                nums = _numbers_after(line, rx.pattern)
                value, parts, ok = total_from(nums)
                if value is not None:
                    record[field] = value
                    evidence.append({'field': field, 'value': value, 'snippet': line.strip()[:240],
                                     **({'breakdown_reconciles': ok} if parts else {})})
                    if not ok: issues.append(f'{field}_breakdown_does_not_reconcile')
                elif nums:
                    issues.append(f'{field}_unreadable_columns')
    for prefix, (pattern, lo, hi) in SCORES.items():
        for line in lines:
            if not re.search(pattern, line, re.I): continue
            nums = [n for n in _numbers_after(line, pattern)]
            if len(nums) not in (2, 3): continue
            if not all(lo <= n <= hi for n in nums) or nums != sorted(nums):
                issues.append(f'{prefix}_implausible'); break
            names = ['25', '50', '75'] if len(nums) == 3 else ['25', '75']
            for n, v in zip(names, nums):
                record[f'{prefix}_{n}'] = v
            evidence.append({'field': f'{prefix}_25..75', 'value': nums, 'snippet': line.strip()[:240]})
            break
    if len(evidence) == 0: return []
    if not all(f in record for f in TOTALS): issues.append('c1_totals_incomplete')
    if any(record.get(f) == 0 for f in TOTALS):
        issues.append('c1_zero_total')  # GA r1: Covenant prints 0 applied/admitted beside 324 enrolled
    if record.get('admits') and record.get('applications') and record['admits'] > record['applications']:
        issues.append('admits_exceed_applications')
    if year < today_year and first < int(today_year[:4]) - 1:
        issues.append(f'stale_year_label:{year}')
    record['notes'] = f'Common Data Set {year} sections C1/C9, extracted by {EXTRACTOR}; totals copied as printed.'
    checks = {'fields': sorted(k for k in record if k not in {'notes', 'applicant_population'})}
    return [common.make('admissions_metrics', inst['institution_key'], year, 'labeled_in_source', record, evidence,
                        entry, EXTRACTOR, {'applicant_population': record['applicant_population']}, checks, issues)]
