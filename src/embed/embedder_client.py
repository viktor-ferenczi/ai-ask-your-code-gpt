import asyncio
import json
import os
import random
import time
from typing import Optional, List

import aiohttp

from common.constants import C
from model.fragment import Fragment

QUERY_EMBEDDERS = os.environ.get('QUERY_EMBEDDERS', 'http://127.0.0.1:40100').split()
STORE_EMBEDDERS = os.environ.get('STORE_EMBEDDERS', 'http://127.0.0.1:40200').split()

EMBEDDER_CHUNK_SIZE = int(os.environ.get('EMBEDDER_CHUNK_SIZE', '128'))


class EmbedderClient:
    def __init__(self, servers: List[str]) -> None:
        self.servers = servers
        self.chunk_size = EMBEDDER_CHUNK_SIZE

    def add_servers(self, servers: List[str]):
        self.servers.extend(servers)

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

        ping_timeout = 0.1
        indices = list(range(len(self.servers)))
        deadline = time.time() + timeout
        while time.time() < deadline:
            random.shuffle(indices)
            for index in indices:
                server = self.servers[index]
                if await self.ping(server, timeout=ping_timeout):
                    return server
            ping_timeout = max(1.0, ping_timeout * 2)
            await asyncio.sleep(ping_timeout)

        return None

    async def ping(self, server: str, *, timeout=1.0) -> bool:
        print(f'Ping: {server}')
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(server, headers={'Accept': 'text/plain'}, timeout=timeout) as response:
                    content = await response.content.read()
                    content = content.decode('utf-8', errors='ignore')
                    if C.DEVELOPMENT and response.status != 200:
                        print(f'Failed to ping embedder {server}: [{response.status}] {content}')
                    return response.status == 200
        except asyncio.TimeoutError:
            pass
        return False
