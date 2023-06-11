from typing import Optional, List, Dict

import aiohttp

from common.constants import C


class DownloadError(Exception):
    pass


async def download_file(url: str, *, headers: Optional[List[Dict[str, str]]] = None, max_size: Optional[int] = None):
    size = 0
    archive = []

    if headers is None:
        headers = C.FAKE_BROWSER_HEADERS

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                while 1:
                    chunk = await response.content.read(32768)
                    if not chunk:
                        break

                    archive.append(chunk)
                    size += len(chunk)

                    if max_size and size > max_size:
                        raise DownloadError(f'Archive at {url!r} is too large. Maximum size: {C.MAX_ARCHIVE_SIZE >> 20}MiB')
    except aiohttp.ClientError as e:
        raise DownloadError(f'Failed to download archive from {url!r}: [{e.__class__.__name__}] {e}')

    return b''.join(archive)
