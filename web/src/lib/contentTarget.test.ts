import { describe, expect, it } from 'vitest'
import { PROVISIONAL_TARGET, bankSize, miniChecksIn } from './contentTarget'

describe('provisional content target (planning only, not launch approval)', () => {
  it('ACT, 40 a week for 12 weeks, 25% planned review: 414 practice + 53 reserved = 467', () => {
    expect(PROVISIONAL_TARGET).toMatchObject({ exam: 'act', questionsPerWeek: 40, weeks: 12, plannedReview: 0.25 })
    expect(miniChecksIn(12)).toBe(2)
    expect(bankSize()).toMatchObject({ practiceShown: 480, practiceUnique: 414, reserved: 53, total: 467 })
    expect(bankSize().reservedPerSection).toEqual({ english: 13, math: 16, reading: 12, science: 12 })
  })

  it('bank size and planned review are settings, matching QUESTION_BANK_RECOMMENDATION.md', () => {
    expect(bankSize({ ...PROVISIONAL_TARGET, plannedReview: 0 }).total).toBe(605)
    expect(bankSize({ ...PROVISIONAL_TARGET, exam: 'sat' }).total).toBe(448)
    expect(bankSize({ ...PROVISIONAL_TARGET, weeks: 52, questionsPerWeek: 20, plannedReview: 0 }).reserved).toBe(157)
    expect(bankSize({ ...PROVISIONAL_TARGET, reservedPerSection: { english: 30, math: 30, reading: 30, science: 30 } }).reserved).toBe(120)
    expect(() => bankSize({ ...PROVISIONAL_TARGET, plannedReview: 1.5 })).toThrow()
  })
})
