// Practice reminder rules, shared by the app (settings preview, in-app nudge) and the scheduled sender
// (send-practice-reminders). Pure: no Deno or browser APIs beyond Intl, so both sides apply the same rules.
//
// A reminder goes out only when every rule allows it:
//   - reminders are on, and the student hasn't snoozed them;
//   - it's one of the family's chosen times (or the end of a snooze), on a chosen day;
//   - it isn't quiet hours (overnight by default) or school hours on a school day;
//   - the daily and weekly limits aren't reached, and the last reminder was at least MIN_GAP_MINUTES ago;
//   - the student hasn't already done today's planned practice, and the week's goal isn't met.

export interface ReminderSettings {
  enabled: boolean
  /** Local times, "HH:MM", at most MAX_TIMES. */
  times: string[]
  /** ISO weekdays (1 = Monday) reminders may go out. */
  days: number[]
  /** Quiet hours, local. May wrap midnight (21:00–07:00). */
  quietStart: string
  quietEnd: string
  /** School hours on school days; no reminders inside them. Null start/end: no school hours. */
  schoolDays: number[]
  schoolStart: string | null
  schoolEnd: string | null
  maxPerDay: number
  maxPerWeek: number
  /** "Remind me later": nothing before this instant, then one reminder at it. */
  snoozedUntil: string | null
}

export interface ReminderContext {
  now: Date
  timeZone: string
  sentToday: number
  sentThisWeek: number
  lastSentAt: string | null
  /** Practice answers submitted today, local date, progress checks excluded. */
  practisedToday: number
  /** Questions submitted this week (counts toward the weekly goal, as on the dashboard). */
  weekDone: number
  weeklyGoal: number | null
}

export type ReminderReason =
  | 'send'
  | 'off'
  | 'snoozed'
  | 'not_a_reminder_day'
  | 'not_a_reminder_time'
  | 'quiet_hours'
  | 'school_hours'
  | 'daily_limit'
  | 'weekly_limit'
  | 'too_soon'
  | 'practice_done'
  | 'week_goal_met'

export const MAX_TIMES = 3
export const MIN_GAP_MINUTES = 120
/** The sender runs every SENDER_WINDOW_MINUTES; a time is due if it fell inside the last window. */
export const SENDER_WINDOW_MINUTES = 15
export const SNOOZE_MINUTES = 60
export const QUICK_SESSION_MINUTES = 5
/** Reminder times are chosen on quarter hours. */
export const TIME_STEP_MINUTES = 15

export const DEFAULT_REMINDERS: ReminderSettings = {
  enabled: false,
  times: ['16:30'],
  days: [1, 2, 3, 4, 5, 6, 7],
  quietStart: '21:00',
  quietEnd: '07:00',
  schoolDays: [1, 2, 3, 4, 5],
  schoolStart: '08:00',
  schoolEnd: '15:00',
  maxPerDay: 1,
  maxPerWeek: 5,
  snoozedUntil: null,
}

/** Friendly, never guilt or score talk. Rotated so the same line doesn't repeat every day. */
export const REMINDER_MESSAGES = [
  'Got a few minutes? Try a quick practice session.',
  'Ready for a short practice set? Five minutes is plenty.',
  'A quick practice session is ready whenever you are.',
] as const

export function reminderMessage(n: number): string {
  return REMINDER_MESSAGES[Math.abs(Math.trunc(n)) % REMINDER_MESSAGES.length]!
}

const HHMM = /^([01]\d|2[0-3]):([0-5]\d)$/
export const minutesOf = (hhmm: string): number => {
  const m = HHMM.exec(hhmm)
  if (!m) throw new Error(`Bad time ${hhmm}`)
  return Number(m[1]) * 60 + Number(m[2])
}

/** Local calendar parts of an instant in a time zone. */
export function localParts(at: Date, timeZone: string): { date: string; weekday: number; minutes: number } {
  const f = new Intl.DateTimeFormat('en-US', { timeZone, year: 'numeric', month: '2-digit', day: '2-digit', weekday: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' })
  const p = Object.fromEntries(f.formatToParts(at).map((x) => [x.type, x.value]))
  const weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].indexOf(p.weekday!) + 1
  return { date: `${p.year}-${p.month}-${p.day}`, weekday, minutes: Number(p.hour) * 60 + Number(p.minute) }
}

/** [start, end) in minutes; wraps midnight when end <= start. */
function inRange(m: number, start: number, end: number): boolean {
  return start === end ? false : start < end ? m >= start && m < end : m >= start || m < end
}

export function inQuietHours(s: ReminderSettings, weekday: number, m: number): boolean {
  void weekday
  return inRange(m, minutesOf(s.quietStart), minutesOf(s.quietEnd))
}

export function inSchoolHours(s: ReminderSettings, weekday: number, m: number): boolean {
  if (!s.schoolStart || !s.schoolEnd || !s.schoolDays.includes(weekday)) return false
  return inRange(m, minutesOf(s.schoolStart), minutesOf(s.schoolEnd))
}

/** Today's planned practice: the weekly goal spread over the reminder days; any practice when there's no goal. */
export function plannedToday(s: ReminderSettings, weeklyGoal: number | null): number {
  return weeklyGoal && weeklyGoal > 0 ? Math.ceil(weeklyGoal / Math.max(1, s.days.length)) : 1
}

export function reminderDecision(s: ReminderSettings, c: ReminderContext, windowMinutes = SENDER_WINDOW_MINUTES): { reason: ReminderReason; slot: string | null } {
  if (!s.enabled) return { reason: 'off', slot: null }
  const nowMs = c.now.getTime()
  const snoozeEnd = s.snoozedUntil ? Date.parse(s.snoozedUntil) : NaN
  if (Number.isFinite(snoozeEnd) && nowMs < snoozeEnd) return { reason: 'snoozed', slot: null }
  const { weekday, minutes } = localParts(c.now, c.timeZone)
  const fromSnooze = Number.isFinite(snoozeEnd) && nowMs - snoozeEnd < windowMinutes * 60_000
  const slot = fromSnooze
    ? 'snooze'
    : (s.times.find((t) => {
        const d = minutes - minutesOf(t)
        return d >= 0 && d < windowMinutes
      }) ?? null)
  if (!fromSnooze && !s.days.includes(weekday)) return { reason: 'not_a_reminder_day', slot: null }
  if (!slot) return { reason: 'not_a_reminder_time', slot: null }
  if (inQuietHours(s, weekday, minutes)) return { reason: 'quiet_hours', slot }
  if (inSchoolHours(s, weekday, minutes)) return { reason: 'school_hours', slot }
  if (c.weeklyGoal && c.weekDone >= c.weeklyGoal) return { reason: 'week_goal_met', slot }
  if (c.practisedToday >= plannedToday(s, c.weeklyGoal)) return { reason: 'practice_done', slot }
  if (c.sentToday >= s.maxPerDay) return { reason: 'daily_limit', slot }
  if (c.sentThisWeek >= s.maxPerWeek) return { reason: 'weekly_limit', slot }
  if (c.lastSentAt && nowMs - Date.parse(c.lastSentAt) < MIN_GAP_MINUTES * 60_000) return { reason: 'too_soon', slot }
  return { reason: 'send', slot }
}

/** Problems with chosen settings, worded for the family. Times that can never fire are called out. */
export function settingsProblems(s: ReminderSettings): string[] {
  const out: string[] = []
  if (s.times.length === 0) out.push('Choose at least one reminder time.')
  if (s.times.length > MAX_TIMES) out.push(`Choose at most ${MAX_TIMES} times.`)
  if (s.days.length === 0) out.push('Choose at least one day.')
  if (!(s.maxPerDay >= 1 && s.maxPerDay <= MAX_TIMES)) out.push(`The daily limit is 1 to ${MAX_TIMES}.`)
  if (!(s.maxPerWeek >= 1 && s.maxPerWeek <= 14)) out.push('The weekly limit is 1 to 14.')
  for (const t of s.times) {
    if (!HHMM.test(t)) {
      out.push(`${t} isn't a time.`)
      continue
    }
    const m = minutesOf(t)
    if (m % TIME_STEP_MINUTES !== 0) out.push(`${formatTime(t)}: choose a time on the quarter hour.`)
    if (inRange(m, minutesOf(s.quietStart), minutesOf(s.quietEnd))) out.push(`${formatTime(t)} is inside quiet hours, so no reminder goes out then.`)
    else if (s.schoolStart && s.schoolEnd && s.days.every((d) => s.schoolDays.includes(d)) && inRange(m, minutesOf(s.schoolStart), minutesOf(s.schoolEnd)))
      out.push(`${formatTime(t)} is during school hours on every reminder day.`)
  }
  return out
}

export function formatTime(hhmm: string): string {
  const m = minutesOf(hhmm)
  const h = Math.floor(m / 60)
  const mm = String(m % 60).padStart(2, '0')
  return `${((h + 11) % 12) + 1}:${mm} ${h < 12 ? 'AM' : 'PM'}`
}

/**
 * The next time a reminder could go out under the time rules alone (days, times, quiet and school hours), within a
 * week. Practice, limits and snoozes can still skip it, so callers say "next possible reminder".
 */
export function nextPossibleReminder(s: ReminderSettings, now: Date, timeZone: string): { at: Date; weekday: number; time: string } | null {
  if (!s.enabled || s.times.length === 0) return null
  // Times are on quarter hours (TIME_STEP_MINUTES), so stepping a quarter hour at a time finds every slot,
  // including across daylight-saving changes, in about 800 checks.
  const q = TIME_STEP_MINUTES * 60_000
  const start = Math.ceil(now.getTime() / q) * q
  for (let step = 0; step <= (8 * 24 * 60) / TIME_STEP_MINUTES; step += 1) {
    const at = new Date(start + step * q)
    const { weekday, minutes } = localParts(at, timeZone)
    const t = s.times.find((x) => minutesOf(x) === minutes)
    if (!t || !s.days.includes(weekday) || inQuietHours(s, weekday, minutes) || inSchoolHours(s, weekday, minutes)) continue
    if (s.snoozedUntil && at.getTime() < Date.parse(s.snoozedUntil)) continue
    return { at, weekday, time: t }
  }
  return null
}

// ---------------------------------------------------------------------------------------------------------------
// One reminder, one device: shared by the web and native senders
// ---------------------------------------------------------------------------------------------------------------

/**
 * The identity of one reminder: the student's local date and slot (or the end of a snooze). The database keeps at
 * most one claimed-or-sent delivery per student and key, so overlapping sender runs, retries, and a student with a
 * phone, a tablet and a laptop still get exactly one notification per reminder.
 */
export function reminderKey(slot: string, now: Date, timeZone: string, snoozedUntil: string | null): string {
  return slot === 'snooze' ? `snooze:${snoozedUntil ?? ''}` : `${localParts(now, timeZone).date}:${slot}`
}

export type PushChannel = 'webpush' | 'fcm'

export interface ReminderDevice {
  id: string
  channel: PushChannel
  /** When the app last opened on this device (permission checked then). */
  checkedAt: string
}

/**
 * Which device gets the reminder: the one the student opened most recently, so it lands where they actually are;
 * the native app wins a tie (on the same day) over a browser. The rest are fallbacks, tried in order only if the
 * push service rejects the first, never in addition to it.
 */
export function deliveryOrder<T extends ReminderDevice>(devices: T[]): T[] {
  const day = (iso: string) => iso.slice(0, 10)
  return [...devices].sort((a, b) => {
    if (day(a.checkedAt) === day(b.checkedAt) && a.channel !== b.channel) return a.channel === 'fcm' ? -1 : 1
    return b.checkedAt.localeCompare(a.checkedAt)
  })
}
