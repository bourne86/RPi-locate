#!/usr/bin/python

from requests import get
import os.path
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
ip = get('https://api.ipify.org').text
# print 'My public IP address is:', ip

if os.path.exists('/home/pi/log-rpi-zero-w.txt') :
	f=open("/home/pi/log-rpi-zero-w.txt", "a+")
	f.write(timestr + " : " + ip + "\n")
else :
	f=open("/home/pi/log-rpi-zero-w.txt", "a+")
	f.write("********************\n***IP Address Log***\n********************\n\n")
	f.write(timestr + " : " + ip + "\n")
