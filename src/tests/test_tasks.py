import asyncio
import unittest
from datetime import datetime
from typing import List, NoReturn

import asyncpg

from storage.database import Database
from storage.tasks import Tasks, TaskName, Task, THandlerResult, TaskState, TaskFailed


class TestTasks(unittest.IsolatedAsyncioTestCase):
    # postgres://user:password@host:port/database
    dsn = 'postgres://askyourcode:askyourcode@127.0.0.1:5432/askyourcode_test'

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:

            db = Database(pool)
            await db.migrate()

            tasks = Tasks(db)
            await tasks.delete_all_tasks()

    async def test_produce_consume(self) -> None:
        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            tasks0: List[Task] = []

            async def handler(task: Task) -> THandlerResult:
                tasks0.append(task)
                self.assertEqual(task.name, TaskName.Test1)
                self.assertEqual(task.state, TaskState.running)
                self.assertIsNotNone(task.started)
                self.assertIsNone(task.params)
                return None

            db = Database(pool)
            tasks = Tasks(db)
            tasks.handlers[TaskName.Test1] = handler

            async with tasks.listener():

                # Produce task
                task = Task(name=TaskName.Test1)
                started = datetime.utcnow()
                await tasks.schedule(task)
                finished = datetime.utcnow()
                created = task.created
                self.assertTrue(started <= created, f'{started!r} <= {created!r}')
                self.assertTrue(created <= finished, f'{created!r} <= {finished!r}')

                # Handle task
                for _ in range(50):
                    await asyncio.sleep(0.01)
                    if tasks0:
                        break

            self.assertEqual(len(tasks0), 1)
            t = await tasks.get_task(task.created)
            self.assertEqual(t.state, TaskState.completed)
            self.assertTrue(bool(t.started))
            self.assertTrue(bool(t.finished))
            self.assertIsNone(t.message)
            self.assertIsNone(t.traceback)

            tasks1 = await tasks.list_pending_tasks(TaskName.Test1)
            self.assertEqual(len(tasks1), 0)

            tasks2 = await tasks.list_pending_tasks(TaskName.Test2)
            self.assertEqual(len(tasks2), 0)

    async def test_failed_handler(self) -> None:
        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            tasks0: List[Task] = []

            async def handler(task: Task) -> NoReturn:
                tasks0.append(task)
                raise TaskFailed('Testing')

            db = Database(pool)
            tasks = Tasks(db)
            tasks.handlers[TaskName.Test1] = handler

            async with tasks.listener():
                task = Task(name=TaskName.Test1)
                await tasks.schedule(task)

                # Handle task
                for _ in range(50):
                    await asyncio.sleep(0.01)
                    if tasks0:
                        break

            self.assertEqual(len(tasks0), 1)
            t = await tasks.get_task(task.created)
            self.assertEqual(t.state, TaskState.failed)
            self.assertTrue(bool(t.started))
            self.assertTrue(bool(t.finished))
            self.assertEqual(t.message, 'Testing')
            self.assertIsNone(t.traceback)

    async def test_crashed_handler(self) -> None:
        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            tasks0: List[Task] = []

            async def handler(task: Task) -> NoReturn:
                tasks0.append(task)
                raise Exception('Testing')

            db = Database(pool)
            tasks = Tasks(db)
            tasks.handlers[TaskName.Test1] = handler

            async with tasks.listener():
                task = Task(name=TaskName.Test1)
                await tasks.schedule(task)

                # Handle task
                for _ in range(50):
                    await asyncio.sleep(0.01)
                    if tasks0:
                        break

            self.assertEqual(len(tasks0), 1)
            t = await tasks.get_task(task.created)
            self.assertEqual(t.state, TaskState.crashed)
            self.assertTrue(bool(t.started))
            self.assertTrue(bool(t.finished))
            self.assertIsNone(t.message)
            self.assertTrue('Exception: Testing' in t.traceback)


if __name__ == '__main__':
    unittest.main()
