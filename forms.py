from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email, password, submit
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    beer = StringField('Favorite Beer', validators = [DataRequired()])
    submit_button = SubmitField()