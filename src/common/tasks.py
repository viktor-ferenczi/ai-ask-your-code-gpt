import asyncio
import json
from contextlib import asynccontextmanager
from datetime import datetime
from traceback import format_exc
from typing import Any, Dict, ContextManager, Callable, Awaitable, List

import asyncpg
from asyncpg import Record
from asyncpg.utils import _quote_ident


class TaskFailed(Exception):
    pass


TCallback = Callable[[Any, Any], Awaitable[Any]]

DROP_TASKS_TABLE_SQL: str = 'drop table public."Tasks";'

CREATE_TASKS_TABLE_SQL: str = """
create table public."Tasks"
(
    created   timestamp default (current_timestamp at time zone 'utc') not null constraint tasks_pk primary key,
    started   timestamp,
    finished  timestamp,
    failed    timestamp,
    name      varchar(50)                         not null,
    project   varchar(36)                         not null,
    params    text      default '{}'::text        not null,
    message   text,
    traceback text
);

comment on column public."Tasks".created is 'When the task was created.';

comment on column public."Tasks".started is 'Processing start time.';

comment on column public."Tasks".finished is 'Processing finish time.';

comment on column public."Tasks".failed is 'Processing failed time.';

comment on column public."Tasks".name is 'Name (type) of the task.';

comment on column public."Tasks".project is 'Project identifier.';

comment on column public."Tasks".params is 'JSON encoded parameters, actual fields depend on the task.';

comment on column public."Tasks".message is 'Message to send back to the user.';

comment on column public."Tasks".traceback is 'Traceback of an error in case of an unexpected failure.';

create index tasks_project
    on public."Tasks" (project);

alter table public."Tasks"
    owner to askyourcode;
"""

CREATE_TASK_SQL: str = """
    INSERT INTO "Tasks" (name, project, params)
    VALUES ($1, $2, $3)
    RETURNING created;
"""

CHECK_TASKS_SQL: str = """
    SELECT created, started, finished, failed, name, params, message, traceback 
    FROM "Tasks"
    WHERE name = $1 AND project = $2
    ORDER BY created;
"""

FETCH_NEXT_TASK_SQL: str = """
    SELECT created, name, params FROM "Tasks"
    WHERE name = $1 AND started IS NULL
    ORDER BY created
    LIMIT 1 FOR UPDATE SKIP LOCKED;
"""

SET_TASK_STARTED_SQL: str = """
    UPDATE "Tasks"
    SET started = current_timestamp
    WHERE created = $1 AND started IS NULL;
"""

SET_TASK_FINISHED_SQL: str = """
    UPDATE "Tasks"
    SET finished = current_timestamp, message = $2
    WHERE created = $1 AND started IS NOT NULL AND finished IS NULL AND failed IS NULL;
"""

SET_TASK_HANDLED_ERROR_SQL: str = """
    UPDATE "Tasks"
    SET failed = current_timestamp, message = $2
    WHERE created = $1 AND started IS NOT NULL AND finished IS NULL AND failed IS NULL;
"""

SET_TASK_UNEXPECTED_ERROR_SQL: str = """
    UPDATE "Tasks"
    SET failed = current_timestamp, message = 'Unexpected error', traceback = $2
    WHERE created = $1 AND started IS NOT NULL AND finished IS NULL AND failed IS NULL;
"""

DELETE_TASK_SQL: str = """
    DELETE FROM "Tasks"
    WHERE created = $1
"""


class TaskManager:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

    @asynccontextmanager
    async def get_conn(self) -> ContextManager[asyncpg.Connection]:
        async with self.pool.acquire() as conn:
            yield conn


class Scheduler(TaskManager):
    async def schedule(self, name: str, project: str, **params) -> datetime:
        max_attempts: int = 10
        retry_delay: float = 0.001
        params_json: str = json.dumps(params)
        async with self.get_conn() as conn:
            for attempt in range(max_attempts):
                try:
                    async with conn.transaction():
                        created: datetime = await conn.fetchval(CREATE_TASK_SQL, name, project, params_json)
                        await conn.execute(f'NOTIFY {_quote_ident(name)}')
                        return created
                except asyncpg.UniqueViolationError:
                    if attempt + 1 == max_attempts:
                        raise
                    await asyncio.sleep(retry_delay)
                    retry_delay = min(1.0, retry_delay * 2)

    async def check(self, name: str, project: str) -> List[Record]:
        async with self.get_conn() as conn:
            async with conn.transaction(readonly=True):
                return await conn.fetch(CHECK_TASKS_SQL, name, project)


class Processor(TaskManager):
    def __init__(self, pool: asyncpg.Pool, processing_timeout: int = 600):
        super().__init__(pool)
        self.processing_timeout: int = processing_timeout
        self.processors: Dict[str, TCallback] = {}

    def register_task(self, name: str, callback: TCallback):
        self.processors[name] = callback

    def unregister_task(self, name: str):
        self.processors.pop(name, None)

    @asynccontextmanager
    async def listen(self):
        async with self.get_conn() as conn:
            async with conn.transaction():
                await self.add_listeners(conn)
            try:
                yield
            finally:
                async with conn.transaction():
                    await self.remove_listeners(conn)

    async def add_listeners(self, conn):
        for name in self.processors:
            await conn.add_listener(name, self.handle_notification)

    async def remove_listeners(self, conn):
        for name in self.processors:
            await conn.remove_listener(name, self.handle_notification)

    async def handle_notification(self, _: asyncpg.Connection, pid: int, name: str, payload: str):
        processor: TCallback = self.processors.get(name)
        if processor is None:
            return

        done = f'{name}$'

        async with self.get_conn() as conn:
            while 1:
                async with conn.transaction():
                    task: Dict[str, Any] = await conn.fetchrow(FETCH_NEXT_TASK_SQL, name)
                    if not task:
                        break
                    created = task['created']
                    await conn.execute(SET_TASK_STARTED_SQL, created)

                kws = json.loads(task['params'])
                try:
                    message = await processor(**kws) or None
                except TaskFailed as e:
                    async with conn.transaction():
                        message = str(e)
                        await conn.execute(SET_TASK_HANDLED_ERROR_SQL, created, message)
                except Exception:
                    async with conn.transaction():
                        traceback = format_exc()
                        await conn.execute(SET_TASK_UNEXPECTED_ERROR_SQL, created, traceback)
                else:
                    async with conn.transaction():
                        await conn.execute(SET_TASK_FINISHED_SQL, created, message)

                await conn.execute(f'NOTIFY {_quote_ident(done)}')


class Cleanup(TaskManager):
    def __init__(self, pool: asyncpg.Pool):
        super().__init__(pool)

    async def delete_all_tasks(self):
        async with self.get_conn() as conn:
            async with conn.transaction():
                await conn.execute('TRUNCATE "Tasks"')

    async def restart_all_processing(self):
        async with self.get_conn() as conn:
            async with conn.transaction():
                await conn.execute('UPDATE "Tasks" SET started = NULL WHERE started IS NOT NULL AND finished IS NULL AND failed IS NULL')
