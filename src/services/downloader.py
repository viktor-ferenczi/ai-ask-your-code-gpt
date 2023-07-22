from common.reuse_addr import patch_reuse_addr

patch_reuse_addr()

import asyncio
import functools
import os
from traceback import print_exc
from typing import Iterator, List, Tuple
from zipfile import BadZipFile, LargeZipFile

from quart import Quart

from common.constants import C
from common.doc import find_common_base_dir
from common.http import download_into_memory, DownloadError, NotModified
from common.server import run_app
from common.timer import timer
from common.zip_support import extract_verify_documents, ArchiveTooLargeError
from storage import archives
from storage.archives import Archive
from storage.database import Database
from storage.pubsub import ChannelName, PubSub
from storage.scheduler import Scheduler, Operation, THandlerResult, Task, TaskFailed


class Downloader:

    def __init__(self, db: Database, url: str) -> None:
        self.db: Database = db
        self.url: str = url

    async def download_verify(self) -> Tuple[bool, Archive]:
        async with self.db.transaction() as conn:
            archive = await archives.find_by_url(conn, self.url)
            cached_etag = archive.etag if archive is not None else None
            try:
                download_result = await download_into_memory(self.url, max_size=C.MAX_ARCHIVE_SIZE, cached_etag=cached_etag)
            except NotModified:
                print(f'Not modified, skipping download: {self.url!r}')
                assert archive is not None
                return False, archive
            except Exception as e:
                print(f'Failed to download archive: {archive!r}')
                raise DownloadError(f'Failed to download archive: {e}')

            # Different (modified) archive from the same URL?
            if archive is not None and archive.checksum != download_result.checksum:
                archive = None

            # Try to find existing archive by checksum
            if archive is None:
                archive = await archives.find_by_checksum(conn, download_result.checksum)

            # Use the existing archive
            if archive is not None:
                return False, archive

            # New archive, store and request extracting it
            out_count = [0]
            paths = list(self.__verify(download_result.body, out_count))
            common_base_dir: str = find_common_base_dir(paths)
            print(f'Common base dir: {common_base_dir!r}')
            doc_count = out_count[0]

            archive = await archives.create(conn, download_result.checksum, download_result.size, doc_count, self.url[:400], download_result.etag[:160], common_base_dir[:400])

            path = archive.path
            dirname = os.path.dirname(path)
            os.makedirs(dirname, exist_ok=True)

            with open(path, 'wb') as f:
                f.write(download_result.body)

            return True, archive

    def __verify(self, body: bytes, out_count: List[int]) -> Iterator[str]:
        try:
            doc_count = 0
            for zip_doc in extract_verify_documents(
                    body,
                    max_file_count=C.MAX_FILE_COUNT,
                    max_file_size=C.MAX_FILE_SIZE,
                    max_total_size=C.MAX_TOTAL_SIZE,
                    verify_only=True):
                doc_count += 1
                yield zip_doc.path.lstrip('/')
        except BadZipFile:
            print(f'Not a ZIP file: {self.url!r}')
            raise DownloadError(f'Not a ZIP file: {self.url!r}')
        except LargeZipFile:
            print(f'ZIP file is too large: {self.url!r}')
            raise DownloadError(f'ZIP file is too large: {self.url!r}')
        except ArchiveTooLargeError as e:
            print(f'{e}: {self.url!r}')
            raise DownloadError(f'{e}: {self.url!r}')
        except Exception:
            print(f'Failed to verify source archive {self.url!r}')
            print_exc()
            raise Exception(f'Failed to verify source archive: {self.url!r}')

        if not doc_count:
            raise DownloadError('The archive does not contain any supported documents')

        print(f'Found {doc_count} files in the archive')
        out_count[0] = doc_count


async def download(db: Database, url: str, project_id: int) -> THandlerResult:
    try:
        downloader = Downloader(db, url)
        with timer(f'Downloaded and verified archive {url!r} for project {project_id!r}'):
            new, archive = await downloader.download_verify()
    except DownloadError as e:
        message = str(e)
        if url.startswith('https://github.com/') and 'HTTP 404: Not Found' in message:
            message += '; Test your URL in a private browser tab without authentication. Private repositories will work at a later time. Authentication is currently not supported by AskYourCode.'
        raise TaskFailed(message)

    if new:
        print(f'Downloaded new archive {archive.checksum!r} for project {project_id!r}, requesting extraction')
    else:
        print(f'Reusing existing archive {archive.checksum!r} for project {project_id!r}, already extracted')

    pubsub = PubSub(db)
    await pubsub.send(ChannelName.DownloadCompleted.name, url=url)

    followup = Task.create_pending(Operation.ExtractArchive, archive_cs=archive.checksum, project_id=project_id)
    return followup


async def worker():
    async with Database.from_dsn(C.DATABASE_DSN) as db:
        scheduler = Scheduler(db)
        await scheduler.listen(Operation.DownloadArchive, functools.partial(download, db))


app = Quart(__name__)
workers = [worker]


@app.get('/')
async def canary():
    await asyncio.sleep(0)
    return 'OK', 200


def main():
    port = int(os.environ.get('HTTP_PORT', '41000'))
    asyncio.run(run_app(app, *[worker() for worker in workers], debug=C.DEVELOPMENT, host='localhost', port=port))


if __name__ == "__main__":
    main()
