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

  if ! check_process "$COMMAND_LINE"; then
    echo "$TITLE: Already stopped"
    continue
  fi

  if pkill -9 -u $UID -f "$COMMAND_LINE"; then
    echo "$TITLE: Stopped"
  else
    echo "$TITLE: Failed to stop"
  fi

  if [ -n "$EXTRA_KILL" ]; then
      pkill -9 -u $UID -f "$EXTRA_KILL"
  fi

done

exit 0
