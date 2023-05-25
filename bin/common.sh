#!/bin/sh

export PYTHONPATH=$HOME/src
export PYTHONUNBUFFERED=1

export PRODUCTION=1

export QUERY_EMBEDDERS="http://127.0.0.1:40100 http://127.0.0.1:40101 http://127.0.0.1:40102 http://127.0.0.1:40103 http://127.0.0.1:40104"
export STORE_EMBEDDERS="http://127.0.0.1:40200 http://127.0.0.1:40201 http://127.0.0.1:40202 http://127.0.0.1:40203 http://127.0.0.1:40204"

run_for_all() {
  for DN in $(find ~/bin/servers -maxdepth 1 -type d); do
    if [ -f $FN/config.sh ]; then
      $1 $DN
    fi
  done
}
