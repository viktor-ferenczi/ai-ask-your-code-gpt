[Hit(uuid='0',
     path='/find_duplicates.py',
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
          '        total_size = sum(file_size * len(file_list) for file_size, '
          'file_list in files_by_size.items() if len(file_list) > 1)\n'
          '\n'
          '        # Calculate the hash only for groups with more than one '
          'file\n'
          '        with ProcessPoolExecutor() as executor, '
          "tqdm(total=total_size, unit='B', unit_scale=True, "
          'desc="Processing files") as pbar:\n'
          '            for file_size, file_list in files_by_size.items():\n'
          '                if len(file_list) > 1:\n'
          '                    file_checksums = '
          'list(executor.map(md5_checksum, file_list))\n'
          '                    for file_path, file_checksum in zip(file_list, '
          'file_checksums):\n'
          '                        '
          'files_by_checksum[file_checksum].append(file_path)\n'
          '                        pbar.update(file_size)\n'
          '\n'
          '        self.files.extend(file_list for file_list in '
          'files_by_checksum.values() if len(file_list) > 1)',
     tokens=295,
     score=1.0),
 Hit(uuid='1',
     path='/find_duplicates.py',
     lineno=1,
     depth=1,
     type='dependency',
     name='',
     text='import hashlibimport osfrom collections import defaultdictfrom '
          'collections import defaultdictfrom concurrent.futures import '
          'ProcessPoolExecutorfrom concurrent.futures import '
          'ProcessPoolExecutorfrom tqdm import tqdmfrom tqdm import tqdm',
     tokens=36,
     score=0.8571428571428572),
 Hit(uuid='2',
     path='/find_duplicates.py',
     lineno=33,
     depth=4,
     type='documentation',
     name='',
     text='# Group files by size# Calculate the hash only for groups with more '
          'than one fileEnter the root directory to search for duplicate '
          'files: Invalid directory path. Please try again.No duplicate files '
          'found.Duplicate files found:\\nTotal disk space that could be saved '
          'by deleting duplicates: ',
     tokens=56,
     score=0.7142857142857143),
 Hit(uuid='3',
     path='/find_duplicates.py',
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
     tokens=58,
     score=0.5714285714285714),
 Hit(uuid='4',
     path='/find_duplicates.py',
     lineno=24,
     depth=3,
     type='function',
     name='__init__',
     text='def __init__(self, root_dir: str) -> None:\n'
          '        super().__init__()\n'
          '        self.root_dir = root_dir\n'
          '        self.files = []',
     tokens=32,
     score=0.4285714285714286),
 Hit(uuid='5',
     path='/find_duplicates.py',
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
          '        total_size = sum(file_size * len(file_list) for file_size, '
          'file_list in files_by_size.items() if len(file_list) > 1)\n'
          '\n'
          '        # Calculate the hash only for groups with more than one '
          'file\n'
          '        with ProcessPoolExecutor() as executor, '
          "tqdm(total=total_size, unit='B', unit_scale=True, "
          'desc="Processing files") as pbar:\n'
          '            for file_size, file_list in files_by_size.items():\n'
          '                if len(file_list) > 1:\n'
          '                    file_checksums = '
          'list(executor.map(md5_checksum, file_list))\n'
          '                    for file_path, file_checksum in zip(file_list, '
          'file_checksums):\n'
          '                        '
          'files_by_checksum[file_checksum].append(file_path)\n'
          '                        pbar.update(file_size)\n'
          '\n'
          '        self.files.extend(file_list for file_list in '
          'files_by_checksum.values() if len(file_list) > 1)',
     tokens=257,
     score=0.2857142857142857),
 Hit(uuid='6',
     path='/find_duplicates.py',
     lineno=54,
     depth=1,
     type='function',
     name='main',
     text='def main():\n'
          '    root_dir = input("Enter the root directory to search for '
          'duplicate files: ")\n'
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
          '    print(f"\\nTotal disk space that could be saved by deleting '
          'duplicates: {total_space_saved} bytes")',
     tokens=171,
     score=0.1428571428571429)]