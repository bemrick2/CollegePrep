import { describe, expect, it } from 'vitest'
import { proposeFirstWeek } from './firstWeek'

const base = { minutesPerSession: 10, weeklyQuestions: 40, needsBaseline: true, baseline: { questions: 27, minutes: 30 }, secondsPerQuestion: 60, freshAvailable: 200 }

describe('proposeFirstWeek', () => {
  it('puts the starting benchmark first, today, and spreads the rest of the goal over the remaining study days', () => {
    // 2026-10-05 is a Monday.
    const w = proposeFirstWeek({ ...base, today: '2026-10-05', studyDays: [1, 3, 5] })
    expect(w.next).toEqual({ kind: 'check', date: '2026-10-05', minutes: 30 })
    expect(w.days.map((d) => [d.label, d.check ? 'check' : d.questions])).toEqual([
      ['Mon', 'check'],
      ['Tue', 0],
      ['Wed', 7],
      ['Thu', 0],
      ['Fri', 7],
      ['Sat', 0],
      ['Sun', 0],
    ])
    // The goal itself is never changed: a full week is 40 over 3 days.
    expect(w.fullWeekPerDay).toBe(14)
    expect(w.partialWeek).toBe(false)
  })

  it('says plainly when the chosen time is less than the goal usually takes, without lowering the goal', () => {
    const w = proposeFirstWeek({ ...base, today: '2026-10-05', studyDays: [1, 2], minutesPerSession: 5 })
    expect(w.minutesCommitted).toBe(10)
    expect(w.minutesNeeded).toBe(40)
    expect(w.shortOfTime).toBe(true)
    expect(w.fullWeekPerDay).toBe(20)
  })

  it('a week already under way is partial; without a baseline need the next practice day is the assignment', () => {
    // Saturday: only Sunday is left among Mon/Wed/Sun.
    const w = proposeFirstWeek({ ...base, needsBaseline: false, today: '2026-10-10', studyDays: [1, 3, 7] })
    expect(w.days.map((d) => d.label)).toEqual(['Sat', 'Sun'])
    expect(w.partialWeek).toBe(true)
    expect(w.next).toMatchObject({ kind: 'practice', date: '2026-10-11', questions: 40 })
    expect(w.days[1]!.overSession).toBe(true)
  })

  it('flags a bank with fewer new questions than the goal, and unknown times stay unknown', () => {
    const w = proposeFirstWeek({ ...base, today: '2026-10-05', studyDays: [1, 2, 3, 4, 5], freshAvailable: 12, secondsPerQuestion: null })
    expect(w.freshShort).toBe(true)
    expect(w.minutesNeeded).toBeNull()
    expect(w.shortOfTime).toBe(false)
  })
})
