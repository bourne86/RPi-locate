#!/usr/bin/python

import csv

with open("mydump-01.csv") as f:
    for l, i in enumerate(f):
        data = i.split(",")
        if data[0] == "Station MAC":
            delete = l
            print "Start of useless data:", l + 1

with open("mydump-01.csv") as f:
    total = sum(1 for line in f)
    print "Total number of rows: " + str(total)

delete2 = delete - 1

reader = csv.reader(open("mydump-01.csv", "rb"), delimiter=',')
f = csv.writer(open("final.csv", "wb"))
for line in reader:
    if reader.line_num == 0:
        print "Removing line"
    elif reader.line_num == 1:
        print "Removing line"
    elif reader.line_num == 2:
        print "Removing line"
    elif reader.line_num > delete2:
        print "Removing line"
    elif str("BTWifi-with-FON") in str(line):
        print "Removing line"
    elif str("Virgin Media") in str(line):
        print "Removing line"
    else:
        f.writerow(line)
        print line
