from savorpages import db


class Category(db.Model):
    # schema for Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), unique=True, nullable=True)

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
