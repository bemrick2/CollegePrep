import { beforeEach, describe, expect, it, vi } from 'vitest'
import { cleanup, render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from '../../lib/app'
import { App } from '../../App'
import { DemoSource } from '../../lib/data/demo/demoSource'
import { sampleFamily } from '../../lib/data/demo/seed'
import bundled from '../../lib/data/demo/comparison-snapshot.json'
import uaf from '../../lib/engine/__fixtures__/uaf-2026-27.json'
import { writeInterests } from '../../lib/interestStore'
import type { InstitutionComparison } from '../../lib/data/types'

/**
 * #171: University of Alaska Fairbanks' stored 2026-27 records (data/institutions/uaf), whose roadmap items are
 * objects ({code, credits, footnotes}, option lists), through the pages that read degree plans, as the student and
 * as the parent.
 */
const snapshot = {
  academic_year: '2026-27',
  institutions: [
    ...(bundled as unknown as { institutions: InstitutionComparison[] }).institutions,
    { found: true, institution_key: 'uaf', academic_year: '2026-27', missing_domains: [], can_offer_paid_addon: false, institution: uaf.institution, domains: { costs: [], awards: [], appeals: [], admissions_metrics: [], ...uaf.domains } } as unknown as InstitutionComparison,
  ],
}

function at(path: string, persona: 'student' | 'parent') {
  // Compare needs two schools: UAF and UTK (whose Computer Science plan is stored as strings).
  localStorage.setItem('pp-compare', JSON.stringify(['uaf', 'utk']))
  const store = sampleFamily(persona)
  // Mechanical engineering at UAF has a roadmap of object items (and so does computer science).
  writeInterests(store.students[0]!.id, { certainty: 'few', interests: [{ kind: 'major', key: 'mechanical-eng', focus: true }, { kind: 'major', key: 'computer-science' }] })
  return render(
    <MemoryRouter initialEntries={[path]}>
      <AppProvider source={new DemoSource(store, { snapshot })}>
        <App />
      </AppProvider>
    </MemoryRouter>,
  )
}

beforeEach(() => {
  localStorage.clear()
  localStorage.setItem('pp-compare', JSON.stringify(['uaf']))
})

describe('stored UAF roadmaps (object plan items) render for student and parent', () => {
  for (const persona of ['student', 'parent'] as const) {
    it(`${persona}: college page, explore majors, compare and savings`, async () => {
      const errors = vi.spyOn(console, 'error').mockImplementation(() => {})
      at('/colleges/uaf', persona)
      expect(await screen.findByRole('heading', { name: 'University of Alaska Fairbanks', level: 1 }, { timeout: 8000 })).toBeInTheDocument()
      expect(screen.getAllByText(/Mechanical Engineering B\.S\./).length).toBeGreaterThan(0)
      cleanup()
      at('/colleges/majors', persona)
      expect(await screen.findByRole('heading', { name: 'Explore majors' })).toBeInTheDocument()
      expect(await screen.findByText(/University of Alaska Fairbanks has verified programs for/, {}, { timeout: 8000 })).toBeInTheDocument()
      // Read from object items: courses the engineering roadmaps share in their first two terms.
      expect(screen.getByText(/Shared first-year courses in the published maps: .*MATH F251X/)).toBeInTheDocument()
      cleanup()
      at('/colleges/compare', persona)
      expect((await screen.findAllByText(/University of Alaska Fairbanks/, {}, { timeout: 8000 })).length).toBeGreaterThan(0)
      cleanup()
      at('/colleges/savings', persona)
      expect((await screen.findAllByText(/University of Alaska Fairbanks/, {}, { timeout: 8000 })).length).toBeGreaterThan(0)
      // Savings reads every saved school's plan for the focus major (degreeCredit) even before scores exist; it
      // used to throw here. The credit steps themselves are covered in lib/engine/planItems.test.ts.
      expect(errors.mock.calls.map((c) => String(c[0])).filter((m) => /is not a function|TypeError/.test(m))).toEqual([])
      errors.mockRestore()
    }, 60_000)
  }
})
