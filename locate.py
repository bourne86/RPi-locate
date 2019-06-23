import requests
import json
import re

# Api-endpoint
URL = "https://pos.api.here.com/positioning/v1/locate?app_id=<app_id_here>&app_code=<app_code_here>"

# Location given here
data = open('output.txt', 'r')
data_2 = data.read()

# Sending get request and saving the response as response object
headers = {'Content-Type': 'application/json'}
r = requests.post(url = URL, data=data_2, headers=headers)

# Show the results
json = r.text
print json
