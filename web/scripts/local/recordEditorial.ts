// Imports filled-in editorial sign-offs into the editorial ledger.
//
//   npx vite-node scripts/local/recordEditorial.ts <signoffs.csv> [more.csv ...] [--registry candidates.json]
//                                                  [--ledger editorialLedger.json] [--reviewers reviewers.json]
//
// Columns (header row required): id, stage, reviewer_id, by, date, result, hash, rights_hash, answer, seconds, license, note
// - reviewer_id must be an active reviewer authorized for the stage (reviewers.json); `by` is display only.
// - hash must be the content printed on the packet, and stage 3 rows of imported items the rights version printed.
// - result is exactly "pass" or "fail". A recorded fail is never removed by a later row.
// Without --registry the rows are for the app's own bank; with it, for that imported batch.
import { readFileSync, writeFileSync } from 'node:fs'
import { QUESTIONS } from '../../src/lib/data/demo/fixtures'
import { practiceExclusions } from '../../src/lib/engine/freshness'
import type { Ledger } from '../../src/lib/data/demo/editorialLedger'
import { registryProblems, type ReviewerRegistry } from '../../src/lib/data/demo/reviewerRegistry'
import { csvRows, itemsFromBank, itemsFromRegistry, recordSignoffs, stateOf } from '../../src/lib/editorialReview'
import type { Registry } from '../../src/lib/questionCandidates'
import { parseArgs } from './reviewArgs'

const usage = 'usage: recordEditorial.ts <signoffs.csv> [...] [--registry candidates.json] [--ledger path] [--reviewers path]'
const { positional: files, opts } = parseArgs(process.argv.slice(2), ['--registry', '--ledger', '--reviewers'], usage)
if (!files.length) throw new Error(usage)
const ledgerPath = opts['--ledger'] ?? new URL('../../src/lib/data/demo/editorialLedger.json', import.meta.url).pathname
const reviewersPath = opts['--reviewers'] ?? new URL('../../src/lib/data/demo/reviewers.json', import.meta.url).pathname
const ledger = JSON.parse(readFileSync(ledgerPath, 'utf8')) as Ledger
const reviewers = JSON.parse(readFileSync(reviewersPath, 'utf8')) as ReviewerRegistry
const bad = registryProblems(reviewers)
if (bad.length) throw new Error(`${reviewersPath} has problems; nothing recorded:\n${bad.join('\n')}`)
const items = opts['--registry']
  ? itemsFromRegistry(JSON.parse(readFileSync(opts['--registry'], 'utf8')) as Registry)
  : itemsFromBank(QUESTIONS, new Set([...practiceExclusions('act', QUESTIONS), ...practiceExclusions('sat', QUESTIONS)]), ledger)

let current = ledger
let added = 0
const refused: string[] = []
const today = new Date().toISOString().slice(0, 10)
for (const f of files) {
  const r = recordSignoffs(current, items, csvRows(readFileSync(f, 'utf8')), reviewers, today, f)
  current = r.ledger
  added += r.added
  refused.push(...r.refused)
}
writeFileSync(ledgerPath, JSON.stringify(current, null, 1) + '\n')
console.log(`${added} sign-offs recorded; ${items.filter((i) => stateOf(i, current, reviewers).humanApproved).length}/${items.length} items human-approved`)
if (refused.length) console.log(`Refused ${refused.length}:\n${refused.join('\n')}`)
