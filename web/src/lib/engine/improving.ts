import type { BenchmarkChange } from './benchmark'

export interface Verdict {
  tone: 'go' | 'warn' | 'neutral'
  headline: string
  detail: string
}

/** Small swings in short practice sets are noise; below these we say "about the same". */
export const NOISE = { benchmarkPts: 3, weeklyPts: 5, minAnswers: 5 }

/**
 * "Am I improving?" in one line: benchmark-to-benchmark when there are two, else this week vs last when both
 * weeks have enough answers, else an honest "too early". Practice accuracy only, never an ACT/SAT score.
 */
export function improvementVerdict(change: BenchmarkChange | null, week: { recent: { n: number; acc: number | null }; prior: { n: number; acc: number | null } }): Verdict {
  if (change && change.accuracyPts !== null) {
    const d = change.accuracyPts
    if (Math.abs(d) < NOISE.benchmarkPts) return { tone: 'neutral', headline: 'About the same as your last benchmark', detail: `Accuracy moved ${d >= 0 ? '+' : ''}${d} pts — within normal variation.` }
    return d > 0
      ? { tone: 'go', headline: `Improving: +${d} pts since your last benchmark`, detail: 'Benchmark accuracy, from adaptive sets of similar difficulty.' }
      : { tone: 'warn', headline: `Down ${-d} pts since your last benchmark`, detail: 'One benchmark can be an off day; the next one shows whether it holds.' }
  }
  const { recent, prior } = week
  if (recent.n >= NOISE.minAnswers && prior.n >= NOISE.minAnswers && recent.acc !== null && prior.acc !== null) {
    const d = Math.round((recent.acc - prior.acc) * 100)
    const pair = `${Math.round(recent.acc * 100)}% this week vs ${Math.round(prior.acc * 100)}% last week`
    if (Math.abs(d) < NOISE.weeklyPts) return { tone: 'neutral', headline: 'Holding steady', detail: `${pair}. Small weekly changes are noise.` }
    return d > 0 ? { tone: 'go', headline: `Improving: +${d} pts this week`, detail: pair } : { tone: 'warn', headline: `Down ${-d} pts this week`, detail: `${pair}. Harder questions can do this; watch the trend.` }
  }
  const need = Math.max(0, NOISE.minAnswers - recent.n)
  return {
    tone: 'neutral',
    headline: 'Too early to tell',
    detail: need > 0 ? `About ${need} more answer${need === 1 ? '' : 's'} this week gives a fair comparison with last week.` : 'Last week had too few answers to compare with.',
  }
}
