#!/bin/sh

NAME="Loader"

WORKING_DIR="$HOME/src/loader"
COMMAND_LINE="python -O -u loader.py"

LOG_PATH="$HOME/log/$NAME.log"

HTTP_PORT=40002

CANARY="http"
CANARY_URL="http://127.0.0.1:$HTTP_PORT"
CANARY_TIMEOUT=5

export HTTP_PORT
