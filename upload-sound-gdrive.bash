#!/bin/bash

ls -lh /home/pi/upstream/sound
TIMESTAMP=`(/bin/date +%Y%m%d)`
ls /home/pi/upstream/sound/|while read line; do /usr/bin/rclone move -v /home/pi/upstream/sound/$line gdrive:Upstream-Stengl-Data/sound/ 2>&1| tee -a /home/pi/upstream/data/sound-xfer-rclone-$TIMESTAMP.log;done
echo "curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Wav File Xfer from Upstreampi @ Stengl\n$(cat /home/pi/upstream/data/sound-xfer-rclone-$TIMESTAMP.log)\n \"}' [Redacted Slack API]"|bash
