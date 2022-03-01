#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    ../venv/bin/celery multi stop withdraw_celery -A AppDfinityOffChainBackend -B --pidfile="./%n.pid" --logfile="./logs/%n%I.log" -l debug --concurrency=8
elif [[ "$OSTYPE" == "darwin"* ]]; then
    celery multi stop withdraw_celery -A AppDfinityOffChainBackend -B --pidfile="./%n.pid" --logfile="./logs/%n%I.log" -l debug --concurrency=8
fi

ps -ef | grep 'm celery worker -A AppDfinityOffChainBackend -B' | grep -v grep | awk '{print $2}' | xargs kill -9
echo stopped
