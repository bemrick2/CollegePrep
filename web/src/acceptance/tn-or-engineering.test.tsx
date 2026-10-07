import { describe, expect, it } from 'vitest'
import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { AppProvider } from '../lib/app'
import { App } from '../App'
import { DemoSource, DEMO_STUDENT } from '../lib/data/demo/demoSource'
import { emptyStore } from '../lib/data/demo/store'
import bundled from '../lib/data/demo/comparison-snapshot.json'
import type { InstitutionComparison } from '../lib/data/types'
import { outlookFor } from '../features/parent/CostOutlook'
import { schoolFit } from '../lib/engine/programFit'
import { writeInterests } from '../lib/interestStore'
import { graduationYearFor } from '../features/onboarding/options'

/**
 * Scenario: an 8th grader in Tennessee, interested in engineering, considering Tennessee and Oregon, wants a
 * four-year school and wants to minimize total cost.
 *
 * Runs against fixtures/tn-or.json (captured from the live RPCs, see README). Until that exists it dry-runs on
 * the bundled snapshot (real records, Tennessee only) so the harness itself stays honest.
 */
const captured = import.meta.glob('./fixtures/tn-or.json', { eager: true, import: 'default' }) as Record<string, unknown>
const fixture = (Object.values(captured)[0] ?? bundled) as unknown as { academic_year: string; institutions: InstitutionComparison[]; source?: string }
const live = Object.keys(captured).length > 0
const HOME = 'TN'
const STATES = ['TN', 'OR']

function pickSchools(): InstitutionComparison[] {
  const four = fixture.institutions.filter((c) => c.found && c.institution?.level === 'four_year' && STATES.includes(c.institution.state_code ?? ''))
  const priced = four.map((c) => ({ c, o: outlookFor(c, HOME) })).filter((x) => x.o.degreeTotal != null)
  // Up to three per state, lowest residency-correct total first (the family wants to minimize cost).
  return STATES.flatMap((st) =>
    priced
      .filter((x) => x.c.institution!.state_code === st)
      .sort((a, b) => a.o.degreeTotal! - b.o.degreeTotal!)
      .slice(0, 3)
      .map((x) => x.c),
  )
}

describe(`acceptance: TN 8th grader, engineering, TN + OR, four-year, lowest cost (${live ? 'live fixture' : 'dry run on bundled snapshot'})`, () => {
  it('onboards without a major, then shows residency-correct costs and verified-only program fit', async () => {
    const user = userEvent.setup()
    const src = new DemoSource(emptyStore(), { snapshot: fixture })
    src.switchPersona(DEMO_STUDENT, 'Student (demo)')
    const ui = render(
      <MemoryRouter initialEntries={['/onboarding/student']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )

    // Setup: grade 8, Tennessee, ACT with no date yet, no score, two study days. Majors and cost goals are
    // deferred to where they matter (Explore majors, Goals), so they are set there afterwards.
    await user.type(await screen.findByLabelText('Your first name'), 'Alex')
    await user.selectOptions(screen.getByLabelText('Home state (optional)'), HOME)
    await user.click(screen.getByRole('button', { name: `Class of ${graduationYearFor(8)}` }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: /^ACT/ }))
    await user.click(screen.getAllByRole('button', { name: 'Not sure yet' }).at(-1)!)
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: 'Not yet' }))
    await user.click(screen.getByRole('button', { name: 'Continue' }))
    await user.click(await screen.findByRole('button', { name: 'Sat' }))
    await user.click(screen.getByRole('button', { name: '10 min' }))
    await user.click(screen.getByRole('button', { name: 'Accept this plan' }))
    await screen.findByRole('link', { name: 'Start the starting benchmark' })
    const me = (await src.getHouseholdContext()).myStudent!
    writeInterests(me.id, { certainty: 'unsure', interests: [{ kind: 'area', key: 'engineering' }] })
    await src.savePlan(me.id, { ...(await src.getPlan(me.id))!, goals: ['raise_score', 'lower_cost'] })
    ui.unmount()

    const schools = pickSchools()
    expect(schools.length).toBeGreaterThan(0)
    localStorage.setItem('pp-compare', JSON.stringify(schools.map((c) => c.institution_key)))

    render(
      <MemoryRouter initialEntries={['/colleges/paths']}>
        <AppProvider source={src}>
          <App />
        </AppProvider>
      </MemoryRouter>,
    )
    expect(await screen.findByRole('heading', { name: 'College paths' })).toBeInTheDocument()
    expect(await screen.findByLabelText('Home state')).toHaveValue(HOME)

    const rows: Record<string, string>[] = []
    for (const c of schools) {
      const name = c.institution!.display_name
      const card = (await screen.findByRole('heading', { name })).closest('article')!
      const o = outlookFor(c, HOME)
      const inState = c.institution!.state_code === HOME
      // Prices follow the family's (stated) home state; a missing out-of-state price is flagged, never passed off.
      if (o.basis === 'out_of_state_missing') expect(within(card).getByText(/No out-of-state price is published/)).toBeInTheDocument()
      else expect(within(card).getByText(inState ? /published (in-state )?cost of attendance/ : /published out-of-state cost of attendance/)).toBeInTheDocument()
      // Program fit is stated only from verified programs; "requires freshman admission" only when the backend says so.
      const fit = schoolFit(c.domains, [{ kind: 'area', key: 'engineering' }])
      if (!fit.fits.some((f) => f.directAdmission)) expect(within(card).queryByText(/requires freshman admission/)).not.toBeInTheDocument()
      rows.push({ school: name, state: c.institution!.state_code ?? '', price: o.residency ?? '—', basis: o.basis, total4yr: o.degreeTotal?.toLocaleString() ?? '—', engineering: fit.fits[0]!.status })
    }
    // No invented savings anywhere on the page.
    expect(screen.queryByText(/(save|savings of) \$[\d,]+/i)).not.toBeInTheDocument()
    console.table(rows)
  }, 30_000)
})
