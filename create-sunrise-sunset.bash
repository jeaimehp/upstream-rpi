#!/bin/bash

mv sunrise-sunset-times.txt sunrise-sunset-times.old
echo "Moving previous version and creating new sunrise-sunset-times.txt file"
python sunrise_sunset.py >> sunrise-sunset-times.txt
echo "Done"
