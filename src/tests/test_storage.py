import hashlib
import unittest

from base_test_case import BaseTestCase
from storage import archives, documents, files, fragments, projects, properties
from storage.archives import Archive
from storage.schema import VERSION


class TestStorage(BaseTestCase):

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

            body = b'Hello World!'
            sha = hashlib.sha256()
            sha.update(body)
            checksum = sha.hexdigest()

            o = await documents.create(conn, checksum, 'text', 'text/plain', body)
            self.assertEqual(o.checksum, sha.hexdigest())

            r = await documents.find_by_checksum(conn, o.checksum)
            self.assertEqual(repr(o), repr(r))

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

            body = b'Hello World!'
            sha = hashlib.sha256()
            sha.update(body)

            o = await fragments.create(conn, sha.hexdigest(), 1, 0, None, 'doc', False, False, '', body.decode())

            r = await fragments.query(conn, sha.hexdigest(), o.id)
            self.assertEqual(len(r), 1)
            self.assertEqual(repr(o), repr(r[0]))

            r = await fragments.query(conn, sha.hexdigest(), o.id + 1)
            self.assertEqual(len(r), 0)

    async def test_projects(self) -> None:
        async with self.db.transaction() as conn:
            await projects.truncate(conn)

            o = await projects.create(conn, 'user', 'name')

            r = await projects.find(conn, o.id)
            self.assertEqual(repr(o), repr(r))

            r = await projects.find_by_uid_and_name(conn, o.uid, o.name)
            self.assertEqual(repr(o), repr(r))

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
