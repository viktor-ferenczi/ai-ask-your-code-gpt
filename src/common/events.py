import asyncio
import json
from contextlib import asynccontextmanager
from datetime import datetime
from traceback import print_exc
from typing import Any, Dict, ContextManager, Callable, Awaitable

import asyncpg
from asyncpg.utils import _quote_ident

TCallback = Callable[[Any, Any], Awaitable[Any]]

DROP_EVENTS_TABLE_SQL: str = 'drop table if exists "Events";'

CREATE_EVENTS_TABLE_SQL: str = """
create table "Events"
(
    created   timestamp default (current_timestamp at time zone 'utc') not null constraint events_pk primary key,
    name      varchar(100)                        not null,
    params    text      default '{}'::text        not null,
    handled   timestamp
);

comment on column "Events".created is 'When the event was produced';

comment on column "Events".name is 'Event type';

comment on column "Events".params is 'JSON encoded parameters, actual fields depend on the event type';

comment on column "Events".handled is 'Timestamp when the event was successfully handled';

alter table "Events"
    owner to askyourcode;
"""

PUBLISH_EVENT_SQL: str = """
    INSERT INTO "Events" (name, params)
    VALUES ($1, $2)
    RETURNING created;
"""

FETCH_NEXT_EVENT_SQL: str = """
    SELECT created, name, params FROM "Events"
    WHERE name = $1 AND handled IS NULL
    ORDER BY created
    LIMIT 1 FOR UPDATE SKIP LOCKED;
"""

MARK_EVENT_HANDLED_SQL: str = """
    UPDATE "Events"
    SET handled = CURRENT_TIMESTAMP
    WHERE created = $1
"""

DELETE_EVENT_SQL: str = """
    DELETE FROM "Events"
    WHERE created = $1
"""


class EventManager:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

    @asynccontextmanager
    async def get_conn(self) -> ContextManager[asyncpg.Connection]:
        async with self.pool.acquire() as conn:
            yield conn


class Producer(EventManager):
    async def publish_event(self, name: str, params: Dict[str, Any], max_attempts: int = 10, retry_delay: float = 0.001) -> datetime:
        params_json: str = json.dumps(params)
        async with self.get_conn() as conn:
            for attempt in range(max_attempts):
                try:
                    async with conn.transaction():
                        created: datetime = await conn.fetchval(PUBLISH_EVENT_SQL, name, params_json)
                        await conn.execute(f'NOTIFY {_quote_ident(name)}')
                        return created
                except asyncpg.UniqueViolationError:
                    if attempt + 1 == max_attempts:
                        raise
                    await asyncio.sleep(retry_delay)
                    retry_delay = min(1.0, retry_delay * 2)


class Consumer(EventManager):
    def __init__(self, pool: asyncpg.Pool, processing_timeout: int = 300):
        super().__init__(pool)
        self.processing_timeout: int = processing_timeout
        self.handlers: Dict[str, TCallback] = {}

    def register_event_handler(self, event_type: str, callback: TCallback):
        self.handlers[event_type] = callback

    def unregister_event_handler(self, event_type: str):
        self.handlers.pop(event_type, None)

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
        for name in self.handlers:
            await conn.add_listener(name, self.handle_notification)

    async def remove_listeners(self, conn):
        for name in self.handlers:
            await conn.remove_listener(name, self.handle_notification)

    async def handle_notification(self, _: asyncpg.Connection, pid: int, channel: str, payload: str):
        event_handler: TCallback = self.handlers.get(channel)
        if event_handler is None:
            return

        async with self.get_conn() as conn:
            while 1:
                async with conn.transaction():
                    event: Dict[str, Any] = await conn.fetchrow(FETCH_NEXT_EVENT_SQL, channel)
                    if not event:
                        break

                created = event['created']
                kws = json.loads(event['params'])

                try:
                    await event_handler(**kws)
                except Exception:
                    print(f'Failed to process event: {event!r}')
                    print_exc()
                finally:
                    async with conn.transaction():
                        await conn.execute(MARK_EVENT_HANDLED_SQL, created)


class Cleanup(EventManager):
    def __init__(self, pool: asyncpg.Pool):
        super().__init__(pool)

    async def recreate_table(self):
        async with self.get_conn() as conn:
            await conn.execute(DROP_EVENTS_TABLE_SQL)
            await conn.execute(CREATE_EVENTS_TABLE_SQL)

    async def delete_all_events(self):
        async with self.get_conn() as conn:
            async with conn.transaction():
                await conn.execute('TRUNCATE "Events"')
