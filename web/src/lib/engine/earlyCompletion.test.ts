import { describe, expect, it } from 'vitest'
import { COMPLETION_CONDITIONS, earlyCompletion, withheldReason } from './earlyCompletion'

describe('early completion: coverage is not a saving', () => {
  it('needs whole covered terms and all four conditions, each from a verified, sourced record', () => {
    const ok = { verified: true as const, sourceUrl: 'https://example.edu/x' }
    const all = Object.fromEntries(COMPLETION_CONDITIONS.map((c) => [c, ok]))
    expect(earlyCompletion(1)).toEqual({ supported: false, missing: COMPLETION_CONDITIONS })
    expect(earlyCompletion(0, all)).toEqual({ supported: false, missing: [] })
    expect(earlyCompletion(2, all)).toEqual({ supported: true, missing: [] })
    expect(earlyCompletion(2, { ...all, sequencing: { verified: false as never, sourceUrl: 'x' } }).missing).toEqual(['sequencing'])
  })

  it('says what is missing in plain words', () => {
    expect(withheldReason(earlyCompletion(1), 1)).toMatch(/doesn’t by itself mean finishing a term sooner.*prerequisites.*offered.*order.*graduation requirement/s)
    expect(withheldReason(earlyCompletion(0), 0)).toBe('No whole plan term is covered, so no time or money saved is shown.')
  })
})
