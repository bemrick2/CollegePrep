// Domain types. Field names mirror the Supabase schema and RPC outputs in
// supabase/migrations/20261002183112_household_practice_progress.sql so the
// live and demo sources return identical shapes.

export type ExamFamily = 'act' | 'sat'
export type Role = 'guardian' | 'student'
export type AnswerFormat = 'choice' | 'numeric' | 'text'
export type Confidence = 1 | 2 | 3
export type HelpMode = 'hint' | 'concept' | 'strategy' | 'worked_example' | 'answer_reveal'

export interface Viewer {
  userId: string
  displayName: string | null
  mode: 'demo' | 'live'
}

export interface Household {
  id: string
  name: string
  time_zone: string
}

export interface HouseholdMember {
  household_id: string
  user_id: string
  role: Role
  can_manage_students: boolean
  can_set_goals: boolean
  can_view_progress: boolean
  can_manage_members: boolean
  can_manage_billing: boolean
}

export interface Student {
  id: string
  household_id: string | null
  display_name: string
  graduation_year: number | null
  grade_level: number | null
  account_mode: 'guardian_managed' | 'student_login'
  is_independent: boolean
  linked_user_id: string | null
  time_zone: string | null
  archived_at: string | null
}

export interface HouseholdContext {
  households: Household[]
  memberships: HouseholdMember[]
  students: Student[]
  /** The student profile linked to the viewer's own login, if any. */
  myStudent: Student | null
}

export interface Skill {
  id: string
  exam_family: ExamFamily
  section: string
  domain: string | null
  skill_key: string
  name: string
  /** Short, answer-free lesson for "Teach me" before answering (CR-8; demo fixtures only until the backend has it). */
  concept_summary?: string | null
}

export interface Strategy {
  strategy_key: string
  name: string
  description: string | null
  /** Sections where the strategy applies, for "Test strategy" before answering (CR-8). */
  sections?: string[] | null
}

export interface TrapType {
  trap_key: string
  name: string
  description: string | null
}

export interface Choice {
  key: string
  text: string
}

/** Client-visible question columns. Answers, hints and explanations are never included. */
export interface PublicQuestion {
  id: string
  exam_family: ExamFamily
  section: string
  difficulty: number | null
  difficulty_label: 'easy' | 'medium' | 'hard' | null
  stem: string
  /** Optional passage shown above the stem (Reading, English, Science). */
  passage?: string | null
  choices: Choice[]
  answer_format: AnswerFormat
  expected_time_seconds: number | null
  primary_skill_key: string | null
  hint_count: number
}

export interface DistractorRationale {
  choice: string
  rationale: string
  trap: string | null
}

export interface StrategyReveal {
  strategy_key: string
  role: 'primary' | 'secondary'
  is_fastest: boolean
  explanation: string | null
}

/** Output of submit_practice_attempt. */
export interface SubmitResult {
  is_correct: boolean | null
  skipped: boolean
  elapsed_ms: number
  accepted_answers: string[]
  teaching_explanation: string | null
  strategy_explanation: string | null
  distractors: DistractorRationale[]
  strategies: StrategyReveal[]
  /** "Remember this" (CR-5, at most 16 words), revealed only after submit. */
  remember_text?: string | null
}

export interface SubmitInput {
  answer: string | null
  activeMs?: number
  firstInteractionMs?: number
  confidence?: Confidence
  strategyKey?: string
  skipped?: boolean
}

export interface HintResult {
  hint_number: number
  hint: string
  remaining: number
}

export interface AiHelpResult {
  request_id: string
  status: 'pending' | 'completed' | 'failed' | 'disabled'
}

export interface SessionPlanItem {
  position: number
  question: PublicQuestion
  reason: 'weak_knowledge' | 'weak_pacing' | 'new_skill' | 'review' | 'untagged' | string
  /** The student has been shown this question before (any session or check). Counts toward the goal; not fresh evidence. */
  seen_before?: boolean
}

export interface PracticeSession {
  id: string
  target_minutes: number
  items: SessionPlanItem[]
}

export interface WeeklyGoal {
  target_questions: number | null
  target_minutes: number | null
  goal_mode: 'fixed' | 'adaptive'
}

/** Output of student_weekly_progress. */
export interface WeeklyProgress {
  student_id: string
  week_start: string
  time_zone: string
  goal: WeeklyGoal | null
  questions_attempted: number
  questions_submitted: number
  skipped: number
  skip_events: number
  returns: number
  answer_changes: number
  correct: number
  accuracy: number | null
  total_elapsed_ms: number
  total_active_ms: number | null
  median_elapsed_ms: number | null
  avg_confidence: number | null
  ai_help_attempts: number
  hints_used: number
  goal_progress: { questions_pct: number | null; minutes_pct: number | null } | null
  streak: { current: number; longest: number }
  skill_summary: { knowledge_weak: string[]; pacing_weak: string[]; insufficient_data: number }
  by_skill: { section: string | null; skill: string | null; submitted: number; correct: number; median_elapsed_ms: number | null }[]
  by_strategy: { strategy_key: string; submitted: number; correct: number }[]
}

/** Output row of student_skill_estimates. */
export interface SkillEstimate {
  skill_id: string
  skill_key: string
  section: string
  attempts: number
  correct: number
  accuracy: number | null
  median_elapsed_ms: number | null
  pacing_ratio: number | null
  knowledge_weak: boolean | null
  pacing_weak: boolean | null
}

export interface Streak {
  current_streak: number
  longest_streak: number
  last_practice_day: string | null
}

export interface TestScore {
  id: string
  exam_family: ExamFamily
  test_date: string
  composite: number | null
  section_scores: Record<string, number>
  score_source: 'official' | 'self_reported' | 'practice_estimate'
}

/** One submitted attempt, for history views. */
export interface AttemptRecord {
  id: string
  question_id: string
  section: string
  skill_key: string | null
  submitted_at: string
  elapsed_ms: number
  expected_time_seconds: number | null
  is_correct: boolean | null
  skipped: boolean
  confidence: Confidence | null
  hint_count: number
}

/** Planning preferences that have no backend home yet (see docs/frontend/CONTRACT_REQUESTS.md). */
export interface StudentPlan {
  exam_family: ExamFamily
  target_score: number | null
  goals: string[]
  daily_minutes: number
}

/** Benchmark summaries are client-held until a backend table exists (contract request CR-2). */
export interface BenchmarkSummary {
  id: string
  kind: 'initial' | 'mini' | 'full'
  exam_family: ExamFamily
  started_at: string
  completed_at: string
  attempt_ids: string[]
  metrics: BenchmarkMetrics
}

export interface SectionMetrics {
  section: string
  answered: number
  correct: number
  skipped: number
  accuracy: number | null
  /** Median of elapsed / expected time. Above 1.25 is flagged as slow, as in the backend's pacing rule. */
  pacing_ratio: number | null
  /** Highest difficulty answered correctly, from the adaptive staircase. */
  ceiling_difficulty: number | null
}

export interface BenchmarkMetrics {
  answered: number
  correct: number
  skipped: number
  skip_events: number
  returns: number
  answer_changes: number
  accuracy: number | null
  median_elapsed_ms: number | null
  pacing_ratio: number | null
  /** Accuracy when the student said "certain" vs. how often they were right. */
  calibration: { confidence: Confidence; answered: number; correct: number }[]
  strategy_use: { strategy_key: string; answered: number; correct: number }[]
  traps_fallen: { trap: string; count: number }[]
  sections: SectionMetrics[]
}

// ---------- College comparison (compare_institutions) ----------

export interface InstitutionIdentity {
  institution_key: string
  display_name: string
  city: string | null
  state_code: string | null
  control: string | null
  website_url: string | null
  net_price_calculator_url: string | null
  identity_academic_year: string | null
  source_url: string | null
  /** IPEDS institution level (CR-9). Absent from the live RPC today; costs are then shown per year only. */
  level?: 'two_year' | 'four_year' | 'less_than_two_year' | null
}

export interface CostRecord {
  residency: string
  student_population: string
  tuition: number | null
  mandatory_fees: number | null
  room: number | null
  board: number | null
  on_campus_food_housing: number | null
  books_supplies: number | null
  transportation: number | null
  personal_misc: number | null
  total_cost_of_attendance: number | null
  notes: string | null
  source_url: string | null
  last_verified_at: string | null
}

export type ComparisonDomain =
  | 'costs'
  | 'admissions_metrics'
  | 'awards'
  | 'credit_policies'
  | 'transfer_policies'
  | 'academic_programs'
  | 'degree_requirements'
  | 'appeals'

export interface InstitutionComparison {
  institution_key: string
  found: boolean
  institution: InstitutionIdentity | null
  academic_year: string
  domains: Record<ComparisonDomain, Record<string, unknown>[]>
  missing_domains: ComparisonDomain[]
  can_offer_paid_addon: boolean
}

export interface InstitutionSearchHit {
  institution_key: string
  display_name: string
  city: string | null
  state_code: string | null
  control: string | null
  level?: 'four_year' | 'two_year' | 'less_than_two_year' | null
  /** Domains with a verified record for the requested year (institutions_with_verified_records). */
  domains?: string[]
}

/** Cost projection (CR-4 v2, `cost_projection`). Verified, exact-year figures only; nothing here is guaranteed. */
export type CostBasis = 'tuition_and_fees' | 'cost_of_attendance'
export type ProjectionResidency = 'in_state' | 'out_of_state' | 'district' | 'international'

export interface CostAssumptions {
  residency: ProjectionResidency
  cost_basis?: CostBasis
  years?: number | null
  /** Credit brought from elsewhere (dual enrollment, transfer). Counted only under a verified cap. */
  prior_credits?: number
  /** AP/IB/CLEP credit read from this school's own published equivalency table. */
  exam_credits?: number
  credits_per_term?: number
  terms_per_year?: 2 | 3
}

/** Published parts of one year's price. null = not published. living_and_other = COA - tuition - fees. */
export interface CostComponents {
  tuition: number | null
  mandatory_fees: number | null
  housing_food: number | null
  books_supplies: number | null
  transportation: number | null
  personal_misc: number | null
  other_expenses: number | null
  total_cost_of_attendance: number | null
  living_and_other: number | null
}

export interface CreditCap {
  kind: string
  credits: number
  source_url: string | null
}

export type LeverReason =
  | 'no_prior_credits'
  | 'no_exam_credits'
  | 'no_verified_cap'
  | 'bounded_by_verified_cap'
  | 'bounded_by_verified_limit'
  | 'from_school_table'
  | 'less_than_one_term'

export interface CreditLever {
  kind: 'prior_credits' | 'exam_credits'
  requested_credits: number
  accepted_upper_bound: number
  caps: CreditCap[]
  /** What this lever alone would save; row totals combine levers. */
  terms_saved: number
  savings: number
  counted: boolean
  reason: LeverReason
  requires_confirmation: true
}

export interface CreditSavings {
  /** Never a confirmed shorter degree: what it would save if the assumptions hold. */
  certainty: 'potential'
  /** exam_credit_total_entered_by_family: the exam credit total came from the client, not computed by the server. */
  assumes: ('counted_credit_applies_to_the_degree' | 'schedule_allows_finishing_early' | 'exam_credit_total_entered_by_family')[]
  /** Savings come only from billing fewer terms by finishing early. */
  mechanism: 'fewer_terms'
  /** No flat-rate vs per-credit tuition data exists, so credit short of a full term is not counted. */
  billing_structure: 'unknown'
  credits_counted: number
  residency_requirement_credits: number | null
  outside_credit_max: number | null
  terms_saved: number
  remainder_credits: number
  by_component: { tuition: number | null; mandatory_fees: number | null; living_and_other: number | null }
  requires_confirmation: true
}

export interface AwardListing {
  award_name: string
  award_type: string | null
  award_amount_text: string | null
  award_min: number | null
  award_max: number | null
  full_tuition?: boolean | null
  full_ride?: boolean | null
  automatic_consideration: boolean | null
  separate_application: boolean | null
  eligibility_summary: string | null
  renewable: boolean | null
  source_url: string | null
}

export interface StateAidListing {
  program_name: string
  program_type: string | null
  award_amount_text: string | null
  award_min?: number | null
  award_max?: number | null
  eligibility_summary: string | null
  official_url: string | null
  source_url: string | null
}

export interface ProjectionCost {
  basis: CostBasis
  /** The verified row used: the requested residency, or 'not_applicable' (one price for everyone). */
  residency: string
  residency_requested: ProjectionResidency
  annual?: number
  /** Repeated from components on priced rows (v1 fields). */
  tuition?: number | null
  mandatory_fees?: number | null
  total_cost_of_attendance?: number | null
  components: CostComponents
  source_url: string | null
  last_verified_at: string | null
}

export interface ProjectionRow {
  institution_key: string
  display_name?: string
  level?: 'four_year' | 'two_year' | 'less_than_two_year' | null
  status: 'ok' | 'missing_cost' | 'missing_years' | 'unknown_institution'
  cost?: ProjectionCost | null
  years?: number
  years_source?: 'level_default' | 'assumption'
  baseline_total?: number
  levers?: CreditLever[]
  credit_savings?: CreditSavings
  optimized_total?: number
  savings_total?: number
  /** optimized_total and savings_total include potential credit savings; neither is a projected price. */
  totals_certainty?: 'potential'
  not_counted?: { awards: AwardListing[]; state_aid: StateAidListing[]; appeals: { appeal_kind: string; process_summary: string | null; policy_url: string | null }[]; loans: 'no_data' }
}

export interface CostProjectionResult {
  academic_year: string
  assumptions: Required<Omit<CostAssumptions, 'years'>> & { years: number | null }
  prices_held_constant: true
  guaranteed: false
  definition: string
  institutions: ProjectionRow[]
}

/** Household plan access (CR-16), whatever the payment source. Provider ids never reach the client. */
export interface Entitlement {
  active: boolean
  in_grace?: boolean
  plan_key?: string | null
  status: string | null
  current_period_end?: string | null
  cancel_at_period_end?: boolean
  can_manage_billing: boolean
  /** Where the plan is managed; only for the payer or a guardian who manages billing. */
  managed_by?: 'web' | 'apple' | 'google' | 'comp' | null
  is_owner?: boolean
}

export interface BillingPlan {
  lookup_key: string
  unit_amount: number | null
  currency: string
  interval: 'month' | 'year' | null
  product_name: string | null
}
