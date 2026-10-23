/**
 * Candidate registry for imported questions (docs/product/QUESTION_REVIEW_WORKFLOW.md).
 *
 * Every item that passes the import validator (questionImport.ts) is recorded here as a candidate. Nothing in this file
 * publishes an item or loosens a gate. It adds four things the validator and the editorial ledger don't keep:
 *
 * 1. **Tracks.** Each candidate is either a practice candidate or a reserved assessment candidate. The workstream's
 *    `requested_pool` sets a provisional track; only a named person (the content lead) confirms or changes it.
 *    A candidate may move from assessment to practice, never back, and never after any version was a practice candidate.
 * 2. **Retired duplicates.** An item that duplicates another candidate or a bank item is kept, as retired with
 *    `duplicate_of`, never deleted and never eligible. A retired candidate stays retired.
 * 3. **Content versions.** An import_id that arrives again with different content becomes a new version; earlier
 *    versions and their history are kept. The editorial ledger pins sign-offs to the content hash, so review restarts.
 * 4. **Answer keys bound to a version.** A key is looked up by (import_id, content hash). A revised question never
 *    inherits an earlier version's key, solves or approval; if it carries the same key text, that key is unverified
 *    until two new blind solves of the revised text match it.
 *
 * Publication eligibility is per item: the latest version of a non-retired candidate whose track was confirmed by a
 * named person and whose every editorial stage (3–8) passed on exactly that content. Sampling a few items checks the
 * process; it never makes the unsampled items eligible.
 */
import type { FixtureQuestion } from './data/demo/fixtures'
import { contentHash } from './data/demo/questionReview'
import { AI_AUTHOR, EDITORIAL_LEDGER, editorialState, type Ledger, type SignOff } from './data/demo/editorialLedger'
import { questionKey, type ImportedQuestion } from './questionImport'

export type Track = 'practice_candidate' | 'assessment_candidate'

export interface CandidateVersion {
  version: number
  content_hash: string
  /** The batch file it came from, e.g. "prep-price-bank-B-2026-10-23.jsonl". */
  batch: string
  received: string
  /** The line exactly as imported (validated), kept so every version can be re-read and re-hashed. */
  item: ImportedQuestion
}

export type HistoryEvent =
  | { at: string; event: 'received'; version: number; batch: string; content_hash: string }
  | { at: string; event: 'revised'; version: number; batch: string; content_hash: string; previous_hash: string; key_carried: boolean }
  | { at: string; event: 'unchanged_resubmission'; batch: string; content_hash: string }
  | { at: string; event: 'retired'; reason: string; duplicate_of?: string; by: string }
  | { at: string; event: 'track_set'; track: Track; by: string; reason: string }
  | { at: string; event: 'refused'; batch: string; reason: string }

export interface Candidate {
  import_id: string
  track: Track
  /** The named person who confirmed the track; null while it is only the workstream's request. */
  track_confirmed_by: string | null
  status: 'draft' | 'retired'
  duplicate_of?: string
  /** Oldest first; never rewritten. */
  versions: CandidateVersion[]
  /** Append-only. */
  history: HistoryEvent[]
}

export interface Registry {
  contract: 'question_candidates/v1'
  candidates: Record<string, Candidate>
}

export const emptyRegistry = (): Registry => ({ contract: 'question_candidates/v1', candidates: {} })

const NOT_A_PERSON = /^(ai\b|ai:|claude|gpt|model|team|reviewer|content lead|editor|tbd|unknown|system)/i
const person = (s: string) => s.trim().toLowerCase()
const trackOf = (pool: ImportedQuestion['requested_pool']): Track => (pool === 'assessment' ? 'assessment_candidate' : 'practice_candidate')

/** The question as the app and the ledger see it: the import line with its import_id as the id. */
export function asQuestion(v: CandidateVersion, importId: string): FixtureQuestion {
  const { contract: _c, import_id: _i, origin: _o, author: _a, license: _l, source_attribution: _s, source_url: _u, requested_pool: _p, status: _st, ...content } = v.item
  return { id: importId, ...(content as Omit<FixtureQuestion, 'id'>) }
}

export const latest = (c: Candidate): CandidateVersion => c.versions[c.versions.length - 1]!

export interface IntakeResult {
  received: string[]
  revised: string[]
  unchanged: string[]
  /** Kept as retired duplicates, with what they duplicate. */
  retired: { import_id: string; duplicate_of: string }[]
  /** Not recorded as a new version, with why (e.g. a revision of a retired or reserved-and-exposed item). */
  refused: { import_id: string; reason: string }[]
}

/**
 * Records a validated batch. Call validateImport first and pass only items with no problems; this does not re-check
 * shape or rights. `bankKeys`: questionKey → id for questions already in the app's bank (fixtures, later hosted).
 * Returns a new registry; the input is not changed.
 */
export function intake(reg: Registry, items: ImportedQuestion[], batch: string, at: string, bankKeys: Map<string, string> = new Map()): { registry: Registry; result: IntakeResult } {
  const next: Registry = JSON.parse(JSON.stringify(reg))
  const result: IntakeResult = { received: [], revised: [], unchanged: [], retired: [], refused: [] }
  // questionKey of the latest version of every live candidate, for duplicate detection across banks.
  const live = new Map<string, string>()
  for (const c of Object.values(next.candidates)) if (c.status !== 'retired') live.set(questionKey(asQuestion(latest(c), c.import_id)), c.import_id)

  for (const item of items) {
    const id = item.import_id
    const hash = contentHash({ id, ...item } as unknown as FixtureQuestion)
    const key = questionKey(item)
    const existing = next.candidates[id]

    if (existing) {
      const cur = latest(existing)
      if (cur.content_hash === hash) {
        existing.history.push({ at, event: 'unchanged_resubmission', batch, content_hash: hash })
        result.unchanged.push(id)
        continue
      }
      if (existing.status === 'retired') {
        existing.history.push({ at, event: 'refused', batch, reason: 'a retired candidate is not revised; submit it under a new import_id if it is a different question' })
        result.refused.push({ import_id: id, reason: 'retired' })
        continue
      }
      const other = live.get(key)
      if (other && other !== id) {
        existing.history.push({ at, event: 'refused', batch, reason: `this revision duplicates ${other}` })
        result.refused.push({ import_id: id, reason: `revision duplicates ${other}` })
        continue
      }
      const keyCarried = JSON.stringify(cur.item.accepted_answers) === JSON.stringify(item.accepted_answers)
      existing.versions.push({ version: cur.version + 1, content_hash: hash, batch, received: at, item })
      existing.history.push({ at, event: 'revised', version: cur.version + 1, batch, content_hash: hash, previous_hash: cur.content_hash, key_carried: keyCarried })
      live.delete(questionKey(asQuestion(cur, id)))
      live.set(key, id)
      result.revised.push(id)
      continue
    }

    const dup = bankKeys.has(key) ? `bank:${bankKeys.get(key)}` : live.get(key)
    const c: Candidate = {
      import_id: id,
      track: trackOf(item.requested_pool),
      track_confirmed_by: null,
      status: dup ? 'retired' : 'draft',
      versions: [{ version: 1, content_hash: hash, batch, received: at, item }],
      history: [{ at, event: 'received', version: 1, batch, content_hash: hash }],
    }
    if (dup) {
      c.duplicate_of = dup
      c.history.push({ at, event: 'retired', reason: 'duplicate', duplicate_of: dup, by: 'intake' })
      result.retired.push({ import_id: id, duplicate_of: dup })
    } else {
      live.set(key, id)
      result.received.push(id)
    }
    next.candidates[id] = c
  }
  return { registry: next, result }
}

/**
 * The content lead confirms or changes a track. `exposed`: ids any student has seen in practice (from the database
 * once hosted is back; empty locally). Throws when the move is not allowed. Returns a new registry.
 */
export function setTrack(reg: Registry, id: string, track: Track, by: string, reason: string, at: string, exposed: Set<string> = new Set()): Registry {
  const c = reg.candidates[id]
  if (!c) throw new Error(`no candidate ${id}`)
  if (c.status === 'retired') throw new Error(`${id} is retired`)
  if (!by.trim() || NOT_A_PERSON.test(by.trim())) throw new Error(`"${by}" is not a named person; only the content lead sets a track`)
  if (!reason.trim()) throw new Error('a reason is required')
  if (c.versions.some((v) => person(v.item.author) === person(by))) throw new Error(`${by} wrote this item and can't set its track`)
  if (track === 'assessment_candidate') {
    const wasPractice = c.history.some((h) => h.event === 'track_set' && h.track === 'practice_candidate') || (c.track === 'practice_candidate' && c.track_confirmed_by)
    if (wasPractice) throw new Error(`${id} was confirmed for practice; a practice item never becomes a reserved assessment item`)
    if (exposed.has(id)) throw new Error(`${id} has been seen in practice and can't be reserved`)
  }
  const next: Registry = JSON.parse(JSON.stringify(reg))
  const n = next.candidates[id]!
  n.track = track
  n.track_confirmed_by = by.trim()
  n.history.push({ at, event: 'track_set', track, by: by.trim(), reason: reason.trim() })
  return next
}

/** Retires a candidate (kept, never deleted). Returns a new registry. */
export function retire(reg: Registry, id: string, by: string, reason: string, at: string, duplicateOf?: string): Registry {
  const c = reg.candidates[id]
  if (!c) throw new Error(`no candidate ${id}`)
  if (!by.trim() || NOT_A_PERSON.test(by.trim())) throw new Error(`"${by}" is not a named person`)
  if (!reason.trim()) throw new Error('a reason is required')
  const next: Registry = JSON.parse(JSON.stringify(reg))
  const n = next.candidates[id]!
  n.status = 'retired'
  if (duplicateOf) n.duplicate_of = duplicateOf
  n.history.push({ at, event: 'retired', reason: reason.trim(), by: by.trim(), ...(duplicateOf ? { duplicate_of: duplicateOf } : {}) })
  return next
}

/**
 * The answer key for one exact version. Throws unless `hash` is that version's content hash, so a key can never be
 * attached to different (revised or stale) content. `verified` is true only when two blind solves of exactly this
 * content, by people who never authored any version, matched it.
 */
export function answerKeyFor(c: Candidate, hash: string, ledger: Ledger = EDITORIAL_LEDGER): { version: number; accepted_answers: string[]; verified: boolean; carried_from?: number } {
  const v = c.versions.find((x) => x.content_hash === hash)
  if (!v) throw new Error(`${c.import_id}: no version has content ${hash}; a key is never attached to other content`)
  const authors = new Set(c.versions.map((x) => person(x.item.author)))
  const keys = v.item.accepted_answers.map((a) => a.trim().toLowerCase())
  const solvers = new Set(
    (ledger.items[c.import_id]?.signoffs ?? [])
      .filter((s) => s.stage === 4 && s.result === 'pass' && s.hash === hash && !NOT_A_PERSON.test(s.by.trim()) && !authors.has(person(s.by)))
      .filter((s) => keys.includes((s.answer ?? '').trim().toLowerCase()))
      .map((s) => person(s.by)),
  )
  const prev = c.versions.filter((x) => x.version < v.version && JSON.stringify(x.item.accepted_answers) === JSON.stringify(v.item.accepted_answers)).pop()
  return { version: v.version, accepted_answers: [...v.item.accepted_answers], verified: solvers.size >= 2, ...(prev ? { carried_from: prev.version } : {}) }
}

export interface Eligibility {
  import_id: string
  track: Track
  version: number
  content_hash: string
  eligible: boolean
  problems: string[]
}

/**
 * Whether one candidate may be published, judged on its latest version alone. Every condition must hold for this
 * item individually; nothing about other items (a sample, a batch pass rate) changes the answer.
 */
export function eligibility(c: Candidate, ledger: Ledger = EDITORIAL_LEDGER): Eligibility {
  const v = latest(c)
  const q = asQuestion(v, c.import_id)
  const problems: string[] = []
  if (c.status === 'retired') problems.push(c.duplicate_of ? `retired: duplicates ${c.duplicate_of}` : 'retired')
  if (!c.track_confirmed_by) problems.push('track is only the workstream’s request; the content lead has not confirmed it')

  // The ledger's author is the import's author (not the AI default), so the author can't approve their own item.
  const entry = ledger.items[c.import_id]
  if (entry && entry.author !== AI_AUTHOR && person(entry.author) !== person(v.item.author)) problems.push(`ledger author "${entry.author}" differs from the import author "${v.item.author}"`)
  const view: Ledger = { items: { [c.import_id]: { author: v.item.author, signoffs: entry?.signoffs ?? [] } } }
  const st = editorialState(q, view)
  if (!st.humanApproved) problems.push(...st.problems, `editorial review is at stage ${st.next}`)

  // Anyone who wrote any version is not independent: their solve isn't blind, and they can't pass stages 6 or 8.
  const authors = new Set(c.versions.map((x) => person(x.item.author)))
  const own = (entry?.signoffs ?? []).filter((s: SignOff) => s.hash === v.content_hash && [4, 6, 8].includes(s.stage) && authors.has(person(s.by)))
  if (own.length) problems.push(`sign-off(s) at stage ${[...new Set(own.map((s) => s.stage))].join(', ')} by an author of an earlier version`)
  if (!answerKeyFor(c, v.content_hash, ledger).verified) problems.push('answer key not confirmed by two independent blind solves of this version')

  return { import_id: c.import_id, track: c.track, version: v.version, content_hash: v.content_hash, eligible: problems.length === 0, problems: [...new Set(problems)] }
}

/** Eligible items of one track. Retired candidates and the other track are never included. */
export function eligibleFor(reg: Registry, track: Track, ledger: Ledger = EDITORIAL_LEDGER): Eligibility[] {
  return Object.values(reg.candidates).filter((c) => c.track === track).map((c) => eligibility(c, ledger)).filter((e) => e.eligible)
}

/** Counts by track and status, for reports. Eligible counts are per item. */
export function summary(reg: Registry, ledger: Ledger = EDITORIAL_LEDGER) {
  const out = { practice_candidate: { draft: 0, retired: 0, eligible: 0 }, assessment_candidate: { draft: 0, retired: 0, eligible: 0 }, versions: 0 }
  for (const c of Object.values(reg.candidates)) {
    out[c.track][c.status]++
    out.versions += c.versions.length
    if (eligibility(c, ledger).eligible) out[c.track].eligible++
  }
  return out
}
