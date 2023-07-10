#!/bin/bash -l
set -euo pipefail

test -n "$USER"
test -n "$ENVIRONMENT"

export PYTHONPATH=$HOME/src
/usr/bin/python3 ~/src/migrate_database.py
