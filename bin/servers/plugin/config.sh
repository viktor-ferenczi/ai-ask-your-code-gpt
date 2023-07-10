NAME="plugin"
TITLE="Plugin"

WORKING_DIR="$HOME/src/plugin"
COMMAND_LINE="$HOME/.local/bin/hypercorn --config hypercorn.toml plugin:app"
WRAPPER="/usr/bin/authbind --deep"
EXTRA_KILL="from multiprocessing"

if [ "$ENVIRONMENT" == "PRODUCTION" ]; then
  export HTTP_PORT=443
  cp "$HOME/src/plugin/hypercorn.prd.toml" "$HOME/src/plugin/hypercorn.toml"
else
  export HTTP_PORT=5555
  cp "$HOME/src/plugin/hypercorn.stg.toml" "$HOME/src/plugin/hypercorn.toml"
fi

CANARY="http"
CANARY_URL="https://plugin.askyourcode.ai/"
CANARY_TIMEOUT=10
