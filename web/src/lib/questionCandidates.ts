/**
 * Candidate registry for imported questions (docs/product/QUESTION_REVIEW_WORKFLOW.md).
 *
 * Every item that passes the import validator (questionImport.ts) is recorded here as a candidate. Nothing in this file
 * publishes an item or loosens a gate. It adds four things the validator and the editorial ledger don't keep:
 *
 * 1. **Tracks.** Each candidate is either a practice candidate or a reserved assessment candidate. The workstream's
 *    `requested_pool` sets a provisional track; only a named person who wrote no version confirms or changes it.
 *    A candidate may move from assessment to practice, never back, and never after any student saw it.
 * 2. **Retired duplicates.** An item whose question matches any version of any candidate (retired ones included) or a
 *    bank item is kept as retired with `duplicate_of`, never deleted and never eligible. A retired candidate stays retired.
 * 3. **Content versions.** A changed line (content or provenance) becomes a new version; earlier versions and the
 *    history are kept. A revision may not return to an earlier version's content: that would revive reviews given
 *    before the reason for revising was known.
 * 4. **Answer keys bound to a version.** A key is looked up by (import_id, content hash). A revised question never
 *    inherits an earlier version's key, solves or approval; if it carries the same key text, that key is unverified
 *    until two new blind solves of the revised text match it.
 *
 * Publication eligibility is per item and is worked out from the append-only history, not from editable summary
 * fields. Sampling a few items checks the process; it never makes the unsampled items eligible.
 */
import type { FixtureQuestion } from './data/demo/fixtures'
import { contentHash, cyrb53 } from './data/demo/questionReview'
import { AI_AUTHOR, canonicalPerson as person, EDITORIAL_LEDGER, editorialState, isIsoDate, isNotAPerson, type Ledger } from './data/demo/editorialLedger'
import { questionKey, type ImportedQuestion } from './questionImport'

export type Track = 'practice_candidate' | 'assessment_candidate'

export interface CandidateVersion {
  version: number
  /** contentHash: what a student sees or is graded on. Ledger sign-offs are pinned to it. */
  content_hash: string
  /** Hash of the whole line, provenance included, so a rights or author change is a new version too. */
  record_hash: string
  /** The batch file it came from, e.g. "prep-price-bank-B-2026-10-23.jsonl". */
  batch: string
  received: string
  /** The line exactly as imported (validated), kept so every version can be re-read and re-hashed. */
  item: ImportedQuestion
}

export type HistoryEvent =
  | { at: string; event: 'received'; version: number; batch: string; content_hash: string }
  | { at: string; event: 'revised'; version: number; batch: string; content_hash: string; previous_hash: string; key_carried: boolean; content_changed: boolean; rights_changed: boolean }
  | { at: string; event: 'unchanged_resubmission'; batch: string; content_hash: string }
  | { at: string; event: 'retired'; reason: string; duplicate_of?: string; by: string }
  | { at: string; event: 'track_set'; track: Track; by: string; reason: string }
  | { at: string; event: 'refused'; batch: string; reason: string }

export interface Candidate {
  import_id: string
  /** Summary fields, kept in step with `history`; eligibility re-derives them from the history. */
  track: Track
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

const trackOf = (pool: ImportedQuestion['requested_pool']): Track => (pool === 'assessment' ? 'assessment_candidate' : 'practice_candidate')
/** Who may claim rights and authorship: any change here voids the rights check (stage 3). */
const RIGHTS_FIELDS = ['author', 'origin', 'license', 'source_attribution', 'source_url'] as const
/** JSON with object keys sorted at every depth, so key order never makes a new version. */
const canonicalJson = (v: unknown): string =>
  Array.isArray(v) ? `[${v.map(canonicalJson).join(',')}]` : v && typeof v === 'object'
    ? `{${Object.keys(v).sort().map((k) => `${JSON.stringify(k)}:${canonicalJson((v as Record<string, unknown>)[k])}`).join(',')}}`
    : JSON.stringify(v ?? null)
const recordHash = (item: ImportedQuestion) => cyrb53(canonicalJson(item))
const authorsOf = (c: Candidate) => new Set(c.versions.map((v) => person(v.item.author)))
const clone = <T,>(x: T): T => JSON.parse(JSON.stringify(x))

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
  /** Not recorded as a new version, with why. */
  refused: { import_id: string; reason: string }[]
}

/**
 * Records a validated batch. Call validateImport first and pass only items with no problems; this does not re-check
 * shape or rights. `bankKeys`: questionKey → id for every question already in the app's bank (fixtures, later hosted);
 * required, so a caller can't skip the bank by forgetting it. Returns a new registry; neither input is changed.
 */
export function intake(reg: Registry, items: ImportedQuestion[], batch: string, at: string, bankKeys: Map<string, string>): { registry: Registry; result: IntakeResult } {
  const next: Registry = clone(reg)
  const result: IntakeResult = { received: [], revised: [], unchanged: [], retired: [], refused: [] }
  const bankIds = new Set(bankKeys.values())
  // Every question any candidate has ever been (every version, retired candidates included), plus the bank.
  const owner = new Map<string, string>()
  for (const [k, id] of bankKeys) owner.set(k, `bank:${id}`)
  // The bank first, then live candidates, then retired ones: a question is attributed to its live owner, never to a
  // retired duplicate of it (whatever order the registry lists them in).
  const byLiveness = Object.values(next.candidates).sort((a, b) => Number(isRetired(a)) - Number(isRetired(b)))
  for (const c of byLiveness) for (const v of c.versions) if (!owner.has(questionKey(v.item))) owner.set(questionKey(v.item), c.import_id)

  for (const raw of items) {
    const item = clone(raw)
    const id = item.import_id
    const hash = contentHash({ id, ...item } as unknown as FixtureQuestion)
    const rec = recordHash(item)
    const key = questionKey(item)
    const existing = next.candidates[id]
    const refuse = (c: Candidate | undefined, reason: string, short = reason) => {
      c?.history.push({ at, event: 'refused', batch, reason })
      result.refused.push({ import_id: id, reason: short })
    }

    if (bankIds.has(id)) {
      refuse(undefined, `import_id ${id} is already the id of a bank question; use another id`, 'import_id is a bank id')
      continue
    }

    if (existing) {
      const cur = latest(existing)
      if (cur.record_hash === rec) {
        existing.history.push({ at, event: 'unchanged_resubmission', batch, content_hash: hash })
        result.unchanged.push(id)
        continue
      }
      if (existing.status === 'retired' || existing.history.some((h) => h.event === 'retired')) {
        refuse(existing, 'a retired candidate is not revised; a genuinely different question needs a new import_id', 'retired')
        continue
      }
      const earlier = existing.versions.find((v) => v.content_hash === hash && v.content_hash !== cur.content_hash)
      if (earlier) {
        refuse(existing, `returns to the content of version ${earlier.version}; earlier reviews must not revive, so change the item or submit it under a new import_id`, `reverts to version ${earlier.version}`)
        continue
      }
      const other = owner.get(key)
      if (other && other !== id) {
        refuse(existing, `this revision duplicates ${other}`, `revision duplicates ${other}`)
        continue
      }
      const contentChanged = cur.content_hash !== hash
      existing.versions.push({ version: cur.version + 1, content_hash: hash, record_hash: rec, batch, received: at, item })
      existing.history.push({
        at, event: 'revised', version: cur.version + 1, batch, content_hash: hash, previous_hash: cur.content_hash,
        key_carried: contentChanged && JSON.stringify(cur.item.accepted_answers) === JSON.stringify(item.accepted_answers),
        content_changed: contentChanged,
        rights_changed: RIGHTS_FIELDS.some((f) => JSON.stringify(cur.item[f] ?? null) !== JSON.stringify(item[f] ?? null)),
      })
      if (!owner.has(key)) owner.set(key, id)
      result.revised.push(id)
      continue
    }

    const dup = owner.get(key)
    const c: Candidate = {
      import_id: id,
      track: trackOf(item.requested_pool),
      track_confirmed_by: null,
      status: dup ? 'retired' : 'draft',
      versions: [{ version: 1, content_hash: hash, record_hash: rec, batch, received: at, item }],
      history: [{ at, event: 'received', version: 1, batch, content_hash: hash }],
    }
    if (dup) {
      c.duplicate_of = dup
      c.history.push({ at, event: 'retired', reason: 'duplicate', duplicate_of: dup, by: 'intake' })
      result.retired.push({ import_id: id, duplicate_of: dup })
    } else {
      owner.set(key, id)
      result.received.push(id)
    }
    next.candidates[id] = c
  }
  return { registry: next, result }
}

function isRetired(c: Candidate) {
  return c.status === 'retired' || c.history.some((h) => h.event === 'retired')
}
const lastTrackSet = (c: Candidate) => c.history.filter((h): h is Extract<HistoryEvent, { event: 'track_set' }> => h.event === 'track_set').pop()

/**
 * The content lead confirms or changes a track. `exposed`: ids any student has seen in practice (from the database
 * once hosted is back; pass an empty set explicitly when there is none). Throws when the move is not allowed.
 */
export function setTrack(reg: Registry, id: string, track: Track, by: string, reason: string, at: string, exposed: Set<string>): Registry {
  const c = reg.candidates[id]
  if (!c) throw new Error(`no candidate ${id}`)
  if (isRetired(c)) throw new Error(`${id} is retired`)
  if (isNotAPerson(by)) throw new Error(`"${by}" is not a named person; only the content lead sets a track`)
  if (!reason.trim()) throw new Error('a reason is required')
  if (authorsOf(c).has(person(by))) throw new Error(`${by} wrote this item and can't set its track`)
  if (track === 'assessment_candidate') {
    if (c.history.some((h) => h.event === 'track_set' && h.track === 'practice_candidate')) throw new Error(`${id} was confirmed for practice; a practice item never becomes a reserved assessment item`)
    if (exposed.has(id)) throw new Error(`${id} has been seen in practice and can't be reserved`)
  }
  const next: Registry = clone(reg)
  const n = next.candidates[id]!
  n.track = track
  n.track_confirmed_by = by.trim()
  n.history.push({ at, event: 'track_set', track, by: by.trim(), reason: reason.trim() })
  return next
}

/** Retires a candidate (kept, never deleted). `duplicateOf`: another candidate's id or `bank:<id>`. */
export function retire(reg: Registry, id: string, by: string, reason: string, at: string, duplicateOf?: string): Registry {
  const c = reg.candidates[id]
  if (!c) throw new Error(`no candidate ${id}`)
  if (isRetired(c)) throw new Error(`${id} is already retired`)
  if (isNotAPerson(by)) throw new Error(`"${by}" is not a named person`)
  if (!reason.trim()) throw new Error('a reason is required')
  if (duplicateOf && !(duplicateOf.startsWith('bank:') || (reg.candidates[duplicateOf] && duplicateOf !== id))) throw new Error(`${duplicateOf} is not another candidate or a bank:<id>`)
  const next: Registry = clone(reg)
  const n = next.candidates[id]!
  n.status = 'retired'
  if (duplicateOf) n.duplicate_of = duplicateOf
  n.history.push({ at, event: 'retired', reason: reason.trim(), by: by.trim(), ...(duplicateOf ? { duplicate_of: duplicateOf } : {}) })
  return next
}

/**
 * The answer key for one exact content. Throws unless `hash` is a version's content hash, so a key can never be
 * attached to different (revised or stale) content. `verified` is true only when two blind solves of exactly this
 * content, by different people who never authored any version, matched it.
 */
export function answerKeyFor(c: Candidate, hash: string, ledger: Ledger = EDITORIAL_LEDGER): { version: number; accepted_answers: string[]; verified: boolean; carried_from?: number } {
  const v = c.versions.filter((x) => x.content_hash === hash).pop()
  if (!v) throw new Error(`${c.import_id}: no version has content ${hash}; a key is never attached to other content`)
  const authors = authorsOf(c)
  const keys = v.item.accepted_answers.map((a) => a.trim().toLowerCase())
  const solvers = new Set(
    (ledger.items[c.import_id]?.signoffs ?? [])
      .filter((s) => s.stage === 4 && s.result === 'pass' && s.hash === hash && !isNotAPerson(s.by) && !authors.has(person(s.by)))
      .filter((s) => keys.includes((s.answer ?? '').trim().toLowerCase()))
      .map((s) => person(s.by)),
  )
  const prev = c.versions.filter((x) => x.version < v.version && x.content_hash !== hash && JSON.stringify(x.item.accepted_answers) === JSON.stringify(v.item.accepted_answers)).pop()
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
 * Whether one candidate may be published, judged on its latest version alone and from its history. Every condition
 * must hold for this item individually; nothing about other items (a sample, a batch pass rate) changes the answer.
 */
export function eligibility(c: Candidate, ledger: Ledger = EDITORIAL_LEDGER): Eligibility {
  const v = latest(c)
  const q = asQuestion(v, c.import_id)
  const problems: string[] = []
  const authors = authorsOf(c)
  if (isRetired(c)) problems.push(c.duplicate_of ? `retired: duplicates ${c.duplicate_of}` : 'retired')

  // The track counts only as the history records it: the last confirmation, by a named person who wrote no version.
  const t = lastTrackSet(c)
  if (!t) problems.push('track is only the workstream’s request; the content lead has not confirmed it')
  else {
    if (t.track !== c.track) problems.push(`track ${c.track} doesn't match the last confirmation (${t.track})`)
    if (isNotAPerson(t.by)) problems.push(`track confirmed by "${t.by}", who is not a named person`)
    if (authors.has(person(t.by))) problems.push(`track confirmed by ${t.by}, who wrote a version of this item`)
  }

  // The ledger's author is the import's author (not the AI default), so the author can't approve their own item.
  const entry = ledger.items[c.import_id]
  if (entry && entry.author !== AI_AUTHOR && person(entry.author) !== person(v.item.author)) problems.push(`ledger author "${entry.author}" differs from the import author "${v.item.author}"`)
  const signoffs = entry?.signoffs ?? []
  const st = editorialState(q, { items: { [c.import_id]: { author: v.item.author, signoffs } } })
  if (!st.humanApproved) problems.push(...st.problems, `editorial review is at stage ${st.next}`)

  // A change to the rights basis or author keeps the content hash, so the rights check must be signed again after it.
  const rightsChange = c.history.filter((h) => h.event === 'revised' && h.rights_changed).pop()
  if (rightsChange && !signoffs.some((s) => s.stage === 3 && s.result === 'pass' && s.hash === v.content_hash && !isNotAPerson(s.by) && isIsoDate(s.date) && s.date > rightsChange.at))
    problems.push(`rights or authorship changed on ${rightsChange.at}; stage 3 must be signed again, dated the next day or later`)

  // Anyone who wrote any version is not independent: their solve isn't blind, and they can't pass stages 6 or 8.
  const own = signoffs.filter((s) => s.hash === v.content_hash && [4, 6, 8].includes(s.stage) && authors.has(person(s.by)))
  if (own.length) problems.push(`sign-off(s) at stage ${[...new Set(own.map((s) => s.stage))].join(', ')} by an author of a version`)
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
    out[c.track][isRetired(c) ? 'retired' : 'draft']++
    out.versions += c.versions.length
    if (eligibility(c, ledger).eligible) out[c.track].eligible++
  }
  return out
}
