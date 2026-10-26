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
  -- Without an open check, reserved content is readable only for items this student has attempted (q6, practised earlier).
  perform hp_test.eq((select string_agg(right(id::text, 1), ',') from public.practice_questions where pool = 'assessment'), '6', 'reserved content hidden until a check');
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

-- Checks use only reserved items: listed unseen first (mid difficulty first), then repeats; practice items are refused.
do $$
declare st uuid := current_setting('t.st')::uuid; b uuid; got text; m jsonb; a uuid; n bigint;
begin
  perform hp_test.as_owner();
  -- q4 difficulty 1 and q8 difficulty 3: mid difficulty first among unseen math items (not id order).
  update public.practice_questions set difficulty = 1 where id = '30000000-0000-0000-0000-000000000004';
  update public.practice_questions set pool = 'assessment', difficulty = 3 where id = '30000000-0000-0000-0000-000000000008';
  -- A reserved draft never appears.
  update public.practice_questions set pool = 'assessment' where id = '30000000-0000-0000-0000-000000000005';
  -- An ACT reserved item (another exam version).
  insert into public.question_types(id, exam_version_id, type_key, name) values
    ('41000000-0000-0000-0000-000000000009', '40000000-0000-0000-0000-000000000002', 'multiple_choice', 'Multiple choice');
  insert into public.practice_questions(id, exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin, pool)
  values ('30000000-0000-0000-0000-000000000009', '40000000-0000-0000-0000-000000000002', '41000000-0000-0000-0000-000000000009', 'math', 'ACT item', '["A","B"]',
    'choice', '["A"]', 60, 'published', 'original-owned', 'authored', 'assessment');
  perform public.approve_practice_question('30000000-0000-0000-0000-000000000009', 'test fixture');

  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  -- A check needs an exam version.
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini')$q$, st), '22023', '%exam version%');
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', null)$q$, st), '22023', '%exam version%');
  -- The first check is an initial one (#263: a repeat needs a completed check first).
  b := public.start_benchmark(st, 'initial', '40000000-0000-0000-0000-000000000001');
  perform set_config('t.b', b::text, true);
  select string_agg(section || ':' || right(question_id::text, 1) || ':' || seen_before, ',' order by section, ord) into got
  from (select x.*, row_number() over () as ord from public.benchmark_questions(b) x) y;
  perform hp_test.eq(got, 'math:8:false,math:4:false,math:6:true,reading:7:false',
    'reserved, published, own-version items only: unseen (mid difficulty first) before repeats, with seen_before');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000001', b), '22023', '%reserved questions only%');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000009', b), '22023', '%own exam version%');
  -- Only the benchmark's own student lists its items.
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  -- Reserved content: hidden from an outsider and from a guardian whose student hasn't attempted it.
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 0::bigint, 'outsider sees no reserved item');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 0::bigint, 'a student without an open check sees none');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment' and exam_version_id = '40000000-0000-0000-0000-000000000001'),
    4::bigint, 'a student with an open check reads its version''s reserved items');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');

  -- The check takes q4 (fresh), q6 (a repeat) and skips q8 in math; q7 (fresh) in reading.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000004', p_benchmark => b);
  perform public.submit_practice_attempt(a, 'A');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000004', b), '22023', '%once per progress check%');
  perform hp_test.eq((select count(*) from public.benchmark_questions(b) where question_id = '30000000-0000-0000-0000-000000000004'), 0::bigint, 'used items leave the list');
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
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');  -- closed
  -- After the check, the student and a viewing guardian can still read the items attempted; not the unattempted one.
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 3::bigint, 'attempted reserved items stay readable to the student');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 3::bigint, 'and to a viewing guardian');

  -- A second check: a skipped repeat doesn't count; everything left is a repeat, least recently shown first.
  -- #263: q8 was assigned to the first check (never attempted), and assignment is exposure, so it is a repeat now.
  perform hp_test.as_owner();
  update public.practice_attempts set presented_at = presented_at - interval '2 days'
    where student_id = st and question_id = '30000000-0000-0000-0000-000000000006';
  update public.practice_benchmark_items set assigned_at = assigned_at - interval '2 days'
    where student_id = st and question_id = '30000000-0000-0000-0000-000000000006';
  -- #263: a repeat check opens 28 days after the last completed one; the first check was taken a month ago.
  update public.practice_benchmarks set started_at = started_at - interval '29 days', completed_at = completed_at - interval '29 days'
    where student_id = st and completed_at is not null;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  b := public.start_benchmark(st, 'mini', '40000000-0000-0000-0000-000000000001');
  select string_agg(right(question_id::text, 1) || ':' || seen_before, ',') into got from public.benchmark_questions(b) where section = 'math';
  perform hp_test.eq(got, '6:true,8:true,4:true', 'all repeats (q8 assigned before, unattempted), least recently shown first');
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000004', p_benchmark => b);
  perform public.submit_practice_attempt(a, null, p_skipped => true);
  a := public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000008', p_benchmark => b);
  perform public.submit_practice_attempt(a, 'B');
  -- A section with no reserved items isn't offered (and so isn't measured).
  perform hp_test.as_owner();
  update public.practice_questions set pool = 'practice' where id = '30000000-0000-0000-0000-000000000007';
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.benchmark_questions(b) where section = 'reading'), 0::bigint, 'no reserved reading items');
  m := public.complete_benchmark(b);
  perform hp_test.check(not (m->'by_section' ? 'reading'), 'unmeasured section absent');
  -- q4 (a skipped repeat) is not counted; q8 (answered) is, because the first check exposed it (#263).
  perform hp_test.eq((m->'by_section'->'math'->>'repeats')::int, 1, 'a skipped repeat is not counted; an assigned-before item is');
  perform hp_test.eq((m->>'comparable')::boolean, false, 'an item exposed by an earlier check makes the check not comparable');
  -- One more reserved SAT math item (qa) that student 51 hasn't been shown.
  perform hp_test.as_owner();
  insert into public.practice_questions(id, exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin, pool)
  values ('30000000-0000-0000-0000-00000000000a', '40000000-0000-0000-0000-000000000001', '41000000-0000-0000-0000-000000000001', 'math', 'Unseen reserved', '["A","B"]',
    'choice', '["A"]', 60, 'published', 'original-owned', 'authored', 'assessment');
  perform public.approve_practice_question('30000000-0000-0000-0000-00000000000a', 'test fixture');
  -- And a second reserved ACT item (qb) nobody attempts, to see what a check unlocks.
  insert into public.practice_questions(id, exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin, pool)
  values ('30000000-0000-0000-0000-00000000000b', '40000000-0000-0000-0000-000000000002', '41000000-0000-0000-0000-000000000009', 'math', 'ACT unseen', '["A","B"]',
    'choice', '["A"]', 60, 'published', 'original-owned', 'authored', 'assessment');
  perform public.approve_practice_question('30000000-0000-0000-0000-00000000000b', 'test fixture');

  -- assessment_pool_status: counts only, for viewers of the student.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  select string_agg(section || ':' || reserved || ':' || unseen, ',') into got
    from public.assessment_pool_status(st, '40000000-0000-0000-0000-000000000001');
  perform hp_test.eq(got, 'math:4:1', 'pool status: published, reviewed reserved items per section and how many are unseen (draft excluded)');
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  select string_agg(section || ':' || reserved || ':' || unseen, ',') into got
    from public.assessment_pool_status(st, '40000000-0000-0000-0000-000000000001');
  perform hp_test.eq(got, 'math:4:1', 'a viewing guardian gets the same counts');
  -- A guardian reads only the reserved items their student attempted, never the unseen one.
  perform hp_test.eq((select string_agg(right(id::text, 1), ',' order by id) from public.practice_questions
    where pool = 'assessment'), '4,6,8', 'guardian reads attempted reserved items only');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000052');
  perform hp_test.expect_error(format('select * from public.assessment_pool_status(%L, %L)', st, '40000000-0000-0000-0000-000000000001'), '42501');
  perform hp_test.as_user('20000000-0000-0000-0000-000000000099');
  perform hp_test.expect_error(format('select * from public.assessment_pool_status(%L, %L)', st, '40000000-0000-0000-0000-000000000001'), '42501');
  perform hp_test.as_anon();
  perform hp_test.expect_error(format('select * from public.assessment_pool_status(%L, %L)', st, '40000000-0000-0000-0000-000000000001'), '42501');

  -- A live check unlocks its own version only; a second start of the same version and kind resumes it.
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  b := public.start_benchmark(st, 'initial', '40000000-0000-0000-0000-000000000002');
  perform hp_test.eq(public.start_benchmark(st, 'initial', '40000000-0000-0000-0000-000000000002'), b, 'a live open check is resumed, not duplicated');
  perform hp_test.eq((select count(*) from public.practice_benchmarks where student_id = st and completed_at is null), 1::bigint, 'one open check');
  -- #263: the full-length form isn't ready, so the server has no 'full' plan and refuses it.
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'full', '40000000-0000-0000-0000-000000000002')$q$, st),
    '22023', '%not available%');
  -- #263: one live check per exam version; another kind is refused while it is open (never a second check).
  perform hp_test.expect_error(format($q$select public.start_benchmark(%L, 'mini', '40000000-0000-0000-0000-000000000002')$q$, st),
    '22023', '%already open%');
  perform hp_test.eq((select count(*) from public.practice_benchmarks where student_id = st and completed_at is null), 1::bigint, 'still one open check');
  perform hp_test.eq((select count(*) from public.practice_questions where id = '30000000-0000-0000-0000-000000000009'), 1::bigint, 'the ACT check reads ACT reserved items');
  -- #263: once something is answered in it, a live check is still resumed with its own assignment (only its unused
  -- items are listed, so the plan doesn't restart at full length); it is not replaced by a fresh draw.
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000009', p_benchmark => b), 'A');
  perform hp_test.eq(public.start_benchmark(st, 'initial', '40000000-0000-0000-0000-000000000002'), b, 'a half-taken live check is resumed');
  perform hp_test.eq((select count(*) from public.benchmark_questions(b) where question_id = '30000000-0000-0000-0000-000000000009'), 0::bigint,
    'the resumed check lists only its unused items');
  perform hp_test.eq((select count(*) from public.practice_questions where id = '30000000-0000-0000-0000-00000000000a'), 0::bigint,
    'an open check of another version unlocks nothing of this one');
  -- An abandoned check expires after 4 hours: no reserved content, no attempts, no list; a new start opens a new check.
  perform hp_test.as_owner();
  update public.practice_benchmarks set started_at = now() - interval '4 hours 1 minute'
    where student_id = st and exam_version_id = '40000000-0000-0000-0000-000000000002' and completed_at is null;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.practice_questions where id = '30000000-0000-0000-0000-00000000000b'), 0::bigint, 'an expired check unlocks nothing');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '22023', '%expired%');
  perform hp_test.expect_error(format('select public.start_practice_attempt(%L, %L, p_benchmark => %L)', st,
    '30000000-0000-0000-0000-000000000009', b), '22023', '%expired%');
  -- No ACT check was completed, so the next start is again an initial one.
  a := public.start_benchmark(st, 'initial', '40000000-0000-0000-0000-000000000002');
  perform hp_test.check(a <> b, 'an expired check is not resumed');
  perform hp_test.check((public.complete_benchmark(b)->>'definition') = 'v2', 'an expired check can still be completed (scores what was answered)');
  perform hp_test.as_owner();
  update public.practice_benchmarks set started_at = now() - interval '3 hours 59 minutes' where id = a;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.eq((select count(*) from public.practice_questions where id = '30000000-0000-0000-0000-00000000000b'), 1::bigint, 'still live just under 4 hours');
  -- Archived students can't use checks.
  perform hp_test.as_owner();
  update public.students set archived_at = now() where id = st;
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform hp_test.expect_error(format('select * from public.benchmark_questions(%L)', b), '42501');
  perform hp_test.as_owner();
  update public.students set archived_at = null where id = st;
  -- Clients can't move items between pools.
  perform hp_test.check(not has_column_privilege('authenticated', 'public.practice_questions', 'pool', 'UPDATE'), 'clients cannot change pool');
end $$;

rollback;
