import { describe, expect, it } from 'vitest'
import type { BenchmarkSummary } from '../data/types'
import { benchmarkRepeats, checkPlan, checkQuestions, contentStatus, firstAnswers, practiceExclusions, type Q } from './freshness'

// ACT mini check: english 3, math 4, reading 3, science 3.
const qs = (section: string, n: number, diffs: number[] = []): Q[] => Array.from({ length: n }, (_, i) => ({ id: `${section}-${String(i).padStart(2, '0')}`, section, exam_family: 'act', difficulty: diffs[i] ?? 3 }))
const pool = [...qs('math', 12, [1, 2, 3, 3, 4, 5, 1, 2, 3, 4, 5, 5]), ...qs('science', 8)]

describe('the reserved assessment pool (CR-23), fresh questions and repeats', () => {
  it('reserves a fixed set per section, mid-difficulty first, and practice never uses it', () => {
    const s = contentStatus('act', pool, new Set())
    expect(s.sections.find((x) => x.section === 'math')).toMatchObject({ total: 12, unseen: 12, reserved: 4, reservedUnseen: 4, freshForPractice: 8 })
    const held = practiceExclusions('act', pool, new Set())
    expect([...held].filter((id) => id.startsWith('math')).sort()).toEqual(['math-01', 'math-02', 'math-03', 'math-08'])
    expect([...held].filter((id) => id.startsWith('science'))).toHaveLength(3)
  })

  it('is fixed: seeing reserved questions (in a check) does not move the reserve onto practice questions', () => {
    const seenReserved = new Set(['math-01', 'math-02', 'math-03', 'math-08'])
    expect([...practiceExclusions('act', pool, seenReserved)].filter((id) => id.startsWith('math')).sort()).toEqual(['math-01', 'math-02', 'math-03', 'math-08'])
    const s = contentStatus('act', pool, seenReserved)
    expect(s.sections.find((x) => x.section === 'math')).toMatchObject({ reserved: 4, reservedUnseen: 0, freshForPractice: 8 })
    expect(s.checkShortSections).toEqual(['math'])
  })

  it('uses the source\'s pool marks when it has them (the CR-23 column), and nothing else', () => {
    const marked = pool.map((q) => ({ ...q, pool: q.id === 'math-11' ? ('assessment' as const) : ('practice' as const) }))
    expect([...practiceExclusions('act', marked)]).toEqual(['math-11'])
    expect(checkQuestions('act', marked).map((q) => q.id)).toEqual(['math-11'])
  })

  it('says when practice is review only, section by section and overall', () => {
    const practiceMath = pool.filter((q) => q.section === 'math' && !practiceExclusions('act', pool).has(q.id))
    const s = contentStatus('act', pool, new Set(practiceMath.map((q) => q.id)))
    expect(s.sections.find((x) => x.section === 'math')).toMatchObject({ unseen: 4, reserved: 4, freshForPractice: 0 })
    expect(s.reviewOnlySections).toEqual(['math'])
    expect(s.practiceAllReview).toBe(false)
    const all = contentStatus('act', pool, new Set(pool.map((q) => q.id)))
    expect(all).toMatchObject({ practiceAllReview: true, freshForPractice: 0 })
    expect(all.checkShortSections).toEqual(['math', 'science'])
  })
})

describe('when the reserved pool is too small for a check', () => {
  const want = { english: 3, math: 4, reading: 3, science: 3 }
  it('unseen reserved first, then reserved repeats (no verdict), shorter where there are too few, unmeasured where there are none', () => {
    // math: 4 reserved, 2 seen. science: 3 reserved (8 questions). english, reading: none at all.
    const plan = checkPlan('act', want, pool, new Set(['math-01', 'math-02']))
    expect(plan.find((p) => p.section === 'math')).toMatchObject({ count: 4, unseen: 2, repeats: 2, status: 'with_repeats', shortened: false })
    expect(plan.find((p) => p.section === 'science')).toMatchObject({ count: 3, unseen: 3, repeats: 0, status: 'fresh' })
    expect(plan.find((p) => p.section === 'english')).toMatchObject({ count: 0, status: 'not_measured' })
    const big = checkPlan('act', { ...want, math: 8 }, pool, new Set())
    expect(big.find((p) => p.section === 'math')).toMatchObject({ wanted: 8, count: 4, shortened: true, status: 'fresh' })
  })

  it('never fills a check with practice questions', () => {
    const ids = new Set(checkQuestions('act', pool).map((q) => q.id))
    expect(ids.size).toBe(7)
    for (const q of pool) if (!ids.has(q.id)) expect(practiceExclusions('act', pool).has(q.id)).toBe(false)
  })
})

describe('repeats and first answers', () => {
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
