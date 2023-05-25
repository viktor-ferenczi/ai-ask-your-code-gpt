from typing import Optional

import aiohttp

from common import constants as C


async def download_file(url: str, *, max_size: Optional[int] = None):
    size = 0
    archive = []

    async with aiohttp.ClientSession(headers=C.FAKE_BROWSER_HEADERS) as session:
        async with session.get(url) as response:
            while 1:
                chunk = await response.content.read(32768)
                if not chunk:
                    break

                archive.append(chunk)
                size += len(chunk)

                if max_size and size > max_size:
                    raise IOError(f'Archive is too large, the maximum size is {C.MAX_ARCHIVE_SIZE >> 20}MiB')

    return b''.join(archive)
