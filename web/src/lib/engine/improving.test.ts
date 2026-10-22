import { describe, expect, it } from 'vitest'
import type { BenchmarkSummary } from '../data/types'
import { improvementVerdict } from './improving'

const wk = (rn: number, rc: number, pn: number, pc: number) => ({ recent: { n: rn, correct: rc }, prior: { n: pn, correct: pc } })
const b = (correct: number, answered: number, sections = [{ section: 'math', answered }]) => ({ metrics: { correct, answered, sections } }) as unknown as BenchmarkSummary
const pair = (to: [number, number], from: [number, number], repeats = 0) => ({ to: b(...to), from: b(...from), repeats })

describe('improvementVerdict (same rule as the progress-check comparison)', () => {
  it('check to check: a clear change on enough answers, noise called noise', () => {
    expect(improvementVerdict(pair([24, 27], [12, 27]), wk(0, 0, 0, 0))).toMatchObject({ tone: 'go', headline: 'Improving: +44 pts since the last check' })
    expect(improvementVerdict(pair([15, 27], [13, 27]), wk(0, 0, 0, 0))).toMatchObject({ tone: 'neutral', headline: 'About the same as the last check' })
    expect(improvementVerdict(pair([8, 27], [20, 27]), wk(0, 0, 0, 0)).tone).toBe('warn')
  })
  it('never judges a change that rests on questions seen before', () => {
    expect(improvementVerdict(pair([27, 27], [5, 27], 6), wk(0, 0, 0, 0))).toMatchObject({ tone: 'neutral', headline: 'Not a clean comparison yet', detail: expect.stringMatching(/^6 questions/) })
  })
  it('no overall verdict between a shortened or partly unmeasured check and a full one', () => {
    const full = b(12, 27, [{ section: 'english', answered: 7 }, { section: 'math', answered: 8 }, { section: 'reading', answered: 6 }, { section: 'science', answered: 6 }])
    const short = b(13, 13, [{ section: 'english', answered: 3 }, { section: 'math', answered: 4 }, { section: 'reading', answered: 3 }, { section: 'science', answered: 3 }])
    const v = improvementVerdict({ from: full, to: short, repeats: 0 }, wk(0, 0, 0, 0))
    expect(v).toMatchObject({ tone: 'neutral', headline: 'Not a like-for-like comparison' })
    expect(v.headline).not.toMatch(/Improving/)
  })
  it('weekly fallback on first answers only, with the same noise rule', () => {
    expect(improvementVerdict(null, wk(20, 18, 20, 8)).headline).toBe('Improving: +50 pts this week')
    expect(improvementVerdict(null, wk(10, 8, 10, 7)).headline).toBe('Holding steady')
    expect(improvementVerdict(null, wk(2, 2, 10, 5))).toMatchObject({ headline: 'Too early to tell', detail: expect.stringMatching(/About 3 more new questions/) })
  })
})
