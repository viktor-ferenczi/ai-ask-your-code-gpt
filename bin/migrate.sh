#!/bin/bash
echo "$(date -Is): Database migration"

if [ -z "$USER" ]; then
  echo "USER environment variable is not set"
  exit 1
fi

set -euo pipefail

. $HOME/bin/common.sh

cd $HOME/src
python -O -u migrate_database.py

echo "$(date -Is): Done $0"
exit 0
