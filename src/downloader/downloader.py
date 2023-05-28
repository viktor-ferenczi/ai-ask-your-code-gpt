import asyncio
import hashlib
import os
import uuid
from traceback import print_exc
from typing import Dict

from quart import Quart, request, Response

import doc_types
from common.constants import C, Msg
from common.http import download_file
from common.server import run_app
from common.timer import timer
from common.zip_support import extract_verify_documents
from project.inventory import Inventory
from project.project import Project


class Downloader:

    def __init__(self, url: str) -> None:
        self.url: str = url

    async def download_verify(self) -> str:
        with timer(f'Downloaded archive from {self.url!r}'):
            archive = await self.__download()

        checksum = hashlib.sha256(archive).hexdigest()

        inventory = Inventory()
        project_id = inventory.find_project(self.url, checksum)

        if project_id is not None:
            print(f'Archive matches an existing project: {project_id!r}')
            return project_id

        await asyncio.sleep(0)

        with timer(f'Verified archive {self.url!r}'):
            self.__verify(archive)

        await asyncio.sleep(0)

        project_id = str(uuid.uuid4())
        inventory.register_project(project_id, self.url, checksum)

        await asyncio.sleep(0)

        project = Project(project_id)
        with open(project.archive_path, 'wb') as f:
            f.write(archive)

        await project.create_database()

        return project_id

    async def __download(self) -> bytes:
        try:
            archive: bytes = await download_file(self.url, max_size=C.MAX_ARCHIVE_SIZE)
        except KeyboardInterrupt:
            raise
        except Exception:
            print(f'Failed to download archive {self.url!r}')
            print_exc()
            raise IOError(f'Failed to download archive {self.url!r}')

        print(f'Downloaded archive of {len(archive)} bytes in size from {self.url!r}')
        return archive

    def __verify(self, archive: bytes):
        try:
            document_count: int = sum(1 for _ in extract_verify_documents(
                archive,
                max_file_count=C.MAX_FILE_COUNT,
                max_file_size=C.MAX_FILE_SIZE,
                max_total_size=C.MAX_TOTAL_SIZE,
                supported_extensions=doc_types.SUPPORTED_EXTENSIONS,
                verify_only=True
            ))
        except KeyboardInterrupt:
            raise
        except Exception:
            print(f'Failed verify source archive {self.url!r}')
            print_exc()
            raise IOError(f'Failed verify source archive: {self.url!r}')

        if not document_count:
            raise IOError(Msg.EmptyArchive)

        print(f'Extracted {document_count} files')


app = Quart(__name__)


@app.get('/')
async def canary():
    return 'OK', 200


@app.post("/download")
async def download():
    body: Dict[str, any] = await request.get_json(force=True)
    url = body.get('url')
    if not url:
        return Response(response='Missing url', status=400)

    with timer(f'Downloaded archived {url!r}'):
        downloader = Downloader(url)
        project_id = await downloader.download_verify()

    return Response(response=project_id, status=200)


def main():
    inventory = Inventory()
    inventory.create_database()

    port = int(os.environ.get('HTTP_PORT', '40001'))
    asyncio.run(run_app(app, debug=C.DEVELOPMENT, host='localhost', port=port))


if __name__ == "__main__":
    main()
