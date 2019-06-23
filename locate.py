import requests
import json

# Api-endpoint
URL = "https://pos.api.here.com/positioning/v1/locate?app_id=<app ip here>&app_code=<app code here>"

# Location given here
data = {"wlan":[{"mac": "8C-1A-BF-20-66-AD"},{"mac": "A0-E4-53-E9-66-A7"},{"mac": "AC-4B-C8-34-F7-01"},{"mac": "A0-21-95-57-79-06"},{"mac": "00-18-56-51-54-FB"},{"mac": "10-30-47-D2-54-55"},{"mac": "B8-6B-23-09-87-B1"},{"mac": "F4-55-95-11-2C-C1"}]}

# Sending get request and saving the response as response object
headers = {'Content-Type': 'application/json'}
r = requests.post(url = URL, data=json.dumps(data), headers=headers)

# Show the results
json = r.text
print json
