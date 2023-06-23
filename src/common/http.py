import hashlib
from typing import Optional, List, Dict, Tuple

import aiohttp

from common.constants import C
from common.text import decode_replace


class DownloadError(Exception):
    pass


class NotModified(Exception):
    pass


async def download_file(url: str, *, headers: Optional[List[Dict[str, str]]] = None, max_size: Optional[int] = None, cached: str = '') -> Tuple[bytes, str]:
    print(f'GET {url}')

    size = 0
    archive = []
    checksum = hashlib.sha256()

    if headers is None:
        headers: Dict[str, str] = C.FAKE_BROWSER_HEADERS

    if cached:
        if (cached.startswith('"') or cached.startswith('W/"')) and cached.endswith('"'):
            headers: Dict[str, str] = headers.copy()
            headers['If-None-Match'] = cached
        else:  # pragma: no cover
            print(f'WARNING: Ignoring invalid cached Etag: {cached}')
            cached = ''

    print('Request headers:')
    for key, value in headers.items():
        print(f'  {key}: {value}')

    etag = ''

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:

                if cached and response.status == 304:
                    print('Response: [304] Not modified')
                    raise NotModified()

                print(f'Response: [{response.status}]')
                for key in response.headers:
                    print(f'  {key}: {response.headers[key]}')
                    if key.lower() == 'etag':
                        etag = response.headers[key]

                if response.status < 200 or response.status >= 400:
                    content = await response.content.read(500)
                    reason = decode_replace(content)
                    raise DownloadError(f'Failed to download {url!r} with HTTP {response.status}: {reason}')

                while 1:
                    chunk: bytes = await response.content.read(32768)
                    if not chunk:
                        break

                    if not etag:
                        checksum.update(chunk)

                    archive.append(chunk)
                    size += len(chunk)

                    if max_size and size > max_size:
                        raise DownloadError(f'Archive at {url!r} is too large. Maximum size: {C.MAX_ARCHIVE_SIZE >> 20}MiB')

    except aiohttp.ClientError as e:
        raise DownloadError(f'Failed to download archive from {url!r}: [{e.__class__.__name__}] {e}')

    data = b''.join(archive)
    assert len(data) == size

    print(f'Downloaded {size} bytes')

    checksum = etag or checksum.hexdigest()
    return data, checksum
