import asyncio
import os
import uuid
from traceback import print_exc
from typing import Dict, Tuple
from zipfile import BadZipFile, LargeZipFile

from quart import Quart, request, Response

from common.constants import C
from common.http import download_file, DownloadError, NotModified
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
        # Find existing project with an archive file (not cleaned yet)
        cached = ''
        project = None
        new_project = True
        project_id = self.inventory.find_project(self.url)
        if project_id:
            project = Project(project_id)
            if os.path.exists(project.archive_path):
                cached = self.inventory.get_archive_checksum(project_id)

        # Download, if an archive found then send Etag (cached)
        with timer(f'Downloaded archive from {self.url!r}'):
            archive, checksum = await self.__download(cached)

        # Read the old cached archive if exists
        if not archive and project and cached and checksum == cached:
            with open(project.archive_path, 'rb') as f:
                archive = f.read()
            new_project = False
        else:
            project_id = self.inventory.find_project(self.url, checksum)
            if project_id is None:
                assert new_project
                project_id = str(uuid.uuid4())
            else:
                new_project = False
                project = Project(project_id)
                if not project.exists:
                    self.inventory.reprocess_project(project_id)

        if not new_project:
            print(f'Archive matches an existing project: {project.project_id!r}')
            self.inventory.touch_project(project_id)

        await asyncio.sleep(0)

        with timer(f'Verified archive {self.url!r}'):
            self.__verify(archive)

        await asyncio.sleep(0)

        project = Project(project_id)
        with open(project.archive_path, 'wb') as f:
            f.write(archive)

        await project.create_database()

        if new_project:
            self.inventory.register_project(project_id, self.url, checksum)

        return project_id

    async def __download(self, cached='') -> Tuple[bytes, str]:
        try:
            archive, checksum = await download_file(self.url, max_size=C.MAX_ARCHIVE_SIZE, cached=cached)
        except KeyboardInterrupt:
            raise
        except NotModified:
            print(f'The archive already downloaded from {self.url!r} has not been modified since, skipping the download')
            return b'', cached
        except DownloadError as e:
            print(str(e))
            raise
        except Exception as e:
            print(f'Failed to download archive {self.url!r}: {e}')
            print_exc()
            raise IOError(f'Failed to download archive {self.url!r}')

        print(f'Downloaded archive of {len(archive)} bytes in size from {self.url!r}')
        return archive, checksum

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
