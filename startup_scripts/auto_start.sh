#!/usr/bin/env bash

cd /home/pi/deployinator
git pull

./startup_scripts/alert_startup_complete.py
./startup_scripts/deployinator.sh
