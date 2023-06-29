import hashlib
import unittest

from base_storage_test import BaseStorageTest
from storage import archives, documents, files, fragments, projects, properties, usages
from storage.archives import Archive
from storage.schema import VERSION


class TestStorage(BaseStorageTest):

    async def test_archives(self) -> None:
        async with self.db.transaction() as conn:
            await archives.truncate(conn)
            o: Archive = await archives.create(conn, 'deadbeef', '/archives/abc.zip', 42, 'https://example.com/abc.zip')

            r1 = await archives.find_by_url(conn, o.url)
            self.assertEqual(repr(o), repr(r1))

            r2 = await archives.find_by_hash(conn, o.hash)
            self.assertEqual(repr(o), repr(r2))

    async def test_documents(self) -> None:
        async with self.db.transaction() as conn:
            await documents.truncate(conn)

            body = 'Hello World!'
            sha = hashlib.sha256()
            sha.update(body.encode())

            o = await documents.create(conn, body, 'text')
            self.assertEqual(o.hash, sha.hexdigest())

            r = await documents.find(conn, o.hash)
            self.assertEqual(repr(o), repr(r))

    async def test_files(self) -> None:
        async with self.db.transaction() as conn:
            await files.truncate(conn)

            body = 'Hello World!'
            sha = hashlib.sha256()
            sha.update(body.encode())

            o = await files.create(conn, 42, '/a/b.txt', 'text/plain', len(body), sha.hexdigest(), None)

            r = await files.find(conn, o.id)
            self.assertEqual(repr(o), repr(r))

    async def test_fragments(self) -> None:
        async with self.db.transaction() as conn:
            await fragments.truncate(conn)

            body = 'Hello World!'
            sha = hashlib.sha256()
            sha.update(body.encode())

            o = await fragments.create(conn, sha.hexdigest(), 0, 1, 0, None, 'doc', False, False, '', body)

            r = await fragments.query(conn, sha.hexdigest(), 0)
            self.assertEqual(len(r), 1)
            self.assertEqual(repr(o), repr(r[0]))

            r = await fragments.query(conn, sha.hexdigest(), 7)
            self.assertEqual(len(r), 0)

    async def test_projects(self) -> None:
        async with self.db.transaction() as conn:
            await projects.truncate(conn)

            o = await projects.create(conn, 'user', 'name')

            r = await projects.find(conn, o.id)
            self.assertEqual(repr(o), repr(r))

    async def test_properties(self) -> None:
        async with self.db.transaction() as conn:
            await properties.write(conn, 'Version', 'x')
            version = await properties.read(conn, 'Version')
            self.assertEqual(version, 'x')

            await properties.write(conn, 'Version', VERSION)
            version = await properties.read(conn, 'Version')
            self.assertEqual(version, VERSION)

    async def test_usages(self) -> None:
        async with self.db.transaction() as conn:
            await usages.truncate(conn)

            o = await usages.create(conn, 42, 101, 11, 102, 12)

            r = await usages.find_usages(conn, 42, 101, 11)
            self.assertEqual(len(r), 1)
            self.assertEqual(repr([o]), repr(r))

            r = await usages.find_definitions(conn, 42, 102, 12)
            self.assertEqual(len(r), 1)
            self.assertEqual(repr([o]), repr(r))

            r = await usages.find_usages(conn, 42, 101, 13)
            self.assertEqual(len(r), 0)

            r = await usages.find_definitions(conn, 42, 103, 12)
            self.assertEqual(len(r), 0)


if __name__ == '__main__':
    unittest.main()
