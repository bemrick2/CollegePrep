import { describe, expect, it, vi, beforeAll } from 'vitest'
import { render, screen, within } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { DemoSource, DEMO_PARENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import real from './pilotFixture.json'

/**
 * SCENARIO, NOT TODAY'S DATA. Every UTC plan in the pilot is partially verified (2026-10-23: printed notes not
 * captured), so no live plan exercises the term-by-term view. This test marks UTC's plan records verified, as they
 * would be once a replacement that captures the note passes independent review, only to keep that view tested.
 * Nothing here is shown to a family or claims any record is verified.
 */
type Fx = { schools: { institution_key: string; domains: Record<string, Record<string, unknown>[]> }[] }
const scenario = JSON.parse(JSON.stringify(real)) as Fx
for (const s of scenario.schools)
  if (s.institution_key === 'utc')
    s.domains.degree_requirements = s.domains.degree_requirements!.map((r) => (r.requirement_kind === 'program_plan' ? { ...r, verification_status: 'verified', notes_capture: 'complete' } : r))

let App: typeof import('../../App').App
let AppProvider: typeof import('../../lib/app').AppProvider
beforeAll(async () => {
  vi.stubEnv('VITE_PLANNING_PILOT', 'true')
  vi.resetModules()
  vi.doMock('./pilotFixture.json', () => ({ default: scenario }))
  ;({ App } = await import('../../App'))
  ;({ AppProvider } = await import('../../lib/app'))
})

describe('college plan pilot, scenario: UTC Management’s plan once its note is captured and reviewed', () => {
  it('shows eight real terms (year headings are not terms, #230) and the printed total', async () => {
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_PARENT, 'Jordan')
    const hh = await src.createHousehold('Home', 'America/Chicago')
    await src.addStudent(hh, 'Riley', 2030, 9)
    render(
      <MemoryRouter initialEntries={['/colleges/plan']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByText('Partly on file', {}, { timeout: 10000 })).toBeInTheDocument()
    expect(screen.queryByText('Degree plan not yet verified')).not.toBeInTheDocument()
    expect(screen.getAllByText(/^Term [1-8]: /)).toHaveLength(8)
    expect(screen.queryByText(/^Term 9: /)).toBeNull()
    expect(screen.getByText(/120 credit hours in total, as printed/)).toBeInTheDocument()
    const plan = screen.getByRole('heading', { name: 'Degree plan' }).closest('section')!
    expect(within(plan).getByRole('link', { name: /^Source, verified / })).toHaveAttribute('href', expect.stringContaining('cob-management-bsba'))
  }, 30_000)
})
