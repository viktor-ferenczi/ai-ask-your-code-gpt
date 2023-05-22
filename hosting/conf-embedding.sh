#!/bin/sh

NAME=embedding

SCRIPT_DIR=~/app/plugin/src/embed
SCRIPT_PATH=$SCRIPT_DIR/embedding_server.py

WORKING_DIR=$SCRIPT_DIR
COMMAND_LINE="python -O -u $SCRIPT_PATH"

LOG_PATH=~/log/embedding.log

CANARY=http
CANARY_URL=$EMBEDDING_SERVER/
CANARY_TIMEOUT=10

