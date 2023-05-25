from typing import Iterator, Iterable

from model.document import Document


def find_common_base_dir(paths: Iterable[str]) -> str:
    dir_sets = []
    for path in paths:
        for i, dirname in enumerate(path.split('/')[:-1]):
            if i == len(dir_sets):
                dir_sets.append(set())
            dir_sets[i].add(dirname)

    print(dir_sets)

    common = [dir_set for dir_set in dir_sets if len(dir_set) == 1]
    if not common:
        return ''

    return '/'.join(next(iter(dir_set)) for dir_set in common) + '/'


def remove_common_base_dir(common_base_dir: str, documents: Iterable[Document]) -> Iterator[Document]:
    if not common_base_dir:
        yield from documents
    else:
        strip_len = len(common_base_dir)
        for doc in documents:
            doc.path = doc.path[strip_len:]
            yield doc
