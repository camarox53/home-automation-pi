#! /bin/python

# @author Cameron A. Morris

import RPi.GPIO as GPIO
import time
import optparse

# Variables
halfoz = 15
oneoz = 30
onehalfoz = 45
twooz = 60
volume = 0
GPIN = 33

# GPIO Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIN,GPIO.OUT)
GPIO.setwarnings(False)

# Argument Parser
parser = optparse.OptionParser()
parser.add_option('-a', '--amount',
    action="store", dest="amount",
    help="amount string", default="null")
options, args = parser.parse_args()

#METHODS
def pump(volume):
        print ("Pump Time Required: {} seconds".format(volume))
        GPIO.output(GPIN,GPIO.HIGH)
        time.sleep(volume)
        GPIO.output(GPIN,GPIO.LOW)

def cleanup():
        time.sleep(1)
        GPIO.cleanup()

# Accepted Script Arguments
if options.amount == "oneoz":
        print "One Ounce Selected"
        pump(oneoz)
elif options.amount == "twooz":
        print "Two Ounces Selected"
        pump(twooz)
elif options.amount == "halfoz":
        print "A half an Ounce is Selected"
        pump(halfoz)
elif options.amount == "onehalfoz":
        print "One Half of an Ounce is Selected"
        pump(onehalfoz)
else:
        print "Invalid Selection"
        
cleanup()
