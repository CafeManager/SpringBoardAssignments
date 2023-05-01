"""Blogly application."""

from flask import Flask, render_template, session, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-secr3t'
debug = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True




connect_db(app)


# redirects to list of users
@app.route("/")
def home_page():
    return render_template('user_profile.html')

# show a list of users
@app.route('/users')
def show_user_list():
    # add logic ot show users
    user_list = User.query.all()
    return render_template('user_list.html', users=user_list)

# show the user creation form
@app.route('/users/new')
def show_user_form():
    return render_template('user_create.html')

# create a new user then redirect
@app.route('/users/new', methods=['POST'])
def submit_user():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    image_url = request.form['image-url']
    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

# show a user profile
@app.route('/users/<id>')
def show_user(id):
    user = User.query.filter(User.id == id).all()[0]
    return render_template('/user_profile.html', user=user)

# show the edit form for a user
@app.route('/users/<id>/edit')
def show_edit_form(id):
    user = User.query.filter(User.id == id).all()[0]
    return render_template('/user_edit.html', user=user)

# update the user data then redirect to /users
@app.route('/users/<id>/edit', methods=['POST'])
def update_user(id):
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    image_url = request.form['image-url']
    user = User.query.filter(User.id == id).all()[0]
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

# delete the user
@app.route('/users/<id>/delete', methods=['POST'])
def delete_user(id):
    user = User.query.filter(User.id == id)
    user.delete()
    db.session.commit()
    return redirect('/users')