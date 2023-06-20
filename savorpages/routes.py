import os
from flask import flash, render_template, redirect, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import cloudinary
import cloudinary.uploader
import cloudinary.api
from savorpages import app, db
from savorpages.models import Category, Users, Recipe


cloudinary.config.update = ({
    'cloud_name': os.environ.get('cloud_name'),
    'api_key': os.environ.get('api_key'),
    'api_secret': os.environ.get('api_secret')
})


@app.route("/")
def home():
    # Renders home page
    return render_template("index.html")


@app.route("/recipes")
def recipes():
    #  Renders recipe page
    recipes = list(Recipe.query.order_by(Recipe.id).all())
    categories = list(Category.query.order_by(
                            Category.category_name).all())
    return render_template("recipes.html", recipes=recipes,
                           categories=categories)


# Manage categories from Code Institute walkthrough
# project's source code amended for my requirements
@app.route("/categories")
def categories():
    # Allows to manage categories only for admin user
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("login"))
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # Allows to manage categories only for admin user
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("home"))
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # Allows to manage categories only for admin user
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("home"))
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    # Allows to manage categories only for admin user
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage categories!")
        return redirect(url_for("home"))
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


# Manage recipes from Code Institute walkthrough
# project's source code amended for my requirements
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Allows only logged user to add a recipe
    if "user" not in session:
        flash("You need to be logged in to add a recipe")
        return redirect(url_for("login"))
    categories = list(Category.query.order_by(Category.category_name).all())

    if request.method == "POST":
        image = request.files["image_url"]
        image_upload = cloudinary.uploader.upload(image)
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_description=request.form.get("recipe_description"),
            ingredients=request.form.get("ingredients"),
            preparation=request.form.get("preparation"),
            cook_time=request.form.get("cook_time"),
            image_url=request.files["image_url"],
            created_by=session["user"],
            category_id=request.form.get("category_id")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("recipes"))
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    # Allows to edit only user's own recipe
    if "user" not in session or session["user"] != recipe.created_by:
        flash("You can edit only your own recipes!")
        return redirect(url_for("recipes"))
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name"),
        recipe.recipe_description = request.form.get("recipe_description"),
        recipe.ingredients = request.form.get("ingredients"),
        recipe.preparation = request.form.get("preparation"),
        recipe.cook_time = request.form.get("cook_time"),
        recipe.category_id = request.form.get("category_id")
        db.session.commit()
        flash("Recipe successfully updated!")
        return redirect(url_for("recipes"))
    return render_template("edit_recipe.html",
                           recipe=recipe, categories=categories)


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    # Allows to delete only user's own recipe
    if "user" not in session or session["user"] != recipe.created_by:
        flash("You can edit only your own recipes and must be logged in!")
        return redirect(url_for("recipes"))
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("recipes"))


# Register, login, log out and profile functionality from
# Code Institute combined database source code
# amended to my requirements
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
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Login functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("username").lower()).all()
        if existing_user:
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Hello again, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Display profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Check if user in session, and redorect to profile page
    if "user" in session:
        recipe_list = Recipe.query.filter_by(created_by=session["user"]).all()
        categories = list(Category.query.order_by(
                            Category.category_name).all())
        return render_template("profile.html", username=session["user"],
                               recipe_list=recipe_list, categories=categories)

    return redirect(url_for("login"))


#  Log out
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))
