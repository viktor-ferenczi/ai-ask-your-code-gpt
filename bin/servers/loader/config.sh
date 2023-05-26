#!/bin/sh

NAME="loader"
TITLE="Loader"

WORKING_DIR="$HOME/src/loader"
COMMAND_LINE="python -O -u loader.py"

LOG_PATH="$HOME/log/$NAME.log"

export HTTP_PORT=40002

CANARY="http"
CANARY_URL="http://127.0.0.1:$HTTP_PORT"
CANARY_TIMEOUT=30

export EMBEDDER_CHUNK_SIZE=128

export QDRANT_LOCATION="localhost"
export QDRANT_HTTP_PORT=6333
export QDRANT_GRPC_PORT=6334
