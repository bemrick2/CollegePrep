import type { HouseholdContext, Student } from './data/types'

/**
 * Mirrors the server's can_edit_student_plans (#218 C1): the student's own login, or a guardian of the student's
 * household with set-goals. Covers the exam plan and academic interests. A view-only guardian sees them, changes nothing.
 */
export function canEditStudentPlans(student: Student | null | undefined, viewerId: string | null | undefined, ctx: HouseholdContext | null | undefined): boolean {
  if (!student) return false
  if (viewerId && student.linked_user_id === viewerId) return true
  return !!ctx?.memberships.some((m) => m.household_id === student.household_id && m.role === 'guardian' && m.can_set_goals)
}

/**
 * Mirrors remove_household_school (#218 C6): a guardian with manage-students or set-goals, or the member who saved
 * the school. `addedBy` null (not known on this source) allows only the guardian rule.
 */
export function canRemoveSavedSchool(householdId: string | null | undefined, addedBy: string | null | undefined, viewerId: string | null | undefined, ctx: HouseholdContext | null | undefined): boolean {
  if (!householdId) return true // a list kept in this browser
  if (viewerId && addedBy && addedBy === viewerId) return true
  return !!ctx?.memberships.some((m) => m.household_id === householdId && m.role === 'guardian' && (m.can_manage_students || m.can_set_goals))
}
