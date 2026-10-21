import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import { FreshContentNotice } from './WeekPlan'
import { contentStatus } from '../lib/engine/freshness'

const pool = Array.from({ length: 10 }, (_, i) => ({ id: `q${i}`, section: 'math', exam_family: 'sat' as const, difficulty: 3 }))

describe('fresh-question notice', () => {
  it('after the starting benchmark the rest is held for the check: says so, never "answered every question"', () => {
    // 6 seen; the mini check holds 4 of the remaining 4, so practice is review only.
    const c = contentStatus('sat', pool, new Set(['q0', 'q1', 'q2', 'q3', 'q4', 'q5']))
    expect(c.practiceAllReview).toBe(true)
    render(<FreshContentNotice content={c} />)
    expect(screen.getByText(/except the 4 kept unseen for the next progress check/)).toBeInTheDocument()
    expect(screen.queryByText(/answered every/)).not.toBeInTheDocument()
  })

  it('when every question has been seen, says the bank is used up', () => {
    render(<FreshContentNotice content={contentStatus('sat', pool, new Set(pool.map((q) => q.id)))} name="Riley" />)
    expect(screen.getByText(/Riley has answered every SAT practice question we have/)).toBeInTheDocument()
  })
})
