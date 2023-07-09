#!/bin/bash

. ~/bin/common.sh

if [ -z "$1" ]; then
  run_for_all $0
  exit 0
fi

set -euo pipefail

CONFIG_DIR="$HOME/bin/servers/$1"
. $CONFIG_DIR/config.sh

function check_canary {
  case $CANARY in
  http)
    curl -s --max-time ${CANARY_TIMEOUT} ${CANARY_URL} >/dev/null 2>&1
    return $?
    ;;

  none)
    return 0
    ;;
  esac
}

INSTANCE_MAX=$((INSTANCE_COUNT - 1))

GOOD=true
for INSTANCE_INDEX in $(seq 0 $INSTANCE_MAX); do

  . $CONFIG_DIR/config.sh

  if check_process "$COMMAND_LINE"; then
    # Process is running, but verify whether it is functional

    # Canary check
    for RETRY in {1..10}; do
      if check_canary; then
        continue 2
      fi
      echo "$(date -Is): $TITLE canary check failed, retry #$RETRY"
      sleep 2
    done

    if check_canary; then
      continue
    fi

    GOOD=false
    break
  fi

done

if ! $GOOD; then
  echo "$(date -Is): $TITLE is running, but it does not respond. Restarting..."
  bash ~/bin/restart.sh $1
fi

exit 0
