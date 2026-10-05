import { useState } from 'react'
import { Navigate, useNavigate } from 'react-router-dom'
import { homePathFor, useApp } from '../../lib/app'
import { Brand } from '../../components/shell'
import { ArrowRight, Bolt, Compass, Shield, Users, Wallet } from '../../components/icons'
import { Card, PageLoading } from '../../components/ui'

export function Landing() {
  const { viewer, ctx, loading, liveAvailable, startDemo, useLive } = useApp()
  const navigate = useNavigate()
  // Starting a demo signs the viewer in, which re-renders this page before any navigate() call lands; the
  // redirect below must therefore go where the person chose, not to the generic "who's using" step.
  const [intent, setIntent] = useState<string | null>(null)
  if (loading) return <PageLoading />
  if (viewer) return <Navigate to={intent ?? homePathFor(viewer, ctx)} replace />

  const begin = async (role: 'parent' | 'student') => {
    if (liveAvailable) {
      useLive()
      navigate(`/auth?role=${role}`)
    } else {
      setIntent(role === 'parent' ? '/onboarding/parent' : '/onboarding/student')
      await startDemo(role, false)
    }
  }

  const sample = async (role: 'parent' | 'student') => {
    setIntent(role === 'parent' ? '/parent' : '/student')
    await startDemo(role, true)
  }

  return (
    <div className="min-h-dvh">
      <header className="mx-auto flex h-16 max-w-6xl items-center px-4 md:px-6">
        <Brand />
        {liveAvailable && (
          <button
            className="ml-auto text-sm font-semibold text-ink-2 hover:text-ink"
            onClick={() => {
              useLive()
              navigate('/auth')
            }}
          >
            Sign in
          </button>
        )}
      </header>

      <main className="mx-auto max-w-6xl px-4 pb-16 md:px-6">
        <section className="grid items-center gap-10 pt-6 md:grid-cols-[1.1fr_1fr] md:pt-14">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.14em] text-go">ACT · SAT · College cost</p>
            <h1 className="display mt-3 text-[40px] font-semibold leading-[1.05] text-ink md:text-[56px]">
              Prepare smarter.
              <br />
              Navigate a better path.
              <br />
              <span className="text-brand">See what college could cost.</span>
            </h1>
            <p className="mt-5 max-w-lg text-lg text-ink-2">
              Short daily practice that adapts to your student, and a calm view of what each college path really costs — built only on verified data.
            </p>
          </div>

          <div className="grid gap-3">
            <RoleCard
              icon={<Users />}
              title="I'm a parent or guardian"
              body="Set up your household, add your student, and see progress and cost in one place."
              onClick={() => void begin('parent')}
            />
            <RoleCard
              icon={<Bolt />}
              title="I'm a student"
              body="Take a short benchmark, then practise about ten minutes a day. Invite a parent later if you want."
              onClick={() => void begin('student')}
            />
            <div className="mt-2 rounded-2xl border border-dashed border-line-strong p-4">
              <div className="text-sm font-semibold text-ink">Just looking?</div>
              <p className="mt-0.5 text-sm text-ink-3">Explore a sample family with a few weeks of practice history. Nothing is saved to an account.</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <button onClick={() => void sample('student')} className="rounded-lg bg-surface-2 px-3 py-2 text-sm font-semibold text-ink hover:bg-surface-3">
                  Sample student view
                </button>
                <button onClick={() => void sample('parent')} className="rounded-lg bg-surface-2 px-3 py-2 text-sm font-semibold text-ink hover:bg-surface-3">
                  Sample parent view
                </button>
              </div>
            </div>
          </div>
        </section>

        <section className="mt-16 grid gap-4 md:grid-cols-3" aria-label="What you get">
          <Feature icon={<Bolt />} title="About ten minutes a day" body="Each session targets the skills that move your score: weak knowledge first, then pacing." />
          <Feature icon={<Compass />} title="Know where you stand" body="Benchmarks separate what you know from how fast you work and how well your test strategy is working." />
          <Feature icon={<Wallet />} title="Real prices, clearly sourced" body="College costs come from official sources with dates. Missing data is shown as missing — never guessed." />
        </section>

        <p className="mt-10 flex items-center gap-2 text-xs text-ink-3">
          <Shield size={14} /> We never store a student's date of birth. Students own their practice history.
        </p>
      </main>
    </div>
  )
}

function RoleCard({ icon, title, body, onClick }: { icon: React.ReactNode; title: string; body: string; onClick: () => void }) {
  return (
    <button onClick={onClick} className="group flex items-start gap-4 rounded-2xl border border-line bg-surface p-5 text-left shadow-card transition hover:-translate-y-0.5 hover:shadow-lift">
      <span className="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-go-soft text-go">{icon}</span>
      <span className="min-w-0 flex-1">
        <span className="block text-lg font-semibold text-ink">{title}</span>
        <span className="mt-1 block text-sm text-ink-3">{body}</span>
      </span>
      <ArrowRight className="mt-1 shrink-0 text-ink-3 transition group-hover:translate-x-0.5 group-hover:text-ink" />
    </button>
  )
}

function Feature({ icon, title, body }: { icon: React.ReactNode; title: string; body: string }) {
  return (
    <Card className="p-5">
      <span className="text-brand">{icon}</span>
      <h2 className="mt-3 font-semibold text-ink">{title}</h2>
      <p className="mt-1 text-sm text-ink-3">{body}</p>
    </Card>
  )
}
