from http import server
from sre_constants import SUCCESS
from app import app
from flask import render_template, redirect, url_for, Flask
from datetime import datetime
import smtplib
import os

from app.forms import emailForm
from flask import request


app.config['SECRET_KEY'] = 'lets get it on'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    current_year = datetime.now().year
    age = int(current_year) - 1997
    return render_template("about.html", age=age)


@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    pw = os.environ.get("PASSWORD")
    us = os.environ.get("address")
    form = emailForm()
    if form.validate_on_submit():
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        total = name + " | " + email + " | " + message
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(us, pw)
        server.sendmail(us, us, total)
        
        return redirect("/")
    else:
        return render_template("contact.html", form=form)