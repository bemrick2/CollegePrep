/**
 * Validation for questions arriving from the separate question-bank workstream (docs/product/QUESTION_IMPORT_CONTRACT.md).
 *
 * This checks shape, provenance and rights fields only. Passing it makes an item a well-formed DRAFT that can enter
 * the editorial pipeline at stage 3 (rights check). It never makes an item publishable: that needs the human stages
 * 3–8 in the editorial ledger, the CR-24 rights gate and approve_practice_question (CR-21). Generation confers nothing.
 */
import type { FixtureQuestion } from './data/demo/fixtures'

export const IMPORT_CONTRACT = 'question_import/v1'

/** CR-24's proposed set. `licensed:<vendor>` needs a signed license on file before stage 3 can pass. */
export const ALLOWED_LICENSES = /^(original-owned|us-federal-pd|public-domain|cc-by-4\.0|licensed:[a-z0-9][a-z0-9-]{1,60})$/
const NEEDS_ATTRIBUTION = /^(public-domain|cc-by-4\.0|licensed:|us-federal-pd)/

export type Origin = 'human_original' | 'ai_drafted' | 'adapted_public_domain' | 'adapted_cc_by' | 'licensed'

export interface ImportedQuestion extends Omit<FixtureQuestion, 'id'> {
  contract: typeof IMPORT_CONTRACT
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

export interface ImportProblem {
  import_id: string
  field: string
  problem: string
}

const SECTIONS: Record<string, string[]> = { act: ['english', 'math', 'reading', 'science'], sat: ['reading_writing', 'math'] }
const ORIGINS: Origin[] = ['human_original', 'ai_drafted', 'adapted_public_domain', 'adapted_cc_by', 'licensed']
const words = (s: string) => s.trim().split(/\s+/).filter(Boolean).length
/** Stems compared after case, punctuation and spacing are removed, to catch exact and trivially edited duplicates. */
export const stemKey = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim()
/** Two items are the same question when stem, passage and choices all match (many English items share a stem). */
export const questionKey = (q: Partial<Pick<FixtureQuestion, 'stem' | 'passage' | 'choices'>>) =>
  stemKey([q.stem ?? '', q.passage ?? '', ...(q.choices ?? []).map((c) => (typeof c === 'string' ? c : c.text))].join(' '))

/**
 * Validates a batch. `skillKeys`: the taxonomy's skill keys; `existingStems`: stemKey of every item already in the
 * bank (any status), from questionKey. Returns every problem found; an empty list means each item may enter the pipeline as a draft.
 */
export function validateImport(items: unknown[], skillKeys: Set<string>, existingStems: Set<string> = new Set()): ImportProblem[] {
  const out: ImportProblem[] = []
  const ids = new Set<string>()
  const stems = new Map<string, string>()
  items.forEach((raw, i) => {
    const q = (raw ?? {}) as Partial<ImportedQuestion>
    const id = typeof q.import_id === 'string' && q.import_id ? q.import_id : `#${i + 1}`
    const bad = (field: string, problem: string) => out.push({ import_id: id, field, problem })
    if (q.contract !== IMPORT_CONTRACT) bad('contract', `must be "${IMPORT_CONTRACT}"`)
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
    if (!skillKeys.has(q.primary_skill_key ?? '')) bad('primary_skill_key', 'not a skill in the taxonomy')

    const answers = Array.isArray(q.accepted_answers) ? q.accepted_answers : []
    if (!answers.length || answers.some((a) => typeof a !== 'string' || !a.trim())) bad('accepted_answers', 'at least one non-empty answer')
    if (q.answer_format === 'choice') {
      const keys: string[] = Array.isArray(q.choices) ? q.choices.map((c) => String(c?.key ?? '')) : []
      if (keys.length < 2 || keys.some((k) => typeof k !== 'string' || !k) || new Set(keys).size !== keys.length) bad('choices', 'at least two choices with unique keys')
      if (answers.length !== 1) bad('accepted_answers', 'a choice question has exactly one key')
      else if (!keys.includes(String(answers[0]))) bad('accepted_answers', 'the key is not one of the choices')
      const rationaleFor = new Set((q.distractors ?? []).map((d) => d?.choice))
      for (const k of keys) if (k !== answers[0] && !rationaleFor.has(k)) bad('distractors', `no rationale for wrong choice ${k}`)
    } else if (q.answer_format === 'numeric') {
      // Accepted spellings may carry a unit or sign as students type them ("$63", "−5"), but each must contain a number.
      if (answers.some((a) => !/^[$−-]?\s*(\d+(\.\d+)?|\.\d+|\d+\/\d+)\s*%?$/.test(String(a).trim()))) bad('accepted_answers', 'numeric answers are numbers or fractions')
    } else bad('answer_format', 'choice or numeric')

    if (!Array.isArray(q.hints) || !q.hints.length) bad('hints', 'at least one hint that does not give the answer away')
    if (typeof q.teaching_explanation !== 'string' || !q.teaching_explanation.trim()) bad('teaching_explanation', 'required')
    if (typeof q.strategy_explanation !== 'string' || !q.strategy_explanation.trim()) bad('strategy_explanation', 'required')
    if (typeof q.remember === 'string' && words(q.remember) > 16) bad('remember', 'at most 16 words')

    // Provenance and rights (CR-24). Checked again by a person at stage 3; this only rejects what can't pass.
    if (!ORIGINS.includes(q.origin as Origin)) bad('origin', ORIGINS.join(', '))
    if (typeof q.author !== 'string' || !q.author.trim()) bad('author', 'a named person, or "ai:<model>"')
    if (q.origin === 'ai_drafted' && !/^ai:/.test(q.author ?? '')) bad('author', 'an AI draft names its model as "ai:<model>"')
    if (!ALLOWED_LICENSES.test(q.license ?? '')) bad('license', 'one of original-owned, us-federal-pd, public-domain, cc-by-4.0, licensed:<vendor>')
    else if (NEEDS_ATTRIBUTION.test(q.license!) && !(typeof q.source_attribution === 'string' && q.source_attribution.trim()))
      bad('source_attribution', `required for ${q.license}`)
    if ((q.origin === 'adapted_cc_by') !== (q.license === 'cc-by-4.0')) bad('license', 'adapted_cc_by and cc-by-4.0 go together')
    if (/\b(act,? inc|college board|bluebook|official sat|official act)\b/i.test(`${q.source_attribution ?? ''} ${q.source_url ?? ''}`))
      bad('source_attribution', 'official ACT or College Board material is not accepted without written permission')

    if (q.requested_pool !== 'practice' && q.requested_pool !== 'assessment') bad('requested_pool', 'practice or assessment')
  })
  return out
}
