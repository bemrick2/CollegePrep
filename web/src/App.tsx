import { Navigate, Route, Routes } from 'react-router-dom'
import { lazy, Suspense, type ReactNode } from 'react'
import { homePathFor, useApp } from './lib/app'
import { FocusShell, ParentShell, RoleShell, StudentShell } from './components/shell'
import { PageLoading } from './components/ui'
const Landing = lazy(() => import('./features/onboarding/Landing').then((m) => ({ default: m.Landing })))
const Auth = lazy(() => import('./features/onboarding/Auth').then((m) => ({ default: m.Auth })))
const Start = lazy(() => import('./features/onboarding/Start').then((m) => ({ default: m.Start })))
const ParentOnboarding = lazy(() => import('./features/onboarding/ParentOnboarding').then((m) => ({ default: m.ParentOnboarding })))
const StudentOnboarding = lazy(() => import('./features/onboarding/StudentOnboarding').then((m) => ({ default: m.StudentOnboarding })))
const Join = lazy(() => import('./features/onboarding/Join').then((m) => ({ default: m.Join })))
const StudentHome = lazy(() => import('./features/student/StudentHome').then((m) => ({ default: m.StudentHome })))
const Goals = lazy(() => import('./features/student/Goals').then((m) => ({ default: m.Goals })))
const PracticeSession = lazy(() => import('./features/practice/PracticeSession').then((m) => ({ default: m.PracticeSession })))
const Benchmark = lazy(() => import('./features/benchmark/Benchmark').then((m) => ({ default: m.Benchmark })))
const ParentProgressPage = lazy(() => import('./features/progress/Progress').then((m) => ({ default: m.ParentProgressPage })))
const StudentProgressPage = lazy(() => import('./features/progress/Progress').then((m) => ({ default: m.StudentProgressPage })))
const ParentDashboard = lazy(() => import('./features/parent/ParentDashboard').then((m) => ({ default: m.ParentDashboard })))
const Household = lazy(() => import('./features/parent/Household').then((m) => ({ default: m.Household })))
const Colleges = lazy(() => import('./features/colleges/Colleges').then((m) => ({ default: m.Colleges })))
const ExploreMajors = lazy(() => import('./features/majors/ExploreMajors').then((m) => ({ default: m.ExploreMajors })))
const Compare = lazy(() => import('./features/colleges/Compare').then((m) => ({ default: m.Compare })))
const CollegeDetail = lazy(() => import('./features/colleges/CollegeDetail').then((m) => ({ default: m.CollegeDetail })))
const CollegePaths = lazy(() => import('./features/colleges/CollegePaths').then((m) => ({ default: m.CollegePaths })))

function RequireViewer({ children }: { children: ReactNode }) {
  const { viewer, loading } = useApp()
  if (loading) return <PageLoading />
  if (!viewer) return <Navigate to="/" replace />
  return <>{children}</>
}

function RequireStudent({ children }: { children: ReactNode }) {
  const { viewer, ctx, loading } = useApp()
  if (loading) return <PageLoading />
  if (!viewer) return <Navigate to="/" replace />
  if (!ctx?.myStudent) return <Navigate to={homePathFor(viewer, ctx)} replace />
  return <>{children}</>
}

function RequireGuardian({ children }: { children: ReactNode }) {
  const { viewer, ctx, loading } = useApp()
  if (loading) return <PageLoading />
  if (!viewer) return <Navigate to="/" replace />
  if (!ctx?.memberships.some((m) => m.role === 'guardian')) return <Navigate to={homePathFor(viewer, ctx)} replace />
  return <>{children}</>
}

export function App() {
  return (
    <Suspense fallback={<PageLoading />}>
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/auth" element={<Auth />} />
      <Route element={<RequireViewer><FocusShell /></RequireViewer>}>
        <Route path="/start" element={<Start />} />
        <Route path="/onboarding/parent" element={<ParentOnboarding />} />
        <Route path="/onboarding/student" element={<StudentOnboarding />} />
      </Route>
      {/* Join handles its own sign-in redirect so an invite link opened on a new device keeps its code. */}
      <Route element={<FocusShell />}>
        <Route path="/join" element={<Join />} />
      </Route>
      <Route element={<RequireStudent><FocusShell /></RequireStudent>}>
        <Route path="/student/practice" element={<PracticeSession />} />
        <Route path="/student/benchmark" element={<Benchmark />} />
      </Route>
      <Route element={<RequireStudent><StudentShell /></RequireStudent>}>
        <Route path="/student" element={<StudentHome />} />
        <Route path="/student/progress" element={<StudentProgressPage />} />
        <Route path="/student/goals" element={<Goals />} />
      </Route>
      <Route element={<RequireGuardian><ParentShell /></RequireGuardian>}>
        <Route path="/parent" element={<ParentDashboard />} />
        <Route path="/parent/progress" element={<ParentProgressPage />} />
        <Route path="/parent/goals" element={<Goals forGuardian />} />
        <Route path="/parent/household" element={<Household />} />
      </Route>
      <Route element={<RequireViewer><RoleShell /></RequireViewer>}>
        <Route path="/colleges" element={<Colleges />} />
        <Route path="/colleges/paths" element={<CollegePaths />} />
        <Route path="/colleges/majors" element={<ExploreMajors />} />
        <Route path="/colleges/compare" element={<Compare />} />
        <Route path="/colleges/:key" element={<CollegeDetail />} />
      </Route>
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
    </Suspense>
  )
}
