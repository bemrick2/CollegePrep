-- Separate test/live customers. Production entitlement authorization remains unchanged.
alter table public.billing_customers add column environment text not null default 'production'
  check (environment in ('production','sandbox'));
alter table public.billing_customers drop constraint billing_customers_pkey;
alter table public.billing_customers add primary key (household_id, provider, environment);

-- Display-only staging billing status. Never use this RPC to authorize production Prep access.
-- Membership and billing-detail privacy checks match the production RPC.
create function public.household_sandbox_billing_status(p_household uuid) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare
  v public.subscriptions;
  v_billing boolean;
begin
  if not public.is_household_member(p_household) then
    raise exception 'Not a member of this household' using errcode = '42501';
  end if;
  select * into v from public.subscriptions s
   where s.household_id = p_household and s.environment = 'sandbox'
   order by case when s.status in ('active','trialing') then 0
                 when s.status in ('past_due','grace','billing_retry') then 1 else 2 end,
            s.current_period_end desc nulls last, s.created_at desc
   limit 1;
  v_billing := v.owner_user_id = auth.uid() or public.has_household_permission(p_household, 'manage_billing');
  if v.id is null then
    return jsonb_build_object('active', false, 'status', null, 'can_manage_billing',
      public.has_household_permission(p_household, 'manage_billing'));
  end if;
  return jsonb_build_object(
    'active', v.status in ('active','trialing','past_due','grace','billing_retry'),
    'in_grace', v.status in ('past_due','grace','billing_retry'),
    'plan_key', v.plan_key,
    'status', v.status,
    'current_period_end', v.current_period_end,
    'cancel_at_period_end', v.cancel_at_period_end,
    'can_manage_billing', v_billing,
    'managed_by', case when v_billing then case v.provider when 'stripe' then 'web' else v.provider end end,
    'is_owner', v.owner_user_id = auth.uid());
end $$;

revoke all on function public.household_sandbox_billing_status(uuid) from public, anon;
grant execute on function public.household_sandbox_billing_status(uuid) to authenticated, service_role;
