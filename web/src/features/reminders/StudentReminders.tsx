import { Navigate } from 'react-router-dom'
import { useApp, useAsync } from '../../lib/app'
import { browserTimeZone } from '../../lib/engine/dates'
import { Card, PageLoading } from '../../components/ui'
import { ReminderSettingsPanel, ThisDevice } from './Reminders'

/** The student's clearly labelled place to change or turn off practice reminders. */
export function StudentReminders() {
  const { source, ctx } = useApp()
  const me = ctx?.myStudent ?? null
  const settings = useAsync(() => (me && source.supportsReminders ? source.reminderSettings(me.id) : Promise.resolve(null)), [source, me?.id])
  if (!me) return <Navigate to="/" replace />
  if (settings.loading) return <PageLoading />
  const tz = me.time_zone ?? ctx?.households.find((h) => h.id === me.household_id)?.time_zone ?? browserTimeZone()
  return (
    <div className="mx-auto grid max-w-xl gap-6">
      <h1 className="display text-[28px] font-semibold text-ink">Practice reminders</h1>
      {!source.supportsReminders ? (
        <p className="text-ink-2">Practice reminders aren't available yet.</p>
      ) : (
        <>
          <Card className="p-5">
            <ReminderSettingsPanel studentId={me.id} name={me.display_name} as="student" canEdit hasGuardian={!!me.household_id && !me.is_independent} timeZone={tz} />
          </Card>
          <ThisDevice remindersOn={!!settings.data?.enabled} />
        </>
      )}
    </div>
  )
}
