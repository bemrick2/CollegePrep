// Lives outside src/ because it uses Node APIs (crypto).
//
// CR-26 against the local disposable backend with the reference SQL: setup answers live on the account, so a
// guardian's choices are what the student's own login reads, and finished setup is recorded once for every device.
// Skipped unless LOCAL_BACKEND_URL is set (scripts/local/live_stack.sh test).
import { createHmac } from 'node:crypto'
import { createClient } from '@supabase/supabase-js'
import { beforeAll, describe, expect, it } from 'vitest'
import { LiveSource } from '../../src/lib/data/live/liveSource'

const URL_ = process.env.LOCAL_BACKEND_URL
const SECRET = process.env.LOCAL_JWT_SECRET ?? 'local-only-jwt-secret-at-least-32-characters'
const PARENT = '00000000-0000-4000-a000-0000000000a6'
const STUDENT = '00000000-0000-4000-a000-000000000055'
const OUTSIDER = '00000000-0000-4000-a000-000000000099'

const b64 = (o: unknown) => Buffer.from(JSON.stringify(o)).toString('base64url')
function jwt(sub: string) {
  const now = Math.floor(Date.now() / 1000)
  const body = `${b64({ alg: 'HS256', typ: 'JWT' })}.${b64({ sub, role: 'authenticated', aud: 'authenticated', iat: now, exp: now + 3600 })}`
  return `${body}.${createHmac('sha256', SECRET).update(body).digest('base64url')}`
}
/** Each call is a separate client: a different device for the same account. */
async function device(sub: string) {
  const sb = createClient(URL_!, 'local-anon-key', { auth: { persistSession: false, autoRefreshToken: false } })
  const { error } = await sb.auth.setSession({ access_token: jwt(sub), refresh_token: 'local' })
  if (error) throw error
  return new LiveSource(sb, { accountSetup: true })
}

describe.skipIf(!URL_)('setup on the account (CR-26)', () => {
  let studentId = ''
  beforeAll(async () => {
    const parent = await device(PARENT)
    const hh = await parent.createHousehold('Setup family', 'America/Chicago')
    studentId = await parent.addStudent(hh, 'Riley', 2028, 11)
    // The parent's setup: test choice, date, study days, a 20-minute session, a practice-test score, done.
    await parent.savePlan(studentId, { exam_family: 'sat', target_score: null, goals: ['raise_score'], daily_minutes: 20, exam_intent: 'both', planned_test_date: '2027-03-06', study_days: [2, 4] })
    await parent.addTestScore(studentId, { exam_family: 'sat', test_date: '2026-06-06', composite: 1180, section_scores: {}, source: 'practice_test' })
    await parent.saveSetupProgress(studentId, { setupCompleted: true, startingPointAnswered: true })
    const inv = await parent.createStudentInvitation(hh, studentId)
    await (await device(STUDENT)).acceptInvitation(inv.inviteCode!)
  })

  it("the student's own device reads the parent's choices, and sees setup as finished", async () => {
    const phone = await device(STUDENT)
    expect(await phone.getPlan(studentId)).toEqual({ exam_family: 'sat', target_score: null, goals: ['raise_score'], daily_minutes: 20, exam_intent: 'both', planned_test_date: '2027-03-06', study_days: [2, 4] })
    expect(await phone.setupProgress(studentId)).toMatchObject({ setupCompletedAt: expect.any(String), startingPointAnsweredAt: expect.any(String), benchmarkScheduledFor: null })
    expect(await phone.testScores(studentId)).toEqual([expect.objectContaining({ score_source: 'practice_test', composite: 1180 })])
  })

  it('the student schedules the benchmark and starts a 20-minute session, but cannot change the plan or claim an official score', async () => {
    const phone = await device(STUDENT)
    const at = new Date(Date.now() + 86_400_000).toISOString()
    await phone.saveSetupProgress(studentId, { benchmarkScheduledFor: at })
    const laptop = await device(STUDENT)
    expect(Date.parse((await laptop.setupProgress(studentId))!.benchmarkScheduledFor!)).toBe(Date.parse(at))
    // Completion is never undone by a later write.
    expect((await laptop.setupProgress(studentId))!.setupCompletedAt).toBeTruthy()
    const s = await phone.startSession(studentId, 20, 'sat')
    expect(s.items.length).toBeGreaterThan(0)
    await expect(phone.savePlan(studentId, { exam_family: 'act', target_score: null, goals: [], daily_minutes: 5 })).rejects.toThrow()
    const sb = createClient(URL_!, 'local-anon-key', { auth: { persistSession: false, autoRefreshToken: false } })
    await sb.auth.setSession({ access_token: jwt(STUDENT), refresh_token: 'local' })
    const { error } = await sb.from('student_test_scores').insert({ student_id: studentId, exam_version_id: (await sb.from('exam_versions').select('id').eq('exam_family', 'sat').limit(1).single()).data!.id, test_date: '2026-06-06', composite: 1500, score_source: 'official' })
    expect(error).toBeTruthy()
  })

  it('an outsider sees none of it and cannot change it', async () => {
    const other = await device(OUTSIDER)
    expect(await other.setupProgress(studentId)).toBeNull()
    await expect(other.saveSetupProgress(studentId, { setupCompleted: true })).rejects.toThrow()
  })
})
