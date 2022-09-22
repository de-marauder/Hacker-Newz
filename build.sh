#!/usr/bin/env bash
# exit on error
uname -a
set -o errexit
# Install poetry
# python3 ./poetry.py

# Add poetry command to PATH
# export PATH=${PATH}:${HOME}/.local/bin
# add-apt-repository ppa:deadsnakes/ppa
# apt update
echo '=================='
echo ${PATH}
echo '=================='
python3 --version
echo '=================='
poetry --version
echo '=================='
# poetry shell
echo '=================='
poetry install
echo '=================='

# Gather static files and migrate database
python3 manage.py collectstatic --no-input
python3 manage.py migrate
