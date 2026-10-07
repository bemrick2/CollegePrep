// Lives outside src/ because it uses Node APIs (crypto, process) that the app's type settings exclude.
// End-to-end check of LiveSource against a real, disposable copy of the backend (every repository migration plus
// the demo question bank). Skipped unless LOCAL_BACKEND_URL is set, so the normal suite never needs a database:
//
//   scripts/local/live_stack.sh up
//   LOCAL_BACKEND_URL=http://127.0.0.1:54321 npx vitest run scripts/local/liveSource.local.test.ts
//
// Users are fixtures created by live_stack.sh; tokens are signed with the local-only secret, the way Supabase Auth
// would sign them. Never point this at a hosted project.
import { createHash, createHmac } from 'node:crypto'
import { createClient } from '@supabase/supabase-js'
import { beforeAll, describe, expect, it } from 'vitest'
import { QUESTIONS } from '../../src/lib/data/demo/fixtures'
import { addDays, weekStartOf } from '../../src/lib/engine/dates'
import { weeklyPlan } from '../../src/lib/engine/weeklyPlan'
import { projectCosts } from '../../src/lib/engine/costProjection'
import type { CostAssumptions, CostProjectionResult } from '../../src/lib/data/types'
import { LiveSource } from '../../src/lib/data/live/liveSource'

const URL_ = process.env.LOCAL_BACKEND_URL
const SECRET = process.env.LOCAL_JWT_SECRET ?? 'local-only-jwt-secret-at-least-32-characters'
const PARENT = '00000000-0000-4000-a000-0000000000a1'
const STUDENT = '00000000-0000-4000-a000-000000000051'
const OUTSIDER = '00000000-0000-4000-a000-000000000099'
const TZ = 'America/Chicago'

const b64 = (o: unknown) => Buffer.from(JSON.stringify(o)).toString('base64url')
function jwt(sub: string) {
  const now = Math.floor(Date.now() / 1000)
  const body = `${b64({ alg: 'HS256', typ: 'JWT' })}.${b64({ sub, role: 'authenticated', aud: 'authenticated', iat: now, exp: now + 3600 })}`
  return `${body}.${createHmac('sha256', SECRET).update(body).digest('base64url')}`
}
async function as(sub: string) {
  const sb = createClient(URL_!, 'local-anon-key', { auth: { persistSession: false, autoRefreshToken: false } })
  const { error } = await sb.auth.setSession({ access_token: jwt(sub), refresh_token: 'local' })
  if (error) throw error
  return new LiveSource(sb)
}
/** Same deterministic ids as seedFromFixtures.ts, so the test knows each seeded question's right answer. */
const uid = (name: string) => {
  const h = createHash('sha1').update(`collegeprep-local:${name}`).digest('hex')
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-5${h.slice(13, 16)}-a${h.slice(17, 20)}-${h.slice(20, 32)}`
}
/** The server rejects client timings longer than its own clock since the question was shown. */
const pause = () => new Promise((r) => setTimeout(r, 25))
const answerFor = new Map(QUESTIONS.map((q) => [uid(`q:${q.id}`), q.accepted_answers[0]!]))

describe.skipIf(!URL_)('LiveSource against the local backend', () => {
  let parent: LiveSource
  let student: LiveSource
  let householdId = ''
  let studentId = ''
  const weekStart = weekStartOf(new Date().toISOString().slice(0, 10))

  beforeAll(async () => {
    parent = await as(PARENT)
    student = await as(STUDENT)
  })

  it('parent sets up a household, a student, a plan and a weekly goal', async () => {
    expect((await parent.getViewer())?.userId).toBe(PARENT)
    householdId = await parent.createHousehold('Local family', TZ)
    studentId = await parent.addStudent(householdId, 'Maya', 2028, 11)
    await parent.savePlan(studentId, { exam_family: 'act', target_score: 28, goals: [], daily_minutes: 10 })
    await parent.setWeeklyGoal(studentId, weekStart, 20, null)
    const ctx = await parent.getHouseholdContext()
    expect(ctx.students.map((s) => s.id)).toContain(studentId)
    expect(ctx.memberships.find((m) => m.household_id === householdId)?.can_set_goals).toBe(true)
  })

  it('parent opts into inactivity alerts; a student who has never practised shows as inactive', async () => {
    await parent.setAlertPreference(studentId, { enabled: true, inactivityDays: 3 })
    expect(await parent.getAlertPreference(studentId)).toEqual({ enabled: true, inactivityDays: 3 })
    expect((await parent.inactiveStudents()).map((s) => s.studentId)).toContain(studentId)
  })

  it('student joins with the 10-character code; wrong and reused codes are refused', async () => {
    const inv = await parent.createStudentInvitation(householdId, studentId)
    expect(inv.inviteCode).toMatch(/^[A-Z0-9]{5}-[A-Z0-9]{5}$/)
    await expect(student.acceptInvitation('AAAAA-AAAAA')).rejects.toThrow()
    expect(await student.acceptInvitation(inv.inviteCode!.toLowerCase())).toBe(householdId)
    const outsider = await as(OUTSIDER)
    await expect(outsider.acceptInvitation(inv.inviteCode!)).rejects.toThrow()
    const ctx = await student.getHouseholdContext()
    expect(ctx.myStudent?.id).toBe(studentId)
    // The outsider sees nothing of the household.
    expect((await outsider.getHouseholdContext()).students).toEqual([])
  })

  it('student takes the starting benchmark (baseline) and the server scores it', async () => {
    const pool = await student.publishedQuestions('act')
    expect(pool.length).toBeGreaterThan(5)
    const bm = await student.startBenchmark(studentId, 'initial', 'act')
    const used = pool.slice(0, 4)
    const ids: string[] = []
    for (const [i, q] of used.entries()) {
      const a = await student.startAttempt(studentId, q.id, null, bm)
      ids.push(a)
      await pause()
      await student.submitAttempt(a, { answer: i % 2 === 0 ? answerFor.get(q.id)! : 'zz-wrong', activeMs: 5 })
    }
    const done = await student.completeBenchmark(studentId, bm, {
      id: 'client', kind: 'initial', exam_family: 'act', started_at: new Date().toISOString(), completed_at: new Date().toISOString(), attempt_ids: ids, metrics: {} as never,
    })
    expect(done.id).toBe(bm)
    // Scored by the server from the stored attempts: two of four right.
    expect(done.metrics).toMatchObject({ answered: 4, correct: 2, accuracy: 0.5 })
    const list = await student.listBenchmarks(studentId)
    expect(list).toHaveLength(1)
    expect(new Set(list[0]!.attempt_ids)).toEqual(new Set(ids))
  })

  it('student practises a short session and gets explanations after each answer', async () => {
    const session = await student.startSession(studentId, 10, 'act')
    expect(session.items.length).toBeGreaterThan(0)
    for (const item of session.items.slice(0, 5)) {
      const a = await student.startAttempt(studentId, item.question.id, session.id)
      await pause()
      const r = await student.submitAttempt(a, { answer: answerFor.get(item.question.id) ?? 'A', activeMs: 5, confidence: 3 })
      expect(r.accepted_answers.length).toBeGreaterThan(0)
      expect(r.teaching_explanation).toBeTruthy()
    }
    await student.endSession(session.id)
  })

  it('the weekly plan reflects practice, excluding benchmark answers', async () => {
    const [week, history, benchmarks, estimates] = await Promise.all([
      student.weeklyProgress(studentId, weekStart),
      student.attemptHistory(studentId, `${addDays(weekStart, -1)}T00:00:00Z`),
      student.listBenchmarks(studentId),
      student.skillEstimates(studentId),
    ])
    expect(week.questions_submitted).toBeGreaterThanOrEqual(5)
    const plan = weeklyPlan({ today: new Date().toISOString().slice(0, 10), weekStart, tz: TZ, plan: null, week, history, benchmarks, estimates, now: new Date() })
    expect(plan.needsBaseline).toBe(false)
    expect(plan.target).toBe(20)
    expect(plan.days.reduce((n, d) => n + d.answered, 0)).toBe(5)
  })

  it('parent sees the update: no longer inactive, and a next-week suggestion', async () => {
    expect((await parent.inactiveStudents()).map((s) => s.studentId)).not.toContain(studentId)
    const sug = await parent.suggestNextWeekGoal(studentId)
    expect(sug.weekStart).toBe(addDays(weekStart, 7))
    // One week of history is not enough for the server's rule.
    expect(sug.targetQuestions).toBeNull()
    expect(sug.basis).toBe('insufficient_history')
    // The student cannot change the goal their guardian set.
    await expect(student.setWeeklyGoal(studentId, addDays(weekStart, 7), 999, null)).rejects.toThrow()
  })

  it('parent saves schools and picks a primary target; a student in the household sees it', async () => {
    await parent.saveSchool(householdId, 'local-test-university')
    await parent.saveSchool(householdId, 'local-test-college')
    await expect(parent.setPrimarySchool(householdId, 'not-saved')).rejects.toThrow()
    await parent.setPrimarySchool(householdId, 'local-test-college')
    await parent.setPrimarySchool(householdId, 'local-test-university')
    expect(await student.primarySchool(householdId)).toBe('local-test-university')
    await parent.setPrimarySchool(householdId, null)
    expect(await parent.primarySchool(householdId)).toBeNull()
  })

  it('student saves interests; the parent sees the same; the server rejects malformed keys', async () => {
    expect(await parent.interests(studentId)).toEqual({ certainty: null, interests: [] })
    await student.saveInterests(studentId, { certainty: 'few', interests: [{ kind: 'major', key: 'computer-science', focus: true }, { kind: 'area', key: 'engineering' }] })
    await student.saveInterests(studentId, { certainty: 'sure', interests: [{ kind: 'major', key: 'computer-science', focus: true }] })
    expect(await parent.interests(studentId)).toEqual({ certainty: 'sure', interests: [{ kind: 'major', key: 'computer-science', focus: true }] })
    await expect(student.saveInterests(studentId, { certainty: 'sure', interests: [{ kind: 'major', key: 'Not A Key' }] })).rejects.toThrow()
    await expect((await as(OUTSIDER)).saveInterests(studentId, { certainty: 'unsure', interests: [] })).rejects.toThrow()
  })

  it('cost_projection on the server and the demo mirror give the same answer for the same verified records', async () => {
    const keys = ['local-test-university', 'local-test-college']
    const records = await parent.compareInstitutions(keys, '2026-27')
    const cases: CostAssumptions[] = [
      { residency: 'in_state' },
      { residency: 'out_of_state', cost_basis: 'cost_of_attendance', exam_credits: 40, prior_credits: 30 },
      { residency: 'in_state', cost_basis: 'cost_of_attendance', exam_credits: 18, years: 3, credits_per_term: 12 },
      { residency: 'international', exam_credits: 9 },
    ]
    for (const a of cases) {
      const live = await parent.costProjection(studentId, keys, '2026-27', a)
      const mirror = projectCosts(records, '2026-27', a)
      // JSON numbers from Postgres numeric compare by value; drop fields the mirror cannot know (state aid is server-only).
      const norm = (r: CostProjectionResult) =>
        JSON.parse(JSON.stringify(r.institutions.map((i) => ({ ...i, cost: i.cost ? { ...i.cost, last_verified_at: null, source_url: null } : i.cost, not_counted: undefined, levers: i.levers?.map((l) => ({ ...l, caps: l.caps.map((c) => ({ ...c, source_url: null })) })) }))), (_k, v) =>
          typeof v === 'string' && /^-?\d+(\.\d+)?$/.test(v) ? Number(v) : v,
        )
      expect(norm(mirror), JSON.stringify(a)).toEqual(norm(live))
    }
    // The residency rule is in play: 120 planned credits minus 90 at the school leaves 30 outside credits.
    const r = (await parent.costProjection(studentId, ['local-test-university'], '2026-27', { residency: 'out_of_state', exam_credits: 40, prior_credits: 30 })).institutions[0]!
    expect(r.credit_savings).toMatchObject({ outside_credit_max: 30, credits_counted: 30, terms_saved: 2 })
    // The college publishes one price for everyone; an in-state request uses it and says so.
    const cc = (await parent.costProjection(studentId, ['local-test-college'], '2026-27', { residency: 'in_state' })).institutions[0]!
    expect(cc.cost).toMatchObject({ residency: 'not_applicable', residency_requested: 'in_state' })
  })
})
