#!/usr/bin/env python3
""" create a basic flask app """

from flask import Flask,redirect,url_for, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """ returns a simple message """
    return render_template('index.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3000")