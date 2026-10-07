import { beforeEach, describe, expect, it, vi } from 'vitest'
import { cleanup, render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { App } from '../../App'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import { localDate, weekStartOf, browserTimeZone } from '../../lib/engine/dates'
import { readStudentSetup } from '../../lib/setupProfile'
import { graduationYearFor } from './options'

function renderAt(path: string, source: DemoSource) {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <AppProvider source={source}>
        <App />
      </AppProvider>
    </MemoryRouter>,
  )
}

const classOf = (grade: number) => `Class of ${graduationYearFor(grade)}`
const step = (n: number, of: number) => screen.findByRole('progressbar', { name: `Step ${n} of ${of}` })
const thisWeek = () => weekStartOf(localDate(new Date(), browserTimeZone()))

beforeEach(() => localStorage.clear())

describe('setup: four short screens', () => {
  it('parent: skips everything unknown, previews the week, then shows the next assignment and an invite', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_PARENT, 'Jordan')
    renderAt('/onboarding/parent', src)

    await step(1, 4)
    await user.type(screen.getByLabelText("Your student's first name"), 'Riley')
    await user.click(screen.getByRole('button', { name: classOf(11) }))
    // Home state and high school are optional: left blank.
    await user.click(screen.getByRole('button', { name: 'Continue' }))

    await step(2, 4)
    expect(screen.getByRole('heading', { name: 'Which test is Riley taking?' })).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /^ACT/ }))
    await user.click(within(screen.getByRole('region', { name: /When is the ACT/ }) ?? document.body).getByRole('button', { name: 'Not sure yet' }))
    // No goal score is preset.
    expect(screen.getByRole('textbox', { name: 'Goal score' })).toHaveValue('')
    await user.click(screen.getByRole('button', { name: 'Continue' }))

    await step(3, 4)
    expect(screen.getByText(/Please don't guess/)).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Not yet' }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))

    await step(4, 4)
    // Accepting needs at least one day and a session length.
    await user.click(screen.getByRole('button', { name: 'Accept this plan' }))
    expect(screen.getByText(/Pick at least one study day/)).toBeInTheDocument()
    for (const d of ['Mon', 'Wed', 'Fri']) await user.click(screen.getByRole('button', { name: d }))
    await user.click(screen.getByRole('button', { name: /^10 min/ }))
    expect(screen.getByRole('button', { name: '40 · steady' })).toHaveAttribute('aria-pressed', 'true')
    const preview = await screen.findByRole('region', { name: /Proposed first week/ })
    expect(within(preview).getByText('Starting benchmark')).toBeInTheDocument()
    expect(screen.getByText(/Demo: choices are kept, but no email is sent/)).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Accept this plan' }))

    expect(await screen.findByRole('heading', { name: 'Riley is set up' })).toBeInTheDocument()
    expect(screen.queryByRole('progressbar')).not.toBeInTheDocument()
    // Quick practice and the starting benchmark are separate; a parent sees them but can't start them.
    expect(screen.getByRole('heading', { name: 'How Riley can start' })).toBeInTheDocument()
    expect(within(screen.getByRole('region', { name: /Starting benchmark · ACT/ })).getByText(/counts only once it's finished/)).toBeInTheDocument()
    expect(screen.queryByRole('link', { name: /Start a 5-minute session/ })).not.toBeInTheDocument()
    expect(screen.getByText('40 questions a week, Monday to Sunday')).toBeInTheDocument()
    expect(screen.getByText('Mon, Wed, Fri')).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: 'Invite Riley' })).toBeInTheDocument()

    const ctx = await src.getHouseholdContext()
    const riley = ctx.students[0]!
    expect(riley).toMatchObject({ display_name: 'Riley', graduation_year: graduationYearFor(11), grade_level: 11 })
    expect(await src.getPlan(riley.id)).toMatchObject({ exam_family: 'act', target_score: null, goals: ['raise_score'], daily_minutes: 10 })
    expect((await src.weeklyProgress(riley.id, thisWeek())).goal?.target_questions).toBe(40)
    expect(await src.testScores(riley.id)).toEqual([])
    // On the account (CR-26), not this browser: the student's device reads the same.
    expect(await src.getPlan(riley.id)).toMatchObject({ exam_intent: 'act', planned_test_date: null, study_days: [1, 3, 5] })
    expect(await src.setupProgress(riley.id)).toMatchObject({ setupCompletedAt: expect.any(String), startingPointAnsweredAt: expect.any(String) })
    expect(readStudentSetup(riley.id)).toEqual({})
  }, 30_000)

  it('student: both tests, a goal score, an official score checked for typos, and resume after leaving mid-way', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Sam')
    const first = renderAt('/onboarding/student', src)

    await step(1, 4)
    // The account already has a name, so it isn't asked again.
    expect(screen.queryByLabelText('Your first name')).not.toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: classOf(12) }))
    // High school isn't asked: it isn't needed for the first practice plan.
    expect(screen.queryByLabelText(/High school/)).not.toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Continue' }))

    await step(2, 4)
    await user.click(screen.getByRole('button', { name: 'Both' }))
    expect(screen.getByRole('heading', { name: 'Which one comes first?' })).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'SAT' }))
    const firstDate = within(screen.getByRole('region', { name: /When is the SAT/ })).getAllByRole('button')[0]!
    await user.click(firstDate)
    expect(screen.getByText(/days away/)).toBeInTheDocument()
    await user.type(screen.getByRole('textbox', { name: 'Goal score' }), '1255')
    expect(screen.getByText(/in steps of 10/, { selector: 'p' })).toBeInTheDocument()
    await user.clear(screen.getByRole('textbox', { name: 'Goal score' }))
    await user.type(screen.getByRole('textbox', { name: 'Goal score' }), '1300')
    await user.click(screen.getByRole('button', { name: 'Continue' }))

    await step(3, 4)
    // Leave and come back: the answers and the screen are kept.
    first.unmount()
    cleanup()
    renderAt('/onboarding/student', src)
    await step(3, 4)
    await user.click(screen.getByRole('button', { name: 'Yes, an official test' }))
    await user.click(screen.getByRole('radio', { name: 'SAT' }))
    await user.type(screen.getByLabelText('SAT Total (400–1600)'), '1200')
    await user.click(screen.getByText('Section scores (optional)'))
    await user.type(screen.getByLabelText('Reading and Writing'), '620')
    await user.type(screen.getByLabelText('Math'), '600')
    await user.type(screen.getByLabelText('Test date'), '2026-06-06')
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByText(/is 1220, not 1200/)).toBeInTheDocument()
    await user.clear(screen.getByLabelText('SAT Total (400–1600)'))
    await user.type(screen.getByLabelText('SAT Total (400–1600)'), '1220')
    await user.click(screen.getByRole('button', { name: 'Continue' }))

    await step(4, 4)
    await user.click(screen.getByRole('button', { name: 'Sat' }))
    await user.click(screen.getByRole('button', { name: /^15 min/ }))
    await user.click(screen.getByRole('button', { name: 'Accept this plan' }))

    expect(await screen.findByRole('heading', { name: "You're set, Sam" })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Start a 5-minute session' })).toHaveAttribute('href', '/student/practice?quick=1')
    expect(screen.getByRole('link', { name: 'Start the benchmark now' })).toHaveAttribute('href', '/student/benchmark')
    expect(screen.getByText('1300 (a goal, not a prediction)')).toBeInTheDocument()
    const me = (await src.getHouseholdContext()).myStudent!
    expect(await src.getPlan(me.id)).toMatchObject({ exam_family: 'sat', exam_intent: 'both', target_score: 1300, daily_minutes: 15, study_days: [6] })
    expect(await src.testScores(me.id)).toEqual([expect.objectContaining({ exam_family: 'sat', composite: 1220, section_scores: { reading_writing: 620, math: 600 }, score_source: 'self_reported' })])
    expect(readStudentSetup(me.id)).toEqual({})
    expect(localStorage.getItem(`pp-setup-draft:${DEMO_STUDENT}`)).toBeNull()
  }, 30_000)

  it('a practice-test score is saved as a practice test, apart from scores used for scholarships', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Ava')
    renderAt('/onboarding/student', src)
    await step(1, 4)
    await user.click(screen.getByRole('button', { name: classOf(10) }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: 'Not sure yet' }))
    await user.click(screen.getByRole('button', { name: 'ACT' }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await step(3, 4)
    await user.click(screen.getByRole('button', { name: 'Yes, a full practice test' }))
    await user.type(screen.getByLabelText('ACT Composite (1–36)'), '24')
    await user.type(screen.getByLabelText('Test date'), '2026-09-01')
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await step(4, 4)
    await user.click(screen.getByRole('button', { name: 'Tue' }))
    await user.click(screen.getByRole('button', { name: /^5 min/ }))
    await user.click(screen.getByRole('button', { name: 'Accept this plan' }))
    await screen.findByRole('heading', { name: "You're set, Ava" })
    const me = (await src.getHouseholdContext()).myStudent!
    expect(await src.testScores(me.id)).toEqual([expect.objectContaining({ score_source: 'practice_test', composite: 24, test_date: '2026-09-01' })])
    expect(await src.getPlan(me.id)).toMatchObject({ exam_intent: 'undecided', planned_test_date: null })
  }, 30_000)

  it('invited student: asked only what the parent did not supply, and never the parent-owned plan', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_PARENT, 'Jordan')
    const hh = await src.createHousehold('Home', 'America/Chicago')
    const sid = await src.addStudent(hh, 'Riley', graduationYearFor(11), 11)
    await src.savePlan(sid, { exam_family: 'act', target_score: null, goals: ['raise_score'], daily_minutes: 10 })
    await src.setWeeklyGoal(sid, weekStartOf(localDate(new Date(), 'America/Chicago')), 40, null)
    const inv = await src.createStudentInvitation(hh, sid)
    src.switchPersona(DEMO_STUDENT, 'Riley')
    renderAt(`/join#t=${inv.code}`, src)
    await user.click(await screen.findByRole('button', { name: 'Join' }))

    // One screen: the starting point. Name, graduation year, test and weekly plan came from the parent.
    expect(await screen.findByRole('heading', { name: 'Starting point' })).toBeInTheDocument()
    expect(screen.getByRole('progressbar', { name: 'Step 1 of 1' })).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: "Don't remember the score" }))
    await user.click(screen.getByRole('button', { name: 'Finish' }))

    expect(await screen.findByRole('heading', { name: "You're set, Riley" })).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: /Weekly commitment \(set by your parent or guardian\)/ })).toBeInTheDocument()
    expect(screen.getByText('40 questions a week, Monday to Sunday')).toBeInTheDocument()
    expect(await src.testScores(sid)).toEqual([])
    expect(await src.getPlan(sid)).toMatchObject({ daily_minutes: 10 })
    // The student's own login still can't change the household plan.
    await expect(src.savePlan(sid, { exam_family: 'sat', target_score: null, goals: [], daily_minutes: 5 })).rejects.toThrow(/guardian/)
  }, 30_000)

  it('from /start the role is asked once, on the first screen', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Student (demo)')
    renderAt('/start', src)
    expect(await screen.findByRole('heading', { name: "Who's setting up?" })).toBeInTheDocument()
    expect(screen.getByRole('progressbar', { name: 'Step 1 of 4' })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /invite code/ })).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'I\'m a parent or guardian' }))
    expect(screen.getByLabelText("Your student's first name")).toBeInTheDocument()
    expect(screen.queryByRole('link', { name: /invite code/ })).not.toBeInTheDocument()
  })

  it('invited student whose parent already entered a score goes straight to the next assignment', async () => {
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_PARENT, 'Jordan')
    const hh = await src.createHousehold('Home', 'America/Chicago')
    const sid = await src.addStudent(hh, 'Riley', graduationYearFor(11), 11)
    await src.savePlan(sid, { exam_family: 'act', target_score: 28, goals: ['raise_score'], daily_minutes: 10 })
    await src.addTestScore(sid, { exam_family: 'act', test_date: '2026-06-13', composite: 24, section_scores: {} })
    const inv = await src.createStudentInvitation(hh, sid)
    src.switchPersona(DEMO_STUDENT, 'Riley')
    await src.acceptInvitation(inv.inviteCode)
    renderAt('/onboarding/student', src)
    expect(await screen.findByRole('heading', { name: "You're set, Riley" })).toBeInTheDocument()
    expect(screen.queryByRole('progressbar')).not.toBeInTheDocument()
    expect(screen.getByText('No weekly goal set yet')).toBeInTheDocument()
    expect(screen.getByText(/Ask your parent or guardian to set a weekly goal/)).toBeInTheDocument()
    expect(screen.getByText('28 (a goal, not a prediction)')).toBeInTheDocument()
  }, 30_000)
})

describe('setup on the account (CR-26 mirror)', () => {
  /** Another device: same account data, none of this browser's own keys. */
  const otherDevice = () => {
    for (const k of Object.keys(localStorage)) if (k !== 'pp-demo-v1') localStorage.removeItem(k)
  }

  it("a parent's choices appear on the student's own device, and finished setup isn't asked again elsewhere", async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_PARENT, 'Jordan')
    renderAt('/onboarding/parent', src)
    await step(1, 4)
    await user.type(screen.getByLabelText("Your student's first name"), 'Riley')
    await user.click(screen.getByRole('button', { name: classOf(11) }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: /^SAT/ }))
    await user.click(within(screen.getByRole('region', { name: /When is the SAT/ })).getAllByRole('button')[0]!)
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: 'Not yet' }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    for (const d of ['Tue', 'Thu']) await user.click(await screen.findByRole('button', { name: d }))
    await user.click(screen.getByRole('button', { name: /^20 min/ }))
    await user.click(screen.getByRole('button', { name: 'Accept this plan' }))
    await screen.findByRole('heading', { name: 'Riley is set up' })
    const riley = (await src.getHouseholdContext()).students[0]!
    const inv = await src.createStudentInvitation(riley.household_id!, riley.id)
    cleanup()

    // Riley's phone.
    otherDevice()
    src.switchPersona(DEMO_STUDENT, 'Riley')
    renderAt(`/join#t=${inv.code}`, src)
    await user.click(await screen.findByRole('button', { name: 'Join' }))
    // Nothing left to ask: the parent answered every screen, including the starting point.
    expect(await screen.findByRole('heading', { name: "You're set, Riley" })).toBeInTheDocument()
    expect(screen.queryByRole('progressbar')).not.toBeInTheDocument()
    expect(screen.getByText('Tue, Thu')).toBeInTheDocument()
    expect(screen.getByText('20 minutes')).toBeInTheDocument()
    expect(screen.getByText('SAT')).toBeInTheDocument()
    cleanup()

    // A laptop later: still not asked again.
    otherDevice()
    renderAt('/onboarding/student', src)
    expect(await screen.findByRole('heading', { name: "You're set, Riley" })).toBeInTheDocument()
    expect(screen.queryByRole('progressbar')).not.toBeInTheDocument()
  }, 30_000)

  it('the starting benchmark can be scheduled for later while a short session starts now; a partial benchmark is not a starting point', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Sam')
    const me = await src.createSelfStudentProfile({ displayName: 'Sam', graduationYear: graduationYearFor(11), gradeLevel: 11, independent: false, timeZone: 'UTC' })
    await src.savePlan(me, { exam_family: 'act', target_score: null, goals: ['raise_score'], daily_minutes: 10, study_days: [1, 3], exam_intent: 'act', planned_test_date: null })
    await src.saveSetupProgress(me, { setupCompleted: true, startingPointAnswered: true })
    renderAt('/student', src)
    const bench = await screen.findByRole('region', { name: /Starting benchmark · ACT/ })
    expect(within(bench).getByText(/questions, about \d+ minutes, in one sitting\. It shows which skills to work on first/)).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Start a 5-minute session' })).toHaveAttribute('href', '/student/practice?quick=1')
    await user.click(within(bench).getByRole('button', { name: 'Schedule it for later' }))
    await user.selectOptions(screen.getByLabelText('Benchmark day'), 'Tomorrow')
    await user.selectOptions(screen.getByLabelText('Benchmark time'), '16:30')
    await user.click(screen.getByRole('button', { name: 'Save time' }))
    expect(await within(bench).findByText(/^Scheduled for .+ at 4:30 PM\.$/)).toBeInTheDocument()
    const when = (await src.setupProgress(me))!.benchmarkScheduledFor!
    expect(new Date(when).getUTCHours()).toBe(16)
    cleanup()

    // Start the benchmark, answer one question, leave: nothing counts as the starting point.
    vi.spyOn(window, 'confirm').mockReturnValue(true)
    renderAt('/student/benchmark', src)
    await user.click(await screen.findByRole('button', { name: /^Start/ }, { timeout: 5000 }))
    const radios = await screen.findAllByRole('radio', {}, { timeout: 5000 }).catch(() => [])
    if (radios.length) await user.click(radios[0]!)
    else await user.type(screen.getByLabelText('Your answer'), '1')
    await user.click(await screen.findByRole('button', { name: 'Certain' }))
    await user.click(await screen.findByRole('button', { name: 'Leave benchmark' }))
    cleanup()
    expect(await src.listBenchmarks(me)).toEqual([])
    renderAt('/student', src)
    expect(await screen.findByRole('region', { name: /Starting benchmark · ACT/ })).toBeInTheDocument()
    expect(screen.getByText(/counts only once it's finished/)).toBeInTheDocument()
  }, 30_000)

  it('sessions of 5 to 30 minutes, with the short ones first', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_STUDENT, 'Ava')
    renderAt('/onboarding/student', src)
    await step(1, 4)
    await user.click(screen.getByRole('button', { name: classOf(10) }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: /^ACT/ }))
    await user.click(screen.getAllByRole('button', { name: 'Not sure yet' }).at(-1)!)
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: 'Not yet' }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await step(4, 4)
    const names = screen.getAllByRole('button', { name: /^\d+ min/ }).map((b) => b.textContent)
    expect(names).toEqual(['5 min', '10 minMost students', '15 min', '20 min', '30 min'])
    await user.click(screen.getByRole('button', { name: 'Wed' }))
    await user.click(screen.getByRole('button', { name: /^30 min/ }))
    await user.click(screen.getByRole('button', { name: 'Accept this plan' }))
    await screen.findByRole('heading', { name: "You're set, Ava" })
    const me = (await src.getHouseholdContext()).myStudent!
    expect((await src.getPlan(me.id))!.daily_minutes).toBe(30)
  }, 30_000)
})

describe('demo: "Try it as" the student', () => {
  it('opens the join link as the student, not the student setup', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore())
    src.switchPersona(DEMO_PARENT, 'Jordan')
    const hh = await src.createHousehold('Home', 'America/Chicago')
    await src.addStudent(hh, 'Ben', graduationYearFor(10), 10)
    renderAt('/parent/household', src)
    await user.click(await screen.findByRole('button', { name: /Copy invite link or code instead/ }))
    await user.click(await screen.findByRole('button', { name: /Try it as Ben/ }))
    await user.click(await screen.findByRole('button', { name: 'Join' }))
    expect(await screen.findByRole('heading', { name: 'Starting point' })).toBeInTheDocument()
    expect((await src.getHouseholdContext()).myStudent?.display_name).toBe('Ben')
  }, 30_000)
})
