-- Statewide dual enrollment / dual credit policies (e.g. Kentucky CPE "Dual Credit Policy for Kentucky")
-- are state-level rules distinct from articulation and residency. Additive: widens the allowed kinds.
alter table public.state_policies drop constraint state_policies_policy_kind_check;
alter table public.state_policies add constraint state_policies_policy_kind_check
  check (policy_kind in ('tuition_residency','statewide_articulation','transfer_pathway',
    'transfer_guarantee','dual_admission','dual_enrollment','other'));
