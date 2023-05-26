#!/bin/sh

NAME="store_embedder"
TITLE="Store Embedder"

WORKING_DIR="$HOME/src/embed"
COMMAND_LINE="python -O -u embedder.py store"

LOG_PATH="$HOME/log/$NAME.log"

export HTTP_PORT=40200

CANARY="http"
CANARY_URL="http://127.0.0.1:$HTTP_PORT"
CANARY_TIMEOUT=15

export EMBEDDER_BATCH_SIZE=32
