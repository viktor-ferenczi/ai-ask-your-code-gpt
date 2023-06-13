#!/bin/bash
~/bin/restart.sh downloader
~/bin/restart.sh loader
~/bin/restart.sh plugin
#~/bin/restart.sh qdrant
~/bin/restart.sh query_embedder
~/bin/restart.sh store_embedder
