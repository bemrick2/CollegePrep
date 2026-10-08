/**
 * Exam credit matching against each school's verified, published equivalency table (credit_equivalencies, returned
 * inside compare_institutions credit_policies). Pure functions; no credit is inferred beyond what a table lists.
 *
 * Exam codes are not normalized across schools yet ("AP-CALCAB" vs "AP-CALCULUS-AB"), so exams are matched on a
 * normalized name until the backend publishes a canonical exam key (contract request CR-10).
 *
 * Families (#197): AP, CLEP, IB (subject + SL/HL level + score 1-7) and Tennessee Statewide Dual Credit (SDC, exam
 * percentage). A minimum the table prints in words ("PENDING", "See details below", "SL & HL" with no score) is
 * "read the criteria", never "no credit": only N/A, none and no credit mean no credit.
 */

export type ExamFamily = 'AP' | 'CLEP' | 'IB' | 'SDC'
export const EXAM_FAMILIES: ExamFamily[] = ['AP', 'CLEP', 'IB', 'SDC']
export const FAMILY_LABEL: Record<ExamFamily, string> = { AP: 'AP', CLEP: 'CLEP', IB: 'IB', SDC: 'Statewide Dual Credit' }
/** The policy_kind each family's table is stored under. */
const POLICY_KIND: Record<ExamFamily, string> = { AP: 'AP', CLEP: 'CLEP', IB: 'IB', SDC: 'statewide_dual_credit' }
export const policyKindOf = (f: ExamFamily): string => POLICY_KIND[f]
export type IbLevel = 'SL' | 'HL'

export interface Equivalency {
  exam_or_course_code: string
  exam_or_course_name?: string | null
  minimum_score?: string | null
  institution_course_equivalent?: string | null
  credits_awarded?: number | null
  applies_to_gen_ed?: boolean | null
  applies_to_major?: boolean | null
  notes?: string | null
}

export interface CreditPolicy {
  policy_kind: string
  policy_url?: string | null
  source_url?: string | null
  last_verified_at?: string | null
  equivalency_count?: number | null
  equivalencies?: Equivalency[]
}

/** A student's exam: taken (with a score) or planned (score null). */
export interface PlannedExam {
  family: ExamFamily
  key: string
  name: string
  score: number | null
  /** IB only: the level the student takes. Null until chosen; a level-specific row never matches an unknown level. */
  level?: IbLevel | null
}

const ALIASES: Record<string, string> = {
  'american history': 'united states history',
  'us history': 'united states history',
  'u s history': 'united states history',
  'world history': 'world history modern',
  'us government and politics': 'united states government and politics',
}

const PREFIX = /^\s*(ap|clep|ib|statewide dual credit|sdc)\b/
/** IB level tags printed in names: "(HL)", "(SL or HL)", "SL", "HL Only". */
const LEVEL_TAG = /\(?\b(sl|hl)(\s*(or|and|&|\/)\s*(sl|hl))?(\s*only)?\b\)?/g

/** Normalized exam identity: family + name without prefix, IB level, punctuation or "&". */
export function examKey(family: ExamFamily, name: string): string {
  let n = name.toLowerCase().replace(PREFIX, '')
  if (family === 'IB') n = n.replace(LEVEL_TAG, ' ')
  n = n
    .replace(/&/g, ' and ')
    .replace(/[^a-z0-9]+/g, ' ')
    .trim()
  n = ALIASES[n] ?? n
  return `${family}:${n}`
}

export function displayName(family: ExamFamily, name: string): string {
  let n = name.trim()
  if (family === 'IB') n = n.replace(/\s*\((SL|HL)(\s*(or|and|&|\/)\s*(SL|HL))?(\s*only)?\)/gi, '').trim()
  const label = FAMILY_LABEL[family]
  return n.toUpperCase().startsWith(label.toUpperCase()) ? n : `${label} ${n}`
}

/** IB levels a row applies to, from its name or minimum ("IB Biology (HL)", "HL 5", "4+ SL"); null = any level. */
export function rowLevels(name: string | null | undefined, minimum: string | null | undefined): IbLevel[] | null {
  const found = new Set<IbLevel>()
  for (const m of `${name ?? ''} ${minimum ?? ''}`.toUpperCase().matchAll(/\b(SL|HL)\b/g)) found.add(m[1] as IbLevel)
  return found.size ? [...found] : null
}

const NO_CREDIT = /^\s*(n\/?a|none|no credit|not accepted|not awarded)\s*$/i

/** Lowest score a published minimum accepts: "4 or 5" -> 4, "3, 4, or 5" -> 3, "75%" -> 75. Null when unparseable. */
export function minScore(s: string | null | undefined): number | null {
  const nums = (s ?? '').match(/\d+(?:\.\d+)?/g)
  return nums ? Math.min(...nums.map(Number)) : null
}

export function familyOf(kind: string): ExamFamily | null {
  return (Object.keys(POLICY_KIND) as ExamFamily[]).find((f) => POLICY_KIND[f] === kind) ?? null
}

/** Exam options offered by the given schools' verified tables, de-duplicated by normalized name. */
export function examOptions(policiesBySchool: CreditPolicy[][]): { family: ExamFamily; key: string; name: string }[] {
  const out = new Map<string, { family: ExamFamily; key: string; name: string }>()
  for (const policies of policiesBySchool)
    for (const p of policies) {
      const family = familyOf(p.policy_kind)
      if (!family) continue
      for (const e of p.equivalencies ?? []) {
        const name = e.exam_or_course_name?.trim()
        if (!name) continue
        const key = examKey(family, name)
        if (!out.has(key)) out.set(key, { family, key, name: displayName(family, name) })
      }
    }
  return [...out.values()].sort((a, b) => a.family.localeCompare(b.family) || a.name.localeCompare(b.name))
}

export interface Threshold {
  min: number | null
  minimumText: string
  course: string | null
  credits: number | null
  notes: string | null
  /** IB: the levels this row applies to; null = any level. */
  levels: IbLevel[] | null
}

/**
 * not_awarded: the table lists the exam but awards no credit at any score ("N/A").
 * read_criteria: the table lists the exam with a minimum printed in words; the student reads the school's page.
 * needs_level: IB rows are level-specific and the student hasn't chosen SL or HL.
 * other_level: IB rows exist only for the other level (e.g. HL only, the student takes SL).
 */
export type MatchStatus =
  | 'qualifies'
  | 'below'
  | 'planned'
  | 'not_awarded'
  | 'read_criteria'
  | 'needs_level'
  | 'other_level'
  | 'not_listed'
  | 'no_table'

export interface ExamMatch {
  exam: PlannedExam
  status: MatchStatus
  /** Every published threshold for this exam at this school, lowest first. */
  thresholds: Threshold[]
  /** Rows at the highest minimum the score meets (several rows can share a minimum, e.g. by admit term). */
  earned: Threshold[]
  /** Lowest published score that earns any credit. */
  lowest: number | null
}

export function matchExam(policies: CreditPolicy[], exam: PlannedExam): ExamMatch {
  const table = policies.find((p) => p.policy_kind === POLICY_KIND[exam.family])
  if (!table || !(table.equivalencies ?? []).length) return { exam, status: 'no_table', thresholds: [], earned: [], lowest: null }
  const all: Threshold[] = (table.equivalencies ?? [])
    .filter((e) => e.exam_or_course_name && examKey(exam.family, e.exam_or_course_name) === exam.key)
    .map((e) => {
      const levels = exam.family === 'IB' ? rowLevels(e.exam_or_course_name, e.minimum_score) : null
      return {
        min: minScore(exam.family === 'IB' ? (e.minimum_score ?? '').replace(/\b(SL|HL)\b/gi, ' ') : e.minimum_score),
        minimumText: e.minimum_score ?? '',
        course: e.institution_course_equivalent ?? null,
        credits: e.credits_awarded ?? null,
        notes: e.notes ?? null,
        levels,
      }
    })
    .sort((a, b) => (a.min ?? 0) - (b.min ?? 0))
  if (!all.length) return { exam, status: 'not_listed', thresholds: all, earned: [], lowest: null }
  // IB: only rows for the student's level (or for any level). With no level chosen, level-specific rows can't be used.
  const thresholds = exam.family === 'IB' ? all.filter((t) => !t.levels || (exam.level != null && t.levels.includes(exam.level))) : all
  if (!thresholds.length) return { exam, status: exam.level == null ? 'needs_level' : 'other_level', thresholds: all, earned: [], lowest: null }
  const scored = thresholds.filter((t) => t.min != null)
  const lowest = scored[0]?.min ?? null
  if (!scored.length)
    return { exam, status: thresholds.every((t) => NO_CREDIT.test(t.minimumText)) ? 'not_awarded' : 'read_criteria', thresholds, earned: [], lowest }
  if (exam.score == null) return { exam, status: 'planned', thresholds, earned: [], lowest }
  const best = Math.max(-1, ...scored.filter((t) => exam.score! >= t.min!).map((t) => t.min!))
  const earned = scored.filter((t) => t.min === best)
  // A row printed in words could be the one that applies: below every numeric minimum is "read the criteria".
  if (!earned.length && thresholds.some((t) => t.min == null && !NO_CREDIT.test(t.minimumText)))
    return { exam, status: 'read_criteria', thresholds, earned, lowest }
  return { exam, status: earned.length ? 'qualifies' : 'below', thresholds, earned, lowest }
}

export interface SchoolCreditSummary {
  matches: ExamMatch[]
  /** Exams whose listed score earns credit per the published table. */
  courses: number
  /** Sum of published credit hours for earned rows; rows without published hours are counted separately. */
  publishedHours: number
  coursesWithoutHours: number
  hasTable: boolean
}

export function summarizeSchool(policies: CreditPolicy[], exams: PlannedExam[]): SchoolCreditSummary {
  const matches = exams.map((e) => matchExam(policies, e))
  // One exam counts once, even when several rows share its minimum; hours only when the table publishes them.
  const hours = matches.filter((m) => m.status === 'qualifies').map((m) => {
    const known = m.earned.map((t) => t.credits).filter((c): c is number => c != null)
    return known.length === m.earned.length ? Math.min(...known) : null
  })
  return {
    matches,
    courses: hours.length,
    publishedHours: hours.reduce<number>((s, h) => s + (h ?? 0), 0),
    coursesWithoutHours: hours.filter((h) => h == null).length,
    hasTable: policies.some((p) => familyOf(p.policy_kind) && (p.equivalencies ?? []).length > 0),
  }
}

/** A full-time semester is conventionally 15 credit hours. Used only to express published hours, never to promise. */
export const HOURS_PER_SEMESTER = 15
