from savorpages import db


class Category(db.Model):
    # schema for Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), unique=True, nullable=True)
    recipes = db.relationship("Recipe", backref="category",
                              cascade="all,delete", lazy=True)

    def __rep__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Users(db.Model):
    # schema for recipe model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __rep__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name


class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('recipes', lazy=True))
    recipe_description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    preparation = db.Column(db.Text, nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id",
                            ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Recipe: {1}".format(
            self.id, self.recipe_name
        )
