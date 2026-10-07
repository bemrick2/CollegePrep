import { describe, expect, it } from 'vitest'
import type { BenchmarkSummary } from '../data/types'
import { benchmarkRepeats, contentStatus, firstAnswers, practiceExclusions, type Q } from './freshness'

// ACT mini check: english 3, math 4, reading 3, science 3.
const qs = (section: string, n: number, diffs: number[] = []): Q[] => Array.from({ length: n }, (_, i) => ({ id: `${section}-${String(i).padStart(2, '0')}`, section, exam_family: 'act', difficulty: diffs[i] ?? 3 }))
const pool = [...qs('math', 12, [1, 2, 3, 3, 4, 5, 1, 2, 3, 4, 5, 5]), ...qs('science', 8)]

describe('fresh, held for the next check, and seen before', () => {
  it('holds the next mini check worth of fresh questions out of practice, mid-difficulty first', () => {
    const s = contentStatus('act', pool, new Set())
    expect(s.sections.find((x) => x.section === 'math')).toMatchObject({ total: 12, unseen: 12, heldForCheck: 4, freshForPractice: 8 })
    const held = practiceExclusions('act', pool, new Set())
    expect([...held].filter((id) => id.startsWith('math')).sort()).toEqual(['math-01', 'math-02', 'math-03', 'math-08'])
    expect([...held].filter((id) => id.startsWith('science'))).toHaveLength(3)
  })

  it('says when practice is review only, section by section and overall', () => {
    const seenMath = new Set(pool.filter((q) => q.section === 'math').slice(0, 8).map((q) => q.id))
    const s = contentStatus('act', pool, seenMath)
    expect(s.sections.find((x) => x.section === 'math')).toMatchObject({ unseen: 4, heldForCheck: 4, freshForPractice: 0 })
    expect(s.reviewOnlySections).toEqual(['math'])
    expect(s.practiceAllReview).toBe(false)
    const all = contentStatus('act', pool, new Set(pool.map((q) => q.id)))
    expect(all).toMatchObject({ practiceAllReview: true, freshForPractice: 0 })
    expect(all.checkShortSections).toEqual(['math', 'science'])
  })

  it('first answers only: a question answered twice counts once, at its first answer', () => {
    const a = [
      { id: 'a1', question_id: 'q1', submitted_at: '2026-10-01T10:00:00Z' },
      { id: 'a2', question_id: 'q1', submitted_at: '2026-10-03T10:00:00Z' },
      { id: 'a3', question_id: 'q2', submitted_at: '2026-10-02T10:00:00Z' },
    ]
    expect(firstAnswers(a).map((x) => x.id)).toEqual(['a1', 'a3'])
  })

  it('counts the questions in a progress check the student had already seen', () => {
    const b = { id: 'b1', kind: 'mini', started_at: '2026-10-05T10:00:00Z', completed_at: '2026-10-05T10:20:00Z', attempt_ids: ['x1', 'x2', 'x3'] } as unknown as BenchmarkSummary
    const history = [
      { id: 'p1', question_id: 'q1', section: 'math', submitted_at: '2026-10-01T10:00:00Z' },
      { id: 'x1', question_id: 'q1', section: 'math', submitted_at: '2026-10-05T10:01:00Z' },
      { id: 'x2', question_id: 'q2', section: 'math', submitted_at: '2026-10-05T10:02:00Z' },
      { id: 'x3', question_id: 'q3', section: 'science', submitted_at: '2026-10-05T10:03:00Z' },
    ]
    expect(Object.fromEntries(benchmarkRepeats(b, history))).toEqual({ math: 1 })
  })
})
