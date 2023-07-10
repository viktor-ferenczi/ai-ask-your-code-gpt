#!/bin/bash

if [ -z "$USER" ]; then
  echo "USER environment variable is not set"
  exit 1
fi

set -euo pipefail

. $HOME/bin/common.sh

cd $HOME/src
python -O -u migrate_database.py

exit 0
