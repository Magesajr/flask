import os
class Config:
  SECRET_KEY='testing'
  PAYMENT_KEY=os.environ.get('PAYMENT_KEY')
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE')
  MAIL_SERVER='smtp.gmail.com'
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USE_SSL=False
  MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
  #MAIL_PASSWORD='ruvzegcwpphdpnug'
  
