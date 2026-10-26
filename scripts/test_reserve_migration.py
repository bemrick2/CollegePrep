"""Emit a rollback-only PostgreSQL test of generated CR-23 reserve scripts (scripts/make_reserve_migration.py).

A reserve script is not a migration: it is never stored under supabase/migrations/, and scripts/apply_migrations.py
--reserve runs it in one transaction with the schema migrations (that release path is tested end to end by
scripts/test_reserve_release.py). This test runs after every repository migration, from the repository root:
  python scripts/test_reserve_migration.py | psql -v ON_ERROR_STOP=1
A script generated for qualifying fixture items marks exactly those items; one listing any unqualified item (no named
human review, practice-seen, unpublished, stale review, wrong or unplanned section, wrong exam, unknown, or a passage
shared with another question) raises and marks nothing. Fixture ids only: no real reserve list is generated or stored.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.make_reserve_migration import reserve_sql

Q = lambda n: f'30000000-0000-0000-0000-00000000000{n}'
X = lambda n: f'3b000000-0000-0000-0000-0000000000{n}'  # extra fixture items created below
SAT = 'sat_digital_2024'
OK = [(Q(1), 'math'), (Q(2), 'math'), (Q(8), 'math')]
BAD = [  # (label, exam version, items, expected message)
    ('not human-reviewed', SAT, OK + [(Q(3), 'reading')], '%' + Q(3) + ' was not approved by a named human reviewer%'),
    ('practice-seen', SAT, OK + [(Q(4), 'math')], '%' + Q(4) + ' has been attempted by a student%'),
    ('planned into a session', SAT, OK + [(Q(7), 'reading')], '%' + Q(7) + ' was planned into a practice session%'),
    ('unpublished', SAT, OK + [(Q(5), 'math')], '%' + Q(5) + ' is not published%'),
    ('stale review', SAT, OK + [(Q(6), 'math')], '%' + Q(6) + ' has no current approved review%'),
    ('wrong section', SAT, [(Q(1), 'reading')] + OK[1:], '%' + Q(1) + ' is in section math, not reading%'),
    ('wrong exam version', 'act_enhanced_2025', OK, '%belongs to exam version sat_digital_2024%'),
    ('unknown exam version', 'sat_2016', OK, '%unknown exam version sat_2016%'),
    ('unknown id', SAT, OK + [('3fffffff-0000-0000-0000-000000000000', 'math')], '%3fffffff-0000-0000-0000-000000000000 does not exist%'),
    ("bare 'human:'", SAT, OK + [(X('a1'), 'math')], '%' + X('a1') + ' was not approved by a named human reviewer%'),
    ("uppercase 'HUMAN:'", SAT, OK + [(X('a2'), 'math')], '%' + X('a2') + ' was not approved by a named human reviewer%'),
    ('section without a plan', SAT, OK + [(X('a3'), 'writing')], '%' + X('a3') + ' is in section writing, which has no progress-check plan%'),
    ('passage shared with a practice item', SAT, OK + [(X('a4'), 'math')], '%' + X('a4') + ' shares its passage with a practice item%'),
    ('passage siblings listed together', SAT, OK + [(X('a6'), 'math'), (X('a7'), 'math')],
     '%' + X('a6') + ' shares its passage with another reserved or listed item; ' + X('a7') + ' shares its passage with another reserved or listed item%'),
    ('passage shared with a reserved item', SAT, OK + [(X('a8'), 'math')], '%' + X('a8') + ' shares its passage with another reserved or listed item%'),
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
  -- Extra items: a1 approved 'human:' (no reviewer named), a2 'HUMAN: Lead' (uppercase), a3 in an unplanned section;
  -- a4 shares passage P1 with a5 (a practice draft); a6 and a7 share passage P2; a8 shares P3 with a9 (already reserved).
  insert into public.practice_passages(id, exam_version_id, body) values
    ('3c000000-0000-0000-0000-000000000001', '40000000-0000-0000-0000-000000000001', 'Passage one'),
    ('3c000000-0000-0000-0000-000000000002', '40000000-0000-0000-0000-000000000001', 'Passage two'),
    ('3c000000-0000-0000-0000-000000000003', '40000000-0000-0000-0000-000000000001', 'Passage three');
  insert into public.practice_questions(id, exam_version_id, question_type_id, section, stem, choices, answer_format, accepted_answers,
    expected_time_seconds, status, license, origin, passage_id)
  select ('3b000000-0000-0000-0000-0000000000' || n)::uuid, '40000000-0000-0000-0000-000000000001', '41000000-0000-0000-0000-000000000001',
    sec, 'Extra ' || n, '["A","B"]', 'choice', '["A"]', 60, stat, 'original-owned', 'authored', pas::uuid
  from (values ('a1', 'math', 'published', null), ('a2', 'math', 'published', null), ('a3', 'writing', 'published', null),
    ('a4', 'math', 'published', '3c000000-0000-0000-0000-000000000001'), ('a5', 'math', 'draft', '3c000000-0000-0000-0000-000000000001'),
    ('a6', 'math', 'published', '3c000000-0000-0000-0000-000000000002'), ('a7', 'math', 'published', '3c000000-0000-0000-0000-000000000002'),
    ('a8', 'math', 'published', '3c000000-0000-0000-0000-000000000003'), ('a9', 'math', 'published', '3c000000-0000-0000-0000-000000000003')
  ) v(n, sec, stat, pas);
  perform public.approve_practice_question('3b000000-0000-0000-0000-0000000000a1', 'human:');
  perform public.approve_practice_question('3b000000-0000-0000-0000-0000000000a2', 'HUMAN: Lead');
  perform public.approve_practice_question(('3b000000-0000-0000-0000-0000000000' || n)::uuid, 'human: content lead (fixture)')
  from unnest(array['a3','a4','a6','a7','a8','a9']) n;
  update public.practice_questions set pool = 'assessment' where id = '3b000000-0000-0000-0000-0000000000a9';
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 1::bigint, 'only the fixture a9 reserved before the script');
end $$;''']
    for label, exam, items, like in BAD:
        out.append(f'''do $$ begin
  perform hp_test.expect_error({dq(reserve_sql(exam, items))}, '23514', {dq(like, 'like')});
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), 1::bigint, {dq('rolled back: ' + label, 'msg')});
end $$;''')
    out.append(reserve_sql(SAT, OK))
    ids = ', '.join(f"'{q}'" for q, _ in OK)
    out.append(f'''do $$ begin
  perform hp_test.eq((select string_agg(id::text, ',' order by id) from public.practice_questions where pool = 'assessment' and id::text like '30%'),
    {dq(','.join(q for q, _ in OK), 'want')}, 'a qualifying list marks exactly its items');
  perform hp_test.eq((select count(*) from public.practice_questions where pool = 'assessment'), {len(OK) + 1}::bigint, 'and nothing else');
  perform hp_test.check((select bool_and(pool = 'assessment') from public.practice_questions where id in ({ids})), 'all listed items marked');
end $$;''')
    out += ['rollback;', r'\o', r'\echo reserve migration tests passed']
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    sys.stdout.write(integration_sql())
