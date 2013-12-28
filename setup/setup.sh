#!/bin/bash
sudo apt-get install sqlite3 python-pip python-virtualenv

#setup virtualenv in current dir
virtualenv .

#install requirements with virtualenv and pip
source bin/activate
sudo pip install -r requirements.txt

