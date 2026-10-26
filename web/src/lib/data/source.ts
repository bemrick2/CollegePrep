import type { ReminderSettings } from '../../../../supabase/functions/_shared/reminders.ts'
export type { ReminderSettings }
import type { InterestProfile } from '../engine/interests'
import type { PlannedExam } from '../engine/examCredit'
import type { NextWeekSuggestion } from '../engine/weeklyPlan'
import type {
  SetupProgress,
  AiHelpResult,
  AttemptRecord,
  BenchmarkSummary,
  CostAssumptions,
  CostProjectionResult,
  ExamFamily,
  HelpMode,
  HintResult,
  HouseholdContext,
  InstitutionComparison,
  InstitutionSearchHit,
  Entitlement,
  BillingPlan,
  PracticeSession,
  PublicQuestion,
  Skill,
  SkillEstimate,
  Strategy,
  Streak,
  StudentPlan,
  SubmitInput,
  SubmitResult,
  TestScore,
  TrapType,
  Viewer,
  WeeklyProgress,
} from './types'

/**
 * Everything the UI reads or writes. LiveSource maps each call to a Supabase
 * table read or RPC; DemoSource reproduces the same rules on local fixtures.
 */
export interface DataSource {
  readonly mode: 'demo' | 'live'

  getViewer(): Promise<Viewer | null>
  signOut(): Promise<void>

  // Households and students
  getHouseholdContext(): Promise<HouseholdContext>
  createHousehold(name: string, timeZone: string): Promise<string>
  addStudent(householdId: string, displayName: string, graduationYear: number | null, gradeLevel: number | null): Promise<string>
  createSelfStudentProfile(input: {
    displayName: string
    graduationYear: number | null
    gradeLevel: number | null
    independent: boolean
    timeZone: string | null
  }): Promise<string>
  createInvitation(householdId: string, role: 'guardian' | 'student', studentId?: string): Promise<string>
  acceptInvitation(code: string): Promise<string>
  /** Create (replacing that student's outstanding invite) or resend a student invitation by email, server-side.
   *  Email failure never invalidates the invitation: the code comes back so it can be copied. */
  sendStudentInvitation(input: { householdId: string; studentId: string; email: string; code?: string; inviteCode?: string }): Promise<InviteSendResult>
  /** A new student invitation (link token + invite code) without email; replaces that student's outstanding one. */
  createStudentInvitation(householdId: string, studentId: string): Promise<StudentInvitation>
  /** Outstanding and past invitations of a household the viewer guards (never the code or its hash). */
  listInvitations(householdId: string): Promise<InvitationSummary[]>
  revokeInvitation(invitationId: string): Promise<void>

  // Goals and progress
  setWeeklyGoal(studentId: string, weekStart: string, targetQuestions: number | null, targetMinutes: number | null): Promise<void>
  weeklyProgress(studentId: string, weekStart: string): Promise<WeeklyProgress>
  /** The backend's suggested question goal for the week after this one (suggest_next_week_goal). */
  suggestNextWeekGoal(studentId: string): Promise<NextWeekSuggestion>
  /** This viewer's own inactivity-alert setting for a student (alert_preferences, email channel). */
  getAlertPreference(studentId: string): Promise<AlertPreference | null>
  setAlertPreference(studentId: string, pref: AlertPreference): Promise<void>
  /** Students this guardian can see who have gone quiet past their alert threshold (student_inactivity). */
  inactiveStudents(): Promise<InactiveStudent[]>
  streak(studentId: string): Promise<Streak>
  skillEstimates(studentId: string): Promise<SkillEstimate[]>
  testScores(studentId: string): Promise<TestScore[]>
  /**
   * A score the family reports (unverified): `self_reported` for an official test, `practice_test` for a full
   * practice test (CR-26; never used for merit). Clients can never write an official or estimated score.
   */
  addTestScore(studentId: string, score: { exam_family: ExamFamily; test_date: string; composite: number; section_scores: Record<string, number>; source?: 'self_reported' | 'practice_test' }): Promise<string>
  /** CR-26: setup answers live on the account. False: they're kept in this browser (lib/setupProfile.ts). */
  readonly supportsAccountSetup: boolean
  setupProgress(studentId: string): Promise<SetupProgress | null>
  saveSetupProgress(studentId: string, patch: { setupCompleted?: boolean; startingPointAnswered?: boolean; benchmarkScheduledFor?: string | null }): Promise<void>
  attemptHistory(studentId: string, sinceIso: string): Promise<AttemptRecord[]>

  // Catalog
  catalog(examFamily: ExamFamily): Promise<{ skills: Skill[]; strategies: Strategy[]; traps: TrapType[] }>
  publishedQuestions(examFamily: ExamFamily): Promise<PublicQuestion[]>

  // Practice
  startSession(studentId: string, targetMinutes: number, examFamily: ExamFamily): Promise<PracticeSession>
  endSession(sessionId: string): Promise<void>
  /** An attempt belongs to a practice session or a benchmark, never both. */
  startAttempt(studentId: string, questionId: string, sessionId: string | null, benchmarkId?: string | null): Promise<string>
  recordEvent(attemptId: string, kind: 'answered' | 'skipped' | 'returned', answer?: string): Promise<string>
  requestHint(attemptId: string): Promise<HintResult>
  submitAttempt(attemptId: string, input: SubmitInput): Promise<SubmitResult>
  requestAiHelp(attemptId: string, mode: HelpMode): Promise<AiHelpResult>
  /** "Remember this" takeaway for sources whose submit result doesn't carry `remember_text`. */
  rememberThis(questionId: string): Promise<string | null>

  // Planning preferences (CR-1) and benchmarks (CR-2)
  getPlan(studentId: string): Promise<StudentPlan | null>
  savePlan(studentId: string, plan: StudentPlan): Promise<void>
  listBenchmarks(studentId: string): Promise<BenchmarkSummary[]>
  /** Opens a benchmark that groups the attempts that follow (start_benchmark). */
  startBenchmark(studentId: string, kind: BenchmarkSummary['kind'], examFamily: ExamFamily): Promise<string>
  /** Closes it. Live stores the server's metrics; `client` carries the staircase details the server doesn't compute. */
  completeBenchmark(studentId: string, benchmarkId: string, client: BenchmarkSummary): Promise<BenchmarkSummary>

  // CR-23 reserved assessment pool. Reserved content is readable only inside an open check, so sizes come as counts.
  /** Per section: reserved items and how many this student hasn't seen. null when the source can't say. */
  assessmentPoolStatus(studentId: string, examFamily: ExamFamily): Promise<PoolStatus[] | null>
  /** The reserved items an open check may still use, unseen first, then repeats (each flagged). */
  benchmarkQuestions(benchmarkId: string, studentId: string, examFamily: ExamFamily): Promise<CheckItem[]>
  /** Which checks the server will open now (#279): the student's live check, if any, and the kinds allowed. */
  benchmarkOptions(studentId: string, examFamily: ExamFamily): Promise<CheckOptions>
  /** Per section of an open check: items assigned to it and items already used (answered or skipped). */
  benchmarkProgress(benchmarkId: string, studentId: string): Promise<CheckProgress[]>

  // Saved schools (CR-9) and verified-school listing (CR-7)
  savedSchools(householdId: string): Promise<string[]>
  saveSchool(householdId: string, institutionKey: string): Promise<void>
  removeSchool(householdId: string, institutionKey: string): Promise<void>
  /** Who saved each school (user id), where the source knows; removal follows it (#218 C6). */
  savedSchoolAdders?(householdId: string): Promise<Record<string, string | null>>
  verifiedSchools(academicYear: string, state?: string): Promise<InstitutionSearchHit[]>
  /** One saved school the family elevates as its primary target (CR-12). False until the backend supports it;
   *  the UI hides the control and shows no primary while false. */
  readonly supportsPrimarySchool: boolean
  /**
   * CR-10: AP and CLEP exams on the account (student_exam_plan, keyed by exam_catalog). False in the demo and until
   * VITE_EXAM_PLAN=true; the plan then stays on this device. IB and Statewide Dual Credit (no catalog key yet) stay
   * on the device either way.
   */
  readonly supportsExamPlan: boolean
  examPlan(studentId: string): Promise<PlannedExam[]>
  /** Saves one exam; rejects with code 'invalid' when it has no catalog key (the caller keeps it on the device). */
  saveExamPlanEntry(studentId: string, exam: PlannedExam): Promise<void>
  removeExamPlanEntry(studentId: string, examKey: string): Promise<void>
  /** True when the backend stores the weekly-summary opt-in (CR-22). The demo stores it but sends no email. */
  readonly supportsWeeklyDigest: boolean
  /** Emails actually sent to this guardian, newest first; null where the backend can't say (CR-22 not applied). */
  emailDeliveries(): Promise<EmailDelivery[] | null>

  /** Practice reminders (CR-27). False where the backend doesn't have them: the app then offers none. */
  readonly supportsReminders: boolean
  reminderSettings(studentId: string): Promise<ReminderSettings>
  /** Guardians are told only when the student's own login turns reminders off (and isn't independent). */
  saveReminderSettings(studentId: string, settings: ReminderSettings): Promise<{ guardiansNotified: boolean }>
  /** "Remind me later". Never notifies anyone. Returns when reminders resume. */
  snoozeReminders(studentId: string, minutes: number): Promise<string>
  /** What this device allowed when the app last opened here. */
  /** channel 'fcm' + token: the native app (Capacitor shell); 'webpush' + subscription: a browser. */
  reportNotificationDevice(input: { deviceId: string; permission: DevicePermission; subscription: PushSubscriptionJSON | null; platform: DevicePlatform; channel?: 'webpush' | 'fcm'; token?: string | null }): Promise<void>
  studentDevices(studentId: string): Promise<DeviceStatus[]>
  reminderHistory(studentId: string): Promise<ReminderChange[]>
  latestReminder(studentId: string): Promise<ReminderDelivery | null>
  markReminderOpened(deliveryId: string): Promise<void>
  /** Major certainty and up to 8 saved areas/majors (CR-13). Optional everywhere; empty when never set. */
  interests(studentId: string): Promise<InterestProfile>
  saveInterests(studentId: string, profile: InterestProfile): Promise<void>
  // Household billing (CR-16). Web purchases go through Stripe Checkout; access is the household entitlement.
  /** False in the demo and until VITE_BILLING_ENABLED=true; the UI then shows no plan, price or checkout. */
  readonly supportsBilling: boolean
  entitlement(householdId: string): Promise<Entitlement>
  billingPlans(): Promise<BillingPlan[]>
  /** URL of a Stripe Checkout page for the household plan. */
  startCheckout(householdId: string, lookupKey: string): Promise<string>
  /** URL of the Stripe Customer Portal for the household's web subscription. */
  billingPortalUrl(householdId: string): Promise<string>
  primarySchool(householdId: string): Promise<string | null>
  /** null clears it. The key must already be saved. */
  setPrimarySchool(householdId: string, institutionKey: string | null): Promise<void>

  // Colleges
  searchInstitutions(query: string, state?: string): Promise<InstitutionSearchHit[]>
  compareInstitutions(keys: string[], academicYear: string): Promise<InstitutionComparison[]>
  /** CR-4 v2: one call per set of schools that share the same assumptions (residency, credits). */
  costProjection(studentId: string, institutionKeys: string[], academicYear: string, assumptions: CostAssumptions): Promise<CostProjectionResult>
}

export class DataError extends Error {
  constructor(
    message: string,
    readonly code: 'forbidden' | 'invalid' | 'not_found' | 'network' | 'unknown' = 'unknown',
  ) {
    super(message)
  }
}

export interface StudentInvitation {
  /** Link token: long, unguessable, only ever put in a link. */
  code: string
  /** Human invite code, XXXXX-XXXXX. */
  inviteCode: string
  invitationId: string
  expiresAt: string
}

export interface InviteSendResult {
  /** Present when a new invitation was created (or the one being resent); absent if creation itself failed. */
  code?: string
  inviteCode?: string
  invitationId?: string
  expiresAt?: string
  emailed: boolean
  /** not_configured: email isn't set up; provider: the email service failed; rejected: the invitation can't be
   *  emailed (used, revoked, expired, too many sends); demo: demo mode never sends email. */
  reason?: 'not_configured' | 'provider' | 'rejected' | 'demo'
  error?: string
}

export interface InvitationSummary {
  id: string
  role: 'guardian' | 'student'
  student_id: string | null
  recipient_email: string | null
  created_at: string
  expires_at: string
  accepted_at: string | null
  revoked_at: string | null
  last_emailed_at: string | null
}

/** One email the server recorded as sent to the signed-in guardian (CR-22 parent_email_deliveries). */
export type DevicePermission = 'granted' | 'denied' | 'default' | 'unsupported'
export type DevicePlatform = 'ios' | 'android' | 'desktop' | 'other'

export interface DeviceStatus {
  deviceId: string
  permission: DevicePermission
  platform: DevicePlatform | null
  /** Allowed, subscribed, and the push service hasn't dropped it. */
  canReceive: boolean
  /** When the app last opened on that device. Device settings changed since then aren't known. */
  checkedAt: string
}

export interface ReminderChange {
  id: string
  enabled: boolean
  by: 'student' | 'guardian'
  at: string
  notifyGuardians: boolean
  /** For the signed-in guardian: when the notice was actually emailed to them; null if not (yet). */
  emailedToMeAt: string | null
}

/** A reminder the server recorded as accepted by a push service (status 'sent'). Never a test or a simulation. */
export interface ReminderDelivery {
  id: string
  sentAt: string
  openedAt: string | null
  snoozedAt: string | null
  /** webpush (a browser or Home Screen web app) or fcm (the native app); null on older rows. */
  channel?: 'webpush' | 'fcm' | null
}

export interface EmailDelivery {
  kind: 'weekly_digest' | 'inactivity' | 'reminders_off'
  /** weekly_digest: the week's Monday. inactivity: the student it was about. */
  weekStart: string | null
  studentId: string | null
  sentAt: string
}

export interface AlertPreference {
  /** The inactivity alert. */
  enabled: boolean
  /** 1-60 days without practice before the guardian is told. */
  inactivityDays: number
  /** Monday email summary of the student's week (CR-22). Only stored where supportsWeeklyDigest. */
  weeklyDigest?: boolean
}

export interface InactiveStudent {
  studentId: string
  daysInactive: number | null
  thresholdDays: number
  lastSubmittedAt: string | null
}

/** CR-23: one section of the reserved pool, as counts only. */
export interface PoolStatus {
  section: string
  reserved: number
  unseen: number
}

/** #279: what the server will start now. A live check is resumed, never replaced by fresh questions. */
export interface CheckOptions {
  initialAllowed: boolean
  miniAllowed: boolean
  /** First date (yyyy-mm-dd) a mini check opens, when it isn't open yet; null otherwise. */
  miniOpensOn: string | null
  fullAllowed: boolean
  /** The student's live check of this exam, if any. */
  open: { id: string; kind: 'initial' | 'mini' | 'full'; startedAt: string } | null
}

/** #279: per section of an open check, items assigned and items already used (answered or skipped). */
export interface CheckProgress {
  section: string
  assigned: number
  used: number
}

/** CR-23: a reserved item an open check may use. */
export interface CheckItem {
  question: PublicQuestion
  seen_before: boolean
}
