#! /bin/python 

# @author Cameron A. Morris
# Python script to turn an LED on and off via a Paspberry Pi 

try:
	f = open("/dev/servoblaster")
	f.write('1=50')
	f.close()
except:
	print("Fuck me, something broke")

