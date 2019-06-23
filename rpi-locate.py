import csv
import json
import os
import requests
import time
import sys

os.system('ifconfig > ifconfig2.txt')

if 'wlan1mon' not in open('ifconfig2.txt').read():
    os.remove('ifconfig2.txt')
    sys.exit()

os.remove('ifconfig2.txt')
time.sleep(20)

#if os.path.exists("mydump-01.csv"):
#    os.remove("mydump-01.csv")

#os.system("sudo timeout 10s airodump-ng wlan1mon --background 1 -w mydump -o csv")

if os.path.exists("output.txt"):
    os.remove("output.txt")

text_file = open("_output.txt", "w")

import os
for file in os.listdir("/home/pi"):
    if file.endswith(".csv"):
        filepath = os.path.join("/home/pi", file)

with open (filepath, "rb") as csvfile:
    reader = csv.reader(csvfile)
    text_file.write('{\n        "wlan":[{')
    for row in reader:
        str1 = str(row[0])
        str2 = str1.replace(':', '-')
        str3 = str(row[8])
        text_file.write('\n        "mac": "' + str2 + '",\n        "powrx":' + str3 + '\n        },{')

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
URL = "https://pos.api.here.com/positioning/v1/locate?app_id=ohiQjJyrYkY5oidVET0S&app_code=T-pIWWZu-4tqUu6aJnpywQ"

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

os.remove("output.txt")
os.remove("mydump-01.csv")
