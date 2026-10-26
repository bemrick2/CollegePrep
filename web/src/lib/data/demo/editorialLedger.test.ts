import { describe, expect, it } from 'vitest'
import { QUESTIONS } from './fixtures'
import { contentHash, REVIEW_RECORD } from './questionReview'
import { editorialState, type Ledger, type SignOff } from './editorialLedger'
import { authorized, REVIEWERS, registryProblems, type ReviewerRegistry } from './reviewerRegistry'
import { testId, testIdentities, testIdentityId, testReviewers } from './testReviewers'
import { IDENTITIES } from './authorIdentity'

const q = QUESTIONS[0]!
const h = contentHash(q)
const key = q.accepted_answers[0]!
const R = testReviewers()
/** A sign-off by the TEST reviewer with this display name. */
const so = (stage: SignOff['stage'], by: string, extra: Partial<SignOff> = {}): SignOff => ({ stage, reviewer_id: testId(by), by, date: '2026-10-08', result: 'pass', hash: h, ...extra })
const TI = testIdentities()
/** A complete review; the author is recorded with a TEST identity (by default the one for that name). */
const full = (author = 'Dana Author', identityId = testIdentityId(author)): Ledger => ({
  items: {
    [q.id]: {
      author,
      author_records: [{ name: author, identity: { kind: 'person', identity_id: identityId } }],
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
const state = (l: Ledger, reviewers: ReviewerRegistry = R, extra = {}) => editorialState(q, l, { reviewers, identities: TI, ...extra })

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
    expect(registryProblems(viaBad).join(' ')).toMatch(/appointed_by must lead to "owner" through content leads/)
    // A registry with any problem counts no sign-off at all, so the item doesn't get past stage 3.
    expect(state(full(), viaBad)).toMatchObject({ next: 3, humanApproved: false, problems: expect.arrayContaining([expect.stringMatching(/reviewer registry has problems/)]) })
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
    // Each author has a recorded identity NOT linked to Jo's reviewer id, so only the (fail-closed) name match blocks.
    for (const author of ['J. Writer', 'writer, jo', 'JO  WRITER\u200b', 'Jose Writer']) {
      const l = full(author, 'au-test-variant')
      l.items[q.id]!.signoffs[6] = so(8, author === 'Jose Writer' ? 'José Writer' : 'Jo Writer')
      expect(editorialState(q, l, { reviewers: R, identities: testIdentities({ 'au-test-variant': { display_name: author } }) }), author).toMatchObject({ next: 8, humanApproved: false })
    }
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

  it('appointments must reach the owner through active leads: a loop or a revoked link anywhere above counts nothing', () => {
    // A loop: two entries appoint each other, no owner anywhere.
    const loop = testReviewers({ [testId('Pat Lead')]: { appointed_by: testId('Claude Debussy') }, [testId('Claude Debussy')]: { appointed_by: testId('Pat Lead') } })
    expect(registryProblems(loop).join(' ')).toMatch(/lead to "owner" through content leads, with no loop/)
    expect(state(full(), loop)).toMatchObject({ humanApproved: false, problems: expect.arrayContaining([expect.stringMatching(/reviewer registry has problems/)]) })
    // A broken chain: owner → Claude Debussy (lead) → Dana Author (lead) → Pat Lead (approver); then Claude is revoked.
    const chain = testReviewers({ [testId('Dana Author')]: { appointed_by: testId('Claude Debussy') }, [testId('Pat Lead')]: { appointed_by: testId('Dana Author') } })
    expect(registryProblems(chain)).toEqual([])
    expect(state(full(), chain)).toMatchObject({ humanApproved: true })
    const broken = testReviewers({ [testId('Claude Debussy')]: { revoked: { on: '2026-10-24', by: 'owner', reason: 'left' } }, [testId('Dana Author')]: { appointed_by: testId('Claude Debussy') }, [testId('Pat Lead')]: { appointed_by: testId('Dana Author') } })
    // A revocation isn't a fault in the file: only those below the revoked lead stop counting; everyone else carries on.
    expect(registryProblems(broken)).toEqual([])
    expect(state(full(), broken)).toMatchObject({ humanApproved: false, next: 8 })
    const l = full()
    l.items[q.id]!.signoffs[6] = so(8, 'Claude Debussy') // appointed by the owner directly
    const brokenButClaudeActive = testReviewers({ [testId('Kim Fair')]: { revoked: { on: '2026-10-24', by: 'owner', reason: 'left' }, roles: ['fairness', 'content_lead'] }, [testId('Dana Author')]: { appointed_by: testId('Kim Fair') }, [testId('Pat Lead')]: { appointed_by: testId('Dana Author') } })
    l.items[q.id]!.signoffs[4] = so(6, 'Ana Solver')
    expect(registryProblems(brokenButClaudeActive)).toEqual([])
    expect(state(l, testReviewers({ [testId('Ana Solver')]: { roles: ['solver', 'fairness'] }, [testId('Dana Author')]: { appointed_by: testId('Kim Fair') }, [testId('Kim Fair')]: { revoked: { on: '2026-10-24', by: 'owner', reason: 'left' }, roles: ['fairness', 'content_lead'] } }))).toMatchObject({ humanApproved: true })
  })

  it('one person, one id: two entries sharing a name or alias make the registry unusable; two solves by one person count once', () => {
    const twin = testReviewers({ [testId('Ana Solver')]: { display_name: 'Sam Solver' } })
    expect(registryProblems(twin).join(' ')).toMatch(/shares a recorded name/)
    expect(state(full(), twin)).toMatchObject({ humanApproved: false })
    const alias = testReviewers({ [testId('Ana Solver')]: { aliases: ['S. Solver'] }, [testId('Sam Solver')]: { aliases: ['s solver'] } })
    expect(registryProblems(alias).join(' ')).toMatch(/shares a recorded name/)
    // Different real people are never merged by word order, and two people with one name are declared, not renamed.
    expect(registryProblems(testReviewers({ [testId('Kim Fair')]: { display_name: 'Li Wang' }, [testId('Ed Copy')]: { display_name: 'Wang Li' } }))).toEqual([])
    const sameName = testReviewers({ [testId('Ana Solver')]: { display_name: 'Maria Garcia' }, [testId('Sam Solver')]: { display_name: 'Maria Garcia' } })
    expect(registryProblems(sameName).join(' ')).toMatch(/shares a recorded name/)
    const declared = testReviewers({
      [testId('Ana Solver')]: { display_name: 'Maria Garcia', distinct_from: [testId('Sam Solver')] },
      [testId('Sam Solver')]: { display_name: 'Maria Garcia', distinct_from: [testId('Ana Solver')] },
    })
    expect(registryProblems(declared)).toEqual([])
    expect(state(full(), declared)).toMatchObject({ humanApproved: true })
  })

  it('a recorded fail blocks whatever its date, and a pass dated in the future doesn’t count', () => {
    const badDate = full()
    badDate.items[q.id]!.signoffs.push(so(6, 'Kim Fair', { result: 'fail', date: '2026-10-32', note: 'bad date fail' }))
    expect(state(badDate)).toMatchObject({ humanApproved: false, next: 6, problems: expect.arrayContaining(['stage 6 failed: bad date fail']) })
    const future = full()
    future.items[q.id]!.signoffs[6] = so(8, 'Pat Lead', { date: '2099-12-31' })
    expect(state(future, R, { today: '2026-10-23' })).toMatchObject({ humanApproved: false, next: 8 })
    expect(state(future, R, { today: '2099-12-31' })).toMatchObject({ humanApproved: true })
  })

  it('a stage-3 fail with no rights version recorded blocks; one for a different rights version does not', () => {
    const l = full()
    l.items[q.id]!.signoffs[0] = so(3, 'Lee Rights', { license: 'original', rights_hash: 'r2' })
    l.items[q.id]!.signoffs.push(so(3, 'Lee Rights', { result: 'fail', note: 'no source on file' })) // no rights_hash
    expect(state(l, R, { rightsHash: 'r2' })).toMatchObject({ humanApproved: false, next: 3 })
    const other = full()
    other.items[q.id]!.signoffs[0] = so(3, 'Lee Rights', { license: 'original', rights_hash: 'r2' })
    other.items[q.id]!.signoffs.push(so(3, 'Lee Rights', { result: 'fail', note: 'v1 claim', rights_hash: 'r1' }))
    expect(state(other, R, { rightsHash: 'r2' })).toMatchObject({ humanApproved: true })
  })

  it('every author ever recorded stays excluded: replacing the author does not let the earlier one approve', () => {
    const l = full('Someone Else')
    l.items[q.id]!.authors = ['Pat Lead', 'Someone Else']
    l.items[q.id]!.author_records!.push({ name: 'Pat Lead', identity: { kind: 'person', identity_id: testIdentityId('Pat Lead') } })
    const r = state(l)
    expect(r).toMatchObject({ next: 8, humanApproved: false })
    expect(r.problems).toContain('needs approval by an authorized approver who is not the author')
  })

  it('authorized() alone refuses anyone below a revoked link or inside a loop', () => {
    const broken = testReviewers({ [testId('Claude Debussy')]: { revoked: { on: '2026-10-24', by: 'owner', reason: 'left' } }, [testId('Dana Author')]: { appointed_by: testId('Claude Debussy') }, [testId('Pat Lead')]: { appointed_by: testId('Dana Author') } })
    expect(authorized(broken, testId('Pat Lead'), 'approver')).toBeNull()
    const loop = testReviewers({ [testId('Pat Lead')]: { appointed_by: testId('Claude Debussy') }, [testId('Claude Debussy')]: { appointed_by: testId('Pat Lead') } })
    expect(authorized(loop, testId('Pat Lead'), 'approver')).toBeNull()
    const ok = testReviewers({ [testId('Dana Author')]: { appointed_by: testId('Claude Debussy') }, [testId('Pat Lead')]: { appointed_by: testId('Dana Author') } })
    expect(authorized(ok, testId('Pat Lead'), 'approver')?.id).toBe(testId('Pat Lead'))
  })

  it('a revoked person can be re-appointed under a new id without making the registry unusable', () => {
    const rehired = testReviewers({ [testId('Ana Solver')]: { revoked: { on: '2026-10-20', by: 'owner', reason: 'left' } } })
    rehired.reviewers['rv-test-ana-solver-2'] = { id: 'rv-test-ana-solver-2', display_name: 'Ana Solver', aliases: [], roles: ['solver'], appointed_by: 'owner', appointed_on: '2026-10-23' }
    expect(registryProblems(rehired)).toEqual([])
    const l = full()
    l.items[q.id]!.signoffs[2] = { ...so(4, 'Ana Solver', { answer: key }), reviewer_id: 'rv-test-ana-solver-2' }
    expect(state(l, rehired)).toMatchObject({ humanApproved: true })
  })

  it('author identity: an author who is also a reviewer is excluded by id, whatever name either is recorded under', () => {
    // "Jordan Smith" writes; the same person reviews as "Pat Lead" with no alias. Only the identity link catches it.
    const l = full('Jordan Smith', 'au-test-jordan')
    const ids = testIdentities({ 'au-test-jordan': { display_name: 'Jordan Smith', reviewer_id: testId('Pat Lead') } })
    ids.identities[testIdentityId('Pat Lead')]!.reviewer_id = undefined // one reviewer, one identity
    expect(editorialState(q, l, { reviewers: R, identities: ids })).toMatchObject({ next: 8, humanApproved: false })
    // Without the link the names don't match, and the approval counts.
    expect(editorialState(q, l, { reviewers: R, identities: testIdentities({ 'au-test-jordan': { display_name: 'Jordan Smith' } }) })).toMatchObject({ humanApproved: true })
  })

  it('a human author known only by name (legacy) is unresolved: never approved, even with every stage passed', () => {
    const legacy = full()
    delete legacy.items[q.id]!.author_records
    expect(state(legacy)).toMatchObject({ passed: 8, next: 2, humanApproved: false, problems: expect.arrayContaining([expect.stringMatching(/a name only, with no recorded identity/)]) })
    // An identity that isn't in the registry is unresolved too; with the real (empty) registry, nothing resolves.
    expect(state(full('Dana Author', 'au-test-missing'))).toMatchObject({ next: 2, humanApproved: false })
    expect(editorialState(q, full(), { reviewers: R, identities: IDENTITIES })).toMatchObject({ next: 2, humanApproved: false })
    // The app bank's recorded AI drafting is explicit AI authorship: resolved.
    const ai = full()
    ai.items[q.id]!.author = 'AI (Claude)'
    delete ai.items[q.id]!.author_records
    expect(state(ai)).toMatchObject({ humanApproved: true })
  })
})

