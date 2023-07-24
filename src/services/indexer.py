import asyncio
import functools
import os
from time import time
from typing import List, Iterable

from quart import Quart

from common.constants import C
from common.core_dump import enable_core_dumps
from common.server import run_app
from common.timer import timer
from common.tools import tiktoken_len
from logic.backend import combine_fragments
from model.fragment import Fragment
from parsers.registrations import PARSERS_BY_NAME
from storage import documents, fragments
from storage.database import Database
from storage.documents import Document
from storage.fragments import Fragment as DbFragment
from storage.scheduler import Scheduler, Operation, THandlerResult, TaskFailed


async def index_batch(db: Database, checksums: List[str], paths: List[str]) -> THandlerResult:
    if not checksums:
        return

    if len(checksums) != len(paths):
        raise TaskFailed('Mismatching number of checksums and paths')

    async with db.connection() as conn:
        docs = await documents.find_many_by_checksums(conn, checksums)

    if len(docs) != len(checksums):
        found = set(doc.checksum for doc in docs)
        missing = set(checksums) - found
        raise TaskFailed(f'Missing documents: {sorted(missing)!r}')

    # Order of docs may not match the order of checksums, so paths need to be looked up
    path_map = {checksum: path for checksum, path in zip(checksums, paths)}

    frags = []
    with timer(f'Indexed {len(docs)} documents'):
        next_sleep = time() + 1.0
        for document in docs:
            frags.extend(index_document(document, path_map[document.checksum]))
            if time() >= next_sleep:
                next_sleep = time() + 1.0
                await asyncio.sleep(0)

    if not frags:
        return None

    await asyncio.sleep(0)
    with timer(f'Stored {len(frags)} fragments of {len(docs)} documents'):
        async with db.transaction() as conn:
            # FIXME: Delete with a single query
            for checksum in checksums:
                await fragments.delete_by_document_cs(conn, checksum)
            await fragments.insert_many(conn, frags)


def index_document(document: Document, path: str) -> Iterable[DbFragment]:
    deadline = time() + C.MAX_DOCUMENT_PARSE_TIME
    with timer(f'Indexed: {document.checksum} {path}', show=C.IS_DEVELOPMENT):
        parser_cls = PARSERS_BY_NAME.get(document.doc_type)
        if parser_cls is None:
            print(f'WARNING: Cannot find parser class by name {document.doc_type}, document: {document.checksum}')
            return

        parser = parser_cls()
        for fragment in combine_fragments(parser.parse(path, document.body), C.MAX_TOKENS_PER_FRAGMENT):
            assert isinstance(fragment, Fragment)

            if len(fragment.type) > 24:
                print(f'WARNING: fragment.type is too long: {fragment.type!r}')
                print(f'Skipped fragment: {fragment!r}')
                continue

            if len(fragment.name) > 160:
                print(f'WARNING: fragment.name is too long: {fragment.name!r}')
                print(f'Skipped fragment: {fragment!r}')
                continue

            yield DbFragment(
                document_cs=document.checksum,
                lineno=fragment.lineno,
                tokens=tiktoken_len(fragment.text),
                depth=fragment.depth,
                parent_id=None,
                category=fragment.type,
                summary=fragment.type == 'summary',
                name=fragment.name,
                body=fragment.text,
            )

            if time() > deadline:
                print(f'WARNING: Document parse time exceeded {C.MAX_DOCUMENT_PARSE_TIME} seconds: document={document.checksum!r}, path={path!r}')
                break


async def worker():
    async with Database.from_dsn(C.DATABASE_DSN) as db:
        scheduler = Scheduler(db)
        await scheduler.listen(Operation.IndexSource, functools.partial(index_batch, db))


app = Quart(__name__)
workers = [worker]


@app.get('/')
async def canary():
    await asyncio.sleep(0)
    return 'OK', 200


def main(http_port: int) -> None:
    asyncio.run(run_app(app, *[worker() for worker in workers], host='localhost', port=http_port, debug=C.DEVELOPMENT))


if __name__ == "__main__":
    enable_core_dumps()
    main(int(os.environ.get('HTTP_PORT', '43000')))
