import asyncio
from datetime import datetime
from typing import Coroutine

import quart


async def run_app(app: quart.Quart, *coros: Coroutine, **kws):
    print(f'{datetime.utcnow().isoformat()}: Service started')
    coros = coros + (app.run_task(**kws), )
    done, pending = await asyncio.wait(coros, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        task.result()
    for task in pending:
        task.cancel()
