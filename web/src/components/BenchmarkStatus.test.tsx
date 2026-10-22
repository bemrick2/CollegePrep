import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { BenchmarkStatus } from './BenchmarkStatus'
import type { BenchmarkSummary } from '../lib/data/types'

const check = (kind: BenchmarkSummary['kind'], completed: string, correct: number, answered: number, repeats?: number) =>
  ({
    id: completed,
    kind,
    exam_family: 'act',
    started_at: completed,
    completed_at: completed,
    attempt_ids: [],
    metrics: { answered, correct, accuracy: correct / answered, pacing_ratio: 1, sections: [{ section: 'math', answered, correct, skipped: 0, accuracy: correct / answered, pacing_ratio: 1, ceiling_difficulty: null, ...(repeats != null ? { repeats } : {}) }] },
  }) as unknown as BenchmarkSummary

describe('the Benchmarks card never shows an unjudged change (#266 review)', () => {
  it('a repeated, shortened second check: no "+N" delta, only a pointer to the judged comparison', () => {
    render(
      <MemoryRouter>
        <BenchmarkStatus history={[check('initial', '2026-09-01T10:00:00Z', 8, 27), check('mini', '2026-10-06T10:00:00Z', 4, 4, 4)]} />
      </MemoryRouter>,
    )
    expect(screen.queryByText(/^\+\d+/)).not.toBeInTheDocument()
    expect(screen.queryByText(/Since the previous benchmark/)).not.toBeInTheDocument()
    expect(screen.getByText(/A change is judged only between like checks on questions not seen before/)).toBeInTheDocument()
  })
})
