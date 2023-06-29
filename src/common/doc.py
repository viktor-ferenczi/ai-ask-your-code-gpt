from typing import Iterator, Iterable

from common.zip_support import ZipDoc


def find_common_base_dir(paths: Iterable[str]) -> str:
    dir_sets = []
    for path in paths:
        dirs = path.split('/')[:-1]
        for i, dirname in enumerate(dirs):
            if i == len(dir_sets):
                dir_sets.append(set())
            dir_sets[i].add(dirname)
        if len(dir_sets) == len(dirs):
            dir_sets.append(set())
        dir_sets[len(dirs)].add(None)

    common = [dir_set for dir_set in dir_sets if None not in dir_set and len(dir_set) == 1]
    if not common:
        return ''

    return '/'.join(next(iter(dir_set)) for dir_set in common) + '/'


def remove_common_base_dir(common_base_dir: str, documents: Iterable[ZipDoc]) -> Iterator[ZipDoc]:
    strip_len = len(common_base_dir)
    for doc in documents:
        doc.path = f'/{doc.path[strip_len:]}'
        yield doc
