#!/bin/bash

. ~/bin/common.sh

set -euo pipefail

cd ~/src
python -O -u cleanup_projects.py 12

exit 0
