import { useEffect, useState, type FormEvent } from 'react'
import { Navigate, useNavigate, useSearchParams } from 'react-router-dom'
import { signupConfirmationUrl } from '../../lib/authRedirect'
import { supabase } from '../../lib/supabase'
import { homePathFor, useApp } from '../../lib/app'
import { Brand } from '../../components/shell'
import { Button, Card, Field, Notice, Segmented, inputClass } from '../../components/ui'

export function Auth() {
  const [params] = useSearchParams()
  const role = params.get('role')
  const { viewer, ctx, refresh, startDemo, mode, useLive } = useApp()
  const navigate = useNavigate()
  const [tab, setTab] = useState<'signup' | 'signin'>(role ? 'signup' : 'signin')
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string | null>(null)
  const [info, setInfo] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)

  // Confirmation links can open in a fresh browser or from a previous demo session.
  useEffect(() => { if (supabase && mode !== 'live') useLive() }, [mode, useLive])

  if (!supabase) return <Navigate to="/" replace />
  if (viewer) {
    const home = homePathFor(viewer, ctx)
    if (home === '/start' && role) return <Navigate to={`/onboarding/${role}`} replace />
    return <Navigate to={home} replace />
  }

  const submit = async (e: FormEvent) => {
    e.preventDefault()
    setError(null)
    setInfo(null)
    setBusy(true)
    try {
      if (tab === 'signup') {
        const { data, error: err } = await supabase!.auth.signUp({ email, password, options: { data: { display_name: name }, emailRedirectTo: signupConfirmationUrl(window.location.origin, import.meta.env.DEV, role) } })
        if (err) throw err
        if (!data.session) {
          setInfo('Check your email to confirm your account, then sign in.')
          setTab('signin')
          return
        }
        await supabase!.from('profiles').upsert({ id: data.user!.id, display_name: name || null })
      } else {
        const { error: err } = await supabase!.auth.signInWithPassword({ email, password })
        if (err) throw err
      }
      await refresh()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Something went wrong')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="grid min-h-dvh place-items-center px-4 py-10">
      <div className="w-full max-w-md">
        <div className="mb-6 flex justify-center">
          <Brand />
        </div>
        <Card className="p-6">
          <div className="flex justify-center">
            <Segmented
              label="Account"
              value={tab}
              onChange={setTab}
              options={[
                { value: 'signup', label: 'Create account' },
                { value: 'signin', label: 'Sign in' },
              ]}
            />
          </div>
          <form onSubmit={submit} className="mt-6 grid gap-4">
            {tab === 'signup' && (
              <Field label="Your first name" htmlFor="name">
                <input id="name" className={inputClass} value={name} onChange={(e) => setName(e.target.value)} autoComplete="given-name" required />
              </Field>
            )}
            <Field label="Email" htmlFor="email">
              <input id="email" type="email" className={inputClass} value={email} onChange={(e) => setEmail(e.target.value)} autoComplete="email" required />
            </Field>
            <Field label="Password" htmlFor="password" hint={tab === 'signup' ? 'At least 8 characters' : undefined}>
              <input
                id="password"
                type="password"
                minLength={8}
                className={inputClass}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                autoComplete={tab === 'signup' ? 'new-password' : 'current-password'}
                required
              />
            </Field>
            {error && <Notice tone="bad">{error}</Notice>}
            {info && <Notice tone="info">{info}</Notice>}
            <Button type="submit" size="lg" block disabled={busy}>
              {busy ? 'One moment…' : tab === 'signup' ? 'Create account' : 'Sign in'}
            </Button>
          </form>
        </Card>
        <p className="mt-4 text-center text-sm text-ink-3">
          Not ready?{' '}
          <button
            className="font-semibold text-ink underline-offset-2 hover:underline"
            onClick={async () => {
              await startDemo(role === 'parent' ? 'parent' : 'student', true)
              navigate(role === 'parent' ? '/parent' : '/student')
            }}
          >
            Explore the demo
          </button>
        </p>
      </div>
    </div>
  )
}
