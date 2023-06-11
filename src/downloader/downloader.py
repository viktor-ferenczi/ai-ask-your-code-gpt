import asyncio
import hashlib
import os
import uuid
from traceback import print_exc
from typing import Dict
from zipfile import BadZipFile, LargeZipFile

from quart import Quart, request, Response

from common.constants import C
from common.http import download_file, DownloadError
from common.server import run_app
from common.timer import timer
from common.zip_support import extract_verify_documents
from project.inventory import Inventory
from project.project import Project


class Downloader:

    def __init__(self, url: str) -> None:
        self.url: str = url
        self.inventory = Inventory()

    async def download_verify(self) -> str:
        with timer(f'Downloaded archive from {self.url!r}'):
            archive = await self.__download()

        checksum = hashlib.sha256(archive).hexdigest()
        project_id = self.inventory.find_project(self.url, checksum)

        if project_id is not None:
            print(f'Archive matches an existing project: {project_id!r}')
            return project_id

        await asyncio.sleep(0)

        with timer(f'Verified archive {self.url!r}'):
            self.__verify(archive)

        await asyncio.sleep(0)

        project_id = str(uuid.uuid4())
        project = Project(project_id)
        with open(project.archive_path, 'wb') as f:
            f.write(archive)

        await project.create_database()

        self.inventory.register_project(project_id, self.url, checksum)

        return project_id

    async def __download(self) -> bytes:
        try:
            archive: bytes = await download_file(self.url, max_size=C.MAX_ARCHIVE_SIZE)
        except KeyboardInterrupt:
            raise
        except DownloadError as e:
            print(str(e))
            raise
        except Exception as e:
            print(f'Failed to download archive {self.url!r}: {e}')
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
                # supported_extensions=set(parsers.PARSERS_BY_EXTENSION),
                verify_only=True
            ))
        except KeyboardInterrupt:
            raise
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

        if not document_count:
            raise DownloadError('The archive does not contain any supported documents')

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

    try:
        with timer(f'Downloaded archive {url!r}'):
            downloader = Downloader(url)
            project_id = await downloader.download_verify()
    except KeyboardInterrupt:
        raise
    except DownloadError as e:
        return Response(response=str(e), status=400)
    except Exception:
        print(f'Unexpected error while trying to download the archive {url!r}:')
        print_exc()
        return Response(response='Unexpected error while trying to download the archive. Please try again later.', status=500)

    return Response(response=project_id, status=200)


def main():
    inventory = Inventory()
    inventory.create_database()

    port = int(os.environ.get('HTTP_PORT', '40001'))
    asyncio.run(run_app(app, debug=C.DEVELOPMENT, host='localhost', port=port))


if __name__ == "__main__":
    main()
