#! /usr/bin/env python

print "Bedroom lights on"

from phue import Bridge 

b = Bridge('192.169.1.109')

#b.connect()

b.set_light([1,2,3,4,5],'on',True)

b.set_light([1,2,3,4,5],'bri',254)

print "Lights on br0"
