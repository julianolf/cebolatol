#!/usr/bin/env bash

# install required packages
apt-get update
apt-get install -y python3 python3-pip

# App root directory
APP_DIR='/vagrant'

# install required python packages
pip3 install -r $APP_DIR/requirements.txt

# start cebolatol app
python3 $APP_DIR/cebolatol.py
