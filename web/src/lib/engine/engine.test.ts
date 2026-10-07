import { describe, expect, it } from 'vitest'
import { gradeAnswer, parseNumericAnswer } from './grading'
import { recommend, skillEstimates, streakFrom, weeklyProgress, type EngineAttempt } from './analytics'
import { addDays, median, weekStartOf } from './dates'
import { benchmarkAttemptIds, benchmarkImprovement, benchmarkSchedule, computeMetrics, nextBenchmarkDue, nextDifficulty, pacingVerdict, pickNext, planBenchmark, type BenchmarkRecord } from './benchmark'
import { achievements, levelOf, totalXp, xpFor } from './gamify'
import type { AttemptRecord, BenchmarkSummary, PublicQuestion } from '../data/types'

const skills = [
  { id: 's1', skill_key: 'algebra', section: 'math' },
  { id: 's2', skill_key: 'commas', section: 'english' },
]

let seq = 0
function attempt(over: Partial<EngineAttempt>): EngineAttempt {
  seq++
  return {
    id: `a${String(seq).padStart(3, '0')}`,
    question_id: 'q1',
    skill_id: 's1',
    skill_key: 'algebra',
    section: 'math',
    presented_at: '2026-09-28T15:00:00Z',
    submitted_at: '2026-09-28T15:01:00Z',
    elapsed_ms: 60_000,
    active_ms: 55_000,
    expected_time_seconds: 60,
    is_correct: true,
    skipped: false,
    confidence: 3,
    hint_count: 0,
    ai_help_used: false,
    strategy_key: null,
    ...over,
  }
}

describe('grading mirrors grade_answer', () => {
  it('matches choices exactly after trimming', () => {
    expect(gradeAnswer('choice', ['B'], ' B ')).toBe(true)
    expect(gradeAnswer('choice', ['B'], 'b')).toBe(false)
  })
  it('treats equivalent numeric forms as equal', () => {
    for (const v of ['1/2', '2/4', '.5', '0.5']) expect(gradeAnswer('numeric', ['1/2'], v)).toBe(true)
    expect(gradeAnswer('numeric', ['1/2'], '1/0')).toBe(false)
    expect(parseNumericAnswer('abc')).toBeNull()
  })
  it('matches text case-insensitively', () => {
    expect(gradeAnswer('text', ['Paris'], ' paris ')).toBe(true)
  })
})

describe('skill estimates', () => {
  it('returns null flags below 5 attempts', () => {
    const est = skillEstimates([attempt({ is_correct: false }), attempt({ is_correct: false })], skills)
    expect(est[0]!.knowledge_weak).toBeNull()
    expect(est[0]!.pacing_weak).toBeNull()
  })
  it('flags knowledge below 60% and never flags pacing for a wrong-and-slow student', () => {
    const rs = Array.from({ length: 5 }, (_, i) => attempt({ is_correct: i < 2, elapsed_ms: 120_000 }))
    const e = skillEstimates(rs, skills)[0]!
    expect(e.knowledge_weak).toBe(true)
    expect(e.pacing_weak).toBe(false)
  })
  it('flags pacing when accurate but slower than 1.25x', () => {
    const rs = Array.from({ length: 5 }, () => attempt({ elapsed_ms: 90_000 }))
    const e = skillEstimates(rs, skills)[0]!
    expect(e.knowledge_weak).toBe(false)
    expect(e.pacing_weak).toBe(true)
    expect(e.pacing_ratio).toBe(1.5)
  })
  it('ignores skipped attempts', () => {
    expect(skillEstimates([attempt({ skipped: true, is_correct: null })], skills)).toHaveLength(0)
  })
})

describe('streaks', () => {
  const on = (day: string) => attempt({ submitted_at: `${day}T15:00:00Z` })
  it('keeps the current streak alive through yesterday', () => {
    const s = streakFrom([on('2026-09-28'), on('2026-09-29'), on('2026-09-30')], 'UTC', '2026-10-01')
    expect(s).toEqual({ current_streak: 3, longest_streak: 3, last_practice_day: '2026-09-30' })
  })
  it('breaks after a missed day and tracks the longest run', () => {
    const s = streakFrom([on('2026-09-20'), on('2026-09-21'), on('2026-09-22'), on('2026-09-28')], 'UTC', '2026-10-01')
    expect(s.current_streak).toBe(0)
    expect(s.longest_streak).toBe(3)
  })
  it('uses the local calendar day', () => {
    // 03:00 UTC on Oct 1 is still Sep 30 in Los Angeles.
    const s = streakFrom([attempt({ submitted_at: '2026-10-01T03:00:00Z' })], 'America/Los_Angeles', '2026-09-30')
    expect(s.last_practice_day).toBe('2026-09-30')
  })
})

describe('recommender', () => {
  it('orders weak knowledge first, then unseen skills, and fills the time budget greedily', () => {
    const weak = Array.from({ length: 5 }, () => attempt({ question_id: 'q-old', is_correct: false }))
    const est = skillEstimates(weak, skills)
    const plan = recommend(
      [
        { id: 'q-new-skill', skill_id: 's2', expected_time_seconds: 60 },
        { id: 'q-weak', skill_id: 's1', expected_time_seconds: 60 },
        { id: 'q-untagged', skill_id: null, expected_time_seconds: 60 },
        { id: 'q-too-long', skill_id: 's1', expected_time_seconds: 900 },
        { id: 'q-no-time', skill_id: 's1', expected_time_seconds: null },
      ],
      est,
      weak,
      5,
    )
    expect(plan.map((p) => [p.question_id, p.reason])).toEqual([
      ['q-weak', 'weak_knowledge'],
      ['q-new-skill', 'new_skill'],
      ['q-untagged', 'untagged'],
    ])
  })
  it('prefers never-seen questions within a bucket', () => {
    const plan = recommend(
      [
        { id: 'qa', skill_id: 's2', expected_time_seconds: 60 },
        { id: 'qb', skill_id: 's2', expected_time_seconds: 60 },
      ],
      [],
      [attempt({ question_id: 'qa', skill_id: 's2' })],
      5,
    )
    expect(plan[0]!.question_id).toBe('qb')
  })
})

describe('weekly progress', () => {
  it('excludes skips from accuracy and reports goal percent', () => {
    const w = weeklyProgress({
      studentId: 'st',
      weekStart: '2026-09-28',
      timeZone: 'UTC',
      goal: { target_questions: 4, target_minutes: null, goal_mode: 'fixed' },
      attempts: [attempt({}), attempt({ is_correct: false }), attempt({ skipped: true, is_correct: null }), attempt({ submitted_at: '2026-09-20T10:00:00Z' })],
      events: [],
      estimates: [],
      today: '2026-10-01',
    })
    expect(w.questions_submitted).toBe(2)
    expect(w.skipped).toBe(1)
    expect(w.accuracy).toBe(0.5)
    expect(w.goal_progress?.questions_pct).toBe(50)
  })
})

describe('dates', () => {
  it('finds the Monday of a week', () => {
    expect(weekStartOf('2026-10-04')).toBe('2026-09-28')
    expect(weekStartOf('2026-09-28')).toBe('2026-09-28')
    expect(addDays('2026-12-31', 1)).toBe('2027-01-01')
  })
  it('computes percentile_cont-style medians', () => {
    expect(median([1, 3, 2, 4])).toBe(2.5)
    expect(median([])).toBeNull()
  })
})

const q = (id: string, section: string, difficulty: number): PublicQuestion => ({
  id,
  exam_family: 'act',
  section,
  difficulty,
  difficulty_label: null,
  stem: '',
  choices: [],
  answer_format: 'choice',
  expected_time_seconds: 60,
  primary_skill_key: null,
  hint_count: 0,
})

describe('benchmark', () => {
  const pool = [q('m1', 'math', 1), q('m3', 'math', 3), q('m5', 'math', 5), q('e2', 'english', 2)]
  it('picks the closest unused difficulty in the section', () => {
    expect(pickNext(pool, 'math', 4, new Set())!.id).toBe('m3')
    expect(pickNext(pool, 'math', 4, new Set(['m3']))!.id).toBe('m5')
    expect(pickNext(pool, 'science', 3, new Set())).toBeNull()
  })
  it('walks a bounded staircase', () => {
    expect(nextDifficulty(5, true)).toBe(5)
    expect(nextDifficulty(1, false)).toBe(1)
    expect(nextDifficulty(3, null)).toBe(3)
  })
  it('caps the plan by what the pool holds', () => {
    const p = planBenchmark('act', 'initial', pool)
    expect(p.sections).toEqual([
      { section: 'english', count: 1 },
      { section: 'math', count: 3 },
    ])
  })
  it('separates knowledge, pacing, calibration and traps', () => {
    const rec = (over: Partial<BenchmarkRecord>): BenchmarkRecord => ({
      question_id: 'q',
      attempt_id: 'a',
      section: 'math',
      difficulty: 3,
      skill_key: null,
      expected_time_seconds: 60,
      answer: 'A',
      is_correct: true,
      skipped: false,
      elapsed_ms: 60_000,
      active_ms: 60_000,
      confidence: 3,
      strategy_key: null,
      skip_events: 0,
      returns: 0,
      answer_changes: 0,
      trap: null,
      ...over,
    })
    const m = computeMetrics([
      rec({}),
      rec({ is_correct: false, confidence: 3, trap: 'sign_error', active_ms: 120_000 }),
      rec({ skipped: true, is_correct: null, answer: null, confidence: null, skip_events: 1, returns: 1 }),
    ])
    expect(m.answered).toBe(2)
    expect(m.skipped).toBe(1)
    expect(m.accuracy).toBe(0.5)
    expect(m.pacing_ratio).toBe(1.5)
    expect(m.calibration.find((c) => c.confidence === 3)).toEqual({ confidence: 3, answered: 2, correct: 1 })
    expect(m.traps_fallen).toEqual([{ trap: 'sign_error', count: 1 }])
    expect(m.returns).toBe(1)
  })
  it('labels pacing verdicts', () => {
    expect(pacingVerdict(0.1)).toBe('rushed')
    expect(pacingVerdict(1)).toBe('on_pace')
    expect(pacingVerdict(1.3)).toBe('slow')
    expect(pacingVerdict(null)).toBe('unknown')
  })
  it('schedules the next benchmark', () => {
    const now = new Date('2026-10-02T12:00:00Z')
    const b = (kind: BenchmarkSummary['kind'], daysAgo: number) =>
      ({ kind, completed_at: new Date(now.getTime() - daysAgo * 86_400_000).toISOString() }) as BenchmarkSummary
    expect(nextBenchmarkDue([], now)).toEqual({ kind: 'initial', inDays: 0 })
    expect(nextBenchmarkDue([b('initial', 10)], now)).toEqual({ kind: 'mini', inDays: 25 })
    expect(nextBenchmarkDue([b('initial', 80)], now).kind).toBe('mini')
    expect(benchmarkSchedule([b('initial', 80)], now, true).kind).toBe('full')
  })
  it('gives a due date, counts overdue days, and a mini after a recent full resets the mini clock only', () => {
    const now = new Date('2026-10-02T12:00:00Z')
    const b = (kind: BenchmarkSummary['kind'], daysAgo: number) =>
      ({ kind, completed_at: new Date(now.getTime() - daysAgo * 86_400_000).toISOString(), attempt_ids: [] as string[] }) as unknown as BenchmarkSummary
    expect(benchmarkSchedule([b('initial', 10)], now)).toMatchObject({ kind: 'mini', inDays: 25, dueDate: '2026-10-27', overdueDays: 0 })
    expect(benchmarkSchedule([b('initial', 40)], now)).toMatchObject({ kind: 'mini', inDays: 0, overdueDays: 5 })
    expect(benchmarkSchedule([b('initial', 72), b('mini', 3)], now, true)).toMatchObject({ kind: 'full', inDays: 0, overdueDays: 2 })
    // No held-out full form yet: the same history schedules a mini, counted from the last check.
    expect(benchmarkSchedule([b('initial', 72), b('mini', 3)], now)).toMatchObject({ kind: 'mini', inDays: 32 })
    expect(benchmarkSchedule([b('full', 20), b('mini', 3)], now)).toMatchObject({ kind: 'mini', inDays: 32 })
  })
  it('reports improvement since the previous benchmark, by section, without treating it as a score', () => {
    const m = (acc: number, pace: number, ceil: number) =>
      ({ accuracy: acc, pacing_ratio: pace, sections: [{ section: 'math', accuracy: acc, ceiling_difficulty: ceil }] }) as unknown as BenchmarkSummary['metrics']
    const one = { kind: 'initial', completed_at: '2026-08-01T00:00:00Z', attempt_ids: ['a1', 'a2'], metrics: m(0.4, 1.4, 2) } as unknown as BenchmarkSummary
    const two = { kind: 'mini', completed_at: '2026-09-10T00:00:00Z', attempt_ids: ['a3'], metrics: m(0.55, 1.1, 3) } as unknown as BenchmarkSummary
    expect(benchmarkImprovement([one])).toBeNull()
    const c = benchmarkImprovement([two, one])!
    expect([c.from, c.to]).toEqual([one, two])
    expect(c.accuracyPts).toBe(15)
    expect(c.pacingDelta).toBe(-0.3)
    expect(c.sections).toEqual([{ section: 'math', accuracyPts: 15, ceilingDelta: 1 }])
    expect([...benchmarkAttemptIds([one, two])].sort()).toEqual(['a1', 'a2', 'a3'])
  })
})

describe('gamification', () => {
  const rec = (over: Partial<AttemptRecord>): AttemptRecord => ({
    id: 'x',
    question_id: 'q',
    section: 'math',
    skill_key: null,
    submitted_at: '2026-09-28T10:00:00Z',
    elapsed_ms: 30_000,
    expected_time_seconds: 60,
    is_correct: true,
    skipped: false,
    confidence: 3,
    hint_count: 0,
    ...over,
  })
  it('rewards effort, correctness and pace, never skips', () => {
    expect(xpFor(rec({}))).toBe(12)
    expect(xpFor(rec({ is_correct: false }))).toBe(4)
    expect(xpFor(rec({ elapsed_ms: 90_000 }))).toBe(10)
    expect(xpFor(rec({ skipped: true, is_correct: null }))).toBe(0)
    expect(totalXp([rec({}), rec({ is_correct: false })])).toBe(16)
  })
  it('levels every 250 XP', () => {
    expect(levelOf(0).level).toBe(1)
    expect(levelOf(260)).toEqual({ level: 2, into: 10, span: 250 })
  })
  it('derives achievements from recorded data', () => {
    const a = achievements({ attempts: Array.from({ length: 8 }, (_, i) => rec({ submitted_at: `2026-09-28T10:0${i}:00Z` })), benchmarks: [], longestStreak: 3, goalsMet: 0 })
    expect(a.find((x) => x.key === 'hot_hand')!.earned).toBe(true)
    expect(a.find((x) => x.key === 'streak_3')!.earned).toBe(true)
    expect(a.find((x) => x.key === 'baseline')!.earned).toBe(false)
  })
})
