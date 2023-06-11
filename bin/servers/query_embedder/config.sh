#!/bin/sh

NAME="query_embedder"
TITLE="Query Embedder"

WORKING_DIR="$HOME/src/embed"
COMMAND_LINE="python -O -u embedder.py query"

LOG_PATH_BASENAME="$HOME/log/$NAME"

export HTTP_PORT=40100

CANARY="http"
CANARY_URL="http://127.0.0.1:$HTTP_PORT"
CANARY_TIMEOUT=10

export EMBEDDER_BATCH_SIZE=1
