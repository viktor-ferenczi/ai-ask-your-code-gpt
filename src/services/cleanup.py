import asyncio
import os
from datetime import datetime

from quart import Quart

from common.constants import C
from common.server import run_app
from storage.database import Database


async def cleanup(db: Database):
    removed: bool = False
    for _ in range(C.CLEANUP_MAX_PROJECTS):

        async with db.transaction() as conn:

            project_id = await conn.fetchval("""
                SELECT id
                FROM project
                WHERE accessed < $1
                LIMIT 1
                FOR UPDATE SKIP LOCKED
            """, datetime.utcnow() - C.PROJECT_EXPIRATION_INTERVAL)

            if project_id is None:
                break

            await conn.execute("""
                DELETE FROM file
                WHERE project_id = $1
            """, project_id)

            await conn.execute("""
                DELETE FROM project
                WHERE id = $1
            """, project_id)

            removed = True

    if not removed:
        return

    async with db.transaction() as conn:

        await conn.execute("""
            DELETE FROM document
            WHERE checksum NOT IN (SELECT DISTINCT document_cs FROM file);
        """)

        await conn.execute("""
            DELETE FROM fragment
            WHERE document_cs NOT IN (SELECT checksum FROM document);
        """)


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
