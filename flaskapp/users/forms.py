from flask_wtf import FlaskForm
from flaskapp.models import User
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError




class RegistrationForm(FlaskForm):
  name=StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
  email=StringField('Email',validators=[DataRequired(),Email()])
  password=PasswordField('Password',validators=[DataRequired()])
  password_confirm=PasswordField('Password confirm',validators=[DataRequired(),EqualTo('password')])
  
  submit=SubmitField('Sign Up')
  
  def validate_name(self,name):
    user=User.query.filter_by(name=name.data).first()
    if user:
      raise ValidationError('This is name of someone else,change the name')
  
  def validate_email(self,email):
    user=User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('This is eamil  of someone else,change the email')

class LoginForm(FlaskForm):
  email=StringField('Email',validators=[DataRequired(),Email()])
  password=PasswordField('Password',validators=[DataRequired()])
  remember_Me= BooleanField('Remember Me')
  submit=SubmitField('Login')
  

  
class UpdateForm(FlaskForm):
  name=StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
  email=StringField('Email',validators=[DataRequired(),Email()])
  picture=FileField('Update Profile',validators=[FileAllowed('jpg png pdf'.split())])
  
  submit=SubmitField('Update')
  
  def validate_name(self,name):
    if name.data != current_user.name:
      user=User.query.filter_by(name=name.data).first()
      if user:
        raise ValidationError('This is name of someone else,change the name')
  
  def validate_email(self,email):
    if email.data != current_user.email:
      user=User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError('This is eamil  of someone else,change the email')

class RequestPass(FlaskForm):
  email=StringField('Email',validators=[DataRequired(),Email()])
  submit=SubmitField('Request')
  def validate_email(self,email):
    user=User.query.filter_by(email=email.data).first()
    if user is None:
      raise ValidationError('There is no Account with that email😔🤕 please register')
        
class ResetPass(FlaskForm):
  password=PasswordField('Password',validators=[DataRequired()])
  password_confirm=PasswordField('Password confirm',validators=[DataRequired(),EqualTo('password')])
  
  submit=SubmitField('Reset')
 