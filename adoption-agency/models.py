from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""
    def __repr__(self):
        pet = self
        return f'<Pet id={pet.id} name={pet.name} species={pet.species} photo_url={pet.photo_url} age={pet.age} notes={pet.notes} available={pet.available}>'
    
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement=True)
    
    name = db.Column(db.String,
                    nullable=False)
    
    species = db.Column(db.String,
                        nullable=False) 
    
    photo_url = db.Column(db.String,
                          default='https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png') 
    
    age = db.Column(db.Integer)

    notes = db.Column(db.Text) 
    
    available = db.Column(db.Boolean,
                        default=True)
    
