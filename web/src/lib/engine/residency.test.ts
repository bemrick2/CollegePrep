import { describe, expect, it } from 'vitest'
import { pickCost } from './residency'

const pub = [
  { residency: 'in_state', total_cost_of_attendance: 36994 },
  { residency: 'out_of_state', total_cost_of_attendance: 58000 },
]

describe('pickCost', () => {
  it('in-state for a home-state school, out-of-state otherwise', () => {
    expect(pickCost(pub, 'TN', 'TN')).toEqual({ cost: pub[0], basis: 'matched' })
    expect(pickCost(pub, 'TN', 'OR')).toEqual({ cost: pub[1], basis: 'matched' })
  })
  it('labels the in-state price as assumed when the home state is unknown', () => {
    expect(pickCost(pub, 'TN', null)).toEqual({ cost: pub[0], basis: 'assumed_in_state' })
  })
  it('flags an out-of-state family when no out-of-state price is published', () => {
    expect(pickCost([pub[0]!], 'TN', 'OR')).toEqual({ cost: pub[0], basis: 'out_of_state_missing' })
  })
  it('private "all students" prices apply to everyone', () => {
    const all = [{ residency: 'not_applicable', total_cost_of_attendance: 69210 }]
    expect(pickCost(all, 'TN', 'OR')).toEqual({ cost: all[0], basis: 'matched' })
  })
})
