#!/bin/bash
# Written for Upstream to run get the time of the sunrise
# then parse it into %H:%M and create and run the at scheduling
# command.
#
# Written by: Je'aime Powell
# Contact: jhpowell@tacc.utexas.edu
# Date: 9/24/20
# Revision 1

# Check things in the at queue using atq
# Remove things from the queue with atrm <atq_job_number>

# This variable can be altered to use any time wanted
SUNSET_TIME=`/usr/bin/python3 /home/pi/upstream/upstream-sunset.py`
##Debug - remove comment to run immediately
#SUNSET_TIME="now"

# Stdin variable. Remember to enclose in quotes " " 
COMMAND=$1

#checks if a stdin command line arguement was given and outputs error if it is not
if [ -z "$1" ]; then
    echo -e "Invalid input, You need to add your command that you want to run at sunset!"
    echo -e "Example: at-sunset.bash \"/path/command [options]\" "
    exit
fi

# Actual command to be run against echo and outputs to system mail /var/spool/mail
echo $COMMAND|at -m $SUNSET_TIME
##Debug
#echo $COMMAND|at -m now


