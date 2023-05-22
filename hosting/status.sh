#!/bin/bash
set -euo pipefail

. ~/bin/conf-$1.sh

COMMAND="python -O -u $SCRIPT_PATH"

if pgrep -f "$COMMAND"; then
  echo "$(date -Is): The $NAME server is running"
else
  echo "$(date -Is): The $NAME server is NOT running"
fi

exit 0
