#!/bin/bash

if [[ -z "$1" ]]; then
  echo "Usage: $0 server_name"
  exit 1
fi

set -euo pipefail

. ~/bin/conf-$1.sh

if pgrep -f "$COMMAND_LINE" >/dev/null; then
  echo "$(date -Is): The $NAME server is running"
else
  echo "$(date -Is): The $NAME server is NOT running"
fi

exit 0
