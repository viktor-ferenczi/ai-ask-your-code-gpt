import os.path
import re


class RX:
    GUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')


class C:
    # Environment
    PRODUCTION = bool(int(os.environ.get('PRODUCTION', '0')))
    DEVELOPMENT = not PRODUCTION

    # Limits

    # Archive file
    MAX_ARCHIVE_SIZE = 20 << 20
    MAX_FILE_SIZE = 5 << 20
    MAX_TOTAL_SIZE = 200 << 20
    MAX_FILE_COUNT = MAX_TOTAL_SIZE >> 10

    # Splitter
    MAX_TOKENS_PER_FRAGMENT = 150  # Tokens

    # Embedder
    MAX_BATCH_SIZE = 1024
    MAX_INSTRUCTION_SIZE = 512
    MAX_TEXT_SIZE = 8192

    # Summary generation
    MAX_SUMMARY_WIDTH = 80

    # Dirs
    SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    DATA_DIR = os.path.normpath(os.environ.get('DATA_DIR', os.path.expanduser('~/.askyourcode')))

    # HTTP
    FAKE_BROWSER_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    }
