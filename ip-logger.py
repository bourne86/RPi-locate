#!/usr/bin/python

import dropbox
import os.path
import time
from requests import get

timestr = time.strftime("%Y%m%d-%H%M%S")
ip = get('https://api.ipify.org').text

if os.path.exists('/home/pi/log-rpi-zero-w.txt') :
        f=open("/home/pi/log-rpi-zero-w.txt", "a+")
        f.write(timestr + " : " + ip + "\n")
else :
        f=open("/home/pi/log-rpi-zero-w.txt", "a+")
        f.write("********************\n***IP Address Log***\n********************\n\n")
        f.write(timestr + " : " + ip + "\n")

time.sleep(3)

minute = time.strftime("%M")
#print minute[1]

if minute == "0":
    d = dropbox.Dropbox('6a3PWl8efcwAAAAAAAAXJ4FeQcIeqDrotu-jcQqnxMtfzgqKnblH0UNrRF4mHTsV')
    with open("/home/pi/log-rpi-zero-w.txt", "rb") as f2:
        d.files_upload(f2.read(), '/IP_Log/log-rpi-zero-w.txt', mode=dropbox.files.WriteMode("overwrite"))
