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
        await conn.execute("""
            DELETE FROM file f
            WHERE NOT EXISTS (
                SELECT 1
                FROM project p
                WHERE p.id = f.project_id
            );
            """)
        deleted_file_count = file_count - await files.count(conn)

    if deleted_file_count:
        print(f'Deleted {deleted_file_count} files')

    async with db.transaction() as conn:
        document_count = await documents.count(conn)
        await conn.execute("""
            DELETE FROM document d
            WHERE NOT EXISTS (
                SELECT 1
                FROM file f
                WHERE f.document_cs = d.checksum AND left(f.document_cs, 2) = d.partition_key
            );
            """)
        deleted_document_count = document_count - await documents.count(conn)

    if deleted_document_count:
        print(f'Deleted {deleted_document_count} documents')

    async with db.transaction() as conn:
        fragment_count = await fragments.count(conn)
        await conn.execute("""
            DELETE FROM fragment fr
            WHERE NOT EXISTS (
                SELECT 1
                FROM document d
                WHERE d.checksum = fr.document_cs AND left(d.checksum, 2) = fr.partition_key
            );
            """)
        deleted_fragment_count = fragment_count - await fragments.count(conn)

    if deleted_fragment_count:
        print(f'Deleted {deleted_fragment_count} fragments')

    async with db.transaction() as conn:
        task_count = await conn.fetchval('SELECT COUNT(*) FROM task')

        await conn.execute("""
                DELETE FROM task
                WHERE state = 'completed'
                  AND finished < $1;
            """, datetime.utcnow() - timedelta(days=3))

        deleted_task_count = task_count - await conn.fetchval('SELECT COUNT(*) FROM task')

    if deleted_task_count:
        print(f'Deleted {deleted_task_count} tasks')


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
    await asyncio.sleep(0)
    return 'OK', 200


def main(http_port: int) -> None:
    asyncio.run(run_app(app, *[worker() for worker in workers], host='localhost', port=http_port, debug=C.DEVELOPMENT))


if __name__ == "__main__":
    main(int(os.environ.get('HTTP_PORT', '44000')))
