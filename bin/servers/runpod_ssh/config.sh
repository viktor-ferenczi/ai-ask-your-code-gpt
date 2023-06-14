#!/bin/sh

NAME="runpod_ssh"
TITLE="Runpod SSH"

WORKING_DIR="$HOME"
COMMAND_LINE="ssh -L 40201:localhost:40201 -n -o ExitOnForwardFailure=yes -o TCPKeepAlive=yes -o ServerAliveInterval=60 -4 -l root -p 43488 185.32.161.60 sleep 86400"
#COMMAND_LINE="ssh -L 40201:localhost:40201 -L 40202:localhost:40202 -n -o ExitOnForwardFailure=yes -o TCPKeepAlive=yes -o ServerAliveInterval=60 -4 -l root -p 43488 185.32.161.60 sleep 86400"

LOG_PATH_BASENAME="$HOME/log/$NAME"

CANARY="none"
