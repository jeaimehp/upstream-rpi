#!/bin/bash
OUTPUT=`/usr/bin/atq`

## Uncomment for debugging
#echo $OUTPUT

if [ -z "${OUTPUT}" ]; then
	echo "No scheduled jobs. Setting rescordings"
	/home/pi/upstream/at-30before-sunset.bash "/home/pi/upstream/upstream-sound-respeaker.bash 3600" >> /home/pi/upstream/data/soundsetting-`(/bin/date +%Y%m%d)`.log
	/usr/bin/atq
fi
