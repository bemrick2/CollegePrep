import type {
  AiHelpResult,
  AttemptRecord,
  BenchmarkSummary,
  CostProjection,
  ExamFamily,
  HelpMode,
  HintResult,
  HouseholdContext,
  InstitutionComparison,
  InstitutionSearchHit,
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

  // Goals and progress
  setWeeklyGoal(studentId: string, weekStart: string, targetQuestions: number | null, targetMinutes: number | null): Promise<void>
  weeklyProgress(studentId: string, weekStart: string): Promise<WeeklyProgress>
  streak(studentId: string): Promise<Streak>
  skillEstimates(studentId: string): Promise<SkillEstimate[]>
  testScores(studentId: string): Promise<TestScore[]>
  attemptHistory(studentId: string, sinceIso: string): Promise<AttemptRecord[]>

  // Catalog
  catalog(examFamily: ExamFamily): Promise<{ skills: Skill[]; strategies: Strategy[]; traps: TrapType[] }>
  publishedQuestions(examFamily: ExamFamily): Promise<PublicQuestion[]>

  // Practice
  startSession(studentId: string, targetMinutes: number, examFamily: ExamFamily): Promise<PracticeSession>
  endSession(sessionId: string): Promise<void>
  startAttempt(studentId: string, questionId: string, sessionId: string | null): Promise<string>
  recordEvent(attemptId: string, kind: 'answered' | 'skipped' | 'returned', answer?: string): Promise<string>
  requestHint(attemptId: string): Promise<HintResult>
  submitAttempt(attemptId: string, input: SubmitInput): Promise<SubmitResult>
  requestAiHelp(attemptId: string, mode: HelpMode): Promise<AiHelpResult>
  /** "Remember this" takeaway. No backend column yet (contract request CR-5); null when unknown. */
  rememberThis(questionId: string): Promise<string | null>

  // Client-held until backend support exists (docs/frontend/CONTRACT_REQUESTS.md)
  getPlan(studentId: string): Promise<StudentPlan | null>
  savePlan(studentId: string, plan: StudentPlan): Promise<void>
  listBenchmarks(studentId: string): Promise<BenchmarkSummary[]>
  saveBenchmark(studentId: string, summary: BenchmarkSummary): Promise<void>

  // Colleges
  searchInstitutions(query: string, state?: string): Promise<InstitutionSearchHit[]>
  compareInstitutions(keys: string[], academicYear: string): Promise<InstitutionComparison[]>
  costProjection(studentId: string): Promise<CostProjection>
}

export class DataError extends Error {
  constructor(
    message: string,
    readonly code: 'forbidden' | 'invalid' | 'not_found' | 'network' | 'unknown' = 'unknown',
  ) {
    super(message)
  }
}
