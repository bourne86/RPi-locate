#!/usr/bin/python

import csv
import json
import os

if os.path.exists("output.txt"):
    os.remove("output.txt")

text_file = open("_output.txt", "w")

with open ("final.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    text_file.write('{\n        "wlan":[{')
    for row in reader:
        str1 = str(row[0])
        str2 = str1.replace(':', '-')
        str3 = str(row[8])
        text_file.write('\n        "mac": "' + str2 + '",\n        "powrx":' + str3 + '\n        },{')
#    text_file.write('        }]\n}')

text_file.close()

with open("_output.txt") as f1:
    lines = f1.readlines()

with open("output.txt", "w") as f2:
    f2.writelines(lines[:-1])

text_file2 = open("output.txt", "a")
text_file2.write('        }]\n}')
text_file2.close()

os.remove("_output.txt")
