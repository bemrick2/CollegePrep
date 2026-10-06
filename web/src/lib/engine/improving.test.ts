import { describe, expect, it } from 'vitest'
import { improvementVerdict } from './improving'

const wk = (rn: number, ra: number | null, pn: number, pa: number | null) => ({ recent: { n: rn, acc: ra }, prior: { n: pn, acc: pa } })
const change = (pts: number) => ({ accuracyPts: pts }) as never

describe('improvementVerdict', () => {
  it('prefers benchmark-to-benchmark change and treats small moves as noise', () => {
    expect(improvementVerdict(change(6), wk(0, null, 0, null)).headline).toBe('Improving: +6 pts since your last benchmark')
    expect(improvementVerdict(change(2), wk(0, null, 0, null)).tone).toBe('neutral')
    expect(improvementVerdict(change(-5), wk(0, null, 0, null)).tone).toBe('warn')
  })
  it('falls back to weekly accuracy only with enough answers', () => {
    expect(improvementVerdict(null, wk(10, 0.78, 10, 0.7)).headline).toBe('Improving: +8 pts this week')
    expect(improvementVerdict(null, wk(10, 0.78, 10, 0.76)).headline).toBe('Holding steady')
    expect(improvementVerdict(null, wk(2, 1, 10, 0.5))).toMatchObject({ headline: 'Too early to tell', detail: expect.stringMatching(/About 3 more answers/) })
  })
})
