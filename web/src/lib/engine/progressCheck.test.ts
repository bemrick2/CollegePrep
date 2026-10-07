import { describe, expect, it } from 'vitest'
import type { BenchmarkSummary } from '../data/types'
import { compareProgress, judgeChange } from './progressCheck'

const sec = (section: string, correct: number, answered: number, pacing: number | null = 1) => ({ section, correct, answered, accuracy: answered ? correct / answered : null, skipped: 0, pacing_ratio: pacing, ceiling_difficulty: null })
const bench = (id: string, kind: BenchmarkSummary['kind'], at: string, sections: ReturnType<typeof sec>[]) =>
  ({ id, kind, exam_family: 'act', started_at: at, completed_at: at, attempt_ids: [], metrics: { sections } }) as unknown as BenchmarkSummary

describe('is a change real or noise?', () => {
  it('a few more right out of a handful is within normal variation', () => {
    // 3/6 -> 4/6: +17 points, but six answers each can't tell that from chance.
    expect(judgeChange({ correct: 4, answered: 6 }, { correct: 3, answered: 6 }).verdict).toBe('within_noise')
  })
  it('a large change on enough answers counts', () => {
    expect(judgeChange({ correct: 18, answered: 20 }, { correct: 8, answered: 20 }).verdict).toBe('up')
    expect(judgeChange({ correct: 6, answered: 20 }, { correct: 16, answered: 20 }).verdict).toBe('down')
  })
  it('too few answers: no verdict', () => {
    expect(judgeChange({ correct: 3, answered: 3 }, { correct: 0, answered: 3 }).verdict).toBe('too_few')
  })
})

describe('comparing a progress check with the baseline and the last check', () => {
  const base = bench('b0', 'initial', '2026-08-01T00:00:00Z', [sec('math', 3, 6), sec('english', 4, 6)])
  const mini1 = bench('b1', 'mini', '2026-09-05T00:00:00Z', [sec('math', 4, 6)])
  const now = bench('b2', 'mini', '2026-10-07T00:00:00Z', [sec('math', 5, 6, 0.9), sec('english', 5, 6)])

  it('uses the starting benchmark as the baseline and the most recent as previous', () => {
    const c = compareProgress(now, [mini1, base])
    expect(c.baseline?.id).toBe('b0')
    expect(c.previous?.id).toBe('b1')
    expect(c.sinceBaseline.find((s) => s.section === 'math')).toMatchObject({ then: { correct: 3, answered: 6 }, now: { correct: 5, answered: 6 }, verdict: 'within_noise', pacingThen: 1, pacingNow: 0.9 })
    expect(c.sinceLast!.find((s) => s.section === 'english')).toMatchObject({ then: null, verdict: 'too_few' })
  })

  it('the baseline itself has nothing to compare with', () => {
    expect(compareProgress(base, [])).toMatchObject({ baseline: null, previous: null, sinceBaseline: [], sinceLast: null })
  })

  it('second check: since-last is the same as since-baseline, so it is not repeated', () => {
    expect(compareProgress(mini1, [base]).sinceLast).toBeNull()
  })
})
