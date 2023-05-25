"""Qdrant based vector project
"""
from typing import List, Optional

from qdrant_client import QdrantClient, grpc
from qdrant_client.conversions.conversion import payload_to_grpc

from model.fragment import Fragment
from model.result import Result


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

    async def store(self, uuids: List[str], embeddings: List[List[float]]):
        if not uuids or not embeddings:
            return
        assert len(uuids) == len(embeddings), (len(uuids), len(embeddings))
        assert len(embeddings[0]) == self.dimensions, (len(embeddings[0]), self.dimensions)

        points = [
            grpc.PointStruct(
                id=grpc.PointId(uuid=uuid),
                vectors=grpc.Vectors(vector=grpc.Vector(data=embedding))
            )
            for uuid, embedding in zip(uuids, embeddings)
        ]

        await self.database.async_grpc_points.Upsert(
            grpc.UpsertPoints(
                collection_name=self.name,
                wait=True,
                points=points
            )
        )

    async def search(self, embedding: List[float], *, limit: int = 10, uuid_filter: Optional[List[str]] = None) -> List[Result]:
        assert len(embedding) == self.dimensions, (len(embedding), self.dimensions)

        point_filter: grpc.Filter = None
        if uuid_filter:
            point_filter = grpc.Filter(should=[grpc.Condition(has_id=grpc.HasIdCondition(has_id=[grpc.PointId(uuid=uuid)])) for uuid in uuid_filter])

        response = await self.database.async_grpc_points.Search(
            grpc.SearchPoints(
                collection_name=self.name,
                vector=embedding,
                filter=point_filter,
                limit=limit
            )
        )

        results = [Result(result.id.uuid, result.score) for result in response.result]
        return results
