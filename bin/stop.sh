#!/bin/bash

if [[ -z "$1" ]]; then
  echo "Usage: $0 server_name"
  exit 1
fi

set -euo pipefail

. ~/bin/conf-$1.sh

if ! pgrep -f "$COMMAND_LINE" >/dev/null; then
  echo "$(date -Is): The $NAME server is not running"
  exit 0
fi

echo "$(date -Is): Stopping the $NAME server"
pkill -f "$COMMAND_LINE"

sleep 1

if pkill -9 -f "$COMMAND_LINE"; then
  echo "$(date -Is): Killed the $NAME server"
else
  echo "$(date -Is): Stopped the $NAME server"
fi

exit 0
