#!/bin/bash
set -euo pipefail

. environment.sh
. ~/bin/conf-$1.sh

function canary {
  case $CANARY in
  http)
    CANARY_REQUEST="--max-time ${CANARY_TIMEOUT} ${CANARY_URL}"
    curl -s "$CANARY_REQUEST" >/dev/null 2>&1
    return $?
    ;;

  none)
    return 0
    ;;
  esac
}

if canary; then
  exit 0
fi

echo "---"
date -Is
echo "---"

if canary; then
  echo "The $NAME server still works, the second Canary attempt succeeded."
  exit 0
fi

echo Server is down. Attempting to restart it.
bash ~/bin/restart.sh "$NAME"
