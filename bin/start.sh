#!/bin/bash

. ~/bin/common.sh

if [ -z "$1" ]; then
  run_for_all $0
  exit 0
fi

set -euo pipefail

CONFIG_DIR="$HOME/bin/servers/$1"
. $CONFIG_DIR/config.sh

if pgrep -f "$COMMAND_LINE" >/dev/null; then
  exit 0
fi

cd "$WORKING_DIR"
nohup authbind --deep $COMMAND_LINE >>"$LOG_PATH" 2>&1 &
echo "$NAME: Started"

exit 0
