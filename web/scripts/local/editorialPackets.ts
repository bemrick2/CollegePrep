// Human editorial review (CONTENT_PLAN.md §5, QUESTION_REVIEW_WORKFLOW.md), offline. Writes, for the content lead:
//   status.csv                    one row per item: track, hashes, stage passed, next stage, problems
//   blind-<exam>-<section>.html   printable blind-solve packets: passage, stem and choices only; no key, hints or explanations
//   solves-template.csv           the sheet solvers fill in (two stage-4 rows per item)
//   signoffs-template.csv         stages 3 and 5-8 (stage 3 rows carry the rights version to sign)
//   review-<exam>-<section>.html  full items with key and explanations, for stages 3 and 5-7 (never give these to solvers)
//
//   npx vite-node scripts/local/editorialPackets.ts <out-dir> [--ids id1,id2,...] [--registry candidates.json]
//                                                   [--ledger editorialLedger.json] [--reviewers reviewers.json]
//
// Without --registry: the app's own bank. With --registry: an imported batch (the latest version of every candidate
// that isn't retired). --ids limits the files to a review batch; an unknown id is an error.
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { QUESTIONS } from '../../src/lib/data/demo/fixtures'
import { practiceExclusions } from '../../src/lib/engine/freshness'
import type { Ledger } from '../../src/lib/data/demo/editorialLedger'
import { registryProblems, type ReviewerRegistry } from '../../src/lib/data/demo/reviewerRegistry'
import { itemsFromBank, itemsFromRegistry, packetFiles, selectItems, stateOf } from '../../src/lib/editorialReview'
import type { Registry } from '../../src/lib/questionCandidates'
import { parseArgs } from './reviewArgs'

const usage = 'usage: editorialPackets.ts <out-dir> [--ids id1,id2,...] [--registry candidates.json] [--ledger path] [--reviewers path]'
const { positional, opts } = parseArgs(process.argv.slice(2), ['--ids', '--registry', '--ledger', '--reviewers'], usage)
if (positional.length !== 1) throw new Error(usage)
const out = positional[0]!
// The same ledger and reviewers the recorder uses, so status.csv agrees with what was recorded.
const ledger = JSON.parse(readFileSync(opts['--ledger'] ?? new URL('../../src/lib/data/demo/editorialLedger.json', import.meta.url).pathname, 'utf8')) as Ledger
const REVIEWERS = JSON.parse(readFileSync(opts['--reviewers'] ?? new URL('../../src/lib/data/demo/reviewers.json', import.meta.url).pathname, 'utf8')) as ReviewerRegistry
const bad = registryProblems(REVIEWERS)
if (bad.length) console.error(`The reviewer registry has problems, so status.csv shows no sign-off as counting:\n${bad.join('\n')}`)
const all = opts['--registry']
  ? itemsFromRegistry(JSON.parse(readFileSync(opts['--registry'], 'utf8')) as Registry)
  : itemsFromBank(QUESTIONS, new Set([...practiceExclusions('act', QUESTIONS), ...practiceExclusions('sat', QUESTIONS)]), ledger)
const items = selectItems(all, opts['--ids'] ? opts['--ids'].split(',').map((s) => s.trim()).filter(Boolean) : null)
const label = opts['--registry'] ? 'Imported batch' : 'App bank'
mkdirSync(out, { recursive: true })
for (const [name, text] of Object.entries(packetFiles(items, ledger, REVIEWERS, label))) writeFileSync(join(out, name), text)
console.log(`${label}: ${items.length} items; ${items.filter((i) => stateOf(i, ledger, REVIEWERS).humanApproved).length} human-approved`)
