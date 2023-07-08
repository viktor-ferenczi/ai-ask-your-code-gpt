#!/bin/bash
# Run this script once a day from the root's crontab!
set -euo pipefail

SRC="/etc/letsencrypt/live/plugin.askyourcode.ai"
DST_PRD="/home/plugin/cert"
DST_STG="/home/staging/cert"

echo "$(date -Is): Certificate renewal"
letsencrypt renew --agree-tos

if ! [ -d $DST_PRD ]; then
  mkdir -p $DST_PRD
  chown plugin:plugin $DST_PRD
fi

cd $SRC
for FN in $(ls *.pem); do
  if ! [ -f $DST_PRD/$FN ] || ! diff -q $SRC/$FN $DST_PRD/$FN >/dev/null; then
    echo "$FN: Updating (content changed, renewed)"
    cat $SRC/$FN >$DST_PRD/$FN
    chown plugin:plugin $DST_PRD/$FN
    cat $SRC/$FN >$DST_STG/$FN
    chown staging:staging $DST_STG/$FN
  else
    echo "$FN: Skipping (no change, not renewed)"
  fi
done
