import { describe, expect, it } from 'vitest'
import { QUESTIONS, SKILLS } from './data/demo/fixtures'
import { IMPORT_CONTRACT, questionKey, validateImport, type ImportedQuestion } from './questionImport'

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
})
