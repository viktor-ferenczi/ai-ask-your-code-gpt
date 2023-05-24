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


if ! pgrep -f "$COMMAND_LINE" >/dev/null; then
  echo "$(date -Is): $NAME is missing, starting it"
  $HOME/bin/start $1



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
