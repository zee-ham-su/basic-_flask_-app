#!/usr/bin/env python3
""" create a basic flask app """
from flask import Flask,redirect,url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "any random string"
app.permanent_session_lifetime = timedelta(minutes=5)


# Routes
@app.route('/', strict_slashes=False)
def home():
    """ returns a simple message """
    return render_template('index.html')


@app.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    """ login route """
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session["user"] = user
        return redirect(url_for("user", username=user))
    else:
        if "user" in session:
            return redirect(url_for("user", username=session["user"]))
        
        return render_template('login.html')


@app.route('/<username>', strict_slashes=False)
def user(username):
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for('login'))

@app.route('/logout', strict_slashes=False)
def logout():
    """ logout user route 
    """
    session.pop("user", None)
    flash("You have been logged out!", "info")
    return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="3000")