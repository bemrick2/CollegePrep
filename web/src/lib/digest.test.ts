import { describe, expect, it } from 'vitest'
import { inactivityEmail, lastCompletedWeekStart, weeklyDigestEmail, type DigestRecipient, type DigestStudent } from '../../../supabase/functions/send-weekly-digest/digest.ts'

const maya: DigestStudent = {
  student_id: 's1',
  student_name: 'Maya',
  week_start: '2026-09-28',
  goal_questions: 20,
  questions_submitted: 18,
  days_practised: 4,
  last_practice_at: '2026-10-03T22:10:00Z',
  focus: [
    { skill_name: 'Linear equations', section: 'math', reason: 'knowledge', accuracy: 0.45, pacing_ratio: 1.1 },
    { skill_name: 'Punctuation', section: 'english', reason: 'pacing', accuracy: 0.8, pacing_ratio: 1.6 },
  ],
  last_check: { kind: 'initial', completed_at: '2026-09-01T17:00:00Z' },
  inactivity: null,
}
const r: DigestRecipient = { user_id: 'u1', email: 'parent@example.test', guardian_name: 'Dana Rivera', time_zone: 'America/Chicago', students: [maya] }

describe('weekly summary email', () => {
  it('says what happened, in plain numbers, with no score', () => {
    const m = weeklyDigestEmail(r, 'https://app.example')
    expect(m.subject).toBe("Maya's week on Prep & Price: 18 of 20 questions")
    expect(m.text).toContain('Hi Dana,')
    expect(m.text).toContain('Here is the week of Sep 28.')
    expect(m.text).toContain('18 of 20 practice questions (goal not met), practised on 4 days of 7.')
    expect(m.text).toContain('- Linear equations (Math): 45% right in practice')
    expect(m.text).toContain('- Punctuation (English): answering at 1.6× test pace')
    expect(m.text).toContain('Last progress check: Starting benchmark, Sep 1.')
    expect(m.text).toContain('Open the parent dashboard: https://app.example/parent')
    expect(m.text).toContain('not an ACT or SAT score')
    expect(m.text + m.html).not.toMatch(/predict|estimated score|on track to score|composite/i)
  })

  it('a week still in progress is not called a missed goal (in-app preview)', () => {
    const m = weeklyDigestEmail(r, 'https://app.example', { inProgress: true })
    expect(m.text).toContain('18 of 20 practice questions (week in progress), practised on 4 days of 7 so far.')
    expect(m.text).not.toContain('goal not met')
  })

  it('leads with an inactivity line only when that alert is on and reached', () => {
    const quiet = { ...maya, questions_submitted: 0, days_practised: 0, inactivity: { threshold_days: 3, days_inactive: 6 } }
    const m = weeklyDigestEmail({ ...r, students: [quiet] }, 'https://app.example')
    expect(m.text).toContain("Maya hasn't practised since Oct 3 (6 days).")
    expect(m.html).toContain('color:#8a4b00')
  })

  it('handles no goal, no baseline and several students', () => {
    const leo: DigestStudent = { ...maya, student_id: 's2', student_name: 'Leo', goal_questions: null, questions_submitted: 1, days_practised: 1, focus: [], last_check: null }
    const m = weeklyDigestEmail({ ...r, students: [maya, leo] }, 'https://app.example')
    expect(m.subject).toBe("Your family's week on Prep & Price (week of Sep 28)")
    expect(m.text).toContain('1 practice question, practised on 1 day of 7. No weekly goal was set.')
    expect(m.text).toContain('No starting benchmark yet.')
    expect(m.text).toContain('No weak skills flagged yet')
  })

  it('escapes names in HTML', () => {
    const m = weeklyDigestEmail({ ...r, students: [{ ...maya, student_name: '<b>Maya</b>' }] }, 'https://app.example')
    expect(m.html).toContain('&lt;b&gt;Maya&lt;/b&gt;')
    expect(m.html).not.toContain('<b>Maya</b>')
  })
})

describe('inactivity alert email', () => {
  it('states the stretch and why it was sent', () => {
    const m = inactivityEmail({ user_id: 'u1', email: 'p@example.test', guardian_name: null, student_name: 'Maya', threshold_days: 3, days_inactive: 4, last_practice_at: '2026-10-03T22:10:00Z', time_zone: 'America/Chicago' }, 'https://app.example')
    expect(m.subject).toBe("Maya hasn't practised in 4 days")
    expect(m.text).toContain("Maya hasn't practised since Oct 3. You asked to hear after 3 days without practice.")
    expect(m.text).toContain('once per stretch')
  })
})

describe('which week', () => {
  it('summarizes the last completed Monday-to-Sunday week', () => {
    expect(lastCompletedWeekStart(new Date('2026-10-05T13:00:00Z'))).toBe('2026-09-28') // Monday
    expect(lastCompletedWeekStart(new Date('2026-10-07T13:00:00Z'))).toBe('2026-09-28') // Wednesday
    expect(lastCompletedWeekStart(new Date('2026-10-04T23:00:00Z'))).toBe('2026-09-21') // Sunday
  })
})
