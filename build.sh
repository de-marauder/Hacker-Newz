#!/usr/bin/env bash
# exit on error
uname -a
set -o errexit
curl -sSL https://bootstrap.pypa.io/get-pip.py | python3
pip3 --version
which python3
python3 -m pip3 install --upgrade pip

pip3 install -r requirements.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate
