"""Blogly application."""

from flask import Flask, render_template, session, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post
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
    return redirect('/users')

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
    posts = Post.query.filter(Post.user_fk == user.id).all()
    return render_template('/user_profile.html', user=user, posts=posts)

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

# past

# show the post creation form
@app.route('/users/<id>/posts/new')
def show_post_form(id):
    user = User.query.filter(User.id == id).all().pop()
    print(user)
    return render_template('user_create_post.html', user=user)

# submit the post to the database
@app.route('/users/<id>/posts/new', methods=['POST'])
def submit_post(id):
    title = request.form['title-textbox']
    content = request.form['content-textbox']
    user_fk = id
    new_post= Post(title=title, content=content, user_fk=user_fk)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{id}')

# show the post
@app.route('/posts/<id>')
def show_post(id):
    
    post = Post.query.filter(Post.id == id).all().pop()
    user = User.query.filter(User.id == post.user_fk).all().pop()
    print(user)
    return render_template('show_post.html', post=post, user=user)

# show the edit post form
@app.route('/posts/<id>/edit')
def show_edit_post_form(id):
    post = Post.query.filter(Post.id == id).all().pop()
    user = User.query.filter(User.id == post.user_fk).all().pop()
    return render_template('show_post_edit.html', user=user, post=post)

# process the post edit in the database
@app.route('/posts/<id>/edit', methods=['POST'])
def process_post_edit(id):
    title = request.form['title-textbox']
    content = request.form['content-textbox']
    post = Post.query.filter(Post.id == id).all().pop()
    post.title = title
    post.content = content
    db.session.add(post)
    db.session.commit()

    return redirect(f'/posts/{id}')

# delete post from database
@app.route('/posts/<id>/delete', methods=['POST'])
def delete_post(id):
    post = Post.query.filter(Post.id == id)
    post_item = post.all().pop()
    user_id = post_item.user_fk
    post.delete()
    db.session.commit()
    return redirect(f'/users/{user_id}')