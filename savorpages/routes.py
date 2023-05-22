from flask import render_template
from savorpages import app, db
from savorpages.models import Category, Users


@app.route("/")
def home():
    return render_template("base.html")
