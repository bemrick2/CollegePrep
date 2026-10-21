// Lives outside src/ because it uses Node APIs (crypto).
//
// The three account journeys end to end against the local disposable backend (every repository migration plus the
// CR-26 reference SQL): a parent with an invited student and two other guardians, and a student who signs up alone.
// Each `device()` is a separate client for the same account, so "another device" means nothing carried over but the
// login. Skipped unless LOCAL_BACKEND_URL is set (scripts/local/live_stack.sh test).
//
// What this can't show: Supabase Auth sign-up and email confirmation (the local auth is a stub), and the invitation
// email itself. Those need hosted (launch checklist A6).
import { createHmac } from 'node:crypto'
import { createClient } from '@supabase/supabase-js'
import { beforeAll, describe, expect, it } from 'vitest'
import { LiveSource } from '../../src/lib/data/live/liveSource'
import { weekStartOf } from '../../src/lib/engine/dates'
import { examKey, type PlannedExam } from '../../src/lib/engine/examCredit'

const URL_ = process.env.LOCAL_BACKEND_URL
const SECRET = process.env.LOCAL_JWT_SECRET ?? 'local-only-jwt-secret-at-least-32-characters'
const PARENT = '00000000-0000-4000-a000-0000000000a7'
const CO_GUARDIAN = '00000000-0000-4000-a000-0000000000a8'
const VIEWER = '00000000-0000-4000-a000-0000000000a9'
const INVITED = '00000000-0000-4000-a000-000000000057'
const SOLO = '00000000-0000-4000-a000-000000000056'
const OUTSIDER = '00000000-0000-4000-a000-000000000099'

const b64 = (o: unknown) => Buffer.from(JSON.stringify(o)).toString('base64url')
function jwt(sub: string) {
  const now = Math.floor(Date.now() / 1000)
  const body = `${b64({ alg: 'HS256', typ: 'JWT' })}.${b64({ sub, role: 'authenticated', aud: 'authenticated', iat: now, exp: now + 3600 })}`
  return `${body}.${createHmac('sha256', SECRET).update(body).digest('base64url')}`
}
async function client(sub: string) {
  const sb = createClient(URL_!, 'local-anon-key', { auth: { persistSession: false, autoRefreshToken: false } })
  const { error } = await sb.auth.setSession({ access_token: jwt(sub), refresh_token: 'local' })
  if (error) throw error
  return sb
}
/** A separate client for the same account: a different device. */
const device = async (sub: string) => new LiveSource(await client(sub), { accountSetup: true, examPlan: true })
const week = weekStartOf(new Date().toISOString().slice(0, 10))

describe.skipIf(!URL_)('parent journey with an invited student and two more guardians', () => {
  let hh = ''
  let studentId = ''

  beforeAll(async () => {
    // Parent: the four setup screens' answers (student, test, starting point, schedule), saved to the account.
    const parent = await device(PARENT)
    hh = await parent.createHousehold('Journey family', 'America/Chicago')
    studentId = await parent.addStudent(hh, 'Jordan', 2029, 10)
    await parent.savePlan(studentId, { exam_family: 'act', target_score: 26, goals: ['raise_score'], daily_minutes: 10, exam_intent: 'act', planned_test_date: '2027-04-10', study_days: [1, 3, 5] })
    await parent.saveSetupProgress(studentId, { startingPointAnswered: true })
  })

  it('setup resumes on another device where it stopped, and is never asked again once finished', async () => {
    const laptop = await device(PARENT)
    // Stopped after the starting-point screen: not finished, so the laptop resumes rather than restarting.
    expect(await laptop.setupProgress(studentId)).toMatchObject({ setupCompletedAt: null, startingPointAnsweredAt: expect.any(String) })
    expect(await laptop.getPlan(studentId)).toMatchObject({ exam_family: 'act', daily_minutes: 10, study_days: [1, 3, 5] })
    await laptop.saveSetupProgress(studentId, { setupCompleted: true })
    await laptop.setWeeklyGoal(studentId, week, 30, null)
    const phone = await device(PARENT)
    expect((await phone.setupProgress(studentId))!.setupCompletedAt).toBeTruthy()
  })

  it('the invited student joins with the code and sees the guardian’s choices on every device, without being asked again', async () => {
    const parent = await device(PARENT)
    const inv = await parent.createStudentInvitation(hh, studentId)
    await (await device(INVITED)).acceptInvitation(inv.inviteCode!)
    for (const d of [await device(INVITED), await device(INVITED)]) {
      const ctx = await d.getHouseholdContext()
      expect(ctx.students.find((s) => s.id === studentId)).toMatchObject({ linked_user_id: INVITED })
      expect(await d.getPlan(studentId)).toMatchObject({ exam_family: 'act', target_score: 26, daily_minutes: 10 })
      expect((await d.setupProgress(studentId))!.setupCompletedAt).toBeTruthy()
    }
    // The code is single use.
    await expect((await device(OUTSIDER)).acceptInvitation(inv.inviteCode!)).rejects.toThrow()
  })

  it('the student practises quickly and schedules the benchmark separately; a started benchmark is not a finished one', async () => {
    const phone = await device(INVITED)
    const quick = await phone.startSession(studentId, 5, 'act')
    expect(quick.items.length).toBeGreaterThan(0)
    const when = new Date(Date.now() + 3 * 86_400_000).toISOString()
    await phone.saveSetupProgress(studentId, { benchmarkScheduledFor: when })
    const started = await phone.startBenchmark(studentId, 'initial', 'act')
    expect(started).toBeTruthy()
    // Not completed, so no device lists it as a result.
    expect(await (await device(INVITED)).listBenchmarks(studentId)).toEqual([])
    expect(await (await device(PARENT)).listBenchmarks(studentId)).toEqual([])
    expect(Date.parse((await (await device(PARENT)).setupProgress(studentId))!.benchmarkScheduledFor!)).toBe(Date.parse(when))
  })

  it('the student cannot change what the guardian chose', async () => {
    const phone = await device(INVITED)
    await expect(phone.savePlan(studentId, { exam_family: 'sat', target_score: null, goals: [], daily_minutes: 5 })).rejects.toThrow()
    await expect(phone.setWeeklyGoal(studentId, week, 5, null)).rejects.toThrow()
    expect(await (await device(PARENT)).getPlan(studentId)).toMatchObject({ exam_family: 'act', daily_minutes: 10 })
  })

  it('guardian permissions: a default co-guardian may set goals but not manage members; a view-only guardian sees progress and changes nothing', async () => {
    const parent = await device(PARENT)
    // Default guardian invitation: manage students, set goals, view progress.
    await (await device(CO_GUARDIAN)).acceptInvitation(await parent.createInvitation(hh, 'guardian'))
    const co = await device(CO_GUARDIAN)
    await co.setWeeklyGoal(studentId, week, 35, null)
    await expect(co.createInvitation(hh, 'guardian')).rejects.toThrow()
    // A view-only guardian (the server accepts an explicit permission list).
    const { data: code, error } = await (await client(PARENT)).rpc('create_household_invitation', { p_household: hh, p_role: 'guardian', p_student: null, p_ttl_hours: 72, p_permissions: ['view_progress'] })
    expect(error).toBeNull()
    await (await device(VIEWER)).acceptInvitation(code as string)
    const viewer = await device(VIEWER)
    expect(await viewer.getPlan(studentId)).toMatchObject({ exam_family: 'act' })
    await expect(viewer.setWeeklyGoal(studentId, week, 10, null)).rejects.toThrow()
    await expect(viewer.savePlan(studentId, { exam_family: 'sat', target_score: null, goals: [], daily_minutes: 5 })).rejects.toThrow()
    await expect(viewer.saveSetupProgress(studentId, { benchmarkScheduledFor: null })).rejects.toThrow()
    const ctx = await viewer.getHouseholdContext()
    expect(ctx.memberships.find((m) => m.household_id === hh)).toMatchObject({ can_view_progress: true, can_set_goals: false, can_manage_members: false })
  })

  it('CR-10: AP and CLEP exams saved by the parent show on the student’s devices; IB stays on the device; permissions hold', async () => {
    const exam = (family: PlannedExam['family'], name: string, score: number | null): PlannedExam => ({ family, key: examKey(family, name), name, score })
    const parent = await device(PARENT)
    await parent.saveExamPlanEntry(studentId, exam('AP', 'AP Calculus AB', 4))
    await parent.saveExamPlanEntry(studentId, exam('CLEP', 'CLEP College Algebra', null))
    // No canonical key for IB yet: refused as 'invalid', so the app keeps it on the device.
    await expect(parent.saveExamPlanEntry(studentId, { ...exam('IB', 'IB Economics', 5), level: 'SL' })).rejects.toMatchObject({ code: 'invalid' })
    // The server checks the AP scale.
    await expect(parent.saveExamPlanEntry(studentId, exam('AP', 'AP Statistics', 7))).rejects.toThrow()
    const phone = await device(INVITED)
    expect((await phone.examPlan(studentId)).sort((a, b) => a.key.localeCompare(b.key))).toEqual([
      { family: 'AP', key: examKey('AP', 'Calculus AB'), name: 'AP Calculus AB', score: 4 },
      { family: 'CLEP', key: examKey('CLEP', 'College Algebra'), name: 'CLEP College Algebra', score: null },
    ])
    // The linked student may record their own score.
    await phone.saveExamPlanEntry(studentId, exam('CLEP', 'College Algebra', 62))
    const viewer = await device(VIEWER)
    expect((await viewer.examPlan(studentId)).find((e) => e.family === 'CLEP')!.score).toBe(62)
    // Current server rule (CR-10 can_edit_student_plans): ANY guardian of the household may edit the exam plan and
    // interests, whatever their permissions. A view-only guardian can therefore add an exam. Raised with Research as
    // a question, not changed here; this assertion pins today's behaviour so a change is deliberate.
    await viewer.saveExamPlanEntry(studentId, exam('AP', 'AP Microeconomics', 3))
    await viewer.removeExamPlanEntry(studentId, examKey('AP', 'Microeconomics'))
    await parent.removeExamPlanEntry(studentId, examKey('AP', 'Calculus AB'))
    expect((await (await device(INVITED)).examPlan(studentId)).map((e) => e.key)).toEqual([examKey('CLEP', 'College Algebra')])
    expect(await (await device(OUTSIDER)).examPlan(studentId)).toEqual([])
  })

  it('an outsider sees nothing', async () => {
    const other = await device(OUTSIDER)
    expect(await other.getPlan(studentId)).toBeNull()
    expect(await other.setupProgress(studentId)).toBeNull()
  })
})

describe.skipIf(!URL_)('a student who signs up alone (no household)', () => {
  let studentId = ''

  it('creates their own profile and finishes setup; another device picks it all up', async () => {
    const phone = await device(SOLO)
    studentId = await phone.createSelfStudentProfile({ displayName: 'Casey', graduationYear: 2028, gradeLevel: 11, independent: false, timeZone: 'America/New_York' })
    await phone.savePlan(studentId, { exam_family: 'sat', target_score: 1300, goals: ['raise_score', 'merit'], daily_minutes: 15, exam_intent: 'sat', planned_test_date: null, study_days: [2, 4, 6] })
    await phone.saveSetupProgress(studentId, { startingPointAnswered: true, setupCompleted: true })
    await phone.setWeeklyGoal(studentId, week, 25, null)
    const laptop = await device(SOLO)
    expect((await laptop.getHouseholdContext()).students).toEqual([expect.objectContaining({ id: studentId, household_id: null, linked_user_id: SOLO })])
    expect(await laptop.getPlan(studentId)).toMatchObject({ exam_family: 'sat', target_score: 1300, daily_minutes: 15, study_days: [2, 4, 6] })
    expect((await laptop.setupProgress(studentId))!.setupCompletedAt).toBeTruthy()
  })

  it('a second profile for the same login is refused', async () => {
    await expect((await device(SOLO)).createSelfStudentProfile({ displayName: 'Casey 2', graduationYear: null, gradeLevel: null, independent: false, timeZone: null })).rejects.toThrow()
  })

  it('quick practice, then a benchmark scheduled for later; nothing counts as a result until it is completed', async () => {
    const phone = await device(SOLO)
    expect((await phone.startSession(studentId, 5, 'sat')).items.length).toBeGreaterThan(0)
    const when = new Date(Date.now() + 86_400_000).toISOString()
    await phone.saveSetupProgress(studentId, { benchmarkScheduledFor: when })
    expect(await (await device(SOLO)).listBenchmarks(studentId)).toEqual([])
  })

  it('nobody else can read or change it', async () => {
    const other = await device(OUTSIDER)
    expect(await other.getPlan(studentId)).toBeNull()
    await expect(other.saveSetupProgress(studentId, { setupCompleted: true })).rejects.toThrow()
    await expect(other.setWeeklyGoal(studentId, week, 1, null)).rejects.toThrow()
  })
})
