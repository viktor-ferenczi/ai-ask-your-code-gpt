import io
from dataclasses import dataclass
from typing import Optional, Iterator, Union
from zipfile import ZipInfo, ZipFile


def iter_files_from_zip(path: str) -> Iterator[str]:
    with ZipFile(path, 'r') as zf:
        yield from zf.namelist()


@dataclass
class ZipDoc:
    path: str
    body: bytes


class ArchiveTooLargeError(Exception):
    pass


def extract_verify_documents(archive: Union[str, bytes], *, max_file_count: int = None, max_file_size: Optional[int] = None, max_total_size: Optional[int] = None, verify_only: bool = False) -> Iterator[ZipDoc]:
    if isinstance(archive, bytes):
        zip_file = ZipFile(io.BytesIO(archive))
    else:
        zip_file = ZipFile(archive, 'r')

    with zip_file as zf:

        namelist = zf.namelist()
        if max_file_count and len(namelist) >= max_file_count:
            raise ArchiveTooLargeError(f'The archive contains too many files, maximum is {max_file_count}')

        total_size = 0
        for index, path in enumerate(namelist):
            if path.endswith('/'):
                # Directory
                continue

            file_info: ZipInfo = zf.getinfo(path)
            file_size = file_info.file_size
            if max_file_size and file_size > max_file_size:
                continue

            if max_total_size:
                total_size += file_size
                if total_size > max_total_size:
                    raise ArchiveTooLargeError(f'Extracted archive is too large, maximum is {max_total_size >> 20}MiB')

            if verify_only:
                yield ZipDoc(path, b'')
            else:
                yield ZipDoc(path, zf.read(path))
