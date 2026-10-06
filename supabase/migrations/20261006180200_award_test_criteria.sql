-- CR-11 (issue #37): numeric ACT/SAT criteria on institutional awards.
-- The importer reads these from the award's published test_requirement text (backend/test_criteria.py).
-- ACT and SAT are each read as published; one is never converted into the other. When both appear, each is
-- that exam's own published figure. A null kind means the text was not classified (read the criteria):
-- bare figures, footnoted or alternative paths ("or National Merit"), and anything ambiguous stay null.
-- compare_institutions serves the new columns through to_jsonb, with no function change.

alter table public.institutional_awards
  add column test_criteria_kind text
    check (test_criteria_kind in ('single_minimum', 'range', 'tiered', 'test_optional', 'none')),
  add column act_min integer check (act_min between 1 and 36),
  add column act_max integer check (act_max between 1 and 36),
  add column sat_min integer check (sat_min between 400 and 1600),
  add column sat_max integer check (sat_max between 400 and 1600),
  add constraint institutional_awards_test_criteria_shape check (
    (act_max is null or act_max > act_min) and (sat_max is null or sat_max > sat_min)
    and case test_criteria_kind
      when 'single_minimum' then act_max is null and sat_max is null and coalesce(act_min, sat_min) is not null
      when 'range' then (act_min is null or act_max is not null) and (sat_min is null or sat_max is not null)
        and coalesce(act_min, sat_min) is not null
      else coalesce(act_min, act_max, sat_min, sat_max) is null
    end is not false);

comment on column public.institutional_awards.test_criteria_kind is
  'How test_requirement states ACT/SAT criteria: single_minimum, range or test_optional; null when not classified (read the criteria).';
comment on column public.institutional_awards.act_min is 'Published ACT minimum (or range low end); never converted from SAT.';
comment on column public.institutional_awards.sat_min is 'Published SAT minimum (or range low end); never converted from ACT.';
