import hashlib
from dataclasses import dataclass
from time import time
from typing import Optional, List, Dict

import aiohttp

from common.constants import C
from common.text import decode_replace


class DownloadError(Exception):
    pass


class NotModified(Exception):
    pass


@dataclass
class DownloadResult:
    url: str
    etag: str
    size: int
    body: bytes
    checksum: str
    duration: float


async def download_into_memory(url: str, *, headers: Optional[List[Dict[str, str]]] = None, max_size: Optional[int] = None, cached_etag: str = '') -> DownloadResult:
    started = time()

    print(f'GET {url}')

    size = 0
    chunks = []
    checksum = hashlib.sha256()

    if headers is None:
        headers: Dict[str, str] = C.FAKE_BROWSER_HEADERS

    if cached_etag:
        if (cached_etag.startswith('"') or cached_etag.startswith('W/"')) and cached_etag.endswith('"'):
            headers: Dict[str, str] = headers.copy()
            headers['If-None-Match'] = cached_etag
        else:  # pragma: no cover
            print(f'WARNING: Ignoring invalid cached Etag: {cached_etag}')
            cached_etag = ''

    print('Request headers:')
    for key, value in headers.items():
        print(f'  {key}: {value}')

    response_etag = ''
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:

                if cached_etag and response.status == 304:
                    print('Response: [304] Not modified')
                    raise NotModified()

                print(f'Response: [{response.status}]')
                for key in response.headers:
                    print(f'  {key}: {response.headers[key]}')
                    if key.lower() == 'etag':
                        response_etag = response.headers[key]

                if response.status < 200 or response.status >= 400:
                    body = await response.content.read(500)
                    reason = decode_replace(body)
                    raise DownloadError(f'Failed to download {url!r} with HTTP {response.status}: {reason}')

                while 1:
                    chunk: bytes = await response.content.read(32768)
                    if not chunk:
                        break

                    checksum.update(chunk)

                    chunks.append(chunk)
                    size += len(chunk)

                    if max_size and size > max_size:
                        raise DownloadError(f'Archive at {url!r} is too large. Maximum size: {C.MAX_ARCHIVE_SIZE >> 20}MiB')

    except aiohttp.ClientError as e:
        raise DownloadError(f'Failed to download archive from {url!r}: [{e.__class__.__name__}] {e}')

    body = b''.join(chunks)
    assert len(body) == size
    checksum = checksum.hexdigest()

    duration = time() - started
    speed = size / max(1e-3, duration)
    print(f'Downloaded {url!r}, {size / 1048576:.3f}MB in {duration:.3f}s ({speed / 1048576:.3})MB/s')

    return DownloadResult(url, response_etag, size, body, checksum, duration)
