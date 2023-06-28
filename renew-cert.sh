#!/bin/bash
# Run this script once a day from the root's crontab!
set -euo pipefail

SRC="/etc/letsencrypt/live/plugin.askyourcode.ai"
DST="/home/plugin/cert"

echo "$(date -Is): Certificate renewal"
letsencrypt renew --agree-tos

cd $SRC
for FN in $(ls *.pem); do
    if ! diff -q $SRC/$FN $DST/$FN >/dev/null; then
        echo "$FN: Updating (content changed, renewed)"
        cat $SRC/$FN >$DST/$FN
        chown plugin:plugin $DST/$FN
    else
        echo "$FN: Skipping (no change, not renewed)"
    fi
done
