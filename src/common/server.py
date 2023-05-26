import asyncio
from typing import Coroutine

import quart


def run_app(app: quart.Quart, *coros: Coroutine, **kws):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for coro in coros:
        loop.create_task(coro)
    app.run(loop=loop, **kws)
