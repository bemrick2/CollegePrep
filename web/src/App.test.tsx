import { describe, expect, it } from 'vitest'
import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from './lib/app'
import { App } from './App'
import { DemoSource, DEMO_PARENT } from './lib/data/demo/demoSource'
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

  it('parent dashboard labels illustrative cost data', async () => {
    renderAt('/parent', new DemoSource(sampleFamily('parent')))
    expect(await screen.findByRole('heading', { name: 'How Maya is doing' })).toBeInTheDocument()
    expect(await screen.findByText(/Illustrative example/)).toBeInTheDocument()
  })
})
