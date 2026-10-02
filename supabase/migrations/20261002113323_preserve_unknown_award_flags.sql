-- Missing full-tuition/full-ride claims are unknown, not verified negatives.
alter table public.institutional_awards alter column full_tuition drop not null,
  alter column full_tuition drop default,
  alter column full_ride drop not null,
  alter column full_ride drop default;
update public.institutional_awards a
set full_tuition=(r.payload->>'full_tuition')::boolean,
    full_ride=(r.payload->>'full_ride')::boolean
from ingestion.reference_records r,public.institutions i
where r.domain='awards' and i.institution_key=r.payload->>'institution_key'
  and a.institution_id=i.id and a.award_name=r.payload->>'award_name'
  and a.academic_year=r.payload->>'academic_year';
