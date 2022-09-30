#!/usr/bin/env python3

# NECCESARY IMPORTS

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template


# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
countries = [
    {'id': 0,
     'country': 'Liberia',
     'capital': 'Monrovia',
     'independence_date': 'July 26, 1847',
     'prior_ruling_country': '', },

     {'id': 1,
     'country': 'South Africa',
     'capital': 'Johannesbourg',
      'independence_date': 'May 31, 1910',
     'prior_ruling_country': 'Britain.',},

    {'id': 2,
        'country': 'Egypt',
        'capital': '1992',
        'independence_date': 'Feb 28, 1922',
        'prior_ruling_country': 'Britain', },

    {'id': 3,
     'country': 'Ethiopia',
     'capital': 'Addis Ababa',
     'independence_date': 'May 5, 1941',
     'prior_ruling_country': 'Italy', },

    {'id': 4,
        'country': 'Libya',
        'capital': 'Tripoli',
        'independence_date': 'Dec 24, 1951',
        'prior_ruling_country': 'Britain', },

    {'id': 5,
     'country': 'Sudan',
     'capital': 'Khartoum',
     'independence_date': 'Jan 1, 1956',
     'prior_ruling_country': 'Britain/Egypt', },

    {'id': 6,
        'country': 'Nigeria',
        'capital': 'Abuja',
        'independence_date': 'Oct 1, 1960',
        'prior_ruling_country': 'Britain', },
    {'id': 7,
     'country': 'Ghana',
     'capital': 'Accra',
     'independence_date': '',
     'prior_ruling_country': 'Britain', },

    {'id': 8,
         'country': 'Congo ',
         'capital': 'Kinshasha',
         'independence_date': 'June 30, 1960',
         'prior_ruling_country': 'Britain', },

  
]

# Endpoint 1: this endpoint returns information about this API in plain text
# This Endpont can be accessed by using typing <curl http://127.0.0.1:22424/> in the Terminal
@app.route("/home")
def home():
    return '''Colonized Countires in Africa
A prototype API for discovering the continent of Africa!!!'''

# Endpoint 2: this endpoint returns a HTML with a user input(somethng typed by the user) using Jinja Logic  
# This Endpont can be accessed by using <curl http://127.0.0.1:22424/<xxxxxx> in the Terminal
@app.route("/<username>")
def index(username):
    return render_template("info.html", name=username)

# Endpoint 3: this endpoint returns a a JSON
# This Endpont can be accessed by using <curl http://127.0.0.1:22424/<xxxxxx> in the Terminal
@app.route("/home/countries")
def glossary():
    # returns Books in JSON format
    return jsonify(countries)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
