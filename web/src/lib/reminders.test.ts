import { describe, expect, it } from 'vitest'
import { DEFAULT_REMINDERS, nextPossibleReminder, plannedToday, reminderDecision, reminderMessage, settingsProblems, type ReminderContext, type ReminderSettings } from '../../../supabase/functions/_shared/reminders.ts'

const TZ = 'America/Chicago'
const on: ReminderSettings = { ...DEFAULT_REMINDERS, enabled: true, times: ['16:30', '19:00'], maxPerDay: 2 }
// 2026-10-07 is a Wednesday; Chicago is UTC-5 in October.
const at = (local: string) => new Date(`${local}:00-05:00`)
const ctx = (local: string, p: Partial<ReminderContext> = {}): ReminderContext => ({ now: at(local), timeZone: TZ, sentToday: 0, sentThisWeek: 0, lastSentAt: null, practisedToday: 0, weekDone: 0, weeklyGoal: 40, ...p })

describe('practice reminder rules', () => {
  it('sends at a chosen local time, within the sender window only', () => {
    expect(reminderDecision(on, ctx('2026-10-07T16:30'))).toEqual({ reason: 'send', slot: '16:30' })
    expect(reminderDecision(on, ctx('2026-10-07T16:44'))).toEqual({ reason: 'send', slot: '16:30' })
    expect(reminderDecision(on, ctx('2026-10-07T16:45')).reason).toBe('not_a_reminder_time')
    expect(reminderDecision({ ...on, enabled: false }, ctx('2026-10-07T16:30')).reason).toBe('off')
  })

  it('never during quiet hours, school hours, or on days not chosen', () => {
    expect(reminderDecision({ ...on, times: ['22:00'] }, ctx('2026-10-07T22:00')).reason).toBe('quiet_hours')
    expect(reminderDecision({ ...on, times: ['06:30'] }, ctx('2026-10-07T06:30')).reason).toBe('quiet_hours')
    expect(reminderDecision({ ...on, times: ['10:00'] }, ctx('2026-10-07T10:00')).reason).toBe('school_hours')
    // Saturday 10:00 is not a school day.
    expect(reminderDecision({ ...on, times: ['10:00'] }, ctx('2026-10-10T10:00')).reason).toBe('send')
    expect(reminderDecision({ ...on, days: [1, 2] }, ctx('2026-10-07T16:30')).reason).toBe('not_a_reminder_day')
  })

  it('stops once today\'s planned practice is done or the week\'s goal is met', () => {
    expect(plannedToday(on, 40)).toBe(6) // 40 over 7 days
    expect(reminderDecision(on, ctx('2026-10-07T16:30', { practisedToday: 6 })).reason).toBe('practice_done')
    expect(reminderDecision(on, ctx('2026-10-07T16:30', { practisedToday: 5 })).reason).toBe('send')
    expect(reminderDecision(on, ctx('2026-10-07T16:30', { weekDone: 40 })).reason).toBe('week_goal_met')
    // No goal: any practice today counts as done.
    expect(reminderDecision(on, ctx('2026-10-07T16:30', { weeklyGoal: null, practisedToday: 1 })).reason).toBe('practice_done')
  })

  it('respects the daily and weekly limits and a minimum gap', () => {
    expect(reminderDecision(on, ctx('2026-10-07T19:00', { sentToday: 2 })).reason).toBe('daily_limit')
    expect(reminderDecision(on, ctx('2026-10-07T19:00', { sentToday: 1, sentThisWeek: 5 })).reason).toBe('weekly_limit')
    expect(reminderDecision({ ...on, times: ['16:30', '17:30'] }, ctx('2026-10-07T17:30', { sentToday: 1, lastSentAt: at('2026-10-07T16:30').toISOString() })).reason).toBe('too_soon')
  })

  it('"Remind me later" holds reminders until the snooze ends, then sends once at its end', () => {
    const snoozed = { ...on, snoozedUntil: at('2026-10-07T17:45').toISOString() }
    expect(reminderDecision(snoozed, ctx('2026-10-07T16:30')).reason).toBe('snoozed')
    expect(reminderDecision(snoozed, ctx('2026-10-07T17:45'))).toEqual({ reason: 'send', slot: 'snooze' })
    expect(reminderDecision(snoozed, ctx('2026-10-07T18:10')).reason).toBe('not_a_reminder_time')
    // The end of a snooze is still bound by quiet hours.
    expect(reminderDecision({ ...on, snoozedUntil: at('2026-10-07T21:30').toISOString() }, ctx('2026-10-07T21:30')).reason).toBe('quiet_hours')
  })

  it('names times that can never fire, and finds the next possible reminder', () => {
    // 10:00 still fires on weekends (not every reminder day is a school day), so only two problems.
    expect(settingsProblems({ ...on, times: ['22:30', '10:00', '16:20'] })).toEqual(['10:30 PM is inside quiet hours, so no reminder goes out then.', '4:20 PM: choose a time on the quarter hour.'])
    expect(settingsProblems({ ...on, days: [1, 2, 3], times: ['10:00'] })).toEqual(['10:00 AM is during school hours on every reminder day.'])
    expect(settingsProblems({ ...on, times: [] })).toContain('Choose at least one reminder time.')
    const n = nextPossibleReminder(on, at('2026-10-07T17:00'), TZ)!
    expect(n.time).toBe('19:00')
    expect(n.at.toISOString()).toBe(at('2026-10-07T19:00').toISOString())
    expect(nextPossibleReminder({ ...on, times: ['10:00'], days: [1, 2, 3, 4, 5] }, at('2026-10-07T17:00'), TZ)).toBeNull()
  })

  it('friendly wording rotates and never mentions scores', () => {
    expect(reminderMessage(0)).toBe('Got a few minutes? Try a quick practice session.')
    for (let i = 0; i < 6; i++) expect(reminderMessage(i)).not.toMatch(/score|streak|miss|behind/i)
  })
})

describe('one reminder, one device', () => {
  it('a reminder is identified by the local date and slot, or the end of a snooze', async () => {
    const { reminderKey } = await import('../../../supabase/functions/_shared/reminders.ts')
    expect(reminderKey('16:30', at('2026-10-07T16:30'), TZ, null)).toBe('2026-10-07:16:30')
    // 23:30 in Chicago is already the 8th in UTC: the student's own date is used.
    expect(reminderKey('23:30', new Date('2026-10-08T04:30:00Z'), TZ, null)).toBe('2026-10-07:23:30')
    expect(reminderKey('snooze', at('2026-10-07T17:45'), TZ, '2026-10-07T22:45:00.000Z')).toBe('snooze:2026-10-07T22:45:00.000Z')
  })

  it('goes to the device opened most recently; the native app wins a same-day tie', async () => {
    const { deliveryOrder } = await import('../../../supabase/functions/_shared/reminders.ts')
    const laptop = { id: 'laptop', channel: 'webpush' as const, checkedAt: '2026-10-07T20:00:00Z' }
    const phone = { id: 'phone', channel: 'fcm' as const, checkedAt: '2026-10-07T12:00:00Z' }
    const oldTablet = { id: 'tablet', channel: 'webpush' as const, checkedAt: '2026-09-30T12:00:00Z' }
    expect(deliveryOrder([oldTablet, laptop, phone]).map((d) => d.id)).toEqual(['phone', 'laptop', 'tablet'])
    expect(deliveryOrder([oldTablet, { ...phone, checkedAt: '2026-10-01T12:00:00Z' }, laptop]).map((d) => d.id)).toEqual(['laptop', 'phone', 'tablet'])
  })
})
