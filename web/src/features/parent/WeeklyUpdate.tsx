import { useEffect, useState } from 'react'
import { useApp, useAsync } from '../../lib/app'
import type { AlertPreference } from '../../lib/data/source'
import type { BenchmarkSummary } from '../../lib/data/types'
import { weeklyDigestEmail, type DigestStudent } from '../../../../supabase/functions/send-weekly-digest/digest.ts'
import type { WeeklyPlan } from '../../lib/engine/weeklyPlan'
import { formatShortDate } from '../../lib/engine/dates'
import { Notice } from '../../components/ui'
import { Section } from '../../components/layout'
import { FocusList, LastWeekRecap, NextWeekGoal, PacePill, ThisWeekGoal, WeekStrip, checkSentence, paceSentence, recapSentence } from '../../components/WeekPlan'
import type { WeekRecap } from '../../lib/engine/weeklyPlan'
import type { EmailDelivery } from '../../lib/data/source'

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
  lastCheck = null,
  lastWeek = null,
  recapFirst = false,
  hasGoal = true,
  onRefresh = () => undefined,
}: {
  studentId: string
  name: string
  plan: WeeklyPlan
  canSetGoals: boolean
  skillName: (key: string) => string | null | undefined
  lastPractice: string | null
  lastCheck?: BenchmarkSummary | null
  lastWeek?: WeekRecap | null
  /** Monday to Wednesday: the finished week leads. */
  recapFirst?: boolean
  hasGoal?: boolean
  onRefresh?: () => void
}) {
  const { source } = useApp()
  const quiet = useAsync(() => source.inactiveStudents(), [source])
  const alert = quiet.data?.find((q) => q.studentId === studentId)
  const deliveries = useAsync(() => source.emailDeliveries(), [source])
  return (
    <Section id="week-heading" title={`${name}'s week`} subtitle={`Week of ${formatShortDate(plan.weekStart)}, from recorded practice`}>
      <div className="grid gap-8 lg:grid-cols-[minmax(0,1.2fr)_minmax(0,1fr)] lg:gap-14">
        <div className="grid content-start gap-5">
          {alert && (
            <Notice tone="warn" title={alert.daysInactive == null ? `${name} hasn't practised yet` : `No practice in ${alert.daysInactive} days`}>
              Your alert is set for {alert.thresholdDays} {alert.thresholdDays === 1 ? 'day' : 'days'}. A quick check-in usually restarts the habit.
              <span className="mt-1 block text-xs text-ink-3">{emailedLine(deliveries.data, 'inactivity', studentId)}</span>
            </Notice>
          )}
          {!hasGoal && (
            <ThisWeekGoal studentId={studentId} weekStart={plan.weekStart} lastGoal={lastWeek?.target ?? null} canSet={canSetGoals} name={name} goalsPath="/parent/goals" onSet={onRefresh} />
          )}
          {lastWeek && recapFirst && <LastWeekRecap recap={lastWeek} />}
          <div>
            {lastWeek && recapFirst && <h3 className="mb-1 text-sm font-bold text-ink">This week</h3>}
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
          {lastWeek && !recapFirst && (
            <p className="text-sm text-ink-3">
              <span className="font-semibold text-ink-2">Last week:</span> {recapSentence(lastWeek)}
            </p>
          )}
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
          <EmailUpdates
            deliveries={deliveries.data}
            studentId={studentId}
            name={name}
            onChange={quiet.reload}
            preview={{
              student_id: studentId,
              student_name: name,
              week_start: plan.weekStart,
              goal_questions: plan.target,
              questions_submitted: plan.done,
              days_practised: plan.daysPractised,
              last_practice_at: lastPractice,
              focus: plan.focus.map((f) => ({ skill_name: skillName(f.skillKey) ?? f.skillKey, section: f.section, reason: f.why, accuracy: f.accuracy ?? null, pacing_ratio: f.pacingRatio ?? null })),
              last_check: lastCheck ? { kind: lastCheck.kind, completed_at: lastCheck.completed_at } : null,
              inactivity: alert ? { threshold_days: alert.thresholdDays, days_inactive: alert.daysInactive } : null,
            }}
          />
        </div>
      </div>
    </Section>
  )
}

/**
 * Email updates the parent controls: the inactivity alert and the Monday summary (CR-22). The summary toggle and its
 * preview appear only where the backend stores the choice; the preview is built by the same composer the sender
 * uses, from this week so far.
 */
function EmailUpdates({ studentId, name, onChange, preview, deliveries }: { studentId: string; name: string; onChange: () => void; preview: DigestStudent; deliveries: EmailDelivery[] | null | undefined }) {
  const { source, viewer } = useApp()
  const [pref, setPref] = useState<AlertPreference | null>(null)
  const [saved, setSaved] = useState<'idle' | 'saving' | 'saved' | { error: string }>('idle')
  const [showPreview, setShowPreview] = useState(false)
  const digest = source.supportsWeeklyDigest
  useEffect(() => {
    let alive = true
    const fallback = { enabled: false, inactivityDays: 3, ...(digest ? { weeklyDigest: false } : {}) }
    source
      .getAlertPreference(studentId)
      .then((p) => alive && setPref(p ?? fallback))
      .catch(() => alive && setPref(fallback))
    return () => {
      alive = false
    }
  }, [source, studentId, digest])
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
  const demo = source.mode === 'demo'
  const email = digest ? weeklyDigestEmail({ user_id: viewer?.userId ?? '', email: '', guardian_name: viewer?.displayName ?? null, time_zone: 'UTC', students: [preview] }, window.location.origin, { inProgress: true }) : null
  return (
    <div>
      <h3 className="text-sm font-bold text-ink">Email updates</h3>
      <label className="mt-2 flex items-start gap-3 text-sm text-ink-2">
        <input type="checkbox" className="mt-0.5 h-4 w-4 accent-[var(--go)]" checked={pref.enabled} onChange={(e) => void save({ ...pref, enabled: e.target.checked })} />
        <span>
          Tell me when {name} goes{' '}
          <select
            id={id}
            aria-label="Days without practice"
            className="mx-1 inline-block h-8 rounded-lg border border-line-strong bg-surface px-2 align-middle text-sm text-ink focus:border-focus focus:outline-none focus:ring-2 focus:ring-info/30"
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
      {digest && (
        <label className="mt-2 flex items-start gap-3 text-sm text-ink-2">
          <input type="checkbox" className="mt-0.5 h-4 w-4 accent-[var(--go)]" checked={!!pref.weeklyDigest} onChange={(e) => void save({ ...pref, weeklyDigest: e.target.checked })} />
          <span>Email me a summary of {name}'s week on Mondays.</span>
        </label>
      )}
      <p className="mt-1 text-xs text-ink-3">
        {saved === 'saved' ? 'Saved. ' : ''}
        {demo
          ? 'Demo: your choices are kept, but no email is sent.'
          : digest
            ? 'Alerts are emailed once per stretch without practice; the summary covers the week just finished.'
            : 'For now the alert shows here; email delivery comes later.'}
      </p>
      {typeof saved === 'object' && <p className="text-sm text-bad">{saved.error}</p>}
      <SentLog deliveries={deliveries} demo={demo} studentId={studentId} name={name} />
      {email && (
        <div className="mt-2">
          <button type="button" aria-expanded={showPreview} onClick={() => setShowPreview(!showPreview)} className="text-xs font-semibold text-go-strong underline dark:text-go">
            {showPreview ? 'Hide the email preview' : 'Preview the Monday email'}
          </button>
          {showPreview && (
            <div className="mt-2 rounded-xl border border-line bg-surface-2 p-3" aria-label="Monday email preview" role="region">
              <p className="text-xs text-ink-3">Built from this week so far. The real email covers the full week.</p>
              <p className="mt-2 text-sm font-semibold text-ink">{email.subject}</p>
              <p className="mt-1 whitespace-pre-line text-sm text-ink-2">{email.text}</p>
            </div>
          )}
        </div>
      )}
    </div>
  )
}

/** "Emailed Oct 5" only from the server's delivery record; otherwise say plainly that it was shown here only. */
function emailedLine(d: EmailDelivery[] | null | undefined, kind: EmailDelivery['kind'], studentId: string): string {
  const hit = (d ?? []).find((x) => x.kind === kind && (kind !== 'inactivity' || x.studentId === studentId))
  return hit ? `Also emailed to you ${formatShortDate(hit.sentAt.slice(0, 10))}.` : 'Shown here on the dashboard. Not emailed.'
}

/** What has actually been emailed, from the server's delivery record. Never inferred from settings. */
function SentLog({ deliveries, demo, studentId, name }: { deliveries: EmailDelivery[] | null | undefined; demo: boolean; studentId: string; name: string }) {
  if (deliveries === undefined) return null
  const mine = (deliveries ?? []).filter((d) => d.kind === 'weekly_digest' || d.studentId === studentId).slice(0, 5)
  return (
    <div className="mt-3">
      <h4 className="text-xs font-bold text-ink">Emails sent to you</h4>
      {demo ? (
        <p className="mt-0.5 text-xs text-ink-3">None. The demo never sends email; updates appear only on this dashboard.</p>
      ) : deliveries === null ? (
        <p className="mt-0.5 text-xs text-ink-3">None. Email delivery isn't switched on yet, so updates appear only on this dashboard.</p>
      ) : mine.length === 0 ? (
        <p className="mt-0.5 text-xs text-ink-3">None yet.</p>
      ) : (
        <ul className="mt-0.5 grid gap-0.5 text-xs text-ink-2">
          {mine.map((d) => (
            <li key={`${d.kind}:${d.weekStart ?? d.studentId}:${d.sentAt}`}>
              {d.kind === 'weekly_digest' ? `Weekly summary, week of ${formatShortDate(d.weekStart!)}` : `Inactivity alert about ${name}`}: emailed {formatShortDate(d.sentAt.slice(0, 10))}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
