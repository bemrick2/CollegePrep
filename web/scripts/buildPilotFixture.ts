import { writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { buildPilotFixture } from './pilotFixture'

const out = join(__dirname, '../src/features/planning/pilotFixture.json')
const f = buildPilotFixture()
writeFileSync(out, JSON.stringify(f, null, 1) + '\n')
console.log(f.schools.map((s) => `${s.institution_key}: ${s.domains.academic_programs.length} programs, ${s.domains.degree_requirements.length} requirements`).join('\n'))
