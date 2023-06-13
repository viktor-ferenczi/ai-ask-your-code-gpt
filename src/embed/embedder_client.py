import asyncio
import json
import os
import random
import time
from traceback import print_exc
from typing import Optional, List

import aiohttp
import numpy as np
from aiohttp import ClientConnectorError

from common.constants import C
from model.fragment import Fragment

QUERY_EMBEDDERS = os.environ.get('QUERY_EMBEDDERS', 'http://127.0.0.1:40100').split()
STORE_EMBEDDERS = os.environ.get('STORE_EMBEDDERS', 'http://127.0.0.1:40200 http://127.0.0.1:40201 http://127.0.0.1:40202').split()

EMBEDDER_CHUNK_SIZE = int(os.environ.get('EMBEDDER_CHUNK_SIZE', '128'))

FREE = 0
BUSY = 1
MISSING = 2


class EmbedderError(Exception):
    pass


class EmbedderClient:
    def __init__(self, servers: List[str]) -> None:
        self.servers: List[str] = servers
        self.missing = [False for _ in self.servers]
        self.chunk_size: int = EMBEDDER_CHUNK_SIZE

    @property
    def server_count(self):
        return len(self.servers)

    async def embed_fragments(self, fragments: List[Fragment], *, timeout=30.0 if C.PRODUCTION else 999999.0) -> np.ndarray:
        data = json.dumps(dict(fragments=[fragment.__dict__ for fragment in fragments]), indent=2)

        server = await self.find_free_server(timeout=300.0 if C.PRODUCTION else 999999.0)
        if not server:
            print(f'Configured embedder servers: {self.servers}')
            raise EmbedderError('No embedder servers are available')

        async with aiohttp.ClientSession() as session:
            async with session.post(f'{server}/embed/fragments', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
                content = await response.content.read()
                if response.status != 200:
                    raise EmbedderError(f'Failed to embed fragments using embedder: {server}')

        embeddings = np.frombuffer(content, np.float32).reshape(len(fragments), 768)
        return embeddings

    async def embed_query(self, instruction: str, query: str, *, timeout=20.0 if C.PRODUCTION else 999999.0) -> np.ndarray:
        if not instruction.strip():
            raise EmbedderError('Empty instruction')

        if not query.strip():
            raise EmbedderError('Empty query')

        data = json.dumps(dict(instruction=instruction, query=query), indent=2)

        server = await self.find_free_server(timeout=30.0 if C.PRODUCTION else 999999.0)
        if not server:
            raise EmbedderError('No embedder servers are available')

        async with aiohttp.ClientSession() as session:
            async with session.post(f'{server}/embed/query', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
                content = await response.content.read()
                if response.status != 200:
                    raise EmbedderError(f'Failed to embed fragments using embedder: {server}')

        embedding = np.frombuffer(content, np.float32).reshape(1, 768)
        return embedding

    async def find_free_server(self, *, timeout=30.0 if C.PRODUCTION else 999999.0) -> Optional[str]:
        if not self.servers:
            raise EmbedderError('No embedder servers are configured')

        deadline = time.time() + timeout

        while time.time() < deadline:
            for i, server in enumerate(self.servers):
                if self.missing[i] and random.randrange(10):
                    continue
                status = await self.check_embedder(server, timeout=0.5)
                if status == FREE:
                    return server
                if status == MISSING:
                    self.missing[i] = True

            await asyncio.sleep(0.5)

        return None

    async def check_embedder(self, server: str, *, timeout=5.0) -> int:
        # noinspection PyBroadException
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{server}/check', headers={'Accept': 'text/plain'}, timeout=timeout) as response:
                    if response.status == 200:
                        if C.DEVELOPMENT:
                            print(f'Embedder {server!r} is FREE')
                        return FREE
                    if response.status == 429:
                        if C.DEVELOPMENT:
                            print(f'Embedder {server!r} is BUSY')
                        return BUSY
        except KeyboardInterrupt:
            raise
        except (ConnectionRefusedError, ClientConnectorError, asyncio.exceptions.CancelledError):
            pass
        except (asyncio.exceptions.TimeoutError, TimeoutError):
            return BUSY
        except Exception:
            print(f'Failed to check embedder {server!r}:')
            print_exc()

        if C.DEVELOPMENT:
            print(f'Embedder {server!r} is MISSING')
        return MISSING
