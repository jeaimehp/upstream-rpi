#!/bin/bash
echo "THIS COMMAND REQUIRES SUDO OR ROOT!!"
echo""
echo "RPi Data Time"
date
echo "Current RTC Date Time"
/usr/sbin/hwclock -r
echo "Updating RTC Date Time from RPi"
/usr/sbin/hwclock -w
/usr/sbin/hwclock -r
