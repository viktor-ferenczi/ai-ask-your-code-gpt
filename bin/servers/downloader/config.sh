#!/bin/sh

NAME="downloader-$INSTANCE_INDEX"
TITLE="Downloader-$INSTANCE_INDEX"

INSTANCE_COUNT=4

WORKING_DIR="$HOME/src/services"
COMMAND_LINE="/usr/bin/python -O -u downloader.py -$INSTANCE_INDEX-"

if [ "$ENVIRONMENT" == "PRODUCTION" ]; then
  export HTTP_PORT=$((41000 + INSTANCE_INDEX))
else
  export HTTP_PORT=$((41500 + INSTANCE_INDEX))
fi

CANARY="http"
CANARY_URL="http://127.0.0.1:$HTTP_PORT"
CANARY_TIMEOUT=10
