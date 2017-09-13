#! /usr/bin/env python

from phue import Bridge
import random

b = Bridge('192.168.1.124') 

lights = b.get_light_objects()

for light in lights: 
    light.brightness = 155 
    light.xy = [0.9,0.6]

print "Netflix lights on"
