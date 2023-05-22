import hashlib
import os
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor

from tqdm import tqdm


def md5_checksum(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read the file in 64KB chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


class Duplicates:

    def __init__(self, root_dir: str) -> None:
        super().__init__()
        self.root_dir = root_dir
        self.files = []

    def collect(self):
        files_by_size = defaultdict(list)
        files_by_checksum = defaultdict(list)

        # Group files by size
        for dirpath, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                file_size = os.path.getsize(file_path)
                files_by_size[file_size].append(file_path)

        total_size = sum(file_size * len(file_list) for file_size, file_list in files_by_size.items() if len(file_list) > 1)

        # Calculate the hash only for groups with more than one file
        with ProcessPoolExecutor() as executor, tqdm(total=total_size, unit='B', unit_scale=True, desc="Processing files") as pbar:
            for file_size, file_list in files_by_size.items():
                if len(file_list) > 1:
                    file_checksums = list(executor.map(md5_checksum, file_list))
                    for file_path, file_checksum in zip(file_list, file_checksums):
                        files_by_checksum[file_checksum].append(file_path)
                        pbar.update(file_size)

        self.files.extend(file_list for file_list in files_by_checksum.values() if len(file_list) > 1)


def main():
    root_dir = input("Enter the root directory to search for duplicate files: ")

    if not os.path.isdir(root_dir):
        print("Invalid directory path. Please try again.")
        return

    duplicates = Duplicates(root_dir)
    duplicates.collect()
    total_space_saved = 0

    if not duplicates.files:
        print("No duplicate files found.")
        return

    print("Duplicate files found:")
    for file_list in duplicates.files:
        print("Duplicate group:")
        first = True
        for file_path in file_list:
            if not first:
                total_space_saved += os.path.getsize(file_path)
            else:
                first = False
            print(f"\t{file_path}")

    print(f"\nTotal disk space that could be saved by deleting duplicates: {total_space_saved} bytes")


if __name__ == '__main__':
    main()
