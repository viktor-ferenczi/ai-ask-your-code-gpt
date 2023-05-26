#!/bin/bash

. ~/bin/common.sh

if [ -z "$1" ]; then
  run_for_all $0
  exit 0
fi

set -euo pipefail

CONFIG_DIR="$HOME/bin/servers/$1"
. $CONFIG_DIR/config.sh

if ! pgrep -f "$COMMAND_LINE" >/dev/null; then
  exit 0
fi

pkill -f "$COMMAND_LINE"

sleep 1

if pgrep -f "$COMMAND_LINE" >/dev/null; then
  echo "$TITLE: Stopped"
  exit 0
fi

if pkill -9 -f "$COMMAND_LINE"; then
  echo "$TITLE: Killed"
else
  echo "$TITLE: Stopped"
fi

exit 0
