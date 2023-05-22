#!/bin/bash
set -euo pipefail
bash ~/bin/stop.sh $1
bash ~/bin/start.sh $1
