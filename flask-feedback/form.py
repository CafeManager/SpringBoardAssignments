from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length
class RegisterForm(FlaskForm):
    """Form for registering."""
    username = StringField('Username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Password')
    email = EmailField('Email', validators=[InputRequired(),  Length(max=50)])
    first_name = StringField('First Name', validators=[InputRequired(), Length(max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=30)])

class LoginForm(FlaskForm):
    """Form for logging in."""
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password')

class FeedbackForm(FlaskForm):
    """Form for creating Feedback"""
    title = StringField('Title', validators=[InputRequired(), Length(max=100)])
    content = StringField('Content', validators=[InputRequired()])