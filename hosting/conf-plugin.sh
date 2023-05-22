#!/bin/sh

NAME=plugin

SCRIPT_DIR=~/app/plugin
SCRIPT_PATH=$SCRIPT_DIR/plugin_server.py

WORKING_DIR=$SCRIPT_DIR
COMMAND_LINE="python -O -u $SCRIPT_PATH"

LOG_PATH=~/log/plugin.log

CANARY=http
CANARY_URL=http://127.0.0.1:5555/
CANARY_TIMEOUT=10
