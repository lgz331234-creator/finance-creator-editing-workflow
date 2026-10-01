import os
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import local_workflow as local
import workflow_guard as guard


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)
        self.script = self.project / 'script.txt'
        self.script.write_text('First approved line.\n')
        self.owner = patch.dict(os.environ, {'CODEX_THREAD_ID': 'task-a'})
        self.owner.start()
        self.addCleanup(self.owner.stop)

    def prepare(self, task='task-a', takeover=False):
        args = SimpleNamespace(task_id=task, takeover=takeover,
                               script=str(self.script), topic=None)
        return local.prepare(args, self.project)

    def test_only_one_task_can_prepare_without_handoff(self):
        result, code = self.prepare()
        self.assertEqual(code, 0)
        self.assertEqual(result['active_task'], 'task-a')
        blocked, code = self.prepare('task-b')
        self.assertEqual((blocked['status'], code), ('ACTIVE_IN_ANOTHER_TASK', 2))
        transferred, code = self.prepare('task-b', takeover=True)
        self.assertEqual((transferred['active_task'], code), ('task-b', 0))
        with self.assertRaises(ValueError):
            local.finish(SimpleNamespace(task_id='task-a'), self.project)
        local.finish(SimpleNamespace(task_id='task-b'), self.project)
        self.assertNotIn('active_task', guard.read(self.project / '.finance-workflow/state.json'))

    def test_check_blocks_pending_and_changed_script(self):
        self.prepare()
        state = self.project / '.finance-workflow'
        review = guard.read(state / 'migration-review.json')
        review['approved_baseline'] = str(self.script)
        review['scope'] = 'Test project'
        for key, item in review['checks'].items():
            item['note'] = 'Checked in isolated test'
            if key in ('timeline_content', 'project_render_config'):
                item['status'] = 'checked'
                item['evidence'] = [{'file': str(self.script), 'sha256': guard.sha(self.script)}]
            else:
                item['status'] = 'not_applicable'
        guard.save(state / 'migration-review.json', review)
        blocked, code = guard.run('check', self.project, ROOT)
        self.assertEqual(code, 2)
        self.assertTrue(any('State card pending' in error for error in blocked['errors']))
        card = guard.read(state / 'state.json')
        for key in ('release_review', 'script_preflight', 'dependent_timing_review'):
            card[key] = 'checked'
        guard.save(state / 'state.json', card)
        ready, code = guard.run('check', self.project, ROOT)
        self.assertEqual((ready['status'], code), ('VERSION_AND_EVIDENCE_CURRENT', 0))
        self.script.write_text('Changed after approval.\n')
        blocked, code = guard.run('check', self.project, ROOT)
        self.assertEqual(code, 2)
        self.assertTrue(any('Script file is missing or changed' in error for error in blocked['errors']))


if __name__ == '__main__':
    unittest.main()
