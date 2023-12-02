from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length,ValidationError




class PostForm(FlaskForm):
  title=StringField('Title',validators=[DataRequired(),Length(min=2,max=20)])
  content=TextAreaField('Content',validators=[DataRequired()])
  submit=SubmitField('Post')