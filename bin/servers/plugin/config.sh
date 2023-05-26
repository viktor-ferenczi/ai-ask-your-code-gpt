#!/bin/sh

NAME="plugin"
TITLE="Plugin"

WORKING_DIR="$HOME/src/plugin"
COMMAND_LINE="hypercorn --config hypercorn.toml plugin:app"
WRAPPER="authbind --deep"

LOG_PATH="$HOME/log/$NAME.log"

CANARY="http"
CANARY_URL="https://plugin.askyourcode.ai/"
CANARY_TIMEOUT=10

export DOWNLOADER_URL="http://127.0.0.1:40001"
