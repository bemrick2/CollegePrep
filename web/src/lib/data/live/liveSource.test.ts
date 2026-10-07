import { describe, expect, it, vi } from 'vitest'
import type { SupabaseClient } from '@supabase/supabase-js'
import { LiveSource } from './liveSource'

type Call = { kind: 'rpc' | 'from'; name: string; args?: unknown; ops: [string, unknown[]][] }

/** Records every table read and RPC; returns canned data per table/function. */
function fakeClient(data: Record<string, unknown>) {
  const calls: Call[] = []
  const builder = (call: Call) => {
    const b: Record<string, unknown> = {}
    for (const op of ['select', 'eq', 'is', 'not', 'order', 'gte', 'lte', 'in', 'ilike', 'limit', 'insert', 'update'])
      b[op] = (...a: unknown[]) => (call.ops.push([op, a]), b)
    b.maybeSingle = () => Promise.resolve({ data: data[`${call.name}:single`] ?? null, error: null })
    b.then = (res: (v: unknown) => unknown) => res({ data: data[call.name] ?? [], error: null })
    return b
  }
  const sb = {
    rpc: (name: string, args: unknown) => (calls.push({ kind: 'rpc', name, args, ops: [] }), Promise.resolve({ data: data[name] ?? null, error: null })),
    from: (name: string) => {
      const c: Call = { kind: 'from', name, ops: [] }
      calls.push(c)
      return builder(c)
    },
    auth: { getUser: () => Promise.resolve({ data: { user: { id: 'u1' } } }) },
    functions: {
      invoke: (name: string, opts: unknown) => (calls.push({ kind: 'rpc', name: `fn:${name}`, args: opts, ops: [] }), Promise.resolve({ data: data[`fn:${name}`] ?? null, error: null })),
    },
  }
  return { sb: sb as unknown as SupabaseClient, calls }
}

describe('LiveSource contracts (issue #37)', () => {
  it('CR-2: benchmark start, attempts attached to it, completion maps server metrics', async () => {
    const { sb, calls } = fakeClient({
      exam_versions: [{ id: 'ev1', effective_from: '2026-01-01', effective_to: null }],
      start_benchmark: 'bm1',
      complete_benchmark: { submitted: 10, accuracy: 0.6, pacing_ratio: 1.1, skips: 1, returns: 1, answer_changes: 0, by_section: { math: { submitted: 10, correct: 6, accuracy: 0.6, pacing_ratio: 1.1 } }, calibration: { by_confidence: { '3': { submitted: 4, accuracy: 0.75 } } }, traps: { sign_error: 2 }, definition: 'v1' },
    })
    const src = new LiveSource(sb)
    expect(await src.startBenchmark('s1', 'mini', 'act')).toBe('bm1')
    expect(calls.find((c) => c.name === 'start_benchmark')!.args).toEqual({ p_student: 's1', p_kind: 'mini', p_exam_version: 'ev1' })
    await src.startAttempt('s1', 'q1', null, 'bm1')
    expect(calls.find((c) => c.name === 'start_practice_attempt')!.args).toEqual({ p_student: 's1', p_question: 'q1', p_session: null, p_benchmark: 'bm1' })
    const client = { id: 'x', kind: 'mini', exam_family: 'act', started_at: 'a', completed_at: 'b', attempt_ids: ['a1'], metrics: { sections: [{ section: 'math', ceiling_difficulty: 3, skipped: 1 }], strategy_use: [], skip_events: 2 } } as never
    const done = await src.completeBenchmark('s1', 'bm1', client)
    expect(done.id).toBe('bm1')
    expect(done.metrics.accuracy).toBe(0.6)
    expect(done.metrics.correct).toBe(6)
    expect(done.metrics.sections[0]).toMatchObject({ section: 'math', accuracy: 0.6, ceiling_difficulty: 3 })
    expect(done.metrics.calibration).toEqual([{ confidence: 3, answered: 4, correct: 3 }])
    expect(done.metrics.traps_fallen).toEqual([{ trap: 'sign_error', count: 2 }])
  })

  it('CR-1: planning preferences read from and written to student_planning_preferences', async () => {
    const { sb, calls } = fakeClient({ 'student_planning_preferences:single': { exam_family: 'sat', target_score: 1300, goals: ['merit'], daily_minutes: 12 } })
    const src = new LiveSource(sb)
    expect(await src.getPlan('s1')).toEqual({ exam_family: 'sat', target_score: 1300, goals: ['merit'], daily_minutes: 12 })
    await src.savePlan('s1', { exam_family: 'act', target_score: 27, goals: [], daily_minutes: 10 })
    const writes = calls.filter((c) => c.name === 'student_planning_preferences').flatMap((c) => c.ops.map((o) => o[0]))
    expect(writes).toContain('update')
  })

  it('CR-9 / CR-7: saved schools through RPCs, verified-school listing', async () => {
    const { sb, calls } = fakeClient({ household_saved_schools: [{ institution_key: 'utk' }], institutions_with_verified_records: [{ institution_key: 'utk', level: 'four_year', domains: ['costs'] }] })
    const src = new LiveSource(sb)
    expect(await src.savedSchools('h1')).toEqual(['utk'])
    await src.saveSchool('h1', 'lipscomb')
    await src.removeSchool('h1', 'utk')
    expect(calls.filter((c) => c.kind === 'rpc').map((c) => [c.name, c.args])).toEqual([
      ['save_household_school', { p_household: 'h1', p_institution_key: 'lipscomb' }],
      ['remove_household_school', { p_household: 'h1', p_institution_key: 'utk' }],
    ])
    expect((await src.verifiedSchools('2026-27'))[0]!.level).toBe('four_year')
    expect(calls.at(-1)!.args).toEqual({ p_academic_year: '2026-27', p_state: null })
  })

  it('CR-12: the primary school is the saved row flagged is_primary, set through the RPC', async () => {
    const { sb, calls } = fakeClient({ 'household_saved_schools:single': { institution_key: 'utk' } })
    const src = new LiveSource(sb)
    expect(src.supportsPrimarySchool).toBe(true)
    expect(await src.primarySchool('h1')).toBe('utk')
    expect(calls[0]!.ops).toContainEqual(['eq', ['is_primary', true]])
    await src.setPrimarySchool('h1', null)
    expect(calls.at(-1)).toMatchObject({ kind: 'rpc', name: 'set_household_primary_school', args: { p_household: 'h1', p_institution_key: null } })
  })

  it('CR-13: interests read from and saved to student_academic_interests, dropping a false focus', async () => {
    const { sb, calls } = fakeClient({ 'student_academic_interests:single': { certainty: 'few', interests: [{ kind: 'major', key: 'finance' }] } })
    const src = new LiveSource(sb)
    expect(await src.interests('s1')).toEqual({ certainty: 'few', interests: [{ kind: 'major', key: 'finance' }] })
    await src.saveInterests('s1', { certainty: 'sure', interests: [{ kind: 'major', key: 'finance', focus: false }, { kind: 'area', key: 'business', focus: true }] })
    expect(calls.at(-1)!.ops).toContainEqual(['update', [{ certainty: 'sure', interests: [{ kind: 'major', key: 'finance' }, { kind: 'area', key: 'business', focus: true }] }]])
  })

  it('CR-4 v2: cost_projection gets the student, keys, year and assumptions as sent', async () => {
    const { sb, calls } = fakeClient({ cost_projection: { definition: 'v2', institutions: [] } })
    const r = await new LiveSource(sb).costProjection('s1', ['utk'], '2026-27', { residency: 'in_state', cost_basis: 'cost_of_attendance', exam_credits: 8 })
    expect(r.definition).toBe('v2')
    expect(calls[0]).toMatchObject({
      kind: 'rpc',
      name: 'cost_projection',
      args: { p_student: 's1', p_institution_keys: ['utk'], p_academic_year: '2026-27', p_assumptions: { residency: 'in_state', cost_basis: 'cost_of_attendance', exam_credits: 8 } },
    })
  })

  it('CR-16 billing: entitlement RPC, Checkout and Portal through edge functions; no Stripe keys in the client', async () => {
    const { sb, calls } = fakeClient({
      household_entitlement: { active: true, status: 'active', can_manage_billing: true, managed_by: 'web' },
      'fn:billing-checkout': { url: 'https://checkout.stripe.com/c/pay/cs_1' },
      'fn:billing-portal': { url: 'https://billing.stripe.com/p/session/1' },
      'fn:billing-plans': { plans: [{ lookup_key: 'pp_family_monthly', unit_amount: 1499, currency: 'usd', interval: 'month', product_name: 'Family' }] },
    })
    const src = new LiveSource(sb)
    expect((await src.entitlement('h1')).managed_by).toBe('web')
    expect(await src.startCheckout('h1', 'pp_family_monthly')).toBe('https://checkout.stripe.com/c/pay/cs_1')
    expect(await src.billingPortalUrl('h1')).toBe('https://billing.stripe.com/p/session/1')
    expect((await src.billingPlans())[0]!.lookup_key).toBe('pp_family_monthly')
    expect(calls.map((c) => [c.name, c.args])).toEqual([
      ['household_entitlement', { p_household: 'h1' }],
      ['fn:billing-checkout', { body: { household_id: 'h1', lookup_key: 'pp_family_monthly' } }],
      ['fn:billing-portal', { body: { household_id: 'h1' } }],
      ['fn:billing-plans', { method: 'GET' }],
    ])
  })

  it('CR-5 / CR-8: catalog and questions select the new content fields', async () => {
    const { sb, calls } = fakeClient({
      practice_questions: [{ id: 'q1', section: 'reading', difficulty: 2, difficulty_label: 'easy', stem: 'S', choices: [{ key: 'A', text: 'a' }], answer_format: 'choice', expected_time_seconds: 60, hint_count: 2, practice_passages: { title: 'T', body: 'B' }, exam_versions: { exam_family: 'act' }, practice_question_skills: [] }],
    })
    const src = new LiveSource(sb)
    await src.catalog('act')
    const sel = (t: string) => calls.find((c) => c.name === t)!.ops.find((o) => o[0] === 'select')![1][0] as string
    expect(sel('skills')).toContain('concept_summary')
    expect(sel('question_strategies')).toContain('sections')
    const [q] = await src.publishedQuestions('act')
    expect(q).toMatchObject({ hint_count: 2, passage: 'T\n\nB' })
  })
})

describe('sandbox billing status isolation', () => {
  it('uses sandbox display status only on the staging host with an explicit flag', async () => {
    vi.stubEnv('VITE_BILLING_ENVIRONMENT', 'sandbox')
    vi.stubGlobal('window', { location: { hostname: 'college-optimizer-staging.netlify.app' } })
    try {
      const { sb, calls } = fakeClient({ household_sandbox_billing_status: { active: true } })
      expect((await new LiveSource(sb).entitlement('h1')).active).toBe(true)
      expect(calls[0]!.name).toBe('household_sandbox_billing_status')
    } finally { vi.unstubAllEnvs(); vi.unstubAllGlobals() }
  })

  it('keeps the production entitlement RPC even if a sandbox flag reaches another host', async () => {
    vi.stubEnv('VITE_BILLING_ENVIRONMENT', 'sandbox')
    vi.stubGlobal('window', { location: { hostname: 'prepandprice.com' } })
    try {
      const { sb, calls } = fakeClient({ household_entitlement: { active: false } })
      expect((await new LiveSource(sb).entitlement('h1')).active).toBe(false)
      expect(calls[0]!.name).toBe('household_entitlement')
    } finally { vi.unstubAllEnvs(); vi.unstubAllGlobals() }
  })
})
