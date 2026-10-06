import { describe, expect, it } from 'vitest'
import { cleanup, render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider, realName } from './lib/app'
import { App } from './App'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from './lib/data/demo/demoSource'
import { emptyStore } from './lib/data/demo/store'
import { sampleFamily } from './lib/data/demo/seed'
import { writeInterests } from './lib/interestStore'

/** The family's stated home state (the sample family lives in Tennessee). */
function livingIn<T extends { households: { id: string }[] }>(state: string, store: T): T {
  for (const h of store.households) localStorage.setItem(`pp-home-state:${h.id}`, state)
  return store
}

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
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-219976']))
    renderAt('/student', new DemoSource(sampleFamily('student')))
    expect(await screen.findByRole('heading', { name: 'Maya' })).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: /^ACT .+ — |Done for today|mixed practice/ })).toBeInTheDocument()
    expect(screen.getAllByRole('link', { name: /^(Continue|Bonus round)$/ })).toHaveLength(1)
    // No scaled-score estimate is produced (CR-3), so none is shown; why it matters comes from verified merit criteria.
    expect(screen.getByText(/We don't estimate your ACT score from practice yet/)).toBeInTheDocument()
    expect(await screen.findByText(/4 merit awards/)).toBeInTheDocument()
    expect(screen.getByText(/4 more ACT points/)).toBeInTheDocument()
    expect(screen.getByText(/not an eligibility decision or a guarantee/)).toBeInTheDocument()
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
    renderAt('/parent', new DemoSource(livingIn('TN', sampleFamily('parent'))))
    // Home leads with one number: the lowest applicable four-year total (the 2-year school never heads the plan).
    expect(await screen.findByRole('heading', { name: "Maya's college plan" })).toBeInTheDocument()
    expect(await screen.findByText('$148K')).toBeInTheDocument()
    expect(screen.getByText(/\$147,976 published in-state cost of attendance, before aid · lowest of your 3 saved schools/)).toBeInTheDocument()
    expect(screen.getByText('Biggest opportunity')).toBeInTheDocument()
    cleanup()
    renderAt('/colleges', new DemoSource(livingIn('TN', sampleFamily('parent'))))
    expect(await screen.findByRole('heading', { name: 'Your colleges', level: 1 })).toBeInTheDocument()
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

  it('cost uses the price that applies to the family and never substitutes a missing one', async () => {
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-221847', 'ipeds-220400']))
    // No home state: public prices are shown "if in-state" and kept out of the comparison.
    renderAt('/colleges', new DemoSource(sampleFamily('parent')))
    expect(await screen.findAllByText(/Set your home state to include it in the comparison/)).toHaveLength(3)
    expect(screen.queryByText(/Biggest difference/)).not.toBeInTheDocument()
    cleanup()
    // Oregon family: out-of-state prices; a school with no out-of-state price shows no number and is excluded.
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-221847', 'ipeds-220400']))
    renderAt('/colleges', new DemoSource(livingIn('OR', sampleFamily('parent'))))
    expect(await screen.findByText('$229,792')).toBeInTheDocument() // UTK out-of-state 57,448 x 4
    expect(screen.getByText('$154,088')).toBeInTheDocument() // Tennessee Tech out-of-state 38,522 x 4
    expect(screen.getByText('No out-of-state price published')).toBeInTheDocument()
    expect(screen.queryByText('$42,636')).not.toBeInTheDocument() // Jackson State in-state x 2 is never substituted
    expect(screen.getByText('$75,704')).toBeInTheDocument() // difference between the two comparable 4-year totals
  })

  it('alternative lower-cost path appears only for a lowest-cost goal, labelled as an unverified example', async () => {
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-221908']))
    const src = new DemoSource(livingIn('TN', sampleFamily('parent')))
    const ctx = await src.getHouseholdContext()
    await src.savePlan(ctx.students[0]!.id, { exam_family: 'act', target_score: 27, goals: ['lower_cost'], daily_minutes: 10 })
    renderAt('/colleges', src)
    expect(await screen.findByText(/Alternative lower-cost path/)).toBeInTheDocument()
    expect(screen.getByText(/transfer agreement not yet verified/)).toBeInTheDocument()
    expect(screen.getByText(/not a recommendation/)).toBeInTheDocument()
    localStorage.removeItem('pp-compare')
  })

  it('college paths match exam scores to the school\'s published table without estimating savings', async () => {
    const user = userEvent.setup()
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-221908']))
    renderAt('/colleges/paths', new DemoSource(livingIn('TN', sampleFamily('parent'))))
    expect(await screen.findByRole('heading', { name: 'College paths' })).toBeInTheDocument()
    expect(await screen.findByRole('heading', { name: 'University of Tennessee, Knoxville' })).toBeInTheDocument()
    // The 2-year school is not a route card, and no transfer is implied.
    expect(screen.queryByRole('heading', { name: 'Northeast State Community College' })).not.toBeInTheDocument()
    expect(screen.getByText(/appears here only once a verified transfer agreement/)).toBeInTheDocument()
    // Merit: published single minimums only, compared with the target (27), never stated as eligibility.
    expect(screen.getAllByText('ACT 31+').length).toBeGreaterThan(0)
    expect(screen.getAllByText('4 above target').length).toBeGreaterThan(0)
    expect(screen.getAllByText(/Compared with the target of 27/).length).toBeGreaterThan(0)
    // Ways to lower the cost: verified levers, conservative merit status, no dollar total.
    expect(screen.getAllByRole('heading', { name: 'Ways to lower this cost' }).length).toBeGreaterThan(0)
    expect(screen.getByText('4 more ACT points reaches 4 merit awards (ACT 31+)')).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /^Show \d+ more$/ }))
    expect(screen.getByText('3 need-based or access programs')).toBeInTheDocument()
    // Elevate one school as the primary target; it moves first.
    await user.click(screen.getAllByRole('button', { name: 'Make top choice' })[0]!)
    expect(await screen.findByText('Top choice')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Clear top choice' })).toBeInTheDocument()
    await user.selectOptions(screen.getByLabelText('Add an exam'), screen.getByRole('option', { name: 'AP Calculus AB' }))
    expect(await screen.findByText('Needs 3+')).toBeInTheDocument()
    await user.selectOptions(screen.getByLabelText('AP Calculus AB score'), '2')
    expect(screen.getByText('Needs 3+ (yours: 2)')).toBeInTheDocument()
    await user.selectOptions(screen.getByLabelText('AP Calculus AB score'), '5')
    expect(screen.getByText('Your 5 earns credit')).toBeInTheDocument()
    expect(screen.queryByText(/saved?\s+\$/i)).not.toBeInTheDocument()
    localStorage.clear()
  })

  it('dashboard elevates the primary target school with its top cost levers', async () => {
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-219976']))
    const src = new DemoSource(livingIn('TN', sampleFamily('parent')))
    renderAt('/parent', src)
    expect(await screen.findByRole('link', { name: 'Mark a top choice' })).toHaveAttribute('href', '/colleges/paths')
    cleanup()
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-219976']))
    localStorage.setItem('pp-primary', 'utk')
    renderAt('/parent', src)
    expect(await screen.findByText('Four-year cost at University of Tennessee, Knoxville')).toBeInTheDocument()
    expect(screen.getByText(/\$147,976 published in-state cost of attendance, before aid · your top choice/)).toBeInTheDocument()
    expect(screen.queryByRole('link', { name: 'Mark a top choice' })).not.toBeInTheDocument()
    // The biggest opportunity is the top choice's strongest verified lever, worded as a possibility.
    expect(screen.getByText(/4 more ACT points reaches 4 merit awards \(ACT 31\+\) at University of Tennessee, Knoxville/)).toBeInTheDocument()
  })

  it('student onboarding asks how sure they are about a major and never requires one', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Student (demo)')
    renderAt('/onboarding/student', src)
    await user.type(await screen.findByLabelText('First name'), 'Jordan')
    await user.click(screen.getByRole('button', { name: '11' }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: 'Continue' }))
    expect(await screen.findByRole('heading', { name: 'What might you study?' })).toBeInTheDocument()
    // Skippable before any choice.
    expect(screen.getByRole('button', { name: 'Skip for now' })).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /I'm not sure yet/ }))
    // Undecided: broad areas only, no majors panel.
    expect(screen.queryByText(/Possible majors in/)).not.toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Health' }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: 'Start my benchmark' }))
    await screen.findByText(/benchmark/i)
    const key = Object.keys(localStorage).find((k) => k.startsWith('pp-interests:'))!
    expect(JSON.parse(localStorage.getItem(key)!)).toEqual({ certainty: 'unsure', interests: [{ kind: 'area', key: 'health' }] })
  })

  it('a student weighing several majors saves at least three, unranked', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Student (demo)')
    renderAt('/onboarding/student', src)
    await user.type(await screen.findByLabelText('First name'), 'Sam')
    await user.click(screen.getByRole('button', { name: '10' }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: /considering a few things/ }))
    await user.click(screen.getByRole('button', { name: 'Engineering & technology' }))
    await user.click(screen.getByRole('button', { name: 'Computer science' }))
    await user.click(screen.getByRole('button', { name: 'Mechanical engineering' }))
    await user.click(screen.getByRole('button', { name: /^Business/ }))
    await user.click(screen.getByRole('button', { name: 'Finance' }))
    expect(screen.getByText(/3 saved/)).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: 'Start my benchmark' }))
    await screen.findByText(/benchmark/i)
    const key = Object.keys(localStorage).find((k) => k.startsWith('pp-interests:'))!
    const saved = JSON.parse(localStorage.getItem(key)!)
    expect(saved.interests.map((i: { key: string }) => i.key)).toEqual(['computer-science', 'mechanical-eng', 'finance'])
    expect(saved.interests.some((i: { focus?: boolean }) => i.focus)).toBe(false)
  })

  it('explore majors shows verified program fit across all interests and updates when interests change', async () => {
    const user = userEvent.setup()
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-219976']))
    const store = livingIn('TN', sampleFamily('parent'))
    writeInterests(store.students[0]!.id, { certainty: 'few', interests: [{ kind: 'major', key: 'computer-science' }, { kind: 'major', key: 'mechanical-eng' }, { kind: 'major', key: 'finance' }] })
    renderAt('/colleges/majors', new DemoSource(store))
    expect(await screen.findByRole('heading', { name: 'Explore majors' })).toBeInTheDocument()
    expect(
      await screen.findByText("University of Tennessee, Knoxville has verified programs for Computer science; Mechanical engineering and Finance aren't in our verified list yet."),
    ).toBeInTheDocument()
    expect(screen.getByText(/Published rule: “Progression to upper-division departmental programs is competitive and space-limited/)).toBeInTheDocument()
    // A school with no verified program list says so instead of implying anything.
    expect(screen.getByText("We haven't verified Lipscomb University's program list yet.")).toBeInTheDocument()
    // Unverified questions are asked, not answered.
    expect(screen.getByText('Does the major require direct (freshman) admission?')).toBeInTheDocument()
    expect(screen.queryByText(/requires freshman admission/)).not.toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Remove Finance' }))
    expect(await screen.findByText("University of Tennessee, Knoxville has verified programs for Computer science; Mechanical engineering isn't in our verified list yet.")).toBeInTheDocument()
  })

  it('compare places the target against the published middle 50%, without predicting admission', async () => {
    localStorage.setItem('pp-compare', JSON.stringify(['utk', 'ipeds-219976']))
    renderAt('/colleges/compare', new DemoSource(livingIn('TN', sampleFamily('parent'))))
    const table = await screen.findByRole('table', { name: 'College comparison' })
    // One row per question, shared by every school: each body row has a cell for each compared school.
    const rows = within(table).getAllByRole('row').slice(1)
    expect(rows.map((r) => within(r).getByRole('rowheader').textContent)).toEqual(
      expect.arrayContaining([expect.stringMatching(/^Cost of attendance/), expect.stringMatching(/^Admissions/), expect.stringMatching(/^Scholarships/), expect.stringMatching(/^Exam credit/), expect.stringMatching(/^Financial-aid appeals/)]),
    )
    for (const r of rows) expect(within(r).getAllByRole('cell')).toHaveLength(2)
    expect(within(table).getAllByRole('columnheader').map((h) => h.textContent)).toEqual([expect.stringMatching(/University of Tennessee, Knoxville/), expect.stringMatching(/Lipscomb University/)])
    expect(await within(table).findByText((_, el) => el?.tagName === 'P' && /Target 27 is below the middle 50%/.test(el.textContent ?? ''))).toBeInTheDocument()
    expect(within(table).getAllByText(/Not an admission prediction/).length).toBeGreaterThan(0)
    // Scholarships preview a fixed number; the rest are on the detail page. Missing records say so, never filled in.
    const awards = rows.find((r) => /^Scholarships/.test(within(r).getByRole('rowheader').textContent ?? ''))!
    expect(within(awards).getByRole('link', { name: /^View all \d+ scholarships$/ })).toHaveAttribute('href', '/colleges/utk#awards-heading')
    expect(within(awards).getByText('No verified scholarships yet.')).toBeInTheDocument()
    // Each school row opens that school's detail page.
    expect(screen.getAllByRole('link', { name: /University of Tennessee, Knoxville/ })[0]).toHaveAttribute('href', '/colleges/utk')
    cleanup()
    renderAt('/colleges/utk', new DemoSource(livingIn('TN', sampleFamily('parent'))))
    expect(await screen.findByRole('heading', { name: 'University of Tennessee, Knoxville', level: 1 })).toBeInTheDocument()
    expect(screen.getByText('$148K')).toBeInTheDocument()
    expect(screen.getByText((_, el) => el?.tagName === 'P' && /Target 27 is below the middle 50%/.test(el.textContent ?? ''))).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: 'Ways to lower the cost' })).toBeInTheDocument()
  })

  it('choosing a role on the landing page goes straight to that onboarding (no second "who is using" step)', async () => {
    const user = userEvent.setup()
    renderAt('/', new DemoSource(emptyStore()))
    await user.click(await screen.findByRole('button', { name: /^I'm a student\s*Take/ }))
    expect(await screen.findByRole('heading', { name: /Let's get you set up/ })).toBeInTheDocument()
    expect(screen.queryByRole('heading', { name: /Who's using/ })).not.toBeInTheDocument()
  })

  it('landing leads with creating a family plan; store badges say coming soon until listings exist', async () => {
    const user = userEvent.setup()
    renderAt('/', new DemoSource(emptyStore()))
    expect(await screen.findAllByText(/Apps for iPhone and Android are coming soon/)).not.toHaveLength(0)
    // No badge artwork or store link until a real listing URL is configured.
    expect(screen.queryByRole('link', { name: /App Store|Google Play/ })).not.toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /Create your family plan/ }))
    expect(await screen.findByRole('heading', { name: /set up your household/i })).toBeInTheDocument()
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
    renderAt('/student/progress', new DemoSource(sampleFamily('student')))
    expect(await screen.findByText(/Not ACT\/SAT scores/)).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /Strategy/ }))
    expect(screen.getByText(/test-taking habits/)).toBeInTheDocument()
  })

  it('benchmark card shows what is due and links to the right kind', async () => {
    renderAt('/student/progress', new DemoSource(sampleFamily('student')))
    expect(await screen.findByRole('heading', { name: /Benchmarks/ })).toBeInTheDocument()
    expect(screen.getByText(/Mini benchmark|Full benchmark/)).toBeInTheDocument()
  })
})
