import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { Button, Card, CardHeader, Field, Notice, Pill, inputClass } from '../../components/ui'
import { InviteCode } from '../onboarding/InviteCode'
import { PlanCard } from './PlanCard'
import { StudentInvite } from './StudentInvite'
import { GRADES, gradeLabel, graduationYearFor } from '../onboarding/options'
import { DEMO_STUDENT } from '../../lib/data/demo/demoSource'

export function Household() {
  const { ctx, source, refresh, mode, switchDemoPersona, setActiveStudentId } = useApp()
  const navigate = useNavigate()
  const household = ctx?.households[0]
  const me = ctx?.memberships.find((m) => m.household_id === household?.id)
  const [codes, setCodes] = useState<Record<string, string>>({})
  const [adding, setAdding] = useState(false)
  const [name, setName] = useState('')
  const [grade, setGrade] = useState<number>(9)
  const [error, setError] = useState<string | null>(null)

  if (!household) return <Notice>No household yet.</Notice>

  const invite = async (key: string, role: 'student' | 'guardian', studentId?: string) => {
    setError(null)
    try {
      const code = await source.createInvitation(household.id, role, studentId)
      setCodes((c) => ({ ...c, [key]: code }))
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Could not create an invite')
    }
  }

  const add = async () => {
    setError(null)
    try {
      const id = await source.addStudent(household.id, name, graduationYearFor(grade), grade)
      setName('')
      setAdding(false)
      setActiveStudentId(id)
      await refresh()
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Could not add student')
    }
  }

  const tryAsStudent = async (code: string) => {
    await switchDemoPersona('student')
    navigate(`/join#t=${encodeURIComponent(code)}`)
  }

  return (
    <div className="grid max-w-3xl gap-5">
      <div>
        <p className="text-sm text-ink-3">Household</p>
        <h1 className="display text-[30px] font-semibold text-ink">{household.name}</h1>
        <p className="mt-1 text-sm text-ink-3">Time zone: {household.time_zone}</p>
      </div>
      {error && <Notice tone="bad">{error}</Notice>}
      {me?.role === 'guardian' && <PlanCard householdId={household.id} />}

      <Card>
        <CardHeader
          title="Students"
          action={
            me?.can_manage_students && (
              <Button size="sm" variant="secondary" onClick={() => setAdding((a) => !a)}>
                {adding ? 'Cancel' : 'Add student'}
              </Button>
            )
          }
        />
        {adding && (
          <div className="grid gap-4 border-b border-line p-5 sm:grid-cols-[1fr_auto_auto] sm:items-end">
            <Field label="First name" htmlFor="new-student">
              <input id="new-student" className={inputClass} value={name} onChange={(e) => setName(e.target.value)} />
            </Field>
            <Field label="Grade" htmlFor="new-grade">
              <select id="new-grade" className={inputClass} value={grade} onChange={(e) => setGrade(Number(e.target.value))}>
                {GRADES.map((g) => (
                  <option key={g} value={g}>
                    {g}
                  </option>
                ))}
              </select>
            </Field>
            <Button disabled={!name.trim()} onClick={() => void add()} className="h-12">
              Add
            </Button>
          </div>
        )}
        <ul className="divide-y divide-line">
          {ctx!.students.map((s) => (
            <li key={s.id} className="grid gap-3 px-5 py-4">
              <div className="flex flex-wrap items-center gap-2">
                <span className="font-semibold text-ink">{s.display_name}</span>
                <span className="text-sm text-ink-3">
                  {gradeLabel(s.grade_level)}
                  {s.graduation_year ? ` · class of ${s.graduation_year}` : ''}
                </span>
                <span className="ml-auto">{s.linked_user_id ? <Pill tone="go">Has login</Pill> : <Pill tone="warn">Not linked yet</Pill>}</span>
              </div>
              {!s.linked_user_id && me?.can_manage_students && (
                <StudentInvite householdId={household.id} student={s} onTryDemo={(code) => void tryAsStudent(code)} />
              )}
            </li>
          ))}
        </ul>
      </Card>

      <Card>
        <CardHeader title="Guardians" subtitle="Another parent or guardian can view progress and set goals." />
        <div className="p-5">
          <ul className="mb-4 grid gap-2 text-sm">
            {ctx!.memberships
              .filter((m) => m.role === 'guardian')
              .map((m) => (
                <li key={m.user_id} className="flex items-center gap-2">
                  <span className="font-semibold text-ink">You</span>
                  {m.can_manage_billing && <Pill tone="brand">Billing</Pill>}
                  {m.can_manage_members && <Pill tone="brand">Manages members</Pill>}
                </li>
              ))}
          </ul>
          {me?.can_manage_members &&
            (codes.guardian ? (
              <InviteCode token={codes.guardian} />
            ) : (
              <Button size="sm" variant="secondary" onClick={() => void invite('guardian', 'guardian')}>
                Invite a guardian
              </Button>
            ))}
          <p className="mt-4 text-xs text-ink-3">
            The person who pays for a subscription is managed separately from guardian and student roles. Students keep their own practice history if they leave a household.
          </p>
        </div>
      </Card>
      {mode === 'demo' && ctx!.students.some((s) => s.linked_user_id === DEMO_STUDENT) && (
        <p className="text-xs text-ink-3">Demo: use “View as student” in the top bar to see the student side.</p>
      )}
    </div>
  )
}
