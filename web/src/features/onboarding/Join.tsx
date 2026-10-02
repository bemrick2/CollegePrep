import { useState, type FormEvent } from 'react'
import { Navigate, useNavigate, useSearchParams } from 'react-router-dom'
import { useApp } from '../../lib/app'
import { Button, Field, Notice, inputClass } from '../../components/ui'
import { StepFrame } from './Stepper'

export function Join() {
  const { source, viewer, refresh } = useApp()
  const [params] = useSearchParams()
  const navigate = useNavigate()
  const [code, setCode] = useState(params.get('code') ?? '')
  const [error, setError] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)

  if (!viewer) return <Navigate to="/" replace />

  const submit = async (e?: FormEvent) => {
    e?.preventDefault()
    setBusy(true)
    setError(null)
    try {
      await source.acceptInvitation(code)
      await refresh()
      const ctx = await source.getHouseholdContext()
      navigate(ctx.myStudent ? '/student' : '/parent')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'That code did not work')
    } finally {
      setBusy(false)
    }
  }

  return (
    <StepFrame
      step={1}
      total={1}
      title="Join your household"
      subtitle="Enter the code your parent or guardian shared. Your practice history always stays with you."
      onBack={() => navigate(-1)}
      footer={
        <Button size="lg" block disabled={busy || code.trim().length < 6} onClick={() => void submit()}>
          {busy ? 'Joining…' : 'Join'}
        </Button>
      }
    >
      <form onSubmit={submit}>
        <Field label="Invite code" htmlFor="code">
          <input
            id="code"
            className={`${inputClass} font-mono text-xl uppercase tracking-[0.2em]`}
            value={code}
            onChange={(e) => setCode(e.target.value)}
            autoComplete="one-time-code"
            autoCapitalize="characters"
            spellCheck={false}
          />
        </Field>
        {error && <Notice tone="bad" className="mt-4">{error}</Notice>}
      </form>
    </StepFrame>
  )
}
