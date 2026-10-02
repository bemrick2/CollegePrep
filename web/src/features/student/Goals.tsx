import { useEffect, useState } from 'react'
import { Navigate, useNavigate } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { localDate, weekStartOf } from '../../lib/engine/dates'
import { Button, Notice, PageLoading } from '../../components/ui'
import { ExamAndTarget, GoalsAndPace, defaultPlanDraft, type PlanDraft } from '../onboarding/PlanFields'

/** Edit test, target and weekly goal. Used by a student, or a guardian for the active student. */
export function Goals({ forGuardian = false }: { forGuardian?: boolean }) {
  const { source, ctx, activeStudent } = useApp()
  const student = forGuardian ? activeStudent : (ctx?.myStudent ?? null)
  const navigate = useNavigate()
  const [draft, setDraft] = useState<PlanDraft | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  const tz = student?.time_zone ?? ctx?.households.find((h) => h.id === student?.household_id)?.time_zone ?? 'UTC'

  useEffect(() => {
    if (!student) return
    void Promise.all([source.getPlan(student.id), source.weeklyProgress(student.id, weekStartOf(localDate(new Date(), tz))).catch(() => null)]).then(([p, w]) => {
      const base = defaultPlanDraft()
      setDraft({
        exam: p?.exam_family ?? base.exam,
        target: p ? p.target_score : base.target,
        goals: p?.goals ?? base.goals,
        weeklyQuestions: w?.goal?.target_questions ?? base.weeklyQuestions,
      })
    })
  }, [source, student, tz])

  if (!student) return <Navigate to="/" replace />
  if (!draft) return <PageLoading />

  const save = async () => {
    setBusy(true)
    setError(null)
    try {
      const prev = await source.getPlan(student.id)
      await source.savePlan(student.id, { exam_family: draft.exam, target_score: draft.target, goals: draft.goals, daily_minutes: prev?.daily_minutes ?? 10 })
      await source.setWeeklyGoal(student.id, weekStartOf(localDate(new Date(), tz)), draft.weeklyQuestions, null)
      navigate(forGuardian ? '/parent' : '/student')
    } catch (e) {
      // A student in a household cannot set their own goal; guardians with set_goals can (backend rule).
      setError(e instanceof Error ? e.message : 'Could not save')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="mx-auto max-w-xl">
      <h1 className="display text-[28px] font-semibold text-ink">{forGuardian ? `Goals for ${student.display_name}` : 'Your goals'}</h1>
      <div className="mt-6 grid gap-8">
        <ExamAndTarget value={draft} onChange={setDraft} who={forGuardian ? 'parent' : 'student'} />
        <GoalsAndPace value={draft} onChange={setDraft} />
      </div>
      {error && <Notice tone="bad" className="mt-4">{error}</Notice>}
      <Button size="lg" block className="mt-6" disabled={busy} onClick={() => void save()}>
        {busy ? 'Saving…' : 'Save'}
      </Button>
    </div>
  )
}
