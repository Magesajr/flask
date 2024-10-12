from flask_wtf import FlaskForm
from flaskapp.models import User
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
import os

folder='flaskapp/main'
choices=[(f,f) for f in os.listdir(folder)]
class DownloadForm(FlaskForm):
  file=SelectField('check your File to download',validators=[DataRequired()],choices=choices)
  submit=SubmitField('download')
