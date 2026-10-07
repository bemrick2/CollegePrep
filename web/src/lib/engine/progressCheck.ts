import type { BenchmarkSummary } from '../data/types'

/**
 * Compares a progress check with the baseline and with the previous check, section by section.
 *
 * These are practice questions, not equated test forms: each check draws different items, and sections hold only
 * a handful of answers. So a change is called real only when it is larger than chance would usually produce:
 * more than two standard errors of the difference between two proportions (pooled). Smaller changes are reported
 * as "within normal variation", whatever their sign. A section where either check reused questions the student had
 * seen before gets no verdict at all ("not_clean"). Nothing here is converted to an ACT or SAT score.
 */
export type ChangeVerdict = 'up' | 'down' | 'within_noise' | 'too_few' | 'not_clean'

export interface SectionChange {
  section: string
  now: { correct: number; answered: number; accuracy: number | null }
  then: { correct: number; answered: number; accuracy: number | null } | null
  /** Accuracy points, now minus then. */
  delta: number | null
  verdict: ChangeVerdict
  pacingNow: number | null
  pacingThen: number | null
  /** Questions the student had seen before, in this check / the earlier one. Any repeat: no verdict. */
  repeatsNow: number
  repeatsThen: number
}

/** Fewer answers than this on either side and no change is judged at all. */
export const MIN_ANSWERS = 4

export function judgeChange(now: { correct: number; answered: number }, then: { correct: number; answered: number }): { delta: number | null; verdict: ChangeVerdict } {
  if (now.answered < MIN_ANSWERS || then.answered < MIN_ANSWERS) {
    const d = now.answered && then.answered ? now.correct / now.answered - then.correct / then.answered : null
    return { delta: d, verdict: 'too_few' }
  }
  const p1 = now.correct / now.answered
  const p0 = then.correct / then.answered
  const pooled = (now.correct + then.correct) / (now.answered + then.answered)
  const se = Math.sqrt(pooled * (1 - pooled) * (1 / now.answered + 1 / then.answered))
  const delta = p1 - p0
  if (se === 0) return { delta, verdict: delta === 0 ? 'within_noise' : delta > 0 ? 'up' : 'down' }
  return { delta, verdict: Math.abs(delta) > 2 * se ? (delta > 0 ? 'up' : 'down') : 'within_noise' }
}

export type RepeatsOf = (b: BenchmarkSummary) => Map<string, number>
const noRepeats: RepeatsOf = () => new Map()

function compareTo(current: BenchmarkSummary, other: BenchmarkSummary | null, repeatsOf: RepeatsOf): SectionChange[] {
  const rNow = repeatsOf(current)
  const rThen = other ? repeatsOf(other) : new Map<string, number>()
  return current.metrics.sections.map((s) => {
    const o = other?.metrics.sections.find((x) => x.section === s.section) ?? null
    const now = { correct: s.correct, answered: s.answered, accuracy: s.accuracy }
    const repeatsNow = rNow.get(s.section) ?? 0
    const repeatsThen = rThen.get(s.section) ?? 0
    if (!o) return { section: s.section, now, then: null, delta: null, verdict: 'too_few', pacingNow: s.pacing_ratio, pacingThen: null, repeatsNow, repeatsThen }
    const then = { correct: o.correct, answered: o.answered, accuracy: o.accuracy }
    const judged = judgeChange(now, then)
    // Recall of a question seen before is not new evidence: report the numbers, but no verdict.
    const verdict: ChangeVerdict = repeatsNow > 0 || repeatsThen > 0 ? 'not_clean' : judged.verdict
    return { section: s.section, now, then, delta: judged.delta, verdict, pacingNow: s.pacing_ratio, pacingThen: o.pacing_ratio, repeatsNow, repeatsThen }
  })
}

export interface ProgressComparison {
  baseline: BenchmarkSummary | null
  previous: BenchmarkSummary | null
  sinceBaseline: SectionChange[]
  /** Only when the previous check is not the baseline itself. */
  sinceLast: SectionChange[] | null
}

/** `history` = completed checks before this one (any order). The first by date is the baseline. */
export function compareProgress(current: BenchmarkSummary, history: BenchmarkSummary[], repeatsOf: RepeatsOf = noRepeats): ProgressComparison {
  const prior = history.filter((b) => b.id !== current.id && b.completed_at && b.completed_at <= current.completed_at).sort((a, b) => a.completed_at.localeCompare(b.completed_at))
  const baseline = prior.find((b) => b.kind === 'initial') ?? prior[0] ?? null
  const previous = prior.at(-1) ?? null
  return {
    baseline,
    previous,
    sinceBaseline: baseline ? compareTo(current, baseline, repeatsOf) : [],
    sinceLast: previous && baseline && previous.id !== baseline.id ? compareTo(current, previous, repeatsOf) : null,
  }
}
