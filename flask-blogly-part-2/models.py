from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Blogly."""
# First, create a User model for SQLAlchemy. Put this in a models.py file.

# It should have the following columns:

# id, an autoincrementing integer number that is the primary key
# first_name and last_name
# image_url for profile images
# Make good choices about whether things should be required, have defaults, and so on.

class User(db.Model):
    """User."""
    def __repr__(self):
        user = self
        return f'<User id={user.id} first_name={user.first_name} last_name={user.last_name} image_url={user.image_url}>'
    
    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(25),
                   nullable=False)
    
    last_name = db.Column(db.String(25),
                   nullable=False)
    
    image_url = db.Column(db.String(100),
                   default='https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png')
    
class Post(db.Model):
    "Post."
    def __repr__(self):
        p = self
        return f"<Post id={p.id} title={p.title} content={p.content} created_at={p.created_at} user_fk"
    
    __tablename__ = "posts"

    id = db.Column(db.Integer, 
                    primary_key = True, 
                    autoincrement=True)

    title = db.Column(db.Text, 
                      nullable=False)

    content = db.Column(db.Text, 
                        nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now())
    user_fk = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_id = db.relationship('User')