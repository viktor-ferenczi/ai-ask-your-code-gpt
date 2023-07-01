import asyncio
import functools
import hashlib
import os
from typing import Iterator, List, Tuple

from quart import Quart

from common.constants import C
from common.doc import remove_common_base_dir
from common.server import run_app
from common.timer import timer
from common.zip_support import extract_verify_documents, ZipDoc
from parsers.registrations import detect, detect_mime
from storage import archives, documents, files
from storage.archives import Archive
from storage.database import Database
from storage.scheduler import Scheduler, Operation, THandlerResult, Task


async def extract(db: Database, archive_cs: str, project_id: int) -> THandlerResult:
    indexing_tasks: List[Task] = []

    with timer(f'Extracted archive {archive_cs!r} for project {project_id!r}'):
        async with db.transaction() as conn:
            archive: Archive = await archives.find_by_checksum(conn, archive_cs)

        path = os.path.join(C.ARCHIVE_DIR, archive.checksum[:3], archive.checksum)

        iter_zip_docs: Iterator[ZipDoc] = extract_verify_documents(path, max_file_size=C.MAX_FILE_SIZE)
        iter_zip_docs: Iterator[ZipDoc] = remove_common_base_dir(archive.common_base_dir, iter_zip_docs)

        batch: List[Tuple[str, str]] = []
        total = 0
        doc_count = 0

        max_bytes_per_batch = min(2_000_000, max(100_000, archive.size // os.cpu_count()))
        max_files_per_batch = min(200, max(10, archive.count // (2 * os.cpu_count())))

        def add(size: int, document_cs: str, path: str) -> None:
            nonlocal batch, total
            batch.append((document_cs, path))
            total += size
            if total >= max_bytes_per_batch or len(batch) >= max_files_per_batch:
                store()

        def store() -> None:
            nonlocal batch, total
            if not C.PRODUCTION:
                print(f'Scheduled a batch of {len(batch)} documents ({total >> 10}kB) for indexing')
            task = Task.create_pending(Operation.IndexSource, batch=batch)
            indexing_tasks.append(task)
            batch = []
            total = 0

        async with db.transaction() as conn:

            for zip_doc in iter_zip_docs:
                if not zip_doc.body:
                    continue

                sha = hashlib.sha256()
                sha.update(zip_doc.body)
                document_cs = sha.hexdigest()

                mime_type = detect_mime(zip_doc.body)

                document = await documents.find_by_checksum(conn, document_cs)
                if document is None:

                    doc_type = detect(zip_doc.path, mime_type)
                    if doc_type is not None:
                        document = await documents.create(conn, document_cs, doc_type.name, mime_type, zip_doc.body)
                        add(len(zip_doc.body), document_cs, zip_doc.path)
                        doc_count += 1

                if project_id and document is not None:
                    await files.create(conn, project_id, zip_doc.path[:400], document_cs, archive_cs)

            if batch:
                store()

    print(f'Produced {doc_count} documents and {len(indexing_tasks)} indexing tasks')
    return indexing_tasks


async def worker():
    async with Database.from_dsn(C.DSN) as db:
        scheduler = Scheduler(db)
        await scheduler.listen(Operation.ExtractArchive, functools.partial(extract, db))


app = Quart(__name__)
workers = [worker]


@app.get('/')
async def canary():
    await asyncio.sleep(0.5)
    return 'OK', 200


if __name__ == "__main__":
    port = int(os.environ.get('HTTP_PORT', '40002'))
    asyncio.run(run_app(app, *[worker() for worker in workers], host='localhost', port=port, debug=C.DEVELOPMENT))
