"""Qdrant based vector database
"""
import asyncio
from typing import List

from qdrant_client import QdrantClient, grpc
from qdrant_client.conversions.conversion import payload_to_grpc

from model.fragment import Fragment
from model.hit import Hit


class Collection:

    def __init__(self, database: QdrantClient, name: str, *, dimensions=768) -> None:
        self.database: QdrantClient = database
        self.name = name
        self.dimensions = dimensions

    async def create(self):
        await self.database.async_grpc_collections.Create(
            grpc.CreateCollection(
                collection_name=self.name,
                vectors_config=grpc.VectorsConfig(
                    params=grpc.VectorParams(size=self.dimensions, distance=grpc.Distance.Dot)
                ),
                timeout=10
            )
        )

    async def delete(self):
        await self.database.async_grpc_collections.Delete(
            grpc.DeleteCollection(
                collection_name=self.name,
                timeout=10
            )
        )

    async def store(self, fragments: List[Fragment], fragment_embeddings: List[List[float]]):
        assert len(fragment_embeddings[0]) == self.dimensions, (len(fragment_embeddings[0]), self.dimensions)

        await self.database.async_grpc_points.Upsert(
            grpc.UpsertPoints(
                collection_name=self.name,
                wait=True,
                points=[
                    grpc.PointStruct(
                        id=grpc.PointId(num=index),
                        vectors=grpc.Vectors(vector=grpc.Vector(data=embedding)),
                        payload=payload_to_grpc(fragment.__dict__),
                    )
                    for index, fragment, embedding in zip(range(len(fragments)), fragments, fragment_embeddings)
                ]
            )
        )

    async def search(self, query_embedding: List[float], limit: int = 10) -> List[Hit]:
        assert len(query_embedding) == self.dimensions, (len(query_embedding), self.dimensions)

        # FIXME: Async does not work!!!
        # query = self.database.grpc_points.Search(
        #     grpc.SearchPoints(
        #         collection_name=self.name,
        #         vector=query_embedding,
        #         limit=limit
        #     )
        # )
        # TypeError: unhashable type: 'SearchResponse'
        # results = await asyncio.wait([query])

        results = self.database.search(
            collection_name=self.name,
            query_vector=query_embedding,
            limit=limit,
            with_payload=True
        )

        hits = [Hit(result.score, Fragment(**result.payload)) for result in results]
        return hits
