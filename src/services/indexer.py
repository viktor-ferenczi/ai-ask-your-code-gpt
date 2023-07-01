import asyncio
import functools
import os
from typing import List, Tuple, Iterator

from asyncpg import Connection
from quart import Quart

from common.constants import C
from common.server import run_app
from common.timer import timer
from common.tools import tiktoken_len
from model.fragment import Fragment
from parsers.registrations import PARSERS_BY_NAME
from storage import documents, fragments
from storage.database import Database
from storage.documents import Document
from storage.fragments import Fragment as DbFragment
from storage.scheduler import Scheduler, Operation, THandlerResult


async def index_batch(db: Database, batch: List[Tuple[str, str]]) -> THandlerResult:
    with timer(f'Indexed {len(batch)} documents'):
        async with db.connection() as conn:
            for document_cs, path in batch:
                await index_document(conn, document_cs, path)
    return None


async def index_document(conn: Connection, document_cs: str, path: str) -> None:
    with timer(f'Indexed: {document_cs} {path}', show=C.DEVELOPMENT):
        document: Document = await documents.find_by_checksum(conn, document_cs)
        if document is None:
            print(f'WARNING: Document is missing when trying to index it: {document_cs}')
            return

        parser_cls = PARSERS_BY_NAME.get(document.doc_type)
        if parser_cls is None:
            print(f'WARNING: Cannot find parser class by name {document.doc_type}, document: {document_cs}')
            return

        def iter_fragments() -> Iterator[DbFragment]:
            parser = parser_cls()
            for fragment in parser.parse(path, document.body):
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
                    document_cs=document_cs,
                    lineno=fragment.lineno,
                    tokens=tiktoken_len(fragment.text),
                    depth=fragment.depth,
                    parent_id=None,
                    category=fragment.type,
                    definition=True,
                    summary=fragment.type == 'summary',
                    name=fragment.name,
                    body=fragment.text,
                )

        await fragments.insert_many(conn, iter_fragments())


async def worker():
    async with Database.from_dsn(C.DSN) as db:
        scheduler = Scheduler(db)
        await scheduler.listen(Operation.IndexSource, functools.partial(index_batch, db))


app = Quart(__name__)
workers = [worker]


@app.get('/')
async def canary():
    await asyncio.sleep(0.5)
    return 'OK', 200


def main(http_port: int) -> None:
    asyncio.run(run_app(app, *[worker() for worker in workers], host='localhost', port=http_port, debug=C.DEVELOPMENT))


if __name__ == "__main__":
    main(int(os.environ.get('HTTP_PORT', '43000')))
