"""Qdrant based vector database
"""
from typing import List

from google._upb._message import MessageMapContainer
from qdrant_client import QdrantClient, grpc
from qdrant_client.conversions.conversion import payload_to_grpc
from qdrant_client.grpc import WithPayloadSelector

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

        response = await self.database.async_grpc_points.Search(
            grpc.SearchPoints(
                collection_name=self.name,
                vector=query_embedding,
                limit=limit,
                with_payload=WithPayloadSelector(enable=True)
            )
        )

        hits = [Hit(result.score, fragment_from_message(result.payload)) for result in response.result]
        hits.sort(key=lambda hit: hit.score, reverse=True)
        return hits


def fragment_from_message(message: MessageMapContainer) -> Fragment:
    return Fragment(
        path=message['path'].string_value,
        lineno=message['lineno'].integer_value,
        text=message['text'].string_value,
        name=message['name'].string_value,
    )
