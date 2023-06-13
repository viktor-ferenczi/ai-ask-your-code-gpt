#!/bin/bash

. ~/bin/common.sh

if [ -z "$1" ]; then
  date -Is
  run_for_all $0
  exit 0
fi

set -euo pipefail

bash ~/bin/stop.sh "$@"
sleep 1
bash ~/bin/start.sh "$@"
