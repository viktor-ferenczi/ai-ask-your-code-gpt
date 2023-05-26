#!/bin/sh

NAME="downloader"
TITLE="Downloader"

WORKING_DIR="$HOME/src/downloader"
COMMAND_LINE="python -O -u downloader.py"

LOG_PATH="$HOME/log/$NAME.log"

HTTP_PORT=40001

CANARY="http"
CANARY_URL="http://127.0.0.1:$HTTP_PORT"
CANARY_TIMEOUT=5

export HTTP_PORT
