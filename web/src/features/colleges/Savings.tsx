import { useId, useState } from 'react'
import { Link } from 'react-router-dom'
import { useApp, useAsync } from '../../lib/app'
import type { AwardListing, CostBasis, CostComponents, CreditLever, InstitutionComparison, ProjectionRow } from '../../lib/data/types'
import { netPrice, type FamilyAid } from '../../lib/engine/costProjection'
import { summarizeSchool, type CreditPolicy } from '../../lib/engine/examCredit'
import { stateName } from '../../lib/engine/residency'
import { useHomeState } from '../../lib/homeState'
import { Card, EmptyState, Notice, Pill, Segmented, Spinner, cx } from '../../components/ui'
import { CollegesTabs } from './CollegesTabs'
import { HomeStateControl } from './HomeStateControl'
import { useExamPlan } from './useExamPlan'
import { useFamilyAid } from './useFamilyAid'
import { COMPARE_YEAR, useSavedComparison } from './useSavedComparison'

const YEAR = COMPARE_YEAR
const usd = (n: number) => n.toLocaleString('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })
const BASIS_LABEL: Record<CostBasis, string> = { tuition_and_fees: 'Tuition and fees', cost_of_attendance: 'Full cost of attendance' }
const COMPONENTS: { key: keyof CostComponents; label: string; group: 'billed' | 'living' }[] = [
  { key: 'tuition', label: 'Tuition', group: 'billed' },
  { key: 'mandatory_fees', label: 'Required fees', group: 'billed' },
  { key: 'housing_food', label: 'Housing and food', group: 'living' },
  { key: 'books_supplies', label: 'Books and supplies', group: 'living' },
  { key: 'transportation', label: 'Transportation', group: 'living' },
  { key: 'personal_misc', label: 'Personal expenses', group: 'living' },
  { key: 'other_expenses', label: 'Other expenses', group: 'living' },
]
const CAP_LABEL: Record<string, string> = {
  transfer_max_credits: 'transfer credit maximum',
  dual_enrollment_limit: 'dual-enrollment limit',
  AP_limit: 'AP credit limit',
  IB_limit: 'IB credit limit',
  CLEP_limit: 'CLEP credit limit',
  cambridge_international_limit: 'Cambridge credit limit',
}
const AWARD_PREVIEW = 3

/**
 * Cost and savings for the family's saved schools: the school's own published price by part, credit counted only
 * by that school's published rules, and the family's own grant and loan numbers kept apart from research data.
 * Every total is an estimate at this year's prices.
 */
export function Savings() {
  const { source, activeStudent } = useApp()
  const { homeState } = useHomeState()
  const cmp = useSavedComparison(YEAR)
  const exams = useExamPlan(activeStudent?.id).exams
  const family = useFamilyAid(activeStudent?.id)
  const [basis, setBasis] = useState<CostBasis>('cost_of_attendance')
  const studentId = activeStudent?.id
  const schools = (cmp.data ?? []).filter((c) => c.found)

  const examCredits = (c: InstitutionComparison) => summarizeSchool((c.domains.credit_policies ?? []) as unknown as CreditPolicy[], exams)
  const residencyFor = (c: InstitutionComparison) => {
    const st = c.institution?.state_code
    return homeState && st && homeState !== st ? 'out_of_state' : 'in_state'
  }
  const otherCredits = family.entries.otherCredits
  const rows = useAsync(
    () =>
      !studentId || !schools.length
        ? Promise.resolve([] as ProjectionRow[])
        : Promise.all(
            schools.map((c) =>
              source
                .costProjection(studentId, [c.institution_key], YEAR, {
                  residency: residencyFor(c),
                  cost_basis: basis,
                  exam_credits: Math.min(examCredits(c).publishedHours, 90),
                  prior_credits: otherCredits,
                })
                .then((r) => r.institutions[0]!),
            ),
          ),
    [source, studentId, schools.map((c) => c.institution_key).join(','), homeState, basis, otherCredits, JSON.stringify(exams)],
  )

  return (
    <div className="grid grid-cols-1 gap-5">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <p className="text-sm text-ink-3">Colleges & cost</p>
          <h1 className="display text-[30px] font-semibold leading-tight text-ink md:text-[36px]">Cost & savings</h1>
          <p className="mt-1 max-w-2xl text-sm text-ink-2">
            Each school's published {YEAR} price, split into what the school bills and what living there costs. Credit counts only where the school's own
            rules allow it. Grants and loans are your numbers, never guessed.
          </p>
        </div>
        <CollegesTabs />
      </div>

      <Card className="grid gap-4 p-5 md:grid-cols-[1fr_auto] md:items-start">
        <div className="grid gap-3">
          <HomeStateControl />
          <div className="flex flex-wrap items-center gap-x-3 gap-y-2">
            <span className="text-sm font-semibold text-ink" id="basis-label">
              Count
            </span>
            <Segmented<CostBasis>
              label="Which costs to count"
              value={basis}
              onChange={setBasis}
              options={[
                { value: 'cost_of_attendance', label: 'Full cost of attendance' },
                { value: 'tuition_and_fees', label: 'Tuition and fees only' },
              ]}
            />
          </div>
        </div>
        <div className="grid gap-2 md:w-72">
          <MoneyOrCount
            id="other-credits"
            label="Credit from dual enrollment or another college"
            hint="Credit hours. Counted only where the school publishes a transfer limit."
            value={otherCredits || null}
            onChange={(n) => family.setOtherCredits(n ?? 0)}
            max={90}
            unit="credits"
          />
          <p className="text-xs text-ink-3">
            AP and CLEP credit comes from scores on{' '}
            <Link to="/colleges/paths" className="font-semibold text-go-strong underline dark:text-go">
              Paths
            </Link>
            {exams.length ? `: ${exams.filter((e) => e.score != null).length} with a score.` : '. None added yet.'}
          </p>
        </div>
      </Card>

      {!studentId ? (
        <Notice tone="info" title="Add a student first">
          Savings depend on the student's credit and the schools you save, so this view needs a student profile.
        </Notice>
      ) : (cmp.loading || rows.loading) && !rows.data?.length ? (
        <div className="py-10">
          <Spinner label="Loading published prices" />
        </div>
      ) : !schools.length ? (
        <Card>
          <EmptyState title="No saved schools yet" action={<Link to="/colleges" className="font-semibold text-go-strong underline dark:text-go">Find and save schools</Link>}>
            Save up to eight schools to see their published prices side by side.
          </EmptyState>
        </Card>
      ) : rows.error ? (
        <Notice tone="bad" title="We couldn't load the cost projection">
          {rows.error.message}
        </Notice>
      ) : (
        <div className={cx('grid gap-4 transition-opacity', rows.loading && 'opacity-60')} aria-busy={rows.loading}>
          {(rows.data ?? []).map((r) => {
            const c = schools.find((x) => x.institution_key === r.institution_key)
            if (!c) return null // removed while the projection reloads
            return (
              <SchoolSavings
                key={r.institution_key}
                row={r}
                comparison={c}
                assumedResidency={!homeState}
                aid={family.aidFor(r.institution_key)}
                onAid={(a) => family.setAid(r.institution_key, a)}
                examSummary={examCredits(c)}
                onBasis={setBasis}
              />
            )
          })}
          <p className="text-xs text-ink-3">
            Estimates at {YEAR} published prices, held flat; real prices usually rise each year. Nothing here is a guarantee of cost, credit or aid.
          </p>
        </div>
      )}
    </div>
  )
}

function residencyLine(row: ProjectionRow, assumed: boolean, schoolState: string | null | undefined) {
  if (!row.cost) return null
  if (row.cost.residency === 'not_applicable') return 'One published price for all students'
  if (row.cost.residency === 'out_of_state') return 'Out-of-state price'
  return assumed ? `In-state price (assumed; set your home state)` : `In-state price for ${stateName(schoolState)} residents`
}

function SchoolSavings({
  row,
  comparison,
  assumedResidency,
  aid,
  onAid,
  examSummary,
  onBasis,
}: {
  row: ProjectionRow
  comparison: InstitutionComparison
  assumedResidency: boolean
  aid: FamilyAid
  onAid: (a: Partial<FamilyAid>) => void
  examSummary: ReturnType<typeof summarizeSchool>
  onBasis: (b: CostBasis) => void
}) {
  const name = row.display_name ?? comparison.institution?.display_name ?? row.institution_key
  const headingId = useId()
  const c = row.cost?.components
  const net = netPrice(row, aid)
  const awards = row.not_counted?.awards ?? []

  return (
    <Card as="article" className="overflow-hidden" aria-labelledby={headingId}>
      <header className="flex flex-wrap items-baseline justify-between gap-2 border-b border-line px-5 py-4">
        <div>
          <h2 id={headingId} className="text-lg font-semibold text-ink">
            <Link to={`/colleges/${row.institution_key}`} className="hover:underline">
              {name}
            </Link>
          </h2>
          <p className="text-sm text-ink-3">{residencyLine(row, assumedResidency, comparison.institution?.state_code) ?? 'No verified price'}</p>
        </div>
        {row.status === 'ok' && <Pill tone="gold">Estimate</Pill>}
      </header>

      {row.status === 'unknown_institution' ? (
        <p className="px-5 py-4 text-sm text-ink-2">This school has no verified record yet, so there is no price to show.</p>
      ) : (
        <div className="grid gap-0 md:grid-cols-2">
          <section className="border-line px-5 py-4 md:border-r" aria-label={`${name}: one year, published`}>
            <h3 className="text-sm font-semibold text-ink">One year, as published</h3>
            {c ? (
              <div className="mt-2 grid gap-1 text-sm">
                {(['billed', 'living'] as const).map((g) => {
                  const parts = COMPONENTS.filter((x) => x.group === g)
                  const shown = parts.filter((x) => c[x.key] != null)
                  const missing = parts.filter((x) => c[x.key] == null)
                  return (
                    <div key={g} className="grid gap-1">
                      <p className="mt-1 text-xs font-semibold text-ink-3">{g === 'billed' ? 'Billed by the school' : 'Living and other costs'}</p>
                      {shown.length > 0 && (
                        <dl className="grid gap-1">
                          {shown.map((x) => (
                            <div key={x.key} className="flex justify-between gap-3">
                              <dt className="text-ink-2">{x.label}</dt>
                              <dd className="tabular font-semibold text-ink">{usd(c[x.key]!)}</dd>
                            </div>
                          ))}
                        </dl>
                      )}
                      {missing.length > 0 && (
                        <p className="text-xs text-ink-3">
                          Not published separately: {missing.map((x) => x.label.toLowerCase()).join(', ')}
                          {g === 'living' && c.total_cost_of_attendance != null && shown.length === 0 ? ' (included in the cost of attendance)' : ''}
                        </p>
                      )}
                    </div>
                  )
                })}
                <dl className="mt-1 flex justify-between gap-3 border-t border-line pt-2">
                  <dt className="font-semibold text-ink">Cost of attendance</dt>
                  <dd className={c.total_cost_of_attendance != null ? 'tabular font-semibold text-ink' : 'text-ink-3'}>
                    {c.total_cost_of_attendance != null ? usd(c.total_cost_of_attendance) : 'Not published'}
                  </dd>
                </dl>
              </div>
            ) : (
              <p className="mt-2 text-sm text-ink-2">No verified {YEAR} price for this residency. We don't substitute another year's or another residency's price.</p>
            )}
            {row.cost?.source_url && (
              <a href={row.cost.source_url} target="_blank" rel="noreferrer" className="mt-2 inline-block text-xs font-semibold text-go-strong underline dark:text-go">
                Published source
              </a>
            )}
          </section>

          <section className="px-5 py-4" aria-label={`${name}: over the degree`}>
            {row.status === 'missing_cost' ? (
              <MissingCost row={row} onBasis={onBasis} />
            ) : row.status === 'missing_years' ? (
              <p className="text-sm text-ink-2">The school's program length isn't on file, so there is no multi-year total.</p>
            ) : (
              <DegreeTotals row={row} net={net!} examSummary={examSummary} name={name} />
            )}
          </section>
        </div>
      )}

      {row.status === 'ok' && (
        <div className="grid gap-4 border-t border-line px-5 py-4 md:grid-cols-2">
          <section aria-label={`${name}: grants and scholarships`}>
            <h3 className="text-sm font-semibold text-ink">Grants and scholarships</h3>
            <MoneyOrCount
              id={`${row.institution_key}-grants`}
              label="Offered to you, per year"
              hint="From an award letter. Free money that you don't repay."
              value={aid.grantsPerYear}
              onChange={(n) => onAid({ grantsPerYear: n })}
              max={500000}
              unit="dollars"
            />
            <AwardList awards={awards} name={name} />
          </section>
          <section aria-label={`${name}: loans`}>
            <h3 className="text-sm font-semibold text-ink">Loans</h3>
            <MoneyOrCount
              id={`${row.institution_key}-loans`}
              label="You plan to borrow, per year"
              hint="Borrowed money is repaid with interest, so it doesn't lower the price. Interest isn't included."
              value={aid.loansPerYear}
              onChange={(n) => onAid({ loansPerYear: n })}
              max={500000}
              unit="dollars"
            />
            <p className="mt-2 text-xs text-ink-3">We have no loan data for any school. Federal and private loan terms aren't shown here.</p>
          </section>
        </div>
      )}
    </Card>
  )
}

function MissingCost({ row, onBasis }: { row: ProjectionRow; onBasis: (b: CostBasis) => void }) {
  const c = row.cost?.components
  if (row.cost?.basis === 'tuition_and_fees' && c?.total_cost_of_attendance != null)
    return (
      <div className="grid gap-2 text-sm text-ink-2">
        <p>This school publishes a full cost of attendance but no separate tuition, so a tuition-and-fees total isn't possible.</p>
        <div>
          <button type="button" onClick={() => onBasis('cost_of_attendance')} className="font-semibold text-go-strong underline dark:text-go">
            Count full cost of attendance instead
          </button>
        </div>
      </div>
    )
  if (row.cost?.basis === 'cost_of_attendance' && c?.tuition != null)
    return (
      <div className="grid gap-2 text-sm text-ink-2">
        <p>This school publishes tuition but no full cost of attendance, so living costs can't be totalled.</p>
        <div>
          <button type="button" onClick={() => onBasis('tuition_and_fees')} className="font-semibold text-go-strong underline dark:text-go">
            Count tuition and fees instead
          </button>
        </div>
      </div>
    )
  return <p className="text-sm text-ink-2">Without a published price there is no total and no savings estimate.</p>
}

function DegreeTotals({ row, net, examSummary, name }: { row: ProjectionRow; net: NonNullable<ReturnType<typeof netPrice>>; examSummary: ReturnType<typeof summarizeSchool>; name: string }) {
  const s = row.credit_savings!
  const basis = row.cost!.basis
  const years = row.years!
  const exam = row.levers!.find((l) => l.kind === 'exam_credits')!
  const prior = row.levers!.find((l) => l.kind === 'prior_credits')!
  return (
    <div className="grid gap-3">
      <h3 className="text-sm font-semibold text-ink">
        Over {years} {years === 1 ? 'year' : 'years'} <span className="font-normal text-ink-3">({BASIS_LABEL[basis].toLowerCase()})</span>
      </h3>
      <dl className="grid gap-1 text-sm" aria-label="From published price to what you pay">
        <Line label="Published price" value={usd(net.publishedTotal)} sub={row.years_source === 'level_default' ? `${years} years is the usual length for this kind of school` : undefined} />
        <Line label="Credit you bring" value={net.creditSavings ? `− ${usd(net.creditSavings)}` : usd(0)} tone={net.creditSavings ? 'go' : undefined} />
        <Line label="Grants you entered" value={net.grants ? `− ${usd(net.grants)}` : 'None entered'} tone={net.grants ? 'go' : undefined} />
        <Line label="Net price" value={usd(net.netPrice)} strong />
        {net.borrowed > 0 && (
          <>
            <Line label="Borrowed (you repay this)" value={usd(net.borrowed)} indent />
            <Line label="Paid from savings or income" value={usd(net.paidWithoutLoans)} indent />
          </>
        )}
      </dl>
      {net.loansCapped && <p className="text-xs text-ink-3">The borrowing you entered is more than what's left to pay, so it stops at the net price.</p>}

      <div className="rounded-xl bg-surface-2 px-3 py-3 text-sm">
        <h4 className="font-semibold text-ink">How credit changes the cost</h4>
        {s.terms_saved > 0 ? (
          <p className="mt-1 text-ink-2">
            {s.credits_counted} credits could let the student finish {s.terms_saved} {s.terms_saved === 1 ? 'term' : 'terms'} early. That saves{' '}
            <span className="font-semibold text-ink">{usd(row.savings_total!)}</span>
            {componentSplit(s.by_component)}. It saves money only by graduating sooner, not by lowering a term's bill.
          </p>
        ) : (
          <p className="mt-1 text-ink-2">No counted credit saves a full term at {name}.</p>
        )}
        <ul className="mt-2 grid gap-1 text-ink-2">
          <LeverLine lever={exam} examSummary={examSummary} />
          <LeverLine lever={prior} />
          {s.outside_credit_max != null && (
            <li>
              {name} requires {s.residency_requirement_credits} credits earned there, so at most {s.outside_credit_max} outside credits fit this plan.
            </li>
          )}
          {s.remainder_credits > 0 && (
            <li>
              {s.remainder_credits} {s.remainder_credits === 1 ? 'credit falls' : 'credits fall'} short of another full term and {s.remainder_credits === 1 ? 'is' : 'are'} not counted. Whether
              they lower a bill depends on whether {name} charges a flat rate or per credit, which we don't have.
            </li>
          )}
        </ul>
        {s.credits_counted > 0 && <p className="mt-2 text-xs text-ink-3">Confirm with the school's registrar before counting on any credit.</p>}
      </div>
    </div>
  )
}

function componentSplit(b: { tuition: number | null; mandatory_fees: number | null; living_and_other: number | null }) {
  const parts = [
    b.tuition ? `${usd(b.tuition)} tuition` : null,
    b.mandatory_fees ? `${usd(b.mandatory_fees)} fees` : null,
    b.living_and_other ? `${usd(b.living_and_other)} living costs` : null,
  ].filter(Boolean)
  return parts.length ? ` (${parts.join(', ')})` : ''
}

function LeverLine({ lever, examSummary }: { lever: CreditLever; examSummary?: ReturnType<typeof summarizeSchool> }) {
  const cap = lever.caps.length ? lever.caps.reduce((a, b) => (b.credits < a.credits ? b : a)) : null
  const capText = cap ? (
    <>
      the school's{' '}
      {cap.source_url ? (
        <a href={cap.source_url} target="_blank" rel="noreferrer" className="underline">
          {CAP_LABEL[cap.kind] ?? cap.kind}
        </a>
      ) : (
        (CAP_LABEL[cap.kind] ?? cap.kind)
      )}{' '}
      of {cap.credits}
    </>
  ) : null
  if (lever.kind === 'exam_credits') {
    if (!examSummary?.hasTable) return <li>No published AP/CLEP credit table on file for this school, so exam credit isn't counted.</li>
    if (lever.requested_credits === 0)
      return <li>{examSummary.courses ? 'Your scores earn courses here, but the table lists no credit hours for them.' : 'No AP or CLEP scores that earn credit here yet.'}</li>
    return (
      <li>
        AP/CLEP: {lever.requested_credits} credits from the school's own table{lever.accepted_upper_bound < lever.requested_credits ? <>, limited to {lever.accepted_upper_bound} by {capText}</> : ''}.
        {examSummary.coursesWithoutHours ? ` ${examSummary.coursesWithoutHours} more earned ${examSummary.coursesWithoutHours === 1 ? 'course lists' : 'courses list'} no hours and ${examSummary.coursesWithoutHours === 1 ? "isn't" : "aren't"} counted.` : ''}
      </li>
    )
  }
  if (lever.reason === 'no_prior_credits') return null
  if (lever.reason === 'no_verified_cap')
    return <li>Other credit: {lever.requested_credits} entered, not counted. The school publishes no transfer limit we can check against.</li>
  return (
    <li>
      Other credit: {lever.requested_credits} entered{lever.accepted_upper_bound < lever.requested_credits ? <>, up to {lever.accepted_upper_bound} under {capText}</> : <>, within {capText}</>}.
    </li>
  )
}

function AwardList({ awards, name }: { awards: AwardListing[]; name: string }) {
  const [all, setAll] = useState(false)
  if (!awards.length) return <p className="mt-2 text-xs text-ink-3">No verified scholarships listed for {name} this year.</p>
  const shown = all ? awards : awards.slice(0, AWARD_PREVIEW)
  return (
    <div className="mt-3">
      <p className="text-xs text-ink-3">
        {name} lists these. They're not subtracted: eligibility depends on the student and the school decides.
      </p>
      <ul className="mt-1 grid gap-1 text-sm">
        {shown.map((a) => (
          <li key={a.award_name} className="flex justify-between gap-3">
            {a.source_url ? (
              <a href={a.source_url} target="_blank" rel="noreferrer" className="text-ink-2 underline decoration-line-strong">
                {a.award_name}
              </a>
            ) : (
              <span className="text-ink-2">{a.award_name}</span>
            )}
            <span className="shrink-0 tabular text-ink-3">{awardAmount(a)}</span>
          </li>
        ))}
      </ul>
      {awards.length > AWARD_PREVIEW && (
        <button type="button" onClick={() => setAll(!all)} className="mt-1 text-xs font-semibold text-go-strong underline dark:text-go">
          {all ? 'Show fewer' : `View all ${awards.length}`}
        </button>
      )}
    </div>
  )
}

function awardAmount(a: AwardListing) {
  if (a.full_ride) return 'Full ride'
  if (a.full_tuition) return 'Full tuition'
  if (a.award_min != null && a.award_max != null && a.award_min !== a.award_max) return `${usd(a.award_min)}–${usd(a.award_max)}`
  if (a.award_max != null) return `Up to ${usd(a.award_max)}`
  if (a.award_min != null) return `From ${usd(a.award_min)}`
  return 'Amount not published'
}

function Line({ label, value, sub, tone, strong, indent }: { label: string; value: string; sub?: string; tone?: 'go'; strong?: boolean; indent?: boolean }) {
  return (
    <div className={cx('flex justify-between gap-3', strong && 'mt-1 border-t border-line pt-2', indent && 'pl-3 text-ink-3')}>
      <dt className={cx(strong ? 'font-semibold text-ink' : 'text-ink-2')}>
        {label}
        {sub && <span className="block text-xs text-ink-3">{sub}</span>}
      </dt>
      <dd className={cx('tabular', strong ? 'text-base font-semibold text-ink' : 'font-semibold', tone === 'go' ? 'text-go-strong dark:text-go' : !strong && 'text-ink')}>{value}</dd>
    </div>
  )
}

function MoneyOrCount({
  id,
  label,
  hint,
  value,
  onChange,
  max,
  unit,
}: {
  id: string
  label: string
  hint: string
  value: number | null
  onChange: (n: number | null) => void
  max: number
  unit: 'dollars' | 'credits'
}) {
  const [text, setText] = useState(value == null ? '' : String(value))
  const hintId = `${id}-hint`
  return (
    <div className="mt-2">
      <label htmlFor={id} className="block text-sm font-semibold text-ink">
        {label}
      </label>
      <p id={hintId} className="text-xs text-ink-3">
        {hint}
      </p>
      <div className="mt-1 flex items-center gap-2">
        {unit === 'dollars' && <span className="text-sm text-ink-3" aria-hidden>$</span>}
        <input
          id={id}
          inputMode="numeric"
          aria-describedby={hintId}
          value={text}
          onChange={(e) => {
            const raw = e.target.value.replace(/[^0-9]/g, '')
            setText(raw)
            onChange(raw === '' ? null : Math.min(Number(raw), max))
          }}
          className="h-10 w-36 rounded-lg border border-line-strong bg-surface px-3 text-[16px] tabular text-ink focus:border-focus focus:outline-none focus:ring-2 focus:ring-info/30"
        />
        {unit === 'credits' && <span className="text-sm text-ink-3">credits</span>}
      </div>
    </div>
  )
}
