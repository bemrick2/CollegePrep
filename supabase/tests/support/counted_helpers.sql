-- Counted assertions and a service-role identity, for tests that report how many assertions passed.
-- Include after support/test_helpers.sql, inside the test transaction.
create sequence hp_test.assertions;
create function hp_test.ok(p_ok boolean, p_msg text) returns void language plpgsql as $$
begin
  perform nextval('hp_test.assertions');
  perform hp_test.check(p_ok, p_msg);
end $$;
create function hp_test.is(p_got anycompatible, p_want anycompatible, p_msg text) returns void language plpgsql as $$
begin
  perform nextval('hp_test.assertions');
  perform hp_test.eq(p_got, p_want, p_msg);
end $$;
create function hp_test.err(p_sql text, p_state text, p_like text default null) returns void language plpgsql as $$
begin
  perform nextval('hp_test.assertions');
  perform hp_test.expect_error(p_sql, p_state, p_like);
end $$;
-- The scheduled senders' identity: the service role, with no user in the token.
create function hp_test.as_service() returns void language plpgsql as $$
begin
  perform set_config('role', 'service_role', true);
  perform set_config('request.jwt.claim.sub', '', true);
end $$;
-- Question n (1-8) of the synthetic bank in test_helpers.sql.
create function hp_test.q(p_n integer) returns uuid language sql immutable as $$
  select ('30000000-0000-0000-0000-00000000000' || p_n)::uuid
$$;
grant usage on schema hp_test to service_role;
grant usage on sequence hp_test.assertions to anon, authenticated, service_role;
grant execute on all functions in schema hp_test to anon, authenticated, service_role;
