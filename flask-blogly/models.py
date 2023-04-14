from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///'

db = SQLAlchemy()


app.config['SQLALCHEMY_DATABASE_URI'] = ''
def connect_db(app):
    db.app = app
    db.init_app()

"""Models for Blogly."""
# First, create a User model for SQLAlchemy. Put this in a models.py file.

# It should have the following columns:

# id, an autoincrementing integer number that is the primary key
# first_name and last_name
# image_url for profile images
# Make good choices about whether things should be required, have defaults, and so on.

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement=True)