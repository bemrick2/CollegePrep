-- Covering indexes for foreign keys on the hottest practice/household paths
-- (Supabase performance advisor: unindexed_foreign_keys). Additive only.
create index if not exists practice_attempts_question_idx on public.practice_attempts(question_id);
create index if not exists practice_attempts_session_idx on public.practice_attempts(session_id);
create index if not exists practice_session_items_question_idx on public.practice_session_items(question_id);
create index if not exists alert_preferences_student_idx on public.alert_preferences(student_id);
create index if not exists ai_help_requests_attempt_idx on public.ai_help_requests(attempt_id);
create index if not exists household_invitations_student_idx on public.household_invitations(student_id);
create index if not exists subscriptions_owner_idx on public.subscriptions(owner_user_id);
create index if not exists practice_question_skills_skill_idx on public.practice_question_skills(skill_id);
