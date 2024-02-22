#!/usr/bin/env python3
""" create a basic flask app """
from flask import Flask,redirect,url_for, render_template, request


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """ returns a simple message """
    return render_template('index.html')

@app.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    """ returns a simple message """
    if request.method == 'POST':
        user_name = request.form['nm']
        return redirect(url_for('user', usr=user_name))
    else:
        return render_template('login.html')


@app.route('/<usr>', strict_slashes=False) 
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/admin')
def admin():
    return redirect(url_for('home'))





if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="3000")