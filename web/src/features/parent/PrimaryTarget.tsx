import { Link } from 'react-router-dom'
import type { Student } from '../../lib/data/types'
import { useSavedComparison, COMPARE_YEAR } from '../colleges/useSavedComparison'
import { useMeritReference } from '../colleges/useMeritReference'
import { useExamPlan } from '../colleges/useExamPlan'
import { schoolLevers } from '../colleges/schoolLevers'
import { CostLeverList } from '../colleges/CostLeverList'
import { outlookFor } from './CostOutlook'
import { useHomeState } from '../../lib/homeState'
import { ArrowRight, Flag } from '../../components/icons'
import { ButtonLink, Card, CardHeader } from '../../components/ui'

const usd = (n: number) => n.toLocaleString(undefined, { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })

/**
 * The family's primary target school (CR-12): its published 4-year cost and the top ways to lower it. Renders
 * nothing where a primary can't be stored yet (live mode until the backend lands), so the dashboard never shows
 * a control that can't save.
 */
export function PrimaryTarget({ student }: { student: Student }) {
  const cmp = useSavedComparison(COMPARE_YEAR)
  const { exam, reference } = useMeritReference(student.id)
  const plan = useExamPlan(student.id)
  const { homeState } = useHomeState()
  if (!cmp.canSetPrimary || cmp.keys.length === 0 || (cmp.loading && !cmp.data)) return null
  const c = cmp.data?.find((x) => x.institution_key === cmp.primary && x.found)
  const name = student.display_name

  if (!c)
    return (
      <Card className="p-5">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="min-w-0">
            <h2 className="flex items-center gap-2 font-semibold text-ink">
              <Flag size={18} /> Choose a primary target
            </h2>
            <p className="mt-0.5 text-sm text-ink-2">Pick the saved school {name} most wants to attend. The plan then leads with its cost and scholarships.</p>
          </div>
          <ButtonLink to="/colleges/paths" variant="brand" size="sm">
            Choose on College paths
          </ButtonLink>
        </div>
      </Card>
    )

  const o = outlookFor(c, homeState)
  return (
    <Card className="overflow-hidden ring-2 ring-brand">
      <CardHeader
        title={
          <span className="flex items-center gap-2">
            <Flag size={18} /> Primary target: {o.name}
          </span>
        }
        subtitle={o.degreeTotal != null ? `${usd(o.degreeTotal)} published cost of attendance over 4 years, before aid` : `No verified ${COMPARE_YEAR} cost yet`}
      />
      <div className="grid gap-3 p-5 pt-3 text-sm">
        <div className="text-xs font-bold uppercase tracking-wide text-ink-3">Ways to lower this cost</div>
        <CostLeverList levers={schoolLevers(c, plan.exams, exam, reference)} max={3} />
        <Link to="/colleges/paths" className="inline-flex items-center gap-1 font-semibold text-brand hover:underline">
          See the full path <ArrowRight size={16} />
        </Link>
      </div>
    </Card>
  )
}
