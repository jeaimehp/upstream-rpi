#!/usr/bin/python3
import bme680
import time

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
i = 0

while (i < collections):
    sensor.get_sensor_data()
    temp_sum = temp_sum + sensor.data.temperature
    humidity_sum = humidity_sum + sensor.data.humidity
    pressure_sum = pressure_sum + sensor.data.pressure
    gas_sum = gas_sum + sensor.data.gas_resistance
    time.sleep (1)
    i += 1
print (temp_sum/collections, "C")
print (humidity_sum/collections, "%RH")
print (pressure_sum/collections, "hPa")
print (gas_sum/collections, "Ohms")






