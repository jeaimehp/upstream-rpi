#!/usr/bin/python3
import Adafruit_ADS1x15

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.

adc = Adafruit_ADS1x15.ADS1115()


for i in range(4):
    print("Analog",i,"= ",adc.read_adc(i, gain=1))






