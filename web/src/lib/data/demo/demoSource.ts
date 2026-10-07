import { practiceExclusions } from '../../engine/freshness'
import { projectCosts } from '../../engine/costProjection'
import type { InterestProfile } from '../../engine/interests'
import { readInterests, writeInterests } from '../../interestStore'
import { INVITE_TTL_HOURS, formatInviteCode } from '../../invites'
import type { AlertPreference, DataSource, InactiveStudent, InvitationSummary, InviteSendResult, StudentInvitation } from '../source'
import { suggestNextWeek, type NextWeekSuggestion } from '../../engine/weeklyPlan'
import { DataError } from '../source'
import type {
  AttemptRecord,
  BillingPlan,
  Entitlement,
  BenchmarkSummary,
  Confidence,
  CostAssumptions,
  CostProjectionResult,
  ExamFamily,
  HelpMode,
  HouseholdContext,
  InstitutionComparison,
  InstitutionSearchHit,
  PracticeSession,
  PublicQuestion,
  Student,
  StudentPlan,
  SubmitInput,
  SubmitResult,
  TestScore,
  Viewer,
  WeeklyProgress,
} from '../types'
import type { FixtureQuestion } from './fixtures'
import { emptyStore, loadStore, saveStore, uid, type DemoAttempt, type DemoStore } from './store'
import { gradeAnswer } from '../../engine/grading'
import { recommend, skillEstimates, streakFrom, weeklyProgress } from '../../engine/analytics'
import { addDays, browserTimeZone, localDate, weekStartOf } from '../../engine/dates'
import { MAX_SAVED_SCHOOLS, readPrimarySchool, readSavedSchools, writePrimarySchool, writeSavedSchools } from '../../savedSchools'

export const DEMO_PARENT = 'demo-parent'
export const DEMO_STUDENT = 'demo-student'

// Fixtures and the comparison snapshot load on first use, so live-mode users never download them.
type Fx = typeof import('./fixtures') & {
  byId: Map<string, FixtureQuestion>
  snapshot: { academic_year: string; institutions: InstitutionComparison[] }
}
let fxPromise: Promise<Fx> | null = null
export function loadFixtures(): Promise<Fx> {
  fxPromise ??= Promise.all([import('./fixtures'), import('./comparison-snapshot.json'), import('./questionReview')]).then(([f, snap, review]) => ({
    ...f,
    // Only items whose current content a review approved are served (questionReview.ts).
    QUESTIONS: review.reviewedOnly(f.QUESTIONS),
    byId: new Map(f.QUESTIONS.map((q) => [q.id, q])),
    snapshot: snap.default as unknown as Fx['snapshot'],
  }))
  return fxPromise
}
const skillIdOf = (q: FixtureQuestion) => `sk-${q.primary_skill_key}`

export function toPublic(q: FixtureQuestion): PublicQuestion {
  return {
    id: q.id,
    exam_family: q.exam_family,
    section: q.section,
    difficulty: q.difficulty,
    difficulty_label: q.difficulty <= 2 ? 'easy' : q.difficulty >= 4 ? 'hard' : 'medium',
    stem: q.stem,
    passage: q.passage ?? null,
    choices: q.choices,
    answer_format: q.answer_format,
    expected_time_seconds: q.expected_time_seconds,
    primary_skill_key: q.primary_skill_key,
    hint_count: q.hints.length,
  }
}

const DEMO_ALPHABET = '23456789ABCDEFGHJKMNPQRSTWXYZ'
const delay = <T,>(v: T): Promise<T> => new Promise((r) => setTimeout(() => r(v), 0))

export class DemoSource implements DataSource {
  readonly mode = 'demo' as const
  private s: DemoStore

  /** `snapshot` replaces the bundled comparison snapshot, e.g. with records captured from the live
   *  compare_institutions RPC for an acceptance scenario (see web/src/acceptance). */
  constructor(store?: DemoStore, private opts: { snapshot?: Fx['snapshot'] } = {}) {
    this.s = store ?? loadStore()
  }

  private async snapshot(): Promise<Fx['snapshot']> {
    return this.opts.snapshot ?? (await loadFixtures()).snapshot
  }

  private commit() {
    saveStore(this.s)
  }

  /** Demo only: switch between the parent and student personas. */
  switchPersona(userId: string, displayName: string) {
    if (!this.s.users.some((u) => u.id === userId)) this.s.users.push({ id: userId, displayName })
    this.s.viewerId = userId
    this.commit()
  }

  replaceStore(store: DemoStore) {
    this.s = store
    this.commit()
  }

  /** Student ids in the current demo store (used to seed browser-only sample data). */
  sampleStudentIds(): string[] {
    return this.s.students.map((x) => x.id)
  }

  sampleHouseholdIds(): string[] {
    return this.s.households.map((x) => x.id)
  }

  reset() {
    this.s = emptyStore()
    this.commit()
  }

  private viewerId(): string {
    if (!this.s.viewerId) throw new DataError('Not signed in', 'forbidden')
    return this.s.viewerId
  }

  private student(id: string): Student {
    const st = this.s.students.find((x) => x.id === id)
    if (!st) throw new DataError('Student not found', 'not_found')
    return st
  }

  private tz(studentId: string): string {
    const st = this.student(studentId)
    const h = this.s.households.find((x) => x.id === st.household_id)
    return st.time_zone ?? h?.time_zone ?? 'UTC'
  }

  private canView(studentId: string): boolean {
    const me = this.viewerId()
    const st = this.student(studentId)
    if (st.linked_user_id === me) return true
    return this.s.members.some((m) => m.household_id === st.household_id && m.user_id === me && m.can_view_progress)
  }

  private requireView(studentId: string) {
    if (!this.canView(studentId)) throw new DataError('Not allowed to view this student', 'forbidden')
  }

  /** Mirrors can_set_student_goals: a guardian with set_goals, or the student's own login outside a household (or independent). */
  private canSetGoals(studentId: string): boolean {
    const me = this.viewerId()
    const st = this.student(studentId)
    if (st.linked_user_id === me && (!st.household_id || st.is_independent)) return true
    return this.s.members.some((m) => m.household_id === st.household_id && m.user_id === me && m.role === 'guardian' && m.can_set_goals)
  }

  /** Mirrors the self_reported insert policy: a guardian who manages students, or the student's own login. */
  private canReportScore(studentId: string): boolean {
    const me = this.viewerId()
    const st = this.student(studentId)
    return st.linked_user_id === me || this.s.members.some((m) => m.household_id === st.household_id && m.user_id === me && m.can_manage_students)
  }

  private requireLinked(studentId: string) {
    if (this.student(studentId).linked_user_id !== this.viewerId())
      throw new DataError("Only the student's own login can practise", 'forbidden')
  }

  private attemptsOf(studentId: string) {
    return this.s.attempts.filter((a) => a.student_id === studentId)
  }

  async getViewer(): Promise<Viewer | null> {
    const id = this.s.viewerId
    if (!id) return delay(null)
    const u = this.s.users.find((x) => x.id === id)
    return delay({ userId: id, displayName: u?.displayName ?? null, mode: 'demo' })
  }

  async signOut() {
    this.s.viewerId = null
    this.commit()
  }

  async getHouseholdContext(): Promise<HouseholdContext> {
    const me = this.viewerId()
    const memberships = this.s.members.filter((m) => m.user_id === me)
    const hids = new Set(memberships.map((m) => m.household_id))
    const myStudent = this.s.students.find((x) => x.linked_user_id === me) ?? null
    const students = this.s.students.filter(
      (x) => !x.archived_at && ((x.household_id && hids.has(x.household_id)) || x.linked_user_id === me),
    )
    return delay({
      households: this.s.households.filter((h) => hids.has(h.id)),
      memberships,
      students,
      myStudent,
    })
  }

  async createHousehold(name: string, timeZone: string) {
    const me = this.viewerId()
    const id = uid('h-')
    this.s.households.push({ id, name: name.trim(), time_zone: timeZone })
    this.s.members.push({
      household_id: id,
      user_id: me,
      role: 'guardian',
      can_manage_students: true,
      can_set_goals: true,
      can_view_progress: true,
      can_manage_members: true,
      can_manage_billing: true,
    })
    this.commit()
    return id
  }

  async addStudent(householdId: string, displayName: string, graduationYear: number | null, gradeLevel: number | null) {
    const me = this.viewerId()
    if (!this.s.members.some((m) => m.household_id === householdId && m.user_id === me && m.can_manage_students))
      throw new DataError('Not allowed to add students to this household', 'forbidden')
    const id = uid('st-')
    this.s.students.push({
      id,
      household_id: householdId,
      display_name: displayName.trim(),
      graduation_year: graduationYear,
      grade_level: gradeLevel,
      account_mode: 'guardian_managed',
      is_independent: false,
      linked_user_id: null,
      time_zone: null,
      archived_at: null,
    })
    this.commit()
    return id
  }

  async createSelfStudentProfile(input: {
    displayName: string
    graduationYear: number | null
    gradeLevel: number | null
    independent: boolean
    timeZone: string | null
  }) {
    const me = this.viewerId()
    if (this.s.students.some((x) => x.linked_user_id === me)) throw new DataError('You already have a student profile', 'invalid')
    const id = uid('st-')
    this.s.students.push({
      id,
      household_id: null,
      display_name: input.displayName.trim(),
      graduation_year: input.graduationYear,
      grade_level: input.gradeLevel,
      account_mode: 'student_login',
      is_independent: input.independent,
      linked_user_id: me,
      time_zone: input.timeZone,
      archived_at: null,
    })
    this.commit()
    return id
  }

  async createInvitation(householdId: string, role: 'guardian' | 'student', studentId?: string) {
    // Demo link tokens never look like live ones (64 hex), so a demo link can't switch a browser to live.
    const code = `demo_${Array.from({ length: 24 }, () => 'abcdefghjkmnpqrstwxyz23456789'[Math.floor(Math.random() * 29)]).join('')}`
    const short = Array.from({ length: 10 }, () => DEMO_ALPHABET[Math.floor(Math.random() * DEMO_ALPHABET.length)]).join('')
    this.s.invitations.push({
      id: uid(),
      created_at: new Date().toISOString(),
      code,
      short_code: short,
      household_id: householdId,
      role,
      student_id: studentId ?? null,
      expires_at: new Date(Date.now() + INVITE_TTL_HOURS * 3600_000).toISOString(),
      accepted_by: null,
    })
    this.commit()
    return code
  }

  async acceptInvitation(code: string) {
    const me = this.viewerId()
    // Same rule order and messages as accept_household_invitation, so the UI can tell them apart.
    const raw = code.trim()
    const norm = raw.toUpperCase().replace(/[^A-Z0-9]/g, '')
    const inv = this.s.invitations.find((i) => i.code === raw || (i.short_code != null && i.short_code === norm))
    if (!inv) throw new DataError('Invalid invitation code', 'invalid')
    if (inv.accepted_by) throw new DataError('Invitation has already been used', 'invalid')
    if (inv.revoked_at) throw new DataError('Invitation has been revoked', 'invalid')
    if (inv.expires_at <= new Date().toISOString()) throw new DataError('Invitation has expired', 'invalid')
    inv.accepted_by = me
    inv.accepted_at = new Date().toISOString()
    if (inv.role === 'guardian') {
      this.s.members.push({
        household_id: inv.household_id,
        user_id: me,
        role: 'guardian',
        can_manage_students: true,
        can_set_goals: true,
        can_view_progress: true,
        can_manage_members: false,
        can_manage_billing: false,
      })
    } else {
      const own = this.s.students.find((x) => x.linked_user_id === me)
      if (inv.student_id) {
        if (own && own.id !== inv.student_id) throw new DataError('You already have a student profile', 'invalid')
        const st = this.student(inv.student_id)
        st.linked_user_id = me
        st.account_mode = 'student_login'
      } else if (own) {
        own.household_id = inv.household_id
      } else {
        throw new DataError('Create your student profile first', 'invalid')
      }
      this.s.members.push({
        household_id: inv.household_id,
        user_id: me,
        role: 'student',
        can_manage_students: false,
        can_set_goals: false,
        can_view_progress: false,
        can_manage_members: false,
        can_manage_billing: false,
      })
    }
    this.commit()
    return inv.household_id
  }

  /** Demo mode never sends email; it creates (replacing) the invitation so the code can be copied. */
  async sendStudentInvitation(input: { householdId: string; studentId: string; email: string; code?: string; inviteCode?: string }): Promise<InviteSendResult> {
    const email = input.email.trim().toLowerCase()
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) throw new DataError('Enter a valid email address', 'invalid')
    const inv = input.code ? this.s.invitations.find((i) => i.code === input.code) : null
    const created = inv ? null : await this.createStudentInvitation(input.householdId, input.studentId)
    const row = inv ?? this.s.invitations.find((i) => i.code === created!.code)!
    row.recipient_email = email
    this.commit()
    return { code: row.code, inviteCode: formatInviteCode(row.short_code ?? ''), invitationId: row.id, expiresAt: row.expires_at, emailed: false, reason: 'demo' }
  }

  async createStudentInvitation(householdId: string, studentId: string): Promise<StudentInvitation> {
    const now = new Date().toISOString()
    for (const i of this.s.invitations)
      if (i.household_id === householdId && i.student_id === studentId && !i.accepted_by && !i.revoked_at && i.expires_at > now) i.revoked_at = now
    const code = await this.createInvitation(householdId, 'student', studentId)
    const row = this.s.invitations.find((i) => i.code === code)!
    return { code, inviteCode: formatInviteCode(row.short_code!), invitationId: row.id!, expiresAt: row.expires_at }
  }

  async listInvitations(householdId: string): Promise<InvitationSummary[]> {
    return delay(
      this.s.invitations
        .filter((i) => i.household_id === householdId)
        .map((i) => ({
          id: i.id ?? i.code,
          role: i.role,
          student_id: i.student_id,
          recipient_email: i.recipient_email ?? null,
          created_at: i.created_at ?? i.expires_at,
          expires_at: i.expires_at,
          accepted_at: i.accepted_at ?? (i.accepted_by ? i.expires_at : null),
          revoked_at: i.revoked_at ?? null,
          last_emailed_at: null,
        }))
        .reverse(),
    )
  }

  async revokeInvitation(invitationId: string) {
    const inv = this.s.invitations.find((i) => (i.id ?? i.code) === invitationId)
    if (!inv) throw new DataError('Not allowed to revoke this invitation', 'forbidden')
    if (inv.accepted_by) throw new DataError('Invitation has already been used', 'invalid')
    inv.revoked_at ??= new Date().toISOString()
    this.commit()
  }

  async setWeeklyGoal(studentId: string, weekStart: string, targetQuestions: number | null, targetMinutes: number | null) {
    if (!this.canSetGoals(studentId)) throw new DataError('Only a guardian with permission to set goals can set this goal', 'forbidden')
    const existing = this.s.goals.find((g) => g.student_id === studentId && g.week_start === weekStart)
    if (existing) {
      existing.target_questions = targetQuestions
      existing.target_minutes = targetMinutes
    } else {
      this.s.goals.push({ id: uid('g-'), student_id: studentId, week_start: weekStart, target_questions: targetQuestions, target_minutes: targetMinutes, goal_mode: 'fixed' })
    }
    this.commit()
  }

  async suggestNextWeekGoal(studentId: string): Promise<NextWeekSuggestion> {
    this.requireView(studentId)
    const tz = this.tz(studentId)
    const thisWeek = weekStartOf(localDate(new Date(), tz))
    const next = addDays(thisWeek, 7)
    const past = await Promise.all(
      [0, 1, 2, 3].map(async (n) => {
        const w = addDays(thisWeek, -7 * n)
        const p = await this.weeklyProgress(studentId, w)
        return { target: p.goal?.target_questions ?? null, done: p.questions_submitted }
      }),
    )
    return suggestNextWeek(next, past)
  }

  async getAlertPreference(studentId: string): Promise<AlertPreference | null> {
    this.requireView(studentId)
    return delay(this.s.alerts?.[`${this.viewerId()}:${studentId}`] ?? null)
  }

  async setAlertPreference(studentId: string, pref: AlertPreference) {
    this.requireView(studentId)
    if (pref.inactivityDays < 1 || pref.inactivityDays > 60) throw new DataError('Choose 1 to 60 days', 'invalid')
    this.s.alerts = { ...(this.s.alerts ?? {}), [`${this.viewerId()}:${studentId}`]: pref }
    this.commit()
  }

  async inactiveStudents(): Promise<InactiveStudent[]> {
    const me = this.viewerId()
    const out: InactiveStudent[] = []
    for (const [k, pref] of Object.entries(this.s.alerts ?? {})) {
      const [user, studentId] = k.split(':') as [string, string]
      if (user !== me || !pref.enabled) continue
      const last = this.attemptsOf(studentId).map((a) => a.submitted_at).sort().pop() ?? null
      const days = last ? Math.floor((Date.now() - new Date(last).getTime()) / 86_400_000) : null
      if (days === null || days >= pref.inactivityDays) out.push({ studentId, daysInactive: days, thresholdDays: pref.inactivityDays, lastSubmittedAt: last })
    }
    return delay(out)
  }

  async weeklyProgress(studentId: string, weekStart: string): Promise<WeeklyProgress> {
    const F = await loadFixtures()
    this.requireView(studentId)
    const tz = this.tz(studentId)
    const g = this.s.goals.find((x) => x.student_id === studentId && x.week_start === weekStart)
    const attempts = this.attemptsOf(studentId)
    return delay(
      weeklyProgress({
        studentId,
        weekStart,
        timeZone: tz,
        goal: g ? { target_questions: g.target_questions, target_minutes: g.target_minutes, goal_mode: g.goal_mode } : null,
        attempts,
        events: this.s.events.filter((e) => e.student_id === studentId),
        estimates: skillEstimates(attempts, F.SKILLS),
        today: localDate(new Date(), tz),
      }),
    )
  }

  async streak(studentId: string) {
    this.requireView(studentId)
    const tz = this.tz(studentId)
    return delay(streakFrom(this.attemptsOf(studentId), tz, localDate(new Date(), tz)))
  }

  async skillEstimates(studentId: string) {
    const F = await loadFixtures()
    this.requireView(studentId)
    return delay(skillEstimates(this.attemptsOf(studentId), F.SKILLS))
  }

  async testScores(studentId: string): Promise<TestScore[]> {
    this.requireView(studentId)
    return delay(this.s.scores.filter((x) => x.student_id === studentId))
  }

  async addTestScore(studentId: string, score: { exam_family: ExamFamily; test_date: string; composite: number; section_scores: Record<string, number> }) {
    if (!this.canReportScore(studentId)) throw new DataError('Not allowed to add a score for this student', 'forbidden')
    const id = uid('sc-')
    this.s.scores.push({ id, student_id: studentId, exam_family: score.exam_family, test_date: score.test_date, composite: score.composite, section_scores: score.section_scores, score_source: 'self_reported' })
    this.commit()
    return delay(id)
  }

  async attemptHistory(studentId: string, sinceIso: string): Promise<AttemptRecord[]> {
    this.requireView(studentId)
    return delay(
      this.attemptsOf(studentId)
        .filter((a) => a.submitted_at && a.submitted_at >= sinceIso)
        .map((a) => ({
          id: a.id,
          question_id: a.question_id,
          section: a.section,
          skill_key: a.skill_key,
          submitted_at: a.submitted_at!,
          elapsed_ms: a.elapsed_ms ?? 0,
          expected_time_seconds: a.expected_time_seconds,
          is_correct: a.is_correct,
          skipped: a.skipped,
          confidence: (a.confidence as Confidence | null) ?? null,
          hint_count: a.hint_count,
        })),
    )
  }

  async catalog(examFamily: ExamFamily) {
    const F = await loadFixtures()
    return delay({ skills: F.SKILLS.filter((s) => s.exam_family === examFamily), strategies: F.STRATEGIES, traps: F.TRAPS })
  }

  async publishedQuestions(examFamily: ExamFamily) {
    const F = await loadFixtures()
    return delay(F.QUESTIONS.filter((q) => q.exam_family === examFamily).map(toPublic))
  }

  async startSession(studentId: string, targetMinutes: number, examFamily: ExamFamily): Promise<PracticeSession> {
    const F = await loadFixtures()
    this.requireLinked(studentId)
    if (targetMinutes < 5 || targetMinutes > 15) throw new DataError('Sessions are 5 to 15 minutes', 'invalid')
    const attempts = this.attemptsOf(studentId)
    const all = F.QUESTIONS.filter((q) => q.exam_family === examFamily)
    // Keep the next progress check's fresh questions out of practice (engine/freshness.ts).
    const seen = new Set(attempts.map((a) => a.question_id))
    const held = practiceExclusions(examFamily, all, seen)
    const pool = all.filter((q) => !held.has(q.id))
    const plan = recommend(
      pool.map((q) => ({ id: q.id, skill_id: skillIdOf(q), expected_time_seconds: q.expected_time_seconds })),
      skillEstimates(attempts, F.SKILLS),
      attempts,
      targetMinutes,
    )
    const id = uid('ps-')
    this.s.sessions.push({ id, student_id: studentId, target_minutes: targetMinutes, started_at: new Date().toISOString(), ended_at: null, question_ids: plan.map((p) => p.question_id) })
    this.commit()
    return {
      id,
      target_minutes: targetMinutes,
      items: plan.map((p, i) => ({ position: i + 1, question: toPublic(F.byId.get(p.question_id)!), reason: p.reason, seen_before: seen.has(p.question_id) })),
    }
  }

  async endSession(sessionId: string) {
    const ps = this.s.sessions.find((x) => x.id === sessionId)
    if (ps && !ps.ended_at) ps.ended_at = new Date().toISOString()
    this.commit()
  }

  async startAttempt(studentId: string, questionId: string, sessionId: string | null, _benchmarkId?: string | null) {
    const F = await loadFixtures()
    this.requireLinked(studentId)
    const q = F.byId.get(questionId)
    if (!q) throw new DataError('Question is not available', 'invalid')
    const id = uid('pa-')
    const now = new Date().toISOString()
    const a: DemoAttempt = {
      id,
      student_id: studentId,
      session_id: sessionId,
      question_id: questionId,
      skill_id: skillIdOf(q),
      skill_key: q.primary_skill_key,
      section: q.section,
      presented_at: now,
      submitted_at: null,
      elapsed_ms: null,
      active_ms: null,
      expected_time_seconds: q.expected_time_seconds,
      is_correct: null,
      skipped: false,
      confidence: null,
      hint_count: 0,
      ai_help_used: false,
      strategy_key: null,
      selected_answer: null,
      attempt_number: this.attemptsOf(studentId).filter((x) => x.question_id === questionId).length + 1,
      last_answer: null,
    }
    this.s.attempts.push(a)
    this.s.events.push({ attempt_id: id, student_id: studentId, kind: 'presented', occurred_at: now })
    this.commit()
    return id
  }

  private openAttempt(attemptId: string): DemoAttempt {
    const a = this.s.attempts.find((x) => x.id === attemptId)
    if (!a) throw new DataError('Attempt not found', 'not_found')
    this.requireLinked(a.student_id)
    if (a.submitted_at) throw new DataError('Attempt was already submitted', 'invalid')
    return a
  }

  async recordEvent(attemptId: string, kind: 'answered' | 'skipped' | 'returned', answer?: string) {
    const a = this.openAttempt(attemptId)
    let k: 'answered' | 'changed_answer' | 'skipped' | 'returned' = kind
    if (kind === 'answered') {
      const v = (answer ?? '').trim()
      if (!v) throw new DataError('An answer is required', 'invalid')
      if (a.last_answer === v) return 'unchanged'
      if (a.last_answer !== null) k = 'changed_answer'
      a.last_answer = v
    }
    this.s.events.push({ attempt_id: attemptId, student_id: a.student_id, kind: k, occurred_at: new Date().toISOString() })
    this.commit()
    return k
  }

  async requestHint(attemptId: string) {
    const F = await loadFixtures()
    const a = this.openAttempt(attemptId)
    const q = F.byId.get(a.question_id)!
    if (a.hint_count >= q.hints.length) throw new DataError('No more hints for this question', 'invalid')
    const hint = q.hints[a.hint_count]!
    a.hint_count++
    this.s.events.push({ attempt_id: attemptId, student_id: a.student_id, kind: 'hint', occurred_at: new Date().toISOString() })
    this.commit()
    return { hint_number: a.hint_count, hint, remaining: q.hints.length - a.hint_count }
  }

  async submitAttempt(attemptId: string, input: SubmitInput): Promise<SubmitResult> {
    const F = await loadFixtures()
    const a = this.openAttempt(attemptId)
    const q = F.byId.get(a.question_id)!
    const skipped = input.skipped ?? false
    const answer = input.answer?.trim() || null
    if (skipped && answer) throw new DataError('A skipped attempt has no answer', 'invalid')
    if (!skipped && !answer) throw new DataError('An answer is required', 'invalid')
    const now = new Date()
    const elapsed = now.getTime() - new Date(a.presented_at).getTime()
    if (!skipped && a.last_answer !== null && a.last_answer !== answer)
      this.s.events.push({ attempt_id: attemptId, student_id: a.student_id, kind: 'changed_answer', occurred_at: now.toISOString() })
    a.submitted_at = now.toISOString()
    a.elapsed_ms = elapsed
    a.active_ms = input.activeMs !== undefined ? Math.min(input.activeMs, elapsed) : null
    a.selected_answer = answer
    a.is_correct = skipped ? null : gradeAnswer(q.answer_format, q.accepted_answers, answer!)
    a.skipped = skipped
    a.confidence = input.confidence ?? null
    a.strategy_key = input.strategyKey ?? null
    this.s.events.push({ attempt_id: attemptId, student_id: a.student_id, kind: skipped ? 'skipped' : 'submitted', occurred_at: now.toISOString() })
    this.commit()
    return {
      is_correct: a.is_correct,
      skipped,
      elapsed_ms: elapsed,
      accepted_answers: q.accepted_answers,
      teaching_explanation: q.teaching_explanation,
      strategy_explanation: q.strategy_explanation,
      distractors: [...q.distractors].sort((x, y) => x.choice.localeCompare(y.choice)),
      strategies: [...q.strategies].sort((x, y) => Number(y.is_fastest) - Number(x.is_fastest)),
    }
  }

  async requestAiHelp(attemptId: string, mode: HelpMode) {
    const a = this.s.attempts.find((x) => x.id === attemptId)
    if (!a) throw new DataError('Attempt not found', 'not_found')
    if (mode === 'answer_reveal' && !a.submitted_at) throw new DataError('The answer can only be revealed after submission', 'invalid')
    // Matches the backend default: AI help is recorded but disabled until a provider exists.
    return delay({ request_id: uid('ai-'), status: 'disabled' as const })
  }

  async rememberThis(questionId: string) {
    const F = await loadFixtures()
    return delay(F.byId.get(questionId)?.remember ?? null)
  }

  async getPlan(studentId: string) {
    return delay(this.s.plans[studentId] ?? null)
  }

  async savePlan(studentId: string, plan: StudentPlan) {
    if (!this.canSetGoals(studentId)) throw new DataError('Only a guardian with permission to set goals can change this plan', 'forbidden')
    this.s.plans[studentId] = plan
    this.commit()
  }

  async listBenchmarks(studentId: string) {
    return delay(this.s.benchmarks[studentId] ?? [])
  }

  async startBenchmark(studentId: string, _kind: BenchmarkSummary['kind'], _exam: ExamFamily) {
    this.requireLinked(studentId)
    return delay(uid('bm-'))
  }

  async completeBenchmark(studentId: string, benchmarkId: string, client: BenchmarkSummary) {
    const summary = { ...client, id: benchmarkId }
    ;(this.s.benchmarks[studentId] ??= []).push(summary)
    this.commit()
    return delay(summary)
  }

  // Saved schools live in this browser for the demo (one household per browser).
  async savedSchools(_householdId: string) {
    return delay(readSavedSchools())
  }

  async saveSchool(_householdId: string, key: string) {
    const list = readSavedSchools()
    if (list.includes(key)) return
    if (list.length >= MAX_SAVED_SCHOOLS) throw new DataError(`Up to ${MAX_SAVED_SCHOOLS} schools`, 'invalid')
    writeSavedSchools([...list, key])
  }

  async removeSchool(_householdId: string, key: string) {
    writeSavedSchools(readSavedSchools().filter((k) => k !== key))
    if (readPrimarySchool() === null) writePrimarySchool(null)
  }

  readonly supportsPrimarySchool = true
  // The demo keeps the weekly-summary choice so the preview can be tried; it never sends email.
  readonly supportsWeeklyDigest = true

  /** The demo never sends email, so there is nothing to list. */
  async emailDeliveries() {
    return delay([] as import('../source').EmailDelivery[])
  }

  async interests(studentId: string) {
    return readInterests(studentId)
  }

  async saveInterests(studentId: string, profile: InterestProfile) {
    writeInterests(studentId, profile)
  }

  // The demo has no billing: no plan, price or checkout is shown (nothing is simulated).
  readonly supportsBilling = false

  async entitlement(_householdId: string): Promise<Entitlement> {
    return { active: false, status: null, can_manage_billing: false }
  }

  async billingPlans(): Promise<BillingPlan[]> {
    return []
  }

  async startCheckout(): Promise<string> {
    throw new DataError('Billing is not available in the demo', 'invalid')
  }

  async billingPortalUrl(): Promise<string> {
    throw new DataError('Billing is not available in the demo', 'invalid')
  }

  async primarySchool(_householdId: string) {
    return delay(readPrimarySchool())
  }

  async setPrimarySchool(_householdId: string, key: string | null) {
    if (key && !readSavedSchools().includes(key)) throw new DataError('Save the school first', 'invalid')
    writePrimarySchool(key)
  }

  async verifiedSchools(academicYear: string): Promise<InstitutionSearchHit[]> {
    const snap = await this.snapshot()
    if (academicYear !== snap.academic_year) return delay([])
    const list = (snap.institutions as unknown as InstitutionComparison[])
      .filter((x) => x.institution)
      .map((x) => ({
        institution_key: x.institution_key,
        display_name: x.institution!.display_name,
        city: x.institution!.city,
        state_code: x.institution!.state_code,
        control: x.institution!.control,
        level: x.institution!.level ?? null,
        domains: Object.entries(x.domains).filter(([, v]) => (v as unknown[]).length > 0).map(([k]) => k),
      }))
      .filter((x) => x.domains.length > 0)
    return delay(list)
  }

  async searchInstitutions(query: string, state?: string): Promise<InstitutionSearchHit[]> {
    const snap = await this.snapshot()
    const q = query.trim().toLowerCase()
    const list = (snap.institutions as unknown as InstitutionComparison[])
      .filter((x) => x.institution)
      .map((x) => ({
        institution_key: x.institution_key,
        display_name: x.institution!.display_name,
        city: x.institution!.city,
        state_code: x.institution!.state_code,
        control: x.institution!.control,
      }))
    return delay(list.filter((x) => (!q || x.display_name.toLowerCase().includes(q)) && (!state || x.state_code === state)))
  }

  async compareInstitutions(keys: string[], academicYear: string): Promise<InstitutionComparison[]> {
    const snap = await this.snapshot()
    const all = snap.institutions as unknown as InstitutionComparison[]
    return delay(
      keys.map(
        (k) =>
          (academicYear === snap.academic_year ? all.find((x) => x.institution_key === k) : undefined) ?? {
            institution_key: k,
            found: false,
            institution: null,
            academic_year: academicYear,
            domains: {} as InstitutionComparison['domains'],
            missing_domains: [],
            can_offer_paid_addon: false,
          },
      ),
    )
  }

  async costProjection(_studentId: string, keys: string[], academicYear: string, assumptions: CostAssumptions): Promise<CostProjectionResult> {
    // Same rules as the server (engine/costProjection.ts mirrors cost_projection v2) over the sample's verified records.
    return delay(projectCosts(await this.compareInstitutions(keys, academicYear), academicYear, assumptions))
  }

}

export function demoTimeZone() {
  return browserTimeZone()
}
