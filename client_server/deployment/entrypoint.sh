#!/bin/sh
set -e

# start application
export PYTHONPATH=/app
exec python3 /app/server/client_server.py
