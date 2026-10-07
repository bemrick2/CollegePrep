import type { BenchmarkSummary } from '../data/types'
import { judgeChange } from './progressCheck'

export interface Verdict {
  tone: 'go' | 'warn' | 'neutral'
  headline: string
  detail: string
}

export interface Counts {
  n: number
  correct: number
}

/** The last two progress checks, and how many of their questions the student had seen before. */
export interface CheckPair {
  from: BenchmarkSummary
  to: BenchmarkSummary
  repeats: number
}

const pts = (c: Counts) => (c.n ? Math.round((c.correct / c.n) * 100) : 0)

/**
 * "Am I improving?" in one line, by the same rule as the progress-check comparison: a change counts only when it is
 * bigger than chance usually produces (two standard errors), and never when it rests on questions seen before.
 * Check-to-check when there are two checks; else this week vs last on FIRST answers only (repeats excluded); else
 * an honest "too early". Practice accuracy only, never an ACT/SAT score.
 */
export function improvementVerdict(check: CheckPair | null, week: { recent: Counts; prior: Counts }): Verdict {
  if (check) {
    if (check.repeats > 0)
      return {
        tone: 'neutral',
        headline: 'Not a clean comparison yet',
        detail: `${check.repeats} ${check.repeats === 1 ? 'question' : 'questions'} in the last two checks had been seen before. Recall isn't new evidence, so the change isn't judged.`,
      }
    const now = { correct: check.to.metrics.correct, answered: check.to.metrics.answered }
    const then = { correct: check.from.metrics.correct, answered: check.from.metrics.answered }
    const j = judgeChange(now, then)
    const d = j.delta == null ? 0 : Math.round(j.delta * 100)
    const pair = `${now.correct}/${now.answered} vs ${then.correct}/${then.answered} on the check before`
    if (j.verdict === 'up') return { tone: 'go', headline: `Improving: +${d} pts since the last check`, detail: `${pair}. Bigger than chance usually produces.` }
    if (j.verdict === 'down') return { tone: 'warn', headline: `Down ${-d} pts since the last check`, detail: `${pair}. One check can be an off day; the next one shows whether it holds.` }
    if (j.verdict === 'too_few') return { tone: 'neutral', headline: 'Too few answers to tell', detail: `${pair}. Checks need more answers to compare.` }
    return { tone: 'neutral', headline: 'About the same as the last check', detail: `${pair} (${d >= 0 ? '+' : ''}${d} pts), within normal variation.` }
  }
  const { recent, prior } = week
  const j = judgeChange({ correct: recent.correct, answered: recent.n }, { correct: prior.correct, answered: prior.n })
  if (j.verdict !== 'too_few' && recent.n >= 5 && prior.n >= 5) {
    const d = pts(recent) - pts(prior)
    const pair = `${pts(recent)}% this week vs ${pts(prior)}% last week, first answers only`
    if (j.verdict === 'up') return { tone: 'go', headline: `Improving: +${d} pts this week`, detail: pair }
    if (j.verdict === 'down') return { tone: 'warn', headline: `Down ${-d} pts this week`, detail: `${pair}. Harder questions can do this; watch the trend.` }
    return { tone: 'neutral', headline: 'Holding steady', detail: `${pair}. Within normal variation.` }
  }
  const need = Math.max(0, 5 - recent.n)
  return {
    tone: 'neutral',
    headline: 'Too early to tell',
    detail:
      need > 0
        ? `About ${need} more new ${need === 1 ? 'question' : 'questions'} this week gives a fair comparison with last week. Questions seen before don't count.`
        : 'Last week had too few new questions to compare with.',
  }
}
