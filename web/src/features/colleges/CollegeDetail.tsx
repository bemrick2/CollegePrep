import { useEffect, useState } from 'react'
import { Link, useLocation, useParams } from 'react-router-dom'
import { useApp, useAsync } from '../../lib/app'
import type { CostRecord } from '../../lib/data/types'
import { Button, Notice, PageLoading, Segmented, cx } from '../../components/ui'
import { Figure, PageHeader, Row, RowList, Section, compactUsd } from '../../components/layout'
import { ChevronLeft } from '../../components/icons'
import { useHomeState } from '../../lib/homeState'
import { pickCost } from '../../lib/engine/residency'
import { meritAwards } from '../../lib/engine/merit'
import { fitSentence, schoolFit } from '../../lib/engine/programFit'
import { costPhrase, outlookFor } from '../parent/CostOutlook'
import { SchoolFitRow } from '../majors/SchoolFitRow'
import { useInterests } from '../majors/useInterests'
import { useSavedSchools } from './useSavedSchools'
import { useMeritReference } from './useMeritReference'
import { useExamPlan } from './useExamPlan'
import { schoolLevers } from './schoolLevers'
import { CostLeverList } from './CostLeverList'
import { HomeStateControl } from './HomeStateControl'
import { CONTROL_LABEL, DOMAIN_LABEL, LEVEL_LABEL, Missing, POLICY_LABEL, RangeNote, SourceLink, academicFit, humanize } from './schoolBits'

const YEARS = ['2026-27', '2025-26']
const usd = (n: number | null | undefined) => (n == null ? null : n.toLocaleString(undefined, { style: 'currency', currency: 'USD', maximumFractionDigits: 0 }))
const RESIDENCY_LABEL: Record<string, string> = { in_state: 'In-state', out_of_state: 'Out-of-state', not_applicable: 'All students', in_district: 'In-district' }

/**
 * One college, answer first: what it would cost this family, then whether it fits academically and by interest,
 * how to lower the cost, and the verified details underneath.
 */
export function CollegeDetail() {
  const { key = '' } = useParams()
  const { source, activeStudent, viewer } = useApp()
  const [year, setYear] = useState(YEARS[0]!)
  const res = useAsync(() => source.compareInstitutions([key], year), [source, key, year])
  const saved = useSavedSchools()
  const { homeState } = useHomeState()
  const merit = useMeritReference(activeStudent?.id)
  const interests = useInterests(activeStudent?.id).profile.interests
  const exams = useExamPlan(activeStudent?.id).exams
  const isStudent = !!viewer && activeStudent?.linked_user_id === viewer.userId
  const who = isStudent ? 'you' : (activeStudent?.display_name ?? 'your student')

  const c = res.data?.[0]
  // "View all …" links from Compare land on the matching section once the record has loaded.
  const { hash } = useLocation()
  useEffect(() => {
    if (hash && c) document.getElementById(hash.slice(1))?.scrollIntoView?.({ block: 'start' })
  }, [hash, !!c]) // eslint-disable-line react-hooks/exhaustive-deps
  if (res.loading && !res.data) return <PageLoading />
  if (res.error) return <Notice tone="bad">{res.error.message}</Notice>
  if (!c || !c.found)
    return (
      <div className="grid gap-4">
        <BackLink />
        <Notice tone="neutral" title="We don't have a verified record for this school">
          It may be listed under a different name. <Link to="/colleges" className="font-semibold underline">Search colleges</Link>
        </Notice>
      </div>
    )

  const inst = c.institution!
  const o = outlookFor(c, homeState)
  const cp = costPhrase(o)
  const isSaved = saved.keys.includes(key)
  const fit = academicFit(c, merit.exam, merit.reference)
  const program = interests.length ? schoolFit(c.domains, interests) : null
  const levers = schoolLevers(c, exams, merit.exam, merit.reference)
  const merits = meritAwards(c.domains.awards)
  const awards = (c.domains.awards ?? []) as Record<string, unknown>[]
  const credit = (c.domains.credit_policies ?? []) as Record<string, unknown>[]
  const appeals = (c.domains.appeals ?? []) as Record<string, unknown>[]
  const adm = (c.domains.admissions_metrics?.[0] ?? null) as Record<string, number | string | null> | null
  const exam = merit.exam

  return (
    <div className="grid grid-cols-1 gap-10">
      <div className="grid gap-4">
        <BackLink />
        <PageHeader
          kicker={[[inst.city, inst.state_code].filter(Boolean).join(', '), inst.control && CONTROL_LABEL[inst.control], inst.level && LEVEL_LABEL[inst.level]].filter(Boolean).join(' · ')}
          title={inst.display_name}
          actions={
            <>
              {isSaved && saved.canSetPrimary && (
                <Button variant="secondary" size="sm" aria-pressed={saved.primary === key} onClick={() => void saved.setPrimary(saved.primary === key ? null : key)}>
                  {saved.primary === key ? 'Top choice ✓' : 'Make top choice'}
                </Button>
              )}
              {isSaved ? (
                <Button variant="ghost" size="sm" onClick={() => void saved.remove(key)}>
                  Remove from your colleges
                </Button>
              ) : (
                <Button variant="brand" size="sm" disabled={saved.keys.length >= saved.max} onClick={() => void saved.add(key)}>
                  Save to your colleges
                </Button>
              )}
            </>
          }
        />
      </div>

      <div className="grid gap-10 lg:grid-cols-[minmax(0,1.2fr)_minmax(0,1fr)] lg:gap-14">
        <div>
          {cp.amount ? (
            <Figure size="xl" value={compactUsd(o.degreeTotal!)} label={`${o.level === 'two_year' ? 'Two' : 'Four'}-year cost for your family`} sub={`${cp.amount} ${cp.label}`} />
          ) : (
            <Figure size="xl" tone="muted" value="—" label="Cost for your family" sub={cp.label} />
          )}
          {cp.note && <p className="mt-2 text-sm text-warn">{cp.note}</p>}
          <HomeStateControl className="mt-4" />
        </div>
        <section aria-labelledby="glance-heading">
          <h2 id="glance-heading" className="text-[17px] font-bold text-ink">
            At a glance
          </h2>
          <RowList className="mt-2">
            <Row title="Academic fit" meta={fit ? <RangeNote fit={fit} exam={exam} /> : adm ? `Set a target ${exam.toUpperCase()} score to compare.` : 'No verified admissions data yet.'} />
            <Row
              title={`What ${who} wants to study`}
              meta={program ? fitSentence(inst.display_name, program) : <Link to="/colleges/majors" className="font-semibold text-brand hover:underline">Save interests to check</Link>}
            />
            <Row
              title="Merit scholarships"
              meta={merits.length ? `${merits.length} verified, ${merits.filter((m) => m.min[exam] != null).length} with a single published ${exam.toUpperCase()} minimum` : 'No verified merit scholarships yet.'}
            />
            <Row title="Credit you could bring" meta={credit.length ? credit.map((p) => POLICY_LABEL[String(p.policy_kind)] ?? humanize(String(p.policy_kind))).join(', ') : 'No verified credit policy yet.'} />
          </RowList>
        </section>
      </div>

      <Section id="lower-heading" title="Ways to lower the cost" subtitle="From this school's verified records. Nothing is added up: awards may not combine and aid depends on family finances.">
        <CostLeverList levers={levers} />
      </Section>

      {program && (
        <Section id="study-heading" title={`Does it have what ${who} wants to study?`} action={<Link to="/colleges/majors" className="font-semibold text-brand hover:underline">Explore majors</Link>}>
          <SchoolFitRow compact name={inst.display_name} domains={c.domains} interests={interests} />
        </Section>
      )}

      <Section id="adm-heading" title="Admissions" subtitle="Middle 50% of admitted students" action={<SourceLink href={adm?.source_url as string | undefined} verified={adm?.last_verified_at as string | undefined} />}>
        {!adm ? (
          <Missing what="admissions data" />
        ) : (
          <div className="grid grid-cols-3 gap-6">
            <Figure size="md" value={adm.act_25 != null ? `${adm.act_25}–${adm.act_75}` : '—'} label="ACT" />
            <Figure size="md" value={adm.sat_25 != null ? `${adm.sat_25}–${adm.sat_75}` : '—'} label="SAT" />
            <Figure size="md" value={typeof adm.admit_rate === 'number' ? `${Math.round(adm.admit_rate <= 1 ? adm.admit_rate * 100 : adm.admit_rate)}%` : '—'} label="Admit rate" />
          </div>
        )}
      </Section>

      <Section id="awards-heading" title="Scholarships" subtitle={awards.length ? `${awards.length} verified` : undefined}>
        {awards.length === 0 ? <Missing what="scholarships" /> : <AwardList awards={awards} />}
      </Section>

      <Section
        id="credit-heading"
        title="Credit you could bring"
        action={
          credit.length > 0 && (
            <Link to="/colleges/paths" className="font-semibold text-brand hover:underline">
              Match exams on College paths
            </Link>
          )
        }
      >
        {credit.length === 0 ? (
          <Missing what="credit policy" />
        ) : (
          <RowList>
            {credit.map((p, i) => (
              <Row
                key={i}
                title={POLICY_LABEL[String(p.policy_kind)] ?? humanize(String(p.policy_kind))}
                meta={typeof p.equivalency_count === 'number' && p.equivalency_count > 0 ? `${p.equivalency_count} exams or courses in the published table` : 'Published policy'}
                value={<SourceLink href={String(p.policy_url ?? p.source_url)} />}
              />
            ))}
          </RowList>
        )}
      </Section>

      <CostBreakdown costs={(c.domains.costs ?? []) as unknown as CostRecord[]} schoolState={inst.state_code} level={inst.level ?? null} year={year} onYear={setYear} />

      <Section id="appeals-heading" title="Financial-aid appeals">
        {appeals.length === 0 ? (
          <Missing what="appeal process" />
        ) : (
          <ul className="grid gap-1.5 text-sm">
            {appeals.map((a, i) => (
              <li key={i} className="flex items-center gap-2">
                <span className={cx('h-1.5 w-1.5 rounded-full', a.offered ? 'bg-go' : 'bg-ink-3')} aria-hidden />
                <span className="text-ink-2">{humanize(String(a.appeal_kind))}</span>
              </li>
            ))}
          </ul>
        )}
      </Section>

      <Section id="unverified-heading" title="Not verified yet">
        <p className="text-sm text-ink-2">
          {c.missing_domains.length ? `For ${c.academic_year}: ${c.missing_domains.map((d) => DOMAIN_LABEL[d] ?? d).join(', ')}.` : `Every record type we track has a verified ${c.academic_year} entry.`}
        </p>
        {inst.net_price_calculator_url && (
          <a href={inst.net_price_calculator_url} target="_blank" rel="noreferrer" className="mt-2 inline-block text-sm font-semibold text-brand hover:underline">
            Estimate your net price on the school's calculator
          </a>
        )}
      </Section>
    </div>
  )
}

function BackLink() {
  return (
    <Link to="/colleges" className="inline-flex items-center gap-1 text-sm font-semibold text-ink-2 hover:text-ink">
      <ChevronLeft size={16} /> Your colleges
    </Link>
  )
}

function AwardList({ awards }: { awards: Record<string, unknown>[] }) {
  const [all, setAll] = useState(false)
  const shown = all ? awards : awards.slice(0, 6)
  return (
    <>
      <RowList>
        {shown.map((a, i) => (
          <li key={i} className="py-3">
            <a href={String(a.source_url)} target="_blank" rel="noreferrer" className="font-semibold text-ink hover:underline">
              {String(a.award_name)}
            </a>
            <p className="mt-0.5 text-sm text-ink-2">{a.award_amount_text ? String(a.award_amount_text) : (usd(a.award_max as number) ?? 'Amount not published')}</p>
            {a.test_requirement || a.gpa_requirement ? (
              <p className="mt-0.5 text-sm text-ink-3">{[a.test_requirement ? String(a.test_requirement) : null, a.gpa_requirement && a.gpa_requirement !== 'N/A' ? `GPA: ${String(a.gpa_requirement)}` : null].filter(Boolean).join(' · ')}</p>
            ) : null}
          </li>
        ))}
      </RowList>
      {awards.length > 6 && (
        <button type="button" onClick={() => setAll((v) => !v)} className="mt-2 text-sm font-semibold text-brand hover:underline">
          {all ? 'Show fewer' : `Show all ${awards.length}`}
        </button>
      )}
    </>
  )
}

function CostBreakdown({ costs, schoolState, level, year, onYear }: { costs: CostRecord[]; schoolState: string | null; level: string | null; year: string; onYear: (y: string) => void }) {
  const { homeState } = useHomeState()
  const picked = pickCost(costs, schoolState, homeState)
  const [residency, setResidency] = useState(picked.cost?.residency ?? costs[0]?.residency ?? '')
  useEffect(() => {
    if (picked.cost) setResidency(picked.cost.residency)
  }, [homeState]) // eslint-disable-line react-hooks/exhaustive-deps
  const [years, setYears] = useState(level === 'two_year' ? 2 : 4)
  const cost = costs.find((x) => x.residency === residency) ?? costs[0]
  return (
    <Section
      id="breakdown-heading"
      title="Cost breakdown"
      subtitle="Published cost of attendance, before aid"
      action={<Segmented label="Academic year" value={year} onChange={onYear} options={YEARS.map((y) => ({ value: y, label: y }))} />}
    >
      {costs.length === 0 || !cost ? (
        <Missing what="cost of attendance for this year" />
      ) : (
        <div className="grid gap-5 md:grid-cols-[1fr_1fr] md:gap-10">
          <div className="grid content-start gap-4">
            {costs.length > 1 && (
              <Segmented label="Residency" value={residency} onChange={setResidency} options={costs.map((x) => ({ value: x.residency, label: RESIDENCY_LABEL[x.residency] ?? x.residency }))} />
            )}
            <Figure size="lg" value={usd(cost.total_cost_of_attendance) ?? '—'} label="Per year" sub={<SourceLink href={cost.source_url} verified={cost.last_verified_at} />} />
            {cost.total_cost_of_attendance != null && (
              <div className="flex flex-wrap items-center gap-3 text-sm">
                <span className="font-semibold text-ink">{usd(Math.round(cost.total_cost_of_attendance * years))}</span>
                <span className="text-ink-3">over</span>
                <Segmented label="Years to degree (your assumption)" value={years} onChange={setYears} options={[2, 3, 3.5, 4, 5].map((y) => ({ value: y, label: String(y) }))} />
                <span className="text-ink-3">years (your assumption)</span>
              </div>
            )}
          </div>
          <dl className="grid grid-cols-[1fr_auto] gap-x-6 gap-y-2 self-start text-sm">
            <Line k="Tuition" v={cost.tuition} />
            <Line k="Fees" v={cost.mandatory_fees} />
            <Line k="Housing & food" v={cost.on_campus_food_housing ?? (cost.room != null && cost.board != null ? cost.room + cost.board : null)} />
            <Line k="Books" v={cost.books_supplies} />
            <Line k="Transport" v={cost.transportation} />
            <Line k="Personal" v={cost.personal_misc} />
          </dl>
        </div>
      )}
    </Section>
  )
}

function Line({ k, v }: { k: string; v: number | null | undefined }) {
  return (
    <>
      <dt className="text-ink-2">{k}</dt>
      <dd className={cx('text-right tabular', v != null ? 'font-semibold text-ink' : 'text-ink-3')}>{usd(v) ?? '—'}</dd>
    </>
  )
}
