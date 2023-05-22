#!/bin/bash
set -euo pipefail

. ~/bin/conf-$1.sh

if pgrep -f "$COMMAND_LINE"; then
  echo "$(date -Is): The $NAME server is running"
else
  echo "$(date -Is): The $NAME server is NOT running"
fi

exit 0
