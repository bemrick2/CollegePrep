import { NavLink, Link, Outlet, useNavigate } from 'react-router-dom'
import type { ReactNode } from 'react'
import { useApp } from '../lib/app'
import { cx } from './ui'
import { Chart, Home, Logo, School, Users, Wallet } from './icons'

export function Brand({ to = '/' }: { to?: string }) {
  return (
    <Link to={to} className="flex items-center gap-2 font-semibold text-ink" aria-label="Prep & Price home">
      <Logo />
      <span className="display text-[19px] font-semibold">
        Prep <span className="text-gold-ink dark:text-gold">&amp;</span> Price
      </span>
    </Link>
  )
}

export function DemoBar() {
  const { mode, viewer, ctx, switchDemoPersona, resetDemo } = useApp()
  const navigate = useNavigate()
  if (mode !== 'demo' || !viewer) return null
  const isStudent = !!ctx?.myStudent
  const canSwitch = (ctx?.students.some((s) => s.linked_user_id && s.linked_user_id !== viewer.userId) ?? false) || (isStudent && (ctx?.households.length ?? 0) > 0)
  return (
    <aside aria-label="Demo mode" className="bg-hero text-hero-ink">
      <div className="mx-auto flex max-w-6xl flex-wrap items-center gap-x-3 gap-y-1 px-4 py-1.5 text-xs">
        <span className="font-semibold">Demo mode</span>
        <span className="hidden opacity-80 sm:inline">Practice questions and history are sample data stored in this browser.</span>
        <span className="ml-auto flex items-center gap-2">
          {canSwitch && (
            <button
              className="rounded-md bg-white/10 px-2 py-1 font-semibold hover:bg-white/20"
              onClick={async () => {
                const next = isStudent ? 'parent' : 'student'
                await switchDemoPersona(next)
                navigate(next === 'parent' ? '/parent' : '/student')
              }}
            >
              View as {isStudent ? 'parent' : 'student'}
            </button>
          )}
          <button
            className="rounded-md px-2 py-1 font-semibold opacity-80 hover:bg-white/10 hover:opacity-100"
            onClick={async () => {
              await resetDemo()
              navigate('/')
            }}
          >
            Exit demo
          </button>
        </span>
      </div>
    </aside>
  )
}

function TabLink({ to, icon, label, end }: { to: string; icon: ReactNode; label: string; end?: boolean }) {
  return (
    <NavLink
      to={to}
      end={end}
      className={({ isActive }) =>
        cx(
          'flex flex-1 flex-col items-center gap-0.5 py-2 text-[11px] font-semibold transition-colors md:flex-none md:flex-row md:gap-2 md:rounded-lg md:px-3 md:py-2 md:text-sm',
          isActive ? 'text-go md:bg-go-soft md:text-go-strong dark:md:text-go' : 'text-ink-3 hover:text-ink',
        )
      }
    >
      {icon}
      <span>{label}</span>
    </NavLink>
  )
}

export function StudentShell() {
  const { signOut, mode } = useApp()
  return (
    <div className="min-h-dvh pb-20 md:pb-0">
      <a href="#main" className="sr-only-focusable absolute left-2 top-2 z-50 rounded bg-surface px-3 py-2">
        Skip to content
      </a>
      <DemoBar />
      <header className="sticky top-0 z-30 border-b border-line bg-bg/90 backdrop-blur">
        <div className="mx-auto flex h-14 max-w-3xl items-center gap-4 px-4">
          <Brand to="/student" />
          <nav aria-label="Student" className="ml-6 hidden gap-1 md:flex">
            <TabLink to="/student" end icon={<Home />} label="Today" />
            <TabLink to="/student/progress" icon={<Chart />} label="Progress" />
            <TabLink to="/colleges" icon={<School />} label="Colleges" />
          </nav>
          {mode === 'live' && (
            <button onClick={() => void signOut()} className="ml-auto text-sm font-semibold text-ink-3 hover:text-ink">
              Sign out
            </button>
          )}
        </div>
      </header>
      <main id="main" className="mx-auto max-w-3xl px-4 pb-28 pt-5 md:py-8">
        <Outlet />
      </main>
      <nav aria-label="Student" className="fixed inset-x-0 bottom-0 z-30 flex border-t border-line bg-surface/95 pb-[env(safe-area-inset-bottom)] backdrop-blur md:hidden">
        <TabLink to="/student" end icon={<Home />} label="Today" />
        <TabLink to="/student/progress" icon={<Chart />} label="Progress" />
        <TabLink to="/colleges" icon={<School />} label="Colleges" />
      </nav>
    </div>
  )
}

export function ParentShell() {
  const { ctx, activeStudent, setActiveStudentId, signOut, mode } = useApp()
  const students = ctx?.students ?? []
  return (
    <div className="min-h-dvh">
      <a href="#main" className="sr-only-focusable absolute left-2 top-2 z-50 rounded bg-surface px-3 py-2">
        Skip to content
      </a>
      <DemoBar />
      <header className="sticky top-0 z-30 border-b border-line bg-bg/90 backdrop-blur">
        <div className="mx-auto flex h-16 max-w-6xl items-center gap-3 px-4 md:px-6">
          <Brand to="/parent" />
          <nav aria-label="Parent" className="ml-4 hidden gap-1 md:flex">
            <ParentLink to="/parent" end icon={<Home />} label="Overview" />
            <ParentLink to="/parent/progress" icon={<Chart />} label="Progress" />
            <ParentLink to="/colleges" icon={<Wallet />} label="Colleges & cost" />
            <ParentLink to="/parent/household" icon={<Users />} label="Household" />
          </nav>
          <div className="ml-auto flex items-center gap-3">
            {students.length > 1 && (
              <label className="flex items-center gap-2 text-sm">
                <span className="sr-only">Student</span>
                <select
                  className="h-9 rounded-lg border border-line-strong bg-surface px-2 text-sm font-semibold"
                  value={activeStudent?.id ?? ''}
                  onChange={(e) => setActiveStudentId(e.target.value)}
                >
                  {students.map((s) => (
                    <option key={s.id} value={s.id}>
                      {s.display_name}
                    </option>
                  ))}
                </select>
              </label>
            )}
            {mode === 'live' && (
              <button onClick={() => void signOut()} className="text-sm font-semibold text-ink-3 hover:text-ink">
                Sign out
              </button>
            )}
          </div>
        </div>
      </header>
      <main id="main" className="mx-auto max-w-6xl px-4 pb-28 pt-6 md:px-6 md:py-8">
        <Outlet />
      </main>
      <nav aria-label="Parent" className="fixed inset-x-0 bottom-0 z-30 flex border-t border-line bg-surface/95 pb-[env(safe-area-inset-bottom)] backdrop-blur md:hidden">
        <TabLink to="/parent" end icon={<Home />} label="Overview" />
        <TabLink to="/parent/progress" icon={<Chart />} label="Progress" />
        <TabLink to="/colleges" icon={<Wallet />} label="Colleges" />
        <TabLink to="/parent/household" icon={<Users />} label="Household" />
      </nav>
    </div>
  )
}

function ParentLink({ to, icon, label, end }: { to: string; icon: ReactNode; label: string; end?: boolean }) {
  return (
    <NavLink
      to={to}
      end={end}
      className={({ isActive }) =>
        cx(
          'flex shrink-0 items-center gap-2 rounded-lg px-3 py-1.5 text-sm font-semibold transition-colors',
          isActive ? 'bg-brand-soft text-brand' : 'text-ink-3 hover:bg-surface-2 hover:text-ink',
        )
      }
    >
      {icon}
      {label}
    </NavLink>
  )
}

/** Shared shell for screens both roles use (colleges): picks the viewer's shell. */
export function RoleShell() {
  const { ctx } = useApp()
  return ctx?.myStudent ? <StudentShell /> : <ParentShell />
}

/** Bare layout for onboarding and full-screen flows. */
export function FocusShell({ children }: { children?: ReactNode }) {
  return (
    <div className="min-h-dvh">
      <DemoBar />
      <main id="main">{children ?? <Outlet />}</main>
    </div>
  )
}
