#! /bin/python 

# @author Cameron A. Morris
# Python script to turn an LED on and off via a Paspberry Pi 

# Import Pi GPIO module 
# Import time to set delays in code execution
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(33,GPIO.OUT)

print "Pin 13 on"
GPIO.output(33,GPIO.HIGH)
time.sleep(45)

print "Pin 13 off"
GPIO.output(33,GPIO.LOW)
time.sleep(1)






GPIO.cleanup()

