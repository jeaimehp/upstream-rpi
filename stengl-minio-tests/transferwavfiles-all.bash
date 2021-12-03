#!/bin/bash
SOUNDFILES_DIR="/home/pi/upstream/sound"
TIMESTAMP=`(date +%Y%m%d)`
echo "Getting the most recent soundfiles from $SOUNDFILES_DIR"
ls -Art $SOUNDFILES_DIR|grep wav > $SOUNDFILES_DIR/../data/sound-xfer-temp.log-$TIMESTAMP

if [[ $(cat $SOUNDFILES_DIR/../data/sound-xfer-temp.log-$TIMESTAMP| wc -l) -eq 0 ]]; then
	echo " "
	echo "NOTE: There are no wav sound files to clean up in $SOUNDFILES_DIR"
	echo " "
	exit 0
fi

echo "Sending files."

#cat $SOUNDFILES_DIR/../data/sound-xfer-temp.log-$TIMESTAMP | while read line;do /usr/bin/python3 $SOUNDFILES_DIR/../stengl-minio-tests/sendtocorral-minio.py $SOUNDFILES_DIR/$line; done
cat $SOUNDFILES_DIR/../data/sound-xfer-temp.log-$TIMESTAMP | while read line; do
	if [[ `(/usr/bin/python3 $SOUNDFILES_DIR/../stengl-minio-tests/stengl-minio-md5check-cleanoutput.py $SOUNDFILES_DIR/$line)` == true ]]; then
	      echo "File $SOUNDFILES_DIR/$line already sync'd"
        else 
               /usr/bin/python3 $SOUNDFILES_DIR/../stengl-minio-tests/sendtocorral-minio.py $SOUNDFILES_DIR/$line
	fi;
done

