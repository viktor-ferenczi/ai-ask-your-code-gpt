import asyncio
import time
import unittest
from datetime import datetime
from typing import List, NoReturn, Any

from base_test_case import BaseTestCase
from storage.scheduler import Scheduler, Operation, Task, THandlerResult, TaskState, TaskFailed


class TestScheduler(BaseTestCase):
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        self.tasks = Scheduler(self.db)
        await self.tasks.delete_all_tasks()

    async def asyncTearDown(self) -> None:
        del self.tasks
        await super().asyncTearDown()

    async def test_produce_consume(self) -> None:
        numbers: List[int] = []

        async def handler(x) -> THandlerResult:
            numbers.append(x)
            return None

        self.tasks.register_handler(Operation.Test1, handler)

        # Listen for tasks and handle them
        async with self.tasks.listen():
            # Schedule a task
            task = Task.create_pending(Operation.Test1, x=42)
            before = datetime.utcnow()
            await self.tasks.schedule(task)
            after = datetime.utcnow()
            created = task.created
            self.assertTrue(before <= created, f'{before!r} <= {created!r}')
            self.assertTrue(created <= after, f'{created!r} <= {after!r}')

            await self.wait_for_processing(numbers)

        # Verify
        self.assertEqual(len(numbers), 1)
        self.assertEqual(numbers[0], 42)
        task = await self.tasks.get_task(task.created)
        await self.verify_task(task, x=42)

        # No tasks left
        pending1 = await self.tasks.list_pending_tasks(Operation.Test1)
        self.assertEqual(len(pending1), 0)
        pending2 = await self.tasks.list_pending_tasks(Operation.Test2)
        self.assertEqual(len(pending2), 0)

    async def verify_task(self, task, **params):
        self.assertEqual(task.operation, Operation.Test1)
        self.assertEqual(task.state, TaskState.completed)
        self.assertEqual(task.params, params)
        self.assertIsNotNone(task.started)
        self.assertIsNotNone(task.finished)
        self.assertIsNone(task.message)
        print(f'Task was handled in {(task.finished - task.started).total_seconds() * 1000:.3f}ms')
        print(f'From task creation {(task.finished - task.created).total_seconds() * 1000:.3f}ms')

    async def test_failed_handler(self) -> None:
        tasks: List[int] = []

        async def handler() -> NoReturn:
            tasks.append(1)
            raise TaskFailed('Test failure')

        self.tasks.register_handler(Operation.Test1, handler)

        async with self.tasks.listen():
            task = Task.create_pending(Operation.Test1)
            await self.tasks.schedule(task)

            await self.wait_for_processing(tasks)

        self.assertEqual(len(tasks), 1)
        task = await self.tasks.get_task(task.created)
        self.assertEqual(task.state, TaskState.failed)
        self.assertTrue(bool(task.started))
        self.assertTrue(bool(task.finished))
        self.assertEqual(task.message, 'Test failure')

    async def test_crashed_handler(self) -> None:
        tasks: List[int] = []

        async def handler() -> NoReturn:
            tasks.append(1)
            raise Exception('Test crash')

        self.tasks.register_handler(Operation.Test1, handler)

        async with self.tasks.listen():
            task = Task.create_pending(Operation.Test1)
            await self.tasks.schedule(task)

            await self.wait_for_processing(tasks)

        self.assertEqual(len(tasks), 1)
        task = await self.tasks.get_task(task.created)
        self.assertEqual(task.state, TaskState.crashed)
        self.assertTrue(bool(task.started))
        self.assertTrue(bool(task.finished))
        self.assertTrue('Exception: Test crash' in task.message)

    async def wait_for_processing(self, tasks: List[Any], expected_count: int = 1, timeout: float = 1.0):
        deadline = time.time() + timeout
        while len(tasks) < expected_count and time.time() < deadline:
            await asyncio.sleep(0)
            if tasks:
                break


if __name__ == '__main__':
    unittest.main()
