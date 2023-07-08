#!/bin/bash
set -euo pipefail

. $HOME/bin/common.sh

cd $HOME/src
python -O -u migrate_database.py

exit 0
