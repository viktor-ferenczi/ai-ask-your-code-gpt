#!/bin/sh

NAME=plugin

SCRIPT_DIR=~/app/plugin/src/plugin
SCRIPT_PATH=$SCRIPT_DIR/plugin_server.py

LOG_PATH=~/log/plugin.log

CANARY_URL=http://127.0.0.1:$PLUGIN_PORT/
CANARY_TIMEOUT=10
