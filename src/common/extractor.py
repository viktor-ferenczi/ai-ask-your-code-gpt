import io
from typing import Optional, Set, Iterator
from zipfile import ZipInfo, ZipFile

from model.document import Document


def extract_files(archive: bytes,
                  *,
                  max_file_size: Optional[int] = None,
                  max_total_size: Optional[int] = None,
                  supported_extensions: Optional[Set] = None,
                  verify_only: bool = False) -> Iterator[Document]:
    total_size = 0
    with ZipFile(io.BytesIO(archive), 'r') as zf:
        for index, path in enumerate(zf.namelist()):
            if path.endswith('/'):
                # Directory
                continue

            if supported_extensions:
                ext = path.split('.')[-1]
                if ext not in supported_extensions:
                    print(f'Skipping file due to unsupported extension: {path}')
                    continue

            file_info: ZipInfo = zf.getinfo(path)
            file_size = file_info.file_size
            if max_file_size and file_size > max_file_size:
                print(f'Skipping large file of {file_size}B in size, maximum is {max_file_size >> 20}MiB: {path!r}')
                continue

            total_size += file_size
            if max_total_size and total_size > max_total_size:
                raise IOError(f'Extracted archive is too large, maximum is {max_total_size >> 20}MiB')

            if verify_only:
                data: bytes = b''
            else:
                data: bytes = zf.read(path)

            document = Document(path, data)
            yield document
