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

    # Query
    MAX_QUERY_LENGTH = 1000
    MAX_QUERY_LIMIT = 100
    MAX_QUERY_PAGE = 100
    MAX_HIT_COUNT = MAX_QUERY_LIMIT * MAX_QUERY_PAGE

    # Embedder
    MAX_BATCH_SIZE = 1024
    MAX_INSTRUCTION_SIZE = 512
    MAX_TEXT_SIZE = 8192

    # Project creation and first search
    MAX_WAIT_TIME_AFTER_DOWNLOAD = 15.0  # s
    MINIMUM_PROGRESS_TO_ALLOW_SEARCH = 20  # %

    # Dirs
    SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    DATA_DIR = os.environ.get('DATA_DIR', os.path.expanduser('~/.askyourcode'))

    # HTTP
    FAKE_BROWSER_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    }

    # Features
    INCLUDE_TOC = False


class Msg:
    # Error messages
    ArchiveIsGoodTryAgainLater = 'The archive is good, but the backend failed to process it. Please try again later.'
    EmptyArchive = 'The archive does not contain any supported documents'
