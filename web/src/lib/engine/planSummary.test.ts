import { describe, expect, it } from 'vitest'
import { planSummary, type SchoolPlanInput } from './planSummary'

const s = (key: string, total: number | null, over: Partial<SchoolPlanInput> = {}): SchoolPlanInput => ({ key, name: key.toUpperCase(), level: 'four_year', total, comparable: total != null, levers: [], ...over })
const lever = (key: string, status: string) => ({ key, status, title: `${key} ${status}`, detail: '' }) as never

describe('planSummary', () => {
  it('leads with the top choice when it has an applicable price, else the lowest', () => {
    expect(planSummary([s('a', 200), s('b', 150)], 'a').headline).toMatchObject({ key: 'a', why: 'top_choice' })
    expect(planSummary([s('a', 200), s('b', 150)], null).headline).toMatchObject({ key: 'b', total: 150, why: 'lowest' })
    expect(planSummary([s('a', null), s('b', 150)], 'a').headline).toMatchObject({ key: 'b', why: 'lowest' })
  })
  it('never headlines a price that does not apply, and says why', () => {
    expect(planSummary([s('a', 120, { comparable: false })], null)).toMatchObject({ headline: null, missing: 'no_applicable_price' })
    expect(planSummary([], null).missing).toBe('no_schools')
    expect(planSummary([s('cc', 40, { level: 'two_year' })], null).missing).toBe('no_four_year')
  })
  it('picks one opportunity, score first, favouring the headline school', () => {
    const r = planSummary([s('a', 200, { levers: [lever('credit', 'on_track')] }), s('b', 150, { levers: [lever('merit-next', 'stretch')] })], null)
    expect(r.opportunity).toMatchObject({ key: 'a', lever: { key: 'credit' } })
    const r2 = planSummary([s('a', 200, { levers: [lever('merit-next', 'within_reach')] }), s('b', 150, { levers: [lever('credit', 'available')] })], null)
    expect(r2.opportunity).toMatchObject({ key: 'a', lever: { key: 'merit-next' } })
  })
})
