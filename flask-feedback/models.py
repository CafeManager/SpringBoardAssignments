"""Models for Feedback app."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()


class User(db.Model):

    def __repr__(self):
        user = self
        return f"<User id={user.id} username={user.username} password={user.password} email={user.email} first_name={user.first_name} last_name={user.last_name}>"

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True)
    
    username = db.Column(db.String(20), 
                    nullable=False, 
                    unique=True)
    
    password = db.Column(db.Text, 
                    nullable=False)

    email = db.Column(db.String(50), 
                    nullable=False)

    first_name = db.Column(db.String(30), 
                    nullable=False)

    last_name = db.Column(db.String(30), 
                    nullable=False)
    
    feedbacks = db.relationship('Feedback', backref="user", cascade='delete, merge, save-update')
    
    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode('utf8')
        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)

    @classmethod
    def authenticate(cls, username, pwd):
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, pwd):
            return user
        else:
            return False

class Feedback(db.Model):
    
    def __repr__(self):
        feedback = self
        return f"<Feedback id={feedback.id} title={feedback.title} content={feedback.content} username={feedback.username}>"

    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, 
            primary_key=True,
            autoincrement=True,
            unique=True)
    
    title =  db.Column(db.String(100), 
                nullable=False)

    content = db.Column(db.Text, 
                nullable=False)

    username = db.Column(db.String(20), 
                db.ForeignKey('users.username', ondelete='CASCADE'),
                nullable=False)
    