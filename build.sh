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
curl https://gist.githubusercontent.com/emilhe/0c7b1a33b2d02f17331242bf4fffd07c/raw/8da0665a58f469c980e7661d7f8c36f3bd3af992/strip_setuptools.py | python - && poetry install
echo '=================='
poetry install
echo '=================='

# Gather static files and migrate database
python3 manage.py collectstatic --no-input
python3 manage.py migrate
