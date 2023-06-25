import asyncio
import json
from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import Any, Dict, ContextManager, Callable, Awaitable

import asyncpg
from asyncpg.utils import _quote_ident

TCallback = Callable[[Any, Any], Awaitable[Any]]


CREATE_EVENTS_TABLE_SQL: str = """
create table public."Events"
(
    created   timestamp default CURRENT_TIMESTAMP not null constraint events_pk primary key,
    type      varchar(100)                        not null,
    params    text      default '{}'::text        not null,
    deadline  timestamp,
    processed timestamp
);

comment on column public."Events".created is 'When the event was produced';

comment on column public."Events".type is 'Event type';

comment on column public."Events".params is 'JSON encoded parameters, actual fields depend on the event type.';

comment on column public."Events".deadline is 'Deadline of event processing after which the event should be retried, NULL if not processed yet ';

comment on column public."Events".processed is 'End of event processing if not NULL';

alter table public."Events"
    owner to askyourcode;
"""

PUBLISH_EVENT_SQL: str = """
    INSERT INTO "Events" (type, params)
    VALUES ($1, $2)
    RETURNING created;
"""

FETCH_NEXT_EVENT_SQL: str = """
    SELECT created, type, params FROM "Events"
    WHERE type = $1 AND deadline IS NULL AND processed IS NULL
    ORDER BY created
    LIMIT 1 FOR UPDATE SKIP LOCKED;
"""

SET_EVENT_DEADLINE_SQL: str = """
    UPDATE "Events"
    SET deadline = $1
    WHERE created = $2 AND processed IS NULL;
"""

MARK_EVENT_PROCESSED_SQL: str = """
    UPDATE "Events"
    SET deadline = NULL, processed = CURRENT_TIMESTAMP
    WHERE created = $1 AND deadline IS NOT NULL;
"""

MARK_EVENT_FAILED_SQL: str = """
    UPDATE "Events"
    SET deadline = CURRENT_TIMESTAMP
    WHERE created = $1 AND processed IS NULL;
"""

DELETE_EVENT_SQL: str = """
    DELETE FROM "Events"
    WHERE created = $1 AND deadline IS NULL AND processed IS NOT NULL
"""


class EventManager:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

    @asynccontextmanager
    async def get_conn(self) -> ContextManager[asyncpg.Connection]:
        async with self.pool.acquire() as conn:
            yield conn


class Producer(EventManager):
    async def publish_event(self, type: str, params: Dict[str, Any], max_attempts: int = 10, retry_delay: float = 0.001) -> datetime:
        params_json: str = json.dumps(params)
        async with self.get_conn() as conn:
            for attempt in range(max_attempts):
                try:
                    async with conn.transaction():
                        created: datetime = await conn.fetchval(PUBLISH_EVENT_SQL, type, params_json)
                        await conn.execute(f'NOTIFY {_quote_ident(type)}')
                        return created
                except asyncpg.UniqueViolationError:
                    if attempt + 1 == max_attempts:
                        raise
                    await asyncio.sleep(retry_delay)
                    retry_delay = min(1.0, retry_delay * 2)


class Consumer(EventManager):
    def __init__(self, pool: asyncpg.Pool, error_type: str = 'Error', processing_timeout: int = 300):
        super().__init__(pool)
        self.error_type = error_type
        self.processing_timeout: int = processing_timeout
        self.event_handlers: Dict[str, TCallback] = {}
        self.error_producer: Producer = Producer(pool)

    def register_event_handler(self, event_type: str, callback: TCallback):
        self.event_handlers[event_type] = callback

    def unregister_event_handler(self, event_type: str):
        self.event_handlers.pop(event_type, None)

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
        for type in self.event_handlers:
            await conn.add_listener(type, self.handle_notification)

    async def remove_listeners(self, conn):
        for type in self.event_handlers:
            await conn.remove_listener(type, self.handle_notification)

    async def handle_notification(self, _: asyncpg.Connection, pid: int, channel: str, payload: str):
        print(f"Got NOTIFY: {pid}, {channel}, {payload}")

        event_handler: TCallback = self.event_handlers.get(channel)
        if event_handler is None:
            return

        async with self.get_conn() as conn:
            while 1:
                async with conn.transaction():
                    event: Dict[str, Any] = await conn.fetchrow(FETCH_NEXT_EVENT_SQL, channel)
                    if not event:
                        break

                    created = event['created']

                    deadline: datetime = datetime.now() + timedelta(seconds=self.processing_timeout)
                    await conn.execute(SET_EVENT_DEADLINE_SQL, deadline, created)

                kws = json.loads(event['params'])
                try:
                    await event_handler(**kws)
                except Exception as e:
                    await self.produce_error_event(event, str(e))
                    async with conn.transaction():
                        await conn.execute(MARK_EVENT_FAILED_SQL, created)
                else:
                    async with conn.transaction():
                        await conn.execute(MARK_EVENT_PROCESSED_SQL, created)

    async def produce_error_event(self, event: Dict[str, Any], message: str):
        error_params: Dict[str, Any] = {
            'event': {
                'type': event['type'],
                'params': event['params']
            },
            'message': message
        }
        await self.error_producer.publish_event(self.error_type, error_params)


class Cleanup(EventManager):
    def __init__(self, pool: asyncpg.Pool):
        super().__init__(pool)

    async def delete_all_events(self):
        async with self.get_conn() as conn:
            async with conn.transaction():
                await conn.execute('TRUNCATE "Events"')

    async def reset_event_processing(self):
        async with self.get_conn() as conn:
            async with conn.transaction():
                await conn.execute('UPDATE "Events" SET deadline = NULL WHERE deadline IS NOT NULL and processed IS NULL')
