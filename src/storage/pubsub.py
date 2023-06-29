import asyncio
import json
from asyncio import Queue
from contextlib import asynccontextmanager
from dataclasses import dataclass
from enum import Enum
from time import time
from typing import Any, Dict, Tuple, AsyncIterator, AsyncContextManager, Optional, Callable

import asyncpg
from asyncpg import Connection
from asyncpg.utils import _quote_ident

from storage.database import Database


class ChannelName(Enum):
    DownloadCompleted = 'DownloadCompleted'


@dataclass
class Event:
    channel: str
    params: Dict[str, Any]


class PubSub:

    def __init__(self, db: Database):
        self.db: Database = db
        self.queue: Queue[Event] = Queue()
        self.listening = False

    async def send(self, channel: str, **params: Any):
        payload = json.dumps(params).replace("'", "''")
        sql = f"NOTIFY {_quote_ident(channel)}, '{payload}'"
        print(sql)
        async with self.db.connection() as conn:
            await conn.execute(sql)

    @asynccontextmanager
    async def listen(self, *channels: str) -> AsyncContextManager:
        assert channels, 'No channels specified'
        async with self.db.connection() as conn:
            self.listening = True
            await self.__add_listeners(conn, channels)
            try:
                yield
            finally:
                await self.__remove_listeners(conn, channels)
                self.listening = False

    async def iter_events(self) -> AsyncIterator[Event]:
        while self.listening:
            yield await self.receive()

    async def receive(self) -> Event:
        event = await self.queue.get()
        print(event)
        return event

    async def receive_with_timeout(self, timeout: float, *, predicate: Optional[Callable[[Event], bool]] = None) -> Event:
        deadline: float = time() + timeout
        while 1:
            event = await asyncio.wait_for(self.receive(), max(1e-3, deadline - time()))
            if predicate is None or predicate(event):
                return event

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
