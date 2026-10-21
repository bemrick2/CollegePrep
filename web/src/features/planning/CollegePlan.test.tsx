import { describe, expect, it, vi, beforeAll } from 'vitest'
import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { DemoSource, DEMO_PARENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import { examKey } from '../../lib/engine/examCredit'

// The pilot is registered only when VITE_PLANNING_PILOT=true, read when the modules load.
let App: typeof import('../../App').App
let AppProvider: typeof import('../../lib/app').AppProvider
beforeAll(async () => {
  vi.stubEnv('VITE_PLANNING_PILOT', 'true')
  vi.resetModules()
  ;({ App } = await import('../../App'))
  ;({ AppProvider } = await import('../../lib/app'))
})

async function family() {
  const src = new DemoSource(emptyStore())
  src.switchPersona(DEMO_PARENT, 'Jordan')
  const hh = await src.createHousehold('Home', 'America/Chicago')
  const sid = await src.addStudent(hh, 'Riley', 2030, 9)
  const ap = (name: string, score: number) => ({ family: 'AP', key: examKey('AP', name), name, score })
  localStorage.setItem(`pp-exam-plan:${sid}`, JSON.stringify([ap('AP Microeconomics', 3), ap('AP Calculus AB', 3)]))
  return src
}
const renderPlan = (src: DemoSource) =>
  render(
    <MemoryRouter initialEntries={['/colleges/plan']}>
      <AppProvider source={src}>
        <App />
      </AppProvider>
    </MemoryRouter>,
  )

describe('college plan pilot (#195), on the stored Tennessee records', () => {
  it('UTC Management: verified plan and cost shown; unverified credit tables named, never shown as credit', async () => {
    const user = userEvent.setup()
    renderPlan(await family())
    expect(await screen.findByRole('heading', { name: 'College plan' }, { timeout: 10000 })).toBeInTheDocument()
    expect(await screen.findByText('Partly on file', {}, { timeout: 10000 })).toBeInTheDocument()
    expect(screen.getAllByText(/^Term [1-8]$/)).toHaveLength(8)
    expect(screen.getByText(/120 credit hours in total, as printed/)).toBeInTheDocument()
    // Exam credit: UTC's AP table isn't verified (no year printed), so no credit is claimed.
    const credit = screen.getByRole('heading', { name: 'Exam credit' }).closest('section')!
    expect(within(credit).getAllByText('Not on file')).toHaveLength(2)
    expect(within(credit).getAllByText(/credit table is on file but not yet verified: the values were checked, but the page prints no academic year/).length).toBeGreaterThan(0)
    // Cost by living arrangement, as published.
    expect(screen.getByText('$30,340')).toBeInTheDocument()
    await user.click(screen.getByRole('radio', { name: 'With family' }))
    expect(screen.getByText('$23,736')).toBeInTheDocument()
    expect(screen.getByText(/In-state price shown: no home state entered\. Published for 2026-27\./)).toBeInTheDocument()
    // Nothing is claimed about time or money saved.
    expect(screen.getByText('No whole plan term is covered by this credit, so no shorter timeline is shown.')).toBeInTheDocument()
    expect(screen.queryByText(/Potential saving/)).not.toBeInTheDocument()
  }, 30_000)

  it('UTK: credit accepted from its verified table, but no business plan on file, so where it counts is unknown', async () => {
    const user = userEvent.setup()
    renderPlan(await family())
    await screen.findByText('Partly on file', {}, { timeout: 10000 })
    await user.selectOptions(screen.getByLabelText('School'), 'utk')
    expect(await screen.findByText('No degree plan on file')).toBeInTheDocument()
    const credit = screen.getByRole('heading', { name: 'Exam credit' }).closest('section')!
    expect(within(credit).getAllByText('Credit; where it counts isn’t on file').length).toBeGreaterThan(0)
    expect(within(credit).getAllByText('Credit hours not listed in the school’s table.').length).toBeGreaterThan(0)
  }, 30_000)

  it('MTSU: no plan and no cost on file; each is named, nothing estimated', async () => {
    const user = userEvent.setup()
    renderPlan(await family())
    await screen.findByText('Partly on file', {}, { timeout: 10000 })
    await user.selectOptions(screen.getByLabelText('School'), 'mtsu')
    expect(await screen.findByText('No degree plan on file')).toBeInTheDocument()
    expect(screen.getAllByText(/No cost of attendance is on file for Middle Tennessee State University\./).length).toBeGreaterThan(0)
    expect(screen.queryByText(/\$\d/)).not.toBeInTheDocument()
  }, 30_000)
})

describe('college plan pilot when the flag is off', () => {
  it('is not offered', async () => {
    vi.unstubAllEnvs()
    vi.resetModules()
    const { App: Off } = await import('../../App')
    const { AppProvider: P } = await import('../../lib/app')
    render(
      <MemoryRouter initialEntries={['/colleges']}>
        <P source={await family()}>
          <Off />
        </P>
      </MemoryRouter>,
    )
    await screen.findAllByRole('link', { name: 'Compare' }, { timeout: 10000 })
    expect(screen.queryByRole('link', { name: 'College plan (pilot)' })).not.toBeInTheDocument()
  }, 30_000)
})
