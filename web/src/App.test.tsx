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
    expect(screen.getByText(/Practice estimate — not an official score/)).toBeInTheDocument()
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

  it('parent cost outlook shows only published, verified costs and no estimated savings', async () => {
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-221908']))
    renderAt('/parent', new DemoSource(sampleFamily('parent')))
    expect(await screen.findByRole('heading', { name: 'How Maya is doing' })).toBeInTheDocument()
    // UTK in-state $36,994 x 4 years; Northeast State (2-year) in-state $20,304 x 2 — never x 4.
    expect(await screen.findByText('$147,976')).toBeInTheDocument()
    expect(screen.getByText('$40,608')).toBeInTheDocument()
    expect(screen.queryByText('$81,216')).not.toBeInTheDocument()
    // Transfer path: 2 x 20,304 + 2 x 36,994, flagged as unverified.
    expect(screen.getByText('$114,596')).toBeInTheDocument()
    expect(screen.getByText(/haven't verified a transfer agreement/)).toBeInTheDocument()
    expect(screen.queryByText(/Potential savings/i)).not.toBeInTheDocument()
    expect(screen.queryByText(/Illustrative/i)).not.toBeInTheDocument()
    localStorage.removeItem('pp-compare')
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
})
