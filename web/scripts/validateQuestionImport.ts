// Validate a question-bank import batch (docs/product/QUESTION_IMPORT_CONTRACT.md) before it enters review.
// Usage: npx vite-node scripts/validateQuestionImport.ts <batch.jsonl>
// Exit 0: every item is a well-formed draft for stage 3. Exit 1: problems, one per line. Nothing is published,
// imported or written; this only reads the file.
import { readFileSync } from 'node:fs'
import { QUESTIONS, SKILLS } from '../src/lib/data/demo/fixtures'
import { questionKey, validateImport } from '../src/lib/questionImport'

const path = process.argv[2]
if (!path) {
  console.error('usage: validateQuestionImport.ts <batch.jsonl>')
  process.exit(2)
}
const lines = readFileSync(path, 'utf8').split('\n').filter((l) => l.trim())
const items: unknown[] = []
let parseErrors = 0
lines.forEach((l, i) => {
  try {
    items.push(JSON.parse(l))
  } catch {
    console.log(`line ${i + 1}\tjson\tnot valid JSON`)
    parseErrors++
  }
})
const problems = validateImport(items, new Set(SKILLS.map((s) => s.skill_key)), new Set(QUESTIONS.map(questionKey)))
for (const p of problems) console.log(`${p.import_id}\t${p.field}\t${p.problem}`)
console.error(`${items.length} items read; ${problems.length + parseErrors} problems. Passing items are drafts only: review stages 3–8 and the rights gate decide publication.`)
process.exit(problems.length + parseErrors ? 1 : 0)
