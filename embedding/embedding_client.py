import json
import random
import time
from typing import Optional, List

import aiohttp

from model.fragment import Fragment


class EmbeddingClient(aiohttp.ClientSession):
    servers: List[str] = []
    rng = random.Random()

    async def embed_fragments(self, fragments: List[Fragment], *, timeout=10.0) -> List[List[float]]:
        data = json.dumps(dict(fragments=[fragment.__dict__ for fragment in fragments]), indent=2)

        server = await self.__find_free_server()

        async with self.post(f'{server}/embed/fragments', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
            content = await response.content.read()
            if response.status != 200:
                raise IOError(f'Failed to embed fragments using embedding server: {server}')

        data = json.loads(content.decode('ascii'))
        fragment_embeddings = data['embeddings']
        return fragment_embeddings

    async def embed_query(self, query: str, *, timeout=10.0) -> List[float]:
        data = json.dumps(dict(query=query), indent=2)

        server = await self.__find_free_server()

        async with self.post(f'{server}/embed/query', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
            content = await response.content.read()
            if response.status != 200:
                raise IOError(f'Failed to embed fragments using embedding server: {server}')

        data = json.loads(content.decode('ascii'))
        query_embedding = data['embedding']
        return query_embedding

    async def __find_free_server(self, *, timeout=10.0) -> Optional[str]:
        if not self.servers:
            raise ValueError('No embedding servers configured')
        deadline = time.time() + timeout
        while time.time() < deadline:
            server = self.rng.choice(self.servers)
            if await self.__ping(server, timeout=1.0):
                return server

        return None

    async def __ping(self, server: str, *, timeout=1.0) -> bool:
        try:
            async with self.get(server, headers={'Accept': 'text/plain'}, timeout=timeout) as response:
                return response.status == 200
        except KeyboardInterrupt:
            raise
        except:
            pass
        return False
