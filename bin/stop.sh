#!/bin/bash

. ~/bin/common.sh

if [ -z "$1" ]; then
  run_for_all $0
  exit 0
fi

set -euo pipefail

CONFIG_DIR="$HOME/bin/servers/$1"
. $CONFIG_DIR/config.sh

if ! check_process "$COMMAND_LINE"; then
  echo "$TITLE: Not running"
  exit 0
fi

if pkill -9 -u $UID -f "$COMMAND_LINE"; then
  echo "$TITLE: Stopped"
else
  echo "$TITLE: Failed to stop"
fi

exit 0
