from model.fragment import Fragment

# Parser: PythonParser

f0 = Fragment(uuid='TEST-00',
         path='find_duplicates.py',
         lineno=1,
         depth=1,
         type='dependency',
         name='',
         text='import hashlib',
         tokens=2)

f1 = Fragment(uuid='TEST-01',
         path='find_duplicates.py',
         lineno=2,
         depth=1,
         type='dependency',
         name='',
         text='import os',
         tokens=2)

f2 = Fragment(uuid='TEST-02',
         path='find_duplicates.py',
         lineno=3,
         depth=1,
         type='dependency',
         name='',
         text='from collections import defaultdict',
         tokens=4)

f3 = Fragment(uuid='TEST-03',
         path='find_duplicates.py',
         lineno=3,
         depth=1,
         type='dependency',
         name='',
         text='from collections import defaultdict',
         tokens=4)

f4 = Fragment(uuid='TEST-04',
         path='find_duplicates.py',
         lineno=4,
         depth=1,
         type='dependency',
         name='',
         text='from concurrent.futures import ProcessPoolExecutor',
         tokens=8)

f5 = Fragment(uuid='TEST-05',
         path='find_duplicates.py',
         lineno=4,
         depth=1,
         type='dependency',
         name='',
         text='from concurrent.futures import ProcessPoolExecutor',
         tokens=8)

f6 = Fragment(uuid='TEST-06',
         path='find_duplicates.py',
         lineno=6,
         depth=1,
         type='dependency',
         name='',
         text='from tqdm import tqdm',
         tokens=4)

f7 = Fragment(uuid='TEST-07',
         path='find_duplicates.py',
         lineno=6,
         depth=1,
         type='dependency',
         name='',
         text='from tqdm import tqdm',
         tokens=4)

f8 = Fragment(uuid='TEST-08',
         path='find_duplicates.py',
         lineno=11,
         depth=1,
         type='function',
         name='md5_checksum',
         text='def md5_checksum(file_path):\n'
              '    hasher = hashlib.md5()\n'
              "    with open(file_path, 'rb') as f:\n"
              '        while True:\n'
              '            data = f.read(CHUNK_SIZE)\n'
              '            if not data:\n'
              '                break\n'
              '            hasher.update(data)\n'
              '    return hasher.hexdigest()',
         tokens=58)

f9 = Fragment(uuid='TEST-09',
         path='find_duplicates.py',
         lineno=22,
         depth=1,
         type='class',
         name='Duplicates',
         text='class Duplicates:\n'
              '\n'
              '    def __init__(self, root_dir: str) -> None:\n'
              '        super().__init__()\n'
              '        self.root_dir = root_dir\n'
              '        self.files = []\n'
              '\n'
              '    def collect(self):\n'
              '        files_by_size = defaultdict(list)\n'
              '        files_by_checksum = defaultdict(list)\n'
              '\n'
              '        # Group files by size\n'
              '        for dirpath, _, filenames in os.walk(self.root_dir):\n'
              '            for filename in filenames:\n'
              '                file_path = os.path.join(dirpath, filename)\n'
              '                file_size = os.path.getsize(file_path)\n'
              '                files_by_size[file_size].append(file_path)\n'
              '\n'
              '        total_size = sum(file_size * len(file_list) for file_size, file_list in files_by_size.items() '
              'if len(file_list) > 1)\n'
              '\n'
              '        # Calculate the hash only for groups with more than one file\n',
         tokens=166)

f10 = Fragment(uuid='TEST-10',
         path='find_duplicates.py',
         lineno=43,
         depth=1,
         type='class',
         name='Duplicates',
         text="        with ProcessPoolExecutor() as executor, tqdm(total=total_size, unit='B', unit_scale=True, "
              'desc="Processing files") as pbar:\n'
              '            for file_size, file_list in files_by_size.items():\n'
              '                if len(file_list) > 1:\n'
              '                    file_checksums = list(executor.map(md5_checksum, file_list))\n'
              '                    for file_path, file_checksum in zip(file_list, file_checksums):\n'
              '                        files_by_checksum[file_checksum].append(file_path)\n'
              '                        pbar.update(file_size)\n'
              '\n'
              '        self.files.extend(file_list for file_list in files_by_checksum.values() if len(file_list) > 1)',
         tokens=129)

f11 = Fragment(uuid='TEST-11',
         path='find_duplicates.py',
         lineno=24,
         depth=3,
         type='function',
         name='__init__',
         text='def __init__(self, root_dir: str) -> None:\n'
              '        super().__init__()\n'
              '        self.root_dir = root_dir\n'
              '        self.files = []',
         tokens=32)

f12 = Fragment(uuid='TEST-12',
         path='find_duplicates.py',
         lineno=29,
         depth=3,
         type='function',
         name='collect',
         text='def collect(self):\n'
              '        files_by_size = defaultdict(list)\n'
              '        files_by_checksum = defaultdict(list)\n'
              '\n'
              '        # Group files by size\n'
              '        for dirpath, _, filenames in os.walk(self.root_dir):\n'
              '            for filename in filenames:\n'
              '                file_path = os.path.join(dirpath, filename)\n'
              '                file_size = os.path.getsize(file_path)\n'
              '                files_by_size[file_size].append(file_path)\n'
              '\n'
              '        total_size = sum(file_size * len(file_list) for file_size, file_list in files_by_size.items() '
              'if len(file_list) > 1)\n'
              '\n'
              '        # Calculate the hash only for groups with more than one file\n',
         tokens=128)

f13 = Fragment(uuid='TEST-13',
         path='find_duplicates.py',
         lineno=43,
         depth=3,
         type='function',
         name='collect',
         text="        with ProcessPoolExecutor() as executor, tqdm(total=total_size, unit='B', unit_scale=True, "
              'desc="Processing files") as pbar:\n'
              '            for file_size, file_list in files_by_size.items():\n'
              '                if len(file_list) > 1:\n'
              '                    file_checksums = list(executor.map(md5_checksum, file_list))\n'
              '                    for file_path, file_checksum in zip(file_list, file_checksums):\n'
              '                        files_by_checksum[file_checksum].append(file_path)\n'
              '                        pbar.update(file_size)\n'
              '\n'
              '        self.files.extend(file_list for file_list in files_by_checksum.values() if len(file_list) > 1)',
         tokens=129)

f14 = Fragment(uuid='TEST-14',
         path='find_duplicates.py',
         lineno=33,
         depth=4,
         type='documentation',
         name='',
         text='# Group files by size',
         tokens=5)

f15 = Fragment(uuid='TEST-15',
         path='find_duplicates.py',
         lineno=42,
         depth=4,
         type='documentation',
         name='',
         text='# Calculate the hash only for groups with more than one file',
         tokens=12)

f16 = Fragment(uuid='TEST-16',
         path='find_duplicates.py',
         lineno=54,
         depth=1,
         type='function',
         name='main',
         text='def main():\n'
              '    root_dir = input("Enter the root directory to search for duplicate files: ")\n'
              '\n'
              '    if not os.path.isdir(root_dir):\n'
              '        print("Invalid directory path. Please try again.")\n'
              '        return\n'
              '\n'
              '    duplicates = Duplicates(root_dir)\n'
              '    duplicates.collect()\n'
              '    total_space_saved = 0\n'
              '\n'
              '    if not duplicates.files:\n'
              '        print("No duplicate files found.")\n'
              '        return\n'
              '\n'
              '    print("Duplicate files found:")\n'
              '    for file_list in duplicates.files:\n'
              '        print("Duplicate group:")\n'
              '        first = True\n'
              '        for file_path in file_list:\n'
              '            if not first:\n'
              '                total_space_saved += os.path.getsize(file_path)\n'
              '            else:\n'
              '                first = False\n'
              '            print(f"\\t{file_path}")\n'
              '\n'
              '    print(f"\\nTotal disk space that could be saved by deleting duplicates: {total_space_saved} bytes")',
         tokens=171)

f17 = Fragment(uuid='TEST-17',
         path='find_duplicates.py',
         lineno=55,
         depth=7,
         type='documentation',
         name='',
         text='Enter the root directory to search for duplicate files: ',
         tokens=11)

f18 = Fragment(uuid='TEST-18',
         path='find_duplicates.py',
         lineno=58,
         depth=8,
         type='documentation',
         name='',
         text='Invalid directory path. Please try again.',
         tokens=8)

f19 = Fragment(uuid='TEST-19',
         path='find_duplicates.py',
         lineno=66,
         depth=8,
         type='documentation',
         name='',
         text='No duplicate files found.',
         tokens=5)

f20 = Fragment(uuid='TEST-20',
         path='find_duplicates.py',
         lineno=69,
         depth=6,
         type='documentation',
         name='',
         text='Duplicate files found:',
         tokens=4)

f21 = Fragment(uuid='TEST-21',
         path='find_duplicates.py',
         lineno=80,
         depth=6,
         type='documentation',
         name='',
         text='\\nTotal disk space that could be saved by deleting duplicates: ',
         tokens=13)

f22 = Fragment(uuid='TEST-22',
         path='find_duplicates.py',
         lineno=1,
         depth=0,
         type='summary',
         name='',
         text='  Functions: main md5_checksum\n'
              '  Classes: Duplicates\n'
              '  Methods: __init__ collect\n'
              '  Variables and usages: CHUNK_SIZE ProcessPoolExecutor append collections concurrent data defaultdict '
              'desc dirpath duplicates executor extend file_checksum file_checksums file_list file_path file_size '
              'filename filenames files files_by_checksum files_by_size first futures getsize hasher hashlib hexdigest '
              'input isdir items join open path pbar print read root_dir total total_size total_space_saved tqdm unit '
              'unit_scale update values walk\n',
         tokens=99)

