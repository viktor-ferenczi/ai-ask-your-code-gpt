#!/bin/sh

NAME="Splitter"

WORKING_DIR="$HOME/src/splitter"
COMMAND_LINE="python -O -u splitter.py"

LOG_PATH="$HOME/log/$NAME.log"

HTTP_PORT=40002

CANARY="http"
CANARY_URL="http://127.0.0.1:$HTTP_PORT"
CANARY_TIMEOUT=5

export HTTP_PORT

export EMBEDDER_URLS="http://127.0.0.1:40003"
export EMBEDDER_CHUNK_SIZE=128

export QDRANT_LOCATION="localhost"
export QDRANT_HTTP_PORT=6333
export QDRANT_GRPC_PORT=6334
