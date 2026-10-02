import type { SkillEstimate, Streak, WeeklyGoal, WeeklyProgress } from '../data/types'
import { addDays, daysBetween, localDate, median } from './dates'

// Pure re-implementations of skill_estimates_internal, streak_internal,
// recommend_internal and student_weekly_progress. Thresholds are the
// backend's v1 rules (docs/HOUSEHOLD_PRACTICE.md); keep them in sync.

export interface EngineAttempt {
  id: string
  question_id: string
  skill_id: string | null
  skill_key: string | null
  section: string
  presented_at: string
  submitted_at: string | null
  elapsed_ms: number | null
  active_ms: number | null
  expected_time_seconds: number | null
  is_correct: boolean | null
  skipped: boolean
  confidence: number | null
  hint_count: number
  ai_help_used: boolean
  strategy_key: string | null
}

export interface EngineEvent {
  attempt_id: string
  kind: 'presented' | 'answered' | 'changed_answer' | 'skipped' | 'returned' | 'hint' | 'ai_help' | 'submitted'
  occurred_at: string
}

export interface EngineQuestion {
  id: string
  skill_id: string | null
  expected_time_seconds: number | null
}

export const KNOWLEDGE_WEAK_BELOW = 0.6
export const PACING_WEAK_ABOVE = 1.25
export const MIN_ATTEMPTS_FOR_FLAGS = 5

const answered = (a: EngineAttempt) => a.submitted_at !== null && !a.skipped

export function skillEstimates(
  attempts: EngineAttempt[],
  skills: { id: string; skill_key: string; section: string }[],
): SkillEstimate[] {
  const bySkill = new Map<string, EngineAttempt[]>()
  for (const a of attempts) {
    if (!answered(a) || !a.skill_id) continue
    const list = bySkill.get(a.skill_id) ?? []
    list.push(a)
    bySkill.set(a.skill_id, list)
  }
  const out: SkillEstimate[] = []
  for (const [skillId, list] of bySkill) {
    const skill = skills.find((s) => s.id === skillId)
    if (!skill) continue
    const recent = [...list]
      .sort((x, y) => (y.submitted_at! < x.submitted_at! ? -1 : y.submitted_at! > x.submitted_at! ? 1 : x.id < y.id ? -1 : 1))
      .slice(0, 30)
    const n = recent.length
    const c = recent.filter((a) => a.is_correct).length
    const ratios = recent
      .filter((a) => a.expected_time_seconds)
      .map((a) => (a.elapsed_ms ?? 0) / (a.expected_time_seconds! * 1000))
    const pace = median(ratios)
    const acc = c / n
    out.push({
      skill_id: skillId,
      skill_key: skill.skill_key,
      section: skill.section,
      attempts: n,
      correct: c,
      accuracy: Math.round(acc * 10000) / 10000,
      median_elapsed_ms: Math.round(median(recent.map((a) => a.elapsed_ms ?? 0)) ?? 0),
      pacing_ratio: pace === null ? null : Math.round(pace * 1000) / 1000,
      knowledge_weak: n >= MIN_ATTEMPTS_FOR_FLAGS ? acc < KNOWLEDGE_WEAK_BELOW : null,
      pacing_weak: n >= MIN_ATTEMPTS_FOR_FLAGS && pace !== null ? acc >= KNOWLEDGE_WEAK_BELOW && pace > PACING_WEAK_ABOVE : null,
    })
  }
  return out.sort((a, b) => (a.section + a.skill_key).localeCompare(b.section + b.skill_key))
}

export function streakFrom(attempts: EngineAttempt[], timeZone: string, asOf: string): Streak {
  const days = [...new Set(attempts.filter(answered).map((a) => localDate(a.submitted_at!, timeZone)))]
    .filter((d) => d <= asOf)
    .sort()
  let longest = 0
  let current = 0
  let run = 0
  for (let i = 0; i < days.length; i++) {
    run = i > 0 && daysBetween(days[i - 1]!, days[i]!) === 1 ? run + 1 : 1
    longest = Math.max(longest, run)
    if (daysBetween(days[i]!, asOf) <= 1 && i === days.length - 1) current = run
  }
  return { current_streak: current, longest_streak: longest, last_practice_day: days.at(-1) ?? null }
}

export type RecommendReason = 'weak_knowledge' | 'weak_pacing' | 'new_skill' | 'review' | 'untagged'

export function recommend(
  questions: EngineQuestion[],
  estimates: SkillEstimate[],
  attempts: EngineAttempt[],
  targetMinutes: number,
): { question_id: string; reason: RecommendReason }[] {
  const lastSeen = new Map<string, string>()
  for (const a of attempts) {
    const prev = lastSeen.get(a.question_id)
    if (!prev || a.presented_at > prev) lastSeen.set(a.question_id, a.presented_at)
  }
  const ranked = questions
    .filter((q) => q.expected_time_seconds)
    .map((q) => {
      const e = estimates.find((s) => s.skill_id === q.skill_id)
      const why: RecommendReason = e?.knowledge_weak
        ? 'weak_knowledge'
        : e?.pacing_weak
          ? 'weak_pacing'
          : !q.skill_id
            ? 'untagged'
            : !e
              ? 'new_skill'
              : 'review'
      const bucket = { weak_knowledge: 0, weak_pacing: 1, new_skill: 2, review: 3, untagged: 4 }[why]
      return { q, why, bucket, seen: lastSeen.get(q.id) ?? null }
    })
    .sort((a, b) => {
      if (a.bucket !== b.bucket) return a.bucket - b.bucket
      if (a.seen !== b.seen) {
        if (a.seen === null) return -1
        if (b.seen === null) return 1
        return a.seen < b.seen ? -1 : 1
      }
      return a.q.id < b.q.id ? -1 : 1
    })
  const budget = targetMinutes * 60
  let used = 0
  const out: { question_id: string; reason: RecommendReason }[] = []
  for (const r of ranked) {
    if (used >= budget) break
    const secs = r.q.expected_time_seconds!
    if (used + secs > budget) continue
    used += secs
    out.push({ question_id: r.q.id, reason: r.why })
  }
  return out
}

export function weeklyProgress(input: {
  studentId: string
  weekStart: string
  timeZone: string
  goal: WeeklyGoal | null
  attempts: EngineAttempt[]
  events: EngineEvent[]
  estimates: SkillEstimate[]
  today: string
}): WeeklyProgress {
  const { weekStart, timeZone, goal, attempts, events, estimates } = input
  const weekEnd = addDays(weekStart, 7)
  const inWeek = (iso: string | null) => {
    if (!iso) return false
    const d = localDate(iso, timeZone)
    return d >= weekStart && d < weekEnd
  }
  const fin = attempts.filter((a) => inWeek(a.submitted_at))
  const sub = fin.filter((a) => !a.skipped)
  const correct = sub.filter((a) => a.is_correct).length
  const totalElapsed = fin.reduce((s, a) => s + (a.elapsed_ms ?? 0), 0)
  const actives = fin.filter((a) => a.active_ms !== null)
  const conf = sub.filter((a) => a.confidence !== null)
  const ev = events.filter((e) => inWeek(e.occurred_at))
  const streak = streakFrom(attempts, timeZone, input.today < addDays(weekStart, 6) ? input.today : addDays(weekStart, 6))

  const bySkillMap = new Map<string, { section: string | null; skill: string | null; list: EngineAttempt[] }>()
  for (const a of sub) {
    const k = `${a.section}|${a.skill_key}`
    const entry = bySkillMap.get(k) ?? { section: a.section, skill: a.skill_key, list: [] }
    entry.list.push(a)
    bySkillMap.set(k, entry)
  }
  const byStrategyMap = new Map<string, { submitted: number; correct: number }>()
  for (const a of sub) {
    if (!a.strategy_key) continue
    const e = byStrategyMap.get(a.strategy_key) ?? { submitted: 0, correct: 0 }
    e.submitted++
    if (a.is_correct) e.correct++
    byStrategyMap.set(a.strategy_key, e)
  }

  return {
    student_id: input.studentId,
    week_start: weekStart,
    time_zone: timeZone,
    goal,
    questions_attempted: attempts.filter((a) => inWeek(a.presented_at)).length,
    questions_submitted: sub.length,
    skipped: fin.filter((a) => a.skipped).length,
    skip_events: ev.filter((e) => e.kind === 'skipped').length,
    returns: ev.filter((e) => e.kind === 'returned').length,
    answer_changes: ev.filter((e) => e.kind === 'changed_answer').length,
    correct,
    accuracy: sub.length ? Math.round((correct / sub.length) * 10000) / 10000 : null,
    total_elapsed_ms: totalElapsed,
    total_active_ms: actives.length ? actives.reduce((s, a) => s + (a.active_ms ?? 0), 0) : null,
    median_elapsed_ms: median(sub.map((a) => a.elapsed_ms ?? 0)),
    avg_confidence: conf.length ? Math.round((conf.reduce((s, a) => s + a.confidence!, 0) / conf.length) * 100) / 100 : null,
    ai_help_attempts: fin.filter((a) => a.ai_help_used).length,
    hints_used: fin.reduce((s, a) => s + a.hint_count, 0),
    goal_progress: goal
      ? {
          questions_pct: goal.target_questions ? Math.round((1000 * sub.length) / goal.target_questions) / 10 : null,
          minutes_pct: goal.target_minutes ? Math.round(totalElapsed / 600 / goal.target_minutes) / 10 : null,
        }
      : null,
    streak: { current: streak.current_streak, longest: streak.longest_streak },
    skill_summary: {
      knowledge_weak: estimates.filter((e) => e.knowledge_weak).map((e) => e.skill_key).sort(),
      pacing_weak: estimates.filter((e) => e.pacing_weak).map((e) => e.skill_key).sort(),
      insufficient_data: estimates.filter((e) => e.knowledge_weak === null).length,
    },
    by_skill: [...bySkillMap.values()]
      .map((e) => ({
        section: e.section,
        skill: e.skill,
        submitted: e.list.length,
        correct: e.list.filter((a) => a.is_correct).length,
        median_elapsed_ms: median(e.list.map((a) => a.elapsed_ms ?? 0)),
      }))
      .sort((a, b) => `${a.section}${a.skill}`.localeCompare(`${b.section}${b.skill}`)),
    by_strategy: [...byStrategyMap.entries()].map(([strategy_key, v]) => ({ strategy_key, ...v })).sort((a, b) => a.strategy_key.localeCompare(b.strategy_key)),
  }
}
