import asyncio
import os

from quart import Quart

from common.constants import C
from common.server import run_app
from storage.database import Database


async def cleanup(db: Database):
    # TODO: Cleanup tasks, expired projects, files, documents, fragments, logs
    pass


async def worker():
    async with Database.from_dsn(C.DATABASE_DSN) as db:
        await asyncio.sleep(C.FIRST_CLEANUP_DELAY)
        await cleanup(db)
        while 1:
            await asyncio.sleep(C.CLEANUP_PERIOD)
            await cleanup(db)


app = Quart(__name__)
workers = [worker]


@app.get('/')
async def canary():
    await asyncio.sleep(0.5)
    return 'OK', 200


def main(http_port: int) -> None:
    asyncio.run(run_app(app, *[worker() for worker in workers], host='localhost', port=http_port, debug=C.DEVELOPMENT))


if __name__ == "__main__":
    main(int(os.environ.get('HTTP_PORT', '44000')))
