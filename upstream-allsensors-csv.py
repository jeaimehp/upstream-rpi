#!/usr/bin/python3

import bme680
import time
#import Adafruit_ADS1x15

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.

#adc = Adafruit_ADS1x15.ADS1115()

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)


sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

collections = 3
temp_sum = 0
humidity_sum = 0
pressure_sum = 0
gas_sum = 0
#a0_sum = 0
#a2_sum = 0
i = 0
epoch_time = int(time.time())

while (i < collections):
    sensor.get_sensor_data()
    temp_sum = temp_sum + sensor.data.temperature
    humidity_sum = humidity_sum + sensor.data.humidity
    pressure_sum = pressure_sum + sensor.data.pressure
    gas_sum = gas_sum + sensor.data.gas_resistance
    #a0_sum = adc.read_adc(0, gain=1)
    #a2_sum = adc.read_adc(2, gain=1)
    time.sleep (1)
    i += 1

print(epoch_time,temp_sum/collections,humidity_sum/collections,pressure_sum/collections,gas_sum/collections)
     #   ,a0_sum/collections,a2_sum/collections)
