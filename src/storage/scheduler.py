import asyncio
import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from traceback import format_exc, print_exc
from typing import Any, Dict, Callable, List, Optional, Union, Awaitable

from asyncpg import Record
from asyncpg.utils import _quote_ident

from common.constants import C
from common.tools import async_retry
from storage.database import Database


class TaskFailed(Exception):
    pass


class TaskState(Enum):
    pending = 'pending'
    completed = 'completed'
    failed = 'failed'
    crashed = 'crashed'


class Operation(Enum):
    Dummy = 'Dummy'
    Test1 = 'Test1'
    Test2 = 'Test2'
    CreateProject = 'CreateProject'
    DownloadArchive = 'DownloadArchive'
    ExtractArchive = 'ExtractArchive'
    DownloadSource = 'DownloadSource'
    IndexSource = 'IndexSource'
    QuerySummary = 'QuerySummary'
    QuerySearch = 'QuerySearch'


@dataclass
class Task:
    created: datetime = datetime(2000, 1, 1)
    started: Optional[datetime] = None
    finished: Optional[datetime] = None
    state: TaskState = TaskState.pending
    operation: Operation = Operation.Dummy
    params: Dict[str, Any] = field(default_factory=lambda: {})
    message: Optional[str] = None

    @classmethod
    def create_pending(cls, operation: Operation, **params: Any) -> "Task":
        return cls(operation=operation, params=params)

    @classmethod
    def from_row(cls, row: Record) -> "Task":
        return cls(
            operation=Operation(row['operation']),
            params=json.loads(row['params']),
            state=TaskState(row['state']),
            created=row['created'],
            started=row['started'],
            finished=row['finished'],
            message=row['message'],
        )


THandlerResult = Union[None, Task, List[Task]]
THandler = Callable[..., Awaitable[THandlerResult]]


class Scheduler:

    def __init__(self, db: Database):
        self.db: Database = db

    async def schedule(self, task: Task):
        params_json = json.dumps(task.params)

        async def fn():
            async with self.db.transaction() as conn:
                name = task.operation.name
                created: datetime = await conn.fetchval('''
                        INSERT INTO task (operation, params)
                        VALUES ($1, $2)
                        RETURNING created;
                    ''', name, params_json)
                notify = f"NOTIFY {_quote_ident(name)}"
                # print(notify)
                await conn.execute(notify)
                task.created = created

        await async_retry(fn)

    async def list_pending_tasks(self, operation: Operation, limit=1_000_000) -> List[Task]:
        async with self.db.transaction(readonly=True) as conn:
            rows = await conn.fetch('''
                SELECT created, started, finished, state, operation, params, message 
                FROM task
                WHERE operation = $1 AND state = 'pending'
                ORDER BY created
                LIMIT $2;            
            ''', operation.name, limit)
        return [Task.from_row(row) for row in rows]

    async def listen(self, operation: Operation, handler: THandler):
        event = asyncio.Event()

        def callback(*args):
            event.set()

        async with self.db.connection() as conn:
            await conn.add_listener(operation.name, callback)
            try:
                while 1:
                    event.clear()
                    if await self.process(operation, handler):
                        continue
                    await event.wait()
            finally:
                await conn.remove_listener(operation.name, callback)

    async def process(self, operation: Operation, handler: THandler) -> bool:
        async with self.db.transaction() as conn:
            # Get the next task to process
            row = await self.get_next_task(conn, operation)
            if row is None:
                # No more tasks
                return False

            # Run the task while still in the transaction, so other workers must skip it
            task: Task = Task.from_row(row)
            task.started = datetime.utcnow()
            result = None
            # noinspection PyBroadException
            try:
                try:
                    result = await asyncio.wait_for(handler(**task.params), timeout=C.TASK_TIMEOUT)
                finally:
                    task.finished = datetime.utcnow()
            except asyncio.TimeoutError:
                task.state = TaskState.failed
                task.message = 'Timeout'
            except TaskFailed as e:
                task.state = TaskState.failed
                task.message = str(e)
            except Exception:
                task.state = TaskState.crashed
                task.message = format_exc()
                print('ERROR: Task handler crashed:')
                print(f'Task: {task!r}')
                print(f'Handler: {handler!r}')
                print(task.message)
            else:
                task.state = TaskState.completed

            await conn.execute('''
                UPDATE task
                SET state = $2,
                    message = $3,
                    started = $4, 
                    finished = $5
                WHERE created = $1
            ''', task.created, task.state.name, task.message, task.started, task.finished)

        # Schedule any follow-up tasks
        follow_up_tasks = ()
        # noinspection PyBroadException
        try:
            if isinstance(result, Task):
                follow_up_tasks = [result]
            elif isinstance(result, (list, tuple)) and all(isinstance(t, Task) for t in result):
                follow_up_tasks = result
            elif result is not None:
                print(f'ERROR: Invalid result returned by a task handler:')
                print(f'Task: {task!r}')
                print(f'Handler: {handler!r}')
                print(f'Result: {result!r}')

            for response_task in follow_up_tasks:
                await self.schedule(response_task)
        except Exception:
            print(f'ERROR: Failed to schedule follow-up tasks')
            print(f'Task: {task!r}')
            print(f'Handler: {handler!r}')
            print(f'Follow-up tasks: {follow_up_tasks!r}')
            print_exc()

        # Attempt to read more tasks from the queue
        return True

    async def get_next_task(self, conn, operation: Operation) -> Optional[Record]:
        row = await conn.fetchrow('''
                SELECT * FROM task
                WHERE operation = $1 AND state = 'pending'
                ORDER BY created
                LIMIT 1 FOR UPDATE SKIP LOCKED;
            ''', operation.name)
        return row

    async def get_task(self, created: datetime) -> Optional[Task]:
        async with self.db.transaction() as conn:
            row = await conn.fetchrow('''
                SELECT * 
                FROM task 
                WHERE created = $1
            ''', created)
            return Task.from_row(row) if row else None

    async def count_tasks(self, state: TaskState) -> int:
        async with self.db.transaction() as conn:
            return await conn.fetchval('''
                SELECT COUNT(1) 
                FROM task 
                WHERE state = $1
            ''', state.name)

    async def delete_all_tasks(self):
        async with self.db.transaction() as conn:
            await conn.execute('TRUNCATE task')
