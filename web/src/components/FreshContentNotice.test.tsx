import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import { FreshContentNotice } from './WeekPlan'
import { contentStatus } from '../lib/engine/freshness'

const pool = Array.from({ length: 10 }, (_, i) => ({ id: `q${i}`, section: 'math', exam_family: 'sat' as const, difficulty: 3 }))

describe('fresh-question notice', () => {
  it('when every practice question is seen, names the questions set aside for checks; never "answered every question"', () => {
    // SAT reserves 4 math questions (q0–q3); the other 6 are practice and all seen.
    const c = contentStatus('sat', pool, new Set(['q4', 'q5', 'q6', 'q7', 'q8', 'q9']))
    expect(c.practiceAllReview).toBe(true)
    render(<FreshContentNotice content={c} />)
    expect(screen.getByText(/Another 4 are set aside for progress checks only/)).toBeInTheDocument()
    expect(screen.queryByText(/answered every/)).not.toBeInTheDocument()
  })

  it('with no reserved questions in the bank, says the practice bank is used up', () => {
    const marked = pool.map((q) => ({ ...q, pool: 'practice' as const }))
    render(<FreshContentNotice content={contentStatus('sat', marked, new Set(pool.map((q) => q.id)))} name="Riley" />)
    expect(screen.getByText(/Riley has answered every SAT practice question we have/)).toBeInTheDocument()
  })
})
