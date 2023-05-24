import io
from typing import Optional, Set, List

import zipfile
from model.document import Document


def extract_files(archive: bytes, *, max_file_size: Optional[int] = None, max_total_size: Optional[int] = None, supported_extensions: Optional[Set] = None, strip_common_folder: bool = True) -> List[Document]:
    documents: List[Document] = []

    prefix = None
    total_size = 0
    with zipfile.ZipFile(io.BytesIO(archive), 'r') as zf:
        for path in zf.namelist():
            if path.endswith('/'):
                # Directory
                continue

            if supported_extensions:
                ext = path.split('.')[-1]
                if ext not in supported_extensions:
                    print(f'Skipping file due to unsupported extension: {path}')
                    continue

            file_info: zipfile.ZipInfo = zf.getinfo(path)
            file_size = file_info.file_size
            if max_file_size and file_size > max_file_size:
                print(f'Skipping large file of {file_size}B in size, maximum is {max_file_size >> 20}MiB: {path!r}')
                continue

            total_size += file_size
            if max_total_size and total_size > max_total_size:
                raise IOError(f'Extracted archive is too large, maximum is {max_total_size >> 20}MiB')

            data: bytes = zf.read(path)
            documents.append(Document(path, data))

            if prefix is None or len(path) < len(prefix):
                prefix = path

    # Strip common folder from all paths
    if strip_common_folder and prefix:
        if not prefix.endswith('/'):
            prefix = prefix.rsplit('/')[0] + '/'
        if all(filename.startswith(prefix) for filename, text in documents):
            strip_len = len(prefix)
            for doc in documents:
                doc.path = doc.path[strip_len:]

    return documents
