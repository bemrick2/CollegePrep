-- Legacy subscription reads must also exclude test purchases.
alter policy subscription_read on public.subscriptions to authenticated
  using (environment = 'production' and
    (owner_user_id = (select auth.uid()) or public.has_household_permission(household_id, 'manage_billing')));

create or replace function public.household_entitlements(p_household uuid)
returns table(plan_key text, status text, current_period_end timestamptz)
language plpgsql stable security definer set search_path = '' as $$
begin
  if not public.is_household_member(p_household) then
    raise exception 'Not a member of this household' using errcode = '42501';
  end if;
  return query select s.plan_key, s.status, s.current_period_end from public.subscriptions s
    where s.household_id = p_household and s.environment = 'production'
    order by s.current_period_end desc nulls last, s.created_at desc;
end $$;
