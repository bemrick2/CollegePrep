import { MAX_INTERESTS, type InterestProfile, type MajorCertainty, type SavedInterest } from '../../engine/interests'
import { INVITE_TTL_HOURS } from '../../invites'
import type { SupabaseClient } from '@supabase/supabase-js'
import type { AlertPreference, DataSource, InactiveStudent, InvitationSummary, InviteSendResult, StudentInvitation } from '../source'
import type { NextWeekSuggestion } from '../../engine/weeklyPlan'
import { DataError } from '../source'
import type {
  BillingPlan,
  Entitlement,
  AttemptRecord,
  BenchmarkMetrics,
  BenchmarkSummary,
  Choice,
  CostAssumptions,
  CostProjectionResult,
  ExamFamily,
  HelpMode,
  HouseholdContext,
  InstitutionComparison,
  InstitutionSearchHit,
  PracticeSession,
  PublicQuestion,
  SkillEstimate,
  StudentPlan,
  SubmitInput,
  SubmitResult,
  TestScore,
  Viewer,
  WeeklyProgress,
} from '../types'

// Supabase-backed source. Every call is an RLS-filtered table read or one of
// the RPCs documented in docs/HOUSEHOLD_PRACTICE.md and docs/BACKEND.md.

interface PgError {
  code?: string
  message: string
}

function fail(err: PgError): never {
  const code = err.code === '42501' ? 'forbidden' : err.code === '22023' ? 'invalid' : 'unknown'
  throw new DataError(err.message, code)
}

async function rpc<T>(sb: SupabaseClient, fn: string, args: Record<string, unknown>): Promise<T> {
  const { data, error } = await sb.rpc(fn, args)
  if (error) fail(error)
  return data as T
}

const OUTCOME_MESSAGE: Record<string, string> = {
  invalid: 'Invalid invitation code',
  expired: 'Invitation has expired',
  used: 'Invitation has already been used',
  revoked: 'Invitation has been revoked',
  rate_limited: 'Too many invite code attempts; try again in 15 minutes',
}

const QUESTION_COLUMNS =
  'id, section, difficulty, difficulty_label, stem, choices, answer_format, expected_time_seconds, hint_count, practice_passages(title, body), exam_versions!inner(exam_family), practice_question_skills(is_primary, skills(skill_key))'

interface QuestionRow {
  id: string
  section: string
  difficulty: number | null
  difficulty_label: PublicQuestion['difficulty_label']
  stem: string
  choices: unknown
  answer_format: PublicQuestion['answer_format']
  expected_time_seconds: number | null
  hint_count: number | null
  practice_passages: { title: string | null; body: string } | null
  exam_versions: { exam_family: ExamFamily }
  practice_question_skills: { is_primary: boolean; skills: { skill_key: string } | null }[]
}

function normalizeChoices(raw: unknown): Choice[] {
  if (!Array.isArray(raw)) return []
  return raw.map((c, i) => {
    if (typeof c === 'string') return { key: String.fromCharCode(65 + i), text: c }
    const o = c as Record<string, unknown>
    return { key: String(o.key ?? o.choice_key ?? String.fromCharCode(65 + i)), text: String(o.text ?? o.label ?? '') }
  })
}

function toPublic(r: QuestionRow): PublicQuestion {
  return {
    id: r.id,
    exam_family: r.exam_versions.exam_family,
    section: r.section,
    difficulty: r.difficulty,
    difficulty_label: r.difficulty_label,
    stem: r.stem,
    passage: r.practice_passages ? (r.practice_passages.title ? `${r.practice_passages.title}\n\n${r.practice_passages.body}` : r.practice_passages.body) : null,
    choices: normalizeChoices(r.choices),
    answer_format: r.answer_format,
    expected_time_seconds: r.expected_time_seconds,
    primary_skill_key: r.practice_question_skills.find((s) => s.is_primary)?.skills?.skill_key ?? null,
    hint_count: r.hint_count ?? 0,
  }
}


/** practice_benchmarks.metrics (definition v1, computed by complete_benchmark). */
interface ServerMetrics {
  attempts?: number
  submitted?: number
  skips?: number
  returns?: number
  answer_changes?: number
  accuracy?: number | null
  pacing_ratio?: number | null
  by_section?: Record<string, { submitted: number; correct: number; accuracy: number | null; pacing_ratio: number | null }>
  calibration?: { by_confidence?: Record<string, { submitted: number; accuracy: number | null }>; confident_wrong_share?: number | null }
  traps?: Record<string, number>
}

/** Maps the server's metrics to the UI shape. Fields the server doesn't compute (the staircase ceiling,
 *  strategy use) come from this run's client record when available, otherwise stay empty. */
function fromServerMetrics(m: ServerMetrics | null, client?: BenchmarkMetrics): BenchmarkMetrics {
  const by = m?.by_section ?? {}
  const submitted = m?.submitted ?? 0
  return {
    answered: submitted,
    correct: Math.round((m?.accuracy ?? 0) * submitted),
    skipped: m?.skips ?? 0,
    skip_events: client?.skip_events ?? m?.skips ?? 0,
    returns: m?.returns ?? 0,
    answer_changes: m?.answer_changes ?? 0,
    accuracy: m?.accuracy ?? null,
    median_elapsed_ms: client?.median_elapsed_ms ?? null,
    pacing_ratio: m?.pacing_ratio ?? null,
    calibration: Object.entries(m?.calibration?.by_confidence ?? {}).map(([c, v]) => ({
      confidence: Number(c) as 1 | 2 | 3,
      answered: v.submitted,
      correct: Math.round((v.accuracy ?? 0) * v.submitted),
    })),
    strategy_use: client?.strategy_use ?? [],
    traps_fallen: Object.entries(m?.traps ?? {}).map(([trap, count]) => ({ trap, count })),
    sections: Object.entries(by).map(([section, v]) => ({
      section,
      answered: v.submitted,
      correct: v.correct,
      skipped: client?.sections?.find((x) => x.section === section)?.skipped ?? 0,
      accuracy: v.accuracy,
      pacing_ratio: v.pacing_ratio,
      ceiling_difficulty: client?.sections?.find((x) => x.section === section)?.ceiling_difficulty ?? null,
    })),
  }
}

export class LiveSource implements DataSource {
  readonly mode = 'live' as const
  constructor(private sb: SupabaseClient) {}

  async getViewer(): Promise<Viewer | null> {
    const { data } = await this.sb.auth.getUser()
    if (!data.user) return null
    const { data: profile } = await this.sb.from('profiles').select('display_name').eq('id', data.user.id).maybeSingle()
    return { userId: data.user.id, displayName: profile?.display_name ?? null, mode: 'live' }
  }

  async signOut() {
    await this.sb.auth.signOut()
  }

  async getHouseholdContext(): Promise<HouseholdContext> {
    const { data: user } = await this.sb.auth.getUser()
    const me = user.user?.id
    const [h, m, s] = await Promise.all([
      this.sb.from('households').select('id, name, time_zone'),
      this.sb.from('household_members').select('*').eq('user_id', me ?? ''),
      this.sb
        .from('students')
        .select('id, household_id, display_name, graduation_year, grade_level, account_mode, is_independent, linked_user_id, time_zone, archived_at')
        .is('archived_at', null),
    ])
    for (const r of [h, m, s]) if (r.error) fail(r.error)
    const students = s.data ?? []
    return {
      households: h.data ?? [],
      memberships: m.data ?? [],
      students,
      myStudent: students.find((x) => x.linked_user_id === me) ?? null,
    }
  }

  createHousehold(name: string, timeZone: string) {
    return rpc<string>(this.sb, 'create_household', { p_name: name, p_time_zone: timeZone })
  }

  addStudent(householdId: string, displayName: string, graduationYear: number | null, gradeLevel: number | null) {
    return rpc<string>(this.sb, 'add_student', {
      p_household: householdId,
      p_display_name: displayName,
      p_graduation_year: graduationYear,
      p_grade_level: gradeLevel,
    })
  }

  createSelfStudentProfile(input: { displayName: string; graduationYear: number | null; gradeLevel: number | null; independent: boolean; timeZone: string | null }) {
    return rpc<string>(this.sb, 'create_self_student_profile', {
      p_display_name: input.displayName,
      p_graduation_year: input.graduationYear,
      p_grade_level: input.gradeLevel,
      p_independent: input.independent,
      p_time_zone: input.timeZone,
    })
  }

  createInvitation(householdId: string, role: 'guardian' | 'student', studentId?: string) {
    return rpc<string>(this.sb, 'create_household_invitation', { p_household: householdId, p_role: role, p_student: studentId ?? null, p_ttl_hours: INVITE_TTL_HOURS })
  }

  async acceptInvitation(code: string) {
    // Wrong, stale and used codes come back as outcomes (so failed guesses are counted server-side).
    const rows = await rpc<{ outcome: string; household_id: string | null }[]>(this.sb, 'redeem_household_invitation', { p_code: code.trim() })
    const r = rows[0]
    if (r?.outcome === 'joined' && r.household_id) return r.household_id
    throw new DataError(OUTCOME_MESSAGE[r?.outcome ?? 'invalid'] ?? OUTCOME_MESSAGE.invalid!, 'invalid')
  }

  async createStudentInvitation(householdId: string, studentId: string): Promise<StudentInvitation> {
    const rows = await rpc<{ code: string; invite_code: string; invitation_id: string; expires_at: string }[]>(this.sb, 'create_student_invitation', {
      p_household: householdId,
      p_student: studentId,
    })
    const r = rows[0]!
    return { code: r.code, inviteCode: r.invite_code, invitationId: r.invitation_id, expiresAt: r.expires_at }
  }

  async sendStudentInvitation(input: { householdId: string; studentId: string; email: string; code?: string; inviteCode?: string }): Promise<InviteSendResult> {
    const { data, error } = await this.sb.functions.invoke('send-household-invitation', {
      body: { householdId: input.householdId, studentId: input.studentId, email: input.email, code: input.code, inviteCode: input.inviteCode, origin: window.location.origin },
    })
    if (error) {
      // The function answers 4xx for requests it refuses (bad email, no permission) with a message in the body.
      const ctx = (error as { context?: Response }).context
      let message = 'We couldn’t send the invitation'
      try {
        const b = ctx ? await ctx.json() : null
        if (b?.error) message = String(b.error)
      } catch {
        // keep the generic message
      }
      const missing = !ctx || ctx.status === 404
      if (!missing && ctx.status >= 400 && ctx.status < 500) throw new DataError(message, ctx.status === 403 ? 'forbidden' : 'invalid')
      // The email function is unreachable or not deployed: still give the parent a working invitation to copy.
      if (input.code) return { code: input.code, inviteCode: input.inviteCode, emailed: false, reason: missing ? 'not_configured' : 'provider' }
      const inv = await this.createStudentInvitation(input.householdId, input.studentId)
      return { ...inv, emailed: false, reason: missing ? 'not_configured' : 'provider' }
    }
    return data as InviteSendResult
  }

  async suggestNextWeekGoal(studentId: string): Promise<NextWeekSuggestion> {
    const r = await rpc<{ week_start: string; target_questions: number | null; basis: string; weeks_considered: number; questions_completion: number | null }>(
      this.sb,
      'suggest_next_week_goal',
      { p_student: studentId },
    )
    return {
      weekStart: r.week_start,
      targetQuestions: r.target_questions,
      basis: r.basis === 'history' ? 'history' : 'insufficient_history',
      weeksConsidered: r.weeks_considered ?? 0,
      completion: r.questions_completion,
    }
  }

  async getAlertPreference(studentId: string): Promise<AlertPreference | null> {
    const { data, error } = await this.sb
      .from('alert_preferences')
      .select('inactivity_days, enabled')
      .eq('student_id', studentId)
      .eq('channel', 'email')
      .maybeSingle()
    if (error) fail(error)
    return data ? { enabled: data.enabled as boolean, inactivityDays: data.inactivity_days as number } : null
  }

  async setAlertPreference(studentId: string, pref: AlertPreference) {
    const existing = await this.getAlertPreference(studentId)
    const r = existing
      ? await this.sb.from('alert_preferences').update({ enabled: pref.enabled, inactivity_days: pref.inactivityDays }).eq('student_id', studentId).eq('channel', 'email')
      : await this.sb.from('alert_preferences').insert({ student_id: studentId, channel: 'email', enabled: pref.enabled, inactivity_days: pref.inactivityDays })
    if (r.error) fail(r.error)
  }

  async inactiveStudents(): Promise<InactiveStudent[]> {
    const rows = await rpc<{ student_id: string; days_inactive: number | null; threshold_days: number; last_submitted_at: string | null }[]>(this.sb, 'student_inactivity', {})
    return (rows ?? []).map((r) => ({ studentId: r.student_id, daysInactive: r.days_inactive, thresholdDays: r.threshold_days, lastSubmittedAt: r.last_submitted_at }))
  }

  async listInvitations(householdId: string): Promise<InvitationSummary[]> {
    const { data, error } = await this.sb
      .from('household_invitations')
      .select('id, role, student_id, recipient_email, created_at, expires_at, accepted_at, revoked_at, last_emailed_at')
      .eq('household_id', householdId)
      .order('created_at', { ascending: false })
    if (error) fail(error)
    return (data ?? []) as InvitationSummary[]
  }

  async revokeInvitation(invitationId: string) {
    await rpc<null>(this.sb, 'revoke_household_invitation', { p_invitation: invitationId })
  }

  async setWeeklyGoal(studentId: string, weekStart: string, targetQuestions: number | null, targetMinutes: number | null) {
    const existing = await this.sb
      .from('weekly_practice_goals')
      .select('id')
      .eq('student_id', studentId)
      .eq('week_start', weekStart)
      .is('subject', null)
      .maybeSingle()
    if (existing.error) fail(existing.error)
    const r = existing.data
      ? await this.sb.from('weekly_practice_goals').update({ target_questions: targetQuestions, target_minutes: targetMinutes }).eq('id', existing.data.id)
      : await this.sb.from('weekly_practice_goals').insert({ student_id: studentId, week_start: weekStart, target_questions: targetQuestions, target_minutes: targetMinutes })
    if (r.error) fail(r.error)
  }

  weeklyProgress(studentId: string, weekStart: string) {
    return rpc<WeeklyProgress>(this.sb, 'student_weekly_progress', { p_student: studentId, p_week_start: weekStart })
  }

  streak(studentId: string) {
    return rpc<{ current_streak: number; longest_streak: number; last_practice_day: string | null }>(this.sb, 'student_streak', { p_student: studentId })
  }

  skillEstimates(studentId: string) {
    return rpc<SkillEstimate[]>(this.sb, 'student_skill_estimates', { p_student: studentId })
  }

  async testScores(studentId: string): Promise<TestScore[]> {
    const { data, error } = await this.sb
      .from('student_test_scores')
      .select('id, test_date, composite, section_scores, score_source, exam_versions(exam_family)')
      .eq('student_id', studentId)
      .order('test_date', { ascending: false })
    if (error) fail(error)
    return (data ?? []).map((r) => {
      const ev = r.exam_versions as unknown as { exam_family: ExamFamily } | null
      return {
        id: r.id,
        exam_family: ev?.exam_family ?? 'act',
        test_date: r.test_date,
        composite: r.composite,
        section_scores: r.section_scores as Record<string, number>,
        score_source: r.score_source,
      }
    })
  }

  async attemptHistory(studentId: string, sinceIso: string): Promise<AttemptRecord[]> {
    const { data, error } = await this.sb
      .from('practice_attempts')
      .select('id, question_id, submitted_at, elapsed_ms, is_correct, skipped, confidence, hint_count, practice_questions(section, expected_time_seconds, practice_question_skills(is_primary, skills(skill_key)))')
      .eq('student_id', studentId)
      .gte('submitted_at', sinceIso)
      .order('submitted_at')
    if (error) fail(error)
    return (data ?? []).map((r) => {
      const q = r.practice_questions as unknown as {
        section: string
        expected_time_seconds: number | null
        practice_question_skills: { is_primary: boolean; skills: { skill_key: string } | null }[]
      }
      return {
        id: r.id,
        question_id: r.question_id,
        section: q.section,
        skill_key: q.practice_question_skills.find((s) => s.is_primary)?.skills?.skill_key ?? null,
        submitted_at: r.submitted_at,
        elapsed_ms: r.elapsed_ms ?? 0,
        expected_time_seconds: q.expected_time_seconds,
        is_correct: r.is_correct,
        skipped: r.skipped,
        confidence: r.confidence,
        hint_count: r.hint_count,
      }
    })
  }

  async catalog(examFamily: ExamFamily) {
    const [sk, st, tr] = await Promise.all([
      this.sb.from('skills').select('id, exam_family, section, domain, skill_key, name, concept_summary').eq('exam_family', examFamily),
      this.sb.from('question_strategies').select('strategy_key, name, description, sections'),
      this.sb.from('trap_types').select('trap_key, name, description'),
    ])
    for (const r of [sk, st, tr]) if (r.error) fail(r.error)
    return { skills: sk.data ?? [], strategies: st.data ?? [], traps: tr.data ?? [] }
  }

  async publishedQuestions(examFamily: ExamFamily) {
    const { data, error } = await this.sb
      .from('practice_questions')
      .select(QUESTION_COLUMNS)
      .eq('status', 'published')
      .eq('exam_versions.exam_family', examFamily)
    if (error) fail(error)
    return ((data ?? []) as unknown as QuestionRow[]).map(toPublic)
  }

  private async currentExamVersion(examFamily: ExamFamily): Promise<string | null> {
    const today = new Date().toISOString().slice(0, 10)
    const { data } = await this.sb
      .from('exam_versions')
      .select('id, effective_from, effective_to')
      .eq('exam_family', examFamily)
      .lte('effective_from', today)
      .order('effective_from', { ascending: false })
    return data?.find((v) => !v.effective_to || v.effective_to > today)?.id ?? null
  }

  async startSession(studentId: string, targetMinutes: number, examFamily: ExamFamily): Promise<PracticeSession> {
    const version = await this.currentExamVersion(examFamily)
    const id = await rpc<string>(this.sb, 'start_practice_session', {
      p_student: studentId,
      p_target_minutes: targetMinutes,
      p_exam_version: version,
    })
    const items = await this.sb.from('practice_session_items').select('position, question_id, reason').eq('session_id', id).order('position')
    if (items.error) fail(items.error)
    const ids = (items.data ?? []).map((i) => i.question_id)
    const qs = ids.length ? await this.sb.from('practice_questions').select(QUESTION_COLUMNS).in('id', ids) : { data: [], error: null }
    if (qs.error) fail(qs.error)
    const byId = new Map(((qs.data ?? []) as unknown as QuestionRow[]).map((q) => [q.id, toPublic(q)]))
    return {
      id,
      target_minutes: targetMinutes,
      items: (items.data ?? []).filter((i) => byId.has(i.question_id)).map((i) => ({ position: i.position, reason: i.reason, question: byId.get(i.question_id)! })),
    }
  }

  async endSession(sessionId: string) {
    await rpc<void>(this.sb, 'end_practice_session', { p_session: sessionId })
  }

  startAttempt(studentId: string, questionId: string, sessionId: string | null, benchmarkId: string | null = null) {
    return rpc<string>(this.sb, 'start_practice_attempt', { p_student: studentId, p_question: questionId, p_session: sessionId, p_benchmark: benchmarkId })
  }

  recordEvent(attemptId: string, kind: 'answered' | 'skipped' | 'returned', answer?: string) {
    return rpc<string>(this.sb, 'record_attempt_event', { p_attempt: attemptId, p_kind: kind, p_answer: answer ?? null })
  }

  async requestHint(attemptId: string) {
    const r = await rpc<{ hint_number: number; hint: unknown; remaining: number }>(this.sb, 'request_hint', { p_attempt: attemptId })
    return { ...r, hint: typeof r.hint === 'string' ? r.hint : JSON.stringify(r.hint) }
  }

  async submitAttempt(attemptId: string, input: SubmitInput): Promise<SubmitResult> {
    const rows = await rpc<SubmitResult[]>(this.sb, 'submit_practice_attempt', {
      p_attempt: attemptId,
      p_selected_answer: input.answer,
      p_active_ms: input.activeMs ?? null,
      p_first_interaction_ms: input.firstInteractionMs ?? null,
      p_confidence: input.confidence ?? null,
      p_strategy_key: input.strategyKey ?? null,
      p_skipped: input.skipped ?? false,
    })
    const r = rows[0]
    if (!r) throw new DataError('No result from submit', 'unknown')
    return r
  }

  requestAiHelp(attemptId: string, mode: HelpMode) {
    return rpc<{ request_id: string; status: 'pending' | 'completed' | 'failed' | 'disabled' }>(this.sb, 'request_ai_help', { p_attempt: attemptId, p_mode: mode })
  }

  async rememberThis() {
    // Live: remember_text arrives with submit_practice_attempt (CR-5).
    return null
  }

  async getPlan(studentId: string): Promise<StudentPlan | null> {
    const { data, error } = await this.sb
      .from('student_planning_preferences')
      .select('exam_family, target_score, goals, daily_minutes')
      .eq('student_id', studentId)
      .maybeSingle()
    if (error) fail(error)
    if (!data) return null
    return { exam_family: (data.exam_family ?? 'act') as ExamFamily, target_score: data.target_score, goals: data.goals ?? [], daily_minutes: data.daily_minutes ?? 10 }
  }

  async savePlan(studentId: string, plan: StudentPlan) {
    const row = { exam_family: plan.exam_family, target_score: plan.target_score, goals: plan.goals, daily_minutes: plan.daily_minutes }
    const existing = await this.sb.from('student_planning_preferences').select('student_id').eq('student_id', studentId).maybeSingle()
    if (existing.error) fail(existing.error)
    const r = existing.data
      ? await this.sb.from('student_planning_preferences').update(row).eq('student_id', studentId)
      : await this.sb.from('student_planning_preferences').insert({ student_id: studentId, ...row })
    if (r.error) fail(r.error)
  }

  async listBenchmarks(studentId: string): Promise<BenchmarkSummary[]> {
    const { data, error } = await this.sb
      .from('practice_benchmarks')
      .select('id, kind, started_at, completed_at, metrics, exam_versions(exam_family), practice_attempts(id)')
      .eq('student_id', studentId)
      .not('completed_at', 'is', null)
      .order('completed_at')
    if (error) fail(error)
    return (data ?? []).map((b) => ({
      id: b.id,
      kind: b.kind as BenchmarkSummary['kind'],
      exam_family: ((b.exam_versions as unknown as { exam_family: ExamFamily } | null)?.exam_family ?? 'act') as ExamFamily,
      started_at: b.started_at,
      completed_at: b.completed_at!,
      attempt_ids: ((b.practice_attempts as unknown as { id: string }[] | null) ?? []).map((a) => a.id),
      metrics: fromServerMetrics(b.metrics as ServerMetrics | null),
    }))
  }

  async startBenchmark(studentId: string, kind: BenchmarkSummary['kind'], examFamily: ExamFamily) {
    const version = await this.currentExamVersion(examFamily)
    return rpc<string>(this.sb, 'start_benchmark', { p_student: studentId, p_kind: kind, p_exam_version: version })
  }

  async completeBenchmark(_studentId: string, benchmarkId: string, client: BenchmarkSummary): Promise<BenchmarkSummary> {
    const m = await rpc<ServerMetrics>(this.sb, 'complete_benchmark', { p_benchmark: benchmarkId })
    return { ...client, id: benchmarkId, metrics: fromServerMetrics(m, client.metrics) }
  }

  async savedSchools(householdId: string) {
    const { data, error } = await this.sb.from('household_saved_schools').select('institution_key').eq('household_id', householdId).order('added_at')
    if (error) fail(error)
    return (data ?? []).map((r) => r.institution_key as string)
  }

  async saveSchool(householdId: string, institutionKey: string) {
    await rpc<void>(this.sb, 'save_household_school', { p_household: householdId, p_institution_key: institutionKey })
  }

  async removeSchool(householdId: string, institutionKey: string) {
    await rpc<void>(this.sb, 'remove_household_school', { p_household: householdId, p_institution_key: institutionKey })
  }

  // CR-16 billing: on only when the deployment sets VITE_BILLING_ENABLED=true (edge functions and Stripe ready).
  readonly supportsBilling = import.meta.env.VITE_BILLING_ENABLED === 'true'

  async entitlement(householdId: string): Promise<Entitlement> {
    // Sandbox status is display-only; production access always uses household_entitlement.
    const sandbox = import.meta.env.VITE_BILLING_ENVIRONMENT === 'sandbox' &&
      typeof window !== 'undefined' && window.location.hostname === 'college-optimizer-staging.netlify.app'
    return rpc<Entitlement>(this.sb, sandbox ? 'household_sandbox_billing_status' : 'household_entitlement', { p_household: householdId })
  }

  private async fn<T>(name: string, body?: Record<string, unknown>): Promise<T> {
    const { data, error } = await this.sb.functions.invoke(name, body ? { body } : { method: 'GET' })
    if (error) {
      // Edge functions answer { error } with a status; surface that message, not a transport error.
      const ctx = (error as { context?: Response }).context
      const msg = ctx && typeof ctx.json === 'function' ? ((await ctx.json().catch(() => null)) as { error?: string } | null)?.error : null
      throw new DataError(msg ?? error.message, 'invalid')
    }
    return data as T
  }

  async billingPlans(): Promise<BillingPlan[]> {
    return (await this.fn<{ plans: BillingPlan[] }>('billing-plans')).plans
  }

  async startCheckout(householdId: string, lookupKey: string): Promise<string> {
    return (await this.fn<{ url: string }>('billing-checkout', { household_id: householdId, lookup_key: lookupKey })).url
  }

  async billingPortalUrl(householdId: string): Promise<string> {
    return (await this.fn<{ url: string }>('billing-portal', { household_id: householdId })).url
  }

  // CR-12: one saved school per household can be the primary target (set_household_primary_school).
  readonly supportsPrimarySchool = true

  async primarySchool(householdId: string): Promise<string | null> {
    const { data, error } = await this.sb.from('household_saved_schools').select('institution_key').eq('household_id', householdId).eq('is_primary', true).maybeSingle()
    if (error) fail(error)
    return (data?.institution_key as string | undefined) ?? null
  }

  async setPrimarySchool(householdId: string, institutionKey: string | null): Promise<void> {
    await rpc<null>(this.sb, 'set_household_primary_school', { p_household: householdId, p_institution_key: institutionKey })
  }

  async interests(studentId: string): Promise<InterestProfile> {
    const { data, error } = await this.sb.from('student_academic_interests').select('certainty, interests').eq('student_id', studentId).maybeSingle()
    if (error) fail(error)
    return { certainty: (data?.certainty as MajorCertainty | null) ?? null, interests: ((data?.interests as SavedInterest[] | null) ?? []).slice(0, MAX_INTERESTS) }
  }

  async saveInterests(studentId: string, p: InterestProfile) {
    // Only kind/key and a true focus are stored (the server rejects other fields).
    const row = { certainty: p.certainty, interests: p.interests.slice(0, MAX_INTERESTS).map((i) => (i.focus ? { kind: i.kind, key: i.key, focus: true } : { kind: i.kind, key: i.key })) }
    const existing = await this.sb.from('student_academic_interests').select('student_id').eq('student_id', studentId).maybeSingle()
    if (existing.error) fail(existing.error)
    const r = existing.data
      ? await this.sb.from('student_academic_interests').update(row).eq('student_id', studentId)
      : await this.sb.from('student_academic_interests').insert({ student_id: studentId, ...row })
    if (r.error) fail(r.error)
  }

  async verifiedSchools(academicYear: string, state?: string): Promise<InstitutionSearchHit[]> {
    return rpc<InstitutionSearchHit[]>(this.sb, 'institutions_with_verified_records', { p_academic_year: academicYear, p_state: state ?? null })
  }

  async searchInstitutions(query: string, state?: string): Promise<InstitutionSearchHit[]> {
    let q = this.sb.from('institutions').select('institution_key, display_name, city, state_code, control, level').order('display_name').limit(20)
    if (query.trim()) q = q.ilike('display_name', `%${query.trim().replace(/[%_]/g, '')}%`)
    if (state) q = q.eq('state_code', state)
    const { data, error } = await q
    if (error) fail(error)
    return data ?? []
  }

  async compareInstitutions(keys: string[], academicYear: string) {
    const r = await rpc<{ institutions: InstitutionComparison[] }>(this.sb, 'compare_institutions', {
      p_institution_keys: keys,
      p_academic_year: academicYear,
    })
    return r.institutions
  }

  costProjection(studentId: string, institutionKeys: string[], academicYear: string, assumptions: CostAssumptions) {
    return rpc<CostProjectionResult>(this.sb, 'cost_projection', {
      p_student: studentId,
      p_institution_keys: institutionKeys,
      p_academic_year: academicYear,
      p_assumptions: assumptions,
    })
  }
}
