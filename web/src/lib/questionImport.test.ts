import { describe, expect, it } from 'vitest'
import { QUESTIONS, SKILLS } from './data/demo/fixtures'
import { IMPORT_CONTRACT, IMPORT_CONTRACT_V2, questionKey, validateImport, type ImportedQuestion } from './questionImport'
import { testIdentities } from './data/demo/testReviewers'
import { IDENTITIES } from './data/demo/authorIdentity'

const skills = SKILLS
/** An existing fixture, dressed as an import, so the validator is tested against real-quality content. */
function asImport(i = 0, extra: Partial<ImportedQuestion> = {}): ImportedQuestion {
  const { id, ...q } = QUESTIONS[i]!
  return { ...q, contract: IMPORT_CONTRACT, import_id: `wk-${id}`.toLowerCase(), origin: 'ai_drafted', author: 'ai:example-model', license: 'original-owned', source_attribution: null, source_url: null, requested_pool: 'practice', ...extra }
}
const problems = (items: unknown[], existing = new Set<string>()) => validateImport(items, skills, existing).map((p) => `${p.field}: ${p.problem}`)

describe('question import contract (question_import/v1)', () => {
  it('accepts well-formed drafts (every current fixture, as an import)', () => {
    expect(problems(QUESTIONS.map((_, i) => asImport(i)))).toEqual([])
  })

  it('never lets an import arrive published', () => {
    expect(problems([asImport(0, { status: 'published' })])).toContain('status: imported questions are drafts; publishing happens only after review')
  })

  it('rejects what can never pass the rights check', () => {
    expect(problems([asImport(0, { license: 'cc-by-nc-4.0' })]).some((p) => p.startsWith('license'))).toBe(true)
    expect(problems([asImport(0, { license: 'cc-by-4.0', origin: 'adapted_cc_by' })])).toContain('source_attribution: required for cc-by-4.0')
    expect(problems([asImport(0, { license: 'public-domain', origin: 'adapted_public_domain', source_attribution: 'Official SAT Practice Test 4' })])).toContain(
      'source_attribution: official ACT or College Board material is not accepted without written permission',
    )
    expect(problems([asImport(0, { origin: 'ai_drafted', author: 'Jordan Lee' })])).toContain('author: an AI draft names its model as "ai:<model>"')
    expect(problems([asImport(0, { author: 'ai:' })])).toContain('author: an AI draft names its model as "ai:<model>"')
    expect(problems([asImport(0, { origin: 'human_original', author: 'ai:model-x' })])).toContain('origin: an "ai:" author means origin ai_drafted')
    expect(problems([asImport(0, { origin: 'licensed', license: 'original-owned' })])).toContain("license: original-owned doesn't fit origin licensed")
    expect(problems([asImport(0, { origin: 'adapted_public_domain', license: 'public-domain', source_attribution: 'x', source_url: 'https://satsuite.collegeboard.org/practice' })])).toContain(
      'source_attribution: official ACT or College Board material is not accepted without written permission',
    )
    expect(problems([asImport(0, { origin: 'adapted_public_domain', license: 'public-domain', source_attribution: 'x', source_url: 'https://www.act.org/content/dam/act/test.pdf' })]).some((p) => p.includes('official'))).toBe(true)
  })

  it('refuses fields outside the contract, so no id, pool, approval or hash can ride along', () => {
    expect(problems([{ ...asImport(0), pool: 'assessment', approved: true, content_hash: 'x' }])).toEqual(
      expect.arrayContaining([expect.stringMatching(/^pool: not a field/), expect.stringMatching(/^approved: not a field/), expect.stringMatching(/^content_hash: not a field/)]),
    )
  })

  it('refuses empty hints, empty choice text, and a skill from the other exam', () => {
    const q = asImport(0)
    expect(problems([{ ...q, hints: [''] }]).some((p) => p.startsWith('hints'))).toBe(true)
    const sat = SKILLS.find((k) => k.exam_family === 'sat')!.skill_key
    expect(problems([{ ...q, primary_skill_key: sat }])).toContain('primary_skill_key: a skill from the other exam')
  })

  it('rejects broken items: key not a choice, missing rationale, unknown skill, long remember line', () => {
    const q = asImport(0)
    const wrongKey = { ...q, accepted_answers: ['Z'] }
    expect(problems([wrongKey])).toContain('accepted_answers: the key is not one of the choices')
    expect(problems([{ ...q, distractors: [] }]).some((p) => p.startsWith('distractors: no rationale'))).toBe(true)
    expect(problems([{ ...q, primary_skill_key: 'act_made_up' }])).toContain('primary_skill_key: not a skill in the taxonomy')
    expect(problems([{ ...q, remember: Array(17).fill('word').join(' ') }])).toContain('remember: at most 16 words')
  })

  it('catches duplicates within a batch and against the bank', () => {
    const a = asImport(0)
    const b = { ...asImport(0), import_id: 'wk-copy', stem: a.stem.toUpperCase() + '!' }
    expect(problems([a, b]).some((p) => p.startsWith('stem: duplicates wk-'))).toBe(true)
    expect(problems([a], new Set([questionKey(a)]))).toContain('stem: duplicates a question already in the bank')
  })

  describe('question_import/v2: author identities', () => {
    const TI = testIdentities()
    const v2 = (i: number, extra: Partial<ImportedQuestion>) => asImport(i, { contract: IMPORT_CONTRACT_V2, ...extra })
    const p2 = (items: unknown[], ids = TI) => validateImport(items, skills, new Set(), ids).map((p) => `${p.field}: ${p.problem}`)

    it('accepts an AI draft that names its model, and a person with a recorded identity', () => {
      expect(p2([v2(0, { author_identity: { kind: 'ai', model: 'example-model' } })])).toEqual([])
      expect(p2([v2(1, { origin: 'human_original', author: 'Jo Writer', author_identity: { kind: 'person', identity_id: 'au-test-jo-writer' } })])).toEqual([])
    })

    it('a v2 line must say who wrote it; a batch never creates an identity', () => {
      expect(p2([v2(0, {})]).join(' ')).toMatch(/author_identity: required/)
      expect(p2([v2(0, { origin: 'human_original', author: 'Jo Writer', author_identity: { kind: 'person', identity_id: 'au-new-person' } })]).join(' ')).toMatch(/is not a recorded identity/)
      // The real identity registry is empty: no person can be named yet.
      expect(p2([v2(0, { origin: 'human_original', author: 'Jo Writer', author_identity: { kind: 'person', identity_id: 'au-test-jo-writer' } })], IDENTITIES).join(' ')).toMatch(/is not a recorded identity/)
      // Built-in object keys are never identities (#290 review).
      for (const k of ['constructor', 'toString', '__proto__', 'hasOwnProperty'])
        expect(p2([v2(0, { origin: 'human_original', author: 'Jo Writer', author_identity: { kind: 'person', identity_id: k } })], IDENTITIES).join(' '), k).toMatch(/is not a recorded identity/)
    })

    it('AI authorship stays explicit and consistent with origin and author', () => {
      expect(p2([v2(0, { author_identity: { kind: 'ai', model: 'other-model' } })]).join(' ')).toMatch(/author: an AI author is written "ai:other-model"/)
      expect(p2([v2(0, { origin: 'human_original', author: 'ai:example-model', author_identity: { kind: 'ai', model: 'example-model' } })]).join(' ')).toMatch(/an AI author means origin ai_drafted/)
      expect(p2([v2(0, { author_identity: { kind: 'person', identity_id: 'au-test-jo-writer' } })]).join(' ')).toMatch(/an AI draft has an AI author identity/)
      expect(p2([v2(0, { author_identity: { kind: 'ai', model: '' } })]).join(' ')).toMatch(/names its model/)
      expect(p2([v2(0, { author_identity: { kind: 'ai', model: 'example-model', identity_id: 'au-x' } as never })]).join(' ')).toMatch(/only kind and model/)
    })

    it('a v1 line can’t carry an identity (it stays legacy); unknown contracts are refused', () => {
      expect(p2([asImport(0, { author_identity: { kind: 'ai', model: 'example-model' } })]).join(' ')).toMatch(/not a field of question_import\/v1/)
      expect(p2([asImport(0, { contract: 'question_import/v3' as never })]).join(' ')).toMatch(/contract: must be/)
    })
  })
})

