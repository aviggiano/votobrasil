#!/bin/bash
sudo apt-get install sqlite3 python-pip python-virtualenv

#setup virtualenv in dir './venv'
virtualenv venv --distribute

#install requirements with virtualenv and pip
source venv/bin/activate
pip install -r requirements.txt

