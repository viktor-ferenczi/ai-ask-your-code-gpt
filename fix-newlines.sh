#!/bin/bash
for DP in $(find src -name __pycache__); do
    rm -rf $DP
done
for DN in bin src; do
    for FP in $(find ./$DN); do
	if [[ -d "$FP" ]]; then
	    continue
	fi
	EXT="${FP##*.}"
	if [[ "$EXT" != "png" ]] && [[ "$EXT" != "pyc" ]] && [[ "$EXT" != "pyo" ]]; then
	    dos2unix $FP
	fi
    done
done
