"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)

class user(db.Model):
    """user."""

    __tablename__ = "user"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(50),
                    nullable=False,
                    unique=True)
    last_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    image_url = db.Column(db.String(50),
                     nullable=False)
