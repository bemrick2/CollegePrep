-- Minimal stand-in for Supabase Auth so migrations and tests run on plain PostgreSQL.
-- Every object is created only when missing, so this is a no-op on a real Supabase project.
-- Tests impersonate a user with: select set_config('request.jwt.claim.sub', '<uuid>', true);
do $$ begin
  if to_regnamespace('auth') is null then
    create schema auth;
    grant usage on schema auth to anon, authenticated;
  end if;
  if to_regclass('auth.users') is null then
    create table auth.users (id uuid primary key);
  end if;
  if to_regprocedure('auth.uid()') is null then
    create function auth.uid() returns uuid language sql stable
      as $f$ select nullif(current_setting('request.jwt.claim.sub', true), '')::uuid $f$;
    grant execute on function auth.uid() to anon, authenticated;
  end if;
end $$;
