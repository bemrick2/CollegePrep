import { readFileSync } from 'node:fs'
import { join } from 'node:path'
import { describe, expect, it } from 'vitest'
import { buildPilotFixture } from './pilotFixture'

describe('planning pilot demo data (#195)', () => {
  it('matches the stored records (rebuild with `npx vite-node scripts/buildPilotFixture.ts` when Research data changes)', () => {
    const stored = JSON.parse(readFileSync(join(__dirname, '../src/features/planning/pilotFixture.json'), 'utf8'))
    expect(stored).toEqual(JSON.parse(JSON.stringify(buildPilotFixture())))
  })
})
