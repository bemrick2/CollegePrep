import { describe, expect, it } from 'vitest'
import { meritAwards, referenceScore, testMinimums } from './merit'

describe('merit test criteria', () => {
  it('reads a single published minimum', () => {
    expect(testMinimums('ACT 30+ / SAT 1360+')).toEqual({ act: 30, sat: 1360 })
    expect(testMinimums('Minimum 31 ACT / 1390 SAT.')).toEqual({ act: 31, sat: 1390 })
    expect(testMinimums("Minimum 31 ACT / 1390 SAT (Chancellor's Scholarships threshold).")).toEqual({ act: 31, sat: 1390 })
    expect(testMinimums('ACT composite of 25 or higher')).toEqual({ act: 25, sat: null })
  })

  it('refuses ranges, tiers and ambiguity', () => {
    expect(testMinimums('3.6-3.79 GPA with 28-36 ACT / 1300-1600 SAT')).toEqual({ act: null, sat: null })
    expect(testMinimums('ACT/SAT composite superscore tiers (writing not used)')).toEqual({ act: null, sat: null })
    expect(testMinimums('ACT 25+ for tier one, ACT 30+ for tier two')).toEqual({ act: null, sat: null })
    expect(testMinimums(null)).toEqual({ act: null, sat: null })
  })

  it('keeps merit awards only', () => {
    const a = meritAwards([
      { award_name: 'Pledge', award_type: 'institutional_need_last_dollar', test_requirement: 'ACT 21+' },
      { award_name: 'Roddy', award_type: 'institutional_merit', test_requirement: 'Minimum 31 ACT / 1390 SAT.', gpa_requirement: 'N/A' },
    ])
    expect(a.map((x) => x.name)).toEqual(['Roddy'])
    expect(a[0]!.gpaText).toBeNull()
  })

  it('never uses a practice estimate as the reference score', () => {
    const scores = [{ exam_family: 'act', composite: 29, score_source: 'practice_estimate', test_date: '2026-09-01' }]
    expect(referenceScore(scores, 'act', 27)).toEqual({ value: 27, basis: 'target' })
    expect(referenceScore([...scores, { exam_family: 'act', composite: 26, score_source: 'self_reported', test_date: '2026-06-01' }], 'act', 27)).toEqual({ value: 26, basis: 'self_reported' })
    expect(referenceScore(scores, 'act', null)).toBeNull()
  })
})
