#!/usr/bin/python
from phue import Bridge
import random

b = Bridge('192.168.1.109') # Enter bridge IP here.

#If running for the first time, press button on bridge and run with b.connect() uncommented
#b.connect()

lights = b.get_light_objects()

#for light in lights:
#        light.brightness = 254
#        light.xy = [random.random(),random.random()]

for light in lights: 
    light.brightness = 155 
    light.xy = [0.3,0.3]


# yellow = 0.5,0.5
# pink = 0.5,0.3
# dark blue = 0.1,0.1
# daylight = 0.4,0.4
# dark red = 0.9, 0.6 
# chill orange = 0.7,0.6 
# darker orange = 0.9,0.7
# bright green = 0.3,0.8
# classy orange = 0.9,0.9
# bright blue = 0.2,0.2
# concentrate = 0.3,0.3
