#!/bin/bash

. ~/bin/common.sh

if [ -z "$1" ]; then
  run_for_all $0
  exit 0
fi

set -euo pipefail

bash ~/bin/stop.sh "$@"
bash ~/bin/start.sh "$@"
