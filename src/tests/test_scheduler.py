import asyncio
import time
import unittest
from datetime import datetime
from typing import List, NoReturn, Any

from base_database_test import BaseDatabaseTest
from storage.scheduler import Scheduler, Operation, Task, THandlerResult, TaskState, TaskFailed


class TestScheduler(BaseDatabaseTest):
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        self.tasks = Scheduler(self.db)
        await self.tasks.delete_all_tasks()

    async def asyncTearDown(self) -> None:
        del self.tasks
        await super().asyncTearDown()

    async def test_produce_consume(self) -> None:
        evidence: List[int] = []

        async def handler(x) -> THandlerResult:
            evidence.append(x)
            return None

        task = await self.run_test_task(handler, evidence, x=42)

        # Verify
        self.assertEqual(len(evidence), 1)
        self.assertEqual(evidence[0], 42)
        task = await self.tasks.get_task(task.id)
        await self.verify_task(task, x=42)

        # No tasks left
        pending1 = await self.tasks.list_pending_tasks(Operation.Test1)
        self.assertEqual(len(pending1), 0)
        pending2 = await self.tasks.list_pending_tasks(Operation.Test2)
        self.assertEqual(len(pending2), 0)

    async def verify_task(self, task: Task, **params):
        self.assertEqual(task.operation, Operation.Test1)
        self.assertEqual(task.state, TaskState.completed)
        self.assertEqual(task.params, params)
        self.assertIsNotNone(task.started)
        self.assertIsNotNone(task.finished)
        self.assertIsNone(task.message)
        print(f'Wait time: {task.wait_time.total_seconds() * 1000:.3f}ms')
        print(f'Runtime: {task.runtime.total_seconds() * 1000:.3f}ms')

    async def test_failed_handler(self) -> None:
        evidence: List[int] = []

        async def handler() -> NoReturn:
            evidence.append(1)
            raise TaskFailed('Test failure')

        task = await self.run_test_task(handler, evidence)

        self.assertEqual(len(evidence), 1)
        task = await self.tasks.get_task(task.id)
        self.assertEqual(task.state, TaskState.failed)
        self.assertTrue(bool(task.started))
        self.assertTrue(bool(task.finished))
        self.assertEqual(task.message, 'Test failure')

    async def test_crashed_handler(self) -> None:
        evidence: List[int] = []

        async def handler() -> NoReturn:
            evidence.append(1)
            raise Exception('Test crash')

        task = await self.run_test_task(handler, evidence)

        self.assertEqual(len(evidence), 1)
        task = await self.tasks.get_task(task.id)
        self.assertEqual(task.state, TaskState.crashed)
        self.assertTrue(bool(task.started))
        self.assertTrue(bool(task.finished))
        self.assertTrue('Exception: Test crash' in task.message)

    async def run_test_task(self, handler, evidence, **params) -> Task:
        async def schedule_task() -> Task:
            task = Task.create_pending(Operation.Test1, **params)
            before = datetime.utcnow()
            await self.tasks.schedule(task)
            after = datetime.utcnow()
            created = task.created
            self.assertTrue(before <= created, f'{before!r} <= {created!r}')
            self.assertTrue(created <= after, f'{created!r} <= {after!r}')
            return task

        listener = asyncio.create_task(self.tasks.listen(Operation.Test1, handler))
        try:
            task = await schedule_task()
            await self.wait_for_processing(evidence)
        finally:
            await asyncio.sleep(0.1)
            listener.cancel()

        return task

    async def wait_for_processing(self, evidence: List[Any], expected_count: int = 1, timeout: float = 1.0):
        deadline = time.time() + timeout
        while len(evidence) < expected_count and time.time() < deadline:
            await asyncio.sleep(0)
            if evidence:
                break


if __name__ == '__main__':
    unittest.main()
