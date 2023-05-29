from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from savorpages import app, db
from savorpages.models import Category, Users


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("username").lower()).all()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Congratulation! You are a member now!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")
