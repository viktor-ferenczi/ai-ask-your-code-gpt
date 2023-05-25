from typing import Optional, List, Dict

import aiohttp

from common.constants import C


async def download_file(url: str, *, headers: Optional[List[Dict[str, str]]] = None, max_size: Optional[int] = None):
    size = 0
    archive = []

    if headers is None:
        headers = C.FAKE_BROWSER_HEADERS

    async with aiohttp.ClientSession(headers=headers) as session:
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
