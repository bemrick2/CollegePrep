import { describe, expect, it } from 'vitest'
import { tierSummary } from './Savings'

describe('tierSummary', () => {
  it('counts exams named only among printed alternatives, never as "no accepted exam credit"', () => {
    const t = { accepted: [{ examName: 'AP Calculus AB', course: 'MATH 1950', hours: 4, status: 'printed_alternative', matched: [] }], acceptedHours: 4, applicableHours: 0, applicableWithoutHours: 0, coveredTerms: [] }
    expect(tierSummary(t as never)).toBe('1 named among alternatives, not placed automatically.')
  })
})
