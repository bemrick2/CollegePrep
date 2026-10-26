import { describe, expect, it } from 'vitest'
import { QUESTIONS } from './data/demo/fixtures'
import { EDITORIAL_LEDGER, type Ledger } from './data/demo/editorialLedger'
import { REVIEWERS } from './data/demo/reviewerRegistry'
import { testId, testIdentities, testIdentityId, testReviewers } from './data/demo/testReviewers'
import { testOnlyBatch } from './__fixtures__/TEST_ONLY_importBatch'
import { csvRows, itemsFromBank, itemsFromRegistry, packetFiles, recordSignoffs, selectItems, SIGNOFF_COLUMNS, stateOf, type ReviewItem } from './editorialReview'
import * as QC from './questionCandidates'
import { emptyRegistry, intake, retire, rightsHash, setTrack, latest } from './questionCandidates'

const R = testReviewers()
const TI = testIdentities()
const AT = '2026-10-23'
const TODAY = '2026-10-23'
const EMPTY: Ledger = { items: {} }

/** A TEST-ONLY batch taken in (as if the app's bank were empty, since its lines are re-dressed bank items). */
function batch(n = 4) {
  return intake(emptyRegistry(), testOnlyBatch(n), 'TEST-ONLY-batch.jsonl', AT, new Map()).registry
}
const row = (item: ReviewItem, stage: number, who: string, extra: Record<string, string> = {}) => ({
  id: item.id,
  stage: String(stage),
  reviewer_id: testId(who),
  by: who,
  date: TODAY,
  result: 'pass',
  hash: item.content_hash,
  rights_hash: stage === 3 ? (item.rights_hash ?? '') : '',
  answer: stage === 4 ? item.question.accepted_answers[0]! : '',
  seconds: '',
  license: stage === 3 ? 'original' : '',
  note: '',
  ...extra,
})
const fullRows = (item: ReviewItem) => [row(item, 3, 'Lee Rights'), row(item, 4, 'Sam Solver'), row(item, 4, 'Ana Solver'), row(item, 5, 'Sam Solver'), row(item, 6, 'Kim Fair'), row(item, 7, 'Ed Copy'), row(item, 8, 'Pat Lead')]

describe('review items from an imported batch (labelled TEST-ONLY fixtures, not the real banks)', () => {
  it('takes the latest version of every candidate that isn’t retired, with its rights version and every author', () => {
    let reg = batch(3)
    const [a, b] = testOnlyBatch(3)
    reg = intake(reg, [{ ...a!, teaching_explanation: 'A clearer explanation.', author: 'Ed Editor' }], 'TEST-ONLY-rev.jsonl', AT, new Map()).registry
    reg = retire(reg, b!.import_id, testId('Pat Lead'), 'test', AT, undefined, R)
    const items = itemsFromRegistry(reg, TI, R)
    expect(items.map((i) => i.id)).toEqual([a!.import_id, testOnlyBatch(3)[2]!.import_id])
    const first = items[0]!
    expect(first).toMatchObject({ source: 'import', batch: 'TEST-ONLY-rev.jsonl', authors: ['Jo Writer', 'Ed Editor'], content_hash: latest(reg.candidates[a!.import_id]!).content_hash })
    expect(first.rights_hash).toBe(rightsHash(latest(reg.candidates[a!.import_id]!)))
    expect(first.question.teaching_explanation).toBe('A clearer explanation.')
  })

  it('selecting a batch: an unknown or empty id list is an error, never a fall-back to every item', () => {
    const items = itemsFromRegistry(batch(3), TI, R)
    expect(() => selectItems(items, ['test-only-nope'])).toThrow(/unknown or missing ids: test-only-nope/)
    expect(() => selectItems(items, [])).toThrow(/unknown or missing ids/)
    expect(selectItems(items, [items[1]!.id]).map((i) => i.id)).toEqual([items[1]!.id])
  })
})

describe('review packets for an imported batch', () => {
  const items = itemsFromRegistry(batch(4), TI, R)
  const files = packetFiles(items, EMPTY, R, 'Imported batch')

  it('blind packets carry no key, hints or explanations; review copies and templates carry the hashes', () => {
    const blind = Object.entries(files).filter(([n]) => n.startsWith('blind-')).map(([, t]) => t).join('\n')
    expect(blind).not.toBe('')
    for (const i of items) {
      expect(blind).toContain(i.content_hash)
      expect(blind).not.toContain(i.question.teaching_explanation)
      for (const h of i.question.hints) expect(blind).not.toContain(h)
    }
    expect(blind).not.toContain('(key)')
    const review = Object.entries(files).filter(([n]) => n.startsWith('review-')).map(([, t]) => t).join('\n')
    for (const i of items) expect(review).toContain(`rights ${i.rights_hash}`)
  })

  it('templates: two blind-solve rows per item, and stage-3 rows carrying the exact rights version', () => {
    const solves = csvRows(files['solves-template.csv']!)
    expect(solves).toHaveLength(items.length * 2)
    expect(solves.every((r) => r.stage === '4' && r.reviewer_id === '' && r.rights_hash === '')).toBe(true)
    const sign = csvRows(files['signoffs-template.csv']!)
    expect(Object.keys(sign[0]!)).toEqual([...SIGNOFF_COLUMNS])
    for (const i of items) expect(sign.find((r) => r.id === i.id && r.stage === '3')!.rights_hash).toBe(i.rights_hash)
    const status = csvRows(files['status.csv']!)
    expect(status.map((r) => [r.source, r.batch, r.next])).toEqual(items.map(() => ['import', 'TEST-ONLY-batch.jsonl', '3 Rights check']))
  })

  it('the app’s own bank still works the same way, without rights versions', () => {
    const bank = itemsFromBank(QUESTIONS, new Set(), EDITORIAL_LEDGER)
    expect(bank).toHaveLength(QUESTIONS.length)
    expect(bank.every((i) => i.source === 'bank' && i.rights_hash === undefined && i.authors[0] === 'AI (Claude)')).toBe(true)
  })
})

describe('recording sign-offs', () => {
  const reg = batch(2)
  const items = itemsFromRegistry(reg, TI, R)
  const it0 = items[0]!

  it('an imported item reviewed in full by authorized test reviewers becomes eligible, item by item', () => {
    const tracked = setTrack(reg, it0.id, it0.track, testId('Pat Lead'), 'test', AT, new Set(), R)
    const r = recordSignoffs(EMPTY, items, fullRows(it0), R, TODAY, 'sheet', TI)
    expect(r.refused).toEqual([])
    expect(r.added).toBe(7)
    expect(stateOf(it0, r.ledger, R).humanApproved).toBe(true)
    expect(QC.eligibility(tracked.candidates[it0.id]!, r.ledger, R, TI).eligible).toBe(true)
    // The other item in the batch was not reviewed and stays ineligible.
    expect(QC.eligibility(tracked.candidates[items[1]!.id]!, r.ledger, R, TI).eligible).toBe(false)
    expect(EMPTY.items).toEqual({}) // the input ledger is unchanged
  })

  it('with the real reviewer registry (empty) every row is refused: no appointment is assumed', () => {
    const r = recordSignoffs(EMPTY, items, fullRows(it0), REVIEWERS, TODAY, 'sheet', TI)
    expect(r.added).toBe(0)
    expect(r.refused).toHaveLength(7)
    expect(r.refused[0]).toMatch(/is not an active reviewer authorized for rights/)
  })

  it('refuses, never guesses: unknown item, bad stage, wrong role, author signing, stale hash or rights version, bad result or date', () => {
    const cases: [Record<string, string>, RegExp][] = [
      [{ ...row(it0, 3, 'Lee Rights'), id: 'test-only-missing' }, /unknown item/],
      [{ ...row(it0, 3, 'Lee Rights'), stage: '9' }, /bad stage/],
      [{ ...row(it0, 3, 'Lee Rights'), stage: '3.0' }, /bad stage/],
      [row(it0, 3, 'Ana Solver'), /not an active reviewer authorized for rights/],
      [row(it0, 8, 'Jo Writer'), /is an author of this item and can’t sign stage 8/],
      [row(it0, 4, 'Jo Writer'), /is an author of this item/],
      [{ ...row(it0, 4, 'Sam Solver'), hash: 'old' }, /is not the current content/],
      [{ ...row(it0, 3, 'Lee Rights'), rights_hash: 'old-rights' }, /is not the current rights version/],
      [{ ...row(it0, 3, 'Lee Rights'), rights_hash: '' }, /is not the current rights version/],
      [{ ...row(it0, 5, 'Sam Solver'), result: 'passed' }, /result must be "pass" or "fail"/],
      [{ ...row(it0, 5, 'Sam Solver'), result: 'failed' }, /result must be "pass" or "fail"/],
      [{ ...row(it0, 5, 'Sam Solver'), result: '' }, /result must be "pass" or "fail"/],
      [{ ...row(it0, 5, 'Sam Solver'), date: '10/23/2026' }, /must be YYYY-MM-DD/],
      [{ ...row(it0, 5, 'Sam Solver'), date: '2099-01-01' }, /not in the future/],
      [{ ...row(it0, 4, 'Sam Solver'), answer: '' }, /records the answer given/],
      [{ ...row(it0, 2, 'Lee Rights'), by: 'Someone' }, /author comes from the import/],
    ]
    for (const [r, why] of cases) {
      const out = recordSignoffs(EMPTY, items, [r], R, TODAY, 'sheet', TI)
      expect(out.added, String(why)).toBe(0)
      expect(out.refused.join(' '), String(why)).toMatch(why)
    }
  })

  it('an unfilled template row is skipped, not refused; "FAIL" in capitals is a fail', () => {
    const blank = { id: it0.id, stage: '4', reviewer_id: '', by: '', date: '', result: '', hash: it0.content_hash, rights_hash: '', answer: '', seconds: '', license: '', note: '' }
    expect(recordSignoffs(EMPTY, items, [blank], R, TODAY, 'sheet', TI)).toMatchObject({ added: 0, refused: [] })
    const out = recordSignoffs(EMPTY, items, [row(it0, 6, 'Kim Fair', { result: 'FAIL', note: 'stereotype' })], R, TODAY, 'sheet', TI)
    expect(out.ledger.items[it0.id]!.signoffs[0]!.result).toBe('fail')
  })
})

describe('recording sign-offs: a recorded fail is never erased (regression, #276 finding)', () => {
  const reg = batch(1)
  const items = itemsFromRegistry(reg, TI, R)
  const it0 = items[0]!
  const fails = (l: Ledger, stage: number) => l.items[it0.id]!.signoffs.filter((s) => s.stage === stage && s.result === 'fail')

  it('a later pass by the same reviewer does not remove their fail; the stage stays failed', () => {
    let l = recordSignoffs(EMPTY, items, fullRows(it0), R, TODAY, 'sheet', TI).ledger
    l = recordSignoffs(l, items, [row(it0, 6, 'Kim Fair', { result: 'fail', note: 'assumes a car' })], R, TODAY, 'sheet', TI).ledger
    l = recordSignoffs(l, items, [row(it0, 6, 'Kim Fair', { result: 'pass', note: 'changed my mind' })], R, TODAY, 'sheet', TI).ledger
    expect(fails(l, 6)).toHaveLength(1)
    expect(stateOf(it0, l, R)).toMatchObject({ humanApproved: false, next: 6, problems: expect.arrayContaining(['stage 6 failed: assumes a car']) })
  })

  it('another reviewer’s pass, under a name that canonically matches, does not remove the fail', () => {
    // Two different registered people whose names are the same words in another order.
    const reviewers = testReviewers({ [testId('Kim Fair')]: { display_name: 'Li Wang' }, [testId('Ed Copy')]: { display_name: 'Wang Li', roles: ['fairness', 'copyedit'] } })
    let l = recordSignoffs(EMPTY, items, fullRows(it0), reviewers, TODAY, 'sheet', TI).ledger
    l = recordSignoffs(l, items, [row(it0, 6, 'Kim Fair', { result: 'fail', note: 'flagged by Li Wang' })], reviewers, TODAY, 'sheet', TI).ledger
    l = recordSignoffs(l, items, [row(it0, 6, 'Ed Copy', { result: 'pass', by: 'Wang Li' })], reviewers, TODAY, 'sheet', TI).ledger
    expect(fails(l, 6)).toHaveLength(1)
    expect(stateOf(it0, l, reviewers).humanApproved).toBe(false)
  })

  it('a second fail is kept alongside the first; a newer pass replaces only the same reviewer’s earlier pass', () => {
    let l = recordSignoffs(EMPTY, items, [row(it0, 5, 'Sam Solver', { result: 'fail', note: 'two answers defensible' })], R, TODAY, 'sheet', TI).ledger
    l = recordSignoffs(l, items, [row(it0, 5, 'Sam Solver', { result: 'fail', note: 'still two answers' })], R, TODAY, 'sheet', TI).ledger
    expect(fails(l, 5)).toHaveLength(2)
    let p = recordSignoffs(EMPTY, items, [row(it0, 7, 'Ed Copy', { note: 'first' })], R, TODAY, 'sheet', TI).ledger
    p = recordSignoffs(p, items, [row(it0, 7, 'Ed Copy', { note: 'second' })], R, TODAY, 'sheet', TI).ledger
    expect(p.items[it0.id]!.signoffs.filter((s) => s.stage === 7).map((s) => s.note)).toEqual(['second'])
  })

  it('a fail on the current rights version blocks; one on an earlier rights version does not', () => {
    let reg2 = setTrack(reg, it0.id, it0.track, testId('Pat Lead'), 'test', AT, new Set(), R)
    let l = recordSignoffs(EMPTY, items, fullRows(it0), R, TODAY, 'sheet', TI).ledger
    l = recordSignoffs(l, items, [row(it0, 3, 'Lee Rights', { result: 'fail', note: 'v1 source unproven' })], R, TODAY, 'sheet', TI).ledger
    expect(QC.eligibility(reg2.candidates[it0.id]!, l, R, TI).eligible).toBe(false)
    // A new rights version (source added); its own rights check passes the same day.
    reg2 = intake(reg2, [{ ...testOnlyBatch(1)[0]!, source_url: 'https://example.org/original-draft' }], 'TEST-ONLY-rev.jsonl', AT, new Map()).registry
    const v2 = itemsFromRegistry(reg2, TI, R)[0]!
    expect(v2.rights_hash).not.toBe(it0.rights_hash)
    l = recordSignoffs(l, [v2], [row(v2, 3, 'Lee Rights')], R, TODAY, 'sheet', TI).ledger
    expect(QC.eligibility(reg2.candidates[it0.id]!, l, R, TI).eligible).toBe(true)
    expect(fails(l, 3)).toHaveLength(1) // the old fail is still on record
  })
})

describe('recording sign-offs: review findings', () => {
  const reg = batch(1)
  const items = itemsFromRegistry(reg, TI, R)
  const it0 = items[0]!

  it('a fail is recorded from anyone (it can only block), including an author’s own fairness fail', () => {
    const stranger = recordSignoffs(EMPTY, items, [{ ...row(it0, 6, 'Kim Fair', { result: 'fail', note: 'flag' }), reviewer_id: 'rv-unknown' }], R, TODAY, 'sheet', TI)
    expect(stranger).toMatchObject({ added: 1, refused: [] })
    const own = recordSignoffs(EMPTY, items, [row(it0, 6, 'Jo Writer', { result: 'fail', note: 'my own concern' })], R, TODAY, 'sheet', TI)
    expect(own).toMatchObject({ added: 1, refused: [] })
    expect(stateOf(it0, own.ledger, R)).toMatchObject({ humanApproved: false })
    // A fail still has to name the current content.
    expect(recordSignoffs(EMPTY, items, [row(it0, 6, 'Kim Fair', { result: 'fail', hash: 'old' })], R, TODAY, 'sheet', TI).refused.join(' ')).toMatch(/not the current content/)
  })

  it('a partly filled row is refused, not skipped; seconds must be a whole number', () => {
    const partial = { id: it0.id, stage: '5', reviewer_id: '', by: '', date: '', result: '', hash: it0.content_hash, rights_hash: '', answer: '', seconds: '', license: '', note: 'looks fine' }
    expect(recordSignoffs(EMPTY, items, [partial], R, TODAY, 'sheet', TI).refused.join(' ')).toMatch(/result must be "pass" or "fail"/)
    expect(recordSignoffs(EMPTY, items, [row(it0, 4, 'Sam Solver', { seconds: 'abc' })], R, TODAY, 'sheet', TI).refused.join(' ')).toMatch(/seconds must be a whole number/)
  })

  it('nothing is recorded against a registry with problems', () => {
    const twin = testReviewers({ [testId('Ana Solver')]: { display_name: 'Sam Solver' } })
    const r = recordSignoffs(EMPTY, items, fullRows(it0), twin, TODAY, 'sheet', TI)
    expect(r.added).toBe(0)
    expect(r.refused[0]).toMatch(/reviewer registry has problems/)
  })
})

describe('recording authorship for the app’s bank (stage 2)', () => {
  const bank = itemsFromBank(QUESTIONS.slice(0, 1), new Set(), EMPTY, TI, R)
  const b0 = bank[0]!
  /** A stage-2 row by `who` recording the author by identity: a TEST "au-…" id or "ai:<model>". */
  const author = (who: string, identity: string, extra: Record<string, string> = {}) => ({ ...row(b0, 2, who), author_identity: identity, ...extra })
  const rec = (l: Ledger, rows: Record<string, string>[]) => recordSignoffs(l, itemsFromBank(QUESTIONS.slice(0, 1), new Set(), l, TI, R), rows, R, TODAY, 'sheet', TI)

  it('needs an active content lead who isn’t an author, the current hash, and a recorded identity (never a bare name)', () => {
    const jo = testIdentityId('Jo Writer')
    expect(rec(EMPTY, [author('Ana Solver', jo)]).refused.join(' ')).toMatch(/not an active content lead/)
    expect(rec(EMPTY, [{ ...author('Pat Lead', jo), hash: 'old' }]).refused.join(' ')).toMatch(/not the current content/)
    expect(rec(EMPTY, [author('Pat Lead', 'Jo Writer')]).refused.join(' ')).toMatch(/a name alone isn’t an identity/)
    expect(rec(EMPTY, [author('Pat Lead', 'au-test-nobody')]).refused.join(' ')).toMatch(/is not a recorded identity/)
    expect(recordSignoffs(EMPTY, bank, [author('Pat Lead', jo)], R, TODAY, 'sheet').refused.join(' ')).toMatch(/is not a recorded identity/) // the real identities.json is empty
    expect(rec(EMPTY, [author('Pat Lead', 'ai:')]).refused.join(' ')).toMatch(/names its model/)
    const ok = rec(EMPTY, [author('Pat Lead', jo)])
    expect(ok).toMatchObject({ added: 1, refused: [] })
    // Recorded under the identity id, never the display name.
    expect(ok.ledger.items[b0.id]).toMatchObject({ author: jo, authors: ['AI (Claude)', jo], author_records: [{ name: jo, identity: { kind: 'person', identity_id: jo } }] })
    // A content lead who is an author can't record the item's authorship (here: linked by id).
    expect(rec(ok.ledger, [author('Jo Writer', testIdentityId('Someone Else'))]).refused.join(' ')).toMatch(/is an author of this item and can’t record its authorship/)
    // An AI author is recorded explicitly.
    expect(rec(EMPTY, [author('Pat Lead', 'ai:claude-opus')]).ledger.items[b0.id]).toMatchObject({ author: 'ai:claude-opus', author_records: [{ identity: { kind: 'ai', model: 'claude-opus' } }] })
  })

  it('authors are append-only: renaming the author never lets the earlier one approve, even in the same run', () => {
    const rows = [author('Pat Lead', testIdentityId('Jo Writer')), author('Claude Debussy', testIdentityId('Someone Else')), row(b0, 8, 'Jo Writer')]
    const r = rec(EMPTY, rows)
    expect(r.ledger.items[b0.id]!.authors).toEqual(['AI (Claude)', testIdentityId('Jo Writer'), testIdentityId('Someone Else')])
    expect(r.refused.join(' ')).toMatch(/is an author of this item and can’t sign stage 8/)
    expect(rec(r.ledger, [row(b0, 8, 'Jo Writer')]).refused.join(' ')).toMatch(/is an author/)
  })

  it('a bank item whose human author has no recorded identity is never approved', () => {
    // A legacy ledger entry: a human name with no identity record (as stage 2 recorded it before import contract v2).
    const legacy: Ledger = { items: { [b0.id]: { author: 'Jo Writer', authors: ['AI (Claude)', 'Jo Writer'], signoffs: [] } } }
    const item = itemsFromBank(QUESTIONS.slice(0, 1), new Set(), legacy, TI, R)[0]!
    expect(item.authorship.resolved).toBe(false)
    const done = rec(legacy, fullRows(item)).ledger
    expect(stateOf(item, done, R)).toMatchObject({ humanApproved: false, next: 2 })
  })

  // #290 review: identities decide, by id; display names never do.
  const recWith = (ids: ReturnType<typeof testIdentities>, l: Ledger, rows: Record<string, string>[]) =>
    recordSignoffs(l, itemsFromBank(QUESTIONS.slice(0, 1), new Set(), l, ids, R), rows, R, TODAY, 'sheet', ids)
  /** Jordan Smith writes; the same person reviews as "Pat Lead" (no alias): only the identity link connects them. */
  const jordanIsPat = () => {
    const ids = testIdentities({ 'au-test-jordan': { display_name: 'Jordan Smith', reviewer_id: testId('Pat Lead') } })
    delete ids.identities[testIdentityId('Pat Lead')]
    return ids
  }

  it('the recorder refuses a linked reviewer under a different name, at stages 4, 6 and 8 (bank and import)', () => {
    // Bank: Pat (the lead) records Jordan, who is linked to Kim's reviewer id; Kim's fairness pass is refused.
    const ids = testIdentities({ 'au-test-jordan': { display_name: 'Jordan Smith', reviewer_id: testId('Kim Fair') } })
    delete ids.identities[testIdentityId('Kim Fair')]
    const authored = recWith(ids, EMPTY, [author('Pat Lead', 'au-test-jordan')])
    expect(authored.refused).toEqual([])
    expect(recWith(ids, authored.ledger, [row(b0, 6, 'Kim Fair')]).refused.join(' ')).toMatch(/is an author of this item and can’t sign stage 6/)
    // In the same run as the stage-2 row, too.
    expect(recWith(ids, EMPTY, [author('Pat Lead', 'au-test-jordan'), row(b0, 6, 'Kim Fair')]).refused.join(' ')).toMatch(/can’t sign stage 6/)
    // And when the item already carries the link, whatever ledger the rows are recorded into.
    const linkedItems = itemsFromBank(QUESTIONS.slice(0, 1), new Set(), authored.ledger, ids, R)
    expect(recordSignoffs(EMPTY, linkedItems, [row(linkedItems[0]!, 6, 'Kim Fair')], R, TODAY, 'sheet', ids).refused.join(' ')).toMatch(/can’t sign stage 6/)
    // Import: the import's own identity links Sam Solver; Sam's blind solve is refused.
    const sam = testIdentities({ 'au-test-jordan': { display_name: 'Jordan Smith', reviewer_id: testId('Sam Solver') } })
    delete sam.identities[testIdentityId('Sam Solver')]
    const line = { ...testOnlyBatch(1)[0]!, contract: 'question_import/v2' as const, origin: 'human_original' as const, author: 'Jordan Smith', author_identity: { kind: 'person' as const, identity_id: 'au-test-jordan' } }
    const reg = intake(emptyRegistry(), [line], 'TEST-ONLY-batch.jsonl', AT, new Map()).registry
    const items = itemsFromRegistry(reg, sam, R)
    expect(items[0]!.authorship.reviewerIds).toEqual([testId('Sam Solver')])
    expect(recordSignoffs(EMPTY, items, [row(items[0]!, 4, 'Sam Solver')], R, TODAY, 'sheet', sam).refused.join(' ')).toMatch(/is an author of this item and can’t sign stage 4/)
    expect(recordSignoffs(EMPTY, items, [row(items[0]!, 4, 'Ana Solver')], R, TODAY, 'sheet', sam).refused).toEqual([])
  })

  it('a content lead can’t record their own identity as the author, by link or by name', () => {
    expect(recWith(jordanIsPat(), EMPTY, [author('Pat Lead', 'au-test-jordan')]).refused.join(' ')).toMatch(/can’t record its authorship/)
    // A different person also named "Pat Lead" (recorded as such): the name still blocks Pat, fail-closed.
    const twin = testIdentities({ 'au-test-pat-two': { display_name: 'Pat Lead', distinct_from: [testId('Pat Lead')] } })
    expect(recWith(twin, EMPTY, [author('Pat Lead', 'au-test-pat-two')]).refused.join(' ')).toMatch(/can’t record its authorship/)
  })

  it('two recorded authors with the same display name keep both identities: the linked reviewer stays excluded', () => {
    const ids = testIdentities({
      'au-test-other': { display_name: 'Sam Lee', distinct_from: [testId('Sam Solver')] },
      [testIdentityId('Sam Solver')]: { display_name: 'Sam Lee', aliases: ['Sam Solver'] },
    })
    const r = recWith(ids, EMPTY, [author('Pat Lead', 'au-test-other'), author('Pat Lead', testIdentityId('Sam Solver'))])
    expect(r.refused).toEqual([])
    expect(recWith(ids, r.ledger, [row(b0, 4, 'Sam Solver')]).refused.join(' ')).toMatch(/is an author of this item and can’t sign stage 4/)
  })

  it('a legacy name stays unresolved even when a recorded identity has the same display name; a mislabelled AI record is unresolved', () => {
    const legacy: Ledger = { items: { [b0.id]: { author: 'Jo Writer', authors: ['AI (Claude)', 'Jo Writer'], signoffs: [] } } }
    const r = rec(legacy, [author('Pat Lead', testIdentityId('Jo Writer'))]) // Jo's identity: display name "Jo Writer"
    expect(r.refused).toEqual([])
    const item = itemsFromBank(QUESTIONS.slice(0, 1), new Set(), r.ledger, TI, R)[0]!
    expect(item.authorship).toMatchObject({ resolved: false, unresolved: [expect.stringMatching(/"Jo Writer" is a name only/)] })
    // A hand-edited AI record must be named "ai:<model>".
    const hand: Ledger = { items: { [b0.id]: { author: 'Jordan Smith', authors: ['AI (Claude)', 'Jordan Smith'], author_records: [{ name: 'Jordan Smith', identity: { kind: 'ai', model: 'claude' } }], signoffs: [] } } }
    expect(itemsFromBank(QUESTIONS.slice(0, 1), new Set(), hand, TI, R)[0]!.authorship.resolved).toBe(false)
    const mismatched: Ledger = { items: { [b0.id]: { author: 'ai:claude', authors: ['ai:claude'], author_records: [{ name: 'ai:claude', identity: { kind: 'person', identity_id: testIdentityId('Jo Writer') } }], signoffs: [] } } }
    expect(itemsFromBank(QUESTIONS.slice(0, 1), new Set(), mismatched, TI, R)[0]!.authorship.resolved).toBe(false)
  })
})


