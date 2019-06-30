#!/usr/bin/python

import csv
import os
import requests

text_file = open("_output.txt", "w")
text_file.write('{\n        "wlan":[{')

reader = csv.reader(open("mydump-01.csv", "rb"), delimiter=',')
f = csv.writer(open("final.csv", "wb"))
for line in reader:
    if reader.line_num == 0:
         continue
    elif reader.line_num == 1:
         continue
    elif reader.line_num == 2:
         continue
    elif str("BTWifi-with-FON") in str(line):
         continue
    elif str("Virgin Media") in str(line):
         continue
    else:
        try:
            gotdata = line[0]
        except IndexError:
            gotdata = 'null'
        if gotdata == 'Station MAC':
            break
        if gotdata != 'null':
            text_file.write('\n        "mac": "' + line[0].replace(':', '-') + '",\n        "powrx":' + line[8] + '\n        },{')

text_file.close()

with open("_output.txt") as f1:
    lines = f1.readlines()

with open("output.txt", "w") as f2:
    f2.writelines(lines[:-1])

text_file2 = open("output.txt", "a")
text_file2.write('        }]\n}')
text_file2.close()

os.remove("_output.txt")

# Api-endpoint
URL = "https://pos.api.here.com/positioning/v1/locate?app_id=?????&app_code=?????"

# Location given here
data = open('output.txt', 'r')
data_2 = data.read()

# Sending get request and saving the response as response object
headers = {'Content-Type': 'application/json'}
r = requests.post(url = URL, data=data_2, headers=headers)

# Show the results
json = r.text
text_file3 = open("locations.txt", "a")
text_file3.write(json + "\n")
text_file3.close()
print json

os.remove('output.txt')
