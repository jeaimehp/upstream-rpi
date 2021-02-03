#!/bin/bash

ls -lh /home/pi/upstream/sound
TIMESTAMP=`(/bin/date +%Y%m%d)`
ls /home/pi/upstream/sound/|while read line; do /usr/bin/rclone move -v /home/pi/upstream/sound/$line gdrive:sound/ 2>&1| tee -a /home/pi/upstream/data/sound-xfer-rclone-$TIMESTAMP.log;done
#echo "curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Wav File Xfer from Upstreampi @ Stengl\n$(cat /home/pi/upstream/data/sound-xfer-rclone-$TIMESTAMP.log)\n \"}' https://hooks.slack.com/services/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"|bash

