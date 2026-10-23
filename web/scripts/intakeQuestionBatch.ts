// Record a validated question-bank batch as candidates (docs/product/QUESTION_REVIEW_WORKFLOW.md), LOCALLY.
//
//   npx vite-node scripts/intakeQuestionBatch.ts <batch.jsonl> --registry <candidates.json> [--write]
//
// 1. Runs the import validator (QUESTION_IMPORT_CONTRACT.md). Any problem stops the whole batch: nothing is recorded.
// 2. Records each item as a draft candidate on its requested track (unconfirmed), a new version of an existing
//    candidate, or a retired duplicate (of the app's bank or of an earlier bank). Nothing is deleted.
// Without --write this is a dry run and changes no file. It never publishes, imports to a database or approves anything.
import { existsSync, readFileSync, writeFileSync } from 'node:fs'
import { basename } from 'node:path'
import { QUESTIONS, SKILLS } from '../src/lib/data/demo/fixtures'
import { questionKey, validateImport, type ImportedQuestion } from '../src/lib/questionImport'
import { emptyRegistry, intake, summary, type Registry } from '../src/lib/questionCandidates'

const args = process.argv.slice(2)
const batch = args[0]
const regPath = args[args.indexOf('--registry') + 1]
const write = args.includes('--write')
if (!batch || args.indexOf('--registry') < 0 || !regPath || regPath.startsWith('--')) {
  console.error('usage: intakeQuestionBatch.ts <batch.jsonl> --registry <candidates.json> [--write]')
  process.exit(2)
}

const items: unknown[] = []
let bad = 0
readFileSync(batch, 'utf8').split('\n').forEach((l, i) => {
  if (!l.trim()) return
  try {
    items.push(JSON.parse(l))
  } catch {
    console.log(`line ${i + 1}\tjson\tnot valid JSON`)
    bad++
  }
})
// Duplicates of the app's bank and of earlier batches are recorded as retired by intake, not refused here, so the
// validator checks only within this batch.
const problems = validateImport(items, SKILLS)
for (const p of problems) console.log(`${p.import_id}\t${p.field}\t${p.problem}`)
if (problems.length || bad) {
  console.error(`${items.length} items read; ${problems.length + bad} problems. Nothing recorded: fix or return the batch.`)
  process.exit(1)
}

const reg: Registry = existsSync(regPath) ? JSON.parse(readFileSync(regPath, 'utf8')) : emptyRegistry()
if (reg.contract !== 'question_candidates/v1') throw new Error(`${regPath} is not a question_candidates/v1 registry`)
const bank = new Map(QUESTIONS.map((q) => [questionKey(q), q.id]))
const { registry, result } = intake(reg, items as ImportedQuestion[], basename(batch), new Date().toISOString().slice(0, 10), bank)

console.log(`received ${result.received.length}, revised ${result.revised.length}, unchanged ${result.unchanged.length}, retired as duplicates ${result.retired.length}, refused ${result.refused.length}`)
for (const r of result.retired) console.log(`retired\t${r.import_id}\tduplicates ${r.duplicate_of}`)
for (const r of result.refused) console.log(`refused\t${r.import_id}\t${r.reason}`)
console.log(JSON.stringify(summary(registry)))
if (write) {
  writeFileSync(regPath, JSON.stringify(registry, null, 2) + '\n')
  console.error(`wrote ${regPath}. Every candidate is a draft: tracks need the content lead, and publication needs stages 3–8 per item.`)
} else console.error('dry run: nothing written (add --write)')
