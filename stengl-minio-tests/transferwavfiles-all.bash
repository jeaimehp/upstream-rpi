#!/bin/bash
SOUNDFILES_DIR="/home/pi/upstream/sound"
TIMESTAMP=`(date +%Y%m%d)`
echo "Getting the most recent soundfiles from $SOUNDFILES_DIR"
ls -Art $SOUNDFILES_DIR/*.wav > $SOUNDFILES_DIR/../data/sound-xfer-temp.log-$TIMESTAMP
echo "Sending files."

#cat $SOUNDFILES_DIR/../data/sound-xfer-temp.log-$TIMESTAMP | while read line;do /usr/bin/python3 $SOUNDFILES_DIR/../stengl-minio-tests/sendtocorral-minio.py $line; done
cat $SOUNDFILES_DIR/../data/sound-xfer-temp.log-$TIMESTAMP | while read line; do
	if [[ `(/usr/bin/python3 $SOUNDFILES_DIR/../stengl-minio-tests/stengl-minio-md5check-cleanoutput.py $line)` == true ]]; then
	      echo "File $line already sync'd"
        else 
               /usr/bin/python3 $SOUNDFILES_DIR/../stengl-minio-tests/sendtocorral-minio.py $line
	fi;
done

