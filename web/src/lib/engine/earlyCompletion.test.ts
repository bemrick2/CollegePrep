import { describe, expect, it } from 'vitest'
import { COMPLETION_CONDITIONS, earlyCompletion, withheldReason } from './earlyCompletion'

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
})
