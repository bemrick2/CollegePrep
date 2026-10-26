-- #263: a progress check is assigned its items once, at start, per section by the server's plan; it exposes only those,
-- accepts attempts only on those, and assignment counts as exposure. Rolled back. Run with psql -v ON_ERROR_STOP=1.
-- Probes P0, P1, P3 and P4 are #263's, on its fixture: every published SAT math item reserved (5), a mini check plans 4.
-- Also the owner's check contract (2026-10-26): resume the live check, one live check per exam version, server-side
-- kind rules (initial first, a repeat 28+ days after the last check started, completed or not; no full form), sizes from
-- the server plan, and benchmark_allowed_kinds (the same rules, read-only).
\set QUIET on
\o /dev/null
begin;
\ir support/test_helpers.sql
-- Moves all of a student's checks a month back (a repeat check opens 28 days after the last check started). A live
-- check moved back expires.
create function hp_test.age_checks(p_student uuid) returns void language sql as $f$
  update public.practice_benchmarks set started_at = started_at - interval '29 days', completed_at = completed_at - interval '29 days'
  where student_id = p_student
$f$;
-- For each kind start_benchmark would refuse per benchmark_allowed_kinds, it does refuse (22023): the two agree.
create function hp_test.kinds_agree(p_student uuid, p_version uuid) returns void language plpgsql as $f$
declare k text; v_allowed text[];
begin
  select allowed_kinds into v_allowed from public.benchmark_allowed_kinds(p_student, p_version);
  foreach k in array array['initial', 'mini', 'full'] loop
    if not k = any(v_allowed) then
      perform hp_test.expect_error(format('select public.start_benchmark(%L, %L, %L)', p_student, k, p_version), '22023');
    end if;
  end loop;
end $f$;
grant execute on function hp_test.kinds_agree(uuid, uuid) to authenticated;

-- Guardian a1 with student 51 (linked); guardian b1 with student 52 (another household); outsider 99.
do $$
declare hh uuid; st uuid; hh2 uuid; st2 uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Assign', 'America/Chicago');
  st := public.add_student(hh, 'Assign Student');
  perform set_config('t.st', st::text, true);
  perform set_config('t.inv', public.create_household_invitation(hh, 'student', st), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv'));
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  hh2 := public.create_household('Other', 'America/Chicago');
  st2 := public.add_student(hh2, 'Other Student');
  perform set_config('t.st2', st2::text, true);
  perform set_config('t.inv2', public.create_household_invitation(hh2, 'student', st2), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform public.accept_household_invitation(current_setting('t.inv2'));

  perform hp_test.as_owner();
  -- #263's fixture: every published SAT math item reserved (q1 q2 q4 q6 q8), plus reading q7. All difficulty 2.
  update public.practice_questions set pool = 'assessment' where section = 'math' and status = 'published';
  update public.practice_questions set pool = 'assessment' where id = '30000000-0000-0000-0000-000000000007';
  -- Two reserved ACT math items (another exam version).
  insert into public.question_types(id, exam_version_id, type_key, name) values
    ('41000000-0000-0000-0000-000000000009', '40000000-0000-0000-0000-000000000002', 'multiple_choice', 'Multiple choice');
  insert into public.practice_questions(id, exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin, pool)
  select v.id::uuid, '40000000-0000-0000-0000-000000000002', '41000000-0000-0000-0000-000000000009', 'math', 'ACT item', '["A","B"]',
    'choice', '["A"]', 60, 'published', 'original-owned', 'authored', 'assessment'
  from (values ('30000000-0000-0000-0000-000000000009'), ('30000000-0000-0000-0000-00000000000b')) v(id);
  perform public.approve_practice_question(v.id::uuid, 'test fixture')
  from (values ('30000000-0000-0000-0000-000000000009'), ('30000000-0000-0000-0000-00000000000b')) v(id);
  -- The plan is the server's and matches the app's PER_SECTION.
  perform hp_test.eq((select items from public.practice_benchmark_plan where exam_family = 'sat' and kind = 'mini' and section = 'math'), 4, 'SAT mini math plans 4');
  perform hp_test.eq((select items from public.practice_benchmark_plan where exam_family = 'act' and kind = 'initial' and section = 'math'), 8, 'ACT initial math plans 8');
  perform hp_test.eq((select count(*) from public.practice_benchmark_plan where not (exam_family = 'sat' and section = 'reading')), 12::bigint, 'seeded plan rows (fixture reading rows aside)');
  perform hp_test.eq((select count(*) from public.practice_benchmark_plan where kind = 'full'), 0::bigint, 'no full plan: the full form is not ready');
  -- The kind rules live in one table.
  perform hp_test.eq((select string_agg(kind || ':' || available || ':' || needs_prior || ':' || needs_no_prior || ':' || min_days_after_prior, ',' order by kind)
    from public.practice_benchmark_kinds), 'full:false:true:false:28,initial:true:false:true:0,mini:true:true:false:28', 'kind rules');
  -- Student 51 completed an initial SAT check a month ago (on an earlier reserve: no items), so a mini check may open.
  insert into public.practice_benchmarks(student_id, kind, exam_version_id, started_at, completed_at)
  values (st, 'initial', '40000000-0000-0000-0000-000000000001', now() - interval '30 days', now() - interval '30 days');
end $$;

-- P0, P1, P3: a check exposes and accepts only its assigned items; only its own student reads them.
do $$
declare st uuid := current_setting('t.st')::uuid; b uuid; got text; n bigint; a uuid; q record; t timestamptz;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  -- P0: no check open, nothing attempted: no reserved stem is readable.
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 0::bigint, 'P0: no reserved stem without a check');

  b := public.start_benchmark(st, 'mini', '40000000-0000-0000-0000-000000000001');
  perform set_config('t.b1', b::text, true);
  -- P1: the check lists exactly the plan size (4 of 5 math), and only those stems are readable.
  select string_agg(section || ':' || right(question_id::text, 1) || ':' || seen_before, ',') into got from public.benchmark_questions(b);
  perform hp_test.eq(got, 'math:1:false,math:2:false,math:4:false,math:6:false,reading:7:false', 'P1: plan-sized assignment per section');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment' and section = 'math'), 4::bigint,
    'P1: 4 reserved math stems readable, not 5');
  perform hp_test.eq((select count(*) from public.practice_questions where id = '30000000-0000-0000-0000-000000000008'), 0::bigint,
    'P1: the unassigned item stays hidden during the check');
  perform hp_test.eq((select count(*) from public.practice_question_skills where question_id = '30000000-0000-0000-0000-000000000008'), 0::bigint,
    'P1: and so do its child rows');
  perform hp_test.eq((select count(*) from public.practice_question_skills where question_id = '30000000-0000-0000-0000-000000000001'), 2::bigint,
    'an assigned item''s child rows are readable');
  perform hp_test.eq((select count(*) from public.practice_questions where exam_version_id = '40000000-0000-0000-0000-000000000002'), 0::bigint,
    'no ACT reserved item is readable from a SAT check');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items where benchmark_id = b), 5::bigint, 'the student reads the assignment');
  perform hp_test.check((select items_assigned_at is not null from public.practice_benchmarks where id = b), 'assignment recorded');

  -- Resume: an untouched live check comes back as is, never re-assigned.
  select max(assigned_at) into t from public.practice_benchmark_items where benchmark_id = b;
  perform hp_test.eq(public.start_benchmark(st, 'mini', '40000000-0000-0000-0000-000000000001'), b, 'resume returns the same check');
  perform hp_test.eq(public.start_benchmark(st, 'mini', '40000000-0000-0000-0000-000000000001'), b, 'and again');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items where benchmark_id = b), 5::bigint, 'resume does not re-assign');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items i where i.student_id = st), 5::bigint, 'resume adds no exposure');
  perform hp_test.eq((select max(assigned_at) from public.practice_benchmark_items where benchmark_id = b), t, 'assignment unchanged');
  perform hp_test.eq((select count(*) from public.practice_benchmarks where student_id = st and completed_at is null), 1::bigint, 'one open check');
  -- Hidden columns stay hidden even for an assigned item during its check.
  perform hp_test.expect_error($q$select accepted_answers from public.practice_questions where id = '30000000-0000-0000-0000-000000000001'$q$, '42501');
  perform hp_test.expect_error($q$select teaching_explanation from public.practice_questions where id = '30000000-0000-0000-0000-000000000001'$q$, '42501');
  perform hp_test.expect_error($q$select review_method from public.practice_questions where id = '30000000-0000-0000-0000-000000000001'$q$, '42501');

  -- P3: the server takes the 5 assigned items (4 math, 1 reading) and nothing else.
  n := 0;
  for q in select x.question_id from public.benchmark_questions(b) x loop
    a := public.start_practice_attempt(st, q.question_id, p_benchmark => b);
    n := n + 1;
    if q.question_id <> '30000000-0000-0000-0000-000000000007' then perform public.submit_practice_attempt(a, 'B'); end if;
  end loop;
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000008', b), '22023', '%not part of this progress check%');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000001', b), '22023', '%once per progress check%');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000009', b), '22023', '%own exam version%');
  perform hp_test.eq((select count(*) from public.practice_attempts where benchmark_id = b), 5::bigint, 'P3: exactly the assigned items were accepted');
  perform hp_test.eq(n, 5::bigint, 'P3: every assigned item was accepted once');
  perform hp_test.eq((select count(*) from public.benchmark_questions(b)), 0::bigint, 'used items leave the list');
  -- After answers and after the refused RPC calls above (a retry), a restart resumes the same live check: same
  -- assignment, no new exposure, no fresh draw. A forged kind is refused and changes nothing.
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'huge', '40000000-0000-0000-0000-000000000001')$q$, st), '22023', '%kind%');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'MINI', '40000000-0000-0000-0000-000000000001')$q$, st), '22023', '%kind%');
  perform hp_test.eq(public.start_benchmark(st, 'mini', '40000000-0000-0000-0000-000000000001'), b, 'a half-taken live check is resumed');
  perform hp_test.eq((select count(*) from public.practice_benchmarks where student_id = st and completed_at is null), 1::bigint, 'restart opens no second check');
  -- One live check per exam version: another kind is refused while it is open.
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'initial', '40000000-0000-0000-0000-000000000001')$q$, st),
    '22023', '%mini progress check is already open%');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items i where i.student_id = st), 5::bigint, 'restart adds no exposure');
  perform hp_test.eq((select max(assigned_at) from public.practice_benchmark_items where benchmark_id = b), t, 'restart keeps the assignment');
  -- The full form isn't available on the server.
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'full', '40000000-0000-0000-0000-000000000001')$q$, st),
    '22023', '%not available%');
  -- Once the check is completed: no initial (a check was completed), no repeat inside the 28-day gap.
  perform public.complete_benchmark(b);
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'initial', '40000000-0000-0000-0000-000000000001')$q$, st),
    '22023', '%initial progress check is only for a student who has not started one%');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st),
    '22023', '%opens 28 days after the last one started%');
  perform hp_test.as_owner();
  update public.practice_benchmarks set started_at = started_at - interval '27 days', completed_at = completed_at - interval '27 days' where id = b;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st),
    '22023', '%opens 28 days%');  -- 27 days later: still inside the gap
  perform hp_test.as_owner();
  perform hp_test.age_checks(st);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  -- A month on, a repeat check opens, assigned anew.
  a := public.start_benchmark(st, 'mini', '40000000-0000-0000-0000-000000000001');
  perform hp_test.check(a <> b, 'a completed check is not resumed');
  perform set_config('t.b1b', a::text, true);
  select string_agg(right(question_id::text, 1) || ':' || seen_before, ',') into got from public.benchmark_questions(a) where section = 'math';
  perform hp_test.eq(got, '8:false,1:true,2:true,4:true', 'the new check: unseen q8 first, then repeats');
end $$;

-- Unauthorized: anon, another household, a guardian, the outsider; direct writes; internal functions.
do $$
declare st uuid := current_setting('t.st')::uuid; b uuid := current_setting('t.b1b')::uuid;
begin
  -- The guardian (view_progress) reads the assignment rows, but not the live check's content, and can't start or list.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items where benchmark_id = b), 5::bigint, 'a viewing guardian reads assignment rows');
  perform hp_test.eq((select count(*) from public.practice_questions where id = '30000000-0000-0000-0000-000000000008'), 0::bigint,
    'a guardian cannot read an unattempted assigned item of a live check');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st), '42501');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000008', b), '42501');
  -- Another household's student and guardian, and the outsider: no rows, no content, no calls.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items), 0::bigint, 'another student reads no assignment');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 0::bigint, 'another student reads no reserved stem');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st), '42501');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000008', b), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items), 0::bigint, 'another guardian reads no assignment');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 0::bigint, 'another guardian reads no reserved stem');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items), 0::bigint, 'outsider reads no assignment');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 0::bigint, 'outsider reads no reserved stem');
  perform hp_test.as_anon();
  perform hp_test.expect_error('select count(*) from public.practice_benchmark_items', '42501');
  perform hp_test.expect_error('select count(*) from public.practice_benchmark_plan', '42501');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st), '42501');
  perform hp_test.expect_error($q$select count(*) from public.practice_questions where pool = 'assessment'$q$, '42501');

  -- Direct writes, even by the check's own student: refused (only start_benchmark assigns).
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format($q$insert into public.practice_benchmark_items(benchmark_id, student_id, exam_version_id, question_id,
    section, position, seen_before) values (%L, %L, '40000000-0000-0000-0000-000000000001', '30000000-0000-0000-0000-000000000006', 'math', 9, false)$q$,
    b, st), '42501');
  perform hp_test.expect_error(format('update public.practice_benchmark_items set seen_before = false where benchmark_id = %L', b), '42501');
  perform hp_test.expect_error(format('delete from public.practice_benchmark_items where student_id = %L', st), '42501');
  perform hp_test.expect_error(format('update public.practice_benchmarks set items_assigned_at = null where id = %L', b), '42501');
  perform hp_test.expect_error($q$insert into public.practice_benchmark_plan values ('sat', 'mini', 'math', 50)$q$, '42501');
  perform hp_test.expect_error($q$update public.practice_benchmark_plan set items = 50$q$, '42501');
  perform hp_test.expect_error(format('select public.assign_benchmark_items_internal(%L)', b), '42501');
  perform hp_test.expect_error(format('select * from public.student_exposure_internal(%L)', st), '42501');
  perform hp_test.check(not has_table_privilege('authenticated', 'public.practice_benchmark_items', 'INSERT,UPDATE,DELETE,TRUNCATE'), 'no client write privilege on items');
  perform hp_test.check(not has_table_privilege('authenticated', 'public.practice_benchmark_plan', 'INSERT,UPDATE,DELETE,TRUNCATE'), 'no client write privilege on the plan');
  perform hp_test.check((select relrowsecurity from pg_class where oid = 'public.practice_benchmark_items'::regclass), 'items have RLS');
  perform hp_test.check((select relrowsecurity from pg_class where oid = 'public.practice_benchmark_plan'::regclass), 'plan has RLS');
  -- The student reads the plan (not secret).
  perform hp_test.eq((select items from public.practice_benchmark_plan where exam_family = 'act' and kind = 'mini' and section = 'english'), 3, 'plan readable');
end $$;

-- Concurrency: starts serialise per student (advisory lock held to commit), assignment happens once (compare-and-set),
-- and the keys refuse a second copy of an item or a position.
do $$
declare st uuid := current_setting('t.st')::uuid; b uuid := current_setting('t.b1b')::uuid; k bigint;
begin
  perform hp_test.as_owner();
  k := hashtextextended('practice_benchmark_start:' || st::text, 0);
  perform hp_test.check(exists (select 1 from pg_locks l where l.locktype = 'advisory' and l.pid = pg_backend_pid() and l.granted
      and l.mode = 'ExclusiveLock' and l.classid = ((k >> 32) & 4294967295)::oid and l.objid = (k & 4294967295)::oid and l.objsubid = 1),
    'start_benchmark holds a transaction advisory lock on the student');
  perform hp_test.expect_error(format('select public.assign_benchmark_items_internal(%L)', b), '22023', '%already has its items%');
  perform hp_test.expect_error(format($q$insert into public.practice_benchmark_items(benchmark_id, student_id, exam_version_id, question_id,
    section, position, seen_before) values (%L, %L, '40000000-0000-0000-0000-000000000001', '30000000-0000-0000-0000-000000000008', 'math', 9, false)$q$,
    b, st), '23505');
  perform hp_test.expect_error(format($q$insert into public.practice_benchmark_items(benchmark_id, student_id, exam_version_id, question_id,
    section, position, seen_before) values (%L, %L, '40000000-0000-0000-0000-000000000001', '30000000-0000-0000-0000-000000000006', 'math', 1, false)$q$,
    b, st), '23505');
  -- Cross-exam isolation in the keys: an ACT item can't be stored on a SAT check, nor a row under another student.
  perform hp_test.expect_error(format($q$insert into public.practice_benchmark_items(benchmark_id, student_id, exam_version_id, question_id,
    section, position, seen_before) values (%L, %L, '40000000-0000-0000-0000-000000000001', '30000000-0000-0000-0000-000000000009', 'math', 9, false)$q$,
    b, st), '23503');
  perform hp_test.expect_error(format($q$insert into public.practice_benchmark_items(benchmark_id, student_id, exam_version_id, question_id,
    section, position, seen_before) values (%L, %L, '40000000-0000-0000-0000-000000000002', '30000000-0000-0000-0000-000000000009', 'math', 9, false)$q$,
    b, st), '23503');
  perform hp_test.expect_error(format($q$insert into public.practice_benchmark_items(benchmark_id, student_id, exam_version_id, question_id,
    section, position, seen_before) values (%L, %L, '40000000-0000-0000-0000-000000000001', '30000000-0000-0000-0000-000000000006', 'math', 9, false)$q$,
    b, current_setting('t.st2')), '23503');
end $$;

-- P4, abandonment and expiry: assignment is exposure, attempted or not.
do $$
declare st uuid := current_setting('t.st')::uuid; b uuid := current_setting('t.b1b')::uuid; c uuid; got text; m jsonb; a uuid;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  -- The second check (q8 unseen, q1 q2 q4 repeats; reading q7, assigned but never answered in the first check, is seen).
  perform hp_test.eq((select seen_before from public.benchmark_questions(b) where question_id = '30000000-0000-0000-0000-000000000007'), true,
    'an assigned, unanswered item of an earlier check counts as seen');
  -- The student reads every stem it can and answers nothing; the check expires.
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment' and id = '30000000-0000-0000-0000-000000000008'), 1::bigint,
    'q8 readable while assigned to the live check');
  perform hp_test.as_owner();
  update public.practice_benchmarks set started_at = now() - interval '4 hours 1 minute' where id = b;
  update public.practice_benchmark_items set assigned_at = now() - interval '4 hours 1 minute' where benchmark_id = b;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.practice_questions where id = '30000000-0000-0000-0000-000000000008'), 0::bigint,
    'an expired check unlocks nothing, not even its own unattempted items');
  -- Drain repro: letting a mini expire doesn't reset the rules; the next repeat still waits 28 days from its start.
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st),
    '22023', '%opens 28 days%');
  perform hp_test.kinds_agree(st, '40000000-0000-0000-0000-000000000001');
  perform hp_test.as_owner();
  perform hp_test.age_checks(st);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  -- P4: the next check marks nothing unseen: q8 was only ever assigned to the expired check.
  c := public.start_benchmark(st, 'mini', '40000000-0000-0000-0000-000000000001');
  perform hp_test.check(c <> b, 'an expired check is not resumed');
  perform hp_test.eq((select count(*) from public.benchmark_questions(c) where not seen_before), 0::bigint, 'P4: no item is marked unseen');
  perform hp_test.eq((select seen_before from public.benchmark_questions(c) where question_id = '30000000-0000-0000-0000-000000000008'), true,
    'P4: the expired check''s unattempted item is seen');
  select string_agg(section || ':' || reserved || ':' || unseen, ',') into got from public.assessment_pool_status(st, '40000000-0000-0000-0000-000000000001');
  perform hp_test.eq(got, 'math:5:0,reading:1:0', 'pool status counts assigned items as seen');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  select string_agg(section || ':' || reserved || ':' || unseen, ',') into got from public.assessment_pool_status(st, '40000000-0000-0000-0000-000000000001');
  perform hp_test.eq(got, 'math:5:0,reading:1:0', 'and so for a viewing guardian');
  -- Answering q8 now is a repeat: the check is not comparable.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000008', p_benchmark => c);
  perform public.submit_practice_attempt(a, 'B');
  m := public.complete_benchmark(c);
  perform hp_test.eq((m->'by_section'->'math'->>'repeats')::int, 1, 'P4: an item only assigned before (never answered) is a repeat');
  perform hp_test.eq((m->>'comparable')::boolean, false, 'P4: and the check is not comparable');
  -- The expired check can still be completed; its unanswered items stay exposure.
  m := public.complete_benchmark(b);
  perform hp_test.eq((select count(*) from public.practice_benchmark_items where benchmark_id = b), 5::bigint, 'exposure rows outlive the check');
  -- After the checks close, only attempted items stay readable (q8 was attempted in c; q6 in the first check).
  perform hp_test.eq((select string_agg(right(id::text, 1), ',' order by id) from public.practice_questions where pool = 'assessment'),
    '1,2,4,6,7,8', 'attempted reserved items stay readable for review');
end $$;

-- An exam version with no reserve: nothing is allowed (reserve_available false) and a start is refused, rolling back,
-- so it doesn't burn the student's initial check. And the 28-day gap is 28 x 24 hours in UTC whatever the session
-- TimeZone, across the November DST change.
do $$
declare st uuid := current_setting('t.st')::uuid; v uuid := '40000000-0000-0000-0000-00000000000e'; got text; b uuid; tz text := current_setting('timezone');
begin
  perform hp_test.as_owner();
  insert into public.exam_versions(id, exam_family, version_key, name, effective_from, rules)
  values (v, 'act', 'act_empty_fixture', 'ACT with no reserve', '2025-04-01', '{"sections":[]}');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  select string_agg(coalesce(live_benchmark::text, '-') || '|' || allowed_kinds::text || '|' || reserve_available, ';') into got
    from public.benchmark_allowed_kinds(st, v);
  perform hp_test.eq(got, '-|{}|false', 'no reserve: nothing allowed, flagged');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'initial', %L)$q$, st, v), '22023', '%Not measured: no reserved questions for this exam%');
  perform hp_test.eq((select count(*) from public.practice_benchmarks where exam_version_id = v), 0::bigint, 'the refused start left no check');
  -- Once reserved items exist in a planned section, the initial check is still available.
  perform hp_test.as_owner();
  insert into public.question_types(id, exam_version_id, type_key, name) values
    ('41000000-0000-0000-0000-00000000000e', v, 'multiple_choice', 'Multiple choice');
  insert into public.practice_questions(id, exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin, pool)
  values ('30000000-0000-0000-0000-0000000000e1', v, '41000000-0000-0000-0000-00000000000e', 'math', 'E1', '["A","B"]', 'choice', '["A"]', 60,
    'published', 'original-owned', 'authored', 'assessment');
  perform public.approve_practice_question('30000000-0000-0000-0000-0000000000e1', 'test fixture');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select allowed_kinds from public.benchmark_allowed_kinds(st, v)), '{initial}'::text[], 'with a reserve, initial is allowed');
  -- A reserved item in an unplanned section doesn't count as a reserve.
  perform hp_test.as_owner();
  update public.practice_questions set section = 'writing' where id = '30000000-0000-0000-0000-0000000000e1';
  perform public.approve_practice_question('30000000-0000-0000-0000-0000000000e1', 'test fixture');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select reserve_available from public.benchmark_allowed_kinds(st, v)), false, 'an unplanned section is no reserve');
  -- UTC gap: a check started 2026-10-20 15:00 UTC; the next mini opens exactly 672 hours later, even in a Chicago session
  -- (DST ends 2026-11-01 there; local-calendar arithmetic would give 673 hours).
  perform hp_test.as_owner();
  update public.practice_questions set section = 'math' where id = '30000000-0000-0000-0000-0000000000e1';
  perform public.approve_practice_question('30000000-0000-0000-0000-0000000000e1', 'test fixture');
  insert into public.practice_benchmarks(student_id, kind, exam_version_id, started_at, completed_at, items_assigned_at)
  values (st, 'initial', v, '2026-10-20 15:00+00', '2026-10-20 16:00+00', '2026-10-20 15:00+00') returning id into b;
  perform set_config('timezone', 'America/Chicago', true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select extract(epoch from next_mini_at - '2026-10-20 15:00+00'::timestamptz) from public.benchmark_allowed_kinds(st, v)),
    (28 * 86400)::numeric, 'the gap is 28 x 24 hours across the DST change, in a Chicago session');
  perform hp_test.eq(public.benchmark_plus_days_utc('2026-10-20 15:00+00', 28), '2026-11-17 15:00+00'::timestamptz, 'UTC day arithmetic');
  perform set_config('timezone', tz, true);
  perform hp_test.as_owner();
  delete from public.practice_benchmarks where id = b;
end $$;

-- Student 52: kind rules from scratch, expiry of a partly answered check, cross-exam independence, a skipped repeat,
-- and legacy checks.
do $$
declare st2 uuid := current_setting('t.st2')::uuid; i uuid; m uuid; ms uuid; act uuid; act2 uuid; got text; r jsonb; t timestamptz;
begin
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  -- benchmark_allowed_kinds: for the student and viewing guardians only; a fresh student may open an initial check.
  select string_agg(coalesce(live_benchmark::text, '-') || '|' || allowed_kinds::text || '|' || coalesce(next_mini_at::text, '-'), ';') into got
    from public.benchmark_allowed_kinds(st2, '40000000-0000-0000-0000-000000000001');
  perform hp_test.eq(got, '-|{initial}|-', 'fresh: no live check, initial allowed, no mini date');
  perform hp_test.eq((select reserve_available from public.benchmark_allowed_kinds(st2, '40000000-0000-0000-0000-000000000001')), true, 'SAT has a reserve');
  perform hp_test.kinds_agree(st2, '40000000-0000-0000-0000-000000000001');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000b1');
  perform hp_test.eq((select allowed_kinds from public.benchmark_allowed_kinds(st2, '40000000-0000-0000-0000-000000000001')), '{initial}'::text[], 'a viewing guardian reads it');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error(format('select * from public.benchmark_allowed_kinds(%L, %L)', st2, '40000000-0000-0000-0000-000000000001'), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select * from public.benchmark_allowed_kinds(%L, %L)', st2, '40000000-0000-0000-0000-000000000001'), '42501');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format('select * from public.benchmark_allowed_kinds(%L, %L)', st2, '40000000-0000-0000-0000-000000000001'), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.expect_error(format('select * from public.benchmark_allowed_kinds(%L, null)', st2), '22023');
  -- No prior check: a repeat is refused, the full form is refused, an initial check opens.
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st2),
    '22023', '%comes after a first check%');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'full', '40000000-0000-0000-0000-000000000001')$q$, st2),
    '22023', '%not available%');
  i := public.start_benchmark(st2, 'initial', '40000000-0000-0000-0000-000000000001');
  perform hp_test.eq((select count(*) from public.benchmark_questions(i) where section = 'math'), 5::bigint, 'initial plans 9: the whole math reserve');
  perform hp_test.check((select live_benchmark = i and live_kind = 'initial' and allowed_kinds = '{initial}'
      and live_expires_at = b.started_at + interval '4 hours' and next_mini_at = b.started_at + interval '672 hours'
    from public.benchmark_allowed_kinds(st2, '40000000-0000-0000-0000-000000000001'), public.practice_benchmarks b where b.id = i),
    'live: the check, its expiry, only its kind (resume), and the next mini 28 days after it started');
  perform hp_test.kinds_agree(st2, '40000000-0000-0000-0000-000000000001');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items where student_id = st2 and benchmark_id = i and seen_before), 0::bigint,
    'another student''s exposure does not count');
  -- Reload with nothing answered, then with one answer: the same check and items, no new exposure.
  select max(assigned_at) into t from public.practice_benchmark_items where benchmark_id = i;
  perform hp_test.eq(public.start_benchmark(st2, 'initial', '40000000-0000-0000-0000-000000000001'), i, 'reload with 0 answers resumes');
  perform public.submit_practice_attempt(public.start_practice_attempt(st2, '30000000-0000-0000-0000-000000000001', p_benchmark => i), 'B');
  perform hp_test.eq(public.start_benchmark(st2, 'initial', '40000000-0000-0000-0000-000000000001'), i, 'reload with an answer resumes');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items where student_id = st2), 6::bigint, 'no new exposure (5 math + 1 reading)');
  perform hp_test.eq((select max(assigned_at) from public.practice_benchmark_items where benchmark_id = i), t, 'same assignment');
  perform hp_test.eq((select count(*) from public.benchmark_questions(i)), 5::bigint, 'the remaining unanswered items');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st2),
    '22023', '%initial progress check is already open%');
  -- The partly answered check expires: it is not resumed. It still counts as the student's first check: a second
  -- initial is refused (drain repro: abandoning and restarting never draws fresh initial sets), and a repeat opens 28
  -- days after the expired check started.
  perform hp_test.as_owner();
  update public.practice_benchmarks set started_at = now() - interval '4 hours 1 minute' where id = i;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'initial', '40000000-0000-0000-0000-000000000001')$q$, st2),
    '22023', '%initial progress check is only for a student who has not started one%');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'initial', '40000000-0000-0000-0000-000000000001')$q$, st2),
    '22023', '%initial progress check is only%');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st2),
    '22023', '%opens 28 days after the last one started%');
  perform hp_test.eq((select count(distinct question_id) from public.practice_benchmark_items where student_id = st2), 6::bigint,
    'drain repro: restarts expose nothing new');
  perform hp_test.check((select live_benchmark is null and allowed_kinds = '{}' and next_mini_at = b.started_at + interval '672 hours'
    from public.benchmark_allowed_kinds(st2, '40000000-0000-0000-0000-000000000001'), public.practice_benchmarks b where b.id = i),
    'after expiry: nothing allowed until the mini date');
  perform hp_test.kinds_agree(st2, '40000000-0000-0000-0000-000000000001');
  perform hp_test.as_owner();
  perform hp_test.age_checks(st2);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.eq((select allowed_kinds from public.benchmark_allowed_kinds(st2, '40000000-0000-0000-0000-000000000001')), '{mini}'::text[],
    'a month on, only a mini');
  perform hp_test.kinds_agree(st2, '40000000-0000-0000-0000-000000000001');
  m := public.start_benchmark(st2, 'mini', '40000000-0000-0000-0000-000000000001');
  perform hp_test.check(m <> i, 'an expired, partly answered check is not resumed');
  perform hp_test.eq((select count(*) from public.benchmark_questions(m) where not seen_before), 0::bigint,
    'the expired check''s assignment counts as seen');
  perform public.complete_benchmark(m);
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'initial', '40000000-0000-0000-0000-000000000001')$q$, st2),
    '22023', '%initial progress check is only%');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000001')$q$, st2),
    '22023', '%opens 28 days%');
  perform hp_test.as_owner();
  perform hp_test.age_checks(st2);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  -- Cross-exam: a live SAT check neither blocks nor resumes an ACT start, and the ACT check neither blocks nor resumes SAT.
  ms := public.start_benchmark(st2, 'mini', '40000000-0000-0000-0000-000000000001');
  act := public.start_benchmark(st2, 'initial', '40000000-0000-0000-0000-000000000002');
  perform hp_test.check(act <> ms, 'an ACT start opens its own check while a SAT check is live');
  perform hp_test.eq(public.start_benchmark(st2, 'mini', '40000000-0000-0000-0000-000000000001'), ms, 'the SAT check still resumes');
  perform hp_test.eq(public.start_benchmark(st2, 'initial', '40000000-0000-0000-0000-000000000002'), act, 'the ACT check resumes');
  select string_agg(right(question_id::text, 1) || ':' || seen_before, ',') into got from public.benchmark_questions(act);
  perform hp_test.eq(got, '9:false,b:false', 'an ACT check is assigned ACT items only');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items x join public.practice_questions q on q.id = x.question_id
    where x.benchmark_id = act and q.exam_version_id <> '40000000-0000-0000-0000-000000000002'), 0::bigint, 'no other-version item');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st2,
    '30000000-0000-0000-0000-000000000001', act), '22023', '%own exam version%');
  perform public.complete_benchmark(ms);
  perform hp_test.eq((select string_agg(right(id::text, 1), ',' order by id) from public.practice_questions
    where pool = 'assessment' and exam_version_id = '40000000-0000-0000-0000-000000000002'), '9,b', 'the live ACT check reads its ACT items');
  -- Answer q9; leave qb (assigned, unanswered); close the check.
  perform public.submit_practice_attempt(public.start_practice_attempt(st2, '30000000-0000-0000-0000-000000000009', p_benchmark => act), 'A');
  perform public.complete_benchmark(act);
  -- A skipped repeat is not counted: one new ACT item (qc); the next check has qc unseen and q9, qb as repeats.
  perform hp_test.as_owner();
  insert into public.practice_questions(id, exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin, pool)
  values ('30000000-0000-0000-0000-00000000000c', '40000000-0000-0000-0000-000000000002', '41000000-0000-0000-0000-000000000009', 'math',
    'ACT item c', '["A","B"]', 'choice', '["A"]', 60, 'published', 'original-owned', 'authored', 'assessment');
  perform public.approve_practice_question('30000000-0000-0000-0000-00000000000c', 'test fixture');
  perform hp_test.age_checks(st2);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  act2 := public.start_benchmark(st2, 'mini', '40000000-0000-0000-0000-000000000002');
  select string_agg(right(question_id::text, 1) || ':' || seen_before, ',') into got from public.benchmark_questions(act2);
  perform hp_test.eq(got, 'c:false,9:true,b:true', 'unseen qc first, then the repeats');
  -- Skip qb (a repeat, assigned but never answered before), answer qc (unseen), leave q9.
  perform public.submit_practice_attempt(public.start_practice_attempt(st2, '30000000-0000-0000-0000-00000000000b', p_benchmark => act2), null, p_skipped => true);
  perform public.submit_practice_attempt(public.start_practice_attempt(st2, '30000000-0000-0000-0000-00000000000c', p_benchmark => act2), 'A');
  r := public.complete_benchmark(act2);
  perform hp_test.eq((r->'by_section'->'math'->>'repeats')::int, 0, 'a check whose only repeat was skipped has no repeats');
  perform hp_test.eq((r->>'comparable')::boolean, true, 'and is comparable');
  -- A check opened before assignment existed lists and takes nothing, and is never resumed.
  perform hp_test.as_owner();
  perform hp_test.age_checks(st2);
  insert into public.practice_benchmarks(student_id, kind, exam_version_id) values (st2, 'mini', '40000000-0000-0000-0000-000000000002') returning id into i;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.eq((select count(*) from public.benchmark_questions(i)), 0::bigint, 'an unassigned (legacy) check lists nothing');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st2,
    '30000000-0000-0000-0000-000000000009', i), '22023', '%not part of this progress check%');
  act := public.start_benchmark(st2, 'mini', '40000000-0000-0000-0000-000000000002');
  perform hp_test.check(act <> i, 'an unassigned check is never resumed');
  perform hp_test.eq((select count(*) from public.practice_benchmark_items where benchmark_id = act), 3::bigint, 'a new check is assigned instead');
end $$;

rollback;
