// Planning engine data structures (docs/product/PLANNING_ENGINE.md §2). Plain values: the same in demo, live and tests.
import type { SavedInterest } from '../interests'
import type { ExamFamily, ExamMatch, PlannedExam } from '../examCredit'
import type { PotentialSaving } from '../costProjection'

export type LivingArrangement = 'on_campus' | 'off_campus' | 'with_family'

/** What the family told us. Every value is the family's answer, never a record. */
export interface PlanningProfile {
  gradeLevel: number | null
  graduationYear: number | null
  /** CR-15: kept in the browser today. */
  homeState: string | null
  interests: SavedInterest[]
  /** CR-10: kept on the device today. */
  exams: PlannedExam[]
  livingArrangement: LivingArrangement | null
}

export interface PlanningTarget {
  institutionKey: string
  programKey: string
}

/**
 * verified: a fact from a record whose verification_status is "verified".
 * estimate: arithmetic over verified values only, with `method` saying how.
 * missing: not on file (including records on file but not verified); `missing` says exactly what.
 * family: a value the family entered.
 */
export type EvidenceState = 'verified' | 'estimate' | 'missing' | 'family'

export interface Evidence {
  state: EvidenceState
  sourceUrl: string | null
  verificationStatus: string | null
  lastVerifiedAt: string | null
  /** The year the source publishes for (catalog_year or academic_year), never the student's entry year. */
  publishedYear: string | null
  method?: string
  missing?: string
}

export interface Line<T> {
  value: T | null
  evidence: Evidence
}

export type CreditFit = 'applies' | 'partly' | 'accepted_not_in_plan' | 'elective_only' | 'unknown' | 'none'

export interface PlanRow {
  term: number
  label: string
  item: string
  credits: number | string | null
}

export interface CreditLine {
  exam: PlannedExam
  /** The school's table result (examCredit); value null when no verified table for this family is on file. */
  acceptance: Line<ExamMatch>
  /** Where awarded credit lands in the verified plan. "none" when the score earns nothing (or acceptance is missing). */
  fit: CreditFit
  rows: PlanRow[]
  hours: Line<number>
}

/** An exam in this school's verified table whose course fills a row of this major's verified plan. */
export interface ExamOption {
  family: ExamFamily
  examName: string
  /** The table's lowest qualifying minimum, as printed. */
  minimumText: string
  level: 'SL' | 'HL' | null
  course: string
  rows: PlanRow[]
  hours: number | null
  evidence: Evidence
}

export interface TermCoverage {
  term: number
  label: string
  covered: boolean
}

export interface DualEnrollmentFacts {
  grades: string[]
  minHsGpa: number | null
  altMinAct: number | null
  perCreditCharge: number | null
  stateGrantAccepted: boolean | null
}

export interface CostByArrangement {
  arrangement: LivingArrangement
  annual: number
}

export interface Unknown {
  topic: 'plan' | 'credit' | 'cost' | 'dual_enrollment' | 'timeline'
  text: string
}

export interface Roadmap {
  target: PlanningTarget & { programName: string | null; institutionName: string | null }
  /** blocked: no verified plan for this major, so credit can be shown as accepted only. */
  status: 'ready' | 'partial' | 'blocked'
  plan: Line<{ catalogYear: string | null; terms: TermCoverage[]; totalCredits: number | null }>
  credit: CreditLine[]
  options: ExamOption[]
  dualEnrollment: Line<DualEnrollmentFacts>
  cost: Line<CostByArrangement[]>
  savings: Line<PotentialSaving>
  timeline: Line<{ termsCovered: number; termsInPlan: number }>
  unknowns: Unknown[]
}
