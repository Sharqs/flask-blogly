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

class Post(db.Model):
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
    created_at = db.Column(db.String(),
                     nullable=False,
                     )                
    user_id = db.Column(db.Integer,
                     db.ForeignKey("users.id"))

class Tag(db.Model):
    """Tag"""

    __tablename__= "Tag"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(),
                    nullable=False,
                    unique=True)

    post = db.relationship("Post",
                            secondary='Post_Tag',
                            backref="Tag")
    
class PostTag(db.Model):
    """Mapping post to tag"""

    __tablename__= "Post_Tag"

    post_id = db.Column(db.Integer,
                        db.ForeignKey("post.id", ondelete="CASCADE")
                        primary_key=True)
    tag_id = db.Column(db.Integer,
                        ForeignKey("tag.id", ondelete="CASCADE"),
                        nullable=False,
                        primary_key=True)
