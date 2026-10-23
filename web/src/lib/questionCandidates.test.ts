import { describe, expect, it } from 'vitest'
import { QUESTIONS } from './data/demo/fixtures'
import type { Ledger, SignOff } from './data/demo/editorialLedger'
import { IMPORT_CONTRACT, questionKey, type ImportedQuestion } from './questionImport'
import { answerKeyFor, eligibility, eligibleFor, emptyRegistry, intake, latest, retire, setTrack, summary, type Registry } from './questionCandidates'

function imp(i = 0, extra: Partial<ImportedQuestion> = {}): ImportedQuestion {
  const { id, ...q } = QUESTIONS[i]!
  return { ...q, contract: IMPORT_CONTRACT, import_id: `wk-${id}`.toLowerCase(), origin: 'ai_drafted', author: 'ai:example-model', license: 'original-owned', source_attribution: null, source_url: null, requested_pool: 'practice', ...extra }
}
const AT = '2026-10-23'
const reg0 = (items: ImportedQuestion[], batch = 'bank-original.jsonl') => intake(emptyRegistry(), items, batch, AT).registry

/** A complete, valid human review of the candidate's latest version. */
function fullReview(reg: Registry, id: string, overrides: Partial<Record<number, Partial<SignOff>>> = {}): Ledger {
  const c = reg.candidates[id]!
  const v = latest(c)
  const key = v.item.accepted_answers[0]!
  const so = (stage: SignOff['stage'], by: string, extra: Partial<SignOff> = {}): SignOff => ({ stage, by, date: AT, result: 'pass', hash: v.content_hash, ...extra, ...(overrides[stage] ?? {}) })
  return {
    items: {
      [id]: {
        author: v.item.author,
        signoffs: [so(3, 'Lee Rights', { license: 'original' }), so(4, 'Sam Solver', { answer: key }), so(4, 'Ana Solver', { answer: key }), so(5, 'Sam Solver'), so(6, 'Kim Fair'), so(7, 'Ed Copy'), so(8, 'Pat Lead')],
      },
    },
  }
}

describe('question candidates: tracks', () => {
  it('starts every candidate as a draft on its requested track, unconfirmed', () => {
    const reg = reg0([imp(0), imp(1, { requested_pool: 'assessment' })])
    const [a, b] = [reg.candidates[imp(0).import_id]!, reg.candidates[imp(1).import_id]!]
    expect(a).toMatchObject({ track: 'practice_candidate', status: 'draft', track_confirmed_by: null })
    expect(b).toMatchObject({ track: 'assessment_candidate', status: 'draft', track_confirmed_by: null })
  })

  it('only a named person who did not write the item sets a track, with a reason', () => {
    const reg = reg0([imp(0, { origin: 'human_original', author: 'Jo Writer' })])
    const id = imp(0).import_id
    expect(() => setTrack(reg, id, 'assessment_candidate', 'AI (Claude)', 'r', AT)).toThrow(/not a named person/)
    expect(() => setTrack(reg, id, 'assessment_candidate', 'Content Lead', 'r', AT)).toThrow(/not a named person/)
    expect(() => setTrack(reg, id, 'assessment_candidate', 'ai:gpt', 'r', AT)).toThrow(/not a named person/)
    expect(() => setTrack(reg, id, 'assessment_candidate', 'Pat Lead', ' ', AT)).toThrow(/reason/)
    expect(() => setTrack(reg, id, 'assessment_candidate', 'jo writer', 'r', AT)).toThrow(/wrote this item/)
    const after = setTrack(reg, id, 'assessment_candidate', 'Pat Lead', 'reserve for ACT mini check', AT)
    expect(after.candidates[id]).toMatchObject({ track: 'assessment_candidate', track_confirmed_by: 'Pat Lead' })
    expect(reg.candidates[id]!.track_confirmed_by).toBeNull() // the input is not changed
  })

  it('a reserved item may move to practice, never back; an exposed item is never reserved', () => {
    const id = imp(0).import_id
    let reg = reg0([imp(0, { requested_pool: 'assessment' })])
    reg = setTrack(reg, id, 'assessment_candidate', 'Pat Lead', 'reserve', AT)
    reg = setTrack(reg, id, 'practice_candidate', 'Pat Lead', 'enough reserve', AT)
    expect(() => setTrack(reg, id, 'assessment_candidate', 'Pat Lead', 'back', AT)).toThrow(/never becomes a reserved/)
    const fresh = reg0([imp(1)])
    expect(() => setTrack(fresh, imp(1).import_id, 'assessment_candidate', 'Pat Lead', 'r', AT, new Set([imp(1).import_id]))).toThrow(/seen in practice/)
  })

  it('never lists a candidate under the other track', () => {
    const p = imp(0).import_id
    const a = imp(1).import_id
    let reg = reg0([imp(0), imp(1, { requested_pool: 'assessment' })])
    reg = setTrack(setTrack(reg, p, 'practice_candidate', 'Pat Lead', 'r', AT), a, 'assessment_candidate', 'Pat Lead', 'r', AT)
    const ledger: Ledger = { items: { ...fullReview(reg, p).items, ...fullReview(reg, a).items } }
    expect(eligibleFor(reg, 'practice_candidate', ledger).map((e) => e.import_id)).toEqual([p])
    expect(eligibleFor(reg, 'assessment_candidate', ledger).map((e) => e.import_id)).toEqual([a])
  })
})

describe('question candidates: duplicates are retired, kept and excluded', () => {
  it('a later bank’s duplicate is kept as retired with duplicate_of, not deleted', () => {
    const reg = reg0([imp(0)])
    const dup = { ...imp(0), import_id: 'bank-b-0001', stem: imp(0).stem.toUpperCase() + '  ' }
    const { registry, result } = intake(reg, [dup], 'bank-B.jsonl', AT)
    expect(result.retired).toEqual([{ import_id: 'bank-b-0001', duplicate_of: imp(0).import_id }])
    expect(registry.candidates['bank-b-0001']).toMatchObject({ status: 'retired', duplicate_of: imp(0).import_id })
    expect(registry.candidates['bank-b-0001']!.versions).toHaveLength(1)
  })

  it('a duplicate of the app’s bank is retired as bank:<id>', () => {
    const bank = new Map([[questionKey(QUESTIONS[0]!), QUESTIONS[0]!.id]])
    const { registry } = intake(emptyRegistry(), [imp(0)], 'b.jsonl', AT, bank)
    expect(registry.candidates[imp(0).import_id]).toMatchObject({ status: 'retired', duplicate_of: `bank:${QUESTIONS[0]!.id}` })
  })

  it('a retired candidate is never eligible, even with a complete review', () => {
    const id = imp(0).import_id
    let reg = setTrack(reg0([imp(0)]), id, 'practice_candidate', 'Pat Lead', 'r', AT)
    const ledger = fullReview(reg, id)
    expect(eligibility(reg.candidates[id]!, ledger).eligible).toBe(true)
    reg = retire(reg, id, 'Pat Lead', 'superseded', AT)
    expect(eligibility(reg.candidates[id]!, ledger)).toMatchObject({ eligible: false })
    expect(eligibleFor(reg, 'practice_candidate', ledger)).toEqual([])
  })

  it('a retired candidate is not revived by a resubmission', () => {
    const id = imp(0).import_id
    const reg = retire(reg0([imp(0)]), id, 'Pat Lead', 'bad item', AT)
    const { registry, result } = intake(reg, [imp(0, { stem: 'A rewritten stem?' })], 'b2.jsonl', AT)
    expect(result.refused).toEqual([{ import_id: id, reason: 'retired' }])
    expect(registry.candidates[id]).toMatchObject({ status: 'retired' })
    expect(registry.candidates[id]!.versions).toHaveLength(1)
  })
})

describe('question candidates: versions and answer keys', () => {
  it('keeps every version and the full history; an identical resubmission adds no version', () => {
    const id = imp(0).import_id
    let reg = reg0([imp(0)])
    reg = intake(reg, [imp(0)], 'again.jsonl', AT).registry
    expect(reg.candidates[id]!.versions).toHaveLength(1)
    reg = intake(reg, [imp(0, { teaching_explanation: 'Clearer explanation.' })], 'rev.jsonl', '2026-10-24').registry
    const c = reg.candidates[id]!
    expect(c.versions.map((v) => v.version)).toEqual([1, 2])
    expect(c.versions[0]!.item.teaching_explanation).toBe(QUESTIONS[0]!.teaching_explanation)
    expect(c.history.map((h) => h.event)).toEqual(['received', 'unchanged_resubmission', 'revised'])
    expect(c.history[2]).toMatchObject({ previous_hash: c.versions[0]!.content_hash, content_hash: c.versions[1]!.content_hash, key_carried: true })
  })

  it('a revision voids the earlier review: approval on v1 does not make v2 eligible', () => {
    const id = imp(0).import_id
    let reg = setTrack(reg0([imp(0)]), id, 'practice_candidate', 'Pat Lead', 'r', AT)
    const v1Review = fullReview(reg, id)
    expect(eligibility(reg.candidates[id]!, v1Review).eligible).toBe(true)
    reg = intake(reg, [imp(0, { stem: QUESTIONS[0]!.stem + ' (revised)' })], 'rev.jsonl', AT).registry
    const e = eligibility(reg.candidates[id]!, v1Review)
    expect(e).toMatchObject({ eligible: false, version: 2 })
    expect(e.problems.join(' ')).toMatch(/earlier content and no longer count/)
  })

  it('an old key never attaches to a revised question', () => {
    const id = imp(0).import_id
    let reg = reg0([imp(0)])
    const v1 = latest(reg.candidates[id]!)
    const v1Review = fullReview(reg, id)
    expect(answerKeyFor(reg.candidates[id]!, v1.content_hash, v1Review)).toMatchObject({ version: 1, verified: true })
    reg = intake(reg, [imp(0, { stem: QUESTIONS[0]!.stem + ' (revised)' })], 'rev.jsonl', AT).registry
    const c = reg.candidates[id]!
    const v2 = latest(c)
    // Same key text, carried from v1, but unverified for v2 until two new blind solves of v2 match it.
    expect(answerKeyFor(c, v2.content_hash, v1Review)).toMatchObject({ version: 2, verified: false, carried_from: 1 })
    expect(() => answerKeyFor(c, 'not-a-version-hash', v1Review)).toThrow(/never attached to other content/)
    // v1's key is still readable for v1 only (history), and stays bound to v1's content.
    expect(answerKeyFor(c, v1.content_hash, v1Review).version).toBe(1)
  })

  it('a changed key is never verified by solves that matched the old key', () => {
    const i = QUESTIONS.findIndex((q) => q.answer_format === 'choice')
    const id = imp(i).import_id
    let reg = reg0([imp(i)])
    const old = imp(i).accepted_answers[0]!
    const other = imp(i).choices.find((c) => c.key !== old)!.key
    reg = intake(reg, [imp(i, { accepted_answers: [other], distractors: imp(i).distractors.map((d) => (d.choice === other ? { ...d, choice: old } : d)) })], 'rev.jsonl', AT).registry
    const c = reg.candidates[id]!
    const v2 = latest(c)
    // Solves recorded against v2's hash but giving the old key do not verify v2's key.
    const ledger = fullReview(reg, id, { 4: { answer: old } })
    const k = answerKeyFor(c, v2.content_hash, ledger)
    expect(k).toMatchObject({ accepted_answers: [other], verified: false })
    expect(k.carried_from).toBeUndefined()
    expect(eligibility(c, ledger).eligible).toBe(false)
  })

  it('a revision that duplicates another live candidate is refused and recorded', () => {
    let reg = reg0([imp(0), imp(1)])
    const { registry, result } = intake(reg, [imp(1, { stem: imp(0).stem, passage: imp(0).passage, choices: imp(0).choices })], 'rev.jsonl', AT)
    expect(result.refused).toEqual([{ import_id: imp(1).import_id, reason: `revision duplicates ${imp(0).import_id}` }])
    expect(registry.candidates[imp(1).import_id]!.versions).toHaveLength(1)
    reg = registry
    expect(reg.candidates[imp(1).import_id]!.history.at(-1)).toMatchObject({ event: 'refused' })
  })
})

describe('question candidates: publication eligibility is per item and never weaker than the ledger', () => {
  const id = imp(0).import_id
  const confirmed = () => setTrack(reg0([imp(0, { origin: 'human_original', author: 'Jo Writer' })]), id, 'practice_candidate', 'Pat Lead', 'r', AT)

  it('today, with an empty ledger, nothing is eligible', () => {
    const reg = reg0(QUESTIONS.map((_, i) => imp(i)))
    expect(summary(reg)).toMatchObject({ practice_candidate: { eligible: 0 }, assessment_candidate: { eligible: 0 } })
  })

  it('needs a confirmed track', () => {
    const reg = reg0([imp(0)])
    expect(eligibility(reg.candidates[id]!, fullReview(reg, id)).problems).toContain('track is only the workstream’s request; the content lead has not confirmed it')
  })

  it('the import author can’t approve their own item, even with no ledger author recorded', () => {
    const reg = confirmed()
    const l = fullReview(reg, id, { 8: { by: 'Jo Writer' } })
    l.items[id]!.author = 'AI (Claude)' // the ledger default must not let the real author through
    const e = eligibility(reg.candidates[id]!, l)
    expect(e.eligible).toBe(false)
    expect(e.problems).toContain('needs approval by a named content lead who is not the author')
  })

  it('a blind solve by any version’s author does not verify the key', () => {
    let reg = confirmed()
    reg = intake(reg, [imp(0, { origin: 'human_original', author: 'Ed Editor', stem: QUESTIONS[0]!.stem + ' (edited)' })], 'rev.jsonl', AT).registry
    const c = reg.candidates[id]!
    const l = fullReview(reg, id)
    const key = latest(c).item.accepted_answers[0]!
    l.items[id]!.signoffs = l.items[id]!.signoffs.filter((s) => s.stage !== 4).concat(
      { stage: 4, by: 'Jo Writer', date: AT, result: 'pass', hash: latest(c).content_hash, answer: key },
      { stage: 4, by: 'Ana Solver', date: AT, result: 'pass', hash: latest(c).content_hash, answer: key },
    )
    expect(answerKeyFor(c, latest(c).content_hash, l).verified).toBe(false)
  })

  it('an author of an earlier version is not an independent solver or approver', () => {
    let reg = confirmed()
    reg = intake(reg, [imp(0, { origin: 'human_original', author: 'Ed Editor', stem: QUESTIONS[0]!.stem + ' (edited)' })], 'rev.jsonl', AT).registry
    const l = fullReview(reg, id, { 6: { by: 'Jo Writer' } })
    l.items[id]!.author = 'Ed Editor'
    const e = eligibility(reg.candidates[id]!, l)
    expect(e.eligible).toBe(false)
    expect(e.problems.join(' ')).toMatch(/author of an earlier version/)
  })

  it('a complete individual review of the latest version is eligible; one failed stage is not', () => {
    const reg = confirmed()
    expect(eligibility(reg.candidates[id]!, fullReview(reg, id)).eligible).toBe(true)
    expect(eligibility(reg.candidates[id]!, fullReview(reg, id, { 6: { result: 'fail', note: 'stereotype' } })).eligible).toBe(false)
  })

  it('approving other items (a sample) does not make an unreviewed item eligible', () => {
    const items = QUESTIONS.slice(0, 5).map((_, i) => imp(i))
    let reg = reg0(items)
    for (const x of items) reg = setTrack(reg, x.import_id, 'practice_candidate', 'Pat Lead', 'r', AT)
    const sampled = items.slice(0, 2)
    const ledger: Ledger = { items: Object.assign({}, ...sampled.map((x) => fullReview(reg, x.import_id).items)) }
    expect(eligibleFor(reg, 'practice_candidate', ledger).map((e) => e.import_id).sort()).toEqual(sampled.map((x) => x.import_id).sort())
  })
})
