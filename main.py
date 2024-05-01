import requests
import json

# set up the request parameters
params = {
'api_key': '01F32D050FA0473F97C74A39D6C097D8',
  'type': 'product',
  'gtin': '37000917816'
}

# make the http GET request to RedCircle API
api_result = requests.get('https://api.redcircleapi.com/request', params)

# print the JSON response from RedCircle API
print(json.dumps(api_result.json()))