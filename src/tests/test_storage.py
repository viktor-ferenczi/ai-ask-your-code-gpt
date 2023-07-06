import hashlib
import unittest
from datetime import datetime, timedelta
from pprint import pformat

from base_database_test import BaseDatabaseTest
from common.tools import hash_bytes
from storage import archives, documents, files, fragments, projects, properties
from storage.archives import Archive
from storage.schema import VERSION


class TestStorage(BaseDatabaseTest):

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        self.bodies = [
            b'Hello 1',
            b'Hello 2',
            b'Hello 3',
        ]
        self.checksums = [hash_bytes(body) for body in self.bodies]

    async def test_archives(self) -> None:
        async with self.db.transaction() as conn:
            await archives.truncate(conn)
            o: Archive = await archives.create(conn, 'deadbeef' * 8, 1234567, 77, 'https://example.com/abc.zip', 'W/ETag-345344g542g435tg', '/')

            r1 = await archives.find_by_url(conn, o.url)
            self.assertEqual(repr(o), repr(r1))

            r2 = await archives.find_by_checksum(conn, o.checksum)
            self.assertEqual(repr(o), repr(r2))

    async def test_documents(self) -> None:
        async with self.db.transaction() as conn:
            await documents.truncate(conn)

            bodies = self.bodies
            checksums = self.checksums

            docs = [
                await documents.create(conn, checksum, 'text', 'text/plain', body)
                for body, checksum in zip(bodies, checksums)
            ]

            for doc, checksum in zip(docs, checksums):
                self.assertEqual(doc.checksum, checksum)

            r = await documents.find_by_checksum(conn, checksums[0])
            self.assertEqual(pformat(r), pformat(docs[0]))

            r = await documents.find_many_by_checksums(conn, checksums)
            r.sort(key=lambda d: d.body)
            self.assertEqual(len(r), len(checksums))
            self.assertEqual(pformat(r), pformat(docs))

    async def test_files(self) -> None:
        async with self.db.transaction() as conn:
            await files.truncate(conn)

            body = b'Hello World!'
            sha = hashlib.sha256()
            sha.update(body)

            o = await files.create(conn, 42, '/a/b.txt', sha.hexdigest(), None)

            r = await files.find(conn, o.id)
            self.assertEqual(repr(o), repr(r))

    async def test_fragments(self) -> None:
        async with self.db.transaction() as conn:
            await fragments.truncate(conn)

            bodies = self.bodies
            checksums = self.checksums

            frags = [
                await fragments.create(conn, checksum, 1, 0, None, 'doc', False, '', body.decode())
                for body, checksum in zip(bodies, checksums)
            ]

            r = await fragments.query(conn, checksums[0], frags[0].id)
            self.assertEqual(len(r), 1)
            self.assertEqual(r[0].document_cs, frags[0].document_cs)

            await fragments.truncate(conn)

            await fragments.insert_many(conn, frags)
            r = await fragments.list_all_fragments(conn)
            self.assertEqual(len(r), 3)

            for o, i in zip(r, frags):
                self.assertEqual(o.document_cs, i.document_cs)

    async def test_projects(self) -> None:
        async with self.db.transaction() as conn:
            await projects.truncate(conn)

            o = await projects.create(conn, 'user', 'name')

            r = await projects.find(conn, o.id)
            self.assertEqual(repr(o), repr(r))

            r = await projects.find_by_uid_and_name(conn, o.uid, o.name)
            self.assertEqual(repr(o), repr(r))

            accessed_ts = datetime.utcnow() - timedelta(minutes=1)
            await projects.update_accessed(conn, o.id, accessed_ts)
            r = await projects.find(conn, o.id)
            self.assertEqual(r.accessed, accessed_ts)

    async def test_properties(self) -> None:
        async with self.db.transaction() as conn:
            await properties.write(conn, 'Version', 'x')
            version = await properties.read(conn, 'Version')
            self.assertEqual(version, 'x')

            await properties.write(conn, 'Version', VERSION)
            version = await properties.read(conn, 'Version')
            self.assertEqual(version, VERSION)


if __name__ == '__main__':
    unittest.main()
