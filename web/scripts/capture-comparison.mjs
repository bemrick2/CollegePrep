#!/usr/bin/env node
// Capture verified comparison records from the live backend for an acceptance scenario.
//
//   VITE_SUPABASE_URL=… VITE_SUPABASE_PUBLISHABLE_KEY=… \
//     node scripts/capture-comparison.mjs --name tn-or --year 2026-27 --states TN,OR
//
// Uses only the public, verified-only RPCs (institutions_with_verified_records, compare_institutions) with the
// publishable key. Never use a service-role key here. Writes src/acceptance/fixtures/<name>.json in the same
// shape as the demo snapshot, so the acceptance test can run the real UI against real records.
import { writeFileSync } from 'node:fs'

const arg = (k, d) => {
  const i = process.argv.indexOf(`--${k}`)
  return i > 0 ? process.argv[i + 1] : d
}
const url = process.env.VITE_SUPABASE_URL
const key = process.env.VITE_SUPABASE_PUBLISHABLE_KEY
if (!url || !key) {
  console.error('Set VITE_SUPABASE_URL and VITE_SUPABASE_PUBLISHABLE_KEY (publishable key only).')
  process.exit(1)
}
const name = arg('name', 'scenario')
const year = arg('year', '2026-27')
const states = arg('states', '').split(',').filter(Boolean)
const explicit = arg('keys', '').split(',').filter(Boolean)

async function rpc(fn, body) {
  const r = await fetch(`${url}/rest/v1/rpc/${fn}`, {
    method: 'POST',
    headers: { apikey: key, Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })
  if (!r.ok) throw new Error(`${fn}: ${r.status} ${await r.text()}`)
  return r.json()
}

let keys = explicit
for (const st of states) {
  const hits = await rpc('institutions_with_verified_records', { p_academic_year: year, p_state: st })
  keys.push(...hits.map((h) => h.institution_key))
}
keys = [...new Set(keys)]
const institutions = []
for (let i = 0; i < keys.length; i += 25) {
  const r = await rpc('compare_institutions', { p_institution_keys: keys.slice(i, i + 25), p_academic_year: year })
  institutions.push(...r.institutions)
}
const out = { academic_year: year, captured_at: new Date().toISOString().slice(0, 10), source: `compare_institutions RPC (${states.join(',') || 'explicit keys'})`, institutions }
const file = new URL(`../src/acceptance/fixtures/${name}.json`, import.meta.url)
writeFileSync(file, JSON.stringify(out))
console.log(`Wrote ${institutions.length} institutions to ${file.pathname}`)
