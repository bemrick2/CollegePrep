import { describe, expect, it } from 'vitest'
import type { AttemptRecord } from '../data/types'
import { MIN_FOR_SCORE, priorScores, threeScores } from './scores'

const now = new Date('2026-10-02T12:00:00Z')
let id = 0
const att = (o: Partial<AttemptRecord>): AttemptRecord => ({
  id: String(++id), question_id: 'q', section: 'math', skill_key: 'k', submitted_at: '2026-10-01T12:00:00Z',
  elapsed_ms: 30_000, expected_time_seconds: 60, is_correct: true, skipped: false, confidence: 3, hint_count: 0, ...o,
})

describe('threeScores', () => {
  it('stays null until there is enough evidence', () => {
    const s = threeScores(Array.from({ length: MIN_FOR_SCORE - 1 }, () => att({})), now)
    expect([s.knowledge.value, s.pacing.value, s.strategy.value]).toEqual([null, null, null])
    expect(s.knowledge.n).toBe(MIN_FOR_SCORE - 1)
  })

  it('knowledge is accuracy; pacing excludes slow and rushed answers', () => {
    const h = [
      ...Array.from({ length: 6 }, () => att({ elapsed_ms: 40_000 })), // on pace
      ...Array.from({ length: 2 }, () => att({ elapsed_ms: 90_000, is_correct: false })), // slow
      ...Array.from({ length: 2 }, () => att({ elapsed_ms: 5_000, is_correct: false })), // rushed (< 0.3x)
    ]
    const s = threeScores(h, now)
    expect(s.knowledge.value).toBe(60)
    expect(s.pacing.value).toBe(60)
  })

  it('strategy combines confident accuracy and hint-free correct answers', () => {
    const h = [
      ...Array.from({ length: 8 }, () => att({ confidence: 3, is_correct: true, hint_count: 0 })),
      ...Array.from({ length: 2 }, () => att({ confidence: 3, is_correct: false })),
      ...Array.from({ length: 2 }, () => att({ confidence: 1, is_correct: true, hint_count: 2 })),
    ]
    // certain: 8/10 = 0.8; correct without hints: 8/10 = 0.8
    expect(threeScores(h, now).strategy.value).toBe(80)
  })

  it('ignores skips and attempts outside the window', () => {
    const h = [
      ...Array.from({ length: 10 }, () => att({ submitted_at: '2026-08-01T00:00:00Z' })),
      ...Array.from({ length: 10 }, () => att({ skipped: true, is_correct: null })),
    ]
    expect(threeScores(h, now).knowledge.n).toBe(0)
  })

  it('prior window is the 28 days before, with no overlap', () => {
    const h = [
      ...Array.from({ length: 10 }, () => att({ submitted_at: '2026-09-20T00:00:00Z', is_correct: true })),
      ...Array.from({ length: 10 }, () => att({ submitted_at: '2026-08-20T00:00:00Z', is_correct: false })),
    ]
    expect(threeScores(h, now).knowledge.value).toBe(100)
    expect(priorScores(h, now).knowledge.value).toBe(0)
  })
})
