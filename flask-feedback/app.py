"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, User, db, Feedback
from form import RegisterForm, LoginForm, FeedbackForm


app = Flask(__name__)
app.config["SECRET_KEY"] = 'do-not-share32'
debug = DebugToolbarExtension(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///feedback'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)

@app.route('/')
def redirect_to_register():
    if 'username' in session:
        return redirect(f"/users/{session['username']}")
    return redirect('/register')


@app.route('/register', methods=['GET', 'POST'])
def get_register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User.register(name, pwd, email, first_name, last_name)
        db.session.add(user)
        db.session.commit()

        session['username'] = user.username
        return redirect('/secret')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def get_login_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            session['username'] = user.username
            return redirect('/secret')
        else:
            form.username.errors = ["Bad username/password"]
    return render_template('login.html', form=form)

@app.route('/secret')
def show_secret():
    if 'username' not in session:
        return redirect('/')
    else:
        return render_template("secret.html")

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/")

@app.route('/users/<name>')
def get_user_data(name):

    if session['username'] == name:
        user = User.query.filter(User.username == name).first()
        return render_template('user_data.html', user=user)
    else:
        flash("You're not allowed to see that!", "error")
        return redirect('/')
    
@app.route('/users/<name>/feedback/add', methods=['GET', 'POST'])
def get_feedback_form(name):
    form = FeedbackForm()
    if session['username'] == name:
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            feedback = Feedback(title=title, content=content, username=name)
            db.session.add(feedback)
            db.session.commit()
            return redirect(f'/users/{name}')
        else:
            return render_template('feedback_add_form.html', form=form)
    else:
        flash("You're not allowed to see that!", "error")
        return redirect('/')

@app.route('/feedback/<id>/delete', methods=['POST'])
def delete_feedback(id):
    print(session['username'])
    
    feedback = Feedback.query.filter(Feedback.id == id).first()
    if feedback.user.username == session['username']:
        db.session.delete(feedback)
        db.session.commit()
        return (jsonify(message="deleted"), 200)
    return (jsonify(message="You do not have permissions for this"), 400)

@app.route('/users/<name>/delete', methods=["POST"])
def delete_user(name):
    if session['username'] == name:
        user = User.query.filter(User.username == name).first()
        db.session.delete(user)
        db.session.commit()
        session.pop("username")
        return redirect('/')
    else:
        flash("You do not have permissions for this", "error")
        return redirect('/')

@app.route('/feedback/<id>/update', methods=["POST", "GET"])
def get_feedback_update(id):
    feedback = Feedback.query.get_or_404(id)
    form = FeedbackForm(obj=feedback)
    if session['username'] == feedback.user.username:
        if form.validate_on_submit():
            feedback.title = form.title.data
            feedback.content = form.content.data
            db.session.add(feedback)
            db.session.commit()
            return redirect(f'/users/{feedback.username}')
        else:
            return render_template('feedback_update_form.html', form=form)
    else:
        flash("You're not allowed to see that!", "error")
        return redirect('/')
    



