// Imports filled-in editorial sign-offs into src/lib/data/demo/editorialLedger.json.
//
//   npx vite-node scripts/local/recordEditorial.ts <signoffs.csv> [more.csv ...]
//
// CSV columns (header row required): id, stage, by, date, result, hash, answer, seconds, license, note
//   stage 2 rows record the item's author (by). Every row must carry the hash printed on the packet it was made
//   from; a row for content that has since changed is refused, so a sign-off can never attach to text nobody saw.
import { readFileSync, writeFileSync } from 'node:fs'
import { QUESTIONS } from '../../src/lib/data/demo/fixtures'
import { contentHash } from '../../src/lib/data/demo/questionReview'
import { EDITORIAL_LEDGER, editorialState, type Ledger, type SignOff, type Stage } from '../../src/lib/data/demo/editorialLedger'

const files = process.argv.slice(2)
if (!files.length) throw new Error('usage: recordEditorial.ts <signoffs.csv> [...]')

function parseCsv(text: string): string[][] {
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

const byId = new Map(QUESTIONS.map((q) => [q.id, q]))
const ledger: Ledger = JSON.parse(JSON.stringify(EDITORIAL_LEDGER))
const refused: string[] = []
let added = 0
for (const f of files) {
  const [head, ...rows] = parseCsv(readFileSync(f, 'utf8'))
  const col = (r: string[], name: string) => (r[head!.indexOf(name)] ?? '').trim()
  for (const r of rows) {
    const id = col(r, 'id')
    const q = byId.get(id)
    const stage = Number(col(r, 'stage')) as Stage
    const by = col(r, 'by')
    if (!q) { refused.push(`${f}: unknown item ${id}`); continue }
    if (![2, 3, 4, 5, 6, 7, 8].includes(stage)) { refused.push(`${id}: bad stage ${col(r, 'stage')}`); continue }
    if (!by) continue // a blank template row
    if (col(r, 'hash') !== contentHash(q)) { refused.push(`${id}: hash ${col(r, 'hash')} is not the current content (${contentHash(q)}); re-issue the packet`); continue }
    const entry = (ledger.items[id] ??= { author: 'AI (Claude)', signoffs: [] })
    if (stage === 2) { entry.author = by; continue }
    const s: SignOff = { stage, by, date: col(r, 'date') || new Date().toISOString().slice(0, 10), result: col(r, 'result') === 'fail' ? 'fail' : 'pass', hash: contentHash(q) }
    if (col(r, 'answer')) s.answer = col(r, 'answer')
    if (col(r, 'seconds')) s.seconds = Number(col(r, 'seconds'))
    if (col(r, 'license')) s.license = col(r, 'license')
    if (col(r, 'note')) s.note = col(r, 'note')
    // One sign-off per person per stage: a newer one replaces theirs.
    entry.signoffs = [...entry.signoffs.filter((x) => !(x.stage === stage && x.by.trim().toLowerCase() === by.toLowerCase() && x.hash === s.hash)), s]
    added++
  }
}
writeFileSync(new URL('../../src/lib/data/demo/editorialLedger.json', import.meta.url), JSON.stringify(ledger, null, 1) + '\n')
const approved = QUESTIONS.filter((q) => editorialState(q, ledger).humanApproved).length
console.log(`${added} sign-offs recorded; ${approved}/${QUESTIONS.length} items human-approved`)
if (refused.length) console.log(`Refused ${refused.length}:\n${refused.join('\n')}`)
