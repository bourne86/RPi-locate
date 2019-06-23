#!/usr/bin/python

import os
import re
import time

os.system('ifconfig > ifconfig.txt')

if 'wlan1mon' in open('ifconfig.txt').read():
    os.system("sudo timeout 10s airodump-ng wlan1mon --background 1 -w mydump -o csv")
else :
    os.system("sudo airmon-ng start wlan1")
    time.sleep(20)
    os.system("sudo timeout 10s airodump-ng wlan1mon --background 1 -w mydump -o csv")

os.remove('ifconfig.txt')
