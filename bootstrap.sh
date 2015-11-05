#!/usr/bin/env bash

# install required packages
apt-get update
apt-get install -y python3 python3-pip

# API root directory
API_DIR='/vagrant'

# install required python packages
pip3 install -r $API_DIR/requirements.txt

# start cebolatol app
python3 $API_DIR/cebolatol.py
