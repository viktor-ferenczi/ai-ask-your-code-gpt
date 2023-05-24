#!/bin/sh

NAME="Qdrant"

WORKING_DIR="$HOME/db"
COMMAND_LINE="qdrant"

LOG_PATH="$HOME/log/$NAME.log"

CANARY="none"

export QDRANT_LOCATION=localhost
export QDRANT_HTTP_PORT=6333
export QDRANT_GRPC_PORT=6334
