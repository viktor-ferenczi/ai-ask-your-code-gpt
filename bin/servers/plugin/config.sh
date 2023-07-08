#!/bin/sh

NAME="plugin"
TITLE="Plugin"

WORKING_DIR="$HOME/src/plugin"
COMMAND_LINE="hypercorn --config hypercorn.toml plugin:app"
WRAPPER="authbind --deep"
EXTRA_KILL="from multiprocessing"

LOG_PATH_BASENAME="$HOME/log/$NAME"

if [ "$ENVIRONMENT" == "PRODUCTION" ]; then
  export HTTP_PORT=443
else
  export HTTP_PORT=5555
fi

CANARY="http"
CANARY_URL="https://plugin.askyourcode.ai/"
CANARY_TIMEOUT=10
