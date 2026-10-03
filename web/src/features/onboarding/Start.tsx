import { Link, Navigate } from 'react-router-dom'
import { homePathFor, useApp } from '../../lib/app'
import { Brand } from '../../components/shell'
import { Bolt, Users } from '../../components/icons'
import { ChoiceCard } from '../../components/ui'

/** Signed in, but no household or student profile yet. */
export function Start() {
  const { viewer, ctx } = useApp()
  if (!viewer) return <Navigate to="/" replace />
  const home = homePathFor(viewer, ctx)
  if (home !== '/start') return <Navigate to={home} replace />
  return (
    <div className="mx-auto max-w-md px-4 py-10">
      <Brand />
      <h1 className="display mt-8 text-[30px] font-semibold text-ink">Who's using Prep &amp; Price?</h1>
      <div className="mt-6 grid gap-3">
        <Link to="/onboarding/parent">
          <ChoiceCard selected={false} onClick={() => {}} icon={<Users />} title="I'm a parent or guardian" description="Set up a household and add a student" />
        </Link>
        <Link to="/onboarding/student">
          <ChoiceCard selected={false} onClick={() => {}} icon={<Bolt />} title="I'm a student" description="Start practising on your own" />
        </Link>
        <Link to="/join" className="mt-2 text-center text-sm font-semibold text-ink-2 hover:text-ink">
          I have an invite code
        </Link>
      </div>
    </div>
  )
}
