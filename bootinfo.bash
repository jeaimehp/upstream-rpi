#!/bin/bash

PUBLICIPADDR=`curl ipv4bot.whatismyipaddress.com`
echo $PUBLICIPADDR
hostname -I


## Slack push
echo "curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"SitRep from UPSTREAMPI_Stengl\n\t PublicIP=$PUBLICIPADDR\n\tPrivateIP=$(hostname -I)\n\tInternalDate=$(date)\n\tDisk Usage=\n$(df -hT|head -n 2)\n\tLast recorded=\n$(ls -lh /home/pi/upstream/sound/|tail -n 2)\n\tScheduled Recordings=\n$(atq) \"}' https://hooks.slack.com/services/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"
