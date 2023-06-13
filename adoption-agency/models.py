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

class Pet(db.Model):
    """Pet."""
    def __repr__(self):
        pet = self
        # return f'<User id={user.id} first_name={user.first_name} last_name={user.last_name} image_url={user.image_url}>'
    
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement=True)
    
    name = db.Column(db.Text,
                    required=True,
                    nullable=False)
    
    species = db.Column(db.String,
                        nullable=False) 
    
    photo_url = db.Column(db.String) 
    
    age = db.Column(db.Integer)

    notes = db.Column(db.String) 
    
    available = db.Column(db.Boolean,
                        default=True)
    
