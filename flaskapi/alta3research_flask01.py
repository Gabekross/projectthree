#!/usr/bin/env python3

# NECCESARY IMPORTS
from unicodedata import name
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template


# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route("/admin/")
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route("/<username>")
def index(username):
    return render_template("info.html", name=username)


@app.route("/")
def glossary():
    # returns Books in JSON format
    return jsonify(books)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
