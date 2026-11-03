// #296 / owner rule 2026-11-03: a per-semester price keeps its period end to end. It is never shown as a yearly price,
// never multiplied by years, and never used in a yearly comparison.
import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { App } from '../../App'
import { DemoSource, DEMO_STUDENT } from '../../lib/data/demo/demoSource'
import { emptyStore } from '../../lib/data/demo/store'
import bundled from '../../lib/data/demo/comparison-snapshot.json'
import type { InstitutionComparison } from '../../lib/data/types'
import { outlookFor } from '../parent/CostOutlook'

const snap = bundled as unknown as { academic_year: string; institutions: InstitutionComparison[] }
const base = snap.institutions.find((c) => c.found && ((c.domains.costs ?? []) as unknown[]).length > 0)!
const SEM = { residency: 'in_state', student_population: 'undergraduate', tuition: 9100, mandatory_fees: null, total_cost_of_attendance: 21000, cost_period: 'semester', verification_status: 'verified', source_url: 'https://example.edu/tuition', last_verified_at: '2026-11-01' }
const semesterOnly: InstitutionComparison = { ...base, domains: { ...base.domains, costs: [SEM] as never } }

describe('per-semester prices', () => {
  it('are never a yearly price in the cost outlook', () => {
    const o = outlookFor(semesterOnly, base.institution?.state_code ?? null)
    expect(o.annual).toBeNull()
    expect(o.degreeTotal).toBeNull()
  })

  it('show on the college page as printed, per semester, with no yearly figure or multi-year total', async () => {
    const src = new DemoSource(emptyStore(), { snapshot: { ...snap, institutions: snap.institutions.map((c) => (c.institution_key === base.institution_key ? semesterOnly : c)) } as never })
    src.switchPersona(DEMO_STUDENT, 'Student (demo)')
    render(
      <MemoryRouter initialEntries={[`/colleges/${encodeURIComponent(base.institution_key)}`]}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByText(/per semester, In-state, as published\. Not shown as a yearly price\./)).toBeInTheDocument()
    expect(screen.getByText('$21,000')).toBeInTheDocument()
    expect(screen.queryByText('Per year')).not.toBeInTheDocument()
    expect(screen.queryByText('$84,000')).not.toBeInTheDocument()
  })
})
