import asyncio
from typing import Coroutine

import quart


async def run_app(app: quart.Quart, *coros: Coroutine, **kws):
    tasks = [app.run_task(**kws)]
    tasks.extend([asyncio.create_task(coro) for coro in coros])
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        task.result()
    for task in pending:
        task.cancel()
