#!/usr/bin/env bash
# exit on error
uname -a
set -o errexit
# Install poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add poetry command to PATH
export PATH=${PATH}:${HOME}/.local/bin

poetry --version
poetry install

# Gather static files and migrate database
python3 manage.py collectstatic --no-input
python3 manage.py migrate
