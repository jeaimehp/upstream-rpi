#!/bin/bash
/usr/bin/raspistill -o /home/pi/upstream/pictures/`(date +%s)`.jpg
echo "Image captured @ $(date)"
