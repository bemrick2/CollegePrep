// Exports the demo question bank for content review: blind (no key, no explanations) and full.
//   npx vite-node scripts/local/exportQuestions.ts <out-dir>
import { writeFileSync } from 'node:fs'
import { QUESTIONS } from '../../src/lib/data/demo/fixtures'

const out = process.argv[2] ?? '.'
const blind = QUESTIONS.map((q) => ({ id: q.id, exam: q.exam_family, section: q.section, passage: q.passage ?? null, stem: q.stem, choices: q.choices, answer_format: q.answer_format }))
writeFileSync(`${out}/blind.json`, JSON.stringify(blind, null, 1))
writeFileSync(`${out}/full.json`, JSON.stringify(QUESTIONS, null, 1))
console.log(`${QUESTIONS.length} questions`)
