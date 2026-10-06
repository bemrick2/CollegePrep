import { Link } from 'react-router-dom'
import { useApp } from '../../lib/app'
import type { InstitutionComparison } from '../../lib/data/types'
import { Notice, PageLoading, Pill } from '../../components/ui'
import { PageHeader, Row, RowList, Section } from '../../components/layout'
import { useHomeState } from '../../lib/homeState'
import { meritAwards } from '../../lib/engine/merit'
import { fitSentence, schoolFit } from '../../lib/engine/programFit'
import { costPhrase, outlookFor } from '../parent/CostOutlook'
import { useInterests } from '../majors/useInterests'
import { useSavedComparison } from './useSavedComparison'
import { useMeritReference } from './useMeritReference'
import { useExamPlan } from './useExamPlan'
import { schoolLevers } from './schoolLevers'
import { CollegesTabs } from './CollegesTabs'
import { HomeStateControl } from './HomeStateControl'
import { POLICY_LABEL, RangeNote, academicFit, humanize } from './schoolBits'

const LEVER_ORDER: Record<string, number> = { on_track: 0, within_reach: 1, stretch: 2, available: 3, check: 4 }

/**
 * Compare answers the family's questions in order — what it costs, whether it's realistic, whether it has what the
 * student wants to study, merit, credit, and the next step — one school per row, each linking to its detail page.
 */
export function Compare() {
  const { activeStudent, viewer } = useApp()
  const cmp = useSavedComparison()
  const { homeState } = useHomeState()
  const merit = useMeritReference(activeStudent?.id)
  const interests = useInterests(activeStudent?.id).profile.interests
  const exams = useExamPlan(activeStudent?.id).exams
  const isStudent = !!viewer && activeStudent?.linked_user_id === viewer.userId
  const who = isStudent ? 'you' : (activeStudent?.display_name ?? 'your student')
  const exam = merit.exam
  const EXAM = exam.toUpperCase()

  const header = (
    <PageHeader kicker="Colleges & cost" title="Compare your colleges" actions={<CollegesTabs />}>
      Each question answered across your saved schools, from verified records only.
    </PageHeader>
  )

  if (cmp.loading && !cmp.data) return <PageLoading />
  if (cmp.error)
    return (
      <div className="grid gap-8">
        {header}
        <Notice tone="bad">{cmp.error.message}</Notice>
      </div>
    )

  const schools = (cmp.data ?? []).filter((c): c is InstitutionComparison & { institution: NonNullable<InstitutionComparison['institution']> } => c.found && !!c.institution)
  if (schools.length < 2)
    return (
      <div className="grid gap-8">
        {header}
        <Section divider={false}>
          <p className="max-w-xl text-[15px] text-ink-2">
            {schools.length === 0 ? 'Save at least two schools to compare them.' : 'Save one more school to compare.'}{' '}
            <Link to="/colleges" className="font-semibold text-brand hover:underline">
              Add a school
            </Link>
          </p>
        </Section>
      </div>
    )

  const outlooks = schools.map((c) => ({ c, o: outlookFor(c, homeState) }))
  const priced = outlooks.filter((x) => x.o.comparable && x.o.degreeTotal != null).sort((a, b) => a.o.degreeTotal! - b.o.degreeTotal!)
  const unpriced = outlooks.filter((x) => !(x.o.comparable && x.o.degreeTotal != null))
  const name = (c: InstitutionComparison) => c.institution!.display_name
  const detail = (c: InstitutionComparison) => `/colleges/${encodeURIComponent(c.institution_key)}`

  return (
    <div className="grid grid-cols-1 gap-10">
      {header}

      <Section id="cmp-cost" title="What would it cost?" subtitle="Published cost of attendance for your family, before aid" action={<HomeStateControl />}>
        <RowList>
          {[...priced, ...unpriced].map(({ c, o }, i) => {
            const cp = costPhrase(o)
            return (
              <Row
                key={c.institution_key}
                to={detail(c)}
                title={
                  <span className="flex flex-wrap items-center gap-2">
                    {name(c)}
                    {i === 0 && priced.length > 1 && <Pill tone="go">Lowest</Pill>}
                    {cmp.primary === c.institution_key && <Pill tone="brand">Top choice</Pill>}
                  </span>
                }
                meta={cp.note ?? cp.label}
                value={<span className="figure text-xl text-ink">{cp.amount ?? <span className="text-sm font-semibold text-ink-3">Not comparable</span>}</span>}
              />
            )
          })}
        </RowList>
        {priced.length > 1 && (
          <p className="mt-3 text-sm text-ink-2">
            {name(priced[priced.length - 1]!.c)} is {usd(priced[priced.length - 1]!.o.degreeTotal! - priced[0]!.o.degreeTotal!)} more than {name(priced[0]!.c)} at published prices.
            Aid can change the order.
          </p>
        )}
      </Section>

      <Section id="cmp-fit" title="Is it realistic?" subtitle={`${merit.reference ? `${merit.reference.value} ${EXAM}` : `Your ${EXAM}`} against the middle 50% of admitted students`}>
        {!merit.reference && (
          <p className="mb-3 text-sm text-ink-2">
            <Link to={isStudent ? '/student/goals' : '/parent/goals'} className="font-semibold text-brand hover:underline">
              Set a target {EXAM} score
            </Link>{' '}
            to compare against each school.
          </p>
        )}
        <RowList>
          {schools.map((c) => {
            const fit = academicFit(c, exam, merit.reference)
            const adm = (c.domains.admissions_metrics?.[0] ?? null) as Record<string, number | null> | null
            const lo = adm?.[`${exam}_25`]
            const hi = adm?.[`${exam}_75`]
            return (
              <Row
                key={c.institution_key}
                to={detail(c)}
                title={name(c)}
                meta={fit ? <RangeNote fit={fit} exam={exam} /> : lo != null && hi != null ? `Middle 50%: ${lo}–${hi} ${EXAM}` : 'No verified admissions data yet.'}
                value={fit ? <Pill tone={fit.where === 'below' ? 'warn' : 'go'}>{fit.where === 'below' ? 'Below' : fit.where === 'within' ? 'Within' : 'Above'}</Pill> : undefined}
              />
            )
          })}
        </RowList>
      </Section>

      <Section
        id="cmp-study"
        title={`Does it have what ${who} ${isStudent ? 'want' : 'wants'} to study?`}
        action={
          <Link to="/colleges/majors" className="font-semibold text-brand hover:underline">
            Explore majors
          </Link>
        }
      >
        {interests.length === 0 ? (
          <p className="text-sm text-ink-2">Save a few interests on Explore majors to check each school's verified programs.</p>
        ) : (
          <RowList>
            {schools.map((c) => {
              const f = schoolFit(c.domains, interests)
              return <Row key={c.institution_key} to={detail(c)} title={name(c)} meta={fitSentence(name(c), f) ?? 'No verified program list yet.'} />
            })}
          </RowList>
        )}
      </Section>

      <Section id="cmp-merit" title="Merit scholarships" subtitle={`Verified awards with a single published ${EXAM} minimum`}>
        <RowList>
          {schools.map((c) => {
            const m = meritAwards(c.domains.awards)
            const withMin = m.filter((a) => a.min[exam] != null)
            return (
              <Row
                key={c.institution_key}
                to={detail(c)}
                title={name(c)}
                meta={m.length ? `${m.length} verified merit ${m.length === 1 ? 'award' : 'awards'}, ${withMin.length} with a published ${EXAM} minimum` : 'No verified merit scholarships yet.'}
              />
            )
          })}
        </RowList>
      </Section>

      <Section
        id="cmp-credit"
        title="Credit that could shorten or lower the degree"
        action={
          <Link to="/colleges/paths" className="font-semibold text-brand hover:underline">
            Match exams on College paths
          </Link>
        }
      >
        <RowList>
          {schools.map((c) => {
            const policies = (c.domains.credit_policies ?? []) as { policy_kind?: string }[]
            return (
              <Row
                key={c.institution_key}
                to={detail(c)}
                title={name(c)}
                meta={policies.length ? policies.map((p) => POLICY_LABEL[String(p.policy_kind)] ?? humanize(String(p.policy_kind))).join(', ') : 'No verified credit policy yet.'}
              />
            )
          })}
        </RowList>
      </Section>

      <Section id="cmp-next" title="Best next step at each school" subtitle="The strongest verified way to lower that school's cost. Nothing is added up.">
        <RowList>
          {schools.map((c) => {
            const lever = [...schoolLevers(c, exams, exam, merit.reference)].sort((a, b) => (LEVER_ORDER[a.status] ?? 9) - (LEVER_ORDER[b.status] ?? 9))[0]
            return <Row key={c.institution_key} to={detail(c)} title={name(c)} meta={lever ? `${lever.title}. ${lever.detail}` : 'No verified cost levers yet.'} />
          })}
        </RowList>
      </Section>
    </div>
  )
}

const usd = (n: number) => n.toLocaleString(undefined, { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })
