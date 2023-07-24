import asyncio
from datetime import datetime
from typing import Coroutine

import quart


async def run_app(app: quart.Quart, *coros: Coroutine, **kws):
    print(f'{datetime.utcnow().isoformat()}: Service started')

    tasks = [asyncio.create_task(coro) for coro in coros]

    await app.run_task(**kws)

    for task in tasks:
        task.cancel()
