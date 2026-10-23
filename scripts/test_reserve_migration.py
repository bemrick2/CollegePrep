"""Emit a rollback-only PostgreSQL test of generated CR-23 reserve migrations (scripts/make_reserve_migration.py).

Run after every repository migration, from the repository root:
  python scripts/test_reserve_migration.py | psql -v ON_ERROR_STOP=1
A migration generated for qualifying fixture items marks exactly those items; one listing any unqualified item (not
human-reviewed, practice-seen, unpublished, stale review, wrong section or exam, unknown) raises and marks nothing.
Fixture ids only: no real reserve list is generated or stored.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.make_reserve_migration import migration_sql

Q = lambda n: f'30000000-0000-0000-0000-00000000000{n}'
SAT = 'sat_digital_2024'
OK = [(Q(1), 'math'), (Q(2), 'math'), (Q(8), 'math')]
BAD = [  # (label, exam version, items, expected message)
    ('not human-reviewed', SAT, OK + [(Q(3), 'reading')], '%' + Q(3) + ' was not approved by a human review%'),
    ('practice-seen', SAT, OK + [(Q(4), 'math')], '%' + Q(4) + ' has been attempted by a student%'),
    ('planned into a session', SAT, OK + [(Q(7), 'reading')], '%' + Q(7) + ' was planned into a practice session%'),
    ('unpublished', SAT, OK + [(Q(5), 'math')], '%' + Q(5) + ' is not published%'),
    ('stale review', SAT, OK + [(Q(6), 'math')], '%' + Q(6) + ' has no current approved review%'),
    ('wrong section', SAT, [(Q(1), 'reading')] + OK[1:], '%' + Q(1) + ' is in section math, not reading%'),
    ('wrong exam version', 'act_enhanced_2025', OK, '%belongs to exam version sat_digital_2024%'),
    ('unknown exam version', 'sat_2016', OK, '%unknown exam version sat_2016%'),
    ('unknown id', SAT, OK + [('3fffffff-0000-0000-0000-000000000000', 'math')], '%3fffffff-0000-0000-0000-000000000000 does not exist%'),
]


def dq(text, tag='gen'):
    assert f'${tag}$' not in text
    return f'${tag}${text}${tag}$'


def integration_sql():
    out = [r'\set QUIET on', r'\o /dev/null', 'begin;', r'\i supabase/tests/support/test_helpers.sql', '''
do $$
declare hh uuid; st uuid;
begin
  -- Human approvals for q1 q2 q4 q6 q7 q8 (authored items); q3 keeps its non-human 'test fixture' approval; q5 is a draft.
  perform public.approve_practice_question(('30000000-0000-0000-0000-00000000000' || n)::uuid, 'human: content lead (fixture)')
  from unnest(array['1','2','4','6','7','8']) n;
  -- q6's content changes after approval: its review is no longer current.
  update public.practice_questions set stem = 'Question 6, revised' where id = '30000000-0000-0000-0000-000000000006';
  -- Student 51 practises q4 and has q7 planned into a practice session (q4 is practice-seen).
  perform hp_test.as_user('20000000-0000-0000-0000-0000000000a1');
  hh := public.create_household('Reserve', 'America/Chicago');
  st := public.add_student(hh, 'Reserve Student');
  perform set_config('t.inv', public.create_household_invitation(hh, 'student', st), true);
  perform hp_test.as_user('20000000-0000-0000-0000-000000000051');
  perform public.accept_household_invitation(current_setting('t.inv'));
  perform public.submit_practice_attempt(public.start_practice_attempt(st, '30000000-0000-0000-0000-000000000004'), 'A');
  perform hp_test.as_owner();
  insert into public.practice_sessions(id, student_id, target_minutes) values ('3a000000-0000-0000-0000-000000000001', st, 10);
  insert into public.practice_session_items(session_id, position, question_id, reason)
  values ('3a000000-0000-0000-0000-000000000001', 1, '30000000-0000-0000-0000-000000000007', 'review');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 0::bigint, 'no reserve before the migration');
end $$;''']
    for label, exam, items, like in BAD:
        out.append(f'''do $$ begin
  perform hp_test.expect_error({dq(migration_sql(exam, items))}, '23514', {dq(like, 'like')});
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 0::bigint, {dq('rolled back: ' + label, 'msg')});
end $$;''')
    out.append(migration_sql(SAT, OK))
    ids = ', '.join(f"'{q}'" for q, _ in OK)
    out.append(f'''do $$ begin
  perform hp_test.eq((select string_agg(id::text, ',' order by id) from public.practice_questions where pool = 'assessment'),
    {dq(','.join(q for q, _ in OK), 'want')}, 'a qualifying list marks exactly its items');
  perform hp_test.check((select bool_and(pool = 'assessment') from public.practice_questions where id in ({ids})), 'all listed items marked');
end $$;''')
    out += ['rollback;', r'\o', r'\echo reserve migration tests passed']
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    sys.stdout.write(integration_sql())
