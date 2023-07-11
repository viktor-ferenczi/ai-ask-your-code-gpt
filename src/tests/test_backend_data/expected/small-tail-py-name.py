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
          'file\n',
     tokens=166,
     score=1.0)]