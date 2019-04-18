"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """user."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(50),
                    nullable=False,
                    unique=True)
    last_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    image_url = db.Column(db.String(),
                     nullable=False)

class Post(db.model):
    """Post"""

    __tablename__= "Post"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(50),
                    nullable=False,
                    unique=True)
    content = db.Column(db.String(),
                     nullable=False,
                     unique=True)
    created_at = db.Column(db.date(),
                     nullable=False,
                     )                
    user_id = db.Column(db.Integer,
                     db.Foreign_key("users.id"),
                     primary_key=True)