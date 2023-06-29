import io
from dataclasses import dataclass
from typing import Optional, Set, Iterator, Union
from zipfile import ZipInfo, ZipFile


def iter_files_from_zip(path: str) -> Iterator[str]:
    with ZipFile(path, 'r') as zf:
        yield from zf.namelist()


@dataclass
class ZipDoc:
    path: str
    body: bytes


def extract_verify_documents(archive: Union[str, bytes], *, max_file_count: int = None, max_file_size: Optional[int] = None, max_total_size: Optional[int] = None, supported_extensions: Optional[Set] = None, verify_only: bool = False) -> Iterator[ZipDoc]:
    total_size = 0

    if isinstance(archive, bytes):
        zip_file = ZipFile(io.BytesIO(archive))
    else:
        zip_file = ZipFile(archive, 'r')

    with zip_file as zf:

        namelist = zf.namelist()
        if max_file_count and len(namelist) >= max_file_count:
            raise IOError(f'The archive contains too many files, maximum is {max_file_count}')

        for index, path in enumerate(namelist):
            if path.endswith('/'):
                # Directory
                continue

            if supported_extensions:
                ext = path.split('.')[-1]
                if ext not in supported_extensions:
                    # print(f'Skipping file due to unsupported extension: {path}')
                    continue

            file_info: ZipInfo = zf.getinfo(path)
            file_size = file_info.file_size
            if max_file_size and file_size > max_file_size:
                # print(f'Skipping large file of {file_size} bytes in size, maximum is {max_file_size >> 20}MiB: {path!r}')
                continue

            total_size += file_size
            if max_total_size and total_size > max_total_size:
                raise IOError(f'Extracted archive is too large, maximum is {max_total_size >> 20}MiB')

            if verify_only:
                data: bytes = b''
            else:
                data: bytes = zf.read(path)

            document = ZipDoc(path, data)
            yield document
