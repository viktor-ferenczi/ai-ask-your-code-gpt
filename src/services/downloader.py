import asyncio
import functools
import os
from traceback import print_exc
from typing import Iterator
from zipfile import BadZipFile, LargeZipFile

from quart import Quart

from common.constants import C
from common.doc import find_common_base_dir
from common.http import download_into_memory, DownloadError, NotModified
from common.server import run_app
from common.timer import timer
from common.tools import sleep_forever
from common.zip_support import extract_verify_documents
from storage import archives
from storage.archives import Archive
from storage.database import Database
from storage.pubsub import ChannelName, PubSub
from storage.scheduler import Scheduler, Operation, THandlerResult, Task, TaskFailed


class Downloader:

    def __init__(self, db: Database, url: str) -> None:
        self.db: Database = db
        self.url: str = url

    async def download_verify(self) -> Archive:
        async with self.db.transaction() as conn:
            archive = await archives.find_by_url(conn, self.url)
            cached_etag = archive.etag if archive is not None else None
            try:
                d = await download_into_memory(self.url, max_size=C.MAX_ARCHIVE_SIZE, cached_etag=cached_etag)
            except NotModified:
                print(f'Not modified, skipping download: {self.url!r}')
                return archive
            except Exception as e:
                print(f'Failed to download archive: {archive!r}')
                print_exc()
                raise DownloadError(f'Failed to download archive: {e}')

            common_base_dir: str = find_common_base_dir(self.__verify(d.body))
            print(f'Common base dir: {common_base_dir!r}')

            if archive is None:
                archive = await archives.find_by_checksum(conn, d.checksum)

            if archive is not None and archive.checksum == d.checksum:
                print(archive)
                print(d)
                assert d.size == archive.size, (d.size, archive.size)
                assert common_base_dir == archive.common_base_dir, (common_base_dir, archive.common_base_dir)
            else:
                archive = await archives.create(conn, d.checksum, d.size, self.url, d.etag, common_base_dir)

            path = archive.path
            dirname = os.path.dirname(path)
            os.makedirs(dirname, exist_ok=True)

            with open(path, 'wb') as f:
                f.write(d.body)

        return archive

    def __verify(self, body: bytes) -> Iterator[str]:
        try:
            doc_count = 0
            for zip_doc in extract_verify_documents(
                    body,
                    max_file_count=C.MAX_FILE_COUNT,
                    max_file_size=C.MAX_FILE_SIZE,
                    max_total_size=C.MAX_TOTAL_SIZE,
                    # supported_extensions=set(parsers.PARSERS_BY_EXTENSION),
                    verify_only=True):
                doc_count += 1
                yield zip_doc.path
        except BadZipFile:
            print(f'Not a ZIP file: {self.url!r}')
            print_exc()
            raise DownloadError(f'Not a ZIP file: {self.url!r}')
        except LargeZipFile:
            print(f'ZIP file is too large: {self.url!r}')
            print_exc()
            raise DownloadError(f'ZIP file is too large: {self.url!r}')
        except Exception:
            print(f'Failed to verify source archive {self.url!r}')
            print_exc()
            raise Exception(f'Failed to verify source archive: {self.url!r}')

        if not doc_count:
            raise DownloadError('The archive does not contain any supported documents')

        print(f'Found {doc_count} files in the archive')


async def download(db: Database, url: str, project_id: int) -> THandlerResult:
    print(f'Downloading {url!r} for project {project_id!r}')
    try:
        downloader = Downloader(db, url)
        with timer(f'Downloaded archive {url!r} for project {project_id!r}'):
            archive: Archive = await downloader.download_verify()
    except asyncio.CancelledError:
        raise TaskFailed('The download was cancelled, please try again in a few seconds')
    except DownloadError as e:
        message = str(e)
        if url.startswith('https://github.com/') and 'HTTP 404: Not Found' in message:
            message += '; Test your URL in a private browser tab without authentication. Private repositories will work at a later time. Authentication is currently not supported by AskYourCode.'
        raise TaskFailed(message)

    pubsub = PubSub(db)
    await pubsub.send(ChannelName.DownloadCompleted.name, url=url)

    return Task.create_pending(Operation.ExtractArchive, archive_cs=archive.checksum, project_id=project_id)


async def worker():
    async with Database.from_dsn(C.DSN) as db:
        scheduler = Scheduler(db)
        scheduler.register_handler(Operation.DownloadArchive, functools.partial(download, db))
        while 1:
            # noinspection PyBroadException
            try:
                async with scheduler.listen():
                    await sleep_forever()
            except Exception:
                print('Unexpected failure:')
                print_exc()


app = Quart(__name__)
workers = [worker]


@app.get('/')
async def canary():
    await asyncio.sleep(0.5)
    return 'OK', 200


def main():
    port = int(os.environ.get('HTTP_PORT', '40000'))
    asyncio.run(run_app(app, *[worker() for worker in workers], debug=C.DEVELOPMENT, host='localhost', port=port))


if __name__ == "__main__":
    main()
