#!/bin/sh

NAME=plugin

WORKING_DIR=~/src/plugin
COMMAND_LINE="hypercorn --config hypercorn.toml plugin_server:app"

LOG_PATH=~/log/plugin.log

CANARY=http
CANARY_URL=https://plugin.askyourcode.ai/
CANARY_TIMEOUT=10
