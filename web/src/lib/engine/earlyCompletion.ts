/**
 * When may the app show a time or dollar saving from credit a student brings?
 *
 * Covering every course in a regular full-time semester (degreeCredit's coveredTerms) is one condition, and it shows
 * credit COVERAGE only. Finishing a term earlier also needs every one of these, from the school's own records:
 *
 *  - prerequisites: the courses left after the covered term can be started without it (their prerequisites are met
 *    by the credit or by earlier terms);
 *  - course_availability: those courses are offered in the terms the student would now take them;
 *  - sequencing: the plan's required order (sequences, cohort courses, co-requisites) allows moving them earlier;
 *  - remaining_requirements: every other graduation requirement (total hours, upper-division and residency hours,
 *    general education, the major's own rules) still fits in the shorter plan.
 *
 * No record on file establishes any of these today, so no saving is ever shown: coverage is shown as coverage, and the
 * saving is withheld with what's missing named. Passing evidence in is the only way to change that, and each item must
 * come from a verified record (never a guess or a default).
 */
export type CompletionCondition = 'prerequisites' | 'course_availability' | 'sequencing' | 'remaining_requirements'

export const COMPLETION_CONDITIONS: CompletionCondition[] = ['prerequisites', 'course_availability', 'sequencing', 'remaining_requirements']

export const CONDITION_TEXT: Record<CompletionCondition, string> = {
  prerequisites: 'the later courses’ prerequisites are met without that term',
  course_availability: 'those courses are offered in the terms the student would take them',
  sequencing: 'the plan’s required course order allows taking them sooner',
  remaining_requirements: 'every other graduation requirement still fits in fewer terms',
}

/**
 * One condition, shown by a verified record for this school's plan and these covered terms. Anything less
 * (unverified, inferred, assumed, another school or plan, other terms) doesn't count.
 */
export interface ConditionEvidence {
  verified: true
  sourceUrl: string
  institutionKey: string
  planKey: string
  /** The covered plan terms (term_index) this record shows can be skipped. */
  terms: number[]
}

export type CompletionEvidence = Partial<Record<CompletionCondition, ConditionEvidence>>

/** Which school, plan and covered terms a saving would be for. */
export interface CompletionScope {
  institutionKey: string
  planKey: string | null
  terms: number[]
}

export interface EarlyCompletion {
  /** True only when whole terms are covered AND every condition is shown by a verified record. */
  supported: boolean
  /** Conditions not shown, in order. Empty only when supported. */
  missing: CompletionCondition[]
}

const isUrl = (u: unknown) => typeof u === 'string' && /^https?:\/\/\S+\.\S+/.test(u.trim())

export function earlyCompletion(coveredTerms: number, evidence: CompletionEvidence = {}, scope?: CompletionScope): EarlyCompletion {
  const shows = (e: ConditionEvidence | undefined) =>
    !!e &&
    e.verified === true &&
    isUrl(e.sourceUrl) &&
    !!scope &&
    e.institutionKey === scope.institutionKey &&
    typeof scope.planKey === 'string' &&
    scope.planKey !== '' &&
    e.planKey === scope.planKey &&
    scope.terms.length === coveredTerms &&
    Array.isArray(e.terms) &&
    scope.terms.every((t) => e.terms.includes(t))
  const missing = COMPLETION_CONDITIONS.filter((c) => !shows(evidence[c]))
  return { supported: coveredTerms > 0 && missing.length === 0, missing }
}

/**
 * The one gate every screen uses for a time or dollar saving (#253): `compute` runs only when early completion is
 * supported, so a screen can't show a saving on coverage alone.
 */
export function gatedSaving<T>(coveredTerms: number, compute: () => T | null, evidence: CompletionEvidence = {}, scope?: CompletionScope): { early: EarlyCompletion; saving: T | null } {
  const early = earlyCompletion(coveredTerms, evidence, scope)
  return { early, saving: early.supported ? compute() : null }
}

/** "Not shown: …" in plain words, for a withheld saving. */
export function withheldReason(e: EarlyCompletion, coveredTerms: number): string {
  if (coveredTerms === 0) return 'No whole plan term is covered, so no time or money saved is shown.'
  if (coveredTerms < 0) return 'No verified plan for a saved major is on file, so no time or money saved is shown.'
  return `Covering a term’s courses doesn’t by itself mean finishing a term sooner. That also needs records showing that ${e.missing.map((c) => CONDITION_TEXT[c]).join('; ')}. None of that is on file, so no time or money saved is shown.`
}
