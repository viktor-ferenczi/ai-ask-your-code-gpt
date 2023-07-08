"""Creates or migrates database schema"""
import asyncio

from common.constants import C
from storage.database import Database


async def main():
    async with Database.from_dsn(C.DATABASE_DSN) as db:
        await db.migrate()


if __name__ == '__main__':
    asyncio.run(main())
