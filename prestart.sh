#! /usr/bin/env bash

# Start DB
python ./app/server_pre_start.py

# Run migrations

alembic upgrade head
