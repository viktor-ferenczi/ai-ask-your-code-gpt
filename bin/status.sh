#!/bin/bash

if [ -z "$USER" ]; then
  echo "USER environment variable is not set"
  exit 1
fi

. ~/bin/common.sh

if [ -z "$1" ]; then
  echo "$(date -Is): Service status check"
  run_for_all $0
  echo "$(date -Is): Done $0"
  exit 0
fi

set -euo pipefail

CONFIG_DIR="$HOME/bin/servers/$1"
. $CONFIG_DIR/config.sh

INSTANCE_MAX=$((INSTANCE_COUNT - 1))

for INSTANCE_INDEX in $(seq 0 $INSTANCE_MAX); do

  . $CONFIG_DIR/config.sh

  if check_process "$COMMAND_LINE"; then
    echo "$TITLE: Running"
  else
    echo "$TITLE: Stopped"
  fi

done

exit 0
