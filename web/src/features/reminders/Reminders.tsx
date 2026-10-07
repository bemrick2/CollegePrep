import { useEffect, useMemo, useState } from 'react'
import { useApp, useAsync } from '../../lib/app'
import type { ReminderChange, ReminderSettings } from '../../lib/data/source'
import {
  DEFAULT_REMINDERS,
  MAX_TIMES,
  SNOOZE_MINUTES,
  formatTime,
  nextPossibleReminder,
  settingsProblems,
} from '../../../../supabase/functions/_shared/reminders.ts'
import { Button, ButtonLink, cx } from '../../components/ui'
import { PLATFORM_NAME, deviceSupport, enableOnThisDevice, readDeviceState, reportDevice, type DeviceState } from '../../lib/pushDevice'

const DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] as const
const QUARTERS = Array.from({ length: 96 }, (_, i) => `${String(Math.floor(i / 4)).padStart(2, '0')}:${String((i % 4) * 15).padStart(2, '0')}`)
const sameSettings = (a: ReminderSettings, b: ReminderSettings) => JSON.stringify({ ...a, snoozedUntil: null }) === JSON.stringify({ ...b, snoozedUntil: null })

const when = (iso: string) => new Date(iso).toLocaleString(undefined, { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' })

function TimeSelect({ value, onChange, label, disabled }: { value: string; onChange: (v: string) => void; label: string; disabled?: boolean }) {
  return (
    <select aria-label={label} disabled={disabled} value={value} onChange={(e) => onChange(e.target.value)} className="h-10 rounded-lg border border-line-strong bg-surface px-2 text-sm text-ink disabled:opacity-60">
      {QUARTERS.map((q) => (
        <option key={q} value={q}>
          {formatTime(q)}
        </option>
      ))}
    </select>
  )
}

function DayChips({ value, onChange, label, disabled }: { value: number[]; onChange: (v: number[]) => void; label: string; disabled?: boolean }) {
  return (
    <div role="group" aria-label={label} className="grid grid-cols-7 gap-1">
      {DAYS.map((d, i) => {
        const on = value.includes(i + 1)
        return (
          <button
            key={d}
            type="button"
            disabled={disabled}
            aria-pressed={on}
            onClick={() => onChange(on ? value.filter((x) => x !== i + 1) : [...value, i + 1].sort())}
            className={cx('h-10 rounded-lg border-2 text-[13px] font-semibold disabled:opacity-60', on ? 'border-go bg-go-soft text-ink' : 'border-line bg-surface text-ink-2')}
          >
            {d}
          </button>
        )
      })}
    </div>
  )
}

/**
 * Reminder settings for one student. The student's own login and guardians with set-goals can change them. When the
 * student turns reminders off and has a guardian (household, not independent), they're told first that their parent
 * will be notified; "Remind me later" is offered instead, and never notifies anyone.
 */
export function ReminderSettingsPanel({ studentId, name, as, canEdit, hasGuardian, timeZone }: { studentId: string; name: string; as: 'student' | 'guardian'; canEdit: boolean; hasGuardian: boolean; timeZone: string }) {
  const { source } = useApp()
  const saved = useAsync(() => source.reminderSettings(studentId), [source, studentId])
  const [draft, setDraft] = useState<ReminderSettings | null>(null)
  const [confirmOff, setConfirmOff] = useState(false)
  const [status, setStatus] = useState<{ tone: 'info' | 'bad'; text: string } | null>(null)
  const [busy, setBusy] = useState(false)
  useEffect(() => {
    if (saved.data) setDraft(saved.data)
  }, [saved.data])
  const s = draft ?? saved.data ?? DEFAULT_REMINDERS
  const set = (p: Partial<ReminderSettings>) => setDraft({ ...s, ...p })
  const problems = settingsProblems(s)
  const blocking = problems.filter((p) => !/inside quiet hours|during school hours/.test(p))
  const next = useMemo(() => nextPossibleReminder(s, new Date(), timeZone), [s, timeZone])
  const you = as === 'student'
  const snoozed = s.snoozedUntil && Date.parse(s.snoozedUntil) > Date.now() ? s.snoozedUntil : null

  if (!saved.data) return null

  const save = async (next: ReminderSettings, done: string) => {
    setBusy(true)
    setStatus(null)
    try {
      const r = await source.saveReminderSettings(studentId, next)
      setDraft(next)
      saved.reload()
      setStatus({ tone: 'info', text: done + (r.guardiansNotified ? (source.mode === 'demo' ? ' Your parent would be notified (the demo sends no email).' : ' Your parent will be notified.') : '') })
    } catch (e) {
      setStatus({ tone: 'bad', text: e instanceof Error ? e.message : 'Could not save' })
    } finally {
      setBusy(false)
    }
  }

  const turnOff = () => {
    if (you && hasGuardian) setConfirmOff(true)
    else void save({ ...s, enabled: false }, 'Practice reminders are off.')
  }

  const snooze = async () => {
    setBusy(true)
    try {
      const until = await source.snoozeReminders(studentId, SNOOZE_MINUTES)
      setConfirmOff(false)
      setDraft({ ...s, snoozedUntil: until })
      setStatus({ tone: 'info', text: `Okay. Reminders pause until ${new Date(until).toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit' })}. Nobody is notified.` })
    } catch (e) {
      setStatus({ tone: 'bad', text: e instanceof Error ? e.message : 'Could not snooze' })
    } finally {
      setBusy(false)
    }
  }

  return (
    <section aria-labelledby={`rem-${studentId}`} className="grid gap-4">
      <div className="flex items-start justify-between gap-3">
        <div>
          <h3 id={`rem-${studentId}`} className="text-[15px] font-bold text-ink">
            Practice reminders
          </h3>
          <p className="text-sm text-ink-2">
            {saved.data.enabled
              ? snoozed
                ? `On, paused until ${when(snoozed)}.`
                : `On. ${next ? `Next possible reminder: ${next.at.toLocaleString(undefined, { weekday: 'short', hour: 'numeric', minute: '2-digit' })}.` : 'No time can send under these settings.'}`
              : 'Off.'}
            {saved.data.enabled && ' Skipped once today’s practice is done.'}
          </p>
        </div>
        {canEdit && (
          <label className="flex shrink-0 items-center gap-2 text-sm font-semibold text-ink">
            <input
              type="checkbox"
              role="switch"
              aria-checked={saved.data.enabled}
              className="h-5 w-9 accent-[var(--go)]"
              checked={saved.data.enabled}
              disabled={busy}
              onChange={(e) => (e.target.checked ? void save({ ...s, enabled: true, snoozedUntil: null }, 'Practice reminders are on.') : turnOff())}
            />
            {saved.data.enabled ? 'On' : 'Off'}
          </label>
        )}
      </div>

      {confirmOff && (
        <div role="alertdialog" aria-labelledby={`off-${studentId}`} aria-describedby={`offd-${studentId}`} className="rounded-xl border border-warn/30 bg-warn-soft p-4">
          <h4 id={`off-${studentId}`} className="font-semibold text-ink">
            Turn off practice reminders?
          </h4>
          <p id={`offd-${studentId}`} className="mt-1 text-sm text-ink-2">
            Your parent will be notified that you turned off practice reminders.
          </p>
          <p className="mt-1 text-sm text-ink-3">Need a break instead? "Remind me later" pauses them for an hour and doesn't notify anyone.</p>
          <div className="mt-3 flex flex-wrap gap-2">
            <Button variant="danger" size="sm" disabled={busy} onClick={() => (setConfirmOff(false), void save({ ...s, enabled: false }, 'Practice reminders are off.'))}>
              Turn off reminders
            </Button>
            <Button variant="secondary" size="sm" disabled={busy} onClick={() => void snooze()}>
              Remind me later
            </Button>
            <Button variant="ghost" size="sm" onClick={() => setConfirmOff(false)}>
              Keep them on
            </Button>
          </div>
        </div>
      )}

      {status && <p role="status" className={cx('text-sm', status.tone === 'bad' ? 'text-bad' : 'text-ink-2')}>{status.text}</p>}

      {saved.data.enabled && canEdit && (
        <details className="rounded-xl border border-line bg-surface p-3" open={as === 'guardian' ? undefined : true}>
          <summary className="cursor-pointer text-sm font-semibold text-ink">Times, quiet hours and limits</summary>
          <div className="mt-3 grid gap-4 text-sm">
            <div>
              <div className="mb-1 font-semibold text-ink">Remind {you ? 'me' : name} at</div>
              <div className="flex flex-wrap items-center gap-2">
                {s.times.map((t, i) => (
                  <span key={i} className="flex items-center gap-1">
                    <TimeSelect label={`Reminder time ${i + 1}`} value={t} onChange={(v) => set({ times: s.times.map((x, j) => (j === i ? v : x)) })} />
                    {s.times.length > 1 && (
                      <button type="button" aria-label={`Remove ${formatTime(t)}`} className="px-1 text-ink-3 hover:text-ink" onClick={() => set({ times: s.times.filter((_, j) => j !== i) })}>
                        ×
                      </button>
                    )}
                  </span>
                ))}
                {s.times.length < MAX_TIMES && (
                  <button type="button" className="text-sm font-semibold text-go-strong underline dark:text-go" onClick={() => set({ times: [...s.times, '19:00'] })}>
                    Add a time
                  </button>
                )}
              </div>
            </div>
            <div>
              <div className="mb-1 font-semibold text-ink">On these days</div>
              <DayChips label="Reminder days" value={s.days} onChange={(v) => set({ days: v })} />
            </div>
            <div className="flex flex-wrap items-center gap-2">
              <span className="font-semibold text-ink">Quiet hours</span>
              <TimeSelect label="Quiet hours start" value={s.quietStart} onChange={(v) => set({ quietStart: v })} />
              <span>to</span>
              <TimeSelect label="Quiet hours end" value={s.quietEnd} onChange={(v) => set({ quietEnd: v })} />
            </div>
            <div className="grid gap-2">
              <label className="flex items-center gap-2 font-semibold text-ink">
                <input type="checkbox" className="h-4 w-4 accent-[var(--go)]" checked={!!s.schoolStart} onChange={(e) => set(e.target.checked ? { schoolStart: '08:00', schoolEnd: '15:00' } : { schoolStart: null, schoolEnd: null })} />
                No reminders during school
              </label>
              {s.schoolStart && s.schoolEnd && (
                <>
                  <div className="flex flex-wrap items-center gap-2">
                    <TimeSelect label="School starts" value={s.schoolStart} onChange={(v) => set({ schoolStart: v })} />
                    <span>to</span>
                    <TimeSelect label="School ends" value={s.schoolEnd} onChange={(v) => set({ schoolEnd: v })} />
                  </div>
                  <DayChips label="School days" value={s.schoolDays} onChange={(v) => set({ schoolDays: v })} />
                </>
              )}
            </div>
            <div className="flex flex-wrap items-center gap-2">
              <span className="font-semibold text-ink">At most</span>
              <select aria-label="Reminders per day" value={s.maxPerDay} onChange={(e) => set({ maxPerDay: Number(e.target.value) })} className="h-10 rounded-lg border border-line-strong bg-surface px-2">
                {[1, 2, 3].map((n) => (
                  <option key={n} value={n}>
                    {n} a day
                  </option>
                ))}
              </select>
              <select aria-label="Reminders per week" value={s.maxPerWeek} onChange={(e) => set({ maxPerWeek: Number(e.target.value) })} className="h-10 rounded-lg border border-line-strong bg-surface px-2">
                {[1, 2, 3, 4, 5, 6, 7, 10, 14].map((n) => (
                  <option key={n} value={n}>
                    {n} a week
                  </option>
                ))}
              </select>
            </div>
            {problems.length > 0 && (
              <ul className="grid gap-1 text-sm text-warn">
                {problems.map((p) => (
                  <li key={p}>{p}</li>
                ))}
              </ul>
            )}
            <div>
              <Button size="sm" disabled={busy || blocking.length > 0 || sameSettings(s, saved.data)} onClick={() => void save(s, 'Saved.')}>
                Save reminder settings
              </Button>
            </div>
          </div>
        </details>
      )}
      {!canEdit && saved.data.enabled && (
        <p className="text-sm text-ink-3">
          {s.times.map(formatTime).join(', ')}, quiet {formatTime(s.quietStart)}–{formatTime(s.quietEnd)}. Only a guardian with permission to set goals, or {name}, can change these.
        </p>
      )}
    </section>
  )
}

/** This device: can it receive reminders? Distinguishes "blocked in device settings" from "reminders off". */
export function ThisDevice({ remindersOn }: { remindersOn: boolean }) {
  const { source } = useApp()
  const support = deviceSupport()
  const [state, setState] = useState<DeviceState | null>(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState<string | null>(null)
  useEffect(() => {
    void readDeviceState().then(setState)
  }, [])
  const enable = async () => {
    setBusy(true)
    setError(null)
    try {
      const st = await enableOnThisDevice()
      setState(st)
      await reportDevice(source, st)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Could not turn on notifications')
    } finally {
      setBusy(false)
    }
  }
  if (!state) return null
  let line: string
  let action: boolean = false
  if (!support.push) line = support.needsHomeScreen ? 'On iPhone and iPad, reminders work only after you add Prep & Price to your Home Screen (Share, then Add to Home Screen) and open it from there.' : "This browser can't show notifications."
  else if (support.needsHomeScreen) line = 'On iPhone and iPad, reminders work only after you add Prep & Price to your Home Screen (Share, then Add to Home Screen) and open it from there.'
  else if (!support.configured) line = "Notifications aren't switched on for Prep & Price yet. Your reminder settings are saved and start once they are."
  else if (state.permission === 'denied') line = "Notifications are blocked in this browser's or phone's settings, so reminders can't reach this device. That's separate from the reminder switch above: allow notifications for this site in settings, then reopen the app."
  else if (state.permission === 'granted' && state.subscription) line = 'This device gets reminders.'
  else {
    line = 'This device isn’t set up for reminders yet.'
    action = true
  }
  return (
    <div className="rounded-xl bg-surface-2 p-3 text-sm">
      <div className="font-semibold text-ink">This device</div>
      <p className="mt-0.5 text-ink-2">{line}</p>
      {action && remindersOn && (
        <Button size="sm" className="mt-2" disabled={busy} onClick={() => void enable()}>
          Allow notifications on this device
        </Button>
      )}
      {error && <p className="mt-1 text-bad">{error}</p>}
      <p className="mt-2 text-xs text-ink-3">Checked when the app opens. If notifications are turned off in phone settings, the app finds out the next time it's opened here.</p>
    </div>
  )
}

/** For guardians: what each of the student's devices allowed when last opened, and the on/off history. */
export function GuardianReminderStatus({ studentId, name }: { studentId: string; name: string }) {
  const { source } = useApp()
  const devices = useAsync(() => source.studentDevices(studentId), [source, studentId])
  const history = useAsync(() => source.reminderHistory(studentId), [source, studentId])
  const lastOff: ReminderChange | undefined = history.data?.find((c) => !c.enabled && c.by === 'student')
  return (
    <div className="grid gap-2 text-sm">
      {lastOff && (
        <p className="text-ink-2">
          {name} turned off practice reminders on {when(lastOff.at)}.{' '}
          {lastOff.emailedToMeAt
            ? `Emailed to you ${when(lastOff.emailedToMeAt)}.`
            : source.mode === 'demo'
              ? 'Shown here only: the demo never sends email.'
              : lastOff.notifyGuardians
                ? 'Not emailed yet.'
                : 'Not emailed (one email per day at most).'}
        </p>
      )}
      <div>
        <div className="font-semibold text-ink">{name}'s devices</div>
        {devices.data && devices.data.length > 0 ? (
          <ul className="mt-0.5 grid gap-0.5 text-ink-2">
            {devices.data.map((d) => (
              <li key={d.deviceId}>
                {PLATFORM_NAME[d.platform ?? 'other']}:{' '}
                {d.canReceive ? 'notifications allowed' : d.permission === 'denied' ? 'notifications blocked in device settings' : d.permission === 'unsupported' ? "can't show notifications" : d.permission === 'granted' ? 'no longer subscribed' : 'not set up yet'}
                <span className="text-ink-3"> (as of {when(d.checkedAt)})</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="mt-0.5 text-ink-3">None yet. Devices appear after {name} opens the app on them.</p>
        )}
        <p className="mt-1 text-xs text-ink-3">Each device is checked when {name} opens the app on it. Turning notifications off in phone settings shows up only after that.</p>
      </div>
    </div>
  )
}

/**
 * On the student's home: a friendly nudge after a reminder went out today and wasn't acted on, with "Remind me
 * later" for browsers whose notifications have no buttons (iPhone, Safari).
 */
export function ReminderNudge({ studentId, practisedToday }: { studentId: string; practisedToday: boolean }) {
  const { source } = useApp()
  const latest = useAsync(() => source.latestReminder(studentId), [source, studentId])
  const [hidden, setHidden] = useState(false)
  const [note, setNote] = useState<string | null>(null)
  const r = latest.data
  const fresh = r && !r.openedAt && !r.snoozedAt && Date.now() - Date.parse(r.sentAt) < 3 * 3600_000
  if (note) return <p role="status" className="text-sm text-ink-2">{note}</p>
  if (!fresh || hidden || practisedToday) return null
  return (
    <div className="flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-line bg-surface p-4">
      <p className="font-semibold text-ink">Got a few minutes? Try a quick practice session.</p>
      <div className="flex gap-2">
        <ButtonLink to={`/student/practice?quick=1&r=${r.id}`} size="sm">
          Start a quick session
        </ButtonLink>
        <Button
          variant="secondary"
          size="sm"
          onClick={async () => {
            setHidden(true)
            try {
              const until = await source.snoozeReminders(studentId, SNOOZE_MINUTES)
              setNote(`Okay, we'll remind you around ${new Date(until).toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit' })}.`)
            } catch {
              setHidden(false)
            }
          }}
        >
          Remind me later
        </Button>
      </div>
    </div>
  )
}

/**
 * When a student opens the app: read this device's notification permission and report it, so the family sees
 * "blocked in settings" separately from "reminders off". Once per app open; never prompts.
 */
export function useDeviceCheck(enabled: boolean) {
  const { source } = useApp()
  useEffect(() => {
    if (!enabled || !source.supportsReminders) return
    let alive = true
    void readDeviceState().then((st) => {
      if (alive) void reportDevice(source, st).catch(() => {})
    })
    return () => {
      alive = false
    }
  }, [enabled, source])
}
