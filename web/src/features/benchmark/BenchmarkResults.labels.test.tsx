import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { BenchmarkResults } from './BenchmarkResults'
import type { BenchmarkSummary, SectionMetrics } from '../../lib/data/types'

const sec = (section: string, answered: number, correct: number, repeats?: number): SectionMetrics => ({ section, answered, correct, skipped: 0, accuracy: correct / answered, pacing_ratio: 1, ceiling_difficulty: null, ...(repeats != null ? { repeats } : {}) })
const summary = (kind: BenchmarkSummary['kind'], completed: string, sections: SectionMetrics[]): BenchmarkSummary => ({
  id: `b-${completed}`,
  kind,
  exam_family: 'act',
  started_at: completed,
  completed_at: completed,
  attempt_ids: [],
  metrics: { answered: sections.reduce((n, s) => n + s.answered, 0), correct: sections.reduce((n, s) => n + s.correct, 0), skipped: 0, skip_events: 0, returns: 0, answer_changes: 0, accuracy: 0.5, median_elapsed_ms: null, pacing_ratio: 1, calibration: [], strategy_use: [], traps_fallen: [], sections },
})

describe('check results say when a check was shortened, repeated or partly unmeasured (CR-23)', () => {
  it('a shortened starting check names each short section and the unmeasured ones', () => {
    render(<MemoryRouter><BenchmarkResults summary={summary('initial', '2026-10-01T10:00:00Z', [sec('english', 3, 2), sec('reading', 3, 1), sec('science', 3, 3)])} traps={[]} /></MemoryRouter>)
    expect(screen.getByText('A shorter check than usual')).toBeInTheDocument()
    expect(screen.getByText(/English: 3 answered of the 7 questions this check usually asks/)).toBeInTheDocument()
    expect(screen.getByText(/Not measured: Math\. No answers in this check/)).toBeInTheDocument()
    expect(screen.getAllByText('Shorter').length).toBe(3)
  })

  it('a check whose questions the server counted as repeats gets no verdict, however much the score moved', () => {
    const base = summary('initial', '2026-09-01T10:00:00Z', [sec('math', 4, 0)])
    const now = summary('mini', '2026-10-06T10:00:00Z', [sec('math', 4, 4, 4)])
    render(<MemoryRouter><BenchmarkResults summary={now} history={[base]} traps={[]} /></MemoryRouter>)
    expect(screen.getByText('4 questions in this check were seen before')).toBeInTheDocument()
    expect(screen.getByText('4 seen before')).toBeInTheDocument()
    expect(screen.getAllByText('Not a clean comparison').length).toBeGreaterThan(0)
    expect(screen.queryByText('Clear improvement')).not.toBeInTheDocument()
  })
})
