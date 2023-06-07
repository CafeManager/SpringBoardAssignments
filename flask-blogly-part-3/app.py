"""Blogly application."""

from flask import Flask, render_template, session, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag
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
    tags = Tag.query.all()
    print(user)
    return render_template('user_create_post.html', user=user, tags=tags)

# submit the post to the database
@app.route('/users/<id>/posts/new', methods=['POST'])
def submit_post(id):
    title = request.form['title-textbox']
    content = request.form['content-textbox']
    user_fk = id
    tag_list = Tag.query.all()
    new_post= Post(title=title, content=content, user_fk=user_fk)
    for tag in tag_list:
        if request.form.get(f'{tag.id}'):
            new_post.tags.append(tag)

    print("here")
    print(new_post.tags)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{id}')

# show the post
@app.route('/posts/<id>')
def show_post(id):
    
    post = Post.query.filter(Post.id == id).all().pop()
    user = User.query.filter(User.id == post.user_fk).all().pop()
    print(user)
    return render_template('show_post.html', post=post, user=user, tags=post.tags)

# show the edit post form
@app.route('/posts/<id>/edit')
def show_edit_post_form(id):
    post = Post.query.filter(Post.id == id).all().pop()
    user = User.query.filter(User.id == post.user_fk).all().pop()
    tag_list = Tag.query.all()
    return render_template('show_post_edit.html', user=user, post=post, tags=tag_list, post_tags=post.tags)

# process the post edit in the database
@app.route('/posts/<id>/edit', methods=['POST'])
def process_post_edit(id):
    title = request.form['title-textbox']
    content = request.form['content-textbox']
    post = Post.query.filter(Post.id == id).all().pop()
    post.title = title
    post.content = content
    post.tags = []
    tag_list = Tag.query.all()
    for tag in tag_list:
        if request.form.get(f'{tag.id}'):
            post.tags.append(tag)

    db.session.add(post)
    db.session.commit()

    return redirect(f'/posts/{id}')

# delete post from database
@app.route('/posts/<id>/delete', methods=['POST'])
def delete_post(id):
    post = Post.query.filter(Post.id == id)
    post_item = post.all().pop()
    user_id = post_item.user_fk
    db.session.delete(post_item)
    db.session.commit()
    return redirect(f'/users/{user_id}')

# start blog 3
@app.route('/tags')
def get_tag_list():
    tag_list = Tag.query.all()
    return render_template('show_tag_list.html', tags=tag_list)

@app.route('/tags/<id>')
def get_tag_details(id):
    tag = Tag.query.filter(Tag.id == id).all().pop()
    posts = tag.posts
    # posts = Post.query.filter()
    return render_template('show_tag.html', tag=tag, posts=posts)

@app.route('/tags/new')
def get_tag_create_form():
    return render_template('show_tag_create.html')

@app.route('/tags/new', methods=['POST'])
def process_tag_create_form():
    tag_name = request.form['tag-textbox']
    tag = Tag(name=tag_name)
    db.session.add(tag)
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<id>/edit')
def show_edit_tag_form(id):
    tag = Tag.query.filter(Tag.id == id).all().pop()
    return render_template('show_tag_edit.html', tag=tag)

@app.route('/tags/<id>/edit', methods=['POST'])
def process_tag_edit_form(id):
    tag = Tag.query.filter(Tag.id == id).all().pop()
    new_name = request.form['tag-name']
    tag.name = new_name
    db.session.add(tag)
    db.session.commit()
    return redirect(f'/tags/{tag.id}/edit')


@app.route('/tags/<id>/delete')
def process_tag_delete(id):
    tag = Tag.query.filter(Tag.id == id).all().pop()
    db.session.delete(tag)
    db.session.commit()
    return redirect('/tags')