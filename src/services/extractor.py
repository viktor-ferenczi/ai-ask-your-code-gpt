import asyncio
import functools
import os
from traceback import print_exc
from typing import Iterator

from quart import Quart

from common.constants import C
from common.doc import remove_common_base_dir
from common.server import run_app
from common.tools import sleep_forever
from common.zip_support import extract_verify_documents, ZipDoc
from parsers.registrations import detect, detect_mime
from storage import archives, documents, files
from storage.archives import Archive
from storage.database import Database
from storage.scheduler import Scheduler, Operation, THandlerResult, Task


async def extract(db: Database, archive_cs: str, project_id: int) -> THandlerResult:
    print(f'Extracting archive {archive_cs!r} for project {project_id!r}')

    async with db.connection() as conn:
        archive: Archive = await archives.find_by_checksum(conn, archive_cs)

    path = os.path.join(C.ARCHIVE_DIR, archive.checksum[:3], archive.checksum)

    iter_zip_doc: Iterator[ZipDoc] = remove_common_base_dir(archive.common_base_dir, extract_verify_documents(path))

    indexing_tasks = []
    async with db.transaction() as conn:

        for zip_doc in iter_zip_doc:
            if not zip_doc.body or len(zip_doc.body) > C.MAX_FILE_SIZE:
                continue

            mime_type = detect_mime(zip_doc.body)
            doc_type = detect(zip_doc.path, mime_type)

            document_cs = None
            if doc_type is not None:
                document = await documents.create(conn, zip_doc.body, doc_type.name)
                document_cs = document.checksum
                task = Task.create_pending(Operation.IndexSource, document_cs=document_cs, path=zip_doc.path)
                indexing_tasks.append(task)

            if project_id:
                await files.create(conn, project_id, zip_doc.path, mime_type, len(zip_doc.body), document_cs, archive_cs)

    return indexing_tasks


async def worker():
    async with Database.from_dsn(C.DSN) as db:
        scheduler = Scheduler(db)
        scheduler.register_handler(Operation.ExtractArchive, functools.partial(extract, db))
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


if __name__ == "__main__":
    port = int(os.environ.get('HTTP_PORT', '40002'))
    asyncio.run(run_app(app, *[worker() for worker in workers], host='localhost', port=port, debug=C.DEVELOPMENT))
