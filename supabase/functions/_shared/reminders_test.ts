// Deno unit tests for the shared reminder rules: `deno test supabase/functions/_shared/`.
// No imports beyond the module under test, so they run offline.
import { DEFAULT_REMINDERS, reminderDecision, reminderKey, type ReminderContext, type ReminderSettings } from './reminders.ts'

const TZ = 'America/Chicago'
// 2026-10-07 is a Wednesday; Chicago is UTC-5 in October.
const at = (local: string) => new Date(`${local}:00-05:00`)
const on: ReminderSettings = { ...DEFAULT_REMINDERS, enabled: true, times: ['16:30'], maxPerDay: 1, schoolStart: null, schoolEnd: null }
const ctx = (local: string, p: Partial<ReminderContext> = {}): ReminderContext => ({
  now: at(local), timeZone: TZ, sentToday: 0, sentThisWeek: 0, lastSentAt: null, practisedToday: 0, weekDone: 0, weeklyGoal: 40, ...p,
})

function eq(got: unknown, want: unknown, msg: string) {
  if (JSON.stringify(got) !== JSON.stringify(want)) throw new Error(`${msg}: got ${JSON.stringify(got)}, want ${JSON.stringify(want)}`)
}

// The student got the 16:30 reminder and tapped "Remind me later" (60 minutes).
const sentAt = at('2026-10-07T16:30').toISOString()
const snoozed = { ...on, snoozedUntil: at('2026-10-07T17:30').toISOString() }

Deno.test('"Remind me later" fires at its end after a real reminder: exempt from the daily limit (sentToday 1)', () => {
  eq(reminderDecision(snoozed, ctx('2026-10-07T17:30', { sentToday: 1, sentThisWeek: 1, lastSentAt: sentAt })), { reason: 'send', slot: 'snooze' }, 'snooze end')
})

Deno.test('"Remind me later" is exempt from the daily limit with sentToday 2 and a higher limit', () => {
  const two = { ...snoozed, times: ['12:00', '16:30'], maxPerDay: 2 }
  eq(reminderDecision(two, ctx('2026-10-07T17:30', { sentToday: 2, sentThisWeek: 2, lastSentAt: sentAt })), { reason: 'send', slot: 'snooze' }, 'snooze end')
})

Deno.test('"Remind me later" is exempt from the minimum gap (60 minutes after the last reminder)', () => {
  eq(reminderDecision(snoozed, ctx('2026-10-07T17:35', { sentToday: 1, sentThisWeek: 1, lastSentAt: sentAt })).reason, 'send', 'inside the gap')
})

Deno.test('a snooze is still bound by the weekly limit, quiet hours and practice already done', () => {
  eq(reminderDecision(snoozed, ctx('2026-10-07T17:30', { sentToday: 1, sentThisWeek: 5, lastSentAt: sentAt })).reason, 'weekly_limit', 'weekly')
  eq(reminderDecision({ ...on, snoozedUntil: at('2026-10-07T21:30').toISOString() }, ctx('2026-10-07T21:30', { sentToday: 1, lastSentAt: sentAt })).reason, 'quiet_hours', 'quiet')
  eq(reminderDecision(snoozed, ctx('2026-10-07T17:30', { sentToday: 1, lastSentAt: sentAt, practisedToday: 6 })).reason, 'practice_done', 'practised')
})

Deno.test('a snooze stays one reminder: one key, and nothing once the snooze is used up or its window has passed', () => {
  const k = reminderKey('snooze', at('2026-10-07T17:30'), TZ, snoozed.snoozedUntil)
  eq(reminderKey('snooze', at('2026-10-07T17:44'), TZ, snoozed.snoozedUntil), k, 'same key across the window')
  // After the sent snooze, the sender clears snoozedUntil: the next run is an ordinary slot check.
  eq(reminderDecision(on, ctx('2026-10-07T17:30', { sentToday: 2, lastSentAt: at('2026-10-07T17:30').toISOString() })).reason, 'not_a_reminder_time', 'used up')
  eq(reminderDecision(snoozed, ctx('2026-10-07T17:45', { sentToday: 1, lastSentAt: sentAt })).reason, 'not_a_reminder_time', 'window passed')
})

Deno.test('ordinary reminders keep the daily limit and the minimum gap', () => {
  const two = { ...on, times: ['16:30', '17:30'], maxPerDay: 2 }
  eq(reminderDecision(on, ctx('2026-10-07T16:30', { sentToday: 1 })).reason, 'daily_limit', 'daily (sentToday 1)')
  eq(reminderDecision(two, ctx('2026-10-07T17:30', { sentToday: 2 })).reason, 'daily_limit', 'daily (sentToday 2)')
  eq(reminderDecision(two, ctx('2026-10-07T17:30', { sentToday: 1, lastSentAt: sentAt })).reason, 'too_soon', 'gap')
})
