import { describe, expect, it } from 'vitest'
import { costLevers } from './costLevers'

const awards = [
  { award_name: 'Roddy', award_type: 'institutional_merit', test_requirement: 'Minimum 31 ACT / 1390 SAT.', award_amount_text: '$5,000 annually' },
  { award_name: 'Neyland', award_type: 'institutional_merit', test_requirement: 'Minimum 31 ACT / 1390 SAT.' },
  { award_name: 'Provost', award_type: 'institutional_merit', test_requirement: 'ACT 26+' },
  { award_name: 'Volunteer', award_type: 'institutional_merit', test_requirement: 'ACT/SAT composite superscore tiers' },
  { award_name: 'Pledge', award_type: 'institutional_need_last_dollar', test_requirement: null },
]
const base = { awards, creditPolicies: [{ policy_kind: 'AP' }, { policy_kind: 'dual_enrollment', policy_url: 'https://x/dual' }], credit: null, exam: 'act' as const, netPriceUrl: 'https://x/npc' }

describe('costLevers', () => {
  it('scores only single published minimums, conservatively, and never as eligibility', () => {
    const l = costLevers({ ...base, reference: { value: 29, basis: 'target' } })
    expect(l[0]).toMatchObject({ key: 'merit-met', status: 'on_track' })
    expect(l[0]!.detail).toMatch(/not an eligibility decision/)
    expect(l.find((x) => x.key === 'merit-next')).toMatchObject({ status: 'within_reach', title: '2 more ACT points reaches 2 merit awards (ACT 31+)' })
    expect(l.find((x) => x.key === 'merit-other')!.title).toMatch(/1 more merit award with GPA-only or tiered/)
    expect(l.find((x) => x.key === 'merit-next')!.detail).not.toMatch(/\.\./)
    // Score levers lead, then credit and dual enrollment.
    expect(l.map((x) => x.key).slice(0, 4)).toEqual(['merit-met', 'merit-next', 'credit', 'dual'])
  })

  it('a far threshold is not "within reach"', () => {
    const l = costLevers({ ...base, reference: { value: 22, basis: 'official' } })
    expect(l.find((x) => x.key === 'merit-next')!.status).toBe('stretch')
    expect(l.some((x) => x.key === 'merit-met')).toBe(false)
  })

  it('asks for a target instead of guessing, and lists verified non-score levers', () => {
    const l = costLevers({ ...base, reference: null })
    expect(l.map((x) => x.key)).toEqual(expect.arrayContaining(['merit-target', 'credit', 'dual', 'need', 'npc']))
    expect(l.find((x) => x.key === 'need')!.detail).toMatch(/depends on family income/)
    // No lever ever states a dollar saving.
    expect(l.some((x) => /save|saving/i.test(x.title + x.detail))).toBe(false)
  })
})
