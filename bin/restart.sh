#!/bin/bash

if [ -z "$USER" ]; then
  echo "USER environment variable is not set"
  exit 1
fi

. ~/bin/common.sh

if [ -z "$1" ]; then
  echo "$(date -Is): Restarting all services"
  run_for_all $0
  echo "$(date -Is): Done"
  exit 0
fi

set -euo pipefail

bash ~/bin/stop.sh "$@"

if [ "$RESTART_WAIT" -gt 0 ]; then
  echo "$(date -Is): Waiting $RESTART_WAIT seconds before starting it again"
  sleep $RESTART_WAIT
fi

bash ~/bin/start.sh "$@"

exit 0
