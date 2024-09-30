#!/usr/bin/env bash

if ! python ./main/cantor_set.py "$@"; then
    echo "STATUS SIGNIFIES ERROR after running with arguments: $@"
    exit 1
fi
