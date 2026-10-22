// Lives outside src/ because it uses Node APIs (crypto).
//
// CR-23 (#248) against the real local server, end to end: practice can't retrieve reserved questions, checks can't
// substitute practice questions, and no other role can get around either rule. Raw PostgREST calls with each role's
// own token, plus LiveSource for the full student flow. Skipped unless LOCAL_BACKEND_URL is set
// (scripts/local/live_stack.sh test). Local only: this proves the server rules and the client path, not hosted.
import { createHash, createHmac } from 'node:crypto'
import { createClient, type SupabaseClient } from '@supabase/supabase-js'
import { beforeAll, describe, expect, it } from 'vitest'
import { QUESTIONS } from '../../src/lib/data/demo/fixtures'
import { practiceExclusions } from '../../src/lib/engine/freshness'
import { compareProgress } from '../../src/lib/engine/progressCheck'
import { LiveSource } from '../../src/lib/data/live/liveSource'
import type { BenchmarkSummary } from '../../src/lib/data/types'

const URL_ = process.env.LOCAL_BACKEND_URL
const SECRET = process.env.LOCAL_JWT_SECRET ?? 'local-only-jwt-secret-at-least-32-characters'
const PARENT = '00000000-0000-4000-a000-0000000000c1'
const VIEWER = '00000000-0000-4000-a000-0000000000c2'
const STUDENT = '00000000-0000-4000-a000-000000000058'
const OUTSIDER = '00000000-0000-4000-a000-000000000099'

const b64 = (o: unknown) => Buffer.from(JSON.stringify(o)).toString('base64url')
function jwt(sub: string) {
  const now = Math.floor(Date.now() / 1000)
  const body = `${b64({ alg: 'HS256', typ: 'JWT' })}.${b64({ sub, role: 'authenticated', aud: 'authenticated', iat: now, exp: now + 3600 })}`
  return `${body}.${createHmac('sha256', SECRET).update(body).digest('base64url')}`
}
async function raw(sub: string): Promise<SupabaseClient> {
  const sb = createClient(URL_!, 'local-anon-key', { auth: { persistSession: false, autoRefreshToken: false } })
  const { error } = await sb.auth.setSession({ access_token: jwt(sub), refresh_token: 'local' })
  if (error) throw error
  return sb
}
/** Same deterministic ids as seedFromFixtures.ts. */
const uid = (name: string) => {
  const h = createHash('sha1').update(`collegeprep-local:${name}`).digest('hex')
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-5${h.slice(13, 16)}-a${h.slice(17, 20)}-${h.slice(20, 32)}`
}
const pause = () => new Promise((r) => setTimeout(r, 25))
const answerFor = new Map(QUESTIONS.map((q) => [uid(`q:${q.id}`), q.accepted_answers[0]!]))
// The seeded assessment pool (seedFromFixtures.ts marks exactly these) and the ACT practice items.
const RESERVED_ACT = new Set([...practiceExclusions('act', QUESTIONS)].map((id) => uid(`q:${id}`)))
const PRACTICE_ACT = QUESTIONS.filter((q) => q.exam_family === 'act' && !practiceExclusions('act', QUESTIONS).has(q.id)).map((q) => uid(`q:${q.id}`))
const anyReserved = () => [...RESERVED_ACT][0]!
const RESERVED_SAT = [...practiceExclusions('sat', QUESTIONS)].map((id) => uid(`q:${id}`))

describe.skipIf(!URL_)('reserved assessment pool on the server (CR-23)', () => {
  const c = {} as Record<'PARENT' | 'VIEWER' | 'STUDENT' | 'OUTSIDER', SupabaseClient>
  let student: LiveSource
  let studentId = ''

  beforeAll(async () => {
    c.PARENT = await raw(PARENT)
    c.VIEWER = await raw(VIEWER)
    c.STUDENT = await raw(STUDENT)
    c.OUTSIDER = await raw(OUTSIDER)
    student = new LiveSource(c.STUDENT)
    const hh = (await c.PARENT.rpc('create_household', { p_name: 'Pool family', p_time_zone: 'America/Chicago' })).data as string
    studentId = (await c.PARENT.rpc('add_student', { p_household: hh, p_display_name: 'Jamie', p_graduation_year: 2029, p_grade_level: 10 })).data as string
    const view = (await c.PARENT.rpc('create_household_invitation', { p_household: hh, p_role: 'guardian', p_student: null, p_ttl_hours: 72, p_permissions: ['view_progress'] })).data as string
    const inv = (await c.PARENT.rpc('create_student_invitation', { p_household: hh, p_student: studentId })).data as { invite_code: string }[]
    for (const [cl, code] of [[c.VIEWER, view], [c.STUDENT, inv[0]!.invite_code]] as const) {
      const r = await cl.rpc('redeem_household_invitation', { p_code: code })
      expect(r.error).toBeNull()
    }
    expect(RESERVED_ACT.size).toBe(13)
  })

  it('practice can’t retrieve reserved questions: not readable, not recommended, not in a session, not attemptable', async () => {
    const read = await c.STUDENT.from('practice_questions').select('id, pool').eq('pool', 'assessment')
    expect(read.error).toBeNull()
    expect(read.data).toEqual([])
    const rec = await c.STUDENT.rpc('recommend_practice_set', { p_student: studentId, p_target_minutes: 30 })
    expect(rec.error).toBeNull()
    expect(((rec.data ?? []) as { question_id: string }[]).filter((r) => RESERVED_ACT.has(r.question_id))).toEqual([])
    for (let i = 0; i < 3; i++) {
      const s = await student.startSession(studentId, 30, 'act')
      expect(s.items.length).toBeGreaterThan(0)
      expect(s.items.filter((x) => RESERVED_ACT.has(x.question.id) || x.question.pool !== 'practice')).toEqual([])
      // An attempt on a reserved question, inside a session or with none, is refused by the server.
      const inSession = await c.STUDENT.rpc('start_practice_attempt', { p_student: studentId, p_question: anyReserved(), p_session: s.id })
      expect(inSession.error?.code).toBe('22023')
      await student.endSession(s.id)
    }
    const loose = await c.STUDENT.rpc('start_practice_attempt', { p_student: studentId, p_question: anyReserved() })
    expect(loose.error?.code).toBe('22023')
    // Even when practice runs out: every practice question answered, sessions are review of practice items only.
    const s = await student.startSession(studentId, 5, 'act')
    for (const id of PRACTICE_ACT) {
      const a = await student.startAttempt(studentId, id, s.id)
      await pause()
      await student.submitAttempt(a, { answer: answerFor.get(id) ?? 'A', activeMs: 5 })
    }
    await student.endSession(s.id)
    const review = await student.startSession(studentId, 30, 'act')
    expect(review.items.length).toBeGreaterThan(0)
    expect(review.items.every((x) => x.seen_before && !RESERVED_ACT.has(x.question.id))).toBe(true)
    await student.endSession(review.id)
  })

  let first: BenchmarkSummary | null = null

  it('a check uses only reserved questions, each once; a practice question is refused; the full flow scores it as comparable', async () => {
    const bm = await student.startBenchmark(studentId, 'initial', 'act')
    const items = await student.benchmarkQuestions(bm)
    expect(new Set(items.map((i) => i.question.id))).toEqual(RESERVED_ACT)
    expect(items.every((i) => i.question.pool === 'assessment' && !i.seen_before)).toBe(true)
    // Substituting a practice question in a check is refused.
    const sub = await c.STUDENT.rpc('start_practice_attempt', { p_student: studentId, p_question: PRACTICE_ACT[0], p_benchmark: bm })
    expect(sub.error?.code).toBe('22023')
    const ids: string[] = []
    for (const it of items) {
      const a = await student.startAttempt(studentId, it.question.id, null, bm)
      ids.push(a)
      await pause()
      await student.submitAttempt(a, { answer: answerFor.get(it.question.id) ?? 'A', activeMs: 5, confidence: 2 })
    }
    // An item is used once per check.
    const again = await c.STUDENT.rpc('start_practice_attempt', { p_student: studentId, p_question: items[0]!.question.id, p_benchmark: bm })
    expect(again.error?.code).toBe('22023')
    expect(await student.benchmarkQuestions(bm)).toEqual([])
    first = await student.completeBenchmark(studentId, bm, { id: 'c', kind: 'initial', exam_family: 'act', started_at: new Date().toISOString(), completed_at: new Date().toISOString(), attempt_ids: ids, metrics: {} as never })
    expect(first.metrics.answered).toBe(13)
    expect(first.metrics.sections.every((s) => s.repeats === 0)).toBe(true)
    // Outside an open check, reserved content is readable again only for items this student has attempted.
    const after = await c.STUDENT.from('practice_questions').select('id').eq('pool', 'assessment')
    expect(new Set((after.data ?? []).map((r) => r.id))).toEqual(RESERVED_ACT)
  })

  it('a second check can only repeat the reserve: every item is flagged, and no section gets a progress verdict', async () => {
    const bm = await student.startBenchmark(studentId, 'mini', 'act')
    const items = await student.benchmarkQuestions(bm)
    expect(items.length).toBe(13)
    expect(items.every((i) => i.seen_before)).toBe(true)
    const ids: string[] = []
    for (const it of items.filter((i) => i.question.section === 'math')) {
      const a = await student.startAttempt(studentId, it.question.id, null, bm)
      ids.push(a)
      await pause()
      await student.submitAttempt(a, { answer: answerFor.get(it.question.id) ?? 'A', activeMs: 5 })
    }
    const second = await student.completeBenchmark(studentId, bm, { id: 'c2', kind: 'mini', exam_family: 'act', started_at: new Date().toISOString(), completed_at: new Date().toISOString(), attempt_ids: ids, metrics: {} as never })
    expect(second.metrics.sections.find((s) => s.section === 'math')!.repeats).toBe(ids.length)
    // The app's comparison reads the server's repeats: no verdict, whatever the score.
    const cmp = compareProgress({ ...second, completed_at: new Date(Date.now() + 1000).toISOString() }, [first!])
    expect(cmp.sinceBaseline.find((x) => x.section === 'math')!.verdict).toBe('not_clean')
  })

  it('no other role can get around it: not the parent, a view-only guardian or an outsider; nobody can re-pool a question', async () => {
    const bm = await student.startBenchmark(studentId, 'mini', 'act')
    for (const who of ['PARENT', 'VIEWER', 'OUTSIDER'] as const) {
      const list = await c[who].rpc('benchmark_questions', { p_benchmark: bm })
      expect([who, list.error?.code]).toEqual([who, '42501'])
      const att = await c[who].rpc('start_practice_attempt', { p_student: studentId, p_question: anyReserved(), p_benchmark: bm })
      expect([who, att.error?.code]).toEqual([who, '42501'])
    }
    // An outsider can't read reserved content at all; the student can't move a question between pools.
    expect((await c.OUTSIDER.from('practice_questions').select('id').eq('pool', 'assessment')).data ?? []).toEqual([])
    const move = await c.STUDENT.from('practice_questions').update({ pool: 'practice' }).eq('id', anyReserved()).select('id')
    expect(move.error?.code ?? (move.data?.length ? 'changed' : 'unchanged')).not.toBe('changed')
    const back = await c.STUDENT.from('practice_questions').select('pool').eq('id', anyReserved()).single()
    expect(back.data?.pool).toBe('assessment')
    // Another student's open check isn't readable through this one's token either.
    const other = await c.OUTSIDER.rpc('complete_benchmark', { p_benchmark: bm })
    expect(other.error?.code).toBe('42501')
  })

  it('pool counts (assessment_pool_status): counts only, for the student and view-progress guardians', async () => {
    const status = await student.assessmentPoolStatus(studentId, 'act')
    // The server in this PR has the RPC, so null (unknown) would be a regression here.
    expect(status).not.toBeNull()
    if (!status) return
    expect(status.reduce((n, s) => n + s.reserved, 0)).toBe(13)
    expect(status.every((s) => s.unseen === 0)).toBe(true)
    const viewer = await new LiveSource(c.VIEWER).assessmentPoolStatus(studentId, 'act')
    expect(viewer?.reduce((n, s) => n + s.reserved, 0)).toBe(13)
    await expect(new LiveSource(c.OUTSIDER).assessmentPoolStatus(studentId, 'act')).rejects.toThrow()
  })

  it('a second start of the same check resumes it rather than opening another (an open check unlocks the reserve)', async () => {
    const a = await student.startBenchmark(studentId, 'mini', 'act')
    const b = await student.startBenchmark(studentId, 'mini', 'act')
    expect(b).toBe(a)
    const open = await c.STUDENT.from('practice_benchmarks').select('id').eq('student_id', studentId).is('completed_at', null)
    expect(open.error).toBeNull()
    expect(open.data?.filter((r) => r.id === a)).toHaveLength(1)
    expect((await c.STUDENT.rpc('complete_benchmark', { p_benchmark: a })).error).toBeNull()
  })

  it('other bypasses are refused: no token, a guardian opening a check, a closed check, the other exam, direct table writes, hidden columns', async () => {
    const versions = await c.STUDENT.from('exam_versions').select('id, exam_family')
    const act = versions.data!.find((v) => v.exam_family === 'act')!.id as string
    // No token at all (anon): no reserved content, no check RPCs.
    // A real anon request: a token with role anon (the local stack has no anon key, so it's signed like the others).
    const now = Math.floor(Date.now() / 1000)
    const anonBody = `${b64({ alg: 'HS256', typ: 'JWT' })}.${b64({ role: 'anon', iat: now, exp: now + 3600 })}`
    const anonToken = `${anonBody}.${createHmac('sha256', SECRET).update(anonBody).digest('base64url')}`
    const anon = createClient(URL_!, anonToken, { auth: { persistSession: false, autoRefreshToken: false }, global: { headers: { Authorization: `Bearer ${anonToken}` } } })
    const anonRead = await anon.from('practice_questions').select('id').eq('pool', 'assessment')
    expect(anonRead.error !== null || (anonRead.data ?? []).length === 0).toBe(true)
    expect((await anon.rpc('start_benchmark', { p_student: studentId, p_kind: 'mini', p_exam_version: act })).error?.code).toBe('42501')
    // A guardian (even the parent who manages the student) can't open a check for the student, so can't unlock the reserve.
    for (const who of ['PARENT', 'VIEWER'] as const) {
      const r = await c[who].rpc('start_benchmark', { p_student: studentId, p_kind: 'mini', p_exam_version: act })
      expect([who, r.error?.code]).toEqual([who, '42501'])
      // Outside a check, a guardian who can view progress reads only reserved items the student has attempted.
      const att = await c.STUDENT.from('practice_attempts').select('question_id').eq('student_id', studentId).not('benchmark_id', 'is', null)
      expect(att.error).toBeNull()
      const attempted = new Set((att.data ?? []).map((r) => r.question_id as string).filter((id) => RESERVED_ACT.has(id)))
      expect(attempted.size).toBeGreaterThan(0)
      const read = await c[who].from('practice_questions').select('id').eq('pool', 'assessment')
      expect([who, read.error]).toEqual([who, null])
      expect([who, new Set((read.data ?? []).map((r) => r.id as string))]).toEqual([who, attempted])
    }
    // A closed check can't take more answers.
    const done = await student.startBenchmark(studentId, 'mini', 'act')
    expect((await c.STUDENT.rpc('complete_benchmark', { p_benchmark: done })).error).toBeNull()
    const late = await c.STUDENT.rpc('start_practice_attempt', { p_student: studentId, p_question: anyReserved(), p_benchmark: done })
    expect([late.error?.code, late.error?.message]).toEqual(['22023', expect.stringMatching(/not an open benchmark/)])
    // An ACT check can't take a reserved SAT question (the check's own exam version only).
    const open = await student.startBenchmark(studentId, 'mini', 'act')
    expect(RESERVED_SAT.length).toBeGreaterThan(0)
    const cross = await c.STUDENT.rpc('start_practice_attempt', { p_student: studentId, p_question: RESERVED_SAT[0], p_benchmark: open })
    expect([cross.error?.code, cross.error?.message]).toEqual(['22023', expect.stringMatching(/own exam version|reserved questions only/)])
    // No client writes attempts, checks or pool assignments directly.
    const insAttempt = await c.STUDENT.from('practice_attempts').insert({ student_id: studentId, question_id: anyReserved() }).select('id')
    expect(insAttempt.error?.code).toBe('42501')
    const insCheck = await c.STUDENT.from('practice_benchmarks').insert({ student_id: studentId, kind: 'mini', exam_version_id: act }).select('id')
    expect(insCheck.error?.code).toBe('42501')
    // Even inside an open check, answers and explanations of reserved items aren't readable.
    const hidden = await c.STUDENT.from('practice_questions').select('id, accepted_answers').eq('pool', 'assessment')
    expect(hidden.error?.code).toBe('42501')
    expect((await c.STUDENT.rpc('complete_benchmark', { p_benchmark: open })).error).toBeNull()
  })
})
