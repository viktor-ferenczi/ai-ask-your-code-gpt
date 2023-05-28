from typing import Iterator, Iterable

from model.document import Document


def find_common_base_dir(paths: Iterable[str]) -> str:
    dir_sets = []
    for path in paths:
        for i, dirname in enumerate(path.split('/')):
            if i == len(dir_sets):
                dir_sets.append(set())
            dir_sets[i].add(dirname)

    common = [dir_set for dir_set in dir_sets if len(dir_set) == 1]
    if not common:
        return ''

    return '/'.join(next(iter(dir_set)) for dir_set in common) + '/'


def remove_common_base_dir(common_base_dir: str, documents: Iterable[Document]) -> Iterator[Document]:
    strip_len = len(common_base_dir)
    for doc in documents:
        doc.path = f'/{doc.path[strip_len:]}'
        yield doc
