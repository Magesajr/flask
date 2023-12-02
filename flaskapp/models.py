from datetime import datetime
from flask import current_app
from flaskapp import db,login_manager
from flask_login import UserMixin
from itsdangerous.url_safe import URLSafeTimedSerializer as serial
import json

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
  


class User(db.Model,UserMixin):
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(20),unique=True,nullable=False)
  email= db.Column(db.String(120),unique=True,nullable=False)
  image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
  password= db.Column(db.String(60),nullable=False)
  posts=db.relationship('Post',backref='Author',lazy=True)
  
  def get_reset_token(self,salt='reset'):
    s=serial(current_app.config['SECRET_KEY'],salt=salt)
    sam=s.dumps({'user_id':self.id})
    return  sam
    
  
    
  @staticmethod  
  def verify_reset_token(token,salt='reset'):
    s=serial(current_app.config['SECRET_KEY'])
    try: 
      user_id=s.loads(token,100,salt=salt)['user_id']
    except:
      return None
    return User.query.get(user_id)
    
    
  def __repr__(self):
      return f"User('{self.name}','{self.email}', '{self.image_file}')"
    
  
class Post(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  title= db.Column(db.String(100),nullable=False)
  date= db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
  content=db.Column(db.Text,nullable=False)
  user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
      
  def __repr__(self):
        return f"Post('{self.title}','{self.date}')"
    

class Payment(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  title= db.Column(db.String(100),nullable=False)
  date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
  content=db.Column(db.Text,nullable=False)
  user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
      
  def __repr__(self):
        return f"PayMent('{self.title}','{self.date}')"
        
  def get_pay_token(self,salt='payment'):
    p=serial(current_app.config['PAYMENT_KEY'],salt=salt)
    pay=p.dumps({'user_id':self.id})
    return pay
   
  @staticmethod 
  def verify_pay_token(token,salt='payment'):
    p=serial(current_app.config['PAYMENT_KEY'])
    try:
      Paytoken=p.loads(token,1800,salt=salt)['user_id']
    except:
      return None
    return User.query.get(Paytoken)
    
  
