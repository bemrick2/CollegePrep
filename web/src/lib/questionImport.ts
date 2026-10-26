/**
 * Validation for questions arriving from the separate question-bank workstream (docs/product/QUESTION_IMPORT_CONTRACT.md).
 *
 * This checks shape, provenance and rights fields only. Passing it makes an item a well-formed DRAFT that can enter
 * the editorial pipeline at stage 3 (rights check). It never makes an item publishable: that needs the human stages
 * 3–8 in the editorial ledger, the CR-24 rights gate and approve_practice_question (CR-21). Generation confers nothing.
 */
import type { FixtureQuestion } from './data/demo/fixtures'
import { AI_MODEL, IDENTITIES, identityOf, type AuthorIdentity, type IdentityRegistry } from './data/demo/authorIdentity'

/** The legacy contract: authors are names only, so a human author is never a resolved identity. Still read. */
export const IMPORT_CONTRACT = 'question_import/v1'
/** The current contract: every line names its author's identity (an AI model, or a recorded person). */
export const IMPORT_CONTRACT_V2 = 'question_import/v2'
export const IMPORT_CONTRACTS = [IMPORT_CONTRACT, IMPORT_CONTRACT_V2] as const

/** CR-24's set (Research, #245). `licensed:<vendor>` needs a signed license on file before stage 3 can pass. */
export const ALLOWED_LICENSES = /^(original-owned|us-federal-pd|public-domain|cc-by-4\.0|cc-by-sa-4\.0|licensed:[a-z0-9][a-z0-9-]{0,62})$/
/** Stricter than the server (which needs attribution for CC and licensed items only): an adapted public-domain
 *  source must be named too, so stage 3 can check it. */
const NEEDS_ATTRIBUTION = /^(public-domain|cc-by-4\.0|cc-by-sa-4\.0|licensed:|us-federal-pd)/

/** The database's `practice_questions.origin` (CR-24) for each import origin. A generated item needs a human review. */
export const DB_ORIGIN: Record<Origin, 'authored' | 'generated' | 'licensed'> = {
  human_original: 'authored',
  ai_drafted: 'generated',
  adapted_public_domain: 'authored',
  adapted_cc_by: 'authored',
  licensed: 'licensed',
}

export type Origin = 'human_original' | 'ai_drafted' | 'adapted_public_domain' | 'adapted_cc_by' | 'licensed'

export interface ImportedQuestion extends Omit<FixtureQuestion, 'id'> {
  contract: (typeof IMPORT_CONTRACTS)[number]
  /**
   * v2 only, required there: who wrote it. `{kind: 'ai', model}` for an AI draft (author "ai:<model>"), or
   * `{kind: 'person', identity_id}` naming a recorded identity (identities.json). A batch never creates an identity.
   */
  author_identity?: AuthorIdentity
  /** Stable id from the workstream; becomes the fixture id / import key. Never reused for different content. */
  import_id: string
  origin: Origin
  /** A named person, or "ai:<model>" for an AI draft. Reviewers later must differ from this. */
  author: string
  license: string
  source_attribution: string | null
  source_url: string | null
  /** The workstream's request; the content lead assigns the final pool before any student sees the item. */
  requested_pool: 'practice' | 'assessment'
  /** Must be absent or "draft". */
  status?: string
}

/** Every field a line may carry. Anything else (an id, a pool, an approval, a hash) is refused, never passed on. */
const ALLOWED_KEYS = new Set([
  'contract', 'import_id', 'exam_family', 'section', 'difficulty', 'stem', 'passage', 'choices', 'answer_format', 'accepted_answers',
  'expected_time_seconds', 'primary_skill_key', 'hints', 'teaching_explanation', 'strategy_explanation', 'remember', 'distractors',
  'strategies', 'origin', 'author', 'author_identity', 'license', 'source_attribution', 'source_url', 'requested_pool', 'status',
])
/** Which licenses each origin may carry. */
const ORIGIN_LICENSES: Record<Origin, RegExp> = {
  human_original: /^original-owned$/,
  ai_drafted: /^original-owned$/,
  adapted_public_domain: /^(public-domain|us-federal-pd)$/,
  adapted_cc_by: /^cc-by(-sa)?-4\.0$/,
  licensed: /^licensed:/,
}
/** Official ACT or College Board material: names, products and domains, anywhere in the item or its source. */
const OFFICIAL = /\b(act,? inc|act\.org|actstudent(\.org)?|act academy|college\s*board|collegeboard(\.org)?|satsuite|bluebook|official\s+(sat|act)|khan academy official sat)\b/i

export interface ImportProblem {
  import_id: string
  field: string
  problem: string
}

const SECTIONS: Record<string, string[]> = { act: ['english', 'math', 'reading', 'science'], sat: ['reading_writing', 'math'] }
const ORIGINS: Origin[] = ['human_original', 'ai_drafted', 'adapted_public_domain', 'adapted_cc_by', 'licensed']
const words = (s: string) => s.trim().split(/\s+/).filter(Boolean).length
/** Stems compared after case, punctuation and spacing are removed, to catch exact and trivially edited duplicates. */
/** Case, spacing and ordinary punctuation are ignored; math symbols (√ ² π −) are kept, so they still distinguish items. */
export const stemKey = (s: string) => s.normalize('NFKC').replace(/\u2212/g, '-').toLowerCase().replace(/[\s.,;:!?'"“”‘’()\[\]-]+/g, ' ').trim()
/** Two items are the same question when stem, passage and choices all match (many English items share a stem). */
export const questionKey = (q: Partial<Pick<FixtureQuestion, 'stem' | 'passage' | 'choices'>>) =>
  stemKey([q.stem ?? '', q.passage ?? '', ...(q.choices ?? []).map((c) => (typeof c === 'string' ? c : c.text))].join(' '))

/**
 * Validates a batch. `skillKeys`: the taxonomy's skill keys; `existingStems`: stemKey of every item already in the
 * bank (any status), from questionKey. Returns every problem found; an empty list means each item may enter the pipeline as a draft.
 */
export function validateImport(items: unknown[], skills: { skill_key: string; exam_family: string }[], existingStems: Set<string> = new Set(), identities: IdentityRegistry = IDENTITIES): ImportProblem[] {
  const skillExam = new Map(skills.map((k) => [k.skill_key, k.exam_family]))
  const out: ImportProblem[] = []
  const ids = new Set<string>()
  const stems = new Map<string, string>()
  items.forEach((raw, i) => {
    const q = (raw ?? {}) as Partial<ImportedQuestion>
    const id = typeof q.import_id === 'string' && q.import_id ? q.import_id : `#${i + 1}`
    const bad = (field: string, problem: string) => out.push({ import_id: id, field, problem })
    for (const k of Object.keys(q)) if (!ALLOWED_KEYS.has(k)) bad(k, 'not a field of the contract; remove it (ids, pools, approvals and hashes are assigned in review)')
    const nonEmpty = (v: unknown) => typeof v === 'string' && v.trim() !== ''
    if (!IMPORT_CONTRACTS.includes(q.contract as never)) bad('contract', `must be "${IMPORT_CONTRACT_V2}" (or the legacy "${IMPORT_CONTRACT}")`)
    if (!/^[a-z0-9][a-z0-9_-]{2,80}$/.test(q.import_id ?? '')) bad('import_id', 'lowercase letters, digits, - or _, 3–81 characters')
    else if (ids.has(q.import_id!)) bad('import_id', 'duplicated in this batch')
    else ids.add(q.import_id!)

    // Never published on arrival.
    if (q.status != null && q.status !== 'draft') bad('status', 'imported questions are drafts; publishing happens only after review')

    if (q.exam_family !== 'act' && q.exam_family !== 'sat') bad('exam_family', 'act or sat')
    else if (!SECTIONS[q.exam_family]!.includes(q.section ?? '')) bad('section', `one of ${SECTIONS[q.exam_family]!.join(', ')}`)
    if (!Number.isInteger(q.difficulty) || q.difficulty! < 1 || q.difficulty! > 5) bad('difficulty', 'an integer 1–5 (the author\'s estimate; calibration comes later)')
    if (typeof q.stem !== 'string' || !q.stem.trim()) bad('stem', 'required')
    else {
      const k = questionKey(q)
      if (existingStems.has(k)) bad('stem', 'duplicates a question already in the bank')
      else if (stems.has(k)) bad('stem', `duplicates ${stems.get(k)} in this batch`)
      else stems.set(k, id)
    }
    if (!Number.isInteger(q.expected_time_seconds) || q.expected_time_seconds! < 10 || q.expected_time_seconds! > 600) bad('expected_time_seconds', 'an integer, 10–600')
    if (!skillExam.has(q.primary_skill_key ?? '')) bad('primary_skill_key', 'not a skill in the taxonomy')
    else if (skillExam.get(q.primary_skill_key!) !== q.exam_family) bad('primary_skill_key', 'a skill from the other exam')

    const answers = Array.isArray(q.accepted_answers) ? q.accepted_answers : []
    if (!answers.length || answers.some((a) => typeof a !== 'string' || !a.trim())) bad('accepted_answers', 'at least one non-empty answer')
    if (q.answer_format === 'choice') {
      const keys: string[] = Array.isArray(q.choices) ? q.choices.map((c) => String(c?.key ?? '')) : []
      if (keys.length < 2 || keys.some((k) => !k) || new Set(keys).size !== keys.length) bad('choices', 'at least two choices with unique keys')
      if ((q.choices ?? []).some((c) => !nonEmpty(typeof c === 'string' ? c : c?.text))) bad('choices', 'every choice has text')
      if (answers.length !== 1) bad('accepted_answers', 'a choice question has exactly one key')
      else if (!keys.includes(String(answers[0]))) bad('accepted_answers', 'the key is not one of the choices')
      const rationaleFor = new Set((q.distractors ?? []).filter((d) => nonEmpty(d?.rationale)).map((d) => d?.choice))
      for (const k of keys) if (k !== answers[0] && !rationaleFor.has(k)) bad('distractors', `no rationale for wrong choice ${k}`)
    } else if (q.answer_format === 'numeric') {
      // Accepted spellings may carry a unit or sign as students type them ("$63", "−5"), but each must contain a number.
      if (answers.some((a) => !/^[$−-]?\s*(\d+(\.\d+)?|\.\d+|\d+\/\d+)\s*%?$/.test(String(a).trim()))) bad('accepted_answers', 'numeric answers are numbers or fractions')
    } else bad('answer_format', 'choice or numeric')

    if (!Array.isArray(q.hints) || !q.hints.length || !q.hints.every(nonEmpty)) bad('hints', 'at least one hint, none empty, none giving the answer away')
    if (typeof q.teaching_explanation !== 'string' || !q.teaching_explanation.trim()) bad('teaching_explanation', 'required')
    if (typeof q.strategy_explanation !== 'string' || !q.strategy_explanation.trim()) bad('strategy_explanation', 'required')
    if (typeof q.remember === 'string' && words(q.remember) > 16) bad('remember', 'at most 16 words')

    // Provenance and rights (CR-24). Checked again by a person at stage 3; this only rejects what can't pass.
    if (!ORIGINS.includes(q.origin as Origin)) bad('origin', ORIGINS.join(', '))
    if (typeof q.author !== 'string' || !q.author.trim()) bad('author', 'a named person, or "ai:<model>"')
    if (q.origin === 'ai_drafted' && !/^ai:\S{2,}/.test(q.author ?? '')) bad('author', 'an AI draft names its model as "ai:<model>"')
    if (q.origin !== 'ai_drafted' && /^ai:/i.test(q.author ?? '')) bad('origin', 'an "ai:" author means origin ai_drafted')

    // Author identity (v2). v1 lines carry none: their human authors stay unresolved and their items ineligible.
    const ai = q.author_identity as AuthorIdentity | undefined
    if (q.contract === IMPORT_CONTRACT && ai !== undefined) bad('author_identity', `not a field of ${IMPORT_CONTRACT}; use ${IMPORT_CONTRACT_V2}`)
    if (q.contract === IMPORT_CONTRACT_V2) {
      if (!ai || typeof ai !== 'object' || (ai.kind !== 'ai' && ai.kind !== 'person')) bad('author_identity', 'required: {"kind": "ai", "model": "<model>"} or {"kind": "person", "identity_id": "au-…"}')
      else if (ai.kind === 'ai') {
        if (Object.keys(ai).some((k) => k !== 'kind' && k !== 'model')) bad('author_identity', 'an AI identity has only kind and model')
        if (!AI_MODEL.test(ai.model ?? '')) bad('author_identity', 'an AI author names its model')
        else if (q.author !== `ai:${ai.model}`) bad('author', `an AI author is written "ai:${ai.model}"`)
        if (q.origin !== 'ai_drafted') bad('author_identity', 'an AI author means origin ai_drafted')
      } else {
        if (Object.keys(ai).some((k) => k !== 'kind' && k !== 'identity_id')) bad('author_identity', 'a person identity has only kind and identity_id')
        if (q.origin === 'ai_drafted') bad('author_identity', 'an AI draft has an AI author identity')
        if (!identityOf(identities, ai.identity_id)) bad('author_identity', `${ai.identity_id || '(blank)'} is not a recorded identity; identities are recorded by the owner or a content lead (identities.json), never by a batch`)
      }
    }
    if (ORIGINS.includes(q.origin as Origin) && ALLOWED_LICENSES.test(q.license ?? '') && !ORIGIN_LICENSES[q.origin as Origin].test(q.license!))
      bad('license', `${q.license} doesn't fit origin ${q.origin}`)
    if (!ALLOWED_LICENSES.test(q.license ?? '')) bad('license', 'one of original-owned, us-federal-pd, public-domain, cc-by-4.0, cc-by-sa-4.0, licensed:<vendor>')
    else if (NEEDS_ATTRIBUTION.test(q.license!) && !(typeof q.source_attribution === 'string' && q.source_attribution.trim()))
      bad('source_attribution', `required for ${q.license}`)
    if (OFFICIAL.test([q.source_attribution, q.source_url, q.stem, q.passage].filter(Boolean).join(' ')))
      bad('source_attribution', 'official ACT or College Board material is not accepted without written permission')

    // A request only: the content lead sets the pool in review; the import path never writes this to the pool column.
    if (q.requested_pool !== 'practice' && q.requested_pool !== 'assessment') bad('requested_pool', 'practice or assessment')
  })
  return out
}
