import os.path
import re

RX_GUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

FAKE_BROWSER_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}

# Limits

# Archive file
MAX_ARCHIVE_SIZE = 2 << 20
MAX_FILE_SIZE = 5 << 20
MAX_TOTAL_SIZE = 20 << 20

# Query
MAX_QUERY_LENGTH = 1000
MAX_QUERY_LIMIT = 50

# Embedder
MAX_BATCH_SIZE = 1024
MAX_INSTRUCTION_SIZE = 512
MAX_TEXT_SIZE = 8192

# Dirs
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.environ.get('DATA_DIR', os.path.expanduser('~/.askyourcode'))
PROJECTS_DIR = os.path.join(DATA_DIR, 'projects')

# Environment
PRODUCTION = bool(int(os.environ.get('PRODUCTION', '0')))
DEVELOPMENT = not PRODUCTION


# Error messages
class Message:
    ArchiveIsGoodTryAgainLater = 'The archive is good, but the backend failed to process it. Please try again later.'
    EmptyArchive = 'The archive does not contain any supported documents'
