import { describe, expect, it } from 'vitest'
import { IDENTITIES, identityProblems, resolveAuthors } from './authorIdentity'
import { testId, testIdentities, testReviewers } from './testReviewers'

const R = testReviewers()

describe('author identities (question_import/v2)', () => {
  it('the real registry is empty: no identity is recorded by this repository', () => {
    expect(IDENTITIES.identities).toEqual({})
    expect(identityProblems(IDENTITIES)).toEqual([])
  })

  it('a registry is refused when a link, an id or who recorded it is wrong', () => {
    expect(identityProblems(testIdentities(), R)).toEqual([])
    expect(identityProblems(testIdentities({ 'au-test-x': { reviewer_id: 'rv-nobody' } }), R).join(' ')).toMatch(/not in the reviewer registry/)
    expect(identityProblems(testIdentities({ 'au-test-x': { reviewer_id: testId('Pat Lead') } }), R).join(' ')).toMatch(/already linked/)
    expect(identityProblems(testIdentities({ 'au-test-x': { recorded_by: testId('Ana Solver') } }), R).join(' ')).toMatch(/recorded_by must be "owner" or an active content lead/)
    expect(identityProblems(testIdentities({ 'au-test-x': { recorded_by: testId('Pat Lead') } }), R)).toEqual([])
    expect(identityProblems(testIdentities({ 'BAD id': {} }), R).join(' ')).toMatch(/id must look like au-/)
  })

  it('resolves AI models and recorded people; a bare name or an unknown identity is unresolved; a broken registry resolves nobody', () => {
    const ok = resolveAuthors([{ name: 'ai:m1', identity: { kind: 'ai', model: 'm1' } }, { name: 'Jo Writer', identity: { kind: 'person', identity_id: 'au-test-jo-writer' } }], testIdentities(), R)
    expect(ok).toMatchObject({ resolved: true, reviewerIds: [testId('Jo Writer')] })
    expect(resolveAuthors([{ name: 'Jo Writer', identity: null }], testIdentities(), R)).toMatchObject({ resolved: false })
    expect(resolveAuthors([{ name: 'X', identity: { kind: 'person', identity_id: 'au-test-missing' } }], testIdentities(), R)).toMatchObject({ resolved: false })
    const broken = testIdentities({ 'au-test-x': { reviewer_id: 'rv-nobody' } })
    expect(resolveAuthors([{ name: 'Jo Writer', identity: { kind: 'person', identity_id: 'au-test-jo-writer' } }], broken, R).unresolved.join(' ')).toMatch(/identity registry has problems/)
  })
})
