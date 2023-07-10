import asyncio
import os
from datetime import datetime, timedelta

from quart import Quart

from common.constants import C
from common.server import run_app
from storage import files, documents, fragments
from storage.database import Database


async def cleanup(db: Database):
    print(f'{datetime.utcnow().isoformat()}: Cleanup')

    async with db.transaction() as conn:
        project_ids = [
            row['id']
            for row in await conn.fetch("""
                    SELECT id
                    FROM project
                    WHERE accessed < $1
                    ORDER BY accessed
                    LIMIT $2
                    FOR UPDATE SKIP LOCKED
                """, datetime.utcnow() - C.PROJECT_EXPIRATION_INTERVAL, C.CLEANUP_MAX_PROJECTS)
        ]

        for project_id in project_ids:
            await conn.execute("""
                    DELETE FROM project
                    WHERE id = $1
                """, project_id)

    if project_ids:
        print(f'Deleted {len(project_ids)} projects')

    async with db.transaction() as conn:
        file_count = await files.count(conn)
        document_count = await documents.count(conn)
        fragment_count = await fragments.count(conn)

        await conn.execute("""
                DELETE FROM file
                WHERE project_id NOT IN (SELECT DISTINCT id FROM project);
            """)

        await conn.execute("""
                DELETE FROM document
                WHERE checksum NOT IN (SELECT DISTINCT document_cs FROM file);
            """)

        await conn.execute("""
                DELETE FROM fragment
                WHERE document_cs NOT IN (SELECT checksum FROM document);
            """)

        deleted_file_count = file_count - await files.count(conn)
        deleted_document_count = document_count - await documents.count(conn)
        deleted_fragment_count = fragment_count - await fragments.count(conn)

    if deleted_file_count or deleted_document_count or deleted_fragment_count:
        print(f'Deleted {deleted_file_count} files, {deleted_document_count} documents, {deleted_fragment_count} fragments')

    async with db.transaction() as conn:
        task_count = await conn.fetchval('SELECT COUNT(*) FROM task')

        await conn.execute("""
                DELETE FROM task
                WHERE state = 'completed'
                  AND finished < $1;
            """, datetime.utcnow() - timedelta(days=3))

        deleted_task_count = await conn.fetchval('SELECT COUNT(*) FROM task') - task_count

    if deleted_task_count:
        print(f'Deleted {deleted_task_count} tasks')

    print()


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
