import math
import time
from grove.adc import ADC
#from grove.helper import SlotHelper
from grove.grove_sound_sensor import GroveSoundSensor

#sh = SlotHelper(SlotHelper.ADC)
pin = 4

sensor = GroveSoundSensor(pin)

print('Detecting sound...')
while True:
    print('Sound value: {0}'.format(sensor.sound))
    time.sleep(.3)
