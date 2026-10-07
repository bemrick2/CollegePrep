import type { FixtureQuestion } from './fixtures'
import record from './questionReviews.json'

/**
 * Content review gate for the question bank. An item is served only when a review approved it AND its content is
 * byte-for-byte what was approved (contentHash). Editing a stem, a choice, the key or an explanation voids the
 * approval until the item is reviewed again and the record regenerated (scripts/local/recordReviews.ts).
 *
 * The review is recorded honestly in questionReviews.json: two independent blind solves, a key-and-explanation
 * audit, and manual resolution of any disagreement. It is not a human editorial review, and nothing here is
 * calibrated against real test-takers.
 */

export interface QuestionReview {
  status: 'approved' | 'changes_needed' | 'rejected'
  hash: string
  reviewed_at: string
  /** Blind solves that matched the key, out of solves run. */
  blind_solves: [number, number]
  audit: 'approve' | 'fix' | 'reject'
  notes: string | null
}

export interface ReviewRecord {
  method: string
  reviewer: string
  human_reviewed: false
  items: Record<string, QuestionReview>
}

export const REVIEW_RECORD = record as unknown as ReviewRecord

/** cyrb53: a fast 53-bit string hash. For change detection only; not a security control. */
function cyrb53(str: string, seed = 0) {
  let h1 = 0xdeadbeef ^ seed
  let h2 = 0x41c6ce57 ^ seed
  for (let i = 0; i < str.length; i++) {
    const ch = str.charCodeAt(i)
    h1 = Math.imul(h1 ^ ch, 2654435761)
    h2 = Math.imul(h2 ^ ch, 1597334677)
  }
  h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909)
  h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909)
  return (4294967296 * (2097151 & h2) + (h1 >>> 0)).toString(16).padStart(14, '0')
}

/** Everything a student sees or is graded on. Field order is fixed so the hash is stable. */
export function contentHash(q: FixtureQuestion): string {
  const content = [
    q.exam_family,
    q.section,
    q.primary_skill_key,
    q.passage ?? null,
    q.stem,
    q.choices,
    q.answer_format,
    q.accepted_answers,
    q.hints,
    q.teaching_explanation,
    q.strategy_explanation,
    q.remember,
    q.distractors,
    q.strategies,
  ]
  return cyrb53(JSON.stringify(content))
}

export function isReviewed(q: FixtureQuestion, rec: ReviewRecord = REVIEW_RECORD): boolean {
  const r = rec.items[q.id]
  return !!r && r.status === 'approved' && r.hash === contentHash(q)
}

/** The bank as served: reviewed items only. */
export function reviewedOnly<T extends FixtureQuestion>(qs: T[], rec: ReviewRecord = REVIEW_RECORD): T[] {
  return qs.filter((q) => isReviewed(q, rec))
}
