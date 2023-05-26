#!/bin/sh

export PYTHONPATH=$HOME/src
export PYTHONUNBUFFERED=1

export PRODUCTION=1

export QUERY_EMBEDDERS="http://127.0.0.1:40100"
export STORE_EMBEDDERS="http://127.0.0.1:40200 http://127.0.0.1:40201 http://127.0.0.1:40202"

run_for_all() {
  for DN in $(find ~/bin/servers -maxdepth 1 -type d); do
    if [ -f $FN/config.sh ]; then
      $1 $DN
    fi
  done
}
