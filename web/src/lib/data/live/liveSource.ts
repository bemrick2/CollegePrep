import type { SupabaseClient } from '@supabase/supabase-js'
import type { DataSource } from '../source'
import { DataError } from '../source'
import type {
  AttemptRecord,
  BenchmarkSummary,
  Choice,
  CostProjection,
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

// Planning prefs and benchmark summaries have no backend table yet (CR-1, CR-2).
// They are kept per browser, keyed by student, until the contract lands.
const localKey = (kind: string, studentId: string) => `pp-live-${kind}-${studentId}`
function readLocal<T>(key: string): T | null {
  try {
    const raw = localStorage.getItem(key)
    return raw ? (JSON.parse(raw) as T) : null
  } catch {
    return null
  }
}
function writeLocal(key: string, value: unknown) {
  try {
    localStorage.setItem(key, JSON.stringify(value))
  } catch {
    // ignore
  }
}

const QUESTION_COLUMNS =
  'id, section, difficulty, difficulty_label, stem, choices, answer_format, expected_time_seconds, exam_versions!inner(exam_family), practice_question_skills(is_primary, skills(skill_key))'

interface QuestionRow {
  id: string
  section: string
  difficulty: number | null
  difficulty_label: PublicQuestion['difficulty_label']
  stem: string
  choices: unknown
  answer_format: PublicQuestion['answer_format']
  expected_time_seconds: number | null
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
    passage: null,
    choices: normalizeChoices(r.choices),
    answer_format: r.answer_format,
    expected_time_seconds: r.expected_time_seconds,
    primary_skill_key: r.practice_question_skills.find((s) => s.is_primary)?.skills?.skill_key ?? null,
    // Hint count is hidden server-side; the UI asks and handles "no more hints".
    hint_count: 1,
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
    return rpc<string>(this.sb, 'create_household_invitation', { p_household: householdId, p_role: role, p_student: studentId ?? null })
  }

  acceptInvitation(code: string) {
    return rpc<string>(this.sb, 'accept_household_invitation', { p_code: code.trim() })
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
      this.sb.from('skills').select('id, exam_family, section, domain, skill_key, name').eq('exam_family', examFamily),
      this.sb.from('question_strategies').select('strategy_key, name, description'),
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

  startAttempt(studentId: string, questionId: string, sessionId: string | null) {
    return rpc<string>(this.sb, 'start_practice_attempt', { p_student: studentId, p_question: questionId, p_session: sessionId })
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
    return null
  }

  async getPlan(studentId: string) {
    return readLocal<StudentPlan>(localKey('plan', studentId))
  }

  async savePlan(studentId: string, plan: StudentPlan) {
    writeLocal(localKey('plan', studentId), plan)
  }

  async listBenchmarks(studentId: string) {
    return readLocal<BenchmarkSummary[]>(localKey('benchmarks', studentId)) ?? []
  }

  async saveBenchmark(studentId: string, summary: BenchmarkSummary) {
    const list = await this.listBenchmarks(studentId)
    writeLocal(localKey('benchmarks', studentId), [...list, summary])
  }

  async searchInstitutions(query: string, state?: string): Promise<InstitutionSearchHit[]> {
    let q = this.sb.from('institutions').select('institution_key, display_name, city, state_code, control').order('display_name').limit(20)
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

  async costProjection(): Promise<CostProjection> {
    return {
      status: 'unavailable',
      reason: 'Cost projections need a verified household cost model, which the backend does not provide yet.',
    }
  }
}
