#!/usr/bin/env bash
# exit on error
uname -a
set -o errexit
# Install poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add poetry command to PATH
export PATH=${PATH}:${HOME}/.local/bin
echo '=================='
echo ${PATH}
echo '=================='
poetry --version
echo '=================='
poetry shell
echo '=================='
poetry install
echo '=================='

# Gather static files and migrate database
python3 manage.py collectstatic --no-input
python3 manage.py migrate
