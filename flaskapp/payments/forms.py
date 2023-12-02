from flask_wtf import FlaskForm
from flaskapp.models import User
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError


class PaymentForm(FlaskForm):
    Tigo=SubmitField('Tigopesa')
    
    entry=StringField('Phone number',validators=[DataRequired(),Length(min=13,max=13)])
    recipient=StringField('recipient Phone number',validators=[DataRequired(),Length(min=13,max=13)])
    Pin=PasswordField('EnteryourPIN',validators=[DataRequired(),Length(min=4,max=4)])
    pay=SubmitField('Pay')
    
    
    
    Voda=SubmitField('Mpesa')
    Azam=SubmitField('Azam-pesa')
    Airtel=SubmitField('Airtel-Money')
    TTCL=SubmitField('T-pesa')
    
    
    picture=FileField('Upload Screenshort of Your Payment(s)',validators=[FileAllowed('jpg png'.split())])
    
    upload = SubmitField('Upload')