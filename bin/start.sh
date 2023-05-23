#!/bin/bash
set -euo pipefail

. ~/bin/conf-$1.sh

if pgrep -f "$COMMAND_LINE"; then
  echo "$(date -Is): The $NAME server is already running"
  exit 0
fi

echo "$(date -Is): Starting the $NAME server"
cd "$WORKING_DIR"
. ~/bin/environment.sh
export PYTHONUNBUFFERED=1
nohup authbind --deep $COMMAND_LINE >>"$LOG_PATH" 2>&1 &
