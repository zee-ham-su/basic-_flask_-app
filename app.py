#!/usr/bin/env python3
""" create a basic flask app """

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """ returns a simple message """
    return "Hello HBNB! this is the main page <h1>HELLO</h1>"

@app.route("/<name>", strict_slashes=False)
def user(name):
    return f"hello {name}!"

@app.route("/admin")
def admin():
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3000")