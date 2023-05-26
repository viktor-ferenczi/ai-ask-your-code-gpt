import asyncio
import json
import os
import random
import time
from traceback import print_exc
from typing import Optional, List

import aiohttp
from aiohttp import ClientConnectorError

from common.constants import C
from common.timer import timer
from model.fragment import Fragment

QUERY_EMBEDDERS = os.environ.get('QUERY_EMBEDDERS', 'http://127.0.0.1:40100').split()
STORE_EMBEDDERS = os.environ.get('STORE_EMBEDDERS', 'http://127.0.0.1:40200 http://127.0.0.1:40201 http://127.0.0.1:40202').split()

EMBEDDER_CHUNK_SIZE = int(os.environ.get('EMBEDDER_CHUNK_SIZE', '128'))

FREE = 0
BUSY = 1
MISSING = 2


class EmbedderClient:
    def __init__(self, servers: List[str]) -> None:
        self.servers: List[str] = servers
        self.retries: List[float] = [0.0 for _ in servers]
        self.chunk_size: int = EMBEDDER_CHUNK_SIZE

    @property
    def server_count(self):
        return len(self.servers)

    async def embed_fragments(self, fragments: List[Fragment], *, timeout=30.0) -> List[List[float]]:
        data = json.dumps(dict(fragments=[fragment.__dict__ for fragment in fragments]), indent=2)

        server = await self.find_free_server()
        if not server:
            print(f'Configure embedding servers: {self.servers}')
            raise IOError('No embedding server is available')

        async with aiohttp.ClientSession() as session:
            async with session.post(f'{server}/embed/fragments', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
                content = await response.content.read()
                if response.status != 200:
                    raise IOError(f'Failed to embed fragments using embed server: {server}')

        fragment_dicts = json.loads(content.decode('ascii'))
        fragment_embeddings = fragment_dicts['embeddings']
        return fragment_embeddings

    async def embed_query(self, instruction: str, query: str, *, timeout=10.0) -> List[float]:
        if not instruction.strip():
            raise ValueError('Empty instruction')

        if not query.strip():
            raise ValueError('Empty query')

        data = json.dumps(dict(instruction=instruction, query=query), indent=2)

        with timer('Embedding server search'):
            server = await self.find_free_server()

        if not server:
            raise IOError('No embedding server is available')

        async with aiohttp.ClientSession() as session:
            async with session.post(f'{server}/embed/query', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
                content = await response.content.read()
                if response.status != 200:
                    raise IOError(f'Failed to embed fragments using embed server: {server}')

        data = json.loads(content.decode('ascii'))
        query_embedding = data['embedding']
        return query_embedding

    async def find_free_server(self, *, timeout=30.0) -> Optional[str]:
        if not self.servers:
            raise ValueError('No embedding servers configured')

        indices = list(range(len(self.servers)))

        deadline = time.time() + timeout
        while time.time() < deadline:

            random.shuffle(indices)

            for index in indices:
                if self.retries[index] > time.time():
                    continue

                server = self.servers[index]
                status = await self.is_free(server, timeout=0.3)

                if status == FREE:
                    self.retries[index] = time.time() + 0.2
                    return server

                if status == BUSY:
                    self.retries[index] = time.time() + 0.1
                    continue

                self.retries[index] = time.time() + 10.0

            next_event = min(deadline, min(self.retries))
            delay = max(0.0, next_event - time.time())
            await asyncio.sleep(delay)

        return None

    async def is_free(self, server: str, *, timeout=1.0) -> int:
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
        except ConnectionRefusedError:
            pass
        except ClientConnectorError:
            pass
        except asyncio.exceptions.CancelledError:
            pass
        except asyncio.exceptions.TimeoutError:
            pass
        except Exception:
            print(f'Failed to check embedder {server!r}:')
            print_exc()

        if C.DEVELOPMENT:
            print(f'Embedder {server!r} is MISSING')
        return MISSING
