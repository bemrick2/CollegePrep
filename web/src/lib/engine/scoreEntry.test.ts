import { describe, expect, it } from 'vitest'
import { checkScore } from './scoreEntry'

const today = '2026-10-07'

describe('checkScore', () => {
  it('accepts a composite with no sections, and keeps only the sections entered', () => {
    expect(checkScore({ exam: 'act', composite: '27', sections: { math: '25', science: '' }, testDate: '2026-06-13' }, today)).toMatchObject({ ok: true, composite: 27, sections: { math: 25 } })
  })
  it('never fills in a missing score', () => {
    const c = checkScore({ exam: 'act', composite: '', sections: {}, testDate: '2026-06-13' }, today)
    expect(c.ok).toBe(false)
    expect(c.composite).toBeNull()
    expect(c.errors.composite).toMatch(/score from the report/)
  })
  it('rejects impossible values and future dates', () => {
    expect(checkScore({ exam: 'act', composite: '37', sections: {}, testDate: '2026-06-13' }, today).errors.composite).toMatch(/1 to 36/)
    expect(checkScore({ exam: 'sat', composite: '1255', sections: {}, testDate: '2026-06-13' }, today).errors.composite).toMatch(/steps of 10/)
    expect(checkScore({ exam: 'sat', composite: '1200', sections: { math: '850' }, testDate: '2026-06-13' }, today).errors.math).toBeTruthy()
    expect(checkScore({ exam: 'act', composite: '25', sections: {}, testDate: '2026-12-01' }, today).errors.testDate).toMatch(/hasn't happened/)
  })
  it('an SAT total must equal its two sections', () => {
    expect(checkScore({ exam: 'sat', composite: '1300', sections: { reading_writing: '650', math: '620' }, testDate: '2026-06-06' }, today).errors.composite).toMatch(/is 1270, not 1300/)
    expect(checkScore({ exam: 'sat', composite: '1270', sections: { reading_writing: '650', math: '620' }, testDate: '2026-06-06' }, today).ok).toBe(true)
  })
})
