import json
from asyncio import Queue
from dataclasses import dataclass
from typing import Any, Dict, Tuple, AsyncIterator

import asyncpg
from asyncpg import Connection
from asyncpg.utils import _quote_ident

from storage.database import Database


@dataclass
class Event:
    channel: str
    params: Dict[str, Any]


class PubSub:

    def __init__(self, db: Database):
        self.db: Database = db
        self.queue: Queue[Event] = Queue()

    async def send(self, channel: str, **params: Any):
        payload = json.dumps(params).replace("'", "''")
        sql = f"NOTIFY {_quote_ident(channel)}, '{payload}'"
        print(sql)
        async with self.db.connection() as conn:
            await conn.execute(sql)

    async def listen(self, *channels: str) -> AsyncIterator[Event]:
        assert channels, 'No channels specified'
        async with self.db.connection() as conn:
            await self.__add_listeners(conn, channels)
            try:
                while 1:
                    event = await self.queue.get()
                    print(event)
                    yield event
            finally:
                await self.__remove_listeners(conn, channels)

    async def __add_listeners(self, conn: Connection, channels: Tuple[str]):
        for channel in channels:
            await conn.add_listener(channel, self.handle_notification)

    async def __remove_listeners(self, conn: Connection, channels: Tuple[str]):
        for channel in channels:
            await conn.remove_listener(channel, self.handle_notification)

    # noinspection PyUnusedLocal
    async def handle_notification(self, conn: asyncpg.Connection, pid: int, channel: str, payload: str):
        event = Event(channel, json.loads(payload))
        await self.queue.put(event)
