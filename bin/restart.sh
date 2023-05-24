#!/bin/bash

. ~/bin/common.sh

if [ -z "$1" ]; then
  run_for_all $0
  exit 0
fi

set -euo pipefail

CONFIG_DIR="$HOME/bin/servers/$1"
. $CONFIG_DIR/config.sh



if [ "$1" == "all" ]; then

fi

bash ~/bin/stop.sh "$@"
bash ~/bin/start.sh "$@"
