import { useRef, useState } from 'react'
import { Link, Navigate, useNavigate } from 'react-router-dom'
import { realName, useApp } from '../../lib/app'
import { browserTimeZone, localDate, weekStartOf } from '../../lib/engine/dates'
import { Button, Field, Notice, inputClass, cx } from '../../components/ui'
import { StepFrame } from './Stepper'
import { ExamAndTarget, GoalsAndPace, defaultPlanDraft, type PlanDraft } from './PlanFields'
import { GRADES, graduationYearFor } from './options'

export function StudentOnboarding() {
  const { source, viewer, ctx, refresh } = useApp()
  const navigate = useNavigate()
  const [step, setStep] = useState(1)
  const [name, setName] = useState(realName(viewer))
  const [grade, setGrade] = useState<number | null>(null)
  const [plan, setPlan] = useState<PlanDraft>(defaultPlanDraft)
  const [error, setError] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  const finishing = useRef(false)

  if (!viewer) return <Navigate to="/" replace />
  if (ctx?.myStudent && !finishing.current) return <Navigate to="/student" replace />

  const finish = async () => {
    setBusy(true)
    setError(null)
    try {
      const tz = browserTimeZone()
      const sid = await source.createSelfStudentProfile({
        displayName: name.trim(),
        graduationYear: grade ? graduationYearFor(grade) : null,
        gradeLevel: grade,
        independent: false,
        timeZone: tz,
      })
      await source.savePlan(sid, { exam_family: plan.exam, target_score: plan.target, goals: plan.goals, daily_minutes: 10 })
      await source.setWeeklyGoal(sid, weekStartOf(localDate(new Date(), tz)), plan.weeklyQuestions, null)
      finishing.current = true
      await refresh()
      navigate('/student/benchmark', { replace: true })
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Could not create your profile')
    } finally {
      setBusy(false)
    }
  }

  if (step === 1)
    return (
      <StepFrame
        step={1}
        total={3}
        title="Hey! Let's get you set up."
        subtitle="Takes about a minute. Then a short benchmark shows where you're starting."
        footer={
          <div className="grid gap-3">
            <Button size="lg" block disabled={!name.trim() || grade === null} onClick={() => setStep(2)}>
              Continue
            </Button>
            <Link to="/join" className="text-center text-sm font-semibold text-ink-2 hover:text-ink">
              I have an invite code from a parent
            </Link>
          </div>
        }
      >
        <div className="grid gap-5">
          <Field label="First name" htmlFor="name">
            <input id="name" className={inputClass} value={name} onChange={(e) => setName(e.target.value)} autoComplete="given-name" />
          </Field>
          <div>
            <div className="text-sm font-semibold text-ink">What grade are you in?</div>
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
          </div>
        </div>
      </StepFrame>
    )

  if (step === 2)
    return (
      <StepFrame
        step={2}
        total={3}
        title="Pick your test and target"
        subtitle="Aim where you want to land. We'll show the gap after your benchmark."
        onBack={() => setStep(1)}
        footer={
          <Button size="lg" block onClick={() => setStep(3)}>
            Continue
          </Button>
        }
      >
        <ExamAndTarget value={plan} onChange={setPlan} who="student" />
      </StepFrame>
    )

  return (
    <StepFrame
      step={3}
      total={3}
      title="What are you aiming for?"
      onBack={() => setStep(2)}
      footer={
        <>
          {error && <Notice tone="bad" className="mb-3">{error}</Notice>}
          <Button size="lg" block disabled={busy} onClick={() => void finish()}>
            {busy ? 'Saving…' : 'Start my benchmark'}
          </Button>
        </>
      }
    >
      <GoalsAndPace value={plan} onChange={setPlan} />
    </StepFrame>
  )
}
