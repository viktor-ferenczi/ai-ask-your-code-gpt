import os.path
import re

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

RX_GUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
