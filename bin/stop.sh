#!/bin/bash

if [ -z "$USER" ]; then
  echo "USER environment variable is not set"
  exit 1
fi

. ~/bin/common.sh

if [ -z "$1" ]; then
  echo "$(date -Is): Stopping all services"
  run_for_all $0
  echo "$(date -Is): Done"
  exit 0
fi

set -euo pipefail

CONFIG_DIR="$HOME/bin/servers/$1"
. $CONFIG_DIR/config.sh

INSTANCE_MAX=$((INSTANCE_COUNT - 1))

for INSTANCE_INDEX in $(seq 0 $INSTANCE_MAX); do

  . $CONFIG_DIR/config.sh

  PID=$(pgrep -u $UID -f "$COMMAND_LINE" | head -n 1)
  if [ -n "$PID" ]; then
    kill -9 $PID || true
    echo "$TITLE: Stopped"
  else
    echo "$TITLE: Already stopped"
  fi

  if [ -n "$EXTRA_KILL" ]; then
      pkill -9 -u $UID -f "$EXTRA_KILL" || true
  fi

done

exit 0
