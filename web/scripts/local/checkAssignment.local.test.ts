// Lives outside src/ because it uses Node APIs (crypto, child_process).
//
// #263 acceptance tests T1–T10 (posted on #263, 2026-10-23) against the real local server, as the app's client and as
// each role with its own token. Skipped unless LOCAL_BACKEND_URL is set (scripts/local/live_stack.sh test).
// Local only: this proves the server rules and the client path, not hosted.
//
// The tests run in order and share two students' history (T4 uses T3's answered item; T5–T7 and T10 share Blake's).
//
// LOCAL TEST SETUP, NOT PRODUCT DATA: the seeded reserve is exactly one check's worth, which can't show that unassigned
// reserved items stay hidden. So this file, through psql on the local database only, shrinks the SAT mini-check plan
// to 2 items per section (no other local test starts a SAT check) and restores it afterwards, and backdates checks
// to make them expire. Nothing here touches hosted.
import { execFileSync } from 'node:child_process'
import { createHash, createHmac } from 'node:crypto'
import { createClient, type SupabaseClient } from '@supabase/supabase-js'
import { afterAll, beforeAll, describe, expect, it } from 'vitest'
import { QUESTIONS } from '../../src/lib/data/demo/fixtures'
import { practiceExclusions } from '../../src/lib/engine/freshness'
import { LiveSource } from '../../src/lib/data/live/liveSource'

const URL_ = process.env.LOCAL_BACKEND_URL
const SECRET = process.env.LOCAL_JWT_SECRET ?? 'local-only-jwt-secret-at-least-32-characters'
const PARENT = '00000000-0000-4000-a000-0000000263c1'
const VIEWER = '00000000-0000-4000-a000-0000000263c2'
const NOVIEW = '00000000-0000-4000-a000-0000000263c3'
const STUDENT = '00000000-0000-4000-a000-000000026358'
const STUDENT2 = '00000000-0000-4000-a000-000000026359'
const OTHER_PARENT = '00000000-0000-4000-a000-0000000263d1'
const OTHER_STUDENT = '00000000-0000-4000-a000-0000000263d8'
const OUTSIDER = '00000000-0000-4000-a000-000000026399'

const b64 = (o: unknown) => Buffer.from(JSON.stringify(o)).toString('base64url')
function jwt(sub: string | null, role = 'authenticated') {
  const now = Math.floor(Date.now() / 1000)
  const body = `${b64({ alg: 'HS256', typ: 'JWT' })}.${b64({ ...(sub ? { sub } : {}), role, aud: role === 'anon' ? undefined : 'authenticated', iat: now, exp: now + 3600 })}`
  return `${body}.${createHmac('sha256', SECRET).update(body).digest('base64url')}`
}
async function raw(sub: string): Promise<SupabaseClient> {
  const sb = createClient(URL_!, 'local-anon-key', { auth: { persistSession: false, autoRefreshToken: false } })
  const { error } = await sb.auth.setSession({ access_token: jwt(sub), refresh_token: 'local' })
  if (error) throw error
  return sb
}
const anon = () => createClient(URL_!, jwt(null, 'anon'), { auth: { persistSession: false, autoRefreshToken: false } })
const uid = (name: string) => {
  const h = createHash('sha1').update(`collegeprep-local:${name}`).digest('hex')
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-5${h.slice(13, 16)}-a${h.slice(17, 20)}-${h.slice(20, 32)}`
}
/** psql on the LOCAL database (live_stack.sh exports PGHOST/PGUSER/PGPASSWORD/PGDATABASE). */
const psql = (q: string) => execFileSync('psql', ['-q', '-X', '-tA', '-v', 'ON_ERROR_STOP=1', '-c', q], { encoding: 'utf8' }).trim()
const LOCAL_DB = process.env.LOCAL_DB ?? 'cp_local'
let dbChecked = false
/** Every statement runs only after confirming it is the local stack's database, never a restored copy or production. */
const sql = (q: string) => {
  if (!dbChecked) {
    const db = psql('select current_database()')
    if (db !== LOCAL_DB) throw new Error(`refusing to write to database "${db}": this file writes only to the local stack's ${LOCAL_DB} (run it through scripts/local/live_stack.sh test)`)
    dbChecked = true
  }
  return psql(q)
}
const pause = () => new Promise((r) => setTimeout(r, 25))
const answerFor = new Map(QUESTIONS.map((q) => [uid(`q:${q.id}`), q.accepted_answers[0]!]))
const sectionOf = new Map(QUESTIONS.map((q) => [uid(`q:${q.id}`), q.section]))
const RESERVED_SAT = new Set([...practiceExclusions('sat', QUESTIONS)].map((id) => uid(`q:${id}`)))
const RESERVED_ACT = new Set([...practiceExclusions('act', QUESTIONS)].map((id) => uid(`q:${id}`)))
const PER = 2 // SAT mini plan per section, set below

describe.skipIf(!URL_)('#263: a progress check exposes only its server-assigned items (T1–T11)', () => {
  const c = {} as Record<'PARENT' | 'VIEWER' | 'NOVIEW' | 'STUDENT' | 'STUDENT2' | 'OTHER_PARENT' | 'OTHER_STUDENT' | 'OUTSIDER', SupabaseClient>
  let student: LiveSource
  let student2: LiveSource
  let sid = ''
  let sid2 = ''
  let otherSid = ''
  let savedPlan = ''
  let savedMini = ''
  const readable = async (cl: SupabaseClient) => {
    const r = await cl.from('practice_questions').select('id, stem').eq('pool', 'assessment')
    expect(r.error).toBeNull()
    return new Set((r.data ?? []).map((x) => x.id as string))
  }
  const expire = (bm: string) => sql(`update public.practice_benchmarks set started_at = now() - interval '5 hours' where id = '${bm}'`)

  beforeAll(async () => {
    // Local auth users for this file only (the stack seeds the other files' users).
    sql(`insert into auth.users(id, email) values ${[PARENT, VIEWER, NOVIEW, STUDENT, STUDENT2, OTHER_PARENT, OTHER_STUDENT, OUTSIDER].map((id, i) => `('${id}', 'c263-${i}@local.test')`).join(', ')} on conflict do nothing`)
    // Before #263 the server has no plan table (it listed the whole reserve); these tests then fail, as they should.
    if (sql(`select to_regclass('public.practice_benchmark_plan') is not null`) === 't') {
      savedPlan = sql(`select string_agg(section || '=' || items, ',' order by section) from public.practice_benchmark_plan where exam_family = 'sat' and kind = 'mini'`)
      sql(`update public.practice_benchmark_plan set items = ${PER} where exam_family = 'sat' and kind = 'mini'`)
    }
    // T1–T10 test assignment, so they open mini checks freely: for this file only, a mini needs no earlier check and no
    // gap. T11 puts the real rules back for its own checks. Restored in afterAll.
    if (sql(`select to_regclass('public.practice_benchmark_kinds') is not null`) === 't') {
      savedMini = sql(`select needs_prior || ',' || min_days_after_prior from public.practice_benchmark_kinds where kind = 'mini'`)
      // The server's rules as migrated. A different value means an earlier run of this file aborted without restoring.
      expect(savedMini, 'practice_benchmark_kinds mini row (rerun live_stack.sh test for a fresh database)').toBe('true,28')
      sql(`update public.practice_benchmark_kinds set needs_prior = false, min_days_after_prior = 0 where kind = 'mini'`)
    }
    const subs = { PARENT, VIEWER, NOVIEW, STUDENT, STUDENT2, OTHER_PARENT, OTHER_STUDENT, OUTSIDER }
    for (const k of Object.keys(subs) as (keyof typeof c)[]) c[k] = await raw(subs[k])
    student = new LiveSource(c.STUDENT)
    student2 = new LiveSource(c.STUDENT2)
    const hh = (await c.PARENT.rpc('create_household', { p_name: '#263 family', p_time_zone: 'America/Chicago' })).data as string
    sid = (await c.PARENT.rpc('add_student', { p_household: hh, p_display_name: 'Avery', p_graduation_year: 2029, p_grade_level: 10 })).data as string
    sid2 = (await c.PARENT.rpc('add_student', { p_household: hh, p_display_name: 'Blake', p_graduation_year: 2029, p_grade_level: 10 })).data as string
    const join = async (cl: SupabaseClient, code: string) => expect((await cl.rpc('redeem_household_invitation', { p_code: code })).error).toBeNull()
    await join(c.VIEWER, (await c.PARENT.rpc('create_household_invitation', { p_household: hh, p_role: 'guardian', p_student: null, p_ttl_hours: 72, p_permissions: ['view_progress'] })).data as string)
    await join(c.NOVIEW, (await c.PARENT.rpc('create_household_invitation', { p_household: hh, p_role: 'guardian', p_student: null, p_ttl_hours: 72, p_permissions: ['manage_planning'] })).data as string)
    await join(c.STUDENT, ((await c.PARENT.rpc('create_student_invitation', { p_household: hh, p_student: sid })).data as { invite_code: string }[])[0]!.invite_code)
    await join(c.STUDENT2, ((await c.PARENT.rpc('create_student_invitation', { p_household: hh, p_student: sid2 })).data as { invite_code: string }[])[0]!.invite_code)
    const hh2 = (await c.OTHER_PARENT.rpc('create_household', { p_name: 'Other family', p_time_zone: 'America/Chicago' })).data as string
    otherSid = (await c.OTHER_PARENT.rpc('add_student', { p_household: hh2, p_display_name: 'Casey', p_graduation_year: 2029, p_grade_level: 10 })).data as string
    await join(c.OTHER_STUDENT, ((await c.OTHER_PARENT.rpc('create_student_invitation', { p_household: hh2, p_student: otherSid })).data as { invite_code: string }[])[0]!.invite_code)
    expect(RESERVED_SAT.size).toBe(8) // 4 per section seeded; the plan above assigns 2 per section
  })

  const realMiniRules = () => {
    const [prior, days] = savedMini.split(',')
    sql(`update public.practice_benchmark_kinds set needs_prior = ${prior === 'true'}, min_days_after_prior = ${Number(days)} where kind = 'mini'`)
  }
  afterAll(() => {
    if (savedMini) realMiniRules()
    if (!savedPlan) return
    for (const pair of savedPlan.split(',')) {
      const [section, items] = pair.split('=')
      sql(`update public.practice_benchmark_plan set items = ${Number(items)} where exam_family = 'sat' and kind = 'mini' and section = '${section}'`)
    }
  })

  let bm1 = ''
  let assigned1 = new Set<string>()
  let firstAnswered = ''

  it('T1 assignment size: the plan size per section, from the reserve, unseen first; no client-chosen ids', async () => {
    expect(await readable(c.STUDENT)).toEqual(new Set()) // P0: nothing before a check opens
    bm1 = await student.startBenchmark(sid, 'mini', 'sat')
    const items = await student.benchmarkQuestions(bm1)
    assigned1 = new Set(items.map((i) => i.question.id))
    expect(items).toHaveLength(2 * PER)
    for (const s of ['reading_writing', 'math']) expect(items.filter((i) => i.question.section === s)).toHaveLength(PER)
    expect(items.every((i) => RESERVED_SAT.has(i.question.id) && i.question.pool === 'assessment' && !i.seen_before)).toBe(true)
    // start_benchmark takes no item list: there is no parameter a client could use to choose ids.
    const version = sql(`select exam_version_id from public.practice_benchmarks where id = '${bm1}'`)
    const chosen = await c.STUDENT.rpc('start_benchmark', { p_student: sid, p_kind: 'mini', p_exam_version: version, p_items: [...RESERVED_SAT] } as never)
    expect(chosen.error?.code).toBe('PGRST202') // no such function signature
  })

  it('T2 read scope: while the check is open the student reads only its assigned stems, by every route', async () => {
    expect(await readable(c.STUDENT)).toEqual(assigned1)
    const unassigned = [...RESERVED_SAT].filter((id) => !assigned1.has(id))
    expect(unassigned).toHaveLength(8 - 2 * PER)
    const direct = await c.STUDENT.from('practice_questions').select('id, stem').in('id', unassigned)
    expect(direct.error).toBeNull()
    expect(direct.data).toEqual([])
    const listed = await c.STUDENT.rpc('benchmark_questions', { p_benchmark: bm1 })
    expect(listed.error).toBeNull()
    expect(new Set(((listed.data ?? []) as { question_id?: string; id?: string }[]).map((r) => r.question_id ?? r.id))).toEqual(assigned1)
  })

  it('T3 attempt scope: an unassigned reserved item is refused; an assigned item is used once', async () => {
    const unassigned = [...RESERVED_SAT].find((id) => !assigned1.has(id))!
    const off = await c.STUDENT.rpc('start_practice_attempt', { p_student: sid, p_question: unassigned, p_benchmark: bm1 })
    expect(off.error).toMatchObject({ code: '22023', message: 'This question is not part of this progress check' })
    const first = [...assigned1][0]!
    firstAnswered = first
    const a = await student.startAttempt(sid, first, null, bm1)
    await pause()
    await student.submitAttempt(a, { answer: answerFor.get(first) ?? 'A', activeMs: 5 })
    const again = await c.STUDENT.rpc('start_practice_attempt', { p_student: sid, p_question: first, p_benchmark: bm1 })
    expect(again.error).toMatchObject({ code: '22023', message: 'A question is used once per progress check' })
  })

  it('T5 retries and resume of an unanswered check: the same check and assignment; nothing new is exposed', async () => {
    // A fresh, unanswered check is resumed as it is.
    const r1 = await student2.startBenchmark(sid2, 'mini', 'sat')
    const set1 = new Set((await student2.benchmarkQuestions(r1)).map((i) => i.question.id))
    for (let i = 0; i < 3; i++) expect(await student2.startBenchmark(sid2, 'mini', 'sat')).toBe(r1)
    expect(new Set((await student2.benchmarkQuestions(r1)).map((i) => i.question.id))).toEqual(set1)
    expect(await readable(c.STUDENT2)).toEqual(set1)
    expect(sql(`select count(*) from public.practice_benchmark_items where benchmark_id = '${r1}'`)).toBe(String(2 * PER))
    expire(r1)
  })

  it('T6 concurrency: parallel starts for one student give one check and one assignment', async () => {
    const [a, b, d] = await Promise.all([1, 2, 3].map(() => student2.startBenchmark(sid2, 'mini', 'sat')))
    expect(new Set([a, b, d]).size).toBe(1)
    expect(sql(`select count(*) from public.practice_benchmarks where student_id = '${sid2}' and items_assigned_at is not null and completed_at is null and started_at > now() - interval '4 hours'`)).toBe('1')
    expect(sql(`select count(*) from public.practice_benchmark_items where benchmark_id = '${a}'`)).toBe(String(2 * PER))
    expect((await readable(c.STUDENT2)).size).toBe(2 * PER)
    expire(a!)
  })

  it('T4 abandonment: an assigned item counts as seen whether or not it was answered; the next check draws unseen items first', async () => {
    expire(bm1) // one item answered, the rest only read
    // An expired check unlocks nothing new: only the one item Avery answered stays readable, under the existing rule
    // that a student (and a viewing guardian) may review items the student attempted. It already counts as seen.
    expect(await readable(c.STUDENT)).toEqual(new Set([firstAnswered]))
    const bm2 = await student.startBenchmark(sid, 'mini', 'sat')
    expect(bm2).not.toBe(bm1)
    const items2 = await student.benchmarkQuestions(bm2)
    expect(items2).toHaveLength(2 * PER)
    const assigned2 = new Set(items2.map((i) => i.question.id))
    // The other half of the reserve, never shown: all unseen.
    expect([...assigned2].filter((id) => assigned1.has(id))).toEqual([])
    expect(items2.every((i) => !i.seen_before)).toBe(true)
    expire(bm2) // abandoned without a single answer
    // Every reserved item has now been assigned once: the third check is all repeats, including the never-answered ones.
    const bm3 = await student.startBenchmark(sid, 'mini', 'sat')
    const items3 = await student.benchmarkQuestions(bm3)
    expect(items3).toHaveLength(2 * PER)
    expect(items3.every((i) => i.seen_before)).toBe(true)
    const pool = await c.STUDENT.rpc('assessment_pool_status', { p_student: sid, p_exam_version: sql(`select exam_version_id from public.practice_benchmarks where id = '${bm3}'`) })
    expect(pool.error).toBeNull()
    const counts = pool.data as { section: string; reserved: number; unseen: number }[]
    expect(counts.map((x) => [x.section, x.reserved, x.unseen]).sort()).toEqual([['math', 4, 0], ['reading_writing', 4, 0]])
    // Answering them all gives a check scored with repeats and never "comparable".
    for (const it of items3) {
      const a = await student.startAttempt(sid, it.question.id, null, bm3)
      await pause()
      await student.submitAttempt(a, { answer: answerFor.get(it.question.id) ?? 'A', activeMs: 5 })
    }
    const m = await c.STUDENT.rpc('complete_benchmark', { p_benchmark: bm3 })
    expect(m.error).toBeNull()
    const d = m.data as { repeats: number; comparable: boolean; by_section: Record<string, { repeats: number; comparable: boolean }> }
    // Every answered item had been assigned before (one only read, never answered): all repeats, nothing comparable.
    expect(d).toMatchObject({ repeats: 2 * PER, comparable: false })
    expect(Object.keys(d.by_section).sort()).toEqual(['math', 'reading_writing'])
    expect(Object.values(d.by_section).every((x) => x.repeats === PER && x.comparable === false)).toBe(true)
  })

  it('T7 cross-exam isolation: an ACT check exposes only ACT items, and a SAT item is refused in it', async () => {
    const sat = await student2.startBenchmark(sid2, 'mini', 'sat')
    const act = await student2.startBenchmark(sid2, 'mini', 'act')
    const actItems = await student2.benchmarkQuestions(act)
    const satItems = await student2.benchmarkQuestions(sat)
    expect(actItems.length).toBeGreaterThan(0)
    expect(actItems.every((i) => RESERVED_ACT.has(i.question.id))).toBe(true)
    expect(satItems.every((i) => RESERVED_SAT.has(i.question.id))).toBe(true)
    expect(await readable(c.STUDENT2)).toEqual(new Set([...actItems, ...satItems].map((i) => i.question.id)))
    const cross = await c.STUDENT2.rpc('start_practice_attempt', { p_student: sid2, p_question: satItems[0]!.question.id, p_benchmark: act })
    expect(cross.error?.code).toBe('22023')
    expire(act)
    expire(sat)
  })

  it('T8 unauthorized: anon, another household, an outsider and a guardian without view-progress see and start nothing', async () => {
    const live = await student.startBenchmark(sid, 'mini', 'sat') // resumes or opens a live check for Avery
    const ids = (await student.benchmarkQuestions(live)).map((i) => i.question.id)
    const a = anon()
    expect((await a.rpc('benchmark_questions', { p_benchmark: live })).error?.code).toBe('42501')
    expect((await a.from('practice_benchmark_items').select('*')).error?.code).toBe('42501')
    for (const who of ['OTHER_PARENT', 'OTHER_STUDENT', 'OUTSIDER', 'NOVIEW'] as const) {
      const cl = c[who]
      expect(await readable(cl), who).toEqual(new Set())
      const list = await cl.rpc('benchmark_questions', { p_benchmark: live })
      expect(list.error?.code, who).toBe('42501') // refused: the caller isn't linked to this student
      const rows = await cl.from('practice_benchmark_items').select('question_id').eq('benchmark_id', live)
      expect(rows.error, who).toBeNull()
      expect(rows.data, who).toEqual([])
      expect((await cl.rpc('start_benchmark', { p_student: sid, p_kind: 'mini', p_exam_version: sql(`select exam_version_id from public.practice_benchmarks where id = '${live}'`) })).error, who).not.toBeNull()
      expect((await cl.rpc('start_practice_attempt', { p_student: sid, p_question: ids[0], p_benchmark: live })).error, who).not.toBeNull()
    }
    // The viewing guardian sees no live-check content and can't act for the student.
    const v = c.VIEWER
    const vStems = await v.from('practice_questions').select('id, stem').in('id', ids)
    expect(vStems.error).toBeNull()
    expect(vStems.data).toEqual([])
    expect((await v.rpc('start_benchmark', { p_student: sid, p_kind: 'mini', p_exam_version: sql(`select exam_version_id from public.practice_benchmarks where id = '${live}'`) })).error).not.toBeNull()
    expect((await v.rpc('start_practice_attempt', { p_student: sid, p_question: ids[0], p_benchmark: live })).error).not.toBeNull()
    // Direct writes to the assignment are refused for every client.
    const ev = sql(`select exam_version_id from public.practice_benchmarks where id = '${live}'`)
    const extra = [...RESERVED_SAT].find((id) => !ids.includes(id)) ?? [...RESERVED_SAT][0]
    for (const cl of [c.STUDENT, c.PARENT, v]) {
      // A complete row, so only the permission can refuse it.
      const ins = await cl.from('practice_benchmark_items').insert({ benchmark_id: live, question_id: extra, student_id: sid, exam_version_id: ev, section: 'math', position: 99, seen_before: false })
      expect(ins.error?.code).toBe('42501')
      const upd = await cl.from('practice_benchmarks').update({ items_assigned_at: null }).eq('id', live)
      expect(upd.error?.code).toBe('42501')
    }
    expect(sql(`select items_assigned_at is not null from public.practice_benchmarks where id = '${live}'`)).toBe('t')
    expect(sql(`select count(*) from public.practice_benchmark_items where benchmark_id = '${live}'`)).toBe(String(ids.length))
    expire(live)
  })

  it('T9 practice isolation: practice never retrieves a reserved item, assigned or not', async () => {
    const live = await student.startBenchmark(sid, 'mini', 'sat')
    const assigned = new Set((await student.benchmarkQuestions(live)).map((i) => i.question.id))
    const s = await student.startSession(sid, 30, 'sat')
    expect(s.items.filter((x) => RESERVED_SAT.has(x.question.id) || x.question.pool !== 'practice')).toEqual([])
    const unassigned = [...RESERVED_SAT].filter((id) => !assigned.has(id))
    expect(unassigned.length).toBeGreaterThan(0)
    for (const q of [...[...assigned].slice(0, 2), ...unassigned.slice(0, 2)]) {
      expect((await c.STUDENT.rpc('start_practice_attempt', { p_student: sid, p_question: q, p_session: s.id })).error?.code).toBe('22023')
      expect((await c.STUDENT.rpc('start_practice_attempt', { p_student: sid, p_question: q })).error?.code).toBe('22023')
    }
    await student.endSession(s.id)
    expire(live)
  })

  it('T10 cap: a mini check accepts at most its assigned items; a direct `full` start is refused', async () => {
    const fresh = await student2.startBenchmark(sid2, 'mini', 'sat')
    const items = await student2.benchmarkQuestions(fresh)
    let accepted = 0
    for (const id of RESERVED_SAT) {
      const r = await c.STUDENT2.rpc('start_practice_attempt', { p_student: sid2, p_question: id, p_benchmark: fresh })
      if (!r.error) {
        accepted++
        await pause()
        await student2.submitAttempt(r.data as string, { answer: answerFor.get(id) ?? 'A', activeMs: 5 })
      }
    }
    expect(accepted).toBe(items.length)
    expect(accepted).toBe(2 * PER)
    expect(sql(`select count(distinct question_id) from public.practice_attempts where benchmark_id = '${fresh}'`)).toBe(String(2 * PER))
    expect(new Set(items.map((i) => sectionOf.get(i.question.id)))).toEqual(new Set(['reading_writing', 'math']))
    expire(fresh)
    const full = await c.STUDENT2.rpc('start_benchmark', { p_student: sid2, p_kind: 'full', p_exam_version: sql(`select exam_version_id from public.practice_benchmarks where id = '${fresh}'`) })
    expect(full.error).toMatchObject({ code: '22023' })
    expect(sql(`select count(*) from public.practice_benchmarks where student_id = '${sid2}' and kind = 'full'`)).toBe('0')
  })

  // After T10: T5b answers an item, and an answered item stays readable to the student, which T6–T8 would count.
  it('T5b resume of a partly answered check: a reload or retry returns the same check; its used items stay used, no new item is assigned', async () => {
    const r1 = await student2.startBenchmark(sid2, 'mini', 'sat')
    try {
      const before = await student2.benchmarkQuestions(r1)
      const first = before[0]!.question.id
      const a = await student2.startAttempt(sid2, first, null, r1)
      await pause()
      await student2.submitAttempt(a, { answer: answerFor.get(first) ?? 'A', activeMs: 5 })
      // Reload: a new client, the same student; and a retry of the start itself.
      const reloadedClient = await raw(STUDENT2)
      const reloaded = new LiveSource(reloadedClient)
      const version = sql(`select exam_version_id from public.practice_benchmarks where id = '${r1}'`)
      const allowed = await reloadedClient.rpc('benchmark_allowed_kinds', { p_student: sid2, p_exam_version: version })
      expect(allowed.error).toBeNull()
      expect((allowed.data as { live_benchmark: string; live_kind: string; allowed_kinds: string[] }[])[0]).toMatchObject({ live_benchmark: r1, live_kind: 'mini', allowed_kinds: ['mini'] })
      expect(await reloaded.startBenchmark(sid2, 'mini', 'sat')).toBe(r1)
      expect(await student2.startBenchmark(sid2, 'mini', 'sat')).toBe(r1)
      const after = await reloaded.benchmarkQuestions(r1)
      expect(after.map((i) => i.question.id)).toEqual(before.slice(1).map((i) => i.question.id))
      expect(sql(`select count(*) from public.practice_benchmark_items where benchmark_id = '${r1}'`)).toBe(String(2 * PER))
      expect(sql(`select count(*) from public.practice_benchmarks where student_id = '${sid2}' and completed_at is null and started_at > now() - interval '4 hours'`)).toBe('1')
      // What a client reads for progress (#291): the student's own assignment rows and attempts in the check.
      const rows = await reloadedClient.from('practice_benchmark_items').select('question_id').eq('benchmark_id', r1)
      expect(rows.error).toBeNull()
      expect(rows.data).toHaveLength(2 * PER)
      const used = await reloadedClient.from('practice_attempts').select('question_id').eq('benchmark_id', r1)
      expect(used.data?.map((x) => x.question_id)).toEqual([first])
      // Another kind while it is live is refused, not opened beside it.
      const other = await c.STUDENT2.rpc('start_benchmark', { p_student: sid2, p_kind: 'initial', p_exam_version: sql(`select exam_version_id from public.practice_benchmarks where id = '${r1}'`) })
      expect(other.error).toMatchObject({ code: '22023' })
      expect(other.error!.message).toMatch(/already open for this exam; resume it/)
    } finally {
      expire(r1) // even on failure, so T12 doesn't find it live
    }
  })

  it('T11 kind rules on the server, for direct calls too: initial once, mini after a first check and 28 days, full refused; the client reads the same rules', async () => {
    realMiniRules()
    try {
      const version = sql(`select id from public.exam_versions where exam_family = 'sat' order by effective_from desc limit 1`)
      const start = (kind: string) => c.OTHER_STUDENT.rpc('start_benchmark', { p_student: otherSid, p_kind: kind, p_exam_version: version })
      const rules = async () => {
        const r = await c.OTHER_STUDENT.rpc('benchmark_allowed_kinds', { p_student: otherSid, p_exam_version: version })
        expect(r.error).toBeNull()
        return (r.data as { live_benchmark: string | null; allowed_kinds: string[]; next_mini_at: string | null; reserve_available: boolean }[])[0]!
      }
      expect(await rules()).toMatchObject({ live_benchmark: null, allowed_kinds: ['initial'], reserve_available: true })
      expect((await start('mini')).error).toMatchObject({ code: '22023', message: 'A repeat progress check comes after a first check for this exam' })
      expect((await start('full')).error).toMatchObject({ code: '22023' })
      const first = (await start('initial')).data as string
      expect(first).toBeTruthy()
      expire(first) // abandoned unanswered: it still counts as the student's check
      expect((await start('initial')).error).toMatchObject({ code: '22023' })
      expect((await start('mini')).error?.message).toMatch(/opens 28 days after the last one started/)
      const opts = await rules()
      expect(opts).toMatchObject({ live_benchmark: null, allowed_kinds: [] })
      expect(Date.parse(opts.next_mini_at!)).toBe(Date.parse(sql(`select to_char((started_at at time zone 'UTC') + interval '28 days', 'YYYY-MM-DD"T"HH24:MI:SS.MS"Z"') from public.practice_benchmarks where id = '${first}'`)))
      // 28 days later (backdated here) the mini opens.
      sql(`update public.practice_benchmarks set started_at = now() - interval '29 days' where id = '${first}'`)
      expect((await rules()).allowed_kinds).toEqual(['mini'])
      const mini = (await start('mini')).data as string
      expect(mini).toBeTruthy()
      expire(mini)
    } finally {
      sql(`update public.practice_benchmark_kinds set needs_prior = false, min_days_after_prior = 0 where kind = 'mini'`)
    }
  })
})
