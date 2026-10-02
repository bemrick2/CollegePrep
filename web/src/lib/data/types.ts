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
}

export interface Strategy {
  strategy_key: string
  name: string
  description: string | null
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
}

/** Household cost projection. No backend endpoint exists yet (contract request CR-4). */
export interface CostProjection {
  status: 'available' | 'unavailable'
  reason?: string
  baseline_total?: number
  optimized_total?: number
  savings?: number
  levers?: { key: string; label: string; estimated_savings: number | null; source_url: string | null }[]
  illustrative?: boolean
}
