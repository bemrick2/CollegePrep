import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { useHomeState } from '../../lib/homeState'
import type { InstitutionComparison } from '../../lib/data/types'
import { buildRoadmap } from '../../lib/engine/planning/roadmap'
import { projectRow } from '../../lib/engine/costProjection'
import type { CreditFit, CreditLine, Evidence, LivingArrangement, Roadmap, TermCoverage } from '../../lib/engine/planning/types'
import { formatShortDate } from '../../lib/engine/dates'
import { useExamPlan } from '../colleges/useExamPlan'
import { CollegesTabs } from '../colleges/CollegesTabs'
import { Notice, PageLoading, Pill, Segmented, cx, inputClass } from '../../components/ui'
import { PageHeader, Section } from '../../components/layout'

/**
 * Planning pilot (#195): one school and one business major, from the stored Tennessee pilot records. Demo only, and
 * only when VITE_PLANNING_PILOT=true (off in every deployed environment until the pilot's exit criteria are met,
 * docs/product/COLLEGE_PLANNING_PILOT.md §4). Everything shown comes from buildRoadmap; nothing is computed here.
 */
export const PLANNING_PILOT = import.meta.env.VITE_PLANNING_PILOT === 'true'

type Fixture = { academic_year: string; schools: { institution_key: string; institution: Record<string, unknown>; domains: Record<string, Record<string, unknown>[]> }[] }

const usd = (n: number) => n.toLocaleString('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })
const ARRANGEMENT: Record<LivingArrangement, string> = { on_campus: 'On campus', off_campus: 'Off campus', with_family: 'With family' }
const FIT: Record<CreditFit, { tone: 'go' | 'warn' | 'neutral'; label: string }> = {
  applies: { tone: 'go', label: 'Fills a course in this plan' },
  partly: { tone: 'warn', label: 'Fills part of a course group' },
  accepted_not_in_plan: { tone: 'warn', label: 'Credit, but not a course this plan lists' },
  elective_only: { tone: 'neutral', label: 'Elective credit only' },
  unknown: { tone: 'neutral', label: 'Credit; where it counts isn’t on file' },
  none: { tone: 'neutral', label: 'No credit at this score' },
  // Unreachable today (a line without a verified table has no acceptance value, so CreditRow shows its own label);
  // kept so the map stays complete.
  not_verified: { tone: 'neutral', label: 'Not verified yet' },
  planned: { tone: 'neutral', label: 'Planned: no score yet' },
  see_table: { tone: 'neutral', label: 'Read the school’s table for this exam' },
}
const STATUS: Record<Roadmap['status'], { tone: 'go' | 'warn' | 'bad'; label: string; text: string }> = {
  ready: { tone: 'go', label: 'Plan, credit tables and cost on file', text: 'The degree plan, this school’s exam-credit tables and its cost are verified records. Anything else is named below.' },
  partial: { tone: 'warn', label: 'Partly on file', text: 'The degree plan is verified; some of what follows isn’t on file yet, and says so.' },
  blocked: { tone: 'bad', label: 'No degree plan on file', text: 'Without a verified term-by-term plan for this major, credit can be shown as accepted, but not where it counts.' },
}

export function CollegePlan() {
  const { activeStudent } = useApp()
  const { homeState } = useHomeState()
  const exams = useExamPlan(activeStudent?.id, false).exams
  const [fx, setFx] = useState<Fixture | null>(null)
  const [school, setSchool] = useState('utc')
  const [program, setProgram] = useState('management-b-s-b-a')
  const [planKey, setPlanKey] = useState<string | null>(null)
  const [arrangement, setArrangement] = useState<LivingArrangement>('on_campus')
  useEffect(() => {
    let live = true
    void import('./pilotFixture.json').then((m) => live && setFx(m.default as unknown as Fixture))
    return () => {
      live = false
    }
  }, [])

  const comparison = useMemo<InstitutionComparison | null>(() => {
    const s = fx?.schools.find((x) => x.institution_key === school)
    if (!s || !fx) return null
    return { institution_key: s.institution_key, found: true, institution: s.institution as never, academic_year: fx.academic_year, domains: s.domains as never, missing_domains: [], can_offer_paid_addon: false }
  }, [fx, school])
  const programs = useMemo(
    () =>
      ((comparison?.domains as Record<string, Record<string, unknown>[]> | undefined)?.academic_programs ?? [])
        .map((p) => ({ key: String(p.program_key), name: String(p.program_name ?? p.program_key), verified: p.verification_status === 'verified' }))
        .sort((a, b) => a.name.localeCompare(b.name)),
    [comparison],
  )
  useEffect(() => {
    if (programs.length && !programs.some((p) => p.key === program)) setProgram(programs[0]!.key)
  }, [programs, program])

  const roadmap = useMemo(() => {
    if (!comparison || !programs.some((p) => p.key === program)) return null
    const residency = homeState && homeState !== String(comparison.institution?.state_code ?? '') ? 'out_of_state' : 'in_state'
    return buildRoadmap({
      comparison,
      programKey: program,
      planKey,
      profile: { gradeLevel: activeStudent?.grade_level ?? null, graduationYear: activeStudent?.graduation_year ?? null, homeState, interests: [], exams, livingArrangement: arrangement },
      projection: projectRow(comparison, comparison.academic_year, { residency, cost_basis: 'cost_of_attendance' }),
    })
  }, [comparison, program, planKey, programs, homeState, exams, arrangement, activeStudent])

  if (!PLANNING_PILOT) return null
  if (!fx) return <PageLoading />
  const who = activeStudent?.display_name ?? 'your student'

  return (
    <div className="grid grid-cols-1 gap-10">
      <PageHeader kicker="Colleges & cost (pilot)" title="College plan" actions={<CollegesTabs />}>
        One school and one business major at a time, from each school’s own records. A fact is shown only when its record is verified; everything else is named
        as not on file.
      </PageHeader>

      <div className="grid gap-4 md:grid-cols-2 lg:max-w-3xl">
        <label className="grid gap-1.5 text-sm font-semibold text-ink">
          School
          <select className={inputClass} value={school} onChange={(e) => (setSchool(e.target.value), setPlanKey(null))}>
            {fx.schools.map((s) => (
              <option key={s.institution_key} value={s.institution_key}>
                {String(s.institution.display_name ?? s.institution_key)}
              </option>
            ))}
          </select>
        </label>
        <label className="grid gap-1.5 text-sm font-semibold text-ink">
          Major
          <select className={inputClass} value={program} onChange={(e) => (setProgram(e.target.value), setPlanKey(null))}>
            {programs.map((p) => (
              <option key={p.key} value={p.key}>
                {p.verified ? p.name : `${p.name} (listing not yet verified)`}
              </option>
            ))}
          </select>
        </label>
      </div>

      {roadmap && (
        <RoadmapView
          r={roadmap}
          who={who}
          examCount={exams.length}
          onPlan={setPlanKey}
          arrangement={arrangement}
          onArrangement={setArrangement}
          priceFor={
            // The engine's own explanation wins (no home state, or no out-of-state price published).
            roadmap.cost.evidence.method ??
            (!comparison?.institution?.state_code
              ? 'In-state price shown: this school’s state isn’t on file.'
              : homeState === String(comparison.institution.state_code)
              ? `In-state price, for a family in ${homeState} (your answer; residency is the school's decision).`
              : `Out-of-state price, for a family in ${homeState} (your answer).`)
          }
        />
      )}
    </div>
  )
}

function RoadmapView({
  r,
  who,
  examCount,
  onPlan,
  arrangement,
  onArrangement,
  priceFor,
}: {
  r: Roadmap
  who: string
  examCount: number
  onPlan: (key: string) => void
  arrangement: LivingArrangement
  onArrangement: (a: LivingArrangement) => void
  priceFor: string
}) {
  const st = STATUS[r.status]
  const plan = r.plan.value
  const costs = r.cost.value ?? []
  const chosen = costs.find((c) => c.arrangement === arrangement) ?? null
  return (
    <>
      <Notice tone={st.tone === 'go' ? 'info' : st.tone === 'warn' ? 'warn' : 'bad'} title={st.label}>
        <p>{st.text}</p>
        <p className="mt-1">
          {plan?.catalogYear ? `Degree plan: ${plan.catalogYear} catalog. ` : ''}
          {r.cost.value && r.cost.evidence.publishedYear ? `Prices: ${r.cost.evidence.publishedYear}, as published. ` : ''}A student entering college years from
          now will face a later catalog and prices; nothing here is projected forward.
        </p>
      </Notice>

      <Section
        id="plan-heading"
        title="Degree plan"
        subtitle={plan ? `${r.target.programName ?? r.target.programKey}${plan.catalogYear ? `, ${plan.catalogYear} catalog` : ''}` : r.target.programVerified ? undefined : 'This school’s listing of the major isn’t verified yet'}
      >
        {r.plans.length > 1 && (
          <label className="mb-4 grid max-w-md gap-1.5 text-sm font-semibold text-ink">
            Plan or track ({r.plans.length} printed for this major)
            <select className={inputClass} value={r.planKey ?? ''} onChange={(e) => onPlan(e.target.value)}>
              {r.plans.map((p, i) => (
                <option key={p.key} value={p.key}>
                  {p.title ?? `Plan ${i + 1} (untitled by the school)`}
                </option>
              ))}
            </select>
          </label>
        )}
        {plan ? (
          <>
            {plan.title && r.plans.length <= 1 && <p className="mb-3 text-sm font-semibold text-ink">{plan.title}</p>}
            <PlanTerms terms={plan.terms} />
            <p className="mt-3 text-sm text-ink-2">
              {plan.totalCredits != null
                ? `${plan.totalCredits} credit hours in total, as printed. `
                : plan.totalText
                  ? `Total as printed: ${plan.totalText.replace(/\s*\(as printed\)\s*$/i, '')}. `
                  : ''}
              <SourceNote e={r.plan.evidence} />
            </p>
          </>
        ) : (
          <Missing e={r.plan.evidence} />
        )}
      </Section>

      <Section id="credit-heading" title="Exam credit" subtitle={`Exams ${who} took or plans to take, against this school’s own table`}>
        {examCount === 0 ? (
          <p className="text-sm text-ink-2">
            No exams added yet.{' '}
            <Link to="/colleges/paths" className="font-semibold text-brand hover:underline">
              Add AP, CLEP, IB or Statewide Dual Credit exams on Paths
            </Link>
            .
          </p>
        ) : (
          <ul className="grid gap-2">
            {r.credit.map((c) => (
              <CreditRow key={c.exam.key} c={c} />
            ))}
          </ul>
        )}
        {r.options.length > 0 && (
          <div className="mt-5">
            <h3 className="text-sm font-bold text-ink">Exams whose credit fills a course in this plan</h3>
            <p className="text-xs text-ink-3">From the school’s verified table; the score shown is the lowest that earns that course.</p>
            <ul className="mt-2 grid gap-1 text-sm text-ink-2">
              {r.options.map((o) => (
                <li key={`${o.examName}-${o.level ?? ''}-${o.minimumText}`}>
                  <span className="font-semibold text-ink">{o.examName}</span>
                  {o.level ? ` (${o.level})` : ''}, {o.minimumText}: {o.course}, term {o.rows.map((x) => x.term).join(' and ')}
                  {o.hours != null ? `, ${o.hours} hours` : ', hours not listed'}
                </li>
              ))}
            </ul>
          </div>
        )}
      </Section>

      <Section id="cost-heading" title="Cost of attendance" subtitle="Per academic year, as the school publishes it">
        {costs.length ? (
          <div className="grid gap-3">
            <Segmented label="Where the student lives" value={arrangement} onChange={onArrangement} options={costs.map((c) => ({ value: c.arrangement, label: ARRANGEMENT[c.arrangement] }))} />
            {chosen ? (
              <p className="text-[15px] text-ink">
                <span className="text-2xl font-bold">{usd(chosen.annual)}</span> <span className="text-ink-3">per year, {ARRANGEMENT[chosen.arrangement].toLowerCase()}</span>
              </p>
            ) : (
              <p className="text-sm text-ink-2">The school doesn’t publish a price for that arrangement.</p>
            )}
            <p className="text-xs text-ink-3">
              {priceFor} Published for {r.cost.evidence.publishedYear}. <SourceNote e={r.cost.evidence} />
            </p>
          </div>
        ) : (
          <Missing e={r.cost.evidence} />
        )}
      </Section>

      <Section id="time-heading" title="Credit coverage, time and money">
        <h3 className="text-sm font-bold text-ink">Credit coverage</h3>
        {r.coverage.value ? (
          <p className="mt-1 text-sm text-ink-2">
            Credit covers every course in {r.coverage.value.termsCovered} of {r.coverage.value.termsInPlan} plan terms. {r.coverage.evidence.method}
          </p>
        ) : (
          <Missing e={r.coverage.evidence} />
        )}
        <h3 className="mt-4 text-sm font-bold text-ink">Time and money saved</h3>
        {r.savings.value ? (
          <p className="mt-1 text-sm text-ink-2">
            <span className="font-semibold text-ink">Potential saving {usd(r.savings.value.net)}</span>. {r.savings.evidence.method}
          </p>
        ) : (
          <p className="mt-1 text-sm text-ink-2">Not shown. {r.savings.evidence.missing}</p>
        )}
      </Section>

      <Section id="de-heading" title="Dual enrollment">
        {r.dualEnrollment.value ? (
          <p className="text-sm text-ink-2">
            Published eligibility: {r.dualEnrollment.value.grades.length ? `grades ${r.dualEnrollment.value.grades.join(' and ')}` : 'grades not stated'}
            {r.dualEnrollment.value.minHsGpa != null ? `, a ${r.dualEnrollment.value.minHsGpa.toFixed(1)} high school GPA` : ''}
            {r.dualEnrollment.value.altMinAct != null ? ` (or an ACT of ${r.dualEnrollment.value.altMinAct})` : ''}.
            {r.dualEnrollment.value.perCreditCharge != null ? ` ${usd(r.dualEnrollment.value.perCreditCharge)} per credit hour, as published.` : ''} <SourceNote e={r.dualEnrollment.evidence} />
          </p>
        ) : (
          <Missing e={r.dualEnrollment.evidence} />
        )}
      </Section>

      <Section id="unknown-heading" title="What isn’t on file yet" subtitle="Named so nothing is guessed">
        {r.unknowns.length ? (
          <ul className="grid list-disc gap-1 pl-5 text-sm text-ink-2">
            {r.unknowns.map((u) => (
              <li key={u.text}>{u.text}</li>
            ))}
          </ul>
        ) : (
          <p className="text-sm text-ink-2">Nothing missing for this school and major.</p>
        )}
      </Section>
    </>
  )
}

const NOT_CHECKED: Record<NonNullable<TermCoverage['notChecked']>, string> = {
  multi_term: 'Printed as one block of more than one term, so whole-term coverage isn’t checked.',
  short_term: 'A summer or short session: not checked for whole-term coverage.',
  quarter_calendar: 'A quarter term: whole-term coverage is checked for semester plans only.',
  hours: 'Under 12 printed credit hours, or none printed: not checked for whole-term coverage.',
}

/** The plan's terms under their year headings, every row as printed. Year headings are not terms (#230). */
function PlanTerms({ terms }: { terms: TermCoverage[] }) {
  const groups: { heading: string | null; terms: TermCoverage[] }[] = []
  for (const t of terms) {
    const last = groups[groups.length - 1]
    if (last && last.heading === t.group) last.terms.push(t)
    else groups.push({ heading: t.group, terms: [t] })
  }
  return (
    <div className="grid gap-4">
      {groups.map((g, gi) => (
        <div key={`${g.heading ?? 'plan'}-${gi}`}>
          {g.heading && <h3 className="mb-2 text-sm font-bold text-ink">{g.heading}</h3>}
          <ul className="grid gap-2 sm:grid-cols-2">
            {g.terms.map((t) => (
              <li key={t.term} className={cx('rounded-xl border p-3 text-sm', t.covered ? 'border-go/40 bg-go-soft' : 'border-line')}>
                <div className="flex flex-wrap items-baseline justify-between gap-2">
                  <span className="font-semibold text-ink">
                    Term {t.term}: {t.label}
                  </span>
                  {t.creditHours != null && <span className="text-xs text-ink-3">{String(t.creditHours)} credit hours, as printed</span>}
                </div>
                {t.covered && <div className="mt-1 text-xs font-semibold text-go-strong">Fully covered by credit</div>}
                {t.notChecked && <div className="mt-1 text-xs text-ink-3">{NOT_CHECKED[t.notChecked]}</div>}
                <ul className="mt-2 grid gap-1 text-xs text-ink-2">
                  {t.rows.map((x, i) =>
                    x.kind === 'heading' ? (
                      <li key={i} className="pt-1 font-semibold text-ink">
                        {x.text}
                      </li>
                    ) : x.kind === 'subtotal' ? (
                      <li key={i} className="flex justify-between gap-3 text-ink-3">
                        <span>{x.text} (printed subtotal)</span>
                        <span className="shrink-0 tabular-nums">{String(x.credits)}</span>
                      </li>
                    ) : (
                      <li key={i} className="flex justify-between gap-3">
                        <span className="min-w-0 break-words">
                          {x.code ? <span className="font-semibold text-ink">{x.code}</span> : null}
                          {x.code ? (x.title ? ` ${x.title}` : '') : x.text}
                          {x.options.length > 0 && <span className="block text-ink-3">{x.choose > 1 ? `Choose ${x.choose} of` : 'Any one of'}: {x.options.join('; ')}</span>}
                          {x.milestone && <span className="block text-ink-3">Milestone: {x.milestone}</span>}
                          {x.note && <span className="block text-ink-3">Note: {x.note}</span>}
                        </span>
                        {x.credits != null && <span className="shrink-0 tabular-nums">{String(x.credits)}</span>}
                      </li>
                    ),
                  )}
                </ul>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  )
}

/** Design (#257): a table on file whose source prints no academic year says so; never "rejected" or "discontinued". */
export function notOnFileLabel(e: { verificationStatus: string | null; academicYearBasis?: string | null }): string {
  if (!e.verificationStatus) return 'Not on file'
  return /unlabeled/.test(e.academicYearBasis ?? '') ? 'Academic year unconfirmed' : 'On file, not yet verified'
}

function CreditRow({ c }: { c: CreditLine }) {
  const f = c.acceptance.value ? FIT[c.fit] : null
  return (
    <li className="rounded-xl bg-surface-2 p-3 text-sm">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <span className="font-semibold text-ink">
          {c.exam.name}
          {c.exam.score != null ? `, score ${c.exam.score}` : ', planned'}
        </span>
        {f ? <Pill tone={f.tone}>{f.label}</Pill> : <Pill tone="neutral">{notOnFileLabel(c.acceptance.evidence)}</Pill>}
      </div>
      {c.acceptance.value ? (
        <>
          {c.rows.length > 0 && (
            <ul className="mt-1 text-xs text-ink-2">
              {c.rows.map((x) => (
                <li key={`${x.term}-${x.item}`}>
                  Term {x.term}: {x.item}
                </li>
              ))}
            </ul>
          )}
          <p className="mt-1 text-xs text-ink-3">{c.hours.value != null ? `${c.hours.value} credit hours, from the school’s table.` : 'Credit hours not listed in the school’s table.'}</p>
        </>
      ) : (
        <p className="mt-1 text-xs text-ink-3">{c.acceptance.evidence.missing}</p>
      )}
    </li>
  )
}

function Missing({ e }: { e: Evidence }) {
  return <p className="text-sm text-ink-2">{e.missing ?? 'Not on file.'}</p>
}

function SourceNote({ e }: { e: Evidence }) {
  if (!e.sourceUrl) return null
  return (
    <a href={e.sourceUrl} target="_blank" rel="noreferrer" className="font-semibold text-ink-3 hover:text-ink hover:underline">
      Source{e.lastVerifiedAt ? `, verified ${formatShortDate(e.lastVerifiedAt)}` : ''}
    </a>
  )
}
