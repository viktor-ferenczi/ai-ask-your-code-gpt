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
  echo "$TITLE: Running"
else
  echo "$TITLE: Not running"
fi

exit 0
