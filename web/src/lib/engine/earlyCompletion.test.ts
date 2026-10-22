import { describe, expect, it } from 'vitest'
import { COMPLETION_CONDITIONS, earlyCompletion, gatedSaving, withheldReason } from './earlyCompletion'

describe('early completion: coverage is not a saving', () => {
  it('needs whole covered terms and all four conditions, each from a verified, sourced record', () => {
    const scope = { institutionKey: 'x', planKey: 'p', terms: [3, 4] }
    const ok = { verified: true as const, sourceUrl: 'https://example.edu/x', institutionKey: 'x', planKey: 'p', terms: [3, 4] }
    const all = Object.fromEntries(COMPLETION_CONDITIONS.map((c) => [c, ok]))
    expect(earlyCompletion(1)).toEqual({ supported: false, missing: COMPLETION_CONDITIONS })
    expect(earlyCompletion(0, all, { ...scope, terms: [] })).toEqual({ supported: false, missing: [] })
    expect(earlyCompletion(2, all, scope)).toEqual({ supported: true, missing: [] })
    expect(earlyCompletion(2, { ...all, sequencing: { ...ok, verified: false as never } }, scope).missing).toEqual(['sequencing'])
  })

  it('evidence counts only for its own school, plan and covered terms, with a real source', () => {
    const scope = { institutionKey: 'x', planKey: 'p', terms: [3, 4] }
    const ok = { verified: true as const, sourceUrl: 'https://example.edu/x', institutionKey: 'x', planKey: 'p', terms: [3, 4] }
    const allOf = (e: typeof ok) => Object.fromEntries(COMPLETION_CONDITIONS.map((c) => [c, e]))
    expect(earlyCompletion(2, allOf(ok)).supported).toBe(false) // no scope
    expect(earlyCompletion(2, allOf({ ...ok, institutionKey: 'other' }), scope).supported).toBe(false)
    expect(earlyCompletion(2, allOf({ ...ok, planKey: 'other-track' }), scope).supported).toBe(false)
    expect(earlyCompletion(2, allOf({ ...ok, terms: [3] }), scope).supported).toBe(false)
    expect(earlyCompletion(2, allOf({ ...ok, sourceUrl: ' ' }), scope).supported).toBe(false)
    expect(earlyCompletion(2, allOf({ ...ok, sourceUrl: 'x' }), scope).supported).toBe(false)
  })

  it('says what is missing in plain words', () => {
    expect(withheldReason(earlyCompletion(1), 1)).toMatch(/doesn’t by itself mean finishing a term sooner.*prerequisites.*offered.*order.*graduation requirement/s)
    expect(withheldReason(earlyCompletion(0), 0)).toBe('No whole plan term is covered, so no time or money saved is shown.')
  })

  it('gatedSaving: a covered term alone never computes a saving; a plan with no key never counts as the same plan', () => {
    let ran = 0
    const g = gatedSaving(1, () => (ran++, 15000))
    expect([g.saving, ran, g.early.supported]).toEqual([null, 0, false])
    const ev = { verified: true as const, sourceUrl: 'https://example.edu/x', institutionKey: 'x', planKey: null as unknown as string, terms: [1] }
    const all = { prerequisites: ev, course_availability: ev, sequencing: ev, remaining_requirements: ev }
    expect(gatedSaving(1, () => 1, all, { institutionKey: 'x', planKey: null, terms: [1] }).saving).toBeNull()
    expect(gatedSaving(1, () => 1, all, { institutionKey: 'x', planKey: '', terms: [1] }).saving).toBeNull()
    // Evidence with no terms list withholds instead of throwing.
    const noTerms = { ...ev, planKey: 'p', terms: undefined as unknown as number[] }
    expect(gatedSaving(1, () => 1, { prerequisites: noTerms, course_availability: noTerms, sequencing: noTerms, remaining_requirements: noTerms }, { institutionKey: 'x', planKey: 'p', terms: [1] }).saving).toBeNull()
  })
})
