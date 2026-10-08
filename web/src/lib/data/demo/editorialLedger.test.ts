import { describe, expect, it } from 'vitest'
import { QUESTIONS } from './fixtures'
import { contentHash, REVIEW_RECORD } from './questionReview'
import { editorialState, type Ledger, type SignOff } from './editorialLedger'

const q = QUESTIONS[0]!
const h = contentHash(q)
const key = q.accepted_answers[0]!
const so = (stage: SignOff['stage'], by: string, extra: Partial<SignOff> = {}): SignOff => ({ stage, by, date: '2026-10-08', result: 'pass', hash: h, ...extra })
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

describe('human editorial ledger (CONTENT_PLAN §5)', () => {
  it('today: no item is human-approved and every item enters at stage 3 (the AI-reviewed bank is not grandfathered)', () => {
    for (const x of QUESTIONS) expect(editorialState(x)).toMatchObject({ passed: 2, next: 3, humanApproved: false })
    expect(REVIEW_RECORD.human_reviewed).toBe(false)
  })

  it('all stages by named people, pinned to the current content, approve the item', () => {
    expect(editorialState(q, full())).toEqual({ passed: 8, next: null, humanApproved: true, problems: [] })
  })

  it('an edit voids every earlier sign-off', () => {
    const l = full()
    for (const s of l.items[q.id]!.signoffs) s.hash = 'old'
    expect(editorialState(q, l)).toMatchObject({ passed: 2, next: 3, humanApproved: false, problems: [expect.stringMatching(/earlier content/), 'needs a rights check'] })
  })

  it('blind solves: two different people, neither the author, both matching the key', () => {
    const l = full('Sam Solver')
    expect(editorialState(q, l)).toMatchObject({ passed: 3, next: 4, problems: ['needs 1 more blind solve(s) by someone other than the author'] })
    const wrong = full()
    wrong.items[q.id]!.signoffs[2] = so(4, 'Ana Solver', { answer: 'not-the-key' })
    expect(editorialState(q, wrong).problems).toEqual(['blind solve by Ana Solver did not match the key'])
  })

  it('rights check needs an allowed license; approver and fairness reviewer cannot be the author; AI is not a reviewer', () => {
    const noLicense = full()
    noLicense.items[q.id]!.signoffs[0] = so(3, 'Lee Rights', { license: 'found online' })
    expect(editorialState(q, noLicense)).toMatchObject({ next: 3, problems: ['rights check has no allowed license recorded'] })
    const selfApproved = full('Pat Lead')
    expect(editorialState(q, selfApproved)).toMatchObject({ next: 8, humanApproved: false })
    const ai = full()
    ai.items[q.id]!.signoffs[6] = so(8, 'Claude')
    expect(editorialState(q, ai)).toMatchObject({ next: 8, problems: ['stage 8: "Claude" is not a named person', expect.stringMatching(/needs approval/)] })
  })

  it('a failed stage stops the item there with the reviewer’s note', () => {
    const l = full()
    l.items[q.id]!.signoffs.push(so(6, 'Kim Fair', { result: 'fail', note: 'context assumes a ski trip' }))
    expect(editorialState(q, l)).toMatchObject({ passed: 5, next: 6, problems: ['stage 6 failed: context assumes a ski trip'] })
  })
})
