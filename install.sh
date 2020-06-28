#!/bin/bash

# install, create and run virtualenv
sudo pip install virtualenv
virtualenv -p python3 venv
. venv/bin/activate

# install dependencies
pip install -r requirements.txt
