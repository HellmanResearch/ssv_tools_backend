#!/usr/bin/env bash
ps -ef | grep 'AppDfinityOffChainBackend.asgi:application' | grep -v grep | awk '{print $2}' | xargs kill
echo stopped