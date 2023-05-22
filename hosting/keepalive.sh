#!/bin/bash
set -euo pipefail

. environment.sh
. $1.conf

CANARY_REQUEST="--max-time ${CANARY_TIMEOUT} ${CANARY_URL}"

if curl -s "$CANARY_REQUEST" >/dev/null; then
  exit 0
fi

echo "---"
date -Is
echo "---"

if curl -sS "$CANARY_REQUEST"; then
  echo "The $SERVER_NAME server still works, the second Canary attempt succeeded."
  exit 0
fi

echo Server is down. Attempting to restart it.
bash ~/bin/restart.sh "$SERVER_NAME"
