import os.path
import re
import sys
from datetime import timedelta

sys.setrecursionlimit(10000)


class RX:
    GUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')


class C:
    # Environments
    PRODUCTION = 'PRODUCTION'
    STAGING = 'STAGING'
    DEVELOPMENT = 'DEVELOPMENT'
    TEST_SUITE = 'TEST_SUITE'

    ENVIRONMENTS = (
        PRODUCTION,
        STAGING,
        DEVELOPMENT,
        TEST_SUITE,
    )

    # Current environment
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
    assert ENVIRONMENT in ENVIRONMENTS

    # Environment flags
    IS_PRODUCTION = ENVIRONMENT == PRODUCTION
    IS_STAGING = ENVIRONMENT == STAGING
    IS_DEVELOPMENT = ENVIRONMENT == DEVELOPMENT
    IS_TEST_SUITE = ENVIRONMENT == TEST_SUITE

    # Database
    # postgres://user:password@host:port/database
    DEFAULT_DATABASE_DSN = {
        PRODUCTION: 'postgres://askyourcode_prd:askyourcode_prd@127.0.0.1:5432/askyourcode_prd',
        STAGING: 'postgres://askyourcode_stg:askyourcode_stg@127.0.0.1:5432/askyourcode_stg',
        DEVELOPMENT: 'postgres://askyourcode_dev:askyourcode_dev@127.0.0.1:5432/askyourcode_dev',
        TEST_SUITE: 'postgres://askyourcode_tst:askyourcode_tst@127.0.0.1:5432/askyourcode_tst',
    }[ENVIRONMENT]
    DATABASE_DSN = os.environ.get('DATABASE_DSN', DEFAULT_DATABASE_DSN)
    DATABASE_COMMAND_TIMEOUT = None

    # Plugin
    PLUGIN_NAME = {
        PRODUCTION: 'AskYourCode',
        STAGING: 'AskYourCodeStg',
        DEVELOPMENT: 'AskYourCodeDev',
        TEST_SUITE: 'AskYourCodeTst',
    }[ENVIRONMENT]

    PLUGIN_ID = {
        PRODUCTION: 'askyourcode',
        STAGING: 'askyourcodestg',
        DEVELOPMENT: 'askyourcodedev',
        TEST_SUITE: 'askyourcodetst',
    }[ENVIRONMENT]

    PLUGIN_URL = {
        PRODUCTION: 'https://plugin.askyourcode.ai',
        STAGING: 'http://localhost:55555',
        DEVELOPMENT: 'http://localhost:5555',
        TEST_SUITE: 'http://localhost:5555',
    }[ENVIRONMENT]

    PLUGIN_HTTP_PORT = {
        PRODUCTION: 443,
        STAGING: 55555,
        DEVELOPMENT: 5555,
        TEST_SUITE: 5555,
    }[ENVIRONMENT]

    # Limits

    # Archive file
    MAX_ARCHIVE_SIZE = 200 << 20
    MAX_TOTAL_SIZE = 200 << 20
    MAX_FILE_SIZE = 1 << 20
    MAX_FILE_COUNT = 100 << 10

    # Task queue
    TASK_TIMEOUT = 600  # s

    # Splitter
    MAX_TOKENS_PER_FRAGMENT = 250

    # Parser
    MAX_FRAGMENTS_PER_DOCUMENT = 1_000_000
    MAX_DOCUMENT_PARSE_TIME = 180  # s

    # Summary
    MAX_SUMMARY_WIDTH = 80

    # Search
    MAX_TOKENS_PER_SEARCH_RESULT = 2000
    MAX_TOKENS_PER_SEARCH_RESPONSE = 2000

    # Project
    PROJECT_ACCESS_UPDATE_INTERVAL = timedelta(minutes=30)
    PROJECT_EXPIRATION_INTERVAL = timedelta(days=1) + PROJECT_ACCESS_UPDATE_INTERVAL

    # Cleanup
    FIRST_CLEANUP_DELAY: int = 17  # s
    CLEANUP_PERIOD: int = 777  # s
    CLEANUP_MAX_PROJECTS = 100  # maximum number of projects to clean up per iteration

    # Dirs
    SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    DATA_DIR = os.path.normpath(os.environ.get('DATA_DIR', os.path.expanduser('~/.askyourcode')))
    ARCHIVE_SUBDIR_NAME = {
        PRODUCTION: 'archive',
        STAGING: 'archive-stg',
        DEVELOPMENT: 'archive-dev',
        TEST_SUITE: 'archive-test',
    }[ENVIRONMENT]
    ARCHIVE_DIR = os.path.join(DATA_DIR, ARCHIVE_SUBDIR_NAME)

    # HTTP
    FAKE_BROWSER_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    }
