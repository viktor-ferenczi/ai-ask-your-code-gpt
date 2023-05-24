#!/bin/bash

if [[ -z "$1" ]]; then
  echo "Usage: $0 server_name"
  exit 1
fi

set -euo pipefail

. ~/bin/conf-$1.sh

if pgrep -f "$COMMAND_LINE" >/dev/null; then
  echo "$(date -Is): The $NAME server is already running"
  exit 0
fi

echo "$(date -Is): Starting the $NAME server"

. ~/bin/environment.sh

export PYTHONUNBUFFERED=1

cd "$WORKING_DIR"
nohup authbind --deep $COMMAND_LINE >>"$LOG_PATH" 2>&1 &

echo "$(date -Is): Started the $NAME server"

exit 0
