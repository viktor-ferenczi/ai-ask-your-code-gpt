import asyncio
import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from traceback import format_exc
from typing import Any, Dict, Callable, List, Optional, Union, Awaitable, Iterable

from asyncpg import Record, Connection
from asyncpg.utils import _quote_ident

from common.constants import C
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
    id: int = 0
    created: datetime = datetime(2000, 1, 1)
    started: Optional[datetime] = None
    finished: Optional[datetime] = None
    state: TaskState = TaskState.pending
    operation: Operation = Operation.Dummy
    params: Dict[str, Any] = field(default_factory=lambda: {})
    message: Optional[str] = None

    @property
    def wait_time(self) -> timedelta:
        if self.started is None:
            return datetime.utcnow() - self.created
        return self.started - self.created

    @property
    def runtime(self) -> Optional[timedelta]:
        if self.finished is None:
            return None
        return self.finished - self.started

    @classmethod
    def create_pending(cls, operation: Operation, **params: Any) -> "Task":
        return cls(operation=operation, params=params)

    @classmethod
    def from_row(cls, row: Record) -> "Task":
        return cls(
            id=row['id'],
            created=row['created'],
            started=row['started'],
            finished=row['finished'],
            state=TaskState(row['state']),
            operation=Operation(row['operation']),
            params=json.loads(row['params']),
            message=row['message'],
        )


THandlerResult = Union[None, Task, List[Task]]
THandler = Callable[..., Awaitable[THandlerResult]]


class Scheduler:

    def __init__(self, db: Database):
        self.db: Database = db

    async def schedule(self, task: Task):
        async with self.db.transaction() as conn:
            await self.__insert(conn, task)

    async def schedule_many(self, tasks: Iterable[Task]):
        async with self.db.transaction() as conn:
            for task in tasks:
                await self.__insert(conn, task)

    async def __insert(self, conn: Connection, task: Task):
        created = datetime.utcnow()
        name = task.operation.name
        params_json = json.dumps(task.params)
        id = await conn.fetchval('''
                    INSERT INTO task (created, operation, params)
                    VALUES ($1, $2, $3)
                    RETURNING id;
                ''', created, name, params_json)
        notify = f"NOTIFY {_quote_ident(name)}"
        # print(notify)
        await conn.execute(notify)
        task.id = id
        task.created = created

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

        def callback(*_):
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
            row = await self.get_next_unclaimed_task_for_update(conn, operation)
            if row is None:
                # No more tasks
                return False

            # Run the task while still in the transaction, so other workers must skip it
            task: Task = Task.from_row(row)
            result = None
            # noinspection PyBroadException
            try:
                try:
                    task.started = datetime.utcnow()
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
                if isinstance(result, Task):
                    await self.__insert(conn, result)
                elif isinstance(result, (list, tuple)) and all(isinstance(t, Task) for t in result):
                    for t in result:
                        await self.__insert(conn, t)
                elif result is not None:
                    print('WARNING: The task completed, but an invalid result was returned by its handler')
                    print(f'Task: {task!r}')
                    print(f'Handler: {handler!r}')
                    print(f'Result: {result!r}')

            await conn.execute('''
                    UPDATE task
                    SET state = $2,
                        message = $3,
                        started = $4, 
                        finished = $5
                    WHERE id = $1
                ''', task.id, task.state.name, task.message, task.started, task.finished)

        # Attempt to read more tasks from the queue
        return True

    async def get_next_unclaimed_task_for_update(self, conn, operation: Operation) -> Optional[Record]:
        row = await conn.fetchrow('''
                    SELECT * FROM task
                    WHERE operation = $1 AND state = 'pending'
                    ORDER BY id
                    LIMIT 1 FOR UPDATE SKIP LOCKED;
                ''', operation.name)
        return row

    async def get_task(self, id: int) -> Optional[Task]:
        async with self.db.transaction() as conn:
            row = await conn.fetchrow('''
                    SELECT * 
                    FROM task 
                    WHERE id = $1
                ''', id)
            return Task.from_row(row) if row else None

    async def wait_task_leave_state(self, id: int, state_to_leave: TaskState.pending, *, polling_period: float = 0.2) -> Task:
        await asyncio.sleep(0)
        while 1:
            task = await self.get_task(id)
            if task.state != state_to_leave:
                return task
            await asyncio.sleep(polling_period)

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
