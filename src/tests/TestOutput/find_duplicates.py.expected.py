from model.fragment import Fragment

# Parser: PythonParser

f0 = Fragment(uuid='TEST-00',
         path='find_duplicates.py',
         lineno=1,
         depth=0,
         type='module',
         name='',
         text='import hashlib\r\n'
              'import os\r\n'
              'from collections import defaultdict\r\n'
              'from concurrent.futures import ProcessPoolExecutor\r\n'
              '\r\n'
              'from tqdm import tqdm\r\n'
              '\r\n'
              'CHUNK_SIZE = 65536\r\n'
              '\r\n'
              '\r\n'
              'def md5_checksum(file_path):\r\n'
              '    hasher = hashlib.md5()\r\n'
              "    with open(file_path, 'rb') as f:\r\n"
              '        while True:\r\n'
              '            data = f.read(CHUNK_SIZE)\r\n'
              '            if not data:\r\n'
              '                break\r\n'
              '            hasher.update(data)\r\n'
              '    return hasher.hexdigest()\r\n')

f1 = Fragment(uuid='TEST-01',
         path='find_duplicates.py',
         lineno=20,
         depth=0,
         type='module',
         name='',
         text='\r\n\r\nclass Duplicates:\r\n')

f2 = Fragment(uuid='TEST-02',
         path='find_duplicates.py',
         lineno=23,
         depth=0,
         type='module',
         name='',
         text='\r\n'
              '    def __init__(self, root_dir: str) -> None:\r\n'
              '        super().__init__()\r\n'
              '        self.root_dir = root_dir\r\n'
              '        self.files = []\r\n')

f3 = Fragment(uuid='TEST-03',
         path='find_duplicates.py',
         lineno=28,
         depth=0,
         type='module',
         name='',
         text='\r\n'
              '    def collect(self):\r\n'
              '        files_by_size = defaultdict(list)\r\n'
              '        files_by_checksum = defaultdict(list)\r\n'
              '\r\n'
              '        # Group files by size\r\n'
              '        for dirpath, _, filenames in os.walk(self.root_dir):\r\n'
              '            for filename in filenames:\r\n'
              '                file_path = os.path.join(dirpath, filename)\r\n'
              '                file_size = os.path.getsize(file_path)\r\n'
              '                files_by_size[file_size].append(file_path)\r\n'
              '\r\n'
              '        total_size = sum(file_size * len(file_list) for file_size, file_list in files_by_size.items() '
              'if len(file_list) > 1)\r\n'
              '\r\n'
              '        # Calculate the hash only for groups with more than one file\r\n')

f4 = Fragment(uuid='TEST-04',
         path='find_duplicates.py',
         lineno=43,
         depth=0,
         type='module',
         name='',
         text="        with ProcessPoolExecutor() as executor, tqdm(total=total_size, unit='B', unit_scale=True, "
              'desc="Processing files") as pbar:\r\n'
              '            for file_size, file_list in files_by_size.items():\r\n'
              '                if len(file_list) > 1:\r\n'
              '                    file_checksums = list(executor.map(md5_checksum, file_list))\r\n'
              '                    for file_path, file_checksum in zip(file_list, file_checksums):\r\n'
              '                        files_by_checksum[file_checksum].append(file_path)\r\n'
              '                        pbar.update(file_size)\r\n'
              '\r\n'
              '        self.files.extend(file_list for file_list in files_by_checksum.values() if len(file_list) > '
              '1)\r\n')

f5 = Fragment(uuid='TEST-05',
         path='find_duplicates.py',
         lineno=52,
         depth=0,
         type='module',
         name='',
         text='\r\n'
              '\r\n'
              'def main():\r\n'
              '    root_dir = input("Enter the root directory to search for duplicate files: ")\r\n'
              '\r\n'
              '    if not os.path.isdir(root_dir):\r\n'
              '        print("Invalid directory path. Please try again.")\r\n'
              '        return\r\n'
              '\r\n'
              '    duplicates = Duplicates(root_dir)\r\n'
              '    duplicates.collect()\r\n'
              '    total_space_saved = 0\r\n'
              '\r\n'
              '    if not duplicates.files:\r\n'
              '        print("No duplicate files found.")\r\n'
              '        return\r\n'
              '\r\n'
              '    print("Duplicate files found:")\r\n')

f6 = Fragment(uuid='TEST-06',
         path='find_duplicates.py',
         lineno=70,
         depth=0,
         type='module',
         name='',
         text='    for file_list in duplicates.files:\r\n        print("Duplicate group:")\r\n        first = True\r\n')

f7 = Fragment(uuid='TEST-07',
         path='find_duplicates.py',
         lineno=73,
         depth=0,
         type='module',
         name='',
         text='        for file_path in file_list:\r\n'
              '            if not first:\r\n'
              '                total_space_saved += os.path.getsize(file_path)\r\n'
              '            else:\r\n'
              '                first = False\r\n'
              '            print(f"\\t{file_path}")\r\n'
              '\r\n'
              '    print(f"\\nTotal disk space that could be saved by deleting duplicates: {total_space_saved} '
              'bytes")\r\n'
              '\r\n'
              '\r\n'
              "if __name__ == '__main__':\r\n"
              '    main()\r\n')

f8 = Fragment(uuid='TEST-08',
         path='find_duplicates.py',
         lineno=1,
         depth=0,
         type='dependency',
         name='',
         text='import hashlib')

f9 = Fragment(uuid='TEST-09', path='find_duplicates.py', lineno=2, depth=0, type='dependency', name='', text='import os')

f10 = Fragment(uuid='TEST-10',
         path='find_duplicates.py',
         lineno=3,
         depth=0,
         type='dependency',
         name='',
         text='from collections import defaultdict')

f11 = Fragment(uuid='TEST-11',
         path='find_duplicates.py',
         lineno=4,
         depth=0,
         type='dependency',
         name='',
         text='from concurrent.futures import ProcessPoolExecutor')

f12 = Fragment(uuid='TEST-12',
         path='find_duplicates.py',
         lineno=6,
         depth=0,
         type='dependency',
         name='',
         text='from tqdm import tqdm')

f13 = Fragment(uuid='TEST-13',
         path='find_duplicates.py',
         lineno=8,
         depth=0,
         type='variable',
         name='CHUNK_SIZE',
         text='CHUNK_SIZE = 65536')

f14 = Fragment(uuid='TEST-14',
         path='find_duplicates.py',
         lineno=11,
         depth=0,
         type='function',
         name='md5_checksum',
         text='def md5_checksum(file_path):\r\n'
              '    hasher = hashlib.md5()\r\n'
              "    with open(file_path, 'rb') as f:\r\n"
              '        while True:\r\n'
              '            data = f.read(CHUNK_SIZE)\r\n'
              '            if not data:\r\n'
              '                break\r\n'
              '            hasher.update(data)\r\n'
              '    return hasher.hexdigest()')

f15 = Fragment(uuid='TEST-15',
         path='find_duplicates.py',
         lineno=12,
         depth=2,
         type='variable',
         name='hasher',
         text='hasher = hashlib.md5()')

f16 = Fragment(uuid='TEST-16',
         path='find_duplicates.py',
         lineno=15,
         depth=6,
         type='variable',
         name='data',
         text='data = f.read(CHUNK_SIZE)')

f17 = Fragment(uuid='TEST-17',
         path='find_duplicates.py',
         lineno=22,
         depth=0,
         type='class',
         name='Duplicates',
         text='class Duplicates:\r\n')

f18 = Fragment(uuid='TEST-18',
         path='find_duplicates.py',
         lineno=23,
         depth=0,
         type='class',
         name='Duplicates',
         text='\r\n'
              '    def __init__(self, root_dir: str) -> None:\r\n'
              '        super().__init__()\r\n'
              '        self.root_dir = root_dir\r\n'
              '        self.files = []\r\n')

f19 = Fragment(uuid='TEST-19',
         path='find_duplicates.py',
         lineno=28,
         depth=0,
         type='class',
         name='Duplicates',
         text='\r\n'
              '    def collect(self):\r\n'
              '        files_by_size = defaultdict(list)\r\n'
              '        files_by_checksum = defaultdict(list)\r\n'
              '\r\n'
              '        # Group files by size\r\n'
              '        for dirpath, _, filenames in os.walk(self.root_dir):\r\n'
              '            for filename in filenames:\r\n'
              '                file_path = os.path.join(dirpath, filename)\r\n'
              '                file_size = os.path.getsize(file_path)\r\n'
              '                files_by_size[file_size].append(file_path)\r\n'
              '\r\n'
              '        total_size = sum(file_size * len(file_list) for file_size, file_list in files_by_size.items() '
              'if len(file_list) > 1)\r\n'
              '\r\n'
              '        # Calculate the hash only for groups with more than one file\r\n')

f20 = Fragment(uuid='TEST-20',
         path='find_duplicates.py',
         lineno=43,
         depth=0,
         type='class',
         name='Duplicates',
         text="        with ProcessPoolExecutor() as executor, tqdm(total=total_size, unit='B', unit_scale=True, "
              'desc="Processing files") as pbar:\r\n'
              '            for file_size, file_list in files_by_size.items():\r\n'
              '                if len(file_list) > 1:\r\n'
              '                    file_checksums = list(executor.map(md5_checksum, file_list))\r\n'
              '                    for file_path, file_checksum in zip(file_list, file_checksums):\r\n'
              '                        files_by_checksum[file_checksum].append(file_path)\r\n'
              '                        pbar.update(file_size)\r\n'
              '\r\n'
              '        self.files.extend(file_list for file_list in files_by_checksum.values() if len(file_list) > 1)')

f21 = Fragment(uuid='TEST-21',
         path='find_duplicates.py',
         lineno=24,
         depth=2,
         type='function',
         name='__init__',
         text='def __init__(self, root_dir: str) -> None:\r\n'
              '        super().__init__()\r\n'
              '        self.root_dir = root_dir\r\n'
              '        self.files = []')

f22 = Fragment(uuid='TEST-22',
         path='find_duplicates.py',
         lineno=26,
         depth=4,
         type='variable',
         name='self.root_dir',
         text='self.root_dir = root_dir')

f23 = Fragment(uuid='TEST-23',
         path='find_duplicates.py',
         lineno=27,
         depth=4,
         type='variable',
         name='self.files',
         text='self.files = []')

f24 = Fragment(uuid='TEST-24',
         path='find_duplicates.py',
         lineno=29,
         depth=2,
         type='function',
         name='collect',
         text='def collect(self):\r\n'
              '        files_by_size = defaultdict(list)\r\n'
              '        files_by_checksum = defaultdict(list)\r\n'
              '\r\n'
              '        # Group files by size\r\n'
              '        for dirpath, _, filenames in os.walk(self.root_dir):\r\n'
              '            for filename in filenames:\r\n'
              '                file_path = os.path.join(dirpath, filename)\r\n'
              '                file_size = os.path.getsize(file_path)\r\n'
              '                files_by_size[file_size].append(file_path)\r\n'
              '\r\n'
              '        total_size = sum(file_size * len(file_list) for file_size, file_list in files_by_size.items() '
              'if len(file_list) > 1)\r\n'
              '\r\n'
              '        # Calculate the hash only for groups with more than one file\r\n')

f25 = Fragment(uuid='TEST-25',
         path='find_duplicates.py',
         lineno=43,
         depth=2,
         type='function',
         name='collect',
         text="        with ProcessPoolExecutor() as executor, tqdm(total=total_size, unit='B', unit_scale=True, "
              'desc="Processing files") as pbar:\r\n'
              '            for file_size, file_list in files_by_size.items():\r\n'
              '                if len(file_list) > 1:\r\n'
              '                    file_checksums = list(executor.map(md5_checksum, file_list))\r\n'
              '                    for file_path, file_checksum in zip(file_list, file_checksums):\r\n'
              '                        files_by_checksum[file_checksum].append(file_path)\r\n'
              '                        pbar.update(file_size)\r\n'
              '\r\n'
              '        self.files.extend(file_list for file_list in files_by_checksum.values() if len(file_list) > 1)')

f26 = Fragment(uuid='TEST-26',
         path='find_duplicates.py',
         lineno=30,
         depth=4,
         type='variable',
         name='files_by_size',
         text='files_by_size = defaultdict(list)')

f27 = Fragment(uuid='TEST-27',
         path='find_duplicates.py',
         lineno=31,
         depth=4,
         type='variable',
         name='files_by_checksum',
         text='files_by_checksum = defaultdict(list)')

f28 = Fragment(uuid='TEST-28',
         path='find_duplicates.py',
         lineno=36,
         depth=8,
         type='variable',
         name='file_path',
         text='file_path = os.path.join(dirpath, filename)')

f29 = Fragment(uuid='TEST-29',
         path='find_duplicates.py',
         lineno=37,
         depth=8,
         type='variable',
         name='file_size',
         text='file_size = os.path.getsize(file_path)')

f30 = Fragment(uuid='TEST-30',
         path='find_duplicates.py',
         lineno=40,
         depth=4,
         type='variable',
         name='total_size',
         text='total_size = sum(file_size * len(file_list) for file_size, file_list in files_by_size.items() if '
              'len(file_list) > 1)')

f31 = Fragment(uuid='TEST-31',
         path='find_duplicates.py',
         lineno=46,
         depth=10,
         type='variable',
         name='file_checksums',
         text='file_checksums = list(executor.map(md5_checksum, file_list))')

f32 = Fragment(uuid='TEST-32',
         path='find_duplicates.py',
         lineno=54,
         depth=0,
         type='function',
         name='main',
         text='def main():\r\n'
              '    root_dir = input("Enter the root directory to search for duplicate files: ")\r\n'
              '\r\n'
              '    if not os.path.isdir(root_dir):\r\n'
              '        print("Invalid directory path. Please try again.")\r\n'
              '        return\r\n'
              '\r\n'
              '    duplicates = Duplicates(root_dir)\r\n'
              '    duplicates.collect()\r\n'
              '    total_space_saved = 0\r\n'
              '\r\n'
              '    if not duplicates.files:\r\n'
              '        print("No duplicate files found.")\r\n'
              '        return\r\n'
              '\r\n'
              '    print("Duplicate files found:")\r\n')

f33 = Fragment(uuid='TEST-33',
         path='find_duplicates.py',
         lineno=70,
         depth=0,
         type='function',
         name='main',
         text='    for file_list in duplicates.files:\r\n        print("Duplicate group:")\r\n        first = True\r\n')

f34 = Fragment(uuid='TEST-34',
         path='find_duplicates.py',
         lineno=73,
         depth=0,
         type='function',
         name='main',
         text='        for file_path in file_list:\r\n'
              '            if not first:\r\n'
              '                total_space_saved += os.path.getsize(file_path)\r\n'
              '            else:\r\n'
              '                first = False\r\n'
              '            print(f"\\t{file_path}")\r\n'
              '\r\n'
              '    print(f"\\nTotal disk space that could be saved by deleting duplicates: {total_space_saved} bytes")')

f35 = Fragment(uuid='TEST-35',
         path='find_duplicates.py',
         lineno=55,
         depth=2,
         type='variable',
         name='root_dir',
         text='root_dir = input("Enter the root directory to search for duplicate files: ")')

f36 = Fragment(uuid='TEST-36',
         path='find_duplicates.py',
         lineno=61,
         depth=2,
         type='variable',
         name='duplicates',
         text='duplicates = Duplicates(root_dir)')

f37 = Fragment(uuid='TEST-37',
         path='find_duplicates.py',
         lineno=63,
         depth=2,
         type='variable',
         name='total_space_saved',
         text='total_space_saved = 0')

f38 = Fragment(uuid='TEST-38',
         path='find_duplicates.py',
         lineno=72,
         depth=4,
         type='variable',
         name='first',
         text='first = True')

f39 = Fragment(uuid='TEST-39',
         path='find_duplicates.py',
         lineno=77,
         depth=9,
         type='variable',
         name='first',
         text='first = False')

f40 = Fragment(uuid='TEST-40',
         path='find_duplicates.py',
         lineno=1,
         depth=0,
         type='summary',
         name='',
         text='Summary:\n'
              '  Path: find_duplicates.py\n'
              '  Language: Python\n'
              '  Functions: md5_checksum main\n'
              '  Classes: Duplicates\n'
              '  Methods: __init__ collect\n'
              '  Variables: first file_checksums total_size file_path duplicates total_space_saved files_by_size '
              'hasher file_size self.root_dir files_by_checksum CHUNK_SIZE self.files data root_dir\n'
              '  Usages: len os zip filenames open list _ join total append path file_checksum values collections '
              'ProcessPoolExecutor sum defaultdict print __name__ futures files map pbar f dirpath read walk hashlib '
              'unit desc isdir input getsize executor update self concurrent unit_scale md5 str filename file_list '
              'super extend items hexdigest tqdm')

