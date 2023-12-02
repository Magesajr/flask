import os
class Config:
  SECRET_KEY=os.environ.get('SECRET_KEY')
  PAYMENT_KEY=os.environ.get('PAYMENT_KEY')
  SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
  MAIL_SERVER='smtp.gmail.com'
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USE_SSL=False
  MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
  