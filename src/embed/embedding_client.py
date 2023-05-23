import asyncio
import json
import random
import sys
import time
from typing import Optional, List

import aiohttp

from model.fragment import Fragment

DEVELOPMENT = sys.platform == 'win32'


class EmbeddingClient:
    def __init__(self, servers: List[str]) -> None:
        self.servers = servers

    def add_servers(self, servers: List[str]):
        self.servers.extend(servers)

    async def embed_fragments(self, fragments: List[Fragment], *, timeout=30.0) -> List[List[float]]:
        data = json.dumps(dict(fragments=[fragment.__dict__ for fragment in fragments]), indent=2)

        server = await self.find_free_server()
        if not server:
            raise IOError('No embedding server is available')

        async with aiohttp.ClientSession() as session:
            async with session.post(f'{server}/embed/fragments', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
                content = await response.content.read()
                if response.status != 200:
                    raise IOError(f'Failed to embed fragments using embed server: {server}')

        fragment_dicts = json.loads(content.decode('ascii'))
        fragment_embeddings = fragment_dicts['embeddings']
        return fragment_embeddings

    async def embed_query(self, query: str, *, timeout=10.0) -> List[float]:
        data = json.dumps(dict(query=query), indent=2)

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

    async def find_free_server(self, *, timeout=10.0) -> Optional[str]:
        if not self.servers:
            raise ValueError('No embedding servers configured')

        delay = 0.05
        max_delay = 0.5 * timeout / len(self.servers)
        deadline = time.time() + timeout
        while time.time() < deadline:
            server = random.choice(self.servers)
            if await self.ping(server, timeout=1.0):
                return server
            await asyncio.sleep(delay)
            delay = min(max_delay, delay * 2.0)

        return None

    async def ping(self, server: str, *, timeout=1.0) -> bool:
        print(f'Ping: {server}')
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(server, headers={'Accept': 'text/plain'}, timeout=timeout) as response:
                    content = await response.content.read()
                    content = content.decode('utf-8', errors='ignore')
                    if DEVELOPMENT and response.status != 200:
                        print(f'Ping failed with [{response.status}] {content}')
                    return response.status == 200
        except asyncio.TimeoutError:
            pass
        return False
