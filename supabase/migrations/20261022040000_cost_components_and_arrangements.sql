-- #218 C3: printed cost components and living arrangements reach the database as printed.
--
-- institution_costs.components            jsonb object: the record's printed lines by key (e.g. UTC's
--                                         "enrollment_fees_in_state", one printed "Enrollment Fees" line that combines
--                                         tuition and mandatory fees), copied verbatim; never summed or split here.
-- institution_costs.living_arrangements   jsonb array: one object per printed arrangement (arrangement, totals and
--                                         lines, source), copied verbatim.
-- Both are served by compare_institutions, which returns every institution_costs column. Null when the record has none.
-- No dedicated "combined tuition and fees" column: a numeric column would invite summing or splitting printed lines.

alter table public.institution_costs
  add column components jsonb check (components is null or jsonb_typeof(components) = 'object'),
  add column living_arrangements jsonb check (living_arrangements is null or jsonb_typeof(living_arrangements) = 'array');
comment on column public.institution_costs.components is
  '#218 C3: printed cost lines by key, verbatim from the reviewed record (scripts/import_supabase.py).';
comment on column public.institution_costs.living_arrangements is
  '#218 C3: printed living arrangements (with family, off campus, on campus) and their lines, verbatim from the record.';

-- The provenance view froze its column list at creation; append the two new columns (existing columns keep their order).
create or replace view public.institution_costs_with_provenance with (security_invoker=true) as
select c.id, c.institution_id, c.academic_year, c.residency, c.tuition, c.mandatory_fees, c.room, c.board, c.books_supplies,
  c.transportation, c.personal_misc, c.total_cost_of_attendance, c.currency, c.source_id, c.verification_status,
  c.last_verified_at, c.notes, c.student_population, c.on_campus_food_housing, c.on_campus_other_expenses,
  s.canonical_url as source_url, c.components, c.living_arrangements
from public.institution_costs c join public.sources s on s.id = c.source_id;
