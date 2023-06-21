"""Blogly application."""

from flask import Flask, render_template, session, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from flask_sqlalchemy import SQLAlchemy
from form import AddPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-secr3t'
debug = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# render pets
@app.route("/")
def home_page():
    pets = Pet.query.filter(Pet.available == True).all()
    return render_template('show_homepage.html', pets=pets, pet_length=len(pets))

#adds a pet to the database or renders a form to add a pet
@app.route("/add", methods=["GET", "POST"])
def add_form():
    form = AddPetForm()
    print("1")
    if form.validate_on_submit():
        name = form.name.data
        species = form.name.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        if(photo_url):
            new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        else:
            new_pet = Pet(name=name, species=species, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()
        
        return redirect("/")
    else:
        return render_template("show_pet_add_form.html", form=form)

# display and edit a pet
@app.route("/pet/<id>", methods=["GET", "POST"])
def display_pet(id):
    print(id)
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.name.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        
        return redirect("/")
    else:
        return render_template("show_pet_edit_form.html", form=form, pet=pet)