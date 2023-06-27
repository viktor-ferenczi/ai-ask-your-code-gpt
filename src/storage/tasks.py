import asyncio
import json
from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from traceback import format_exc
from typing import Any, Dict, Callable, List, Optional, Union, Awaitable, AsyncContextManager

import asyncpg
from asyncpg import Record, Connection, Pool
from asyncpg.utils import _quote_ident

from common.tools import async_retry
from storage import sql
from storage.database import Database


class TaskName(Enum):
    Test1 = 'Test1'
    Test2 = 'Test2'
    CreateProject = 'CreateProject'
    DownloadArchive = 'DownloadArchive'
    IndexArchive = 'IndexArchive'
    DownloadSource = 'DownloadSource'
    IndexSource = 'IndexSource'
    QuerySummary = 'QuerySummary'
    QuerySearch = 'QuerySearch'


class TaskState(Enum):
    new = 'pending'
    running = 'running'
    completed = 'completed'
    failed = 'failed'
    crashed = 'crashed'


ZERO_TIME = datetime(2000, 1, 1)


@dataclass
class Task:
    name: TaskName
    project: Optional[str] = None
    params: Optional[Dict[str, Any]] = None
    state: TaskState = 'pending'
    created: datetime = ZERO_TIME
    started: Optional[datetime] = None
    finished: Optional[datetime] = None
    message: Optional[str] = None
    traceback: Optional[str] = None

    @classmethod
    def from_row(cls, row):
        params = row['params']
        return cls(
            name=TaskName(row['name']),
            project=row['project'],
            params=json.loads(params) if params else None,
            state=TaskState(row['state']),
            created=row['created'],
            started=row['started'],
            finished=row['finished'],
            message=row['message'],
            traceback=row['traceback'],
        )


class TaskFailed(Exception):
    pass


THandlerResult = Union[None, Task, List[Task]]
THandler = Callable[[Task], Awaitable[THandlerResult]]


class Tasks:
    dsn = 'postgres://askyourcode:askyourcode@127.0.0.1:5432/askyourcode'

    max_retries: int = 10
    retry_delay: float = 0.001
    handler_timeout: float = 300.0
    suffix: str = ''

    def __init__(self, db: Database):
        self.db: Database = db
        self.handlers: Dict[TaskName, THandler] = {}

    @classmethod
    @asynccontextmanager
    async def init(cls) -> AsyncContextManager["Tasks"]:
        # FIXME: This should work, but instead freezes at the end of block:
        # async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:

        # Workaround
        pool: Pool = asyncpg.create_pool(cls.dsn, command_timeout=60)
        await pool._async__init__()
        db = Database(pool)
        try:
            await db.migrate()
            yield cls(db)
        finally:
            del db
            # await asyncio.wait_for(pool.close(), timeout=3)
            # Workaround
            pool.terminate()

    async def wait_complete(self, task: Task, *, timeout: float = 30.0, poll_period: float = 0.5) -> Optional[Task]:
        assert timeout >= 2.0 * poll_period
        created = task.created

        deadline = datetime.utcnow() + timedelta(seconds=timeout - poll_period)
        while datetime.utcnow() < deadline:
            await asyncio.sleep(poll_period)

            task = await self.get_task(created)
            if not task:
                continue

            if task.state in (TaskState.completed, TaskState.failed, TaskState.crashed):
                return task

        return None

    async def schedule(self, task: Task):
        async with self.db.connection() as conn:
            await async_retry(lambda: self.__schedule(conn, task))

    async def __schedule(self, conn: Connection, task: Task):
        params_json = json.dumps(task.params)
        async with conn.transaction():
            name = task.name.name
            created: datetime = await conn.fetchval(sql.CREATE_TASK, name, task.project, params_json)
            notify = f"NOTIFY {_quote_ident(name)}, '{created.isoformat()}'"
            print(notify)
            await conn.execute(notify)
            task.created = created

    async def list_tasks_by_project(self, name: TaskName, project: str) -> List[Record]:
        async with self.db.transaction(readonly=True) as conn:
            return await conn.fetch(sql.LIST_PROJECT_TASKS, name.name, project)

    async def list_pending_tasks(self, name: TaskName) -> List[Record]:
        async with self.db.transaction(readonly=True) as conn:
            return await conn.fetch(sql.LIST_PENDING_TASKS, name.name)

    @asynccontextmanager
    async def listener(self, suffix: str = '') -> AsyncContextManager:
        assert self.handlers, 'No tasks registered'
        async with self.db.connection() as conn:
            await self.__add_listeners(conn, suffix)
            try:
                yield
            finally:
                await self.__remove_listeners(conn, suffix)

    async def __add_listeners(self, conn: Connection, suffix: str):
        for name in self.handlers:
            await conn.add_listener(f'{name.name}{suffix}', self.handle_notification)

    async def __remove_listeners(self, conn: Connection, suffix: str):
        for name in self.handlers:
            await conn.remove_listener(f'{name.name}{suffix}', self.handle_notification)

    async def handle_notification(self, listener_conn: asyncpg.Connection, pid: int, name: str, payload: str):
        print(f'TASK pid={pid!r}, name={name!r}, payload={payload!r}')
        # if pid == listener_conn.get_server_pid():
        #     return

        handler: THandler = self.handlers.get(TaskName(name))
        if handler is None:
            return

        async with self.db.connection() as conn:

            row = await conn.fetchrow(sql.FETCH_TASK_FOR_UPDATE, datetime.fromisoformat(payload))
            if row is None:
                return

            task: Task = Task.from_row(row)
            if task.state != TaskState.new:
                return

            new_state = await conn.fetchval(sql.SET_TASK_RUNNING, task.created)
            assert new_state == 'running'

            task = await self.get_task(task.created)

        try:
            result = await asyncio.wait_for(handler(task), timeout=self.handler_timeout)

            if result is None:
                response_tasks = []
            elif isinstance(result, Task):
                response_tasks = [result]
            elif isinstance(result, list) and all(isinstance(t, Task) for t in result):
                response_tasks = result
            else:
                raise ValueError(f'Invalid result returned by the task handler: {result!r}')

        except asyncio.TimeoutError:
            async with self.db.transaction() as conn:
                new_state = await conn.fetchval(sql.SET_TASK_FAILED, task.created, 'Timed out')
                assert new_state == 'failed'
        except TaskFailed as e:
            async with self.db.transaction() as conn:
                message = str(e)
                new_state = await conn.fetchval(sql.SET_TASK_FAILED, task.created, message)
                assert new_state == 'failed'
        except Exception:
            async with self.db.transaction() as conn:
                traceback = format_exc()
                print('Handler crashed:')
                print(f'task = {task!r}')
                print(traceback)
                new_state = await conn.fetchval(sql.SET_TASK_CRASHED, task.created, traceback)
                assert new_state == 'crashed'
        else:
            async with self.db.transaction() as conn:
                new_state = await conn.fetchval(sql.SET_TASK_COMPLETED, task.created)
                assert new_state == 'completed'
                for response_task in response_tasks:
                    await self.schedule(response_task)

    async def retry_all_tasks(self):
        async with self.db.transaction() as conn:
            await conn.execute(sql.RETRY_TASKS)

    async def delete_all_tasks(self):
        async with self.db.transaction() as conn:
            await conn.execute(sql.TRUNCATE_TASKS)

    async def get_task(self, created: datetime) -> Optional[Task]:
        async with self.db.transaction() as conn:
            row = await conn.fetchrow(sql.GET_TASK, created)
            return Task.from_row(row) if row else None

    async def update_task(self, task: Task) -> Optional[Task]:
        async with self.db.transaction() as conn:
            row = await conn.fetchrow(sql.UPDATE_TASK, task.created, task.project)
            return Task.from_row(row) if row else None
