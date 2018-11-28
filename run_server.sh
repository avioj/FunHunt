#!/usr/bin/env bash
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
nohup python3 $dir/run.py >& /dev/null &