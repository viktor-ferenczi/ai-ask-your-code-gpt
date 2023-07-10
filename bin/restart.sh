#!/bin/bash -l

. ~/bin/common.sh

if [ -z "$1" ]; then
  date -Is
  run_for_all $0
  exit 0
fi

set -euo pipefail

bash ~/bin/stop.sh "$@"

if [ "$RESTART_WAIT" -gt 0 ]; then
  echo "$(date -Is): Waiting $RESTART_WAIT seconds before starting it again"
  sleep $RESTART_WAIT
fi

bash ~/bin/start.sh "$@"
