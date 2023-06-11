#!/bin/bash

. ~/bin/common.sh

if [ -z "$1" ]; then
  run_for_all $0
  exit 0
fi

set -euo pipefail

CONFIG_DIR="$HOME/bin/servers/$1"
. $CONFIG_DIR/config.sh

if check_process "$COMMAND_LINE"; then
  echo "$TITLE: Already running"
  exit 0
fi

TODAY=$(date -I)
LOG_PATH="${LOG_PATH_BASENAME}.${TODAY}.log"

cd "$WORKING_DIR"
nohup $WRAPPER $COMMAND_LINE >>"${LOG_PATH}" 2>&1 &
echo "$TITLE: Started"

exit 0
