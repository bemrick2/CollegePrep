-- CR-16: household subscription entitlement, fed by any payment source (Stripe on the web now, Apple IAP later).
-- Additive to public.subscriptions (initial household migration): wider normalised statuses, period/renewal
-- fields, a household -> Stripe customer map, an idempotent webhook event log, and one effective-entitlement RPC.
-- Writes come only from server-side payment handlers (service_role). Clients read through the RPC.

-- Normalised status across providers. Stripe: trialing active past_due canceled incomplete incomplete_expired
-- unpaid paused. Apple (later): grace billing_retry expired refunded revoked.
alter table public.subscriptions drop constraint subscriptions_status_check;
alter table public.subscriptions add constraint subscriptions_status_check check (status in (
  'trialing','active','past_due','canceled','incomplete','incomplete_expired','unpaid','paused',
  'grace','billing_retry','expired','refunded','revoked'));
alter table public.subscriptions add constraint subscriptions_provider_check
  check (provider in ('stripe','apple','google','comp')) not valid;

alter table public.subscriptions add column current_period_start timestamptz;
alter table public.subscriptions add column cancel_at_period_end boolean not null default false;
alter table public.subscriptions add column environment text not null default 'production'
  check (environment in ('production','sandbox'));
alter table public.subscriptions add column last_event_at timestamptz;
alter table public.subscriptions add column updated_at timestamptz not null default now();

-- One payment-provider customer per household and provider (Stripe customer created at first checkout).
create table public.billing_customers (
  household_id uuid not null references public.households(id) on delete cascade,
  provider text not null check (provider in ('stripe','apple','google')),
  provider_customer_id text not null,
  created_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  primary key (household_id, provider),
  unique (provider, provider_customer_id)
);

-- Every provider event exactly once (unique per provider event id), with its outcome, for replays and audit.
create table public.billing_events (
  id bigint generated always as identity primary key,
  provider text not null check (provider in ('stripe','apple','google')),
  event_id text not null,
  event_type text not null,
  household_id uuid,
  provider_subscription_id text,
  payload jsonb not null,
  received_at timestamptz not null default now(),
  processed_at timestamptz,
  error text,
  unique (provider, event_id)
);
create index billing_events_subscription_idx on public.billing_events(provider_subscription_id);

alter table public.billing_customers enable row level security;
alter table public.billing_events enable row level security;
revoke all on public.billing_customers, public.billing_events from public, anon, authenticated;
grant select, insert, update, delete on public.billing_customers, public.billing_events to service_role;

-- Effective entitlement for one household. Any member (guardian or linked student) may read whether the
-- household has access; billing details (who pays, where it is managed) only for the owner or a guardian
-- with manage_billing. Access statuses: active/trialing; past_due/grace/billing_retry keep access while the
-- provider retries payment. Provider identifiers never leave the server.
create function public.household_entitlement(p_household uuid) returns jsonb
language plpgsql stable security definer set search_path = '' as $$
declare
  v public.subscriptions;
  v_billing boolean;
begin
  if not public.is_household_member(p_household) then
    raise exception 'Not a member of this household' using errcode = '42501';
  end if;
  select * into v from public.subscriptions s
   where s.household_id = p_household and s.environment = 'production'
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

revoke all on function public.household_entitlement(uuid) from public, anon;
grant execute on function public.household_entitlement(uuid) to authenticated, service_role;
