/**
 * Merit scholarship test criteria, read from each award's published `test_requirement` text. Awards store the
 * criterion as text only (no numeric column yet: contract request CR-11), so this extracts a single minimum when
 * the text states one plainly ("ACT 30+", "Minimum 31 ACT / 1390 SAT") and returns null for ranges, tiers or
 * anything ambiguous. A null means "read the criteria", never "no test requirement".
 */

export interface TestMinimums {
  act: number | null
  sat: number | null
}

const uniq = (xs: number[]) => [...new Set(xs)]

function single(xs: number[], lo: number, hi: number): number | null {
  const ok = uniq(xs.filter((n) => n >= lo && n <= hi))
  return ok.length === 1 ? ok[0]! : null
}

export function testMinimums(text: string | null | undefined): TestMinimums {
  const t = (text ?? '').replace(/\s+/g, ' ')
  if (!t || /tier|range|\d\s*[-–]\s*\d/i.test(t)) return { act: null, sat: null }
  const act: number[] = []
  const sat: number[] = []
  // "ACT 30+", "ACT of 30+", "ACT composite 30 or higher"
  for (const m of t.matchAll(/\bACT(?:\s+composite)?(?:\s+of)?\s+(\d{2})\s*(?:\+|or (?:higher|above|better))/gi)) act.push(Number(m[1]))
  // "30+ ACT", "Minimum 31 ACT", "minimum of 31 ACT"
  for (const m of t.matchAll(/(?:\bminimum(?:\s+of)?\s+(\d{2})|\b(\d{2})\s*\+)\s*ACT\b/gi)) act.push(Number(m[1] ?? m[2]))
  for (const m of t.matchAll(/\bSAT(?:\s+total)?(?:\s+of)?\s+(\d{3,4})\s*(?:\+|or (?:higher|above|better))/gi)) sat.push(Number(m[1]))
  for (const m of t.matchAll(/(?:\bminimum(?:\s+of)?\s+(\d{3,4})|\b(\d{3,4})\s*\+)\s*SAT\b/gi)) sat.push(Number(m[1] ?? m[2]))
  // "Minimum 31 ACT / 1390 SAT": the SAT figure shares the "minimum".
  for (const m of t.matchAll(/\bminimum(?:\s+of)?\s+\d{2}\s*ACT\s*(?:\/|or)\s*(\d{3,4})\s*SAT\b/gi)) sat.push(Number(m[1]))
  return { act: single(act, 1, 36), sat: single(sat, 400, 1600) }
}

export interface MeritAward {
  name: string
  amountText: string | null
  amountMax: number | null
  min: TestMinimums
  requirementText: string | null
  gpaText: string | null
  sourceUrl: string | null
  renewable: boolean | null
}

interface AwardRecord {
  award_name?: string | null
  award_type?: string | null
  award_amount_text?: string | null
  award_max?: number | null
  test_requirement?: string | null
  gpa_requirement?: string | null
  source_url?: string | null
  renewable?: boolean | null
}

/** Merit awards only (award_type contains "merit"); need-based and access awards are not score thresholds. */
export function meritAwards(records: unknown[] | undefined): MeritAward[] {
  return ((records ?? []) as AwardRecord[])
    .filter((a) => (a.award_type ?? '').includes('merit'))
    .map((a) => ({
      name: a.award_name ?? 'Scholarship',
      amountText: a.award_amount_text ?? null,
      amountMax: a.award_max ?? null,
      min: testMinimums(a.test_requirement),
      requirementText: a.test_requirement ?? null,
      gpaText: a.gpa_requirement && a.gpa_requirement !== 'N/A' ? a.gpa_requirement : null,
      sourceUrl: a.source_url ?? null,
      renewable: a.renewable ?? null,
    }))
}

export interface ReferenceScore {
  value: number
  basis: 'official' | 'self_reported' | 'target'
}

/** The score merit criteria may be compared with: an official score, a labelled self-reported one, or the target.
 *  Practice estimates are never a reference. */
export function referenceScore(
  scores: { exam_family: string; composite: number | null; score_source: string; test_date: string }[],
  exam: 'act' | 'sat',
  target: number | null,
): ReferenceScore | null {
  const s = scores
    .filter((x) => x.exam_family === exam && x.composite != null && (x.score_source === 'official' || x.score_source === 'self_reported'))
    .sort((a, b) => b.test_date.localeCompare(a.test_date))[0]
  if (s) return { value: s.composite!, basis: s.score_source === 'official' ? 'official' : 'self_reported' }
  return target != null ? { value: target, basis: 'target' } : null
}

export const BASIS_LABEL: Record<ReferenceScore['basis'], string> = {
  official: 'official score',
  self_reported: 'self-reported score (unverified)',
  target: 'target',
}
