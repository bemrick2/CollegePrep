import type { ExamFamily } from '../../lib/data/types'
import { formatShortDate } from '../../lib/engine/dates'
import { WEEKDAY_LABEL, type FirstWeek } from '../../lib/engine/firstWeek'
import { Button, ButtonLink } from '../../components/ui'
import { StudentInvite } from '../parent/StudentInvite'
import { StepFrame } from './Stepper'
import { WeekPreview } from './SetupScreens'
import { EXAM_NAME } from './options'
import { FirstSteps } from './FirstSteps'
import type { Role } from './SetupScreens'

/**
 * What setup produced, made actionable: the one next assignment and the weekly commitment. A target is shown as a
 * goal only. No score is predicted and no improvement is promised.
 */
export function SetupResult(p: {
  role: Role
  name: string
  studentId: string | null
  householdId: string | null
  exam: ExamFamily
  weekly: number | null
  minutes: number | null
  studyDays: number[]
  target: number | null
  setByGuardian: boolean
  week: FirstWeek | null
  baseline: { questions: number; minutes: number } | null
  needsBaseline: boolean
  timeZone: string
  benchmarkScheduledFor: string | null
  onContinue: () => void
}) {
  const parent = p.role === 'parent'
  const who = parent ? p.name || 'your student' : 'you'
  const days = [...p.studyDays].sort().map((d) => WEEKDAY_LABEL[d - 1]).join(', ')
  const next = p.week?.next
  return (
    <StepFrame
      step={1}
      total={1}
      hideProgress
      title={parent ? `${p.name || 'Your student'} is set up` : `You're set${p.name ? `, ${p.name}` : ''}`}
      footer={
        parent || p.needsBaseline ? (
          <Button size="lg" block variant={parent ? 'go' : 'secondary'} onClick={p.onContinue}>
            {parent ? 'Go to your dashboard' : 'Go to home'}
          </Button>
        ) : (
          <div className="grid gap-3">
            <ButtonLink to="/student/practice" size="lg" block>
              Start today's practice
            </ButtonLink>
            <button type="button" onClick={p.onContinue} className="text-center text-sm font-semibold text-ink-2 hover:text-ink">
              Not now, go to home
            </button>
          </div>
        )
      }
    >
      {p.needsBaseline && p.studentId ? (
        <>
          <h2 className="mb-2 text-sm font-semibold text-ink-2">{parent ? `How ${p.name || 'your student'} can start` : 'Two ways to start'}</h2>
          <FirstSteps
            studentId={p.studentId}
            exam={p.exam}
            baseline={p.baseline}
            scheduledFor={p.benchmarkScheduledFor}
            timeZone={p.timeZone}
            canStart={!parent}
            name={p.name || 'your student'}
          />
          {parent && <p className="mt-2 text-sm text-ink-2">Practice happens on {p.name || 'your student'}'s own login. Invite them below.</p>}
        </>
      ) : (
        <section aria-labelledby="next-heading" className="rounded-2xl border-2 border-go bg-go-soft p-4">
          <h2 id="next-heading" className="text-sm font-semibold text-ink-2">
            {parent ? `${p.name || 'Your student'}'s next assignment` : 'Your next assignment'}
          </h2>
          {next?.kind === 'practice' ? (
            <p className="mt-1 text-lg font-semibold text-ink">
              Practice · {formatShortDate(next.date)}
              <span className="block text-sm font-normal text-ink-2">
                {next.questions} questions, {next.minutes}-minute session
              </span>
            </p>
          ) : (
            <p className="mt-1 text-lg font-semibold text-ink">Today's practice set</p>
          )}
        </section>
      )}

      <section aria-labelledby="commit-heading" className="mt-5">
        <h2 id="commit-heading" className="text-[15px] font-semibold text-ink">
          Weekly commitment{p.setByGuardian ? ' (set by your parent or guardian)' : ''}
        </h2>
        <dl className="mt-2 grid gap-1 text-sm">
          <Row label="Goal">{p.weekly ? `${p.weekly} questions a week, Monday to Sunday` : 'No weekly goal set yet'}</Row>
          {days && <Row label="Study days">{days}</Row>}
          {p.minutes && <Row label="Session">{p.minutes} minutes</Row>}
          <Row label="Test">{EXAM_NAME[p.exam]}</Row>
          {p.target != null && <Row label="Goal score">{p.target} (a goal, not a prediction)</Row>}
        </dl>
        {!p.weekly && p.setByGuardian && <p className="mt-2 text-sm text-ink-3">Ask your parent or guardian to set a weekly goal. Until then, practise whenever you can.</p>}
      </section>

      {p.week && p.studyDays.length > 0 && (
        <div className="mt-5">
          <WeekPreview week={p.week} />
        </div>
      )}

      {parent && p.householdId && p.studentId && (
        <section aria-labelledby="invite-heading" className="mt-6">
          <h2 id="invite-heading" className="text-[15px] font-semibold text-ink">
            Invite {who}
          </h2>
          <p className="mt-1 text-sm text-ink-2">Their history stays on their own login. Email an invitation or copy the link. You can also do this later from Household.</p>
          <div className="mt-3">
            <StudentInvite showTitle={false} householdId={p.householdId} student={{ id: p.studentId, display_name: p.name || 'your student' }} />
          </div>
        </section>
      )}
    </StepFrame>
  )
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div className="flex gap-3">
      <dt className="w-24 shrink-0 text-ink-3">{label}</dt>
      <dd className="text-ink">{children}</dd>
    </div>
  )
}
