#!/bin/bash
/usr/bin/python3 /home/pi/upstream/upstream-allsensors-csv.py >> /home/pi/upstream/data/sensors-`(/bin/date +%Y%m%d)`.log
