import { beforeEach, describe, expect, it } from 'vitest'
import { DemoSource, DEMO_PARENT, DEMO_STUDENT } from './demoSource'
import { emptyStore } from './store'
import { QUESTIONS } from './fixtures'
import { sampleFamily } from './seed'

let src: DemoSource

beforeEach(() => {
  src = new DemoSource(emptyStore())
})

async function parentWithStudent() {
  src.switchPersona(DEMO_PARENT, 'Parent')
  const hid = await src.createHousehold('Test household', 'UTC')
  const sid = await src.addStudent(hid, 'Ava', 2028, 10)
  const code = await src.createInvitation(hid, 'student', sid)
  return { hid, sid, code }
}

describe('DemoSource follows the backend access rules', () => {
  it('lets a student claim a guardian-created profile by code', async () => {
    const { sid, code } = await parentWithStudent()
    src.switchPersona(DEMO_STUDENT, 'Ava')
    await src.acceptInvitation(code)
    const ctx = await src.getHouseholdContext()
    expect(ctx.myStudent?.id).toBe(sid)
    await expect(src.acceptInvitation(code)).rejects.toThrow(/already been used/)
  })

  it('never lets a guardian practise as the student', async () => {
    const { sid } = await parentWithStudent()
    await expect(src.startAttempt(sid, QUESTIONS[0]!.id, null)).rejects.toThrow(/own login/)
    await expect(src.startSession(sid, 10, 'act')).rejects.toThrow(/own login/)
  })

  it('reveals answers only on submit, and grades on the source side', async () => {
    src.switchPersona(DEMO_STUDENT, 'Ava')
    const sid = await src.createSelfStudentProfile({ displayName: 'Ava', graduationYear: null, gradeLevel: 10, independent: false, timeZone: 'UTC' })
    const session = await src.startSession(sid, 10, 'act')
    expect(session.items.length).toBeGreaterThan(0)
    const pub = session.items[0]!.question as unknown as Record<string, unknown>
    for (const hidden of ['accepted_answers', 'hints', 'teaching_explanation', 'strategy_explanation', 'distractors']) expect(pub).not.toHaveProperty(hidden)

    const fixture = QUESTIONS.find((q) => q.id === session.items[0]!.question.id)!
    const id = await src.startAttempt(sid, fixture.id, session.id)
    const res = await src.submitAttempt(id, { answer: fixture.accepted_answers[0]!, confidence: 3 })
    expect(res.is_correct).toBe(true)
    expect(res.accepted_answers).toEqual(fixture.accepted_answers)
    await expect(src.submitAttempt(id, { answer: 'A' })).rejects.toThrow(/already submitted/)
  })

  it('keeps skips out of accuracy', async () => {
    src.switchPersona(DEMO_STUDENT, 'Ava')
    const sid = await src.createSelfStudentProfile({ displayName: 'Ava', graduationYear: null, gradeLevel: 10, independent: false, timeZone: 'UTC' })
    const q = QUESTIONS[0]!
    const id = await src.startAttempt(sid, q.id, null)
    await expect(src.submitAttempt(id, { answer: 'A', skipped: true })).rejects.toThrow(/no answer/)
    const r = await src.submitAttempt(id, { answer: null, skipped: true })
    expect(r.is_correct).toBeNull()
    const w = await src.weeklyProgress(sid, weekStart())
    expect(w.questions_submitted).toBe(0)
    expect(w.skipped).toBe(1)
    expect(w.accuracy).toBeNull()
  })

  it('logs answer changes and runs out of hints', async () => {
    src.switchPersona(DEMO_STUDENT, 'Ava')
    const sid = await src.createSelfStudentProfile({ displayName: 'Ava', graduationYear: null, gradeLevel: 10, independent: false, timeZone: 'UTC' })
    const q = QUESTIONS.find((x) => x.answer_format === 'choice')!
    const id = await src.startAttempt(sid, q.id, null)
    expect(await src.recordEvent(id, 'answered', 'A')).toBe('answered')
    expect(await src.recordEvent(id, 'answered', 'A')).toBe('unchanged')
    expect(await src.recordEvent(id, 'answered', 'B')).toBe('changed_answer')
    for (let i = 0; i < q.hints.length; i++) await src.requestHint(id)
    await expect(src.requestHint(id)).rejects.toThrow(/No more hints/)
  })

  it('reports AI help as disabled, matching the backend default', async () => {
    src.switchPersona(DEMO_STUDENT, 'Ava')
    const sid = await src.createSelfStudentProfile({ displayName: 'Ava', graduationYear: null, gradeLevel: 10, independent: false, timeZone: 'UTC' })
    const id = await src.startAttempt(sid, QUESTIONS[0]!.id, null)
    await expect(src.requestAiHelp(id, 'answer_reveal')).rejects.toThrow(/after submission/)
    expect((await src.requestAiHelp(id, 'concept')).status).toBe('disabled')
  })

  it('returns comparison snapshots only for the captured year, and explicit not-found otherwise', async () => {
    const [utk] = await src.compareInstitutions(['utk'], '2026-27')
    expect(utk!.found).toBe(true)
    expect(utk!.domains.costs.length).toBeGreaterThan(0)
    const [old] = await src.compareInstitutions(['utk'], '2025-26')
    expect(old!.found).toBe(false)
  })

  it('builds a coherent sample family', async () => {
    const s = new DemoSource(sampleFamily('parent', new Date('2026-10-02T18:00:00Z')))
    const ctx = await s.getHouseholdContext()
    expect(ctx.students).toHaveLength(1)
    const sid = ctx.students[0]!.id
    expect((await s.listBenchmarks(sid))[0]!.metrics.answered).toBeGreaterThan(0)
    expect((await s.skillEstimates(sid)).length).toBeGreaterThan(5)
  })
})

function weekStart() {
  const d = new Date()
  const day = (d.getUTCDay() + 6) % 7
  d.setUTCDate(d.getUTCDate() - day)
  return d.toISOString().slice(0, 10)
}
