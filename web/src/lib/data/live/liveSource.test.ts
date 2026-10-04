import { describe, expect, it } from 'vitest'
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

  it('CR-12 pending: no primary school in live mode, and no client-side stand-in', async () => {
    const { sb, calls } = fakeClient({})
    const src = new LiveSource(sb)
    expect(src.supportsPrimarySchool).toBe(false)
    expect(await src.primarySchool('h1')).toBeNull()
    await expect(src.setPrimarySchool('h1', 'utk')).rejects.toThrow(/not available yet/)
    expect(calls).toHaveLength(0)
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
