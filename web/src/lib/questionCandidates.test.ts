import { describe, expect, it } from 'vitest'
import { QUESTIONS } from './data/demo/fixtures'
import type { Ledger, SignOff } from './data/demo/editorialLedger'
import { IMPORT_CONTRACT, questionKey, type ImportedQuestion } from './questionImport'
import * as QC from './questionCandidates'
import { emptyRegistry, intake, latest, rightsHash, type Registry, type Track } from './questionCandidates'
import { testId, testReviewers } from './data/demo/testReviewers'

// TEST ONLY reviewers (testReviewers.ts). Tests name people by display name; the wrappers pass their stable test ids.
const R = testReviewers()
const rid = (who: string) => (who.startsWith('rv-') ? who : testId(who))
const setTrack = (reg: Registry, id: string, t: Track, who: string, reason: string, at: string, exposed: Set<string>) => QC.setTrack(reg, id, t, rid(who), reason, at, exposed, R)
const retire = (reg: Registry, id: string, who: string, reason: string, at: string, dup?: string) => QC.retire(reg, id, rid(who), reason, at, dup, R)
const eligibility = (c: QC.Candidate, l?: Ledger) => QC.eligibility(c, l, R)
const eligibleFor = (reg: Registry, t: Track, l?: Ledger) => QC.eligibleFor(reg, t, l, R)
const answerKeyFor = (c: QC.Candidate, h: string, l?: Ledger) => QC.answerKeyFor(c, h, l, R)
const summary = (reg: Registry, l?: Ledger) => QC.summary(reg, l, R)
/** A sign-off by the TEST reviewer with this display name. */
const sig = (stage: SignOff['stage'], by: string, hash: string, extra: Partial<SignOff> = {}): SignOff => ({ stage, reviewer_id: testId(by), by, date: '2026-10-23', result: 'pass', hash, ...extra })

function imp(i = 0, extra: Partial<ImportedQuestion> = {}): ImportedQuestion {
  const { id, ...q } = QUESTIONS[i]!
  return { ...q, contract: IMPORT_CONTRACT, import_id: `wk-${id}`.toLowerCase(), origin: 'ai_drafted', author: 'ai:example-model', license: 'original-owned', source_attribution: null, source_url: null, requested_pool: 'practice', ...extra }
}
const AT = '2026-10-23'
const NOBANK = new Map<string, string>()
const NONE = new Set<string>()
const reg0 = (items: ImportedQuestion[], batch = 'bank-original.jsonl') => intake(emptyRegistry(), items, batch, AT, NOBANK).registry

/** A complete, valid human review of the candidate's latest version. */
function fullReview(reg: Registry, id: string, overrides: Partial<Record<number, Partial<SignOff>>> = {}): Ledger {
  const c = reg.candidates[id]!
  const v = latest(c)
  const key = v.item.accepted_answers[0]!
  const so = (stage: SignOff['stage'], by: string, extra: Partial<SignOff> = {}): SignOff => {
    const x: SignOff = { stage, reviewer_id: '', by, date: AT, result: 'pass', hash: v.content_hash, ...(stage === 3 ? { rights_hash: rightsHash(v) } : {}), ...extra, ...(overrides[stage] ?? {}) }
    return { ...x, reviewer_id: overrides[stage]?.reviewer_id ?? testId(x.by) }
  }
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

  it('only an active content lead, by reviewer id, who did not write the item sets a track, with a reason', () => {
    const reg = reg0([imp(0, { origin: 'human_original', author: 'Jo Writer' })])
    const id = imp(0).import_id
    expect(() => setTrack(reg, id, 'assessment_candidate', 'AI (Claude)', 'r', AT, NONE)).toThrow(/not an active content lead/)
    expect(() => setTrack(reg, id, 'assessment_candidate', 'Ana Solver', 'r', AT, NONE)).toThrow(/not an active content lead/) // registered, wrong role
    expect(() => QC.setTrack(reg, id, 'assessment_candidate', testId('Pat Lead'), 'r', AT, NONE)).toThrow(/not an active content lead/) // the real registry is empty
    expect(() => setTrack(reg, id, 'assessment_candidate', 'Pat Lead', ' ', AT, NONE)).toThrow(/reason/)
    expect(() => setTrack(reg, id, 'assessment_candidate', 'jo writer', 'r', AT, NONE)).toThrow(/wrote this item/)
    const after = setTrack(reg, id, 'assessment_candidate', 'Pat Lead', 'reserve for ACT mini check', AT, NONE)
    expect(after.candidates[id]).toMatchObject({ track: 'assessment_candidate', track_confirmed_by: testId('Pat Lead') })
    expect(reg.candidates[id]!.track_confirmed_by).toBeNull() // the input is not changed
  })

  it('a reserved item may move to practice, never back; an exposed item is never reserved', () => {
    const id = imp(0).import_id
    let reg = reg0([imp(0, { requested_pool: 'assessment' })])
    reg = setTrack(reg, id, 'assessment_candidate', 'Pat Lead', 'reserve', AT, NONE)
    reg = setTrack(reg, id, 'practice_candidate', 'Pat Lead', 'enough reserve', AT, NONE)
    expect(() => setTrack(reg, id, 'assessment_candidate', 'Pat Lead', 'back', AT, NONE)).toThrow(/never becomes a reserved/)
    const fresh = reg0([imp(1)])
    expect(() => setTrack(fresh, imp(1).import_id, 'assessment_candidate', 'Pat Lead', 'r', AT, new Set([imp(1).import_id]))).toThrow(/seen in practice/)
  })

  it('never lists a candidate under the other track', () => {
    const p = imp(0).import_id
    const a = imp(1).import_id
    let reg = reg0([imp(0), imp(1, { requested_pool: 'assessment' })])
    reg = setTrack(setTrack(reg, p, 'practice_candidate', 'Pat Lead', 'r', AT, NONE), a, 'assessment_candidate', 'Pat Lead', 'r', AT, NONE)
    const ledger: Ledger = { items: { ...fullReview(reg, p).items, ...fullReview(reg, a).items } }
    expect(eligibleFor(reg, 'practice_candidate', ledger).map((e) => e.import_id)).toEqual([p])
    expect(eligibleFor(reg, 'assessment_candidate', ledger).map((e) => e.import_id)).toEqual([a])
  })
})

describe('question candidates: duplicates are retired, kept and excluded', () => {
  it('a later bank’s duplicate is kept as retired with duplicate_of, not deleted', () => {
    const reg = reg0([imp(0)])
    const dup = { ...imp(0), import_id: 'bank-b-0001', stem: imp(0).stem.toUpperCase() + '  ' }
    const { registry, result } = intake(reg, [dup], 'bank-B.jsonl', AT, NOBANK)
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
    let reg = setTrack(reg0([imp(0)]), id, 'practice_candidate', 'Pat Lead', 'r', AT, NONE)
    const ledger = fullReview(reg, id)
    expect(eligibility(reg.candidates[id]!, ledger).eligible).toBe(true)
    reg = retire(reg, id, 'Pat Lead', 'superseded', AT)
    expect(eligibility(reg.candidates[id]!, ledger)).toMatchObject({ eligible: false })
    expect(eligibleFor(reg, 'practice_candidate', ledger)).toEqual([])
  })

  it('a retired candidate is not revived by a resubmission', () => {
    const id = imp(0).import_id
    const reg = retire(reg0([imp(0)]), id, 'Pat Lead', 'bad item', AT)
    const { registry, result } = intake(reg, [imp(0, { stem: 'A rewritten stem?' })], 'b2.jsonl', AT, NOBANK)
    expect(result.refused).toEqual([{ import_id: id, reason: 'retired' }])
    expect(registry.candidates[id]).toMatchObject({ status: 'retired' })
    expect(registry.candidates[id]!.versions).toHaveLength(1)
  })
})

describe('question candidates: versions and answer keys', () => {
  it('keeps every version and the full history; an identical resubmission adds no version', () => {
    const id = imp(0).import_id
    let reg = reg0([imp(0)])
    reg = intake(reg, [imp(0)], 'again.jsonl', AT, NOBANK).registry
    expect(reg.candidates[id]!.versions).toHaveLength(1)
    reg = intake(reg, [imp(0, { teaching_explanation: 'Clearer explanation.' })], 'rev.jsonl', '2026-10-24', NOBANK).registry
    const c = reg.candidates[id]!
    expect(c.versions.map((v) => v.version)).toEqual([1, 2])
    expect(c.versions[0]!.item.teaching_explanation).toBe(QUESTIONS[0]!.teaching_explanation)
    expect(c.history.map((h) => h.event)).toEqual(['received', 'unchanged_resubmission', 'revised'])
    expect(c.history[2]).toMatchObject({ previous_hash: c.versions[0]!.content_hash, content_hash: c.versions[1]!.content_hash, key_carried: true })
  })

  it('a revision voids the earlier review: approval on v1 does not make v2 eligible', () => {
    const id = imp(0).import_id
    let reg = setTrack(reg0([imp(0)]), id, 'practice_candidate', 'Pat Lead', 'r', AT, NONE)
    const v1Review = fullReview(reg, id)
    expect(eligibility(reg.candidates[id]!, v1Review).eligible).toBe(true)
    reg = intake(reg, [imp(0, { stem: QUESTIONS[0]!.stem + ' (revised)' })], 'rev.jsonl', AT, NOBANK).registry
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
    reg = intake(reg, [imp(0, { stem: QUESTIONS[0]!.stem + ' (revised)' })], 'rev.jsonl', AT, NOBANK).registry
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
    reg = intake(reg, [imp(i, { accepted_answers: [other], distractors: imp(i).distractors.map((d) => (d.choice === other ? { ...d, choice: old } : d)) })], 'rev.jsonl', AT, NOBANK).registry
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
    const { registry, result } = intake(reg, [imp(1, { stem: imp(0).stem, passage: imp(0).passage, choices: imp(0).choices })], 'rev.jsonl', AT, NOBANK)
    expect(result.refused).toEqual([{ import_id: imp(1).import_id, reason: `revision duplicates ${imp(0).import_id}` }])
    expect(registry.candidates[imp(1).import_id]!.versions).toHaveLength(1)
    reg = registry
    expect(reg.candidates[imp(1).import_id]!.history.at(-1)).toMatchObject({ event: 'refused' })
  })
})

describe('question candidates: publication eligibility is per item and never weaker than the ledger', () => {
  const id = imp(0).import_id
  const confirmed = () => setTrack(reg0([imp(0, { origin: 'human_original', author: 'Jo Writer' })]), id, 'practice_candidate', 'Pat Lead', 'r', AT, NONE)

  it('today, with an empty ledger, nothing is eligible even with every track confirmed', () => {
    let reg = reg0(QUESTIONS.map((_, i) => imp(i)))
    for (const c of Object.values(reg.candidates)) reg = setTrack(reg, c.import_id, c.track, 'Pat Lead', 'r', AT, NONE)
    expect(summary(reg)).toMatchObject({ practice_candidate: { eligible: 0 }, assessment_candidate: { eligible: 0 } })
    for (const c of Object.values(reg.candidates)) expect(eligibility(c).problems).toContain('editorial review is at stage 3')
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
    expect(e.problems).toContain('needs approval by an authorized approver who is not the author')
  })

  it('a blind solve by any version’s author does not verify the key', () => {
    let reg = confirmed()
    reg = intake(reg, [imp(0, { origin: 'human_original', author: 'Ed Editor', stem: QUESTIONS[0]!.stem + ' (edited)' })], 'rev.jsonl', AT, NOBANK).registry
    const c = reg.candidates[id]!
    const l = fullReview(reg, id)
    const key = latest(c).item.accepted_answers[0]!
    l.items[id]!.signoffs = l.items[id]!.signoffs.filter((s) => s.stage !== 4).concat(
      sig(4, 'Jo Writer', latest(c).content_hash, { answer: key }),
      sig(4, 'Ana Solver', latest(c).content_hash, { answer: key }),
    )
    expect(answerKeyFor(c, latest(c).content_hash, l).verified).toBe(false)
  })

  it('an author of an earlier version is not an independent solver or approver', () => {
    let reg = confirmed()
    reg = intake(reg, [imp(0, { origin: 'human_original', author: 'Ed Editor', stem: QUESTIONS[0]!.stem + ' (edited)' })], 'rev.jsonl', AT, NOBANK).registry
    const l = fullReview(reg, id, { 6: { by: 'Jo Writer' } })
    l.items[id]!.author = 'Ed Editor'
    const e = eligibility(reg.candidates[id]!, l)
    expect(e.eligible).toBe(false)
    expect(e.problems.join(' ')).toMatch(/needs a fairness review by an authorized reviewer other than the author/)
  })

  it('a complete individual review of the latest version is eligible; one failed stage is not', () => {
    const reg = confirmed()
    expect(eligibility(reg.candidates[id]!, fullReview(reg, id)).eligible).toBe(true)
    expect(eligibility(reg.candidates[id]!, fullReview(reg, id, { 6: { result: 'fail', note: 'stereotype' } })).eligible).toBe(false)
  })

  it('approving other items (a sample) does not make an unreviewed item eligible', () => {
    const items = QUESTIONS.slice(0, 5).map((_, i) => imp(i))
    let reg = reg0(items)
    for (const x of items) reg = setTrack(reg, x.import_id, 'practice_candidate', 'Pat Lead', 'r', AT, NONE)
    const sampled = items.slice(0, 2)
    const ledger: Ledger = { items: Object.assign({}, ...sampled.map((x) => fullReview(reg, x.import_id).items)) }
    expect(eligibleFor(reg, 'practice_candidate', ledger).map((e) => e.import_id).sort()).toEqual(sampled.map((x) => x.import_id).sort())
  })
})

describe('question candidates: review findings (names, reverts, duplicates, history)', () => {
  const id = imp(0).import_id
  const human = (extra: Partial<ImportedQuestion> = {}) => imp(0, { origin: 'human_original', author: 'Jo Writer', ...extra })
  const confirmedHuman = () => setTrack(reg0([human()]), id, 'practice_candidate', 'Pat Lead', 'r', AT, NONE)

  it('a revision may not return to an earlier version (that would revive its review)', () => {
    let reg = confirmedHuman()
    const v1Review = fullReview(reg, id)
    reg = intake(reg, [human({ stem: QUESTIONS[0]!.stem + ' (revised)' })], 'v2.jsonl', AT, NOBANK).registry
    const { registry, result } = intake(reg, [human()], 'v3.jsonl', AT, NOBANK)
    expect(result.refused).toEqual([{ import_id: id, reason: 'reverts to version 1' }])
    expect(registry.candidates[id]!.versions).toHaveLength(2)
    expect(eligibility(registry.candidates[id]!, v1Review).eligible).toBe(false)
  })

  it('a revision into a copy of a bank question is refused', () => {
    const bank = new Map([[questionKey(QUESTIONS[5]!), QUESTIONS[5]!.id]])
    const reg = intake(emptyRegistry(), [imp(0)], 'a.jsonl', AT, bank).registry
    const { result } = intake(reg, [imp(0, { stem: QUESTIONS[5]!.stem, passage: QUESTIONS[5]!.passage, choices: QUESTIONS[5]!.choices })], 'b.jsonl', AT, bank)
    expect(result.refused).toEqual([{ import_id: id, reason: `revision duplicates bank:${QUESTIONS[5]!.id}` }])
  })

  it('retired content does not come back under a new import_id', () => {
    const reg = retire(reg0([imp(0)]), id, 'Pat Lead', 'key leaked', AT)
    const { registry, result } = intake(reg, [{ ...imp(0), import_id: 'wk-new-0001' }], 'b.jsonl', AT, NOBANK)
    expect(result.retired).toEqual([{ import_id: 'wk-new-0001', duplicate_of: id }])
    expect(registry.candidates['wk-new-0001']!.status).toBe('retired')
  })

  it('an earlier version’s question is still a duplicate, for new items and for revisions', () => {
    let reg = reg0([imp(0), imp(1)])
    reg = intake(reg, [imp(0, { stem: 'A rewritten stem?' })], 'v2.jsonl', AT, NOBANK).registry
    const n = intake(reg, [{ ...imp(0), import_id: 'wk-new-0002' }], 'b.jsonl', AT, NOBANK)
    expect(n.result.retired).toEqual([{ import_id: 'wk-new-0002', duplicate_of: id }])
    const r = intake(reg, [imp(1, { stem: imp(0).stem, passage: imp(0).passage, choices: imp(0).choices })], 'b.jsonl', AT, NOBANK)
    expect(r.result.refused).toEqual([{ import_id: imp(1).import_id, reason: `revision duplicates ${id}` }])
  })

  it('an import_id that is a bank id is refused', () => {
    const bank = new Map([[questionKey(QUESTIONS[5]!), QUESTIONS[5]!.id]])
    const { result } = intake(emptyRegistry(), [{ ...imp(0), import_id: QUESTIONS[5]!.id }], 'a.jsonl', AT, bank)
    expect(result.refused).toEqual([{ import_id: QUESTIONS[5]!.id, reason: 'import_id is a bank id' }])
  })

  it('eligibility reads the history, not editable summary fields', () => {
    let reg = confirmedHuman()
    const l = fullReview(reg, id)
    reg = retire(reg, id, 'Pat Lead', 'bad', AT)
    reg.candidates[id]!.status = 'draft' // a hand edit
    expect(eligibility(reg.candidates[id]!, l).eligible).toBe(false)
    const fresh = reg0([human()])
    fresh.candidates[id]!.track_confirmed_by = 'Pat Lead' // no track_set event
    expect(eligibility(fresh.candidates[id]!, fullReview(fresh, id)).eligible).toBe(false)
  })

  it('a track confirmer who later writes a version no longer counts as the confirmer', () => {
    let reg = confirmedHuman()
    reg = intake(reg, [human({ author: 'Pat Lead', stem: QUESTIONS[0]!.stem + ' (edited)' })], 'v2.jsonl', AT, NOBANK).registry
    const l = fullReview(reg, id, { 8: { by: 'Lee Rights' } })
    expect(eligibility(reg.candidates[id]!, l).problems).toContain(`track confirmed by ${testId('Pat Lead')}, who wrote a version of this item`)
  })

  it('a rights or author change voids the rights check by version, and a same-day re-check of the new version counts', () => {
    let reg = confirmedHuman()
    const l = fullReview(reg, id)
    expect(eligibility(reg.candidates[id]!, l).eligible).toBe(true)
    const r = intake(reg, [human({ license: 'licensed:acme', origin: 'licensed', source_attribution: 'Acme' })], 'v2.jsonl', AT, NOBANK)
    expect(r.result.revised).toEqual([id])
    reg = r.registry
    const c = reg.candidates[id]!
    expect(c.versions).toHaveLength(2)
    expect(c.versions[1]!.content_hash).toBe(c.versions[0]!.content_hash)
    expect(rightsHash(c.versions[1]!)).not.toBe(rightsHash(c.versions[0]!))
    expect(eligibility(c, l).problems.join(' ')).toMatch(/rights check was for an earlier rights version/)
    // Re-checked the same day, bound to the new rights version: counts at once. No date is compared.
    l.items[id]!.signoffs.push(sig(3, 'Lee Rights', c.versions[1]!.content_hash, { date: AT, license: 'licensed: acme', rights_hash: rightsHash(c.versions[1]!) }))
    expect(eligibility(c, l).problems.join(' ')).toMatch(/no allowed license/)
    l.items[id]!.signoffs.push(sig(3, 'Lee Rights', c.versions[1]!.content_hash, { date: AT, license: 'original', rights_hash: rightsHash(c.versions[1]!) }))
    expect(eligibility(c, l).eligible).toBe(true)
  })

  it('a rights check of a newer version, recorded before an older one, still binds to its own version', () => {
    let reg = confirmedHuman()
    const v1 = latest(reg.candidates[id]!)
    reg = intake(reg, [human({ source_url: 'https://example.org/s' })], 'v2.jsonl', AT, NOBANK).registry
    const c = reg.candidates[id]!
    const l = fullReview(reg, id)
    // A stale v1 rights check appended last (and dated later) does not displace the v2 check.
    l.items[id]!.signoffs.push(sig(3, 'Lee Rights', v1.content_hash, { date: '2026-12-31', license: 'original', rights_hash: rightsHash(v1) }))
    expect(eligibility(c, l).eligible).toBe(true)
    // And a v1 rights FAIL doesn't block v2, while a v2 fail does.
    l.items[id]!.signoffs.push(sig(3, 'Lee Rights', v1.content_hash, { result: 'fail', note: 'v1 source unproven', rights_hash: rightsHash(v1) }))
    expect(eligibility(c, l).eligible).toBe(true)
    l.items[id]!.signoffs.push(sig(3, 'Lee Rights', v1.content_hash, { result: 'fail', note: 'v2 source unproven', rights_hash: rightsHash(latest(c)) }))
    expect(eligibility(c, l).eligible).toBe(false)
  })
  it('intake and retire change neither the registry nor the items passed in', () => {
    const items = [imp(0)]
    const reg = reg0([imp(1)])
    const before = JSON.stringify(reg)
    const out = intake(reg, items, 'a.jsonl', AT, NOBANK).registry
    items[0]!.stem = 'mutated after intake'
    expect(out.candidates[id]!.versions[0]!.item.stem).toBe(QUESTIONS[0]!.stem)
    retire(reg, imp(1).import_id, 'Pat Lead', 'x', AT)
    expect(JSON.stringify(reg)).toBe(before)
  })

  it('retire refuses an already-retired item and an unknown duplicate_of', () => {
    const reg = reg0([imp(0), imp(1)])
    expect(() => retire(reg, id, 'Pat Lead', 'dup', AT, 'nope')).toThrow(/not another candidate/)
    expect(() => retire(reg, id, 'Pat Lead', 'dup', AT, id)).toThrow(/not another candidate/)
    expect(() => retire(retire(reg, id, 'Pat Lead', 'x', AT), id, 'Pat Lead', 'again', AT)).toThrow(/already retired/)
  })

  it('a question is owned by its live candidate, not a retired duplicate listed first', () => {
    let reg = reg0([imp(0)])
    reg = intake(reg, [{ ...imp(0), import_id: '100' }], 'b.jsonl', AT, NOBANK).registry
    expect(Object.keys(reg.candidates)[0]).toBe('100') // integer-like keys list first
    const rev = intake(reg, [imp(0, { teaching_explanation: 'Clearer.' })], 'c.jsonl', AT, NOBANK)
    expect(rev.result.revised).toEqual([id])
    const dup = intake(reg, [{ ...imp(0), import_id: 'wk-dup-3' }], 'd.jsonl', AT, NOBANK)
    expect(dup.result.retired).toEqual([{ import_id: 'wk-dup-3', duplicate_of: id }])
  })

  it('the same line with its keys in another order is unchanged, not a new version', () => {
    const reg = reg0([imp(0)])
    const reordered = Object.fromEntries(Object.entries(imp(0)).reverse()) as unknown as ImportedQuestion
    expect(intake(reg, [reordered], 'b.jsonl', AT, NOBANK).result.unchanged).toEqual([id])
    expect(intake(reg, [imp(0, { choices: imp(0).choices.map((c) => ({ text: c.text, key: c.key }) as typeof c) })], 'b.jsonl', AT, NOBANK).result.unchanged).toEqual([id])
  })


  it('identity comes from the registry: a registered reviewer under any name variant of the author is still the author', () => {
    // Registered people whose display name or alias is a variant of the author's name.
    const reviewers = testReviewers({
      [testId('Sam Solver')]: { aliases: ['Writer, Jo'] },
      [testId('Ana Solver')]: { display_name: 'JO  WRITER​' },
      [testId('Kim Fair')]: { display_name: 'Jo-Writer (author)' },
    })
    const reg = confirmedHuman()
    const e = QC.eligibility(reg.candidates[id]!, fullReview(reg, id), reviewers)
    expect(e.eligible).toBe(false)
    expect(e.problems).toContain('needs 2 more blind solve(s) by an authorized solver other than the author')
    // Accents too.
    const acc = QC.setTrack(reg0([human({ author: 'Jose Writer' })]), id, 'practice_candidate', testId('Pat Lead'), 'r', AT, NONE, R)
    expect(eligibility(acc.candidates[id]!, fullReview(acc, id, { 8: { by: 'José Writer' } })).eligible).toBe(false)
  })

  it('one reviewer is one solver, whatever names they sign under', () => {
    const reg = confirmedHuman()
    const c = reg.candidates[id]!
    const h = latest(c).content_hash
    const key = latest(c).item.accepted_answers[0]!
    const l = fullReview(reg, id)
    l.items[id]!.signoffs = l.items[id]!.signoffs.filter((s) => s.stage !== 4).concat(sig(4, 'Sam Solver', h, { answer: key }), { ...sig(4, 'Sam Solver', h, { answer: key }), by: 'Samuel S.' })
    expect(answerKeyFor(c, h, l).verified).toBe(false)
  })

  it('a display name is never a reason to refuse: registered reviewers named Claude Debussy or Ai Nguyen count', () => {
    const reg = QC.setTrack(reg0([human()]), id, 'practice_candidate', testId('Claude Debussy'), 'reserve later', AT, NONE, R)
    expect(reg.candidates[id]!.track_confirmed_by).toBe(testId('Claude Debussy'))
    const l = fullReview(reg, id, { 8: { by: 'Claude Debussy' } })
    l.items[id]!.signoffs = l.items[id]!.signoffs.map((s) => (s.stage === 4 && s.by === 'Ana Solver' ? { ...s, by: 'Ai Nguyen', reviewer_id: testId('Ai Nguyen') } : s))
    expect(eligibility(reg.candidates[id]!, l).eligible).toBe(true)
  })

  it('with the real (empty) registry nothing is eligible and no track can be confirmed: no appointment is assumed', () => {
    const reg = confirmedHuman()
    expect(QC.eligibility(reg.candidates[id]!, fullReview(reg, id)).eligible).toBe(false)
    expect(() => QC.setTrack(reg0([human()]), id, 'practice_candidate', testId('Pat Lead'), 'r', AT, NONE)).toThrow(/not an active content lead/)
  })

  it('a revoked content lead’s track confirmation stops counting', () => {
    const reg = confirmedHuman()
    const revoked = testReviewers({ [testId('Pat Lead')]: { revoked: { on: '2026-10-24', by: 'owner', reason: 'stepped down' } } })
    expect(QC.eligibility(reg.candidates[id]!, fullReview(reg, id, { 8: { by: 'Claude Debussy' } }), revoked).problems).toContain(`track confirmed by ${testId('Pat Lead')}, who is not an active content lead`)
  })
})

