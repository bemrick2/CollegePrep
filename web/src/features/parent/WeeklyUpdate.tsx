import { useEffect, useState } from 'react'
import { useApp, useAsync } from '../../lib/app'
import type { AlertPreference } from '../../lib/data/source'
import type { WeeklyPlan } from '../../lib/engine/weeklyPlan'
import { formatShortDate } from '../../lib/engine/dates'
import { Notice, cx, inputClass } from '../../components/ui'
import { Section } from '../../components/layout'
import { FocusList, NextWeekGoal, PacePill, WeekStrip, checkSentence, paceSentence } from '../../components/WeekPlan'

/**
 * The parent's weekly accountability view: is the plan happening (days practised, pace against the goal), what the
 * sessions are working on, when the next progress check is, next week's suggested goal, and an inactivity alert
 * the parent controls. Everything is read from recorded practice; nothing is estimated.
 */
export function WeeklyUpdate({
  studentId,
  name,
  plan,
  canSetGoals,
  skillName,
  lastPractice,
}: {
  studentId: string
  name: string
  plan: WeeklyPlan
  canSetGoals: boolean
  skillName: (key: string) => string | null | undefined
  lastPractice: string | null
}) {
  const { source } = useApp()
  const quiet = useAsync(() => source.inactiveStudents(), [source])
  const alert = quiet.data?.find((q) => q.studentId === studentId)
  return (
    <Section id="week-heading" title={`${name}'s week`} subtitle={`Week of ${formatShortDate(plan.weekStart)}, from recorded practice`}>
      <div className="grid gap-8 lg:grid-cols-[minmax(0,1.2fr)_minmax(0,1fr)] lg:gap-14">
        <div className="grid content-start gap-5">
          {alert && (
            <Notice tone="warn" title={alert.daysInactive == null ? `${name} hasn't practised yet` : `No practice in ${alert.daysInactive} days`}>
              Your alert is set for {alert.thresholdDays} {alert.thresholdDays === 1 ? 'day' : 'days'}. A quick check-in usually restarts the habit.
            </Notice>
          )}
          <div>
            <p className="flex flex-wrap items-center gap-2 text-[15px] text-ink">
              <PacePill plan={plan} /> {paceSentence(plan)}
            </p>
            <WeekStrip plan={plan} className="mt-4 max-w-sm" />
            <p className="mt-2 text-sm text-ink-3">
              Practised {plan.daysPractised} of 7 days, {plan.minutesPerSession}-minute sessions.
              {lastPractice ? ` Last practice ${formatShortDate(lastPractice)}.` : ''}
            </p>
          </div>
          <div>
            <h3 className="text-sm font-bold text-ink">Focus this week</h3>
            <p className="mb-2 mt-0.5 text-sm text-ink-3">Sessions lead with the weakest skills the backend has flagged.</p>
            <FocusList plan={plan} skillName={skillName} />
          </div>
        </div>
        <div className="grid content-start gap-5">
          <div>
            <h3 className="text-sm font-bold text-ink">Progress check</h3>
            <p className="mt-1 text-sm text-ink-2">{checkSentence(plan, name)}</p>
          </div>
          <div>
            <h3 className="text-sm font-bold text-ink">Next week</h3>
            <div className="mt-1">
              <NextWeekGoal studentId={studentId} weekStart={plan.weekStart} canSet={canSetGoals} name={name} />
            </div>
          </div>
          <InactivityAlert studentId={studentId} name={name} onChange={quiet.reload} />
        </div>
      </div>
    </Section>
  )
}

function InactivityAlert({ studentId, name, onChange }: { studentId: string; name: string; onChange: () => void }) {
  const { source } = useApp()
  const [pref, setPref] = useState<AlertPreference | null>(null)
  const [saved, setSaved] = useState<'idle' | 'saving' | 'saved' | { error: string }>('idle')
  useEffect(() => {
    let alive = true
    source
      .getAlertPreference(studentId)
      .then((p) => alive && setPref(p ?? { enabled: false, inactivityDays: 3 }))
      .catch(() => alive && setPref({ enabled: false, inactivityDays: 3 }))
    return () => {
      alive = false
    }
  }, [source, studentId])
  if (!pref) return null
  const save = async (next: AlertPreference) => {
    setPref(next)
    setSaved('saving')
    try {
      await source.setAlertPreference(studentId, next)
      setSaved('saved')
      onChange()
    } catch (e) {
      setSaved({ error: e instanceof Error ? e.message : 'Could not save' })
    }
  }
  const id = `alert-days-${studentId}`
  return (
    <div>
      <h3 className="text-sm font-bold text-ink">Inactivity alert</h3>
      <label className="mt-2 flex items-start gap-3 text-sm text-ink-2">
        <input type="checkbox" className="mt-0.5 h-4 w-4 accent-[var(--go)]" checked={pref.enabled} onChange={(e) => void save({ ...pref, enabled: e.target.checked })} />
        <span>
          Tell me when {name} goes{' '}
          <select
            id={id}
            aria-label="Days without practice"
            className={cx(inputClass, 'inline-block h-8 w-auto px-2 py-0 text-sm')}
            value={pref.inactivityDays}
            onChange={(e) => void save({ ...pref, inactivityDays: Number(e.target.value) })}
          >
            {[2, 3, 4, 5, 7, 10, 14].map((d) => (
              <option key={d} value={d}>
                {d}
              </option>
            ))}
          </select>{' '}
          days without practice.
        </span>
      </label>
      <p className="mt-1 text-xs text-ink-3">
        {saved === 'saved' ? 'Saved. ' : ''}For now the alert shows here; email delivery of alerts comes later.
      </p>
      {typeof saved === 'object' && <p className="text-sm text-bad">{saved.error}</p>}
    </div>
  )
}
