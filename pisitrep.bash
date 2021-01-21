#!/bin/bash

date
echo "------------------------------------"
echo "System $(vcgencmd measure_temp)"
echo "Core $(vcgencmd measure_volts core)"
echo "Controller $(vcgencmd measure_volts sdram_c)"
echo "Input/Output $(vcgencmd measure_volts sdram_i)"
echo "Physical $(vcgencmd measure_volts sdram_p)"

