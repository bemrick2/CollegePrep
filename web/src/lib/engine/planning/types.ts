// Planning engine data structures (docs/product/PLANNING_ENGINE.md §2). Plain values: the same in demo, live and tests.
import type { SavedInterest } from '../interests'
import type { ExamFamily, ExamMatch, PlannedExam } from '../examCredit'
import type { PotentialSaving } from '../costProjection'
import type { EarlyCompletion } from '../earlyCompletion'

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
  /** The record's academic_year_basis, e.g. 'source_unlabeled' when the source prints no academic year. */
  academicYearBasis?: string | null
  method?: string
  missing?: string
  /** The record's notes_capture: 'incomplete' when notes printed with it aren't captured and reviewed yet. */
  notesCapture?: string | null
}

export interface Line<T> {
  value: T | null
  evidence: Evidence
}

/**
 * none: the school's verified table gives no credit at this score (below the minimum, or not awarded).
 * not_verified: the table is on file but not verified, or isn't on file; nothing about this score is claimed.
 * planned: no score entered yet. see_table: the table needs something we don't read (criteria, an IB level, an exam it
 * doesn't list), so the family should read it.
 */
export type CreditFit = 'applies' | 'partly' | 'accepted_not_in_plan' | 'elective_only' | 'unknown' | 'none' | 'not_verified' | 'planned' | 'see_table'

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
  /** Where awarded credit lands in the verified plan; see CreditFit for the other states. */
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
  /** 1, 2, 3… over real terms; year headings aren't terms (#230). */
  term: number
  label: string
  /** The year heading printed above the term ("Freshman", "Year One"), when the plan has one. */
  group: string | null
  /** As printed (credit_hours or the printed subtotal); never summed. */
  creditHours: string | number | null
  rows: PlanCourseRow[]
  covered: boolean
  /** Why whole-term coverage isn't checked for this term (planItems.planTerms), or null when it is. */
  notChecked: 'multi_term' | 'short_term' | 'quarter_calendar' | 'hours' | null
}

/** One printed row of a plan term, kept as printed. */
export interface PlanCourseRow {
  kind: 'course' | 'choice' | 'text' | 'heading' | 'subtotal'
  code: string | null
  title: string | null
  /** The row as printed (code and title, or the text). */
  text: string
  credits: number | string | null
  note: string | null
  milestone: string | null
  /** For a choice: the options, as printed. */
  options: string[]
  /** How many of the options the requirement takes, as printed (1 when the plan prints no count). */
  choose: number
}

/** One of the school's plans for the major (a track, a concentration, a four-year or transfer path). */
export interface PlanChoice {
  key: string
  /** The plan's printed title (rule_details.source_section); null when the school prints none. */
  title: string | null
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
  /** programVerified: the school's listing of this major is a verified record (otherwise show it as unverified). */
  target: PlanningTarget & { programName: string | null; programVerified: boolean; institutionName: string | null }
  /**
   * ready: the degree plan, every exam-credit table the school has on file, and the cost are verified.
   * blocked: no verified plan for this major, so credit can be shown as accepted only.
   */
  status: 'ready' | 'partial' | 'blocked'
  plan: Line<{ catalogYear: string | null; title: string | null; terms: TermCoverage[]; totalCredits: number | null; totalText: string | null }>
  /** Every plan the school prints for this major, in order; the roadmap uses `planKey` (default: the first). */
  plans: PlanChoice[]
  planKey: string | null
  credit: CreditLine[]
  options: ExamOption[]
  dualEnrollment: Line<DualEnrollmentFacts>
  cost: Line<CostByArrangement[]>
  /**
   * Whole regular semesters whose every course the credit covers. This is credit COVERAGE, never a shorter degree or a
   * saving on its own (engine/earlyCompletion.ts).
   */
  coverage: Line<{ termsCovered: number; termsInPlan: number }>
  /** Whether records show the student could actually finish sooner; `missing` names what isn't shown. */
  earlyCompletion: EarlyCompletion
  /** A time or dollar saving: only when earlyCompletion is supported. Withheld otherwise, with the reason. */
  savings: Line<PotentialSaving>
  unknowns: Unknown[]
}
