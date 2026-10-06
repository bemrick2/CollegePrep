import { useState } from 'react'
import { Navigate, useNavigate } from 'react-router-dom'
import { realName, useApp } from '../../lib/app'
import { browserTimeZone, localDate, weekStartOf } from '../../lib/engine/dates'
import { Button, Field, Notice, inputClass, cx } from '../../components/ui'
import { StepFrame } from './Stepper'
import { ExamAndTarget, GoalsAndPace, defaultPlanDraft, type PlanDraft } from './PlanFields'
import { GRADES, graduationYearFor, timeZones } from './options'
import { InviteCode } from './InviteCode'
import { StoreBadges } from '../../components/StoreBadges'
import { US_STATES } from '../../lib/engine/residency'
import { writeHomeState } from '../../lib/homeState'

export function ParentOnboarding() {
  const { source, viewer, refresh, setActiveStudentId } = useApp()
  const navigate = useNavigate()
  const [step, setStep] = useState(1)
  const [householdName, setHouseholdName] = useState(realName(viewer) ? `${realName(viewer)}'s household` : '')
  const [tz, setTz] = useState(browserTimeZone())
  const [homeState, setHomeState] = useState('')
  const [studentName, setStudentName] = useState('')
  const [grade, setGrade] = useState<number | null>(null)
  const [plan, setPlan] = useState<PlanDraft>(defaultPlanDraft)
  const [code, setCode] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)

  if (!viewer) return <Navigate to="/" replace />

  const finishSetup = async () => {
    setBusy(true)
    setError(null)
    try {
      const hid = await source.createHousehold(householdName.trim() || 'Our household', tz)
      if (homeState) writeHomeState(hid, homeState)
      const sid = await source.addStudent(hid, studentName.trim(), grade ? graduationYearFor(grade) : null, grade)
      await source.savePlan(sid, { exam_family: plan.exam, target_score: plan.target, goals: plan.goals, daily_minutes: 10 })
      await source.setWeeklyGoal(sid, weekStartOf(localDate(new Date(), tz)), plan.weeklyQuestions, null)
      const invite = await source.createInvitation(hid, 'student', sid)
      setActiveStudentId(sid)
      setCode(invite)
      setStep(4)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Could not finish setup')
    } finally {
      setBusy(false)
    }
  }

  const done = async () => {
    await refresh()
    navigate('/parent')
  }

  if (step === 1)
    return (
      <StepFrame
        step={1}
        total={4}
        title="Let's set up your household"
        subtitle="A household connects guardians and students. You can add another guardian later."
        footer={
          <Button size="lg" block disabled={!householdName.trim()} onClick={() => setStep(2)}>
            Continue
          </Button>
        }
      >
        <div className="grid gap-5">
          <Field label="Household name" htmlFor="hh">
            <input id="hh" className={inputClass} value={householdName} onChange={(e) => setHouseholdName(e.target.value)} placeholder="The Rivera household" />
          </Field>
          <Field label="Home state (optional)" htmlFor="home-state-onb" hint="Picks in-state or out-of-state college prices. You can change it later.">
            <select id="home-state-onb" className={inputClass} value={homeState} onChange={(e) => setHomeState(e.target.value)}>
              <option value="">Prefer not to say</option>
              {US_STATES.map(([c, n]) => (
                <option key={c} value={c}>
                  {n}
                </option>
              ))}
            </select>
          </Field>
          <Field label="Time zone" htmlFor="tz" hint="Streaks and weekly goals reset at local midnight.">
            <select id="tz" className={inputClass} value={tz} onChange={(e) => setTz(e.target.value)}>
              {timeZones().map((z) => (
                <option key={z}>{z}</option>
              ))}
            </select>
          </Field>
        </div>
      </StepFrame>
    )

  if (step === 2)
    return (
      <StepFrame
        step={2}
        total={4}
        title="Who's preparing?"
        subtitle="Add your student. We store grade and graduation year only — never a date of birth."
        onBack={() => setStep(1)}
        footer={
          <Button size="lg" block disabled={!studentName.trim() || grade === null} onClick={() => setStep(3)}>
            Continue
          </Button>
        }
      >
        <div className="grid gap-5">
          <Field label="Student's first name" htmlFor="sn">
            <input id="sn" className={inputClass} value={studentName} onChange={(e) => setStudentName(e.target.value)} autoComplete="off" />
          </Field>
          <div>
            <div className="text-sm font-semibold text-ink">Grade this school year</div>
            <div className="mt-2 grid grid-cols-4 gap-2 sm:grid-cols-7">
              {GRADES.map((g) => (
                <button
                  key={g}
                  type="button"
                  aria-pressed={grade === g}
                  onClick={() => setGrade(g)}
                  className={cx('h-12 rounded-xl border-2 font-semibold tabular', grade === g ? 'border-go bg-go-soft text-ink' : 'border-line bg-surface text-ink-2 hover:border-line-strong')}
                >
                  {g}
                </button>
              ))}
            </div>
            {grade !== null && <p className="mt-2 text-xs text-ink-3">Class of {graduationYearFor(grade)}</p>}
          </div>
        </div>
      </StepFrame>
    )

  if (step === 3)
    return (
      <StepFrame
        step={3}
        total={4}
        title={`Goals for ${studentName.trim() || 'your student'}`}
        subtitle="These shape the daily plan. Your student can adjust them too."
        onBack={() => setStep(2)}
        footer={
          <>
            {error && <Notice tone="bad" className="mb-3">{error}</Notice>}
            <Button size="lg" block disabled={busy} onClick={() => void finishSetup()}>
              {busy ? 'Setting up…' : 'Create household'}
            </Button>
          </>
        }
      >
        <div className="grid gap-8">
          <ExamAndTarget value={plan} onChange={setPlan} who="parent" />
          <GoalsAndPace value={plan} onChange={setPlan} />
        </div>
      </StepFrame>
    )

  return (
    <StepFrame
      step={4}
      total={4}
      title={`Invite ${studentName.trim() || 'your student'}`}
      subtitle="Practice happens on your student's own login, so their history stays theirs. Send them the invite link: it works once, on any device."
      footer={
        <Button size="lg" block onClick={() => void done()}>
          Go to your dashboard
        </Button>
      }
    >
      {code && <InviteCode code={code} />}
      <ol className="mt-6 grid gap-3 text-sm text-ink-2">
        <li className="flex gap-3">
          <Num n={1} /> Your student opens the link on their own phone or computer and creates their account (or enters the code under “I have an invite code”).
        </li>
        <li className="flex gap-3">
          <Num n={2} /> They take a short benchmark — about 30 minutes — to set a baseline.
        </li>
        <li className="flex gap-3">
          <Num n={3} /> You'll see progress, pacing and next steps on your dashboard.
        </li>
      </ol>
      <div className="mt-6 rounded-2xl bg-surface-2 p-4">
        <div className="text-sm font-semibold text-ink">On a phone?</div>
        <p className="mt-0.5 text-sm text-ink-2">You and your student can sign in to the app with these same accounts. Nothing to buy again there.</p>
        <StoreBadges className="mt-1" />
      </div>
    </StepFrame>
  )
}

function Num({ n }: { n: number }) {
  return <span className="grid h-6 w-6 shrink-0 place-items-center rounded-full bg-brand-soft text-xs font-bold text-brand">{n}</span>
}
