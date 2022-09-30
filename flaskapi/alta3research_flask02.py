#!/usr/bin/env python3
import requests
from pprint import pprint
import crayons
# used to make HTTP requests (GET, POST, PUT, DELETE, etc.)
import urllib.request
import json

URL = "http://127.0.0.1:2224/"

# Sends a get request to an Endpoint that returns a JSON
response = requests.get(URL)

print(crayons.blue('==============================================='))
# To check type of dta returned, expecting an unreadable format
print(type(response))
print(crayons.blue('==============================================='))
# Prints the data requested from the API
# No readable data expected
pprint(response)

# Sends a GET request to the endpoint  and retirn ot in python format(readable by a user)
response = urllib.request.urlopen(URL)
data = response.read()   # read off all attached content
encoding = response.info().get_content_charset('utf-8')  # prep bytes decode
json_data = json.loads(data.decode(encoding))  # decode data


# test to check type of data returned, type of data should be a list of dictionaries
print(crayons.blue('==============================================='))
print(type(json_data))
print(crayons.blue('==============================================='))


print(json_data)
print(crayons.blue('==============================================='))

# Accept user input
#use user nput to determine what to display
#for loop loops to the list of dictionaries, print out country and ID.
for country in json_data:
    print(country.get('id'," "))
    print(country.get('country'))
# prompt for user input
print("Enter country index")
country_index= input()
x=int(country_index)
print("Enter one of 'capital' , 'independence_date', 'prior_ruling_country")
y=input()
print(json_data[x][y])


