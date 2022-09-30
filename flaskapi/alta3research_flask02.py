#!/usr/bin/env python3
import requests
from pprint import pprint

# used to make HTTP requests (GET, POST, PUT, DELETE, etc.)
import urllib.request
import json

URL = "http://127.0.0.1:2224/"

# Sends a get request to an Endpoint that returns a JSON
response = requests.get(URL)

# To check type of dta returned, expecting an unreadable format
print(type(response))
print("=============================")
# Prints the data requested from the API
# No readable data expected
pprint(response)

# Sends a GET request to the endpoint  and retirn ot in python format(readable by a user)
response = urllib.request.urlopen(URL)
data = response.read()   # read off all attached content
encoding = response.info().get_content_charset('utf-8')  # prep bytes decode
json_data = json.loads(data.decode(encoding))  # decode data


# test to check type of data returned, type of dat shoul dbe  list of dictionaries
print("=============================")
print(type(json_data))
print("=============================")
print(json_data)


print("=============================")
print(json_data[1]['title'])    # perform a test looku
