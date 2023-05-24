#!/bin/sh

export PYTHONPATH=$HOME/src
export PYTHONUNBUFFERED=1

export PRODUCTION=1

run_for_all() {
  for DN in $(find ~/bin/servers -maxdepth 1 -type d); do
    if [ -f $FN/config.sh ]; then
      $1 $DN
    fi
  done
}
