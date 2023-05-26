import asyncio
import io
import os
from traceback import print_exc
from typing import Dict

from quart import Quart, request, Response

import doc_types
from common.constants import C, Msg, RX
from common.zip_support import extract_verify_documents
from common.http import download_file
from common.server import run_app
from common.timer import timer
from project.inventory import Inventory
from project.project import Project


class Downloader:

    def __init__(self, project_id: str, url: str) -> None:
        self.project_id: str = project_id
        self.url: str = url

        self.project = Project(project_id)

    async def download_verify(self):
        with timer(f'Downloaded archive for project {self.project_id!r}'):
            archive = await self.__download()

        await asyncio.sleep(0)

        with timer(f'Verified archive for project {self.project_id!r}'):
            self.__verify(archive)

        with open(self.project.archive_path, 'wb') as f:
            f.write(archive)

        await self.project.create_database()

    async def __download(self) -> bytes:
        try:
            archive: bytes = await download_file(self.url, max_size=C.MAX_ARCHIVE_SIZE)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f'Failed to download archive {self.url!r} for project {self.project_id!r}')
            print_exc()
            raise IOError(f'Failed to download archive {self.url!r}')

        print(f'Downloaded archive of {len(archive)} bytes in size for project {self.project_id!r} from {self.url!r}')
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
            print(f'Failed verify source archive {self.url!r} for project {self.project_id!r}')
            print_exc()
            raise IOError(f'Failed verify source archive: {self.url!r}')

        if not document_count:
            raise IOError(Msg.EmptyArchive)

        print(f'Extracted {document_count} files')


app = Quart(__name__)


@app.get('/')
async def canary():
    return 'OK', 200


@app.post("/download/<string:project_id>")
async def download(project_id: str):
    project_id = project_id.lower()
    if not RX.GUID.match(project_id):
        return Response(response='Invalid project_id, it must be a GUID', status=400)

    body: Dict[str, any] = await request.get_json(force=True)
    url = body.get('url')
    if not url:
        return Response(response='Missing url', status=400)

    with timer(f'Loaded project {project_id!r}'):

        downloader = Downloader(project_id, url)
        await downloader.download_verify()

        inventory = Inventory()
        inventory.register_project(project_id)

    return Response(response='OK', status=200)


def main():
    inventory = Inventory()
    inventory.create_database()

    port = int(os.environ.get('HTTP_PORT', '40001'))
    run_app(app, debug=True, host='localhost', port=port)


if __name__ == "__main__":
    main()
