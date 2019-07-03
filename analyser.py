#!/usr/bin/python

import os
import requests
import json
import time
import dropbox

os.system('sudo iwlist wlan0 scan > /home/pi/_scan.txt')

text_file = open("/home/pi/_temp.txt", "w")
text_file.write('{\n        "wlan":[{')

f = open("/home/pi/_scan.txt", "r")
for x in f:
    if "Address" in x:
        text_file.write('\n        "mac": "')
        txt = x[29:-1]
        txt2 = txt.replace(":","-")
        text_file.write(txt2)
    elif "Signal" in x:
        text_file.write('",\n        "powrx": ')
        txt3 = x[48:-7]
        text_file.write(txt3)
        text_file.write('\n        },{')
    else:
        continue

text_file.close()

with open("/home/pi/_temp.txt") as f1:
    lines = f1.readlines()

with open("/home/pi/wifi.txt", "w") as f2:
    f2.writelines(lines[:-1])

text_file2 = open("/home/pi/wifi.txt", "a")
text_file2.write('        }]\n}')
text_file2.close()

os.remove("/home/pi/_temp.txt")
os.remove('/home/pi/_scan.txt')

# Api-endpoint
URL = "https://pos.api.here.com/positioning/v1/locate?app_id=<<<>>>&app_code=<<<>>>"

# Location given here
data = open('/home/pi/wifi.txt', 'r')
data_2 = data.read()

# Sending get request and saving the response as response object
headers = {'Content-Type': 'application/json'}
r = requests.post(url = URL, data=data_2, headers=headers)
values = json.loads(r.text)
lat = values['location']['lat']
lng = values['location']['lng']
accuracy = values['location']['accuracy']

# Show the results
data_3 = str(lat) + ", " + str(lng) + ", " + str(accuracy)
timestr = time.strftime("%d%m%Y %H%M%S")
if os.path.exists('/home/pi/locations.txt') :
        text_file3 = open("/home/pi/locations.txt", "a+")
        text_file3.write(timestr + ", " + data_3 + "\n")
else :
        text_file3=open("/home/pi/locations.txt", "a+")
        text_file3.write("date/time, latitude, longitude, accuracy\n")
        text_file3.write(timestr + ", " + data_3 + "\n")

text_file3.close()

os.remove('/home/pi/wifi.txt')

d = dropbox.Dropbox('<<<>>>')
with open("/home/pi/locations.txt", "rb") as f2:
    d.files_upload(f2.read(), '/IP_Log/locations.txt', mode=dropbox.files.WriteMode("overwrite"))

