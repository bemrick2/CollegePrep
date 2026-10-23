import { describe, expect, it } from 'vitest'
import { QUESTIONS } from './fixtures'
import { contentHash, REVIEW_RECORD } from './questionReview'
import { editorialState, type Ledger, type SignOff } from './editorialLedger'
import { REVIEWERS, registryProblems, type ReviewerRegistry } from './reviewerRegistry'
import { testId, testReviewers } from './testReviewers'

const q = QUESTIONS[0]!
const h = contentHash(q)
const key = q.accepted_answers[0]!
const R = testReviewers()
/** A sign-off by the TEST reviewer with this display name. */
const so = (stage: SignOff['stage'], by: string, extra: Partial<SignOff> = {}): SignOff => ({ stage, reviewer_id: testId(by), by, date: '2026-10-08', result: 'pass', hash: h, ...extra })
const full = (author = 'Dana Author'): Ledger => ({
  items: {
    [q.id]: {
      author,
      signoffs: [
        so(3, 'Lee Rights', { license: 'original' }),
        so(4, 'Sam Solver', { answer: key, seconds: 50 }),
        so(4, 'Ana Solver', { answer: key.toLowerCase(), seconds: 70 }),
        so(5, 'Sam Solver'),
        so(6, 'Kim Fair'),
        so(7, 'Ed Copy'),
        so(8, 'Pat Lead'),
      ],
    },
  },
})
const state = (l: Ledger, reviewers: ReviewerRegistry = R, extra = {}) => editorialState(q, l, { reviewers, ...extra })

describe('human editorial ledger (CONTENT_PLAN §5)', () => {
  it('today: the real reviewer registry is empty, no item is human-approved and every item enters at stage 3', () => {
    expect(Object.keys(REVIEWERS.reviewers)).toEqual([])
    expect(registryProblems(REVIEWERS)).toEqual([])
    for (const x of QUESTIONS) expect(editorialState(x)).toMatchObject({ passed: 2, next: 3, humanApproved: false })
    expect(REVIEW_RECORD.human_reviewed).toBe(false)
  })

  it('all stages by authorized reviewers, pinned to the current content, approve the item', () => {
    expect(state(full())).toEqual({ passed: 8, next: null, humanApproved: true, problems: [] })
  })

  it('a complete ledger approves nothing against the real (empty) registry: no appointment is assumed', () => {
    expect(state(full(), REVIEWERS)).toMatchObject({ humanApproved: false, next: 3 })
  })

  it('identity is the reviewer id, not the name: an unknown id, a revoked reviewer or the wrong role does not count', () => {
    const unknown = full()
    unknown.items[q.id]!.signoffs[6] = { ...so(8, 'Pat Lead'), reviewer_id: 'rv-nobody' }
    expect(state(unknown)).toMatchObject({ next: 8, humanApproved: false })
    expect(state(unknown).problems).toContain('stage 8: reviewer rv-nobody is not an active reviewer authorized for approver; it doesn’t count'.replace('’', "'"))
    const revoked = testReviewers({ [testId('Pat Lead')]: { revoked: { on: '2026-10-23', by: 'owner', reason: 'left' } } })
    expect(state(full(), revoked)).toMatchObject({ next: 8, humanApproved: false })
    const wrongRole = full()
    wrongRole.items[q.id]!.signoffs[0] = so(3, 'Ana Solver', { license: 'original' }) // a solver, not a rights checker
    expect(state(wrongRole)).toMatchObject({ next: 3, humanApproved: false })
    // A name alone, with no id, never counts, whatever it says.
    const nameOnly = full()
    nameOnly.items[q.id]!.signoffs[6] = { ...so(8, 'Pat Lead'), reviewer_id: '' }
    expect(state(nameOnly)).toMatchObject({ next: 8, humanApproved: false })
  })

  it('a display name is never a reason to refuse: a registered reviewer named Claude Debussy approves like anyone else', () => {
    const l = full()
    l.items[q.id]!.signoffs[6] = so(8, 'Claude Debussy')
    expect(state(l)).toMatchObject({ humanApproved: true })
  })

  it('a lead appointed by a revoked or non-lead appointer does not count', () => {
    const viaBad = testReviewers({ [testId('Pat Lead')]: { appointed_by: testId('Ana Solver') } })
    expect(registryProblems(viaBad).join(' ')).toMatch(/appointed_by must be "owner" or an active content lead/)
    expect(state(full(), viaBad)).toMatchObject({ next: 8, humanApproved: false })
  })

  it('an edit voids every earlier sign-off', () => {
    const l = full()
    for (const s of l.items[q.id]!.signoffs) s.hash = 'old'
    expect(state(l)).toMatchObject({ passed: 2, next: 3, humanApproved: false, problems: [expect.stringMatching(/earlier content/), 'needs a rights check'] })
  })

  it('blind solves: two different reviewer ids, neither the author, both matching the key', () => {
    expect(state(full('Sam Solver'))).toMatchObject({ passed: 3, next: 4, problems: ['needs 1 more blind solve(s) by an authorized solver other than the author'] })
    const twice = full()
    twice.items[q.id]!.signoffs[2] = { ...so(4, 'Sam Solver', { answer: key }), by: 'Samuel Solver' } // same id, another name
    expect(state(twice)).toMatchObject({ next: 4, humanApproved: false })
    const wrong = full()
    wrong.items[q.id]!.signoffs[2] = so(4, 'Ana Solver', { answer: 'not-the-key' })
    expect(state(wrong).problems).toEqual([`blind solve by ${testId('Ana Solver')} did not match the key`])
  })

  it('the author can’t solve, review fairness or approve, under any recorded name of theirs', () => {
    expect(state(full('Pat Lead'))).toMatchObject({ next: 8, humanApproved: false })
    // Author recorded as an alias of the registered reviewer, or as a variant of the display name.
    for (const author of ['J. Writer', 'writer, jo', 'JO  WRITER​']) {
      const l = full(author)
      l.items[q.id]!.signoffs[6] = so(8, 'Jo Writer')
      expect(state(l), author).toMatchObject({ next: 8, humanApproved: false })
    }
    const accent = full('Jose Writer')
    accent.items[q.id]!.signoffs[6] = so(8, 'José Writer')
    expect(state(accent)).toMatchObject({ next: 8, humanApproved: false })
  })

  it('rights check needs an allowed license', () => {
    const noLicense = full()
    noLicense.items[q.id]!.signoffs[0] = so(3, 'Lee Rights', { license: 'found online' })
    expect(state(noLicense)).toMatchObject({ next: 3, problems: ['rights check has no allowed license recorded'] })
  })

  it('a rights check binds to the exact rights version when one is given; a same-day re-check of the new version counts', () => {
    const l = full()
    l.items[q.id]!.signoffs[0] = so(3, 'Lee Rights', { license: 'original', rights_hash: 'rights-v1' })
    expect(state(l, R, { rightsHash: 'rights-v1' })).toMatchObject({ humanApproved: true })
    expect(state(l, R, { rightsHash: 'rights-v2' })).toMatchObject({ next: 3, humanApproved: false, problems: [expect.stringMatching(/earlier rights version/)] })
    l.items[q.id]!.signoffs.push(so(3, 'Lee Rights', { license: 'original', rights_hash: 'rights-v2', date: '2026-10-08' })) // same date
    expect(state(l, R, { rightsHash: 'rights-v2' })).toMatchObject({ humanApproved: true })
  })

  it('a failed stage blocks, even when recorded by someone not in the registry', () => {
    const l = full()
    l.items[q.id]!.signoffs.push(so(6, 'Kim Fair', { result: 'fail', note: 'context assumes a car' }))
    expect(state(l)).toMatchObject({ passed: 5, next: 6, problems: ['stage 6 failed: context assumes a car'] })
    const stranger = full()
    stranger.items[q.id]!.signoffs.push({ ...so(6, 'Kim Fair', { result: 'fail', note: 'flagged' }), reviewer_id: 'rv-unknown' })
    expect(state(stranger)).toMatchObject({ next: 6, humanApproved: false })
  })

  it('a sign-off whose date is not YYYY-MM-DD does not count', () => {
    const l = full()
    l.items[q.id]!.signoffs[6] = so(8, 'Pat Lead', { date: 'Oct 8 2026' })
    expect(state(l)).toMatchObject({ next: 8, humanApproved: false })
  })
})
