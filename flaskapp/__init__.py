from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flaskapp.config import  Config
from flask_bootstrap import Bootstrap5


db = SQLAlchemy()
bootstrap=Bootstrap5()
login_manager=LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'
mail=Mail()

def create_app(config_class=Config):
  app=Flask(__name__)
  app.config.from_object(Config)
  db.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)
  bootstrap.init_app(app)
  
  from flaskapp.users.route import users
  from flaskapp.posts.route import posts
  from flaskapp.main.route import main
  from flaskapp.errors.errors_handlers import errors
  from flaskapp.payments.users_payments import pays 
  
  
  app.register_blueprint(users)
  app.register_blueprint(posts)
  app.register_blueprint(main)
  app.register_blueprint(errors)
  app.register_blueprint(pays)
  
  return app

  

