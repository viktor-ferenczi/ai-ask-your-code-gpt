#!/bin/bash
set -euo pipefail
cd "$HOME/log"

# Compress after 3 days
for FN in $(find . -type f -mtime +3 | grep '.20' | egrep '.log$'); do
    echo "Compressed: $FN"
    gzip -9 $FN
done

# Delete after 90 days
for FN in $(find . -type f -mtime +90 | grep '.20' | egrep '.log.gz$'); do
    echo "Deleted: $FN"
    rm -f $FN
done
