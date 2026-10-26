import io, os, sys, tempfile, unittest
from contextlib import redirect_stdout
from unittest import mock
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import apply_migrations as a


class ApplyMigrationTests(unittest.TestCase):
    def write(self, text):
        d = Path(tempfile.mkdtemp()); p = d / '20990101000000_x.sql'; p.write_text(text); return p

    def test_one_transaction_records_whole_file(self):
        sql = a.transaction_sql(self.write('create table t(id int);\r\n'), '20990101000000', 'x')
        self.assertTrue(sql.startswith('begin;\n\\i '))
        self.assertTrue(sql.rstrip().endswith('commit;'))
        self.assertIn("values ('20990101000000', 'x', array[$m", sql)
        self.assertIn('create table t(id int);\n', sql)
        self.assertNotIn('\r', sql)

    def test_dollar_tag_never_collides_with_content(self):
        sql = a.transaction_sql(self.write("select $m$ text $m$;"), '20990101000000', 'x')
        tag = sql.split('array[')[1].split('$')[1]
        self.assertNotIn(f'${tag}$', "select $m$ text $m$;")

    def test_files_with_own_transaction_control_are_refused(self):
        for text in ('begin;\nselect 1;\ncommit;', 'select 1;\n  COMMIT ;'):
            with self.assertRaises(ValueError):
                a.transaction_sql(self.write(text), '20990101000000', 'x')

    def test_repository_migrations_are_applicable(self):
        for p in sorted(a.h.MIGRATIONS.glob('*.sql')):
            a.transaction_sql(p, p.name[:14], p.stem[15:])


class UntilTests(unittest.TestCase):
    """--until VERSION: apply pending files up to and including VERSION, then stop; refuse unknown versions."""
    LOCAL = {
        '20261022030000': {'file': '20261022030000_a.sql', 'name': 'a'},
        '20261022040000': {'file': '20261022040000_b.sql', 'name': 'b'},
        '20261022050000': {'file': '20261022050000_c.sql', 'name': 'c'},
        '20261023010000': {'file': '20261023010000_d.sql', 'name': 'd'},
    }
    PENDING = ['20261022030000_a.sql', '20261022040000_b.sql', '20261022050000_c.sql', '20261023010000_d.sql']

    def test_select_until_stops_after_the_version(self):
        self.assertEqual(a.select_until(self.PENDING, self.LOCAL, '20261022040000'), self.PENDING[:2])
        self.assertEqual(a.select_until(self.PENDING, self.LOCAL, '20261023010000'), self.PENDING)
        self.assertEqual(a.select_until(self.PENDING, self.LOCAL, None), self.PENDING)
        # A version that is already live leaves nothing to apply.
        self.assertEqual(a.select_until(self.PENDING[2:], self.LOCAL, '20261022040000'), [])

    def test_check_until_refuses_unknown_and_malformed_versions(self):
        self.assertEqual(a.check_until(None, self.LOCAL), [])
        self.assertEqual(a.check_until('20261022040000', self.LOCAL), [])
        self.assertIn('no repository migration', a.check_until('20261022045000', self.LOCAL)[0])
        for bad in ('2026102204', '20261022040000_b', 'latest', ''):
            self.assertIn('not a 14-digit', a.check_until(bad, self.LOCAL)[0])

    fail_psql = False

    @staticmethod
    def reserve_marker(sql):
        return "/reserve.sql'" in sql  # the test reserve files are all named reserve.sql

    def reserve_file(self, text=None):
        import make_reserve_migration as r
        d = Path(tempfile.mkdtemp()); p = d / 'reserve.sql'
        p.write_text(text if text is not None else r.reserve_sql('sat_digital_2024', [('30000000-0000-0000-0000-000000000001', 'math')]))
        return p

    def run_main(self, argv, live_pending):
        """main() against the real repository files, with the live database and psql replaced by fakes."""
        local, _ = a.h.local_migrations()
        pending = [v['file'] for k, v in sorted(local.items()) if k in live_pending]
        calls, state = [], {'pending': list(pending)}

        def fake_live_errors(_local, _rows):
            return [], list(state['pending'])

        def fake_run(cmd, *args, **kw):
            sql = Path(cmd[-1]).read_text()
            ran = [f for f in list(state['pending']) if f in sql]
            calls.append(tuple(ran) if self.reserve_marker(sql) else ran[0])
            if self.fail_psql:
                return mock.Mock(returncode=3)
            for f in ran:
                state['pending'].remove(f)
            return mock.Mock(returncode=0)

        out = io.StringIO()
        with mock.patch.object(a.h, 'live_rows', return_value=[]) as rows, \
             mock.patch.object(a.h, 'live_errors', side_effect=fake_live_errors), \
             mock.patch.object(a.h, 'offline_errors', return_value=[]), \
             mock.patch.object(a, 'require_live_writes') as guard, \
             mock.patch.object(a.subprocess, 'run', side_effect=fake_run), \
             mock.patch.dict(os.environ, {'DATABASE_URL': 'postgres://fake/never-used'}), redirect_stdout(out):
            code = a.main(argv)
        return code, out.getvalue(), calls, guard, rows

    def test_dry_run_with_until_lists_only_files_up_to_the_version(self):
        code, out, calls, guard, _ = self.run_main(['--dry-run', '--until', '20261022040000'],
                                                   {'20261022040000', '20261022050000', '20261023010000'})
        self.assertEqual(code, 0)
        self.assertIn('pending 20261022040000_cost_components_and_arrangements.sql', out)
        self.assertNotIn('pending 20261022050000', out)
        self.assertIn('not applied (after --until): 20261022050000_assessment_pool.sql', out)
        self.assertIn('not applied (after --until): 20261023010000_benchmark_item_assignment.sql', out)
        self.assertEqual(calls, [])
        guard.assert_not_called()

    def test_apply_with_until_runs_files_up_to_the_version_then_stops(self):
        code, out, calls, guard, _ = self.run_main(['--until', '20261022040000'],
                                                   {'20261022030000', '20261022040000', '20261022050000', '20261023010000'})
        self.assertEqual(code, 0, out)
        self.assertEqual(calls, ['20261022030000_question_rights_gate.sql', '20261022040000_cost_components_and_arrangements.sql'])
        self.assertIn('Live history matches the repository up to 20261022040000', out)
        guard.assert_called_once()

    def test_apply_without_until_runs_every_pending_file(self):
        code, out, calls, _, _ = self.run_main([], {'20261022030000', '20261022040000'})
        self.assertEqual(code, 0, out)
        self.assertEqual([c[:14] for c in calls], ['20261022030000', '20261022040000'])

    def test_pool_migration_is_refused_without_a_reserve(self):
        # A push-triggered run (no --until, no --reserve) must never apply the pool, nor anything before it.
        for argv in ([], ['--dry-run'], ['--until', '20261023010000']):
            code, out, calls, _, _ = self.run_main(argv, {'20261022040000', '20261022050000', '20261023010000'})
            self.assertEqual(code, 1, out)
            self.assertIn('applies only with --reserve', out)
            self.assertEqual(calls, [])

    def test_reserve_runs_in_one_transaction_with_the_selected_migrations(self):
        res = self.reserve_file()
        code, out, calls, guard, _ = self.run_main(['--until', '20261023010000', '--reserve', str(res)],
                                                   {'20261022050000', '20261023010000'})
        self.assertEqual(code, 0, out)
        self.assertEqual(calls, [('20261022050000_assessment_pool.sql', '20261023010000_benchmark_item_assignment.sql')])
        guard.assert_called_once()
        self.assertIn('applied reserve', out)

    def test_combined_sql_is_one_transaction_ending_with_the_reserve(self):
        res = self.reserve_file()
        m = a.h.MIGRATIONS
        sql = a.combined_transaction_sql([(m / '20261022050000_assessment_pool.sql', '20261022050000', 'assessment_pool'),
                                          (m / '20261023010000_benchmark_item_assignment.sql', '20261023010000', 'benchmark_item_assignment')], res)
        self.assertEqual(sql.count('begin;\n'), 1); self.assertTrue(sql.endswith(f"\\i '{res.resolve().as_posix()}'\ncommit;\n"))
        self.assertLess(sql.index('20261022050000'), sql.index('20261023010000'))
        self.assertEqual(sql.count('insert into supabase_migrations.schema_migrations'), 2)
        import hashlib
        self.assertIn(f"set_config('collegeprep.reserve_file_sha256', '{hashlib.sha256(res.read_bytes()).hexdigest()}', true)", sql)

    def test_failed_reserve_transaction_reports_nothing_applied(self):
        res = self.reserve_file()
        self.fail_psql = True
        code, out, calls, _, _ = self.run_main(['--reserve', str(res)], {'20261022050000', '20261023010000'})
        self.assertEqual(code, 1)
        self.assertIn('rolled back: no migration was applied and nothing was marked', out)

    def test_dry_run_with_reserve_is_a_rollback_rehearsal(self):
        res = self.reserve_file()
        seen = []
        real = a.combined_transaction_sql
        with mock.patch.object(a, 'combined_transaction_sql', side_effect=lambda *x, **k: seen.append(real(*x, **k)) or seen[-1]):
            code, out, calls, guard, _ = self.run_main(['--dry-run', '--until', '20261023010000', '--reserve', str(res)],
                                                       {'20261022050000', '20261023010000'})
        self.assertEqual(code, 0, out)
        self.assertIn('Rehearsal passed (rolled back', out)
        self.assertTrue(seen[0].endswith('rollback;\n')); self.assertNotIn('commit;', seen[0])
        self.assertEqual(len(calls), 1); guard.assert_called_once()  # it touches the live database, so the hold applies
        self.fail_psql = True
        code, out, _, _, _ = self.run_main(['--dry-run', '--reserve', str(res)], {'20261022050000', '20261023010000'})
        self.assertEqual(code, 1); self.assertIn('Rehearsal FAILED', out)

    def test_bad_reserve_scripts_are_refused_before_database_work(self):
        inside = a.h.MIGRATIONS / '20991231000000_not_written.sql'
        good = self.reserve_file().read_text()
        marker_line = good.split('\n', 1)[0] + '\n'
        for path, msg in ((self.reserve_file('select 1;\n'), 'not a reserve script'),
                          (self.reserve_file(good + 'commit;\n'), 'transaction control'),
                          # the review repro: COMMIT WORK right after the marker would leave the pool applied
                          (self.reserve_file(marker_line + 'commit work;\n' + good.split('\n', 1)[1]), 'transaction control'),
                          (self.reserve_file(good.replace('do $reserve$', 'END TRANSACTION;\ndo $reserve$')), 'transaction control'),
                          (self.reserve_file(good.replace('do $reserve$', "\\! echo hi\ndo $reserve$")), 'meta-command'),
                          (self.reserve_file(good.replace("set pool = 'assessment'", "set pool = 'assessment', status = 'draft'")), 'differs from what the generator writes'),
                          (self.reserve_file(good.replace('-000000000001', '-000000000002', 1)), 'differs from what the generator writes'),
                          (inside, 'must not live under supabase/migrations'),
                          (Path(tempfile.mkdtemp()) / 'missing.sql', 'No such file')):
            code, out, calls, guard, rows = self.run_main(['--reserve', str(path)], {'20261022050000', '20261023010000'})
            self.assertEqual(code, 1); self.assertIn(msg, out)
            self.assertEqual(calls, []); guard.assert_not_called(); rows.assert_not_called()

    def test_reserve_needs_the_assignment_migration(self):
        res = self.reserve_file()
        code, out, calls, _, _ = self.run_main(['--until', '20261022050000', '--reserve', str(res)], {'20261022050000', '20261023010000'})
        self.assertEqual(code, 1); self.assertIn('needs 20261023010000', out); self.assertEqual(calls, [])

    def test_reserve_alone_after_the_schema_is_live(self):
        res = self.reserve_file()
        code, out, calls, _, _ = self.run_main(['--reserve', str(res)], set())
        self.assertEqual(code, 0, out); self.assertEqual(calls, [()])

    def test_unknown_until_is_refused_before_any_database_work(self):
        code, out, calls, guard, rows = self.run_main(['--until', '20261022045000'], {'20261022040000', '20261022050000'})
        self.assertEqual(code, 1)
        self.assertIn('no repository migration has that version', out)
        self.assertEqual(calls, [])
        guard.assert_not_called(); rows.assert_not_called()

    def test_until_already_applied_applies_nothing(self):
        code, out, calls, _, _ = self.run_main(['--until', '20261022040000'], {'20261022050000', '20261023010000'})
        self.assertEqual(code, 0)
        self.assertIn('No pending migrations up to 20261022040000', out)
        self.assertEqual(calls, [])


if __name__ == '__main__':
    unittest.main()
