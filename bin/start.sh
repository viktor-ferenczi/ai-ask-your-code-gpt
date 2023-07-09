#!/bin/bash

. ~/bin/common.sh

if [ -z "$1" ]; then
  run_for_all $0
  exit 0
fi

set -euo pipefail

CONFIG_DIR="$HOME/bin/servers/$1"
. $CONFIG_DIR/config.sh

INSTANCE_MAX=$((INSTANCE_COUNT - 1))

for INSTANCE_INDEX in $(seq 0 $INSTANCE_MAX); do

  . $CONFIG_DIR/config.sh

  if check_process "$COMMAND_LINE"; then
    echo "$TITLE: Already running"
    continue
  fi

  TODAY=$(date -I)
  LOG_PATH="${HOME}/log/${NAME}.${TODAY}.log"

  cd "$WORKING_DIR"
  if ($WRAPPER nohup $COMMAND_LINE >>"${LOG_PATH}" 2>&1 &) then
    echo "$TITLE: Started [$HTTP_PORT]"
  else
    echo "$TITLE: Failed to start"
    exit 1
  fi

done

exit 0
