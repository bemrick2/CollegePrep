-- CR-23 reserved assessment pool (#218 B1): practice never uses reserved items, checks use only them, repeats are
-- reported. Rolled back. Run with psql -v ON_ERROR_STOP=1.
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql

-- Guardian a1 with student 51 (linked); student 52 is another household's student; outsider 99.
do $$
declare hh uuid; st uuid; hh2 uuid; st2 uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Pool', 'America/Chicago');
  st := public.add_student(hh, 'Pool Student');
  perform set_config('t.st', st::text, true);
  perform set_config('t.inv', public.create_household_invitation(hh, 'student', st), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  hh2 := public.create_household('Other', 'America/Chicago');
  st2 := public.add_student(hh2, 'Other Student');
  perform set_config('t.inv2', public.create_household_invitation(hh2, 'student', st2), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.accept_household_invitation(current_setting('t.inv2'));
  perform set_config('t.st2', st2::text, true);
  -- Before the pool exists for it, student 51 practises q6 (so q6 is a repeat once reserved).
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000006'), 'D');
  perform hp_test.as_owner();
  -- Reserve q4 and q6 (math) and q7 (reading). Every question defaults to the practice pool.
  perform hp_test.eq((select count(*) from public.practice_questions where pool <> 'practice'), 0::bigint, 'default pool is practice');
  update public.practice_questions set pool = 'assessment' where id in ('30000000-0000-0000-0000-000000000004',
    '30000000-0000-0000-0000-000000000006', '30000000-0000-0000-0000-000000000007');
  perform hp_test.expect_error($q$update public.practice_questions set pool = 'quiz' where id = '30000000-0000-0000-0000-000000000001'$q$, '23514');
end $$;

-- Practice never uses reserved items.
do $$
declare st uuid := current_setting('t.st')::uuid; ses uuid; n bigint;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 3::bigint, 'clients read pool');
  select count(*) into n from public.recommend_practice_set(st, 15) r
    join public.practice_questions q on q.id = r.question_id where q.pool = 'assessment';
  perform hp_test.eq(n, 0::bigint, 'recommender offers no reserved item');
  perform hp_test.check((select count(*) from public.recommend_practice_set(st, 15)) > 0, 'recommender still offers practice items');
  ses := public.start_practice_session(st, 15);
  select count(*) into n from public.practice_session_items i join public.practice_questions q on q.id = i.question_id
    where i.session_id = ses and q.pool = 'assessment';
  perform hp_test.eq(n, 0::bigint, 'a session holds no reserved item');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, %L)', st, '30000000-0000-0000-0000-000000000004', ses),
    '22023', '%not used in practice%');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L)', st, '30000000-0000-0000-0000-000000000007'),
    '22023', '%not used in practice%');
  perform public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000001', ses);  -- practice items still work
end $$;

-- Checks use only reserved items: listed unseen first, then repeats; practice items are refused.
do $$
declare st uuid := current_setting('t.st')::uuid; b uuid; got text; m jsonb; a uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  b := public.start_benchmark(st, 'mini', '40000000-0000-0000-0000-000000000001');
  perform set_config('t.b', b::text, true);
  select string_agg(section || ':' || right(question_id::text, 1) || ':' || seen_before, ',' order by section, ord) into got
  from (select x.*, row_number() over () as ord from public.benchmark_questions(b) x) y;
  perform hp_test.eq(got, 'math:4:false,math:6:true,reading:7:false', 'reserved items only, unseen before repeats, with seen_before');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000001', b), '22023', '%reserved questions only%');
  -- Only the benchmark's own student lists its items.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');

  -- The check takes q4 (fresh) and q6 (a repeat) in math, q7 (fresh) in reading.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000004', p_benchmark => b);
  perform public.submit_practice_attempt(a, 'A');
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000006', p_benchmark => b);
  perform public.submit_practice_attempt(a, 'D');
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000007', p_benchmark => b);
  perform public.submit_practice_attempt(a, 'A');
  m := public.complete_benchmark(b);
  perform hp_test.eq(m->>'definition', 'v2', 'metrics v2');
  perform hp_test.eq((m->'by_section'->'math'->>'repeats')::int, 1, 'math has one repeat');
  perform hp_test.eq((m->'by_section'->'math'->>'comparable')::boolean, false, 'a section with a repeat gets no verdict');
  perform hp_test.eq((m->'by_section'->'reading'->>'repeats')::int, 0, 'reading has none');
  perform hp_test.eq((m->'by_section'->'reading'->>'comparable')::boolean, true, 'a clean section is comparable');
  perform hp_test.eq((m->>'repeats')::int, 1, 'overall repeats');
  perform hp_test.eq((m->>'comparable')::boolean, false, 'overall not comparable');
  perform hp_test.check((select metrics = m from public.practice_benchmarks where id = b), 'stored as returned');
  -- A closed benchmark lists nothing.
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');

  -- A second check: q4 and q7 are now repeats too (shown in the first check), and come after nothing fresh.
  b := public.start_benchmark(st, 'mini', '40000000-0000-0000-0000-000000000001');
  select string_agg(right(question_id::text, 1) || ':' || seen_before, ',') into got from public.benchmark_questions(b) where section = 'math';
  perform hp_test.check(got in ('4:true,6:true', '6:true,4:true'), 'only repeats left: listed least recently shown first (' || got || ')');
  -- A section with no reserved items isn't offered (and so isn't measured).
  perform hp_test.as_owner();
  update public.practice_questions set pool = 'practice' where id = '30000000-0000-0000-0000-000000000007';
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.benchmark_questions(b) where section = 'reading'), 0::bigint, 'no reserved reading items');
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000004', p_benchmark => b);
  perform public.submit_practice_attempt(a, 'A');
  m := public.complete_benchmark(b);
  perform hp_test.check(not (m->'by_section' ? 'reading'), 'unmeasured section absent');
  perform hp_test.eq((m->'by_section'->'math'->>'repeats')::int, 1, 'a check repeat is a repeat');
  -- Clients can't move items between pools.
  perform hp_test.check(not has_column_privilege('public.practice_questions', 'pool', 'UPDATE'), 'clients cannot change pool');
  perform hp_test.as_owner();
end $$;

rollback;
