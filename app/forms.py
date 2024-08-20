from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first
    #     if user:
    #         raise ValidationError('Username already taken.')
        
    # def validate_email(self, email):
    #     email = User.query.filter_by(email=email.data).first
    #     if email:
    #         raise ValidationError('Email already in use.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Picture', validators=[FileAllowed(['png', 'jpeg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first
            if user:
                raise ValidationError('Username already taken.')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first
            if email:
                raise ValidationError('Email already in use.')


class PostForm(FlaskForm):
    title = StringField('Position', validators=[DataRequired()])
    content = TextAreaField('Job Description', validators=[DataRequired()])
    submit = SubmitField('Post')