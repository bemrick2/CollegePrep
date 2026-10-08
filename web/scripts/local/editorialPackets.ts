// Human editorial review (CONTENT_PLAN.md §5), offline. Writes, for the content lead:
//   status.csv              one row per item: stage passed, next stage, problems (the tracking sheet)
//   blind-<exam>-<section>.html  printable blind-solve packets: passage, stem and choices only; no key, hints or explanations
//   solves-template.csv     the sheet solvers fill in and recordEditorial.ts imports
//   review-<exam>-<section>.html full items with key and explanations, for stages 5-7 (never give these to solvers)
//
//   npx vite-node scripts/local/editorialPackets.ts <out-dir>
import { mkdirSync, writeFileSync } from 'node:fs'
import { QUESTIONS, type FixtureQuestion } from '../../src/lib/data/demo/fixtures'
import { contentHash } from '../../src/lib/data/demo/questionReview'
import { editorialState, STAGE_NAME } from '../../src/lib/data/demo/editorialLedger'

const out = process.argv[2]
if (!out) throw new Error('usage: editorialPackets.ts <out-dir>')
mkdirSync(out, { recursive: true })

const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]!)
const csv = (v: unknown) => `"${String(v ?? '').replace(/"/g, '""')}"`
const page = (title: string, body: string) => `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>${esc(title)}</title>
<style>body{font:15px/1.5 Georgia,serif;max-width:46rem;margin:2rem auto;padding:0 1rem;color:#111;background:#fff}
article{break-inside:avoid;border-top:1px solid #999;padding:1rem 0}h1{font-size:1.3rem}.id{font:12px monospace;color:#555}
.passage{white-space:pre-wrap;background:#f4f4f4;padding:.75rem}ul.choices{list-style:none;padding-left:0}.ans{margin-top:.5rem}
.key{color:#064;font-weight:bold}</style></head><body><h1>${esc(title)}</h1>${body}</body></html>`

const groups = new Map<string, FixtureQuestion[]>()
for (const q of QUESTIONS) groups.set(`${q.exam_family}-${q.section}`, [...(groups.get(`${q.exam_family}-${q.section}`) ?? []), q])

for (const [g, qs] of groups) {
  const blind = qs
    .map(
      (q) => `<article><div class="id">${esc(q.id)} · hash ${contentHash(q)}</div>
${q.passage ? `<div class="passage">${esc(q.passage)}</div>` : ''}<p>${esc(q.stem)}</p>
${q.answer_format === 'choice' ? `<ul class="choices">${q.choices.map((c) => `<li><b>${esc(c.key)}.</b> ${esc(c.text)}</li>`).join('')}</ul>` : '<p>(Enter a number.)</p>'}
<p class="ans">Your answer: ________ &nbsp; Time (seconds): ______</p></article>`,
    )
    .join('\n')
  writeFileSync(`${out}/blind-${g}.html`, page(`Blind solve: ${g} (${qs.length} items). No key, hints or explanations.`, blind))
  const full = qs
    .map(
      (q) => `<article><div class="id">${esc(q.id)} · difficulty ${q.difficulty} · skill ${esc(q.primary_skill_key)} · hash ${contentHash(q)}</div>
${q.passage ? `<div class="passage">${esc(q.passage)}</div>` : ''}<p>${esc(q.stem)}</p>
${q.answer_format === 'choice' ? `<ul class="choices">${q.choices.map((c) => `<li><b>${esc(c.key)}.</b> ${esc(c.text)}${q.accepted_answers.includes(c.key) ? ' <span class="key">(key)</span>' : ''}</li>`).join('')}</ul>` : `<p class="key">Accepted: ${esc(q.accepted_answers.join(', '))}</p>`}
<p><b>Explanation.</b> ${esc(q.teaching_explanation)}</p><p><b>Strategy.</b> ${esc(q.strategy_explanation)}</p>
<p><b>Hints.</b> ${q.hints.map(esc).join(' / ')}</p>
<ul>${q.distractors.map((d) => `<li>${esc(d.choice)}: ${esc(d.rationale)}</li>`).join('')}</ul></article>`,
    )
    .join('\n')
  writeFileSync(`${out}/review-${g}.html`, page(`Review copy: ${g}. Contains the key: not for blind solvers.`, full))
}

const rows = QUESTIONS.map((q) => {
  const s = editorialState(q)
  return [q.id, q.exam_family, q.section, q.difficulty, contentHash(q), `${s.passed} ${STAGE_NAME[s.passed]}`, s.next ? `${s.next} ${STAGE_NAME[s.next]}` : 'approved', s.problems.join('; ')]
})
writeFileSync(`${out}/status.csv`, [['id', 'exam', 'section', 'difficulty', 'hash', 'passed', 'next', 'problems'], ...rows].map((r) => r.map(csv).join(',')).join('\n') + '\n')
writeFileSync(
  `${out}/solves-template.csv`,
  [['id', 'stage', 'by', 'date', 'result', 'hash', 'answer', 'seconds', 'license', 'note'], ...QUESTIONS.map((q) => [q.id, 4, '', '', 'pass', contentHash(q), '', '', '', ''])].map((r) => r.map(csv).join(',')).join('\n') + '\n',
)
console.log(`${QUESTIONS.length} items, ${groups.size} packets; ${rows.filter((r) => r[6] === 'approved').length} human-approved`)
