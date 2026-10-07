import { describe, expect, it } from 'vitest'
import type { AttemptRecord, BenchmarkSummary, SkillEstimate, WeeklyProgress } from '../data/types'
import { showRecap, suggestNextWeek, suggestionReason, weekRecap, weeklyPlan } from './weeklyPlan'

const tz = 'America/Chicago'
const at = (date: string, n: number, id = `${date}-${n}`): AttemptRecord =>
  ({ id, question_id: 'q', section: 'math', skill_key: 'k', submitted_at: `${date}T17:00:00Z`, elapsed_ms: 60000, expected_time_seconds: 60, is_correct: true, skipped: false, confidence: null }) as AttemptRecord
const week = (target: number | null, done: number): WeeklyProgress =>
  ({ goal: target == null ? null : { target_questions: target, target_minutes: null, goal_mode: 'fixed' }, questions_submitted: done }) as unknown as WeeklyProgress
const est = (skill_key: string, o: Partial<SkillEstimate>): SkillEstimate =>
  ({ skill_id: skill_key, skill_key, section: 'math', attempts: 10, correct: 5, accuracy: 0.5, median_elapsed_ms: 60000, pacing_ratio: 1, knowledge_weak: false, pacing_weak: false, ...o }) as SkillEstimate
const bench = (completed_at: string, ids: string[] = [], kind: BenchmarkSummary['kind'] = 'initial'): BenchmarkSummary =>
  ({ id: completed_at, kind, exam_family: 'act', started_at: completed_at, completed_at, attempt_ids: ids, metrics: {} }) as unknown as BenchmarkSummary

describe('weekly plan', () => {
  // Wednesday 2026-10-07; week starts Monday 2026-10-05.
  const base = { today: '2026-10-07', weekStart: '2026-10-05', tz, plan: { exam_family: 'act' as const, target_score: 27, goals: [], daily_minutes: 10 } }

  it('marks practised, missed, today and upcoming days, ignoring benchmark answers', () => {
    const history = [at('2026-10-05', 1), at('2026-10-05', 2), at('2026-10-06', 1, 'bench-1')]
    const p = weeklyPlan({ ...base, week: week(35, 2), history, benchmarks: [bench('2026-10-06T18:00:00Z', ['bench-1'])], estimates: [], now: new Date('2026-10-07T18:00:00Z') })
    expect(p.days.map((d) => d.status)).toEqual(['done', 'missed', 'today', 'upcoming', 'upcoming', 'upcoming', 'upcoming'])
    expect(p.days[0]!.answered).toBe(2)
    expect(p.daysPractised).toBe(1)
  })

  it('paces the goal over seven days with the dashboard rule and says what finishes it', () => {
    const b = [bench('2026-09-30T18:00:00Z')]
    const now = new Date('2026-10-07T18:00:00Z')
    expect(weeklyPlan({ ...base, week: week(35, 15), history: [], benchmarks: b, estimates: [], now })).toMatchObject({ expectedByToday: 15, pace: 'on_track', perDayToFinish: 4 })
    expect(weeklyPlan({ ...base, week: week(35, 5), history: [], benchmarks: b, estimates: [], now }).pace).toBe('behind')
    expect(weeklyPlan({ ...base, week: week(35, 20), history: [], benchmarks: b, estimates: [], now }).pace).toBe('ahead')
    expect(weeklyPlan({ ...base, week: week(35, 40), history: [], benchmarks: b, estimates: [], now })).toMatchObject({ pace: 'met', perDayToFinish: 0 })
    expect(weeklyPlan({ ...base, week: week(null, 3), history: [], benchmarks: b, estimates: [], now })).toMatchObject({ pace: 'no_goal', perDayToFinish: null, expectedByToday: null })
  })

  it('focuses on knowledge gaps (lowest accuracy first), then pacing, at most three', () => {
    const estimates = [
      est('a', { knowledge_weak: true, accuracy: 0.55 }),
      est('b', { knowledge_weak: true, accuracy: 0.4 }),
      est('c', { pacing_weak: true, pacing_ratio: 1.6 }),
      est('d', { pacing_weak: true, pacing_ratio: 1.9 }),
      est('e', { knowledge_weak: false }),
    ]
    const p = weeklyPlan({ ...base, week: week(35, 0), history: [], benchmarks: [bench('2026-10-01T00:00:00Z')], estimates, now: new Date('2026-10-07T18:00:00Z') })
    expect(p.focus.map((f) => [f.skillKey, f.why])).toEqual([
      ['b', 'knowledge'],
      ['a', 'knowledge'],
      ['d', 'pacing'],
    ])
  })

  it('puts the progress check on its due day, or today when overdue; none before a baseline', () => {
    const now = new Date('2026-10-07T18:00:00Z')
    const due = weeklyPlan({ ...base, week: week(35, 0), history: [], benchmarks: [bench('2026-09-04T18:00:00Z')], estimates: [], now })
    expect(due.check).toMatchObject({ kind: 'mini', dueDate: '2026-10-09', thisWeek: true, overdueDays: 0 })
    expect(due.days.find((d) => d.check)?.date).toBe('2026-10-09')
    const late = weeklyPlan({ ...base, week: week(35, 0), history: [], benchmarks: [bench('2026-08-20T18:00:00Z')], estimates: [], now })
    expect(late.check.overdueDays).toBeGreaterThan(0)
    expect(late.days.find((d) => d.check)?.date).toBe('2026-10-07')
    const fresh = weeklyPlan({ ...base, week: week(35, 0), history: [], benchmarks: [], estimates: [], now })
    expect(fresh.needsBaseline).toBe(true)
    expect(fresh.days.some((d) => d.check)).toBe(false)
  })
})

describe('next-week suggestion (mirrors suggest_next_week_goal v1)', () => {
  it('needs two weeks with a goal', () => {
    expect(suggestNextWeek('2026-10-12', [{ target: 40, done: 40 }, { target: null, done: 3 }])).toMatchObject({ targetQuestions: null, basis: 'insufficient_history' })
  })
  it('steps up 10% at full completion, holds at 70%+, eases 15% below', () => {
    expect(suggestNextWeek('2026-10-12', [{ target: 40, done: 44 }, { target: 40, done: 40 }]).targetQuestions).toBe(44)
    expect(suggestNextWeek('2026-10-12', [{ target: 40, done: 30 }, { target: 40, done: 32 }]).targetQuestions).toBe(40)
    expect(suggestNextWeek('2026-10-12', [{ target: 40, done: 10 }, { target: 40, done: 12 }]).targetQuestions).toBe(34)
    expect(suggestNextWeek('2026-10-12', [{ target: 4, done: 0 }, { target: 4, done: 0 }]).targetQuestions).toBe(5)
  })
  it('explains itself in plain words', () => {
    expect(suggestionReason(suggestNextWeek('2026-10-12', [{ target: 40, done: 44 }, { target: 40, done: 40 }]))).toMatch(/steps up/)
    expect(suggestionReason(suggestNextWeek('2026-10-12', []))).toMatch(/Not enough finished weeks/)
  })
})

describe('last week recap', () => {
  const base = { weekStart: '2026-09-28', tz, plan: { exam_family: 'act' as const, target_score: 27, goals: [], daily_minutes: 10 }, benchmarks: [], estimates: [] }
  it('counts the finished week with the same rules, Sunday included, nothing "today"', () => {
    const history = [at('2026-09-28', 1), at('2026-09-30', 1), at('2026-10-04', 1), at('2026-10-04', 2)]
    const r = weekRecap({ ...base, week: week(20, 18), history })
    expect(r).toMatchObject({ target: 20, done: 18, met: false, shortBy: 2, daysPractised: 3 })
    expect(r.days.map((d) => d.status)).toEqual(['done', 'missed', 'done', 'missed', 'missed', 'missed', 'done'])
    expect(r.days.some((d) => d.check)).toBe(false)
  })
  it('met and no-goal weeks', () => {
    expect(weekRecap({ ...base, week: week(10, 12), history: [] })).toMatchObject({ met: true, shortBy: null })
    expect(weekRecap({ ...base, week: week(null, 4), history: [] })).toMatchObject({ met: null, shortBy: null, target: null })
  })
  it('leads Monday to Wednesday only', () => {
    expect(showRecap('2026-10-05', '2026-10-05')).toBe(true)
    expect(showRecap('2026-10-07', '2026-10-05')).toBe(true)
    expect(showRecap('2026-10-08', '2026-10-05')).toBe(false)
  })
})
