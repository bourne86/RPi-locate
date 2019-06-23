import requests
import json
import re

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
print json
