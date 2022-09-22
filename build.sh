#!/usr/bin/env bash
# exit on error
set -o errexit
sudo apt-get update
sudo apt-get -y install python3-pip
pip3 --version

pip3 install -r requirements.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate
