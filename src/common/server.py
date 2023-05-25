import asyncio
from typing import Coroutine

import quart


def run_app(app: quart.Quart, *coros: Coroutine, **kws):
    loop = asyncio.get_event_loop()
    for test in coros:
        loop.create_task(test)
    app.run(loop=loop, **kws)
