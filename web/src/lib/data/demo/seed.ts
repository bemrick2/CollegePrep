import { QUESTIONS } from './fixtures'
import { emptyStore, type DemoAttempt, type DemoEvent, type DemoStore } from './store'
import { DEMO_PARENT, DEMO_STUDENT } from './demoSource'
import { addDays, browserTimeZone, localDate, weekStartOf } from '../../engine/dates'
import { computeMetrics, type BenchmarkRecord } from '../../engine/benchmark'
import type { Confidence } from '../types'

// A deterministic sample household so the parent and student views have
// history to show. Everything here is synthetic and labelled as demo data.

function rng(seed: number) {
  let s = seed >>> 0
  return () => {
    s = (s * 1664525 + 1013904223) >>> 0
    return s / 2 ** 32
  }
}

const SECTION_PROFILE: Record<string, { acc: number; pace: number }> = {
  english: { acc: 0.82, pace: 0.9 },
  reading: { acc: 0.7, pace: 1.05 },
  math: { acc: 0.6, pace: 1.45 },
  science: { acc: 0.64, pace: 1.1 },
}

export function sampleFamily(viewer: 'parent' | 'student', now = new Date()): DemoStore {
  const s = emptyStore()
  const tz = browserTimeZone()
  const rand = rng(20261002)
  const today = localDate(now, tz)
  const hid = 'h-sample'
  const sid = 'st-sample-maya'

  s.users.push({ id: DEMO_PARENT, displayName: 'Elena Rivera' }, { id: DEMO_STUDENT, displayName: 'Maya Rivera' })
  s.viewerId = viewer === 'parent' ? DEMO_PARENT : DEMO_STUDENT
  s.households.push({ id: hid, name: 'Rivera household', time_zone: tz })
  s.members.push(
    { household_id: hid, user_id: DEMO_PARENT, role: 'guardian', can_manage_students: true, can_set_goals: true, can_view_progress: true, can_manage_members: true, can_manage_billing: true },
    { household_id: hid, user_id: DEMO_STUDENT, role: 'student', can_manage_students: false, can_set_goals: false, can_view_progress: false, can_manage_members: false, can_manage_billing: false },
  )
  s.students.push({
    id: sid,
    household_id: hid,
    display_name: 'Maya',
    graduation_year: now.getFullYear() + 2,
    grade_level: 11,
    account_mode: 'student_login',
    is_independent: false,
    linked_user_id: DEMO_STUDENT,
    time_zone: null,
    archived_at: null,
  })
  s.plans[sid] = { exam_family: 'act', target_score: 27, goals: ['merit', 'college_credit'], daily_minutes: 10 }

  const thisWeek = weekStartOf(today)
  for (let w = 3; w >= 0; w--) {
    s.goals.push({ id: `g-${w}`, student_id: sid, week_start: addDays(thisWeek, -7 * w), target_questions: w >= 2 ? 35 : 40, target_minutes: null, goal_mode: 'fixed' })
  }

  const pool = QUESTIONS.filter((q) => q.exam_family === 'act')
  const attempts: DemoAttempt[] = []
  const events: DemoEvent[] = []
  let n = 0

  const addAttempt = (day: string, minuteOffset: number, q: (typeof pool)[number], progress: number, sessionId: string | null) => {
    const prof = SECTION_PROFILE[q.section] ?? { acc: 0.7, pace: 1 }
    const pCorrect = Math.min(0.95, prof.acc + 0.12 * progress - (q.difficulty - 3) * 0.08)
    const skipped = rand() < 0.04
    const correct = skipped ? null : rand() < pCorrect
    const pace = prof.pace * (1 - 0.15 * progress) * (0.7 + rand() * 0.6)
    const elapsed = Math.round(q.expected_time_seconds * 1000 * pace)
    const presented = new Date(new Date(`${day}T16:00:00`).getTime() + minuteOffset * 60_000)
    const submitted = new Date(presented.getTime() + elapsed)
    const id = `pa-sample-${++n}`
    const conf = (correct ? (rand() < 0.6 ? 3 : 2) : rand() < 0.5 ? 1 : 2) as Confidence
    attempts.push({
      id,
      student_id: sid,
      session_id: sessionId,
      question_id: q.id,
      skill_id: `sk-${q.primary_skill_key}`,
      skill_key: q.primary_skill_key,
      section: q.section,
      presented_at: presented.toISOString(),
      submitted_at: submitted.toISOString(),
      elapsed_ms: elapsed,
      active_ms: Math.round(elapsed * 0.92),
      expected_time_seconds: q.expected_time_seconds,
      is_correct: correct,
      skipped,
      confidence: skipped ? null : conf,
      hint_count: rand() < 0.1 ? 1 : 0,
      ai_help_used: false,
      strategy_key: rand() < 0.5 ? (q.strategies.find((x) => x.is_fastest)?.strategy_key ?? null) : null,
      selected_answer: skipped ? null : correct ? (q.accepted_answers[0] ?? null) : (q.distractors[0]?.choice ?? null),
      attempt_number: attempts.filter((a) => a.question_id === q.id).length + 1,
      last_answer: null,
    })
    events.push({ attempt_id: id, student_id: sid, kind: 'presented', occurred_at: presented.toISOString() })
    if (!skipped && rand() < 0.08) events.push({ attempt_id: id, student_id: sid, kind: 'changed_answer', occurred_at: submitted.toISOString() })
    events.push({ attempt_id: id, student_id: sid, kind: skipped ? 'skipped' : 'submitted', occurred_at: submitted.toISOString() })
    return attempts.at(-1)!
  }

  // Initial benchmark 24 days ago: 6 questions per section, adaptive-looking difficulty spread.
  const benchDay = addDays(today, -24)
  const benchRecords: BenchmarkRecord[] = []
  let minute = 0
  for (const section of ['english', 'math', 'reading', 'science']) {
    const qs = pool.filter((q) => q.section === section).slice(0, 6)
    for (const q of qs) {
      const a = addAttempt(benchDay, minute++, q, 0, null)
      benchRecords.push({
        question_id: q.id,
        attempt_id: a.id,
        section,
        difficulty: q.difficulty,
        skill_key: q.primary_skill_key,
        expected_time_seconds: q.expected_time_seconds,
        answer: a.selected_answer,
        is_correct: a.is_correct,
        skipped: a.skipped,
        elapsed_ms: a.elapsed_ms!,
        active_ms: a.active_ms!,
        confidence: a.confidence as Confidence | null,
        strategy_key: a.strategy_key,
        skip_events: a.skipped ? 1 : 0,
        returns: 0,
        answer_changes: 0,
        trap: a.is_correct === false ? (q.distractors[0]?.trap ?? null) : null,
      })
    }
  }
  const benchAt = new Date(`${benchDay}T17:00:00`).toISOString()
  s.benchmarks[sid] = [
    { id: 'bm-sample-1', kind: 'initial', exam_family: 'act', started_at: benchAt, completed_at: benchAt, attempt_ids: benchRecords.map((r) => r.attempt_id), metrics: computeMetrics(benchRecords) },
  ]

  // Daily practice, most days, ending yesterday so today's plan is still open.
  for (let d = 23; d >= 1; d--) {
    if (rand() < 0.22 && d > 3) continue
    const day = addDays(today, -d)
    const count = 5 + Math.floor(rand() * 5)
    const progress = (23 - d) / 23
    for (let i = 0; i < count; i++) {
      const q = pool[Math.floor(rand() * pool.length)]!
      addAttempt(day, i * 2, q, progress, `ps-sample-${d}`)
    }
  }

  s.attempts = attempts
  s.events = events
  // No practice_estimate rows: the backend does not produce scaled-score estimates (CR-3), so neither does the demo.
  return s
}
