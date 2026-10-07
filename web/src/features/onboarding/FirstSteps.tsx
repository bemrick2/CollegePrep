import { useState } from 'react'
import { useApp } from '../../lib/app'
import { addDays, localDate } from '../../lib/engine/dates'
import { QUICK_SESSION_MINUTES, formatTime } from '../../../../supabase/functions/_shared/reminders.ts'
import { Button, ButtonLink, cx } from '../../components/ui'
import { EXAM_NAME } from './options'
import type { ExamFamily } from '../../lib/data/types'

const QUARTERS = Array.from({ length: 64 }, (_, i) => {
  const m = 6 * 60 + i * 15 // 6:00 AM to 9:45 PM
  return `${String(Math.floor(m / 60)).padStart(2, '0')}:${String(m % 60).padStart(2, '0')}`
})

/** "Thu, Oct 8 at 4:30 PM" in the student's time zone. */
export function scheduledLabel(iso: string, timeZone: string) {
  const d = new Date(iso)
  return `${d.toLocaleDateString(undefined, { weekday: 'short', month: 'short', day: 'numeric', timeZone })} at ${d.toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit', timeZone })}`
}

/** A local date + "HH:MM" in a time zone, as an instant (searches the two candidate UTC offsets around it). */
export function zonedInstant(date: string, hhmm: string, timeZone: string): Date {
  const guess = new Date(`${date}T${hhmm}:00Z`)
  for (let off = -14 * 60; off <= 14 * 60; off += 15) {
    const t = new Date(guess.getTime() - off * 60_000)
    const p = new Intl.DateTimeFormat('en-CA', { timeZone, year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).formatToParts(t)
    const v = Object.fromEntries(p.map((x) => [x.type, x.value]))
    if (`${v.year}-${v.month}-${v.day}` === date && `${v.hour}:${v.minute}` === hhmm) return t
  }
  return guess
}

/**
 * The two ways to begin, kept apart: a short practice session now, and the starting benchmark, now or at a time
 * the student picks. Only a finished benchmark counts as the starting point; a partly done one doesn't.
 */
export function FirstSteps({
  studentId,
  exam,
  baseline,
  scheduledFor,
  timeZone,
  canStart,
  name,
  onScheduled,
}: {
  studentId: string
  exam: ExamFamily
  baseline: { questions: number; minutes: number } | null
  scheduledFor: string | null
  timeZone: string
  /** The student's own login (a guardian sees the plan, not the buttons). */
  canStart: boolean
  name: string
  onScheduled?: (iso: string | null) => void
}) {
  const { source } = useApp()
  const [picking, setPicking] = useState(false)
  const today = localDate(new Date(), timeZone)
  const [day, setDay] = useState(addDays(today, 1))
  const [time, setTime] = useState('16:30')
  const [when, setWhen] = useState<string | null>(scheduledFor)
  const [error, setError] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  const you = canStart
  const length = baseline ? `${baseline.questions} questions, about ${baseline.minutes} minutes, in one sitting` : 'About 30 minutes, in one sitting'

  const save = async (iso: string | null) => {
    setBusy(true)
    setError(null)
    try {
      await source.saveSetupProgress(studentId, { benchmarkScheduledFor: iso })
      setWhen(iso)
      setPicking(false)
      onScheduled?.(iso)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Could not save')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="grid gap-4">
      <section aria-labelledby="quick-heading" className="rounded-2xl border-2 border-go bg-go-soft p-4">
        <h2 id="quick-heading" className="text-lg font-semibold text-ink">
          Quick practice · {QUICK_SESSION_MINUTES} minutes
        </h2>
        <p className="mt-1 text-sm text-ink-2">
          A short mixed set to get going {you ? 'now' : `whenever ${name} likes`}. It counts toward this week's goal. Practice is aimed at specific skills once the benchmark is done.
        </p>
        {canStart && (
          <ButtonLink to="/student/practice?quick=1" size="md" className="mt-3">
            Start a {QUICK_SESSION_MINUTES}-minute session
          </ButtonLink>
        )}
      </section>

      <section aria-labelledby="bench-heading" className="rounded-2xl border border-line bg-surface p-4">
        <h2 id="bench-heading" className="text-lg font-semibold text-ink">
          Starting benchmark · {EXAM_NAME[exam]}
        </h2>
        <p className="mt-1 text-sm text-ink-2">
          {length}. It shows which skills to work on first, so the weekly plan can aim at them. It's practice, not an {EXAM_NAME[exam]} score, and it counts only once it's finished.
        </p>
        {when && <p className="mt-2 text-sm font-semibold text-ink">Scheduled for {scheduledLabel(when, timeZone)}.</p>}
        {canStart && (
          <div className="mt-3 flex flex-wrap gap-2">
            <ButtonLink to="/student/benchmark" variant="secondary" size="sm">
              Start the benchmark now
            </ButtonLink>
            <Button variant="ghost" size="sm" onClick={() => setPicking(!picking)} aria-expanded={picking}>
              {when ? 'Change the time' : 'Schedule it for later'}
            </Button>
            {when && (
              <Button variant="ghost" size="sm" disabled={busy} onClick={() => void save(null)}>
                Clear schedule
              </Button>
            )}
          </div>
        )}
        {picking && (
          <div className="mt-3 flex flex-wrap items-center gap-2 text-sm">
            <select aria-label="Benchmark day" value={day} onChange={(e) => setDay(e.target.value)} className="h-10 rounded-lg border border-line-strong bg-surface px-2">
              {Array.from({ length: 14 }, (_, i) => addDays(today, i)).map((d, i) => (
                <option key={d} value={d}>
                  {i === 0 ? 'Today' : i === 1 ? 'Tomorrow' : new Date(`${d}T12:00:00Z`).toLocaleDateString(undefined, { weekday: 'short', month: 'short', day: 'numeric', timeZone: 'UTC' })}
                </option>
              ))}
            </select>
            <select aria-label="Benchmark time" value={time} onChange={(e) => setTime(e.target.value)} className="h-10 rounded-lg border border-line-strong bg-surface px-2">
              {QUARTERS.map((q) => (
                <option key={q} value={q}>
                  {formatTime(q)}
                </option>
              ))}
            </select>
            <Button
              size="sm"
              disabled={busy}
              onClick={() => {
                const at = zonedInstant(day, time, timeZone)
                if (at.getTime() <= Date.now()) {
                  setError('Pick a time that hasn’t passed yet.')
                  return
                }
                void save(at.toISOString())
              }}
            >
              Save time
            </Button>
          </div>
        )}
        {error && <p className={cx('mt-2 text-sm text-bad')}>{error}</p>}
      </section>
    </div>
  )
}
