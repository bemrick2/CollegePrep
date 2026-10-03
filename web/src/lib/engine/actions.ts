import type { BenchmarkSchedule } from './benchmark'

export type ActionTone = 'go' | 'warn' | 'info' | 'brand'

export interface ParentAction {
  key: string
  title: string
  detail: string
  to?: string
  tone: ActionTone
  /** Lower runs first. */
  rank: number
}

export interface SchoolFacts {
  name: string
  levers: string[] // 'AP credit', 'CLEP credit', 'IB credit', 'Dual enrollment', ...
  awards: { name: string; act_min?: number | null; sat_min?: number | null }[]
}

export interface ActionInput {
  name: string
  exam: 'act' | 'sat'
  linked: boolean
  benchmarks: number
  schedule: BenchmarkSchedule
  /** Weakest areas from practice: knowledge first, then pacing. */
  focus: { section: string; label: string; kind: 'knowledge' | 'pacing'; detail: string }[]
  behind: { done: number; goal: number; expected: number } | null
  idleDays: number | null
  goals: string[]
  targetScore: number | null
  /** Official (or explicitly self-reported) composite. Practice estimates must never be compared with thresholds. */
  officialScore: { composite: number; selfReported: boolean } | null
  schools: SchoolFacts[]
}

const EXAM = { act: 'ACT', sat: 'SAT' } as const

/**
 * "What should we do next?" — a short, prioritised list built only from recorded practice and verified college
 * records. Merit thresholds are compared with the family's target or an official score, never a practice
 * estimate, and never stated as eligibility.
 */
export function parentActions(i: ActionInput, max = 5): ParentAction[] {
  const out: ParentAction[] = []
  const exam = EXAM[i.exam]
  if (!i.linked) out.push({ key: 'invite', rank: 0, tone: 'brand', title: `Invite ${i.name} to log in`, detail: 'Practice happens on their own login. Create a code on the Household page.', to: '/parent/household' })
  if (i.benchmarks === 0) out.push({ key: 'bench', rank: 1, tone: 'go', title: `${i.name} should take the starting benchmark`, detail: 'About 30 minutes. It sets the baseline the daily plan depends on.' })
  else if (i.schedule.inDays === 0)
    out.push({ key: 'bench', rank: 2, tone: 'go', title: `Take the next ${i.schedule.kind === 'full' ? 'full' : 'mini'} benchmark`, detail: i.schedule.overdueDays > 0 ? `Due ${i.schedule.overdueDays} days ago. It shows what changed since the last one.` : 'Due now. It shows what changed since the last one.' })

  const top = i.focus[0]
  if (top) out.push({ key: `focus-${top.section}`, rank: 3, tone: 'warn', title: `Focus on ${exam} ${top.label} this week`, detail: top.detail })
  if (i.behind) out.push({ key: 'behind', rank: 4, tone: 'warn', title: "Behind on this week's goal", detail: `${i.behind.done} of ${i.behind.goal} questions; about ${i.behind.expected} would be on track by today.` })
  if (i.linked && i.idleDays !== null && i.idleDays >= 3) out.push({ key: 'idle', rank: 4, tone: 'warn', title: `No practice in ${i.idleDays} days`, detail: 'A quick check-in usually restarts the habit.' })

  if (i.schools.length === 0) {
    out.push({ key: 'schools', rank: 5, tone: 'info', title: 'Add target colleges', detail: 'Pick up to four to see verified costs, credit policies and scholarships.', to: '/colleges' })
    return finish(out, max)
  }

  // Merit: a published numeric threshold above the reference score (target or official), nearest first.
  const ref = i.officialScore?.composite ?? i.targetScore
  const key = i.exam === 'act' ? 'act_min' : 'sat_min'
  const merits = i.schools
    .flatMap((s) => s.awards.map((a) => ({ school: s.name, award: a.name, min: a[key] ?? null })))
    .filter((m): m is { school: string; award: string; min: number } => m.min != null)
  if (merits.length && ref != null) {
    const reach = merits.filter((m) => m.min > ref).sort((a, b) => a.min - b.min)[0]
    const met = merits.filter((m) => m.min <= ref).sort((a, b) => b.min - a.min)[0]
    const basis = i.officialScore ? (i.officialScore.selfReported ? 'self-reported score (unverified)' : 'official score') : 'target'
    if (reach)
      out.push({ key: 'merit', rank: 6, tone: 'info', title: `${reach.school}: ${reach.award} lists ${exam} ${reach.min}+`, detail: `That's ${reach.min - ref} above the ${basis} of ${ref}. Published criteria only — not an eligibility decision.`, to: '/colleges' })
    else if (met)
      out.push({ key: 'merit', rank: 6, tone: 'info', title: `${met.school}: ${met.award} lists ${exam} ${met.min}+`, detail: `The ${basis} of ${ref} meets the published test criterion. Other criteria (GPA, deadlines) still apply — not an eligibility decision.`, to: '/colleges' })
  }

  const credit = i.schools.find((s) => s.levers.some((l) => /AP|CLEP|IB/.test(l)))
  if (credit && (i.goals.includes('college_credit') || i.goals.includes('lower_cost') || out.length < 4))
    out.push({ key: 'credit', rank: 7, tone: 'info', title: `Review ${credit.name}'s verified ${credit.levers.filter((l) => /AP|CLEP|IB/.test(l)).join(', ')}`, detail: 'Exam scores that earn credit can shorten time to degree.', to: '/colleges' })
  const dual = i.schools.find((s) => s.levers.some((l) => /dual/i.test(l)))
  if (dual && (i.goals.includes('college_credit') || i.goals.includes('lower_cost') || out.length < 4))
    out.push({ key: 'dual', rank: 8, tone: 'info', title: `Check ${dual.name}'s verified dual-enrollment policy`, detail: 'See which high-school college courses it accepts before enrolling.', to: '/colleges' })
  out.push({ key: 'compare', rank: 9, tone: 'info', title: 'Compare your colleges side by side', detail: 'Verified costs, scholarships and credit policies.', to: '/colleges' })
  return finish(out, max)
}

function finish(out: ParentAction[], max: number) {
  return out.sort((a, b) => a.rank - b.rank).slice(0, max)
}
