import os
class Config:
  SECRET_KEY='testing'
  PAYMENT_KEY=os.environ.get('PAYMENT_KEY')
  SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
  MAIL_SERVER='smtp.gmail.com'
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USE_SSL=False
  MAIL_USERNAME='sam263708@gmail.com'
  MAIL_PASSWORD='ruvzegcwpphdpnug'
  
