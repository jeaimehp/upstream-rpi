#!/bin/bash
grep $(date +"%m/%d/%Y") /home/pi/upstream/2021-sunrise-sunset.txt |awk '{print $2,$1}'
