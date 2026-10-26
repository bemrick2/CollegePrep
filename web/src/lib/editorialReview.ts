/**
 * Review packets and sign-off recording for the human editorial review (docs/product/QUESTION_REVIEW_WORKFLOW.md),
 * for both the app's own bank and imported candidate batches (questionCandidates.ts).
 *
 * Pure functions: the scripts in web/scripts/local/ read and write the files. Nothing here approves, publishes or
 * imports anything; it prepares paper for people and records what they signed, under every rule the ledger enforces.
 */
import type { FixtureQuestion } from './data/demo/fixtures'
import { contentHash } from './data/demo/questionReview'
import { AI_AUTHOR, editorialState, isIsoDate, ledgerAuthors, ledgerAuthorship, STAGE_NAME, type Ledger, type SignOff, type Stage } from './data/demo/editorialLedger'
import { AI_MODEL, IDENTITIES, type AuthorIdentity, type IdentityRegistry, type ResolvedAuthors } from './data/demo/authorIdentity'
import { authorized, isAuthor, registryProblems, STAGE_ROLE, type ReviewerRegistry } from './data/demo/reviewerRegistry'
import { asQuestion, authorshipOf, latest, rightsHash, sameClaimsHashes, type Registry, type Track } from './questionCandidates'

export interface ReviewItem {
  id: string
  question: FixtureQuestion
  track: Track
  content_hash: string
  /** Imported items only: the rights version a stage-3 check must sign. */
  rights_hash?: string
  /** Imported items only: rights versions with the same claims (a stage-3 fail on any of them still blocks). */
  same_claims?: string[]
  /** Every author name of the item (all versions); the AI default for the app's bank. */
  authors: string[]
  /** The authors resolved to identities (an AI model or a recorded person), with any linked reviewer ids. */
  authorship: ResolvedAuthors
  source: 'bank' | 'import'
  /** Imported items: the batch the current version came from. */
  batch?: string
}

/** The app's own bank. `reserved`: ids currently set aside for checks. */
export function itemsFromBank(questions: FixtureQuestion[], reserved: Set<string>, ledger: Ledger, identities: IdentityRegistry = IDENTITIES, reviewers?: ReviewerRegistry): ReviewItem[] {
  return questions.map((q) => ({
    id: q.id,
    question: q,
    track: reserved.has(q.id) ? 'assessment_candidate' : 'practice_candidate',
    content_hash: contentHash(q),
    authors: ledgerAuthors(ledger.items[q.id]),
    authorship: ledgerAuthorship(ledger.items[q.id], identities, reviewers),
    source: 'bank',
  }))
}

/** An imported batch: the latest version of every candidate that isn't retired. Retired candidates are never reviewed. */
export function itemsFromRegistry(reg: Registry, identities: IdentityRegistry = IDENTITIES, reviewers?: ReviewerRegistry): ReviewItem[] {
  return Object.values(reg.candidates)
    .filter((c) => c.status !== 'retired' && !c.history.some((h) => h.event === 'retired'))
    .map((c) => {
      const v = latest(c)
      return {
        id: c.import_id,
        question: asQuestion(v, c.import_id),
        track: c.track,
        content_hash: v.content_hash,
        rights_hash: rightsHash(v),
        same_claims: sameClaimsHashes(c, v),
        authors: [...new Set(c.versions.map((x) => x.item.author))],
        authorship: authorshipOf(c, identities, reviewers),
        source: 'import' as const,
        batch: v.batch,
      }
    })
}

/** Restricts items to `ids`. Throws on an unknown or empty list, so a typo never widens a batch to everything. */
export function selectItems(items: ReviewItem[], ids: string[] | null): ReviewItem[] {
  if (!ids) return items
  const known = new Set(items.map((i) => i.id))
  const unknown = ids.filter((id) => !known.has(id))
  if (!ids.length || unknown.length) throw new Error(`unknown or missing ids: ${unknown.join(', ') || '(none given)'}`)
  return items.filter((i) => ids.includes(i.id))
}

export const stateOf = (item: ReviewItem, ledger: Ledger, reviewers: ReviewerRegistry) =>
  editorialState(item.question, ledger, {
    reviewers,
    authors: item.authors,
    // Imports: authorship from the import; the bank: from the ledger as it stands now (stage 2 may have added authors).
    ...(item.source === 'import' ? { authorship: item.authorship } : {}),
    ...(item.rights_hash ? { rightsHash: item.rights_hash, sameClaims: item.same_claims ?? [] } : {}),
  })

// --- packets -------------------------------------------------------------------------------------------------------

const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]!)
const csv = (v: unknown) => `"${String(v ?? '').replace(/"/g, '""')}"`
const table = (rows: unknown[][]) => rows.map((r) => r.map(csv).join(',')).join('\n') + '\n'
const page = (title: string, body: string) => `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>${esc(title)}</title>
<style>body{font:15px/1.5 Georgia,serif;max-width:46rem;margin:2rem auto;padding:0 1rem;color:#111;background:#fff}
article{break-inside:avoid;border-top:1px solid #999;padding:1rem 0}h1{font-size:1.3rem}.id{font:12px monospace;color:#555}
.passage{white-space:pre-wrap;background:#f4f4f4;padding:.75rem}ul.choices{list-style:none;padding-left:0}.ans{margin-top:.5rem}
.key{color:#064;font-weight:bold}</style></head><body><h1>${esc(title)}</h1>${body}</body></html>`

export const SIGNOFF_COLUMNS = ['id', 'stage', 'reviewer_id', 'by', 'date', 'result', 'hash', 'rights_hash', 'answer', 'seconds', 'license', 'note', 'author_identity'] as const

/** Every packet file, by file name. Blind packets carry no key, hints or explanations. */
export function packetFiles(items: ReviewItem[], ledger: Ledger, reviewers: ReviewerRegistry, label: string): Record<string, string> {
  const files: Record<string, string> = {}
  const groups = new Map<string, ReviewItem[]>()
  for (const i of items) groups.set(`${i.question.exam_family}-${i.question.section}`, [...(groups.get(`${i.question.exam_family}-${i.question.section}`) ?? []), i])
  for (const [g, list] of groups) {
    const blind = list
      .map(({ question: q, content_hash }) => `<article><div class="id">${esc(q.id)} · hash ${content_hash}</div>
${q.passage ? `<div class="passage">${esc(q.passage)}</div>` : ''}<p>${esc(q.stem)}</p>
${q.answer_format === 'choice' ? `<ul class="choices">${q.choices.map((c) => `<li><b>${esc(c.key)}.</b> ${esc(c.text)}</li>`).join('')}</ul>` : '<p>(Enter a number.)</p>'}
<p class="ans">Your answer: ________ &nbsp; Time (seconds): ______</p></article>`)
      .join('\n')
    files[`blind-${g}.html`] = page(`${label} blind solve: ${g} (${list.length} items). No key, hints or explanations.`, blind)
    const full = list
      .map(({ question: q, content_hash, rights_hash, authors, source }) => `<article><div class="id">${esc(q.id)} · ${source} · difficulty ${q.difficulty} · skill ${esc(q.primary_skill_key)} · hash ${content_hash}${rights_hash ? ` · rights ${rights_hash}` : ''} · author ${esc(authors.join(' / '))}</div>
${q.passage ? `<div class="passage">${esc(q.passage)}</div>` : ''}<p>${esc(q.stem)}</p>
${q.answer_format === 'choice' ? `<ul class="choices">${q.choices.map((c) => `<li><b>${esc(c.key)}.</b> ${esc(c.text)}${q.accepted_answers.includes(c.key) ? ' <span class="key">(key)</span>' : ''}</li>`).join('')}</ul>` : `<p class="key">Accepted: ${esc(q.accepted_answers.join(', '))}</p>`}
<p><b>Explanation.</b> ${esc(q.teaching_explanation)}</p><p><b>Strategy.</b> ${esc(q.strategy_explanation)}</p>
<p><b>Hints.</b> ${q.hints.map(esc).join(' / ')}</p>
<ul>${q.distractors.map((d) => `<li>${esc(d.choice)}: ${esc(d.rationale)}</li>`).join('')}</ul></article>`)
      .join('\n')
    files[`review-${g}.html`] = page(`${label} review copy: ${g}. Contains the key: not for blind solvers.`, full)
  }
  files['status.csv'] = table([
    ['id', 'source', 'batch', 'exam', 'section', 'difficulty', 'track', 'hash', 'rights_hash', 'authors_resolved', 'passed', 'next', 'problems'],
    ...items.map((i) => {
      const s = stateOf(i, ledger, reviewers)
      return [i.id, i.source, i.batch ?? '', i.question.exam_family, i.question.section, i.question.difficulty, i.track, i.content_hash, i.rights_hash ?? '', i.authorship.resolved ? 'yes' : 'no', `${s.passed} ${STAGE_NAME[s.passed]}`, s.next ? `${s.next} ${STAGE_NAME[s.next]}` : 'approved', s.problems.join('; ')]
    }),
  ])
  const row = (i: ReviewItem, stage: Stage) => [i.id, stage, '', '', '', '', i.content_hash, stage === 3 ? (i.rights_hash ?? '') : '', '', '', '', '', '']
  files['solves-template.csv'] = table([[...SIGNOFF_COLUMNS], ...items.flatMap((i) => [row(i, 4), row(i, 4)])])
  files['signoffs-template.csv'] = table([[...SIGNOFF_COLUMNS], ...items.flatMap((i) => [row(i, 3), row(i, 5), row(i, 6), row(i, 7), row(i, 8)])])
  return files
}

// --- recording -----------------------------------------------------------------------------------------------------

export function parseCsv(text: string): string[][] {
  const rows: string[][] = []
  let row: string[] = []
  let cell = ''
  let quoted = false
  for (let i = 0; i < text.length; i++) {
    const ch = text[i]!
    if (quoted) {
      if (ch === '"' && text[i + 1] === '"') (cell += '"'), i++
      else if (ch === '"') quoted = false
      else cell += ch
    } else if (ch === '"') quoted = true
    else if (ch === ',') row.push(cell), (cell = '')
    else if (ch === '\n' || ch === '\r') {
      if (ch === '\r' && text[i + 1] === '\n') i++
      row.push(cell), rows.push(row), (row = []), (cell = '')
    } else cell += ch
  }
  if (cell || row.length) row.push(cell), rows.push(row)
  return rows.filter((r) => r.some((c) => c.trim()))
}

/** CSV text → rows keyed by header. */
export function csvRows(text: string): Record<string, string>[] {
  const [head, ...rows] = parseCsv(text)
  if (!head) return []
  return rows.map((r) => Object.fromEntries(head.map((h, i) => [h.trim(), (r[i] ?? '').trim()])))
}

export interface RecordResult {
  ledger: Ledger
  added: number
  refused: string[]
}

/**
 * Records filled-in sign-off rows. Returns a new ledger; the input isn't changed. A row is refused, never guessed at,
 * when its item, stage, reviewer, role, hash, rights version, date, result or seconds isn't exactly right. The
 * recordEditorial script writes nothing when any row is refused.
 *
 * A PASS needs an active reviewer authorized for the stage who isn't an author (stages 4, 6, 8). A FAIL can only
 * block, so it is recorded from anyone with a reviewer id or a name, as long as it names the current content.
 * A newer row from the same reviewer for the same stage and content (and, at stage 3, rights version) replaces that
 * reviewer's earlier PASS. A recorded FAIL is never removed or replaced by any later row: it stands until the item is
 * revised.
 *
 * Stage 2 (app bank only) adds an author. It needs an active content lead who isn't an author, and the current hash;
 * authors are append-only, so every author ever recorded stays excluded from stages 4, 6 and 8.
 */
export function recordSignoffs(ledger: Ledger, items: ReviewItem[], rows: Record<string, string>[], reviewers: ReviewerRegistry, today: string, where = 'sheet', identities: IdentityRegistry = IDENTITIES): RecordResult {
  const next: Ledger = JSON.parse(JSON.stringify(ledger))
  const byId = new Map(items.map((i) => [i.id, i]))
  const refused: string[] = []
  let added = 0
  const tomorrow = new Date(Date.parse(`${today}T00:00:00Z`) + 86400000).toISOString().slice(0, 10)
  const registryBad = registryProblems(reviewers)
  const FILLABLE = ['reviewer_id', 'by', 'date', 'result', 'answer', 'seconds', 'license', 'note', 'author_identity'] as const
  rows.forEach((r, n) => {
    const at = `${where} row ${n + 2}`
    const id = r.id ?? ''
    const item = byId.get(id)
    const stageRaw = r.stage ?? ''
    const stage = Number(stageRaw) as Stage
    const reviewerId = r.reviewer_id ?? ''
    const refuse = (why: string) => refused.push(`${at} (${id || 'no id'}): ${why}`)
    if (!item) return refuse('unknown item, or not in this batch')
    if (![2, 3, 4, 5, 6, 7, 8].includes(stage) || !/^[2-8]$/.test(stageRaw)) return refuse(`bad stage "${stageRaw}"`)
    if (FILLABLE.every((k) => !(r[k] ?? '').trim())) return // an unfilled template row
    if (registryBad.length) return refuse(`the reviewer registry has problems; nothing can be recorded: ${registryBad[0]}`)
    if (r.hash !== item.content_hash) return refuse(`hash ${r.hash || '(blank)'} is not the current content (${item.content_hash}); re-issue the packet`)
    const date = r.date || today
    if (!isIsoDate(date) || date > tomorrow) return refuse(`date "${date}" must be YYYY-MM-DD and not in the future`)
    // Authors as of this row: the item's, plus any recorded earlier in this same run (stage 2 is append-only).
    const nowAuthorship = item.source === 'import' ? item.authorship : ledgerAuthorship(next.items[id], identities, reviewers)
    const authorsNow = [...new Set([...item.authors, ...(next.items[id] ? ledgerAuthors(next.items[id]) : []), ...nowAuthorship.names])]
    /** An author by linked reviewer id, or (fail-closed) by any recorded name. */
    const isAnAuthor = (rv: Parameters<typeof isAuthor>[0]) => nowAuthorship.reviewerIds.includes(rv.id) || item.authorship.reviewerIds.includes(rv.id) || isAuthor(rv, authorsNow)

    if (stage === 2) {
      // Authorship: for an imported item it comes from the import itself and isn't changed here.
      if (item.source === 'import') return refuse('an imported item’s author comes from the import, not the sign-off sheet')
      // The author is recorded by identity: "au-…" (identities.json) or "ai:<model>". A name alone is never an identity.
      const raw = (r.author_identity ?? r.note ?? '').trim()
      let identity: AuthorIdentity
      let name: string
      if (/^ai:/.test(raw)) {
        const model = raw.slice(3)
        if (!AI_MODEL.test(model)) return refuse('an AI author names its model, as "ai:<model>"')
        identity = { kind: 'ai', model }
        name = raw
      } else if (/^au-/.test(raw)) {
        const x = identities.identities?.[raw]
        if (!x) return refuse(`${raw} is not a recorded identity (identities.json); identities are recorded by the owner or a content lead`)
        identity = { kind: 'person', identity_id: raw }
        name = x.display_name
      } else return refuse('stage 2 rows give the author’s identity ("au-…" or "ai:<model>") in "author_identity" (or "note"); a name alone isn’t an identity')
      const lead = authorized(reviewers, reviewerId, 'content_lead')
      if (!lead) return refuse(`reviewer "${reviewerId}" is not an active content lead; only a content lead records authorship`)
      if (isAnAuthor(lead) || (identity.kind === 'person' && identities.identities[identity.identity_id]!.reviewer_id === lead.id)) return refuse(`${reviewerId} is an author of this item and can’t record its authorship`)
      const entry = (next.items[id] ??= { author: AI_AUTHOR, signoffs: [] })
      entry.authors = [...new Set([...ledgerAuthors(entry), name])]
      entry.author_records = [...(entry.author_records ?? []), { name, identity }]
      entry.author = name
      added++
      return
    }

    const result = (r.result ?? '').toLowerCase()
    if (result !== 'pass' && result !== 'fail') return refuse(`result must be "pass" or "fail", not "${r.result ?? ''}"`)
    if (stage === 3 && item.rights_hash && r.rights_hash !== item.rights_hash) return refuse(`rights_hash ${r.rights_hash || '(blank)'} is not the current rights version (${item.rights_hash}); re-issue the packet`)
    if (r.seconds && !/^\d+$/.test(r.seconds)) return refuse(`seconds must be a whole number, not "${r.seconds}"`)
    const role = STAGE_ROLE[stage as Exclude<Stage, 2>]
    const reviewer = authorized(reviewers, reviewerId, role)
    if (result === 'pass') {
      if (!reviewer) return refuse(`reviewer "${reviewerId}" is not an active reviewer authorized for ${role}`)
      if ([4, 6, 8].includes(stage) && isAnAuthor(reviewer)) return refuse(`${reviewerId} is an author of this item and can’t sign stage ${stage}`)
      if (stage === 4 && !r.answer) return refuse('a blind solve records the answer given')
    } else if (!reviewerId && !r.by) return refuse('a fail names who recorded it (reviewer_id or by)')
    const s: SignOff = { stage, reviewer_id: reviewer?.id ?? reviewerId, by: r.by || reviewer?.display_name || reviewerId, date, result, hash: item.content_hash }
    if (stage === 3 && item.rights_hash) s.rights_hash = item.rights_hash
    if (r.answer) s.answer = r.answer
    if (r.seconds) s.seconds = Number(r.seconds)
    if (r.license) s.license = r.license
    if (r.note) s.note = r.note
    const entry = (next.items[id] ??= { author: item.source === 'import' ? item.authors[item.authors.length - 1]! : AI_AUTHOR, signoffs: [] })
    const sameSlot = (x: SignOff) => x.stage === stage && x.reviewer_id === s.reviewer_id && x.hash === s.hash && (x.rights_hash ?? null) === (s.rights_hash ?? null)
    entry.signoffs = [...entry.signoffs.filter((x) => !(sameSlot(x) && x.result === 'pass')), s]
    added++
  })
  return { ledger: next, added, refused }
}
