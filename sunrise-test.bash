#!/bin/bash
grep $(date +"%m/%d/%Y") /home/pi/upstream/sunrise-sunset-times.txt |awk '{print $2,$1}'
