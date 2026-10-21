// Lives outside src/ because it uses Node APIs (crypto).
//
// Guardian and student permissions tested directly against the server: raw PostgREST table reads/writes and RPCs
// with each role's own signed token, not through LiveSource, so a client-side check can't hide a server gap.
// Runs on the local disposable backend (every migration plus Design's reference SQL). Skipped unless
// LOCAL_BACKEND_URL is set (scripts/local/live_stack.sh test).
//
// Roles, one household: PARENT (created it: every permission), CO (default guardian invite: manage students, set
// goals, view progress), VIEWER (guardian invited with view_progress only), STUDENT (linked by invitation),
// OUTSIDER (no relation).
import { createHmac } from 'node:crypto'
import { createClient, type SupabaseClient } from '@supabase/supabase-js'
import { beforeAll, describe, expect, it } from 'vitest'
import { weekStartOf } from '../../src/lib/engine/dates'

const URL_ = process.env.LOCAL_BACKEND_URL
const SECRET = process.env.LOCAL_JWT_SECRET ?? 'local-only-jwt-secret-at-least-32-characters'
const U = {
  PARENT: '00000000-0000-4000-a000-0000000000b1',
  CO: '00000000-0000-4000-a000-0000000000b2',
  VIEWER: '00000000-0000-4000-a000-0000000000b3',
  STUDENT: '00000000-0000-4000-a000-0000000000b4',
  OUTSIDER: '00000000-0000-4000-a000-000000000099',
} as const
type Role = keyof typeof U
const ROLES = Object.keys(U) as Role[]

const b64 = (o: unknown) => Buffer.from(JSON.stringify(o)).toString('base64url')
function jwt(sub: string) {
  const now = Math.floor(Date.now() / 1000)
  const body = `${b64({ alg: 'HS256', typ: 'JWT' })}.${b64({ sub, role: 'authenticated', aud: 'authenticated', iat: now, exp: now + 3600 })}`
  return `${body}.${createHmac('sha256', SECRET).update(body).digest('base64url')}`
}
const clients = {} as Record<Role, SupabaseClient>
async function as(sub: string) {
  const sb = createClient(URL_!, 'local-anon-key', { auth: { persistSession: false, autoRefreshToken: false } })
  const { error } = await sb.auth.setSession({ access_token: jwt(sub), refresh_token: 'local' })
  if (error) throw error
  return sb
}
const rpc = async (r: Role, fn: string, args: Record<string, unknown>) => clients[r].rpc(fn, args)
/** A write "took effect" only when it returned rows: row security filters silently, so 0 rows means refused. */
const wrote = (res: { error: unknown; data: unknown[] | null }) => !res.error && (res.data?.length ?? 0) > 0
const week = weekStartOf(new Date().toISOString().slice(0, 10))

describe.skipIf(!URL_)('permissions on the server, role by role', () => {
  let hh = ''
  let student = ''
  let spare = ''

  beforeAll(async () => {
    for (const r of ROLES) clients[r] = await as(U[r])
    hh = (await rpc('PARENT', 'create_household', { p_name: 'Permission family', p_time_zone: 'America/Chicago' })).data as string
    student = (await rpc('PARENT', 'add_student', { p_household: hh, p_display_name: 'Avery', p_graduation_year: 2029, p_grade_level: 10 })).data as string
    spare = (await rpc('PARENT', 'add_student', { p_household: hh, p_display_name: 'Sam', p_graduation_year: 2031, p_grade_level: 8 })).data as string
    const co = (await rpc('PARENT', 'create_household_invitation', { p_household: hh, p_role: 'guardian', p_student: null, p_ttl_hours: 72 })).data as string
    const view = (await rpc('PARENT', 'create_household_invitation', { p_household: hh, p_role: 'guardian', p_student: null, p_ttl_hours: 72, p_permissions: ['view_progress'] })).data as string
    const inv = (await rpc('PARENT', 'create_student_invitation', { p_household: hh, p_student: student })).data as { invite_code: string }[]
    for (const [r, code] of [['CO', co], ['VIEWER', view], ['STUDENT', inv[0]!.invite_code]] as const) {
      const res = await rpc(r, 'redeem_household_invitation', { p_code: code })
      expect((res.data as { outcome: string }[])[0]!.outcome).toBe('joined')
    }
    const plan = await clients.PARENT.from('student_planning_preferences').insert({ student_id: student, exam_family: 'act', goals: ['raise_score'], daily_minutes: 10 }).select()
    expect(plan.error).toBeNull()
  })

  it('reading: the household sees the student and plan; the outsider sees nothing', async () => {
    for (const r of ROLES) {
      const s = await clients[r].from('students').select('id').eq('id', student)
      const p = await clients[r].from('student_planning_preferences').select('daily_minutes').eq('student_id', student)
      const expected = r === 'OUTSIDER' ? 0 : 1
      expect([r, s.data?.length], 'students').toEqual([r, expected])
      expect([r, p.data?.length], 'plan').toEqual([r, expected])
    }
  })

  it('invitation hashes are never readable, by anyone; only guardians list invitations', async () => {
    for (const r of ROLES) {
      const hash = await clients[r].from('household_invitations').select('code_hash').eq('household_id', hh)
      expect([r, !!hash.error]).toEqual([r, true])
      const list = await clients[r].from('household_invitations').select('id, role').eq('household_id', hh)
      expect([r, (list.data?.length ?? 0) > 0]).toEqual([r, r === 'PARENT' || r === 'CO' || r === 'VIEWER'])
    }
  })

  it('plan and weekly goal: only guardians with set-goals change them', async () => {
    const allowed: Role[] = ['PARENT', 'CO']
    for (const r of ROLES) {
      const upd = await clients[r].from('student_planning_preferences').update({ daily_minutes: 15 }).eq('student_id', student).select()
      expect([r, wrote(upd)]).toEqual([r, allowed.includes(r)])
      await clients.PARENT.from('weekly_practice_goals').delete().eq('student_id', student).eq('week_start', week)
      const goal = await clients[r].from('weekly_practice_goals').insert({ student_id: student, week_start: week, target_questions: 20 }).select()
      expect([r, wrote(goal)]).toEqual([r, allowed.includes(r)])
    }
  })

  it('student profile edits need manage-students; the linked student in a household cannot edit their own profile', async () => {
    const allowed: Role[] = ['PARENT', 'CO']
    for (const r of ROLES) {
      const upd = await clients[r].from('students').update({ display_name: `Avery ${r}` }).eq('id', student).select()
      expect([r, wrote(upd)]).toEqual([r, allowed.includes(r)])
    }
  })

  it('inviting: guardians need manage-members; student invitations need manage-students', async () => {
    for (const r of ROLES) {
      const g = await rpc(r, 'create_household_invitation', { p_household: hh, p_role: 'guardian', p_student: null, p_ttl_hours: 72 })
      expect([r, !g.error]).toEqual([r, r === 'PARENT'])
      const s = await rpc(r, 'create_student_invitation', { p_household: hh, p_student: spare })
      expect([r, !s.error]).toEqual([r, r === 'PARENT' || r === 'CO'])
    }
  })

  it('member permissions and removal need manage-members, and the last manager cannot be removed', async () => {
    for (const r of ['CO', 'VIEWER', 'STUDENT', 'OUTSIDER'] as Role[]) {
      const up = await rpc(r, 'update_member_permissions', { p_household: hh, p_user: U.VIEWER, p_set_goals: true })
      expect([r, !!up.error]).toEqual([r, true])
      const rm = await rpc(r, 'remove_household_member', { p_household: hh, p_user: U.VIEWER })
      expect([r, !!rm.error]).toEqual([r, true])
    }
    const viewer = await clients.VIEWER.from('household_members').select('can_set_goals').eq('household_id', hh).eq('user_id', U.VIEWER).single()
    expect(viewer.data).toEqual({ can_set_goals: false })
    // The parent is the only member manager: they can't strip their own manage-members.
    const self = await rpc('PARENT', 'update_member_permissions', { p_household: hh, p_user: U.PARENT, p_manage_members: false })
    expect(self.error).toBeTruthy()
  })

  it('practice is the linked student’s own: no guardian or outsider can start a session or answer for them', async () => {
    for (const r of ROLES) {
      const s = await rpc(r, 'start_practice_session', { p_student: student, p_target_minutes: 5, p_exam_version: null })
      expect([r, !s.error]).toEqual([r, r === 'STUDENT'])
    }
    const q = await clients.STUDENT.from('practice_questions').select('id').eq('status', 'published').limit(1).single()
    for (const r of ['PARENT', 'CO', 'VIEWER', 'OUTSIDER'] as Role[]) {
      const a = await rpc(r, 'start_practice_attempt', { p_student: student, p_question: q.data!.id })
      expect([r, !!a.error]).toEqual([r, true])
    }
  })

  it('official scores: no client can write one; the linked student may report a self-reported score', async () => {
    const ev = (await clients.STUDENT.from('exam_versions').select('id').eq('exam_family', 'act').limit(1).single()).data!.id
    for (const r of ROLES) {
      const off = await clients[r].from('student_test_scores').insert({ student_id: student, exam_version_id: ev, test_date: '2026-06-13', composite: 30, score_source: 'official' }).select()
      expect([r, wrote(off)]).toEqual([r, false])
    }
    const self = await clients.STUDENT.from('student_test_scores').insert({ student_id: student, exam_version_id: ev, test_date: '2026-06-13', composite: 24, score_source: 'self_reported' }).select()
    expect(wrote(self)).toBe(true)
  })

  it('CR-10 exam plan: today any guardian may write it (open question #218 C1); the outsider may not', async () => {
    const cat = await clients.PARENT.from('exam_catalog').select('exam_key').eq('exam_key', 'ap:microeconomics').single()
    expect(cat.data).toBeTruthy()
    for (const r of ROLES) {
      await clients.PARENT.from('student_exam_plan').delete().eq('student_id', student).eq('exam_key', 'ap:microeconomics')
      const ins = await clients[r].from('student_exam_plan').insert({ student_id: student, exam_key: 'ap:microeconomics', score: 3 }).select()
      // Pinned server behaviour: the view-only guardian is allowed here, unlike plans and goals. The app doesn't offer it.
      expect([r, wrote(ins)]).toEqual([r, r !== 'OUTSIDER'])
    }
  })
})
