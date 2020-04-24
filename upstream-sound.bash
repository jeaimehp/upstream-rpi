#!/bin/bash
RECORDTIME=$1
if [ -z "$RECORDTIME" ]
then
	echo "Recording with default 10 seconds\n"
	echo "USAGE: upstream-sound.bash <time in seconds>"
	/usr/bin/arecord --duration=10 --channels=2 --format=S16_LE --rate 44100 --device=hw:1,0 /home/pi/upstream/sound/`(date +%s)`.wav
	echo "Recorded sound @ $(date)"
else
	/usr/bin/arecord --duration=$RECORDTIME --channels=2 --format=S16_LE --rate 44100 --device=hw:1,0 /home/pi/upstream/sound/`(date +%s)`.wav
	echo "Recorded sound @ $(date) for $RECORDTIME seconds"
fi
