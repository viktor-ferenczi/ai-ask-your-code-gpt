#!/bin/sh

export PYTHONPATH=$HOME/src
export PYTHONUNBUFFERED=1

export PRODUCTION=1

export QUERY_EMBEDDERS="http://127.0.0.1:40100"
export STORE_EMBEDDERS="http://127.0.0.1:40200 http://127.0.0.1:40201 http://127.0.0.1:40202"

export SERVERS_DIR="$HOME/bin/servers"

WRAPPER=""
EXTRA_KILL=""

run_for_all() {
  for DN in $(ls -1 $SERVERS_DIR); do
    if [ -f $SERVERS_DIR/$DN/config.sh ]; then
      $1 $DN
    fi
  done
}

check_process() {
    COUNT=$(pgrep -c -u $UID -f "$1")
    if [ $COUNT -eq 0 ]; then
        return 1
    else
        return 0
    fi
}
