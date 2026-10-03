import { describe, expect, it } from 'vitest'
import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider, realName } from './lib/app'
import { App } from './App'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from './lib/data/demo/demoSource'
import { emptyStore } from './lib/data/demo/store'
import { sampleFamily } from './lib/data/demo/seed'

function renderAt(path: string, source: DemoSource) {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <AppProvider source={source}>
        <App />
      </AppProvider>
    </MemoryRouter>,
  )
}

describe('app flows', () => {
  it('student home shows one clear next action', async () => {
    renderAt('/student', new DemoSource(sampleFamily('student')))
    expect(await screen.findByRole('heading', { name: 'Maya' })).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: /About 10 minutes|Done for today/ })).toBeInTheDocument()
    // No scaled-score estimate is produced (CR-3), so none is shown.
    expect(screen.getByText(/No score estimate yet/)).toBeInTheDocument()
  })

  it('practice: answer with confidence, then see explanation tabs', async () => {
    const user = userEvent.setup()
    renderAt('/student/practice', new DemoSource(sampleFamily('student')))
    const group = await screen.findByRole('radiogroup', {}, { timeout: 3000 }).catch(() => null)
    if (group) await user.click(within(group).getAllByRole('radio')[0]!)
    else await user.type(screen.getByLabelText('Your answer'), '1')
    await user.click(screen.getByRole('button', { name: 'Certain' }))
    expect(await screen.findByRole('tab', { name: /Teach me/ })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /Continue|Finish/ })).toBeInTheDocument()
  })

  it('parent onboarding creates a household, student and invite code', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_PARENT, 'Jordan')
    renderAt('/onboarding/parent', src)
    await user.click(await screen.findByRole('button', { name: 'Continue' }))
    await user.type(screen.getByLabelText("Student's first name"), 'Riley')
    await user.click(screen.getByRole('button', { name: '11' }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(screen.getByRole('button', { name: 'Create household' }))
    expect(await screen.findByText('Invite code')).toBeInTheDocument()
    const ctx = await src.getHouseholdContext()
    expect(ctx.students.map((s) => s.display_name)).toEqual(['Riley'])
    expect(await src.getPlan(ctx.students[0]!.id)).toMatchObject({ exam_family: 'act' })
  })

  it('parent cost outlook leads with four-year schools, published costs only, no estimated savings', async () => {
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-219976', 'ipeds-221908']))
    renderAt('/parent', new DemoSource(sampleFamily('parent')))
    expect(await screen.findByRole('heading', { name: 'How Maya is doing' })).toBeInTheDocument()
    // UTK in-state $36,994 x 4; Lipscomb $69,210 x 4; Northeast State (2-year) $20,304 x 2 — never x 4.
    expect(await screen.findByText('$147,976')).toBeInTheDocument()
    expect(screen.getByText('$276,840')).toBeInTheDocument()
    expect(screen.getByText('$128,864')).toBeInTheDocument() // difference between the two four-year schools
    expect(screen.getByText('$40,608')).toBeInTheDocument()
    expect(screen.queryByText(/Potential savings/i)).not.toBeInTheDocument()
    // No community-college path unless the family asked for the lowest-cost route.
    expect(screen.queryByText(/Alternative lower-cost path/)).not.toBeInTheDocument()
    localStorage.removeItem('pp-compare')
  })

  it('alternative lower-cost path appears only for a lowest-cost goal, labelled as an unverified example', async () => {
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-221908']))
    const src = new DemoSource(sampleFamily('parent'))
    const ctx = await src.getHouseholdContext()
    await src.savePlan(ctx.students[0]!.id, { exam_family: 'act', target_score: 27, goals: ['lower_cost'], daily_minutes: 10 })
    renderAt('/parent', src)
    expect(await screen.findByText(/Alternative lower-cost path/)).toBeInTheDocument()
    expect(screen.getByText(/transfer agreement not yet verified/)).toBeInTheDocument()
    expect(screen.getByText(/not a recommendation/)).toBeInTheDocument()
    localStorage.removeItem('pp-compare')
  })

  it('college paths match exam scores to the school\'s published table without estimating savings', async () => {
    const user = userEvent.setup()
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-221908']))
    renderAt('/colleges/paths', new DemoSource(sampleFamily('parent')))
    expect(await screen.findByRole('heading', { name: 'College paths' })).toBeInTheDocument()
    expect(await screen.findByRole('heading', { name: 'University of Tennessee, Knoxville' })).toBeInTheDocument()
    // The 2-year school is not a route card, and no transfer is implied.
    expect(screen.queryByRole('heading', { name: 'Northeast State Community College' })).not.toBeInTheDocument()
    expect(screen.getByText(/appears here only once a verified transfer agreement/)).toBeInTheDocument()
    await user.selectOptions(screen.getByLabelText('Add an exam'), screen.getByRole('option', { name: 'AP Calculus AB' }))
    expect(await screen.findByText('Needs 3+')).toBeInTheDocument()
    await user.selectOptions(screen.getByLabelText('AP Calculus AB score'), '2')
    expect(screen.getByText('Needs 3+ (yours: 2)')).toBeInTheDocument()
    await user.selectOptions(screen.getByLabelText('AP Calculus AB score'), '5')
    expect(screen.getByText('Your 5 earns credit')).toBeInTheDocument()
    expect(screen.queryByText(/saved?\s+\$/i)).not.toBeInTheDocument()
    localStorage.clear()
  })

  it('choosing a role on the landing page goes straight to that onboarding (no second "who is using" step)', async () => {
    const user = userEvent.setup()
    renderAt('/', new DemoSource(emptyStore()))
    await user.click(await screen.findByRole('button', { name: /I'm a student/ }))
    expect(await screen.findByRole('heading', { name: /Let's get you set up/ })).toBeInTheDocument()
    expect(screen.queryByRole('heading', { name: /Who's using/ })).not.toBeInTheDocument()
  })

  it('demo placeholder names never prefill forms', async () => {
    expect(realName({ userId: 'u', displayName: 'Student (demo)' } as never)).toBe('')
    expect(realName({ userId: 'u', displayName: 'Jordan' } as never)).toBe('Jordan')
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Student (demo)')
    renderAt('/onboarding/student', src)
    expect(await screen.findByLabelText('First name')).toHaveValue('')
  })

  it('pre-answer Teach me and Test strategy show answer-free help', async () => {
    const user = userEvent.setup()
    renderAt('/student/practice', new DemoSource(sampleFamily('student')))
    await user.click(await screen.findByRole('button', { name: /Teach me/ }, { timeout: 3000 }))
    expect(await screen.findByRole('note', { name: 'Concept' })).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /Test strategy/ }))
    const strategies = await screen.findByRole('note', { name: 'Test strategies' })
    expect(within(strategies).getByText(/fastest for this question/)).toBeInTheDocument()
    // Nothing is graded or revealed yet.
    expect(screen.queryByRole('tab', { name: /Other answers/ })).not.toBeInTheDocument()
    expect(screen.getAllByRole('radio').every((r) => r.getAttribute('aria-checked') === 'false')).toBe(true)
  })

  it('practice indicators say they are not ACT/SAT scores and explain each one', async () => {
    const user = userEvent.setup()
    renderAt('/student', new DemoSource(sampleFamily('student')))
    expect(await screen.findByText(/Not ACT\/SAT scores/)).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /Strategy/ }))
    expect(screen.getByText(/test-taking habits/)).toBeInTheDocument()
  })

  it('benchmark card shows what is due and links to the right kind', async () => {
    renderAt('/student', new DemoSource(sampleFamily('student')))
    expect(await screen.findByRole('heading', { name: /Benchmarks/ })).toBeInTheDocument()
    expect(screen.getByText(/Mini benchmark|Full benchmark/)).toBeInTheDocument()
  })
})
