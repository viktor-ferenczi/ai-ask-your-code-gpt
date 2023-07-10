export PYTHONPATH=$HOME/src
export PYTHONUNBUFFERED=1

if [ "$USER" == "plugin" ]; then
  export ENVIRONMENT="PRODUCTION"
  export HTTP_PORT_OFFSET=0
else
  export ENVIRONMENT="STAGING"
  export HTTP_PORT_OFFSET=500
fi

export SERVERS_DIR="$HOME/bin/servers"

CPU_COUNT=$(nproc --all)

CANARY="none"
CANARY_URL="http://127.0.0.1"
CANARY_TIMEOUT=10

INSTANCE_INDEX=0
INSTANCE_COUNT=1

WRAPPER=""
EXTRA_KILL=""

RESTART_WAIT=1

run_for_all() {
  for DN in $(ls -1 $SERVERS_DIR); do
    if [ -f $SERVERS_DIR/$DN/config.sh ]; then
      $1 $DN
    fi
  done
}

check_process() {
    COUNT=$(pgrep -c -u $UID -f "$1")
    if [ $COUNT -eq 0 ]; then
        return 1
    else
        return 0
    fi
}
