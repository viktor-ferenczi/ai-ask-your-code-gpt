#!/bin/bash
set -euo pipefail

. ~/bin/conf-common.sh
. ~/bin/conf-$1.sh

COMMAND="python -O -u $SCRIPT_PATH"

if pgrep -f "$COMMAND"; then
  echo "$(date -Is): The $NAME server is already running"
  exit 0
fi

echo "$(date -Is): Starting the $NAME server"
cd "$SCRIPT_DIR"
nohup python -O -u "$SCRIPT_PATH" >"$LOG_PATH" 2>&1 &
