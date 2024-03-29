#!/bin/bash
RECORDTIME=$1
if [ -z "$RECORDTIME" ]
then
	echo "Recording with default 10 seconds\n"
	echo "USAGE: upstream-sound-respeaker.bash <time in seconds>"
	/usr/bin/arecord -Dac108 --duration=10 --channels=6 --format=S32_LE --rate 16000 /home/pi/upstream/sound/$HOSTNAME-`(date +%s)`.wav
	echo "Recorded sound @ $(date)"
else
	/usr/bin/arecord -Dac108 --duration=$RECORDTIME --channels=6 --format=S32_LE --rate 16000 /home/pi/upstream/sound/$HOSTNAME-`(date +%s)`.wav
	echo "Recorded sound @ $(date) for $RECORDTIME seconds"
fi
