import os.path
import re
import sys

sys.setrecursionlimit(10000)


class RX:
    GUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')


class C:
    # Environments
    PRODUCTION = 'PRODUCTION'
    DEVELOPMENT = 'DEVELOPMENT'
    TEST_SUITE = 'TEST_SUITE'

    ENVIRONMENTS = (
        PRODUCTION,
        DEVELOPMENT,
        TEST_SUITE,
    )

    # Current environment
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
    assert ENVIRONMENT in ENVIRONMENTS

    # Environment flags
    IS_PRODUCTION = ENVIRONMENT == PRODUCTION
    IS_DEVELOPMENT = ENVIRONMENT == DEVELOPMENT
    IS_TEST_SUITE = ENVIRONMENT == TEST_SUITE

    # Database
    # postgres://user:password@host:port/database
    DEFAULT_DATABASE_DSN = {
        PRODUCTION: 'postgres://askyourcode:askyourcode@127.0.0.1:5432/askyourcode',
        DEVELOPMENT: 'postgres://askyourcode:askyourcode@127.0.0.1:5432/askyourcode',
        TEST_SUITE: 'postgres://askyourcode:askyourcode@127.0.0.1:5432/askyourcode_test',
    }[ENVIRONMENT]
    DATABASE_DSN = os.environ.get('DATABASE_DSN', DEFAULT_DATABASE_DSN)
    DATABASE_COMMAND_TIMEOUT = None

    # Limits

    # Archive file
    MAX_ARCHIVE_SIZE = 200 << 20
    MAX_TOTAL_SIZE = 200 << 20
    MAX_FILE_SIZE = 1 << 20
    MAX_FILE_COUNT = 100 << 10

    # Task queue
    TASK_TIMEOUT = 300  # s

    # Splitter
    MAX_TOKENS_PER_FRAGMENT = 150

    # Parser
    MAX_FRAGMENTS_PER_DOCUMENT = 1_000_000

    # Summary generation
    MAX_SUMMARY_WIDTH = 80

    # Cleanup
    FIRST_CLEANUP_DELAY: int = 77  # s
    CLEANUP_PERIOD: int = 777  # s

    # Dirs
    SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    DATA_DIR = os.path.normpath(os.environ.get('DATA_DIR', os.path.expanduser('~/.askyourcode')))
    ARCHIVE_SUBDIR_NAME = {
        PRODUCTION: 'archive',
        DEVELOPMENT: 'archive-dev',
        TEST_SUITE: 'archive-test',
    }[ENVIRONMENT]
    ARCHIVE_DIR = os.path.join(DATA_DIR, ARCHIVE_SUBDIR_NAME)

    # HTTP
    FAKE_BROWSER_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    }
