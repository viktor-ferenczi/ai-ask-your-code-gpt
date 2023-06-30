import asyncio
import functools
import os
from typing import List, Tuple

import asyncpg
from quart import Quart

from common.constants import C
from common.server import run_app
from common.timer import timer
from model.fragment import Fragment
from parsers.registrations import PARSERS_BY_NAME
from storage import documents, fragments
from storage.database import Database
from storage.documents import Document
from storage.scheduler import Scheduler, Operation, THandlerResult


async def index_batch(db: Database, batch: List[Tuple[str, str]]) -> THandlerResult:
    for document_cs, path in batch:
        await index_document(db, document_cs, path)
    return None


async def index_document(db: Database, document_cs: str, path: str) -> None:
    with timer(f'Indexed: {document_cs} {path}', show=C.DEVELOPMENT):
        async with db.connection() as conn:
            document: Document = await documents.find_by_checksum(conn, document_cs)
            if document is None:
                print(f'WARNING: Document is missing when trying to index it: {document_cs}')
                return

            parser_cls = PARSERS_BY_NAME.get(document.doctype)
            if parser_cls is None:
                print(f'WARNING: Cannot find parser class by name {document.doctype}, document: {document_cs}')
                return

            parser = parser_cls()
            for fragment in parser.parse(path, document.body):
                assert isinstance(fragment, Fragment)

                if len(fragment.type) > 24:
                    print(f'WARNING: fragment.type is too long: {fragment.type!r}')
                    print(f'Skipped fragment: {fragment!r}')
                    continue

                if len(fragment.name) > 80:
                    print(f'WARNING: fragment.name is too long: {fragment.name!r}')
                    print(f'Skipped fragment: {fragment!r}')
                    continue

                try:
                    await fragments.create(
                        conn,
                        document_cs,
                        fragment.lineno,
                        fragment.depth,
                        None,
                        fragment.type,
                        True,
                        fragment.type == 'summary',
                        fragment.name,
                        fragment.text)
                except asyncpg.CharacterNotInRepertoireError as e:
                    print(f'WARNING: Failed to store fragment: {e}')
                    print(f'Skipped fragment: {fragment!r}')


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
    main(int(os.environ.get('HTTP_PORT', '40002')))
