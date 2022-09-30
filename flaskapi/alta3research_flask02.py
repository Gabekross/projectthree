#!/usr/bin/env python3
import requests
from pprint import pprint
import crayons
# used to make HTTP requests (GET, POST, PUT, DELETE, etc.)
import urllib.request
import json

URL = "http://127.0.0.1:2224/home/countries"

# Sends a get request to an Endpoint in a Flask API.
# THE Flask API returns a JSON
response = requests.get(URL)

print(crayons.blue('==============================================='))
# Checking type of data returned, expecting an unreadable format
print(type(response))
print(crayons.blue('==============================================='))

# Prints the data requested from the API
# A response is expected but mo readable data expected
pprint(response)

# Sends a GET request to the endpoint  ina a Flask API.
response = urllib.request.urlopen(URL)
data = response.read()   # read off all attached content
encoding = response.info().get_content_charset('utf-8')  # prep bytes decode

#  Noramlize returned JSON to a python format(readable by a user)
json_data = json.loads(data.decode(encoding))  # decode data


# test to check type of data returned, type of data should be a list of dictionaries
print(crayons.blue('==============================================='))
print(type(json_data))
print(crayons.blue('==============================================='))

# Print out normalized data to readale format
print(json_data)
print(crayons.blue('==============================================='))

#Give user option sort through teh list and view their desired country
# Accept user input
#use user nput to determine what to display
#for loop loops to the list of dictionaries, print out country and ID.
for country in json_data:
    print(country.get('id'), end=": ")
    print(country.get('country'))
    

#Give user option sort through teh list and view their desired country
# prompt for user input
print("Enter country index (e.g <3> Ignore braces: ")

#Save user input in country_index variable
country_index= input()

#convert country_index string to an to an integer and save in variable x
x=int(country_index)

print(crayons.red('Enter one of: (Check for spelling): capital , independence_date, prior_ruling_country'))
# Accept user selection and save user selection in variable y
y=input()
print(json_data[x][y])





