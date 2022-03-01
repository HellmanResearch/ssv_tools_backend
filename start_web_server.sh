#!/usr/bin/env bash
nohup ../venv/bin/daphne AppDfinityOffChainBackend.asgi:application -b 0.0.0.0 -p 8012 >> web_server_stdout.log 2>&1 &
echo started