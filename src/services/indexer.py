import asyncio
import functools
import os
from traceback import print_exc

from quart import Quart

from common.constants import C
from common.server import run_app
from common.timer import timer
from common.tools import sleep_forever
from model.fragment import Fragment
from parsers.registrations import PARSERS_BY_NAME
from storage import documents, fragments
from storage.database import Database
from storage.documents import Document
from storage.scheduler import Scheduler, Operation, THandlerResult


async def index(db: Database, document_cs: str, path: str) -> THandlerResult:
    print(f'Indexing: {document_cs} {path}')
    with timer(f'Indexed: {document_cs} {path}'):
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
                await fragments.create(
                    conn,
                    document_cs,
                    fragment.lineno,
                    fragment.depth,
                    None,
                    fragment.category,
                    True,
                    fragment.category == 'summary',
                    fragment.name,
                    fragment.body)


async def worker():
    async with Database.from_dsn(C.DSN) as db:
        scheduler = Scheduler(db)
        scheduler.register_handler(Operation.IndexSource, functools.partial(index, db))
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
