from typing import Iterator, Iterable, List

from common.zip_support import ZipDoc


def find_common_base_dir(paths: List[str]) -> str:
    if not paths:
        return ''

    if len(paths) == 1:
        return '/'.join(paths[0].split('/')[:-1])

    common_dirs = paths[0].split('/')[:-1]
    common_dirs_len = len(common_dirs)

    for path in paths[1:]:

        split_path = path.split('/')[:-1]
        for i, a, b in zip(range(common_dirs_len), common_dirs, split_path):
            if a != b:
                del common_dirs[i:]
                common_dirs_len = i
                break

        split_path_len = len(split_path)
        if split_path_len < common_dirs_len:
            common_dirs = common_dirs[:split_path_len]
            common_dirs_len = split_path_len

        if not common_dirs_len:
            break

    return '/'.join(common_dirs)


def remove_common_base_dir(common_base_dir: str, documents: Iterable[ZipDoc]) -> Iterator[ZipDoc]:
    strip_len = len(common_base_dir)
    for doc in documents:
        doc.path = f'/{doc.path[strip_len:].lstrip("/")}'
        yield doc
