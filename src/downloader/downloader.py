import asyncio
import os
from traceback import print_exc
from typing import Dict, List

import aiohttp
from quart import Quart, request, Response

import common.constants as C
import doc_types
from common import extractor
from common.http import download_file
from common.storage import ArchiveStorage
from common.timer import timer
from model.document import Document

PORT = int(os.environ.get('HTTP_PORT', '40001'))

SPLITTER_PORT = int(os.environ.get('SPLITTER_PORT', '40002'))

SUPPORTED_EXTENSIONS = set(doc_types.DOC_TYPES.keys())


class Downloader:

    def __init__(self, project_id: str, url: str) -> None:
        self.project_id: str = project_id
        self.url: str = url

        self.archive_storage: ArchiveStorage = ArchiveStorage(project_id)

    def download_verify(self):
        with timer(f'Downloaded archive for project {self.project_id!r}'):
            archive = self.__download()

        asyncio.sleep(0)

        files = self.__extract(archive, verify_only=True)
        if not files:
            raise IOError(C.Message.EmptyArchive)

        self.archive_storage.save(archive)

        self.__trigger_processing()

    def __download(self) -> bytes:
        try:
            archive: bytes = await download_file(self.url, max_size=C.MAX_ARCHIVE_SIZE)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f'Failed to download archive {self.url!r} for project {self.project_id!r}')
            print_exc()
            raise IOError(f'Failed to download archive {self.url!r}: {e}')

        print(f'Downloaded archive of {len(archive)}B size for project {self.project_id!r} from {self.url!r}')
        return archive

    def __extract(self, archive: bytes, *, verify_only: bool = False) -> List[Document]:
        try:
            documents = extractor.extract_files(
                archive,
                max_file_size=C.MAX_FILE_SIZE,
                max_total_size=C.MAX_TOTAL_SIZE,
                supported_extensions=SUPPORTED_EXTENSIONS,
                strip_common_folder=True,
                verify_only=verify_only,
                async_sleep_period=100)
        except KeyboardInterrupt:
            raise
        except Exception:
            print(f'Failed extract source archive {self.url!r} for project {self.project_id!r}')
            print_exc()
            raise IOError(f'Failed extract source archive: {self.url!r}')
        print(f'Extracted {len(documents)} files')
        return documents

    def __trigger_processing(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(f'http://127.0.0.1:{SPLITTER_PORT}/project/{self.project_id}') as response:
                    if response.status != 200:
                        raise IOError()
        except KeyboardInterrupt:
            raise
        except Exception:
            print('ERROR: The splitter could not be notified. Is it running?')
            print_exc()
            self.archive_storage.remove()
            raise IOError(C.Message.ArchiveIsGoodTryAgainLater)


app = Quart(__name__)


@app.get('/')
async def canary():
    return Response(response='OK', status=200)


@app.post("/download/<string:project_id>")
async def download(project_id: str):
    project_id = project_id.lower()
    if not C.RX_GUID.match(project_id):
        return Response(response='Invalid project_id, it must be a GUID', status=400)

    body: Dict[str, any] = await request.get_json(force=True)
    url = body.get('url')
    if not url:
        return Response(response='Missing url', status=400)

    with timer(f'Loaded project {project_id!r}'):

        downloader = Downloader(project_id, url)
        downloader.download_verify()

    return Response(response='OK', status=200)


def run():
    app.run(debug=True, host="localhost", port=PORT)


async def run_task():
    await app.run_task(debug=True, host="localhost", port=PORT)


if __name__ == "__main__":
    run()
