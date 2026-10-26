import { describe, expect, it } from 'vitest'
import { IDENTITIES, identityOf, identityProblems, resolveAuthors } from './authorIdentity'
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

  it('(#290 review) built-in keys are never identities, and resolving one never throws', () => {
    for (const k of ['constructor', 'toString', '__proto__', 'hasOwnProperty']) {
      expect(identityOf(IDENTITIES, k)).toBeUndefined()
      expect(resolveAuthors([{ name: 'X', identity: { kind: 'person', identity_id: k } }], IDENTITIES, R)).toMatchObject({ resolved: false })
    }
  })

  it('(#290 review) a registry of the wrong contract is refused; an AI author must name its model', () => {
    expect(identityProblems({ contract: 'something/v9', identities: {} } as never, R).join(' ')).toMatch(/not an author_identity_registry\/v1 file/)
    expect(resolveAuthors([{ name: 'ai:', identity: { kind: 'ai', model: '' } }], testIdentities(), R).unresolved.join(' ')).toMatch(/must name its model/)
    expect(resolveAuthors([{ name: 'ai:m 1', identity: { kind: 'ai', model: 'm 1' } }], testIdentities(), R)).toMatchObject({ resolved: false })
  })

  it('(#290 review) a person may not be recorded under the bank\'s AI drafting name', () => {
    expect(identityProblems(testIdentities({ 'au-test-x': { display_name: 'AI (Claude)' } }), R).join(' ')).toMatch(/AI drafting name/)
    expect(identityProblems(testIdentities({ 'au-test-x': { display_name: 'Someone', aliases: ['ai (claude)'] } }), R).join(' ')).toMatch(/AI drafting name/)
  })

  it('(#290 review) a reviewer whose names match an identity must be the one linked to it, or recorded as a different person', () => {
    // Jo's identity linked to Pat by mistake: Jo, reviewing under Jo's own name, matches but isn't linked.
    const wrong = testIdentities({ 'au-test-jo-writer': { reviewer_id: testId('Pat Lead') } })
    delete wrong.identities['au-test-pat-lead']
    expect(identityProblems(wrong, R).join(' ')).toMatch(new RegExp(`reviewer ${testId('Jo Writer')} has a name matching this identity`))
    // Two different people named alike: recorded as such, no problem.
    const twin = testIdentities({ 'au-test-jo-two': { display_name: 'Jo Writer', distinct_from: [testId('Jo Writer')] } })
    expect(identityProblems(twin, R)).toEqual([])
    expect(identityProblems(testIdentities({ 'au-test-jo-two': { display_name: 'Jo Writer' } }), R).join(' ')).toMatch(/has a name matching this identity/)
  })

  it('(#290 confirm) alias-only matches, distinct_from entries and built-in reviewer ids are checked, without throwing', () => {
    // Jo's identity carries an alias of Ana's; Ana isn't linked to it.
    expect(identityProblems(testIdentities({ 'au-test-x': { display_name: 'Someone', aliases: ['Ana Solver'] } }), R).join(' ')).toMatch(new RegExp(`reviewer ${testId('Ana Solver')} has a name matching`))
    expect(identityProblems(testIdentities({ 'au-test-x': { distinct_from: 'rv-test-jo-writer' as never } }), R).join(' ')).toMatch(/distinct_from must be a list/)
    expect(identityProblems(testIdentities({ 'au-test-x': { distinct_from: ['rv-nobody', 42 as never] } }), R).join(' ')).toMatch(/distinct_from rv-nobody is not a reviewer id[\s\S]*distinct_from 42/)
    expect(identityProblems(testIdentities({ [`au-test-jo-writer`]: { distinct_from: [testId('Jo Writer')] } }), R).join(' ')).toMatch(/own reviewer, not a different person/)
    for (const k of ['constructor', '__proto__', 'toString']) {
      expect(identityProblems(testIdentities({ 'au-test-x': { reviewer_id: k } }), R).join(' '), k).toMatch(/is not in the reviewer registry/)
      expect(() => identityProblems(testIdentities({ 'au-test-x': { recorded_by: k } }), R), k).not.toThrow()
      expect(identityProblems(testIdentities({ 'au-test-x': { recorded_by: k } }), R).join(' '), k).toMatch(/recorded_by must be/)
    }
  })
})
