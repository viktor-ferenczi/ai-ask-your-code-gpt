#!/bin/bash

. ~/bin/common.sh

set -euo pipefail

cd ~/src
python -O -u delete_project.py $1

exit 0
