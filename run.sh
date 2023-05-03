#!/bin/bash

pwd

#check if python installed
#check if venv exists

python3 -m venv contact-venv
source contact-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 src/main.py