#!/bin/bash
set -euo pipefail

. ~/bin/conf-$1.sh

if ! pgrep -f "$COMMAND_LINE"; then
  echo "$(date -Is): The $NAME server is not running"
  exit 0
fi

echo "$(date -Is): Stopping the $NAME server"
pkill -f "$COMMAND_LINE"

for NN in 10 9 8 7 6 5 4 3 2 1; do
  if ! pgrep -f "$COMMAND_LINE"; then
    exit 0
  fi
  echo "Waiting ${NN}"
  sleep 1
done

if pkill -f "$COMMAND_LINE"; then
  echo "Killed"
else
  echo "Stopped"
fi

exit 0
