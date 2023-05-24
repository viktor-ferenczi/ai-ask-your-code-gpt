#!/bin/bash
set -euo pipefail

. environment.sh
. ~/bin/conf-$1.sh

function canary {
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

# Running?
if pgrep -f "$COMMAND_LINE" >/dev/null; then

  # Canary check
  for RETRY in 1 2 3 4 5; do
    if canary; then
      exit 0
    fi
    echo "$(date -Is): The $NAME server canary check failed, retry #$RETRY"
    sleep 1
  done

  if canary; then
    exit 0
  fi

  echo "$(date -Is): The $NAME is running, but does not respond. Restarting it now.
  bash ~/bin/restart.sh "$NAME"

else

  echo "$(date -Is): The $NAME is not running. Starting it now.
  bash ~/bin/start.sh "$NAME"

fi

exit 0
